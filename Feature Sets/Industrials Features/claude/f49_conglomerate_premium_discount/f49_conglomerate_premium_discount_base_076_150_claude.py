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


def _f49_evebitda_dynamics(evebitda, w):
    return _mean(evebitda, w)


def _f49_premium_discount(evebitda, ebitdamargin, w):
    return _mean(evebitda * ebitdamargin, w)


def _f49_sotp_proxy(ev, ebitda, revenue, w):
    return _mean((ev / ebitda.replace(0, np.nan).abs()) * (revenue / ev.replace(0, np.nan).abs()), w)


# v076-v150 — additional patterns
def f49cpd_f49_conglomerate_premium_discount_evebitda_lograw_252d_base_v076_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lograw_252d_base_v077_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_lograw_252d_base_v078_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_chg_63d_base_v079_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    chg = evebitda - evebitda.shift(63)
    return ((base + chg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_63d_base_v080_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    pct = evebitda.pct_change(63)
    return ((base * (1.0 + pct)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_pctchg_252d_base_v081_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252)
    pct = (evebitda * ebitdamargin).pct_change(252)
    return ((base * (1.0 + pct)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_pctchg_252d_base_v082_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    inner = (ev / ebitda.replace(0, np.nan).abs()) * (revenue / ev.replace(0, np.nan).abs())
    pct = inner.pct_change(252)
    return ((base * (1.0 + pct)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_vs_long_252d_base_v083_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    long = _f49_evebitda_dynamics(evebitda, 252)
    return ((g - long) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_vs_long_504d_base_v084_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    long = _f49_evebitda_dynamics(evebitda, 504)
    return ((g - long) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_vs_long_252d_base_v085_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    long = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return ((g - long) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_vs_long_252d_base_v086_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    long = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return ((g - long) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_lo_252d_base_v087_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    return ((lo * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lo_252d_base_v088_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    return ((lo * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_hi_252d_base_v089_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    return ((hi * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscskew_252d_base_v090_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    return (g.rolling(252, min_periods=63).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisckurt_252d_base_v091_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    return (g.rolling(252, min_periods=63).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpskew_252d_base_v092_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    return (g.rolling(252, min_periods=63).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpkurt_252d_base_v093_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    return (g.rolling(252, min_periods=63).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqpremdisc_252d_base_v094_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (g * g.abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqsotp_252d_base_v095_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (g * g.abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_63d_base_v096_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    return (g * _z(volume, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_252d_base_v097_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (g * _z(volume, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxvolz_63d_base_v098_signal(evebitda, ebitdamargin, volume, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    return (g * _z(volume, 63) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxvolz_252d_base_v099_signal(ev, ebitda, revenue, volume, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (g * _z(volume, 252) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxdv_63d_base_v100_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    dv = closeadj * volume
    return (g * _mean(dv, 21)).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxdv_252d_base_v101_signal(evebitda, ebitdamargin, volume, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    dv = closeadj * volume
    return (g * _mean(dv, 63)).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxdv_252d_base_v102_signal(ev, ebitda, revenue, volume, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    dv = closeadj * volume
    return (g * _mean(dv, 63)).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_252d_base_v103_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (g * ebitdamargin * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_63d_base_v104_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    return (g * ebitdamargin * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_revgrowth_252d_base_v105_signal(evebitda, revenue, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_revgrowth_252d_base_v106_signal(evebitda, ebitdamargin, revenue, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_revgrowth_252d_base_v107_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_evgrowth_252d_base_v108_signal(evebitda, ev, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    eg = ev.pct_change(252)
    return (g * eg * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ebgrowth_252d_base_v109_signal(evebitda, ebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    eb = ebitda.pct_change(252)
    return (g * eb * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_base_v110_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    mr = ebitdamargin.rolling(252, min_periods=63).max() - ebitdamargin.rolling(252, min_periods=63).min()
    return (g * mr * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_marginrange_252d_base_v111_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    mr = ebitdamargin.rolling(252, min_periods=63).max() - ebitdamargin.rolling(252, min_periods=63).min()
    return (g * mr * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_252d_base_v112_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return ((a - b) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxsotp_252d_base_v113_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_premium_discount(evebitda, ebitdamargin, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return ((a + b) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_63d_base_v114_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 63)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    return ((a - b) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxlogprice_252d_base_v115_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxlogprice_252d_base_v116_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_volgrowth_252d_base_v117_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    vg = volume.pct_change(252)
    return (g * vg * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_lagdiff_252d_base_v118_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    return ((g - g.shift(252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lagdiff_252d_base_v119_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    return ((g - g.shift(252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_lagdiff_252d_base_v120_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    return ((g - g.shift(252)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_252d_base_v121_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    return ((cnt + g * 10.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_event_lo_252d_base_v122_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    return ((cnt + g * 10.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_min_63d_base_v123_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    return ((g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_max_252d_base_v124_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    return ((g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_min_63d_base_v125_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    return ((g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_max_252d_base_v126_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    return ((g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_minus_const_252d_base_v127_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return ((g - 8.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_minus_const_252d_base_v128_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return ((g - 1.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_42d_alt_base_v129_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 42) * np.log(closeadj.abs().replace(0, np.nan))
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_42d_alt_base_v130_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 42) * np.log(closeadj.abs().replace(0, np.nan))
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_42d_alt_base_v131_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 42) * np.log(closeadj.abs().replace(0, np.nan))
    return (base * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_voladj_252d_base_v132_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    vol = _std(evebitda.pct_change(), 252)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_252d_base_v133_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    vol = _std((evebitda * ebitdamargin).pct_change(), 252)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_trend_252d_base_v134_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_trend_252d_base_v135_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_trend_252d_base_v136_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_5m21_base_v137_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 5)
    lg = _f49_evebitda_dynamics(evebitda, 21)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_diff_5m21_base_v138_signal(evebitda, ebitdamargin, closeadj):
    sh = _f49_premium_discount(evebitda, ebitdamargin, 5)
    lg = _f49_premium_discount(evebitda, ebitdamargin, 21)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_diff_5m21_base_v139_signal(ev, ebitda, revenue, closeadj):
    sh = _f49_sotp_proxy(ev, ebitda, revenue, 5)
    lg = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_composite_504d_base_v140_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 504)
    b = _f49_premium_discount(evebitda, ebitdamargin, 504)
    c = _f49_sotp_proxy(ev, ebitda, revenue, 504)
    return ((a + b + c) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxprice_252d_base_v141_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (g * closeadj * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxprice_252d_base_v142_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (g * closeadj * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxprice_252d_base_v143_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (g * closeadj * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_63d_base_v144_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    vol = _std((evebitda * ebitdamargin).pct_change(), 63)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_x_revenue_252d_base_v145_signal(evebitda, revenue, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    return (g * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_x_revenue_252d_base_v146_signal(evebitda, ebitdamargin, revenue, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (g * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_252d_base_v147_signal(evebitda, ebitdamargin, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_premium_discount(evebitda, ebitdamargin, 252)
    return (a / b.replace(0, np.nan).abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_252d_base_v148_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (a / b.replace(0, np.nan).abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_sotp_ratio_252d_base_v149_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_premium_discount(evebitda, ebitdamargin, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    return (a / b.replace(0, np.nan).abs() * closeadj).replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_med_alt_252d_base_v150_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    return ((g - med) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49cpd_f49_conglomerate_premium_discount_evebitda_lograw_252d_base_v076_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lograw_252d_base_v077_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_lograw_252d_base_v078_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_chg_63d_base_v079_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_63d_base_v080_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_pctchg_252d_base_v081_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_pctchg_252d_base_v082_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_vs_long_252d_base_v083_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_vs_long_504d_base_v084_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_vs_long_252d_base_v085_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_vs_long_252d_base_v086_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_lo_252d_base_v087_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lo_252d_base_v088_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_hi_252d_base_v089_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscskew_252d_base_v090_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisckurt_252d_base_v091_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpskew_252d_base_v092_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpkurt_252d_base_v093_signal,
    f49cpd_f49_conglomerate_premium_discount_sqpremdisc_252d_base_v094_signal,
    f49cpd_f49_conglomerate_premium_discount_sqsotp_252d_base_v095_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_63d_base_v096_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_252d_base_v097_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxvolz_63d_base_v098_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxvolz_252d_base_v099_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxdv_63d_base_v100_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxdv_252d_base_v101_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxdv_252d_base_v102_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_252d_base_v103_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_63d_base_v104_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_revgrowth_252d_base_v105_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_revgrowth_252d_base_v106_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_revgrowth_252d_base_v107_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_evgrowth_252d_base_v108_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ebgrowth_252d_base_v109_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_base_v110_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_marginrange_252d_base_v111_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_252d_base_v112_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxsotp_252d_base_v113_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_63d_base_v114_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxlogprice_252d_base_v115_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxlogprice_252d_base_v116_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_volgrowth_252d_base_v117_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_lagdiff_252d_base_v118_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lagdiff_252d_base_v119_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_lagdiff_252d_base_v120_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_252d_base_v121_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_event_lo_252d_base_v122_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_min_63d_base_v123_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_max_252d_base_v124_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_min_63d_base_v125_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_max_252d_base_v126_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_minus_const_252d_base_v127_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_minus_const_252d_base_v128_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_42d_alt_base_v129_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_42d_alt_base_v130_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_42d_alt_base_v131_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_voladj_252d_base_v132_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_252d_base_v133_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_trend_252d_base_v134_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_trend_252d_base_v135_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_trend_252d_base_v136_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_5m21_base_v137_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_diff_5m21_base_v138_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_diff_5m21_base_v139_signal,
    f49cpd_f49_conglomerate_premium_discount_composite_504d_base_v140_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxprice_252d_base_v141_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxprice_252d_base_v142_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxprice_252d_base_v143_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_63d_base_v144_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_x_revenue_252d_base_v145_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_x_revenue_252d_base_v146_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_252d_base_v147_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_252d_base_v148_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_sotp_ratio_252d_base_v149_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_med_alt_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CONGLOMERATE_PREMIUM_DISCOUNT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ev      = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    evebitda = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ev": ev, "evebitda": evebitda,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_evebitda_dynamics", "_f49_premium_discount", "_f49_sotp_proxy")
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
    print(f"OK f49_conglomerate_premium_discount_base_076_150_claude: {n_features} features pass")
