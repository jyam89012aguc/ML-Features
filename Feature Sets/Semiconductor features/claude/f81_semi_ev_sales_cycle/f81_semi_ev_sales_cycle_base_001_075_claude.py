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
def _f81_daily(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f81_evs(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f81_cx_int(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f81_phase(capex, w):
    m = capex.rolling(w, min_periods=max(2, w // 2)).mean()
    return capex - m


# 21d mean of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_level_21d_base_v001_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_level_63d_base_v002_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_level_126d_base_v003_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_level_252d_base_v004_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_level_504d_base_v005_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_z_21d_base_v006_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _z(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_z_63d_base_v007_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_z_126d_base_v008_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_z_252d_base_v009_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_z_504d_base_v010_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of EV/Sales from rolling peak
def f81es_f81_semi_ev_sales_cycle_evs_dd_21d_base_v011_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of EV/Sales from rolling peak
def f81es_f81_semi_ev_sales_cycle_evs_dd_63d_base_v012_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of EV/Sales from rolling peak
def f81es_f81_semi_ev_sales_cycle_evs_dd_126d_base_v013_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of EV/Sales from rolling peak
def f81es_f81_semi_ev_sales_cycle_evs_dd_252d_base_v014_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of EV/Sales from rolling peak
def f81es_f81_semi_ev_sales_cycle_evs_dd_504d_base_v015_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d run-up of EV/Sales above rolling trough
def f81es_f81_semi_ev_sales_cycle_evs_up_21d_base_v016_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d run-up of EV/Sales above rolling trough
def f81es_f81_semi_ev_sales_cycle_evs_up_63d_base_v017_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d run-up of EV/Sales above rolling trough
def f81es_f81_semi_ev_sales_cycle_evs_up_126d_base_v018_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d run-up of EV/Sales above rolling trough
def f81es_f81_semi_ev_sales_cycle_evs_up_252d_base_v019_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d run-up of EV/Sales above rolling trough
def f81es_f81_semi_ev_sales_cycle_evs_up_504d_base_v020_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d range of EV/Sales (max - min)
def f81es_f81_semi_ev_sales_cycle_evs_rng_21d_base_v021_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _max(s, 21) - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d range of EV/Sales (max - min)
def f81es_f81_semi_ev_sales_cycle_evs_rng_63d_base_v022_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _max(s, 63) - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d range of EV/Sales (max - min)
def f81es_f81_semi_ev_sales_cycle_evs_rng_126d_base_v023_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _max(s, 126) - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d range of EV/Sales (max - min)
def f81es_f81_semi_ev_sales_cycle_evs_rng_252d_base_v024_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _max(s, 252) - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d range of EV/Sales (max - min)
def f81es_f81_semi_ev_sales_cycle_evs_rng_504d_base_v025_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _max(s, 504) - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d EV/Sales position in rolling range
def f81es_f81_semi_ev_sales_cycle_evs_pos_21d_base_v026_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lo = _min(s, 21)
    hi = _max(s, 21)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d EV/Sales position in rolling range
def f81es_f81_semi_ev_sales_cycle_evs_pos_63d_base_v027_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lo = _min(s, 63)
    hi = _max(s, 63)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d EV/Sales position in rolling range
def f81es_f81_semi_ev_sales_cycle_evs_pos_126d_base_v028_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lo = _min(s, 126)
    hi = _max(s, 126)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d EV/Sales position in rolling range
def f81es_f81_semi_ev_sales_cycle_evs_pos_252d_base_v029_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lo = _min(s, 252)
    hi = _max(s, 252)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d EV/Sales position in rolling range
def f81es_f81_semi_ev_sales_cycle_evs_pos_504d_base_v030_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lo = _min(s, 504)
    hi = _max(s, 504)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_vol_21d_base_v031_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _std(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_vol_63d_base_v032_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _std(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_vol_126d_base_v033_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _std(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_vol_252d_base_v034_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _std(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d std of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_vol_504d_base_v035_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = _std(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d pct change of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_chg_21d_base_v036_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.pct_change(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d pct change of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_chg_63d_base_v037_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d pct change of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_chg_126d_base_v038_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d pct change of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_chg_252d_base_v039_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d pct change of EV/Sales
def f81es_f81_semi_ev_sales_cycle_evs_chg_504d_base_v040_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex intensity (capex/rev)
def f81es_f81_semi_ev_sales_cycle_cxi_level_21d_base_v041_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _mean(p, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex intensity (capex/rev)
def f81es_f81_semi_ev_sales_cycle_cxi_level_63d_base_v042_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _mean(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex intensity (capex/rev)
def f81es_f81_semi_ev_sales_cycle_cxi_level_126d_base_v043_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _mean(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex intensity (capex/rev)
def f81es_f81_semi_ev_sales_cycle_cxi_level_252d_base_v044_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _mean(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex intensity (capex/rev)
def f81es_f81_semi_ev_sales_cycle_cxi_level_504d_base_v045_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _mean(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_z_21d_base_v046_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _z(p, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_z_63d_base_v047_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _z(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_z_126d_base_v048_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _z(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_z_252d_base_v049_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_z_504d_base_v050_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = _z(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d capex phase (capex - rolling mean)
def f81es_f81_semi_ev_sales_cycle_cxphase_21d_base_v051_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    result = _f81_phase(cx, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d capex phase (capex - rolling mean)
def f81es_f81_semi_ev_sales_cycle_cxphase_63d_base_v052_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    result = _f81_phase(cx, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d capex phase (capex - rolling mean)
def f81es_f81_semi_ev_sales_cycle_cxphase_126d_base_v053_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    result = _f81_phase(cx, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d capex phase (capex - rolling mean)
def f81es_f81_semi_ev_sales_cycle_cxphase_252d_base_v054_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    result = _f81_phase(cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d capex phase (capex - rolling mean)
def f81es_f81_semi_ev_sales_cycle_cxphase_504d_base_v055_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    result = _f81_phase(cx, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of EV/Sales during capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxup_21d_base_v056_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 21)
    masked = s.where(phase > 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of EV/Sales during capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxup_63d_base_v057_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 63)
    masked = s.where(phase > 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of EV/Sales during capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxup_126d_base_v058_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 126)
    masked = s.where(phase > 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of EV/Sales during capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxup_252d_base_v059_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 252)
    masked = s.where(phase > 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of EV/Sales during capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxup_504d_base_v060_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 504)
    masked = s.where(phase > 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of EV/Sales during capex down-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxdn_21d_base_v061_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 21)
    masked = s.where(phase < 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of EV/Sales during capex down-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxdn_63d_base_v062_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 63)
    masked = s.where(phase < 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of EV/Sales during capex down-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxdn_126d_base_v063_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 126)
    masked = s.where(phase < 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of EV/Sales during capex down-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxdn_252d_base_v064_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 252)
    masked = s.where(phase < 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of EV/Sales during capex down-phase
def f81es_f81_semi_ev_sales_cycle_evs_cxdn_504d_base_v065_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 504)
    masked = s.where(phase < 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d EV/Sales up-phase minus down-phase mean spread
def f81es_f81_semi_ev_sales_cycle_evs_phasespread_21d_base_v066_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 21)
    up = _mean(s.where(phase > 0), 21)
    dn = _mean(s.where(phase < 0), 21)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)



# 63d EV/Sales up-phase minus down-phase mean spread
def f81es_f81_semi_ev_sales_cycle_evs_phasespread_63d_base_v067_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 63)
    up = _mean(s.where(phase > 0), 63)
    dn = _mean(s.where(phase < 0), 63)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)



# 126d EV/Sales up-phase minus down-phase mean spread
def f81es_f81_semi_ev_sales_cycle_evs_phasespread_126d_base_v068_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 126)
    up = _mean(s.where(phase > 0), 126)
    dn = _mean(s.where(phase < 0), 126)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)



# 252d EV/Sales up-phase minus down-phase mean spread
def f81es_f81_semi_ev_sales_cycle_evs_phasespread_252d_base_v069_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 252)
    up = _mean(s.where(phase > 0), 252)
    dn = _mean(s.where(phase < 0), 252)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)



# 504d EV/Sales up-phase minus down-phase mean spread
def f81es_f81_semi_ev_sales_cycle_evs_phasespread_504d_base_v070_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 504)
    up = _mean(s.where(phase > 0), 504)
    dn = _mean(s.where(phase < 0), 504)
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)



# 21d regime flag EV/Sales above 21d mean
def f81es_f81_semi_ev_sales_cycle_evs_regime_21d_base_v071_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = (s > _mean(s, 21)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d regime flag EV/Sales above 63d mean
def f81es_f81_semi_ev_sales_cycle_evs_regime_63d_base_v072_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = (s > _mean(s, 63)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d regime flag EV/Sales above 126d mean
def f81es_f81_semi_ev_sales_cycle_evs_regime_126d_base_v073_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = (s > _mean(s, 126)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d regime flag EV/Sales above 252d mean
def f81es_f81_semi_ev_sales_cycle_evs_regime_252d_base_v074_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = (s > _mean(s, 252)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d regime flag EV/Sales above 504d mean
def f81es_f81_semi_ev_sales_cycle_evs_regime_504d_base_v075_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = (s > _mean(s, 504)).astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



