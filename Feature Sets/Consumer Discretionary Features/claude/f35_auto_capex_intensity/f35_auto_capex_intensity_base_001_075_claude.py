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
_F35_REV_REF = {"s": None}
_F35_PPE_REF = {"s": None}
_F35_FCF_REF = {"s": None}


def _f35_capex_intensity(capex, w):
    cap_m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    rev = _F35_REV_REF["s"]
    if rev is None:
        denom = cap_m
    else:
        denom = rev.rolling(w, min_periods=max(1, w // 2)).mean()
    return cap_m / denom.replace(0, np.nan)


def _f35_capex_to_ppe(capex, w):
    cap_m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    ppe = _F35_PPE_REF["s"]
    if ppe is None:
        denom = cap_m
    else:
        denom = ppe.rolling(w, min_periods=max(1, w // 2)).mean()
    return cap_m / denom.replace(0, np.nan)


def _f35_capex_burden_combo(capex, fcf, w):
    cap_m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    fcf_m = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return cap_m / (fcf_m.abs().replace(0, np.nan) + cap_m)


def _f35_capex_burden(capex, w):
    cap_m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    fcf = _F35_FCF_REF["s"]
    if fcf is None:
        denom = cap_m
    else:
        denom = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return cap_m / (denom.abs().replace(0, np.nan) + cap_m)
def f35aci_f35_auto_capex_intensity_revphase_63d_base_v001_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_revphase_126d_base_v002_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_revphase_252d_base_v003_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_revphase_504d_base_v004_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_revphase_378d_base_v005_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006-v010: margin cycle position scaled
def f35aci_f35_auto_capex_intensity_mpos_63d_base_v006_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_base_v007_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_base_v008_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_base_v009_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_base_v010_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011-v015: composite OEM cycle score
def f35aci_f35_auto_capex_intensity_score_63d_base_v011_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_base_v012_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_base_v013_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_base_v014_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_base_v015_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v020: capex phase × fcf (cycle * investment)
def f35aci_f35_auto_capex_intensity_phase_x_capex_63d_base_v016_signal(capex, fcf, closeadj):
    result = _f35_capex_intensity(capex, 63) * _mean(fcf, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_126d_base_v017_signal(capex, fcf, closeadj):
    result = _f35_capex_intensity(capex, 126) * _mean(fcf, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_252d_base_v018_signal(capex, fcf, closeadj):
    result = _f35_capex_intensity(capex, 252) * _mean(fcf, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_504d_base_v019_signal(capex, fcf, closeadj):
    result = _f35_capex_intensity(capex, 504) * _mean(fcf, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_378d_base_v020_signal(capex, fcf, closeadj):
    result = _f35_capex_intensity(capex, 378) * _mean(fcf, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021-v025: margin position × capex level (capex-weighted)
def f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_base_v021_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 63) * _mean(capex, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_base_v022_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 126) * _mean(capex, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_base_v023_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 252) * _mean(capex, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_base_v024_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 504) * _mean(capex, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_378d_base_v025_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 378) * _mean(capex, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026-v030: capex cycle phase × ebitdamargin level
def f35aci_f35_auto_capex_intensity_phase_x_marginlvl_63d_base_v026_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_intensity(capex, 63) * _mean(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_marginlvl_126d_base_v027_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_intensity(capex, 126) * _mean(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_marginlvl_252d_base_v028_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_intensity(capex, 252) * _mean(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_marginlvl_504d_base_v029_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_intensity(capex, 504) * _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_marginlvl_378d_base_v030_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_intensity(capex, 378) * _mean(ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v035: rev cycle phase z over secondary window
def f35aci_f35_auto_capex_intensity_phase_z_63d_base_v031_signal(capex, closeadj):
    result = _z(_f35_capex_intensity(capex, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_z_126d_base_v032_signal(capex, closeadj):
    result = _z(_f35_capex_intensity(capex, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_z_252d_base_v033_signal(capex, closeadj):
    result = _z(_f35_capex_intensity(capex, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_z_504d_base_v034_signal(capex, closeadj):
    result = _z(_f35_capex_intensity(capex, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_z_378d_base_v035_signal(capex, closeadj):
    result = _z(_f35_capex_intensity(capex, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v040: margin cycle pos z
def f35aci_f35_auto_capex_intensity_mpos_z_63d_base_v036_signal(ebitdamargin, closeadj):
    result = _z(_f35_capex_to_ppe(ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_z_126d_base_v037_signal(ebitdamargin, closeadj):
    result = _z(_f35_capex_to_ppe(ebitdamargin, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_z_252d_base_v038_signal(ebitdamargin, closeadj):
    result = _z(_f35_capex_to_ppe(ebitdamargin, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_z_504d_base_v039_signal(ebitdamargin, closeadj):
    result = _z(_f35_capex_to_ppe(ebitdamargin, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_z_378d_base_v040_signal(ebitdamargin, closeadj):
    result = _z(_f35_capex_to_ppe(ebitdamargin, 378), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v045: rolling std of capex cycle phase
def f35aci_f35_auto_capex_intensity_phase_std_63d_base_v041_signal(capex, closeadj):
    result = _std(_f35_capex_intensity(capex, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_std_126d_base_v042_signal(capex, closeadj):
    result = _std(_f35_capex_intensity(capex, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_std_252d_base_v043_signal(capex, closeadj):
    result = _std(_f35_capex_intensity(capex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_std_504d_base_v044_signal(capex, closeadj):
    result = _std(_f35_capex_intensity(capex, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_std_378d_base_v045_signal(capex, closeadj):
    result = _std(_f35_capex_intensity(capex, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v050: rolling mean of margin cycle pos
def f35aci_f35_auto_capex_intensity_mpos_mean_63d_base_v046_signal(ebitdamargin, closeadj):
    result = _mean(_f35_capex_to_ppe(ebitdamargin, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_mean_126d_base_v047_signal(ebitdamargin, closeadj):
    result = _mean(_f35_capex_to_ppe(ebitdamargin, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_mean_252d_base_v048_signal(ebitdamargin, closeadj):
    result = _mean(_f35_capex_to_ppe(ebitdamargin, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_mean_504d_base_v049_signal(ebitdamargin, closeadj):
    result = _mean(_f35_capex_to_ppe(ebitdamargin, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_mean_378d_base_v050_signal(ebitdamargin, closeadj):
    result = _mean(_f35_capex_to_ppe(ebitdamargin, 378), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v055: composite score × capex
def f35aci_f35_auto_capex_intensity_score_x_rev_63d_base_v051_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 63) * _mean(capex, 21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_126d_base_v052_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 126) * _mean(capex, 63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_252d_base_v053_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 252) * _mean(capex, 126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_504d_base_v054_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 504) * _mean(capex, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_378d_base_v055_signal(capex, ebitdamargin, closeadj):
    result = _f35_capex_burden_combo(capex, ebitdamargin, 378) * _mean(capex, 189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056-v060: capex phase normalized by fcf intensity
def f35aci_f35_auto_capex_intensity_phase_per_capex_63d_base_v056_signal(capex, fcf, closeadj):
    capint = _safe_div(_mean(fcf, 63), _mean(capex, 63))
    result = _f35_capex_intensity(capex, 63) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_per_capex_126d_base_v057_signal(capex, fcf, closeadj):
    capint = _safe_div(_mean(fcf, 126), _mean(capex, 126))
    result = _f35_capex_intensity(capex, 126) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_per_capex_252d_base_v058_signal(capex, fcf, closeadj):
    capint = _safe_div(_mean(fcf, 252), _mean(capex, 252))
    result = _f35_capex_intensity(capex, 252) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_per_capex_504d_base_v059_signal(capex, fcf, closeadj):
    capint = _safe_div(_mean(fcf, 504), _mean(capex, 504))
    result = _f35_capex_intensity(capex, 504) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_per_capex_378d_base_v060_signal(capex, fcf, closeadj):
    capint = _safe_div(_mean(fcf, 378), _mean(capex, 378))
    result = _f35_capex_intensity(capex, 378) * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v065: margin cycle pos × fcf
def f35aci_f35_auto_capex_intensity_mpos_x_capex_63d_base_v061_signal(ebitdamargin, fcf, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 63) * _mean(fcf, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_126d_base_v062_signal(ebitdamargin, fcf, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 126) * _mean(fcf, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_252d_base_v063_signal(ebitdamargin, fcf, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 252) * _mean(fcf, 126) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_504d_base_v064_signal(ebitdamargin, fcf, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 504) * _mean(fcf, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_378d_base_v065_signal(ebitdamargin, fcf, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 378) * _mean(fcf, 189) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v070: cycle score sign × magnitude expanded
def f35aci_f35_auto_capex_intensity_score_signedmag_63d_base_v066_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 63)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signedmag_126d_base_v067_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 126)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signedmag_252d_base_v068_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 252)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signedmag_504d_base_v069_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 504)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signedmag_378d_base_v070_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 378)
    result = np.sign(s) * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071-v075: phase × close (price scaled cycle)
def f35aci_f35_auto_capex_intensity_phase_x_close_21d_base_v071_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_close_42d_base_v072_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_close_189d_base_v073_signal(capex, closeadj):
    result = _f35_capex_intensity(capex, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_close_42d_base_v074_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_close_189d_base_v075_signal(ebitdamargin, closeadj):
    result = _f35_capex_to_ppe(ebitdamargin, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35aci_f35_auto_capex_intensity_revphase_63d_base_v001_signal,
    f35aci_f35_auto_capex_intensity_revphase_126d_base_v002_signal,
    f35aci_f35_auto_capex_intensity_revphase_252d_base_v003_signal,
    f35aci_f35_auto_capex_intensity_revphase_504d_base_v004_signal,
    f35aci_f35_auto_capex_intensity_revphase_378d_base_v005_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_base_v006_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_base_v007_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_base_v008_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_base_v009_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_base_v010_signal,
    f35aci_f35_auto_capex_intensity_score_63d_base_v011_signal,
    f35aci_f35_auto_capex_intensity_score_126d_base_v012_signal,
    f35aci_f35_auto_capex_intensity_score_252d_base_v013_signal,
    f35aci_f35_auto_capex_intensity_score_504d_base_v014_signal,
    f35aci_f35_auto_capex_intensity_score_378d_base_v015_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_63d_base_v016_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_126d_base_v017_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_252d_base_v018_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_504d_base_v019_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_378d_base_v020_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_base_v021_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_base_v022_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_base_v023_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_base_v024_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_378d_base_v025_signal,
    f35aci_f35_auto_capex_intensity_phase_x_marginlvl_63d_base_v026_signal,
    f35aci_f35_auto_capex_intensity_phase_x_marginlvl_126d_base_v027_signal,
    f35aci_f35_auto_capex_intensity_phase_x_marginlvl_252d_base_v028_signal,
    f35aci_f35_auto_capex_intensity_phase_x_marginlvl_504d_base_v029_signal,
    f35aci_f35_auto_capex_intensity_phase_x_marginlvl_378d_base_v030_signal,
    f35aci_f35_auto_capex_intensity_phase_z_63d_base_v031_signal,
    f35aci_f35_auto_capex_intensity_phase_z_126d_base_v032_signal,
    f35aci_f35_auto_capex_intensity_phase_z_252d_base_v033_signal,
    f35aci_f35_auto_capex_intensity_phase_z_504d_base_v034_signal,
    f35aci_f35_auto_capex_intensity_phase_z_378d_base_v035_signal,
    f35aci_f35_auto_capex_intensity_mpos_z_63d_base_v036_signal,
    f35aci_f35_auto_capex_intensity_mpos_z_126d_base_v037_signal,
    f35aci_f35_auto_capex_intensity_mpos_z_252d_base_v038_signal,
    f35aci_f35_auto_capex_intensity_mpos_z_504d_base_v039_signal,
    f35aci_f35_auto_capex_intensity_mpos_z_378d_base_v040_signal,
    f35aci_f35_auto_capex_intensity_phase_std_63d_base_v041_signal,
    f35aci_f35_auto_capex_intensity_phase_std_126d_base_v042_signal,
    f35aci_f35_auto_capex_intensity_phase_std_252d_base_v043_signal,
    f35aci_f35_auto_capex_intensity_phase_std_504d_base_v044_signal,
    f35aci_f35_auto_capex_intensity_phase_std_378d_base_v045_signal,
    f35aci_f35_auto_capex_intensity_mpos_mean_63d_base_v046_signal,
    f35aci_f35_auto_capex_intensity_mpos_mean_126d_base_v047_signal,
    f35aci_f35_auto_capex_intensity_mpos_mean_252d_base_v048_signal,
    f35aci_f35_auto_capex_intensity_mpos_mean_504d_base_v049_signal,
    f35aci_f35_auto_capex_intensity_mpos_mean_378d_base_v050_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_63d_base_v051_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_126d_base_v052_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_252d_base_v053_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_504d_base_v054_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_378d_base_v055_signal,
    f35aci_f35_auto_capex_intensity_phase_per_capex_63d_base_v056_signal,
    f35aci_f35_auto_capex_intensity_phase_per_capex_126d_base_v057_signal,
    f35aci_f35_auto_capex_intensity_phase_per_capex_252d_base_v058_signal,
    f35aci_f35_auto_capex_intensity_phase_per_capex_504d_base_v059_signal,
    f35aci_f35_auto_capex_intensity_phase_per_capex_378d_base_v060_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_63d_base_v061_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_126d_base_v062_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_252d_base_v063_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_504d_base_v064_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_378d_base_v065_signal,
    f35aci_f35_auto_capex_intensity_score_signedmag_63d_base_v066_signal,
    f35aci_f35_auto_capex_intensity_score_signedmag_126d_base_v067_signal,
    f35aci_f35_auto_capex_intensity_score_signedmag_252d_base_v068_signal,
    f35aci_f35_auto_capex_intensity_score_signedmag_504d_base_v069_signal,
    f35aci_f35_auto_capex_intensity_score_signedmag_378d_base_v070_signal,
    f35aci_f35_auto_capex_intensity_phase_x_close_21d_base_v071_signal,
    f35aci_f35_auto_capex_intensity_phase_x_close_42d_base_v072_signal,
    f35aci_f35_auto_capex_intensity_phase_x_close_189d_base_v073_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_close_42d_base_v074_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_close_189d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_AUTO_CAPEX_INTENSITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    # f35 also needs ebitdamargin synthesized because original f31 features used it as
    # a function arg name; we keep the arg name to avoid signature collisions.
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    _F35_REV_REF["s"] = revenue
    _F35_PPE_REF["s"] = ppnenet
    _F35_FCF_REF["s"] = fcf

    cols = {"closeadj": closeadj, "capex": capex, "revenue": revenue, "ppnenet": ppnenet, "fcf": fcf,
            "ebitdamargin": ebitdamargin}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_capex_intensity", "_f35_capex_to_ppe", "_f35_capex_burden")
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
    print(f"OK f35_auto_capex_intensity_base_001_075_claude: {n_features} features pass")
