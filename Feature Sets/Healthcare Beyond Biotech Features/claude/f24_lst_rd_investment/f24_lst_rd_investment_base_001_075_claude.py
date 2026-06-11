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
def f24lri_f24_lst_rd_investment_rdi_iw5_pct5_mul_base_v001_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_z5sc63_log_base_v002_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_ratiomean5_sqrt_base_v003_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_log_smean_base_v004_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_ema63_sq_base_v005_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_pct21_mul_base_v006_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_z21sc63_log_base_v007_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_ratiomean21_sqrt_base_v008_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_log_smean_base_v009_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_ema63_sq_base_v010_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_pct63_mul_base_v011_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_z63sc63_log_base_v012_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_ratiomean63_sqrt_base_v013_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_log_smean_base_v014_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_ema63_sq_base_v015_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_pct126_mul_base_v016_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_z126sc63_log_base_v017_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_ratiomean126_sqrt_base_v018_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_log_smean_base_v019_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_ema63_sq_base_v020_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_pct252_mul_base_v021_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_z252sc63_log_base_v022_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_ratiomean252_sqrt_base_v023_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_log_smean_base_v024_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_ema63_sq_base_v025_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_pct5_mul_base_v026_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_z5sc63_log_base_v027_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_ratiomean5_sqrt_base_v028_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_log_smean_base_v029_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_ema63_sq_base_v030_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_pct21_mul_base_v031_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_z21sc63_log_base_v032_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_ratiomean21_sqrt_base_v033_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_log_smean_base_v034_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_ema63_sq_base_v035_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_pct63_mul_base_v036_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_z63sc63_log_base_v037_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_ratiomean63_sqrt_base_v038_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_log_smean_base_v039_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_ema63_sq_base_v040_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_pct126_mul_base_v041_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_z126sc63_log_base_v042_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_ratiomean126_sqrt_base_v043_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_log_smean_base_v044_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_ema63_sq_base_v045_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_pct252_mul_base_v046_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_z252sc63_log_base_v047_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_ratiomean252_sqrt_base_v048_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_log_smean_base_v049_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_ema63_sq_base_v050_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_pct5_mul_base_v051_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_z5sc63_log_base_v052_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_ratiomean5_sqrt_base_v053_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_log_smean_base_v054_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_ema63_sq_base_v055_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_pct21_mul_base_v056_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_z21sc63_log_base_v057_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_ratiomean21_sqrt_base_v058_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_log_smean_base_v059_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_ema63_sq_base_v060_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_pct63_mul_base_v061_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_z63sc63_log_base_v062_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_ratiomean63_sqrt_base_v063_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_log_smean_base_v064_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_ema63_sq_base_v065_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_pct126_mul_base_v066_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_z126sc63_log_base_v067_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_ratiomean126_sqrt_base_v068_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_log_smean_base_v069_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_ema63_sq_base_v070_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_pct252_mul_base_v071_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_z252sc63_log_base_v072_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_ratiomean252_sqrt_base_v073_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_log_smean_base_v074_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_ema63_sq_base_v075_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24lri_f24_lst_rd_investment_rdi_iw5_pct5_mul_base_v001_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_z5sc63_log_base_v002_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_ratiomean5_sqrt_base_v003_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_log_smean_base_v004_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_ema63_sq_base_v005_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_pct21_mul_base_v006_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_z21sc63_log_base_v007_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_ratiomean21_sqrt_base_v008_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_log_smean_base_v009_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_ema63_sq_base_v010_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_pct63_mul_base_v011_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_z63sc63_log_base_v012_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_ratiomean63_sqrt_base_v013_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_log_smean_base_v014_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_ema63_sq_base_v015_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_pct126_mul_base_v016_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_z126sc63_log_base_v017_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_ratiomean126_sqrt_base_v018_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_log_smean_base_v019_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_ema63_sq_base_v020_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_pct252_mul_base_v021_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_z252sc63_log_base_v022_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_ratiomean252_sqrt_base_v023_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_log_smean_base_v024_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_ema63_sq_base_v025_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_pct5_mul_base_v026_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_z5sc63_log_base_v027_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_ratiomean5_sqrt_base_v028_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_log_smean_base_v029_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_ema63_sq_base_v030_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_pct21_mul_base_v031_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_z21sc63_log_base_v032_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_ratiomean21_sqrt_base_v033_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_log_smean_base_v034_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_ema63_sq_base_v035_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_pct63_mul_base_v036_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_z63sc63_log_base_v037_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_ratiomean63_sqrt_base_v038_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_log_smean_base_v039_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_ema63_sq_base_v040_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_pct126_mul_base_v041_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_z126sc63_log_base_v042_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_ratiomean126_sqrt_base_v043_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_log_smean_base_v044_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_ema63_sq_base_v045_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_pct252_mul_base_v046_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_z252sc63_log_base_v047_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_ratiomean252_sqrt_base_v048_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_log_smean_base_v049_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_ema63_sq_base_v050_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_pct5_mul_base_v051_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_z5sc63_log_base_v052_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_ratiomean5_sqrt_base_v053_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_log_smean_base_v054_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_ema63_sq_base_v055_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_pct21_mul_base_v056_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_z21sc63_log_base_v057_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_ratiomean21_sqrt_base_v058_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_log_smean_base_v059_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_ema63_sq_base_v060_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_pct63_mul_base_v061_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_z63sc63_log_base_v062_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_ratiomean63_sqrt_base_v063_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_log_smean_base_v064_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_ema63_sq_base_v065_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_pct126_mul_base_v066_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_z126sc63_log_base_v067_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_ratiomean126_sqrt_base_v068_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_log_smean_base_v069_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_ema63_sq_base_v070_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_pct252_mul_base_v071_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_z252sc63_log_base_v072_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_ratiomean252_sqrt_base_v073_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_log_smean_base_v074_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_ema63_sq_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF24_LST_RD_INVESTMENT_REGISTRY_001_075 = REGISTRY


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
    print(f"OK lst_rd_investment_base_001_075_claude: {n_features} features pass")
