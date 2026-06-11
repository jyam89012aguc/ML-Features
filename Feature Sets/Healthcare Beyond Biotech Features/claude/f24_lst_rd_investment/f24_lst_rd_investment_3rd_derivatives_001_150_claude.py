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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


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
def f24lri_f24_lst_rd_investment_rdi_iw5_jw5_mul_jerk_v001_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw5_log_jerk_v002_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw21_mul_jerk_v003_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw21_log_jerk_v004_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw42_mul_jerk_v005_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw42_log_jerk_v006_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw63_mul_jerk_v007_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw63_log_jerk_v008_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw126_mul_jerk_v009_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw5_jw126_log_jerk_v010_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw5_sqrt_jerk_v011_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw5_raw_jerk_v012_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw21_sqrt_jerk_v013_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw21_raw_jerk_v014_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw42_sqrt_jerk_v015_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw42_raw_jerk_v016_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw63_sqrt_jerk_v017_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw63_raw_jerk_v018_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw126_sqrt_jerk_v019_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw21_jw126_raw_jerk_v020_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw5_sq_jerk_v021_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw5_smean_jerk_v022_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw21_sq_jerk_v023_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw21_smean_jerk_v024_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw42_sq_jerk_v025_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw42_smean_jerk_v026_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw63_sq_jerk_v027_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw63_smean_jerk_v028_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw126_sq_jerk_v029_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw63_jw126_smean_jerk_v030_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw5_ema_jerk_v031_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw5_ctr_jerk_v032_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw21_ema_jerk_v033_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw21_ctr_jerk_v034_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw42_ema_jerk_v035_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw42_ctr_jerk_v036_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw63_ema_jerk_v037_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw63_ctr_jerk_v038_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw126_ema_jerk_v039_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw126_jw126_ctr_jerk_v040_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw5_zsc_jerk_v041_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw5_zs63_jerk_v042_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw21_zsc_jerk_v043_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw21_zs63_jerk_v044_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw42_zsc_jerk_v045_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw42_zs63_jerk_v046_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw63_zsc_jerk_v047_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw63_zs63_jerk_v048_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw126_zsc_jerk_v049_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdi_iw252_jw126_zs63_jerk_v050_signal(rnd, revenue, closeadj):
    base = _f24_rd_intensity(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw5_mul_jerk_v051_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw5_log_jerk_v052_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw21_mul_jerk_v053_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw21_log_jerk_v054_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw42_mul_jerk_v055_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw42_log_jerk_v056_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw63_mul_jerk_v057_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw63_log_jerk_v058_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw126_mul_jerk_v059_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw5_jw126_log_jerk_v060_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 5)
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw5_sqrt_jerk_v061_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw5_raw_jerk_v062_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw21_sqrt_jerk_v063_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw21_raw_jerk_v064_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw42_sqrt_jerk_v065_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw42_raw_jerk_v066_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw63_sqrt_jerk_v067_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw63_raw_jerk_v068_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw126_sqrt_jerk_v069_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw21_jw126_raw_jerk_v070_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw5_sq_jerk_v071_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw5_smean_jerk_v072_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw21_sq_jerk_v073_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw21_smean_jerk_v074_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw42_sq_jerk_v075_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw42_smean_jerk_v076_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw63_sq_jerk_v077_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw63_smean_jerk_v078_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw126_sq_jerk_v079_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw63_jw126_smean_jerk_v080_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 63)
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw5_ema_jerk_v081_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw5_ctr_jerk_v082_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw21_ema_jerk_v083_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw21_ctr_jerk_v084_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw42_ema_jerk_v085_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw42_ctr_jerk_v086_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw63_ema_jerk_v087_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw63_ctr_jerk_v088_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw126_ema_jerk_v089_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw126_jw126_ctr_jerk_v090_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 126)
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw5_zsc_jerk_v091_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw5_zs63_jerk_v092_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw21_zsc_jerk_v093_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw21_zs63_jerk_v094_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw42_zsc_jerk_v095_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw42_zs63_jerk_v096_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw63_zsc_jerk_v097_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw63_zs63_jerk_v098_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw126_zsc_jerk_v099_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdc_iw252_jw126_zs63_jerk_v100_signal(rnd, closeadj):
    base = _f24_rd_compound(rnd, 252)
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw5_mul_jerk_v101_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw5_log_jerk_v102_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw21_mul_jerk_v103_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw21_log_jerk_v104_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw42_mul_jerk_v105_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw42_log_jerk_v106_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw63_mul_jerk_v107_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw63_log_jerk_v108_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw126_mul_jerk_v109_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw5_jw126_log_jerk_v110_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 5)
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw5_sqrt_jerk_v111_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw5_raw_jerk_v112_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw21_sqrt_jerk_v113_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw21_raw_jerk_v114_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw42_sqrt_jerk_v115_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw42_raw_jerk_v116_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw63_sqrt_jerk_v117_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw63_raw_jerk_v118_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw126_sqrt_jerk_v119_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw21_jw126_raw_jerk_v120_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw5_sq_jerk_v121_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw5_smean_jerk_v122_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw21_sq_jerk_v123_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw21_smean_jerk_v124_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw42_sq_jerk_v125_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw42_smean_jerk_v126_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw63_sq_jerk_v127_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw63_smean_jerk_v128_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw126_sq_jerk_v129_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw63_jw126_smean_jerk_v130_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 63)
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw5_ema_jerk_v131_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw5_ctr_jerk_v132_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw21_ema_jerk_v133_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw21_ctr_jerk_v134_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw42_ema_jerk_v135_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw42_ctr_jerk_v136_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw63_ema_jerk_v137_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw63_ctr_jerk_v138_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw126_ema_jerk_v139_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw126_jw126_ctr_jerk_v140_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 126)
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw5_zsc_jerk_v141_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw5_zs63_jerk_v142_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw21_zsc_jerk_v143_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw21_zs63_jerk_v144_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw42_zsc_jerk_v145_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw42_zs63_jerk_v146_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw63_zsc_jerk_v147_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw63_zs63_jerk_v148_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw126_zsc_jerk_v149_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f24lri_f24_lst_rd_investment_rdq_iw252_jw126_zs63_jerk_v150_signal(rnd, revenue, closeadj):
    base = _f24_rd_quality(rnd, revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24lri_f24_lst_rd_investment_rdi_iw5_jw5_mul_jerk_v001_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw5_log_jerk_v002_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw21_mul_jerk_v003_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw21_log_jerk_v004_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw42_mul_jerk_v005_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw42_log_jerk_v006_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw63_mul_jerk_v007_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw63_log_jerk_v008_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw126_mul_jerk_v009_signal,
    f24lri_f24_lst_rd_investment_rdi_iw5_jw126_log_jerk_v010_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw5_sqrt_jerk_v011_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw5_raw_jerk_v012_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw21_sqrt_jerk_v013_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw21_raw_jerk_v014_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw42_sqrt_jerk_v015_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw42_raw_jerk_v016_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw63_sqrt_jerk_v017_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw63_raw_jerk_v018_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw126_sqrt_jerk_v019_signal,
    f24lri_f24_lst_rd_investment_rdi_iw21_jw126_raw_jerk_v020_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw5_sq_jerk_v021_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw5_smean_jerk_v022_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw21_sq_jerk_v023_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw21_smean_jerk_v024_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw42_sq_jerk_v025_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw42_smean_jerk_v026_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw63_sq_jerk_v027_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw63_smean_jerk_v028_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw126_sq_jerk_v029_signal,
    f24lri_f24_lst_rd_investment_rdi_iw63_jw126_smean_jerk_v030_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw5_ema_jerk_v031_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw5_ctr_jerk_v032_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw21_ema_jerk_v033_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw21_ctr_jerk_v034_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw42_ema_jerk_v035_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw42_ctr_jerk_v036_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw63_ema_jerk_v037_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw63_ctr_jerk_v038_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw126_ema_jerk_v039_signal,
    f24lri_f24_lst_rd_investment_rdi_iw126_jw126_ctr_jerk_v040_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw5_zsc_jerk_v041_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw5_zs63_jerk_v042_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw21_zsc_jerk_v043_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw21_zs63_jerk_v044_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw42_zsc_jerk_v045_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw42_zs63_jerk_v046_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw63_zsc_jerk_v047_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw63_zs63_jerk_v048_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw126_zsc_jerk_v049_signal,
    f24lri_f24_lst_rd_investment_rdi_iw252_jw126_zs63_jerk_v050_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw5_mul_jerk_v051_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw5_log_jerk_v052_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw21_mul_jerk_v053_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw21_log_jerk_v054_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw42_mul_jerk_v055_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw42_log_jerk_v056_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw63_mul_jerk_v057_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw63_log_jerk_v058_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw126_mul_jerk_v059_signal,
    f24lri_f24_lst_rd_investment_rdc_iw5_jw126_log_jerk_v060_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw5_sqrt_jerk_v061_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw5_raw_jerk_v062_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw21_sqrt_jerk_v063_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw21_raw_jerk_v064_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw42_sqrt_jerk_v065_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw42_raw_jerk_v066_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw63_sqrt_jerk_v067_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw63_raw_jerk_v068_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw126_sqrt_jerk_v069_signal,
    f24lri_f24_lst_rd_investment_rdc_iw21_jw126_raw_jerk_v070_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw5_sq_jerk_v071_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw5_smean_jerk_v072_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw21_sq_jerk_v073_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw21_smean_jerk_v074_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw42_sq_jerk_v075_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw42_smean_jerk_v076_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw63_sq_jerk_v077_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw63_smean_jerk_v078_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw126_sq_jerk_v079_signal,
    f24lri_f24_lst_rd_investment_rdc_iw63_jw126_smean_jerk_v080_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw5_ema_jerk_v081_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw5_ctr_jerk_v082_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw21_ema_jerk_v083_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw21_ctr_jerk_v084_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw42_ema_jerk_v085_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw42_ctr_jerk_v086_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw63_ema_jerk_v087_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw63_ctr_jerk_v088_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw126_ema_jerk_v089_signal,
    f24lri_f24_lst_rd_investment_rdc_iw126_jw126_ctr_jerk_v090_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw5_zsc_jerk_v091_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw5_zs63_jerk_v092_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw21_zsc_jerk_v093_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw21_zs63_jerk_v094_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw42_zsc_jerk_v095_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw42_zs63_jerk_v096_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw63_zsc_jerk_v097_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw63_zs63_jerk_v098_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw126_zsc_jerk_v099_signal,
    f24lri_f24_lst_rd_investment_rdc_iw252_jw126_zs63_jerk_v100_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw5_mul_jerk_v101_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw5_log_jerk_v102_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw21_mul_jerk_v103_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw21_log_jerk_v104_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw42_mul_jerk_v105_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw42_log_jerk_v106_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw63_mul_jerk_v107_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw63_log_jerk_v108_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw126_mul_jerk_v109_signal,
    f24lri_f24_lst_rd_investment_rdq_iw5_jw126_log_jerk_v110_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw5_sqrt_jerk_v111_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw5_raw_jerk_v112_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw21_sqrt_jerk_v113_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw21_raw_jerk_v114_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw42_sqrt_jerk_v115_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw42_raw_jerk_v116_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw63_sqrt_jerk_v117_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw63_raw_jerk_v118_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw126_sqrt_jerk_v119_signal,
    f24lri_f24_lst_rd_investment_rdq_iw21_jw126_raw_jerk_v120_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw5_sq_jerk_v121_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw5_smean_jerk_v122_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw21_sq_jerk_v123_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw21_smean_jerk_v124_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw42_sq_jerk_v125_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw42_smean_jerk_v126_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw63_sq_jerk_v127_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw63_smean_jerk_v128_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw126_sq_jerk_v129_signal,
    f24lri_f24_lst_rd_investment_rdq_iw63_jw126_smean_jerk_v130_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw5_ema_jerk_v131_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw5_ctr_jerk_v132_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw21_ema_jerk_v133_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw21_ctr_jerk_v134_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw42_ema_jerk_v135_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw42_ctr_jerk_v136_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw63_ema_jerk_v137_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw63_ctr_jerk_v138_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw126_ema_jerk_v139_signal,
    f24lri_f24_lst_rd_investment_rdq_iw126_jw126_ctr_jerk_v140_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw5_zsc_jerk_v141_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw5_zs63_jerk_v142_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw21_zsc_jerk_v143_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw21_zs63_jerk_v144_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw42_zsc_jerk_v145_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw42_zs63_jerk_v146_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw63_zsc_jerk_v147_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw63_zs63_jerk_v148_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw126_zsc_jerk_v149_signal,
    f24lri_f24_lst_rd_investment_rdq_iw252_jw126_zs63_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF24_LST_RD_INVESTMENT_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK lst_rd_investment_3rd_derivatives_001_150_claude: {n_features} features pass")
