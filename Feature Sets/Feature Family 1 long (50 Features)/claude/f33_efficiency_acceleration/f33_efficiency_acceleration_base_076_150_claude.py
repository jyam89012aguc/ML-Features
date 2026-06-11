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


# ===== folder domain primitives =====
def _f33_efficiency_accel_assetturn(revenue, assets, w):
    at = revenue / assets.replace(0, np.nan)
    g = _diff(at, w) / at.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f33_efficiency_accel_eqturn(revenue, equity, w):
    eqt = revenue / equity.replace(0, np.nan)
    g = _diff(eqt, w) / eqt.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f33_efficiency_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 21d asset turnover accel × debt
def f33ea_f33_efficiency_acceleration_atrnaccelxdebt_21d_base_v076_signal(revenue, assets, debt, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 21) * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × debt
def f33ea_f33_efficiency_acceleration_atrnaccelxdebt_252d_base_v077_signal(revenue, assets, debt, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current ratio
def f33ea_f33_efficiency_acceleration_atrnaccelxcur_63d_base_v078_signal(revenue, assets, currentratio, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × current ratio
def f33ea_f33_efficiency_acceleration_atrnaccelxcur_252d_base_v079_signal(revenue, assets, currentratio, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of revenue/sharesbas × sharesbas
def f33ea_f33_efficiency_acceleration_revshareintensity_63d_base_v080_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of revenue/sharesbas × sharesbas
def f33ea_f33_efficiency_acceleration_revshareintensity_252d_base_v081_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel EMA(63d)
def f33ea_f33_efficiency_acceleration_atrnaccelema_63d_base_v082_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel EMA(252d)
def f33ea_f33_efficiency_acceleration_atrnaccelema_252d_base_v083_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eq turnover accel EMA(63d)
def f33ea_f33_efficiency_acceleration_eqtrnaccelema_63d_base_v084_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel EMA(252d)
def f33ea_f33_efficiency_acceleration_eqtrnaccelema_252d_base_v085_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel signed × magnitude
def f33ea_f33_efficiency_acceleration_atrnaccelsq_63d_base_v086_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel signed × magnitude
def f33ea_f33_efficiency_acceleration_atrnaccelsq_252d_base_v087_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel signed × magnitude
def f33ea_f33_efficiency_acceleration_eqtrnaccelsq_63d_base_v088_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel signed × magnitude
def f33ea_f33_efficiency_acceleration_eqtrnaccelsq_252d_base_v089_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel area sum
def f33ea_f33_efficiency_acceleration_atrnaccelarea_63d_base_v090_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel area sum
def f33ea_f33_efficiency_acceleration_atrnaccelarea_252d_base_v091_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel area sum
def f33ea_f33_efficiency_acceleration_eqtrnaccelarea_63d_base_v092_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel area sum
def f33ea_f33_efficiency_acceleration_eqtrnaccelarea_252d_base_v093_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d combined turnover accel composite
def f33ea_f33_efficiency_acceleration_turncombo_63d_base_v094_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d combined turnover accel composite
def f33ea_f33_efficiency_acceleration_turncombo_252d_base_v095_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel - eq turnover accel divergence
def f33ea_f33_efficiency_acceleration_atrnminuseq_63d_base_v096_signal(revenue, assets, equity, closeadj):
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 63) - _f33_efficiency_accel_eqturn(revenue, equity, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel - eq turnover accel divergence
def f33ea_f33_efficiency_acceleration_atrnminuseq_252d_base_v097_signal(revenue, assets, equity, closeadj):
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 252) - _f33_efficiency_accel_eqturn(revenue, equity, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × revenue growth
def f33ea_f33_efficiency_acceleration_atrnaccelxrevg_63d_base_v098_signal(revenue, assets, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × revenue growth
def f33ea_f33_efficiency_acceleration_atrnaccelxrevg_252d_base_v099_signal(revenue, assets, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel × revenue growth
def f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_63d_base_v100_signal(revenue, equity, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_eqturn(revenue, equity, 63) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × revenue growth
def f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_252d_base_v101_signal(revenue, equity, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_eqturn(revenue, equity, 252) * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel × eps growth
def f33ea_f33_efficiency_acceleration_atrnaccelxepsg_21d_base_v102_signal(revenue, assets, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 21) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × eps growth
def f33ea_f33_efficiency_acceleration_atrnaccelxepsg_252d_base_v103_signal(revenue, assets, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of (gp - capex) / revenue
def f33ea_f33_efficiency_acceleration_gpmcapxratio_63d_base_v104_signal(gp, capex, revenue, closeadj):
    s = (gp - capex) / revenue.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of (gp - capex) / revenue
def f33ea_f33_efficiency_acceleration_gpmcapxratio_252d_base_v105_signal(gp, capex, revenue, closeadj):
    s = (gp - capex) / revenue.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × FCF/EBITDA quality
def f33ea_f33_efficiency_acceleration_atrnaccelxqual_63d_base_v106_signal(revenue, assets, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × FCF/EBITDA quality
def f33ea_f33_efficiency_acceleration_atrnaccelxqual_252d_base_v107_signal(revenue, assets, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel ÷ eq turnover accel
def f33ea_f33_efficiency_acceleration_atrnvseq_63d_base_v108_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel ÷ eq turnover accel
def f33ea_f33_efficiency_acceleration_atrnvseq_252d_base_v109_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel rolling 252d mean
def f33ea_f33_efficiency_acceleration_atrnaccelxavg_252d_base_v110_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel rolling mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelxavg_252d_base_v111_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current asset level
def f33ea_f33_efficiency_acceleration_atrnxasset_63d_base_v112_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = a * assets.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × current equity level
def f33ea_f33_efficiency_acceleration_eqtrnxeq_252d_base_v113_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = a * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel sign rolling sum 63d
def f33ea_f33_efficiency_acceleration_atrnaccelsignsum_63d_base_v114_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel sign rolling sum 252d
def f33ea_f33_efficiency_acceleration_atrnaccelsignsum_252d_base_v115_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eq turnover accel sign rolling sum 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_63d_base_v116_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    sg = np.sign(a)
    result = sg.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eq turnover accel sign rolling sum 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_252d_base_v117_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    sg = np.sign(a)
    result = sg.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × tax expense
def f33ea_f33_efficiency_acceleration_atrnaccelxtax_63d_base_v118_signal(revenue, assets, taxexp, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × tax expense
def f33ea_f33_efficiency_acceleration_atrnaccelxtax_252d_base_v119_signal(revenue, assets, taxexp, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * taxexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel × interest expense
def f33ea_f33_efficiency_acceleration_eqtrnaccelxint_63d_base_v120_signal(revenue, equity, intexp, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 63) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × interest expense
def f33ea_f33_efficiency_acceleration_eqtrnaccelxint_252d_base_v121_signal(revenue, equity, intexp, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 252) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × retained earnings
def f33ea_f33_efficiency_acceleration_atrnaccelxretearn_63d_base_v122_signal(revenue, assets, retearn, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × retained earnings
def f33ea_f33_efficiency_acceleration_atrnaccelxretearn_252d_base_v123_signal(revenue, assets, retearn, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * retearn.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel × liabilities
def f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_63d_base_v124_signal(revenue, equity, liabilities, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 63) * liabilities.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × liabilities
def f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_252d_base_v125_signal(revenue, equity, liabilities, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 252) * liabilities.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of revenue/sharesbas zscore 252d
def f33ea_f33_efficiency_acceleration_revpsaccelz_252d_base_v126_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of revenue/sharesbas zscore 504d
def f33ea_f33_efficiency_acceleration_revpsaccelz_504d_base_v127_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window asset turnover accel composite
def f33ea_f33_efficiency_acceleration_atrnaccelmulti_base_v128_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    b = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    c = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window eq turnover accel composite
def f33ea_f33_efficiency_acceleration_eqtrnaccelmulti_base_v129_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    c = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current ratio × revenue
def f33ea_f33_efficiency_acceleration_atrnhealth_63d_base_v130_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × current ratio × revenue
def f33ea_f33_efficiency_acceleration_atrnhealth_252d_base_v131_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    result = a * currentratio * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × netinc growth
def f33ea_f33_efficiency_acceleration_atrnaccelxnig_63d_base_v132_signal(revenue, assets, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × netinc growth
def f33ea_f33_efficiency_acceleration_atrnaccelxnig_252d_base_v133_signal(revenue, assets, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel - expanding mean (anomaly)
def f33ea_f33_efficiency_acceleration_atrnaccelanomaly_63d_base_v134_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel - expanding mean
def f33ea_f33_efficiency_acceleration_atrnaccelanomaly_252d_base_v135_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel - expanding mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelanomaly_63d_base_v136_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = a.expanding(min_periods=63).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel - expanding mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelanomaly_252d_base_v137_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = a.expanding(min_periods=126).mean()
    result = (a - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EBITDA accel × asset turnover
def f33ea_f33_efficiency_acceleration_ebitdaaccelxat_63d_base_v138_signal(ebitda, revenue, assets, closeadj):
    a = _f33_efficiency_accel_growth(ebitda, 63)
    at = revenue / assets.replace(0, np.nan)
    result = a * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EBITDA accel × asset turnover
def f33ea_f33_efficiency_acceleration_ebitdaaccelxat_252d_base_v139_signal(ebitda, revenue, assets, closeadj):
    a = _f33_efficiency_accel_growth(ebitda, 252)
    at = revenue / assets.replace(0, np.nan)
    result = a * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of opinc/sharesbas × sharesbas
def f33ea_f33_efficiency_acceleration_opincpsxlevel_63d_base_v140_signal(opinc, sharesbas, closeadj):
    s = opinc / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of opinc/sharesbas × sharesbas
def f33ea_f33_efficiency_acceleration_opincpsxlevel_252d_base_v141_signal(opinc, sharesbas, closeadj):
    s = opinc / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    result = a * sharesbas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × eq turnover accel (joint)
def f33ea_f33_efficiency_acceleration_jointeffaccel_63d_base_v142_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × eq turnover accel
def f33ea_f33_efficiency_acceleration_jointeffaccel_252d_base_v143_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current ratio deviation
def f33ea_f33_efficiency_acceleration_atrnaccelxcurdev_63d_base_v144_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    dev = currentratio - _mean(currentratio, 252)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × current ratio deviation
def f33ea_f33_efficiency_acceleration_atrnaccelxcurdev_252d_base_v145_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    dev = currentratio - _mean(currentratio, 504)
    result = a * dev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel - 63d EBITDA/asset accel divergence
def f33ea_f33_efficiency_acceleration_atrnminusebitda_63d_base_v146_signal(revenue, assets, ebitda, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 63) - _f33_efficiency_accel_growth(s, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel - 252d EBITDA/asset accel
def f33ea_f33_efficiency_acceleration_atrnminusebitda_252d_base_v147_signal(revenue, assets, ebitda, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 252) - _f33_efficiency_accel_growth(s, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel × ROE quality
def f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_63d_base_v148_signal(revenue, equity, netinc, closeadj):
    q = netinc / equity.replace(0, np.nan)
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × ROE quality
def f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_252d_base_v149_signal(revenue, equity, netinc, closeadj):
    q = netinc / equity.replace(0, np.nan)
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    result = a * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite efficiency severity 252d: asset + eq turnover + ROA accel area
def f33ea_f33_efficiency_acceleration_compositesev_252d_base_v150_signal(revenue, assets, equity, netinc, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    s_roa = netinc / assets.replace(0, np.nan)
    c = _f33_efficiency_accel_growth(s_roa, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ea_f33_efficiency_acceleration_atrnaccelxdebt_21d_base_v076_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxdebt_252d_base_v077_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcur_63d_base_v078_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcur_252d_base_v079_signal,
    f33ea_f33_efficiency_acceleration_revshareintensity_63d_base_v080_signal,
    f33ea_f33_efficiency_acceleration_revshareintensity_252d_base_v081_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelema_63d_base_v082_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelema_252d_base_v083_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelema_63d_base_v084_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelema_252d_base_v085_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsq_63d_base_v086_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsq_252d_base_v087_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsq_63d_base_v088_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsq_252d_base_v089_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelarea_63d_base_v090_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelarea_252d_base_v091_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelarea_63d_base_v092_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelarea_252d_base_v093_signal,
    f33ea_f33_efficiency_acceleration_turncombo_63d_base_v094_signal,
    f33ea_f33_efficiency_acceleration_turncombo_252d_base_v095_signal,
    f33ea_f33_efficiency_acceleration_atrnminuseq_63d_base_v096_signal,
    f33ea_f33_efficiency_acceleration_atrnminuseq_252d_base_v097_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrevg_63d_base_v098_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrevg_252d_base_v099_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_63d_base_v100_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_252d_base_v101_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxepsg_21d_base_v102_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxepsg_252d_base_v103_signal,
    f33ea_f33_efficiency_acceleration_gpmcapxratio_63d_base_v104_signal,
    f33ea_f33_efficiency_acceleration_gpmcapxratio_252d_base_v105_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxqual_63d_base_v106_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxqual_252d_base_v107_signal,
    f33ea_f33_efficiency_acceleration_atrnvseq_63d_base_v108_signal,
    f33ea_f33_efficiency_acceleration_atrnvseq_252d_base_v109_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxavg_252d_base_v110_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxavg_252d_base_v111_signal,
    f33ea_f33_efficiency_acceleration_atrnxasset_63d_base_v112_signal,
    f33ea_f33_efficiency_acceleration_eqtrnxeq_252d_base_v113_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsignsum_63d_base_v114_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsignsum_252d_base_v115_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_63d_base_v116_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_252d_base_v117_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxtax_63d_base_v118_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxtax_252d_base_v119_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxint_63d_base_v120_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxint_252d_base_v121_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxretearn_63d_base_v122_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxretearn_252d_base_v123_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_63d_base_v124_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_252d_base_v125_signal,
    f33ea_f33_efficiency_acceleration_revpsaccelz_252d_base_v126_signal,
    f33ea_f33_efficiency_acceleration_revpsaccelz_504d_base_v127_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmulti_base_v128_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmulti_base_v129_signal,
    f33ea_f33_efficiency_acceleration_atrnhealth_63d_base_v130_signal,
    f33ea_f33_efficiency_acceleration_atrnhealth_252d_base_v131_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxnig_63d_base_v132_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxnig_252d_base_v133_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelanomaly_63d_base_v134_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelanomaly_252d_base_v135_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelanomaly_63d_base_v136_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelanomaly_252d_base_v137_signal,
    f33ea_f33_efficiency_acceleration_ebitdaaccelxat_63d_base_v138_signal,
    f33ea_f33_efficiency_acceleration_ebitdaaccelxat_252d_base_v139_signal,
    f33ea_f33_efficiency_acceleration_opincpsxlevel_63d_base_v140_signal,
    f33ea_f33_efficiency_acceleration_opincpsxlevel_252d_base_v141_signal,
    f33ea_f33_efficiency_acceleration_jointeffaccel_63d_base_v142_signal,
    f33ea_f33_efficiency_acceleration_jointeffaccel_252d_base_v143_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcurdev_63d_base_v144_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcurdev_252d_base_v145_signal,
    f33ea_f33_efficiency_acceleration_atrnminusebitda_63d_base_v146_signal,
    f33ea_f33_efficiency_acceleration_atrnminusebitda_252d_base_v147_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_63d_base_v148_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_252d_base_v149_signal,
    f33ea_f33_efficiency_acceleration_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EFFICIENCY_ACCELERATION_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f33_efficiency_accel_assetturn", "_f33_efficiency_accel_eqturn", "_f33_efficiency_accel_growth")
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
    print(f"OK f33_efficiency_acceleration_base_076_150_claude: {n_features} features pass")
