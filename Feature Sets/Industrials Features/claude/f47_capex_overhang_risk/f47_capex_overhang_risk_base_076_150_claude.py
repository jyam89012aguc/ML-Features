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


def _f47_capex_overinvestment(capex, depamor, w):
    return _mean(capex / depamor.replace(0, np.nan).abs(), w)


def _f47_capex_roic_pressure(capex, roic, w):
    return _mean(capex, w) * _mean(roic, w)


def _f47_overhang_signal(capex, ebit, w):
    return _mean(capex / ebit.replace(0, np.nan).abs(), w)


# v076-v084: capex/revenue × OI scaled
def f47cohr_f47_capex_overhang_risk_oi_volz_63d_base_v076_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_volz_252d_base_v077_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_volz_63d_base_v078_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_volz_252d_base_v079_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_dv_63d_base_v080_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_dv_252d_base_v081_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixvolc_21d_base_v082_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    result = base * closeadj * np.log(volume.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxvolc_21d_base_v083_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21)
    result = base * closeadj * np.log(volume.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrevz_63d_base_v084_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * _z(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085-v091: ROIC pressure variants
def f47cohr_f47_capex_overhang_risk_pressxroicrank_252d_base_v085_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    rr = roic.rolling(504, min_periods=126).rank(pct=True)
    result = base * rr / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressxroicz_252d_base_v086_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    rz = _z(roic, 504)
    result = base * rz / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressxneg_63d_base_v087_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63)
    delta = roic - roic.shift(63)
    neg = (delta < 0).astype(float)
    med = delta.rolling(252, min_periods=63).median()
    mod = (delta < med).astype(float)
    result = (base * neg + base * mod * 0.5 + base * 0.25) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressxneg_252d_base_v088_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    delta = roic - roic.shift(252)
    med = delta.rolling(504, min_periods=126).median()
    mod = (delta < med).astype(float)
    result = (base * mod + base * 0.5) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_capexxroic_63d_base_v089_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63)
    result = base * roic / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_capexxroic_252d_base_v090_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    result = base * roic / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressxlogprice_252d_base_v091_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan)) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


