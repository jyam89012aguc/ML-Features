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
def _f25_revenue_compound(revenue, w):
    return revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()

def _f25_share_growth(revenue, w):
    g = revenue.pct_change(periods=w)
    base_g = g.rolling(w * 2, min_periods=max(1, w // 2)).mean()
    return g - base_g

def _f25_market_share_score(revenue, ebitda, w):
    r_g = revenue.pct_change(periods=w)
    e_g = ebitda.pct_change(periods=w)
    return r_g * np.sign(e_g) + r_g.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====
def f25lms_f25_lst_market_share_growth_rc_iw5_jw5_mul_jerk_v001_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw5_log_jerk_v002_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw21_mul_jerk_v003_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw21_log_jerk_v004_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw42_mul_jerk_v005_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw42_log_jerk_v006_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw63_mul_jerk_v007_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw63_log_jerk_v008_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw126_mul_jerk_v009_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_jw126_log_jerk_v010_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw5_sqrt_jerk_v011_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw5_raw_jerk_v012_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw21_sqrt_jerk_v013_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw21_raw_jerk_v014_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw42_sqrt_jerk_v015_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw42_raw_jerk_v016_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw63_sqrt_jerk_v017_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw63_raw_jerk_v018_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw126_sqrt_jerk_v019_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_jw126_raw_jerk_v020_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw5_sq_jerk_v021_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw5_smean_jerk_v022_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw21_sq_jerk_v023_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw21_smean_jerk_v024_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw42_sq_jerk_v025_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw42_smean_jerk_v026_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw63_sq_jerk_v027_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw63_smean_jerk_v028_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw126_sq_jerk_v029_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_jw126_smean_jerk_v030_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw5_ema_jerk_v031_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw5_ctr_jerk_v032_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw21_ema_jerk_v033_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw21_ctr_jerk_v034_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw42_ema_jerk_v035_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw42_ctr_jerk_v036_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw63_ema_jerk_v037_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw63_ctr_jerk_v038_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw126_ema_jerk_v039_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_jw126_ctr_jerk_v040_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw5_zsc_jerk_v041_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw5_zs63_jerk_v042_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw21_zsc_jerk_v043_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw21_zs63_jerk_v044_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw42_zsc_jerk_v045_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw42_zs63_jerk_v046_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw63_zsc_jerk_v047_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw63_zs63_jerk_v048_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw126_zsc_jerk_v049_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_jw126_zs63_jerk_v050_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw5_mul_jerk_v051_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw5_log_jerk_v052_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw21_mul_jerk_v053_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw21_log_jerk_v054_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw42_mul_jerk_v055_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw42_log_jerk_v056_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw63_mul_jerk_v057_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw63_log_jerk_v058_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw126_mul_jerk_v059_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_jw126_log_jerk_v060_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw5_sqrt_jerk_v061_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw5_raw_jerk_v062_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw21_sqrt_jerk_v063_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw21_raw_jerk_v064_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw42_sqrt_jerk_v065_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw42_raw_jerk_v066_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw63_sqrt_jerk_v067_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw63_raw_jerk_v068_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw126_sqrt_jerk_v069_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_jw126_raw_jerk_v070_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw5_sq_jerk_v071_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw5_smean_jerk_v072_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw21_sq_jerk_v073_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw21_smean_jerk_v074_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw42_sq_jerk_v075_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw42_smean_jerk_v076_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw63_sq_jerk_v077_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw63_smean_jerk_v078_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw126_sq_jerk_v079_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_jw126_smean_jerk_v080_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw5_ema_jerk_v081_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw5_ctr_jerk_v082_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw21_ema_jerk_v083_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw21_ctr_jerk_v084_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw42_ema_jerk_v085_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw42_ctr_jerk_v086_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw63_ema_jerk_v087_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw63_ctr_jerk_v088_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw126_ema_jerk_v089_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_jw126_ctr_jerk_v090_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw5_zsc_jerk_v091_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw5_zs63_jerk_v092_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw21_zsc_jerk_v093_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw21_zs63_jerk_v094_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw42_zsc_jerk_v095_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw42_zs63_jerk_v096_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw63_zsc_jerk_v097_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw63_zs63_jerk_v098_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw126_zsc_jerk_v099_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_jw126_zs63_jerk_v100_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw5_mul_jerk_v101_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw5_log_jerk_v102_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw21_mul_jerk_v103_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw21_log_jerk_v104_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 21) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw42_mul_jerk_v105_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw42_log_jerk_v106_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 42) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw63_mul_jerk_v107_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw63_log_jerk_v108_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw126_mul_jerk_v109_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_jw126_log_jerk_v110_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _jerk(base, 126) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw5_sqrt_jerk_v111_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw5_raw_jerk_v112_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw21_sqrt_jerk_v113_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw21_raw_jerk_v114_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw42_sqrt_jerk_v115_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 42) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw42_raw_jerk_v116_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw63_sqrt_jerk_v117_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw63_raw_jerk_v118_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw126_sqrt_jerk_v119_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_jw126_raw_jerk_v120_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw5_sq_jerk_v121_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw5_smean_jerk_v122_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw21_sq_jerk_v123_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw21_smean_jerk_v124_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw42_sq_jerk_v125_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw42_smean_jerk_v126_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw63_sq_jerk_v127_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw63_smean_jerk_v128_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw126_sq_jerk_v129_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_jw126_smean_jerk_v130_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _jerk(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw5_ema_jerk_v131_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 5) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw5_ctr_jerk_v132_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 5) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw21_ema_jerk_v133_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw21_ctr_jerk_v134_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 21) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw42_ema_jerk_v135_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 42) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw42_ctr_jerk_v136_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 42) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw63_ema_jerk_v137_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw63_ctr_jerk_v138_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 63) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw126_ema_jerk_v139_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 126) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_jw126_ctr_jerk_v140_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _jerk(base, 126) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw5_zsc_jerk_v141_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 5) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw5_zs63_jerk_v142_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw21_zsc_jerk_v143_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 21) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw21_zs63_jerk_v144_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw42_zsc_jerk_v145_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 42) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw42_zs63_jerk_v146_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw63_zsc_jerk_v147_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 63) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw63_zs63_jerk_v148_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw126_zsc_jerk_v149_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 126) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_jw126_zs63_jerk_v150_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _jerk(base, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25lms_f25_lst_market_share_growth_rc_iw5_jw5_mul_jerk_v001_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw5_log_jerk_v002_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw21_mul_jerk_v003_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw21_log_jerk_v004_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw42_mul_jerk_v005_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw42_log_jerk_v006_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw63_mul_jerk_v007_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw63_log_jerk_v008_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw126_mul_jerk_v009_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_jw126_log_jerk_v010_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw5_sqrt_jerk_v011_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw5_raw_jerk_v012_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw21_sqrt_jerk_v013_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw21_raw_jerk_v014_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw42_sqrt_jerk_v015_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw42_raw_jerk_v016_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw63_sqrt_jerk_v017_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw63_raw_jerk_v018_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw126_sqrt_jerk_v019_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_jw126_raw_jerk_v020_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw5_sq_jerk_v021_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw5_smean_jerk_v022_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw21_sq_jerk_v023_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw21_smean_jerk_v024_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw42_sq_jerk_v025_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw42_smean_jerk_v026_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw63_sq_jerk_v027_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw63_smean_jerk_v028_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw126_sq_jerk_v029_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_jw126_smean_jerk_v030_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw5_ema_jerk_v031_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw5_ctr_jerk_v032_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw21_ema_jerk_v033_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw21_ctr_jerk_v034_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw42_ema_jerk_v035_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw42_ctr_jerk_v036_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw63_ema_jerk_v037_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw63_ctr_jerk_v038_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw126_ema_jerk_v039_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_jw126_ctr_jerk_v040_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw5_zsc_jerk_v041_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw5_zs63_jerk_v042_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw21_zsc_jerk_v043_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw21_zs63_jerk_v044_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw42_zsc_jerk_v045_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw42_zs63_jerk_v046_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw63_zsc_jerk_v047_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw63_zs63_jerk_v048_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw126_zsc_jerk_v049_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_jw126_zs63_jerk_v050_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw5_mul_jerk_v051_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw5_log_jerk_v052_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw21_mul_jerk_v053_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw21_log_jerk_v054_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw42_mul_jerk_v055_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw42_log_jerk_v056_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw63_mul_jerk_v057_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw63_log_jerk_v058_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw126_mul_jerk_v059_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_jw126_log_jerk_v060_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw5_sqrt_jerk_v061_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw5_raw_jerk_v062_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw21_sqrt_jerk_v063_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw21_raw_jerk_v064_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw42_sqrt_jerk_v065_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw42_raw_jerk_v066_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw63_sqrt_jerk_v067_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw63_raw_jerk_v068_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw126_sqrt_jerk_v069_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_jw126_raw_jerk_v070_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw5_sq_jerk_v071_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw5_smean_jerk_v072_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw21_sq_jerk_v073_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw21_smean_jerk_v074_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw42_sq_jerk_v075_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw42_smean_jerk_v076_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw63_sq_jerk_v077_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw63_smean_jerk_v078_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw126_sq_jerk_v079_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_jw126_smean_jerk_v080_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw5_ema_jerk_v081_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw5_ctr_jerk_v082_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw21_ema_jerk_v083_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw21_ctr_jerk_v084_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw42_ema_jerk_v085_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw42_ctr_jerk_v086_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw63_ema_jerk_v087_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw63_ctr_jerk_v088_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw126_ema_jerk_v089_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_jw126_ctr_jerk_v090_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw5_zsc_jerk_v091_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw5_zs63_jerk_v092_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw21_zsc_jerk_v093_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw21_zs63_jerk_v094_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw42_zsc_jerk_v095_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw42_zs63_jerk_v096_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw63_zsc_jerk_v097_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw63_zs63_jerk_v098_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw126_zsc_jerk_v099_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_jw126_zs63_jerk_v100_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw5_mul_jerk_v101_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw5_log_jerk_v102_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw21_mul_jerk_v103_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw21_log_jerk_v104_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw42_mul_jerk_v105_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw42_log_jerk_v106_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw63_mul_jerk_v107_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw63_log_jerk_v108_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw126_mul_jerk_v109_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_jw126_log_jerk_v110_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw5_sqrt_jerk_v111_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw5_raw_jerk_v112_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw21_sqrt_jerk_v113_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw21_raw_jerk_v114_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw42_sqrt_jerk_v115_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw42_raw_jerk_v116_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw63_sqrt_jerk_v117_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw63_raw_jerk_v118_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw126_sqrt_jerk_v119_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_jw126_raw_jerk_v120_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw5_sq_jerk_v121_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw5_smean_jerk_v122_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw21_sq_jerk_v123_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw21_smean_jerk_v124_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw42_sq_jerk_v125_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw42_smean_jerk_v126_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw63_sq_jerk_v127_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw63_smean_jerk_v128_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw126_sq_jerk_v129_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_jw126_smean_jerk_v130_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw5_ema_jerk_v131_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw5_ctr_jerk_v132_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw21_ema_jerk_v133_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw21_ctr_jerk_v134_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw42_ema_jerk_v135_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw42_ctr_jerk_v136_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw63_ema_jerk_v137_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw63_ctr_jerk_v138_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw126_ema_jerk_v139_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_jw126_ctr_jerk_v140_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw5_zsc_jerk_v141_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw5_zs63_jerk_v142_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw21_zsc_jerk_v143_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw21_zs63_jerk_v144_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw42_zsc_jerk_v145_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw42_zs63_jerk_v146_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw63_zsc_jerk_v147_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw63_zs63_jerk_v148_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw126_zsc_jerk_v149_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_jw126_zs63_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF25_LST_MARKET_SHARE_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_revenue_compound", "_f25_share_growth", "_f25_market_share_score",)
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
    print(f"OK lst_market_share_growth_3rd_derivatives_001_150_claude: {n_features} features pass")
