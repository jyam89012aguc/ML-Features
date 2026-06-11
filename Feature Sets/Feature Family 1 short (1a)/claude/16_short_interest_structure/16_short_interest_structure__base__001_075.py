"""short_interest_structure base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct STRUCTURE hypotheses (continued in __base__076_150.py for 150 total).
Inputs: NSIR (shortinterest, daystocover) forward-filled to daily by binder,
plus SEP (volume, close) and SF1 (sharesbas) for normalization.
NaN-stub policy: all-NaN inputs return pd.Series(np.nan, index=input.index).
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
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
#                BASE FEATURES 001-075
# ============================================================


def f16_sint_001_log_short_interest(shortinterest: pd.Series) -> pd.Series:
    """Log short interest — level."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _safe_log(shortinterest)


def f16_sint_002_short_interest_level(shortinterest: pd.Series) -> pd.Series:
    """Raw short interest — shares short."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.astype(float)


def f16_sint_003_log_log_short_interest(shortinterest: pd.Series) -> pd.Series:
    """Log of log short interest — heavy-tail compression."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _safe_log(_safe_log(shortinterest).clip(lower=1e-6))


def f16_sint_004_si_rank_pct_252d(shortinterest: pd.Series) -> pd.Series:
    """Rank-percentile of SI within own 252d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_rank_pct(shortinterest, YDAYS)


def f16_sint_005_si_rank_pct_1260d(shortinterest: pd.Series) -> pd.Series:
    """Rank-percentile of SI within own 5y window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_rank_pct(shortinterest, 1260)


def f16_sint_006_log_si_winsorized_252d(shortinterest: pd.Series) -> pd.Series:
    """Winsorized log SI (1-99 pct, 252d window)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _winsorize(_safe_log(shortinterest), 0.01, 0.99, YDAYS)


def f16_sint_007_si_to_float(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """SI as fraction of float (sharesbas)."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    return _safe_div(shortinterest, sharesbas)


def f16_sint_008_si_to_avg_volume_21d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """SI divided by 21d avg volume — short-horizon DTC proxy."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    avgv = volume.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return _safe_div(shortinterest, avgv)


def f16_sint_009_si_to_avg_volume_63d(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """SI divided by 63d avg volume — quarter-horizon DTC proxy."""
    stub = _all_nan_stub(shortinterest, volume)
    if stub is not None:
        return stub
    avgv = volume.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean()
    return _safe_div(shortinterest, avgv)


def f16_sint_010_si_to_dollar_volume_21d(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """SI shares divided by 21d avg dollar volume (close*volume)."""
    stub = _all_nan_stub(shortinterest, close, volume)
    if stub is not None:
        return stub
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    return _safe_div(shortinterest, dv)


def f16_sint_011_daystocover_raw(daystocover: pd.Series) -> pd.Series:
    """Raw days-to-cover."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.astype(float)


def f16_sint_012_log_daystocover(daystocover: pd.Series) -> pd.Series:
    """Log days-to-cover — compress heavy tail."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _safe_log(daystocover)


def f16_sint_013_daystocover_winsorized_252d(daystocover: pd.Series) -> pd.Series:
    """Winsorized DTC (1-99 pct, 252d)."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _winsorize(daystocover, 0.01, 0.99, YDAYS)


def f16_sint_014_daystocover_zscore_252d(daystocover: pd.Series) -> pd.Series:
    """DTC z-score vs own 252d distribution — annual regime."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _rolling_zscore(daystocover, YDAYS)


def f16_sint_015_daystocover_zscore_504d(daystocover: pd.Series) -> pd.Series:
    """DTC z-score vs own 504d distribution — 2y regime."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _rolling_zscore(daystocover, 504)


def f16_sint_016_daystocover_zscore_1260d(daystocover: pd.Series) -> pd.Series:
    """DTC z-score vs own 1260d distribution — 5y regime."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _rolling_zscore(daystocover, 1260)


def f16_sint_017_daystocover_rank_pct_252d(daystocover: pd.Series) -> pd.Series:
    """DTC percentile rank vs own 252d distribution."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _rolling_rank_pct(daystocover, YDAYS)


