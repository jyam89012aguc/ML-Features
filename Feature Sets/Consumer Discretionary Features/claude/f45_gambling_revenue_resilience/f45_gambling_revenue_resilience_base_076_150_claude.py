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


def _f45_revenue_smoothness(revenue, w):
    g = revenue.pct_change()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    m = g.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return m / sd.replace(0, np.nan)


def _f45_margin_stability(ebitdamargin, w):
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / sd.replace(0, np.nan)


def _f45_gaming_resilience_score(revenue, ebitda, w):
    g_rev = revenue.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    g_ebt = ebitda.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (g_rev.replace(0, np.nan) + g_ebt.replace(0, np.nan))


def f45grr_f45_gambling_revenue_resilience_grema_504d_base_v076_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 504)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_21d_base_v077_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_42d_base_v078_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_63d_base_v079_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_126d_base_v080_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_189d_base_v081_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_252d_base_v082_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_378d_base_v083_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grz_504d_base_v084_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxvol_21d_base_v085_signal(revenue, volume):
    s = _f45_revenue_smoothness(revenue, 21)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxvol_63d_base_v086_signal(revenue, volume):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxvol_252d_base_v087_signal(revenue, volume):
    s = _f45_revenue_smoothness(revenue, 252)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxvol_21d_base_v088_signal(ebitdamargin, volume):
    s = _f45_margin_stability(ebitdamargin, 21)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxvol_63d_base_v089_signal(ebitdamargin, volume):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxvol_252d_base_v090_signal(ebitdamargin, volume):
    s = _f45_margin_stability(ebitdamargin, 252)
    result = s * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grxvol_21d_base_v091_signal(revenue, ebitda, volume):
    r = _f45_gaming_resilience_score(revenue, ebitda, 21)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grxvol_63d_base_v092_signal(revenue, ebitda, volume):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grxvol_252d_base_v093_signal(revenue, ebitda, volume):
    r = _f45_gaming_resilience_score(revenue, ebitda, 252)
    result = r * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsdiff_21m63_base_v094_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 21)
    b = _f45_revenue_smoothness(revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsdiff_63m252_base_v095_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 63)
    b = _f45_revenue_smoothness(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsdiff_252m504_base_v096_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 252)
    b = _f45_revenue_smoothness(revenue, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msdiff_21m63_base_v097_signal(ebitdamargin, closeadj):
    a = _f45_margin_stability(ebitdamargin, 21)
    b = _f45_margin_stability(ebitdamargin, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msdiff_63m252_base_v098_signal(ebitdamargin, closeadj):
    a = _f45_margin_stability(ebitdamargin, 63)
    b = _f45_margin_stability(ebitdamargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msdiff_252m504_base_v099_signal(ebitdamargin, closeadj):
    a = _f45_margin_stability(ebitdamargin, 252)
    b = _f45_margin_stability(ebitdamargin, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grdiff_21m63_base_v100_signal(revenue, ebitda, closeadj):
    a = _f45_gaming_resilience_score(revenue, ebitda, 21)
    b = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grdiff_63m252_base_v101_signal(revenue, ebitda, closeadj):
    a = _f45_gaming_resilience_score(revenue, ebitda, 63)
    b = _f45_gaming_resilience_score(revenue, ebitda, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grdiff_252m504_base_v102_signal(revenue, ebitda, closeadj):
    a = _f45_gaming_resilience_score(revenue, ebitda, 252)
    b = _f45_gaming_resilience_score(revenue, ebitda, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrat_63v252_base_v103_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 63)
    b = _f45_revenue_smoothness(revenue, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrat_21v63_base_v104_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 21)
    b = _f45_revenue_smoothness(revenue, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrat_252v504_base_v105_signal(revenue, closeadj):
    a = _f45_revenue_smoothness(revenue, 252)
    b = _f45_revenue_smoothness(revenue, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grrat_63v252_base_v106_signal(revenue, ebitda, closeadj):
    a = _f45_gaming_resilience_score(revenue, ebitda, 63)
    b = _f45_gaming_resilience_score(revenue, ebitda, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grrat_21v63_base_v107_signal(revenue, ebitda, closeadj):
    a = _f45_gaming_resilience_score(revenue, ebitda, 21)
    b = _f45_gaming_resilience_score(revenue, ebitda, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rslog_63d_base_v108_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63).abs().replace(0, np.nan)
    result = np.log(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rslog_252d_base_v109_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252).abs().replace(0, np.nan)
    result = np.log(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grlog_63d_base_v110_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63).abs().replace(0, np.nan)
    result = np.log(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grlog_252d_base_v111_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 252).abs().replace(0, np.nan)
    result = np.log(r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsstd_63d_base_v112_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _std(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsstd_252d_base_v113_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _std(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_comp_63d_base_v114_signal(revenue, ebitda, ebitdamargin, closeadj):
    rs = _f45_revenue_smoothness(revenue, 63)
    ms = _f45_margin_stability(ebitdamargin, 63)
    result = (rs + ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_comp_252d_base_v115_signal(revenue, ebitda, ebitdamargin, closeadj):
    rs = _f45_revenue_smoothness(revenue, 252)
    ms = _f45_margin_stability(ebitdamargin, 252)
    result = (rs + ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_comp_504d_base_v116_signal(revenue, ebitda, ebitdamargin, closeadj):
    rs = _f45_revenue_smoothness(revenue, 504)
    ms = _f45_margin_stability(ebitdamargin, 504)
    result = (rs + ms) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rssq_63d_base_v117_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    m = _mean(s, 63)
    result = ((s - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rssq_252d_base_v118_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    m = _mean(s, 252)
    result = ((s - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rssmooth_63o21_base_v119_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rssmooth_252o63_base_v120_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rssmooth_504o126_base_v121_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 504)
    result = _mean(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_mssmooth_63o21_base_v122_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_mssmooth_252o63_base_v123_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 252)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_mssmooth_504o126_base_v124_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 504)
    result = _mean(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxdv_21d_base_v125_signal(revenue, closeadj, volume):
    s = _f45_revenue_smoothness(revenue, 21)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxdv_63d_base_v126_signal(revenue, closeadj, volume):
    s = _f45_revenue_smoothness(revenue, 63)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsxdv_252d_base_v127_signal(revenue, closeadj, volume):
    s = _f45_revenue_smoothness(revenue, 252)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxdv_21d_base_v128_signal(ebitdamargin, closeadj, volume):
    s = _f45_margin_stability(ebitdamargin, 21)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxdv_63d_base_v129_signal(ebitdamargin, closeadj, volume):
    s = _f45_margin_stability(ebitdamargin, 63)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msxdv_252d_base_v130_signal(ebitdamargin, closeadj, volume):
    s = _f45_margin_stability(ebitdamargin, 252)
    dv = closeadj * volume
    result = s * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrank_63d_base_v131_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrank_126d_base_v132_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrank_252d_base_v133_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsrank_504d_base_v134_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = s.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msrank_63d_base_v135_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msrank_252d_base_v136_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = s.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msrank_504d_base_v137_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = s.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grrank_63d_base_v138_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = r.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grrank_252d_base_v139_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = r.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_grrank_504d_base_v140_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = r.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsemadiff_21m63_base_v141_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = (_ema(s, 21) - _ema(s, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsemadiff_63m252_base_v142_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = (_ema(s, 63) - _ema(s, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsemadiff_126m252_base_v143_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    result = (_ema(s, 126) - _ema(s, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msemadiff_21m63_base_v144_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = (_ema(s, 21) - _ema(s, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msemadiff_63m252_base_v145_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    result = (_ema(s, 63) - _ema(s, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gremadiff_21m63_base_v146_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = (_ema(r, 21) - _ema(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_gremadiff_63m252_base_v147_signal(revenue, ebitda, closeadj):
    r = _f45_gaming_resilience_score(revenue, ebitda, 63)
    result = (_ema(r, 63) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsminmax_63d_base_v148_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 63)
    hi = s.rolling(63, min_periods=max(1, 63//2)).max()
    lo = s.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((s - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_rsminmax_252d_base_v149_signal(revenue, closeadj):
    s = _f45_revenue_smoothness(revenue, 252)
    hi = s.rolling(252, min_periods=max(1, 252//2)).max()
    lo = s.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((s - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f45grr_f45_gambling_revenue_resilience_msminmax_63d_base_v150_signal(ebitdamargin, closeadj):
    s = _f45_margin_stability(ebitdamargin, 63)
    hi = s.rolling(63, min_periods=max(1, 63//2)).max()
    lo = s.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((s - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45grr_f45_gambling_revenue_resilience_grema_504d_base_v076_signal,
    f45grr_f45_gambling_revenue_resilience_grz_21d_base_v077_signal,
    f45grr_f45_gambling_revenue_resilience_grz_42d_base_v078_signal,
    f45grr_f45_gambling_revenue_resilience_grz_63d_base_v079_signal,
    f45grr_f45_gambling_revenue_resilience_grz_126d_base_v080_signal,
    f45grr_f45_gambling_revenue_resilience_grz_189d_base_v081_signal,
    f45grr_f45_gambling_revenue_resilience_grz_252d_base_v082_signal,
    f45grr_f45_gambling_revenue_resilience_grz_378d_base_v083_signal,
    f45grr_f45_gambling_revenue_resilience_grz_504d_base_v084_signal,
    f45grr_f45_gambling_revenue_resilience_rsxvol_21d_base_v085_signal,
    f45grr_f45_gambling_revenue_resilience_rsxvol_63d_base_v086_signal,
    f45grr_f45_gambling_revenue_resilience_rsxvol_252d_base_v087_signal,
    f45grr_f45_gambling_revenue_resilience_msxvol_21d_base_v088_signal,
    f45grr_f45_gambling_revenue_resilience_msxvol_63d_base_v089_signal,
    f45grr_f45_gambling_revenue_resilience_msxvol_252d_base_v090_signal,
    f45grr_f45_gambling_revenue_resilience_grxvol_21d_base_v091_signal,
    f45grr_f45_gambling_revenue_resilience_grxvol_63d_base_v092_signal,
    f45grr_f45_gambling_revenue_resilience_grxvol_252d_base_v093_signal,
    f45grr_f45_gambling_revenue_resilience_rsdiff_21m63_base_v094_signal,
    f45grr_f45_gambling_revenue_resilience_rsdiff_63m252_base_v095_signal,
    f45grr_f45_gambling_revenue_resilience_rsdiff_252m504_base_v096_signal,
    f45grr_f45_gambling_revenue_resilience_msdiff_21m63_base_v097_signal,
    f45grr_f45_gambling_revenue_resilience_msdiff_63m252_base_v098_signal,
    f45grr_f45_gambling_revenue_resilience_msdiff_252m504_base_v099_signal,
    f45grr_f45_gambling_revenue_resilience_grdiff_21m63_base_v100_signal,
    f45grr_f45_gambling_revenue_resilience_grdiff_63m252_base_v101_signal,
    f45grr_f45_gambling_revenue_resilience_grdiff_252m504_base_v102_signal,
    f45grr_f45_gambling_revenue_resilience_rsrat_63v252_base_v103_signal,
    f45grr_f45_gambling_revenue_resilience_rsrat_21v63_base_v104_signal,
    f45grr_f45_gambling_revenue_resilience_rsrat_252v504_base_v105_signal,
    f45grr_f45_gambling_revenue_resilience_grrat_63v252_base_v106_signal,
    f45grr_f45_gambling_revenue_resilience_grrat_21v63_base_v107_signal,
    f45grr_f45_gambling_revenue_resilience_rslog_63d_base_v108_signal,
    f45grr_f45_gambling_revenue_resilience_rslog_252d_base_v109_signal,
    f45grr_f45_gambling_revenue_resilience_grlog_63d_base_v110_signal,
    f45grr_f45_gambling_revenue_resilience_grlog_252d_base_v111_signal,
    f45grr_f45_gambling_revenue_resilience_rsstd_63d_base_v112_signal,
    f45grr_f45_gambling_revenue_resilience_rsstd_252d_base_v113_signal,
    f45grr_f45_gambling_revenue_resilience_comp_63d_base_v114_signal,
    f45grr_f45_gambling_revenue_resilience_comp_252d_base_v115_signal,
    f45grr_f45_gambling_revenue_resilience_comp_504d_base_v116_signal,
    f45grr_f45_gambling_revenue_resilience_rssq_63d_base_v117_signal,
    f45grr_f45_gambling_revenue_resilience_rssq_252d_base_v118_signal,
    f45grr_f45_gambling_revenue_resilience_rssmooth_63o21_base_v119_signal,
    f45grr_f45_gambling_revenue_resilience_rssmooth_252o63_base_v120_signal,
    f45grr_f45_gambling_revenue_resilience_rssmooth_504o126_base_v121_signal,
    f45grr_f45_gambling_revenue_resilience_mssmooth_63o21_base_v122_signal,
    f45grr_f45_gambling_revenue_resilience_mssmooth_252o63_base_v123_signal,
    f45grr_f45_gambling_revenue_resilience_mssmooth_504o126_base_v124_signal,
    f45grr_f45_gambling_revenue_resilience_rsxdv_21d_base_v125_signal,
    f45grr_f45_gambling_revenue_resilience_rsxdv_63d_base_v126_signal,
    f45grr_f45_gambling_revenue_resilience_rsxdv_252d_base_v127_signal,
    f45grr_f45_gambling_revenue_resilience_msxdv_21d_base_v128_signal,
    f45grr_f45_gambling_revenue_resilience_msxdv_63d_base_v129_signal,
    f45grr_f45_gambling_revenue_resilience_msxdv_252d_base_v130_signal,
    f45grr_f45_gambling_revenue_resilience_rsrank_63d_base_v131_signal,
    f45grr_f45_gambling_revenue_resilience_rsrank_126d_base_v132_signal,
    f45grr_f45_gambling_revenue_resilience_rsrank_252d_base_v133_signal,
    f45grr_f45_gambling_revenue_resilience_rsrank_504d_base_v134_signal,
    f45grr_f45_gambling_revenue_resilience_msrank_63d_base_v135_signal,
    f45grr_f45_gambling_revenue_resilience_msrank_252d_base_v136_signal,
    f45grr_f45_gambling_revenue_resilience_msrank_504d_base_v137_signal,
    f45grr_f45_gambling_revenue_resilience_grrank_63d_base_v138_signal,
    f45grr_f45_gambling_revenue_resilience_grrank_252d_base_v139_signal,
    f45grr_f45_gambling_revenue_resilience_grrank_504d_base_v140_signal,
    f45grr_f45_gambling_revenue_resilience_rsemadiff_21m63_base_v141_signal,
    f45grr_f45_gambling_revenue_resilience_rsemadiff_63m252_base_v142_signal,
    f45grr_f45_gambling_revenue_resilience_rsemadiff_126m252_base_v143_signal,
    f45grr_f45_gambling_revenue_resilience_msemadiff_21m63_base_v144_signal,
    f45grr_f45_gambling_revenue_resilience_msemadiff_63m252_base_v145_signal,
    f45grr_f45_gambling_revenue_resilience_gremadiff_21m63_base_v146_signal,
    f45grr_f45_gambling_revenue_resilience_gremadiff_63m252_base_v147_signal,
    f45grr_f45_gambling_revenue_resilience_rsminmax_63d_base_v148_signal,
    f45grr_f45_gambling_revenue_resilience_rsminmax_252d_base_v149_signal,
    f45grr_f45_gambling_revenue_resilience_msminmax_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_GAMBLING_REVENUE_RESILIENCE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f45_revenue_smoothness", "_f45_margin_stability", "_f45_gaming_resilience_score")
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
    print(f"OK gambling_revenue_resilience_base_076_150_claude: {n_features} features pass")
