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
def _f23_service_margin_floor(ebitdamargin, w):
    mn = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    mean = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / mean.replace(0, np.nan).abs()

def _f23_aftermarket_durability(grossmargin, w):
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    mn = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / (sd.replace(0, np.nan) + 1e-6)

def _f23_service_revenue_stability(revenue, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    mn = g.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / (sd.replace(0, np.nan) + 1e-6)


# ===== features =====
def f23laq_f23_lst_aftermarket_quality_smf_iw5_pct5_mul_base_v001_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_z5sc63_log_base_v002_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_ratiomean5_sqrt_base_v003_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_log_smean_base_v004_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_ema63_sq_base_v005_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_pct21_mul_base_v006_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_z21sc63_log_base_v007_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_ratiomean21_sqrt_base_v008_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_log_smean_base_v009_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_ema63_sq_base_v010_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_pct63_mul_base_v011_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_z63sc63_log_base_v012_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_ratiomean63_sqrt_base_v013_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_log_smean_base_v014_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_ema63_sq_base_v015_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_pct126_mul_base_v016_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_z126sc63_log_base_v017_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_ratiomean126_sqrt_base_v018_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_log_smean_base_v019_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_ema63_sq_base_v020_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_pct252_mul_base_v021_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_z252sc63_log_base_v022_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_ratiomean252_sqrt_base_v023_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_log_smean_base_v024_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_ema63_sq_base_v025_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_pct5_mul_base_v026_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_z5sc63_log_base_v027_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_ratiomean5_sqrt_base_v028_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_log_smean_base_v029_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_ema63_sq_base_v030_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_pct21_mul_base_v031_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_z21sc63_log_base_v032_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_ratiomean21_sqrt_base_v033_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_log_smean_base_v034_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_ema63_sq_base_v035_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_pct63_mul_base_v036_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_z63sc63_log_base_v037_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_ratiomean63_sqrt_base_v038_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_log_smean_base_v039_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_ema63_sq_base_v040_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_pct126_mul_base_v041_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_z126sc63_log_base_v042_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_ratiomean126_sqrt_base_v043_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_log_smean_base_v044_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_ema63_sq_base_v045_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_pct252_mul_base_v046_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_z252sc63_log_base_v047_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_ratiomean252_sqrt_base_v048_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_log_smean_base_v049_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_ema63_sq_base_v050_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_pct5_mul_base_v051_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_z5sc63_log_base_v052_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_ratiomean5_sqrt_base_v053_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_log_smean_base_v054_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_ema63_sq_base_v055_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_pct21_mul_base_v056_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_z21sc63_log_base_v057_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_ratiomean21_sqrt_base_v058_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_log_smean_base_v059_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_ema63_sq_base_v060_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_pct63_mul_base_v061_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_z63sc63_log_base_v062_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_ratiomean63_sqrt_base_v063_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_log_smean_base_v064_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_ema63_sq_base_v065_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_pct126_mul_base_v066_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_z126sc63_log_base_v067_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_ratiomean126_sqrt_base_v068_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_log_smean_base_v069_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_ema63_sq_base_v070_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_pct252_mul_base_v071_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_z252sc63_log_base_v072_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _z(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_ratiomean252_sqrt_base_v073_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = (base / _mean(base, 252).replace(0, np.nan)) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_log_smean_base_v074_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_ema63_sq_base_v075_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23laq_f23_lst_aftermarket_quality_smf_iw5_pct5_mul_base_v001_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_z5sc63_log_base_v002_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_ratiomean5_sqrt_base_v003_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_log_smean_base_v004_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_ema63_sq_base_v005_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_pct21_mul_base_v006_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_z21sc63_log_base_v007_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_ratiomean21_sqrt_base_v008_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_log_smean_base_v009_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_ema63_sq_base_v010_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_pct63_mul_base_v011_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_z63sc63_log_base_v012_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_ratiomean63_sqrt_base_v013_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_log_smean_base_v014_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_ema63_sq_base_v015_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_pct126_mul_base_v016_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_z126sc63_log_base_v017_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_ratiomean126_sqrt_base_v018_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_log_smean_base_v019_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_ema63_sq_base_v020_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_pct252_mul_base_v021_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_z252sc63_log_base_v022_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_ratiomean252_sqrt_base_v023_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_log_smean_base_v024_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_ema63_sq_base_v025_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_pct5_mul_base_v026_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_z5sc63_log_base_v027_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_ratiomean5_sqrt_base_v028_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_log_smean_base_v029_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_ema63_sq_base_v030_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_pct21_mul_base_v031_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_z21sc63_log_base_v032_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_ratiomean21_sqrt_base_v033_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_log_smean_base_v034_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_ema63_sq_base_v035_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_pct63_mul_base_v036_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_z63sc63_log_base_v037_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_ratiomean63_sqrt_base_v038_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_log_smean_base_v039_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_ema63_sq_base_v040_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_pct126_mul_base_v041_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_z126sc63_log_base_v042_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_ratiomean126_sqrt_base_v043_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_log_smean_base_v044_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_ema63_sq_base_v045_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_pct252_mul_base_v046_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_z252sc63_log_base_v047_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_ratiomean252_sqrt_base_v048_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_log_smean_base_v049_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_ema63_sq_base_v050_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_pct5_mul_base_v051_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_z5sc63_log_base_v052_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_ratiomean5_sqrt_base_v053_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_log_smean_base_v054_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_ema63_sq_base_v055_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_pct21_mul_base_v056_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_z21sc63_log_base_v057_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_ratiomean21_sqrt_base_v058_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_log_smean_base_v059_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_ema63_sq_base_v060_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_pct63_mul_base_v061_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_z63sc63_log_base_v062_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_ratiomean63_sqrt_base_v063_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_log_smean_base_v064_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_ema63_sq_base_v065_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_pct126_mul_base_v066_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_z126sc63_log_base_v067_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_ratiomean126_sqrt_base_v068_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_log_smean_base_v069_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_ema63_sq_base_v070_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_pct252_mul_base_v071_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_z252sc63_log_base_v072_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_ratiomean252_sqrt_base_v073_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_log_smean_base_v074_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_ema63_sq_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF23_LST_AFTERMARKET_QUALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "grossmargin": grossmargin, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_service_margin_floor", "_f23_aftermarket_durability", "_f23_service_revenue_stability",)
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
    print(f"OK lst_aftermarket_quality_base_001_075_claude: {n_features} features pass")
