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


# 21d log-dev of EV/Sales from 21d mean
def f81es_f81_semi_ev_sales_cycle_evs_logdev_21d_base_v076_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lg = np.log(s.replace(0, np.nan).abs())
    result = lg - _mean(lg, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d log-dev of EV/Sales from 63d mean
def f81es_f81_semi_ev_sales_cycle_evs_logdev_63d_base_v077_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lg = np.log(s.replace(0, np.nan).abs())
    result = lg - _mean(lg, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d log-dev of EV/Sales from 126d mean
def f81es_f81_semi_ev_sales_cycle_evs_logdev_126d_base_v078_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lg = np.log(s.replace(0, np.nan).abs())
    result = lg - _mean(lg, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d log-dev of EV/Sales from 252d mean
def f81es_f81_semi_ev_sales_cycle_evs_logdev_252d_base_v079_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lg = np.log(s.replace(0, np.nan).abs())
    result = lg - _mean(lg, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d log-dev of EV/Sales from 504d mean
def f81es_f81_semi_ev_sales_cycle_evs_logdev_504d_base_v080_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lg = np.log(s.replace(0, np.nan).abs())
    result = lg - _mean(lg, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d robust z-score of EV/Sales (median/MAD)
def f81es_f81_semi_ev_sales_cycle_evs_robustz_21d_base_v081_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    med = s.rolling(21, min_periods=max(2, 21//2)).median()
    mad = (s - med).abs().rolling(21, min_periods=max(2, 21//2)).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d robust z-score of EV/Sales (median/MAD)
def f81es_f81_semi_ev_sales_cycle_evs_robustz_63d_base_v082_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    med = s.rolling(63, min_periods=max(2, 63//2)).median()
    mad = (s - med).abs().rolling(63, min_periods=max(2, 63//2)).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d robust z-score of EV/Sales (median/MAD)
def f81es_f81_semi_ev_sales_cycle_evs_robustz_126d_base_v083_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    med = s.rolling(126, min_periods=max(2, 126//2)).median()
    mad = (s - med).abs().rolling(126, min_periods=max(2, 126//2)).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d robust z-score of EV/Sales (median/MAD)
def f81es_f81_semi_ev_sales_cycle_evs_robustz_252d_base_v084_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    med = s.rolling(252, min_periods=max(2, 252//2)).median()
    mad = (s - med).abs().rolling(252, min_periods=max(2, 252//2)).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d robust z-score of EV/Sales (median/MAD)
def f81es_f81_semi_ev_sales_cycle_evs_robustz_504d_base_v085_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    med = s.rolling(504, min_periods=max(2, 504//2)).median()
    mad = (s - med).abs().rolling(504, min_periods=max(2, 504//2)).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score of EV/Sales divided by capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_ratio_21d_base_v086_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    r = s / p.replace(0, np.nan)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score of EV/Sales divided by capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_ratio_63d_base_v087_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    r = s / p.replace(0, np.nan)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score of EV/Sales divided by capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_ratio_126d_base_v088_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    r = s / p.replace(0, np.nan)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score of EV/Sales divided by capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_ratio_252d_base_v089_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    r = s / p.replace(0, np.nan)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score of EV/Sales divided by capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_ratio_504d_base_v090_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    r = s / p.replace(0, np.nan)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_dd_21d_base_v091_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _max(p, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_dd_63d_base_v092_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _max(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_dd_126d_base_v093_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _max(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_dd_252d_base_v094_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _max(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of capex intensity
def f81es_f81_semi_ev_sales_cycle_cxi_dd_504d_base_v095_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _max(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d run-up of capex intensity above trough
def f81es_f81_semi_ev_sales_cycle_cxi_up_21d_base_v096_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _min(p, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d run-up of capex intensity above trough
def f81es_f81_semi_ev_sales_cycle_cxi_up_63d_base_v097_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _min(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d run-up of capex intensity above trough
def f81es_f81_semi_ev_sales_cycle_cxi_up_126d_base_v098_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _min(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d run-up of capex intensity above trough
def f81es_f81_semi_ev_sales_cycle_cxi_up_252d_base_v099_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _min(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d run-up of capex intensity above trough
def f81es_f81_semi_ev_sales_cycle_cxi_up_504d_base_v100_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    p = _f81_cx_int(cx, rv)
    result = p - _min(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d EMA EV/Sales crossover (21 vs 42)
def f81es_f81_semi_ev_sales_cycle_evs_ema_x_21d_base_v101_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.ewm(span=21, adjust=False).mean() - s.ewm(span=42, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d EMA EV/Sales crossover (63 vs 126)
def f81es_f81_semi_ev_sales_cycle_evs_ema_x_63d_base_v102_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.ewm(span=63, adjust=False).mean() - s.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d EMA EV/Sales crossover (126 vs 252)
def f81es_f81_semi_ev_sales_cycle_evs_ema_x_126d_base_v103_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.ewm(span=126, adjust=False).mean() - s.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d EMA EV/Sales crossover (252 vs 504)
def f81es_f81_semi_ev_sales_cycle_evs_ema_x_252d_base_v104_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.ewm(span=252, adjust=False).mean() - s.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d EMA EV/Sales crossover (504 vs 1008)
def f81es_f81_semi_ev_sales_cycle_evs_ema_x_504d_base_v105_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    result = s.ewm(span=504, adjust=False).mean() - s.ewm(span=1008, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of EV/Sales when capex above 252d trend (peak)
def f81es_f81_semi_ev_sales_cycle_evs_cxpeak_21d_base_v106_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase > 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of EV/Sales when capex above 252d trend (peak)
def f81es_f81_semi_ev_sales_cycle_evs_cxpeak_63d_base_v107_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase > 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of EV/Sales when capex above 252d trend (peak)
def f81es_f81_semi_ev_sales_cycle_evs_cxpeak_126d_base_v108_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase > 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of EV/Sales when capex above 252d trend (peak)
def f81es_f81_semi_ev_sales_cycle_evs_cxpeak_252d_base_v109_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase > 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of EV/Sales when capex above 252d trend (peak)
def f81es_f81_semi_ev_sales_cycle_evs_cxpeak_504d_base_v110_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase > 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of EV/Sales when capex below 252d trend (trough)
def f81es_f81_semi_ev_sales_cycle_evs_cxtrough_21d_base_v111_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase < 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of EV/Sales when capex below 252d trend (trough)
def f81es_f81_semi_ev_sales_cycle_evs_cxtrough_63d_base_v112_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase < 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of EV/Sales when capex below 252d trend (trough)
def f81es_f81_semi_ev_sales_cycle_evs_cxtrough_126d_base_v113_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase < 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of EV/Sales when capex below 252d trend (trough)
def f81es_f81_semi_ev_sales_cycle_evs_cxtrough_252d_base_v114_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase < 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of EV/Sales when capex below 252d trend (trough)
def f81es_f81_semi_ev_sales_cycle_evs_cxtrough_504d_base_v115_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    peak_phase = _f81_phase(cx, 252)
    masked = s.where(peak_phase < 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d composite EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_evs_cycle_composite_21d_base_v116_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = _z(s, 21) - _z(p, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d composite EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_evs_cycle_composite_63d_base_v117_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = _z(s, 63) - _z(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d composite EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_evs_cycle_composite_126d_base_v118_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = _z(s, 126) - _z(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d composite EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_evs_cycle_composite_252d_base_v119_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = _z(s, 252) - _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d composite EV/Sales z minus capex-intensity z
def f81es_f81_semi_ev_sales_cycle_evs_cycle_composite_504d_base_v120_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = _z(s, 504) - _z(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean EV/Sales pct chg during capex growth+
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxup_21d_base_v121_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=21)
    chg = s.pct_change(periods=21)
    masked = chg.where(cg > 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean EV/Sales pct chg during capex growth+
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxup_63d_base_v122_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=63)
    chg = s.pct_change(periods=63)
    masked = chg.where(cg > 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean EV/Sales pct chg during capex growth+
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxup_126d_base_v123_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=126)
    chg = s.pct_change(periods=126)
    masked = chg.where(cg > 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean EV/Sales pct chg during capex growth+
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxup_252d_base_v124_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=252)
    chg = s.pct_change(periods=252)
    masked = chg.where(cg > 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean EV/Sales pct chg during capex growth+
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxup_504d_base_v125_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=504)
    chg = s.pct_change(periods=504)
    masked = chg.where(cg > 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean EV/Sales pct chg during capex growth-
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxdn_21d_base_v126_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=21)
    chg = s.pct_change(periods=21)
    masked = chg.where(cg < 0)
    result = _mean(masked, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean EV/Sales pct chg during capex growth-
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxdn_63d_base_v127_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=63)
    chg = s.pct_change(periods=63)
    masked = chg.where(cg < 0)
    result = _mean(masked, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean EV/Sales pct chg during capex growth-
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxdn_126d_base_v128_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=126)
    chg = s.pct_change(periods=126)
    masked = chg.where(cg < 0)
    result = _mean(masked, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean EV/Sales pct chg during capex growth-
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxdn_252d_base_v129_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=252)
    chg = s.pct_change(periods=252)
    masked = chg.where(cg < 0)
    result = _mean(masked, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean EV/Sales pct chg during capex growth-
def f81es_f81_semi_ev_sales_cycle_evs_chg_cxdn_504d_base_v130_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    cg = cx.pct_change(periods=504)
    chg = s.pct_change(periods=504)
    masked = chg.where(cg < 0)
    result = _mean(masked, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d log-dev of EV/Sales from 21d EMA trend
def f81es_f81_semi_ev_sales_cycle_evs_lt_dev_21d_base_v131_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lt = s.ewm(span=21, adjust=False).mean()
    result = np.log(s.replace(0, np.nan).abs() / lt.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)



# 63d log-dev of EV/Sales from 63d EMA trend
def f81es_f81_semi_ev_sales_cycle_evs_lt_dev_63d_base_v132_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lt = s.ewm(span=63, adjust=False).mean()
    result = np.log(s.replace(0, np.nan).abs() / lt.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)



# 126d log-dev of EV/Sales from 126d EMA trend
def f81es_f81_semi_ev_sales_cycle_evs_lt_dev_126d_base_v133_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lt = s.ewm(span=126, adjust=False).mean()
    result = np.log(s.replace(0, np.nan).abs() / lt.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)



# 252d log-dev of EV/Sales from 252d EMA trend
def f81es_f81_semi_ev_sales_cycle_evs_lt_dev_252d_base_v134_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lt = s.ewm(span=252, adjust=False).mean()
    result = np.log(s.replace(0, np.nan).abs() / lt.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)



# 504d log-dev of EV/Sales from 504d EMA trend
def f81es_f81_semi_ev_sales_cycle_evs_lt_dev_504d_base_v135_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    lt = s.ewm(span=504, adjust=False).mean()
    result = np.log(s.replace(0, np.nan).abs() / lt.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_corr_21d_base_v136_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = s.rolling(21, min_periods=max(2, 21//2)).corr(p)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_corr_63d_base_v137_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = s.rolling(63, min_periods=max(2, 63//2)).corr(p)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_corr_126d_base_v138_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = s.rolling(126, min_periods=max(2, 126//2)).corr(p)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_corr_252d_base_v139_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = s.rolling(252, min_periods=max(2, 252//2)).corr(p)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr EV/Sales vs capex intensity
def f81es_f81_semi_ev_sales_cycle_evs_cxi_corr_504d_base_v140_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    p = _f81_cx_int(cx, rv)
    result = s.rolling(504, min_periods=max(2, 504//2)).corr(p)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d regime flag EV/Sales rich & capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_regimecx_21d_base_v141_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 21)
    cond = (s > _mean(s, 21)) & (phase > 0)
    result = cond.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d regime flag EV/Sales rich & capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_regimecx_63d_base_v142_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 63)
    cond = (s > _mean(s, 63)) & (phase > 0)
    result = cond.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d regime flag EV/Sales rich & capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_regimecx_126d_base_v143_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 126)
    cond = (s > _mean(s, 126)) & (phase > 0)
    result = cond.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d regime flag EV/Sales rich & capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_regimecx_252d_base_v144_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 252)
    cond = (s > _mean(s, 252)) & (phase > 0)
    result = cond.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d regime flag EV/Sales rich & capex up-phase
def f81es_f81_semi_ev_sales_cycle_evs_regimecx_504d_base_v145_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    phase = _f81_phase(cx, 504)
    cond = (s > _mean(s, 504)) & (phase > 0)
    result = cond.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d range of EV/Sales normalized by mean
def f81es_f81_semi_ev_sales_cycle_evs_rngnorm_21d_base_v146_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    rng = _max(s, 21) - _min(s, 21)
    m = _mean(s, 21)
    result = rng / m.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d range of EV/Sales normalized by mean
def f81es_f81_semi_ev_sales_cycle_evs_rngnorm_63d_base_v147_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    rng = _max(s, 63) - _min(s, 63)
    m = _mean(s, 63)
    result = rng / m.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d range of EV/Sales normalized by mean
def f81es_f81_semi_ev_sales_cycle_evs_rngnorm_126d_base_v148_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    rng = _max(s, 126) - _min(s, 126)
    m = _mean(s, 126)
    result = rng / m.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d range of EV/Sales normalized by mean
def f81es_f81_semi_ev_sales_cycle_evs_rngnorm_252d_base_v149_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    rng = _max(s, 252) - _min(s, 252)
    m = _mean(s, 252)
    result = rng / m.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d range of EV/Sales normalized by mean
def f81es_f81_semi_ev_sales_cycle_evs_rngnorm_504d_base_v150_signal(ev, revenue, capex, closeadj):
    e = _f81_daily(ev, closeadj)
    rv = _f81_daily(revenue, closeadj)
    cx = _f81_daily(capex, closeadj)
    s = _f81_evs(e, rv)
    rng = _max(s, 504) - _min(s, 504)
    m = _mean(s, 504)
    result = rng / m.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)



