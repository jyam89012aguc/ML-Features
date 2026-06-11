"""
99_going_concern_flags — Extended Features 001-075
Domain: going-concern language and audit warnings — additional distress-signal
        variants: gap windows, decay-weighted intensity, transition timing,
        sequencing depth, flag-price coupling angles, and severity composites
        not covered by the base or derivative files.
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Flag series are forward-filled between filings; flat
stretches are correct and expected.

    going_concern : daily binary (1.0 / 0.0) — 1 when the most recent annual
                    audit on record contains going-concern doubt language, else 0.
    audit_warning : daily binary (1.0 / 0.0) — 1 when the most recent filing
                    carries an audit qualification, material-weakness, or
                    restatement warning, else 0.
    close         : split/dividend-adjusted daily close price, USD.

Sparse / stepwise output on binary flag data is expected and correct.
Functions look strictly backward using .shift(positive), .rolling(),
.expanding(), or .ewm().  Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _streak_length(flag: pd.Series) -> pd.Series:
    """Current consecutive run-length of flag == 1 (resets to 0 on any 0 day)."""
    arr = flag.fillna(0).values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=flag.index)


def _zero_streak_length(flag: pd.Series) -> pd.Series:
    """Current consecutive run-length of flag == 0 (resets to 0 on any 1 day)."""
    inv = (flag.fillna(0) == 0).astype(float)
    return _streak_length(inv)


def _days_since_last_one(flag: pd.Series) -> pd.Series:
    """Trading days since the most recent 1 in flag; NaN before first occurrence."""
    arr = flag.fillna(0).values.astype(float)
    out = np.full(len(arr), np.nan)
    last = -1
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=flag.index)


def _onset(flag: pd.Series) -> pd.Series:
    """1 on day flag transitions 0 -> 1."""
    return ((flag == 1) & (flag.shift(1).fillna(0) == 0)).astype(float)


def _clearing(flag: pd.Series) -> pd.Series:
    """1 on day flag transitions 1 -> 0."""
    return ((flag == 0) & (flag.shift(1).fillna(0) == 1)).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional flag-fraction window lengths ---

def gcf_ext_001_gc_fraction_5d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 5-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_WK)


def gcf_ext_002_gc_fraction_42d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 42-day (2-month) window where going-concern was active."""
    return _rolling_mean(going_concern.astype(float), 42)


def gcf_ext_003_gc_fraction_189d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 189-day (3-quarter) window where going-concern was active."""
    return _rolling_mean(going_concern.astype(float), 189)


def gcf_ext_004_gc_fraction_378d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 378-day (1.5-year) window where going-concern was active."""
    return _rolling_mean(going_concern.astype(float), 378)


def gcf_ext_005_aw_fraction_5d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 5-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_WK)


def gcf_ext_006_aw_fraction_42d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 42-day (2-month) window where audit-warning was active."""
    return _rolling_mean(audit_warning.astype(float), 42)


def gcf_ext_007_aw_fraction_189d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 189-day (3-quarter) window where audit-warning was active."""
    return _rolling_mean(audit_warning.astype(float), 189)


def gcf_ext_008_aw_fraction_378d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 378-day (1.5-year) window where audit-warning was active."""
    return _rolling_mean(audit_warning.astype(float), 378)


def gcf_ext_009_gc_rolling_sum_42d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 42-day window."""
    return _rolling_sum(going_concern.astype(float), 42)


def gcf_ext_010_aw_rolling_sum_42d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 42-day window."""
    return _rolling_sum(audit_warning.astype(float), 42)


def gcf_ext_011_either_fraction_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day window where EITHER flag was active."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_mean(either, _TD_QTR)


def gcf_ext_012_both_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where BOTH flags were simultaneously active."""
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    return _rolling_mean(both, _TD_YEAR)


# --- Group B (013-024): Decay-weighted intensity and EWM variants ---

