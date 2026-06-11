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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f04_inventory_days(inventory, cor):
    return 365.0 * inventory / cor.replace(0, np.nan).abs()


def _f04_inventory_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan).abs()


def _f04_inventory_growth_gap(inventory, revenue, w):
    inv_g = inventory.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return inv_g - rev_g

def f04ids_f04_inventory_destock_signature_idy_5d_jerk_v001_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 5) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_10d_jerk_v002_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 10) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_21d_jerk_v003_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 21) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_42d_jerk_v004_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 42) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_63d_jerk_v005_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 63) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_126d_jerk_v006_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 126) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_189d_jerk_v007_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 189) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idy_252d_jerk_v008_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _mean(base, 252) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_5d_jerk_v009_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 5) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_10d_jerk_v010_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 10) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_21d_jerk_v011_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 21) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_42d_jerk_v012_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 42) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_63d_jerk_v013_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 63) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_126d_jerk_v014_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 126) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_189d_jerk_v015_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 189) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itr_252d_jerk_v016_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(base, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_5d_jerk_v017_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 5)
    _b = base * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_10d_jerk_v018_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 10)
    _b = base * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_21d_jerk_v019_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = base * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_42d_jerk_v020_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 42)
    _b = base * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_63d_jerk_v021_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = base * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_126d_jerk_v022_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = base * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_189d_jerk_v023_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 189)
    _b = base * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_igg_252d_jerk_v024_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = base * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_5d_jerk_v025_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 5) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_10d_jerk_v026_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 10) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_21d_jerk_v027_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 21) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_42d_jerk_v028_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 42) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_63d_jerk_v029_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 63) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_126d_jerk_v030_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 126) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_189d_jerk_v031_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 189) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idystd_252d_jerk_v032_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _std(base, 252) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_5d_jerk_v033_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 5) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_10d_jerk_v034_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 10) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_21d_jerk_v035_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 21) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_42d_jerk_v036_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 42) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_63d_jerk_v037_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 63) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_126d_jerk_v038_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 126) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_189d_jerk_v039_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 189) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrstd_252d_jerk_v040_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _std(base, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_5d_jerk_v041_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 5)
    _b = _std(base, 5) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_10d_jerk_v042_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 10)
    _b = _std(base, 10) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_21d_jerk_v043_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = _std(base, 21) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_42d_jerk_v044_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 42)
    _b = _std(base, 42) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_63d_jerk_v045_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = _std(base, 63) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_126d_jerk_v046_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = _std(base, 126) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_189d_jerk_v047_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 189)
    _b = _std(base, 189) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggstd_252d_jerk_v048_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = _std(base, 252) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyz_21d_jerk_v049_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _z(base, 42) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyz_63d_jerk_v050_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _z(base, 126) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyz_126d_jerk_v051_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _z(base, 252) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyz_252d_jerk_v052_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = _z(base, 504) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrz_21d_jerk_v053_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _z(base, 42) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrz_63d_jerk_v054_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _z(base, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrz_126d_jerk_v055_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _z(base, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrz_252d_jerk_v056_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = _z(base, 504) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggz_21d_jerk_v057_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = _z(base, 42) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggz_63d_jerk_v058_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = _z(base, 126) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggz_126d_jerk_v059_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = _z(base, 252) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggz_252d_jerk_v060_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = _z(base, 504) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turns_21d_jerk_v061_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _mean(turns_v, 21) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turns_63d_jerk_v062_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _mean(turns_v, 63) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turns_126d_jerk_v063_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _mean(turns_v, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turns_252d_jerk_v064_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _mean(turns_v, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsz_21d_jerk_v065_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _z(turns_v, 42) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsz_63d_jerk_v066_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _z(turns_v, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsz_126d_jerk_v067_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _z(turns_v, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsz_252d_jerk_v068_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _z(turns_v, 504) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsstd_21d_jerk_v069_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _std(turns_v, 21) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsstd_63d_jerk_v070_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _std(turns_v, 63) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsstd_126d_jerk_v071_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _std(turns_v, 126) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_turnsstd_252d_jerk_v072_signal(inventory, cor, closeadj):
    days = _f04_inventory_days(inventory, cor)
    turns_v = 365.0 / days.replace(0, np.nan).abs()
    _b = _std(turns_v, 252) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxitr_21d_jerk_v073_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 21) * _mean(b, 21) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxitr_63d_jerk_v074_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 63) * _mean(b, 63) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxitr_126d_jerk_v075_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 126) * _mean(b, 126) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxitr_252d_jerk_v076_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 252) * _mean(b, 252) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxigg_21d_jerk_v077_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = _mean(a, 21) * b * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxigg_63d_jerk_v078_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = _mean(a, 63) * b * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxigg_126d_jerk_v079_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = _mean(a, 126) * b * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxigg_252d_jerk_v080_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    b = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = _mean(a, 252) * b * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxigg_21d_jerk_v081_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    b = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = _mean(a, 21) * b * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxigg_63d_jerk_v082_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    b = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = _mean(a, 63) * b * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxigg_126d_jerk_v083_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    b = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = _mean(a, 126) * b * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxigg_252d_jerk_v084_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    b = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = _mean(a, 252) * b * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_trio_21d_jerk_v085_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor) / 365.0
    b = _f04_inventory_to_revenue(inventory, revenue)
    c = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = (a + b + c) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_trio_63d_jerk_v086_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor) / 365.0
    b = _f04_inventory_to_revenue(inventory, revenue)
    c = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = (a + b + c) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_trio_126d_jerk_v087_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor) / 365.0
    b = _f04_inventory_to_revenue(inventory, revenue)
    c = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = (a + b + c) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_trio_252d_jerk_v088_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor) / 365.0
    b = _f04_inventory_to_revenue(inventory, revenue)
    c = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = (a + b + c) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxret_21d_jerk_v089_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    ret = closeadj.pct_change(21)
    _b = a * ret * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxret_63d_jerk_v090_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    ret = closeadj.pct_change(63)
    _b = a * ret * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxret_126d_jerk_v091_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    ret = closeadj.pct_change(126)
    _b = a * ret * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxret_21d_jerk_v092_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 21)
    ret = closeadj.pct_change(21)
    _b = a * ret * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxret_63d_jerk_v093_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 63)
    ret = closeadj.pct_change(63)
    _b = a * ret * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxret_126d_jerk_v094_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 126)
    ret = closeadj.pct_change(126)
    _b = a * ret * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxvol_21d_jerk_v095_signal(inventory, cor, closeadj, volume):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 21) * _mean(closeadj * volume, 21) / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxvol_63d_jerk_v096_signal(inventory, cor, closeadj, volume):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 63) * _mean(closeadj * volume, 63) / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxvol_126d_jerk_v097_signal(inventory, cor, closeadj, volume):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 126) * _mean(closeadj * volume, 126) / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxvol_21d_jerk_v098_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 21) * _mean(closeadj * volume, 21)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxvol_63d_jerk_v099_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 63) * _mean(closeadj * volume, 63)
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxvol_126d_jerk_v100_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 126) * _mean(closeadj * volume, 126)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxvol_21d_jerk_v101_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = a * _mean(closeadj * volume, 21)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxvol_63d_jerk_v102_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = a * _mean(closeadj * volume, 63)
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxvol_126d_jerk_v103_signal(inventory, revenue, closeadj, volume):
    a = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = a * _mean(closeadj * volume, 126)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_destockscore_21d_jerk_v104_signal(inventory, revenue, cor, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 21)
    b = _f04_inventory_days(inventory, cor)
    _b = a * _z(b, 42) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_destockscore_63d_jerk_v105_signal(inventory, revenue, cor, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 63)
    b = _f04_inventory_days(inventory, cor)
    _b = a * _z(b, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_destockscore_126d_jerk_v106_signal(inventory, revenue, cor, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 126)
    b = _f04_inventory_days(inventory, cor)
    _b = a * _z(b, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_destockscore_252d_jerk_v107_signal(inventory, revenue, cor, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 252)
    b = _f04_inventory_days(inventory, cor)
    _b = a * _z(b, 504) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyema_21d_jerk_v108_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyema_63d_jerk_v109_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyema_126d_jerk_v110_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrema_21d_jerk_v111_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrema_63d_jerk_v112_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrema_126d_jerk_v113_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggema_21d_jerk_v114_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggema_63d_jerk_v115_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggema_126d_jerk_v116_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrassets_21d_jerk_v117_signal(inventory, assets, closeadj):
    a = _f04_inventory_to_revenue(inventory, assets)
    _b = _mean(a, 21) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrassets_63d_jerk_v118_signal(inventory, assets, closeadj):
    a = _f04_inventory_to_revenue(inventory, assets)
    _b = _mean(a, 63) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrassets_126d_jerk_v119_signal(inventory, assets, closeadj):
    a = _f04_inventory_to_revenue(inventory, assets)
    _b = _mean(a, 126) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrassets_252d_jerk_v120_signal(inventory, assets, closeadj):
    a = _f04_inventory_to_revenue(inventory, assets)
    _b = _mean(a, 252) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcor_21d_jerk_v121_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _mean(a, 21) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcor_63d_jerk_v122_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _mean(a, 63) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcor_126d_jerk_v123_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _mean(a, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcor_252d_jerk_v124_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _mean(a, 252) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idylog_21d_jerk_v125_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = np.log(_mean(base, 21).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idylog_63d_jerk_v126_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = np.log(_mean(base, 63).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idylog_126d_jerk_v127_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = np.log(_mean(base, 126).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idylog_252d_jerk_v128_signal(inventory, cor, closeadj):
    base = _f04_inventory_days(inventory, cor)
    _b = np.log(_mean(base, 252).replace(0, np.nan).abs() + 1.0) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrlog_21d_jerk_v129_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = np.log(_mean(base, 21).replace(0, np.nan).abs() + 0.001) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrlog_63d_jerk_v130_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = np.log(_mean(base, 63).replace(0, np.nan).abs() + 0.001) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrlog_126d_jerk_v131_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = np.log(_mean(base, 126).replace(0, np.nan).abs() + 0.001) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrlog_252d_jerk_v132_signal(inventory, revenue, closeadj):
    base = _f04_inventory_to_revenue(inventory, revenue)
    _b = np.log(_mean(base, 252).replace(0, np.nan).abs() + 0.001) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggsign_21d_jerk_v133_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = base.abs() * np.sign(base) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggsign_63d_jerk_v134_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = base.abs() * np.sign(base) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggsign_126d_jerk_v135_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = base.abs() * np.sign(base) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggsign_252d_jerk_v136_signal(inventory, revenue, closeadj):
    base = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = base.abs() * np.sign(base) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxrev_21d_jerk_v137_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 21) * (revenue / 1e9) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxrev_63d_jerk_v138_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 63) * (revenue / 1e9) * closeadj / 365.0
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxrev_126d_jerk_v139_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 126) * (revenue / 1e9) * closeadj / 365.0
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_idyxrev_252d_jerk_v140_signal(inventory, cor, revenue, closeadj):
    a = _f04_inventory_days(inventory, cor)
    _b = _mean(a, 252) * (revenue / 1e9) * closeadj / 365.0
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxrev_21d_jerk_v141_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 21) * (revenue / 1e9) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxrev_63d_jerk_v142_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 63) * (revenue / 1e9) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxrev_126d_jerk_v143_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 126) * (revenue / 1e9) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrxrev_252d_jerk_v144_signal(inventory, revenue, closeadj):
    a = _f04_inventory_to_revenue(inventory, revenue)
    _b = _mean(a, 252) * (revenue / 1e9) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxrev_21d_jerk_v145_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 21)
    _b = a * (revenue / 1e9) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxrev_63d_jerk_v146_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 63)
    _b = a * (revenue / 1e9) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxrev_126d_jerk_v147_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 126)
    _b = a * (revenue / 1e9) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_iggxrev_252d_jerk_v148_signal(inventory, revenue, closeadj):
    a = _f04_inventory_growth_gap(inventory, revenue, 252)
    _b = a * (revenue / 1e9) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcorz_21d_jerk_v149_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _z(a, 42) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04ids_f04_inventory_destock_signature_itrcorz_63d_jerk_v150_signal(inventory, cor, closeadj):
    a = _f04_inventory_to_revenue(inventory, cor)
    _b = _z(a, 126) * closeadj
    result = _jerk(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04ids_f04_inventory_destock_signature_idy_5d_jerk_v001_signal,
    f04ids_f04_inventory_destock_signature_idy_10d_jerk_v002_signal,
    f04ids_f04_inventory_destock_signature_idy_21d_jerk_v003_signal,
    f04ids_f04_inventory_destock_signature_idy_42d_jerk_v004_signal,
    f04ids_f04_inventory_destock_signature_idy_63d_jerk_v005_signal,
    f04ids_f04_inventory_destock_signature_idy_126d_jerk_v006_signal,
    f04ids_f04_inventory_destock_signature_idy_189d_jerk_v007_signal,
    f04ids_f04_inventory_destock_signature_idy_252d_jerk_v008_signal,
    f04ids_f04_inventory_destock_signature_itr_5d_jerk_v009_signal,
    f04ids_f04_inventory_destock_signature_itr_10d_jerk_v010_signal,
    f04ids_f04_inventory_destock_signature_itr_21d_jerk_v011_signal,
    f04ids_f04_inventory_destock_signature_itr_42d_jerk_v012_signal,
    f04ids_f04_inventory_destock_signature_itr_63d_jerk_v013_signal,
    f04ids_f04_inventory_destock_signature_itr_126d_jerk_v014_signal,
    f04ids_f04_inventory_destock_signature_itr_189d_jerk_v015_signal,
    f04ids_f04_inventory_destock_signature_itr_252d_jerk_v016_signal,
    f04ids_f04_inventory_destock_signature_igg_5d_jerk_v017_signal,
    f04ids_f04_inventory_destock_signature_igg_10d_jerk_v018_signal,
    f04ids_f04_inventory_destock_signature_igg_21d_jerk_v019_signal,
    f04ids_f04_inventory_destock_signature_igg_42d_jerk_v020_signal,
    f04ids_f04_inventory_destock_signature_igg_63d_jerk_v021_signal,
    f04ids_f04_inventory_destock_signature_igg_126d_jerk_v022_signal,
    f04ids_f04_inventory_destock_signature_igg_189d_jerk_v023_signal,
    f04ids_f04_inventory_destock_signature_igg_252d_jerk_v024_signal,
    f04ids_f04_inventory_destock_signature_idystd_5d_jerk_v025_signal,
    f04ids_f04_inventory_destock_signature_idystd_10d_jerk_v026_signal,
    f04ids_f04_inventory_destock_signature_idystd_21d_jerk_v027_signal,
    f04ids_f04_inventory_destock_signature_idystd_42d_jerk_v028_signal,
    f04ids_f04_inventory_destock_signature_idystd_63d_jerk_v029_signal,
    f04ids_f04_inventory_destock_signature_idystd_126d_jerk_v030_signal,
    f04ids_f04_inventory_destock_signature_idystd_189d_jerk_v031_signal,
    f04ids_f04_inventory_destock_signature_idystd_252d_jerk_v032_signal,
    f04ids_f04_inventory_destock_signature_itrstd_5d_jerk_v033_signal,
    f04ids_f04_inventory_destock_signature_itrstd_10d_jerk_v034_signal,
    f04ids_f04_inventory_destock_signature_itrstd_21d_jerk_v035_signal,
    f04ids_f04_inventory_destock_signature_itrstd_42d_jerk_v036_signal,
    f04ids_f04_inventory_destock_signature_itrstd_63d_jerk_v037_signal,
    f04ids_f04_inventory_destock_signature_itrstd_126d_jerk_v038_signal,
    f04ids_f04_inventory_destock_signature_itrstd_189d_jerk_v039_signal,
    f04ids_f04_inventory_destock_signature_itrstd_252d_jerk_v040_signal,
    f04ids_f04_inventory_destock_signature_iggstd_5d_jerk_v041_signal,
    f04ids_f04_inventory_destock_signature_iggstd_10d_jerk_v042_signal,
    f04ids_f04_inventory_destock_signature_iggstd_21d_jerk_v043_signal,
    f04ids_f04_inventory_destock_signature_iggstd_42d_jerk_v044_signal,
    f04ids_f04_inventory_destock_signature_iggstd_63d_jerk_v045_signal,
    f04ids_f04_inventory_destock_signature_iggstd_126d_jerk_v046_signal,
    f04ids_f04_inventory_destock_signature_iggstd_189d_jerk_v047_signal,
    f04ids_f04_inventory_destock_signature_iggstd_252d_jerk_v048_signal,
    f04ids_f04_inventory_destock_signature_idyz_21d_jerk_v049_signal,
    f04ids_f04_inventory_destock_signature_idyz_63d_jerk_v050_signal,
    f04ids_f04_inventory_destock_signature_idyz_126d_jerk_v051_signal,
    f04ids_f04_inventory_destock_signature_idyz_252d_jerk_v052_signal,
    f04ids_f04_inventory_destock_signature_itrz_21d_jerk_v053_signal,
    f04ids_f04_inventory_destock_signature_itrz_63d_jerk_v054_signal,
    f04ids_f04_inventory_destock_signature_itrz_126d_jerk_v055_signal,
    f04ids_f04_inventory_destock_signature_itrz_252d_jerk_v056_signal,
    f04ids_f04_inventory_destock_signature_iggz_21d_jerk_v057_signal,
    f04ids_f04_inventory_destock_signature_iggz_63d_jerk_v058_signal,
    f04ids_f04_inventory_destock_signature_iggz_126d_jerk_v059_signal,
    f04ids_f04_inventory_destock_signature_iggz_252d_jerk_v060_signal,
    f04ids_f04_inventory_destock_signature_turns_21d_jerk_v061_signal,
    f04ids_f04_inventory_destock_signature_turns_63d_jerk_v062_signal,
    f04ids_f04_inventory_destock_signature_turns_126d_jerk_v063_signal,
    f04ids_f04_inventory_destock_signature_turns_252d_jerk_v064_signal,
    f04ids_f04_inventory_destock_signature_turnsz_21d_jerk_v065_signal,
    f04ids_f04_inventory_destock_signature_turnsz_63d_jerk_v066_signal,
    f04ids_f04_inventory_destock_signature_turnsz_126d_jerk_v067_signal,
    f04ids_f04_inventory_destock_signature_turnsz_252d_jerk_v068_signal,
    f04ids_f04_inventory_destock_signature_turnsstd_21d_jerk_v069_signal,
    f04ids_f04_inventory_destock_signature_turnsstd_63d_jerk_v070_signal,
    f04ids_f04_inventory_destock_signature_turnsstd_126d_jerk_v071_signal,
    f04ids_f04_inventory_destock_signature_turnsstd_252d_jerk_v072_signal,
    f04ids_f04_inventory_destock_signature_idyxitr_21d_jerk_v073_signal,
    f04ids_f04_inventory_destock_signature_idyxitr_63d_jerk_v074_signal,
    f04ids_f04_inventory_destock_signature_idyxitr_126d_jerk_v075_signal,
    f04ids_f04_inventory_destock_signature_idyxitr_252d_jerk_v076_signal,
    f04ids_f04_inventory_destock_signature_idyxigg_21d_jerk_v077_signal,
    f04ids_f04_inventory_destock_signature_idyxigg_63d_jerk_v078_signal,
    f04ids_f04_inventory_destock_signature_idyxigg_126d_jerk_v079_signal,
    f04ids_f04_inventory_destock_signature_idyxigg_252d_jerk_v080_signal,
    f04ids_f04_inventory_destock_signature_itrxigg_21d_jerk_v081_signal,
    f04ids_f04_inventory_destock_signature_itrxigg_63d_jerk_v082_signal,
    f04ids_f04_inventory_destock_signature_itrxigg_126d_jerk_v083_signal,
    f04ids_f04_inventory_destock_signature_itrxigg_252d_jerk_v084_signal,
    f04ids_f04_inventory_destock_signature_trio_21d_jerk_v085_signal,
    f04ids_f04_inventory_destock_signature_trio_63d_jerk_v086_signal,
    f04ids_f04_inventory_destock_signature_trio_126d_jerk_v087_signal,
    f04ids_f04_inventory_destock_signature_trio_252d_jerk_v088_signal,
    f04ids_f04_inventory_destock_signature_itrxret_21d_jerk_v089_signal,
    f04ids_f04_inventory_destock_signature_itrxret_63d_jerk_v090_signal,
    f04ids_f04_inventory_destock_signature_itrxret_126d_jerk_v091_signal,
    f04ids_f04_inventory_destock_signature_iggxret_21d_jerk_v092_signal,
    f04ids_f04_inventory_destock_signature_iggxret_63d_jerk_v093_signal,
    f04ids_f04_inventory_destock_signature_iggxret_126d_jerk_v094_signal,
    f04ids_f04_inventory_destock_signature_idyxvol_21d_jerk_v095_signal,
    f04ids_f04_inventory_destock_signature_idyxvol_63d_jerk_v096_signal,
    f04ids_f04_inventory_destock_signature_idyxvol_126d_jerk_v097_signal,
    f04ids_f04_inventory_destock_signature_itrxvol_21d_jerk_v098_signal,
    f04ids_f04_inventory_destock_signature_itrxvol_63d_jerk_v099_signal,
    f04ids_f04_inventory_destock_signature_itrxvol_126d_jerk_v100_signal,
    f04ids_f04_inventory_destock_signature_iggxvol_21d_jerk_v101_signal,
    f04ids_f04_inventory_destock_signature_iggxvol_63d_jerk_v102_signal,
    f04ids_f04_inventory_destock_signature_iggxvol_126d_jerk_v103_signal,
    f04ids_f04_inventory_destock_signature_destockscore_21d_jerk_v104_signal,
    f04ids_f04_inventory_destock_signature_destockscore_63d_jerk_v105_signal,
    f04ids_f04_inventory_destock_signature_destockscore_126d_jerk_v106_signal,
    f04ids_f04_inventory_destock_signature_destockscore_252d_jerk_v107_signal,
    f04ids_f04_inventory_destock_signature_idyema_21d_jerk_v108_signal,
    f04ids_f04_inventory_destock_signature_idyema_63d_jerk_v109_signal,
    f04ids_f04_inventory_destock_signature_idyema_126d_jerk_v110_signal,
    f04ids_f04_inventory_destock_signature_itrema_21d_jerk_v111_signal,
    f04ids_f04_inventory_destock_signature_itrema_63d_jerk_v112_signal,
    f04ids_f04_inventory_destock_signature_itrema_126d_jerk_v113_signal,
    f04ids_f04_inventory_destock_signature_iggema_21d_jerk_v114_signal,
    f04ids_f04_inventory_destock_signature_iggema_63d_jerk_v115_signal,
    f04ids_f04_inventory_destock_signature_iggema_126d_jerk_v116_signal,
    f04ids_f04_inventory_destock_signature_itrassets_21d_jerk_v117_signal,
    f04ids_f04_inventory_destock_signature_itrassets_63d_jerk_v118_signal,
    f04ids_f04_inventory_destock_signature_itrassets_126d_jerk_v119_signal,
    f04ids_f04_inventory_destock_signature_itrassets_252d_jerk_v120_signal,
    f04ids_f04_inventory_destock_signature_itrcor_21d_jerk_v121_signal,
    f04ids_f04_inventory_destock_signature_itrcor_63d_jerk_v122_signal,
    f04ids_f04_inventory_destock_signature_itrcor_126d_jerk_v123_signal,
    f04ids_f04_inventory_destock_signature_itrcor_252d_jerk_v124_signal,
    f04ids_f04_inventory_destock_signature_idylog_21d_jerk_v125_signal,
    f04ids_f04_inventory_destock_signature_idylog_63d_jerk_v126_signal,
    f04ids_f04_inventory_destock_signature_idylog_126d_jerk_v127_signal,
    f04ids_f04_inventory_destock_signature_idylog_252d_jerk_v128_signal,
    f04ids_f04_inventory_destock_signature_itrlog_21d_jerk_v129_signal,
    f04ids_f04_inventory_destock_signature_itrlog_63d_jerk_v130_signal,
    f04ids_f04_inventory_destock_signature_itrlog_126d_jerk_v131_signal,
    f04ids_f04_inventory_destock_signature_itrlog_252d_jerk_v132_signal,
    f04ids_f04_inventory_destock_signature_iggsign_21d_jerk_v133_signal,
    f04ids_f04_inventory_destock_signature_iggsign_63d_jerk_v134_signal,
    f04ids_f04_inventory_destock_signature_iggsign_126d_jerk_v135_signal,
    f04ids_f04_inventory_destock_signature_iggsign_252d_jerk_v136_signal,
    f04ids_f04_inventory_destock_signature_idyxrev_21d_jerk_v137_signal,
    f04ids_f04_inventory_destock_signature_idyxrev_63d_jerk_v138_signal,
    f04ids_f04_inventory_destock_signature_idyxrev_126d_jerk_v139_signal,
    f04ids_f04_inventory_destock_signature_idyxrev_252d_jerk_v140_signal,
    f04ids_f04_inventory_destock_signature_itrxrev_21d_jerk_v141_signal,
    f04ids_f04_inventory_destock_signature_itrxrev_63d_jerk_v142_signal,
    f04ids_f04_inventory_destock_signature_itrxrev_126d_jerk_v143_signal,
    f04ids_f04_inventory_destock_signature_itrxrev_252d_jerk_v144_signal,
    f04ids_f04_inventory_destock_signature_iggxrev_21d_jerk_v145_signal,
    f04ids_f04_inventory_destock_signature_iggxrev_63d_jerk_v146_signal,
    f04ids_f04_inventory_destock_signature_iggxrev_126d_jerk_v147_signal,
    f04ids_f04_inventory_destock_signature_iggxrev_252d_jerk_v148_signal,
    f04ids_f04_inventory_destock_signature_itrcorz_21d_jerk_v149_signal,
    f04ids_f04_inventory_destock_signature_itrcorz_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_INVENTORY_DESTOCK_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f04_inventory_days', '_f04_inventory_to_revenue', '_f04_inventory_growth_gap')
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
    print(f"OK f04_inventory_destock_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
