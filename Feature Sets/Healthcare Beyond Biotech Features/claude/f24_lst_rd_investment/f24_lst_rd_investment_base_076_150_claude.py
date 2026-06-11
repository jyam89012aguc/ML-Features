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
def _f24_rd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)

def _f24_rd_compound(rnd, w):
    return rnd.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()

def _f24_rd_quality(rnd, revenue, w):
    rd_g = rnd.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return rd_g - rev_g


# ===== features =====
def f24lri_f24_lst_rd_investment_rdi_iw5_mean63_mul_base_v076_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_std63_log_base_v077_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_diff5_sqrt_base_v078_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_sqr_smean_base_v079_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_mmr252_sq_base_v080_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_mean63_mul_base_v081_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_std63_log_base_v082_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_diff21_sqrt_base_v083_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_sqr_smean_base_v084_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_mmr252_sq_base_v085_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_mean63_mul_base_v086_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_std63_log_base_v087_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_diff63_sqrt_base_v088_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_sqr_smean_base_v089_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_mmr252_sq_base_v090_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_mean63_mul_base_v091_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_std63_log_base_v092_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_diff126_sqrt_base_v093_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_sqr_smean_base_v094_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_mmr252_sq_base_v095_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_mean63_mul_base_v096_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_std63_log_base_v097_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_diff252_sqrt_base_v098_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_sqr_smean_base_v099_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_mmr252_sq_base_v100_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_mean63_mul_base_v101_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_std63_log_base_v102_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_diff5_sqrt_base_v103_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_sqr_smean_base_v104_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_mmr252_sq_base_v105_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_mean63_mul_base_v106_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_std63_log_base_v107_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_diff21_sqrt_base_v108_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_sqr_smean_base_v109_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_mmr252_sq_base_v110_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_mean63_mul_base_v111_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_std63_log_base_v112_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_diff63_sqrt_base_v113_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_sqr_smean_base_v114_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_mmr252_sq_base_v115_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_mean63_mul_base_v116_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_std63_log_base_v117_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_diff126_sqrt_base_v118_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_sqr_smean_base_v119_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_mmr252_sq_base_v120_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_mean63_mul_base_v121_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_std63_log_base_v122_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_diff252_sqrt_base_v123_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_sqr_smean_base_v124_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_mmr252_sq_base_v125_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_mean63_mul_base_v126_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_std63_log_base_v127_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_diff5_sqrt_base_v128_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_sqr_smean_base_v129_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_mmr252_sq_base_v130_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_mean63_mul_base_v131_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_std63_log_base_v132_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_diff21_sqrt_base_v133_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_sqr_smean_base_v134_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_mmr252_sq_base_v135_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_mean63_mul_base_v136_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_std63_log_base_v137_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_diff63_sqrt_base_v138_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_sqr_smean_base_v139_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_mmr252_sq_base_v140_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_mean63_mul_base_v141_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_std63_log_base_v142_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_diff126_sqrt_base_v143_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_sqr_smean_base_v144_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_mmr252_sq_base_v145_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_mean63_mul_base_v146_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_std63_log_base_v147_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_diff252_sqrt_base_v148_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_sqr_smean_base_v149_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_mmr252_sq_base_v150_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24lri_f24_lst_rd_investment_rdi_iw5_mean63_mul_base_v076_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_std63_log_base_v077_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_diff5_sqrt_base_v078_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_sqr_smean_base_v079_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_mmr252_sq_base_v080_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_mean63_mul_base_v081_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_std63_log_base_v082_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_diff21_sqrt_base_v083_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_sqr_smean_base_v084_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_mmr252_sq_base_v085_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_mean63_mul_base_v086_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_std63_log_base_v087_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_diff63_sqrt_base_v088_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_sqr_smean_base_v089_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_mmr252_sq_base_v090_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_mean63_mul_base_v091_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_std63_log_base_v092_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_diff126_sqrt_base_v093_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_sqr_smean_base_v094_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_mmr252_sq_base_v095_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_mean63_mul_base_v096_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_std63_log_base_v097_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_diff252_sqrt_base_v098_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_sqr_smean_base_v099_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_mmr252_sq_base_v100_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_mean63_mul_base_v101_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_std63_log_base_v102_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_diff5_sqrt_base_v103_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_sqr_smean_base_v104_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_mmr252_sq_base_v105_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_mean63_mul_base_v106_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_std63_log_base_v107_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_diff21_sqrt_base_v108_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_sqr_smean_base_v109_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_mmr252_sq_base_v110_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_mean63_mul_base_v111_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_std63_log_base_v112_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_diff63_sqrt_base_v113_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_sqr_smean_base_v114_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_mmr252_sq_base_v115_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_mean63_mul_base_v116_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_std63_log_base_v117_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_diff126_sqrt_base_v118_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_sqr_smean_base_v119_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_mmr252_sq_base_v120_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_mean63_mul_base_v121_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_std63_log_base_v122_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_diff252_sqrt_base_v123_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_sqr_smean_base_v124_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_mmr252_sq_base_v125_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_mean63_mul_base_v126_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_std63_log_base_v127_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_diff5_sqrt_base_v128_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_sqr_smean_base_v129_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_mmr252_sq_base_v130_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_mean63_mul_base_v131_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_std63_log_base_v132_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_diff21_sqrt_base_v133_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_sqr_smean_base_v134_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_mmr252_sq_base_v135_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_mean63_mul_base_v136_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_std63_log_base_v137_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_diff63_sqrt_base_v138_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_sqr_smean_base_v139_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_mmr252_sq_base_v140_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_mean63_mul_base_v141_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_std63_log_base_v142_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_diff126_sqrt_base_v143_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_sqr_smean_base_v144_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_mmr252_sq_base_v145_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_mean63_mul_base_v146_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_std63_log_base_v147_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_diff252_sqrt_base_v148_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_sqr_smean_base_v149_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_mmr252_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF24_LST_RD_INVESTMENT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "rnd": rnd, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_rd_intensity", "_f24_rd_compound", "_f24_rd_quality",)
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
    print(f"OK lst_rd_investment_base_076_150_claude: {n_features} features pass")
