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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f48_bottom_signature(revenue, w):
    rmin = revenue.rolling(w, min_periods=max(2, w // 2)).min()
    rmean = revenue.rolling(w, min_periods=max(2, w // 2)).mean()
    return (revenue - rmin) / rmean.replace(0, np.nan).abs()


def _f48_margin_bottom(ebitdamargin, w):
    mmin = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).min()
    return (ebitdamargin - mmin)


def _f48_cycle_bottom_score(revenue, ebitda, fcf, w):
    rs = (revenue - revenue.rolling(w, min_periods=max(2, w // 2)).min()) / revenue.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    es = (ebitda - ebitda.rolling(w, min_periods=max(2, w // 2)).min()) / ebitda.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    fs = (fcf - fcf.rolling(w, min_periods=max(2, w // 2)).min()) / fcf.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    return (rs + es + fs) / 3.0



def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk5_jerk_v001_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk10_jerk_v002_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk21_jerk_v003_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk42_jerk_v004_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk63_jerk_v005_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk126_jerk_v006_signal(revenue):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_f48_bottom_signature(revenue, 5))
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk5_jerk_v007_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk10_jerk_v008_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk21_jerk_v009_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk42_jerk_v010_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk63_jerk_v011_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk126_jerk_v012_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk5_jerk_v013_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk10_jerk_v014_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk21_jerk_v015_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk42_jerk_v016_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk63_jerk_v017_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk126_jerk_v018_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk5_jerk_v019_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk10_jerk_v020_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk21_jerk_v021_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk42_jerk_v022_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk63_jerk_v023_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk126_jerk_v024_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk5_jerk_v025_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk10_jerk_v026_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk21_jerk_v027_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk42_jerk_v028_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk63_jerk_v029_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk126_jerk_v030_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk5_jerk_v031_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk10_jerk_v032_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk21_jerk_v033_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk42_jerk_v034_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk63_jerk_v035_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk126_jerk_v036_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk5_jerk_v037_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk10_jerk_v038_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk21_jerk_v039_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk42_jerk_v040_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk63_jerk_v041_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk126_jerk_v042_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk5_jerk_v043_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk10_jerk_v044_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk21_jerk_v045_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk42_jerk_v046_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk63_jerk_v047_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk126_jerk_v048_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk5_jerk_v049_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk10_jerk_v050_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk21_jerk_v051_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk42_jerk_v052_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk63_jerk_v053_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk126_jerk_v054_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_z(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk5_jerk_v055_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk10_jerk_v056_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk21_jerk_v057_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk42_jerk_v058_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk63_jerk_v059_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk126_jerk_v060_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk5_jerk_v061_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk10_jerk_v062_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk21_jerk_v063_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk42_jerk_v064_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk63_jerk_v065_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk126_jerk_v066_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk5_jerk_v067_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk10_jerk_v068_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk21_jerk_v069_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk42_jerk_v070_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk63_jerk_v071_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk126_jerk_v072_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk5_jerk_v073_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk10_jerk_v074_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk21_jerk_v075_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk42_jerk_v076_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk63_jerk_v077_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk126_jerk_v078_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_mean(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk5_jerk_v079_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk10_jerk_v080_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk21_jerk_v081_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk42_jerk_v082_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk63_jerk_v083_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk126_jerk_v084_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk5_jerk_v085_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk10_jerk_v086_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk21_jerk_v087_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk42_jerk_v088_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk63_jerk_v089_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk126_jerk_v090_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk5_jerk_v091_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk10_jerk_v092_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk21_jerk_v093_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk42_jerk_v094_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk63_jerk_v095_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk126_jerk_v096_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk5_jerk_v097_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk10_jerk_v098_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk21_jerk_v099_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk42_jerk_v100_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk63_jerk_v101_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk126_jerk_v102_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = (_std(_f48_bottom_signature(revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk5_jerk_v103_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk10_jerk_v104_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk21_jerk_v105_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk42_jerk_v106_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk63_jerk_v107_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk126_jerk_v108_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk5_jerk_v109_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk10_jerk_v110_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk21_jerk_v111_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk42_jerk_v112_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk63_jerk_v113_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk126_jerk_v114_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk5_jerk_v115_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk10_jerk_v116_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk21_jerk_v117_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk42_jerk_v118_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk63_jerk_v119_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk126_jerk_v120_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk5_jerk_v121_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk10_jerk_v122_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk21_jerk_v123_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk42_jerk_v124_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk63_jerk_v125_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk126_jerk_v126_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk5_jerk_v127_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk10_jerk_v128_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk21_jerk_v129_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk42_jerk_v130_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk63_jerk_v131_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk126_jerk_v132_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk5_jerk_v133_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk10_jerk_v134_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk21_jerk_v135_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk42_jerk_v136_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk63_jerk_v137_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk126_jerk_v138_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk5_jerk_v139_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk10_jerk_v140_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk21_jerk_v141_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk42_jerk_v142_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk63_jerk_v143_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk126_jerk_v144_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk5_jerk_v145_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk10_jerk_v146_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk21_jerk_v147_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk42_jerk_v148_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk63_jerk_v149_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk126_jerk_v150_signal(revenue, closeadj):
    base_tmp = _f48_bottom_signature(revenue, 5)
    transformed = ((_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk5_jerk_v001_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk10_jerk_v002_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk21_jerk_v003_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk42_jerk_v004_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk63_jerk_v005_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_jk126_jerk_v006_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk5_jerk_v007_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk10_jerk_v008_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk21_jerk_v009_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk42_jerk_v010_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk63_jerk_v011_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_jk126_jerk_v012_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk5_jerk_v013_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk10_jerk_v014_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk21_jerk_v015_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk42_jerk_v016_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk63_jerk_v017_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_jk126_jerk_v018_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk5_jerk_v019_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk10_jerk_v020_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk21_jerk_v021_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk42_jerk_v022_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk63_jerk_v023_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_jk126_jerk_v024_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk5_jerk_v025_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk10_jerk_v026_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk21_jerk_v027_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk42_jerk_v028_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk63_jerk_v029_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_jk126_jerk_v030_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk5_jerk_v031_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk10_jerk_v032_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk21_jerk_v033_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk42_jerk_v034_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk63_jerk_v035_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_jk126_jerk_v036_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk5_jerk_v037_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk10_jerk_v038_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk21_jerk_v039_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk42_jerk_v040_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk63_jerk_v041_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_jk126_jerk_v042_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk5_jerk_v043_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk10_jerk_v044_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk21_jerk_v045_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk42_jerk_v046_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk63_jerk_v047_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_jk126_jerk_v048_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk5_jerk_v049_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk10_jerk_v050_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk21_jerk_v051_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk42_jerk_v052_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk63_jerk_v053_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_jk126_jerk_v054_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk5_jerk_v055_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk10_jerk_v056_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk21_jerk_v057_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk42_jerk_v058_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk63_jerk_v059_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_jk126_jerk_v060_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk5_jerk_v061_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk10_jerk_v062_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk21_jerk_v063_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk42_jerk_v064_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk63_jerk_v065_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_jk126_jerk_v066_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk5_jerk_v067_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk10_jerk_v068_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk21_jerk_v069_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk42_jerk_v070_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk63_jerk_v071_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_jk126_jerk_v072_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk5_jerk_v073_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk10_jerk_v074_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk21_jerk_v075_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk42_jerk_v076_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk63_jerk_v077_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_jk126_jerk_v078_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk5_jerk_v079_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk10_jerk_v080_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk21_jerk_v081_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk42_jerk_v082_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk63_jerk_v083_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_jk126_jerk_v084_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk5_jerk_v085_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk10_jerk_v086_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk21_jerk_v087_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk42_jerk_v088_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk63_jerk_v089_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_jk126_jerk_v090_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk5_jerk_v091_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk10_jerk_v092_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk21_jerk_v093_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk42_jerk_v094_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk63_jerk_v095_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_jk126_jerk_v096_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk5_jerk_v097_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk10_jerk_v098_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk21_jerk_v099_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk42_jerk_v100_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk63_jerk_v101_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_jk126_jerk_v102_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk5_jerk_v103_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk10_jerk_v104_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk21_jerk_v105_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk42_jerk_v106_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk63_jerk_v107_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_jk126_jerk_v108_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk5_jerk_v109_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk10_jerk_v110_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk21_jerk_v111_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk42_jerk_v112_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk63_jerk_v113_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_jk126_jerk_v114_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk5_jerk_v115_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk10_jerk_v116_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk21_jerk_v117_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk42_jerk_v118_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk63_jerk_v119_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_jk126_jerk_v120_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk5_jerk_v121_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk10_jerk_v122_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk21_jerk_v123_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk42_jerk_v124_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk63_jerk_v125_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_jk126_jerk_v126_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk5_jerk_v127_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk10_jerk_v128_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk21_jerk_v129_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk42_jerk_v130_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk63_jerk_v131_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_jk126_jerk_v132_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk5_jerk_v133_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk10_jerk_v134_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk21_jerk_v135_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk42_jerk_v136_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk63_jerk_v137_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_jk126_jerk_v138_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk5_jerk_v139_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk10_jerk_v140_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk21_jerk_v141_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk42_jerk_v142_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk63_jerk_v143_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_jk126_jerk_v144_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk5_jerk_v145_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk10_jerk_v146_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk21_jerk_v147_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk42_jerk_v148_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk63_jerk_v149_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_jk126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_COMMODITY_BOTTOM_TO_TOP_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_bottom_signature", "_f48_margin_bottom", "_f48_cycle_bottom_score",)
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
    print(f"OK {__file__}: {n_features} features pass")
