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
def _f31_cashflow_accel_fcf(fcf, w):
    g = _diff(fcf, w) / fcf.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_ncfo(ncfo, w):
    g = _diff(ncfo, w) / ncfo.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 21d FCF accel × debt magnitude (cash vs leverage)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_21d_base_v076_signal(fcf, debt, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 21) * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × debt magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_252d_base_v077_signal(fcf, debt, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current ratio
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_63d_base_v078_signal(fcf, currentratio, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × current ratio
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_252d_base_v079_signal(fcf, currentratio, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF / sharesbas (per-share intensity ratio)
def f31cfa_f31_cash_flow_acceleration_fcfshareintensity_63d_base_v080_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF / sharesbas (per-share intensity ratio)
def f31cfa_f31_cash_flow_acceleration_fcfshareintensity_252d_base_v081_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF acceleration EMA(63d) scaled by closeadj
def f31cfa_f31_cash_flow_acceleration_fcfaccelema_63d_base_v082_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF acceleration EMA(252d)
def f31cfa_f31_cash_flow_acceleration_fcfaccelema_252d_base_v083_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NCFO acceleration EMA(63d)
def f31cfa_f31_cash_flow_acceleration_ncfoaccelema_63d_base_v084_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO acceleration EMA(252d)
def f31cfa_f31_cash_flow_acceleration_ncfoaccelema_252d_base_v085_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel signed × FCF level (severity)
def f31cfa_f31_cash_flow_acceleration_fcfaccelsq_63d_base_v086_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel signed × magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelsq_252d_base_v087_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel signed × magnitude
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_63d_base_v088_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel signed × magnitude
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_252d_base_v089_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel area sum (cumulative cashflow accel pressure)
def f31cfa_f31_cash_flow_acceleration_fcfaccelarea_63d_base_v090_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel area sum
def f31cfa_f31_cash_flow_acceleration_fcfaccelarea_252d_base_v091_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel area sum
def f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_63d_base_v092_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel area sum
def f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_252d_base_v093_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: FCF + NCFO acceleration sum
def f31cfa_f31_cash_flow_acceleration_cashaccelcomp_63d_base_v094_signal(fcf, ncfo, closeadj):
    s = fcf + ncfo
    result = _f31_cashflow_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: FCF + NCFO acceleration sum
def f31cfa_f31_cash_flow_acceleration_cashaccelcomp_252d_base_v095_signal(fcf, ncfo, closeadj):
    s = fcf + ncfo
    result = _f31_cashflow_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel - NCFO accel (divergence)
def f31cfa_f31_cash_flow_acceleration_fcfminusncfo_63d_base_v096_signal(fcf, ncfo, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 63) - _f31_cashflow_accel_ncfo(ncfo, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel - NCFO accel (divergence)
def f31cfa_f31_cash_flow_acceleration_fcfminusncfo_252d_base_v097_signal(fcf, ncfo, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 252) - _f31_cashflow_accel_ncfo(ncfo, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × revenue growth (cash + sales acceleration)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_63d_base_v098_signal(fcf, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × revenue growth
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_252d_base_v099_signal(fcf, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel × revenue growth
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_63d_base_v100_signal(ncfo, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_ncfo(ncfo, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel × revenue growth
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_252d_base_v101_signal(ncfo, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_ncfo(ncfo, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel × eps growth
def f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_21d_base_v102_signal(fcf, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 21) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × eps growth
def f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_252d_base_v103_signal(fcf, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 252) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of (NCFO - capex) / revenue
def f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_63d_base_v104_signal(ncfo, capex, revenue, closeadj):
    s = (ncfo - capex) / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of (NCFO - capex) / revenue
def f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_252d_base_v105_signal(ncfo, capex, revenue, closeadj):
    s = (ncfo - capex) / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current FCF/EBITDA
def f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_63d_base_v106_signal(fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 63) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × current FCF/EBITDA
def f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_252d_base_v107_signal(fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 252) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel ÷ NCFO accel (relative cash quality accel)
def f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_63d_base_v108_signal(fcf, ncfo, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_ncfo(ncfo, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel ÷ NCFO accel
def f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_252d_base_v109_signal(fcf, ncfo, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    b = _f31_cashflow_accel_ncfo(ncfo, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel maximum value rolling 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxavg_252d_base_v110_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel rolling mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxavg_252d_base_v111_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF/equity acceleration × equity
def f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_63d_base_v112_signal(fcf, equity, closeadj):
    s = fcf / equity.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(s, 63) * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF/equity acceleration × equity
def f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_252d_base_v113_signal(fcf, equity, closeadj):
    s = fcf / equity.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(s, 252) * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel sign run-length proxy (rolling sign sum)
def f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_63d_base_v114_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel sign run-length proxy
def f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_252d_base_v115_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel sign sum
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_63d_base_v116_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel sign sum
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_252d_base_v117_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × tax expense magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_63d_base_v118_signal(fcf, taxexp, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × tax expense magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_252d_base_v119_signal(fcf, taxexp, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × interest expense magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxint_63d_base_v120_signal(fcf, intexp, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × interest expense magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxint_252d_base_v121_signal(fcf, intexp, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × retained earnings (compound)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_63d_base_v122_signal(fcf, retearn, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × retained earnings
def f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_252d_base_v123_signal(fcf, retearn, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel × liabilities magnitude (debt-cash mix)
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_63d_base_v124_signal(ncfo, liabilities, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 63) * liabilities.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel × liabilities magnitude
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_252d_base_v125_signal(ncfo, liabilities, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 252) * liabilities.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF/sharesbas zscored 252d
def f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_252d_base_v126_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF/sharesbas zscored 504d
def f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_504d_base_v127_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel + 63d FCF accel + 252d FCF accel composite
def f31cfa_f31_cash_flow_acceleration_fcfaccelmulti_base_v128_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    b = _f31_cashflow_accel_fcf(fcf, 63)
    c = _f31_cashflow_accel_fcf(fcf, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NCFO accel + 63d NCFO accel + 252d NCFO accel composite
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmulti_base_v129_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    b = _f31_cashflow_accel_ncfo(ncfo, 63)
    c = _f31_cashflow_accel_ncfo(ncfo, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current ratio × revenue
def f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_63d_base_v130_signal(fcf, currentratio, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × current ratio × revenue
def f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_252d_base_v131_signal(fcf, currentratio, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel times netinc growth (joint accel)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_63d_base_v132_signal(fcf, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 63) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel times netinc growth
def f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_252d_base_v133_signal(fcf, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    result = _f31_cashflow_accel_fcf(fcf, 252) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel - average expanding accel (anomaly)
def f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_63d_base_v134_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel - expanding mean
def f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_252d_base_v135_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel - expanding mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelanomaly_63d_base_v136_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel - expanding mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelanomaly_252d_base_v137_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EBITDA accel × current FCF magnitude
def f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_63d_base_v138_signal(ebitda, fcf, closeadj):
    a = _f31_cashflow_accel_growth(ebitda, 63)
    result = a * fcf.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EBITDA accel × current FCF magnitude
def f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_252d_base_v139_signal(ebitda, fcf, closeadj):
    a = _f31_cashflow_accel_growth(ebitda, 252)
    result = a * fcf.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of NCFO/sharesbas × sharesbas
def f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_63d_base_v140_signal(ncfo, sharesbas, closeadj):
    s = ncfo / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of NCFO/sharesbas × sharesbas
def f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_252d_base_v141_signal(ncfo, sharesbas, closeadj):
    s = ncfo / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × ebitda accel (joint cashflow accel)
def f31cfa_f31_cash_flow_acceleration_jointcashaccel_63d_base_v142_signal(fcf, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_growth(ebitda, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × ebitda accel (joint cashflow accel)
def f31cfa_f31_cash_flow_acceleration_jointcashaccel_252d_base_v143_signal(fcf, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    b = _f31_cashflow_accel_growth(ebitda, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current ratio - current ratio mean (deviation)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurdev_63d_base_v144_signal(fcf, currentratio, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    dev = currentratio - _mean(currentratio, 252)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × current ratio deviation
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurdev_252d_base_v145_signal(fcf, currentratio, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    dev = currentratio - _mean(currentratio, 504)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel - 63d ebitda accel (FCF-quality accel divergence)
def f31cfa_f31_cash_flow_acceleration_fcfminusebitdaaccel_63d_base_v146_signal(fcf, ebitda, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 63) - _f31_cashflow_accel_growth(ebitda, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel - 252d ebitda accel
def f31cfa_f31_cash_flow_acceleration_fcfminusebitdaaccel_252d_base_v147_signal(fcf, ebitda, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 252) - _f31_cashflow_accel_growth(ebitda, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel × FCF/NCFO ratio (cashflow quality acceleration)
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_63d_base_v148_signal(ncfo, fcf, closeadj):
    q = fcf / ncfo.replace(0, np.nan)
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel × FCF/NCFO ratio
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_252d_base_v149_signal(ncfo, fcf, closeadj):
    q = fcf / ncfo.replace(0, np.nan)
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite cashflow severity 252d: FCF + NCFO + EBITDA accel area
def f31cfa_f31_cash_flow_acceleration_compositesev_252d_base_v150_signal(fcf, ncfo, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_ncfo(ncfo, 63)
    c = _f31_cashflow_accel_growth(ebitda, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_21d_base_v076_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_252d_base_v077_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_63d_base_v078_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_252d_base_v079_signal,
    f31cfa_f31_cash_flow_acceleration_fcfshareintensity_63d_base_v080_signal,
    f31cfa_f31_cash_flow_acceleration_fcfshareintensity_252d_base_v081_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelema_63d_base_v082_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelema_252d_base_v083_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelema_63d_base_v084_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelema_252d_base_v085_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsq_63d_base_v086_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsq_252d_base_v087_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_63d_base_v088_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_252d_base_v089_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelarea_63d_base_v090_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelarea_252d_base_v091_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_63d_base_v092_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_252d_base_v093_signal,
    f31cfa_f31_cash_flow_acceleration_cashaccelcomp_63d_base_v094_signal,
    f31cfa_f31_cash_flow_acceleration_cashaccelcomp_252d_base_v095_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusncfo_63d_base_v096_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusncfo_252d_base_v097_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_63d_base_v098_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_252d_base_v099_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_63d_base_v100_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_252d_base_v101_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_21d_base_v102_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_252d_base_v103_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_63d_base_v104_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_252d_base_v105_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_63d_base_v106_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_252d_base_v107_signal,
    f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_63d_base_v108_signal,
    f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_252d_base_v109_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxavg_252d_base_v110_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxavg_252d_base_v111_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_63d_base_v112_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_252d_base_v113_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_63d_base_v114_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_252d_base_v115_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_63d_base_v116_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_252d_base_v117_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_63d_base_v118_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_252d_base_v119_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxint_63d_base_v120_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxint_252d_base_v121_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_63d_base_v122_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_252d_base_v123_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_63d_base_v124_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_252d_base_v125_signal,
    f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_252d_base_v126_signal,
    f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_504d_base_v127_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmulti_base_v128_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmulti_base_v129_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_63d_base_v130_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_252d_base_v131_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_63d_base_v132_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_252d_base_v133_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_63d_base_v134_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_252d_base_v135_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelanomaly_63d_base_v136_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelanomaly_252d_base_v137_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_63d_base_v138_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_252d_base_v139_signal,
    f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_63d_base_v140_signal,
    f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_252d_base_v141_signal,
    f31cfa_f31_cash_flow_acceleration_jointcashaccel_63d_base_v142_signal,
    f31cfa_f31_cash_flow_acceleration_jointcashaccel_252d_base_v143_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurdev_63d_base_v144_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurdev_252d_base_v145_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusebitdaaccel_63d_base_v146_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusebitdaaccel_252d_base_v147_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_63d_base_v148_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_252d_base_v149_signal,
    f31cfa_f31_cash_flow_acceleration_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_FLOW_ACCELERATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fund_walk = lambda mu, sd, base: pd.Series(base * np.exp(np.cumsum(np.random.normal(mu, sd, n))))
    revenue = fund_walk(0.0006, 0.015, 1e8).rename("revenue")
    netinc = fund_walk(0.0005, 0.02, 1e7).rename("netinc")
    fcf = fund_walk(0.0005, 0.025, 8e6).rename("fcf")
    equity = fund_walk(0.0004, 0.012, 5e8).rename("equity")
    debt = fund_walk(0.0004, 0.015, 3e8).rename("debt")
    assets = fund_walk(0.0004, 0.012, 1.2e9).rename("assets")
    ebitda = fund_walk(0.0005, 0.018, 2e7).rename("ebitda")
    capex = fund_walk(0.0004, 0.022, 5e6).rename("capex")
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    opinc = fund_walk(0.0005, 0.02, 2.5e7).rename("opinc")
    gp = fund_walk(0.0005, 0.018, 4e7).rename("gp")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")
    currentratio = fund_walk(0.0001, 0.01, 1.5).rename("currentratio")
    intexp = fund_walk(0.0003, 0.018, 5e6).rename("intexp")
    retearn = fund_walk(0.0005, 0.02, 1e8).rename("retearn")
    liabilities = fund_walk(0.0004, 0.012, 7e8).rename("liabilities")
    taxexp = fund_walk(0.0004, 0.022, 4e6).rename("taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
        "currentratio": currentratio, "intexp": intexp, "retearn": retearn,
        "liabilities": liabilities, "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_cashflow_accel_fcf", "_f31_cashflow_accel_ncfo", "_f31_cashflow_accel_growth")
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
    print(f"OK f31_cash_flow_acceleration_base_076_150_claude: {n_features} features pass")
