"""dilution_structure_snapshot d1 features 001_075 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_3Y = 756
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)

def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)

def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)

def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()

def f19_dssp_001_sharesbas_zscore_252d_d1(sharesbas: pd.Series) -> pd.Series:
    return _rolling_zscore(sharesbas, YDAYS).diff()

def f19_dssp_002_sharesbas_zscore_63d_d1(sharesbas: pd.Series) -> pd.Series:
    return _rolling_zscore(sharesbas, QDAYS).diff()

def f19_dssp_003_sharesbas_log_diff_21d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(MDAYS).diff()

def f19_dssp_004_sharesbas_log_diff_63d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(QDAYS).diff()

def f19_dssp_005_sharesbas_log_diff_252d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(YDAYS).diff()

def f19_dssp_006_sharesbas_log_diff_756d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(DDAYS_3Y).diff()

def f19_dssp_007_sharesbas_log_diff_1260d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(DDAYS_5Y).diff()

def f19_dssp_008_sharesbas_pct_change_21d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_div(sharesbas - sharesbas.shift(MDAYS), sharesbas.shift(MDAYS)).diff()

def f19_dssp_009_sharesbas_pct_change_63d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_div(sharesbas - sharesbas.shift(QDAYS), sharesbas.shift(QDAYS)).diff()

def f19_dssp_010_sharesbas_pct_change_252d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_div(sharesbas - sharesbas.shift(YDAYS), sharesbas.shift(YDAYS)).diff()

def f19_dssp_011_sharesbas_rank_pct_252d_d1(sharesbas: pd.Series) -> pd.Series:
    return _rolling_rank_pct(sharesbas, YDAYS).diff()

def f19_dssp_012_sharesbas_distance_to_252d_max_log_d1(sharesbas: pd.Series) -> pd.Series:
    mx = sharesbas.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(sharesbas) - _safe_log(mx)).diff()

def f19_dssp_013_days_since_sharesbas_max_252d_d1(sharesbas: pd.Series) -> pd.Series:
    return _days_since_max(sharesbas, YDAYS).diff()

def f19_dssp_014_days_since_sharesbas_max_756d_d1(sharesbas: pd.Series) -> pd.Series:
    return _days_since_max(sharesbas, DDAYS_3Y).diff()

def f19_dssp_015_sharesbas_at_yearly_max_indicator_d1(sharesbas: pd.Series) -> pd.Series:
    mx = sharesbas.rolling(YDAYS, min_periods=QDAYS).max()
    return ((sharesbas >= mx - 1e-06) & sharesbas.notna() & mx.notna()).astype(float).diff()

def f19_dssp_016_sharesbas_streak_above_long_mean_252d_d1(sharesbas: pd.Series) -> pd.Series:
    m = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (sharesbas > m).astype(int)
    return _streak_above_zero(flag, YDAYS).diff()

def f19_dssp_017_sharesbas_above_p90_count_63d_d1(sharesbas: pd.Series) -> pd.Series:
    thr = sharesbas.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (sharesbas >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f19_dssp_018_sharesbas_above_p99_count_252d_d1(sharesbas: pd.Series) -> pd.Series:
    thr = sharesbas.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (sharesbas >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_019_sharesbas_acceleration_21d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(MDAYS).diff(MDAYS).diff()

def f19_dssp_020_sharesbas_acceleration_63d_d1(sharesbas: pd.Series) -> pd.Series:
    return _safe_log(sharesbas).diff(QDAYS).diff(QDAYS).diff()

def f19_dssp_021_sharesbas_sma_5_to_sma_252_d1(sharesbas: pd.Series) -> pd.Series:
    s5 = sharesbas.rolling(WDAYS, min_periods=2).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s5, s252).diff()

def f19_dssp_022_sharesbas_sma_21_to_sma_252_d1(sharesbas: pd.Series) -> pd.Series:
    s21 = sharesbas.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252).diff()

def f19_dssp_023_sharesbas_sma_63_to_sma_252_d1(sharesbas: pd.Series) -> pd.Series:
    s63 = sharesbas.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s63, s252).diff()

def f19_dssp_024_sharesbas_sma_5_to_sma_63_d1(sharesbas: pd.Series) -> pd.Series:
    s5 = sharesbas.rolling(WDAYS, min_periods=2).mean()
    s63 = sharesbas.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s5, s63).diff()

def f19_dssp_025_sharesbas_ema_log_diff_speed_d1(sharesbas: pd.Series) -> pd.Series:
    e5 = _ema(sharesbas, WDAYS)
    e63 = _ema(sharesbas, QDAYS)
    return (_safe_log(e5) - _safe_log(e63)).diff()

def f19_dssp_026_shareswadil_zscore_252d_d1(shareswadil: pd.Series) -> pd.Series:
    return _rolling_zscore(shareswadil, YDAYS).diff()

def f19_dssp_027_shareswadil_log_diff_21d_d1(shareswadil: pd.Series) -> pd.Series:
    return _safe_log(shareswadil).diff(MDAYS).diff()

def f19_dssp_028_shareswadil_log_diff_63d_d1(shareswadil: pd.Series) -> pd.Series:
    return _safe_log(shareswadil).diff(QDAYS).diff()

def f19_dssp_029_shareswadil_log_diff_252d_d1(shareswadil: pd.Series) -> pd.Series:
    return _safe_log(shareswadil).diff(YDAYS).diff()

def f19_dssp_030_shareswadil_log_diff_756d_d1(shareswadil: pd.Series) -> pd.Series:
    return _safe_log(shareswadil).diff(DDAYS_3Y).diff()

def f19_dssp_031_shareswadil_minus_shareswa_level_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return (shareswadil - shareswa).diff()

def f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_div(shareswadil - shareswa, shareswa).diff()

def f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(QDAYS).diff()

def f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(YDAYS).diff()

def f19_dssp_035_shareswadil_minus_shareswa_zscore_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _rolling_zscore(shareswadil - shareswa, YDAYS).diff()

def f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _rolling_rank_pct(shareswadil - shareswa, YDAYS).diff()

def f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(MDAYS).diff()

def f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    thr = over.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (over >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_039_dilution_overhang_above_5pct_count_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    ratio = _safe_div(shareswadil - shareswa, shareswa)
    flag = (ratio >= 0.05).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_040_dilution_overhang_acceleration_21d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(MDAYS).diff(MDAYS).diff()

def f19_dssp_041_dilution_overhang_acceleration_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(QDAYS).diff(QDAYS).diff()

def f19_dssp_042_dilution_overhang_p90_count_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    thr = over.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (over >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f19_dssp_043_days_since_dilution_overhang_max_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _days_since_max(shareswadil - shareswa, YDAYS).diff()

def f19_dssp_044_dilution_overhang_streak_above_long_mean_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    m = over.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (over > m).astype(int)
    return _streak_above_zero(flag, YDAYS).diff()

def f19_dssp_045_dilution_overhang_zscore_change_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    z = _rolling_zscore(shareswadil - shareswa, YDAYS)
    return z.diff(QDAYS).diff()

def f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    m = over.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (over > m).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f19_dssp_047_shareswadil_vs_sharesbas_ratio_d1(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(shareswadil, sharesbas).diff()

def f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d_d1(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_log(shareswadil) - _safe_log(sharesbas)).diff(MDAYS).diff()

def f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d_d1(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_log(shareswadil) - _safe_log(sharesbas)).diff(QDAYS).diff()

def f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d_d1(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    r = _safe_div(shareswadil, sharesbas)
    thr = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (r >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f19_dssp_051_shareswa_zscore_252d_d1(shareswa: pd.Series) -> pd.Series:
    return _rolling_zscore(shareswa, YDAYS).diff()

def f19_dssp_052_shareswa_log_diff_21d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(MDAYS).diff()

def f19_dssp_053_shareswa_log_diff_63d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(QDAYS).diff()

def f19_dssp_054_shareswa_log_diff_252d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(YDAYS).diff()

def f19_dssp_055_shareswa_log_diff_756d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(DDAYS_3Y).diff()

def f19_dssp_056_shareswa_vs_sharesbas_ratio_d1(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return _safe_div(shareswa, sharesbas).diff()

def f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d_d1(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_log(shareswa) - _safe_log(sharesbas)).diff(QDAYS).diff()

def f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d_d1(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    return (_safe_log(shareswa) - _safe_log(sharesbas)).diff(YDAYS).diff()

def f19_dssp_059_shareswa_pct_change_252d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_div(shareswa - shareswa.shift(YDAYS), shareswa.shift(YDAYS)).diff()

def f19_dssp_060_shareswa_rank_pct_252d_d1(shareswa: pd.Series) -> pd.Series:
    return _rolling_rank_pct(shareswa, YDAYS).diff()

def f19_dssp_061_shareswa_distance_to_252d_max_log_d1(shareswa: pd.Series) -> pd.Series:
    mx = shareswa.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(shareswa) - _safe_log(mx)).diff()

def f19_dssp_062_shareswa_acceleration_21d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(MDAYS).diff(MDAYS).diff()

def f19_dssp_063_shareswa_acceleration_63d_d1(shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswa).diff(QDAYS).diff(QDAYS).diff()

def f19_dssp_064_shareswa_quarterly_step_change_indicator_252d_d1(shareswa: pd.Series) -> pd.Series:
    d = _safe_log(shareswa).diff(MDAYS).abs()
    thr = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (d >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_065_days_since_shareswa_max_252d_d1(shareswa: pd.Series) -> pd.Series:
    return _days_since_max(shareswa, YDAYS).diff()

def f19_dssp_066_sharefactor_log_diff_21d_d1(sharefactor: pd.Series) -> pd.Series:
    return _safe_log(sharefactor).diff(MDAYS).diff()

def f19_dssp_067_sharefactor_log_diff_63d_d1(sharefactor: pd.Series) -> pd.Series:
    return _safe_log(sharefactor).diff(QDAYS).diff()

def f19_dssp_068_sharefactor_log_diff_252d_d1(sharefactor: pd.Series) -> pd.Series:
    return _safe_log(sharefactor).diff(YDAYS).diff()

def f19_dssp_069_sharefactor_increase_event_count_252d_d1(sharefactor: pd.Series) -> pd.Series:
    flag = (sharefactor.diff() > 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_070_days_since_sharefactor_increase_252d_d1(sharefactor: pd.Series) -> pd.Series:
    flag = (sharefactor.diff() > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f19_dssp_071_sharefactor_increase_intensity_252d_d1(sharefactor: pd.Series) -> pd.Series:
    d = sharefactor.diff().clip(lower=0.0)
    return d.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_072_sharefactor_decrease_event_count_252d_d1(sharefactor: pd.Series) -> pd.Series:
    flag = (sharefactor.diff() < 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_073_sharefactor_decrease_intensity_252d_d1(sharefactor: pd.Series) -> pd.Series:
    d = sharefactor.diff().clip(upper=0.0).abs()
    return d.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_074_days_since_sharefactor_decrease_252d_d1(sharefactor: pd.Series) -> pd.Series:
    flag = (sharefactor.diff() < 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f19_dssp_075_sharefactor_reverse_split_indicator_252d_d1(sharefactor: pd.Series) -> pd.Series:
    flag = (sharefactor.diff() < 0).astype(float)
    cnt = flag.rolling(YDAYS, min_periods=QDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan).diff()
DILUTION_STRUCTURE_SNAPSHOT_D1_REGISTRY_001_075 = {'f19_dssp_001_sharesbas_zscore_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_001_sharesbas_zscore_252d_d1}, 'f19_dssp_002_sharesbas_zscore_63d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_002_sharesbas_zscore_63d_d1}, 'f19_dssp_003_sharesbas_log_diff_21d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_003_sharesbas_log_diff_21d_d1}, 'f19_dssp_004_sharesbas_log_diff_63d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_004_sharesbas_log_diff_63d_d1}, 'f19_dssp_005_sharesbas_log_diff_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_005_sharesbas_log_diff_252d_d1}, 'f19_dssp_006_sharesbas_log_diff_756d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_006_sharesbas_log_diff_756d_d1}, 'f19_dssp_007_sharesbas_log_diff_1260d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_007_sharesbas_log_diff_1260d_d1}, 'f19_dssp_008_sharesbas_pct_change_21d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_008_sharesbas_pct_change_21d_d1}, 'f19_dssp_009_sharesbas_pct_change_63d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_009_sharesbas_pct_change_63d_d1}, 'f19_dssp_010_sharesbas_pct_change_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_010_sharesbas_pct_change_252d_d1}, 'f19_dssp_011_sharesbas_rank_pct_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_011_sharesbas_rank_pct_252d_d1}, 'f19_dssp_012_sharesbas_distance_to_252d_max_log_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_012_sharesbas_distance_to_252d_max_log_d1}, 'f19_dssp_013_days_since_sharesbas_max_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_013_days_since_sharesbas_max_252d_d1}, 'f19_dssp_014_days_since_sharesbas_max_756d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_014_days_since_sharesbas_max_756d_d1}, 'f19_dssp_015_sharesbas_at_yearly_max_indicator_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_015_sharesbas_at_yearly_max_indicator_d1}, 'f19_dssp_016_sharesbas_streak_above_long_mean_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_016_sharesbas_streak_above_long_mean_252d_d1}, 'f19_dssp_017_sharesbas_above_p90_count_63d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_017_sharesbas_above_p90_count_63d_d1}, 'f19_dssp_018_sharesbas_above_p99_count_252d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_018_sharesbas_above_p99_count_252d_d1}, 'f19_dssp_019_sharesbas_acceleration_21d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_019_sharesbas_acceleration_21d_d1}, 'f19_dssp_020_sharesbas_acceleration_63d_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_020_sharesbas_acceleration_63d_d1}, 'f19_dssp_021_sharesbas_sma_5_to_sma_252_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_021_sharesbas_sma_5_to_sma_252_d1}, 'f19_dssp_022_sharesbas_sma_21_to_sma_252_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_022_sharesbas_sma_21_to_sma_252_d1}, 'f19_dssp_023_sharesbas_sma_63_to_sma_252_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_023_sharesbas_sma_63_to_sma_252_d1}, 'f19_dssp_024_sharesbas_sma_5_to_sma_63_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_024_sharesbas_sma_5_to_sma_63_d1}, 'f19_dssp_025_sharesbas_ema_log_diff_speed_d1': {'inputs': ['sharesbas'], 'func': f19_dssp_025_sharesbas_ema_log_diff_speed_d1}, 'f19_dssp_026_shareswadil_zscore_252d_d1': {'inputs': ['shareswadil'], 'func': f19_dssp_026_shareswadil_zscore_252d_d1}, 'f19_dssp_027_shareswadil_log_diff_21d_d1': {'inputs': ['shareswadil'], 'func': f19_dssp_027_shareswadil_log_diff_21d_d1}, 'f19_dssp_028_shareswadil_log_diff_63d_d1': {'inputs': ['shareswadil'], 'func': f19_dssp_028_shareswadil_log_diff_63d_d1}, 'f19_dssp_029_shareswadil_log_diff_252d_d1': {'inputs': ['shareswadil'], 'func': f19_dssp_029_shareswadil_log_diff_252d_d1}, 'f19_dssp_030_shareswadil_log_diff_756d_d1': {'inputs': ['shareswadil'], 'func': f19_dssp_030_shareswadil_log_diff_756d_d1}, 'f19_dssp_031_shareswadil_minus_shareswa_level_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_031_shareswadil_minus_shareswa_level_d1}, 'f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa_d1}, 'f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d_d1}, 'f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d_d1}, 'f19_dssp_035_shareswadil_minus_shareswa_zscore_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_035_shareswadil_minus_shareswa_zscore_252d_d1}, 'f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d_d1}, 'f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d_d1}, 'f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d_d1}, 'f19_dssp_039_dilution_overhang_above_5pct_count_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_039_dilution_overhang_above_5pct_count_252d_d1}, 'f19_dssp_040_dilution_overhang_acceleration_21d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_040_dilution_overhang_acceleration_21d_d1}, 'f19_dssp_041_dilution_overhang_acceleration_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_041_dilution_overhang_acceleration_63d_d1}, 'f19_dssp_042_dilution_overhang_p90_count_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_042_dilution_overhang_p90_count_63d_d1}, 'f19_dssp_043_days_since_dilution_overhang_max_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_043_days_since_dilution_overhang_max_252d_d1}, 'f19_dssp_044_dilution_overhang_streak_above_long_mean_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_044_dilution_overhang_streak_above_long_mean_d1}, 'f19_dssp_045_dilution_overhang_zscore_change_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_045_dilution_overhang_zscore_change_63d_d1}, 'f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d_d1}, 'f19_dssp_047_shareswadil_vs_sharesbas_ratio_d1': {'inputs': ['shareswadil', 'sharesbas'], 'func': f19_dssp_047_shareswadil_vs_sharesbas_ratio_d1}, 'f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d_d1': {'inputs': ['shareswadil', 'sharesbas'], 'func': f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d_d1}, 'f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d_d1': {'inputs': ['shareswadil', 'sharesbas'], 'func': f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d_d1}, 'f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d_d1': {'inputs': ['shareswadil', 'sharesbas'], 'func': f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d_d1}, 'f19_dssp_051_shareswa_zscore_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_051_shareswa_zscore_252d_d1}, 'f19_dssp_052_shareswa_log_diff_21d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_052_shareswa_log_diff_21d_d1}, 'f19_dssp_053_shareswa_log_diff_63d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_053_shareswa_log_diff_63d_d1}, 'f19_dssp_054_shareswa_log_diff_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_054_shareswa_log_diff_252d_d1}, 'f19_dssp_055_shareswa_log_diff_756d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_055_shareswa_log_diff_756d_d1}, 'f19_dssp_056_shareswa_vs_sharesbas_ratio_d1': {'inputs': ['shareswa', 'sharesbas'], 'func': f19_dssp_056_shareswa_vs_sharesbas_ratio_d1}, 'f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d_d1': {'inputs': ['shareswa', 'sharesbas'], 'func': f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d_d1}, 'f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d_d1': {'inputs': ['shareswa', 'sharesbas'], 'func': f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d_d1}, 'f19_dssp_059_shareswa_pct_change_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_059_shareswa_pct_change_252d_d1}, 'f19_dssp_060_shareswa_rank_pct_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_060_shareswa_rank_pct_252d_d1}, 'f19_dssp_061_shareswa_distance_to_252d_max_log_d1': {'inputs': ['shareswa'], 'func': f19_dssp_061_shareswa_distance_to_252d_max_log_d1}, 'f19_dssp_062_shareswa_acceleration_21d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_062_shareswa_acceleration_21d_d1}, 'f19_dssp_063_shareswa_acceleration_63d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_063_shareswa_acceleration_63d_d1}, 'f19_dssp_064_shareswa_quarterly_step_change_indicator_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_064_shareswa_quarterly_step_change_indicator_252d_d1}, 'f19_dssp_065_days_since_shareswa_max_252d_d1': {'inputs': ['shareswa'], 'func': f19_dssp_065_days_since_shareswa_max_252d_d1}, 'f19_dssp_066_sharefactor_log_diff_21d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_066_sharefactor_log_diff_21d_d1}, 'f19_dssp_067_sharefactor_log_diff_63d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_067_sharefactor_log_diff_63d_d1}, 'f19_dssp_068_sharefactor_log_diff_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_068_sharefactor_log_diff_252d_d1}, 'f19_dssp_069_sharefactor_increase_event_count_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_069_sharefactor_increase_event_count_252d_d1}, 'f19_dssp_070_days_since_sharefactor_increase_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_070_days_since_sharefactor_increase_252d_d1}, 'f19_dssp_071_sharefactor_increase_intensity_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_071_sharefactor_increase_intensity_252d_d1}, 'f19_dssp_072_sharefactor_decrease_event_count_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_072_sharefactor_decrease_event_count_252d_d1}, 'f19_dssp_073_sharefactor_decrease_intensity_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_073_sharefactor_decrease_intensity_252d_d1}, 'f19_dssp_074_days_since_sharefactor_decrease_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_074_days_since_sharefactor_decrease_252d_d1}, 'f19_dssp_075_sharefactor_reverse_split_indicator_252d_d1': {'inputs': ['sharefactor'], 'func': f19_dssp_075_sharefactor_reverse_split_indicator_252d_d1}}
