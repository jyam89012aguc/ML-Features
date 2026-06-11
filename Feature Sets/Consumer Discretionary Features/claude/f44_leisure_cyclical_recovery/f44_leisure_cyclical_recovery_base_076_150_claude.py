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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f44_revenue_recovery(revenue, w):
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - trough) / trough.replace(0, np.nan).abs()


def _f44_margin_recovery(ebitdamargin, w):
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f44_recovery_strength(revenue, ebitda, w):
    rev_t = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    ebt_t = ebitda.rolling(w, min_periods=max(1, w // 2)).min()
    return ((revenue - rev_t) / rev_t.replace(0, np.nan).abs()
            + (ebitda - ebt_t) / ebt_t.replace(0, np.nan).abs())


def f44lcr_f44_leisure_cyclical_recovery_mrecz_504d_base_v076_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_21d_base_v077_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_42d_base_v078_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_63d_base_v079_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_126d_base_v080_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_189d_base_v081_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_252d_base_v082_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_378d_base_v083_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrz_504d_base_v084_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecxvol_21d_base_v085_signal(revenue, volume):
    r = _f44_revenue_recovery(revenue, 21)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecxvol_63d_base_v086_signal(revenue, volume):
    r = _f44_revenue_recovery(revenue, 63)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecxvol_252d_base_v087_signal(revenue, volume):
    r = _f44_revenue_recovery(revenue, 252)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecxvol_21d_base_v088_signal(ebitdamargin, volume):
    m = _f44_margin_recovery(ebitdamargin, 21)
    result = m * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecxvol_63d_base_v089_signal(ebitdamargin, volume):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = m * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecxvol_252d_base_v090_signal(ebitdamargin, volume):
    m = _f44_margin_recovery(ebitdamargin, 252)
    result = m * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrxvol_21d_base_v091_signal(revenue, ebitda, volume):
    r = _f44_recovery_strength(revenue, ebitda, 21)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrxvol_63d_base_v092_signal(revenue, ebitda, volume):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrxvol_252d_base_v093_signal(revenue, ebitda, volume):
    r = _f44_recovery_strength(revenue, ebitda, 252)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecdiff_21m63_base_v094_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 21)
    l = _f44_revenue_recovery(revenue, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecdiff_63m252_base_v095_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 63)
    l = _f44_revenue_recovery(revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecdiff_252m504_base_v096_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 252)
    l = _f44_revenue_recovery(revenue, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecdiff_126m252_base_v097_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 126)
    l = _f44_revenue_recovery(revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecdiff_21m63_base_v098_signal(ebitdamargin, closeadj):
    s = _f44_margin_recovery(ebitdamargin, 21)
    l = _f44_margin_recovery(ebitdamargin, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecdiff_63m252_base_v099_signal(ebitdamargin, closeadj):
    s = _f44_margin_recovery(ebitdamargin, 63)
    l = _f44_margin_recovery(ebitdamargin, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecdiff_252m504_base_v100_signal(ebitdamargin, closeadj):
    s = _f44_margin_recovery(ebitdamargin, 252)
    l = _f44_margin_recovery(ebitdamargin, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrdiff_21m63_base_v101_signal(revenue, ebitda, closeadj):
    s = _f44_recovery_strength(revenue, ebitda, 21)
    l = _f44_recovery_strength(revenue, ebitda, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrdiff_63m252_base_v102_signal(revenue, ebitda, closeadj):
    s = _f44_recovery_strength(revenue, ebitda, 63)
    l = _f44_recovery_strength(revenue, ebitda, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrdiff_252m504_base_v103_signal(revenue, ebitda, closeadj):
    s = _f44_recovery_strength(revenue, ebitda, 252)
    l = _f44_recovery_strength(revenue, ebitda, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrat_63v252_base_v104_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 63)
    l = _f44_revenue_recovery(revenue, 252).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrat_21v63_base_v105_signal(revenue, closeadj):
    s = _f44_revenue_recovery(revenue, 21)
    l = _f44_revenue_recovery(revenue, 63).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrrat_63v252_base_v106_signal(revenue, ebitda, closeadj):
    s = _f44_recovery_strength(revenue, ebitda, 63)
    l = _f44_recovery_strength(revenue, ebitda, 252).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrrat_21v63_base_v107_signal(revenue, ebitda, closeadj):
    s = _f44_recovery_strength(revenue, ebitda, 21)
    l = _f44_recovery_strength(revenue, ebitda, 63).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecstd_63d_base_v108_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _std(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecstd_252d_base_v109_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecstd_504d_base_v110_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    result = _std(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecstd_63d_base_v111_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _std(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecstd_252d_base_v112_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    result = _std(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecstd_504d_base_v113_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    result = _std(m, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_63o21_base_v114_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _mean(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_252o63_base_v115_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    result = _mean(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_504o126_base_v116_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    result = _mean(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_63o21_base_v117_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _mean(m, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_252o63_base_v118_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    result = _mean(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_504o126_base_v119_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    result = _mean(m, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_reccomp_63d_base_v120_signal(revenue, ebitda, ebitdamargin, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = (r + m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_reccomp_252d_base_v121_signal(revenue, ebitda, ebitdamargin, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    m = _f44_margin_recovery(ebitdamargin, 252)
    result = (r + m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_reccomp_504d_base_v122_signal(revenue, ebitda, ebitdamargin, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    m = _f44_margin_recovery(ebitdamargin, 504)
    result = (r + m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecsq_63d_base_v123_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecsq_252d_base_v124_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrlog_63d_base_v125_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63).abs().replace(0, np.nan)
    result = np.log(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrlog_252d_base_v126_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 252).abs().replace(0, np.nan)
    result = np.log(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrank_63d_base_v127_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = r.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrank_126d_base_v128_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = r.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrank_252d_base_v129_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = r.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecrank_504d_base_v130_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = r.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecrank_63d_base_v131_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = m.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecrank_252d_base_v132_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = m.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecrank_504d_base_v133_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = m.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrrank_63d_base_v134_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = r.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrrank_252d_base_v135_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = r.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrrank_504d_base_v136_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = r.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_21m63_base_v137_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = (_ema(r, 21) - _ema(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_63m252_base_v138_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = (_ema(r, 63) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_126m252_base_v139_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = (_ema(r, 126) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecemadiff_21m63_base_v140_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = (_ema(m, 21) - _ema(m, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecemadiff_63m252_base_v141_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = (_ema(m, 63) - _ema(m, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstremadiff_21m63_base_v142_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = (_ema(r, 21) - _ema(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstremadiff_63m252_base_v143_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = (_ema(r, 63) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecminmax_63d_base_v144_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    hi = r.rolling(63, min_periods=max(1, 63//2)).max()
    lo = r.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecminmax_252d_base_v145_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    hi = r.rolling(252, min_periods=max(1, 252//2)).max()
    lo = r.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecminmax_63d_base_v146_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    hi = m.rolling(63, min_periods=max(1, 63//2)).max()
    lo = m.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((m - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecminmax_252d_base_v147_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    hi = m.rolling(252, min_periods=max(1, 252//2)).max()
    lo = m.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((m - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrminmax_63d_base_v148_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    hi = r.rolling(63, min_periods=max(1, 63//2)).max()
    lo = r.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrminmax_252d_base_v149_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 252)
    hi = r.rolling(252, min_periods=max(1, 252//2)).max()
    lo = r.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecxdv_21d_base_v150_signal(revenue, closeadj, volume):
    r = _f44_revenue_recovery(revenue, 21)
    dv = closeadj * volume
    result = r * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44lcr_f44_leisure_cyclical_recovery_mrecz_504d_base_v076_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_21d_base_v077_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_42d_base_v078_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_63d_base_v079_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_126d_base_v080_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_189d_base_v081_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_252d_base_v082_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_378d_base_v083_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrz_504d_base_v084_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecxvol_21d_base_v085_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecxvol_63d_base_v086_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecxvol_252d_base_v087_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecxvol_21d_base_v088_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecxvol_63d_base_v089_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecxvol_252d_base_v090_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrxvol_21d_base_v091_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrxvol_63d_base_v092_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrxvol_252d_base_v093_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecdiff_21m63_base_v094_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecdiff_63m252_base_v095_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecdiff_252m504_base_v096_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecdiff_126m252_base_v097_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecdiff_21m63_base_v098_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecdiff_63m252_base_v099_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecdiff_252m504_base_v100_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrdiff_21m63_base_v101_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrdiff_63m252_base_v102_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrdiff_252m504_base_v103_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrat_63v252_base_v104_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrat_21v63_base_v105_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrrat_63v252_base_v106_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrrat_21v63_base_v107_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecstd_63d_base_v108_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecstd_252d_base_v109_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecstd_504d_base_v110_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecstd_63d_base_v111_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecstd_252d_base_v112_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecstd_504d_base_v113_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_63o21_base_v114_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_252o63_base_v115_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecsmooth_504o126_base_v116_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_63o21_base_v117_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_252o63_base_v118_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecsmooth_504o126_base_v119_signal,
    f44lcr_f44_leisure_cyclical_recovery_reccomp_63d_base_v120_signal,
    f44lcr_f44_leisure_cyclical_recovery_reccomp_252d_base_v121_signal,
    f44lcr_f44_leisure_cyclical_recovery_reccomp_504d_base_v122_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecsq_63d_base_v123_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecsq_252d_base_v124_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrlog_63d_base_v125_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrlog_252d_base_v126_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrank_63d_base_v127_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrank_126d_base_v128_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrank_252d_base_v129_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecrank_504d_base_v130_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecrank_63d_base_v131_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecrank_252d_base_v132_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecrank_504d_base_v133_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrrank_63d_base_v134_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrrank_252d_base_v135_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrrank_504d_base_v136_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_21m63_base_v137_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_63m252_base_v138_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecemadiff_126m252_base_v139_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecemadiff_21m63_base_v140_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecemadiff_63m252_base_v141_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstremadiff_21m63_base_v142_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstremadiff_63m252_base_v143_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecminmax_63d_base_v144_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecminmax_252d_base_v145_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecminmax_63d_base_v146_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecminmax_252d_base_v147_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrminmax_63d_base_v148_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrminmax_252d_base_v149_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecxdv_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_LEISURE_CYCLICAL_RECOVERY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ebitda": ebitda, "ebitdamargin": ebitdamargin }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f44_revenue_recovery", "_f44_margin_recovery", "_f44_recovery_strength")
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
    print(f"OK leisure_cyclical_recovery_base_076_150_claude: {n_features} features pass")
