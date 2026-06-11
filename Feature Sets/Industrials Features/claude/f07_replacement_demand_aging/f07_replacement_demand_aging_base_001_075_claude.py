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
    # accumulated depreciation proxy / ppe ~= age fraction
    return depamor / ppnenet.replace(0, np.nan).abs()


def _f07_replacement_ratio(capex, depamor):
    # capex / depreciation: <1 under-investing, >1 expanding
    return capex / depamor.replace(0, np.nan).abs()


def _f07_aging_pressure(depamor, ppnenet, w):
    age = depamor / ppnenet.replace(0, np.nan).abs()
    m = age.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = age.rolling(w, min_periods=max(1, w // 2)).std()
    return (age - m) / sd.replace(0, np.nan)


# 21d mean age proxy * closeadj
def f07rda_f07_replacement_demand_aging_age_21d_base_v001_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean age proxy * closeadj
def f07rda_f07_replacement_demand_aging_age_63d_base_v002_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean age * closeadj
def f07rda_f07_replacement_demand_aging_age_126d_base_v003_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean age * closeadj
def f07rda_f07_replacement_demand_aging_age_252d_base_v004_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean age * closeadj
def f07rda_f07_replacement_demand_aging_age_504d_base_v005_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean replacement ratio * closeadj
def f07rda_f07_replacement_demand_aging_rep_21d_base_v006_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean replacement ratio * closeadj
def f07rda_f07_replacement_demand_aging_rep_63d_base_v007_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_rep_126d_base_v008_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_rep_252d_base_v009_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_rep_504d_base_v010_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d aging pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_63d_base_v011_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d aging pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_126d_base_v012_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d aging pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_252d_base_v013_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d aging pressure * closeadj
def f07rda_f07_replacement_demand_aging_press_504d_base_v014_signal(depamor, ppnenet, closeadj):
    result = _f07_aging_pressure(depamor, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std age * closeadj
def f07rda_f07_replacement_demand_aging_agestd_21d_base_v015_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std age * closeadj
def f07rda_f07_replacement_demand_aging_agestd_63d_base_v016_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std age * closeadj
def f07rda_f07_replacement_demand_aging_agestd_252d_base_v017_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std age * closeadj
def f07rda_f07_replacement_demand_aging_agestd_504d_base_v018_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repstd_21d_base_v019_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repstd_63d_base_v020_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repstd_252d_base_v021_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repstd_504d_base_v022_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z age * closeadj
def f07rda_f07_replacement_demand_aging_agez_21d_base_v023_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z age * closeadj
def f07rda_f07_replacement_demand_aging_agez_63d_base_v024_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z age * closeadj
def f07rda_f07_replacement_demand_aging_agez_252d_base_v025_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z age * closeadj
def f07rda_f07_replacement_demand_aging_agez_504d_base_v026_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repz_21d_base_v027_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repz_63d_base_v028_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repz_252d_base_v029_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z rep ratio * closeadj
def f07rda_f07_replacement_demand_aging_repz_504d_base_v030_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d age * closeadj
def f07rda_f07_replacement_demand_aging_age_5d_base_v031_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d age * closeadj
def f07rda_f07_replacement_demand_aging_age_10d_base_v032_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d age * closeadj
def f07rda_f07_replacement_demand_aging_age_42d_base_v033_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d age * closeadj
def f07rda_f07_replacement_demand_aging_age_189d_base_v034_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d age * closeadj
def f07rda_f07_replacement_demand_aging_age_378d_base_v035_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d rep * closeadj
def f07rda_f07_replacement_demand_aging_rep_5d_base_v036_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d rep * closeadj
def f07rda_f07_replacement_demand_aging_rep_10d_base_v037_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rep * closeadj
def f07rda_f07_replacement_demand_aging_rep_42d_base_v038_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rep * closeadj
def f07rda_f07_replacement_demand_aging_rep_189d_base_v039_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d rep * closeadj
def f07rda_f07_replacement_demand_aging_rep_378d_base_v040_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA age * closeadj
def f07rda_f07_replacement_demand_aging_ageema_21d_base_v041_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA age * closeadj
def f07rda_f07_replacement_demand_aging_ageema_63d_base_v042_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA age * closeadj
def f07rda_f07_replacement_demand_aging_ageema_252d_base_v043_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA rep * closeadj
def f07rda_f07_replacement_demand_aging_repema_21d_base_v044_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA rep * closeadj
def f07rda_f07_replacement_demand_aging_repema_63d_base_v045_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA rep * closeadj
def f07rda_f07_replacement_demand_aging_repema_252d_base_v046_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age gap vs 252d * closeadj
def f07rda_f07_replacement_demand_aging_agegap_21v252_base_v047_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age gap vs 252d * closeadj
def f07rda_f07_replacement_demand_aging_agegap_63v252_base_v048_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age gap vs 504d * closeadj
def f07rda_f07_replacement_demand_aging_agegap_63v504_base_v049_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(base, 63) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d age gap vs 504d * closeadj
def f07rda_f07_replacement_demand_aging_agegap_126v504_base_v050_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = (_mean(base, 126) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rep gap vs 252d
def f07rda_f07_replacement_demand_aging_repgap_21v252_base_v051_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rep gap vs 252d
def f07rda_f07_replacement_demand_aging_repgap_63v252_base_v052_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rep gap vs 504d
def f07rda_f07_replacement_demand_aging_repgap_63v504_base_v053_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = (_mean(base, 63) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rep gap vs 504d
def f07rda_f07_replacement_demand_aging_repgap_126v504_base_v054_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = (_mean(base, 126) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d aging pressure * rep
def f07rda_f07_replacement_demand_aging_pressxrep_21d_base_v055_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 21)
    r = _f07_replacement_ratio(capex, depamor)
    result = p * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d aging pressure * rep
def f07rda_f07_replacement_demand_aging_pressxrep_63d_base_v056_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    r = _f07_replacement_ratio(capex, depamor)
    result = p * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d aging pressure * rep
def f07rda_f07_replacement_demand_aging_pressxrep_252d_base_v057_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    r = _f07_replacement_ratio(capex, depamor)
    result = p * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d aging pressure * rep
def f07rda_f07_replacement_demand_aging_pressxrep_504d_base_v058_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    r = _f07_replacement_ratio(capex, depamor)
    result = p * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age / rep ratio
def f07rda_f07_replacement_demand_aging_ageovrep_21v252_base_v059_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 21) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age / rep ratio
def f07rda_f07_replacement_demand_aging_ageovrep_63v252_base_v060_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 63) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age / rep ratio
def f07rda_f07_replacement_demand_aging_ageovrep_252v252_base_v061_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 252) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age + rep composite
def f07rda_f07_replacement_demand_aging_comp_21d_base_v062_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 21) + _mean(r, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age + rep composite
def f07rda_f07_replacement_demand_aging_comp_63d_base_v063_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 63) + _mean(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age + rep composite
def f07rda_f07_replacement_demand_aging_comp_252d_base_v064_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 252) + _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d age + rep composite
def f07rda_f07_replacement_demand_aging_comp_504d_base_v065_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 504) + _mean(r, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age - rep diff
def f07rda_f07_replacement_demand_aging_diff_21d_base_v066_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 21) - _mean(r, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age - rep diff
def f07rda_f07_replacement_demand_aging_diff_63d_base_v067_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 63) - _mean(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age - rep diff
def f07rda_f07_replacement_demand_aging_diff_252d_base_v068_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 252) - _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d age - rep diff
def f07rda_f07_replacement_demand_aging_diff_504d_base_v069_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = (_mean(a, 504) - _mean(r, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d age * rep multiplier
def f07rda_f07_replacement_demand_aging_agexrep_21d_base_v070_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = _mean(a * r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d age * rep multiplier
def f07rda_f07_replacement_demand_aging_agexrep_63d_base_v071_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = _mean(a * r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d age * rep multiplier
def f07rda_f07_replacement_demand_aging_agexrep_252d_base_v072_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    result = _mean(a * r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log age * closeadj
def f07rda_f07_replacement_demand_aging_agelog_63d_base_v073_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet)
    result = np.log(_mean(base, 63).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log rep * closeadj
def f07rda_f07_replacement_demand_aging_replog_252d_base_v074_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor)
    result = np.log(_mean(base, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pressure squared
def f07rda_f07_replacement_demand_aging_presssq_252d_base_v075_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    result = p * p.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07rda_f07_replacement_demand_aging_age_21d_base_v001_signal,
    f07rda_f07_replacement_demand_aging_age_63d_base_v002_signal,
    f07rda_f07_replacement_demand_aging_age_126d_base_v003_signal,
    f07rda_f07_replacement_demand_aging_age_252d_base_v004_signal,
    f07rda_f07_replacement_demand_aging_age_504d_base_v005_signal,
    f07rda_f07_replacement_demand_aging_rep_21d_base_v006_signal,
    f07rda_f07_replacement_demand_aging_rep_63d_base_v007_signal,
    f07rda_f07_replacement_demand_aging_rep_126d_base_v008_signal,
    f07rda_f07_replacement_demand_aging_rep_252d_base_v009_signal,
    f07rda_f07_replacement_demand_aging_rep_504d_base_v010_signal,
    f07rda_f07_replacement_demand_aging_press_63d_base_v011_signal,
    f07rda_f07_replacement_demand_aging_press_126d_base_v012_signal,
    f07rda_f07_replacement_demand_aging_press_252d_base_v013_signal,
    f07rda_f07_replacement_demand_aging_press_504d_base_v014_signal,
    f07rda_f07_replacement_demand_aging_agestd_21d_base_v015_signal,
    f07rda_f07_replacement_demand_aging_agestd_63d_base_v016_signal,
    f07rda_f07_replacement_demand_aging_agestd_252d_base_v017_signal,
    f07rda_f07_replacement_demand_aging_agestd_504d_base_v018_signal,
    f07rda_f07_replacement_demand_aging_repstd_21d_base_v019_signal,
    f07rda_f07_replacement_demand_aging_repstd_63d_base_v020_signal,
    f07rda_f07_replacement_demand_aging_repstd_252d_base_v021_signal,
    f07rda_f07_replacement_demand_aging_repstd_504d_base_v022_signal,
    f07rda_f07_replacement_demand_aging_agez_21d_base_v023_signal,
    f07rda_f07_replacement_demand_aging_agez_63d_base_v024_signal,
    f07rda_f07_replacement_demand_aging_agez_252d_base_v025_signal,
    f07rda_f07_replacement_demand_aging_agez_504d_base_v026_signal,
    f07rda_f07_replacement_demand_aging_repz_21d_base_v027_signal,
    f07rda_f07_replacement_demand_aging_repz_63d_base_v028_signal,
    f07rda_f07_replacement_demand_aging_repz_252d_base_v029_signal,
    f07rda_f07_replacement_demand_aging_repz_504d_base_v030_signal,
    f07rda_f07_replacement_demand_aging_age_5d_base_v031_signal,
    f07rda_f07_replacement_demand_aging_age_10d_base_v032_signal,
    f07rda_f07_replacement_demand_aging_age_42d_base_v033_signal,
    f07rda_f07_replacement_demand_aging_age_189d_base_v034_signal,
    f07rda_f07_replacement_demand_aging_age_378d_base_v035_signal,
    f07rda_f07_replacement_demand_aging_rep_5d_base_v036_signal,
    f07rda_f07_replacement_demand_aging_rep_10d_base_v037_signal,
    f07rda_f07_replacement_demand_aging_rep_42d_base_v038_signal,
    f07rda_f07_replacement_demand_aging_rep_189d_base_v039_signal,
    f07rda_f07_replacement_demand_aging_rep_378d_base_v040_signal,
    f07rda_f07_replacement_demand_aging_ageema_21d_base_v041_signal,
    f07rda_f07_replacement_demand_aging_ageema_63d_base_v042_signal,
    f07rda_f07_replacement_demand_aging_ageema_252d_base_v043_signal,
    f07rda_f07_replacement_demand_aging_repema_21d_base_v044_signal,
    f07rda_f07_replacement_demand_aging_repema_63d_base_v045_signal,
    f07rda_f07_replacement_demand_aging_repema_252d_base_v046_signal,
    f07rda_f07_replacement_demand_aging_agegap_21v252_base_v047_signal,
    f07rda_f07_replacement_demand_aging_agegap_63v252_base_v048_signal,
    f07rda_f07_replacement_demand_aging_agegap_63v504_base_v049_signal,
    f07rda_f07_replacement_demand_aging_agegap_126v504_base_v050_signal,
    f07rda_f07_replacement_demand_aging_repgap_21v252_base_v051_signal,
    f07rda_f07_replacement_demand_aging_repgap_63v252_base_v052_signal,
    f07rda_f07_replacement_demand_aging_repgap_63v504_base_v053_signal,
    f07rda_f07_replacement_demand_aging_repgap_126v504_base_v054_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_21d_base_v055_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_63d_base_v056_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_252d_base_v057_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_504d_base_v058_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_21v252_base_v059_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_63v252_base_v060_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_252v252_base_v061_signal,
    f07rda_f07_replacement_demand_aging_comp_21d_base_v062_signal,
    f07rda_f07_replacement_demand_aging_comp_63d_base_v063_signal,
    f07rda_f07_replacement_demand_aging_comp_252d_base_v064_signal,
    f07rda_f07_replacement_demand_aging_comp_504d_base_v065_signal,
    f07rda_f07_replacement_demand_aging_diff_21d_base_v066_signal,
    f07rda_f07_replacement_demand_aging_diff_63d_base_v067_signal,
    f07rda_f07_replacement_demand_aging_diff_252d_base_v068_signal,
    f07rda_f07_replacement_demand_aging_diff_504d_base_v069_signal,
    f07rda_f07_replacement_demand_aging_agexrep_21d_base_v070_signal,
    f07rda_f07_replacement_demand_aging_agexrep_63d_base_v071_signal,
    f07rda_f07_replacement_demand_aging_agexrep_252d_base_v072_signal,
    f07rda_f07_replacement_demand_aging_agelog_63d_base_v073_signal,
    f07rda_f07_replacement_demand_aging_replog_252d_base_v074_signal,
    f07rda_f07_replacement_demand_aging_presssq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_REPLACEMENT_DEMAND_AGING_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f07_replacement_demand_aging_base_001_075_claude: {n_features} features pass")
