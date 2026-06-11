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
_F34_CAPEX_REF = {"s": None}


def _f34_revenue_accel(revenue, w):
    g = revenue.pct_change(periods=max(1, w // 2))
    return g.diff(periods=max(1, w // 2))


def _f34_capex_revenue_dynamics(capex, w):
    g = capex.pct_change(periods=max(1, w // 2))
    return g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f34_ev_growth_signature_combo(revenue, capex, w):
    accel = _f34_revenue_accel(revenue, w)
    capdyn = _f34_capex_revenue_dynamics(capex, w)
    return accel * capdyn


def _f34_ev_growth_signature(revenue, w):
    accel = _f34_revenue_accel(revenue, w)
    cap = _F34_CAPEX_REF["s"]
    if cap is None:
        return accel
    capdyn = _f34_capex_revenue_dynamics(cap, w)
    return accel * capdyn
def f34ega_f34_ev_growth_acceleration_phase_63d_slope_v001_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_63d_slope_v002_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_63d_slope_v003_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_63d_slope_v004_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_63d_slope_v005_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_126d_slope_v006_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_126d_slope_v007_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_126d_slope_v008_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_126d_slope_v009_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_126d_slope_v010_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_252d_slope_v011_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_252d_slope_v012_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_252d_slope_v013_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_252d_slope_v014_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_252d_slope_v015_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_504d_slope_v016_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_504d_slope_v017_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_504d_slope_v018_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_504d_slope_v019_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_504d_slope_v020_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_378d_slope_v021_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_378d_slope_v022_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_378d_slope_v023_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_378d_slope_v024_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_378d_slope_v025_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_21d_slope_v026_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_21d_slope_v027_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_21d_slope_v028_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_42d_slope_v029_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_42d_slope_v030_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group B v031-v060: slopes of margin cycle pos × closeadj
def f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v031_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v032_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v033_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v034_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v035_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v036_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v037_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v038_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v039_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v040_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v041_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v042_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v043_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v044_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v045_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v046_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v047_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v048_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v049_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v050_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v051_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v052_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v053_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v054_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v055_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v056_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v057_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v058_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_42d_slope_v059_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_42d_slope_v060_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group C v061-v090: slopes of OEM cycle score × closeadj
def f34ega_f34_ev_growth_acceleration_score_63d_slope_v061_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_63d_slope_v062_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_63d_slope_v063_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_63d_slope_v064_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_63d_slope_v065_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_slope_v066_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_slope_v067_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_slope_v068_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_slope_v069_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_slope_v070_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_slope_v071_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_slope_v072_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_slope_v073_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_slope_v074_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_slope_v075_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_slope_v076_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_slope_v077_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_slope_v078_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_slope_v079_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_slope_v080_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_slope_v081_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_slope_v082_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_slope_v083_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_slope_v084_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_slope_v085_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_21d_slope_v086_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_21d_slope_v087_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_21d_slope_v088_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_42d_slope_v089_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_42d_slope_v090_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group D v091-v120: slope_pct variations of phase × ppnenet
def f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_slope_v091_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 63) * _mean(ppnenet, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_slope_v092_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 63) * _mean(ppnenet, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_slope_v093_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 126) * _mean(ppnenet, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_slope_v094_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 126) * _mean(ppnenet, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_slope_v095_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 252) * _mean(ppnenet, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_slope_v096_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 252) * _mean(ppnenet, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_slope_v097_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 504) * _mean(ppnenet, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_slope_v098_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 504) * _mean(ppnenet, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_slope_v099_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * _mean(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_slope_v100_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * _mean(revenue, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_slope_v101_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * _mean(revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_slope_v102_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * _mean(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_slope_v103_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * _mean(revenue, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_slope_v104_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * _mean(revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_slope_v105_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * _mean(revenue, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_slope_v106_signal(revenue, capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 504) * _mean(revenue, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_63d_slope_v107_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * _mean(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_63d_slope_v108_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * _mean(revenue, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_126d_slope_v109_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * _mean(revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_126d_slope_v110_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * _mean(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_252d_slope_v111_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * _mean(revenue, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_252d_slope_v112_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * _mean(revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_504d_slope_v113_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * _mean(revenue, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_504d_slope_v114_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 504) * _mean(revenue, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_378d_slope_v115_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * _mean(revenue, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_378d_slope_v116_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 378) * _mean(revenue, 189) * closeadj
    result = _slope_pct(base, 89)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signed_63d_slope_v117_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 63)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signed_126d_slope_v118_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 126)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signed_252d_slope_v119_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 252)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signed_504d_slope_v120_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 504)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group E v121-v150: slopes of various combos and z-scores
def f34ega_f34_ev_growth_acceleration_phasez_63d_slope_v121_signal(revenue, closeadj):
    base = _z(_f34_revenue_accel(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phasez_126d_slope_v122_signal(revenue, closeadj):
    base = _z(_f34_revenue_accel(revenue, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phasez_252d_slope_v123_signal(revenue, closeadj):
    base = _z(_f34_revenue_accel(revenue, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mposz_63d_slope_v124_signal(capex, closeadj):
    base = _z(_f34_capex_revenue_dynamics(capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mposz_126d_slope_v125_signal(capex, closeadj):
    base = _z(_f34_capex_revenue_dynamics(capex, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mposz_252d_slope_v126_signal(capex, closeadj):
    base = _z(_f34_capex_revenue_dynamics(capex, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_ema_63d_slope_v127_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_ema_126d_slope_v128_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_ema_252d_slope_v129_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_ema_63d_slope_v130_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_ema_126d_slope_v131_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_ema_252d_slope_v132_signal(capex, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_margin_63d_slope_v133_signal(revenue, capex, closeadj):
    base = _f34_revenue_accel(revenue, 63) * _mean(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_margin_126d_slope_v134_signal(revenue, capex, closeadj):
    base = _f34_revenue_accel(revenue, 126) * _mean(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_margin_252d_slope_v135_signal(revenue, capex, closeadj):
    base = _f34_revenue_accel(revenue, 252) * _mean(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_revgrow_63d_slope_v136_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 63) * revenue.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_revgrow_126d_slope_v137_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 126) * revenue.pct_change(126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_revgrow_252d_slope_v138_signal(revenue, closeadj):
    base = _f34_revenue_accel(revenue, 252) * revenue.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_div_63d_slope_v139_signal(revenue, capex, closeadj):
    p = _f34_revenue_accel(revenue, 63)
    m = _f34_capex_revenue_dynamics(capex, 63)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_div_126d_slope_v140_signal(revenue, capex, closeadj):
    p = _f34_revenue_accel(revenue, 126)
    m = _f34_capex_revenue_dynamics(capex, 126)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_div_252d_slope_v141_signal(revenue, capex, closeadj):
    p = _f34_revenue_accel(revenue, 252)
    m = _f34_capex_revenue_dynamics(capex, 252)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capexz_63d_slope_v142_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 63) * _z(ppnenet, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capexz_126d_slope_v143_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 126) * _z(ppnenet, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capexz_252d_slope_v144_signal(revenue, ppnenet, closeadj):
    base = _f34_revenue_accel(revenue, 252) * _z(ppnenet, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_margin_63d_slope_v145_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 63) * capex * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_margin_126d_slope_v146_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 126) * capex * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_margin_252d_slope_v147_signal(revenue, capex, closeadj):
    base = _f34_ev_growth_signature_combo(revenue, capex, 252) * capex * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_63d_slope_v148_signal(capex, ppnenet, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 63) * _mean(ppnenet, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_126d_slope_v149_signal(capex, ppnenet, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 126) * _mean(ppnenet, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_252d_slope_v150_signal(capex, ppnenet, closeadj):
    base = _f34_capex_revenue_dynamics(capex, 252) * _mean(ppnenet, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34ega_f34_ev_growth_acceleration_phase_63d_slope_v001_signal,
    f34ega_f34_ev_growth_acceleration_phase_63d_slope_v002_signal,
    f34ega_f34_ev_growth_acceleration_phase_63d_slope_v003_signal,
    f34ega_f34_ev_growth_acceleration_phase_63d_slope_v004_signal,
    f34ega_f34_ev_growth_acceleration_phase_63d_slope_v005_signal,
    f34ega_f34_ev_growth_acceleration_phase_126d_slope_v006_signal,
    f34ega_f34_ev_growth_acceleration_phase_126d_slope_v007_signal,
    f34ega_f34_ev_growth_acceleration_phase_126d_slope_v008_signal,
    f34ega_f34_ev_growth_acceleration_phase_126d_slope_v009_signal,
    f34ega_f34_ev_growth_acceleration_phase_126d_slope_v010_signal,
    f34ega_f34_ev_growth_acceleration_phase_252d_slope_v011_signal,
    f34ega_f34_ev_growth_acceleration_phase_252d_slope_v012_signal,
    f34ega_f34_ev_growth_acceleration_phase_252d_slope_v013_signal,
    f34ega_f34_ev_growth_acceleration_phase_252d_slope_v014_signal,
    f34ega_f34_ev_growth_acceleration_phase_252d_slope_v015_signal,
    f34ega_f34_ev_growth_acceleration_phase_504d_slope_v016_signal,
    f34ega_f34_ev_growth_acceleration_phase_504d_slope_v017_signal,
    f34ega_f34_ev_growth_acceleration_phase_504d_slope_v018_signal,
    f34ega_f34_ev_growth_acceleration_phase_504d_slope_v019_signal,
    f34ega_f34_ev_growth_acceleration_phase_504d_slope_v020_signal,
    f34ega_f34_ev_growth_acceleration_phase_378d_slope_v021_signal,
    f34ega_f34_ev_growth_acceleration_phase_378d_slope_v022_signal,
    f34ega_f34_ev_growth_acceleration_phase_378d_slope_v023_signal,
    f34ega_f34_ev_growth_acceleration_phase_378d_slope_v024_signal,
    f34ega_f34_ev_growth_acceleration_phase_378d_slope_v025_signal,
    f34ega_f34_ev_growth_acceleration_phase_21d_slope_v026_signal,
    f34ega_f34_ev_growth_acceleration_phase_21d_slope_v027_signal,
    f34ega_f34_ev_growth_acceleration_phase_21d_slope_v028_signal,
    f34ega_f34_ev_growth_acceleration_phase_42d_slope_v029_signal,
    f34ega_f34_ev_growth_acceleration_phase_42d_slope_v030_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v031_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v032_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v033_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v034_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_slope_v035_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v036_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v037_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v038_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v039_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_slope_v040_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v041_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v042_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v043_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v044_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_slope_v045_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v046_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v047_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v048_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v049_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_slope_v050_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v051_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v052_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v053_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v054_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_slope_v055_signal,
    f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v056_signal,
    f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v057_signal,
    f34ega_f34_ev_growth_acceleration_mpos_21d_slope_v058_signal,
    f34ega_f34_ev_growth_acceleration_mpos_42d_slope_v059_signal,
    f34ega_f34_ev_growth_acceleration_mpos_42d_slope_v060_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_slope_v061_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_slope_v062_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_slope_v063_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_slope_v064_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_slope_v065_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_slope_v066_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_slope_v067_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_slope_v068_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_slope_v069_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_slope_v070_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_slope_v071_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_slope_v072_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_slope_v073_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_slope_v074_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_slope_v075_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_slope_v076_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_slope_v077_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_slope_v078_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_slope_v079_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_slope_v080_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_slope_v081_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_slope_v082_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_slope_v083_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_slope_v084_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_slope_v085_signal,
    f34ega_f34_ev_growth_acceleration_score_21d_slope_v086_signal,
    f34ega_f34_ev_growth_acceleration_score_21d_slope_v087_signal,
    f34ega_f34_ev_growth_acceleration_score_21d_slope_v088_signal,
    f34ega_f34_ev_growth_acceleration_score_42d_slope_v089_signal,
    f34ega_f34_ev_growth_acceleration_score_42d_slope_v090_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_slope_v091_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_slope_v092_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_slope_v093_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_slope_v094_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_slope_v095_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_slope_v096_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_slope_v097_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_slope_v098_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_slope_v099_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_slope_v100_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_slope_v101_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_slope_v102_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_slope_v103_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_slope_v104_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_slope_v105_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_slope_v106_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_63d_slope_v107_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_63d_slope_v108_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_126d_slope_v109_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_126d_slope_v110_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_252d_slope_v111_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_252d_slope_v112_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_504d_slope_v113_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_504d_slope_v114_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_378d_slope_v115_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_378d_slope_v116_signal,
    f34ega_f34_ev_growth_acceleration_score_signed_63d_slope_v117_signal,
    f34ega_f34_ev_growth_acceleration_score_signed_126d_slope_v118_signal,
    f34ega_f34_ev_growth_acceleration_score_signed_252d_slope_v119_signal,
    f34ega_f34_ev_growth_acceleration_score_signed_504d_slope_v120_signal,
    f34ega_f34_ev_growth_acceleration_phasez_63d_slope_v121_signal,
    f34ega_f34_ev_growth_acceleration_phasez_126d_slope_v122_signal,
    f34ega_f34_ev_growth_acceleration_phasez_252d_slope_v123_signal,
    f34ega_f34_ev_growth_acceleration_mposz_63d_slope_v124_signal,
    f34ega_f34_ev_growth_acceleration_mposz_126d_slope_v125_signal,
    f34ega_f34_ev_growth_acceleration_mposz_252d_slope_v126_signal,
    f34ega_f34_ev_growth_acceleration_phase_ema_63d_slope_v127_signal,
    f34ega_f34_ev_growth_acceleration_phase_ema_126d_slope_v128_signal,
    f34ega_f34_ev_growth_acceleration_phase_ema_252d_slope_v129_signal,
    f34ega_f34_ev_growth_acceleration_mpos_ema_63d_slope_v130_signal,
    f34ega_f34_ev_growth_acceleration_mpos_ema_126d_slope_v131_signal,
    f34ega_f34_ev_growth_acceleration_mpos_ema_252d_slope_v132_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_margin_63d_slope_v133_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_margin_126d_slope_v134_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_margin_252d_slope_v135_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_revgrow_63d_slope_v136_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_revgrow_126d_slope_v137_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_revgrow_252d_slope_v138_signal,
    f34ega_f34_ev_growth_acceleration_div_63d_slope_v139_signal,
    f34ega_f34_ev_growth_acceleration_div_126d_slope_v140_signal,
    f34ega_f34_ev_growth_acceleration_div_252d_slope_v141_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capexz_63d_slope_v142_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capexz_126d_slope_v143_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capexz_252d_slope_v144_signal,
    f34ega_f34_ev_growth_acceleration_score_x_margin_63d_slope_v145_signal,
    f34ega_f34_ev_growth_acceleration_score_x_margin_126d_slope_v146_signal,
    f34ega_f34_ev_growth_acceleration_score_x_margin_252d_slope_v147_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_63d_slope_v148_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_126d_slope_v149_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_EV_GROWTH_ACCELERATION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    _F34_CAPEX_REF["s"] = capex

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex, "ppnenet": ppnenet}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_revenue_accel", "_f34_capex_revenue_dynamics", "_f34_ev_growth_signature")
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
    print(f"OK f34_ev_growth_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
