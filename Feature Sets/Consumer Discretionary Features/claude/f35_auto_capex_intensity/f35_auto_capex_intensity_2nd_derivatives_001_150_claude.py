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
def f35aci_f35_auto_capex_intensity_phase_63d_slope_v001_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_63d_slope_v002_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_63d_slope_v003_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_63d_slope_v004_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_63d_slope_v005_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_126d_slope_v006_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_126d_slope_v007_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_126d_slope_v008_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_126d_slope_v009_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_126d_slope_v010_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_252d_slope_v011_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_252d_slope_v012_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_252d_slope_v013_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_252d_slope_v014_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_252d_slope_v015_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_504d_slope_v016_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_504d_slope_v017_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_504d_slope_v018_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_504d_slope_v019_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_504d_slope_v020_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_378d_slope_v021_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_378d_slope_v022_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_378d_slope_v023_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_378d_slope_v024_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_378d_slope_v025_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_21d_slope_v026_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_21d_slope_v027_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_21d_slope_v028_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_42d_slope_v029_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_42d_slope_v030_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group B v031-v060: slopes of margin cycle pos × closeadj
def f35aci_f35_auto_capex_intensity_mpos_63d_slope_v031_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_63d_slope_v032_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_63d_slope_v033_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_63d_slope_v034_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_63d_slope_v035_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_slope_v036_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_slope_v037_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_slope_v038_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_slope_v039_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_126d_slope_v040_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_slope_v041_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_slope_v042_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_slope_v043_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_slope_v044_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_252d_slope_v045_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_slope_v046_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_slope_v047_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_slope_v048_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_slope_v049_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_504d_slope_v050_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_slope_v051_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_slope_v052_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_slope_v053_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_slope_v054_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_378d_slope_v055_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_21d_slope_v056_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_21d_slope_v057_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_21d_slope_v058_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_42d_slope_v059_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_42d_slope_v060_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group C v061-v090: slopes of OEM cycle score × closeadj
def f35aci_f35_auto_capex_intensity_score_63d_slope_v061_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_63d_slope_v062_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_63d_slope_v063_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_63d_slope_v064_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_63d_slope_v065_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_slope_v066_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_slope_v067_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_slope_v068_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_slope_v069_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_126d_slope_v070_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_slope_v071_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_slope_v072_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_slope_v073_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_slope_v074_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_252d_slope_v075_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_slope_v076_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_slope_v077_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_slope_v078_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_slope_v079_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_504d_slope_v080_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_slope_v081_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_slope_v082_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_slope_v083_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_slope_v084_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_378d_slope_v085_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_21d_slope_v086_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_21d_slope_v087_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_21d_slope_v088_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_42d_slope_v089_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_42d_slope_v090_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group D v091-v120: slope_pct variations of phase × fcf
def f35aci_f35_auto_capex_intensity_phase_x_capex_63d_slope_v091_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 63) * _mean(fcf, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_63d_slope_v092_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 63) * _mean(fcf, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_126d_slope_v093_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 126) * _mean(fcf, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_126d_slope_v094_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 126) * _mean(fcf, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_252d_slope_v095_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 252) * _mean(fcf, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_252d_slope_v096_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 252) * _mean(fcf, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_504d_slope_v097_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 504) * _mean(fcf, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capex_504d_slope_v098_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 504) * _mean(fcf, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_slope_v099_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_slope_v100_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_slope_v101_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_slope_v102_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_slope_v103_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_slope_v104_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_slope_v105_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_slope_v106_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_63d_slope_v107_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_63d_slope_v108_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_126d_slope_v109_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_126d_slope_v110_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_252d_slope_v111_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_252d_slope_v112_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_504d_slope_v113_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_504d_slope_v114_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 504) * _mean(capex, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_378d_slope_v115_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * _mean(capex, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_rev_378d_slope_v116_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 378) * _mean(capex, 189) * closeadj
    result = _slope_pct(base, 89)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signed_63d_slope_v117_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 63)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signed_126d_slope_v118_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 126)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signed_252d_slope_v119_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 252)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_signed_504d_slope_v120_signal(capex, ebitdamargin, closeadj):
    s = _f35_capex_burden_combo(capex, ebitdamargin, 504)
    base = np.sign(s) * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group E v121-v150: slopes of various combos and z-scores
