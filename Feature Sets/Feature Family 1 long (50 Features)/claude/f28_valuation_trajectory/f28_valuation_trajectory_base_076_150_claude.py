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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f28_valuation_traj(multiple, w):
    base = _mean(multiple, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f28_pe_change(pe, w):
    return _diff(_mean(pe, w), w) / _mean(pe.abs(), w).replace(0, np.nan)


def _f28_multiple_zscore(multiple, w_short, w_long):
    return _z(_mean(multiple, w_short), w_long)


# 504d ratio of EVEBIT current vs 504d mean
def f28vt_f28_valuation_trajectory_evebitvsmean_504d_base_v076_signal(evebit, marketcap):
    base = _safe_div(evebit, _mean(evebit, 504))
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_valuation_traj(evebit, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of EVEBITDA current vs 252d mean
def f28vt_f28_valuation_trajectory_evebitdavsmean_252d_base_v077_signal(evebitda, marketcap):
    base = _safe_div(evebitda, _mean(evebitda, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_valuation_traj(evebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap z-score
def f28vt_f28_valuation_trajectory_mcapz_504d_base_v078_signal(marketcap):
    base = _f28_multiple_zscore(marketcap, 63, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap z-score
def f28vt_f28_valuation_trajectory_mcapz_252d_base_v079_signal(marketcap):
    base = _f28_multiple_zscore(marketcap, 21, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV z-score
def f28vt_f28_valuation_trajectory_evz_252d_base_v080_signal(ev, marketcap):
    base = _f28_multiple_zscore(ev, 21, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV z-score
def f28vt_f28_valuation_trajectory_evz_504d_base_v081_signal(ev, marketcap):
    base = _f28_multiple_zscore(ev, 63, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE absolute change × marketcap
def f28vt_f28_valuation_trajectory_pechgabs_21d_base_v082_signal(pe, marketcap):
    result = _f28_pe_change(pe, 21).abs() * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE absolute change × marketcap
def f28vt_f28_valuation_trajectory_pechgabs_252d_base_v083_signal(pe, marketcap):
    result = _f28_pe_change(pe, 252).abs() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE absolute change × marketcap
def f28vt_f28_valuation_trajectory_pechgabs_504d_base_v084_signal(pe, marketcap):
    result = _f28_pe_change(pe, 504).abs() * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB absolute change × marketcap
def f28vt_f28_valuation_trajectory_pbchgabs_252d_base_v085_signal(pb, marketcap):
    result = _f28_pe_change(pb, 252).abs() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PS absolute change × marketcap
def f28vt_f28_valuation_trajectory_pschgabs_252d_base_v086_signal(ps, marketcap):
    result = _f28_pe_change(ps, 252).abs() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE coefficient of variation
def f28vt_f28_valuation_trajectory_pecv_252d_base_v087_signal(pe, marketcap):
    base = _safe_div(_std(pe, 252), _mean(pe.abs(), 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE coefficient of variation
def f28vt_f28_valuation_trajectory_pecv_504d_base_v088_signal(pe, marketcap):
    base = _safe_div(_std(pe, 504), _mean(pe.abs(), 504))
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA coefficient of variation
def f28vt_f28_valuation_trajectory_evebitdacv_252d_base_v089_signal(evebitda, marketcap):
    base = _safe_div(_std(evebitda, 252), _mean(evebitda.abs(), 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of short vs long PE change
def f28vt_f28_valuation_trajectory_pechgratio_21v63_base_v090_signal(pe, marketcap):
    sg = _f28_pe_change(pe, 21)
    lg = _f28_pe_change(pe, 63).replace(0, np.nan)
    result = (sg / lg) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of short vs long PE change
def f28vt_f28_valuation_trajectory_pechgratio_63v252_base_v091_signal(pe, marketcap):
    sg = _f28_pe_change(pe, 63)
    lg = _f28_pe_change(pe, 252).replace(0, np.nan)
    result = (sg / lg) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE change momentum scaled
def f28vt_f28_valuation_trajectory_pechgxmom_21d_base_v092_signal(pe, marketcap):
    mom = marketcap.pct_change(21)
    base = _f28_pe_change(pe, 21) * (1.0 + mom)
    result = base * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE change momentum scaled
def f28vt_f28_valuation_trajectory_pechgxmom_63d_base_v093_signal(pe, marketcap):
    mom = marketcap.pct_change(63)
    base = _f28_pe_change(pe, 63) * (1.0 + mom)
    result = base * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE change momentum scaled
def f28vt_f28_valuation_trajectory_pechgxmom_252d_base_v094_signal(pe, marketcap):
    mom = marketcap.pct_change(252)
    base = _f28_pe_change(pe, 252) * (1.0 + mom)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE acceleration via diff of change
def f28vt_f28_valuation_trajectory_peaccel_252d_base_v095_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    base = _diff(g, 63)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE acceleration via diff of change
def f28vt_f28_valuation_trajectory_peaccel_504d_base_v096_signal(pe, marketcap):
    g = _f28_pe_change(pe, 252)
    base = _diff(g, 252)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of (PE - mean PE)
def f28vt_f28_valuation_trajectory_pearea_252d_base_v097_signal(pe, marketcap):
    base = (pe - _mean(pe, 252)).rolling(252, min_periods=63).sum()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of (PE - mean PE)
def f28vt_f28_valuation_trajectory_pearea_504d_base_v098_signal(pe, marketcap):
    base = (pe - _mean(pe, 504)).rolling(504, min_periods=126).sum()
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of PE change
def f28vt_f28_valuation_trajectory_pechgskew_252d_base_v099_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).rolling(252, min_periods=63).skew()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of PE change
def f28vt_f28_valuation_trajectory_pechgskew_504d_base_v100_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).rolling(504, min_periods=126).skew()
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt of PE change
def f28vt_f28_valuation_trajectory_pechgkurt_252d_base_v101_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).rolling(252, min_periods=63).kurt()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt of PE change
def f28vt_f28_valuation_trajectory_pechgkurt_504d_base_v102_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).rolling(504, min_periods=126).kurt()
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite valuation: PE+PB+PS trajectory
def f28vt_f28_valuation_trajectory_composite_252d_base_v103_signal(pe, pb, ps, marketcap):
    base = _f28_pe_change(pe, 252) + _f28_pe_change(pb, 252) + _f28_pe_change(ps, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite valuation: PE+PB+PS trajectory
def f28vt_f28_valuation_trajectory_composite_504d_base_v104_signal(pe, pb, ps, marketcap):
    base = _f28_pe_change(pe, 504) + _f28_pe_change(pb, 504) + _f28_pe_change(ps, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV trajectory × marketcap²
def f28vt_f28_valuation_trajectory_evtrajxmcap_252d_base_v105_signal(ev, marketcap):
    base = _f28_valuation_traj(ev, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) ** 2.0 / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap trajectory × marketcap
def f28vt_f28_valuation_trajectory_mcaptrajxmcap_504d_base_v106_signal(marketcap):
    base = _f28_valuation_traj(marketcap, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE × PB compound multiple
def f28vt_f28_valuation_trajectory_pexpb_252d_base_v107_signal(pe, pb, marketcap):
    base = _mean(pe, 252) * _mean(pb, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) / 100.0 + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE × PS compound multiple
def f28vt_f28_valuation_trajectory_pexps_504d_base_v108_signal(pe, ps, marketcap):
    base = _mean(pe, 504) * _mean(ps, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) / 100.0 + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE level × marketcap (scale-aware)
def f28vt_f28_valuation_trajectory_pelvlxmcap_21d_base_v109_signal(pe, marketcap):
    base = _mean(pe, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    result = base + _f28_pe_change(pe, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE area × marketcap
def f28vt_f28_valuation_trajectory_pelvlxmcap_252d_base_v110_signal(pe, marketcap):
    base = _mean(pe, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    result = base + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE area × marketcap
def f28vt_f28_valuation_trajectory_pelvlxmcap_504d_base_v111_signal(pe, marketcap):
    base = _mean(pe, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    result = base + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE difference current vs 504d-mean
def f28vt_f28_valuation_trajectory_pediff_504_base_v112_signal(pe, marketcap):
    base = pe - _mean(pe, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB difference current vs 504d-mean
def f28vt_f28_valuation_trajectory_pbdiff_504_base_v113_signal(pb, marketcap):
    base = pb - _mean(pb, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pb, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PS difference current vs 504d-mean
def f28vt_f28_valuation_trajectory_psdiff_504_base_v114_signal(ps, marketcap):
    base = ps - _mean(ps, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(ps, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit difference current vs 504d-mean
def f28vt_f28_valuation_trajectory_evebitdiff_504_base_v115_signal(evebit, marketcap):
    base = evebit - _mean(evebit, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_valuation_traj(evebit, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda difference current vs 504d-mean
def f28vt_f28_valuation_trajectory_evebitdadiff_504_base_v116_signal(evebitda, marketcap):
    base = evebitda - _mean(evebitda, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_valuation_traj(evebitda, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 252d-PE-min relative current
def f28vt_f28_valuation_trajectory_pevsmin_252d_base_v117_signal(pe, marketcap):
    base = pe / _mean(pe, 252).replace(0, np.nan)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE rolling sum
def f28vt_f28_valuation_trajectory_pesum_504d_base_v118_signal(pe, marketcap):
    base = pe.rolling(504, min_periods=126).sum() / 504.0
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_valuation_traj(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE rolling sum
def f28vt_f28_valuation_trajectory_pesum_252d_base_v119_signal(pe, marketcap):
    base = pe.rolling(252, min_periods=63).sum() / 252.0
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_valuation_traj(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA rolling sum
def f28vt_f28_valuation_trajectory_evebitdasum_252d_base_v120_signal(evebitda, marketcap):
    base = evebitda.rolling(252, min_periods=63).sum() / 252.0
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_valuation_traj(evebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of PE rises (rolling sum sign)
def f28vt_f28_valuation_trajectory_pesignsum_252d_base_v121_signal(pe, marketcap):
    g = _f28_pe_change(pe, 21)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(252, min_periods=63).sum()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of PE rises sign
def f28vt_f28_valuation_trajectory_pesignsum_504d_base_v122_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(504, min_periods=126).sum()
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV * marketcap proxy
def f28vt_f28_valuation_trajectory_evxmcap_252d_base_v123_signal(ev, marketcap):
    base = _f28_pe_change(ev, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) ** 2.0
    result = base / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV * marketcap proxy
def f28vt_f28_valuation_trajectory_evxmcap_504d_base_v124_signal(ev, marketcap):
    base = _f28_pe_change(ev, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) ** 2.0
    result = base / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of EVEBITDA changes
def f28vt_f28_valuation_trajectory_evebitdacumchg_252d_base_v125_signal(evebitda, marketcap):
    g = _f28_pe_change(evebitda, 21)
    base = g.rolling(252, min_periods=63).sum()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of EVEBITDA changes
def f28vt_f28_valuation_trajectory_evebitdacumchg_504d_base_v126_signal(evebitda, marketcap):
    g = _f28_pe_change(evebitda, 63)
    base = g.rolling(504, min_periods=126).sum()
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap volatility scaled by marketcap
def f28vt_f28_valuation_trajectory_mcapvol_21d_base_v127_signal(marketcap):
    base = _std(marketcap.pct_change(), 21)
    result = base * np.log(_mean(marketcap, 21).replace(0, np.nan).abs()) + _f28_pe_change(marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap volatility scaled
def f28vt_f28_valuation_trajectory_mcapvol_252d_base_v128_signal(marketcap):
    base = _std(marketcap.pct_change(), 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV volatility scaled
def f28vt_f28_valuation_trajectory_evvol_504d_base_v129_signal(ev, marketcap):
    base = _std(ev.pct_change(), 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(ev, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV/EBIT change
def f28vt_f28_valuation_trajectory_evebitchg_21d_base_v130_signal(evebit, marketcap):
    result = _f28_pe_change(evebit, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBIT change
def f28vt_f28_valuation_trajectory_evebitchg_63d_base_v131_signal(evebit, marketcap):
    result = _f28_pe_change(evebit, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV/EBITDA change
def f28vt_f28_valuation_trajectory_evebitdachg_21d_base_v132_signal(evebitda, marketcap):
    result = _f28_pe_change(evebitda, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBITDA change
def f28vt_f28_valuation_trajectory_evebitdachg_63d_base_v133_signal(evebitda, marketcap):
    result = _f28_pe_change(evebitda, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA change
def f28vt_f28_valuation_trajectory_evebitdachg_252d_base_v134_signal(evebitda, marketcap):
    result = _f28_pe_change(evebitda, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBITDA change
def f28vt_f28_valuation_trajectory_evebitdachg_504d_base_v135_signal(evebitda, marketcap):
    result = _f28_pe_change(evebitda, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap to PS ratio (revenue-implied)
def f28vt_f28_valuation_trajectory_mcapps_252d_base_v136_signal(ps, marketcap):
    base = _safe_div(_mean(marketcap, 252), _mean(ps, 252)) / 1e6
    result = base + _f28_pe_change(ps, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap to PB ratio
def f28vt_f28_valuation_trajectory_mcappb_504d_base_v137_signal(pb, marketcap):
    base = _safe_div(_mean(marketcap, 504), _mean(pb, 504)) / 1e6
    result = base + _f28_pe_change(pb, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d harmonic-mean style PE
def f28vt_f28_valuation_trajectory_peharm_252d_base_v138_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _safe_div(pd.Series(1.0, index=pe.index), _mean(inv, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d harmonic-mean style PE
def f28vt_f28_valuation_trajectory_peharm_504d_base_v139_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _safe_div(pd.Series(1.0, index=pe.index), _mean(inv, 504))
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings yield (1/PE) trajectory
def f28vt_f28_valuation_trajectory_eyldtraj_252d_base_v140_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    result = _f28_valuation_traj(inv, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d earnings yield trajectory
def f28vt_f28_valuation_trajectory_eyldtraj_504d_base_v141_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    result = _f28_valuation_traj(inv, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sales yield (1/PS) trajectory
def f28vt_f28_valuation_trajectory_syldtraj_252d_base_v142_signal(ps, marketcap):
    inv = _safe_div(pd.Series(1.0, index=ps.index), ps)
    result = _f28_valuation_traj(inv, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sales yield trajectory
def f28vt_f28_valuation_trajectory_syldtraj_504d_base_v143_signal(ps, marketcap):
    inv = _safe_div(pd.Series(1.0, index=ps.index), ps)
    result = _f28_valuation_traj(inv, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA inverse trajectory (EBITDA yield)
def f28vt_f28_valuation_trajectory_ebitdayldtraj_252d_base_v144_signal(evebitda, marketcap):
    inv = _safe_div(pd.Series(1.0, index=evebitda.index), evebitda)
    result = _f28_valuation_traj(inv, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBITDA inverse trajectory
def f28vt_f28_valuation_trajectory_ebitdayldtraj_504d_base_v145_signal(evebitda, marketcap):
    inv = _safe_div(pd.Series(1.0, index=evebitda.index), evebitda)
    result = _f28_valuation_traj(inv, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d 63d-roll-PE-volatility / 252d-roll-PE-volatility
def f28vt_f28_valuation_trajectory_pevolratio_252d_base_v146_signal(pe, marketcap):
    sv = _std(pe.pct_change(), 63)
    lv = _std(pe.pct_change(), 252).replace(0, np.nan)
    base = sv / lv
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE vol ratio long
def f28vt_f28_valuation_trajectory_pevolratio_504d_base_v147_signal(pe, marketcap):
    sv = _std(pe.pct_change(), 126)
    lv = _std(pe.pct_change(), 504).replace(0, np.nan)
    base = sv / lv
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evebit z-score 252d
def f28vt_f28_valuation_trajectory_evebitz_252d_base_v148_signal(evebit, marketcap):
    base = _f28_multiple_zscore(evebit, 21, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit z-score 504d
def f28vt_f28_valuation_trajectory_evebitz_504d_base_v149_signal(evebit, marketcap):
    base = _f28_multiple_zscore(evebit, 63, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite valuation: EV/EBITDA + PE + PS
def f28vt_f28_valuation_trajectory_compvalshort_252d_base_v150_signal(evebitda, pe, ps, marketcap):
    base = _f28_pe_change(evebitda, 252) + _f28_pe_change(pe, 252) + _f28_pe_change(ps, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28vt_f28_valuation_trajectory_evebitvsmean_504d_base_v076_signal,
    f28vt_f28_valuation_trajectory_evebitdavsmean_252d_base_v077_signal,
    f28vt_f28_valuation_trajectory_mcapz_504d_base_v078_signal,
    f28vt_f28_valuation_trajectory_mcapz_252d_base_v079_signal,
    f28vt_f28_valuation_trajectory_evz_252d_base_v080_signal,
    f28vt_f28_valuation_trajectory_evz_504d_base_v081_signal,
    f28vt_f28_valuation_trajectory_pechgabs_21d_base_v082_signal,
    f28vt_f28_valuation_trajectory_pechgabs_252d_base_v083_signal,
    f28vt_f28_valuation_trajectory_pechgabs_504d_base_v084_signal,
    f28vt_f28_valuation_trajectory_pbchgabs_252d_base_v085_signal,
    f28vt_f28_valuation_trajectory_pschgabs_252d_base_v086_signal,
    f28vt_f28_valuation_trajectory_pecv_252d_base_v087_signal,
    f28vt_f28_valuation_trajectory_pecv_504d_base_v088_signal,
    f28vt_f28_valuation_trajectory_evebitdacv_252d_base_v089_signal,
    f28vt_f28_valuation_trajectory_pechgratio_21v63_base_v090_signal,
    f28vt_f28_valuation_trajectory_pechgratio_63v252_base_v091_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_21d_base_v092_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_63d_base_v093_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_252d_base_v094_signal,
    f28vt_f28_valuation_trajectory_peaccel_252d_base_v095_signal,
    f28vt_f28_valuation_trajectory_peaccel_504d_base_v096_signal,
    f28vt_f28_valuation_trajectory_pearea_252d_base_v097_signal,
    f28vt_f28_valuation_trajectory_pearea_504d_base_v098_signal,
    f28vt_f28_valuation_trajectory_pechgskew_252d_base_v099_signal,
    f28vt_f28_valuation_trajectory_pechgskew_504d_base_v100_signal,
    f28vt_f28_valuation_trajectory_pechgkurt_252d_base_v101_signal,
    f28vt_f28_valuation_trajectory_pechgkurt_504d_base_v102_signal,
    f28vt_f28_valuation_trajectory_composite_252d_base_v103_signal,
    f28vt_f28_valuation_trajectory_composite_504d_base_v104_signal,
    f28vt_f28_valuation_trajectory_evtrajxmcap_252d_base_v105_signal,
    f28vt_f28_valuation_trajectory_mcaptrajxmcap_504d_base_v106_signal,
    f28vt_f28_valuation_trajectory_pexpb_252d_base_v107_signal,
    f28vt_f28_valuation_trajectory_pexps_504d_base_v108_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_21d_base_v109_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_252d_base_v110_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_504d_base_v111_signal,
    f28vt_f28_valuation_trajectory_pediff_504_base_v112_signal,
    f28vt_f28_valuation_trajectory_pbdiff_504_base_v113_signal,
    f28vt_f28_valuation_trajectory_psdiff_504_base_v114_signal,
    f28vt_f28_valuation_trajectory_evebitdiff_504_base_v115_signal,
    f28vt_f28_valuation_trajectory_evebitdadiff_504_base_v116_signal,
    f28vt_f28_valuation_trajectory_pevsmin_252d_base_v117_signal,
    f28vt_f28_valuation_trajectory_pesum_504d_base_v118_signal,
    f28vt_f28_valuation_trajectory_pesum_252d_base_v119_signal,
    f28vt_f28_valuation_trajectory_evebitdasum_252d_base_v120_signal,
    f28vt_f28_valuation_trajectory_pesignsum_252d_base_v121_signal,
    f28vt_f28_valuation_trajectory_pesignsum_504d_base_v122_signal,
    f28vt_f28_valuation_trajectory_evxmcap_252d_base_v123_signal,
    f28vt_f28_valuation_trajectory_evxmcap_504d_base_v124_signal,
    f28vt_f28_valuation_trajectory_evebitdacumchg_252d_base_v125_signal,
    f28vt_f28_valuation_trajectory_evebitdacumchg_504d_base_v126_signal,
    f28vt_f28_valuation_trajectory_mcapvol_21d_base_v127_signal,
    f28vt_f28_valuation_trajectory_mcapvol_252d_base_v128_signal,
    f28vt_f28_valuation_trajectory_evvol_504d_base_v129_signal,
    f28vt_f28_valuation_trajectory_evebitchg_21d_base_v130_signal,
    f28vt_f28_valuation_trajectory_evebitchg_63d_base_v131_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_21d_base_v132_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_63d_base_v133_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_252d_base_v134_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_504d_base_v135_signal,
    f28vt_f28_valuation_trajectory_mcapps_252d_base_v136_signal,
    f28vt_f28_valuation_trajectory_mcappb_504d_base_v137_signal,
    f28vt_f28_valuation_trajectory_peharm_252d_base_v138_signal,
    f28vt_f28_valuation_trajectory_peharm_504d_base_v139_signal,
    f28vt_f28_valuation_trajectory_eyldtraj_252d_base_v140_signal,
    f28vt_f28_valuation_trajectory_eyldtraj_504d_base_v141_signal,
    f28vt_f28_valuation_trajectory_syldtraj_252d_base_v142_signal,
    f28vt_f28_valuation_trajectory_syldtraj_504d_base_v143_signal,
    f28vt_f28_valuation_trajectory_ebitdayldtraj_252d_base_v144_signal,
    f28vt_f28_valuation_trajectory_ebitdayldtraj_504d_base_v145_signal,
    f28vt_f28_valuation_trajectory_pevolratio_252d_base_v146_signal,
    f28vt_f28_valuation_trajectory_pevolratio_504d_base_v147_signal,
    f28vt_f28_valuation_trajectory_evebitz_252d_base_v148_signal,
    f28vt_f28_valuation_trajectory_evebitz_504d_base_v149_signal,
    f28vt_f28_valuation_trajectory_compvalshort_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_VALUATION_TRAJECTORY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit,
        "evebitda": evebitda, "pe": pe, "pb": pb, "ps": ps,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_valuation_traj", "_f28_pe_change", "_f28_multiple_zscore")
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
    print(f"OK f28_valuation_trajectory_base_076_150_claude: {n_features} features pass")
