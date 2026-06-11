"""Family f070 - EV to R&D investment valuation (Valuation Multiples) | Sharadar tables: DAILY,SF1 | fields: ev, rnd | 3rd derivatives 001-150"""
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
def _ev_rnd_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ev_rnd_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ev_rnd_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ev
def erv_f070_ev_rnd_valuation_raw_21d_accel_v001_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ev
def erv_f070_ev_rnd_valuation_raw_21d_accel_v002_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ev
def erv_f070_ev_rnd_valuation_raw_21d_accel_v003_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ev
def erv_f070_ev_rnd_valuation_raw_63d_accel_v004_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ev
def erv_f070_ev_rnd_valuation_raw_63d_accel_v005_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ev
def erv_f070_ev_rnd_valuation_raw_63d_accel_v006_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ev
def erv_f070_ev_rnd_valuation_raw_126d_accel_v007_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ev
def erv_f070_ev_rnd_valuation_raw_126d_accel_v008_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ev
def erv_f070_ev_rnd_valuation_raw_126d_accel_v009_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ev
def erv_f070_ev_rnd_valuation_raw_252d_accel_v010_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ev
def erv_f070_ev_rnd_valuation_raw_252d_accel_v011_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ev
def erv_f070_ev_rnd_valuation_raw_252d_accel_v012_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ev
def erv_f070_ev_rnd_valuation_raw_504d_accel_v013_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ev
def erv_f070_ev_rnd_valuation_raw_504d_accel_v014_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ev
def erv_f070_ev_rnd_valuation_raw_504d_accel_v015_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ev
def erv_f070_ev_rnd_valuation_log_21d_accel_v016_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ev
def erv_f070_ev_rnd_valuation_log_21d_accel_v017_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ev
def erv_f070_ev_rnd_valuation_log_21d_accel_v018_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ev
def erv_f070_ev_rnd_valuation_log_63d_accel_v019_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ev
def erv_f070_ev_rnd_valuation_log_63d_accel_v020_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ev
def erv_f070_ev_rnd_valuation_log_63d_accel_v021_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ev
def erv_f070_ev_rnd_valuation_log_126d_accel_v022_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ev
def erv_f070_ev_rnd_valuation_log_126d_accel_v023_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ev
def erv_f070_ev_rnd_valuation_log_126d_accel_v024_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ev
def erv_f070_ev_rnd_valuation_log_252d_accel_v025_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ev
def erv_f070_ev_rnd_valuation_log_252d_accel_v026_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ev
def erv_f070_ev_rnd_valuation_log_252d_accel_v027_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ev
def erv_f070_ev_rnd_valuation_log_504d_accel_v028_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ev
def erv_f070_ev_rnd_valuation_log_504d_accel_v029_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ev
def erv_f070_ev_rnd_valuation_log_504d_accel_v030_signal(ev, closeadj):
    base = _mean(_ev_rnd_valuation_log(ev), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ev
def erv_f070_ev_rnd_valuation_pershare_21d_accel_v031_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ev
def erv_f070_ev_rnd_valuation_pershare_21d_accel_v032_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ev
def erv_f070_ev_rnd_valuation_pershare_21d_accel_v033_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ev
def erv_f070_ev_rnd_valuation_pershare_63d_accel_v034_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ev
def erv_f070_ev_rnd_valuation_pershare_63d_accel_v035_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ev
def erv_f070_ev_rnd_valuation_pershare_63d_accel_v036_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ev
def erv_f070_ev_rnd_valuation_pershare_126d_accel_v037_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ev
def erv_f070_ev_rnd_valuation_pershare_126d_accel_v038_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ev
def erv_f070_ev_rnd_valuation_pershare_126d_accel_v039_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ev
def erv_f070_ev_rnd_valuation_pershare_252d_accel_v040_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ev
def erv_f070_ev_rnd_valuation_pershare_252d_accel_v041_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ev
def erv_f070_ev_rnd_valuation_pershare_252d_accel_v042_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ev
def erv_f070_ev_rnd_valuation_pershare_504d_accel_v043_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ev
def erv_f070_ev_rnd_valuation_pershare_504d_accel_v044_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ev
def erv_f070_ev_rnd_valuation_pershare_504d_accel_v045_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_valuation_per_share(ev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_21d_accel_v046_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_21d_accel_v047_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_21d_accel_v048_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_63d_accel_v049_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_63d_accel_v050_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_63d_accel_v051_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_126d_accel_v052_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_126d_accel_v053_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_126d_accel_v054_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_252d_accel_v055_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_252d_accel_v056_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_252d_accel_v057_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_504d_accel_v058_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_504d_accel_v059_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_rnd ev
def erv_f070_ev_rnd_valuation_per_rnd_504d_accel_v060_signal(ev, rnd):
    base = _mean(_ev_rnd_valuation_scaled(ev, rnd), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_21d_accel_v061_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_21d_accel_v062_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_21d_accel_v063_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_63d_accel_v064_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_63d_accel_v065_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_63d_accel_v066_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_126d_accel_v067_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_126d_accel_v068_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_126d_accel_v069_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_252d_accel_v070_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_252d_accel_v071_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_252d_accel_v072_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_504d_accel_v073_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_504d_accel_v074_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ev
def erv_f070_ev_rnd_valuation_per_assets_504d_accel_v075_signal(ev, assets):
    base = _mean(_ev_rnd_valuation_scaled(ev, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_21d_accel_v076_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_21d_accel_v077_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_21d_accel_v078_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_63d_accel_v079_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_63d_accel_v080_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_63d_accel_v081_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_126d_accel_v082_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_126d_accel_v083_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_126d_accel_v084_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_252d_accel_v085_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_252d_accel_v086_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_252d_accel_v087_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_504d_accel_v088_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_504d_accel_v089_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap ev
def erv_f070_ev_rnd_valuation_per_marketcap_504d_accel_v090_signal(ev, marketcap):
    base = _mean(_ev_rnd_valuation_scaled(ev, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ev
def erv_f070_ev_rnd_valuation_std_21d_accel_v091_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ev
def erv_f070_ev_rnd_valuation_std_21d_accel_v092_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ev
def erv_f070_ev_rnd_valuation_std_21d_accel_v093_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ev
def erv_f070_ev_rnd_valuation_std_63d_accel_v094_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ev
def erv_f070_ev_rnd_valuation_std_63d_accel_v095_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ev
def erv_f070_ev_rnd_valuation_std_63d_accel_v096_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ev
def erv_f070_ev_rnd_valuation_std_126d_accel_v097_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ev
def erv_f070_ev_rnd_valuation_std_126d_accel_v098_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ev
def erv_f070_ev_rnd_valuation_std_126d_accel_v099_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ev
def erv_f070_ev_rnd_valuation_std_252d_accel_v100_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ev
def erv_f070_ev_rnd_valuation_std_252d_accel_v101_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ev
def erv_f070_ev_rnd_valuation_std_252d_accel_v102_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ev
def erv_f070_ev_rnd_valuation_std_504d_accel_v103_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ev
def erv_f070_ev_rnd_valuation_std_504d_accel_v104_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ev
def erv_f070_ev_rnd_valuation_std_504d_accel_v105_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ev
def erv_f070_ev_rnd_valuation_ewm_21d_accel_v106_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ev
def erv_f070_ev_rnd_valuation_ewm_21d_accel_v107_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ev
def erv_f070_ev_rnd_valuation_ewm_21d_accel_v108_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ev
def erv_f070_ev_rnd_valuation_ewm_63d_accel_v109_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ev
def erv_f070_ev_rnd_valuation_ewm_63d_accel_v110_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ev
def erv_f070_ev_rnd_valuation_ewm_63d_accel_v111_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ev
def erv_f070_ev_rnd_valuation_ewm_126d_accel_v112_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ev
def erv_f070_ev_rnd_valuation_ewm_126d_accel_v113_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ev
def erv_f070_ev_rnd_valuation_ewm_126d_accel_v114_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ev
def erv_f070_ev_rnd_valuation_ewm_252d_accel_v115_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ev
def erv_f070_ev_rnd_valuation_ewm_252d_accel_v116_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ev
def erv_f070_ev_rnd_valuation_ewm_252d_accel_v117_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ev
def erv_f070_ev_rnd_valuation_ewm_504d_accel_v118_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ev
def erv_f070_ev_rnd_valuation_ewm_504d_accel_v119_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ev
def erv_f070_ev_rnd_valuation_ewm_504d_accel_v120_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ev
def erv_f070_ev_rnd_valuation_sq_21d_accel_v121_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ev
def erv_f070_ev_rnd_valuation_sq_21d_accel_v122_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ev
def erv_f070_ev_rnd_valuation_sq_21d_accel_v123_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ev
def erv_f070_ev_rnd_valuation_sq_63d_accel_v124_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ev
def erv_f070_ev_rnd_valuation_sq_63d_accel_v125_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ev
def erv_f070_ev_rnd_valuation_sq_63d_accel_v126_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ev
def erv_f070_ev_rnd_valuation_sq_126d_accel_v127_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ev
def erv_f070_ev_rnd_valuation_sq_126d_accel_v128_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ev
def erv_f070_ev_rnd_valuation_sq_126d_accel_v129_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ev
def erv_f070_ev_rnd_valuation_sq_252d_accel_v130_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ev
def erv_f070_ev_rnd_valuation_sq_252d_accel_v131_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ev
def erv_f070_ev_rnd_valuation_sq_252d_accel_v132_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ev
def erv_f070_ev_rnd_valuation_sq_504d_accel_v133_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ev
def erv_f070_ev_rnd_valuation_sq_504d_accel_v134_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ev
def erv_f070_ev_rnd_valuation_sq_504d_accel_v135_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ev
def erv_f070_ev_rnd_valuation_z_21d_accel_v136_signal(ev):
    base = _z(ev, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ev
def erv_f070_ev_rnd_valuation_z_21d_accel_v137_signal(ev):
    base = _z(ev, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ev
def erv_f070_ev_rnd_valuation_z_21d_accel_v138_signal(ev):
    base = _z(ev, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ev
def erv_f070_ev_rnd_valuation_z_63d_accel_v139_signal(ev):
    base = _z(ev, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ev
def erv_f070_ev_rnd_valuation_z_63d_accel_v140_signal(ev):
    base = _z(ev, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ev
def erv_f070_ev_rnd_valuation_z_63d_accel_v141_signal(ev):
    base = _z(ev, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ev
def erv_f070_ev_rnd_valuation_z_126d_accel_v142_signal(ev):
    base = _z(ev, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ev
def erv_f070_ev_rnd_valuation_z_126d_accel_v143_signal(ev):
    base = _z(ev, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ev
def erv_f070_ev_rnd_valuation_z_126d_accel_v144_signal(ev):
    base = _z(ev, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ev
def erv_f070_ev_rnd_valuation_z_252d_accel_v145_signal(ev):
    base = _z(ev, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ev
def erv_f070_ev_rnd_valuation_z_252d_accel_v146_signal(ev):
    base = _z(ev, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ev
def erv_f070_ev_rnd_valuation_z_252d_accel_v147_signal(ev):
    base = _z(ev, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ev
def erv_f070_ev_rnd_valuation_z_504d_accel_v148_signal(ev):
    base = _z(ev, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ev
def erv_f070_ev_rnd_valuation_z_504d_accel_v149_signal(ev):
    base = _z(ev, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ev
def erv_f070_ev_rnd_valuation_z_504d_accel_v150_signal(ev):
    base = _z(ev, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
