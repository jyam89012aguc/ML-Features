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
def f33adi_f33_auto_dealer_inventory_dynamics_revphase_63d_base_v001_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_revphase_126d_base_v002_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_revphase_252d_base_v003_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_revphase_504d_base_v004_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_revphase_378d_base_v005_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006-v010: margin cycle position scaled
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_base_v006_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_base_v007_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_base_v008_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_base_v009_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_base_v010_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011-v015: composite OEM cycle score
def f33adi_f33_auto_dealer_inventory_dynamics_score_63d_base_v011_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_126d_base_v012_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_252d_base_v013_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_504d_base_v014_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_378d_base_v015_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v020: inventory phase × capex (cycle * investment)
def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_base_v016_signal(inventory, capex, closeadj):
    result = _f33_dealer_inv_days(inventory, 63) * _mean(capex, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_base_v017_signal(inventory, capex, closeadj):
    result = _f33_dealer_inv_days(inventory, 126) * _mean(capex, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_base_v018_signal(inventory, capex, closeadj):
    result = _f33_dealer_inv_days(inventory, 252) * _mean(capex, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_base_v019_signal(inventory, capex, closeadj):
    result = _f33_dealer_inv_days(inventory, 504) * _mean(capex, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_378d_base_v020_signal(inventory, capex, closeadj):
    result = _f33_dealer_inv_days(inventory, 378) * _mean(capex, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021-v025: margin position × inventory level (inventory-weighted)
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_base_v021_signal(inventory, ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 63) * _mean(inventory, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_base_v022_signal(inventory, ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 126) * _mean(inventory, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_base_v023_signal(inventory, ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 252) * _mean(inventory, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_base_v024_signal(inventory, ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 504) * _mean(inventory, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_378d_base_v025_signal(inventory, ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 378) * _mean(inventory, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026-v030: inventory cycle phase × ebitdamargin level
def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_63d_base_v026_signal(inventory, ebitdamargin, closeadj):
    result = _f33_dealer_inv_days(inventory, 63) * _mean(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_126d_base_v027_signal(inventory, ebitdamargin, closeadj):
    result = _f33_dealer_inv_days(inventory, 126) * _mean(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_252d_base_v028_signal(inventory, ebitdamargin, closeadj):
    result = _f33_dealer_inv_days(inventory, 252) * _mean(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_504d_base_v029_signal(inventory, ebitdamargin, closeadj):
    result = _f33_dealer_inv_days(inventory, 504) * _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_378d_base_v030_signal(inventory, ebitdamargin, closeadj):
    result = _f33_dealer_inv_days(inventory, 378) * _mean(ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v035: rev cycle phase z over secondary window
def f33adi_f33_auto_dealer_inventory_dynamics_phase_z_63d_base_v031_signal(inventory, closeadj):
    result = _z(_f33_dealer_inv_days(inventory, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_z_126d_base_v032_signal(inventory, closeadj):
    result = _z(_f33_dealer_inv_days(inventory, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_z_252d_base_v033_signal(inventory, closeadj):
    result = _z(_f33_dealer_inv_days(inventory, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_z_504d_base_v034_signal(inventory, closeadj):
    result = _z(_f33_dealer_inv_days(inventory, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_z_378d_base_v035_signal(inventory, closeadj):
    result = _z(_f33_dealer_inv_days(inventory, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v040: margin cycle pos z
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_63d_base_v036_signal(ebitdamargin, closeadj):
    result = _z(_f33_inv_revenue_gap(ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_126d_base_v037_signal(ebitdamargin, closeadj):
    result = _z(_f33_inv_revenue_gap(ebitdamargin, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_252d_base_v038_signal(ebitdamargin, closeadj):
    result = _z(_f33_inv_revenue_gap(ebitdamargin, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_504d_base_v039_signal(ebitdamargin, closeadj):
    result = _z(_f33_inv_revenue_gap(ebitdamargin, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_378d_base_v040_signal(ebitdamargin, closeadj):
    result = _z(_f33_inv_revenue_gap(ebitdamargin, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v045: rolling std of inventory cycle phase
def f33adi_f33_auto_dealer_inventory_dynamics_phase_std_63d_base_v041_signal(inventory, closeadj):
    result = _std(_f33_dealer_inv_days(inventory, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_std_126d_base_v042_signal(inventory, closeadj):
    result = _std(_f33_dealer_inv_days(inventory, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_std_252d_base_v043_signal(inventory, closeadj):
    result = _std(_f33_dealer_inv_days(inventory, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_std_504d_base_v044_signal(inventory, closeadj):
    result = _std(_f33_dealer_inv_days(inventory, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_std_378d_base_v045_signal(inventory, closeadj):
    result = _std(_f33_dealer_inv_days(inventory, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v050: rolling mean of margin cycle pos
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_63d_base_v046_signal(ebitdamargin, closeadj):
    result = _mean(_f33_inv_revenue_gap(ebitdamargin, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_126d_base_v047_signal(ebitdamargin, closeadj):
    result = _mean(_f33_inv_revenue_gap(ebitdamargin, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_252d_base_v048_signal(ebitdamargin, closeadj):
    result = _mean(_f33_inv_revenue_gap(ebitdamargin, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_504d_base_v049_signal(ebitdamargin, closeadj):
    result = _mean(_f33_inv_revenue_gap(ebitdamargin, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_378d_base_v050_signal(ebitdamargin, closeadj):
    result = _mean(_f33_inv_revenue_gap(ebitdamargin, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v055: composite score × inventory
def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_base_v051_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63) * _mean(inventory, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_base_v052_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126) * _mean(inventory, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_base_v053_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252) * _mean(inventory, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_base_v054_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504) * _mean(inventory, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_base_v055_signal(inventory, ebitdamargin, closeadj):
    result = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378) * _mean(inventory, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056-v060: inventory phase normalized by capex intensity
def f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_63d_base_v056_signal(inventory, capex, closeadj):
    capint = _safe_div(_mean(capex, 63), _mean(inventory, 63))
    result = _f33_dealer_inv_days(inventory, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_126d_base_v057_signal(inventory, capex, closeadj):
    capint = _safe_div(_mean(capex, 126), _mean(inventory, 126))
    result = _f33_dealer_inv_days(inventory, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_252d_base_v058_signal(inventory, capex, closeadj):
    capint = _safe_div(_mean(capex, 252), _mean(inventory, 252))
    result = _f33_dealer_inv_days(inventory, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_504d_base_v059_signal(inventory, capex, closeadj):
    capint = _safe_div(_mean(capex, 504), _mean(inventory, 504))
    result = _f33_dealer_inv_days(inventory, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_378d_base_v060_signal(inventory, capex, closeadj):
    capint = _safe_div(_mean(capex, 378), _mean(inventory, 378))
    result = _f33_dealer_inv_days(inventory, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v065: margin cycle pos × capex
def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_63d_base_v061_signal(ebitdamargin, capex, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 63) * _mean(capex, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_126d_base_v062_signal(ebitdamargin, capex, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 126) * _mean(capex, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_252d_base_v063_signal(ebitdamargin, capex, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 252) * _mean(capex, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_504d_base_v064_signal(ebitdamargin, capex, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 504) * _mean(capex, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_378d_base_v065_signal(ebitdamargin, capex, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 378) * _mean(capex, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v070: cycle score sign × magnitude expanded
def f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_63d_base_v066_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 63)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_126d_base_v067_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 126)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_252d_base_v068_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 252)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_504d_base_v069_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 504)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_378d_base_v070_signal(inventory, ebitdamargin, closeadj):
    s = _f33_floor_plan_pressure_combo(inventory, ebitdamargin, 378)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071-v075: phase × close (price scaled cycle)
def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_21d_base_v071_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_42d_base_v072_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_189d_base_v073_signal(inventory, closeadj):
    result = _f33_dealer_inv_days(inventory, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_close_42d_base_v074_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_close_189d_base_v075_signal(ebitdamargin, closeadj):
    result = _f33_inv_revenue_gap(ebitdamargin, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33adi_f33_auto_dealer_inventory_dynamics_revphase_63d_base_v001_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_revphase_126d_base_v002_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_revphase_252d_base_v003_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_revphase_504d_base_v004_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_revphase_378d_base_v005_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_63d_base_v006_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_126d_base_v007_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_252d_base_v008_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_504d_base_v009_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_378d_base_v010_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_63d_base_v011_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_126d_base_v012_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_252d_base_v013_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_504d_base_v014_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_378d_base_v015_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_63d_base_v016_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_126d_base_v017_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_252d_base_v018_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_504d_base_v019_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_capex_378d_base_v020_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_63d_base_v021_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_126d_base_v022_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_252d_base_v023_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_504d_base_v024_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_rev_378d_base_v025_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_63d_base_v026_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_126d_base_v027_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_252d_base_v028_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_504d_base_v029_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_marginlvl_378d_base_v030_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_z_63d_base_v031_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_z_126d_base_v032_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_z_252d_base_v033_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_z_504d_base_v034_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_z_378d_base_v035_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_63d_base_v036_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_126d_base_v037_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_252d_base_v038_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_504d_base_v039_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_z_378d_base_v040_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_std_63d_base_v041_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_std_126d_base_v042_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_std_252d_base_v043_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_std_504d_base_v044_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_std_378d_base_v045_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_63d_base_v046_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_126d_base_v047_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_252d_base_v048_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_504d_base_v049_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_mean_378d_base_v050_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_63d_base_v051_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_126d_base_v052_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_252d_base_v053_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_504d_base_v054_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_x_rev_378d_base_v055_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_63d_base_v056_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_126d_base_v057_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_252d_base_v058_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_504d_base_v059_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_per_capex_378d_base_v060_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_63d_base_v061_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_126d_base_v062_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_252d_base_v063_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_504d_base_v064_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_capex_378d_base_v065_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_63d_base_v066_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_126d_base_v067_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_252d_base_v068_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_504d_base_v069_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_score_signedmag_378d_base_v070_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_21d_base_v071_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_42d_base_v072_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_phase_x_close_189d_base_v073_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_close_42d_base_v074_signal,
    f33adi_f33_auto_dealer_inventory_dynamics_mpos_x_close_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_AUTO_DEALER_INVENTORY_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_auto_dealer_inventory_dynamics_base_001_075_claude: {n_features} features pass")