def gcf_ext_013_gc_ewm_intensity_5(going_concern: pd.Series) -> pd.Series:
    """EWM (span=5) smoothed going-concern flag — very-short-run intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_WK)


def gcf_ext_014_gc_ewm_intensity_42(going_concern: pd.Series) -> pd.Series:
    """EWM (span=42) smoothed going-concern flag — bi-monthly intensity."""
    return _ewm_mean(going_concern.astype(float), 42)


def gcf_ext_015_gc_ewm_intensity_126(going_concern: pd.Series) -> pd.Series:
    """EWM (span=126) smoothed going-concern flag — half-year intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_2Q)


def gcf_ext_016_gc_ewm_intensity_504(going_concern: pd.Series) -> pd.Series:
    """EWM (span=504) smoothed going-concern flag — two-year intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_2Y)


def gcf_ext_017_aw_ewm_intensity_21(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=21) smoothed audit-warning flag — monthly intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_MO)


def gcf_ext_018_aw_ewm_intensity_126(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=126) smoothed audit-warning flag — half-year intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_2Q)


def gcf_ext_019_aw_ewm_intensity_504(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=504) smoothed audit-warning flag — two-year intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_2Y)


def gcf_ext_020_either_ewm_intensity_63(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed either-flag indicator."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _ewm_mean(either, _TD_QTR)


def gcf_ext_021_flag_sum_ewm_63(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed daily flag sum (0/1/2) — composite decay intensity."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _ewm_mean(s, _TD_QTR)


def gcf_ext_022_gc_ewm_63_minus_126(going_concern: pd.Series) -> pd.Series:
    """GC EWM span-63 minus EWM span-126 (intensity acceleration cross)."""
    return _ewm_mean(going_concern.astype(float), _TD_QTR) - _ewm_mean(going_concern.astype(float), _TD_2Q)


def gcf_ext_023_aw_ewm_63_minus_126(audit_warning: pd.Series) -> pd.Series:
    """AW EWM span-63 minus EWM span-126 (intensity acceleration cross)."""
    return _ewm_mean(audit_warning.astype(float), _TD_QTR) - _ewm_mean(audit_warning.astype(float), _TD_2Q)


def gcf_ext_024_gc_ewm_ratio_21_252(going_concern: pd.Series) -> pd.Series:
    """Ratio of GC EWM span-21 to EWM span-252 (short vs long intensity ratio)."""
    short = _ewm_mean(going_concern.astype(float), _TD_MO)
    long_ = _ewm_mean(going_concern.astype(float), _TD_YEAR)
    return _safe_div(short, long_)


# --- Group C (025-036): Off-flag durations and clearance timing ---

def gcf_ext_025_gc_off_streak(going_concern: pd.Series) -> pd.Series:
    """Consecutive trading days going-concern flag has been continuously OFF."""
    return _zero_streak_length(going_concern)


def gcf_ext_026_aw_off_streak(audit_warning: pd.Series) -> pd.Series:
    """Consecutive trading days audit-warning flag has been continuously OFF."""
    return _zero_streak_length(audit_warning)


def gcf_ext_027_both_off_streak(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Consecutive trading days with BOTH flags off (clean spell length)."""
    neither = ((going_concern == 0) & (audit_warning == 0)).astype(float)
    return _streak_length(neither)


