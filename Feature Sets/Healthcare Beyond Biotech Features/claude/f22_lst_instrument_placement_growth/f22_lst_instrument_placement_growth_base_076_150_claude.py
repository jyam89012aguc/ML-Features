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
def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_mean63_mul_base_v076_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_std63_log_base_v077_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_diff5_sqrt_base_v078_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sqr_smean_base_v079_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_mmr252_sq_base_v080_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_mean63_mul_base_v081_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_std63_log_base_v082_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_diff21_sqrt_base_v083_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sqr_smean_base_v084_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_mmr252_sq_base_v085_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_mean63_mul_base_v086_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_std63_log_base_v087_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_diff63_sqrt_base_v088_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sqr_smean_base_v089_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_mmr252_sq_base_v090_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_mean63_mul_base_v091_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_std63_log_base_v092_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_diff126_sqrt_base_v093_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sqr_smean_base_v094_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_mmr252_sq_base_v095_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_mean63_mul_base_v096_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_std63_log_base_v097_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_diff252_sqrt_base_v098_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sqr_smean_base_v099_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_mmr252_sq_base_v100_signal(ppnenet, closeadj):
    base = _f22_ppe_growth(ppnenet, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_mean63_mul_base_v101_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_std63_log_base_v102_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_diff5_sqrt_base_v103_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sqr_smean_base_v104_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw5_mmr252_sq_base_v105_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_mean63_mul_base_v106_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_std63_log_base_v107_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_diff21_sqrt_base_v108_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sqr_smean_base_v109_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw21_mmr252_sq_base_v110_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_mean63_mul_base_v111_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_std63_log_base_v112_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_diff63_sqrt_base_v113_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sqr_smean_base_v114_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw63_mmr252_sq_base_v115_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_mean63_mul_base_v116_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_std63_log_base_v117_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_diff126_sqrt_base_v118_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sqr_smean_base_v119_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw126_mmr252_sq_base_v120_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_mean63_mul_base_v121_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_std63_log_base_v122_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_diff252_sqrt_base_v123_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sqr_smean_base_v124_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_pulse_iw252_mmr252_sq_base_v125_signal(capex, ppnenet, closeadj):
    base = _f22_placement_pulse(capex, ppnenet, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_mean63_mul_base_v126_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_std63_log_base_v127_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_diff5_sqrt_base_v128_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_sqr_smean_base_v129_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw5_mmr252_sq_base_v130_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_mean63_mul_base_v131_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_std63_log_base_v132_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_diff21_sqrt_base_v133_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_sqr_smean_base_v134_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw21_mmr252_sq_base_v135_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_mean63_mul_base_v136_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_std63_log_base_v137_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_diff63_sqrt_base_v138_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_sqr_smean_base_v139_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw63_mmr252_sq_base_v140_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_mean63_mul_base_v141_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_std63_log_base_v142_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_diff126_sqrt_base_v143_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_sqr_smean_base_v144_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw126_mmr252_sq_base_v145_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_mean63_mul_base_v146_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_std63_log_base_v147_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_diff252_sqrt_base_v148_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_sqr_smean_base_v149_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f22lip_f22_lst_instrument_placement_growth_iis_iw252_mmr252_sq_base_v150_signal(capex, ppnenet, revenue, closeadj):
    base = _f22_instrument_install_score(capex, ppnenet, revenue, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_mean63_mul_base_v076_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_std63_log_base_v077_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_diff5_sqrt_base_v078_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_sqr_smean_base_v079_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw5_mmr252_sq_base_v080_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_mean63_mul_base_v081_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_std63_log_base_v082_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_diff21_sqrt_base_v083_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_sqr_smean_base_v084_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw21_mmr252_sq_base_v085_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_mean63_mul_base_v086_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_std63_log_base_v087_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_diff63_sqrt_base_v088_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_sqr_smean_base_v089_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw63_mmr252_sq_base_v090_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_mean63_mul_base_v091_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_std63_log_base_v092_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_diff126_sqrt_base_v093_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_sqr_smean_base_v094_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw126_mmr252_sq_base_v095_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_mean63_mul_base_v096_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_std63_log_base_v097_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_diff252_sqrt_base_v098_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_sqr_smean_base_v099_signal,
    f22lip_f22_lst_instrument_placement_growth_ppeg_iw252_mmr252_sq_base_v100_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_mean63_mul_base_v101_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_std63_log_base_v102_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_diff5_sqrt_base_v103_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_sqr_smean_base_v104_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw5_mmr252_sq_base_v105_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_mean63_mul_base_v106_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_std63_log_base_v107_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_diff21_sqrt_base_v108_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_sqr_smean_base_v109_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw21_mmr252_sq_base_v110_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_mean63_mul_base_v111_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_std63_log_base_v112_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_diff63_sqrt_base_v113_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_sqr_smean_base_v114_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw63_mmr252_sq_base_v115_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_mean63_mul_base_v116_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_std63_log_base_v117_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_diff126_sqrt_base_v118_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_sqr_smean_base_v119_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw126_mmr252_sq_base_v120_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_mean63_mul_base_v121_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_std63_log_base_v122_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_diff252_sqrt_base_v123_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_sqr_smean_base_v124_signal,
    f22lip_f22_lst_instrument_placement_growth_pulse_iw252_mmr252_sq_base_v125_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_mean63_mul_base_v126_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_std63_log_base_v127_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_diff5_sqrt_base_v128_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_sqr_smean_base_v129_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw5_mmr252_sq_base_v130_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_mean63_mul_base_v131_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_std63_log_base_v132_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_diff21_sqrt_base_v133_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_sqr_smean_base_v134_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw21_mmr252_sq_base_v135_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_mean63_mul_base_v136_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_std63_log_base_v137_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_diff63_sqrt_base_v138_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_sqr_smean_base_v139_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw63_mmr252_sq_base_v140_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_mean63_mul_base_v141_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_std63_log_base_v142_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_diff126_sqrt_base_v143_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_sqr_smean_base_v144_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw126_mmr252_sq_base_v145_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_mean63_mul_base_v146_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_std63_log_base_v147_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_diff252_sqrt_base_v148_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_sqr_smean_base_v149_signal,
    f22lip_f22_lst_instrument_placement_growth_iis_iw252_mmr252_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF22_LST_INSTRUMENT_PLACEMENT_GROWTH_REGISTRY_076_150 = REGISTRY


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
    print(f"OK lst_instrument_placement_growth_base_076_150_claude: {n_features} features pass")
