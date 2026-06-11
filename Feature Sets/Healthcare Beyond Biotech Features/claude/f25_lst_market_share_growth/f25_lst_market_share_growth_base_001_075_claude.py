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
def f25lms_f25_lst_market_share_growth_rc_iw5_pct5_mul_base_v001_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_z5sc63_log_base_v002_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_ratiomean5_sqrt_base_v003_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_log_smean_base_v004_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw5_ema63_sq_base_v005_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_pct21_mul_base_v006_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_z21sc63_log_base_v007_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_ratiomean21_sqrt_base_v008_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_log_smean_base_v009_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw21_ema63_sq_base_v010_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_pct63_mul_base_v011_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_z63sc63_log_base_v012_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_ratiomean63_sqrt_base_v013_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_log_smean_base_v014_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw63_ema63_sq_base_v015_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_pct126_mul_base_v016_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_z126sc63_log_base_v017_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_ratiomean126_sqrt_base_v018_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_log_smean_base_v019_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw126_ema63_sq_base_v020_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_pct252_mul_base_v021_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_z252sc63_log_base_v022_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_ratiomean252_sqrt_base_v023_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_log_smean_base_v024_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_rc_iw252_ema63_sq_base_v025_signal(revenue, closeadj):
    base = _f25_revenue_compound(revenue, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_pct5_mul_base_v026_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_z5sc63_log_base_v027_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_ratiomean5_sqrt_base_v028_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_log_smean_base_v029_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw5_ema63_sq_base_v030_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_pct21_mul_base_v031_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_z21sc63_log_base_v032_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_ratiomean21_sqrt_base_v033_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_log_smean_base_v034_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw21_ema63_sq_base_v035_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_pct63_mul_base_v036_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_z63sc63_log_base_v037_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_ratiomean63_sqrt_base_v038_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_log_smean_base_v039_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw63_ema63_sq_base_v040_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_pct126_mul_base_v041_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_z126sc63_log_base_v042_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_ratiomean126_sqrt_base_v043_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_log_smean_base_v044_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw126_ema63_sq_base_v045_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_pct252_mul_base_v046_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_z252sc63_log_base_v047_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_ratiomean252_sqrt_base_v048_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_log_smean_base_v049_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_sg_iw252_ema63_sq_base_v050_signal(revenue, closeadj):
    base = _f25_share_growth(revenue, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_pct5_mul_base_v051_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_z5sc63_log_base_v052_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_ratiomean5_sqrt_base_v053_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_log_smean_base_v054_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw5_ema63_sq_base_v055_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_pct21_mul_base_v056_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_z21sc63_log_base_v057_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_ratiomean21_sqrt_base_v058_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_log_smean_base_v059_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw21_ema63_sq_base_v060_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_pct63_mul_base_v061_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_z63sc63_log_base_v062_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_ratiomean63_sqrt_base_v063_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_log_smean_base_v064_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw63_ema63_sq_base_v065_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_pct126_mul_base_v066_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_z126sc63_log_base_v067_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_ratiomean126_sqrt_base_v068_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_log_smean_base_v069_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw126_ema63_sq_base_v070_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_pct252_mul_base_v071_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_z252sc63_log_base_v072_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_ratiomean252_sqrt_base_v073_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_log_smean_base_v074_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f25lms_f25_lst_market_share_growth_mss_iw252_ema63_sq_base_v075_signal(revenue, ebitda, closeadj):
    base = _f25_market_share_score(revenue, ebitda, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25lms_f25_lst_market_share_growth_rc_iw5_pct5_mul_base_v001_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_z5sc63_log_base_v002_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_ratiomean5_sqrt_base_v003_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_log_smean_base_v004_signal,
    f25lms_f25_lst_market_share_growth_rc_iw5_ema63_sq_base_v005_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_pct21_mul_base_v006_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_z21sc63_log_base_v007_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_ratiomean21_sqrt_base_v008_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_log_smean_base_v009_signal,
    f25lms_f25_lst_market_share_growth_rc_iw21_ema63_sq_base_v010_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_pct63_mul_base_v011_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_z63sc63_log_base_v012_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_ratiomean63_sqrt_base_v013_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_log_smean_base_v014_signal,
    f25lms_f25_lst_market_share_growth_rc_iw63_ema63_sq_base_v015_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_pct126_mul_base_v016_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_z126sc63_log_base_v017_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_ratiomean126_sqrt_base_v018_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_log_smean_base_v019_signal,
    f25lms_f25_lst_market_share_growth_rc_iw126_ema63_sq_base_v020_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_pct252_mul_base_v021_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_z252sc63_log_base_v022_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_ratiomean252_sqrt_base_v023_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_log_smean_base_v024_signal,
    f25lms_f25_lst_market_share_growth_rc_iw252_ema63_sq_base_v025_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_pct5_mul_base_v026_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_z5sc63_log_base_v027_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_ratiomean5_sqrt_base_v028_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_log_smean_base_v029_signal,
    f25lms_f25_lst_market_share_growth_sg_iw5_ema63_sq_base_v030_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_pct21_mul_base_v031_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_z21sc63_log_base_v032_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_ratiomean21_sqrt_base_v033_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_log_smean_base_v034_signal,
    f25lms_f25_lst_market_share_growth_sg_iw21_ema63_sq_base_v035_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_pct63_mul_base_v036_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_z63sc63_log_base_v037_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_ratiomean63_sqrt_base_v038_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_log_smean_base_v039_signal,
    f25lms_f25_lst_market_share_growth_sg_iw63_ema63_sq_base_v040_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_pct126_mul_base_v041_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_z126sc63_log_base_v042_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_ratiomean126_sqrt_base_v043_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_log_smean_base_v044_signal,
    f25lms_f25_lst_market_share_growth_sg_iw126_ema63_sq_base_v045_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_pct252_mul_base_v046_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_z252sc63_log_base_v047_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_ratiomean252_sqrt_base_v048_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_log_smean_base_v049_signal,
    f25lms_f25_lst_market_share_growth_sg_iw252_ema63_sq_base_v050_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_pct5_mul_base_v051_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_z5sc63_log_base_v052_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_ratiomean5_sqrt_base_v053_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_log_smean_base_v054_signal,
    f25lms_f25_lst_market_share_growth_mss_iw5_ema63_sq_base_v055_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_pct21_mul_base_v056_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_z21sc63_log_base_v057_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_ratiomean21_sqrt_base_v058_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_log_smean_base_v059_signal,
    f25lms_f25_lst_market_share_growth_mss_iw21_ema63_sq_base_v060_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_pct63_mul_base_v061_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_z63sc63_log_base_v062_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_ratiomean63_sqrt_base_v063_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_log_smean_base_v064_signal,
    f25lms_f25_lst_market_share_growth_mss_iw63_ema63_sq_base_v065_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_pct126_mul_base_v066_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_z126sc63_log_base_v067_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_ratiomean126_sqrt_base_v068_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_log_smean_base_v069_signal,
    f25lms_f25_lst_market_share_growth_mss_iw126_ema63_sq_base_v070_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_pct252_mul_base_v071_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_z252sc63_log_base_v072_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_ratiomean252_sqrt_base_v073_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_log_smean_base_v074_signal,
    f25lms_f25_lst_market_share_growth_mss_iw252_ema63_sq_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF25_LST_MARKET_SHARE_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK lst_market_share_growth_base_001_075_claude: {n_features} features pass")
