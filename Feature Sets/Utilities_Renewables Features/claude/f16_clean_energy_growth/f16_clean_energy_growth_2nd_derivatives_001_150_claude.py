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


# ===== folder domain primitives =====
def _f16_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f16_growth_acceleration(revenue, w):
    g = revenue.pct_change(periods=w)
    return g.diff(periods=w)


def _f16_growth_quality(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return eg - rg

def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d5_slope_v001_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d10_slope_v002_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d21_slope_v003_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d42_slope_v004_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d63_slope_v005_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d126_slope_v006_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d5_slope_v007_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d10_slope_v008_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d21_slope_v009_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d42_slope_v010_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d63_slope_v011_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d126_slope_v012_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d5_slope_v013_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d10_slope_v014_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d21_slope_v015_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d42_slope_v016_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d63_slope_v017_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d126_slope_v018_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 5) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d5_slope_v019_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d10_slope_v020_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d21_slope_v021_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d42_slope_v022_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d63_slope_v023_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d126_slope_v024_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d5_slope_v025_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d10_slope_v026_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d21_slope_v027_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d42_slope_v028_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d63_slope_v029_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d126_slope_v030_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d5_slope_v031_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d10_slope_v032_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d21_slope_v033_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d42_slope_v034_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d63_slope_v035_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d126_slope_v036_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 21) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d5_slope_v037_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d10_slope_v038_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d21_slope_v039_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d42_slope_v040_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d63_slope_v041_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d126_slope_v042_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d5_slope_v043_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d10_slope_v044_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d21_slope_v045_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d42_slope_v046_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d63_slope_v047_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d126_slope_v048_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d5_slope_v049_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d10_slope_v050_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d21_slope_v051_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d42_slope_v052_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d63_slope_v053_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d126_slope_v054_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d5_slope_v055_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d10_slope_v056_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d21_slope_v057_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d42_slope_v058_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d63_slope_v059_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d126_slope_v060_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d5_slope_v061_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d10_slope_v062_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d21_slope_v063_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d42_slope_v064_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d63_slope_v065_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d126_slope_v066_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d5_slope_v067_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d10_slope_v068_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d21_slope_v069_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d42_slope_v070_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d63_slope_v071_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d126_slope_v072_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 5), 63) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d5_slope_v073_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d10_slope_v074_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d21_slope_v075_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d42_slope_v076_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d63_slope_v077_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d126_slope_v078_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d5_slope_v079_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d10_slope_v080_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d21_slope_v081_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d42_slope_v082_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d63_slope_v083_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d126_slope_v084_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d5_slope_v085_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d10_slope_v086_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d21_slope_v087_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d42_slope_v088_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d63_slope_v089_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d126_slope_v090_signal(revenue, closeadj):
    result = _slope_diff_norm((_f16_revenue_growth(revenue, 5)).abs() * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d5_slope_v091_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d10_slope_v092_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d21_slope_v093_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d42_slope_v094_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d63_slope_v095_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d126_slope_v096_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d5_slope_v097_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d10_slope_v098_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d21_slope_v099_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d42_slope_v100_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d63_slope_v101_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d126_slope_v102_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d5_slope_v103_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d10_slope_v104_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d21_slope_v105_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d42_slope_v106_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d63_slope_v107_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d126_slope_v108_signal(revenue, closeadj):
    result = _slope_diff_norm(_f16_revenue_growth(revenue, 10) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d5_slope_v109_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d10_slope_v110_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d21_slope_v111_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d42_slope_v112_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d63_slope_v113_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d126_slope_v114_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d5_slope_v115_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d10_slope_v116_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d21_slope_v117_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d42_slope_v118_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d63_slope_v119_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d126_slope_v120_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d5_slope_v121_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d10_slope_v122_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d21_slope_v123_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d42_slope_v124_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d63_slope_v125_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d126_slope_v126_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 21) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d5_slope_v127_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d10_slope_v128_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d21_slope_v129_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d42_slope_v130_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d63_slope_v131_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d126_slope_v132_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d5_slope_v133_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d10_slope_v134_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d21_slope_v135_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d42_slope_v136_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d63_slope_v137_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d126_slope_v138_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d5_slope_v139_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d10_slope_v140_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d21_slope_v141_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d42_slope_v142_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d63_slope_v143_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d126_slope_v144_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f16_revenue_growth(revenue, 10), 63) * _std(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d5_slope_v145_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d10_slope_v146_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d21_slope_v147_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d42_slope_v148_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d63_slope_v149_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d126_slope_v150_signal(revenue, closeadj):
    result = _slope_diff_norm(_std(_f16_revenue_growth(revenue, 10), 63) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d5_slope_v001_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d10_slope_v002_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d21_slope_v003_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d42_slope_v004_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d63_slope_v005_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_5d_d126_slope_v006_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d5_slope_v007_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d10_slope_v008_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d21_slope_v009_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d42_slope_v010_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d63_slope_v011_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_5d_d126_slope_v012_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d5_slope_v013_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d10_slope_v014_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d21_slope_v015_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d42_slope_v016_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d63_slope_v017_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_5d_d126_slope_v018_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d5_slope_v019_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d10_slope_v020_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d21_slope_v021_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d42_slope_v022_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d63_slope_v023_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_5d_d126_slope_v024_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d5_slope_v025_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d10_slope_v026_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d21_slope_v027_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d42_slope_v028_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d63_slope_v029_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_5d_d126_slope_v030_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d5_slope_v031_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d10_slope_v032_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d21_slope_v033_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d42_slope_v034_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d63_slope_v035_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_5d_d126_slope_v036_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d5_slope_v037_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d10_slope_v038_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d21_slope_v039_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d42_slope_v040_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d63_slope_v041_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_5d_d126_slope_v042_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d5_slope_v043_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d10_slope_v044_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d21_slope_v045_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d42_slope_v046_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d63_slope_v047_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_5d_d126_slope_v048_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d5_slope_v049_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d10_slope_v050_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d21_slope_v051_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d42_slope_v052_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d63_slope_v053_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_5d_d126_slope_v054_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d5_slope_v055_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d10_slope_v056_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d21_slope_v057_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d42_slope_v058_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d63_slope_v059_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_5d_d126_slope_v060_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d5_slope_v061_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d10_slope_v062_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d21_slope_v063_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d42_slope_v064_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d63_slope_v065_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xmean63_5d_d126_slope_v066_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d5_slope_v067_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d10_slope_v068_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d21_slope_v069_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d42_slope_v070_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d63_slope_v071_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xstd63_5d_d126_slope_v072_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d5_slope_v073_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d10_slope_v074_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d21_slope_v075_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d42_slope_v076_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d63_slope_v077_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xclose_5d_d126_slope_v078_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d5_slope_v079_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d10_slope_v080_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d21_slope_v081_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d42_slope_v082_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d63_slope_v083_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xmean63_5d_d126_slope_v084_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d5_slope_v085_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d10_slope_v086_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d21_slope_v087_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d42_slope_v088_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d63_slope_v089_signal,
    f16ceg_f16_clean_energy_growth_p1_abs_xstd63_5d_d126_slope_v090_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d5_slope_v091_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d10_slope_v092_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d21_slope_v093_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d42_slope_v094_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d63_slope_v095_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xclose_10d_d126_slope_v096_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d5_slope_v097_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d10_slope_v098_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d21_slope_v099_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d42_slope_v100_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d63_slope_v101_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xmean63_10d_d126_slope_v102_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d5_slope_v103_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d10_slope_v104_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d21_slope_v105_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d42_slope_v106_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d63_slope_v107_signal,
    f16ceg_f16_clean_energy_growth_p1_raw_xstd63_10d_d126_slope_v108_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d5_slope_v109_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d10_slope_v110_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d21_slope_v111_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d42_slope_v112_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d63_slope_v113_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xclose_10d_d126_slope_v114_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d5_slope_v115_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d10_slope_v116_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d21_slope_v117_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d42_slope_v118_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d63_slope_v119_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xmean63_10d_d126_slope_v120_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d5_slope_v121_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d10_slope_v122_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d21_slope_v123_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d42_slope_v124_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d63_slope_v125_signal,
    f16ceg_f16_clean_energy_growth_p1_mean21_xstd63_10d_d126_slope_v126_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d5_slope_v127_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d10_slope_v128_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d21_slope_v129_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d42_slope_v130_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d63_slope_v131_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xclose_10d_d126_slope_v132_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d5_slope_v133_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d10_slope_v134_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d21_slope_v135_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d42_slope_v136_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d63_slope_v137_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xmean63_10d_d126_slope_v138_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d5_slope_v139_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d10_slope_v140_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d21_slope_v141_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d42_slope_v142_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d63_slope_v143_signal,
    f16ceg_f16_clean_energy_growth_p1_mean63_xstd63_10d_d126_slope_v144_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d5_slope_v145_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d10_slope_v146_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d21_slope_v147_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d42_slope_v148_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d63_slope_v149_signal,
    f16ceg_f16_clean_energy_growth_p1_std63_xclose_10d_d126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_CLEAN_ENERGY_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY

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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f16_revenue_growth', '_f16_growth_acceleration', '_f16_growth_quality')
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
    print(f"OK f16_clean_energy_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
