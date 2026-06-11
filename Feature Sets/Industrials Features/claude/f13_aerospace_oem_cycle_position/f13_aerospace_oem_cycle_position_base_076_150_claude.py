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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (f13 aerospace_oem_cycle_position) =====
def _f13_revenue_inflection(revenue, w):
    sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    short = revenue.rolling(max(1, w // 3), min_periods=max(1, w // 6)).mean()
    return (short - sm) / sm.replace(0, np.nan).abs()


def _f13_cycle_trough_indicator(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f13_recovery_strength(revenue, ebitda, w):
    rg = revenue.pct_change(periods=max(1, w // 2))
    eg = ebitda.pct_change(periods=max(1, w // 2))
    return (rg + eg) * 0.5


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_dshift_v076_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = (base - base.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_absprod_v077_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_stdw_v078_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_meanw_v079_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = _mean(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_xvol_v080_signal(closeadj, revenue, volume):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * _mean(volume, 15) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_xdv_v081_signal(closeadj, ebitda, revenue, volume):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xebitda_v082_signal(closeadj, ebitda, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj * _mean(ebitda, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_xnetinc_v083_signal(closeadj, netinc, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj * _mean(netinc, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_xcapex_v084_signal(capex, closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xdrev_v085_signal(closeadj, deferredrev, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * closeadj * _mean(deferredrev, 126) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_xnm_v086_signal(closeadj, netmargin, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_xebm_v087_signal(closeadj, ebitda, ebitdamargin, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_logc_v088_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_sqrtc_v089_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_dshift_v090_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_absprod_v091_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_stdw_v092_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_meanw_v093_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xvol_v094_signal(closeadj, revenue, volume):
    base = _f13_revenue_inflection(revenue, 63)
    result = base * _mean(volume, 15) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_xdv_v095_signal(closeadj, revenue, volume):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_xebitda_v096_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xnetinc_v097_signal(closeadj, netinc, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj * _mean(netinc, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_xcapex_v098_signal(capex, closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_xdrev_v099_signal(closeadj, deferredrev, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xnm_v100_signal(closeadj, netmargin, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_xebm_v101_signal(closeadj, ebitdamargin, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_logc_v102_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_sqrtc_v103_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_dshift_v104_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_absprod_v105_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_stdw_v106_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_meanw_v107_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_xvol_v108_signal(closeadj, ebitda, revenue, volume):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xdv_v109_signal(closeadj, revenue, volume):
    base = _f13_revenue_inflection(revenue, 63)
    result = base * _mean(closeadj * volume, 15) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_xebitda_v110_signal(closeadj, ebitda, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_xnetinc_v111_signal(closeadj, ebitda, netinc, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xcapex_v112_signal(capex, closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj * _mean(capex, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_xdrev_v113_signal(closeadj, deferredrev, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_xnm_v114_signal(closeadj, ebitda, netmargin, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xebm_v115_signal(closeadj, ebitdamargin, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_logc_v116_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_sqrtc_v117_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_dshift_v118_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = (base - base.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_absprod_v119_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_stdw_v120_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_meanw_v121_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_xvol_v122_signal(closeadj, revenue, volume):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_xdv_v123_signal(closeadj, ebitda, revenue, volume):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = base * _mean(closeadj * volume, 5) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xebitda_v124_signal(closeadj, ebitda, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = base * closeadj * _mean(ebitda, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_xnetinc_v125_signal(closeadj, netinc, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_xcapex_v126_signal(capex, closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * closeadj * _mean(capex, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xdrev_v127_signal(closeadj, deferredrev, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj * _mean(deferredrev, 63) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_xnm_v128_signal(closeadj, netmargin, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_xebm_v129_signal(closeadj, ebitda, ebitdamargin, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_logc_v130_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_sqrtc_v131_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_dshift_v132_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_absprod_v133_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_stdw_v134_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_meanw_v135_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_xvol_v136_signal(closeadj, revenue, volume):
    base = _f13_revenue_inflection(revenue, 21)
    result = base * _mean(volume, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_xdv_v137_signal(closeadj, revenue, volume):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = base * _mean(closeadj * volume, 5) * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_xebitda_v138_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = base * closeadj * _mean(ebitda, 21) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xnetinc_v139_signal(closeadj, netinc, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = base * closeadj * _mean(netinc, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_xcapex_v140_signal(capex, closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * closeadj * _mean(capex, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_xdrev_v141_signal(closeadj, deferredrev, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * closeadj * _mean(deferredrev, 31) / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xnm_v142_signal(closeadj, netmargin, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj * netmargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_xebm_v143_signal(closeadj, ebitdamargin, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj * ebitdamargin
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_logc_v144_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * np.log(closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_sqrtc_v145_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_dshift_v146_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_absprod_v147_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = base.abs() * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_stdw_v148_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_meanw_v149_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_xvol_v150_signal(closeadj, ebitda, revenue, volume):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = base * _mean(volume, 126) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_dshift_v076_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_absprod_v077_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_stdw_v078_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_meanw_v079_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_xvol_v080_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_xdv_v081_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xebitda_v082_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_xnetinc_v083_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_xcapex_v084_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xdrev_v085_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_xnm_v086_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_xebm_v087_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_logc_v088_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_sqrtc_v089_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_dshift_v090_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_absprod_v091_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_stdw_v092_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_meanw_v093_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xvol_v094_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_xdv_v095_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_xebitda_v096_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xnetinc_v097_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_xcapex_v098_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_xdrev_v099_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xnm_v100_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_xebm_v101_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_logc_v102_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_sqrtc_v103_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_dshift_v104_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_absprod_v105_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_stdw_v106_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_meanw_v107_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_xvol_v108_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xdv_v109_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_xebitda_v110_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_xnetinc_v111_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xcapex_v112_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_xdrev_v113_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_xnm_v114_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_xebm_v115_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_logc_v116_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_sqrtc_v117_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_dshift_v118_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_absprod_v119_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_stdw_v120_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_meanw_v121_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_xvol_v122_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_xdv_v123_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xebitda_v124_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_xnetinc_v125_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_xcapex_v126_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xdrev_v127_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_xnm_v128_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_xebm_v129_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_logc_v130_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_sqrtc_v131_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_dshift_v132_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_absprod_v133_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_stdw_v134_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_meanw_v135_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_xvol_v136_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_xdv_v137_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_xebitda_v138_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_xnetinc_v139_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_xcapex_v140_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_xdrev_v141_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_xnm_v142_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_xebm_v143_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_logc_v144_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_sqrtc_v145_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_dshift_v146_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_absprod_v147_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_stdw_v148_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_meanw_v149_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_xvol_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_AEROSPACE_OEM_CYCLE_POSITION_REGISTRY_076_150 = REGISTRY
F13_AEROSPACE_OEM_CYCLE_POSITION_REGISTRY_076_150 = REGISTRY

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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f13_revenue_inflection", "_f13_cycle_trough_indicator", "_f13_recovery_strength",)
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
    print(f"OK f13_aerospace_oem_cycle_position_base_076_150_claude: {n_features} features pass")
