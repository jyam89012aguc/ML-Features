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


# 21d acceleration of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accel_21d_3d_v001_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accel_63d_3d_v002_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accel_126d_3d_v003_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accel_252d_3d_v004_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accel_21d_3d_v005_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accel_63d_3d_v006_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accel_126d_3d_v007_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accel_252d_3d_v008_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accel_21d_3d_v009_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accel_63d_3d_v010_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accel_126d_3d_v011_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accel_252d_3d_v012_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accel_21d_3d_v013_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accel_63d_3d_v014_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accel_126d_3d_v015_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accel_252d_3d_v016_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accel_21d_3d_v017_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accel_63d_3d_v018_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accel_126d_3d_v019_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accel_252d_3d_v020_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accel_21d_3d_v021_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accel_63d_3d_v022_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accel_126d_3d_v023_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accel_252d_3d_v024_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accel_21d_3d_v025_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accel_63d_3d_v026_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accel_126d_3d_v027_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accel_252d_3d_v028_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slopez_21d_z126_3d_v029_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slopez_63d_z252_3d_v030_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slopez_126d_z252_3d_v031_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_slopez_252d_z504_3d_v032_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slopez_21d_z126_3d_v033_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slopez_63d_z252_3d_v034_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slopez_126d_z252_3d_v035_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_slopez_252d_z504_3d_v036_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slopez_21d_z126_3d_v037_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slopez_63d_z252_3d_v038_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slopez_126d_z252_3d_v039_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_slopez_252d_z504_3d_v040_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slopez_21d_z126_3d_v041_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slopez_63d_z252_3d_v042_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slopez_126d_z252_3d_v043_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_slopez_252d_z504_3d_v044_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slopez_21d_z126_3d_v045_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slopez_63d_z252_3d_v046_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slopez_126d_z252_3d_v047_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_slopez_252d_z504_3d_v048_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slopez_21d_z126_3d_v049_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slopez_63d_z252_3d_v050_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slopez_126d_z252_3d_v051_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_slopez_252d_z504_3d_v052_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slopez_21d_z126_3d_v053_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slopez_63d_z252_3d_v054_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slopez_126d_z252_3d_v055_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_slopez_252d_z504_3d_v056_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_jerk_21d_3d_v057_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_jerk_63d_3d_v058_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_jerk_126d_3d_v059_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_jerk_21d_3d_v060_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_jerk_63d_3d_v061_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_jerk_126d_3d_v062_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_jerk_21d_3d_v063_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_jerk_63d_3d_v064_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_jerk_126d_3d_v065_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_jerk_21d_3d_v066_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_jerk_63d_3d_v067_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_jerk_126d_3d_v068_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_jerk_21d_3d_v069_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_jerk_63d_3d_v070_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_jerk_126d_3d_v071_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_jerk_21d_3d_v072_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_jerk_63d_3d_v073_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_jerk_126d_3d_v074_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_jerk_21d_3d_v075_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_jerk_63d_3d_v076_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_jerk_126d_3d_v077_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_to_netcash smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_smoothaccel_63d_sm252_3d_v078_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_to_netcash smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_smoothaccel_252d_sm504_3d_v079_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_to_cash smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_smoothaccel_63d_sm252_3d_v080_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_to_cash smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_smoothaccel_252d_sm504_3d_v081_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_to_liqpool smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_smoothaccel_63d_sm252_3d_v082_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_to_liqpool smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_smoothaccel_252d_sm504_3d_v083_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netcash_to_mcap smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_smoothaccel_63d_sm252_3d_v084_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netcash_to_mcap smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_smoothaccel_252d_sm504_3d_v085_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_neg_box smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_smoothaccel_63d_sm252_3d_v086_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_neg_box smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_smoothaccel_252d_sm504_3d_v087_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_below_cash smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_smoothaccel_63d_sm252_3d_v088_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_below_cash smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_smoothaccel_252d_sm504_3d_v089_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_minus_cash smoothed over 252d
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_smoothaccel_63d_sm252_3d_v090_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_minus_cash smoothed over 504d
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_smoothaccel_252d_sm504_3d_v091_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accelz_21d_z252_3d_v092_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_accelz_63d_z504_3d_v093_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accelz_21d_z252_3d_v094_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_accelz_63d_z504_3d_v095_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accelz_21d_z252_3d_v096_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_accelz_63d_z504_3d_v097_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accelz_21d_z252_3d_v098_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_accelz_63d_z504_3d_v099_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accelz_21d_z252_3d_v100_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_accelz_63d_z504_3d_v101_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accelz_21d_z252_3d_v102_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_accelz_63d_z504_3d_v103_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accelz_21d_z252_3d_v104_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_minus_cash
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_accelz_63d_z504_3d_v105_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_to_netcash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_signflip_63d_3d_v106_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_to_netcash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_signflip_252d_3d_v107_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_to_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_signflip_63d_3d_v108_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_to_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_signflip_252d_3d_v109_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_to_liqpool (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_signflip_63d_3d_v110_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_to_liqpool (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_signflip_252d_3d_v111_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netcash_to_mcap (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_signflip_63d_3d_v112_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netcash_to_mcap (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_signflip_252d_3d_v113_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_neg_box (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_signflip_63d_3d_v114_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_neg_box (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_signflip_252d_3d_v115_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_below_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_signflip_63d_3d_v116_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_below_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_signflip_252d_3d_v117_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_minus_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_signflip_63d_3d_v118_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_minus_cash (raw count, no price scaling)
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_signflip_252d_3d_v119_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_netcash normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rngaccel_63d_r252_3d_v120_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_netcash normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_rngaccel_252d_r504_3d_v121_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_cash normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rngaccel_63d_r252_3d_v122_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_cash normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_rngaccel_252d_r504_3d_v123_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_liqpool normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_rngaccel_63d_r252_3d_v124_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_liqpool normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_rngaccel_252d_r504_3d_v125_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netcash_to_mcap normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_rngaccel_63d_r252_3d_v126_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netcash_to_mcap normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_rngaccel_252d_r504_3d_v127_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_neg_box normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_rngaccel_63d_r252_3d_v128_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_neg_box normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_rngaccel_252d_r504_3d_v129_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_below_cash normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_rngaccel_63d_r252_3d_v130_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_below_cash normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_rngaccel_252d_r504_3d_v131_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_minus_cash normalized by 252d range
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_rngaccel_63d_r252_3d_v132_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_minus_cash normalized by 504d range
def f072cav_f072_cash_adjusted_valuation_mcap_minus_cash_rngaccel_252d_r504_3d_v133_signal(marketcap, cashneq, closeadj):
    base = marketcap - cashneq
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_cumslope_21d_3d_v134_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_cumslope_63d_3d_v135_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of mcap_to_netcash
def f072cav_f072_cash_adjusted_valuation_mcap_to_netcash_cumslope_252d_3d_v136_signal(marketcap, cashneq, investmentsc, debt, closeadj):
    base = _f072_mcap_to_netcash(marketcap, cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_cumslope_21d_3d_v137_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_cumslope_63d_3d_v138_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_to_cash
def f072cav_f072_cash_adjusted_valuation_ev_to_cash_cumslope_252d_3d_v139_signal(ev, cashneq, closeadj):
    base = ev / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_cumslope_21d_3d_v140_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_cumslope_63d_3d_v141_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_to_liqpool
def f072cav_f072_cash_adjusted_valuation_ev_to_liqpool_cumslope_252d_3d_v142_signal(ev, cashneq, investmentsc, closeadj):
    base = ev / (cashneq.fillna(0) + investmentsc.fillna(0)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_cumslope_21d_3d_v143_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_cumslope_63d_3d_v144_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netcash_to_mcap
def f072cav_f072_cash_adjusted_valuation_netcash_to_mcap_cumslope_252d_3d_v145_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = (cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_cumslope_21d_3d_v146_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_cumslope_63d_3d_v147_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_neg_box
def f072cav_f072_cash_adjusted_valuation_ev_neg_box_cumslope_252d_3d_v148_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_cumslope_21d_3d_v149_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_below_cash
def f072cav_f072_cash_adjusted_valuation_ev_below_cash_cumslope_63d_3d_v150_signal(ev, cashneq, closeadj):
    base = ((ev - cashneq) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

