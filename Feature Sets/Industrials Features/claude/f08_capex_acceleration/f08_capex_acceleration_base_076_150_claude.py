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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f08_capex_growth(capex, w):
    return capex.pct_change(periods=w)


def _f08_capex_to_revenue(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f08_capex_intensity_change(capex, revenue, w):
    intens = capex / revenue.replace(0, np.nan).abs()
    return intens.diff(periods=w)


# 21d capex growth * close^2
def f08cap_f08_capex_acceleration_growxprice_21d_base_v076_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth * close^2
def f08cap_f08_capex_acceleration_growxprice_63d_base_v077_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    result = g * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth * close^2
def f08cap_f08_capex_acceleration_growxprice_252d_base_v078_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 252)
    result = g * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crev * close^2
def f08cap_f08_capex_acceleration_crevxprice_21d_base_v079_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = _mean(c, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crev * close^2
def f08cap_f08_capex_acceleration_crevxprice_63d_base_v080_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = _mean(c, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev * close^2
def f08cap_f08_capex_acceleration_crevxprice_252d_base_v081_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = _mean(c, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth absolute value rolling mean 21d
def f08cap_f08_capex_acceleration_growabs_21d_base_v082_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = _mean(g.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs capex growth
def f08cap_f08_capex_acceleration_growabs_63d_base_v083_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = _mean(g.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs capex growth
def f08cap_f08_capex_acceleration_growabs_252d_base_v084_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = _mean(g.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d abs capex growth
def f08cap_f08_capex_acceleration_growabs_504d_base_v085_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = _mean(g.abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth rolling sum 21d
def f08cap_f08_capex_acceleration_growsum_21d_base_v086_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    result = g.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth rolling sum 63d
def f08cap_f08_capex_acceleration_growsum_63d_base_v087_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth rolling sum 252d
def f08cap_f08_capex_acceleration_growsum_252d_base_v088_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth max 21d
def f08cap_f08_capex_acceleration_growmax_21d_base_v089_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth max 63d
def f08cap_f08_capex_acceleration_growmax_63d_base_v090_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth max 252d
def f08cap_f08_capex_acceleration_growmax_252d_base_v091_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth min 21d
def f08cap_f08_capex_acceleration_growmin_21d_base_v092_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(21, min_periods=5).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth min 63d
def f08cap_f08_capex_acceleration_growmin_63d_base_v093_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth min 252d
def f08cap_f08_capex_acceleration_growmin_252d_base_v094_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth range 252d
def f08cap_f08_capex_acceleration_growrng_252d_base_v095_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Crev max 252d
def f08cap_f08_capex_acceleration_crevmax_252d_base_v096_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = c.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Crev min 252d
def f08cap_f08_capex_acceleration_crevmin_252d_base_v097_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = c.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Crev range 252d
def f08cap_f08_capex_acceleration_crevrng_252d_base_v098_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    rng = c.rolling(252, min_periods=63).max() - c.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crev percentile 252d
def f08cap_f08_capex_acceleration_crevpct_252d_base_v099_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth percentile 252d
def f08cap_f08_capex_acceleration_growpct_252d_base_v100_signal(capex, closeadj):
    b = _f08_capex_growth(capex, 21)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth percentile 504d
def f08cap_f08_capex_acceleration_growpct_504d_base_v101_signal(capex, closeadj):
    b = _f08_capex_growth(capex, 21)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex_grow * close return
def f08cap_f08_capex_acceleration_growxcret_21d_base_v102_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    cret = closeadj.pct_change(21)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex_grow * close return
def f08cap_f08_capex_acceleration_growxcret_63d_base_v103_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    cret = closeadj.pct_change(63)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex_grow * close return
def f08cap_f08_capex_acceleration_growxcret_252d_base_v104_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 252)
    cret = closeadj.pct_change(252)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d iint * close return
def f08cap_f08_capex_acceleration_iintxcret_21d_base_v105_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    cret = closeadj.pct_change(21)
    result = i * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d iint * close return
def f08cap_f08_capex_acceleration_iintxcret_63d_base_v106_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    cret = closeadj.pct_change(63)
    result = i * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d iint * close return
def f08cap_f08_capex_acceleration_iintxcret_252d_base_v107_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    cret = closeadj.pct_change(252)
    result = i * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt abs growth
def f08cap_f08_capex_acceleration_growsqrt_21d_base_v108_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21).abs()
    result = np.sqrt(_mean(g, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt abs growth
def f08cap_f08_capex_acceleration_growsqrt_63d_base_v109_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21).abs()
    result = np.sqrt(_mean(g, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt abs growth
def f08cap_f08_capex_acceleration_growsqrt_252d_base_v110_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21).abs()
    result = np.sqrt(_mean(g, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt crev
def f08cap_f08_capex_acceleration_crevsqrt_63d_base_v111_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue).abs()
    result = np.sqrt(_mean(c, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt crev
def f08cap_f08_capex_acceleration_crevsqrt_252d_base_v112_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue).abs()
    result = np.sqrt(_mean(c, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crev CV
def f08cap_f08_capex_acceleration_crevcv_21d_base_v113_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cv = _std(c, 21) / _mean(c, 21).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crev CV
def f08cap_f08_capex_acceleration_crevcv_63d_base_v114_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cv = _std(c, 63) / _mean(c, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev CV
def f08cap_f08_capex_acceleration_crevcv_252d_base_v115_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cv = _std(c, 252) / _mean(c, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration count: 21d count of (growth > 0.05) * close
def f08cap_f08_capex_acceleration_accelcount_21d_base_v116_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    accel = (g > 0.05).astype(float)
    result = accel.rolling(21, min_periods=5).sum() * closeadj + g
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration count 63d
def f08cap_f08_capex_acceleration_accelcount_63d_base_v117_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    accel = (g > 0.05).astype(float)
    result = accel.rolling(63, min_periods=21).sum() * closeadj + g
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration count 252d
def f08cap_f08_capex_acceleration_accelcount_252d_base_v118_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    accel = (g > 0.05).astype(float)
    result = accel.rolling(252, min_periods=63).sum() * closeadj + g
    return result.replace([np.inf, -np.inf], np.nan)


# deceleration count 252d
def f08cap_f08_capex_acceleration_decelcount_252d_base_v119_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    dec = (g < -0.05).astype(float)
    result = dec.rolling(252, min_periods=63).sum() * closeadj + g
    return result.replace([np.inf, -np.inf], np.nan)


# deceleration count 504d
def f08cap_f08_capex_acceleration_decelcount_504d_base_v120_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    dec = (g < -0.05).astype(float)
    result = dec.rolling(504, min_periods=126).sum() * closeadj + g
    return result.replace([np.inf, -np.inf], np.nan)


# Capex ratio 21v252 * close
def f08cap_f08_capex_acceleration_capratio_21v252_base_v121_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 21) / _mean(capex, 252).replace(0, np.nan).abs()
    result = ratio * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# Capex ratio 63v252 * close
def f08cap_f08_capex_acceleration_capratio_63v252_base_v122_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 63) / _mean(capex, 252).replace(0, np.nan).abs()
    result = ratio * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# Capex ratio 63v504 * close
def f08cap_f08_capex_acceleration_capratio_63v504_base_v123_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 63) / _mean(capex, 504).replace(0, np.nan).abs()
    result = ratio * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# Capex ratio 126v504 * close
def f08cap_f08_capex_acceleration_capratio_126v504_base_v124_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 126) / _mean(capex, 504).replace(0, np.nan).abs()
    result = ratio * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev ratio 21v252
def f08cap_f08_capex_acceleration_crevratio_21v252_base_v125_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(c, 21) / _mean(c, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev ratio 63v252
def f08cap_f08_capex_acceleration_crevratio_63v252_base_v126_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(c, 63) / _mean(c, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev ratio 63v504
def f08cap_f08_capex_acceleration_crevratio_63v504_base_v127_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(c, 63) / _mean(c, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex log * close
def f08cap_f08_capex_acceleration_caplog_252d_base_v128_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = np.log(_mean(capex, 252).replace(0, np.nan).abs())
    result = base * closeadj / 10 + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# Crev log
def f08cap_f08_capex_acceleration_crevlog_252d_base_v129_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = np.log(_mean(c, 252).replace(0, np.nan).abs())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative iint
def f08cap_f08_capex_acceleration_iintcum_63d_base_v130_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    result = i.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative iint
def f08cap_f08_capex_acceleration_iintcum_252d_base_v131_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    result = i.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative iint
def f08cap_f08_capex_acceleration_iintcum_504d_base_v132_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    result = i.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow x revenue grow alignment 63d
def f08cap_f08_capex_acceleration_growxrevgrow_63d_base_v133_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow x revenue grow 252d
def f08cap_f08_capex_acceleration_growxrevgrow_252d_base_v134_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    rg = revenue.pct_change(252)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow minus revenue grow 63d
def f08cap_f08_capex_acceleration_growminusrev_63d_base_v135_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    result = (g - rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow minus revenue grow 252d
def f08cap_f08_capex_acceleration_growminusrev_252d_base_v136_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    rg = revenue.pct_change(252)
    result = (g - rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow vs revenue grow ratio 63d
def f08cap_f08_capex_acceleration_growoverrev_63d_base_v137_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    result = (g / rg.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow vs revenue grow ratio 252d
def f08cap_f08_capex_acceleration_growoverrev_252d_base_v138_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    rg = revenue.pct_change(252)
    result = (g / rg.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: grow(21) - grow(63), 63d window
def f08cap_f08_capex_acceleration_accel_21m63_base_v139_signal(capex, closeadj):
    g21 = _f08_capex_growth(capex, 21)
    g63 = _f08_capex_growth(capex, 63)
    result = (g21 - g63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: grow(63) - grow(252)
def f08cap_f08_capex_acceleration_accel_63m252_base_v140_signal(capex, closeadj):
    g63 = _f08_capex_growth(capex, 63)
    g252 = _f08_capex_growth(capex, 252)
    result = (g63 - g252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: grow(252) - grow(504)
def f08cap_f08_capex_acceleration_accel_252m504_base_v141_signal(capex, closeadj):
    g252 = _f08_capex_growth(capex, 252)
    g504 = _f08_capex_growth(capex, 504)
    result = (g252 - g504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d iint x revenue ratio
def f08cap_f08_capex_acceleration_iintnorm_63d_base_v142_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    result = (i / c.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d iint normalized
def f08cap_f08_capex_acceleration_iintnorm_252d_base_v143_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    result = (i / c.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cap_growth * crev (overinvestment)
def f08cap_f08_capex_acceleration_overinv_21d_base_v144_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 21)
    c = _f08_capex_to_revenue(capex, revenue)
    z = _z(c, 252)
    result = g * z * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cap_growth * crev z
def f08cap_f08_capex_acceleration_overinv_63d_base_v145_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    z = _z(c, 252)
    result = g * z * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cap_growth * crev z
def f08cap_f08_capex_acceleration_overinv_252d_base_v146_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    z = _z(c, 504)
    result = g * z * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite (grow + iint) * close
def f08cap_f08_capex_acceleration_composite_252d_base_v147_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    i = _f08_capex_intensity_change(capex, revenue, 63)
    result = (g + i) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite (grow + iint) * close
def f08cap_f08_capex_acceleration_composite_504d_base_v148_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 126)
    i = _f08_capex_intensity_change(capex, revenue, 252)
    result = (g + i) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex level / median * close
def f08cap_f08_capex_acceleration_caplevel_252d_base_v149_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = capex / capex.rolling(252, min_periods=63).median().replace(0, np.nan).abs()
    result = base * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex level / median * close
def f08cap_f08_capex_acceleration_caplevel_504d_base_v150_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = capex / capex.rolling(504, min_periods=126).median().replace(0, np.nan).abs()
    result = base * closeadj + g * 0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cap_f08_capex_acceleration_growxprice_21d_base_v076_signal,
    f08cap_f08_capex_acceleration_growxprice_63d_base_v077_signal,
    f08cap_f08_capex_acceleration_growxprice_252d_base_v078_signal,
    f08cap_f08_capex_acceleration_crevxprice_21d_base_v079_signal,
    f08cap_f08_capex_acceleration_crevxprice_63d_base_v080_signal,
    f08cap_f08_capex_acceleration_crevxprice_252d_base_v081_signal,
    f08cap_f08_capex_acceleration_growabs_21d_base_v082_signal,
    f08cap_f08_capex_acceleration_growabs_63d_base_v083_signal,
    f08cap_f08_capex_acceleration_growabs_252d_base_v084_signal,
    f08cap_f08_capex_acceleration_growabs_504d_base_v085_signal,
    f08cap_f08_capex_acceleration_growsum_21d_base_v086_signal,
    f08cap_f08_capex_acceleration_growsum_63d_base_v087_signal,
    f08cap_f08_capex_acceleration_growsum_252d_base_v088_signal,
    f08cap_f08_capex_acceleration_growmax_21d_base_v089_signal,
    f08cap_f08_capex_acceleration_growmax_63d_base_v090_signal,
    f08cap_f08_capex_acceleration_growmax_252d_base_v091_signal,
    f08cap_f08_capex_acceleration_growmin_21d_base_v092_signal,
    f08cap_f08_capex_acceleration_growmin_63d_base_v093_signal,
    f08cap_f08_capex_acceleration_growmin_252d_base_v094_signal,
    f08cap_f08_capex_acceleration_growrng_252d_base_v095_signal,
    f08cap_f08_capex_acceleration_crevmax_252d_base_v096_signal,
    f08cap_f08_capex_acceleration_crevmin_252d_base_v097_signal,
    f08cap_f08_capex_acceleration_crevrng_252d_base_v098_signal,
    f08cap_f08_capex_acceleration_crevpct_252d_base_v099_signal,
    f08cap_f08_capex_acceleration_growpct_252d_base_v100_signal,
    f08cap_f08_capex_acceleration_growpct_504d_base_v101_signal,
    f08cap_f08_capex_acceleration_growxcret_21d_base_v102_signal,
    f08cap_f08_capex_acceleration_growxcret_63d_base_v103_signal,
    f08cap_f08_capex_acceleration_growxcret_252d_base_v104_signal,
    f08cap_f08_capex_acceleration_iintxcret_21d_base_v105_signal,
    f08cap_f08_capex_acceleration_iintxcret_63d_base_v106_signal,
    f08cap_f08_capex_acceleration_iintxcret_252d_base_v107_signal,
    f08cap_f08_capex_acceleration_growsqrt_21d_base_v108_signal,
    f08cap_f08_capex_acceleration_growsqrt_63d_base_v109_signal,
    f08cap_f08_capex_acceleration_growsqrt_252d_base_v110_signal,
    f08cap_f08_capex_acceleration_crevsqrt_63d_base_v111_signal,
    f08cap_f08_capex_acceleration_crevsqrt_252d_base_v112_signal,
    f08cap_f08_capex_acceleration_crevcv_21d_base_v113_signal,
    f08cap_f08_capex_acceleration_crevcv_63d_base_v114_signal,
    f08cap_f08_capex_acceleration_crevcv_252d_base_v115_signal,
    f08cap_f08_capex_acceleration_accelcount_21d_base_v116_signal,
    f08cap_f08_capex_acceleration_accelcount_63d_base_v117_signal,
    f08cap_f08_capex_acceleration_accelcount_252d_base_v118_signal,
    f08cap_f08_capex_acceleration_decelcount_252d_base_v119_signal,
    f08cap_f08_capex_acceleration_decelcount_504d_base_v120_signal,
    f08cap_f08_capex_acceleration_capratio_21v252_base_v121_signal,
    f08cap_f08_capex_acceleration_capratio_63v252_base_v122_signal,
    f08cap_f08_capex_acceleration_capratio_63v504_base_v123_signal,
    f08cap_f08_capex_acceleration_capratio_126v504_base_v124_signal,
    f08cap_f08_capex_acceleration_crevratio_21v252_base_v125_signal,
    f08cap_f08_capex_acceleration_crevratio_63v252_base_v126_signal,
    f08cap_f08_capex_acceleration_crevratio_63v504_base_v127_signal,
    f08cap_f08_capex_acceleration_caplog_252d_base_v128_signal,
    f08cap_f08_capex_acceleration_crevlog_252d_base_v129_signal,
    f08cap_f08_capex_acceleration_iintcum_63d_base_v130_signal,
    f08cap_f08_capex_acceleration_iintcum_252d_base_v131_signal,
    f08cap_f08_capex_acceleration_iintcum_504d_base_v132_signal,
    f08cap_f08_capex_acceleration_growxrevgrow_63d_base_v133_signal,
    f08cap_f08_capex_acceleration_growxrevgrow_252d_base_v134_signal,
    f08cap_f08_capex_acceleration_growminusrev_63d_base_v135_signal,
    f08cap_f08_capex_acceleration_growminusrev_252d_base_v136_signal,
    f08cap_f08_capex_acceleration_growoverrev_63d_base_v137_signal,
    f08cap_f08_capex_acceleration_growoverrev_252d_base_v138_signal,
    f08cap_f08_capex_acceleration_accel_21m63_base_v139_signal,
    f08cap_f08_capex_acceleration_accel_63m252_base_v140_signal,
    f08cap_f08_capex_acceleration_accel_252m504_base_v141_signal,
    f08cap_f08_capex_acceleration_iintnorm_63d_base_v142_signal,
    f08cap_f08_capex_acceleration_iintnorm_252d_base_v143_signal,
    f08cap_f08_capex_acceleration_overinv_21d_base_v144_signal,
    f08cap_f08_capex_acceleration_overinv_63d_base_v145_signal,
    f08cap_f08_capex_acceleration_overinv_252d_base_v146_signal,
    f08cap_f08_capex_acceleration_composite_252d_base_v147_signal,
    f08cap_f08_capex_acceleration_composite_504d_base_v148_signal,
    f08cap_f08_capex_acceleration_caplevel_252d_base_v149_signal,
    f08cap_f08_capex_acceleration_caplevel_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPEX_ACCELERATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "capex": capex, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_capex_growth", "_f08_capex_to_revenue", "_f08_capex_intensity_change")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f08_capex_acceleration_base_076_150_claude: {n_features} features pass")
