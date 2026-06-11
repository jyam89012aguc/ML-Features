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


def _f43_revenue_vol(revenue, w):
    g = revenue.pct_change()
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f43_revenue_drawdown(revenue, w):
    peak = revenue.rolling(w, min_periods=max(1, w // 2)).max()
    return (revenue - peak) / peak.replace(0, np.nan).abs()


def _f43_demand_cycle_score(revenue, ebitda, w):
    r = ebitda / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f43ldc_f43_lodging_demand_cycle_rddxvol_252d_base_v076_signal(revenue, volume):
    d = _f43_revenue_drawdown(revenue, 252)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsxvol_21d_base_v077_signal(revenue, ebitda, volume):
    d = _f43_demand_cycle_score(revenue, ebitda, 21)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsxvol_63d_base_v078_signal(revenue, ebitda, volume):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsxvol_252d_base_v079_signal(revenue, ebitda, volume):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = d * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvoldiff_21m63_base_v080_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 21)
    l = _f43_revenue_vol(revenue, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvoldiff_63m252_base_v081_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 63)
    l = _f43_revenue_vol(revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvoldiff_252m504_base_v082_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 252)
    l = _f43_revenue_vol(revenue, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrat_63v252_base_v083_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 63)
    l = _f43_revenue_vol(revenue, 252).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrat_21v63_base_v084_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 21)
    l = _f43_revenue_vol(revenue, 63).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrat_252v504_base_v085_signal(revenue, closeadj):
    s = _f43_revenue_vol(revenue, 252)
    l = _f43_revenue_vol(revenue, 504).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrat_63v252_base_v086_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 63)
    l = _f43_revenue_drawdown(revenue, 252).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrat_21v63_base_v087_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 21)
    l = _f43_revenue_drawdown(revenue, 63).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrat_252v504_base_v088_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 252)
    l = _f43_revenue_drawdown(revenue, 504).replace(0, np.nan).abs()
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdddiff_21m63_base_v089_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 21)
    l = _f43_revenue_drawdown(revenue, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdddiff_63m252_base_v090_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 63)
    l = _f43_revenue_drawdown(revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdddiff_252m504_base_v091_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 252)
    l = _f43_revenue_drawdown(revenue, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rdddiff_126m252_base_v092_signal(revenue, closeadj):
    s = _f43_revenue_drawdown(revenue, 126)
    l = _f43_revenue_drawdown(revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsdiff_21m63_base_v093_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 21)
    l = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsdiff_63m252_base_v094_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 63)
    l = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsdiff_252m504_base_v095_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 252)
    l = _f43_demand_cycle_score(revenue, ebitda, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsdiff_126m252_base_v096_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 126)
    l = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrat_63v252_base_v097_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 63)
    l = _f43_demand_cycle_score(revenue, ebitda, 252).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrat_21v63_base_v098_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 21)
    l = _f43_demand_cycle_score(revenue, ebitda, 63).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrat_252v504_base_v099_signal(revenue, ebitda, closeadj):
    s = _f43_demand_cycle_score(revenue, ebitda, 252)
    l = _f43_demand_cycle_score(revenue, ebitda, 504).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolstd_63d_base_v100_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _std(v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolstd_252d_base_v101_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = _std(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsstd_63d_base_v102_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsstd_252d_base_v103_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsstd_504d_base_v104_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 504)
    result = _std(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_cyclecomp_63d_base_v105_signal(revenue, ebitda, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = (v + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_cyclecomp_252d_base_v106_signal(revenue, ebitda, closeadj):
    v = _f43_revenue_vol(revenue, 252)
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = (v + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_cyclecomp_504d_base_v107_signal(revenue, ebitda, closeadj):
    v = _f43_revenue_vol(revenue, 504)
    d = _f43_demand_cycle_score(revenue, ebitda, 504)
    result = (v + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvollog_63d_base_v108_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63).abs().replace(0, np.nan)
    result = np.log(v) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvollog_252d_base_v109_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 252).abs().replace(0, np.nan)
    result = np.log(v) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsq_63d_base_v110_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsq_252d_base_v111_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcssqdev_63d_base_v112_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    m = _mean(d, 63)
    result = ((d - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcssqdev_252d_base_v113_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    m = _mean(d, 252)
    result = ((d - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxcr_21d_base_v114_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 21)
    result = d * (closeadj / closeadj.rolling(252, min_periods=63).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxcr_63d_base_v115_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = d * (closeadj / closeadj.rolling(252, min_periods=63).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxcr_252d_base_v116_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = d * (closeadj / closeadj.rolling(252, min_periods=63).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsxlong_63d_base_v117_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = (d - _mean(d, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsxlong_252d_base_v118_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    result = (d - _mean(d, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrank_63d_base_v119_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = v.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrank_126d_base_v120_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = v.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrank_252d_base_v121_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = v.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolrank_504d_base_v122_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = v.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrank_63d_base_v123_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = d.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrank_252d_base_v124_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = d.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddrank_504d_base_v125_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    result = d.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrank_63d_base_v126_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = d.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrank_252d_base_v127_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = d.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsrank_504d_base_v128_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = d.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolemadiff_21m63_base_v129_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = (_ema(v, 21) - _ema(v, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolemadiff_63m252_base_v130_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = (_ema(v, 63) - _ema(v, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolemadiff_126m252_base_v131_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    result = (_ema(v, 126) - _ema(v, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsemadiff_21m63_base_v132_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = (_ema(d, 21) - _ema(d, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsemadiff_63m252_base_v133_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    result = (_ema(d, 63) - _ema(d, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddema_21d_base_v134_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddema_63d_base_v135_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddema_252d_base_v136_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddema_504d_base_v137_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 504)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolminmax_63d_base_v138_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    hi = v.rolling(63, min_periods=max(1, 63//2)).max()
    lo = v.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((v - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolminmax_252d_base_v139_signal(revenue, closeadj):
    v = _f43_revenue_vol(revenue, 63)
    hi = v.rolling(252, min_periods=max(1, 252//2)).max()
    lo = v.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((v - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddminmax_63d_base_v140_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    hi = d.rolling(63, min_periods=max(1, 63//2)).max()
    lo = d.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((d - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddminmax_252d_base_v141_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    hi = d.rolling(252, min_periods=max(1, 252//2)).max()
    lo = d.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((d - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsminmax_63d_base_v142_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 63)
    hi = d.rolling(63, min_periods=max(1, 63//2)).max()
    lo = d.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((d - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_dcsminmax_252d_base_v143_signal(revenue, ebitda, closeadj):
    d = _f43_demand_cycle_score(revenue, ebitda, 252)
    hi = d.rolling(252, min_periods=max(1, 252//2)).max()
    lo = d.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((d - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxhlr_21d_base_v144_signal(revenue, high, low):
    v = _f43_revenue_vol(revenue, 21)
    rng = (high - low).rolling(21, min_periods=max(1, 21//2)).mean()
    result = v * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxhlr_63d_base_v145_signal(revenue, high, low):
    v = _f43_revenue_vol(revenue, 63)
    rng = (high - low).rolling(63, min_periods=max(1, 63//2)).mean()
    result = v * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rvolxhlr_252d_base_v146_signal(revenue, high, low):
    v = _f43_revenue_vol(revenue, 252)
    rng = (high - low).rolling(252, min_periods=max(1, 252//2)).mean()
    result = v * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsign_21d_base_v147_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 21)
    result = np.sign(d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsign_63d_base_v148_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 63)
    result = np.sign(d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddsign_252d_base_v149_signal(revenue, closeadj):
    d = _f43_revenue_drawdown(revenue, 252)
    result = np.sign(d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43ldc_f43_lodging_demand_cycle_rddxdv_21d_base_v150_signal(revenue, closeadj, volume):
    d = _f43_revenue_drawdown(revenue, 21)
    dv = closeadj * volume
    result = d * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43ldc_f43_lodging_demand_cycle_rddxvol_252d_base_v076_signal,
    f43ldc_f43_lodging_demand_cycle_dcsxvol_21d_base_v077_signal,
    f43ldc_f43_lodging_demand_cycle_dcsxvol_63d_base_v078_signal,
    f43ldc_f43_lodging_demand_cycle_dcsxvol_252d_base_v079_signal,
    f43ldc_f43_lodging_demand_cycle_rvoldiff_21m63_base_v080_signal,
    f43ldc_f43_lodging_demand_cycle_rvoldiff_63m252_base_v081_signal,
    f43ldc_f43_lodging_demand_cycle_rvoldiff_252m504_base_v082_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrat_63v252_base_v083_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrat_21v63_base_v084_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrat_252v504_base_v085_signal,
    f43ldc_f43_lodging_demand_cycle_rddrat_63v252_base_v086_signal,
    f43ldc_f43_lodging_demand_cycle_rddrat_21v63_base_v087_signal,
    f43ldc_f43_lodging_demand_cycle_rddrat_252v504_base_v088_signal,
    f43ldc_f43_lodging_demand_cycle_rdddiff_21m63_base_v089_signal,
    f43ldc_f43_lodging_demand_cycle_rdddiff_63m252_base_v090_signal,
    f43ldc_f43_lodging_demand_cycle_rdddiff_252m504_base_v091_signal,
    f43ldc_f43_lodging_demand_cycle_rdddiff_126m252_base_v092_signal,
    f43ldc_f43_lodging_demand_cycle_dcsdiff_21m63_base_v093_signal,
    f43ldc_f43_lodging_demand_cycle_dcsdiff_63m252_base_v094_signal,
    f43ldc_f43_lodging_demand_cycle_dcsdiff_252m504_base_v095_signal,
    f43ldc_f43_lodging_demand_cycle_dcsdiff_126m252_base_v096_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrat_63v252_base_v097_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrat_21v63_base_v098_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrat_252v504_base_v099_signal,
    f43ldc_f43_lodging_demand_cycle_rvolstd_63d_base_v100_signal,
    f43ldc_f43_lodging_demand_cycle_rvolstd_252d_base_v101_signal,
    f43ldc_f43_lodging_demand_cycle_dcsstd_63d_base_v102_signal,
    f43ldc_f43_lodging_demand_cycle_dcsstd_252d_base_v103_signal,
    f43ldc_f43_lodging_demand_cycle_dcsstd_504d_base_v104_signal,
    f43ldc_f43_lodging_demand_cycle_cyclecomp_63d_base_v105_signal,
    f43ldc_f43_lodging_demand_cycle_cyclecomp_252d_base_v106_signal,
    f43ldc_f43_lodging_demand_cycle_cyclecomp_504d_base_v107_signal,
    f43ldc_f43_lodging_demand_cycle_rvollog_63d_base_v108_signal,
    f43ldc_f43_lodging_demand_cycle_rvollog_252d_base_v109_signal,
    f43ldc_f43_lodging_demand_cycle_rddsq_63d_base_v110_signal,
    f43ldc_f43_lodging_demand_cycle_rddsq_252d_base_v111_signal,
    f43ldc_f43_lodging_demand_cycle_dcssqdev_63d_base_v112_signal,
    f43ldc_f43_lodging_demand_cycle_dcssqdev_252d_base_v113_signal,
    f43ldc_f43_lodging_demand_cycle_rddxcr_21d_base_v114_signal,
    f43ldc_f43_lodging_demand_cycle_rddxcr_63d_base_v115_signal,
    f43ldc_f43_lodging_demand_cycle_rddxcr_252d_base_v116_signal,
    f43ldc_f43_lodging_demand_cycle_dcsxlong_63d_base_v117_signal,
    f43ldc_f43_lodging_demand_cycle_dcsxlong_252d_base_v118_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrank_63d_base_v119_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrank_126d_base_v120_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrank_252d_base_v121_signal,
    f43ldc_f43_lodging_demand_cycle_rvolrank_504d_base_v122_signal,
    f43ldc_f43_lodging_demand_cycle_rddrank_63d_base_v123_signal,
    f43ldc_f43_lodging_demand_cycle_rddrank_252d_base_v124_signal,
    f43ldc_f43_lodging_demand_cycle_rddrank_504d_base_v125_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrank_63d_base_v126_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrank_252d_base_v127_signal,
    f43ldc_f43_lodging_demand_cycle_dcsrank_504d_base_v128_signal,
    f43ldc_f43_lodging_demand_cycle_rvolemadiff_21m63_base_v129_signal,
    f43ldc_f43_lodging_demand_cycle_rvolemadiff_63m252_base_v130_signal,
    f43ldc_f43_lodging_demand_cycle_rvolemadiff_126m252_base_v131_signal,
    f43ldc_f43_lodging_demand_cycle_dcsemadiff_21m63_base_v132_signal,
    f43ldc_f43_lodging_demand_cycle_dcsemadiff_63m252_base_v133_signal,
    f43ldc_f43_lodging_demand_cycle_rddema_21d_base_v134_signal,
    f43ldc_f43_lodging_demand_cycle_rddema_63d_base_v135_signal,
    f43ldc_f43_lodging_demand_cycle_rddema_252d_base_v136_signal,
    f43ldc_f43_lodging_demand_cycle_rddema_504d_base_v137_signal,
    f43ldc_f43_lodging_demand_cycle_rvolminmax_63d_base_v138_signal,
    f43ldc_f43_lodging_demand_cycle_rvolminmax_252d_base_v139_signal,
    f43ldc_f43_lodging_demand_cycle_rddminmax_63d_base_v140_signal,
    f43ldc_f43_lodging_demand_cycle_rddminmax_252d_base_v141_signal,
    f43ldc_f43_lodging_demand_cycle_dcsminmax_63d_base_v142_signal,
    f43ldc_f43_lodging_demand_cycle_dcsminmax_252d_base_v143_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxhlr_21d_base_v144_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxhlr_63d_base_v145_signal,
    f43ldc_f43_lodging_demand_cycle_rvolxhlr_252d_base_v146_signal,
    f43ldc_f43_lodging_demand_cycle_rddsign_21d_base_v147_signal,
    f43ldc_f43_lodging_demand_cycle_rddsign_63d_base_v148_signal,
    f43ldc_f43_lodging_demand_cycle_rddsign_252d_base_v149_signal,
    f43ldc_f43_lodging_demand_cycle_rddxdv_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_LODGING_DEMAND_CYCLE_REGISTRY_076_150 = REGISTRY


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

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ebitda": ebitda }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f43_revenue_vol", "_f43_revenue_drawdown", "_f43_demand_cycle_score")
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
    print(f"OK lodging_demand_cycle_base_076_150_claude: {n_features} features pass")
