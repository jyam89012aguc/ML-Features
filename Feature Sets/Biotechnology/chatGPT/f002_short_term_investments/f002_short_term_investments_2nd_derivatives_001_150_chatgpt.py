"""Family f002 - SF1 liquid securities buffer (Liquidity and Runway) | Sharadar tables: SF1 | fields: investmentsc, investments, cashneq, assets | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_slope_v001_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_slope_v002_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw investmentsc
def sti_f002_short_term_investments_raw_21d_slope_v003_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_slope_v004_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_slope_v005_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw investmentsc
def sti_f002_short_term_investments_raw_63d_slope_v006_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_slope_v007_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_slope_v008_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw investmentsc
def sti_f002_short_term_investments_raw_126d_slope_v009_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_slope_v010_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_slope_v011_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw investmentsc
def sti_f002_short_term_investments_raw_252d_slope_v012_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_slope_v013_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_slope_v014_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw investmentsc
def sti_f002_short_term_investments_raw_504d_slope_v015_signal(investmentsc, closeadj):
    base = _mean(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_slope_v016_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_slope_v017_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log investmentsc
def sti_f002_short_term_investments_log_21d_slope_v018_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_slope_v019_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_slope_v020_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log investmentsc
def sti_f002_short_term_investments_log_63d_slope_v021_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_slope_v022_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_slope_v023_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log investmentsc
def sti_f002_short_term_investments_log_126d_slope_v024_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_slope_v025_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_slope_v026_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log investmentsc
def sti_f002_short_term_investments_log_252d_slope_v027_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_slope_v028_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_slope_v029_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log investmentsc
def sti_f002_short_term_investments_log_504d_slope_v030_signal(investmentsc, closeadj):
    base = _mean(_short_term_investments_log(investmentsc), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_slope_v031_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_slope_v032_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare investmentsc
def sti_f002_short_term_investments_pershare_21d_slope_v033_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_slope_v034_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_slope_v035_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare investmentsc
def sti_f002_short_term_investments_pershare_63d_slope_v036_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_slope_v037_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_slope_v038_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare investmentsc
def sti_f002_short_term_investments_pershare_126d_slope_v039_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_slope_v040_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_slope_v041_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare investmentsc
def sti_f002_short_term_investments_pershare_252d_slope_v042_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_slope_v043_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_slope_v044_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare investmentsc
def sti_f002_short_term_investments_pershare_504d_slope_v045_signal(investmentsc, sharesbas, closeadj):
    base = _mean(_short_term_investments_per_share(investmentsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_slope_v046_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_slope_v047_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_21d_slope_v048_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_slope_v049_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_slope_v050_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_63d_slope_v051_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_slope_v052_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_slope_v053_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_126d_slope_v054_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_slope_v055_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_slope_v056_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_252d_slope_v057_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_slope_v058_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_slope_v059_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_investments investmentsc
def sti_f002_short_term_investments_per_investments_504d_slope_v060_signal(investmentsc, investments):
    base = _mean(_short_term_investments_scaled(investmentsc, investments), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_slope_v061_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_slope_v062_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_21d_slope_v063_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_slope_v064_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_slope_v065_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_63d_slope_v066_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_slope_v067_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_slope_v068_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_126d_slope_v069_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_slope_v070_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_slope_v071_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_252d_slope_v072_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_slope_v073_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_slope_v074_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_cashneq investmentsc
def sti_f002_short_term_investments_per_cashneq_504d_slope_v075_signal(investmentsc, cashneq):
    base = _mean(_short_term_investments_scaled(investmentsc, cashneq), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_slope_v076_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_slope_v077_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_21d_slope_v078_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_slope_v079_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_slope_v080_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_63d_slope_v081_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_slope_v082_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_slope_v083_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_126d_slope_v084_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_slope_v085_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_slope_v086_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_252d_slope_v087_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_slope_v088_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_slope_v089_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets investmentsc
def sti_f002_short_term_investments_per_assets_504d_slope_v090_signal(investmentsc, assets):
    base = _mean(_short_term_investments_scaled(investmentsc, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_slope_v091_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_slope_v092_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std investmentsc
def sti_f002_short_term_investments_std_21d_slope_v093_signal(investmentsc, closeadj):
    base = _std(investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_slope_v094_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_slope_v095_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std investmentsc
def sti_f002_short_term_investments_std_63d_slope_v096_signal(investmentsc, closeadj):
    base = _std(investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_slope_v097_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_slope_v098_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std investmentsc
def sti_f002_short_term_investments_std_126d_slope_v099_signal(investmentsc, closeadj):
    base = _std(investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_slope_v100_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_slope_v101_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std investmentsc
def sti_f002_short_term_investments_std_252d_slope_v102_signal(investmentsc, closeadj):
    base = _std(investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_slope_v103_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_slope_v104_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std investmentsc
def sti_f002_short_term_investments_std_504d_slope_v105_signal(investmentsc, closeadj):
    base = _std(investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_slope_v106_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_slope_v107_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm investmentsc
def sti_f002_short_term_investments_ewm_21d_slope_v108_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_slope_v109_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_slope_v110_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm investmentsc
def sti_f002_short_term_investments_ewm_63d_slope_v111_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_slope_v112_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_slope_v113_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm investmentsc
def sti_f002_short_term_investments_ewm_126d_slope_v114_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_slope_v115_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_slope_v116_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm investmentsc
def sti_f002_short_term_investments_ewm_252d_slope_v117_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_slope_v118_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_slope_v119_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm investmentsc
def sti_f002_short_term_investments_ewm_504d_slope_v120_signal(investmentsc, closeadj):
    base = investmentsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_slope_v121_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_slope_v122_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq investmentsc
def sti_f002_short_term_investments_sq_21d_slope_v123_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_slope_v124_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_slope_v125_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq investmentsc
def sti_f002_short_term_investments_sq_63d_slope_v126_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_slope_v127_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_slope_v128_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq investmentsc
def sti_f002_short_term_investments_sq_126d_slope_v129_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_slope_v130_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_slope_v131_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq investmentsc
def sti_f002_short_term_investments_sq_252d_slope_v132_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_slope_v133_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_slope_v134_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq investmentsc
def sti_f002_short_term_investments_sq_504d_slope_v135_signal(investmentsc, closeadj):
    base = _mean(investmentsc * investmentsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_slope_v136_signal(investmentsc):
    base = _z(investmentsc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_slope_v137_signal(investmentsc):
    base = _z(investmentsc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z investmentsc
def sti_f002_short_term_investments_z_21d_slope_v138_signal(investmentsc):
    base = _z(investmentsc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_slope_v139_signal(investmentsc):
    base = _z(investmentsc, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_slope_v140_signal(investmentsc):
    base = _z(investmentsc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z investmentsc
def sti_f002_short_term_investments_z_63d_slope_v141_signal(investmentsc):
    base = _z(investmentsc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_slope_v142_signal(investmentsc):
    base = _z(investmentsc, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_slope_v143_signal(investmentsc):
    base = _z(investmentsc, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z investmentsc
def sti_f002_short_term_investments_z_126d_slope_v144_signal(investmentsc):
    base = _z(investmentsc, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_slope_v145_signal(investmentsc):
    base = _z(investmentsc, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_slope_v146_signal(investmentsc):
    base = _z(investmentsc, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z investmentsc
def sti_f002_short_term_investments_z_252d_slope_v147_signal(investmentsc):
    base = _z(investmentsc, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_slope_v148_signal(investmentsc):
    base = _z(investmentsc, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_slope_v149_signal(investmentsc):
    base = _z(investmentsc, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z investmentsc
def sti_f002_short_term_investments_z_504d_slope_v150_signal(investmentsc):
    base = _z(investmentsc, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