# v092-v100: combination effects
def f47cohr_f47_capex_overhang_risk_oixsignal_63d_base_v092_signal(capex, depamor, ebit, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 63)
    b = _f47_overhang_signal(capex, ebit, 63)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_252d_base_v093_signal(capex, depamor, ebit, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_504d_base_v094_signal(capex, depamor, ebit, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 504)
    b = _f47_overhang_signal(capex, ebit, 504)
    result = (a * b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroic_252d_base_v095_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    rz = _z(roic, 504)
    result = base * rz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxroic_252d_base_v096_signal(capex, ebit, roic, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    rz = _z(roic, 504)
    result = base * rz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebitda_252d_base_v097_signal(capex, depamor, ebit, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebitda_63d_base_v098_signal(capex, depamor, ebit, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 63)
    b = _f47_overhang_signal(capex, ebit, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compxroic_252d_base_v099_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    rz = _z(roic, 504)
    result = (a + b) * rz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compxneg_252d_base_v100_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    delta = roic - roic.shift(252)
    med = delta.rolling(504, min_periods=126).median()
    mod = (delta < med).astype(float)
    result = ((a + b) * mod + (a + b) * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101-v110: skew/kurt/rank variants
def f47cohr_f47_capex_overhang_risk_oiskew_252d_base_v101_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    result = g.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oikurt_252d_base_v102_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    result = g.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalskew_252d_base_v103_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    result = g.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalkurt_252d_base_v104_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    result = g.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_sqoi_252d_base_v105_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_sqsignal_252d_base_v106_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_lograwoi_252d_base_v107_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    result = np.log1p(g.abs()) * np.sign(g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_lograwsig_252d_base_v108_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    result = np.log1p(g.abs()) * np.sign(g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiminus1_252d_base_v109_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    result = (g - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalminus1_252d_base_v110_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    result = (g - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111-v120: lagged diffs and event counts
def f47cohr_f47_capex_overhang_risk_oilagdiff_252d_base_v111_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    result = (g - g.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signallagdiff_252d_base_v112_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    result = (g - g.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_presslagdiff_252d_base_v113_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 63)
    result = (g - g.shift(252)) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oievent_hi_252d_base_v114_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + g * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalevent_hi_252d_base_v115_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + g * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimedsplit_252d_base_v116_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmedsplit_252d_base_v117_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebit_63d_base_v118_signal(capex, depamor, ebit, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * np.log(ebit.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxlogcapex_252d_base_v119_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroicdelta_252d_base_v120_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    delta = roic - roic.shift(252)
    result = base * delta * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v135: mixed scaling, alternative kernels
def f47cohr_f47_capex_overhang_risk_oixrev_252d_base_v121_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = base * (revenue / capex.replace(0, np.nan).abs()) * closeadj * 1e-4
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_252d_base_v122_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * (revenue / capex.replace(0, np.nan).abs()) * closeadj * 1e-4
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixdvnorm_63d_base_v123_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    dv = closeadj * volume
    result = base * _z(dv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxdvnorm_63d_base_v124_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    dv = closeadj * volume
    result = base * _z(dv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oilog_252d_base_v125_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signallog_252d_base_v126_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirev_ratio_252d_base_v127_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    cr = capex / revenue.replace(0, np.nan).abs()
    result = (base + cr * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrev_ratio_252d_base_v128_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    cr = capex / revenue.replace(0, np.nan).abs()
    result = (base + cr * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimedsplit_504d_base_v129_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 504)
    med = g.rolling(504, min_periods=126).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmedsplit_504d_base_v130_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 504)
    med = g.rolling(504, min_periods=126).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixlogcap_63d_base_v131_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxlogcap_63d_base_v132_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixdep_63d_base_v133_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * np.log(depamor.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxdep_252d_base_v134_signal(capex, ebit, depamor, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * np.log(depamor.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_negroicxoi_252d_base_v135_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    rdelta = roic - roic.shift(252)
    med = rdelta.rolling(504, min_periods=126).median()
    mod = (rdelta < med).astype(float)
    result = (base * mod + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v150: more variants
def f47cohr_f47_capex_overhang_risk_oi42d_base_v136_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42)
    result = (base * np.log(closeadj.abs().replace(0, np.nan))) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal42d_base_v137_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42)
    result = (base * np.log(closeadj.abs().replace(0, np.nan))) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrevgrowth_63d_base_v138_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    rg = revenue.pct_change(63)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebitgrowth_63d_base_v139_signal(capex, depamor, ebit, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    eg = ebit.pct_change(63)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxebitgrowth_252d_base_v140_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    eg = ebit.pct_change(252)
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrev_growth_504d_base_v141_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504)
    rg = revenue.pct_change(252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_growth_504d_base_v142_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 504)
    rg = revenue.pct_change(252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oitrend_252d_base_v143_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = trend * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signaltrend_252d_base_v144_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = trend * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_presstrend_252d_base_v145_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = trend / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroicrange_252d_base_v146_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    rrange = roic.rolling(252, min_periods=63).max() - roic.rolling(252, min_periods=63).min()
    result = base * rrange * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxroicrange_252d_base_v147_signal(capex, ebit, roic, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    rrange = roic.rolling(252, min_periods=63).max() - roic.rolling(252, min_periods=63).min()
    result = base * rrange * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oicapexshare_252d_base_v148_signal(capex, depamor, ebitda, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    cap_share = capex / ebitda.replace(0, np.nan).abs()
    result = base * cap_share * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalcapexshare_252d_base_v149_signal(capex, ebit, ebitda, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    cap_share = capex / ebitda.replace(0, np.nan).abs()
    result = base * cap_share * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compositesev_252d_base_v150_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    rdelta = roic - roic.shift(252)
    result = ((a + b) * (1.0 - rdelta)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47cohr_f47_capex_overhang_risk_oi_volz_63d_base_v076_signal,
    f47cohr_f47_capex_overhang_risk_oi_volz_252d_base_v077_signal,
    f47cohr_f47_capex_overhang_risk_signal_volz_63d_base_v078_signal,
    f47cohr_f47_capex_overhang_risk_signal_volz_252d_base_v079_signal,
    f47cohr_f47_capex_overhang_risk_oi_dv_63d_base_v080_signal,
    f47cohr_f47_capex_overhang_risk_signal_dv_252d_base_v081_signal,
    f47cohr_f47_capex_overhang_risk_oixvolc_21d_base_v082_signal,
    f47cohr_f47_capex_overhang_risk_signalxvolc_21d_base_v083_signal,
    f47cohr_f47_capex_overhang_risk_oixrevz_63d_base_v084_signal,
    f47cohr_f47_capex_overhang_risk_pressxroicrank_252d_base_v085_signal,
    f47cohr_f47_capex_overhang_risk_pressxroicz_252d_base_v086_signal,
    f47cohr_f47_capex_overhang_risk_pressxneg_63d_base_v087_signal,
    f47cohr_f47_capex_overhang_risk_pressxneg_252d_base_v088_signal,
    f47cohr_f47_capex_overhang_risk_capexxroic_63d_base_v089_signal,
    f47cohr_f47_capex_overhang_risk_capexxroic_252d_base_v090_signal,
    f47cohr_f47_capex_overhang_risk_pressxlogprice_252d_base_v091_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_63d_base_v092_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_252d_base_v093_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_504d_base_v094_signal,
    f47cohr_f47_capex_overhang_risk_oixroic_252d_base_v095_signal,
    f47cohr_f47_capex_overhang_risk_signalxroic_252d_base_v096_signal,
    f47cohr_f47_capex_overhang_risk_oixebitda_252d_base_v097_signal,
    f47cohr_f47_capex_overhang_risk_oixebitda_63d_base_v098_signal,
    f47cohr_f47_capex_overhang_risk_compxroic_252d_base_v099_signal,
    f47cohr_f47_capex_overhang_risk_compxneg_252d_base_v100_signal,
    f47cohr_f47_capex_overhang_risk_oiskew_252d_base_v101_signal,
    f47cohr_f47_capex_overhang_risk_oikurt_252d_base_v102_signal,
    f47cohr_f47_capex_overhang_risk_signalskew_252d_base_v103_signal,
    f47cohr_f47_capex_overhang_risk_signalkurt_252d_base_v104_signal,
    f47cohr_f47_capex_overhang_risk_sqoi_252d_base_v105_signal,
    f47cohr_f47_capex_overhang_risk_sqsignal_252d_base_v106_signal,
    f47cohr_f47_capex_overhang_risk_lograwoi_252d_base_v107_signal,
    f47cohr_f47_capex_overhang_risk_lograwsig_252d_base_v108_signal,
    f47cohr_f47_capex_overhang_risk_oiminus1_252d_base_v109_signal,
    f47cohr_f47_capex_overhang_risk_signalminus1_252d_base_v110_signal,
    f47cohr_f47_capex_overhang_risk_oilagdiff_252d_base_v111_signal,
    f47cohr_f47_capex_overhang_risk_signallagdiff_252d_base_v112_signal,
    f47cohr_f47_capex_overhang_risk_presslagdiff_252d_base_v113_signal,
    f47cohr_f47_capex_overhang_risk_oievent_hi_252d_base_v114_signal,
    f47cohr_f47_capex_overhang_risk_signalevent_hi_252d_base_v115_signal,
    f47cohr_f47_capex_overhang_risk_oimedsplit_252d_base_v116_signal,
    f47cohr_f47_capex_overhang_risk_signalmedsplit_252d_base_v117_signal,
    f47cohr_f47_capex_overhang_risk_oixebit_63d_base_v118_signal,
    f47cohr_f47_capex_overhang_risk_signalxlogcapex_252d_base_v119_signal,
    f47cohr_f47_capex_overhang_risk_oixroicdelta_252d_base_v120_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_252d_base_v121_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_252d_base_v122_signal,
    f47cohr_f47_capex_overhang_risk_oixdvnorm_63d_base_v123_signal,
    f47cohr_f47_capex_overhang_risk_signalxdvnorm_63d_base_v124_signal,
    f47cohr_f47_capex_overhang_risk_oilog_252d_base_v125_signal,
    f47cohr_f47_capex_overhang_risk_signallog_252d_base_v126_signal,
    f47cohr_f47_capex_overhang_risk_oirev_ratio_252d_base_v127_signal,
    f47cohr_f47_capex_overhang_risk_signalrev_ratio_252d_base_v128_signal,
    f47cohr_f47_capex_overhang_risk_oimedsplit_504d_base_v129_signal,
    f47cohr_f47_capex_overhang_risk_signalmedsplit_504d_base_v130_signal,
    f47cohr_f47_capex_overhang_risk_oixlogcap_63d_base_v131_signal,
    f47cohr_f47_capex_overhang_risk_signalxlogcap_63d_base_v132_signal,
    f47cohr_f47_capex_overhang_risk_oixdep_63d_base_v133_signal,
    f47cohr_f47_capex_overhang_risk_signalxdep_252d_base_v134_signal,
    f47cohr_f47_capex_overhang_risk_negroicxoi_252d_base_v135_signal,
    f47cohr_f47_capex_overhang_risk_oi42d_base_v136_signal,
    f47cohr_f47_capex_overhang_risk_signal42d_base_v137_signal,
    f47cohr_f47_capex_overhang_risk_oixrevgrowth_63d_base_v138_signal,
    f47cohr_f47_capex_overhang_risk_oixebitgrowth_63d_base_v139_signal,
    f47cohr_f47_capex_overhang_risk_signalxebitgrowth_252d_base_v140_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_growth_504d_base_v141_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_growth_504d_base_v142_signal,
    f47cohr_f47_capex_overhang_risk_oitrend_252d_base_v143_signal,
    f47cohr_f47_capex_overhang_risk_signaltrend_252d_base_v144_signal,
    f47cohr_f47_capex_overhang_risk_presstrend_252d_base_v145_signal,
    f47cohr_f47_capex_overhang_risk_oixroicrange_252d_base_v146_signal,
    f47cohr_f47_capex_overhang_risk_signalxroicrange_252d_base_v147_signal,
    f47cohr_f47_capex_overhang_risk_oicapexshare_252d_base_v148_signal,
    f47cohr_f47_capex_overhang_risk_signalcapexshare_252d_base_v149_signal,
    f47cohr_f47_capex_overhang_risk_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_CAPEX_OVERHANG_RISK_REGISTRY_076_150 = REGISTRY


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
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "capex": capex, "depamor": depamor, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_capex_overinvestment", "_f47_capex_roic_pressure", "_f47_overhang_signal")
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
    print(f"OK f47_capex_overhang_risk_base_076_150_claude: {n_features} features pass")
