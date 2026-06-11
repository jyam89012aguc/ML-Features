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
def _f07_ppe_age_proxy(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan).abs()


def _f07_replacement_ratio(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f07_aging_pressure(depamor, ppnenet, w):
    age = depamor / ppnenet.replace(0, np.nan).abs()
    m = age.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = age.rolling(w, min_periods=max(1, w // 2)).std()
    return (age - m) / sd.replace(0, np.nan)


# age * close^2 (21d)
def f07rda_f07_replacement_demand_aging_agexprice_21d_base_v076_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age * close^2 (63d)
def f07rda_f07_replacement_demand_aging_agexprice_63d_base_v077_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age * close^2 (252d)
def f07rda_f07_replacement_demand_aging_agexprice_252d_base_v078_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep * close^2 (21d)
def f07rda_f07_replacement_demand_aging_repxprice_21d_base_v079_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep * close^2 (63d)
def f07rda_f07_replacement_demand_aging_repxprice_63d_base_v080_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep * close^2 (252d)
def f07rda_f07_replacement_demand_aging_repxprice_252d_base_v081_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age * capex / 1e9 (21d)
def f07rda_f07_replacement_demand_aging_agexcap_21d_base_v082_signal(depamor, ppnenet, capex, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base * capex, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# age * capex / 1e9 (63d)
def f07rda_f07_replacement_demand_aging_agexcap_63d_base_v083_signal(depamor, ppnenet, capex, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base * capex, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# age * capex / 1e9 (252d)
def f07rda_f07_replacement_demand_aging_agexcap_252d_base_v084_signal(depamor, ppnenet, capex, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base * capex, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# rep * depamor / 1e9 (21d)
def f07rda_f07_replacement_demand_aging_repxdep_21d_base_v085_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base * depamor, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# rep * depamor / 1e9 (63d)
def f07rda_f07_replacement_demand_aging_repxdep_63d_base_v086_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base * depamor, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# rep * depamor / 1e9 (252d)
def f07rda_f07_replacement_demand_aging_repxdep_252d_base_v087_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base * depamor, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age * rep ratio (cross product mean)
def f07rda_f07_replacement_demand_aging_aoverrep_21d_base_v088_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 21) / _mean(r, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age / rep ratio
def f07rda_f07_replacement_demand_aging_aoverrep_63d_base_v089_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 63) / _mean(r, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age / rep ratio
def f07rda_f07_replacement_demand_aging_aoverrep_252d_base_v090_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 252) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d age / rep ratio
def f07rda_f07_replacement_demand_aging_aoverrep_504d_base_v091_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 504) / _mean(r, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aging_pressure x capex 21d
def f07rda_f07_replacement_demand_aging_pressxcap_21d_base_v092_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 21)
    result = p * capex * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# aging_pressure x capex 63d
def f07rda_f07_replacement_demand_aging_pressxcap_63d_base_v093_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    result = p * capex * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# aging_pressure x capex 252d
def f07rda_f07_replacement_demand_aging_pressxcap_252d_base_v094_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    result = p * capex * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# aging_pressure x depamor 63d
def f07rda_f07_replacement_demand_aging_pressxdep_63d_base_v095_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    result = p * depamor * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# aging_pressure x depamor 252d
def f07rda_f07_replacement_demand_aging_pressxdep_252d_base_v096_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    result = p * depamor * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 5d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_5d_base_v097_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_10d_base_v098_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_21d_base_v099_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_42d_base_v100_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_189d_base_v101_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d aging_pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_378d_base_v102_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age max 21d * closeadj
def f07rda_f07_replacement_demand_aging_agemax_21d_base_v103_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = b.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age max 63d * closeadj
def f07rda_f07_replacement_demand_aging_agemax_63d_base_v104_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = b.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age max 252d * closeadj
def f07rda_f07_replacement_demand_aging_agemax_252d_base_v105_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = b.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age max 504d * closeadj
def f07rda_f07_replacement_demand_aging_agemax_504d_base_v106_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = b.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age min 252d * closeadj
def f07rda_f07_replacement_demand_aging_agemin_252d_base_v107_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = b.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age range 252d * closeadj
def f07rda_f07_replacement_demand_aging_agerng_252d_base_v108_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep range 252d * closeadj
def f07rda_f07_replacement_demand_aging_reprng_252d_base_v109_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep max 252d * closeadj
def f07rda_f07_replacement_demand_aging_repmax_252d_base_v110_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    result = b.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep min 252d * closeadj
def f07rda_f07_replacement_demand_aging_repmin_252d_base_v111_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    result = b.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age percentile 252d * closeadj
def f07rda_f07_replacement_demand_aging_agepct_252d_base_v112_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age percentile 504d * closeadj
def f07rda_f07_replacement_demand_aging_agepct_504d_base_v113_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep percentile 252d * closeadj
def f07rda_f07_replacement_demand_aging_reppct_252d_base_v114_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep percentile 504d * closeadj
def f07rda_f07_replacement_demand_aging_reppct_504d_base_v115_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt age * closeadj
def f07rda_f07_replacement_demand_aging_agesqrt_21d_base_v116_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).abs()
    result = np.sqrt(_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt age * closeadj
def f07rda_f07_replacement_demand_aging_agesqrt_63d_base_v117_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).abs()
    result = np.sqrt(_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt age * closeadj
def f07rda_f07_replacement_demand_aging_agesqrt_252d_base_v118_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).abs()
    result = np.sqrt(_mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt rep * closeadj
def f07rda_f07_replacement_demand_aging_repsqrt_21d_base_v119_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).abs()
    result = np.sqrt(_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt rep * closeadj
def f07rda_f07_replacement_demand_aging_repsqrt_63d_base_v120_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).abs()
    result = np.sqrt(_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt rep * closeadj
def f07rda_f07_replacement_demand_aging_repsqrt_252d_base_v121_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).abs()
    result = np.sqrt(_mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age CV * closeadj
def f07rda_f07_replacement_demand_aging_agecv_21d_base_v122_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 21) / _mean(b, 21).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age CV * closeadj
def f07rda_f07_replacement_demand_aging_agecv_63d_base_v123_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age CV * closeadj
def f07rda_f07_replacement_demand_aging_agecv_252d_base_v124_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rep CV * closeadj
def f07rda_f07_replacement_demand_aging_repcv_63d_base_v125_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rep CV * closeadj
def f07rda_f07_replacement_demand_aging_repcv_252d_base_v126_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sign of (age - mean) * std * close
def f07rda_f07_replacement_demand_aging_agesign_63d_base_v127_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    dev = b - _mean(b, 252)
    result = np.sign(dev) * _std(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sign of (rep - mean) * std * close
def f07rda_f07_replacement_demand_aging_repsign_63d_base_v128_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    dev = b - _mean(b, 252)
    result = np.sign(dev) * _std(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite aging+rep z 63d
def f07rda_f07_replacement_demand_aging_compz_63d_base_v129_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    r = _f07_replacement_ratio(capex, depamor)
    result = (p + _z(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite aging+rep z 252d
def f07rda_f07_replacement_demand_aging_compz_252d_base_v130_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    r = _f07_replacement_ratio(capex, depamor)
    result = (p + _z(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite aging+rep z 504d
def f07rda_f07_replacement_demand_aging_compz_504d_base_v131_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    r = _f07_replacement_ratio(capex, depamor)
    result = (p + _z(r, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age ratio 21v252 * closeadj
def f07rda_f07_replacement_demand_aging_ageratio_21v252_base_v132_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age ratio 63v252 * closeadj
def f07rda_f07_replacement_demand_aging_ageratio_63v252_base_v133_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age ratio 63v504 * closeadj
def f07rda_f07_replacement_demand_aging_ageratio_63v504_base_v134_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep ratio 21v252 * closeadj
def f07rda_f07_replacement_demand_aging_repratio_21v252_base_v135_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    result = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep ratio 63v252 * closeadj
def f07rda_f07_replacement_demand_aging_repratio_63v252_base_v136_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    result = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rep ratio 63v504 * closeadj
def f07rda_f07_replacement_demand_aging_repratio_63v504_base_v137_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    result = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pressure * close return 21d
def f07rda_f07_replacement_demand_aging_pressxcret_21d_base_v138_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 21)
    cret = closeadj.pct_change(21)
    result = p * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pressure * close return 63d
def f07rda_f07_replacement_demand_aging_pressxcret_63d_base_v139_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    cret = closeadj.pct_change(63)
    result = p * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pressure * close return 252d
def f07rda_f07_replacement_demand_aging_pressxcret_252d_base_v140_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    cret = closeadj.pct_change(252)
    result = p * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# age * volume proxy (close cumulative)
def f07rda_f07_replacement_demand_aging_agexcumvol_63d_base_v141_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _mean(closeadj, 63) * closeadj
    result = _mean(b, 63) * cv
    return result.replace([np.inf, -np.inf], np.nan)


# rep * close cumulative weight
def f07rda_f07_replacement_demand_aging_repxcumvol_63d_base_v142_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _mean(closeadj, 63) * closeadj
    result = _mean(b, 63) * cv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d under-investment indicator (rep<1) * closeadj
def f07rda_f07_replacement_demand_aging_underinv_252d_base_v143_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    under = (b < 1.0).astype(float)
    result = (_mean(under, 252) + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d under-investment * closeadj
def f07rda_f07_replacement_demand_aging_underinv_504d_base_v144_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    under = (b < 1.0).astype(float)
    result = (_mean(under, 504) + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d over-investment (rep>1.5) * closeadj
def f07rda_f07_replacement_demand_aging_overinv_252d_base_v145_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    over = (b > 1.5).astype(float)
    result = (_mean(over, 252) + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d over-investment * closeadj
def f07rda_f07_replacement_demand_aging_overinv_504d_base_v146_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    over = (b > 1.5).astype(float)
    result = (_mean(over, 504) + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pressure_252d squared * close
def f07rda_f07_replacement_demand_aging_presssq_504d_base_v147_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    result = p * p.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite (age + rep) ema 63d
def f07rda_f07_replacement_demand_aging_compema_63d_base_v148_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (a + r).ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite (age + rep) ema 252d
def f07rda_f07_replacement_demand_aging_compema_252d_base_v149_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (a + r).ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# global aging composite 504d
def f07rda_f07_replacement_demand_aging_globcomp_504d_base_v150_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    base = _mean(a, 504) + _mean(r, 504) + p
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07rda_f07_replacement_demand_aging_agexprice_21d_base_v076_signal,
    f07rda_f07_replacement_demand_aging_agexprice_63d_base_v077_signal,
    f07rda_f07_replacement_demand_aging_agexprice_252d_base_v078_signal,
    f07rda_f07_replacement_demand_aging_repxprice_21d_base_v079_signal,
    f07rda_f07_replacement_demand_aging_repxprice_63d_base_v080_signal,
    f07rda_f07_replacement_demand_aging_repxprice_252d_base_v081_signal,
    f07rda_f07_replacement_demand_aging_agexcap_21d_base_v082_signal,
    f07rda_f07_replacement_demand_aging_agexcap_63d_base_v083_signal,
    f07rda_f07_replacement_demand_aging_agexcap_252d_base_v084_signal,
    f07rda_f07_replacement_demand_aging_repxdep_21d_base_v085_signal,
    f07rda_f07_replacement_demand_aging_repxdep_63d_base_v086_signal,
    f07rda_f07_replacement_demand_aging_repxdep_252d_base_v087_signal,
    f07rda_f07_replacement_demand_aging_aoverrep_21d_base_v088_signal,
    f07rda_f07_replacement_demand_aging_aoverrep_63d_base_v089_signal,
    f07rda_f07_replacement_demand_aging_aoverrep_252d_base_v090_signal,
    f07rda_f07_replacement_demand_aging_aoverrep_504d_base_v091_signal,
    f07rda_f07_replacement_demand_aging_pressxcap_21d_base_v092_signal,
    f07rda_f07_replacement_demand_aging_pressxcap_63d_base_v093_signal,
    f07rda_f07_replacement_demand_aging_pressxcap_252d_base_v094_signal,
    f07rda_f07_replacement_demand_aging_pressxdep_63d_base_v095_signal,
    f07rda_f07_replacement_demand_aging_pressxdep_252d_base_v096_signal,
    f07rda_f07_replacement_demand_aging_press_5d_base_v097_signal,
    f07rda_f07_replacement_demand_aging_press_10d_base_v098_signal,
    f07rda_f07_replacement_demand_aging_press_21d_base_v099_signal,
    f07rda_f07_replacement_demand_aging_press_42d_base_v100_signal,
    f07rda_f07_replacement_demand_aging_press_189d_base_v101_signal,
    f07rda_f07_replacement_demand_aging_press_378d_base_v102_signal,
    f07rda_f07_replacement_demand_aging_agemax_21d_base_v103_signal,
    f07rda_f07_replacement_demand_aging_agemax_63d_base_v104_signal,
    f07rda_f07_replacement_demand_aging_agemax_252d_base_v105_signal,
    f07rda_f07_replacement_demand_aging_agemax_504d_base_v106_signal,
    f07rda_f07_replacement_demand_aging_agemin_252d_base_v107_signal,
    f07rda_f07_replacement_demand_aging_agerng_252d_base_v108_signal,
    f07rda_f07_replacement_demand_aging_reprng_252d_base_v109_signal,
    f07rda_f07_replacement_demand_aging_repmax_252d_base_v110_signal,
    f07rda_f07_replacement_demand_aging_repmin_252d_base_v111_signal,
    f07rda_f07_replacement_demand_aging_agepct_252d_base_v112_signal,
    f07rda_f07_replacement_demand_aging_agepct_504d_base_v113_signal,
    f07rda_f07_replacement_demand_aging_reppct_252d_base_v114_signal,
    f07rda_f07_replacement_demand_aging_reppct_504d_base_v115_signal,
    f07rda_f07_replacement_demand_aging_agesqrt_21d_base_v116_signal,
    f07rda_f07_replacement_demand_aging_agesqrt_63d_base_v117_signal,
    f07rda_f07_replacement_demand_aging_agesqrt_252d_base_v118_signal,
    f07rda_f07_replacement_demand_aging_repsqrt_21d_base_v119_signal,
    f07rda_f07_replacement_demand_aging_repsqrt_63d_base_v120_signal,
    f07rda_f07_replacement_demand_aging_repsqrt_252d_base_v121_signal,
    f07rda_f07_replacement_demand_aging_agecv_21d_base_v122_signal,
    f07rda_f07_replacement_demand_aging_agecv_63d_base_v123_signal,
    f07rda_f07_replacement_demand_aging_agecv_252d_base_v124_signal,
    f07rda_f07_replacement_demand_aging_repcv_63d_base_v125_signal,
    f07rda_f07_replacement_demand_aging_repcv_252d_base_v126_signal,
    f07rda_f07_replacement_demand_aging_agesign_63d_base_v127_signal,
    f07rda_f07_replacement_demand_aging_repsign_63d_base_v128_signal,
    f07rda_f07_replacement_demand_aging_compz_63d_base_v129_signal,
    f07rda_f07_replacement_demand_aging_compz_252d_base_v130_signal,
    f07rda_f07_replacement_demand_aging_compz_504d_base_v131_signal,
    f07rda_f07_replacement_demand_aging_ageratio_21v252_base_v132_signal,
    f07rda_f07_replacement_demand_aging_ageratio_63v252_base_v133_signal,
    f07rda_f07_replacement_demand_aging_ageratio_63v504_base_v134_signal,
    f07rda_f07_replacement_demand_aging_repratio_21v252_base_v135_signal,
    f07rda_f07_replacement_demand_aging_repratio_63v252_base_v136_signal,
    f07rda_f07_replacement_demand_aging_repratio_63v504_base_v137_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_21d_base_v138_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_63d_base_v139_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_252d_base_v140_signal,
    f07rda_f07_replacement_demand_aging_agexcumvol_63d_base_v141_signal,
    f07rda_f07_replacement_demand_aging_repxcumvol_63d_base_v142_signal,
    f07rda_f07_replacement_demand_aging_underinv_252d_base_v143_signal,
    f07rda_f07_replacement_demand_aging_underinv_504d_base_v144_signal,
    f07rda_f07_replacement_demand_aging_overinv_252d_base_v145_signal,
    f07rda_f07_replacement_demand_aging_overinv_504d_base_v146_signal,
    f07rda_f07_replacement_demand_aging_presssq_504d_base_v147_signal,
    f07rda_f07_replacement_demand_aging_compema_63d_base_v148_signal,
    f07rda_f07_replacement_demand_aging_compema_252d_base_v149_signal,
    f07rda_f07_replacement_demand_aging_globcomp_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_REPLACEMENT_DEMAND_AGING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {"closeadj": closeadj, "depamor": depamor, "ppnenet": ppnenet, "capex": capex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_ppe_age_proxy", "_f07_replacement_ratio", "_f07_aging_pressure")
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
    print(f"OK f07_replacement_demand_aging_base_076_150_claude: {n_features} features pass")
