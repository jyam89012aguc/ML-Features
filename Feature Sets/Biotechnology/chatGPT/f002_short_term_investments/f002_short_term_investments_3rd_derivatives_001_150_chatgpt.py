"""Family f002 - SF1 liquid securities buffer (Liquidity and Runway) | Sharadar tables: SF1 | fields: investmentsc, investments, cashneq, assets | 3rd derivatives 001-150"""
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
def _short_term_investments_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _short_term_investments_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _short_term_investments_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_accel_v001_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_accel_v002_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_accel_v003_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_accel_v004_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_accel_v005_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_accel_v006_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_accel_v007_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_accel_v008_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_accel_v009_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_accel_v010_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_accel_v011_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_accel_v012_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_accel_v013_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_accel_v014_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_accel_v015_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_accel_v016_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_accel_v017_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_accel_v018_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_accel_v019_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_accel_v020_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_accel_v021_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_accel_v022_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_accel_v023_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_accel_v024_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_accel_v025_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_accel_v026_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_accel_v027_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_accel_v028_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_accel_v029_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_accel_v030_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_accel_v031_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_accel_v032_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_accel_v033_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_accel_v034_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_accel_v035_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_accel_v036_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_accel_v037_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_accel_v038_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_accel_v039_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_accel_v040_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_accel_v041_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_accel_v042_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_accel_v043_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_accel_v044_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_accel_v045_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_accel_v046_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_accel_v047_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_accel_v048_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_accel_v049_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_accel_v050_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_accel_v051_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_accel_v052_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_accel_v053_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_accel_v054_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_accel_v055_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_accel_v056_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_accel_v057_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_accel_v058_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_accel_v059_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_accel_v060_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_accel_v061_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_accel_v062_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_accel_v063_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_accel_v064_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_accel_v065_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_accel_v066_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_accel_v067_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_accel_v068_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_accel_v069_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_accel_v070_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_accel_v071_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_accel_v072_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_accel_v073_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_accel_v074_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_accel_v075_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_accel_v076_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_accel_v077_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_accel_v078_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_accel_v079_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_accel_v080_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_accel_v081_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_accel_v082_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_accel_v083_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_accel_v084_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_accel_v085_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_accel_v086_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_accel_v087_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_accel_v088_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_accel_v089_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_accel_v090_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_accel_v091_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_accel_v092_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_accel_v093_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_accel_v094_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_accel_v095_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_accel_v096_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_accel_v097_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_accel_v098_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_accel_v099_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_accel_v100_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_accel_v101_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_accel_v102_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_accel_v103_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_accel_v104_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_accel_v105_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_accel_v106_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_accel_v107_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_accel_v108_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_accel_v109_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_accel_v110_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_accel_v111_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_accel_v112_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_accel_v113_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_accel_v114_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_accel_v115_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_accel_v116_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_accel_v117_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_accel_v118_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_accel_v119_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_accel_v120_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_accel_v121_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_accel_v122_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_accel_v123_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_accel_v124_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_accel_v125_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_accel_v126_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_accel_v127_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_accel_v128_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_accel_v129_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_accel_v130_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_accel_v131_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_accel_v132_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_accel_v133_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_accel_v134_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_accel_v135_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_accel_v136_signal(investmentsc):
    base = _z(investmentsc, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_accel_v137_signal(investmentsc):
    base = _z(investmentsc, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_accel_v138_signal(investmentsc):
    base = _z(investmentsc, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_accel_v139_signal(investmentsc):
    base = _z(investmentsc, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_accel_v140_signal(investmentsc):
    base = _z(investmentsc, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_accel_v141_signal(investmentsc):
    base = _z(investmentsc, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_accel_v142_signal(investmentsc):
    base = _z(investmentsc, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_accel_v143_signal(investmentsc):
    base = _z(investmentsc, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_accel_v144_signal(investmentsc):
    base = _z(investmentsc, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_accel_v145_signal(investmentsc):
    base = _z(investmentsc, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_accel_v146_signal(investmentsc):
    base = _z(investmentsc, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_accel_v147_signal(investmentsc):
    base = _z(investmentsc, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_accel_v148_signal(investmentsc):
    base = _z(investmentsc, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_accel_v149_signal(investmentsc):
    base = _z(investmentsc, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_accel_v150_signal(investmentsc):
    base = _z(investmentsc, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
