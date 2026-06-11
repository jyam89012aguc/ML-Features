"""short_interest_buildup_trajectory d1 features 001-075 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the final return expression with .diff().
Self-contained; helpers redefined locally per HANDOFF.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 3, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _rolling_max(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).max()


def _rolling_min(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).min()


def _pct_change(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


def f25_sibt_001_log_shortinterest_d1(shortinterest):
    return (_safe_log(shortinterest)).diff()


def f25_sibt_002_log_shortinterest_ema_21d_d1(shortinterest):
    return (_ema(_safe_log(shortinterest), 21, min_periods=5)).diff()


def f25_sibt_003_log_shortinterest_ema_63d_d1(shortinterest):
    return (_ema(_safe_log(shortinterest), 63, min_periods=10)).diff()


def f25_sibt_004_shortinterest_to_21d_mean_d1(shortinterest):
    return (_safe_div(shortinterest, shortinterest.rolling(21, min_periods=3).mean())).diff()


def f25_sibt_005_shortinterest_to_63d_mean_d1(shortinterest):
    return (_safe_div(shortinterest, shortinterest.rolling(63, min_periods=10).mean())).diff()


def f25_sibt_006_shortinterest_to_126d_mean_d1(shortinterest):
    return (_safe_div(shortinterest, shortinterest.rolling(126, min_periods=20).mean())).diff()


def f25_sibt_007_shortinterest_to_252d_mean_d1(shortinterest):
    return (_safe_div(shortinterest, shortinterest.rolling(252, min_periods=42).mean())).diff()


def f25_sibt_008_log_shortinterest_minus_log_ema_63d_d1(shortinterest):
    return (_safe_log(shortinterest) - _ema(_safe_log(shortinterest), 63, min_periods=10)).diff()


def f25_sibt_009_shortinterest_pct_change_21d_d1(shortinterest):
    return (_pct_change(shortinterest, 21)).diff()


def f25_sibt_010_shortinterest_pct_change_63d_d1(shortinterest):
    return (_pct_change(shortinterest, 63)).diff()


def f25_sibt_011_shortinterest_pct_change_126d_d1(shortinterest):
    return (_pct_change(shortinterest, 126)).diff()


def f25_sibt_012_log_shortinterest_diff_21d_d1(shortinterest):
    return (_safe_log(shortinterest) - _safe_log(shortinterest.shift(21))).diff()


def f25_sibt_013_log_shortinterest_diff_63d_d1(shortinterest):
    return (_safe_log(shortinterest) - _safe_log(shortinterest.shift(63))).diff()


def f25_sibt_014_shortinterest_acceleration_21_vs_63_d1(shortinterest):
    short_21 = _pct_change(shortinterest, 21)
    short_63 = _pct_change(shortinterest, 63)
    return (short_21 - short_63).diff()


def f25_sibt_015_shortinterest_acceleration_63_vs_252_d1(shortinterest):
    short_63 = _pct_change(shortinterest, 63)
    short_252 = _pct_change(shortinterest, 252)
    return (short_63 - short_252).diff()


# ---- Block B: % of FLOAT buildup trajectory (016-030) ----


def f25_sibt_016_shortpctfloat_level_d1(shortpctfloat):
    return (shortpctfloat).diff()


def f25_sibt_017_shortpctfloat_ema_21d_d1(shortpctfloat):
    return (_ema(shortpctfloat, 21, min_periods=5)).diff()


def f25_sibt_018_shortpctfloat_ema_63d_d1(shortpctfloat):
    return (_ema(shortpctfloat, 63, min_periods=10)).diff()


def f25_sibt_019_shortpctfloat_change_21d_d1(shortpctfloat):
    return (shortpctfloat - shortpctfloat.shift(21)).diff()


def f25_sibt_020_shortpctfloat_change_63d_d1(shortpctfloat):
    return (shortpctfloat - shortpctfloat.shift(63)).diff()


def f25_sibt_021_shortpctfloat_change_126d_d1(shortpctfloat):
    return (shortpctfloat - shortpctfloat.shift(126)).diff()


def f25_sibt_022_shortpctfloat_pct_change_63d_d1(shortpctfloat):
    return (_pct_change(shortpctfloat, 63)).diff()


def f25_sibt_023_shortpctfloat_minus_252d_median_d1(shortpctfloat):
    return (shortpctfloat - shortpctfloat.rolling(252, min_periods=42).median()).diff()


def f25_sibt_024_shortpctfloat_distance_to_10pct_threshold_d1(shortpctfloat):
    return (shortpctfloat - 10.0).diff()


def f25_sibt_025_shortpctfloat_distance_to_20pct_threshold_d1(shortpctfloat):
    return (shortpctfloat - 20.0).diff()


def f25_sibt_026_shortpctfloat_distance_to_40pct_threshold_d1(shortpctfloat):
    return (shortpctfloat - 40.0).diff()


def f25_sibt_027_shortpctfloat_above_10_indicator_d1(shortpctfloat):
    return ((shortpctfloat > 10.0).astype(float).where(shortpctfloat.notna(), np.nan)).diff()


def f25_sibt_028_shortpctfloat_above_20_indicator_d1(shortpctfloat):
    return ((shortpctfloat > 20.0).astype(float).where(shortpctfloat.notna(), np.nan)).diff()


def f25_sibt_029_shortpctfloat_to_63d_max_d1(shortpctfloat):
    return (_safe_div(shortpctfloat, _rolling_max(shortpctfloat, 63, mp=10))).diff()


def f25_sibt_030_shortpctfloat_acceleration_21_vs_63_d1(shortpctfloat):
    chg_21 = shortpctfloat - shortpctfloat.shift(21)
    chg_63 = shortpctfloat - shortpctfloat.shift(63)
    return (chg_21 - chg_63).diff()


# ---- Block C: % of SHARES OUTSTANDING buildup trajectory (031-045) ----


def f25_sibt_031_shortpctshares_level_d1(shortpctshares):
    return (shortpctshares).diff()


def f25_sibt_032_shortpctshares_ema_21d_d1(shortpctshares):
    return (_ema(shortpctshares, 21, min_periods=5)).diff()


def f25_sibt_033_shortpctshares_ema_63d_d1(shortpctshares):
    return (_ema(shortpctshares, 63, min_periods=10)).diff()


def f25_sibt_034_shortpctshares_change_21d_d1(shortpctshares):
    return (shortpctshares - shortpctshares.shift(21)).diff()


def f25_sibt_035_shortpctshares_change_63d_d1(shortpctshares):
    return (shortpctshares - shortpctshares.shift(63)).diff()


def f25_sibt_036_shortpctshares_change_126d_d1(shortpctshares):
    return (shortpctshares - shortpctshares.shift(126)).diff()


def f25_sibt_037_shortpctshares_pct_change_63d_d1(shortpctshares):
    return (_pct_change(shortpctshares, 63)).diff()


def f25_sibt_038_shortpctshares_minus_252d_median_d1(shortpctshares):
    return (shortpctshares - shortpctshares.rolling(252, min_periods=42).median()).diff()


def f25_sibt_039_float_vs_shares_short_gap_d1(shortpctfloat, shortpctshares):
    return (shortpctfloat - shortpctshares).diff()


def f25_sibt_040_float_vs_shares_short_ratio_d1(shortpctfloat, shortpctshares):
    return (_safe_div(shortpctfloat, shortpctshares)).diff()


def f25_sibt_041_shortpctshares_acceleration_21_vs_63_d1(shortpctshares):
    chg_21 = shortpctshares - shortpctshares.shift(21)
    chg_63 = shortpctshares - shortpctshares.shift(63)
    return (chg_21 - chg_63).diff()


def f25_sibt_042_shortpctshares_above_5pct_indicator_d1(shortpctshares):
    return ((shortpctshares > 5.0).astype(float).where(shortpctshares.notna(), np.nan)).diff()


def f25_sibt_043_shortpctshares_above_15pct_indicator_d1(shortpctshares):
    return ((shortpctshares > 15.0).astype(float).where(shortpctshares.notna(), np.nan)).diff()


def f25_sibt_044_shortpctshares_to_126d_max_d1(shortpctshares):
    return (_safe_div(shortpctshares, _rolling_max(shortpctshares, 126, mp=20))).diff()


def f25_sibt_045_shortpctshares_distance_to_252d_high_d1(shortpctshares):
    return (shortpctshares - _rolling_max(shortpctshares, 252, mp=42)).diff()


# ---- Block D: Days-to-cover (DTC) trajectory (046-060) ----


def f25_sibt_046_daystocover_level_d1(daystocover):
    return (daystocover).diff()


def f25_sibt_047_log_daystocover_d1(daystocover):
    return (_safe_log(daystocover)).diff()


def f25_sibt_048_daystocover_ema_21d_d1(daystocover):
    return (_ema(daystocover, 21, min_periods=5)).diff()


def f25_sibt_049_daystocover_ema_63d_d1(daystocover):
    return (_ema(daystocover, 63, min_periods=10)).diff()


def f25_sibt_050_daystocover_change_21d_d1(daystocover):
    return (daystocover - daystocover.shift(21)).diff()


def f25_sibt_051_daystocover_change_63d_d1(daystocover):
    return (daystocover - daystocover.shift(63)).diff()


def f25_sibt_052_daystocover_change_126d_d1(daystocover):
    return (daystocover - daystocover.shift(126)).diff()


def f25_sibt_053_daystocover_pct_change_63d_d1(daystocover):
    return (_pct_change(daystocover, 63)).diff()


def f25_sibt_054_daystocover_minus_252d_median_d1(daystocover):
    return (daystocover - daystocover.rolling(252, min_periods=42).median()).diff()


def f25_sibt_055_daystocover_to_63d_max_d1(daystocover):
    return (_safe_div(daystocover, _rolling_max(daystocover, 63, mp=10))).diff()


def f25_sibt_056_daystocover_to_252d_max_d1(daystocover):
    return (_safe_div(daystocover, _rolling_max(daystocover, 252, mp=42))).diff()


def f25_sibt_057_daystocover_above_5_indicator_d1(daystocover):
    return ((daystocover > 5.0).astype(float).where(daystocover.notna(), np.nan)).diff()


def f25_sibt_058_daystocover_above_10_indicator_d1(daystocover):
    return ((daystocover > 10.0).astype(float).where(daystocover.notna(), np.nan)).diff()


def f25_sibt_059_daystocover_acceleration_21_vs_63_d1(daystocover):
    chg_21 = daystocover - daystocover.shift(21)
    chg_63 = daystocover - daystocover.shift(63)
    return (chg_21 - chg_63).diff()


def f25_sibt_060_daystocover_ema_ratio_21_to_63_d1(daystocover):
    e21 = _ema(daystocover, 21, min_periods=5)
    e63 = _ema(daystocover, 63, min_periods=10)
    return (_safe_div(e21, e63)).diff()


# ---- Block E: DTC x SI compounding squeeze potential (061-075) ----


def f25_sibt_061_dtc_times_log_shortinterest_d1(daystocover, shortinterest):
    return (daystocover * _safe_log(shortinterest)).diff()


def f25_sibt_062_dtc_times_shortpctfloat_d1(daystocover, shortpctfloat):
    return (daystocover * shortpctfloat).diff()


def f25_sibt_063_dtc_times_shortpctshares_d1(daystocover, shortpctshares):
    return (daystocover * shortpctshares).diff()


def f25_sibt_064_dtc_chg63_times_si_chg63_d1(daystocover, shortinterest):
    dtc_chg = daystocover - daystocover.shift(63)
    si_chg = _pct_change(shortinterest, 63)
    return (dtc_chg * si_chg).diff()


def f25_sibt_065_dtc_chg63_times_spf_chg63_d1(daystocover, shortpctfloat):
    dtc_chg = daystocover - daystocover.shift(63)
    spf_chg = shortpctfloat - shortpctfloat.shift(63)
    return (dtc_chg * spf_chg).diff()


def f25_sibt_066_squeeze_compound_zscore_63d_d1(daystocover, shortpctfloat):
    z_dtc = _rolling_zscore(daystocover, 63)
    z_spf = _rolling_zscore(shortpctfloat, 63)
    return (z_dtc * z_spf).diff()


def f25_sibt_067_squeeze_compound_zscore_126d_d1(daystocover, shortpctfloat):
    z_dtc = _rolling_zscore(daystocover, 126)
    z_spf = _rolling_zscore(shortpctfloat, 126)
    return (z_dtc * z_spf).diff()


def f25_sibt_068_dtc_zscore_63d_d1(daystocover):
    return (_rolling_zscore(daystocover, 63)).diff()


def f25_sibt_069_si_zscore_63d_d1(shortinterest):
    return (_rolling_zscore(shortinterest, 63)).diff()


def f25_sibt_070_spf_zscore_63d_d1(shortpctfloat):
    return (_rolling_zscore(shortpctfloat, 63)).diff()


def f25_sibt_071_dtc_x_spf_both_rising_indicator_d1(daystocover, shortpctfloat):
    dtc_chg = daystocover - daystocover.shift(63)
    spf_chg = shortpctfloat - shortpctfloat.shift(63)
    both = ((dtc_chg > 0) & (spf_chg > 0)).astype(float)
    valid = daystocover.notna() & shortpctfloat.notna()
    return (both.where(valid, np.nan)).diff()


def f25_sibt_072_dtc_plus_spf_compound_chg63_d1(daystocover, shortpctfloat):
    dtc_chg = daystocover - daystocover.shift(63)
    spf_chg = shortpctfloat - shortpctfloat.shift(63)
    return (dtc_chg + spf_chg).diff()


def f25_sibt_073_log_si_times_dtc_chg63_d1(shortinterest, daystocover):
    return (_safe_log(shortinterest) * (daystocover - daystocover.shift(63))).diff()


def f25_sibt_074_dtc_times_si_pct_chg126_d1(daystocover, shortinterest):
    return (daystocover * _pct_change(shortinterest, 126)).diff()


def f25_sibt_075_compound_squeeze_index_d1(daystocover, shortpctfloat, shortinterest):
    return (daystocover * shortpctfloat * _safe_log(shortinterest)).diff()


SHORT_INTEREST_BUILDUP_TRAJECTORY_D1_REGISTRY_001_075 = {
    "f25_sibt_001_log_shortinterest_d1": {"inputs": ["shortinterest"], "func": f25_sibt_001_log_shortinterest_d1},
    "f25_sibt_002_log_shortinterest_ema_21d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_002_log_shortinterest_ema_21d_d1},
    "f25_sibt_003_log_shortinterest_ema_63d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_003_log_shortinterest_ema_63d_d1},
    "f25_sibt_004_shortinterest_to_21d_mean_d1": {"inputs": ["shortinterest"], "func": f25_sibt_004_shortinterest_to_21d_mean_d1},
    "f25_sibt_005_shortinterest_to_63d_mean_d1": {"inputs": ["shortinterest"], "func": f25_sibt_005_shortinterest_to_63d_mean_d1},
    "f25_sibt_006_shortinterest_to_126d_mean_d1": {"inputs": ["shortinterest"], "func": f25_sibt_006_shortinterest_to_126d_mean_d1},
    "f25_sibt_007_shortinterest_to_252d_mean_d1": {"inputs": ["shortinterest"], "func": f25_sibt_007_shortinterest_to_252d_mean_d1},
    "f25_sibt_008_log_shortinterest_minus_log_ema_63d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_008_log_shortinterest_minus_log_ema_63d_d1},
    "f25_sibt_009_shortinterest_pct_change_21d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_009_shortinterest_pct_change_21d_d1},
    "f25_sibt_010_shortinterest_pct_change_63d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_010_shortinterest_pct_change_63d_d1},
    "f25_sibt_011_shortinterest_pct_change_126d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_011_shortinterest_pct_change_126d_d1},
    "f25_sibt_012_log_shortinterest_diff_21d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_012_log_shortinterest_diff_21d_d1},
    "f25_sibt_013_log_shortinterest_diff_63d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_013_log_shortinterest_diff_63d_d1},
    "f25_sibt_014_shortinterest_acceleration_21_vs_63_d1": {"inputs": ["shortinterest"], "func": f25_sibt_014_shortinterest_acceleration_21_vs_63_d1},
    "f25_sibt_015_shortinterest_acceleration_63_vs_252_d1": {"inputs": ["shortinterest"], "func": f25_sibt_015_shortinterest_acceleration_63_vs_252_d1},
    "f25_sibt_016_shortpctfloat_level_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_016_shortpctfloat_level_d1},
    "f25_sibt_017_shortpctfloat_ema_21d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_017_shortpctfloat_ema_21d_d1},
    "f25_sibt_018_shortpctfloat_ema_63d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_018_shortpctfloat_ema_63d_d1},
    "f25_sibt_019_shortpctfloat_change_21d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_019_shortpctfloat_change_21d_d1},
    "f25_sibt_020_shortpctfloat_change_63d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_020_shortpctfloat_change_63d_d1},
    "f25_sibt_021_shortpctfloat_change_126d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_021_shortpctfloat_change_126d_d1},
    "f25_sibt_022_shortpctfloat_pct_change_63d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_022_shortpctfloat_pct_change_63d_d1},
    "f25_sibt_023_shortpctfloat_minus_252d_median_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_023_shortpctfloat_minus_252d_median_d1},
    "f25_sibt_024_shortpctfloat_distance_to_10pct_threshold_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_024_shortpctfloat_distance_to_10pct_threshold_d1},
    "f25_sibt_025_shortpctfloat_distance_to_20pct_threshold_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_025_shortpctfloat_distance_to_20pct_threshold_d1},
    "f25_sibt_026_shortpctfloat_distance_to_40pct_threshold_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_026_shortpctfloat_distance_to_40pct_threshold_d1},
    "f25_sibt_027_shortpctfloat_above_10_indicator_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_027_shortpctfloat_above_10_indicator_d1},
    "f25_sibt_028_shortpctfloat_above_20_indicator_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_028_shortpctfloat_above_20_indicator_d1},
    "f25_sibt_029_shortpctfloat_to_63d_max_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_029_shortpctfloat_to_63d_max_d1},
    "f25_sibt_030_shortpctfloat_acceleration_21_vs_63_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_030_shortpctfloat_acceleration_21_vs_63_d1},
    "f25_sibt_031_shortpctshares_level_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_031_shortpctshares_level_d1},
    "f25_sibt_032_shortpctshares_ema_21d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_032_shortpctshares_ema_21d_d1},
    "f25_sibt_033_shortpctshares_ema_63d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_033_shortpctshares_ema_63d_d1},
    "f25_sibt_034_shortpctshares_change_21d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_034_shortpctshares_change_21d_d1},
    "f25_sibt_035_shortpctshares_change_63d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_035_shortpctshares_change_63d_d1},
    "f25_sibt_036_shortpctshares_change_126d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_036_shortpctshares_change_126d_d1},
    "f25_sibt_037_shortpctshares_pct_change_63d_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_037_shortpctshares_pct_change_63d_d1},
    "f25_sibt_038_shortpctshares_minus_252d_median_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_038_shortpctshares_minus_252d_median_d1},
    "f25_sibt_039_float_vs_shares_short_gap_d1": {"inputs": ["shortpctfloat", "shortpctshares"], "func": f25_sibt_039_float_vs_shares_short_gap_d1},
    "f25_sibt_040_float_vs_shares_short_ratio_d1": {"inputs": ["shortpctfloat", "shortpctshares"], "func": f25_sibt_040_float_vs_shares_short_ratio_d1},
    "f25_sibt_041_shortpctshares_acceleration_21_vs_63_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_041_shortpctshares_acceleration_21_vs_63_d1},
    "f25_sibt_042_shortpctshares_above_5pct_indicator_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_042_shortpctshares_above_5pct_indicator_d1},
    "f25_sibt_043_shortpctshares_above_15pct_indicator_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_043_shortpctshares_above_15pct_indicator_d1},
    "f25_sibt_044_shortpctshares_to_126d_max_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_044_shortpctshares_to_126d_max_d1},
    "f25_sibt_045_shortpctshares_distance_to_252d_high_d1": {"inputs": ["shortpctshares"], "func": f25_sibt_045_shortpctshares_distance_to_252d_high_d1},
    "f25_sibt_046_daystocover_level_d1": {"inputs": ["daystocover"], "func": f25_sibt_046_daystocover_level_d1},
    "f25_sibt_047_log_daystocover_d1": {"inputs": ["daystocover"], "func": f25_sibt_047_log_daystocover_d1},
    "f25_sibt_048_daystocover_ema_21d_d1": {"inputs": ["daystocover"], "func": f25_sibt_048_daystocover_ema_21d_d1},
    "f25_sibt_049_daystocover_ema_63d_d1": {"inputs": ["daystocover"], "func": f25_sibt_049_daystocover_ema_63d_d1},
    "f25_sibt_050_daystocover_change_21d_d1": {"inputs": ["daystocover"], "func": f25_sibt_050_daystocover_change_21d_d1},
    "f25_sibt_051_daystocover_change_63d_d1": {"inputs": ["daystocover"], "func": f25_sibt_051_daystocover_change_63d_d1},
    "f25_sibt_052_daystocover_change_126d_d1": {"inputs": ["daystocover"], "func": f25_sibt_052_daystocover_change_126d_d1},
    "f25_sibt_053_daystocover_pct_change_63d_d1": {"inputs": ["daystocover"], "func": f25_sibt_053_daystocover_pct_change_63d_d1},
    "f25_sibt_054_daystocover_minus_252d_median_d1": {"inputs": ["daystocover"], "func": f25_sibt_054_daystocover_minus_252d_median_d1},
    "f25_sibt_055_daystocover_to_63d_max_d1": {"inputs": ["daystocover"], "func": f25_sibt_055_daystocover_to_63d_max_d1},
    "f25_sibt_056_daystocover_to_252d_max_d1": {"inputs": ["daystocover"], "func": f25_sibt_056_daystocover_to_252d_max_d1},
    "f25_sibt_057_daystocover_above_5_indicator_d1": {"inputs": ["daystocover"], "func": f25_sibt_057_daystocover_above_5_indicator_d1},
    "f25_sibt_058_daystocover_above_10_indicator_d1": {"inputs": ["daystocover"], "func": f25_sibt_058_daystocover_above_10_indicator_d1},
    "f25_sibt_059_daystocover_acceleration_21_vs_63_d1": {"inputs": ["daystocover"], "func": f25_sibt_059_daystocover_acceleration_21_vs_63_d1},
    "f25_sibt_060_daystocover_ema_ratio_21_to_63_d1": {"inputs": ["daystocover"], "func": f25_sibt_060_daystocover_ema_ratio_21_to_63_d1},
    "f25_sibt_061_dtc_times_log_shortinterest_d1": {"inputs": ["daystocover", "shortinterest"], "func": f25_sibt_061_dtc_times_log_shortinterest_d1},
    "f25_sibt_062_dtc_times_shortpctfloat_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_062_dtc_times_shortpctfloat_d1},
    "f25_sibt_063_dtc_times_shortpctshares_d1": {"inputs": ["daystocover", "shortpctshares"], "func": f25_sibt_063_dtc_times_shortpctshares_d1},
    "f25_sibt_064_dtc_chg63_times_si_chg63_d1": {"inputs": ["daystocover", "shortinterest"], "func": f25_sibt_064_dtc_chg63_times_si_chg63_d1},
    "f25_sibt_065_dtc_chg63_times_spf_chg63_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_065_dtc_chg63_times_spf_chg63_d1},
    "f25_sibt_066_squeeze_compound_zscore_63d_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_066_squeeze_compound_zscore_63d_d1},
    "f25_sibt_067_squeeze_compound_zscore_126d_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_067_squeeze_compound_zscore_126d_d1},
    "f25_sibt_068_dtc_zscore_63d_d1": {"inputs": ["daystocover"], "func": f25_sibt_068_dtc_zscore_63d_d1},
    "f25_sibt_069_si_zscore_63d_d1": {"inputs": ["shortinterest"], "func": f25_sibt_069_si_zscore_63d_d1},
    "f25_sibt_070_spf_zscore_63d_d1": {"inputs": ["shortpctfloat"], "func": f25_sibt_070_spf_zscore_63d_d1},
    "f25_sibt_071_dtc_x_spf_both_rising_indicator_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_071_dtc_x_spf_both_rising_indicator_d1},
    "f25_sibt_072_dtc_plus_spf_compound_chg63_d1": {"inputs": ["daystocover", "shortpctfloat"], "func": f25_sibt_072_dtc_plus_spf_compound_chg63_d1},
    "f25_sibt_073_log_si_times_dtc_chg63_d1": {"inputs": ["shortinterest", "daystocover"], "func": f25_sibt_073_log_si_times_dtc_chg63_d1},
    "f25_sibt_074_dtc_times_si_pct_chg126_d1": {"inputs": ["daystocover", "shortinterest"], "func": f25_sibt_074_dtc_times_si_pct_chg126_d1},
    "f25_sibt_075_compound_squeeze_index_d1": {"inputs": ["daystocover", "shortpctfloat", "shortinterest"], "func": f25_sibt_075_compound_squeeze_index_d1},
}
