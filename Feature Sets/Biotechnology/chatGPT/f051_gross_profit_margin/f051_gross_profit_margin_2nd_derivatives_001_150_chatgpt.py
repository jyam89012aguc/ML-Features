"""Family f051 - Gross profit and gross margin (Margins and Profitability) | Sharadar tables: SF1 | fields: gp, grossmargin, revenue | 2nd derivatives 001-150"""
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
def _gross_profit_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _gross_profit_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _gross_profit_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw gp
def gpm_f051_gross_profit_margin_raw_21d_slope_v001_signal(gp, closeadj):
    base = _mean(gp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw gp
def gpm_f051_gross_profit_margin_raw_21d_slope_v002_signal(gp, closeadj):
    base = _mean(gp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw gp
def gpm_f051_gross_profit_margin_raw_21d_slope_v003_signal(gp, closeadj):
    base = _mean(gp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw gp
def gpm_f051_gross_profit_margin_raw_63d_slope_v004_signal(gp, closeadj):
    base = _mean(gp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw gp
def gpm_f051_gross_profit_margin_raw_63d_slope_v005_signal(gp, closeadj):
    base = _mean(gp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw gp
def gpm_f051_gross_profit_margin_raw_63d_slope_v006_signal(gp, closeadj):
    base = _mean(gp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw gp
def gpm_f051_gross_profit_margin_raw_126d_slope_v007_signal(gp, closeadj):
    base = _mean(gp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw gp
def gpm_f051_gross_profit_margin_raw_126d_slope_v008_signal(gp, closeadj):
    base = _mean(gp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw gp
def gpm_f051_gross_profit_margin_raw_126d_slope_v009_signal(gp, closeadj):
    base = _mean(gp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw gp
def gpm_f051_gross_profit_margin_raw_252d_slope_v010_signal(gp, closeadj):
    base = _mean(gp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw gp
def gpm_f051_gross_profit_margin_raw_252d_slope_v011_signal(gp, closeadj):
    base = _mean(gp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw gp
def gpm_f051_gross_profit_margin_raw_252d_slope_v012_signal(gp, closeadj):
    base = _mean(gp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw gp
def gpm_f051_gross_profit_margin_raw_504d_slope_v013_signal(gp, closeadj):
    base = _mean(gp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw gp
def gpm_f051_gross_profit_margin_raw_504d_slope_v014_signal(gp, closeadj):
    base = _mean(gp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw gp
def gpm_f051_gross_profit_margin_raw_504d_slope_v015_signal(gp, closeadj):
    base = _mean(gp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log gp
def gpm_f051_gross_profit_margin_log_21d_slope_v016_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log gp
def gpm_f051_gross_profit_margin_log_21d_slope_v017_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log gp
def gpm_f051_gross_profit_margin_log_21d_slope_v018_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log gp
def gpm_f051_gross_profit_margin_log_63d_slope_v019_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log gp
def gpm_f051_gross_profit_margin_log_63d_slope_v020_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log gp
def gpm_f051_gross_profit_margin_log_63d_slope_v021_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log gp
def gpm_f051_gross_profit_margin_log_126d_slope_v022_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log gp
def gpm_f051_gross_profit_margin_log_126d_slope_v023_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log gp
def gpm_f051_gross_profit_margin_log_126d_slope_v024_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log gp
def gpm_f051_gross_profit_margin_log_252d_slope_v025_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log gp
def gpm_f051_gross_profit_margin_log_252d_slope_v026_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log gp
def gpm_f051_gross_profit_margin_log_252d_slope_v027_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log gp
def gpm_f051_gross_profit_margin_log_504d_slope_v028_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log gp
def gpm_f051_gross_profit_margin_log_504d_slope_v029_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log gp
def gpm_f051_gross_profit_margin_log_504d_slope_v030_signal(gp, closeadj):
    base = _mean(_gross_profit_margin_log(gp), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare gp
def gpm_f051_gross_profit_margin_pershare_21d_slope_v031_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare gp
def gpm_f051_gross_profit_margin_pershare_21d_slope_v032_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare gp
def gpm_f051_gross_profit_margin_pershare_21d_slope_v033_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare gp
def gpm_f051_gross_profit_margin_pershare_63d_slope_v034_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare gp
def gpm_f051_gross_profit_margin_pershare_63d_slope_v035_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare gp
def gpm_f051_gross_profit_margin_pershare_63d_slope_v036_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare gp
def gpm_f051_gross_profit_margin_pershare_126d_slope_v037_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare gp
def gpm_f051_gross_profit_margin_pershare_126d_slope_v038_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare gp
def gpm_f051_gross_profit_margin_pershare_126d_slope_v039_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare gp
def gpm_f051_gross_profit_margin_pershare_252d_slope_v040_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare gp
def gpm_f051_gross_profit_margin_pershare_252d_slope_v041_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare gp
def gpm_f051_gross_profit_margin_pershare_252d_slope_v042_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare gp
def gpm_f051_gross_profit_margin_pershare_504d_slope_v043_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare gp
def gpm_f051_gross_profit_margin_pershare_504d_slope_v044_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare gp
def gpm_f051_gross_profit_margin_pershare_504d_slope_v045_signal(gp, sharesbas, closeadj):
    base = _mean(_gross_profit_margin_per_share(gp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_21d_slope_v046_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_21d_slope_v047_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_21d_slope_v048_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_63d_slope_v049_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_63d_slope_v050_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_63d_slope_v051_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_126d_slope_v052_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_126d_slope_v053_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_126d_slope_v054_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_252d_slope_v055_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_252d_slope_v056_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_252d_slope_v057_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_504d_slope_v058_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_504d_slope_v059_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_grossmargin gp
def gpm_f051_gross_profit_margin_per_grossmargin_504d_slope_v060_signal(gp, grossmargin):
    base = _mean(_gross_profit_margin_scaled(gp, grossmargin), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_21d_slope_v061_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_21d_slope_v062_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_21d_slope_v063_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_63d_slope_v064_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_63d_slope_v065_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_63d_slope_v066_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_126d_slope_v067_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_126d_slope_v068_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_126d_slope_v069_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_252d_slope_v070_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_252d_slope_v071_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_252d_slope_v072_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_504d_slope_v073_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_504d_slope_v074_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue gp
def gpm_f051_gross_profit_margin_per_revenue_504d_slope_v075_signal(gp, revenue):
    base = _mean(_gross_profit_margin_scaled(gp, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_21d_slope_v076_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_21d_slope_v077_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_21d_slope_v078_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_63d_slope_v079_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_63d_slope_v080_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_63d_slope_v081_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_126d_slope_v082_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_126d_slope_v083_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_126d_slope_v084_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_252d_slope_v085_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_252d_slope_v086_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_252d_slope_v087_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_504d_slope_v088_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_504d_slope_v089_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets gp
def gpm_f051_gross_profit_margin_per_assets_504d_slope_v090_signal(gp, assets):
    base = _mean(_gross_profit_margin_scaled(gp, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std gp
def gpm_f051_gross_profit_margin_std_21d_slope_v091_signal(gp, closeadj):
    base = _std(gp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std gp
def gpm_f051_gross_profit_margin_std_21d_slope_v092_signal(gp, closeadj):
    base = _std(gp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std gp
def gpm_f051_gross_profit_margin_std_21d_slope_v093_signal(gp, closeadj):
    base = _std(gp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std gp
def gpm_f051_gross_profit_margin_std_63d_slope_v094_signal(gp, closeadj):
    base = _std(gp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std gp
def gpm_f051_gross_profit_margin_std_63d_slope_v095_signal(gp, closeadj):
    base = _std(gp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std gp
def gpm_f051_gross_profit_margin_std_63d_slope_v096_signal(gp, closeadj):
    base = _std(gp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std gp
def gpm_f051_gross_profit_margin_std_126d_slope_v097_signal(gp, closeadj):
    base = _std(gp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std gp
def gpm_f051_gross_profit_margin_std_126d_slope_v098_signal(gp, closeadj):
    base = _std(gp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std gp
def gpm_f051_gross_profit_margin_std_126d_slope_v099_signal(gp, closeadj):
    base = _std(gp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std gp
def gpm_f051_gross_profit_margin_std_252d_slope_v100_signal(gp, closeadj):
    base = _std(gp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std gp
def gpm_f051_gross_profit_margin_std_252d_slope_v101_signal(gp, closeadj):
    base = _std(gp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std gp
def gpm_f051_gross_profit_margin_std_252d_slope_v102_signal(gp, closeadj):
    base = _std(gp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std gp
def gpm_f051_gross_profit_margin_std_504d_slope_v103_signal(gp, closeadj):
    base = _std(gp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std gp
def gpm_f051_gross_profit_margin_std_504d_slope_v104_signal(gp, closeadj):
    base = _std(gp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std gp
def gpm_f051_gross_profit_margin_std_504d_slope_v105_signal(gp, closeadj):
    base = _std(gp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm gp
def gpm_f051_gross_profit_margin_ewm_21d_slope_v106_signal(gp, closeadj):
    base = gp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm gp
def gpm_f051_gross_profit_margin_ewm_21d_slope_v107_signal(gp, closeadj):
    base = gp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm gp
def gpm_f051_gross_profit_margin_ewm_21d_slope_v108_signal(gp, closeadj):
    base = gp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm gp
def gpm_f051_gross_profit_margin_ewm_63d_slope_v109_signal(gp, closeadj):
    base = gp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm gp
def gpm_f051_gross_profit_margin_ewm_63d_slope_v110_signal(gp, closeadj):
    base = gp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm gp
def gpm_f051_gross_profit_margin_ewm_63d_slope_v111_signal(gp, closeadj):
    base = gp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm gp
def gpm_f051_gross_profit_margin_ewm_126d_slope_v112_signal(gp, closeadj):
    base = gp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm gp
def gpm_f051_gross_profit_margin_ewm_126d_slope_v113_signal(gp, closeadj):
    base = gp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm gp
def gpm_f051_gross_profit_margin_ewm_126d_slope_v114_signal(gp, closeadj):
    base = gp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm gp
def gpm_f051_gross_profit_margin_ewm_252d_slope_v115_signal(gp, closeadj):
    base = gp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm gp
def gpm_f051_gross_profit_margin_ewm_252d_slope_v116_signal(gp, closeadj):
    base = gp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm gp
def gpm_f051_gross_profit_margin_ewm_252d_slope_v117_signal(gp, closeadj):
    base = gp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm gp
def gpm_f051_gross_profit_margin_ewm_504d_slope_v118_signal(gp, closeadj):
    base = gp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm gp
def gpm_f051_gross_profit_margin_ewm_504d_slope_v119_signal(gp, closeadj):
    base = gp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm gp
def gpm_f051_gross_profit_margin_ewm_504d_slope_v120_signal(gp, closeadj):
    base = gp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq gp
def gpm_f051_gross_profit_margin_sq_21d_slope_v121_signal(gp, closeadj):
    base = _mean(gp * gp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq gp
def gpm_f051_gross_profit_margin_sq_21d_slope_v122_signal(gp, closeadj):
    base = _mean(gp * gp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq gp
def gpm_f051_gross_profit_margin_sq_21d_slope_v123_signal(gp, closeadj):
    base = _mean(gp * gp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq gp
def gpm_f051_gross_profit_margin_sq_63d_slope_v124_signal(gp, closeadj):
    base = _mean(gp * gp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq gp
def gpm_f051_gross_profit_margin_sq_63d_slope_v125_signal(gp, closeadj):
    base = _mean(gp * gp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq gp
def gpm_f051_gross_profit_margin_sq_63d_slope_v126_signal(gp, closeadj):
    base = _mean(gp * gp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq gp
def gpm_f051_gross_profit_margin_sq_126d_slope_v127_signal(gp, closeadj):
    base = _mean(gp * gp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq gp
def gpm_f051_gross_profit_margin_sq_126d_slope_v128_signal(gp, closeadj):
    base = _mean(gp * gp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq gp
def gpm_f051_gross_profit_margin_sq_126d_slope_v129_signal(gp, closeadj):
    base = _mean(gp * gp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq gp
def gpm_f051_gross_profit_margin_sq_252d_slope_v130_signal(gp, closeadj):
    base = _mean(gp * gp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq gp
def gpm_f051_gross_profit_margin_sq_252d_slope_v131_signal(gp, closeadj):
    base = _mean(gp * gp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq gp
def gpm_f051_gross_profit_margin_sq_252d_slope_v132_signal(gp, closeadj):
    base = _mean(gp * gp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq gp
def gpm_f051_gross_profit_margin_sq_504d_slope_v133_signal(gp, closeadj):
    base = _mean(gp * gp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq gp
def gpm_f051_gross_profit_margin_sq_504d_slope_v134_signal(gp, closeadj):
    base = _mean(gp * gp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq gp
def gpm_f051_gross_profit_margin_sq_504d_slope_v135_signal(gp, closeadj):
    base = _mean(gp * gp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z gp
def gpm_f051_gross_profit_margin_z_21d_slope_v136_signal(gp):
    base = _z(gp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z gp
def gpm_f051_gross_profit_margin_z_21d_slope_v137_signal(gp):
    base = _z(gp, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z gp
def gpm_f051_gross_profit_margin_z_21d_slope_v138_signal(gp):
    base = _z(gp, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z gp
def gpm_f051_gross_profit_margin_z_63d_slope_v139_signal(gp):
    base = _z(gp, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z gp
def gpm_f051_gross_profit_margin_z_63d_slope_v140_signal(gp):
    base = _z(gp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z gp
def gpm_f051_gross_profit_margin_z_63d_slope_v141_signal(gp):
    base = _z(gp, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z gp
def gpm_f051_gross_profit_margin_z_126d_slope_v142_signal(gp):
    base = _z(gp, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z gp
def gpm_f051_gross_profit_margin_z_126d_slope_v143_signal(gp):
    base = _z(gp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z gp
def gpm_f051_gross_profit_margin_z_126d_slope_v144_signal(gp):
    base = _z(gp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z gp
def gpm_f051_gross_profit_margin_z_252d_slope_v145_signal(gp):
    base = _z(gp, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z gp
def gpm_f051_gross_profit_margin_z_252d_slope_v146_signal(gp):
    base = _z(gp, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z gp
def gpm_f051_gross_profit_margin_z_252d_slope_v147_signal(gp):
    base = _z(gp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z gp
def gpm_f051_gross_profit_margin_z_504d_slope_v148_signal(gp):
    base = _z(gp, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z gp
def gpm_f051_gross_profit_margin_z_504d_slope_v149_signal(gp):
    base = _z(gp, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z gp
def gpm_f051_gross_profit_margin_z_504d_slope_v150_signal(gp):
    base = _z(gp, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
