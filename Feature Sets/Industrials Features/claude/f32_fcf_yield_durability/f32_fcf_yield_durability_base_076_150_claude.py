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
def _f32_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f32_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f32_fcf_compound_quality(fcf, marketcap, w):
    y = fcf / marketcap.replace(0, np.nan)
    return _mean(y, w) - 0.5 * _std(y, w)


def f32fyd_f32_fcf_yield_durability_yield_5d_base_v076_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_10d_base_v077_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_42d_base_v078_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_189d_base_v079_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_378d_base_v080_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_5d_base_v081_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_10d_base_v082_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_42d_base_v083_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_189d_base_v084_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_378d_base_v085_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_5d_base_v086_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_10d_base_v087_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_42d_base_v088_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_189d_base_v089_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_378d_base_v090_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityema_63d_base_v091_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityema_252d_base_v092_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqema_63d_base_v093_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqema_252d_base_v094_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldperc_63d_base_v095_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldperc_252d_base_v096_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityperc_63d_base_v097_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityperc_252d_base_v098_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqperc_63d_base_v099_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqperc_252d_base_v100_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxvol_63d_base_v101_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxvol_252d_base_v102_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxmkt_63d_base_v103_signal(fcf, ev, marketcap, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 63) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxmkt_252d_base_v104_signal(fcf, ev, marketcap, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 252) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxmkt_63d_base_v105_signal(fcf, ev, marketcap, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxmkt_252d_base_v106_signal(fcf, ev, marketcap, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxmkt_63d_base_v107_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 63) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxmkt_252d_base_v108_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 252) * closeadj * np.log(marketcap.abs().replace(0, np.nan)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusprice_63d_base_v109_signal(fcf, ev, closeadj):
    base = _mean(_f32_fcf_yield(fcf, ev), 63)
    pret = closeadj.pct_change(63)
    result = (base - pret) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusprice_252d_base_v110_signal(fcf, ev, closeadj):
    base = _mean(_f32_fcf_yield(fcf, ev), 252)
    pret = closeadj.pct_change(252)
    result = (base - pret) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldquadratic_63d_base_v111_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 63) * closeadj + _std(base, 63) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldquadratic_252d_base_v112_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 252) * closeadj + _std(base, 252) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusstd_63d_base_v113_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 63) - _std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusstd_252d_base_v114_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 252) - _std(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusstd_504d_base_v115_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 504) - _std(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxprice_5d_base_v116_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 21) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxprice_504d_base_v117_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 504) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxsqprice_63d_base_v118_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxsqprice_252d_base_v119_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxsqprice_63d_base_v120_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxsqprice_252d_base_v121_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminus_fcfgrowth_63d_base_v122_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(63)
    result = (_mean(base, 63) + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminus_fcfgrowth_252d_base_v123_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(252)
    result = (_mean(base, 252) + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compositeq_63d_base_v124_signal(fcf, ev, marketcap, closeadj):
    a = _mean(_f32_fcf_yield(fcf, ev), 63)
    b = _f32_fcf_compound_quality(fcf, marketcap, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compositeq_252d_base_v125_signal(fcf, ev, marketcap, closeadj):
    a = _mean(_f32_fcf_yield(fcf, ev), 252)
    b = _f32_fcf_compound_quality(fcf, marketcap, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldebitda_63d_base_v126_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rng = base.rolling(63, min_periods=20).max() - base.rolling(63, min_periods=20).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldebitda_252d_base_v127_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldfwdcomp_63d_base_v128_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 21) + _mean(base, 63) + _mean(base, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldfwdcomp_252d_base_v129_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 63) + _mean(base, 252) + _mean(base, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxevg_63d_base_v130_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = ev.pct_change(63)
    result = _mean(base, 63) * closeadj * (1.0 + g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxevg_252d_base_v131_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = ev.pct_change(252)
    result = _mean(base, 252) * closeadj * (1.0 + g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddrawdown_63d_base_v132_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    peak = base.rolling(63, min_periods=20).max()
    dd = (base - peak) / peak.replace(0, np.nan).abs()
    result = dd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddrawdown_252d_base_v133_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    peak = base.rolling(252, min_periods=63).max()
    dd = (base - peak) / peak.replace(0, np.nan).abs()
    result = dd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddrawdown_504d_base_v134_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    peak = base.rolling(504, min_periods=126).max()
    dd = (base - peak) / peak.replace(0, np.nan).abs()
    result = dd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsymmrange_63d_base_v135_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rng = base.rolling(63, min_periods=20).quantile(0.9) - base.rolling(63, min_periods=20).quantile(0.1)
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsymmrange_252d_base_v136_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rng = base.rolling(252, min_periods=63).quantile(0.9) - base.rolling(252, min_periods=63).quantile(0.1)
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqsharpe_63d_base_v137_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = (_mean(base, 63) / _std(base, 63).replace(0, np.nan)) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqsharpe_252d_base_v138_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = (_mean(base, 252) / _std(base, 252).replace(0, np.nan)) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsharpe_63d_base_v139_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 63) / _std(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsharpe_252d_base_v140_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 252) / _std(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxinvprice_63d_base_v141_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 63) * closeadj * (1.0 / _mean(closeadj, 63).replace(0, np.nan)) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxinvprice_252d_base_v142_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 252) * closeadj * (1.0 / _mean(closeadj, 252).replace(0, np.nan)) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusvol_63d_base_v143_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    vol = _std(closeadj.pct_change(), 63)
    result = (_mean(base, 63) - vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusvol_252d_base_v144_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    vol = _std(closeadj.pct_change(), 252)
    result = (_mean(base, 252) - vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilitydeep_63d_base_v145_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 63)
    med = base.rolling(252, min_periods=63).median()
    deep = (base < med).astype(float)
    result = _mean(deep, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityhi_252d_base_v146_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 252)
    med = base.rolling(504, min_periods=126).median()
    hi = (base > med).astype(float)
    result = _mean(hi, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldslopeprod_63d_base_v147_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 63) * closeadj * np.sign(base - base.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldslopeprod_252d_base_v148_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 252) * closeadj * np.sign(base - base.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxabsprice_63d_base_v149_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * np.log(closeadj.replace(0, np.nan).abs()) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxabsprice_252d_base_v150_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * np.log(closeadj.replace(0, np.nan).abs()) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32fyd_f32_fcf_yield_durability_yield_5d_base_v076_signal,
    f32fyd_f32_fcf_yield_durability_yield_10d_base_v077_signal,
    f32fyd_f32_fcf_yield_durability_yield_42d_base_v078_signal,
    f32fyd_f32_fcf_yield_durability_yield_189d_base_v079_signal,
    f32fyd_f32_fcf_yield_durability_yield_378d_base_v080_signal,
    f32fyd_f32_fcf_yield_durability_stability_5d_base_v081_signal,
    f32fyd_f32_fcf_yield_durability_stability_10d_base_v082_signal,
    f32fyd_f32_fcf_yield_durability_stability_42d_base_v083_signal,
    f32fyd_f32_fcf_yield_durability_stability_189d_base_v084_signal,
    f32fyd_f32_fcf_yield_durability_stability_378d_base_v085_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_5d_base_v086_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_10d_base_v087_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_42d_base_v088_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_189d_base_v089_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_378d_base_v090_signal,
    f32fyd_f32_fcf_yield_durability_stabilityema_63d_base_v091_signal,
    f32fyd_f32_fcf_yield_durability_stabilityema_252d_base_v092_signal,
    f32fyd_f32_fcf_yield_durability_compoundqema_63d_base_v093_signal,
    f32fyd_f32_fcf_yield_durability_compoundqema_252d_base_v094_signal,
    f32fyd_f32_fcf_yield_durability_yieldperc_63d_base_v095_signal,
    f32fyd_f32_fcf_yield_durability_yieldperc_252d_base_v096_signal,
    f32fyd_f32_fcf_yield_durability_stabilityperc_63d_base_v097_signal,
    f32fyd_f32_fcf_yield_durability_stabilityperc_252d_base_v098_signal,
    f32fyd_f32_fcf_yield_durability_compoundqperc_63d_base_v099_signal,
    f32fyd_f32_fcf_yield_durability_compoundqperc_252d_base_v100_signal,
    f32fyd_f32_fcf_yield_durability_yieldxvol_63d_base_v101_signal,
    f32fyd_f32_fcf_yield_durability_yieldxvol_252d_base_v102_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxmkt_63d_base_v103_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxmkt_252d_base_v104_signal,
    f32fyd_f32_fcf_yield_durability_yieldxmkt_63d_base_v105_signal,
    f32fyd_f32_fcf_yield_durability_yieldxmkt_252d_base_v106_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxmkt_63d_base_v107_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxmkt_252d_base_v108_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusprice_63d_base_v109_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusprice_252d_base_v110_signal,
    f32fyd_f32_fcf_yield_durability_yieldquadratic_63d_base_v111_signal,
    f32fyd_f32_fcf_yield_durability_yieldquadratic_252d_base_v112_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusstd_63d_base_v113_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusstd_252d_base_v114_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusstd_504d_base_v115_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxprice_5d_base_v116_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxprice_504d_base_v117_signal,
    f32fyd_f32_fcf_yield_durability_yieldxsqprice_63d_base_v118_signal,
    f32fyd_f32_fcf_yield_durability_yieldxsqprice_252d_base_v119_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxsqprice_63d_base_v120_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxsqprice_252d_base_v121_signal,
    f32fyd_f32_fcf_yield_durability_yieldminus_fcfgrowth_63d_base_v122_signal,
    f32fyd_f32_fcf_yield_durability_yieldminus_fcfgrowth_252d_base_v123_signal,
    f32fyd_f32_fcf_yield_durability_compositeq_63d_base_v124_signal,
    f32fyd_f32_fcf_yield_durability_compositeq_252d_base_v125_signal,
    f32fyd_f32_fcf_yield_durability_yieldebitda_63d_base_v126_signal,
    f32fyd_f32_fcf_yield_durability_yieldebitda_252d_base_v127_signal,
    f32fyd_f32_fcf_yield_durability_yieldfwdcomp_63d_base_v128_signal,
    f32fyd_f32_fcf_yield_durability_yieldfwdcomp_252d_base_v129_signal,
    f32fyd_f32_fcf_yield_durability_yieldxevg_63d_base_v130_signal,
    f32fyd_f32_fcf_yield_durability_yieldxevg_252d_base_v131_signal,
    f32fyd_f32_fcf_yield_durability_yielddrawdown_63d_base_v132_signal,
    f32fyd_f32_fcf_yield_durability_yielddrawdown_252d_base_v133_signal,
    f32fyd_f32_fcf_yield_durability_yielddrawdown_504d_base_v134_signal,
    f32fyd_f32_fcf_yield_durability_yieldsymmrange_63d_base_v135_signal,
    f32fyd_f32_fcf_yield_durability_yieldsymmrange_252d_base_v136_signal,
    f32fyd_f32_fcf_yield_durability_compoundqsharpe_63d_base_v137_signal,
    f32fyd_f32_fcf_yield_durability_compoundqsharpe_252d_base_v138_signal,
    f32fyd_f32_fcf_yield_durability_yieldsharpe_63d_base_v139_signal,
    f32fyd_f32_fcf_yield_durability_yieldsharpe_252d_base_v140_signal,
    f32fyd_f32_fcf_yield_durability_yieldxinvprice_63d_base_v141_signal,
    f32fyd_f32_fcf_yield_durability_yieldxinvprice_252d_base_v142_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusvol_63d_base_v143_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusvol_252d_base_v144_signal,
    f32fyd_f32_fcf_yield_durability_stabilitydeep_63d_base_v145_signal,
    f32fyd_f32_fcf_yield_durability_stabilityhi_252d_base_v146_signal,
    f32fyd_f32_fcf_yield_durability_yieldslopeprod_63d_base_v147_signal,
    f32fyd_f32_fcf_yield_durability_yieldslopeprod_252d_base_v148_signal,
    f32fyd_f32_fcf_yield_durability_yieldxabsprice_63d_base_v149_signal,
    f32fyd_f32_fcf_yield_durability_yieldxabsprice_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_FCF_YIELD_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf      = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")

    cols = {
        "closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_fcf_yield", "_f32_fcf_yield_stability", "_f32_fcf_compound_quality")
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
    print(f"OK f32_fcf_yield_durability_base_076_150_claude: {n_features} features pass")
