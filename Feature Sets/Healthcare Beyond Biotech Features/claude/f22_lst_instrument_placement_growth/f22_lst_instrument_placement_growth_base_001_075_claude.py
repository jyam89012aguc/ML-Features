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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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
def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_pct5_mul_base_v001_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_z5sc63_log_base_v002_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_ratiomean5_sqrt_base_v003_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_log_smean_base_v004_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_ema63_sq_base_v005_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_pct21_mul_base_v006_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_z21sc63_log_base_v007_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_ratiomean21_sqrt_base_v008_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_log_smean_base_v009_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_ema63_sq_base_v010_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_pct63_mul_base_v011_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_z63sc63_log_base_v012_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_ratiomean63_sqrt_base_v013_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_log_smean_base_v014_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_ema63_sq_base_v015_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_pct126_mul_base_v016_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_z126sc63_log_base_v017_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_ratiomean126_sqrt_base_v018_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_log_smean_base_v019_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_ema63_sq_base_v020_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_pct252_mul_base_v021_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_z252sc63_log_base_v022_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_ratiomean252_sqrt_base_v023_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_log_smean_base_v024_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_ema63_sq_base_v025_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_pct5_mul_base_v026_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_z5sc63_log_base_v027_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_ratiomean5_sqrt_base_v028_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_log_smean_base_v029_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_ema63_sq_base_v030_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_pct21_mul_base_v031_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_z21sc63_log_base_v032_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_ratiomean21_sqrt_base_v033_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_log_smean_base_v034_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_ema63_sq_base_v035_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_pct63_mul_base_v036_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_z63sc63_log_base_v037_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_ratiomean63_sqrt_base_v038_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_log_smean_base_v039_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_ema63_sq_base_v040_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_pct126_mul_base_v041_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_z126sc63_log_base_v042_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_ratiomean126_sqrt_base_v043_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_log_smean_base_v044_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_ema63_sq_base_v045_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_pct252_mul_base_v046_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_z252sc63_log_base_v047_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_ratiomean252_sqrt_base_v048_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_log_smean_base_v049_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_ema63_sq_base_v050_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_pct5_mul_base_v051_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_z5sc63_log_base_v052_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_ratiomean5_sqrt_base_v053_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_log_smean_base_v054_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_ema63_sq_base_v055_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_pct21_mul_base_v056_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_z21sc63_log_base_v057_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_ratiomean21_sqrt_base_v058_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_log_smean_base_v059_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_ema63_sq_base_v060_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_pct63_mul_base_v061_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_z63sc63_log_base_v062_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_ratiomean63_sqrt_base_v063_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_log_smean_base_v064_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_ema63_sq_base_v065_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_pct126_mul_base_v066_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_z126sc63_log_base_v067_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_ratiomean126_sqrt_base_v068_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_log_smean_base_v069_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_ema63_sq_base_v070_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_pct252_mul_base_v071_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_z252sc63_log_base_v072_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_ratiomean252_sqrt_base_v073_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_log_smean_base_v074_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_ema63_sq_base_v075_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_pct5_mul_base_v001_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_z5sc63_log_base_v002_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_ratiomean5_sqrt_base_v003_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_log_smean_base_v004_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_ema63_sq_base_v005_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_pct21_mul_base_v006_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_z21sc63_log_base_v007_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_ratiomean21_sqrt_base_v008_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_log_smean_base_v009_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_ema63_sq_base_v010_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_pct63_mul_base_v011_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_z63sc63_log_base_v012_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_ratiomean63_sqrt_base_v013_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_log_smean_base_v014_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_ema63_sq_base_v015_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_pct126_mul_base_v016_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_z126sc63_log_base_v017_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_ratiomean126_sqrt_base_v018_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_log_smean_base_v019_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_ema63_sq_base_v020_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_pct252_mul_base_v021_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_z252sc63_log_base_v022_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_ratiomean252_sqrt_base_v023_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_log_smean_base_v024_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_ema63_sq_base_v025_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_pct5_mul_base_v026_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_z5sc63_log_base_v027_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_ratiomean5_sqrt_base_v028_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_log_smean_base_v029_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_ema63_sq_base_v030_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_pct21_mul_base_v031_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_z21sc63_log_base_v032_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_ratiomean21_sqrt_base_v033_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_log_smean_base_v034_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_ema63_sq_base_v035_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_pct63_mul_base_v036_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_z63sc63_log_base_v037_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_ratiomean63_sqrt_base_v038_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_log_smean_base_v039_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_ema63_sq_base_v040_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_pct126_mul_base_v041_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_z126sc63_log_base_v042_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_ratiomean126_sqrt_base_v043_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_log_smean_base_v044_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_ema63_sq_base_v045_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_pct252_mul_base_v046_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_z252sc63_log_base_v047_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_ratiomean252_sqrt_base_v048_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_log_smean_base_v049_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_ema63_sq_base_v050_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_pct5_mul_base_v051_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_z5sc63_log_base_v052_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_ratiomean5_sqrt_base_v053_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_log_smean_base_v054_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_ema63_sq_base_v055_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_pct21_mul_base_v056_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_z21sc63_log_base_v057_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_ratiomean21_sqrt_base_v058_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_log_smean_base_v059_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_ema63_sq_base_v060_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_pct63_mul_base_v061_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_z63sc63_log_base_v062_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_ratiomean63_sqrt_base_v063_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_log_smean_base_v064_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_ema63_sq_base_v065_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_pct126_mul_base_v066_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_z126sc63_log_base_v067_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_ratiomean126_sqrt_base_v068_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_log_smean_base_v069_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_ema63_sq_base_v070_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_pct252_mul_base_v071_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_z252sc63_log_base_v072_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_ratiomean252_sqrt_base_v073_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_log_smean_base_v074_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_ema63_sq_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF22_LST_INSTRUMENT_PLACEMENT_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK lst_instrument_placement_growth_base_001_075_claude: {n_features} features pass")
