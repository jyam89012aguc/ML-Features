"""Family f053 - EBITDA profitability (Margins and Profitability) | Sharadar tables: SF1 | fields: ebitda, ebitdamargin, revenue | 3rd derivatives 001-150"""
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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _ebitda_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ebitda_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ebitda_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ebitda
def em_f053_ebitda_margin_raw_21d_accel_v001_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ebitda
def em_f053_ebitda_margin_raw_21d_accel_v002_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ebitda
def em_f053_ebitda_margin_raw_21d_accel_v003_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ebitda
def em_f053_ebitda_margin_raw_63d_accel_v004_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ebitda
def em_f053_ebitda_margin_raw_63d_accel_v005_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ebitda
def em_f053_ebitda_margin_raw_63d_accel_v006_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ebitda
def em_f053_ebitda_margin_raw_126d_accel_v007_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ebitda
def em_f053_ebitda_margin_raw_126d_accel_v008_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ebitda
def em_f053_ebitda_margin_raw_126d_accel_v009_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ebitda
def em_f053_ebitda_margin_raw_252d_accel_v010_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ebitda
def em_f053_ebitda_margin_raw_252d_accel_v011_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ebitda
def em_f053_ebitda_margin_raw_252d_accel_v012_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ebitda
def em_f053_ebitda_margin_raw_504d_accel_v013_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ebitda
def em_f053_ebitda_margin_raw_504d_accel_v014_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ebitda
def em_f053_ebitda_margin_raw_504d_accel_v015_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ebitda
def em_f053_ebitda_margin_log_21d_accel_v016_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ebitda
def em_f053_ebitda_margin_log_21d_accel_v017_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ebitda
def em_f053_ebitda_margin_log_21d_accel_v018_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ebitda
def em_f053_ebitda_margin_log_63d_accel_v019_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ebitda
def em_f053_ebitda_margin_log_63d_accel_v020_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ebitda
def em_f053_ebitda_margin_log_63d_accel_v021_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ebitda
def em_f053_ebitda_margin_log_126d_accel_v022_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ebitda
def em_f053_ebitda_margin_log_126d_accel_v023_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ebitda
def em_f053_ebitda_margin_log_126d_accel_v024_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ebitda
def em_f053_ebitda_margin_log_252d_accel_v025_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ebitda
def em_f053_ebitda_margin_log_252d_accel_v026_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ebitda
def em_f053_ebitda_margin_log_252d_accel_v027_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ebitda
def em_f053_ebitda_margin_log_504d_accel_v028_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ebitda
def em_f053_ebitda_margin_log_504d_accel_v029_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ebitda
def em_f053_ebitda_margin_log_504d_accel_v030_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ebitda
def em_f053_ebitda_margin_pershare_21d_accel_v031_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ebitda
def em_f053_ebitda_margin_pershare_21d_accel_v032_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ebitda
def em_f053_ebitda_margin_pershare_21d_accel_v033_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ebitda
def em_f053_ebitda_margin_pershare_63d_accel_v034_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ebitda
def em_f053_ebitda_margin_pershare_63d_accel_v035_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ebitda
def em_f053_ebitda_margin_pershare_63d_accel_v036_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ebitda
def em_f053_ebitda_margin_pershare_126d_accel_v037_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ebitda
def em_f053_ebitda_margin_pershare_126d_accel_v038_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ebitda
def em_f053_ebitda_margin_pershare_126d_accel_v039_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ebitda
def em_f053_ebitda_margin_pershare_252d_accel_v040_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ebitda
def em_f053_ebitda_margin_pershare_252d_accel_v041_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ebitda
def em_f053_ebitda_margin_pershare_252d_accel_v042_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ebitda
def em_f053_ebitda_margin_pershare_504d_accel_v043_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ebitda
def em_f053_ebitda_margin_pershare_504d_accel_v044_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ebitda
def em_f053_ebitda_margin_pershare_504d_accel_v045_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_21d_accel_v046_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_21d_accel_v047_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_21d_accel_v048_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_63d_accel_v049_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_63d_accel_v050_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_63d_accel_v051_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_126d_accel_v052_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_126d_accel_v053_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_126d_accel_v054_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_252d_accel_v055_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_252d_accel_v056_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_252d_accel_v057_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_504d_accel_v058_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_504d_accel_v059_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ebitdamargin ebitda
def em_f053_ebitda_margin_per_ebitdamargin_504d_accel_v060_signal(ebitda, ebitdamargin):
    base = _mean(_ebitda_margin_scaled(ebitda, ebitdamargin), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_21d_accel_v061_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_21d_accel_v062_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_21d_accel_v063_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_63d_accel_v064_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_63d_accel_v065_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_63d_accel_v066_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_126d_accel_v067_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_126d_accel_v068_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_126d_accel_v069_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_252d_accel_v070_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_252d_accel_v071_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_252d_accel_v072_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_504d_accel_v073_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_504d_accel_v074_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_revenue ebitda
def em_f053_ebitda_margin_per_revenue_504d_accel_v075_signal(ebitda, revenue):
    base = _mean(_ebitda_margin_scaled(ebitda, revenue), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ebitda
def em_f053_ebitda_margin_per_assets_21d_accel_v076_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ebitda
def em_f053_ebitda_margin_per_assets_21d_accel_v077_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ebitda
def em_f053_ebitda_margin_per_assets_21d_accel_v078_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ebitda
def em_f053_ebitda_margin_per_assets_63d_accel_v079_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ebitda
def em_f053_ebitda_margin_per_assets_63d_accel_v080_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ebitda
def em_f053_ebitda_margin_per_assets_63d_accel_v081_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ebitda
def em_f053_ebitda_margin_per_assets_126d_accel_v082_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ebitda
def em_f053_ebitda_margin_per_assets_126d_accel_v083_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ebitda
def em_f053_ebitda_margin_per_assets_126d_accel_v084_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ebitda
def em_f053_ebitda_margin_per_assets_252d_accel_v085_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ebitda
def em_f053_ebitda_margin_per_assets_252d_accel_v086_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ebitda
def em_f053_ebitda_margin_per_assets_252d_accel_v087_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ebitda
def em_f053_ebitda_margin_per_assets_504d_accel_v088_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ebitda
def em_f053_ebitda_margin_per_assets_504d_accel_v089_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ebitda
def em_f053_ebitda_margin_per_assets_504d_accel_v090_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ebitda
def em_f053_ebitda_margin_std_21d_accel_v091_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ebitda
def em_f053_ebitda_margin_std_21d_accel_v092_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ebitda
def em_f053_ebitda_margin_std_21d_accel_v093_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ebitda
def em_f053_ebitda_margin_std_63d_accel_v094_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ebitda
def em_f053_ebitda_margin_std_63d_accel_v095_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ebitda
def em_f053_ebitda_margin_std_63d_accel_v096_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ebitda
def em_f053_ebitda_margin_std_126d_accel_v097_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ebitda
def em_f053_ebitda_margin_std_126d_accel_v098_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ebitda
def em_f053_ebitda_margin_std_126d_accel_v099_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ebitda
def em_f053_ebitda_margin_std_252d_accel_v100_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ebitda
def em_f053_ebitda_margin_std_252d_accel_v101_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ebitda
def em_f053_ebitda_margin_std_252d_accel_v102_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ebitda
def em_f053_ebitda_margin_std_504d_accel_v103_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ebitda
def em_f053_ebitda_margin_std_504d_accel_v104_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ebitda
def em_f053_ebitda_margin_std_504d_accel_v105_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ebitda
def em_f053_ebitda_margin_ewm_21d_accel_v106_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ebitda
def em_f053_ebitda_margin_ewm_21d_accel_v107_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ebitda
def em_f053_ebitda_margin_ewm_21d_accel_v108_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ebitda
def em_f053_ebitda_margin_ewm_63d_accel_v109_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ebitda
def em_f053_ebitda_margin_ewm_63d_accel_v110_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ebitda
def em_f053_ebitda_margin_ewm_63d_accel_v111_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ebitda
def em_f053_ebitda_margin_ewm_126d_accel_v112_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ebitda
def em_f053_ebitda_margin_ewm_126d_accel_v113_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ebitda
def em_f053_ebitda_margin_ewm_126d_accel_v114_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ebitda
def em_f053_ebitda_margin_ewm_252d_accel_v115_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ebitda
def em_f053_ebitda_margin_ewm_252d_accel_v116_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ebitda
def em_f053_ebitda_margin_ewm_252d_accel_v117_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ebitda
def em_f053_ebitda_margin_ewm_504d_accel_v118_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ebitda
def em_f053_ebitda_margin_ewm_504d_accel_v119_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ebitda
def em_f053_ebitda_margin_ewm_504d_accel_v120_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ebitda
def em_f053_ebitda_margin_sq_21d_accel_v121_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ebitda
def em_f053_ebitda_margin_sq_21d_accel_v122_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ebitda
def em_f053_ebitda_margin_sq_21d_accel_v123_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ebitda
def em_f053_ebitda_margin_sq_63d_accel_v124_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ebitda
def em_f053_ebitda_margin_sq_63d_accel_v125_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ebitda
def em_f053_ebitda_margin_sq_63d_accel_v126_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ebitda
def em_f053_ebitda_margin_sq_126d_accel_v127_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ebitda
def em_f053_ebitda_margin_sq_126d_accel_v128_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ebitda
def em_f053_ebitda_margin_sq_126d_accel_v129_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ebitda
def em_f053_ebitda_margin_sq_252d_accel_v130_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ebitda
def em_f053_ebitda_margin_sq_252d_accel_v131_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ebitda
def em_f053_ebitda_margin_sq_252d_accel_v132_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ebitda
def em_f053_ebitda_margin_sq_504d_accel_v133_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ebitda
def em_f053_ebitda_margin_sq_504d_accel_v134_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ebitda
def em_f053_ebitda_margin_sq_504d_accel_v135_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ebitda
def em_f053_ebitda_margin_z_21d_accel_v136_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ebitda
def em_f053_ebitda_margin_z_21d_accel_v137_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ebitda
def em_f053_ebitda_margin_z_21d_accel_v138_signal(ebitda):
    base = _z(ebitda, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ebitda
def em_f053_ebitda_margin_z_63d_accel_v139_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ebitda
def em_f053_ebitda_margin_z_63d_accel_v140_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ebitda
def em_f053_ebitda_margin_z_63d_accel_v141_signal(ebitda):
    base = _z(ebitda, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ebitda
def em_f053_ebitda_margin_z_126d_accel_v142_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ebitda
def em_f053_ebitda_margin_z_126d_accel_v143_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ebitda
def em_f053_ebitda_margin_z_126d_accel_v144_signal(ebitda):
    base = _z(ebitda, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ebitda
def em_f053_ebitda_margin_z_252d_accel_v145_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ebitda
def em_f053_ebitda_margin_z_252d_accel_v146_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ebitda
def em_f053_ebitda_margin_z_252d_accel_v147_signal(ebitda):
    base = _z(ebitda, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ebitda
def em_f053_ebitda_margin_z_504d_accel_v148_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ebitda
def em_f053_ebitda_margin_z_504d_accel_v149_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ebitda
def em_f053_ebitda_margin_z_504d_accel_v150_signal(ebitda):
    base = _z(ebitda, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
