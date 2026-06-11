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
def _f22_ppe_growth(ppnenet, w):
    g = ppnenet.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).mean()

def _f22_placement_pulse(capex, ppnenet, w):
    cap_g = capex.pct_change(periods=w)
    ppe_g = ppnenet.pct_change(periods=w)
    return cap_g - ppe_g

def _f22_instrument_install_score(capex, ppnenet, revenue, w):
    cap_g = capex.rolling(w, min_periods=max(1, w // 2)).mean() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    ppe_g = ppnenet.pct_change(periods=w)
    return cap_g * ppe_g


# ===== features =====
def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw5_spct_mul_slope_v001_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw5_sdn_log_slope_v002_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw21_spct_sqrt_slope_v003_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw21_sdn_smean_slope_v004_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw42_spct_sq_slope_v005_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw42_sdn_mul_slope_v006_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw63_spct_log_slope_v007_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw63_sdn_sqrt_slope_v008_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw126_spct_smean_slope_v009_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw126_sdn_sq_slope_v010_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw5_spct_mul_slope_v011_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw5_sdn_log_slope_v012_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw21_spct_sqrt_slope_v013_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw21_sdn_smean_slope_v014_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw42_spct_sq_slope_v015_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw42_sdn_mul_slope_v016_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw63_spct_log_slope_v017_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw63_sdn_sqrt_slope_v018_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw126_spct_smean_slope_v019_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw126_sdn_sq_slope_v020_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw5_spct_mul_slope_v021_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw5_sdn_log_slope_v022_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw21_spct_sqrt_slope_v023_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw21_sdn_smean_slope_v024_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw42_spct_sq_slope_v025_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw42_sdn_mul_slope_v026_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw63_spct_log_slope_v027_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw63_sdn_sqrt_slope_v028_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw126_spct_smean_slope_v029_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw126_sdn_sq_slope_v030_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw5_spct_mul_slope_v031_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw5_sdn_log_slope_v032_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw21_spct_sqrt_slope_v033_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw21_sdn_smean_slope_v034_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw42_spct_sq_slope_v035_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw42_sdn_mul_slope_v036_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw63_spct_log_slope_v037_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw63_sdn_sqrt_slope_v038_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw126_spct_smean_slope_v039_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw126_sdn_sq_slope_v040_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw5_spct_mul_slope_v041_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw5_sdn_log_slope_v042_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw21_spct_sqrt_slope_v043_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw21_sdn_smean_slope_v044_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw42_spct_sq_slope_v045_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw42_sdn_mul_slope_v046_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw63_spct_log_slope_v047_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw63_sdn_sqrt_slope_v048_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw126_spct_smean_slope_v049_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw126_sdn_sq_slope_v050_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw5_spct_mul_slope_v051_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw5_sdn_log_slope_v052_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw21_spct_sqrt_slope_v053_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw21_sdn_smean_slope_v054_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw42_spct_sq_slope_v055_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw42_sdn_mul_slope_v056_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw63_spct_log_slope_v057_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw63_sdn_sqrt_slope_v058_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw126_spct_smean_slope_v059_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw126_sdn_sq_slope_v060_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw5_spct_mul_slope_v061_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw5_sdn_log_slope_v062_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw21_spct_sqrt_slope_v063_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw21_sdn_smean_slope_v064_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw42_spct_sq_slope_v065_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw42_sdn_mul_slope_v066_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw63_spct_log_slope_v067_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw63_sdn_sqrt_slope_v068_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw126_spct_smean_slope_v069_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw126_sdn_sq_slope_v070_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw5_spct_mul_slope_v071_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw5_sdn_log_slope_v072_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw21_spct_sqrt_slope_v073_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw21_sdn_smean_slope_v074_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw42_spct_sq_slope_v075_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw42_sdn_mul_slope_v076_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw63_spct_log_slope_v077_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw63_sdn_sqrt_slope_v078_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw126_spct_smean_slope_v079_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw126_sdn_sq_slope_v080_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw5_spct_mul_slope_v081_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw5_sdn_log_slope_v082_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw21_spct_sqrt_slope_v083_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw21_sdn_smean_slope_v084_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw42_spct_sq_slope_v085_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw42_sdn_mul_slope_v086_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw63_spct_log_slope_v087_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw63_sdn_sqrt_slope_v088_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw126_spct_smean_slope_v089_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw126_sdn_sq_slope_v090_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw5_spct_mul_slope_v091_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw5_sdn_log_slope_v092_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw21_spct_sqrt_slope_v093_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw21_sdn_smean_slope_v094_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw42_spct_sq_slope_v095_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw42_sdn_mul_slope_v096_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw63_spct_log_slope_v097_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw63_sdn_sqrt_slope_v098_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw126_spct_smean_slope_v099_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw126_sdn_sq_slope_v100_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw5_spct_mul_slope_v101_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw5_sdn_log_slope_v102_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw21_spct_sqrt_slope_v103_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw21_sdn_smean_slope_v104_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw42_spct_sq_slope_v105_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw42_sdn_mul_slope_v106_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw63_spct_log_slope_v107_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw63_sdn_sqrt_slope_v108_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw126_spct_smean_slope_v109_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw126_sdn_sq_slope_v110_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw5_spct_mul_slope_v111_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw5_sdn_log_slope_v112_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw21_spct_sqrt_slope_v113_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw21_sdn_smean_slope_v114_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw42_spct_sq_slope_v115_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw42_sdn_mul_slope_v116_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw63_spct_log_slope_v117_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw63_sdn_sqrt_slope_v118_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw126_spct_smean_slope_v119_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw126_sdn_sq_slope_v120_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw5_spct_mul_slope_v121_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw5_sdn_log_slope_v122_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw21_spct_sqrt_slope_v123_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw21_sdn_smean_slope_v124_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw42_spct_sq_slope_v125_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw42_sdn_mul_slope_v126_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw63_spct_log_slope_v127_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw63_sdn_sqrt_slope_v128_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw126_spct_smean_slope_v129_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw126_sdn_sq_slope_v130_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw5_spct_mul_slope_v131_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw5_sdn_log_slope_v132_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw21_spct_sqrt_slope_v133_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw21_sdn_smean_slope_v134_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw42_spct_sq_slope_v135_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw42_sdn_mul_slope_v136_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw63_spct_log_slope_v137_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw63_sdn_sqrt_slope_v138_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw126_spct_smean_slope_v139_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw126_sdn_sq_slope_v140_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw5_spct_mul_slope_v141_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw5_sdn_log_slope_v142_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw21_spct_sqrt_slope_v143_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw21_sdn_smean_slope_v144_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw42_spct_sq_slope_v145_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw42_sdn_mul_slope_v146_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw63_spct_log_slope_v147_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw63_sdn_sqrt_slope_v148_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw126_spct_smean_slope_v149_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw126_sdn_sq_slope_v150_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw5_spct_mul_slope_v001_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw5_sdn_log_slope_v002_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw21_spct_sqrt_slope_v003_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw21_sdn_smean_slope_v004_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw42_spct_sq_slope_v005_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw42_sdn_mul_slope_v006_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw63_spct_log_slope_v007_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw63_sdn_sqrt_slope_v008_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw126_spct_smean_slope_v009_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sw126_sdn_sq_slope_v010_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw5_spct_mul_slope_v011_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw5_sdn_log_slope_v012_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw21_spct_sqrt_slope_v013_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw21_sdn_smean_slope_v014_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw42_spct_sq_slope_v015_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw42_sdn_mul_slope_v016_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw63_spct_log_slope_v017_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw63_sdn_sqrt_slope_v018_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw126_spct_smean_slope_v019_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sw126_sdn_sq_slope_v020_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw5_spct_mul_slope_v021_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw5_sdn_log_slope_v022_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw21_spct_sqrt_slope_v023_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw21_sdn_smean_slope_v024_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw42_spct_sq_slope_v025_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw42_sdn_mul_slope_v026_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw63_spct_log_slope_v027_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw63_sdn_sqrt_slope_v028_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw126_spct_smean_slope_v029_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sw126_sdn_sq_slope_v030_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw5_spct_mul_slope_v031_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw5_sdn_log_slope_v032_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw21_spct_sqrt_slope_v033_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw21_sdn_smean_slope_v034_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw42_spct_sq_slope_v035_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw42_sdn_mul_slope_v036_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw63_spct_log_slope_v037_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw63_sdn_sqrt_slope_v038_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw126_spct_smean_slope_v039_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sw126_sdn_sq_slope_v040_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw5_spct_mul_slope_v041_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw5_sdn_log_slope_v042_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw21_spct_sqrt_slope_v043_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw21_sdn_smean_slope_v044_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw42_spct_sq_slope_v045_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw42_sdn_mul_slope_v046_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw63_spct_log_slope_v047_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw63_sdn_sqrt_slope_v048_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw126_spct_smean_slope_v049_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sw126_sdn_sq_slope_v050_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw5_spct_mul_slope_v051_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw5_sdn_log_slope_v052_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw21_spct_sqrt_slope_v053_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw21_sdn_smean_slope_v054_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw42_spct_sq_slope_v055_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw42_sdn_mul_slope_v056_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw63_spct_log_slope_v057_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw63_sdn_sqrt_slope_v058_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw126_spct_smean_slope_v059_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sw126_sdn_sq_slope_v060_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw5_spct_mul_slope_v061_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw5_sdn_log_slope_v062_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw21_spct_sqrt_slope_v063_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw21_sdn_smean_slope_v064_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw42_spct_sq_slope_v065_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw42_sdn_mul_slope_v066_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw63_spct_log_slope_v067_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw63_sdn_sqrt_slope_v068_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw126_spct_smean_slope_v069_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sw126_sdn_sq_slope_v070_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw5_spct_mul_slope_v071_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw5_sdn_log_slope_v072_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw21_spct_sqrt_slope_v073_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw21_sdn_smean_slope_v074_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw42_spct_sq_slope_v075_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw42_sdn_mul_slope_v076_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw63_spct_log_slope_v077_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw63_sdn_sqrt_slope_v078_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw126_spct_smean_slope_v079_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sw126_sdn_sq_slope_v080_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw5_spct_mul_slope_v081_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw5_sdn_log_slope_v082_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw21_spct_sqrt_slope_v083_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw21_sdn_smean_slope_v084_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw42_spct_sq_slope_v085_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw42_sdn_mul_slope_v086_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw63_spct_log_slope_v087_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw63_sdn_sqrt_slope_v088_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw126_spct_smean_slope_v089_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sw126_sdn_sq_slope_v090_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw5_spct_mul_slope_v091_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw5_sdn_log_slope_v092_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw21_spct_sqrt_slope_v093_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw21_sdn_smean_slope_v094_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw42_spct_sq_slope_v095_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw42_sdn_mul_slope_v096_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw63_spct_log_slope_v097_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw63_sdn_sqrt_slope_v098_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw126_spct_smean_slope_v099_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sw126_sdn_sq_slope_v100_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw5_spct_mul_slope_v101_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw5_sdn_log_slope_v102_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw21_spct_sqrt_slope_v103_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw21_sdn_smean_slope_v104_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw42_spct_sq_slope_v105_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw42_sdn_mul_slope_v106_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw63_spct_log_slope_v107_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw63_sdn_sqrt_slope_v108_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw126_spct_smean_slope_v109_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sw126_sdn_sq_slope_v110_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw5_spct_mul_slope_v111_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw5_sdn_log_slope_v112_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw21_spct_sqrt_slope_v113_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw21_sdn_smean_slope_v114_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw42_spct_sq_slope_v115_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw42_sdn_mul_slope_v116_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw63_spct_log_slope_v117_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw63_sdn_sqrt_slope_v118_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw126_spct_smean_slope_v119_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sw126_sdn_sq_slope_v120_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw5_spct_mul_slope_v121_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw5_sdn_log_slope_v122_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw21_spct_sqrt_slope_v123_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw21_sdn_smean_slope_v124_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw42_spct_sq_slope_v125_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw42_sdn_mul_slope_v126_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw63_spct_log_slope_v127_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw63_sdn_sqrt_slope_v128_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw126_spct_smean_slope_v129_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sw126_sdn_sq_slope_v130_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw5_spct_mul_slope_v131_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw5_sdn_log_slope_v132_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw21_spct_sqrt_slope_v133_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw21_sdn_smean_slope_v134_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw42_spct_sq_slope_v135_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw42_sdn_mul_slope_v136_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw63_spct_log_slope_v137_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw63_sdn_sqrt_slope_v138_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw126_spct_smean_slope_v139_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sw126_sdn_sq_slope_v140_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw5_spct_mul_slope_v141_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw5_sdn_log_slope_v142_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw21_spct_sqrt_slope_v143_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw21_sdn_smean_slope_v144_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw42_spct_sq_slope_v145_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw42_sdn_mul_slope_v146_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw63_spct_log_slope_v147_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw63_sdn_sqrt_slope_v148_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw126_spct_smean_slope_v149_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sw126_sdn_sq_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF22_LST_INSTRUMENT_PLACEMENT_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "ppnenet": ppnenet, "capex": capex, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_ppe_growth", "_f22_placement_pulse", "_f22_instrument_install_score",)
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
    print(f"OK lst_instrument_placement_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
