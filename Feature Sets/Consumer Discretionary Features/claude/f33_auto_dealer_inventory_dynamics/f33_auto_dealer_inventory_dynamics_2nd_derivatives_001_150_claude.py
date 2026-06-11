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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
_F33_COR_REF = {"s": None}
_F33_REV_REF = {"s": None}
_F33_DEBT_REF = {"s": None}


def _f33_dealer_inv_days(inventory, w):
    inv_m = inventory.rolling(w, min_periods=max(1, w // 2)).mean()
    cor = _F33_COR_REF["s"]
    if cor is None:
        # Fallback: use inventory's own scale as denominator
        denom = inv_m
    else:
        denom = cor.rolling(w, min_periods=max(1, w // 2)).mean()
    return (inv_m / denom.replace(0, np.nan)) * 365.0


def _f33_inv_revenue_gap(inventory, w):
    inv_m = inventory.rolling(w, min_periods=max(1, w // 2)).mean()
    rev = _F33_REV_REF["s"]
    if rev is None:
        denom = inv_m
    else:
        denom = rev.rolling(w, min_periods=max(1, w // 2)).mean()
    return inv_m / denom.replace(0, np.nan)


def _f33_floor_plan_pressure(inventory, w):
    inv_m = inventory.rolling(w, min_periods=max(1, w // 2)).mean()
    debt = _F33_DEBT_REF["s"]
    if debt is None:
        denom = inv_m
    else:
        denom = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return inv_m / denom.replace(0, np.nan)


def _f33_floor_plan_pressure_combo(inventory, revenue, w):
    """2-arg variant for OEM-score-style usage."""
    p = _f33_dealer_inv_days(inventory, w)
    g = _f33_inv_revenue_gap(inventory, w)
    return p * g
def f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v001_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v002_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v003_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v004_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v005_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v006_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v007_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v008_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v009_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v010_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v011_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v012_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v013_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v014_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v015_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v016_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v017_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v018_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v019_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v020_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v021_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v022_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v023_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v024_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v025_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v026_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v027_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v028_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_42d_slope_v029_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_42d_slope_v030_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group B v031-v060: slopes of margin cycle pos × closeadj
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v031_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v032_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v033_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v034_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v035_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v036_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v037_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v038_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v039_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v040_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v041_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v042_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v043_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v044_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v045_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v046_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v047_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v048_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v049_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v050_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v051_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v052_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v053_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v054_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v055_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v056_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v057_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v058_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_42d_slope_v059_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_42d_slope_v060_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group C v061-v090: slopes of OEM cycle score × closeadj
def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v061_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v062_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v063_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v064_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v065_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v066_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v067_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v068_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v069_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v070_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v071_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v072_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v073_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v074_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v075_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v076_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v077_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v078_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v079_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v080_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v081_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v082_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v083_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v084_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v085_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v086_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v087_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v088_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_42d_slope_v089_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_42d_slope_v090_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group D v091-v120: slope_pct variations of phase × capex
def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_slope_v091_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_slope_v092_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_slope_v093_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_slope_v094_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_slope_v095_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_slope_v096_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_slope_v097_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_slope_v098_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_slope_v099_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * _mean(inventory, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_slope_v100_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * _mean(inventory, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_slope_v101_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * _mean(inventory, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_slope_v102_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * _mean(inventory, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_slope_v103_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * _mean(inventory, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_slope_v104_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * _mean(inventory, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_slope_v105_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * _mean(inventory, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_slope_v106_signal(inventory, ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 504) * _mean(inventory, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_slope_v107_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * _mean(inventory, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_slope_v108_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * _mean(inventory, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_slope_v109_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * _mean(inventory, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_slope_v110_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * _mean(inventory, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_slope_v111_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * _mean(inventory, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_slope_v112_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * _mean(inventory, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_slope_v113_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * _mean(inventory, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_slope_v114_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * _mean(inventory, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_slope_v115_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * _mean(inventory, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_slope_v116_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * _mean(inventory, 189) * closeadj
    result = _slope_pct(base, 89)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signed_63d_slope_v117_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signed_126d_slope_v118_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signed_252d_slope_v119_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signed_504d_slope_v120_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group E v121-v150: slopes of various combos and z-scores
def f33adi_f33_auto_dealer_inventory_dynamics_phasez_63d_slope_v121_signal(inventory, closeadj):
    base = _z(_f33_dealer_inv_days(inventory, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phasez_126d_slope_v122_signal(inventory, closeadj):
    base = _z(_f33_dealer_inv_days(inventory, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phasez_252d_slope_v123_signal(inventory, closeadj):
    base = _z(_f33_dealer_inv_days(inventory, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mposz_63d_slope_v124_signal(ebitdamargin, closeadj):
    base = _z(_f33_inv_revenue_gap(ebitdamargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mposz_126d_slope_v125_signal(ebitdamargin, closeadj):
    base = _z(_f33_inv_revenue_gap(ebitdamargin, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mposz_252d_slope_v126_signal(ebitdamargin, closeadj):
    base = _z(_f33_inv_revenue_gap(ebitdamargin, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_63d_slope_v127_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_126d_slope_v128_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_252d_slope_v129_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_63d_slope_v130_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_126d_slope_v131_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_252d_slope_v132_signal(ebitdamargin, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_63d_slope_v133_signal(inventory, ebitdamargin, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * _mean(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_126d_slope_v134_signal(inventory, ebitdamargin, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * _mean(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_252d_slope_v135_signal(inventory, ebitdamargin, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * _mean(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_63d_slope_v136_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * inventory.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_126d_slope_v137_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * inventory.pct_change(126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_252d_slope_v138_signal(inventory, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * inventory.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_div_63d_slope_v139_signal(inventory, ebitdamargin, closeadj):
    p = _f33_dealer_inv_days(inventory, 63)
    m = _f33_inv_revenue_gap(ebitdamargin, 63)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_div_126d_slope_v140_signal(inventory, ebitdamargin, closeadj):
    p = _f33_dealer_inv_days(inventory, 126)
    m = _f33_inv_revenue_gap(ebitdamargin, 126)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_div_252d_slope_v141_signal(inventory, ebitdamargin, closeadj):
    p = _f33_dealer_inv_days(inventory, 252)
    m = _f33_inv_revenue_gap(ebitdamargin, 252)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_63d_slope_v142_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 63) * _z(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_126d_slope_v143_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 126) * _z(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_252d_slope_v144_signal(inventory, capex, closeadj):
    base = _f33_dealer_inv_days(inventory, 252) * _z(capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_63d_slope_v145_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_126d_slope_v146_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_252d_slope_v147_signal(inventory, ebitdamargin, closeadj):
    base = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_63d_slope_v148_signal(ebitdamargin, capex, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_126d_slope_v149_signal(ebitdamargin, capex, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_252d_slope_v150_signal(ebitdamargin, capex, closeadj):
    base = _f33_inv_revenue_gap(ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v001_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v002_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v003_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v004_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_63d_slope_v005_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v006_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v007_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v008_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v009_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_126d_slope_v010_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v011_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v012_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v013_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v014_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_252d_slope_v015_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v016_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v017_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v018_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v019_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_504d_slope_v020_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v021_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v022_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v023_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v024_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_378d_slope_v025_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v026_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v027_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_21d_slope_v028_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_42d_slope_v029_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_42d_slope_v030_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v031_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v032_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v033_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v034_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_slope_v035_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v036_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v037_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v038_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v039_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_slope_v040_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v041_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v042_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v043_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v044_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_slope_v045_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v046_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v047_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v048_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v049_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_slope_v050_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v051_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v052_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v053_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v054_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_slope_v055_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v056_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v057_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_21d_slope_v058_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_42d_slope_v059_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_42d_slope_v060_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v061_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v062_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v063_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v064_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_slope_v065_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v066_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v067_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v068_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v069_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_slope_v070_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v071_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v072_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v073_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v074_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_slope_v075_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v076_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v077_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v078_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v079_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_slope_v080_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v081_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v082_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v083_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v084_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_slope_v085_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v086_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v087_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_21d_slope_v088_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_42d_slope_v089_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_42d_slope_v090_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_slope_v091_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_slope_v092_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_slope_v093_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_slope_v094_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_slope_v095_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_slope_v096_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_slope_v097_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_slope_v098_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_slope_v099_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_slope_v100_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_slope_v101_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_slope_v102_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_slope_v103_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_slope_v104_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_slope_v105_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_slope_v106_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_slope_v107_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_slope_v108_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_slope_v109_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_slope_v110_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_slope_v111_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_slope_v112_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_slope_v113_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_slope_v114_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_slope_v115_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_slope_v116_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signed_63d_slope_v117_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signed_126d_slope_v118_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signed_252d_slope_v119_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signed_504d_slope_v120_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phasez_63d_slope_v121_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phasez_126d_slope_v122_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phasez_252d_slope_v123_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mposz_63d_slope_v124_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mposz_126d_slope_v125_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mposz_252d_slope_v126_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_63d_slope_v127_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_126d_slope_v128_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_ema_252d_slope_v129_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_63d_slope_v130_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_126d_slope_v131_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_ema_252d_slope_v132_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_63d_slope_v133_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_126d_slope_v134_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_margin_252d_slope_v135_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_63d_slope_v136_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_126d_slope_v137_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_revgrow_252d_slope_v138_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_div_63d_slope_v139_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_div_126d_slope_v140_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_div_252d_slope_v141_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_63d_slope_v142_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_126d_slope_v143_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capexz_252d_slope_v144_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_63d_slope_v145_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_126d_slope_v146_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_margin_252d_slope_v147_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_63d_slope_v148_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_126d_slope_v149_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_AUTO_DEALER_INVENTORY_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="inventory")
    cor = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    _F33_COR_REF["s"] = cor
    _F33_REV_REF["s"] = revenue
    _F33_DEBT_REF["s"] = debt

    cols = {"closeadj": closeadj, "inventory": inventory, "cor": cor, "revenue": revenue, "debt": debt,
            "ebitdamargin": ebitdamargin, "capex": capex}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_dealer_inv_days", "_f33_inv_revenue_gap", "_f33_floor_plan_pressure")
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
    print(f"OK f33_auto_dealer_inventory_dynamics_2nd_derivatives_001_150_claude: {n_features} features pass")
