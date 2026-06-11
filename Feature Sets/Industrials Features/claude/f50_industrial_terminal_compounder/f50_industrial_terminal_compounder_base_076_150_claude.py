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


def _f50_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    return _mean(roic + fcfm, w)


def _f50_compounder_score(roic, ebitdamargin, w):
    return _mean(roic * ebitdamargin, w)


def _f50_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan).abs()
    rev_stab = 1.0 / (_std(revenue.pct_change(), w).replace(0, np.nan) + 1e-6)
    return _mean(fcfm * roic, w) * _mean(rev_stab, w)


def f50itc_f50_industrial_terminal_compounder_qcomp_lograw_252d_base_v076_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_lograw_252d_base_v077_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_lograw_252d_base_v078_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    return (np.log(g.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_med_252d_base_v079_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    return ((g - med) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_med_252d_base_v080_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    return ((g - med) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_lo_252d_base_v081_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    return ((lo * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_lo_252d_base_v082_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    return ((lo * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_252d_base_v083_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    return ((cnt + g * 10.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_event_lo_252d_base_v084_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    return ((cnt + g * 10.0) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_min_63d_base_v085_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return ((g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_max_252d_base_v086_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return ((g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_min_63d_base_v087_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return ((g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_max_252d_base_v088_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return ((g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_range_252d_base_v089_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    return (rng * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_range_252d_base_v090_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    return (rng * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_252d_base_v091_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_252d_base_v092_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_x_revgrowth_252d_base_v093_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    rg = revenue.pct_change(252)
    return (g * rg * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_252d_base_v094_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_252d_base_v095_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_chg_252d_base_v096_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    inner = roic + fcf / revenue.replace(0, np.nan).abs()
    return ((base + (inner - inner.shift(252))) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_chg_252d_base_v097_signal(roic, ebitdamargin, closeadj):
    base = _f50_compounder_score(roic, ebitdamargin, 252)
    inner = roic * ebitdamargin
    return ((base + (inner - inner.shift(252))) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_voladj_252d_base_v098_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    vol = _std(revenue.pct_change(), 252)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_voladj_252d_base_v099_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    vol = _std((roic * ebitdamargin).pct_change(), 252)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_trend_252d_base_v100_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_trend_252d_base_v101_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_trend_252d_base_v102_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    return (trend * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxvol_dv_252d_base_v103_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    dv = closeadj * volume
    return (g * _mean(dv, 63)).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexvol_dv_252d_base_v104_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    dv = closeadj * volume
    return (g * _mean(dv, 63)).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_diff_252m504_base_v105_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 252)
    lg = _f50_quality_composite(roic, fcf, revenue, 504)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_diff_252m504_base_v106_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 252)
    lg = _f50_compounder_score(roic, ebitdamargin, 504)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_diff_252m504_base_v107_signal(fcf, revenue, roic, closeadj):
    sh = _f50_terminal_quality(fcf, revenue, roic, 252)
    lg = _f50_terminal_quality(fcf, revenue, roic, 504)
    return ((sh - lg) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_diff_21m63_base_v108_signal(roic, fcf, revenue, closeadj):
    sh = _f50_quality_composite(roic, fcf, revenue, 21)
    lg = _f50_quality_composite(roic, fcf, revenue, 63)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_diff_21m63_base_v109_signal(roic, ebitdamargin, closeadj):
    sh = _f50_compounder_score(roic, ebitdamargin, 21)
    lg = _f50_compounder_score(roic, ebitdamargin, 63)
    return ((sh - lg) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_252d_base_v110_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_252d_base_v111_signal(roic, ebitdamargin, revenue, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_x_logrevenue_252d_base_v112_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    return (g * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_volgrowth_252d_base_v113_signal(roic, fcf, revenue, volume, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    vg = volume.pct_change(252)
    return (g * vg * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_volgrowth_252d_base_v114_signal(roic, ebitdamargin, volume, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    vg = volume.pct_change(252)
    return (g * vg * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxebitda_252d_base_v115_signal(roic, fcf, revenue, ebitda, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.log(ebitda.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexebitda_252d_base_v116_signal(roic, ebitdamargin, ebitda, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * np.log(ebitda.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxfcf_252d_base_v117_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.log(fcf.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_skew_504d_base_v118_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return (g.rolling(504, min_periods=126).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_skew_504d_base_v119_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return (g.rolling(504, min_periods=126).skew() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_kurt_504d_base_v120_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return (g.rolling(504, min_periods=126).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_kurt_252d_base_v121_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return (g.rolling(252, min_periods=63).kurt() * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxprice_504d_base_v122_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504)
    return (g * closeadj * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexprice_504d_base_v123_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504)
    return (g * closeadj * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_chg_252d_base_v124_signal(fcf, revenue, roic, closeadj):
    base = _f50_terminal_quality(fcf, revenue, roic, 252)
    inner = (fcf / revenue.replace(0, np.nan).abs()) * roic
    return ((base + (inner - inner.shift(252))) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_log_504d_base_v125_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504)
    return (np.sign(g) * np.log1p(g.abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_log_504d_base_v126_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504)
    return (np.sign(g) * np.log1p(g.abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_voladj_63d_base_v127_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    vol = _std(revenue.pct_change(), 63)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_voladj_63d_base_v128_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    vol = _std((roic * ebitdamargin).pct_change(), 63)
    return (g / vol.replace(0, np.nan) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_med_504d_base_v129_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 504)
    med = g.rolling(504, min_periods=126).median()
    return ((g - med) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_med_504d_base_v130_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 504)
    med = g.rolling(504, min_periods=126).median()
    return ((g - med) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_max_504d_base_v131_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    return ((g.rolling(504, min_periods=126).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_max_504d_base_v132_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 21)
    return ((g.rolling(504, min_periods=126).max() + g * 0.1) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_range_504d_base_v133_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 21)
    rng = g.rolling(504, min_periods=126).max() - g.rolling(504, min_periods=126).min()
    return (rng * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_ema_21d_base_v134_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_ema_21d_base_v135_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_ema_21d_base_v136_signal(fcf, revenue, roic, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj * 1e-4
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcompxprice_log_252d_base_v137_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj * 1.5).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscorexprice_log_252d_base_v138_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj * 1.5).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_minus_const_252d_base_v139_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return ((g - 0.2) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_minus_const_252d_base_v140_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return ((g - 0.025) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_minus_smoothed_252d_base_v141_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    sm = _mean(g, 252)
    return ((g - sm) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_minus_smoothed_252d_base_v142_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    sm = _mean(g, 252)
    return ((g - sm) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_sotp_x_252d_base_v143_signal(roic, fcf, revenue, ebitda, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    return (g * (revenue / ebitda.replace(0, np.nan).abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_sotp_x_252d_base_v144_signal(roic, ebitdamargin, revenue, ebitda, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 252)
    return (g * (revenue / ebitda.replace(0, np.nan).abs()) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_tquality_sotp_x_252d_base_v145_signal(fcf, revenue, roic, ebitda, closeadj):
    g = _f50_terminal_quality(fcf, revenue, roic, 252)
    return (g * (revenue / ebitda.replace(0, np.nan).abs()) * closeadj * 1e-4).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_long_ema_504d_base_v146_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 63)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_cscore_long_ema_504d_base_v147_signal(roic, ebitdamargin, closeadj):
    g = _f50_compounder_score(roic, ebitdamargin, 63)
    base = g.ewm(span=504, adjust=False).mean() * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_qcomp_negativity_252d_base_v148_signal(roic, fcf, revenue, closeadj):
    g = _f50_quality_composite(roic, fcf, revenue, 252)
    med = g.rolling(252, min_periods=63).median()
    neg = (g < med).astype(float)
    return ((neg * g + g * 0.5) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_full_composite_504d_base_v149_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 504)
    b = _f50_compounder_score(roic, ebitdamargin, 504)
    c = _f50_terminal_quality(fcf, revenue, roic, 504)
    return ((a + b + c * 1e-4) * closeadj).replace([np.inf, -np.inf], np.nan)


def f50itc_f50_industrial_terminal_compounder_terminal_value_proxy_252d_base_v150_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    a = _f50_quality_composite(roic, fcf, revenue, 252)
    b = _f50_compounder_score(roic, ebitdamargin, 252)
    return (a * b * closeadj * 10.0).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50itc_f50_industrial_terminal_compounder_qcomp_lograw_252d_base_v076_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_lograw_252d_base_v077_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_lograw_252d_base_v078_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_med_252d_base_v079_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_med_252d_base_v080_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_lo_252d_base_v081_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_lo_252d_base_v082_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_event_hi_252d_base_v083_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_event_lo_252d_base_v084_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_min_63d_base_v085_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_max_252d_base_v086_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_min_63d_base_v087_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_max_252d_base_v088_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_range_252d_base_v089_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_range_252d_base_v090_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_revgrowth_252d_base_v091_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_revgrowth_252d_base_v092_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_x_revgrowth_252d_base_v093_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxsqrtprice_252d_base_v094_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexsqrtprice_252d_base_v095_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_chg_252d_base_v096_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_chg_252d_base_v097_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_voladj_252d_base_v098_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_voladj_252d_base_v099_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_trend_252d_base_v100_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_trend_252d_base_v101_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_trend_252d_base_v102_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxvol_dv_252d_base_v103_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexvol_dv_252d_base_v104_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_diff_252m504_base_v105_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_diff_252m504_base_v106_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_diff_252m504_base_v107_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_diff_21m63_base_v108_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_diff_21m63_base_v109_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_x_logrevenue_252d_base_v110_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_x_logrevenue_252d_base_v111_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_x_logrevenue_252d_base_v112_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_volgrowth_252d_base_v113_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_volgrowth_252d_base_v114_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxebitda_252d_base_v115_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexebitda_252d_base_v116_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxfcf_252d_base_v117_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_skew_504d_base_v118_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_skew_504d_base_v119_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_kurt_504d_base_v120_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_kurt_252d_base_v121_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxprice_504d_base_v122_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexprice_504d_base_v123_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_chg_252d_base_v124_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_log_504d_base_v125_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_log_504d_base_v126_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_voladj_63d_base_v127_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_voladj_63d_base_v128_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_med_504d_base_v129_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_med_504d_base_v130_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_max_504d_base_v131_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_max_504d_base_v132_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_range_504d_base_v133_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_ema_21d_base_v134_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_ema_21d_base_v135_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_ema_21d_base_v136_signal,
    f50itc_f50_industrial_terminal_compounder_qcompxprice_log_252d_base_v137_signal,
    f50itc_f50_industrial_terminal_compounder_cscorexprice_log_252d_base_v138_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_minus_const_252d_base_v139_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_minus_const_252d_base_v140_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_minus_smoothed_252d_base_v141_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_minus_smoothed_252d_base_v142_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_sotp_x_252d_base_v143_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_sotp_x_252d_base_v144_signal,
    f50itc_f50_industrial_terminal_compounder_tquality_sotp_x_252d_base_v145_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_long_ema_504d_base_v146_signal,
    f50itc_f50_industrial_terminal_compounder_cscore_long_ema_504d_base_v147_signal,
    f50itc_f50_industrial_terminal_compounder_qcomp_negativity_252d_base_v148_signal,
    f50itc_f50_industrial_terminal_compounder_full_composite_504d_base_v149_signal,
    f50itc_f50_industrial_terminal_compounder_terminal_value_proxy_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_INDUSTRIAL_TERMINAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf,
        "roic": roic, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_compounder_score", "_f50_terminal_quality")
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
    print(f"OK f50_industrial_terminal_compounder_base_076_150_claude: {n_features} features pass")
