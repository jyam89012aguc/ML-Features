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
def f23laq_f23_lst_aftermarket_quality_smf_iw5_mean63_mul_base_v076_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_std63_log_base_v077_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_diff5_sqrt_base_v078_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_sqr_smean_base_v079_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw5_mmr252_sq_base_v080_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_mean63_mul_base_v081_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_std63_log_base_v082_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_diff21_sqrt_base_v083_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_sqr_smean_base_v084_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw21_mmr252_sq_base_v085_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_mean63_mul_base_v086_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_std63_log_base_v087_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_diff63_sqrt_base_v088_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_sqr_smean_base_v089_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw63_mmr252_sq_base_v090_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_mean63_mul_base_v091_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_std63_log_base_v092_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_diff126_sqrt_base_v093_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_sqr_smean_base_v094_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw126_mmr252_sq_base_v095_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_mean63_mul_base_v096_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_std63_log_base_v097_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_diff252_sqrt_base_v098_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_sqr_smean_base_v099_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_smf_iw252_mmr252_sq_base_v100_signal(ebitdamargin, closeadj):
    base = _f23_service_margin_floor(ebitdamargin, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_mean63_mul_base_v101_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_std63_log_base_v102_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_diff5_sqrt_base_v103_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_sqr_smean_base_v104_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw5_mmr252_sq_base_v105_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_mean63_mul_base_v106_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_std63_log_base_v107_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_diff21_sqrt_base_v108_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_sqr_smean_base_v109_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw21_mmr252_sq_base_v110_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_mean63_mul_base_v111_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_std63_log_base_v112_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_diff63_sqrt_base_v113_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_sqr_smean_base_v114_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw63_mmr252_sq_base_v115_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_mean63_mul_base_v116_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_std63_log_base_v117_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_diff126_sqrt_base_v118_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_sqr_smean_base_v119_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw126_mmr252_sq_base_v120_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_mean63_mul_base_v121_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_std63_log_base_v122_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_diff252_sqrt_base_v123_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_sqr_smean_base_v124_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_dur_iw252_mmr252_sq_base_v125_signal(grossmargin, closeadj):
    base = _f23_aftermarket_durability(grossmargin, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_mean63_mul_base_v126_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_std63_log_base_v127_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_diff5_sqrt_base_v128_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = base.diff(5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_sqr_smean_base_v129_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw5_mmr252_sq_base_v130_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 5)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_mean63_mul_base_v131_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_std63_log_base_v132_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_diff21_sqrt_base_v133_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = base.diff(21) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_sqr_smean_base_v134_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw21_mmr252_sq_base_v135_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 21)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_mean63_mul_base_v136_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_std63_log_base_v137_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_diff63_sqrt_base_v138_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = base.diff(63) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_sqr_smean_base_v139_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw63_mmr252_sq_base_v140_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_mean63_mul_base_v141_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_std63_log_base_v142_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_diff126_sqrt_base_v143_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = base.diff(126) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_sqr_smean_base_v144_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw126_mmr252_sq_base_v145_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 126)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_mean63_mul_base_v146_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_std63_log_base_v147_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = _std(base, 63) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_diff252_sqrt_base_v148_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = base.diff(252) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_sqr_smean_base_v149_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    result = base * base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f23laq_f23_lst_aftermarket_quality_srs_iw252_mmr252_sq_base_v150_signal(revenue, closeadj):
    base = _f23_service_revenue_stability(revenue, 252)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = ((base - lo) / (hi - lo).replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23laq_f23_lst_aftermarket_quality_smf_iw5_mean63_mul_base_v076_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_std63_log_base_v077_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_diff5_sqrt_base_v078_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_sqr_smean_base_v079_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw5_mmr252_sq_base_v080_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_mean63_mul_base_v081_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_std63_log_base_v082_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_diff21_sqrt_base_v083_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_sqr_smean_base_v084_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw21_mmr252_sq_base_v085_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_mean63_mul_base_v086_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_std63_log_base_v087_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_diff63_sqrt_base_v088_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_sqr_smean_base_v089_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw63_mmr252_sq_base_v090_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_mean63_mul_base_v091_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_std63_log_base_v092_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_diff126_sqrt_base_v093_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_sqr_smean_base_v094_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw126_mmr252_sq_base_v095_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_mean63_mul_base_v096_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_std63_log_base_v097_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_diff252_sqrt_base_v098_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_sqr_smean_base_v099_signal,
    f23laq_f23_lst_aftermarket_quality_smf_iw252_mmr252_sq_base_v100_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_mean63_mul_base_v101_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_std63_log_base_v102_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_diff5_sqrt_base_v103_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_sqr_smean_base_v104_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw5_mmr252_sq_base_v105_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_mean63_mul_base_v106_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_std63_log_base_v107_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_diff21_sqrt_base_v108_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_sqr_smean_base_v109_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw21_mmr252_sq_base_v110_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_mean63_mul_base_v111_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_std63_log_base_v112_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_diff63_sqrt_base_v113_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_sqr_smean_base_v114_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw63_mmr252_sq_base_v115_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_mean63_mul_base_v116_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_std63_log_base_v117_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_diff126_sqrt_base_v118_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_sqr_smean_base_v119_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw126_mmr252_sq_base_v120_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_mean63_mul_base_v121_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_std63_log_base_v122_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_diff252_sqrt_base_v123_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_sqr_smean_base_v124_signal,
    f23laq_f23_lst_aftermarket_quality_dur_iw252_mmr252_sq_base_v125_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_mean63_mul_base_v126_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_std63_log_base_v127_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_diff5_sqrt_base_v128_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_sqr_smean_base_v129_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw5_mmr252_sq_base_v130_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_mean63_mul_base_v131_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_std63_log_base_v132_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_diff21_sqrt_base_v133_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_sqr_smean_base_v134_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw21_mmr252_sq_base_v135_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_mean63_mul_base_v136_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_std63_log_base_v137_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_diff63_sqrt_base_v138_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_sqr_smean_base_v139_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw63_mmr252_sq_base_v140_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_mean63_mul_base_v141_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_std63_log_base_v142_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_diff126_sqrt_base_v143_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_sqr_smean_base_v144_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw126_mmr252_sq_base_v145_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_mean63_mul_base_v146_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_std63_log_base_v147_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_diff252_sqrt_base_v148_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_sqr_smean_base_v149_signal,
    f23laq_f23_lst_aftermarket_quality_srs_iw252_mmr252_sq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FF23_LST_AFTERMARKET_QUALITY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK lst_aftermarket_quality_base_076_150_claude: {n_features} features pass")