def gcf_ext_028_gc_off_streak_pct_rank_504d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of current GC off-streak within trailing 504-day window."""
    return _rolling_rank_pct(_zero_streak_length(going_concern), _TD_2Y)


def gcf_ext_029_gc_streak_minus_off_streak(going_concern: pd.Series) -> pd.Series:
    """GC active-streak length minus GC off-streak length (net flag-state momentum)."""
    return _streak_length(going_concern) - _zero_streak_length(going_concern)


def gcf_ext_030_aw_streak_minus_off_streak(audit_warning: pd.Series) -> pd.Series:
    """AW active-streak length minus AW off-streak length (net flag-state momentum)."""
    return _streak_length(audit_warning) - _zero_streak_length(audit_warning)


def gcf_ext_031_days_since_gc_either_event(going_concern: pd.Series) -> pd.Series:
    """Days since the most recent GC onset OR clearing event (last flag change)."""
    change = ((_onset(going_concern) + _clearing(going_concern)) > 0).astype(float)
    return _days_since_last_one(change)


def gcf_ext_032_days_since_aw_either_event(audit_warning: pd.Series) -> pd.Series:
    """Days since the most recent AW onset OR clearing event (last flag change)."""
    change = ((_onset(audit_warning) + _clearing(audit_warning)) > 0).astype(float)
    return _days_since_last_one(change)


def gcf_ext_033_gc_streak_log(going_concern: pd.Series) -> pd.Series:
    """Natural log of (1 + current GC streak length) — compressed streak scale."""
    return np.log1p(_streak_length(going_concern))


def gcf_ext_034_aw_streak_log(audit_warning: pd.Series) -> pd.Series:
    """Natural log of (1 + current AW streak length) — compressed streak scale."""
    return np.log1p(_streak_length(audit_warning))


def gcf_ext_035_gc_streak_vs_504d_max(going_concern: pd.Series) -> pd.Series:
    """Current GC streak length divided by max GC streak in trailing 504-day window."""
    streak = _streak_length(going_concern)
    return _safe_div(streak, _rolling_max(streak, _TD_2Y))


def gcf_ext_036_gc_streak_vs_expanding_max(going_concern: pd.Series) -> pd.Series:
    """Current GC streak length divided by its all-history expanding maximum."""
    streak = _streak_length(going_concern)
    return _safe_div(streak, streak.expanding(min_periods=1).max())


# --- Group D (037-048): Episode counts and onset-density variants ---

def gcf_ext_037_gc_episodes_42d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 42-day window."""
    return _rolling_sum(_onset(going_concern), 42)


def gcf_ext_038_gc_episodes_126d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 126-day window."""
    return _rolling_sum(_onset(going_concern), _TD_2Q)


def gcf_ext_039_gc_episodes_1260d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 1260-day window."""
    return _rolling_sum(_onset(going_concern), _TD_5Y)


def gcf_ext_040_aw_episodes_63d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 63-day window."""
    return _rolling_sum(_onset(audit_warning), _TD_QTR)


def gcf_ext_041_aw_episodes_126d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 126-day window."""
    return _rolling_sum(_onset(audit_warning), _TD_2Q)


def gcf_ext_042_aw_episodes_756d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 756-day window."""
    return _rolling_sum(_onset(audit_warning), _TD_3Y)


def gcf_ext_043_gc_clearing_count_252d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern clearing events in trailing 252-day window."""
    return _rolling_sum(_clearing(going_concern), _TD_YEAR)


def gcf_ext_044_aw_clearing_count_252d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning clearing events in trailing 252-day window."""
    return _rolling_sum(_clearing(audit_warning), _TD_YEAR)


def gcf_ext_045_gc_flag_changes_252d(going_concern: pd.Series) -> pd.Series:
    """Total count of GC flag transitions (onsets + clearings) in trailing 252 days."""
    change = _onset(going_concern) + _clearing(going_concern)
    return _rolling_sum(change, _TD_YEAR)


def gcf_ext_046_aw_flag_changes_252d(audit_warning: pd.Series) -> pd.Series:
    """Total count of AW flag transitions (onsets + clearings) in trailing 252 days."""
    change = _onset(audit_warning) + _clearing(audit_warning)
    return _rolling_sum(change, _TD_YEAR)


def gcf_ext_047_gc_clearing_count_expanding(going_concern: pd.Series) -> pd.Series:
    """Cumulative all-history count of going-concern clearing events."""
    return _clearing(going_concern).expanding(min_periods=1).sum()


def gcf_ext_048_gc_episode_density_504d(going_concern: pd.Series) -> pd.Series:
    """GC onset episode count over trailing 504 days divided by 504 (per-day density)."""
    return _rolling_sum(_onset(going_concern), _TD_2Y) / float(_TD_2Y)


# --- Group E (049-060): Rolling z-score / percentile-rank variants ---

def gcf_ext_049_gc_fraction_21d_zscore_252d(going_concern: pd.Series) -> pd.Series:
    """Z-score of the 21-day GC fraction within a 252-day rolling window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_MO)
    return _zscore_rolling(frac, _TD_YEAR)


