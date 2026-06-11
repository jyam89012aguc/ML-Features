"""Family f005 - Current liquidity coverage (Liquidity and Runway) | Sharadar tables: SF1 | fields: currentratio, assetsc, liabilitiesc, cashneq | 2nd derivatives 001-150"""
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
def _current_liquidity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _current_liquidity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _current_liquidity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw currentratio
def cl_f005_current_liquidity_raw_21d_slope_v001_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw currentratio
def cl_f005_current_liquidity_raw_21d_slope_v002_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw currentratio
def cl_f005_current_liquidity_raw_21d_slope_v003_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw currentratio
def cl_f005_current_liquidity_raw_63d_slope_v004_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw currentratio
def cl_f005_current_liquidity_raw_63d_slope_v005_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw currentratio
def cl_f005_current_liquidity_raw_63d_slope_v006_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw currentratio
def cl_f005_current_liquidity_raw_126d_slope_v007_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw currentratio
def cl_f005_current_liquidity_raw_126d_slope_v008_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw currentratio
def cl_f005_current_liquidity_raw_126d_slope_v009_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw currentratio
def cl_f005_current_liquidity_raw_252d_slope_v010_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw currentratio
def cl_f005_current_liquidity_raw_252d_slope_v011_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw currentratio
def cl_f005_current_liquidity_raw_252d_slope_v012_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw currentratio
def cl_f005_current_liquidity_raw_504d_slope_v013_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw currentratio
def cl_f005_current_liquidity_raw_504d_slope_v014_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw currentratio
def cl_f005_current_liquidity_raw_504d_slope_v015_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log currentratio
def cl_f005_current_liquidity_log_21d_slope_v016_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log currentratio
def cl_f005_current_liquidity_log_21d_slope_v017_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log currentratio
def cl_f005_current_liquidity_log_21d_slope_v018_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log currentratio
def cl_f005_current_liquidity_log_63d_slope_v019_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log currentratio
def cl_f005_current_liquidity_log_63d_slope_v020_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log currentratio
def cl_f005_current_liquidity_log_63d_slope_v021_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log currentratio
def cl_f005_current_liquidity_log_126d_slope_v022_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log currentratio
def cl_f005_current_liquidity_log_126d_slope_v023_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log currentratio
def cl_f005_current_liquidity_log_126d_slope_v024_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log currentratio
def cl_f005_current_liquidity_log_252d_slope_v025_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log currentratio
def cl_f005_current_liquidity_log_252d_slope_v026_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log currentratio
def cl_f005_current_liquidity_log_252d_slope_v027_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log currentratio
def cl_f005_current_liquidity_log_504d_slope_v028_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log currentratio
def cl_f005_current_liquidity_log_504d_slope_v029_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log currentratio
def cl_f005_current_liquidity_log_504d_slope_v030_signal(currentratio, closeadj):
    base = _mean(_current_liquidity_log(currentratio), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare currentratio
def cl_f005_current_liquidity_pershare_21d_slope_v031_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare currentratio
def cl_f005_current_liquidity_pershare_21d_slope_v032_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare currentratio
def cl_f005_current_liquidity_pershare_21d_slope_v033_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare currentratio
def cl_f005_current_liquidity_pershare_63d_slope_v034_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare currentratio
def cl_f005_current_liquidity_pershare_63d_slope_v035_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare currentratio
def cl_f005_current_liquidity_pershare_63d_slope_v036_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare currentratio
def cl_f005_current_liquidity_pershare_126d_slope_v037_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare currentratio
def cl_f005_current_liquidity_pershare_126d_slope_v038_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare currentratio
def cl_f005_current_liquidity_pershare_126d_slope_v039_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare currentratio
def cl_f005_current_liquidity_pershare_252d_slope_v040_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare currentratio
def cl_f005_current_liquidity_pershare_252d_slope_v041_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare currentratio
def cl_f005_current_liquidity_pershare_252d_slope_v042_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare currentratio
def cl_f005_current_liquidity_pershare_504d_slope_v043_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare currentratio
def cl_f005_current_liquidity_pershare_504d_slope_v044_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare currentratio
def cl_f005_current_liquidity_pershare_504d_slope_v045_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_liquidity_per_share(currentratio, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_21d_slope_v046_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_21d_slope_v047_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_21d_slope_v048_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_63d_slope_v049_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_63d_slope_v050_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_63d_slope_v051_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_126d_slope_v052_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_126d_slope_v053_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_126d_slope_v054_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_252d_slope_v055_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_252d_slope_v056_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_252d_slope_v057_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_504d_slope_v058_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_504d_slope_v059_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assetsc currentratio
def cl_f005_current_liquidity_per_assetsc_504d_slope_v060_signal(currentratio, assetsc):
    base = _mean(_current_liquidity_scaled(currentratio, assetsc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_21d_slope_v061_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_21d_slope_v062_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_21d_slope_v063_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_63d_slope_v064_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_63d_slope_v065_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_63d_slope_v066_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_126d_slope_v067_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_126d_slope_v068_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_126d_slope_v069_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_252d_slope_v070_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_252d_slope_v071_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_252d_slope_v072_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_504d_slope_v073_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_504d_slope_v074_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_liabilitiesc currentratio
def cl_f005_current_liquidity_per_liabilitiesc_504d_slope_v075_signal(currentratio, liabilitiesc):
    base = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_21d_slope_v076_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_21d_slope_v077_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_21d_slope_v078_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_63d_slope_v079_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_63d_slope_v080_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_63d_slope_v081_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_126d_slope_v082_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_126d_slope_v083_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_126d_slope_v084_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_252d_slope_v085_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_252d_slope_v086_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_252d_slope_v087_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_504d_slope_v088_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_504d_slope_v089_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_cashneq currentratio
def cl_f005_current_liquidity_per_cashneq_504d_slope_v090_signal(currentratio, cashneq):
    base = _mean(_current_liquidity_scaled(currentratio, cashneq), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std currentratio
def cl_f005_current_liquidity_std_21d_slope_v091_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std currentratio
def cl_f005_current_liquidity_std_21d_slope_v092_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std currentratio
def cl_f005_current_liquidity_std_21d_slope_v093_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std currentratio
def cl_f005_current_liquidity_std_63d_slope_v094_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std currentratio
def cl_f005_current_liquidity_std_63d_slope_v095_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std currentratio
def cl_f005_current_liquidity_std_63d_slope_v096_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std currentratio
def cl_f005_current_liquidity_std_126d_slope_v097_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std currentratio
def cl_f005_current_liquidity_std_126d_slope_v098_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std currentratio
def cl_f005_current_liquidity_std_126d_slope_v099_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std currentratio
def cl_f005_current_liquidity_std_252d_slope_v100_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std currentratio
def cl_f005_current_liquidity_std_252d_slope_v101_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std currentratio
def cl_f005_current_liquidity_std_252d_slope_v102_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std currentratio
def cl_f005_current_liquidity_std_504d_slope_v103_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std currentratio
def cl_f005_current_liquidity_std_504d_slope_v104_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std currentratio
def cl_f005_current_liquidity_std_504d_slope_v105_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm currentratio
def cl_f005_current_liquidity_ewm_21d_slope_v106_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm currentratio
def cl_f005_current_liquidity_ewm_21d_slope_v107_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm currentratio
def cl_f005_current_liquidity_ewm_21d_slope_v108_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm currentratio
def cl_f005_current_liquidity_ewm_63d_slope_v109_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm currentratio
def cl_f005_current_liquidity_ewm_63d_slope_v110_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm currentratio
def cl_f005_current_liquidity_ewm_63d_slope_v111_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm currentratio
def cl_f005_current_liquidity_ewm_126d_slope_v112_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm currentratio
def cl_f005_current_liquidity_ewm_126d_slope_v113_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm currentratio
def cl_f005_current_liquidity_ewm_126d_slope_v114_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm currentratio
def cl_f005_current_liquidity_ewm_252d_slope_v115_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm currentratio
def cl_f005_current_liquidity_ewm_252d_slope_v116_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm currentratio
def cl_f005_current_liquidity_ewm_252d_slope_v117_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm currentratio
def cl_f005_current_liquidity_ewm_504d_slope_v118_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm currentratio
def cl_f005_current_liquidity_ewm_504d_slope_v119_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm currentratio
def cl_f005_current_liquidity_ewm_504d_slope_v120_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq currentratio
def cl_f005_current_liquidity_sq_21d_slope_v121_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq currentratio
def cl_f005_current_liquidity_sq_21d_slope_v122_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq currentratio
def cl_f005_current_liquidity_sq_21d_slope_v123_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq currentratio
def cl_f005_current_liquidity_sq_63d_slope_v124_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq currentratio
def cl_f005_current_liquidity_sq_63d_slope_v125_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq currentratio
def cl_f005_current_liquidity_sq_63d_slope_v126_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq currentratio
def cl_f005_current_liquidity_sq_126d_slope_v127_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq currentratio
def cl_f005_current_liquidity_sq_126d_slope_v128_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq currentratio
def cl_f005_current_liquidity_sq_126d_slope_v129_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq currentratio
def cl_f005_current_liquidity_sq_252d_slope_v130_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq currentratio
def cl_f005_current_liquidity_sq_252d_slope_v131_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq currentratio
def cl_f005_current_liquidity_sq_252d_slope_v132_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq currentratio
def cl_f005_current_liquidity_sq_504d_slope_v133_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq currentratio
def cl_f005_current_liquidity_sq_504d_slope_v134_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq currentratio
def cl_f005_current_liquidity_sq_504d_slope_v135_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z currentratio
def cl_f005_current_liquidity_z_21d_slope_v136_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z currentratio
def cl_f005_current_liquidity_z_21d_slope_v137_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z currentratio
def cl_f005_current_liquidity_z_21d_slope_v138_signal(currentratio):
    base = _z(currentratio, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z currentratio
def cl_f005_current_liquidity_z_63d_slope_v139_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z currentratio
def cl_f005_current_liquidity_z_63d_slope_v140_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z currentratio
def cl_f005_current_liquidity_z_63d_slope_v141_signal(currentratio):
    base = _z(currentratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z currentratio
def cl_f005_current_liquidity_z_126d_slope_v142_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z currentratio
def cl_f005_current_liquidity_z_126d_slope_v143_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z currentratio
def cl_f005_current_liquidity_z_126d_slope_v144_signal(currentratio):
    base = _z(currentratio, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z currentratio
def cl_f005_current_liquidity_z_252d_slope_v145_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z currentratio
def cl_f005_current_liquidity_z_252d_slope_v146_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z currentratio
def cl_f005_current_liquidity_z_252d_slope_v147_signal(currentratio):
    base = _z(currentratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z currentratio
def cl_f005_current_liquidity_z_504d_slope_v148_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z currentratio
def cl_f005_current_liquidity_z_504d_slope_v149_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z currentratio
def cl_f005_current_liquidity_z_504d_slope_v150_signal(currentratio):
    base = _z(currentratio, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
