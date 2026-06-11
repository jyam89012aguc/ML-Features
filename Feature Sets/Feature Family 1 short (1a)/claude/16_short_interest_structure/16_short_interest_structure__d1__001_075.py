"""short_interest_structure D1 features 001_075 — order-1 derivative wrappers.

Each function inlines the corresponding base computation and appends .diff()
1 times to produce the k-th derivative of that signal. Inputs and PIT
discipline are identical to __base__001_075.py.
NaN-stub policy: all-NaN inputs return pd.Series(np.nan, index=input.index).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lower=0.01, upper=0.99, window=252, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    lo = s.rolling(window, min_periods=min_periods).quantile(lower)
    hi = s.rolling(window, min_periods=min_periods).quantile(upper)
    return s.clip(lower=lo, upper=hi)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _all_nan_stub(*series):
    base = next((x for x in series if isinstance(x, pd.Series)), None)
    if base is None:
        return None
    if all(isinstance(x, pd.Series) and x.isna().all() for x in series):
        return pd.Series(np.nan, index=base.index)
    return None


# ============================================================
#               D1 FEATURES 001_075
# ============================================================


def f16_sint_001_log_short_interest_d1(shortinterest: pd.Series) -> pd.Series:
    return (_safe_log(shortinterest)).diff()


def f16_sint_002_short_interest_level_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.astype(float)).diff()


def f16_sint_003_log_log_short_interest_d1(shortinterest: pd.Series) -> pd.Series:
    return (_safe_log(_safe_log(shortinterest).clip(lower=1e-6))).diff()


def f16_sint_004_si_rank_pct_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(shortinterest, YDAYS)).diff()


def f16_sint_005_si_rank_pct_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(shortinterest, 1260)).diff()


def f16_sint_006_log_si_winsorized_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_winsorize(_safe_log(shortinterest), 0.01, 0.99, YDAYS)).diff()


def f16_sint_007_si_to_float_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_div(shortinterest, sharesbas)).diff()


def f16_sint_008_si_to_avg_volume_21d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return (_safe_div(shortinterest, avgv)).diff()


def f16_sint_009_si_to_avg_volume_63d_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    avgv = volume.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    return (_safe_div(shortinterest, avgv)).diff()


def f16_sint_010_si_to_dollar_volume_21d_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return (_safe_div(shortinterest, dv)).diff()


def f16_sint_011_daystocover_raw_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.astype(float)).diff()


def f16_sint_012_log_daystocover_d1(daystocover: pd.Series) -> pd.Series:
    return (_safe_log(daystocover)).diff()


def f16_sint_013_daystocover_winsorized_252d_d1(daystocover: pd.Series) -> pd.Series:
    return (_winsorize(daystocover, 0.01, 0.99, YDAYS)).diff()


def f16_sint_014_daystocover_zscore_252d_d1(daystocover: pd.Series) -> pd.Series:
    return (_rolling_zscore(daystocover, YDAYS)).diff()


def f16_sint_015_daystocover_zscore_504d_d1(daystocover: pd.Series) -> pd.Series:
    return (_rolling_zscore(daystocover, 504)).diff()


def f16_sint_016_daystocover_zscore_1260d_d1(daystocover: pd.Series) -> pd.Series:
    return (_rolling_zscore(daystocover, 1260)).diff()


def f16_sint_017_daystocover_rank_pct_252d_d1(daystocover: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(daystocover, YDAYS)).diff()


def f16_sint_018_daystocover_rank_pct_1260d_d1(daystocover: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(daystocover, 1260)).diff()


def f16_sint_019_daystocover_distance_to_max_252d_d1(daystocover: pd.Series) -> pd.Series:
    rmax = daystocover.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(daystocover, rmax) - 1.0).diff()


def f16_sint_020_daystocover_distance_to_max_1260d_d1(daystocover: pd.Series) -> pd.Series:
    rmax = daystocover.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(daystocover, rmax) - 1.0).diff()


def f16_sint_021_si_zscore_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest, YDAYS)).diff()


def f16_sint_022_si_zscore_504d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest, 504)).diff()


def f16_sint_023_si_zscore_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_zscore(shortinterest, 1260)).diff()


def f16_sint_024_log_si_zscore_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_zscore(_safe_log(shortinterest), YDAYS)).diff()


def f16_sint_025_log_si_zscore_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_zscore(_safe_log(shortinterest), 1260)).diff()


def f16_sint_026_si_to_float_zscore_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_rolling_zscore(si_f, YDAYS)).diff()


def f16_sint_027_si_to_float_zscore_1260d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_rolling_zscore(si_f, 1260)).diff()


def f16_sint_028_si_distance_to_max_252d_d1(shortinterest: pd.Series) -> pd.Series:
    rmax = shortinterest.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(shortinterest, rmax) - 1.0).diff()


def f16_sint_029_si_distance_to_max_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    rmax = shortinterest.rolling(1260, min_periods=YDAYS).max()
    return (_safe_div(shortinterest, rmax) - 1.0).diff()


def f16_sint_030_si_distance_to_min_252d_d1(shortinterest: pd.Series) -> pd.Series:
    rmin = shortinterest.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(shortinterest, rmin) - 1.0).diff()


def f16_sint_031_si_rank_pct_504d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(shortinterest, 504)).diff()


def f16_sint_032_si_to_float_rank_pct_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_rolling_rank_pct(si_f, YDAYS)).diff()


def f16_sint_033_si_to_float_rank_pct_1260d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (_rolling_rank_pct(si_f, 1260)).diff()


def f16_sint_034_si_to_dollar_volume_rank_pct_252d_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    sd = _safe_div(shortinterest, dv)
    return (_rolling_rank_pct(sd, YDAYS)).diff()


def f16_sint_035_log_si_rank_pct_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(_safe_log(shortinterest), YDAYS)).diff()


def f16_sint_036_log_si_rank_pct_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_rolling_rank_pct(_safe_log(shortinterest), 1260)).diff()


def f16_sint_037_si_quintile_state_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    return ((pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0).diff()


def f16_sint_038_si_quintile_state_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    return ((pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0).diff()


def f16_sint_039_daystocover_quintile_state_252d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, YDAYS)
    return ((pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0).diff()


def f16_sint_040_daystocover_quintile_state_1260d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, 1260)
    return ((pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0).diff()


def f16_sint_041_si_fraction_above_80pct_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.80).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_042_si_fraction_above_80pct_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.80).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_043_si_fraction_above_median_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.50).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_044_si_fraction_above_median_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.50).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_045_si_longest_above_median_streak_252d_d1(shortinterest: pd.Series) -> pd.Series:
    med = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    above = (shortinterest > med).astype(float)
    grp = (above == 0).cumsum()
    cur_streak = above.groupby(grp).cumsum()
    return (cur_streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()


def f16_sint_046_si_longest_above_median_streak_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    med = shortinterest.rolling(1260, min_periods=YDAYS).median()
    above = (shortinterest > med).astype(float)
    grp = (above == 0).cumsum()
    cur_streak = above.groupby(grp).cumsum()
    return (cur_streak.rolling(1260, min_periods=YDAYS).max()).diff()


def f16_sint_047_dtc_fraction_above_80pct_252d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, YDAYS)
    above = (pct >= 0.80).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_048_dtc_fraction_above_80pct_1260d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, 1260)
    above = (pct >= 0.80).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_049_si_persistence_above_own_median_252d_d1(shortinterest: pd.Series) -> pd.Series:
    med = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    above = (shortinterest > med).astype(float)
    cross = above.diff().abs().fillna(0)
    return (1.0 - cross.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS).diff()


def f16_sint_050_si_top_decile_persistence_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.90).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_051_si_top_decile_persistence_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.90).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_052_dtc_top_decile_persistence_252d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, YDAYS)
    above = (pct >= 0.90).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_053_dtc_top_decile_persistence_1260d_d1(daystocover: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(daystocover, 1260)
    above = (pct >= 0.90).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_054_si_fraction_in_top_quartile_252d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.75).astype(float)
    return (above.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f16_sint_055_si_fraction_in_top_quartile_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.75).astype(float)
    return (above.rolling(1260, min_periods=YDAYS).mean()).diff()


def f16_sint_056_si_rolling_std_63d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f16_sint_057_si_rolling_std_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f16_sint_058_si_rolling_std_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    return (shortinterest.rolling(1260, min_periods=YDAYS).std()).diff()


def f16_sint_059_log_si_rolling_std_252d_d1(shortinterest: pd.Series) -> pd.Series:
    return (_safe_log(shortinterest).rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f16_sint_060_dtc_rolling_std_63d_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f16_sint_061_dtc_rolling_std_252d_d1(daystocover: pd.Series) -> pd.Series:
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f16_sint_062_si_cv_252d_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = shortinterest.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(sd, m)).diff()


def f16_sint_063_si_cv_1260d_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    sd = shortinterest.rolling(1260, min_periods=YDAYS).std()
    return (_safe_div(sd, m)).diff()


def f16_sint_064_dtc_cv_252d_d1(daystocover: pd.Series) -> pd.Series:
    m = daystocover.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = daystocover.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(sd, m)).diff()


def f16_sint_065_dtc_cv_1260d_d1(daystocover: pd.Series) -> pd.Series:
    m = daystocover.rolling(1260, min_periods=YDAYS).mean()
    sd = daystocover.rolling(1260, min_periods=YDAYS).std()
    return (_safe_div(sd, m)).diff()


def f16_sint_066_si_to_float_rolling_std_252d_d1(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    si_f = _safe_div(shortinterest, sharesbas)
    return (si_f.rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f16_sint_067_si_rolling_iqr_252d_d1(shortinterest: pd.Series) -> pd.Series:
    q3 = shortinterest.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = shortinterest.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q3 - q1).diff()


def f16_sint_068_dtc_rolling_iqr_252d_d1(daystocover: pd.Series) -> pd.Series:
    q3 = daystocover.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = daystocover.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q3 - q1).diff()


def f16_sint_069_log_si_rolling_iqr_252d_d1(shortinterest: pd.Series) -> pd.Series:
    ls = _safe_log(shortinterest)
    q3 = ls.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = ls.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q3 - q1).diff()


def f16_sint_070_si_stability_score_252d_d1(shortinterest: pd.Series) -> pd.Series:
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = shortinterest.rolling(YDAYS, min_periods=QDAYS).std()
    cv = _safe_div(sd, m)
    return (1.0 / (1.0 + cv)).diff()


def f16_sint_071_corr_si_close_252d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(close)).diff()


def f16_sint_072_corr_dtc_close_252d_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    return (daystocover.rolling(YDAYS, min_periods=QDAYS).corr(close)).diff()


def f16_sint_073_corr_si_close_504d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (shortinterest.rolling(504, min_periods=YDAYS).corr(close)).diff()


def f16_sint_074_corr_dtc_close_504d_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    return (daystocover.rolling(504, min_periods=YDAYS).corr(close)).diff()


def f16_sint_075_corr_si_close_1260d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    return (shortinterest.rolling(1260, min_periods=YDAYS).corr(close)).diff()


# ============================================================
#                     REGISTRY
# ============================================================

SHORT_INTEREST_STRUCTURE_D1_REGISTRY_001_075 = {
    "f16_sint_001_log_short_interest_d1": {"inputs": ["shortinterest"], "func": f16_sint_001_log_short_interest_d1},
    "f16_sint_002_short_interest_level_d1": {"inputs": ["shortinterest"], "func": f16_sint_002_short_interest_level_d1},
    "f16_sint_003_log_log_short_interest_d1": {"inputs": ["shortinterest"], "func": f16_sint_003_log_log_short_interest_d1},
    "f16_sint_004_si_rank_pct_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_004_si_rank_pct_252d_d1},
    "f16_sint_005_si_rank_pct_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_005_si_rank_pct_1260d_d1},
    "f16_sint_006_log_si_winsorized_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_006_log_si_winsorized_252d_d1},
    "f16_sint_007_si_to_float_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_007_si_to_float_d1},
    "f16_sint_008_si_to_avg_volume_21d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_008_si_to_avg_volume_21d_d1},
    "f16_sint_009_si_to_avg_volume_63d_d1": {"inputs": ["shortinterest", "volume"], "func": f16_sint_009_si_to_avg_volume_63d_d1},
    "f16_sint_010_si_to_dollar_volume_21d_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_010_si_to_dollar_volume_21d_d1},
    "f16_sint_011_daystocover_raw_d1": {"inputs": ["daystocover"], "func": f16_sint_011_daystocover_raw_d1},
    "f16_sint_012_log_daystocover_d1": {"inputs": ["daystocover"], "func": f16_sint_012_log_daystocover_d1},
    "f16_sint_013_daystocover_winsorized_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_013_daystocover_winsorized_252d_d1},
    "f16_sint_014_daystocover_zscore_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_014_daystocover_zscore_252d_d1},
    "f16_sint_015_daystocover_zscore_504d_d1": {"inputs": ["daystocover"], "func": f16_sint_015_daystocover_zscore_504d_d1},
    "f16_sint_016_daystocover_zscore_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_016_daystocover_zscore_1260d_d1},
    "f16_sint_017_daystocover_rank_pct_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_017_daystocover_rank_pct_252d_d1},
    "f16_sint_018_daystocover_rank_pct_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_018_daystocover_rank_pct_1260d_d1},
    "f16_sint_019_daystocover_distance_to_max_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_019_daystocover_distance_to_max_252d_d1},
    "f16_sint_020_daystocover_distance_to_max_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_020_daystocover_distance_to_max_1260d_d1},
    "f16_sint_021_si_zscore_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_021_si_zscore_252d_d1},
    "f16_sint_022_si_zscore_504d_d1": {"inputs": ["shortinterest"], "func": f16_sint_022_si_zscore_504d_d1},
    "f16_sint_023_si_zscore_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_023_si_zscore_1260d_d1},
    "f16_sint_024_log_si_zscore_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_024_log_si_zscore_252d_d1},
    "f16_sint_025_log_si_zscore_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_025_log_si_zscore_1260d_d1},
    "f16_sint_026_si_to_float_zscore_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_026_si_to_float_zscore_252d_d1},
    "f16_sint_027_si_to_float_zscore_1260d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_027_si_to_float_zscore_1260d_d1},
    "f16_sint_028_si_distance_to_max_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_028_si_distance_to_max_252d_d1},
    "f16_sint_029_si_distance_to_max_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_029_si_distance_to_max_1260d_d1},
    "f16_sint_030_si_distance_to_min_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_030_si_distance_to_min_252d_d1},
    "f16_sint_031_si_rank_pct_504d_d1": {"inputs": ["shortinterest"], "func": f16_sint_031_si_rank_pct_504d_d1},
    "f16_sint_032_si_to_float_rank_pct_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_032_si_to_float_rank_pct_252d_d1},
    "f16_sint_033_si_to_float_rank_pct_1260d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_033_si_to_float_rank_pct_1260d_d1},
    "f16_sint_034_si_to_dollar_volume_rank_pct_252d_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_034_si_to_dollar_volume_rank_pct_252d_d1},
    "f16_sint_035_log_si_rank_pct_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_035_log_si_rank_pct_252d_d1},
    "f16_sint_036_log_si_rank_pct_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_036_log_si_rank_pct_1260d_d1},
    "f16_sint_037_si_quintile_state_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_037_si_quintile_state_252d_d1},
    "f16_sint_038_si_quintile_state_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_038_si_quintile_state_1260d_d1},
    "f16_sint_039_daystocover_quintile_state_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_039_daystocover_quintile_state_252d_d1},
    "f16_sint_040_daystocover_quintile_state_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_040_daystocover_quintile_state_1260d_d1},
    "f16_sint_041_si_fraction_above_80pct_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_041_si_fraction_above_80pct_252d_d1},
    "f16_sint_042_si_fraction_above_80pct_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_042_si_fraction_above_80pct_1260d_d1},
    "f16_sint_043_si_fraction_above_median_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_043_si_fraction_above_median_252d_d1},
    "f16_sint_044_si_fraction_above_median_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_044_si_fraction_above_median_1260d_d1},
    "f16_sint_045_si_longest_above_median_streak_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_045_si_longest_above_median_streak_252d_d1},
    "f16_sint_046_si_longest_above_median_streak_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_046_si_longest_above_median_streak_1260d_d1},
    "f16_sint_047_dtc_fraction_above_80pct_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_047_dtc_fraction_above_80pct_252d_d1},
    "f16_sint_048_dtc_fraction_above_80pct_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_048_dtc_fraction_above_80pct_1260d_d1},
    "f16_sint_049_si_persistence_above_own_median_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_049_si_persistence_above_own_median_252d_d1},
    "f16_sint_050_si_top_decile_persistence_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_050_si_top_decile_persistence_252d_d1},
    "f16_sint_051_si_top_decile_persistence_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_051_si_top_decile_persistence_1260d_d1},
    "f16_sint_052_dtc_top_decile_persistence_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_052_dtc_top_decile_persistence_252d_d1},
    "f16_sint_053_dtc_top_decile_persistence_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_053_dtc_top_decile_persistence_1260d_d1},
    "f16_sint_054_si_fraction_in_top_quartile_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_054_si_fraction_in_top_quartile_252d_d1},
    "f16_sint_055_si_fraction_in_top_quartile_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_055_si_fraction_in_top_quartile_1260d_d1},
    "f16_sint_056_si_rolling_std_63d_d1": {"inputs": ["shortinterest"], "func": f16_sint_056_si_rolling_std_63d_d1},
    "f16_sint_057_si_rolling_std_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_057_si_rolling_std_252d_d1},
    "f16_sint_058_si_rolling_std_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_058_si_rolling_std_1260d_d1},
    "f16_sint_059_log_si_rolling_std_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_059_log_si_rolling_std_252d_d1},
    "f16_sint_060_dtc_rolling_std_63d_d1": {"inputs": ["daystocover"], "func": f16_sint_060_dtc_rolling_std_63d_d1},
    "f16_sint_061_dtc_rolling_std_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_061_dtc_rolling_std_252d_d1},
    "f16_sint_062_si_cv_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_062_si_cv_252d_d1},
    "f16_sint_063_si_cv_1260d_d1": {"inputs": ["shortinterest"], "func": f16_sint_063_si_cv_1260d_d1},
    "f16_sint_064_dtc_cv_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_064_dtc_cv_252d_d1},
    "f16_sint_065_dtc_cv_1260d_d1": {"inputs": ["daystocover"], "func": f16_sint_065_dtc_cv_1260d_d1},
    "f16_sint_066_si_to_float_rolling_std_252d_d1": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_066_si_to_float_rolling_std_252d_d1},
    "f16_sint_067_si_rolling_iqr_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_067_si_rolling_iqr_252d_d1},
    "f16_sint_068_dtc_rolling_iqr_252d_d1": {"inputs": ["daystocover"], "func": f16_sint_068_dtc_rolling_iqr_252d_d1},
    "f16_sint_069_log_si_rolling_iqr_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_069_log_si_rolling_iqr_252d_d1},
    "f16_sint_070_si_stability_score_252d_d1": {"inputs": ["shortinterest"], "func": f16_sint_070_si_stability_score_252d_d1},
    "f16_sint_071_corr_si_close_252d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_071_corr_si_close_252d_d1},
    "f16_sint_072_corr_dtc_close_252d_d1": {"inputs": ["daystocover", "close"], "func": f16_sint_072_corr_dtc_close_252d_d1},
    "f16_sint_073_corr_si_close_504d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_073_corr_si_close_504d_d1},
    "f16_sint_074_corr_dtc_close_504d_d1": {"inputs": ["daystocover", "close"], "func": f16_sint_074_corr_dtc_close_504d_d1},
    "f16_sint_075_corr_si_close_1260d_d1": {"inputs": ["shortinterest", "close"], "func": f16_sint_075_corr_si_close_1260d_d1},
}