def gcf_ext_050_gc_fraction_126d_zscore_756d(going_concern: pd.Series) -> pd.Series:
    """Z-score of the 126-day GC fraction within a 756-day rolling window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_2Q)
    return _zscore_rolling(frac, _TD_3Y)


def gcf_ext_051_aw_fraction_21d_zscore_252d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of the 21-day AW fraction within a 252-day rolling window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_MO)
    return _zscore_rolling(frac, _TD_YEAR)


def gcf_ext_052_aw_fraction_126d_zscore_756d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of the 126-day AW fraction within a 756-day rolling window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_2Q)
    return _zscore_rolling(frac, _TD_3Y)


def gcf_ext_053_gc_fraction_pct_rank_252d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day GC fraction within a 252-day window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_QTR)
    return _rolling_rank_pct(frac, _TD_YEAR)


def gcf_ext_054_aw_fraction_pct_rank_252d(audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day AW fraction within a 252-day window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_QTR)
    return _rolling_rank_pct(frac, _TD_YEAR)


def gcf_ext_055_gc_fraction_pct_rank_1260d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of the 252-day GC fraction within a 1260-day window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    return _rolling_rank_pct(frac, _TD_5Y)


def gcf_ext_056_gc_streak_zscore_504d(going_concern: pd.Series) -> pd.Series:
    """Z-score of current GC streak length within a 504-day rolling window."""
    return _zscore_rolling(_streak_length(going_concern), _TD_2Y)


def gcf_ext_057_aw_streak_zscore_504d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of current AW streak length within a 504-day rolling window."""
    return _zscore_rolling(_streak_length(audit_warning), _TD_2Y)


def gcf_ext_058_flag_sum_zscore_504d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Z-score of the daily flag sum (0/1/2) within a 504-day rolling window."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _zscore_rolling(s, _TD_2Y)


def gcf_ext_059_flag_sum_pct_rank_504d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of the daily flag sum within a 504-day rolling window."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_rank_pct(s, _TD_2Y)


def gcf_ext_060_gc_fraction_expanding_zscore(going_concern: pd.Series) -> pd.Series:
    """Expanding all-history z-score of the 63-day GC fraction."""
    frac = _rolling_mean(going_concern.astype(float), _TD_QTR)
    m  = frac.expanding(min_periods=2).mean()
    sd = frac.expanding(min_periods=2).std()
    return _safe_div(frac - m, sd)


# --- Group F (061-068): Flag-price coupling variants ---

def gcf_ext_061_gc_flag_times_price_dd_63d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by percent drawdown from the 63-day price high."""
    peak = _rolling_max(close, _TD_QTR)
    dd = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd


def gcf_ext_062_aw_flag_times_price_dd_63d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag multiplied by percent drawdown from the 63-day price high."""
    peak = _rolling_max(close, _TD_QTR)
    dd = _safe_div(close - peak, peak)
    return audit_warning.astype(float) * dd


def gcf_ext_063_gc_flag_times_price_dd_504d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by percent drawdown from the 504-day price high."""
    peak = _rolling_max(close, _TD_2Y)
    dd = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd


def gcf_ext_064_gc_days_at_3y_low_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days GC active AND close at its 756-day rolling low."""
    low = _rolling_min(close, _TD_3Y)
    joint = (going_concern.astype(float) * (close <= low + _EPS).astype(float))
    return _rolling_sum(joint, _TD_YEAR)


