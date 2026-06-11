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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f81_daily(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f81_evs(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f81_cx_int(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f81_phase(capex, w):
    m = capex.rolling(w, min_periods=max(2, w // 2)).mean()
    return capex - m


# 21d slope of EV/Sales level vs 21d mean
def f81es_f81_semi_ev_sales_cycle_level_21d_slope_v001_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _mean(_f81_evs(e, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_z_21d_slope_v002_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of drawdown of EV/Sales
def f81es_f81_semi_ev_sales_cycle_dd_21d_slope_v003_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _max(_f81_evs(e, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of run-up of EV/Sales
def f81es_f81_semi_ev_sales_cycle_up_21d_slope_v004_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _min(_f81_evs(e, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_vol_21d_slope_v005_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _std(_f81_evs(e, rv), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of log-dev of EV/Sales from 21d mean
def f81es_f81_semi_ev_sales_cycle_logdev_21d_slope_v006_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (np.log(_f81_evs(e, rv).replace(0, np.nan).abs()) - _mean(np.log(_f81_evs(e, rv).replace(0, np.nan).abs()), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex intensity level vs 21d mean
def f81es_f81_semi_ev_sales_cycle_cxi_21d_slope_v007_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _mean(_f81_cx_int(cx, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxiz_21d_slope_v008_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_cx_int(cx, rv), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex phase 21d
def f81es_f81_semi_ev_sales_cycle_phase_21d_slope_v009_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_composite_21d_slope_v010_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_z(_f81_evs(e, rv), 21) - _z(_f81_cx_int(cx, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales up- minus down-phase mean
def f81es_f81_semi_ev_sales_cycle_phasespread_21d_slope_v011_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv).where(_f81_phase(cx, 21) > 0), 21) - _mean(_f81_evs(e, rv).where(_f81_phase(cx, 21) < 0), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_cxicorr_21d_slope_v012_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).rolling(21, min_periods=max(2, 21//2)).corr(_f81_cx_int(cx, rv))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of log-dev EV/Sales from 21d EMA
def f81es_f81_semi_ev_sales_cycle_ltdev_21d_slope_v013_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_evs(e, rv).ewm(span=21, adjust=False).mean().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of range of EV/Sales
def f81es_f81_semi_ev_sales_cycle_rng_21d_slope_v014_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_max(_f81_evs(e, rv), 21) - _min(_f81_evs(e, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex intensity drawdown
def f81es_f81_semi_ev_sales_cycle_cxidd_21d_slope_v015_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _max(_f81_cx_int(cx, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex intensity run-up
def f81es_f81_semi_ev_sales_cycle_cxiup_21d_slope_v016_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratio_21d_slope_v017_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of log-ratio EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_logratio_21d_slope_v018_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_cx_int(cx, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales EMA crossover (21 vs 21*2)
def f81es_f81_semi_ev_sales_cycle_emax_21d_slope_v019_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv).ewm(span=21, adjust=False).mean() - _f81_evs(e, rv).ewm(span=21*2, adjust=False).mean())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex pct_change(21)
def f81es_f81_semi_ev_sales_cycle_cxgrowth_21d_slope_v020_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = cx.pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of revenue pct_change(21)
def f81es_f81_semi_ev_sales_cycle_rvgrowth_21d_slope_v021_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = rv.pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV pct_change(21)
def f81es_f81_semi_ev_sales_cycle_evgrowth_21d_slope_v022_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = e.pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales pct_change(21)
def f81es_f81_semi_ev_sales_cycle_evschg_21d_slope_v023_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of rolling corr capex phase vs EV/Sales
def f81es_f81_semi_ev_sales_cycle_cxiphasecorr_21d_slope_v024_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 21).rolling(21, min_periods=max(2, 21//2)).corr(_f81_evs(e, rv))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales position in range
def f81es_f81_semi_ev_sales_cycle_pos_21d_slope_v025_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 21)) / (_max(_f81_evs(e, rv), 21) - _min(_f81_evs(e, rv), 21)).replace(0, np.nan))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_posdev_21d_slope_v026_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 21)) / (_max(_f81_evs(e, rv), 21) - _min(_f81_evs(e, rv), 21)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of capex intensity position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_cxiposdev_21d_slope_v027_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 21)) / (_max(_f81_cx_int(cx, rv), 21) - _min(_f81_cx_int(cx, rv), 21)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of log EV/Sales
def f81es_f81_semi_ev_sales_cycle_logevs_21d_slope_v028_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of z-score EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratioz_21d_slope_v029_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d slope of EV/Sales mean rel to 21d-mean of mean
def f81es_f81_semi_ev_sales_cycle_evsmeansdev_21d_slope_v030_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv), 21) - _mean(_mean(_f81_evs(e, rv), 21), 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales level vs 63d mean
def f81es_f81_semi_ev_sales_cycle_level_63d_slope_v031_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _mean(_f81_evs(e, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_z_63d_slope_v032_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of drawdown of EV/Sales
def f81es_f81_semi_ev_sales_cycle_dd_63d_slope_v033_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _max(_f81_evs(e, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of run-up of EV/Sales
def f81es_f81_semi_ev_sales_cycle_up_63d_slope_v034_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _min(_f81_evs(e, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_vol_63d_slope_v035_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _std(_f81_evs(e, rv), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of log-dev of EV/Sales from 63d mean
def f81es_f81_semi_ev_sales_cycle_logdev_63d_slope_v036_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (np.log(_f81_evs(e, rv).replace(0, np.nan).abs()) - _mean(np.log(_f81_evs(e, rv).replace(0, np.nan).abs()), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex intensity level vs 63d mean
def f81es_f81_semi_ev_sales_cycle_cxi_63d_slope_v037_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _mean(_f81_cx_int(cx, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxiz_63d_slope_v038_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_cx_int(cx, rv), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex phase 63d
def f81es_f81_semi_ev_sales_cycle_phase_63d_slope_v039_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_composite_63d_slope_v040_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_z(_f81_evs(e, rv), 63) - _z(_f81_cx_int(cx, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales up- minus down-phase mean
def f81es_f81_semi_ev_sales_cycle_phasespread_63d_slope_v041_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv).where(_f81_phase(cx, 63) > 0), 63) - _mean(_f81_evs(e, rv).where(_f81_phase(cx, 63) < 0), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_cxicorr_63d_slope_v042_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).rolling(63, min_periods=max(2, 63//2)).corr(_f81_cx_int(cx, rv))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of log-dev EV/Sales from 63d EMA
def f81es_f81_semi_ev_sales_cycle_ltdev_63d_slope_v043_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_evs(e, rv).ewm(span=63, adjust=False).mean().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of range of EV/Sales
def f81es_f81_semi_ev_sales_cycle_rng_63d_slope_v044_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_max(_f81_evs(e, rv), 63) - _min(_f81_evs(e, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex intensity drawdown
def f81es_f81_semi_ev_sales_cycle_cxidd_63d_slope_v045_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _max(_f81_cx_int(cx, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex intensity run-up
def f81es_f81_semi_ev_sales_cycle_cxiup_63d_slope_v046_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratio_63d_slope_v047_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of log-ratio EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_logratio_63d_slope_v048_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_cx_int(cx, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales EMA crossover (63 vs 63*2)
def f81es_f81_semi_ev_sales_cycle_emax_63d_slope_v049_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv).ewm(span=63, adjust=False).mean() - _f81_evs(e, rv).ewm(span=63*2, adjust=False).mean())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex pct_change(63)
def f81es_f81_semi_ev_sales_cycle_cxgrowth_63d_slope_v050_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = cx.pct_change(periods=63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of revenue pct_change(63)
def f81es_f81_semi_ev_sales_cycle_rvgrowth_63d_slope_v051_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = rv.pct_change(periods=63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV pct_change(63)
def f81es_f81_semi_ev_sales_cycle_evgrowth_63d_slope_v052_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = e.pct_change(periods=63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales pct_change(63)
def f81es_f81_semi_ev_sales_cycle_evschg_63d_slope_v053_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).pct_change(periods=63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of rolling corr capex phase vs EV/Sales
def f81es_f81_semi_ev_sales_cycle_cxiphasecorr_63d_slope_v054_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 63).rolling(63, min_periods=max(2, 63//2)).corr(_f81_evs(e, rv))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales position in range
def f81es_f81_semi_ev_sales_cycle_pos_63d_slope_v055_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 63)) / (_max(_f81_evs(e, rv), 63) - _min(_f81_evs(e, rv), 63)).replace(0, np.nan))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_posdev_63d_slope_v056_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 63)) / (_max(_f81_evs(e, rv), 63) - _min(_f81_evs(e, rv), 63)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of capex intensity position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_cxiposdev_63d_slope_v057_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 63)) / (_max(_f81_cx_int(cx, rv), 63) - _min(_f81_cx_int(cx, rv), 63)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of log EV/Sales
def f81es_f81_semi_ev_sales_cycle_logevs_63d_slope_v058_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of z-score EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratioz_63d_slope_v059_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d slope of EV/Sales mean rel to 63d-mean of mean
def f81es_f81_semi_ev_sales_cycle_evsmeansdev_63d_slope_v060_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv), 63) - _mean(_mean(_f81_evs(e, rv), 63), 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales level vs 126d mean
def f81es_f81_semi_ev_sales_cycle_level_126d_slope_v061_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _mean(_f81_evs(e, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_z_126d_slope_v062_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of drawdown of EV/Sales
def f81es_f81_semi_ev_sales_cycle_dd_126d_slope_v063_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _max(_f81_evs(e, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of run-up of EV/Sales
def f81es_f81_semi_ev_sales_cycle_up_126d_slope_v064_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _min(_f81_evs(e, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_vol_126d_slope_v065_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _std(_f81_evs(e, rv), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of log-dev of EV/Sales from 126d mean
def f81es_f81_semi_ev_sales_cycle_logdev_126d_slope_v066_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (np.log(_f81_evs(e, rv).replace(0, np.nan).abs()) - _mean(np.log(_f81_evs(e, rv).replace(0, np.nan).abs()), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex intensity level vs 126d mean
def f81es_f81_semi_ev_sales_cycle_cxi_126d_slope_v067_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _mean(_f81_cx_int(cx, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxiz_126d_slope_v068_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_cx_int(cx, rv), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex phase 126d
def f81es_f81_semi_ev_sales_cycle_phase_126d_slope_v069_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_composite_126d_slope_v070_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_z(_f81_evs(e, rv), 126) - _z(_f81_cx_int(cx, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales up- minus down-phase mean
def f81es_f81_semi_ev_sales_cycle_phasespread_126d_slope_v071_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv).where(_f81_phase(cx, 126) > 0), 126) - _mean(_f81_evs(e, rv).where(_f81_phase(cx, 126) < 0), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_cxicorr_126d_slope_v072_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).rolling(126, min_periods=max(2, 126//2)).corr(_f81_cx_int(cx, rv))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of log-dev EV/Sales from 126d EMA
def f81es_f81_semi_ev_sales_cycle_ltdev_126d_slope_v073_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_evs(e, rv).ewm(span=126, adjust=False).mean().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of range of EV/Sales
def f81es_f81_semi_ev_sales_cycle_rng_126d_slope_v074_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_max(_f81_evs(e, rv), 126) - _min(_f81_evs(e, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex intensity drawdown
def f81es_f81_semi_ev_sales_cycle_cxidd_126d_slope_v075_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _max(_f81_cx_int(cx, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex intensity run-up
def f81es_f81_semi_ev_sales_cycle_cxiup_126d_slope_v076_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratio_126d_slope_v077_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of log-ratio EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_logratio_126d_slope_v078_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_cx_int(cx, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales EMA crossover (126 vs 126*2)
def f81es_f81_semi_ev_sales_cycle_emax_126d_slope_v079_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv).ewm(span=126, adjust=False).mean() - _f81_evs(e, rv).ewm(span=126*2, adjust=False).mean())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex pct_change(126)
def f81es_f81_semi_ev_sales_cycle_cxgrowth_126d_slope_v080_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = cx.pct_change(periods=126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of revenue pct_change(126)
def f81es_f81_semi_ev_sales_cycle_rvgrowth_126d_slope_v081_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = rv.pct_change(periods=126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV pct_change(126)
def f81es_f81_semi_ev_sales_cycle_evgrowth_126d_slope_v082_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = e.pct_change(periods=126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales pct_change(126)
def f81es_f81_semi_ev_sales_cycle_evschg_126d_slope_v083_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).pct_change(periods=126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of rolling corr capex phase vs EV/Sales
def f81es_f81_semi_ev_sales_cycle_cxiphasecorr_126d_slope_v084_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 126).rolling(126, min_periods=max(2, 126//2)).corr(_f81_evs(e, rv))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales position in range
def f81es_f81_semi_ev_sales_cycle_pos_126d_slope_v085_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 126)) / (_max(_f81_evs(e, rv), 126) - _min(_f81_evs(e, rv), 126)).replace(0, np.nan))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_posdev_126d_slope_v086_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 126)) / (_max(_f81_evs(e, rv), 126) - _min(_f81_evs(e, rv), 126)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of capex intensity position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_cxiposdev_126d_slope_v087_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 126)) / (_max(_f81_cx_int(cx, rv), 126) - _min(_f81_cx_int(cx, rv), 126)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of log EV/Sales
def f81es_f81_semi_ev_sales_cycle_logevs_126d_slope_v088_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of z-score EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratioz_126d_slope_v089_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d slope of EV/Sales mean rel to 126d-mean of mean
def f81es_f81_semi_ev_sales_cycle_evsmeansdev_126d_slope_v090_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv), 126) - _mean(_mean(_f81_evs(e, rv), 126), 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales level vs 252d mean
def f81es_f81_semi_ev_sales_cycle_level_252d_slope_v091_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _mean(_f81_evs(e, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_z_252d_slope_v092_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv), 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of drawdown of EV/Sales
def f81es_f81_semi_ev_sales_cycle_dd_252d_slope_v093_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _max(_f81_evs(e, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of run-up of EV/Sales
def f81es_f81_semi_ev_sales_cycle_up_252d_slope_v094_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _min(_f81_evs(e, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_vol_252d_slope_v095_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _std(_f81_evs(e, rv), 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of log-dev of EV/Sales from 252d mean
def f81es_f81_semi_ev_sales_cycle_logdev_252d_slope_v096_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (np.log(_f81_evs(e, rv).replace(0, np.nan).abs()) - _mean(np.log(_f81_evs(e, rv).replace(0, np.nan).abs()), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex intensity level vs 252d mean
def f81es_f81_semi_ev_sales_cycle_cxi_252d_slope_v097_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _mean(_f81_cx_int(cx, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxiz_252d_slope_v098_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_cx_int(cx, rv), 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex phase 252d
def f81es_f81_semi_ev_sales_cycle_phase_252d_slope_v099_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_composite_252d_slope_v100_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_z(_f81_evs(e, rv), 252) - _z(_f81_cx_int(cx, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales up- minus down-phase mean
def f81es_f81_semi_ev_sales_cycle_phasespread_252d_slope_v101_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv).where(_f81_phase(cx, 252) > 0), 252) - _mean(_f81_evs(e, rv).where(_f81_phase(cx, 252) < 0), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_cxicorr_252d_slope_v102_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).rolling(252, min_periods=max(2, 252//2)).corr(_f81_cx_int(cx, rv))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of log-dev EV/Sales from 252d EMA
def f81es_f81_semi_ev_sales_cycle_ltdev_252d_slope_v103_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_evs(e, rv).ewm(span=252, adjust=False).mean().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of range of EV/Sales
def f81es_f81_semi_ev_sales_cycle_rng_252d_slope_v104_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_max(_f81_evs(e, rv), 252) - _min(_f81_evs(e, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex intensity drawdown
def f81es_f81_semi_ev_sales_cycle_cxidd_252d_slope_v105_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _max(_f81_cx_int(cx, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex intensity run-up
def f81es_f81_semi_ev_sales_cycle_cxiup_252d_slope_v106_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratio_252d_slope_v107_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of log-ratio EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_logratio_252d_slope_v108_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_cx_int(cx, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales EMA crossover (252 vs 252*2)
def f81es_f81_semi_ev_sales_cycle_emax_252d_slope_v109_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv).ewm(span=252, adjust=False).mean() - _f81_evs(e, rv).ewm(span=252*2, adjust=False).mean())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex pct_change(252)
def f81es_f81_semi_ev_sales_cycle_cxgrowth_252d_slope_v110_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = cx.pct_change(periods=252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of revenue pct_change(252)
def f81es_f81_semi_ev_sales_cycle_rvgrowth_252d_slope_v111_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = rv.pct_change(periods=252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV pct_change(252)
def f81es_f81_semi_ev_sales_cycle_evgrowth_252d_slope_v112_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = e.pct_change(periods=252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales pct_change(252)
def f81es_f81_semi_ev_sales_cycle_evschg_252d_slope_v113_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).pct_change(periods=252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of rolling corr capex phase vs EV/Sales
def f81es_f81_semi_ev_sales_cycle_cxiphasecorr_252d_slope_v114_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 252).rolling(252, min_periods=max(2, 252//2)).corr(_f81_evs(e, rv))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales position in range
def f81es_f81_semi_ev_sales_cycle_pos_252d_slope_v115_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 252)) / (_max(_f81_evs(e, rv), 252) - _min(_f81_evs(e, rv), 252)).replace(0, np.nan))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_posdev_252d_slope_v116_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 252)) / (_max(_f81_evs(e, rv), 252) - _min(_f81_evs(e, rv), 252)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of capex intensity position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_cxiposdev_252d_slope_v117_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 252)) / (_max(_f81_cx_int(cx, rv), 252) - _min(_f81_cx_int(cx, rv), 252)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of log EV/Sales
def f81es_f81_semi_ev_sales_cycle_logevs_252d_slope_v118_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of z-score EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratioz_252d_slope_v119_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d slope of EV/Sales mean rel to 252d-mean of mean
def f81es_f81_semi_ev_sales_cycle_evsmeansdev_252d_slope_v120_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv), 252) - _mean(_mean(_f81_evs(e, rv), 252), 252))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales level vs 504d mean
def f81es_f81_semi_ev_sales_cycle_level_504d_slope_v121_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _mean(_f81_evs(e, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_z_504d_slope_v122_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv), 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of drawdown of EV/Sales
def f81es_f81_semi_ev_sales_cycle_dd_504d_slope_v123_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _max(_f81_evs(e, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of run-up of EV/Sales
def f81es_f81_semi_ev_sales_cycle_up_504d_slope_v124_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) - _min(_f81_evs(e, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_vol_504d_slope_v125_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _std(_f81_evs(e, rv), 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of log-dev of EV/Sales from 504d mean
def f81es_f81_semi_ev_sales_cycle_logdev_504d_slope_v126_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (np.log(_f81_evs(e, rv).replace(0, np.nan).abs()) - _mean(np.log(_f81_evs(e, rv).replace(0, np.nan).abs()), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex intensity level vs 504d mean
def f81es_f81_semi_ev_sales_cycle_cxi_504d_slope_v127_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _mean(_f81_cx_int(cx, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxiz_504d_slope_v128_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_cx_int(cx, rv), 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex phase 504d
def f81es_f81_semi_ev_sales_cycle_phase_504d_slope_v129_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_composite_504d_slope_v130_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_z(_f81_evs(e, rv), 504) - _z(_f81_cx_int(cx, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales up- minus down-phase mean
def f81es_f81_semi_ev_sales_cycle_phasespread_504d_slope_v131_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv).where(_f81_phase(cx, 504) > 0), 504) - _mean(_f81_evs(e, rv).where(_f81_phase(cx, 504) < 0), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_cxicorr_504d_slope_v132_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).rolling(504, min_periods=max(2, 504//2)).corr(_f81_cx_int(cx, rv))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of log-dev EV/Sales from 504d EMA
def f81es_f81_semi_ev_sales_cycle_ltdev_504d_slope_v133_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_evs(e, rv).ewm(span=504, adjust=False).mean().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of range of EV/Sales
def f81es_f81_semi_ev_sales_cycle_rng_504d_slope_v134_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_max(_f81_evs(e, rv), 504) - _min(_f81_evs(e, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex intensity drawdown
def f81es_f81_semi_ev_sales_cycle_cxidd_504d_slope_v135_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _max(_f81_cx_int(cx, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex intensity run-up
def f81es_f81_semi_ev_sales_cycle_cxiup_504d_slope_v136_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratio_504d_slope_v137_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of log-ratio EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_logratio_504d_slope_v138_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs() / _f81_cx_int(cx, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales EMA crossover (504 vs 504*2)
def f81es_f81_semi_ev_sales_cycle_emax_504d_slope_v139_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_f81_evs(e, rv).ewm(span=504, adjust=False).mean() - _f81_evs(e, rv).ewm(span=504*2, adjust=False).mean())
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex pct_change(504)
def f81es_f81_semi_ev_sales_cycle_cxgrowth_504d_slope_v140_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = cx.pct_change(periods=504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of revenue pct_change(504)
def f81es_f81_semi_ev_sales_cycle_rvgrowth_504d_slope_v141_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = rv.pct_change(periods=504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV pct_change(504)
def f81es_f81_semi_ev_sales_cycle_evgrowth_504d_slope_v142_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = e.pct_change(periods=504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales pct_change(504)
def f81es_f81_semi_ev_sales_cycle_evschg_504d_slope_v143_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_evs(e, rv).pct_change(periods=504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of rolling corr capex phase vs EV/Sales
def f81es_f81_semi_ev_sales_cycle_cxiphasecorr_504d_slope_v144_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _f81_phase(cx, 504).rolling(504, min_periods=max(2, 504//2)).corr(_f81_evs(e, rv))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales position in range
def f81es_f81_semi_ev_sales_cycle_pos_504d_slope_v145_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 504)) / (_max(_f81_evs(e, rv), 504) - _min(_f81_evs(e, rv), 504)).replace(0, np.nan))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_posdev_504d_slope_v146_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_evs(e, rv) - _min(_f81_evs(e, rv), 504)) / (_max(_f81_evs(e, rv), 504) - _min(_f81_evs(e, rv), 504)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of capex intensity position deviated 0.5
def f81es_f81_semi_ev_sales_cycle_cxiposdev_504d_slope_v147_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = ((_f81_cx_int(cx, rv) - _min(_f81_cx_int(cx, rv), 504)) / (_max(_f81_cx_int(cx, rv), 504) - _min(_f81_cx_int(cx, rv), 504)).replace(0, np.nan) - 0.5)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of log EV/Sales
def f81es_f81_semi_ev_sales_cycle_logevs_504d_slope_v148_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = np.log(_f81_evs(e, rv).replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of z-score EV/Sales over capex intensity
def f81es_f81_semi_ev_sales_cycle_ratioz_504d_slope_v149_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = _z(_f81_evs(e, rv) / _f81_cx_int(cx, rv).replace(0, np.nan), 504)
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d slope of EV/Sales mean rel to 504d-mean of mean
def f81es_f81_semi_ev_sales_cycle_evsmeansdev_504d_slope_v150_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    base = (_mean(_f81_evs(e, rv), 504) - _mean(_mean(_f81_evs(e, rv), 504), 504))
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



