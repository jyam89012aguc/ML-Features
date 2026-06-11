"""Family f020 - SG&A versus R&D mix (R&D and Innovation) | Sharadar tables: SF1 | fields: sgna, rnd, opex | 3rd derivatives 001-150"""
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
def _sga_rnd_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sga_rnd_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sga_rnd_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_accel_v001_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_accel_v002_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_accel_v003_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_accel_v004_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_accel_v005_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_accel_v006_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_accel_v007_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_accel_v008_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_accel_v009_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_accel_v010_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_accel_v011_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_accel_v012_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_accel_v013_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_accel_v014_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_accel_v015_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_accel_v016_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_accel_v017_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_accel_v018_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_accel_v019_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_accel_v020_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_accel_v021_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_accel_v022_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_accel_v023_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_accel_v024_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_accel_v025_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_accel_v026_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_accel_v027_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_accel_v028_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_accel_v029_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_accel_v030_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_accel_v031_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_accel_v032_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_accel_v033_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_accel_v034_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_accel_v035_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_accel_v036_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_accel_v037_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_accel_v038_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_accel_v039_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_accel_v040_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_accel_v041_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_accel_v042_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_accel_v043_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_accel_v044_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_accel_v045_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_accel_v046_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_accel_v047_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_accel_v048_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_accel_v049_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_accel_v050_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_accel_v051_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_accel_v052_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_accel_v053_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_accel_v054_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_accel_v055_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_accel_v056_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_accel_v057_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_accel_v058_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_accel_v059_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_accel_v060_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_accel_v061_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_accel_v062_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_accel_v063_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_accel_v064_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_accel_v065_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_accel_v066_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_accel_v067_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_accel_v068_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_accel_v069_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_accel_v070_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_accel_v071_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_accel_v072_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_accel_v073_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_accel_v074_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_accel_v075_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_accel_v076_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_accel_v077_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_accel_v078_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_accel_v079_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_accel_v080_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_accel_v081_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_accel_v082_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_accel_v083_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_accel_v084_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_accel_v085_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_accel_v086_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_accel_v087_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_accel_v088_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_accel_v089_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_accel_v090_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_accel_v091_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_accel_v092_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_accel_v093_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_accel_v094_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_accel_v095_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_accel_v096_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_accel_v097_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_accel_v098_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_accel_v099_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_accel_v100_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_accel_v101_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_accel_v102_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_accel_v103_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_accel_v104_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_accel_v105_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_accel_v106_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_accel_v107_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_accel_v108_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_accel_v109_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_accel_v110_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_accel_v111_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_accel_v112_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_accel_v113_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_accel_v114_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_accel_v115_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_accel_v116_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_accel_v117_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_accel_v118_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_accel_v119_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_accel_v120_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_accel_v121_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_accel_v122_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_accel_v123_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_accel_v124_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_accel_v125_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_accel_v126_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_accel_v127_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_accel_v128_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_accel_v129_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_accel_v130_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_accel_v131_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_accel_v132_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_accel_v133_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_accel_v134_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_accel_v135_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_accel_v136_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_accel_v137_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_accel_v138_signal(sgna):
    base = _z(sgna, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_accel_v139_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_accel_v140_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_accel_v141_signal(sgna):
    base = _z(sgna, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_accel_v142_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_accel_v143_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_accel_v144_signal(sgna):
    base = _z(sgna, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_accel_v145_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_accel_v146_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_accel_v147_signal(sgna):
    base = _z(sgna, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_accel_v148_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_accel_v149_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_accel_v150_signal(sgna):
    base = _z(sgna, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