def gcf_ext_065_aw_days_at_3y_low_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days AW active AND close at its 756-day rolling low."""
    low = _rolling_min(close, _TD_3Y)
    joint = (audit_warning.astype(float) * (close <= low + _EPS).astype(float))
    return _rolling_sum(joint, _TD_YEAR)


def gcf_ext_066_gc_flag_times_volatility_63d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by 63-day realized volatility of daily log returns."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    return going_concern.astype(float) * _rolling_std(lr, _TD_QTR)


def gcf_ext_067_gc_flagged_price_pct_rank_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Close percentile rank (252d) measured only on GC-flagged days, else NaN."""
    rank = _rolling_rank_pct(close, _TD_YEAR)
    return rank.where(going_concern == 1, other=np.nan)


def gcf_ext_068_gc_flag_times_drawdown_ratio(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag times ratio of close to its 252-day rolling high (proximity to peak)."""
    peak = _rolling_max(close, _TD_YEAR)
    return going_concern.astype(float) * _safe_div(close, peak)


# --- Group G (069-075): Lead/lag sequencing and severity composites ---

def gcf_ext_069_gc_active_no_recent_aw(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if GC active but no AW day occurred in the prior 252 days (unwarned GC)."""
    aw_prior = _rolling_sum(audit_warning.astype(float), _TD_YEAR)
    return ((going_concern == 1) & (aw_prior == 0)).astype(float)


def gcf_ext_070_aw_then_gc_within_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 on GC onset days where an AW day occurred within the prior 63 days (fast escalation)."""
    gc_on = _onset(going_concern)
    aw_recent = _rolling_sum(audit_warning.astype(float).shift(1), _TD_QTR)
    return (gc_on * (aw_recent > 0)).astype(float)


def gcf_ext_071_flag_sum_above_1_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where the flag sum equalled 2 (both flags on)."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_mean((s >= 2.0).astype(float), _TD_YEAR)


def gcf_ext_072_gc_persistence_score(going_concern: pd.Series) -> pd.Series:
    """GC persistence: 63-day fraction multiplied by log(1 + current streak length)."""
    frac = _rolling_mean(going_concern.astype(float), _TD_QTR)
    return frac * np.log1p(_streak_length(going_concern))


def gcf_ext_073_distress_breadth_score(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Mean of 252-day GC fraction and 252-day AW fraction (combined breadth)."""
    gc_frac = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    aw_frac = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    return (gc_frac + aw_frac) / 2.0


def gcf_ext_074_chronic_distress_flag(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if EITHER flag has been active on at least half of the trailing 252 days."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return (_rolling_mean(either, _TD_YEAR) >= 0.5).astype(float)


def gcf_ext_075_distress_capitulation_composite(
    going_concern: pd.Series,
    audit_warning: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Capitulation composite: weighted GC EWM-63 intensity (x2) plus AW EWM-63
    intensity, scaled by the absolute percent drawdown from the expanding peak.
    Higher = deeper audit distress coincident with price capitulation.
    """
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    intensity = (2.0 * gc_ewm + aw_ewm) / 3.0
    peak = close.expanding(min_periods=1).max()
    dd = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    return intensity * (1.0 + dd)


# ── Registry ──────────────────────────────────────────────────────────────────

GOING_CONCERN_FLAGS_EXTENDED_REGISTRY_001_075 = {
    "gcf_ext_001_gc_fraction_5d":                 {"inputs": ["going_concern"],                            "func": gcf_ext_001_gc_fraction_5d},
    "gcf_ext_002_gc_fraction_42d":                {"inputs": ["going_concern"],                            "func": gcf_ext_002_gc_fraction_42d},
    "gcf_ext_003_gc_fraction_189d":               {"inputs": ["going_concern"],                            "func": gcf_ext_003_gc_fraction_189d},
    "gcf_ext_004_gc_fraction_378d":               {"inputs": ["going_concern"],                            "func": gcf_ext_004_gc_fraction_378d},
    "gcf_ext_005_aw_fraction_5d":                 {"inputs": ["audit_warning"],                            "func": gcf_ext_005_aw_fraction_5d},
    "gcf_ext_006_aw_fraction_42d":                {"inputs": ["audit_warning"],                            "func": gcf_ext_006_aw_fraction_42d},
    "gcf_ext_007_aw_fraction_189d":               {"inputs": ["audit_warning"],                            "func": gcf_ext_007_aw_fraction_189d},
    "gcf_ext_008_aw_fraction_378d":               {"inputs": ["audit_warning"],                            "func": gcf_ext_008_aw_fraction_378d},
    "gcf_ext_009_gc_rolling_sum_42d":             {"inputs": ["going_concern"],                            "func": gcf_ext_009_gc_rolling_sum_42d},
    "gcf_ext_010_aw_rolling_sum_42d":             {"inputs": ["audit_warning"],                            "func": gcf_ext_010_aw_rolling_sum_42d},
    "gcf_ext_011_either_fraction_63d":            {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_011_either_fraction_63d},
    "gcf_ext_012_both_fraction_252d":             {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_012_both_fraction_252d},
    "gcf_ext_013_gc_ewm_intensity_5":             {"inputs": ["going_concern"],                            "func": gcf_ext_013_gc_ewm_intensity_5},
    "gcf_ext_014_gc_ewm_intensity_42":            {"inputs": ["going_concern"],                            "func": gcf_ext_014_gc_ewm_intensity_42},
    "gcf_ext_015_gc_ewm_intensity_126":           {"inputs": ["going_concern"],                            "func": gcf_ext_015_gc_ewm_intensity_126},
    "gcf_ext_016_gc_ewm_intensity_504":           {"inputs": ["going_concern"],                            "func": gcf_ext_016_gc_ewm_intensity_504},
    "gcf_ext_017_aw_ewm_intensity_21":            {"inputs": ["audit_warning"],                            "func": gcf_ext_017_aw_ewm_intensity_21},
    "gcf_ext_018_aw_ewm_intensity_126":           {"inputs": ["audit_warning"],                            "func": gcf_ext_018_aw_ewm_intensity_126},
    "gcf_ext_019_aw_ewm_intensity_504":           {"inputs": ["audit_warning"],                            "func": gcf_ext_019_aw_ewm_intensity_504},
    "gcf_ext_020_either_ewm_intensity_63":        {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_020_either_ewm_intensity_63},
    "gcf_ext_021_flag_sum_ewm_63":                {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_021_flag_sum_ewm_63},
    "gcf_ext_022_gc_ewm_63_minus_126":            {"inputs": ["going_concern"],                            "func": gcf_ext_022_gc_ewm_63_minus_126},
    "gcf_ext_023_aw_ewm_63_minus_126":            {"inputs": ["audit_warning"],                            "func": gcf_ext_023_aw_ewm_63_minus_126},
    "gcf_ext_024_gc_ewm_ratio_21_252":            {"inputs": ["going_concern"],                            "func": gcf_ext_024_gc_ewm_ratio_21_252},
    "gcf_ext_025_gc_off_streak":                  {"inputs": ["going_concern"],                            "func": gcf_ext_025_gc_off_streak},
    "gcf_ext_026_aw_off_streak":                  {"inputs": ["audit_warning"],                            "func": gcf_ext_026_aw_off_streak},
    "gcf_ext_027_both_off_streak":                {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_027_both_off_streak},
    "gcf_ext_028_gc_off_streak_pct_rank_504d":    {"inputs": ["going_concern"],                            "func": gcf_ext_028_gc_off_streak_pct_rank_504d},
    "gcf_ext_029_gc_streak_minus_off_streak":     {"inputs": ["going_concern"],                            "func": gcf_ext_029_gc_streak_minus_off_streak},
    "gcf_ext_030_aw_streak_minus_off_streak":     {"inputs": ["audit_warning"],                            "func": gcf_ext_030_aw_streak_minus_off_streak},
    "gcf_ext_031_days_since_gc_either_event":     {"inputs": ["going_concern"],                            "func": gcf_ext_031_days_since_gc_either_event},
    "gcf_ext_032_days_since_aw_either_event":     {"inputs": ["audit_warning"],                            "func": gcf_ext_032_days_since_aw_either_event},
    "gcf_ext_033_gc_streak_log":                  {"inputs": ["going_concern"],                            "func": gcf_ext_033_gc_streak_log},
    "gcf_ext_034_aw_streak_log":                  {"inputs": ["audit_warning"],                            "func": gcf_ext_034_aw_streak_log},
    "gcf_ext_035_gc_streak_vs_504d_max":          {"inputs": ["going_concern"],                            "func": gcf_ext_035_gc_streak_vs_504d_max},
    "gcf_ext_036_gc_streak_vs_expanding_max":     {"inputs": ["going_concern"],                            "func": gcf_ext_036_gc_streak_vs_expanding_max},
    "gcf_ext_037_gc_episodes_42d":                {"inputs": ["going_concern"],                            "func": gcf_ext_037_gc_episodes_42d},
    "gcf_ext_038_gc_episodes_126d":               {"inputs": ["going_concern"],                            "func": gcf_ext_038_gc_episodes_126d},
    "gcf_ext_039_gc_episodes_1260d":              {"inputs": ["going_concern"],                            "func": gcf_ext_039_gc_episodes_1260d},
    "gcf_ext_040_aw_episodes_63d":                {"inputs": ["audit_warning"],                            "func": gcf_ext_040_aw_episodes_63d},
    "gcf_ext_041_aw_episodes_126d":               {"inputs": ["audit_warning"],                            "func": gcf_ext_041_aw_episodes_126d},
    "gcf_ext_042_aw_episodes_756d":               {"inputs": ["audit_warning"],                            "func": gcf_ext_042_aw_episodes_756d},
    "gcf_ext_043_gc_clearing_count_252d":         {"inputs": ["going_concern"],                            "func": gcf_ext_043_gc_clearing_count_252d},
    "gcf_ext_044_aw_clearing_count_252d":         {"inputs": ["audit_warning"],                            "func": gcf_ext_044_aw_clearing_count_252d},
    "gcf_ext_045_gc_flag_changes_252d":           {"inputs": ["going_concern"],                            "func": gcf_ext_045_gc_flag_changes_252d},
    "gcf_ext_046_aw_flag_changes_252d":           {"inputs": ["audit_warning"],                            "func": gcf_ext_046_aw_flag_changes_252d},
    "gcf_ext_047_gc_clearing_count_expanding":    {"inputs": ["going_concern"],                            "func": gcf_ext_047_gc_clearing_count_expanding},
    "gcf_ext_048_gc_episode_density_504d":        {"inputs": ["going_concern"],                            "func": gcf_ext_048_gc_episode_density_504d},
    "gcf_ext_049_gc_fraction_21d_zscore_252d":    {"inputs": ["going_concern"],                            "func": gcf_ext_049_gc_fraction_21d_zscore_252d},
    "gcf_ext_050_gc_fraction_126d_zscore_756d":   {"inputs": ["going_concern"],                            "func": gcf_ext_050_gc_fraction_126d_zscore_756d},
    "gcf_ext_051_aw_fraction_21d_zscore_252d":    {"inputs": ["audit_warning"],                            "func": gcf_ext_051_aw_fraction_21d_zscore_252d},
    "gcf_ext_052_aw_fraction_126d_zscore_756d":   {"inputs": ["audit_warning"],                            "func": gcf_ext_052_aw_fraction_126d_zscore_756d},
    "gcf_ext_053_gc_fraction_pct_rank_252d":      {"inputs": ["going_concern"],                            "func": gcf_ext_053_gc_fraction_pct_rank_252d},
    "gcf_ext_054_aw_fraction_pct_rank_252d":      {"inputs": ["audit_warning"],                            "func": gcf_ext_054_aw_fraction_pct_rank_252d},
    "gcf_ext_055_gc_fraction_pct_rank_1260d":     {"inputs": ["going_concern"],                            "func": gcf_ext_055_gc_fraction_pct_rank_1260d},
    "gcf_ext_056_gc_streak_zscore_504d":          {"inputs": ["going_concern"],                            "func": gcf_ext_056_gc_streak_zscore_504d},
    "gcf_ext_057_aw_streak_zscore_504d":          {"inputs": ["audit_warning"],                            "func": gcf_ext_057_aw_streak_zscore_504d},
    "gcf_ext_058_flag_sum_zscore_504d":           {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_058_flag_sum_zscore_504d},
    "gcf_ext_059_flag_sum_pct_rank_504d":         {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_059_flag_sum_pct_rank_504d},
    "gcf_ext_060_gc_fraction_expanding_zscore":   {"inputs": ["going_concern"],                            "func": gcf_ext_060_gc_fraction_expanding_zscore},
    "gcf_ext_061_gc_flag_times_price_dd_63d":     {"inputs": ["going_concern", "close"],                   "func": gcf_ext_061_gc_flag_times_price_dd_63d},
    "gcf_ext_062_aw_flag_times_price_dd_63d":     {"inputs": ["audit_warning", "close"],                   "func": gcf_ext_062_aw_flag_times_price_dd_63d},
    "gcf_ext_063_gc_flag_times_price_dd_504d":    {"inputs": ["going_concern", "close"],                   "func": gcf_ext_063_gc_flag_times_price_dd_504d},
    "gcf_ext_064_gc_days_at_3y_low_252d":         {"inputs": ["going_concern", "close"],                   "func": gcf_ext_064_gc_days_at_3y_low_252d},
    "gcf_ext_065_aw_days_at_3y_low_252d":         {"inputs": ["audit_warning", "close"],                   "func": gcf_ext_065_aw_days_at_3y_low_252d},
    "gcf_ext_066_gc_flag_times_volatility_63d":   {"inputs": ["going_concern", "close"],                   "func": gcf_ext_066_gc_flag_times_volatility_63d},
    "gcf_ext_067_gc_flagged_price_pct_rank_252d": {"inputs": ["going_concern", "close"],                   "func": gcf_ext_067_gc_flagged_price_pct_rank_252d},
    "gcf_ext_068_gc_flag_times_drawdown_ratio":   {"inputs": ["going_concern", "close"],                   "func": gcf_ext_068_gc_flag_times_drawdown_ratio},
    "gcf_ext_069_gc_active_no_recent_aw":         {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_069_gc_active_no_recent_aw},
    "gcf_ext_070_aw_then_gc_within_63d":          {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_070_aw_then_gc_within_63d},
    "gcf_ext_071_flag_sum_above_1_fraction_252d": {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_071_flag_sum_above_1_fraction_252d},
    "gcf_ext_072_gc_persistence_score":           {"inputs": ["going_concern"],                            "func": gcf_ext_072_gc_persistence_score},
    "gcf_ext_073_distress_breadth_score":         {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_073_distress_breadth_score},
    "gcf_ext_074_chronic_distress_flag":          {"inputs": ["going_concern", "audit_warning"],           "func": gcf_ext_074_chronic_distress_flag},
    "gcf_ext_075_distress_capitulation_composite":{"inputs": ["going_concern", "audit_warning", "close"],  "func": gcf_ext_075_distress_capitulation_composite},
}