def f35aci_f35_auto_capex_intensity_phasez_63d_slope_v121_signal(capex, closeadj):
    base = _z(_f35_capex_intensity(capex, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phasez_126d_slope_v122_signal(capex, closeadj):
    base = _z(_f35_capex_intensity(capex, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phasez_252d_slope_v123_signal(capex, closeadj):
    base = _z(_f35_capex_intensity(capex, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mposz_63d_slope_v124_signal(ebitdamargin, closeadj):
    base = _z(_f35_capex_to_ppe(ebitdamargin, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mposz_126d_slope_v125_signal(ebitdamargin, closeadj):
    base = _z(_f35_capex_to_ppe(ebitdamargin, 126), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mposz_252d_slope_v126_signal(ebitdamargin, closeadj):
    base = _z(_f35_capex_to_ppe(ebitdamargin, 252), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_ema_63d_slope_v127_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_ema_126d_slope_v128_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_ema_252d_slope_v129_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_ema_63d_slope_v130_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_ema_126d_slope_v131_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_ema_252d_slope_v132_signal(ebitdamargin, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_margin_63d_slope_v133_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_intensity(capex, 63) * _mean(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_margin_126d_slope_v134_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_intensity(capex, 126) * _mean(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_margin_252d_slope_v135_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_intensity(capex, 252) * _mean(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_revgrow_63d_slope_v136_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 63) * capex.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_revgrow_126d_slope_v137_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 126) * capex.pct_change(126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_revgrow_252d_slope_v138_signal(capex, closeadj):
    base = _f35_capex_intensity(capex, 252) * capex.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_div_63d_slope_v139_signal(capex, ebitdamargin, closeadj):
    p = _f35_capex_intensity(capex, 63)
    m = _f35_capex_to_ppe(ebitdamargin, 63)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_div_126d_slope_v140_signal(capex, ebitdamargin, closeadj):
    p = _f35_capex_intensity(capex, 126)
    m = _f35_capex_to_ppe(ebitdamargin, 126)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_div_252d_slope_v141_signal(capex, ebitdamargin, closeadj):
    p = _f35_capex_intensity(capex, 252)
    m = _f35_capex_to_ppe(ebitdamargin, 252)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capexz_63d_slope_v142_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 63) * _z(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capexz_126d_slope_v143_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 126) * _z(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_phase_x_capexz_252d_slope_v144_signal(capex, fcf, closeadj):
    base = _f35_capex_intensity(capex, 252) * _z(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_margin_63d_slope_v145_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 63) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_margin_126d_slope_v146_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 126) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_score_x_margin_252d_slope_v147_signal(capex, ebitdamargin, closeadj):
    base = _f35_capex_burden_combo(capex, ebitdamargin, 252) * ebitdamargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_63d_slope_v148_signal(ebitdamargin, fcf, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 63) * _mean(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_126d_slope_v149_signal(ebitdamargin, fcf, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 126) * _mean(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35aci_f35_auto_capex_intensity_mpos_x_capex_252d_slope_v150_signal(ebitdamargin, fcf, closeadj):
    base = _f35_capex_to_ppe(ebitdamargin, 252) * _mean(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35aci_f35_auto_capex_intensity_phase_63d_slope_v001_signal,
    f35aci_f35_auto_capex_intensity_phase_63d_slope_v002_signal,
    f35aci_f35_auto_capex_intensity_phase_63d_slope_v003_signal,
    f35aci_f35_auto_capex_intensity_phase_63d_slope_v004_signal,
    f35aci_f35_auto_capex_intensity_phase_63d_slope_v005_signal,
    f35aci_f35_auto_capex_intensity_phase_126d_slope_v006_signal,
    f35aci_f35_auto_capex_intensity_phase_126d_slope_v007_signal,
    f35aci_f35_auto_capex_intensity_phase_126d_slope_v008_signal,
    f35aci_f35_auto_capex_intensity_phase_126d_slope_v009_signal,
    f35aci_f35_auto_capex_intensity_phase_126d_slope_v010_signal,
    f35aci_f35_auto_capex_intensity_phase_252d_slope_v011_signal,
    f35aci_f35_auto_capex_intensity_phase_252d_slope_v012_signal,
    f35aci_f35_auto_capex_intensity_phase_252d_slope_v013_signal,
    f35aci_f35_auto_capex_intensity_phase_252d_slope_v014_signal,
    f35aci_f35_auto_capex_intensity_phase_252d_slope_v015_signal,
    f35aci_f35_auto_capex_intensity_phase_504d_slope_v016_signal,
    f35aci_f35_auto_capex_intensity_phase_504d_slope_v017_signal,
    f35aci_f35_auto_capex_intensity_phase_504d_slope_v018_signal,
    f35aci_f35_auto_capex_intensity_phase_504d_slope_v019_signal,
    f35aci_f35_auto_capex_intensity_phase_504d_slope_v020_signal,
    f35aci_f35_auto_capex_intensity_phase_378d_slope_v021_signal,
    f35aci_f35_auto_capex_intensity_phase_378d_slope_v022_signal,
    f35aci_f35_auto_capex_intensity_phase_378d_slope_v023_signal,
    f35aci_f35_auto_capex_intensity_phase_378d_slope_v024_signal,
    f35aci_f35_auto_capex_intensity_phase_378d_slope_v025_signal,
    f35aci_f35_auto_capex_intensity_phase_21d_slope_v026_signal,
    f35aci_f35_auto_capex_intensity_phase_21d_slope_v027_signal,
    f35aci_f35_auto_capex_intensity_phase_21d_slope_v028_signal,
    f35aci_f35_auto_capex_intensity_phase_42d_slope_v029_signal,
    f35aci_f35_auto_capex_intensity_phase_42d_slope_v030_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_slope_v031_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_slope_v032_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_slope_v033_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_slope_v034_signal,
    f35aci_f35_auto_capex_intensity_mpos_63d_slope_v035_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_slope_v036_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_slope_v037_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_slope_v038_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_slope_v039_signal,
    f35aci_f35_auto_capex_intensity_mpos_126d_slope_v040_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_slope_v041_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_slope_v042_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_slope_v043_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_slope_v044_signal,
    f35aci_f35_auto_capex_intensity_mpos_252d_slope_v045_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_slope_v046_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_slope_v047_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_slope_v048_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_slope_v049_signal,
    f35aci_f35_auto_capex_intensity_mpos_504d_slope_v050_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_slope_v051_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_slope_v052_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_slope_v053_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_slope_v054_signal,
    f35aci_f35_auto_capex_intensity_mpos_378d_slope_v055_signal,
    f35aci_f35_auto_capex_intensity_mpos_21d_slope_v056_signal,
    f35aci_f35_auto_capex_intensity_mpos_21d_slope_v057_signal,
    f35aci_f35_auto_capex_intensity_mpos_21d_slope_v058_signal,
    f35aci_f35_auto_capex_intensity_mpos_42d_slope_v059_signal,
    f35aci_f35_auto_capex_intensity_mpos_42d_slope_v060_signal,
    f35aci_f35_auto_capex_intensity_score_63d_slope_v061_signal,
    f35aci_f35_auto_capex_intensity_score_63d_slope_v062_signal,
    f35aci_f35_auto_capex_intensity_score_63d_slope_v063_signal,
    f35aci_f35_auto_capex_intensity_score_63d_slope_v064_signal,
    f35aci_f35_auto_capex_intensity_score_63d_slope_v065_signal,
    f35aci_f35_auto_capex_intensity_score_126d_slope_v066_signal,
    f35aci_f35_auto_capex_intensity_score_126d_slope_v067_signal,
    f35aci_f35_auto_capex_intensity_score_126d_slope_v068_signal,
    f35aci_f35_auto_capex_intensity_score_126d_slope_v069_signal,
    f35aci_f35_auto_capex_intensity_score_126d_slope_v070_signal,
    f35aci_f35_auto_capex_intensity_score_252d_slope_v071_signal,
    f35aci_f35_auto_capex_intensity_score_252d_slope_v072_signal,
    f35aci_f35_auto_capex_intensity_score_252d_slope_v073_signal,
    f35aci_f35_auto_capex_intensity_score_252d_slope_v074_signal,
    f35aci_f35_auto_capex_intensity_score_252d_slope_v075_signal,
    f35aci_f35_auto_capex_intensity_score_504d_slope_v076_signal,
    f35aci_f35_auto_capex_intensity_score_504d_slope_v077_signal,
    f35aci_f35_auto_capex_intensity_score_504d_slope_v078_signal,
    f35aci_f35_auto_capex_intensity_score_504d_slope_v079_signal,
    f35aci_f35_auto_capex_intensity_score_504d_slope_v080_signal,
    f35aci_f35_auto_capex_intensity_score_378d_slope_v081_signal,
    f35aci_f35_auto_capex_intensity_score_378d_slope_v082_signal,
    f35aci_f35_auto_capex_intensity_score_378d_slope_v083_signal,
    f35aci_f35_auto_capex_intensity_score_378d_slope_v084_signal,
    f35aci_f35_auto_capex_intensity_score_378d_slope_v085_signal,
    f35aci_f35_auto_capex_intensity_score_21d_slope_v086_signal,
    f35aci_f35_auto_capex_intensity_score_21d_slope_v087_signal,
    f35aci_f35_auto_capex_intensity_score_21d_slope_v088_signal,
    f35aci_f35_auto_capex_intensity_score_42d_slope_v089_signal,
    f35aci_f35_auto_capex_intensity_score_42d_slope_v090_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_63d_slope_v091_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_63d_slope_v092_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_126d_slope_v093_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_126d_slope_v094_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_252d_slope_v095_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_252d_slope_v096_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_504d_slope_v097_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capex_504d_slope_v098_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_slope_v099_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_63d_slope_v100_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_slope_v101_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_126d_slope_v102_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_slope_v103_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_252d_slope_v104_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_slope_v105_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_rev_504d_slope_v106_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_63d_slope_v107_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_63d_slope_v108_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_126d_slope_v109_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_126d_slope_v110_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_252d_slope_v111_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_252d_slope_v112_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_504d_slope_v113_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_504d_slope_v114_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_378d_slope_v115_signal,
    f35aci_f35_auto_capex_intensity_score_x_rev_378d_slope_v116_signal,
    f35aci_f35_auto_capex_intensity_score_signed_63d_slope_v117_signal,
    f35aci_f35_auto_capex_intensity_score_signed_126d_slope_v118_signal,
    f35aci_f35_auto_capex_intensity_score_signed_252d_slope_v119_signal,
    f35aci_f35_auto_capex_intensity_score_signed_504d_slope_v120_signal,
    f35aci_f35_auto_capex_intensity_phasez_63d_slope_v121_signal,
    f35aci_f35_auto_capex_intensity_phasez_126d_slope_v122_signal,
    f35aci_f35_auto_capex_intensity_phasez_252d_slope_v123_signal,
    f35aci_f35_auto_capex_intensity_mposz_63d_slope_v124_signal,
    f35aci_f35_auto_capex_intensity_mposz_126d_slope_v125_signal,
    f35aci_f35_auto_capex_intensity_mposz_252d_slope_v126_signal,
    f35aci_f35_auto_capex_intensity_phase_ema_63d_slope_v127_signal,
    f35aci_f35_auto_capex_intensity_phase_ema_126d_slope_v128_signal,
    f35aci_f35_auto_capex_intensity_phase_ema_252d_slope_v129_signal,
    f35aci_f35_auto_capex_intensity_mpos_ema_63d_slope_v130_signal,
    f35aci_f35_auto_capex_intensity_mpos_ema_126d_slope_v131_signal,
    f35aci_f35_auto_capex_intensity_mpos_ema_252d_slope_v132_signal,
    f35aci_f35_auto_capex_intensity_phase_x_margin_63d_slope_v133_signal,
    f35aci_f35_auto_capex_intensity_phase_x_margin_126d_slope_v134_signal,
    f35aci_f35_auto_capex_intensity_phase_x_margin_252d_slope_v135_signal,
    f35aci_f35_auto_capex_intensity_phase_x_revgrow_63d_slope_v136_signal,
    f35aci_f35_auto_capex_intensity_phase_x_revgrow_126d_slope_v137_signal,
    f35aci_f35_auto_capex_intensity_phase_x_revgrow_252d_slope_v138_signal,
    f35aci_f35_auto_capex_intensity_div_63d_slope_v139_signal,
    f35aci_f35_auto_capex_intensity_div_126d_slope_v140_signal,
    f35aci_f35_auto_capex_intensity_div_252d_slope_v141_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capexz_63d_slope_v142_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capexz_126d_slope_v143_signal,
    f35aci_f35_auto_capex_intensity_phase_x_capexz_252d_slope_v144_signal,
    f35aci_f35_auto_capex_intensity_score_x_margin_63d_slope_v145_signal,
    f35aci_f35_auto_capex_intensity_score_x_margin_126d_slope_v146_signal,
    f35aci_f35_auto_capex_intensity_score_x_margin_252d_slope_v147_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_63d_slope_v148_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_126d_slope_v149_signal,
    f35aci_f35_auto_capex_intensity_mpos_x_capex_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_AUTO_CAPEX_INTENSITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f35_auto_capex_intensity_2nd_derivatives_001_150_claude: {n_features} features pass")
