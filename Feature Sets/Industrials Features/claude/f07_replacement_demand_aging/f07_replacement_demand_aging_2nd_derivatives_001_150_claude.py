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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# slope of 21d age * close, 5d
def f07rda_f07_replacement_demand_aging_age_21d_slope_v001_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d age * close, 21d
def f07rda_f07_replacement_demand_aging_age_21d_slope_v002_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d age * close, 21d
def f07rda_f07_replacement_demand_aging_age_63d_slope_v003_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d age, 63d
def f07rda_f07_replacement_demand_aging_age_63d_slope_v004_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d age, 21d
def f07rda_f07_replacement_demand_aging_age_126d_slope_v005_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d age, 63d
def f07rda_f07_replacement_demand_aging_age_126d_slope_v006_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d age, 21d
def f07rda_f07_replacement_demand_aging_age_252d_slope_v007_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d age, 63d
def f07rda_f07_replacement_demand_aging_age_252d_slope_v008_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d age, 63d
def f07rda_f07_replacement_demand_aging_age_504d_slope_v009_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d age, 126d
def f07rda_f07_replacement_demand_aging_age_504d_slope_v010_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d rep, 5d
def f07rda_f07_replacement_demand_aging_rep_21d_slope_v011_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d rep, 21d
def f07rda_f07_replacement_demand_aging_rep_21d_slope_v012_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d rep, 21d
def f07rda_f07_replacement_demand_aging_rep_63d_slope_v013_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d rep, 63d
def f07rda_f07_replacement_demand_aging_rep_63d_slope_v014_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d rep, 21d
def f07rda_f07_replacement_demand_aging_rep_126d_slope_v015_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d rep, 63d
def f07rda_f07_replacement_demand_aging_rep_126d_slope_v016_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d rep, 21d
def f07rda_f07_replacement_demand_aging_rep_252d_slope_v017_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d rep, 63d
def f07rda_f07_replacement_demand_aging_rep_252d_slope_v018_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d rep, 63d
def f07rda_f07_replacement_demand_aging_rep_504d_slope_v019_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d rep, 126d
def f07rda_f07_replacement_demand_aging_rep_504d_slope_v020_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d press, 5d
def f07rda_f07_replacement_demand_aging_press_63d_slope_v021_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d press, 21d
def f07rda_f07_replacement_demand_aging_press_63d_slope_v022_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d press, 21d
def f07rda_f07_replacement_demand_aging_press_126d_slope_v023_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d press, 21d
def f07rda_f07_replacement_demand_aging_press_252d_slope_v024_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d press, 63d
def f07rda_f07_replacement_demand_aging_press_252d_slope_v025_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d press, 63d
def f07rda_f07_replacement_demand_aging_press_504d_slope_v026_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d press, 126d
def f07rda_f07_replacement_demand_aging_press_504d_slope_v027_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std age 21d, 21d
def f07rda_f07_replacement_demand_aging_agestd_21d_slope_v028_signal(depamor, ppnenet, closeadj):
    base = _std(_f07_ppe_age_proxy(depamor, ppnenet), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std age 63d, 21d
def f07rda_f07_replacement_demand_aging_agestd_63d_slope_v029_signal(depamor, ppnenet, closeadj):
    base = _std(_f07_ppe_age_proxy(depamor, ppnenet), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std age 252d, 63d
def f07rda_f07_replacement_demand_aging_agestd_252d_slope_v030_signal(depamor, ppnenet, closeadj):
    base = _std(_f07_ppe_age_proxy(depamor, ppnenet), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std age 504d, 126d
def f07rda_f07_replacement_demand_aging_agestd_504d_slope_v031_signal(depamor, ppnenet, closeadj):
    base = _std(_f07_ppe_age_proxy(depamor, ppnenet), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std rep 21d, 21d
def f07rda_f07_replacement_demand_aging_repstd_21d_slope_v032_signal(capex, depamor, closeadj):
    base = _std(_f07_replacement_ratio(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std rep 63d, 21d
def f07rda_f07_replacement_demand_aging_repstd_63d_slope_v033_signal(capex, depamor, closeadj):
    base = _std(_f07_replacement_ratio(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std rep 252d, 63d
def f07rda_f07_replacement_demand_aging_repstd_252d_slope_v034_signal(capex, depamor, closeadj):
    base = _std(_f07_replacement_ratio(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of std rep 504d, 126d
def f07rda_f07_replacement_demand_aging_repstd_504d_slope_v035_signal(capex, depamor, closeadj):
    base = _std(_f07_replacement_ratio(capex, depamor), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z age 21d, 21d
def f07rda_f07_replacement_demand_aging_agez_21d_slope_v036_signal(depamor, ppnenet, closeadj):
    base = _z(_f07_ppe_age_proxy(depamor, ppnenet), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z age 63d, 21d
def f07rda_f07_replacement_demand_aging_agez_63d_slope_v037_signal(depamor, ppnenet, closeadj):
    base = _z(_f07_ppe_age_proxy(depamor, ppnenet), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z age 252d, 63d
def f07rda_f07_replacement_demand_aging_agez_252d_slope_v038_signal(depamor, ppnenet, closeadj):
    base = _z(_f07_ppe_age_proxy(depamor, ppnenet), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z age 504d, 126d
def f07rda_f07_replacement_demand_aging_agez_504d_slope_v039_signal(depamor, ppnenet, closeadj):
    base = _z(_f07_ppe_age_proxy(depamor, ppnenet), 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z rep 21d, 21d
def f07rda_f07_replacement_demand_aging_repz_21d_slope_v040_signal(capex, depamor, closeadj):
    base = _z(_f07_replacement_ratio(capex, depamor), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z rep 63d, 21d
def f07rda_f07_replacement_demand_aging_repz_63d_slope_v041_signal(capex, depamor, closeadj):
    base = _z(_f07_replacement_ratio(capex, depamor), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z rep 252d, 63d
def f07rda_f07_replacement_demand_aging_repz_252d_slope_v042_signal(capex, depamor, closeadj):
    base = _z(_f07_replacement_ratio(capex, depamor), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of z rep 504d, 126d
def f07rda_f07_replacement_demand_aging_repz_504d_slope_v043_signal(capex, depamor, closeadj):
    base = _z(_f07_replacement_ratio(capex, depamor), 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d age, 5d
def f07rda_f07_replacement_demand_aging_age_5d_slope_v044_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 10d age, 10d
def f07rda_f07_replacement_demand_aging_age_10d_slope_v045_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 42d age, 21d
def f07rda_f07_replacement_demand_aging_age_42d_slope_v046_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 189d age, 63d
def f07rda_f07_replacement_demand_aging_age_189d_slope_v047_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 378d age, 126d
def f07rda_f07_replacement_demand_aging_age_378d_slope_v048_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 378) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d rep, 5d
def f07rda_f07_replacement_demand_aging_rep_5d_slope_v049_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 10d rep, 10d
def f07rda_f07_replacement_demand_aging_rep_10d_slope_v050_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 42d rep, 21d
def f07rda_f07_replacement_demand_aging_rep_42d_slope_v051_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 189d rep, 63d
def f07rda_f07_replacement_demand_aging_rep_189d_slope_v052_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 378d rep, 126d
def f07rda_f07_replacement_demand_aging_rep_378d_slope_v053_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 378) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d EMA age, 21d
def f07rda_f07_replacement_demand_aging_ageema_21d_slope_v054_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d EMA age, 21d
def f07rda_f07_replacement_demand_aging_ageema_63d_slope_v055_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d EMA age, 63d
def f07rda_f07_replacement_demand_aging_ageema_252d_slope_v056_signal(depamor, ppnenet, closeadj):
    base = _f07_ppe_age_proxy(depamor, ppnenet).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d EMA rep, 21d
def f07rda_f07_replacement_demand_aging_repema_21d_slope_v057_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d EMA rep, 21d
def f07rda_f07_replacement_demand_aging_repema_63d_slope_v058_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d EMA rep, 63d
def f07rda_f07_replacement_demand_aging_repema_252d_slope_v059_signal(capex, depamor, closeadj):
    base = _f07_replacement_ratio(capex, depamor).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age gap 21v252, 21d
def f07rda_f07_replacement_demand_aging_agegap_21v252_slope_v060_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age gap 63v252, 21d
def f07rda_f07_replacement_demand_aging_agegap_63v252_slope_v061_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age gap 63v504, 63d
def f07rda_f07_replacement_demand_aging_agegap_63v504_slope_v062_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age gap 126v504, 63d
def f07rda_f07_replacement_demand_aging_agegap_126v504_slope_v063_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep gap 21v252, 21d
def f07rda_f07_replacement_demand_aging_repgap_21v252_slope_v064_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep gap 63v252, 21d
def f07rda_f07_replacement_demand_aging_repgap_63v252_slope_v065_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep gap 63v504, 63d
def f07rda_f07_replacement_demand_aging_repgap_63v504_slope_v066_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep gap 126v504, 63d
def f07rda_f07_replacement_demand_aging_repgap_126v504_slope_v067_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x rep 21d, 21d
def f07rda_f07_replacement_demand_aging_pressxrep_21d_slope_v068_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 21)
    r = _f07_replacement_ratio(capex, depamor)
    base = p * r * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x rep 63d, 21d
def f07rda_f07_replacement_demand_aging_pressxrep_63d_slope_v069_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    r = _f07_replacement_ratio(capex, depamor)
    base = p * r * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x rep 252d, 63d
def f07rda_f07_replacement_demand_aging_pressxrep_252d_slope_v070_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    r = _f07_replacement_ratio(capex, depamor)
    base = p * r * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age/rep 21v252, 21d
def f07rda_f07_replacement_demand_aging_ageovrep_21v252_slope_v071_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 21) / _mean(r, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age/rep 63v252, 21d
def f07rda_f07_replacement_demand_aging_ageovrep_63v252_slope_v072_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 63) / _mean(r, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age/rep 252v252, 63d
def f07rda_f07_replacement_demand_aging_ageovrep_252_slope_v073_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 252) / _mean(r, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age+rep comp 21d, 21d
def f07rda_f07_replacement_demand_aging_comp_21d_slope_v074_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 21) + _mean(r, 21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp 63d, 21d
def f07rda_f07_replacement_demand_aging_comp_63d_slope_v075_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 63) + _mean(r, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp 252d, 63d
def f07rda_f07_replacement_demand_aging_comp_252d_slope_v076_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 252) + _mean(r, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp 504d, 126d
def f07rda_f07_replacement_demand_aging_comp_504d_slope_v077_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 504) + _mean(r, 504)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age-rep diff 21d, 21d
def f07rda_f07_replacement_demand_aging_diff_21d_slope_v078_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 21) - _mean(r, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age-rep diff 63d, 21d
def f07rda_f07_replacement_demand_aging_diff_63d_slope_v079_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 63) - _mean(r, 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age-rep diff 252d, 63d
def f07rda_f07_replacement_demand_aging_diff_252d_slope_v080_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 252) - _mean(r, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age*rep mult 21d, 21d
def f07rda_f07_replacement_demand_aging_agexrep_21d_slope_v081_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = _mean(a * r, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age*rep mult 63d, 21d
def f07rda_f07_replacement_demand_aging_agexrep_63d_slope_v082_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = _mean(a * r, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age*rep mult 252d, 63d
def f07rda_f07_replacement_demand_aging_agexrep_252d_slope_v083_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = _mean(a * r, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age x capex 63d, 21d
def f07rda_f07_replacement_demand_aging_agexcap_63d_slope_v084_signal(depamor, ppnenet, capex, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet) * capex, 63) * closeadj / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age x capex 252d, 63d
def f07rda_f07_replacement_demand_aging_agexcap_252d_slope_v085_signal(depamor, ppnenet, capex, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet) * capex, 252) * closeadj / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep x dep 63d, 21d
def f07rda_f07_replacement_demand_aging_repxdep_63d_slope_v086_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor) * depamor, 63) * closeadj / 1e9
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep x dep 252d, 63d
def f07rda_f07_replacement_demand_aging_repxdep_252d_slope_v087_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor) * depamor, 252) * closeadj / 1e9
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x cap 63d, 21d
def f07rda_f07_replacement_demand_aging_pressxcap_63d_slope_v088_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    base = p * capex * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x cap 252d, 63d
def f07rda_f07_replacement_demand_aging_pressxcap_252d_slope_v089_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    base = p * capex * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x dep 63d, 21d
def f07rda_f07_replacement_demand_aging_pressxdep_63d_slope_v090_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    base = p * depamor * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x dep 252d, 63d
def f07rda_f07_replacement_demand_aging_pressxdep_252d_slope_v091_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    base = p * depamor * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 5d, 5d
def f07rda_f07_replacement_demand_aging_press_5d_slope_v092_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 10d, 10d
def f07rda_f07_replacement_demand_aging_press_10d_slope_v093_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 10) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 21d, 21d
def f07rda_f07_replacement_demand_aging_press_21d_slope_v094_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 42d, 21d
def f07rda_f07_replacement_demand_aging_press_42d_slope_v095_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 189d, 63d
def f07rda_f07_replacement_demand_aging_press_189d_slope_v096_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press 378d, 126d
def f07rda_f07_replacement_demand_aging_press_378d_slope_v097_signal(depamor, ppnenet, closeadj):
    base = _f07_aging_pressure(depamor, ppnenet, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age max 21d, 21d
def f07rda_f07_replacement_demand_aging_agemax_21d_slope_v098_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = b.rolling(21, min_periods=5).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age max 63d, 21d
def f07rda_f07_replacement_demand_aging_agemax_63d_slope_v099_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = b.rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age max 252d, 63d
def f07rda_f07_replacement_demand_aging_agemax_252d_slope_v100_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = b.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age max 504d, 126d
def f07rda_f07_replacement_demand_aging_agemax_504d_slope_v101_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = b.rolling(504, min_periods=126).max() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age min 252d, 63d
def f07rda_f07_replacement_demand_aging_agemin_252d_slope_v102_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = b.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age range 252d, 63d
def f07rda_f07_replacement_demand_aging_agerng_252d_slope_v103_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep range 252d, 63d
def f07rda_f07_replacement_demand_aging_reprng_252d_slope_v104_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep max 252d, 63d
def f07rda_f07_replacement_demand_aging_repmax_252d_slope_v105_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = b.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep min 252d, 63d
def f07rda_f07_replacement_demand_aging_repmin_252d_slope_v106_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = b.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age pct 252d, 63d
def f07rda_f07_replacement_demand_aging_agepct_252d_slope_v107_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age pct 504d, 126d
def f07rda_f07_replacement_demand_aging_agepct_504d_slope_v108_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep pct 252d, 63d
def f07rda_f07_replacement_demand_aging_reppct_252d_slope_v109_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep pct 504d, 126d
def f07rda_f07_replacement_demand_aging_reppct_504d_slope_v110_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt age 63d, 21d
def f07rda_f07_replacement_demand_aging_agesqrt_63d_slope_v111_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet).abs()
    base = np.sqrt(_mean(b, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt age 252d, 63d
def f07rda_f07_replacement_demand_aging_agesqrt_252d_slope_v112_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt rep 63d, 21d
def f07rda_f07_replacement_demand_aging_repsqrt_63d_slope_v113_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor).abs()
    base = np.sqrt(_mean(b, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sqrt rep 252d, 63d
def f07rda_f07_replacement_demand_aging_repsqrt_252d_slope_v114_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age CV 21d, 21d
def f07rda_f07_replacement_demand_aging_agecv_21d_slope_v115_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 21) / _mean(b, 21).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age CV 63d, 21d
def f07rda_f07_replacement_demand_aging_agecv_63d_slope_v116_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age CV 252d, 63d
def f07rda_f07_replacement_demand_aging_agecv_252d_slope_v117_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep CV 63d, 21d
def f07rda_f07_replacement_demand_aging_repcv_63d_slope_v118_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep CV 252d, 63d
def f07rda_f07_replacement_demand_aging_repcv_252d_slope_v119_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp z 63d, 21d
def f07rda_f07_replacement_demand_aging_compz_63d_slope_v120_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    r = _f07_replacement_ratio(capex, depamor)
    base = (p + _z(r, 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp z 252d, 63d
def f07rda_f07_replacement_demand_aging_compz_252d_slope_v121_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    r = _f07_replacement_ratio(capex, depamor)
    base = (p + _z(r, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp z 504d, 126d
def f07rda_f07_replacement_demand_aging_compz_504d_slope_v122_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    r = _f07_replacement_ratio(capex, depamor)
    base = (p + _z(r, 504)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age ratio 21v252, 21d
def f07rda_f07_replacement_demand_aging_ageratio_21v252_slope_v123_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age ratio 63v252, 21d
def f07rda_f07_replacement_demand_aging_ageratio_63v252_slope_v124_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age ratio 63v504, 63d
def f07rda_f07_replacement_demand_aging_ageratio_63v504_slope_v125_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep ratio 21v252, 21d
def f07rda_f07_replacement_demand_aging_repratio_21v252_slope_v126_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep ratio 63v252, 21d
def f07rda_f07_replacement_demand_aging_repratio_63v252_slope_v127_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep ratio 63v504, 63d
def f07rda_f07_replacement_demand_aging_repratio_63v504_slope_v128_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x cret 21d, 21d
def f07rda_f07_replacement_demand_aging_pressxcret_21d_slope_v129_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 21)
    cret = closeadj.pct_change(21)
    base = p * cret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x cret 63d, 21d
def f07rda_f07_replacement_demand_aging_pressxcret_63d_slope_v130_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 63)
    cret = closeadj.pct_change(63)
    base = p * cret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x cret 252d, 63d
def f07rda_f07_replacement_demand_aging_pressxcret_252d_slope_v131_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    cret = closeadj.pct_change(252)
    base = p * cret * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of under-invest 252d, 63d
def f07rda_f07_replacement_demand_aging_underinv_252d_slope_v132_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    under = (b < 1.0).astype(float)
    base = (_mean(under, 252) + b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of under-invest 504d, 126d
def f07rda_f07_replacement_demand_aging_underinv_504d_slope_v133_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    under = (b < 1.0).astype(float)
    base = (_mean(under, 504) + b) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of over-invest 252d, 63d
def f07rda_f07_replacement_demand_aging_overinv_252d_slope_v134_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    over = (b > 1.5).astype(float)
    base = (_mean(over, 252) + b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of over-invest 504d, 126d
def f07rda_f07_replacement_demand_aging_overinv_504d_slope_v135_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    over = (b > 1.5).astype(float)
    base = (_mean(over, 504) + b) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press squared 252d, 63d
def f07rda_f07_replacement_demand_aging_presssq_252d_slope_v136_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press squared 504d, 126d
def f07rda_f07_replacement_demand_aging_presssq_504d_slope_v137_signal(depamor, ppnenet, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    base = p * p.abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp ema 63d, 21d
def f07rda_f07_replacement_demand_aging_compema_63d_slope_v138_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (a + r).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp ema 252d, 63d
def f07rda_f07_replacement_demand_aging_compema_252d_slope_v139_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (a + r).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of global aging composite 504d, 126d
def f07rda_f07_replacement_demand_aging_globcomp_504d_slope_v140_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    p = _f07_aging_pressure(depamor, ppnenet, 252)
    base = (_mean(a, 504) + _mean(r, 504) + p) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age log 63d, 21d
def f07rda_f07_replacement_demand_aging_agelog_63d_slope_v141_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    base = np.log(_mean(b, 63).replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep log 252d, 63d
def f07rda_f07_replacement_demand_aging_replog_252d_slope_v142_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    base = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age x cumclose 63d
def f07rda_f07_replacement_demand_aging_agexcumcl_63d_slope_v143_signal(depamor, ppnenet, closeadj):
    b = _f07_ppe_age_proxy(depamor, ppnenet)
    cv = _mean(closeadj, 63) * closeadj
    base = _mean(b, 63) * cv
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep x cumclose 63d
def f07rda_f07_replacement_demand_aging_repxcumcl_63d_slope_v144_signal(capex, depamor, closeadj):
    b = _f07_replacement_ratio(capex, depamor)
    cv = _mean(closeadj, 63) * closeadj
    base = _mean(b, 63) * cv
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age 5d, 21d (alt long)
def f07rda_f07_replacement_demand_aging_age_5d_21slope_v145_signal(depamor, ppnenet, closeadj):
    base = _mean(_f07_ppe_age_proxy(depamor, ppnenet), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rep 5d, 21d
def f07rda_f07_replacement_demand_aging_rep_5d_21slope_v146_signal(capex, depamor, closeadj):
    base = _mean(_f07_replacement_ratio(capex, depamor), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of press x rep 504d, 126d
def f07rda_f07_replacement_demand_aging_pressxrep_504d_slope_v147_signal(depamor, ppnenet, capex, closeadj):
    p = _f07_aging_pressure(depamor, ppnenet, 504)
    r = _f07_replacement_ratio(capex, depamor)
    base = p * r * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of age + 2*rep weighted 252d, 63d
def f07rda_f07_replacement_demand_aging_weight_252d_slope_v148_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 252) + 2 * _mean(r, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 2*age + rep weighted 252d, 63d
def f07rda_f07_replacement_demand_aging_weight2_252d_slope_v149_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (2 * _mean(a, 252) + _mean(r, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of comp 504d, 252d
def f07rda_f07_replacement_demand_aging_comp_504d_252slope_v150_signal(depamor, ppnenet, capex, closeadj):
    a = _f07_ppe_age_proxy(depamor, ppnenet)
    r = _f07_replacement_ratio(capex, depamor)
    base = (_mean(a, 504) + _mean(r, 504)) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07rda_f07_replacement_demand_aging_age_21d_slope_v001_signal,
    f07rda_f07_replacement_demand_aging_age_21d_slope_v002_signal,
    f07rda_f07_replacement_demand_aging_age_63d_slope_v003_signal,
    f07rda_f07_replacement_demand_aging_age_63d_slope_v004_signal,
    f07rda_f07_replacement_demand_aging_age_126d_slope_v005_signal,
    f07rda_f07_replacement_demand_aging_age_126d_slope_v006_signal,
    f07rda_f07_replacement_demand_aging_age_252d_slope_v007_signal,
    f07rda_f07_replacement_demand_aging_age_252d_slope_v008_signal,
    f07rda_f07_replacement_demand_aging_age_504d_slope_v009_signal,
    f07rda_f07_replacement_demand_aging_age_504d_slope_v010_signal,
    f07rda_f07_replacement_demand_aging_rep_21d_slope_v011_signal,
    f07rda_f07_replacement_demand_aging_rep_21d_slope_v012_signal,
    f07rda_f07_replacement_demand_aging_rep_63d_slope_v013_signal,
    f07rda_f07_replacement_demand_aging_rep_63d_slope_v014_signal,
    f07rda_f07_replacement_demand_aging_rep_126d_slope_v015_signal,
    f07rda_f07_replacement_demand_aging_rep_126d_slope_v016_signal,
    f07rda_f07_replacement_demand_aging_rep_252d_slope_v017_signal,
    f07rda_f07_replacement_demand_aging_rep_252d_slope_v018_signal,
    f07rda_f07_replacement_demand_aging_rep_504d_slope_v019_signal,
    f07rda_f07_replacement_demand_aging_rep_504d_slope_v020_signal,
    f07rda_f07_replacement_demand_aging_press_63d_slope_v021_signal,
    f07rda_f07_replacement_demand_aging_press_63d_slope_v022_signal,
    f07rda_f07_replacement_demand_aging_press_126d_slope_v023_signal,
    f07rda_f07_replacement_demand_aging_press_252d_slope_v024_signal,
    f07rda_f07_replacement_demand_aging_press_252d_slope_v025_signal,
    f07rda_f07_replacement_demand_aging_press_504d_slope_v026_signal,
    f07rda_f07_replacement_demand_aging_press_504d_slope_v027_signal,
    f07rda_f07_replacement_demand_aging_agestd_21d_slope_v028_signal,
    f07rda_f07_replacement_demand_aging_agestd_63d_slope_v029_signal,
    f07rda_f07_replacement_demand_aging_agestd_252d_slope_v030_signal,
    f07rda_f07_replacement_demand_aging_agestd_504d_slope_v031_signal,
    f07rda_f07_replacement_demand_aging_repstd_21d_slope_v032_signal,
    f07rda_f07_replacement_demand_aging_repstd_63d_slope_v033_signal,
    f07rda_f07_replacement_demand_aging_repstd_252d_slope_v034_signal,
    f07rda_f07_replacement_demand_aging_repstd_504d_slope_v035_signal,
    f07rda_f07_replacement_demand_aging_agez_21d_slope_v036_signal,
    f07rda_f07_replacement_demand_aging_agez_63d_slope_v037_signal,
    f07rda_f07_replacement_demand_aging_agez_252d_slope_v038_signal,
    f07rda_f07_replacement_demand_aging_agez_504d_slope_v039_signal,
    f07rda_f07_replacement_demand_aging_repz_21d_slope_v040_signal,
    f07rda_f07_replacement_demand_aging_repz_63d_slope_v041_signal,
    f07rda_f07_replacement_demand_aging_repz_252d_slope_v042_signal,
    f07rda_f07_replacement_demand_aging_repz_504d_slope_v043_signal,
    f07rda_f07_replacement_demand_aging_age_5d_slope_v044_signal,
    f07rda_f07_replacement_demand_aging_age_10d_slope_v045_signal,
    f07rda_f07_replacement_demand_aging_age_42d_slope_v046_signal,
    f07rda_f07_replacement_demand_aging_age_189d_slope_v047_signal,
    f07rda_f07_replacement_demand_aging_age_378d_slope_v048_signal,
    f07rda_f07_replacement_demand_aging_rep_5d_slope_v049_signal,
    f07rda_f07_replacement_demand_aging_rep_10d_slope_v050_signal,
    f07rda_f07_replacement_demand_aging_rep_42d_slope_v051_signal,
    f07rda_f07_replacement_demand_aging_rep_189d_slope_v052_signal,
    f07rda_f07_replacement_demand_aging_rep_378d_slope_v053_signal,
    f07rda_f07_replacement_demand_aging_ageema_21d_slope_v054_signal,
    f07rda_f07_replacement_demand_aging_ageema_63d_slope_v055_signal,
    f07rda_f07_replacement_demand_aging_ageema_252d_slope_v056_signal,
    f07rda_f07_replacement_demand_aging_repema_21d_slope_v057_signal,
    f07rda_f07_replacement_demand_aging_repema_63d_slope_v058_signal,
    f07rda_f07_replacement_demand_aging_repema_252d_slope_v059_signal,
    f07rda_f07_replacement_demand_aging_agegap_21v252_slope_v060_signal,
    f07rda_f07_replacement_demand_aging_agegap_63v252_slope_v061_signal,
    f07rda_f07_replacement_demand_aging_agegap_63v504_slope_v062_signal,
    f07rda_f07_replacement_demand_aging_agegap_126v504_slope_v063_signal,
    f07rda_f07_replacement_demand_aging_repgap_21v252_slope_v064_signal,
    f07rda_f07_replacement_demand_aging_repgap_63v252_slope_v065_signal,
    f07rda_f07_replacement_demand_aging_repgap_63v504_slope_v066_signal,
    f07rda_f07_replacement_demand_aging_repgap_126v504_slope_v067_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_21d_slope_v068_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_63d_slope_v069_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_252d_slope_v070_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_21v252_slope_v071_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_63v252_slope_v072_signal,
    f07rda_f07_replacement_demand_aging_ageovrep_252_slope_v073_signal,
    f07rda_f07_replacement_demand_aging_comp_21d_slope_v074_signal,
    f07rda_f07_replacement_demand_aging_comp_63d_slope_v075_signal,
    f07rda_f07_replacement_demand_aging_comp_252d_slope_v076_signal,
    f07rda_f07_replacement_demand_aging_comp_504d_slope_v077_signal,
    f07rda_f07_replacement_demand_aging_diff_21d_slope_v078_signal,
    f07rda_f07_replacement_demand_aging_diff_63d_slope_v079_signal,
    f07rda_f07_replacement_demand_aging_diff_252d_slope_v080_signal,
    f07rda_f07_replacement_demand_aging_agexrep_21d_slope_v081_signal,
    f07rda_f07_replacement_demand_aging_agexrep_63d_slope_v082_signal,
    f07rda_f07_replacement_demand_aging_agexrep_252d_slope_v083_signal,
    f07rda_f07_replacement_demand_aging_agexcap_63d_slope_v084_signal,
    f07rda_f07_replacement_demand_aging_agexcap_252d_slope_v085_signal,
    f07rda_f07_replacement_demand_aging_repxdep_63d_slope_v086_signal,
    f07rda_f07_replacement_demand_aging_repxdep_252d_slope_v087_signal,
    f07rda_f07_replacement_demand_aging_pressxcap_63d_slope_v088_signal,
    f07rda_f07_replacement_demand_aging_pressxcap_252d_slope_v089_signal,
    f07rda_f07_replacement_demand_aging_pressxdep_63d_slope_v090_signal,
    f07rda_f07_replacement_demand_aging_pressxdep_252d_slope_v091_signal,
    f07rda_f07_replacement_demand_aging_press_5d_slope_v092_signal,
    f07rda_f07_replacement_demand_aging_press_10d_slope_v093_signal,
    f07rda_f07_replacement_demand_aging_press_21d_slope_v094_signal,
    f07rda_f07_replacement_demand_aging_press_42d_slope_v095_signal,
    f07rda_f07_replacement_demand_aging_press_189d_slope_v096_signal,
    f07rda_f07_replacement_demand_aging_press_378d_slope_v097_signal,
    f07rda_f07_replacement_demand_aging_agemax_21d_slope_v098_signal,
    f07rda_f07_replacement_demand_aging_agemax_63d_slope_v099_signal,
    f07rda_f07_replacement_demand_aging_agemax_252d_slope_v100_signal,
    f07rda_f07_replacement_demand_aging_agemax_504d_slope_v101_signal,
    f07rda_f07_replacement_demand_aging_agemin_252d_slope_v102_signal,
    f07rda_f07_replacement_demand_aging_agerng_252d_slope_v103_signal,
    f07rda_f07_replacement_demand_aging_reprng_252d_slope_v104_signal,
    f07rda_f07_replacement_demand_aging_repmax_252d_slope_v105_signal,
    f07rda_f07_replacement_demand_aging_repmin_252d_slope_v106_signal,
    f07rda_f07_replacement_demand_aging_agepct_252d_slope_v107_signal,
    f07rda_f07_replacement_demand_aging_agepct_504d_slope_v108_signal,
    f07rda_f07_replacement_demand_aging_reppct_252d_slope_v109_signal,
    f07rda_f07_replacement_demand_aging_reppct_504d_slope_v110_signal,
    f07rda_f07_replacement_demand_aging_agesqrt_63d_slope_v111_signal,
    f07rda_f07_replacement_demand_aging_agesqrt_252d_slope_v112_signal,
    f07rda_f07_replacement_demand_aging_repsqrt_63d_slope_v113_signal,
    f07rda_f07_replacement_demand_aging_repsqrt_252d_slope_v114_signal,
    f07rda_f07_replacement_demand_aging_agecv_21d_slope_v115_signal,
    f07rda_f07_replacement_demand_aging_agecv_63d_slope_v116_signal,
    f07rda_f07_replacement_demand_aging_agecv_252d_slope_v117_signal,
    f07rda_f07_replacement_demand_aging_repcv_63d_slope_v118_signal,
    f07rda_f07_replacement_demand_aging_repcv_252d_slope_v119_signal,
    f07rda_f07_replacement_demand_aging_compz_63d_slope_v120_signal,
    f07rda_f07_replacement_demand_aging_compz_252d_slope_v121_signal,
    f07rda_f07_replacement_demand_aging_compz_504d_slope_v122_signal,
    f07rda_f07_replacement_demand_aging_ageratio_21v252_slope_v123_signal,
    f07rda_f07_replacement_demand_aging_ageratio_63v252_slope_v124_signal,
    f07rda_f07_replacement_demand_aging_ageratio_63v504_slope_v125_signal,
    f07rda_f07_replacement_demand_aging_repratio_21v252_slope_v126_signal,
    f07rda_f07_replacement_demand_aging_repratio_63v252_slope_v127_signal,
    f07rda_f07_replacement_demand_aging_repratio_63v504_slope_v128_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_21d_slope_v129_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_63d_slope_v130_signal,
    f07rda_f07_replacement_demand_aging_pressxcret_252d_slope_v131_signal,
    f07rda_f07_replacement_demand_aging_underinv_252d_slope_v132_signal,
    f07rda_f07_replacement_demand_aging_underinv_504d_slope_v133_signal,
    f07rda_f07_replacement_demand_aging_overinv_252d_slope_v134_signal,
    f07rda_f07_replacement_demand_aging_overinv_504d_slope_v135_signal,
    f07rda_f07_replacement_demand_aging_presssq_252d_slope_v136_signal,
    f07rda_f07_replacement_demand_aging_presssq_504d_slope_v137_signal,
    f07rda_f07_replacement_demand_aging_compema_63d_slope_v138_signal,
    f07rda_f07_replacement_demand_aging_compema_252d_slope_v139_signal,
    f07rda_f07_replacement_demand_aging_globcomp_504d_slope_v140_signal,
    f07rda_f07_replacement_demand_aging_agelog_63d_slope_v141_signal,
    f07rda_f07_replacement_demand_aging_replog_252d_slope_v142_signal,
    f07rda_f07_replacement_demand_aging_agexcumcl_63d_slope_v143_signal,
    f07rda_f07_replacement_demand_aging_repxcumcl_63d_slope_v144_signal,
    f07rda_f07_replacement_demand_aging_age_5d_21slope_v145_signal,
    f07rda_f07_replacement_demand_aging_rep_5d_21slope_v146_signal,
    f07rda_f07_replacement_demand_aging_pressxrep_504d_slope_v147_signal,
    f07rda_f07_replacement_demand_aging_weight_252d_slope_v148_signal,
    f07rda_f07_replacement_demand_aging_weight2_252d_slope_v149_signal,
    f07rda_f07_replacement_demand_aging_comp_504d_252slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_REPLACEMENT_DEMAND_AGING_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_replacement_demand_aging_2nd_derivatives_001_150_claude: {n_features} features pass")
