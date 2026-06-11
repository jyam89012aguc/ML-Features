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
def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw5_spct_mul_slope_v001_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw5_sdn_log_slope_v002_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw21_spct_sqrt_slope_v003_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw21_sdn_smean_slope_v004_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw42_spct_sq_slope_v005_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw42_sdn_mul_slope_v006_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw63_spct_log_slope_v007_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw63_sdn_sqrt_slope_v008_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw126_spct_smean_slope_v009_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sw126_sdn_sq_slope_v010_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw5_spct_mul_slope_v011_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw5_sdn_log_slope_v012_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw21_spct_sqrt_slope_v013_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw21_sdn_smean_slope_v014_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw42_spct_sq_slope_v015_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw42_sdn_mul_slope_v016_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw63_spct_log_slope_v017_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw63_sdn_sqrt_slope_v018_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw126_spct_smean_slope_v019_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sw126_sdn_sq_slope_v020_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw5_spct_mul_slope_v021_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw5_sdn_log_slope_v022_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw21_spct_sqrt_slope_v023_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw21_sdn_smean_slope_v024_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw42_spct_sq_slope_v025_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw42_sdn_mul_slope_v026_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw63_spct_log_slope_v027_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw63_sdn_sqrt_slope_v028_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw126_spct_smean_slope_v029_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sw126_sdn_sq_slope_v030_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw5_spct_mul_slope_v031_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw5_sdn_log_slope_v032_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw21_spct_sqrt_slope_v033_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw21_sdn_smean_slope_v034_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw42_spct_sq_slope_v035_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw42_sdn_mul_slope_v036_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw63_spct_log_slope_v037_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw63_sdn_sqrt_slope_v038_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw126_spct_smean_slope_v039_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sw126_sdn_sq_slope_v040_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw5_spct_mul_slope_v041_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw5_sdn_log_slope_v042_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw21_spct_sqrt_slope_v043_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw21_sdn_smean_slope_v044_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw42_spct_sq_slope_v045_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw42_sdn_mul_slope_v046_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw63_spct_log_slope_v047_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw63_sdn_sqrt_slope_v048_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw126_spct_smean_slope_v049_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sw126_sdn_sq_slope_v050_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw5_spct_mul_slope_v051_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw5_sdn_log_slope_v052_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw21_spct_sqrt_slope_v053_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw21_sdn_smean_slope_v054_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw42_spct_sq_slope_v055_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw42_sdn_mul_slope_v056_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw63_spct_log_slope_v057_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw63_sdn_sqrt_slope_v058_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw126_spct_smean_slope_v059_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sw126_sdn_sq_slope_v060_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw5_spct_mul_slope_v061_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw5_sdn_log_slope_v062_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw21_spct_sqrt_slope_v063_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw21_sdn_smean_slope_v064_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw42_spct_sq_slope_v065_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw42_sdn_mul_slope_v066_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw63_spct_log_slope_v067_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw63_sdn_sqrt_slope_v068_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw126_spct_smean_slope_v069_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sw126_sdn_sq_slope_v070_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw5_spct_mul_slope_v071_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw5_sdn_log_slope_v072_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw21_spct_sqrt_slope_v073_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw21_sdn_smean_slope_v074_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw42_spct_sq_slope_v075_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw42_sdn_mul_slope_v076_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw63_spct_log_slope_v077_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw63_sdn_sqrt_slope_v078_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw126_spct_smean_slope_v079_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sw126_sdn_sq_slope_v080_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw5_spct_mul_slope_v081_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw5_sdn_log_slope_v082_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw21_spct_sqrt_slope_v083_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw21_sdn_smean_slope_v084_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw42_spct_sq_slope_v085_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw42_sdn_mul_slope_v086_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw63_spct_log_slope_v087_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw63_sdn_sqrt_slope_v088_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw126_spct_smean_slope_v089_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sw126_sdn_sq_slope_v090_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw5_spct_mul_slope_v091_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw5_sdn_log_slope_v092_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw21_spct_sqrt_slope_v093_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw21_sdn_smean_slope_v094_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw42_spct_sq_slope_v095_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw42_sdn_mul_slope_v096_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw63_spct_log_slope_v097_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw63_sdn_sqrt_slope_v098_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw126_spct_smean_slope_v099_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sw126_sdn_sq_slope_v100_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw5_spct_mul_slope_v101_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw5_sdn_log_slope_v102_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw21_spct_sqrt_slope_v103_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw21_sdn_smean_slope_v104_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw42_spct_sq_slope_v105_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw42_sdn_mul_slope_v106_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw63_spct_log_slope_v107_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw63_sdn_sqrt_slope_v108_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw126_spct_smean_slope_v109_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sw126_sdn_sq_slope_v110_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw5_spct_mul_slope_v111_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw5_sdn_log_slope_v112_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw21_spct_sqrt_slope_v113_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw21_sdn_smean_slope_v114_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw42_spct_sq_slope_v115_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw42_sdn_mul_slope_v116_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw63_spct_log_slope_v117_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw63_sdn_sqrt_slope_v118_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw126_spct_smean_slope_v119_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sw126_sdn_sq_slope_v120_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw5_spct_mul_slope_v121_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw5_sdn_log_slope_v122_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw21_spct_sqrt_slope_v123_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw21_sdn_smean_slope_v124_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw42_spct_sq_slope_v125_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw42_sdn_mul_slope_v126_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw63_spct_log_slope_v127_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw63_sdn_sqrt_slope_v128_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw126_spct_smean_slope_v129_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sw126_sdn_sq_slope_v130_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw5_spct_mul_slope_v131_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw5_sdn_log_slope_v132_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw21_spct_sqrt_slope_v133_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw21_sdn_smean_slope_v134_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw42_spct_sq_slope_v135_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw42_sdn_mul_slope_v136_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw63_spct_log_slope_v137_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw63_sdn_sqrt_slope_v138_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw126_spct_smean_slope_v139_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sw126_sdn_sq_slope_v140_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw5_spct_mul_slope_v141_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw5_sdn_log_slope_v142_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_diff_norm(base, 5) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw21_spct_sqrt_slope_v143_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_pct(base, 21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw21_sdn_smean_slope_v144_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw42_spct_sq_slope_v145_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_pct(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw42_sdn_mul_slope_v146_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw63_spct_log_slope_v147_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_pct(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw63_sdn_sqrt_slope_v148_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_diff_norm(base, 63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw126_spct_smean_slope_v149_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_pct(base, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sw126_sdn_sq_slope_v150_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw5_spct_mul_slope_v001_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw5_sdn_log_slope_v002_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw21_spct_sqrt_slope_v003_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw21_sdn_smean_slope_v004_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw42_spct_sq_slope_v005_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw42_sdn_mul_slope_v006_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw63_spct_log_slope_v007_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw63_sdn_sqrt_slope_v008_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw126_spct_smean_slope_v009_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sw126_sdn_sq_slope_v010_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw5_spct_mul_slope_v011_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw5_sdn_log_slope_v012_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw21_spct_sqrt_slope_v013_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw21_sdn_smean_slope_v014_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw42_spct_sq_slope_v015_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw42_sdn_mul_slope_v016_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw63_spct_log_slope_v017_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw63_sdn_sqrt_slope_v018_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw126_spct_smean_slope_v019_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sw126_sdn_sq_slope_v020_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw5_spct_mul_slope_v021_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw5_sdn_log_slope_v022_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw21_spct_sqrt_slope_v023_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw21_sdn_smean_slope_v024_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw42_spct_sq_slope_v025_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw42_sdn_mul_slope_v026_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw63_spct_log_slope_v027_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw63_sdn_sqrt_slope_v028_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw126_spct_smean_slope_v029_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sw126_sdn_sq_slope_v030_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw5_spct_mul_slope_v031_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw5_sdn_log_slope_v032_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw21_spct_sqrt_slope_v033_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw21_sdn_smean_slope_v034_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw42_spct_sq_slope_v035_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw42_sdn_mul_slope_v036_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw63_spct_log_slope_v037_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw63_sdn_sqrt_slope_v038_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw126_spct_smean_slope_v039_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sw126_sdn_sq_slope_v040_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw5_spct_mul_slope_v041_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw5_sdn_log_slope_v042_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw21_spct_sqrt_slope_v043_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw21_sdn_smean_slope_v044_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw42_spct_sq_slope_v045_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw42_sdn_mul_slope_v046_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw63_spct_log_slope_v047_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw63_sdn_sqrt_slope_v048_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw126_spct_smean_slope_v049_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sw126_sdn_sq_slope_v050_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw5_spct_mul_slope_v051_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw5_sdn_log_slope_v052_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw21_spct_sqrt_slope_v053_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw21_sdn_smean_slope_v054_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw42_spct_sq_slope_v055_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw42_sdn_mul_slope_v056_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw63_spct_log_slope_v057_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw63_sdn_sqrt_slope_v058_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw126_spct_smean_slope_v059_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sw126_sdn_sq_slope_v060_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw5_spct_mul_slope_v061_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw5_sdn_log_slope_v062_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw21_spct_sqrt_slope_v063_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw21_sdn_smean_slope_v064_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw42_spct_sq_slope_v065_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw42_sdn_mul_slope_v066_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw63_spct_log_slope_v067_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw63_sdn_sqrt_slope_v068_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw126_spct_smean_slope_v069_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sw126_sdn_sq_slope_v070_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw5_spct_mul_slope_v071_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw5_sdn_log_slope_v072_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw21_spct_sqrt_slope_v073_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw21_sdn_smean_slope_v074_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw42_spct_sq_slope_v075_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw42_sdn_mul_slope_v076_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw63_spct_log_slope_v077_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw63_sdn_sqrt_slope_v078_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw126_spct_smean_slope_v079_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sw126_sdn_sq_slope_v080_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw5_spct_mul_slope_v081_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw5_sdn_log_slope_v082_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw21_spct_sqrt_slope_v083_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw21_sdn_smean_slope_v084_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw42_spct_sq_slope_v085_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw42_sdn_mul_slope_v086_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw63_spct_log_slope_v087_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw63_sdn_sqrt_slope_v088_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw126_spct_smean_slope_v089_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sw126_sdn_sq_slope_v090_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw5_spct_mul_slope_v091_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw5_sdn_log_slope_v092_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw21_spct_sqrt_slope_v093_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw21_sdn_smean_slope_v094_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw42_spct_sq_slope_v095_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw42_sdn_mul_slope_v096_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw63_spct_log_slope_v097_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw63_sdn_sqrt_slope_v098_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw126_spct_smean_slope_v099_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sw126_sdn_sq_slope_v100_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw5_spct_mul_slope_v101_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw5_sdn_log_slope_v102_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw21_spct_sqrt_slope_v103_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw21_sdn_smean_slope_v104_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw42_spct_sq_slope_v105_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw42_sdn_mul_slope_v106_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw63_spct_log_slope_v107_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw63_sdn_sqrt_slope_v108_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw126_spct_smean_slope_v109_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sw126_sdn_sq_slope_v110_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw5_spct_mul_slope_v111_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw5_sdn_log_slope_v112_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw21_spct_sqrt_slope_v113_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw21_sdn_smean_slope_v114_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw42_spct_sq_slope_v115_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw42_sdn_mul_slope_v116_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw63_spct_log_slope_v117_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw63_sdn_sqrt_slope_v118_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw126_spct_smean_slope_v119_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sw126_sdn_sq_slope_v120_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw5_spct_mul_slope_v121_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw5_sdn_log_slope_v122_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw21_spct_sqrt_slope_v123_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw21_sdn_smean_slope_v124_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw42_spct_sq_slope_v125_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw42_sdn_mul_slope_v126_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw63_spct_log_slope_v127_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw63_sdn_sqrt_slope_v128_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw126_spct_smean_slope_v129_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sw126_sdn_sq_slope_v130_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw5_spct_mul_slope_v131_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw5_sdn_log_slope_v132_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw21_spct_sqrt_slope_v133_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw21_sdn_smean_slope_v134_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw42_spct_sq_slope_v135_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw42_sdn_mul_slope_v136_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw63_spct_log_slope_v137_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw63_sdn_sqrt_slope_v138_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw126_spct_smean_slope_v139_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sw126_sdn_sq_slope_v140_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw5_spct_mul_slope_v141_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw5_sdn_log_slope_v142_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw21_spct_sqrt_slope_v143_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw21_sdn_smean_slope_v144_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw42_spct_sq_slope_v145_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw42_sdn_mul_slope_v146_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw63_spct_log_slope_v147_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw63_sdn_sqrt_slope_v148_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw126_spct_smean_slope_v149_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sw126_sdn_sq_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF23_LST_AFTERMARKET_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK lst_aftermarket_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