def f16_sint_018_daystocover_rank_pct_1260d(daystocover: pd.Series) -> pd.Series:
    """DTC percentile rank vs own 1260d distribution."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return _rolling_rank_pct(daystocover, 1260)


def f16_sint_019_daystocover_distance_to_max_252d(daystocover: pd.Series) -> pd.Series:
    """DTC distance below 252d max, as a ratio (current/max - 1)."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    rmax = daystocover.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(daystocover, rmax) - 1.0


def f16_sint_020_daystocover_distance_to_max_1260d(daystocover: pd.Series) -> pd.Series:
    """DTC distance below 1260d max."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    rmax = daystocover.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(daystocover, rmax) - 1.0


def f16_sint_021_si_zscore_252d(shortinterest: pd.Series) -> pd.Series:
    """SI z-score vs own 252d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest, YDAYS)


def f16_sint_022_si_zscore_504d(shortinterest: pd.Series) -> pd.Series:
    """SI z-score vs own 504d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest, 504)


def f16_sint_023_si_zscore_1260d(shortinterest: pd.Series) -> pd.Series:
    """SI z-score vs own 1260d (5y) window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_zscore(shortinterest, 1260)


def f16_sint_024_log_si_zscore_252d(shortinterest: pd.Series) -> pd.Series:
    """Log-SI z-score vs own 252d — heavy-tail robust regime."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_zscore(_safe_log(shortinterest), YDAYS)


def f16_sint_025_log_si_zscore_1260d(shortinterest: pd.Series) -> pd.Series:
    """Log-SI z-score vs own 1260d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_zscore(_safe_log(shortinterest), 1260)


def f16_sint_026_si_to_float_zscore_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """SI/float z-score vs own 252d window."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _rolling_zscore(si_f, YDAYS)


def f16_sint_027_si_to_float_zscore_1260d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """SI/float z-score vs own 1260d window."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _rolling_zscore(si_f, 1260)


def f16_sint_028_si_distance_to_max_252d(shortinterest: pd.Series) -> pd.Series:
    """SI distance to own 252d max (current/max - 1)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    rmax = shortinterest.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(shortinterest, rmax) - 1.0


def f16_sint_029_si_distance_to_max_1260d(shortinterest: pd.Series) -> pd.Series:
    """SI distance to own 1260d max."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    rmax = shortinterest.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(shortinterest, rmax) - 1.0


def f16_sint_030_si_distance_to_min_252d(shortinterest: pd.Series) -> pd.Series:
    """SI distance above own 252d min (current/min - 1)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    rmin = shortinterest.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(shortinterest, rmin) - 1.0


def f16_sint_031_si_rank_pct_504d(shortinterest: pd.Series) -> pd.Series:
    """Rank-percentile of SI within own 504d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_rank_pct(shortinterest, 504)


def f16_sint_032_si_to_float_rank_pct_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rank-pct of SI/float within own 252d window."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _rolling_rank_pct(si_f, YDAYS)


def f16_sint_033_si_to_float_rank_pct_1260d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rank-pct of SI/float within own 1260d window."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return _rolling_rank_pct(si_f, 1260)


