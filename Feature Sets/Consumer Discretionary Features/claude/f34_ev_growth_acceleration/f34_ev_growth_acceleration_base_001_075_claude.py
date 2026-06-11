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
def f34ega_f34_ev_growth_acceleration_revphase_63d_base_v001_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_revphase_126d_base_v002_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_revphase_252d_base_v003_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_revphase_504d_base_v004_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_revphase_378d_base_v005_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006-v010: margin cycle position scaled
def f34ega_f34_ev_growth_acceleration_mpos_63d_base_v006_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_126d_base_v007_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_252d_base_v008_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_504d_base_v009_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_378d_base_v010_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011-v015: composite OEM cycle score
def f34ega_f34_ev_growth_acceleration_score_63d_base_v011_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_126d_base_v012_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_252d_base_v013_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_504d_base_v014_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_378d_base_v015_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v020: revenue phase × ppnenet (cycle * investment)
def f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_base_v016_signal(revenue, ppnenet, closeadj):
    result = _f34_revenue_accel(revenue, 63) * _mean(ppnenet, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_base_v017_signal(revenue, ppnenet, closeadj):
    result = _f34_revenue_accel(revenue, 126) * _mean(ppnenet, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_base_v018_signal(revenue, ppnenet, closeadj):
    result = _f34_revenue_accel(revenue, 252) * _mean(ppnenet, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_base_v019_signal(revenue, ppnenet, closeadj):
    result = _f34_revenue_accel(revenue, 504) * _mean(ppnenet, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_capex_378d_base_v020_signal(revenue, ppnenet, closeadj):
    result = _f34_revenue_accel(revenue, 378) * _mean(ppnenet, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021-v025: margin position × revenue level (revenue-weighted)
def f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_base_v021_signal(revenue, capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 63) * _mean(revenue, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_base_v022_signal(revenue, capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 126) * _mean(revenue, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_base_v023_signal(revenue, capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 252) * _mean(revenue, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_base_v024_signal(revenue, capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 504) * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_rev_378d_base_v025_signal(revenue, capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 378) * _mean(revenue, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026-v030: revenue cycle phase × capex level
def f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_63d_base_v026_signal(revenue, capex, closeadj):
    result = _f34_revenue_accel(revenue, 63) * _mean(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_126d_base_v027_signal(revenue, capex, closeadj):
    result = _f34_revenue_accel(revenue, 126) * _mean(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_252d_base_v028_signal(revenue, capex, closeadj):
    result = _f34_revenue_accel(revenue, 252) * _mean(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_504d_base_v029_signal(revenue, capex, closeadj):
    result = _f34_revenue_accel(revenue, 504) * _mean(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_378d_base_v030_signal(revenue, capex, closeadj):
    result = _f34_revenue_accel(revenue, 378) * _mean(capex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v035: rev cycle phase z over secondary window
def f34ega_f34_ev_growth_acceleration_phase_z_63d_base_v031_signal(revenue, closeadj):
    result = _z(_f34_revenue_accel(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_z_126d_base_v032_signal(revenue, closeadj):
    result = _z(_f34_revenue_accel(revenue, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_z_252d_base_v033_signal(revenue, closeadj):
    result = _z(_f34_revenue_accel(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_z_504d_base_v034_signal(revenue, closeadj):
    result = _z(_f34_revenue_accel(revenue, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_z_378d_base_v035_signal(revenue, closeadj):
    result = _z(_f34_revenue_accel(revenue, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v040: margin cycle pos z
def f34ega_f34_ev_growth_acceleration_mpos_z_63d_base_v036_signal(capex, closeadj):
    result = _z(_f34_capex_revenue_dynamics(capex, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_z_126d_base_v037_signal(capex, closeadj):
    result = _z(_f34_capex_revenue_dynamics(capex, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_z_252d_base_v038_signal(capex, closeadj):
    result = _z(_f34_capex_revenue_dynamics(capex, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_z_504d_base_v039_signal(capex, closeadj):
    result = _z(_f34_capex_revenue_dynamics(capex, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_z_378d_base_v040_signal(capex, closeadj):
    result = _z(_f34_capex_revenue_dynamics(capex, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v045: rolling std of revenue cycle phase
def f34ega_f34_ev_growth_acceleration_phase_std_63d_base_v041_signal(revenue, closeadj):
    result = _std(_f34_revenue_accel(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_std_126d_base_v042_signal(revenue, closeadj):
    result = _std(_f34_revenue_accel(revenue, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_std_252d_base_v043_signal(revenue, closeadj):
    result = _std(_f34_revenue_accel(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_std_504d_base_v044_signal(revenue, closeadj):
    result = _std(_f34_revenue_accel(revenue, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_std_378d_base_v045_signal(revenue, closeadj):
    result = _std(_f34_revenue_accel(revenue, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v050: rolling mean of margin cycle pos
def f34ega_f34_ev_growth_acceleration_mpos_mean_63d_base_v046_signal(capex, closeadj):
    result = _mean(_f34_capex_revenue_dynamics(capex, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_mean_126d_base_v047_signal(capex, closeadj):
    result = _mean(_f34_capex_revenue_dynamics(capex, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_mean_252d_base_v048_signal(capex, closeadj):
    result = _mean(_f34_capex_revenue_dynamics(capex, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_mean_504d_base_v049_signal(capex, closeadj):
    result = _mean(_f34_capex_revenue_dynamics(capex, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_mean_378d_base_v050_signal(capex, closeadj):
    result = _mean(_f34_capex_revenue_dynamics(capex, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v055: composite score × revenue
def f34ega_f34_ev_growth_acceleration_score_x_rev_63d_base_v051_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 63) * _mean(revenue, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_126d_base_v052_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 126) * _mean(revenue, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_252d_base_v053_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 252) * _mean(revenue, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_504d_base_v054_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 504) * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_x_rev_378d_base_v055_signal(revenue, capex, closeadj):
    result = _f34_ev_growth_signature_combo(revenue, capex, 378) * _mean(revenue, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056-v060: revenue phase normalized by ppnenet intensity
def f34ega_f34_ev_growth_acceleration_phase_per_capex_63d_base_v056_signal(revenue, ppnenet, closeadj):
    capint = _safe_div(_mean(ppnenet, 63), _mean(revenue, 63))
    result = _f34_revenue_accel(revenue, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_per_capex_126d_base_v057_signal(revenue, ppnenet, closeadj):
    capint = _safe_div(_mean(ppnenet, 126), _mean(revenue, 126))
    result = _f34_revenue_accel(revenue, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_per_capex_252d_base_v058_signal(revenue, ppnenet, closeadj):
    capint = _safe_div(_mean(ppnenet, 252), _mean(revenue, 252))
    result = _f34_revenue_accel(revenue, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_per_capex_504d_base_v059_signal(revenue, ppnenet, closeadj):
    capint = _safe_div(_mean(ppnenet, 504), _mean(revenue, 504))
    result = _f34_revenue_accel(revenue, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_per_capex_378d_base_v060_signal(revenue, ppnenet, closeadj):
    capint = _safe_div(_mean(ppnenet, 378), _mean(revenue, 378))
    result = _f34_revenue_accel(revenue, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v065: margin cycle pos × ppnenet
def f34ega_f34_ev_growth_acceleration_mpos_x_capex_63d_base_v061_signal(capex, ppnenet, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 63) * _mean(ppnenet, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_126d_base_v062_signal(capex, ppnenet, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 126) * _mean(ppnenet, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_252d_base_v063_signal(capex, ppnenet, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 252) * _mean(ppnenet, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_504d_base_v064_signal(capex, ppnenet, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 504) * _mean(ppnenet, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_capex_378d_base_v065_signal(capex, ppnenet, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 378) * _mean(ppnenet, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v070: cycle score sign × magnitude expanded
def f34ega_f34_ev_growth_acceleration_score_signedmag_63d_base_v066_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 63)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signedmag_126d_base_v067_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 126)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signedmag_252d_base_v068_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 252)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signedmag_504d_base_v069_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 504)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_score_signedmag_378d_base_v070_signal(revenue, capex, closeadj):
    s = _f34_ev_growth_signature_combo(revenue, capex, 378)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071-v075: phase × close (price scaled cycle)
def f34ega_f34_ev_growth_acceleration_phase_x_close_21d_base_v071_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_close_42d_base_v072_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_phase_x_close_189d_base_v073_signal(revenue, closeadj):
    result = _f34_revenue_accel(revenue, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_close_42d_base_v074_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34ega_f34_ev_growth_acceleration_mpos_x_close_189d_base_v075_signal(capex, closeadj):
    result = _f34_capex_revenue_dynamics(capex, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34ega_f34_ev_growth_acceleration_revphase_63d_base_v001_signal,
    f34ega_f34_ev_growth_acceleration_revphase_126d_base_v002_signal,
    f34ega_f34_ev_growth_acceleration_revphase_252d_base_v003_signal,
    f34ega_f34_ev_growth_acceleration_revphase_504d_base_v004_signal,
    f34ega_f34_ev_growth_acceleration_revphase_378d_base_v005_signal,
    f34ega_f34_ev_growth_acceleration_mpos_63d_base_v006_signal,
    f34ega_f34_ev_growth_acceleration_mpos_126d_base_v007_signal,
    f34ega_f34_ev_growth_acceleration_mpos_252d_base_v008_signal,
    f34ega_f34_ev_growth_acceleration_mpos_504d_base_v009_signal,
    f34ega_f34_ev_growth_acceleration_mpos_378d_base_v010_signal,
    f34ega_f34_ev_growth_acceleration_score_63d_base_v011_signal,
    f34ega_f34_ev_growth_acceleration_score_126d_base_v012_signal,
    f34ega_f34_ev_growth_acceleration_score_252d_base_v013_signal,
    f34ega_f34_ev_growth_acceleration_score_504d_base_v014_signal,
    f34ega_f34_ev_growth_acceleration_score_378d_base_v015_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_63d_base_v016_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_126d_base_v017_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_252d_base_v018_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_504d_base_v019_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_capex_378d_base_v020_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_63d_base_v021_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_126d_base_v022_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_252d_base_v023_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_504d_base_v024_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_rev_378d_base_v025_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_63d_base_v026_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_126d_base_v027_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_252d_base_v028_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_504d_base_v029_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_marginlvl_378d_base_v030_signal,
    f34ega_f34_ev_growth_acceleration_phase_z_63d_base_v031_signal,
    f34ega_f34_ev_growth_acceleration_phase_z_126d_base_v032_signal,
    f34ega_f34_ev_growth_acceleration_phase_z_252d_base_v033_signal,
    f34ega_f34_ev_growth_acceleration_phase_z_504d_base_v034_signal,
    f34ega_f34_ev_growth_acceleration_phase_z_378d_base_v035_signal,
    f34ega_f34_ev_growth_acceleration_mpos_z_63d_base_v036_signal,
    f34ega_f34_ev_growth_acceleration_mpos_z_126d_base_v037_signal,
    f34ega_f34_ev_growth_acceleration_mpos_z_252d_base_v038_signal,
    f34ega_f34_ev_growth_acceleration_mpos_z_504d_base_v039_signal,
    f34ega_f34_ev_growth_acceleration_mpos_z_378d_base_v040_signal,
    f34ega_f34_ev_growth_acceleration_phase_std_63d_base_v041_signal,
    f34ega_f34_ev_growth_acceleration_phase_std_126d_base_v042_signal,
    f34ega_f34_ev_growth_acceleration_phase_std_252d_base_v043_signal,
    f34ega_f34_ev_growth_acceleration_phase_std_504d_base_v044_signal,
    f34ega_f34_ev_growth_acceleration_phase_std_378d_base_v045_signal,
    f34ega_f34_ev_growth_acceleration_mpos_mean_63d_base_v046_signal,
    f34ega_f34_ev_growth_acceleration_mpos_mean_126d_base_v047_signal,
    f34ega_f34_ev_growth_acceleration_mpos_mean_252d_base_v048_signal,
    f34ega_f34_ev_growth_acceleration_mpos_mean_504d_base_v049_signal,
    f34ega_f34_ev_growth_acceleration_mpos_mean_378d_base_v050_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_63d_base_v051_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_126d_base_v052_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_252d_base_v053_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_504d_base_v054_signal,
    f34ega_f34_ev_growth_acceleration_score_x_rev_378d_base_v055_signal,
    f34ega_f34_ev_growth_acceleration_phase_per_capex_63d_base_v056_signal,
    f34ega_f34_ev_growth_acceleration_phase_per_capex_126d_base_v057_signal,
    f34ega_f34_ev_growth_acceleration_phase_per_capex_252d_base_v058_signal,
    f34ega_f34_ev_growth_acceleration_phase_per_capex_504d_base_v059_signal,
    f34ega_f34_ev_growth_acceleration_phase_per_capex_378d_base_v060_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_63d_base_v061_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_126d_base_v062_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_252d_base_v063_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_504d_base_v064_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_capex_378d_base_v065_signal,
    f34ega_f34_ev_growth_acceleration_score_signedmag_63d_base_v066_signal,
    f34ega_f34_ev_growth_acceleration_score_signedmag_126d_base_v067_signal,
    f34ega_f34_ev_growth_acceleration_score_signedmag_252d_base_v068_signal,
    f34ega_f34_ev_growth_acceleration_score_signedmag_504d_base_v069_signal,
    f34ega_f34_ev_growth_acceleration_score_signedmag_378d_base_v070_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_close_21d_base_v071_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_close_42d_base_v072_signal,
    f34ega_f34_ev_growth_acceleration_phase_x_close_189d_base_v073_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_close_42d_base_v074_signal,
    f34ega_f34_ev_growth_acceleration_mpos_x_close_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_EV_GROWTH_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f34_ev_growth_acceleration_base_001_075_claude: {n_features} features pass")
