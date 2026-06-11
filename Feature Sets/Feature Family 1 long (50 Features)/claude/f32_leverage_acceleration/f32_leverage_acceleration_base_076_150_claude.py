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
def _f32_leverage_accel_de(debt, equity, w):
    de = debt / equity.replace(0, np.nan)
    g = _diff(de, w) / de.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f32_leverage_accel_debt(debt, w):
    g = _diff(debt, w) / debt.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f32_leverage_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 21d D/E accel × revenue magnitude
def f32la_f32_leverage_acceleration_deaccelxrev_21d_base_v076_signal(debt, equity, revenue, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 21) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × revenue magnitude
def f32la_f32_leverage_acceleration_deaccelxrev_252d_base_v077_signal(debt, equity, revenue, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 252) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × current ratio
def f32la_f32_leverage_acceleration_deaccelxcurratio_63d_base_v078_signal(debt, equity, currentratio, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × current ratio
def f32la_f32_leverage_acceleration_deaccelxcurratio_252d_base_v079_signal(debt, equity, currentratio, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt × sharesbas
def f32la_f32_leverage_acceleration_debtshareintensity_63d_base_v080_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt × sharesbas
def f32la_f32_leverage_acceleration_debtshareintensity_252d_base_v081_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E acceleration EMA(63d)
def f32la_f32_leverage_acceleration_deaccelema_63d_base_v082_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E acceleration EMA(252d)
def f32la_f32_leverage_acceleration_deaccelema_252d_base_v083_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt acceleration EMA(63d)
def f32la_f32_leverage_acceleration_debtaccelema_63d_base_v084_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt acceleration EMA(252d)
def f32la_f32_leverage_acceleration_debtaccelema_252d_base_v085_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel signed × magnitude
def f32la_f32_leverage_acceleration_deaccelsq_63d_base_v086_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel signed × magnitude
def f32la_f32_leverage_acceleration_deaccelsq_252d_base_v087_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel signed × magnitude
def f32la_f32_leverage_acceleration_debtaccelsq_63d_base_v088_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel signed × magnitude
def f32la_f32_leverage_acceleration_debtaccelsq_252d_base_v089_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel area sum
def f32la_f32_leverage_acceleration_deaccelarea_63d_base_v090_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel area sum
def f32la_f32_leverage_acceleration_deaccelarea_252d_base_v091_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel area sum
def f32la_f32_leverage_acceleration_debtaccelarea_63d_base_v092_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel area sum
def f32la_f32_leverage_acceleration_debtaccelarea_252d_base_v093_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite leverage accel: debt + equity dilution
def f32la_f32_leverage_acceleration_levaccelcomp_63d_base_v094_signal(debt, equity, closeadj):
    s = debt + equity
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite leverage accel
def f32la_f32_leverage_acceleration_levaccelcomp_252d_base_v095_signal(debt, equity, closeadj):
    s = debt + equity
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel - debt accel (divergence)
def f32la_f32_leverage_acceleration_deminusdebt_63d_base_v096_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 63) - _f32_leverage_accel_debt(debt, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel - debt accel
def f32la_f32_leverage_acceleration_deminusdebt_252d_base_v097_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 252) - _f32_leverage_accel_debt(debt, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × revenue growth
def f32la_f32_leverage_acceleration_deaccelxrevg_63d_base_v098_signal(debt, equity, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × revenue growth
def f32la_f32_leverage_acceleration_deaccelxrevg_252d_base_v099_signal(debt, equity, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × revenue growth
def f32la_f32_leverage_acceleration_debtaccelxrevg_63d_base_v100_signal(debt, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f32_leverage_accel_debt(debt, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × revenue growth
def f32la_f32_leverage_acceleration_debtaccelxrevg_252d_base_v101_signal(debt, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f32_leverage_accel_debt(debt, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E accel × eps growth
def f32la_f32_leverage_acceleration_deaccelxepsg_21d_base_v102_signal(debt, equity, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 21) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × eps growth
def f32la_f32_leverage_acceleration_deaccelxepsg_252d_base_v103_signal(debt, equity, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 252) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of (debt - cash equiv proxy via NCFO) /revenue
def f32la_f32_leverage_acceleration_netdebtxrev_63d_base_v104_signal(debt, ncfo, revenue, closeadj):
    s = (debt - ncfo) / revenue.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of (debt - NCFO) / revenue
def f32la_f32_leverage_acceleration_netdebtxrev_252d_base_v105_signal(debt, ncfo, revenue, closeadj):
    s = (debt - ncfo) / revenue.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × FCF/EBITDA quality
def f32la_f32_leverage_acceleration_deaccelxqual_63d_base_v106_signal(debt, equity, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 63) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × FCF/EBITDA quality
def f32la_f32_leverage_acceleration_deaccelxqual_252d_base_v107_signal(debt, equity, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_de(debt, equity, 252) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel ÷ debt accel
def f32la_f32_leverage_acceleration_devsdebt_63d_base_v108_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_debt(debt, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel ÷ debt accel
def f32la_f32_leverage_acceleration_devsdebt_252d_base_v109_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    b = _f32_leverage_accel_debt(debt, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel rolling 252d mean
def f32la_f32_leverage_acceleration_deaccelxavg_252d_base_v110_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel rolling 252d mean
def f32la_f32_leverage_acceleration_debtaccelxavg_252d_base_v111_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/equity accel × equity
def f32la_f32_leverage_acceleration_debttoeqxlevel_63d_base_v112_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    result = a * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/equity accel × equity
def f32la_f32_leverage_acceleration_debttoeqxlevel_252d_base_v113_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    result = a * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E accel sign rolling sum 63d
def f32la_f32_leverage_acceleration_deaccelsignsum_63d_base_v114_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E accel sign rolling sum 252d
def f32la_f32_leverage_acceleration_deaccelsignsum_252d_base_v115_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt accel sign rolling sum 63d
def f32la_f32_leverage_acceleration_debtaccelsignsum_63d_base_v116_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt accel sign rolling sum 252d
def f32la_f32_leverage_acceleration_debtaccelsignsum_252d_base_v117_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × tax expense
def f32la_f32_leverage_acceleration_debtaccelxtax_63d_base_v118_signal(debt, taxexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 63) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × tax expense
def f32la_f32_leverage_acceleration_debtaccelxtax_252d_base_v119_signal(debt, taxexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 252) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × interest expense
def f32la_f32_leverage_acceleration_debtaccelxintexp_63d_base_v120_signal(debt, intexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 63) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × interest expense
def f32la_f32_leverage_acceleration_debtaccelxintexp_252d_base_v121_signal(debt, intexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 252) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × retained earnings
def f32la_f32_leverage_acceleration_debtaccelxretearn_63d_base_v122_signal(debt, retearn, closeadj):
    result = _f32_leverage_accel_debt(debt, 63) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × retained earnings
def f32la_f32_leverage_acceleration_debtaccelxretearn_252d_base_v123_signal(debt, retearn, closeadj):
    result = _f32_leverage_accel_debt(debt, 252) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d liab accel × intexp
def f32la_f32_leverage_acceleration_liabaccelxintexp_63d_base_v124_signal(liabilities, intexp, closeadj):
    result = _f32_leverage_accel_growth(liabilities, 63) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d liab accel × intexp
def f32la_f32_leverage_acceleration_liabaccelxintexp_252d_base_v125_signal(liabilities, intexp, closeadj):
    result = _f32_leverage_accel_growth(liabilities, 252) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/sharesbas zscore 252d
def f32la_f32_leverage_acceleration_debtpsaccelz_252d_base_v126_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/sharesbas zscore 504d
def f32la_f32_leverage_acceleration_debtpsaccelz_504d_base_v127_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window D/E accel composite
def f32la_f32_leverage_acceleration_deaccelmulti_base_v128_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    b = _f32_leverage_accel_de(debt, equity, 63)
    c = _f32_leverage_accel_de(debt, equity, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window debt accel composite
def f32la_f32_leverage_acceleration_debtaccelmulti_base_v129_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    b = _f32_leverage_accel_debt(debt, 63)
    c = _f32_leverage_accel_debt(debt, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × current ratio × revenue
def f32la_f32_leverage_acceleration_deaccelhealth_63d_base_v130_signal(debt, equity, currentratio, revenue, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × current ratio × revenue
def f32la_f32_leverage_acceleration_deaccelhealth_252d_base_v131_signal(debt, equity, currentratio, revenue, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × netinc growth
def f32la_f32_leverage_acceleration_debtaccelxnetincg_63d_base_v132_signal(debt, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    result = _f32_leverage_accel_debt(debt, 63) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × netinc growth
def f32la_f32_leverage_acceleration_debtaccelxnetincg_252d_base_v133_signal(debt, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    result = _f32_leverage_accel_debt(debt, 252) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel - expanding mean (anomaly)
def f32la_f32_leverage_acceleration_deaccelanomaly_63d_base_v134_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel - expanding mean
def f32la_f32_leverage_acceleration_deaccelanomaly_252d_base_v135_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel - expanding mean
def f32la_f32_leverage_acceleration_debtaccelanomaly_63d_base_v136_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel - expanding mean
def f32la_f32_leverage_acceleration_debtaccelanomaly_252d_base_v137_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp accel × debt
def f32la_f32_leverage_acceleration_intexpaccelxdebt_63d_base_v138_signal(intexp, debt, closeadj):
    a = _f32_leverage_accel_growth(intexp, 63)
    result = a * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp accel × debt
def f32la_f32_leverage_acceleration_intexpaccelxdebt_252d_base_v139_signal(intexp, debt, closeadj):
    a = _f32_leverage_accel_growth(intexp, 252)
    result = a * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of liab/sharesbas × sharesbas
def f32la_f32_leverage_acceleration_liabpsxlevel_63d_base_v140_signal(liabilities, sharesbas, closeadj):
    s = liabilities / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of liab/sharesbas × sharesbas
def f32la_f32_leverage_acceleration_liabpsxlevel_252d_base_v141_signal(liabilities, sharesbas, closeadj):
    s = liabilities / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × intexp accel (joint leverage accel)
def f32la_f32_leverage_acceleration_jointlevaccel_63d_base_v142_signal(debt, equity, intexp, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_growth(intexp, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × intexp accel
def f32la_f32_leverage_acceleration_jointlevaccel_252d_base_v143_signal(debt, equity, intexp, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    b = _f32_leverage_accel_growth(intexp, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × current ratio deviation
def f32la_f32_leverage_acceleration_deaccelxcurdev_63d_base_v144_signal(debt, equity, currentratio, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    dev = currentratio - _mean(currentratio, 252)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × current ratio deviation
def f32la_f32_leverage_acceleration_deaccelxcurdev_252d_base_v145_signal(debt, equity, currentratio, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    dev = currentratio - _mean(currentratio, 504)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel - 63d debt accel
def f32la_f32_leverage_acceleration_deminusdebtaccel_63d_base_v146_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 63) - _f32_leverage_accel_debt(debt, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel - 252d debt accel
def f32la_f32_leverage_acceleration_deminusdebtaccel_252d_base_v147_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 252) - _f32_leverage_accel_debt(debt, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × debt/EBITDA quality
def f32la_f32_leverage_acceleration_debtaccelxquality_63d_base_v148_signal(debt, ebitda, closeadj):
    q = debt / ebitda.replace(0, np.nan)
    a = _f32_leverage_accel_debt(debt, 63)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × debt/EBITDA quality
def f32la_f32_leverage_acceleration_debtaccelxquality_252d_base_v149_signal(debt, ebitda, closeadj):
    q = debt / ebitda.replace(0, np.nan)
    a = _f32_leverage_accel_debt(debt, 252)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage severity 252d: D/E + debt + liab area
def f32la_f32_leverage_acceleration_compositesev_252d_base_v150_signal(debt, equity, liabilities, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_debt(debt, 63)
    c = _f32_leverage_accel_growth(liabilities, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32la_f32_leverage_acceleration_deaccelxrev_21d_base_v076_signal,
    f32la_f32_leverage_acceleration_deaccelxrev_252d_base_v077_signal,
    f32la_f32_leverage_acceleration_deaccelxcurratio_63d_base_v078_signal,
    f32la_f32_leverage_acceleration_deaccelxcurratio_252d_base_v079_signal,
    f32la_f32_leverage_acceleration_debtshareintensity_63d_base_v080_signal,
    f32la_f32_leverage_acceleration_debtshareintensity_252d_base_v081_signal,
    f32la_f32_leverage_acceleration_deaccelema_63d_base_v082_signal,
    f32la_f32_leverage_acceleration_deaccelema_252d_base_v083_signal,
    f32la_f32_leverage_acceleration_debtaccelema_63d_base_v084_signal,
    f32la_f32_leverage_acceleration_debtaccelema_252d_base_v085_signal,
    f32la_f32_leverage_acceleration_deaccelsq_63d_base_v086_signal,
    f32la_f32_leverage_acceleration_deaccelsq_252d_base_v087_signal,
    f32la_f32_leverage_acceleration_debtaccelsq_63d_base_v088_signal,
    f32la_f32_leverage_acceleration_debtaccelsq_252d_base_v089_signal,
    f32la_f32_leverage_acceleration_deaccelarea_63d_base_v090_signal,
    f32la_f32_leverage_acceleration_deaccelarea_252d_base_v091_signal,
    f32la_f32_leverage_acceleration_debtaccelarea_63d_base_v092_signal,
    f32la_f32_leverage_acceleration_debtaccelarea_252d_base_v093_signal,
    f32la_f32_leverage_acceleration_levaccelcomp_63d_base_v094_signal,
    f32la_f32_leverage_acceleration_levaccelcomp_252d_base_v095_signal,
    f32la_f32_leverage_acceleration_deminusdebt_63d_base_v096_signal,
    f32la_f32_leverage_acceleration_deminusdebt_252d_base_v097_signal,
    f32la_f32_leverage_acceleration_deaccelxrevg_63d_base_v098_signal,
    f32la_f32_leverage_acceleration_deaccelxrevg_252d_base_v099_signal,
    f32la_f32_leverage_acceleration_debtaccelxrevg_63d_base_v100_signal,
    f32la_f32_leverage_acceleration_debtaccelxrevg_252d_base_v101_signal,
    f32la_f32_leverage_acceleration_deaccelxepsg_21d_base_v102_signal,
    f32la_f32_leverage_acceleration_deaccelxepsg_252d_base_v103_signal,
    f32la_f32_leverage_acceleration_netdebtxrev_63d_base_v104_signal,
    f32la_f32_leverage_acceleration_netdebtxrev_252d_base_v105_signal,
    f32la_f32_leverage_acceleration_deaccelxqual_63d_base_v106_signal,
    f32la_f32_leverage_acceleration_deaccelxqual_252d_base_v107_signal,
    f32la_f32_leverage_acceleration_devsdebt_63d_base_v108_signal,
    f32la_f32_leverage_acceleration_devsdebt_252d_base_v109_signal,
    f32la_f32_leverage_acceleration_deaccelxavg_252d_base_v110_signal,
    f32la_f32_leverage_acceleration_debtaccelxavg_252d_base_v111_signal,
    f32la_f32_leverage_acceleration_debttoeqxlevel_63d_base_v112_signal,
    f32la_f32_leverage_acceleration_debttoeqxlevel_252d_base_v113_signal,
    f32la_f32_leverage_acceleration_deaccelsignsum_63d_base_v114_signal,
    f32la_f32_leverage_acceleration_deaccelsignsum_252d_base_v115_signal,
    f32la_f32_leverage_acceleration_debtaccelsignsum_63d_base_v116_signal,
    f32la_f32_leverage_acceleration_debtaccelsignsum_252d_base_v117_signal,
    f32la_f32_leverage_acceleration_debtaccelxtax_63d_base_v118_signal,
    f32la_f32_leverage_acceleration_debtaccelxtax_252d_base_v119_signal,
    f32la_f32_leverage_acceleration_debtaccelxintexp_63d_base_v120_signal,
    f32la_f32_leverage_acceleration_debtaccelxintexp_252d_base_v121_signal,
    f32la_f32_leverage_acceleration_debtaccelxretearn_63d_base_v122_signal,
    f32la_f32_leverage_acceleration_debtaccelxretearn_252d_base_v123_signal,
    f32la_f32_leverage_acceleration_liabaccelxintexp_63d_base_v124_signal,
    f32la_f32_leverage_acceleration_liabaccelxintexp_252d_base_v125_signal,
    f32la_f32_leverage_acceleration_debtpsaccelz_252d_base_v126_signal,
    f32la_f32_leverage_acceleration_debtpsaccelz_504d_base_v127_signal,
    f32la_f32_leverage_acceleration_deaccelmulti_base_v128_signal,
    f32la_f32_leverage_acceleration_debtaccelmulti_base_v129_signal,
    f32la_f32_leverage_acceleration_deaccelhealth_63d_base_v130_signal,
    f32la_f32_leverage_acceleration_deaccelhealth_252d_base_v131_signal,
    f32la_f32_leverage_acceleration_debtaccelxnetincg_63d_base_v132_signal,
    f32la_f32_leverage_acceleration_debtaccelxnetincg_252d_base_v133_signal,
    f32la_f32_leverage_acceleration_deaccelanomaly_63d_base_v134_signal,
    f32la_f32_leverage_acceleration_deaccelanomaly_252d_base_v135_signal,
    f32la_f32_leverage_acceleration_debtaccelanomaly_63d_base_v136_signal,
    f32la_f32_leverage_acceleration_debtaccelanomaly_252d_base_v137_signal,
    f32la_f32_leverage_acceleration_intexpaccelxdebt_63d_base_v138_signal,
    f32la_f32_leverage_acceleration_intexpaccelxdebt_252d_base_v139_signal,
    f32la_f32_leverage_acceleration_liabpsxlevel_63d_base_v140_signal,
    f32la_f32_leverage_acceleration_liabpsxlevel_252d_base_v141_signal,
    f32la_f32_leverage_acceleration_jointlevaccel_63d_base_v142_signal,
    f32la_f32_leverage_acceleration_jointlevaccel_252d_base_v143_signal,
    f32la_f32_leverage_acceleration_deaccelxcurdev_63d_base_v144_signal,
    f32la_f32_leverage_acceleration_deaccelxcurdev_252d_base_v145_signal,
    f32la_f32_leverage_acceleration_deminusdebtaccel_63d_base_v146_signal,
    f32la_f32_leverage_acceleration_deminusdebtaccel_252d_base_v147_signal,
    f32la_f32_leverage_acceleration_debtaccelxquality_63d_base_v148_signal,
    f32la_f32_leverage_acceleration_debtaccelxquality_252d_base_v149_signal,
    f32la_f32_leverage_acceleration_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_LEVERAGE_ACCELERATION_REGISTRY_076_150 = REGISTRY


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
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")
    currentratio = fund_walk(0.0001, 0.01, 1.5).rename("currentratio")
    intexp = fund_walk(0.0003, 0.018, 5e6).rename("intexp")
    retearn = fund_walk(0.0005, 0.02, 1e8).rename("retearn")
    liabilities = fund_walk(0.0004, 0.012, 7e8).rename("liabilities")
    taxexp = fund_walk(0.0004, 0.022, 4e6).rename("taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "intexp": intexp, "retearn": retearn, "liabilities": liabilities,
        "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_leverage_accel_de", "_f32_leverage_accel_debt", "_f32_leverage_accel_growth")
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
    print(f"OK f32_leverage_acceleration_base_076_150_claude: {n_features} features pass")