def f16_sint_034_si_to_dollar_volume_rank_pct_252d(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rank-pct of SI/avg dollar volume within own 252d window."""
    stub = _all_nan_stub(shortinterest, close, volume)
    if stub is not None:
        return stub
    dv = (close * volume).rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).mean()
    sd = _safe_div(shortinterest, dv)
    return _rolling_rank_pct(sd, YDAYS)


def f16_sint_035_log_si_rank_pct_252d(shortinterest: pd.Series) -> pd.Series:
    """Rank-pct of log SI within own 252d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_rank_pct(_safe_log(shortinterest), YDAYS)


def f16_sint_036_log_si_rank_pct_1260d(shortinterest: pd.Series) -> pd.Series:
    """Rank-pct of log SI within own 1260d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _rolling_rank_pct(_safe_log(shortinterest), 1260)


def f16_sint_037_si_quintile_state_252d(shortinterest: pd.Series) -> pd.Series:
    """Current SI quintile (1-5) within own 252d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    return (pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0


def f16_sint_038_si_quintile_state_1260d(shortinterest: pd.Series) -> pd.Series:
    """Current SI quintile (1-5) within own 1260d window."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    return (pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0


def f16_sint_039_daystocover_quintile_state_252d(daystocover: pd.Series) -> pd.Series:
    """Current DTC quintile (1-5) within own 252d window."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, YDAYS)
    return (pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0


def f16_sint_040_daystocover_quintile_state_1260d(daystocover: pd.Series) -> pd.Series:
    """Current DTC quintile (1-5) within own 1260d window."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, 1260)
    return (pct * 5.0).clip(upper=4.999).apply(np.floor) + 1.0


def f16_sint_041_si_fraction_above_80pct_252d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where SI percentile >= 0.80 — structural persistence in top quintile."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.80).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_042_si_fraction_above_80pct_1260d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of last 1260 bars where SI percentile >= 0.80 over 1260d hist."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.80).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_043_si_fraction_above_median_252d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where SI percentile >= 0.50."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.50).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_044_si_fraction_above_median_1260d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of last 1260 bars where SI percentile >= 0.50."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.50).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_045_si_longest_above_median_streak_252d(shortinterest: pd.Series) -> pd.Series:
    """Longest consecutive run of SI above 252d median, measured rolling."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    med = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    above = (shortinterest > med).astype(float)
    grp = (above == 0).cumsum()
    cur_streak = above.groupby(grp).cumsum()
    return cur_streak.rolling(YDAYS, min_periods=QDAYS).max()


def f16_sint_046_si_longest_above_median_streak_1260d(shortinterest: pd.Series) -> pd.Series:
    """Longest consecutive run of SI above 1260d median, measured rolling."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    med = shortinterest.rolling(1260, min_periods=YDAYS).median()
    above = (shortinterest > med).astype(float)
    grp = (above == 0).cumsum()
    cur_streak = above.groupby(grp).cumsum()
    return cur_streak.rolling(1260, min_periods=YDAYS).max()


def f16_sint_047_dtc_fraction_above_80pct_252d(daystocover: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where DTC percentile >= 0.80."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, YDAYS)
    above = (pct >= 0.80).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_048_dtc_fraction_above_80pct_1260d(daystocover: pd.Series) -> pd.Series:
    """Fraction of last 1260 bars where DTC percentile >= 0.80."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, 1260)
    above = (pct >= 0.80).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_049_si_persistence_above_own_median_252d(shortinterest: pd.Series) -> pd.Series:
    """Persistence proxy: 1 - count of crossings/N. High = sticky regime."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    med = shortinterest.rolling(YDAYS, min_periods=QDAYS).median()
    above = (shortinterest > med).astype(float)
    cross = above.diff().abs().fillna(0)
    return 1.0 - cross.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS


def f16_sint_050_si_top_decile_persistence_252d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of 252 bars where SI percentile >= 0.90."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.90).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_051_si_top_decile_persistence_1260d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of 1260 bars where SI percentile (1260d) >= 0.90."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.90).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_052_dtc_top_decile_persistence_252d(daystocover: pd.Series) -> pd.Series:
    """Fraction of 252 bars where DTC percentile (252d) >= 0.90."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, YDAYS)
    above = (pct >= 0.90).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_053_dtc_top_decile_persistence_1260d(daystocover: pd.Series) -> pd.Series:
    """Fraction of 1260 bars where DTC percentile (1260d) >= 0.90."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(daystocover, 1260)
    above = (pct >= 0.90).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_054_si_fraction_in_top_quartile_252d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of 252 bars where SI rank-pct (252d) >= 0.75."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, YDAYS)
    above = (pct >= 0.75).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_sint_055_si_fraction_in_top_quartile_1260d(shortinterest: pd.Series) -> pd.Series:
    """Fraction of 1260 bars where SI rank-pct (1260d) >= 0.75."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    pct = _rolling_rank_pct(shortinterest, 1260)
    above = (pct >= 0.75).astype(float)
    return above.rolling(1260, min_periods=YDAYS).mean()


def f16_sint_056_si_rolling_std_63d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 63d std of SI — short-horizon stickiness inverse."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(QDAYS, min_periods=MDAYS).std()


def f16_sint_057_si_rolling_std_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d std of SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).std()


def f16_sint_058_si_rolling_std_1260d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 1260d std of SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return shortinterest.rolling(1260, min_periods=YDAYS).std()


def f16_sint_059_log_si_rolling_std_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d std of log SI — proportional volatility."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    return _safe_log(shortinterest).rolling(YDAYS, min_periods=QDAYS).std()


def f16_sint_060_dtc_rolling_std_63d(daystocover: pd.Series) -> pd.Series:
    """Rolling 63d std of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.rolling(QDAYS, min_periods=MDAYS).std()


def f16_sint_061_dtc_rolling_std_252d(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d std of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    return daystocover.rolling(YDAYS, min_periods=QDAYS).std()


def f16_sint_062_si_cv_252d(shortinterest: pd.Series) -> pd.Series:
    """SI coefficient of variation over 252d (std/mean)."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = shortinterest.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd, m)


def f16_sint_063_si_cv_1260d(shortinterest: pd.Series) -> pd.Series:
    """SI coefficient of variation over 1260d."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(1260, min_periods=YDAYS).mean()
    sd = shortinterest.rolling(1260, min_periods=YDAYS).std()
    return _safe_div(sd, m)


def f16_sint_064_dtc_cv_252d(daystocover: pd.Series) -> pd.Series:
    """DTC coefficient of variation over 252d."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    m = daystocover.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = daystocover.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd, m)


def f16_sint_065_dtc_cv_1260d(daystocover: pd.Series) -> pd.Series:
    """DTC coefficient of variation over 1260d."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    m = daystocover.rolling(1260, min_periods=YDAYS).mean()
    sd = daystocover.rolling(1260, min_periods=YDAYS).std()
    return _safe_div(sd, m)


def f16_sint_066_si_to_float_rolling_std_252d(shortinterest: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 252d std of SI/float."""
    stub = _all_nan_stub(shortinterest, sharesbas)
    if stub is not None:
        return stub
    si_f = _safe_div(shortinterest, sharesbas)
    return si_f.rolling(YDAYS, min_periods=QDAYS).std()


def f16_sint_067_si_rolling_iqr_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d interquartile range of SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    q3 = shortinterest.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = shortinterest.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q3 - q1


def f16_sint_068_dtc_rolling_iqr_252d(daystocover: pd.Series) -> pd.Series:
    """Rolling 252d IQR of DTC."""
    stub = _all_nan_stub(daystocover)
    if stub is not None:
        return stub
    q3 = daystocover.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = daystocover.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q3 - q1


def f16_sint_069_log_si_rolling_iqr_252d(shortinterest: pd.Series) -> pd.Series:
    """Rolling 252d IQR of log SI."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    ls = _safe_log(shortinterest)
    q3 = ls.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q1 = ls.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q3 - q1


def f16_sint_070_si_stability_score_252d(shortinterest: pd.Series) -> pd.Series:
    """Stability = 1 / (1 + CV_252d) — high when SI level is consistent."""
    stub = _all_nan_stub(shortinterest)
    if stub is not None:
        return stub
    m = shortinterest.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = shortinterest.rolling(YDAYS, min_periods=QDAYS).std()
    cv = _safe_div(sd, m)
    return 1.0 / (1.0 + cv)


def f16_sint_071_corr_si_close_252d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr between SI and close — positive = abnormal squeeze setup."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return shortinterest.rolling(YDAYS, min_periods=QDAYS).corr(close)


def f16_sint_072_corr_dtc_close_252d(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr between DTC and close."""
    stub = _all_nan_stub(daystocover, close)
    if stub is not None:
        return stub
    return daystocover.rolling(YDAYS, min_periods=QDAYS).corr(close)


def f16_sint_073_corr_si_close_504d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 504d corr between SI and close."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return shortinterest.rolling(504, min_periods=YDAYS).corr(close)


def f16_sint_074_corr_dtc_close_504d(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 504d corr between DTC and close."""
    stub = _all_nan_stub(daystocover, close)
    if stub is not None:
        return stub
    return daystocover.rolling(504, min_periods=YDAYS).corr(close)


def f16_sint_075_corr_si_close_1260d(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 1260d corr between SI and close — long-horizon co-movement."""
    stub = _all_nan_stub(shortinterest, close)
    if stub is not None:
        return stub
    return shortinterest.rolling(1260, min_periods=YDAYS).corr(close)


# ============================================================
#                     REGISTRY
# ============================================================

SHORT_INTEREST_STRUCTURE_BASE_REGISTRY_001_075 = {
    "f16_sint_001_log_short_interest": {"inputs": ["shortinterest"], "func": f16_sint_001_log_short_interest},
    "f16_sint_002_short_interest_level": {"inputs": ["shortinterest"], "func": f16_sint_002_short_interest_level},
    "f16_sint_003_log_log_short_interest": {"inputs": ["shortinterest"], "func": f16_sint_003_log_log_short_interest},
    "f16_sint_004_si_rank_pct_252d": {"inputs": ["shortinterest"], "func": f16_sint_004_si_rank_pct_252d},
    "f16_sint_005_si_rank_pct_1260d": {"inputs": ["shortinterest"], "func": f16_sint_005_si_rank_pct_1260d},
    "f16_sint_006_log_si_winsorized_252d": {"inputs": ["shortinterest"], "func": f16_sint_006_log_si_winsorized_252d},
    "f16_sint_007_si_to_float": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_007_si_to_float},
    "f16_sint_008_si_to_avg_volume_21d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_008_si_to_avg_volume_21d},
    "f16_sint_009_si_to_avg_volume_63d": {"inputs": ["shortinterest", "volume"], "func": f16_sint_009_si_to_avg_volume_63d},
    "f16_sint_010_si_to_dollar_volume_21d": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_010_si_to_dollar_volume_21d},
    "f16_sint_011_daystocover_raw": {"inputs": ["daystocover"], "func": f16_sint_011_daystocover_raw},
    "f16_sint_012_log_daystocover": {"inputs": ["daystocover"], "func": f16_sint_012_log_daystocover},
    "f16_sint_013_daystocover_winsorized_252d": {"inputs": ["daystocover"], "func": f16_sint_013_daystocover_winsorized_252d},
    "f16_sint_014_daystocover_zscore_252d": {"inputs": ["daystocover"], "func": f16_sint_014_daystocover_zscore_252d},
    "f16_sint_015_daystocover_zscore_504d": {"inputs": ["daystocover"], "func": f16_sint_015_daystocover_zscore_504d},
    "f16_sint_016_daystocover_zscore_1260d": {"inputs": ["daystocover"], "func": f16_sint_016_daystocover_zscore_1260d},
    "f16_sint_017_daystocover_rank_pct_252d": {"inputs": ["daystocover"], "func": f16_sint_017_daystocover_rank_pct_252d},
    "f16_sint_018_daystocover_rank_pct_1260d": {"inputs": ["daystocover"], "func": f16_sint_018_daystocover_rank_pct_1260d},
    "f16_sint_019_daystocover_distance_to_max_252d": {"inputs": ["daystocover"], "func": f16_sint_019_daystocover_distance_to_max_252d},
    "f16_sint_020_daystocover_distance_to_max_1260d": {"inputs": ["daystocover"], "func": f16_sint_020_daystocover_distance_to_max_1260d},
    "f16_sint_021_si_zscore_252d": {"inputs": ["shortinterest"], "func": f16_sint_021_si_zscore_252d},
    "f16_sint_022_si_zscore_504d": {"inputs": ["shortinterest"], "func": f16_sint_022_si_zscore_504d},
    "f16_sint_023_si_zscore_1260d": {"inputs": ["shortinterest"], "func": f16_sint_023_si_zscore_1260d},
    "f16_sint_024_log_si_zscore_252d": {"inputs": ["shortinterest"], "func": f16_sint_024_log_si_zscore_252d},
    "f16_sint_025_log_si_zscore_1260d": {"inputs": ["shortinterest"], "func": f16_sint_025_log_si_zscore_1260d},
    "f16_sint_026_si_to_float_zscore_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_026_si_to_float_zscore_252d},
    "f16_sint_027_si_to_float_zscore_1260d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_027_si_to_float_zscore_1260d},
    "f16_sint_028_si_distance_to_max_252d": {"inputs": ["shortinterest"], "func": f16_sint_028_si_distance_to_max_252d},
    "f16_sint_029_si_distance_to_max_1260d": {"inputs": ["shortinterest"], "func": f16_sint_029_si_distance_to_max_1260d},
    "f16_sint_030_si_distance_to_min_252d": {"inputs": ["shortinterest"], "func": f16_sint_030_si_distance_to_min_252d},
    "f16_sint_031_si_rank_pct_504d": {"inputs": ["shortinterest"], "func": f16_sint_031_si_rank_pct_504d},
    "f16_sint_032_si_to_float_rank_pct_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_032_si_to_float_rank_pct_252d},
    "f16_sint_033_si_to_float_rank_pct_1260d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_033_si_to_float_rank_pct_1260d},
    "f16_sint_034_si_to_dollar_volume_rank_pct_252d": {"inputs": ["shortinterest", "close", "volume"], "func": f16_sint_034_si_to_dollar_volume_rank_pct_252d},
    "f16_sint_035_log_si_rank_pct_252d": {"inputs": ["shortinterest"], "func": f16_sint_035_log_si_rank_pct_252d},
    "f16_sint_036_log_si_rank_pct_1260d": {"inputs": ["shortinterest"], "func": f16_sint_036_log_si_rank_pct_1260d},
    "f16_sint_037_si_quintile_state_252d": {"inputs": ["shortinterest"], "func": f16_sint_037_si_quintile_state_252d},
    "f16_sint_038_si_quintile_state_1260d": {"inputs": ["shortinterest"], "func": f16_sint_038_si_quintile_state_1260d},
    "f16_sint_039_daystocover_quintile_state_252d": {"inputs": ["daystocover"], "func": f16_sint_039_daystocover_quintile_state_252d},
    "f16_sint_040_daystocover_quintile_state_1260d": {"inputs": ["daystocover"], "func": f16_sint_040_daystocover_quintile_state_1260d},
    "f16_sint_041_si_fraction_above_80pct_252d": {"inputs": ["shortinterest"], "func": f16_sint_041_si_fraction_above_80pct_252d},
    "f16_sint_042_si_fraction_above_80pct_1260d": {"inputs": ["shortinterest"], "func": f16_sint_042_si_fraction_above_80pct_1260d},
    "f16_sint_043_si_fraction_above_median_252d": {"inputs": ["shortinterest"], "func": f16_sint_043_si_fraction_above_median_252d},
    "f16_sint_044_si_fraction_above_median_1260d": {"inputs": ["shortinterest"], "func": f16_sint_044_si_fraction_above_median_1260d},
    "f16_sint_045_si_longest_above_median_streak_252d": {"inputs": ["shortinterest"], "func": f16_sint_045_si_longest_above_median_streak_252d},
    "f16_sint_046_si_longest_above_median_streak_1260d": {"inputs": ["shortinterest"], "func": f16_sint_046_si_longest_above_median_streak_1260d},
    "f16_sint_047_dtc_fraction_above_80pct_252d": {"inputs": ["daystocover"], "func": f16_sint_047_dtc_fraction_above_80pct_252d},
    "f16_sint_048_dtc_fraction_above_80pct_1260d": {"inputs": ["daystocover"], "func": f16_sint_048_dtc_fraction_above_80pct_1260d},
    "f16_sint_049_si_persistence_above_own_median_252d": {"inputs": ["shortinterest"], "func": f16_sint_049_si_persistence_above_own_median_252d},
    "f16_sint_050_si_top_decile_persistence_252d": {"inputs": ["shortinterest"], "func": f16_sint_050_si_top_decile_persistence_252d},
    "f16_sint_051_si_top_decile_persistence_1260d": {"inputs": ["shortinterest"], "func": f16_sint_051_si_top_decile_persistence_1260d},
    "f16_sint_052_dtc_top_decile_persistence_252d": {"inputs": ["daystocover"], "func": f16_sint_052_dtc_top_decile_persistence_252d},
    "f16_sint_053_dtc_top_decile_persistence_1260d": {"inputs": ["daystocover"], "func": f16_sint_053_dtc_top_decile_persistence_1260d},
    "f16_sint_054_si_fraction_in_top_quartile_252d": {"inputs": ["shortinterest"], "func": f16_sint_054_si_fraction_in_top_quartile_252d},
    "f16_sint_055_si_fraction_in_top_quartile_1260d": {"inputs": ["shortinterest"], "func": f16_sint_055_si_fraction_in_top_quartile_1260d},
    "f16_sint_056_si_rolling_std_63d": {"inputs": ["shortinterest"], "func": f16_sint_056_si_rolling_std_63d},
    "f16_sint_057_si_rolling_std_252d": {"inputs": ["shortinterest"], "func": f16_sint_057_si_rolling_std_252d},
    "f16_sint_058_si_rolling_std_1260d": {"inputs": ["shortinterest"], "func": f16_sint_058_si_rolling_std_1260d},
    "f16_sint_059_log_si_rolling_std_252d": {"inputs": ["shortinterest"], "func": f16_sint_059_log_si_rolling_std_252d},
    "f16_sint_060_dtc_rolling_std_63d": {"inputs": ["daystocover"], "func": f16_sint_060_dtc_rolling_std_63d},
    "f16_sint_061_dtc_rolling_std_252d": {"inputs": ["daystocover"], "func": f16_sint_061_dtc_rolling_std_252d},
    "f16_sint_062_si_cv_252d": {"inputs": ["shortinterest"], "func": f16_sint_062_si_cv_252d},
    "f16_sint_063_si_cv_1260d": {"inputs": ["shortinterest"], "func": f16_sint_063_si_cv_1260d},
    "f16_sint_064_dtc_cv_252d": {"inputs": ["daystocover"], "func": f16_sint_064_dtc_cv_252d},
    "f16_sint_065_dtc_cv_1260d": {"inputs": ["daystocover"], "func": f16_sint_065_dtc_cv_1260d},
    "f16_sint_066_si_to_float_rolling_std_252d": {"inputs": ["shortinterest", "sharesbas"], "func": f16_sint_066_si_to_float_rolling_std_252d},
    "f16_sint_067_si_rolling_iqr_252d": {"inputs": ["shortinterest"], "func": f16_sint_067_si_rolling_iqr_252d},
    "f16_sint_068_dtc_rolling_iqr_252d": {"inputs": ["daystocover"], "func": f16_sint_068_dtc_rolling_iqr_252d},
    "f16_sint_069_log_si_rolling_iqr_252d": {"inputs": ["shortinterest"], "func": f16_sint_069_log_si_rolling_iqr_252d},
    "f16_sint_070_si_stability_score_252d": {"inputs": ["shortinterest"], "func": f16_sint_070_si_stability_score_252d},
    "f16_sint_071_corr_si_close_252d": {"inputs": ["shortinterest", "close"], "func": f16_sint_071_corr_si_close_252d},
    "f16_sint_072_corr_dtc_close_252d": {"inputs": ["daystocover", "close"], "func": f16_sint_072_corr_dtc_close_252d},
    "f16_sint_073_corr_si_close_504d": {"inputs": ["shortinterest", "close"], "func": f16_sint_073_corr_si_close_504d},
    "f16_sint_074_corr_dtc_close_504d": {"inputs": ["daystocover", "close"], "func": f16_sint_074_corr_dtc_close_504d},
    "f16_sint_075_corr_si_close_1260d": {"inputs": ["shortinterest", "close"], "func": f16_sint_075_corr_si_close_1260d},
}
