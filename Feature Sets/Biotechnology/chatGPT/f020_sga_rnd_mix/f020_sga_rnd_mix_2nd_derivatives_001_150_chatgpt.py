"""Family f020 - SG&A versus R&D mix (R&D and Innovation) | Sharadar tables: SF1 | fields: sgna, rnd, opex | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_slope_v001_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_slope_v002_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sgna
def srm_f020_sga_rnd_mix_raw_21d_slope_v003_signal(sgna, closeadj):
    base = _mean(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_slope_v004_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_slope_v005_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sgna
def srm_f020_sga_rnd_mix_raw_63d_slope_v006_signal(sgna, closeadj):
    base = _mean(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_slope_v007_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_slope_v008_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sgna
def srm_f020_sga_rnd_mix_raw_126d_slope_v009_signal(sgna, closeadj):
    base = _mean(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_slope_v010_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_slope_v011_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sgna
def srm_f020_sga_rnd_mix_raw_252d_slope_v012_signal(sgna, closeadj):
    base = _mean(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_slope_v013_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_slope_v014_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sgna
def srm_f020_sga_rnd_mix_raw_504d_slope_v015_signal(sgna, closeadj):
    base = _mean(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_slope_v016_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_slope_v017_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sgna
def srm_f020_sga_rnd_mix_log_21d_slope_v018_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_slope_v019_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_slope_v020_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sgna
def srm_f020_sga_rnd_mix_log_63d_slope_v021_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_slope_v022_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_slope_v023_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sgna
def srm_f020_sga_rnd_mix_log_126d_slope_v024_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_slope_v025_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_slope_v026_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sgna
def srm_f020_sga_rnd_mix_log_252d_slope_v027_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_slope_v028_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_slope_v029_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sgna
def srm_f020_sga_rnd_mix_log_504d_slope_v030_signal(sgna, closeadj):
    base = _mean(_sga_rnd_mix_log(sgna), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_slope_v031_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_slope_v032_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sgna
def srm_f020_sga_rnd_mix_pershare_21d_slope_v033_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_slope_v034_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_slope_v035_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sgna
def srm_f020_sga_rnd_mix_pershare_63d_slope_v036_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_slope_v037_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_slope_v038_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sgna
def srm_f020_sga_rnd_mix_pershare_126d_slope_v039_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_slope_v040_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_slope_v041_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sgna
def srm_f020_sga_rnd_mix_pershare_252d_slope_v042_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_slope_v043_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_slope_v044_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sgna
def srm_f020_sga_rnd_mix_pershare_504d_slope_v045_signal(sgna, sharesbas, closeadj):
    base = _mean(_sga_rnd_mix_per_share(sgna, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_slope_v046_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_slope_v047_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_21d_slope_v048_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_slope_v049_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_slope_v050_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_63d_slope_v051_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_slope_v052_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_slope_v053_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_126d_slope_v054_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_slope_v055_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_slope_v056_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_252d_slope_v057_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_slope_v058_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_slope_v059_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_rnd sgna
def srm_f020_sga_rnd_mix_per_rnd_504d_slope_v060_signal(sgna, rnd):
    base = _mean(_sga_rnd_mix_scaled(sgna, rnd), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_slope_v061_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_slope_v062_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_21d_slope_v063_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_slope_v064_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_slope_v065_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_63d_slope_v066_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_slope_v067_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_slope_v068_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_126d_slope_v069_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_slope_v070_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_slope_v071_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_252d_slope_v072_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_slope_v073_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_slope_v074_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sgna
def srm_f020_sga_rnd_mix_per_assets_504d_slope_v075_signal(sgna, assets):
    base = _mean(_sga_rnd_mix_scaled(sgna, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_slope_v076_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_slope_v077_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_21d_slope_v078_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_slope_v079_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_slope_v080_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_63d_slope_v081_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_slope_v082_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_slope_v083_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_126d_slope_v084_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_slope_v085_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_slope_v086_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_252d_slope_v087_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_slope_v088_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_slope_v089_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sgna
def srm_f020_sga_rnd_mix_per_marketcap_504d_slope_v090_signal(sgna, marketcap):
    base = _mean(_sga_rnd_mix_scaled(sgna, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_slope_v091_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_slope_v092_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sgna
def srm_f020_sga_rnd_mix_std_21d_slope_v093_signal(sgna, closeadj):
    base = _std(sgna, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_slope_v094_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_slope_v095_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sgna
def srm_f020_sga_rnd_mix_std_63d_slope_v096_signal(sgna, closeadj):
    base = _std(sgna, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_slope_v097_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_slope_v098_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sgna
def srm_f020_sga_rnd_mix_std_126d_slope_v099_signal(sgna, closeadj):
    base = _std(sgna, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_slope_v100_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_slope_v101_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sgna
def srm_f020_sga_rnd_mix_std_252d_slope_v102_signal(sgna, closeadj):
    base = _std(sgna, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_slope_v103_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_slope_v104_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sgna
def srm_f020_sga_rnd_mix_std_504d_slope_v105_signal(sgna, closeadj):
    base = _std(sgna, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_slope_v106_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_slope_v107_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sgna
def srm_f020_sga_rnd_mix_ewm_21d_slope_v108_signal(sgna, closeadj):
    base = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_slope_v109_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_slope_v110_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sgna
def srm_f020_sga_rnd_mix_ewm_63d_slope_v111_signal(sgna, closeadj):
    base = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_slope_v112_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_slope_v113_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sgna
def srm_f020_sga_rnd_mix_ewm_126d_slope_v114_signal(sgna, closeadj):
    base = sgna.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_slope_v115_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_slope_v116_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sgna
def srm_f020_sga_rnd_mix_ewm_252d_slope_v117_signal(sgna, closeadj):
    base = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_slope_v118_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_slope_v119_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sgna
def srm_f020_sga_rnd_mix_ewm_504d_slope_v120_signal(sgna, closeadj):
    base = sgna.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_slope_v121_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_slope_v122_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sgna
def srm_f020_sga_rnd_mix_sq_21d_slope_v123_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_slope_v124_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_slope_v125_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sgna
def srm_f020_sga_rnd_mix_sq_63d_slope_v126_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_slope_v127_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_slope_v128_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sgna
def srm_f020_sga_rnd_mix_sq_126d_slope_v129_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_slope_v130_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_slope_v131_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sgna
def srm_f020_sga_rnd_mix_sq_252d_slope_v132_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_slope_v133_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_slope_v134_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sgna
def srm_f020_sga_rnd_mix_sq_504d_slope_v135_signal(sgna, closeadj):
    base = _mean(sgna * sgna, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_slope_v136_signal(sgna):
    base = _z(sgna, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_slope_v137_signal(sgna):
    base = _z(sgna, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sgna
def srm_f020_sga_rnd_mix_z_21d_slope_v138_signal(sgna):
    base = _z(sgna, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_slope_v139_signal(sgna):
    base = _z(sgna, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_slope_v140_signal(sgna):
    base = _z(sgna, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sgna
def srm_f020_sga_rnd_mix_z_63d_slope_v141_signal(sgna):
    base = _z(sgna, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_slope_v142_signal(sgna):
    base = _z(sgna, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_slope_v143_signal(sgna):
    base = _z(sgna, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sgna
def srm_f020_sga_rnd_mix_z_126d_slope_v144_signal(sgna):
    base = _z(sgna, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_slope_v145_signal(sgna):
    base = _z(sgna, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_slope_v146_signal(sgna):
    base = _z(sgna, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sgna
def srm_f020_sga_rnd_mix_z_252d_slope_v147_signal(sgna):
    base = _z(sgna, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_slope_v148_signal(sgna):
    base = _z(sgna, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_slope_v149_signal(sgna):
    base = _z(sgna, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sgna
def srm_f020_sga_rnd_mix_z_504d_slope_v150_signal(sgna):
    base = _z(sgna, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
