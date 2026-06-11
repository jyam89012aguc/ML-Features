"""
99_going_concern_flags — Base Features 001-100
Domain: going-concern language and audit warnings — explicit auditor distress signals
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_TD_MO    = 21    # 1 month
_TD_WK    = 5     # 1 week
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


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
    arr = flag.values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=flag.index)


def _days_since_last_one(flag: pd.Series) -> pd.Series:
    """
    Number of trading days since the most recent 1 in flag.
    Returns NaN before the first 1 is observed.
    """
    arr = flag.values.astype(float)
    out = np.full(len(arr), np.nan)
    last = -1
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=flag.index)


def _count_episodes(flag: pd.Series, w: int) -> pd.Series:
    """
    Count distinct flag-on episodes (separate spells) within a rolling window w.
    An episode starts on any day where flag transitions from 0 -> 1.
    """
    onset = ((flag == 1) & (flag.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Current flag level and simple flag state ---

def gcf_001_going_concern_level(going_concern: pd.Series) -> pd.Series:
    """Current going-concern flag value (1 = flag active, 0 = no flag)."""
    return going_concern.astype(float)


def gcf_002_audit_warning_level(audit_warning: pd.Series) -> pd.Series:
    """Current audit-warning flag value (1 = warning active, 0 = none)."""
    return audit_warning.astype(float)


def gcf_003_either_flag_active(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if either going-concern or audit-warning flag is active, else 0."""
    return ((going_concern == 1) | (audit_warning == 1)).astype(float)


def gcf_004_both_flags_active(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if both going-concern AND audit-warning flags are simultaneously active."""
    return ((going_concern == 1) & (audit_warning == 1)).astype(float)


def gcf_005_gc_only_not_aw(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if going-concern is active but audit-warning is not (isolated GC)."""
    return ((going_concern == 1) & (audit_warning == 0)).astype(float)


def gcf_006_aw_only_not_gc(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if audit-warning active but going-concern not yet raised."""
    return ((audit_warning == 1) & (going_concern == 0)).astype(float)


def gcf_007_flag_sum(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Sum of both binary flags (0, 1, or 2); severity index."""
    return going_concern.astype(float) + audit_warning.astype(float)


def gcf_008_gc_onset_flag(going_concern: pd.Series) -> pd.Series:
    """1 on the exact day going-concern flag transitions from 0 to 1, else 0."""
    prev = going_concern.shift(1).fillna(0)
    return ((going_concern == 1) & (prev == 0)).astype(float)


def gcf_009_gc_clearing_flag(going_concern: pd.Series) -> pd.Series:
    """1 on the exact day going-concern flag transitions from 1 to 0, else 0."""
    prev = going_concern.shift(1).fillna(0)
    return ((going_concern == 0) & (prev == 1)).astype(float)


def gcf_010_aw_onset_flag(audit_warning: pd.Series) -> pd.Series:
    """1 on the exact day audit-warning flag transitions from 0 to 1, else 0."""
    prev = audit_warning.shift(1).fillna(0)
    return ((audit_warning == 1) & (prev == 0)).astype(float)


def gcf_011_aw_clearing_flag(audit_warning: pd.Series) -> pd.Series:
    """1 on the exact day audit-warning flag transitions from 1 to 0, else 0."""
    prev = audit_warning.shift(1).fillna(0)
    return ((audit_warning == 0) & (prev == 1)).astype(float)


def gcf_012_escalation_aw_to_gc(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 on days when going-concern turns on while audit-warning was already active."""
    gc_onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    aw_active = (audit_warning.shift(1).fillna(0) == 1).astype(float)
    return gc_onset * aw_active


def gcf_013_gc_streak_length(going_concern: pd.Series) -> pd.Series:
    """Consecutive trading days going-concern flag has been continuously active."""
    return _streak_length(going_concern)


def gcf_014_aw_streak_length(audit_warning: pd.Series) -> pd.Series:
    """Consecutive trading days audit-warning flag has been continuously active."""
    return _streak_length(audit_warning)


def gcf_015_combined_streak_length(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Consecutive trading days EITHER flag has been continuously active."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _streak_length(either)


# --- Group B (016-030): Rolling flag sums over multiple windows ---

def gcf_016_gc_rolling_sum_21d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 21-day (1-month) window."""
    return _rolling_sum(going_concern.astype(float), _TD_MO)


def gcf_017_gc_rolling_sum_63d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 63-day (1-quarter) window."""
    return _rolling_sum(going_concern.astype(float), _TD_QTR)


def gcf_018_gc_rolling_sum_126d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 126-day (2-quarter) window."""
    return _rolling_sum(going_concern.astype(float), _TD_2Q)


def gcf_019_gc_rolling_sum_252d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 252-day (1-year) window."""
    return _rolling_sum(going_concern.astype(float), _TD_YEAR)


def gcf_020_gc_rolling_sum_504d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 504-day (2-year) window."""
    return _rolling_sum(going_concern.astype(float), _TD_2Y)


def gcf_021_gc_rolling_sum_756d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 756-day (3-year) window."""
    return _rolling_sum(going_concern.astype(float), _TD_3Y)


def gcf_022_aw_rolling_sum_21d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 21-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_MO)


def gcf_023_aw_rolling_sum_63d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 63-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_QTR)


def gcf_024_aw_rolling_sum_126d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 126-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_2Q)


def gcf_025_aw_rolling_sum_252d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 252-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_YEAR)


def gcf_026_aw_rolling_sum_504d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 504-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_2Y)


def gcf_027_aw_rolling_sum_756d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 756-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_3Y)


def gcf_028_either_rolling_sum_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of days EITHER flag active in trailing 63-day window."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_sum(either, _TD_QTR)


def gcf_029_either_rolling_sum_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of days EITHER flag active in trailing 252-day window."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_sum(either, _TD_YEAR)


def gcf_030_both_rolling_sum_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of days BOTH flags active simultaneously in trailing 252-day window."""
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    return _rolling_sum(both, _TD_YEAR)


# --- Group C (031-045): Rolling flag fractions (flagged-day proportion) ---

def gcf_031_gc_fraction_21d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 21-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_MO)


def gcf_032_gc_fraction_63d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_QTR)


def gcf_033_gc_fraction_126d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 126-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_2Q)


def gcf_034_gc_fraction_252d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_YEAR)


def gcf_035_gc_fraction_504d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 504-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_2Y)


def gcf_036_gc_fraction_756d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 756-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_3Y)


def gcf_037_aw_fraction_63d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_QTR)


def gcf_038_aw_fraction_252d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_YEAR)


def gcf_039_aw_fraction_504d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 504-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_2Y)


def gcf_040_aw_fraction_756d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 756-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_3Y)


def gcf_041_either_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where EITHER flag was active."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_mean(either, _TD_YEAR)


def gcf_042_gc_expanding_fraction(going_concern: pd.Series) -> pd.Series:
    """Expanding (all-history) fraction of days going-concern flag was active."""
    return going_concern.astype(float).expanding(min_periods=1).mean()


def gcf_043_aw_expanding_fraction(audit_warning: pd.Series) -> pd.Series:
    """Expanding (all-history) fraction of days audit-warning flag was active."""
    return audit_warning.astype(float).expanding(min_periods=1).mean()


def gcf_044_gc_cumulative_flagged_days(going_concern: pd.Series) -> pd.Series:
    """Cumulative count of going-concern flagged days over all history."""
    return going_concern.astype(float).expanding(min_periods=1).sum()


def gcf_045_aw_cumulative_flagged_days(audit_warning: pd.Series) -> pd.Series:
    """Cumulative count of audit-warning flagged days over all history."""
    return audit_warning.astype(float).expanding(min_periods=1).sum()


# --- Group D (046-060): Episode counts and time-since-event features ---

def gcf_046_gc_episodes_63d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 63-day window."""
    return _count_episodes(going_concern, _TD_QTR)


def gcf_047_gc_episodes_252d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 252-day window."""
    return _count_episodes(going_concern, _TD_YEAR)


def gcf_048_gc_episodes_504d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 504-day window."""
    return _count_episodes(going_concern, _TD_2Y)


def gcf_049_gc_episodes_756d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 756-day window."""
    return _count_episodes(going_concern, _TD_3Y)


def gcf_050_aw_episodes_252d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 252-day window."""
    return _count_episodes(audit_warning, _TD_YEAR)


def gcf_051_aw_episodes_504d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 504-day window."""
    return _count_episodes(audit_warning, _TD_2Y)


def gcf_052_days_since_gc_onset(going_concern: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent going-concern onset; NaN before first onset."""
    onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    return _days_since_last_one(onset)


def gcf_053_days_since_aw_onset(audit_warning: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent audit-warning onset; NaN before first onset."""
    onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    return _days_since_last_one(onset)


def gcf_054_days_since_gc_clearing(going_concern: pd.Series) -> pd.Series:
    """Trading days since the most recent going-concern clearing event; NaN before first clearing."""
    clearing = ((going_concern == 0) & (going_concern.shift(1).fillna(0) == 1)).astype(float)
    return _days_since_last_one(clearing)


def gcf_055_days_since_aw_clearing(audit_warning: pd.Series) -> pd.Series:
    """Trading days since the most recent audit-warning clearing event."""
    clearing = ((audit_warning == 0) & (audit_warning.shift(1).fillna(0) == 1)).astype(float)
    return _days_since_last_one(clearing)


def gcf_056_longest_gc_spell_252d(going_concern: pd.Series) -> pd.Series:
    """Longest continuous going-concern spell (in days) within trailing 252-day window."""
    def _max_spell(arr):
        best = 0
        cur = 0
        for v in arr:
            if v == 1.0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return going_concern.astype(float).rolling(_TD_YEAR, min_periods=1).apply(_max_spell, raw=True)


def gcf_057_longest_gc_spell_504d(going_concern: pd.Series) -> pd.Series:
    """Longest continuous going-concern spell (in days) within trailing 504-day window."""
    def _max_spell(arr):
        best = 0
        cur = 0
        for v in arr:
            if v == 1.0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return going_concern.astype(float).rolling(_TD_2Y, min_periods=1).apply(_max_spell, raw=True)


def gcf_058_longest_aw_spell_252d(audit_warning: pd.Series) -> pd.Series:
    """Longest continuous audit-warning spell (in days) within trailing 252-day window."""
    def _max_spell(arr):
        best = 0
        cur = 0
        for v in arr:
            if v == 1.0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return audit_warning.astype(float).rolling(_TD_YEAR, min_periods=1).apply(_max_spell, raw=True)


def gcf_059_gc_streak_vs_252d_max(going_concern: pd.Series) -> pd.Series:
    """Current GC streak length divided by max GC streak in trailing 252-day window."""
    streak = _streak_length(going_concern)
    mx = streak.rolling(_TD_YEAR, min_periods=1).max()
    return _safe_div(streak, mx)


def gcf_060_aw_streak_vs_252d_max(audit_warning: pd.Series) -> pd.Series:
    """Current AW streak length divided by max AW streak in trailing 252-day window."""
    streak = _streak_length(audit_warning)
    mx = streak.rolling(_TD_YEAR, min_periods=1).max()
    return _safe_div(streak, mx)


# --- Group E (061-075): Flag interactions with price / EWM smoothing ---

def gcf_061_gc_ewm_intensity_21(going_concern: pd.Series) -> pd.Series:
    """EWM (span=21) smoothed going-concern flag — short-run intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_MO)


def gcf_062_gc_ewm_intensity_63(going_concern: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed going-concern flag — quarterly intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_QTR)


def gcf_063_gc_ewm_intensity_252(going_concern: pd.Series) -> pd.Series:
    """EWM (span=252) smoothed going-concern flag — annual intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_YEAR)


def gcf_064_aw_ewm_intensity_63(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed audit-warning flag."""
    return _ewm_mean(audit_warning.astype(float), _TD_QTR)


def gcf_065_aw_ewm_intensity_252(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=252) smoothed audit-warning flag — annual intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_YEAR)


def gcf_066_gc_flag_weighted_close(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Close price on days when going-concern is active, else NaN (flag-masked price)."""
    return close.where(going_concern == 1, other=np.nan)


def gcf_067_aw_flag_weighted_close(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Close price on days when audit-warning is active, else NaN."""
    return close.where(audit_warning == 1, other=np.nan)


def gcf_068_gc_price_drawdown_during_flag(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """
    Close minus its expanding peak, restricted to days when going-concern is active.
    Zero on non-flag days; captures price decline depth while flag is on.
    """
    peak = close.expanding(min_periods=1).max()
    dd = close - peak
    return dd.where(going_concern == 1, other=0.0)


def gcf_069_aw_price_drawdown_during_flag(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Close minus expanding peak, restricted to days when audit-warning is active."""
    peak = close.expanding(min_periods=1).max()
    dd = close - peak
    return dd.where(audit_warning == 1, other=0.0)


def gcf_070_gc_flag_weighted_price_decline_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """
    Rolling 252-day sum of (close - prior_close) on going-concern flagged days only.
    Accumulates price change only while flag is on.
    """
    daily_ret = close - close.shift(1)
    flagged_ret = daily_ret * going_concern.astype(float)
    return _rolling_sum(flagged_ret, _TD_YEAR)


def gcf_071_aw_flag_weighted_price_decline_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day sum of daily price change on audit-warning flagged days only."""
    daily_ret = close - close.shift(1)
    flagged_ret = daily_ret * audit_warning.astype(float)
    return _rolling_sum(flagged_ret, _TD_YEAR)


def gcf_072_close_pct_drawdown_expanding(close: pd.Series) -> pd.Series:
    """Percent drawdown of close from its all-time expanding peak (price depth signal)."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def gcf_073_gc_active_at_price_low_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """1 if going-concern is currently active AND close equals its 252-day rolling min."""
    price_low = _rolling_min(close, _TD_YEAR)
    at_low = (close <= price_low + _EPS).astype(float)
    return at_low * going_concern.astype(float)


def gcf_074_aw_active_at_price_low_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """1 if audit-warning is currently active AND close equals its 252-day rolling min."""
    price_low = _rolling_min(close, _TD_YEAR)
    at_low = (close <= price_low + _EPS).astype(float)
    return at_low * audit_warning.astype(float)


def gcf_075_combined_distress_composite(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite distress score: equally weighted sum of (gc fraction 252d,
    aw fraction 252d, pct drawdown from expanding peak normalised to [0,1]).
    Higher = more distress.
    """
    gc_frac = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    aw_frac = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    peak = close.expanding(min_periods=1).max()
    dd_pct = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    return (gc_frac + aw_frac + dd_pct) / 3.0


# --- Group K (151-175): Additional windows, normalizations, and interactions ---

def gcf_151_gc_rolling_median_63d(going_concern: pd.Series) -> pd.Series:
    """Rolling 63-day median of going-concern flag — robust short-run level."""
    return _rolling_median(going_concern.astype(float), _TD_QTR)


def gcf_152_aw_rolling_median_63d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 63-day median of audit-warning flag — robust short-run level."""
    return _rolling_median(audit_warning.astype(float), _TD_QTR)


def gcf_153_gc_rolling_median_252d(going_concern: pd.Series) -> pd.Series:
    """Rolling 252-day median of going-concern flag — robust annual level."""
    return _rolling_median(going_concern.astype(float), _TD_YEAR)


def gcf_154_aw_rolling_median_252d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 252-day median of audit-warning flag — robust annual level."""
    return _rolling_median(audit_warning.astype(float), _TD_YEAR)


def gcf_155_gc_streak_normalized_504d(going_concern: pd.Series) -> pd.Series:
    """GC streak length divided by 504-day rolling max streak — relative run depth."""
    streak = _streak_length(going_concern)
    mx = streak.rolling(_TD_2Y, min_periods=1).max()
    return _safe_div(streak, mx)


def gcf_156_aw_streak_normalized_504d(audit_warning: pd.Series) -> pd.Series:
    """AW streak length divided by 504-day rolling max streak — relative run depth."""
    streak = _streak_length(audit_warning)
    mx = streak.rolling(_TD_2Y, min_periods=1).max()
    return _safe_div(streak, mx)


def gcf_157_gc_episodes_126d(going_concern: pd.Series) -> pd.Series:
    """Count of distinct going-concern onset episodes in trailing 126-day window."""
    return _count_episodes(going_concern, _TD_2Q)


def gcf_158_aw_episodes_126d(audit_warning: pd.Series) -> pd.Series:
    """Count of distinct audit-warning onset episodes in trailing 126-day window."""
    return _count_episodes(audit_warning, _TD_2Q)


def gcf_159_both_flags_rolling_sum_504d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of days BOTH flags active simultaneously in trailing 504-day window."""
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    return _rolling_sum(both, _TD_2Y)


def gcf_160_either_rolling_sum_504d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of days EITHER flag active in trailing 504-day window."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_sum(either, _TD_2Y)


def gcf_161_gc_ewm_intensity_5(going_concern: pd.Series) -> pd.Series:
    """EWM (span=5) smoothed going-concern flag — very short-run (weekly) intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_WK)


def gcf_162_aw_ewm_intensity_5(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=5) smoothed audit-warning flag — very short-run intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_WK)


def gcf_163_gc_ewm_intensity_126(going_concern: pd.Series) -> pd.Series:
    """EWM (span=126) smoothed going-concern flag — 2-quarter intensity."""
    return _ewm_mean(going_concern.astype(float), _TD_2Q)


def gcf_164_aw_ewm_intensity_126(audit_warning: pd.Series) -> pd.Series:
    """EWM (span=126) smoothed audit-warning flag — 2-quarter intensity."""
    return _ewm_mean(audit_warning.astype(float), _TD_2Q)


def gcf_165_close_log_return_21d(close: pd.Series) -> pd.Series:
    """21-day log return of close price (monthly total return)."""
    return np.log(close.clip(lower=_EPS) / close.shift(_TD_MO).clip(lower=_EPS))


def gcf_166_gc_active_at_price_low_504d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """1 if going-concern is active AND close equals its 504-day rolling min."""
    price_low = _rolling_min(close, _TD_2Y)
    at_low = (close <= price_low + _EPS).astype(float)
    return at_low * going_concern.astype(float)


def gcf_167_aw_active_at_price_low_504d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """1 if audit-warning is active AND close equals its 504-day rolling min."""
    price_low = _rolling_min(close, _TD_2Y)
    at_low = (close <= price_low + _EPS).astype(float)
    return at_low * audit_warning.astype(float)


def gcf_168_both_active_at_price_low_252d(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BOTH flags active AND close equals its 252-day rolling min."""
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    price_low = _rolling_min(close, _TD_YEAR)
    at_low = (close <= price_low + _EPS).astype(float)
    return both * at_low


def gcf_169_gc_onset_after_price_drop_63d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """1 on GC onset days where the 63-day price return was negative (flag after drop)."""
    gc_onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    ret_63 = np.log(close.clip(lower=_EPS) / close.shift(_TD_QTR).clip(lower=_EPS))
    price_fell = (ret_63 < 0).astype(float)
    return gc_onset * price_fell


def gcf_170_aw_onset_after_price_drop_63d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """1 on AW onset days where the 63-day price return was negative."""
    aw_onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    ret_63 = np.log(close.clip(lower=_EPS) / close.shift(_TD_QTR).clip(lower=_EPS))
    price_fell = (ret_63 < 0).astype(float)
    return aw_onset * price_fell


def gcf_171_gc_fraction_21d_vs_252d_ratio(going_concern: pd.Series) -> pd.Series:
    """Ratio of 21-day GC fraction to 252-day GC fraction (recent vs annual concentration)."""
    frac_21 = _rolling_mean(going_concern.astype(float), _TD_MO)
    frac_252 = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    return _safe_div(frac_21, frac_252)


def gcf_172_aw_fraction_21d_vs_252d_ratio(audit_warning: pd.Series) -> pd.Series:
    """Ratio of 21-day AW fraction to 252-day AW fraction."""
    frac_21 = _rolling_mean(audit_warning.astype(float), _TD_MO)
    frac_252 = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    return _safe_div(frac_21, frac_252)


def gcf_173_gc_days_at_5y_price_low(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where GC active AND close is at a 5-year low."""
    price_low = _rolling_min(close, _TD_5Y)
    at_low = (close <= price_low + _EPS).astype(float)
    joint = going_concern.astype(float) * at_low
    return _rolling_sum(joint, _TD_YEAR)


def gcf_174_aw_days_at_5y_price_low(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where AW active AND close is at a 5-year low."""
    price_low = _rolling_min(close, _TD_5Y)
    at_low = (close <= price_low + _EPS).astype(float)
    joint = audit_warning.astype(float) * at_low
    return _rolling_sum(joint, _TD_YEAR)


def gcf_175_distress_price_severity_504d(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    Distress-price severity: product of 504-day flag fraction (either flag) and
    absolute percent drawdown from 504-day rolling price high.
    Combines persistence of warning signals with medium-term price deterioration.
    """
    either_frac = _rolling_mean(((going_concern == 1) | (audit_warning == 1)).astype(float), _TD_2Y)
    peak_504 = _rolling_max(close, _TD_2Y)
    dd_pct = _safe_div(close - peak_504, peak_504).clip(lower=-1.0, upper=0.0).abs()
    return either_frac * dd_pct


# ── Registry 001-075 ──────────────────────────────────────────────────────────

GOING_CONCERN_FLAGS_REGISTRY_001_075 = {
    "gcf_001_going_concern_level":              {"inputs": ["going_concern"],                        "func": gcf_001_going_concern_level},
    "gcf_002_audit_warning_level":              {"inputs": ["audit_warning"],                        "func": gcf_002_audit_warning_level},
    "gcf_003_either_flag_active":               {"inputs": ["going_concern", "audit_warning"],       "func": gcf_003_either_flag_active},
    "gcf_004_both_flags_active":                {"inputs": ["going_concern", "audit_warning"],       "func": gcf_004_both_flags_active},
    "gcf_005_gc_only_not_aw":                   {"inputs": ["going_concern", "audit_warning"],       "func": gcf_005_gc_only_not_aw},
    "gcf_006_aw_only_not_gc":                   {"inputs": ["going_concern", "audit_warning"],       "func": gcf_006_aw_only_not_gc},
    "gcf_007_flag_sum":                         {"inputs": ["going_concern", "audit_warning"],       "func": gcf_007_flag_sum},
    "gcf_008_gc_onset_flag":                    {"inputs": ["going_concern"],                        "func": gcf_008_gc_onset_flag},
    "gcf_009_gc_clearing_flag":                 {"inputs": ["going_concern"],                        "func": gcf_009_gc_clearing_flag},
    "gcf_010_aw_onset_flag":                    {"inputs": ["audit_warning"],                        "func": gcf_010_aw_onset_flag},
    "gcf_011_aw_clearing_flag":                 {"inputs": ["audit_warning"],                        "func": gcf_011_aw_clearing_flag},
    "gcf_012_escalation_aw_to_gc":              {"inputs": ["going_concern", "audit_warning"],       "func": gcf_012_escalation_aw_to_gc},
    "gcf_013_gc_streak_length":                 {"inputs": ["going_concern"],                        "func": gcf_013_gc_streak_length},
    "gcf_014_aw_streak_length":                 {"inputs": ["audit_warning"],                        "func": gcf_014_aw_streak_length},
    "gcf_015_combined_streak_length":           {"inputs": ["going_concern", "audit_warning"],       "func": gcf_015_combined_streak_length},
    "gcf_016_gc_rolling_sum_21d":               {"inputs": ["going_concern"],                        "func": gcf_016_gc_rolling_sum_21d},
    "gcf_017_gc_rolling_sum_63d":               {"inputs": ["going_concern"],                        "func": gcf_017_gc_rolling_sum_63d},
    "gcf_018_gc_rolling_sum_126d":              {"inputs": ["going_concern"],                        "func": gcf_018_gc_rolling_sum_126d},
    "gcf_019_gc_rolling_sum_252d":              {"inputs": ["going_concern"],                        "func": gcf_019_gc_rolling_sum_252d},
    "gcf_020_gc_rolling_sum_504d":              {"inputs": ["going_concern"],                        "func": gcf_020_gc_rolling_sum_504d},
    "gcf_021_gc_rolling_sum_756d":              {"inputs": ["going_concern"],                        "func": gcf_021_gc_rolling_sum_756d},
    "gcf_022_aw_rolling_sum_21d":               {"inputs": ["audit_warning"],                        "func": gcf_022_aw_rolling_sum_21d},
    "gcf_023_aw_rolling_sum_63d":               {"inputs": ["audit_warning"],                        "func": gcf_023_aw_rolling_sum_63d},
    "gcf_024_aw_rolling_sum_126d":              {"inputs": ["audit_warning"],                        "func": gcf_024_aw_rolling_sum_126d},
    "gcf_025_aw_rolling_sum_252d":              {"inputs": ["audit_warning"],                        "func": gcf_025_aw_rolling_sum_252d},
    "gcf_026_aw_rolling_sum_504d":              {"inputs": ["audit_warning"],                        "func": gcf_026_aw_rolling_sum_504d},
    "gcf_027_aw_rolling_sum_756d":              {"inputs": ["audit_warning"],                        "func": gcf_027_aw_rolling_sum_756d},
    "gcf_028_either_rolling_sum_63d":           {"inputs": ["going_concern", "audit_warning"],       "func": gcf_028_either_rolling_sum_63d},
    "gcf_029_either_rolling_sum_252d":          {"inputs": ["going_concern", "audit_warning"],       "func": gcf_029_either_rolling_sum_252d},
    "gcf_030_both_rolling_sum_252d":            {"inputs": ["going_concern", "audit_warning"],       "func": gcf_030_both_rolling_sum_252d},
    "gcf_031_gc_fraction_21d":                  {"inputs": ["going_concern"],                        "func": gcf_031_gc_fraction_21d},
    "gcf_032_gc_fraction_63d":                  {"inputs": ["going_concern"],                        "func": gcf_032_gc_fraction_63d},
    "gcf_033_gc_fraction_126d":                 {"inputs": ["going_concern"],                        "func": gcf_033_gc_fraction_126d},
    "gcf_034_gc_fraction_252d":                 {"inputs": ["going_concern"],                        "func": gcf_034_gc_fraction_252d},
    "gcf_035_gc_fraction_504d":                 {"inputs": ["going_concern"],                        "func": gcf_035_gc_fraction_504d},
    "gcf_036_gc_fraction_756d":                 {"inputs": ["going_concern"],                        "func": gcf_036_gc_fraction_756d},
    "gcf_037_aw_fraction_63d":                  {"inputs": ["audit_warning"],                        "func": gcf_037_aw_fraction_63d},
    "gcf_038_aw_fraction_252d":                 {"inputs": ["audit_warning"],                        "func": gcf_038_aw_fraction_252d},
    "gcf_039_aw_fraction_504d":                 {"inputs": ["audit_warning"],                        "func": gcf_039_aw_fraction_504d},
    "gcf_040_aw_fraction_756d":                 {"inputs": ["audit_warning"],                        "func": gcf_040_aw_fraction_756d},
    "gcf_041_either_fraction_252d":             {"inputs": ["going_concern", "audit_warning"],       "func": gcf_041_either_fraction_252d},
    "gcf_042_gc_expanding_fraction":            {"inputs": ["going_concern"],                        "func": gcf_042_gc_expanding_fraction},
    "gcf_043_aw_expanding_fraction":            {"inputs": ["audit_warning"],                        "func": gcf_043_aw_expanding_fraction},
    "gcf_044_gc_cumulative_flagged_days":       {"inputs": ["going_concern"],                        "func": gcf_044_gc_cumulative_flagged_days},
    "gcf_045_aw_cumulative_flagged_days":       {"inputs": ["audit_warning"],                        "func": gcf_045_aw_cumulative_flagged_days},
    "gcf_046_gc_episodes_63d":                  {"inputs": ["going_concern"],                        "func": gcf_046_gc_episodes_63d},
    "gcf_047_gc_episodes_252d":                 {"inputs": ["going_concern"],                        "func": gcf_047_gc_episodes_252d},
    "gcf_048_gc_episodes_504d":                 {"inputs": ["going_concern"],                        "func": gcf_048_gc_episodes_504d},
    "gcf_049_gc_episodes_756d":                 {"inputs": ["going_concern"],                        "func": gcf_049_gc_episodes_756d},
    "gcf_050_aw_episodes_252d":                 {"inputs": ["audit_warning"],                        "func": gcf_050_aw_episodes_252d},
    "gcf_051_aw_episodes_504d":                 {"inputs": ["audit_warning"],                        "func": gcf_051_aw_episodes_504d},
    "gcf_052_days_since_gc_onset":              {"inputs": ["going_concern"],                        "func": gcf_052_days_since_gc_onset},
    "gcf_053_days_since_aw_onset":              {"inputs": ["audit_warning"],                        "func": gcf_053_days_since_aw_onset},
    "gcf_054_days_since_gc_clearing":           {"inputs": ["going_concern"],                        "func": gcf_054_days_since_gc_clearing},
    "gcf_055_days_since_aw_clearing":           {"inputs": ["audit_warning"],                        "func": gcf_055_days_since_aw_clearing},
    "gcf_056_longest_gc_spell_252d":            {"inputs": ["going_concern"],                        "func": gcf_056_longest_gc_spell_252d},
    "gcf_057_longest_gc_spell_504d":            {"inputs": ["going_concern"],                        "func": gcf_057_longest_gc_spell_504d},
    "gcf_058_longest_aw_spell_252d":            {"inputs": ["audit_warning"],                        "func": gcf_058_longest_aw_spell_252d},
    "gcf_059_gc_streak_vs_252d_max":            {"inputs": ["going_concern"],                        "func": gcf_059_gc_streak_vs_252d_max},
    "gcf_060_aw_streak_vs_252d_max":            {"inputs": ["audit_warning"],                        "func": gcf_060_aw_streak_vs_252d_max},
    "gcf_061_gc_ewm_intensity_21":              {"inputs": ["going_concern"],                        "func": gcf_061_gc_ewm_intensity_21},
    "gcf_062_gc_ewm_intensity_63":              {"inputs": ["going_concern"],                        "func": gcf_062_gc_ewm_intensity_63},
    "gcf_063_gc_ewm_intensity_252":             {"inputs": ["going_concern"],                        "func": gcf_063_gc_ewm_intensity_252},
    "gcf_064_aw_ewm_intensity_63":              {"inputs": ["audit_warning"],                        "func": gcf_064_aw_ewm_intensity_63},
    "gcf_065_aw_ewm_intensity_252":             {"inputs": ["audit_warning"],                        "func": gcf_065_aw_ewm_intensity_252},
    "gcf_066_gc_flag_weighted_close":           {"inputs": ["going_concern", "close"],               "func": gcf_066_gc_flag_weighted_close},
    "gcf_067_aw_flag_weighted_close":           {"inputs": ["audit_warning", "close"],               "func": gcf_067_aw_flag_weighted_close},
    "gcf_068_gc_price_drawdown_during_flag":    {"inputs": ["going_concern", "close"],               "func": gcf_068_gc_price_drawdown_during_flag},
    "gcf_069_aw_price_drawdown_during_flag":    {"inputs": ["audit_warning", "close"],               "func": gcf_069_aw_price_drawdown_during_flag},
    "gcf_070_gc_flag_weighted_price_decline_252d": {"inputs": ["going_concern", "close"],            "func": gcf_070_gc_flag_weighted_price_decline_252d},
    "gcf_071_aw_flag_weighted_price_decline_252d": {"inputs": ["audit_warning", "close"],            "func": gcf_071_aw_flag_weighted_price_decline_252d},
    "gcf_072_close_pct_drawdown_expanding":     {"inputs": ["close"],                                "func": gcf_072_close_pct_drawdown_expanding},
    "gcf_073_gc_active_at_price_low_252d":      {"inputs": ["going_concern", "close"],               "func": gcf_073_gc_active_at_price_low_252d},
    "gcf_074_aw_active_at_price_low_252d":      {"inputs": ["audit_warning", "close"],               "func": gcf_074_aw_active_at_price_low_252d},
    "gcf_075_combined_distress_composite":      {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_075_combined_distress_composite},
    "gcf_151_gc_rolling_median_63d":            {"inputs": ["going_concern"],                        "func": gcf_151_gc_rolling_median_63d},
    "gcf_152_aw_rolling_median_63d":            {"inputs": ["audit_warning"],                        "func": gcf_152_aw_rolling_median_63d},
    "gcf_153_gc_rolling_median_252d":           {"inputs": ["going_concern"],                        "func": gcf_153_gc_rolling_median_252d},
    "gcf_154_aw_rolling_median_252d":           {"inputs": ["audit_warning"],                        "func": gcf_154_aw_rolling_median_252d},
    "gcf_155_gc_streak_normalized_504d":        {"inputs": ["going_concern"],                        "func": gcf_155_gc_streak_normalized_504d},
    "gcf_156_aw_streak_normalized_504d":        {"inputs": ["audit_warning"],                        "func": gcf_156_aw_streak_normalized_504d},
    "gcf_157_gc_episodes_126d":                 {"inputs": ["going_concern"],                        "func": gcf_157_gc_episodes_126d},
    "gcf_158_aw_episodes_126d":                 {"inputs": ["audit_warning"],                        "func": gcf_158_aw_episodes_126d},
    "gcf_159_both_flags_rolling_sum_504d":      {"inputs": ["going_concern", "audit_warning"],       "func": gcf_159_both_flags_rolling_sum_504d},
    "gcf_160_either_rolling_sum_504d":          {"inputs": ["going_concern", "audit_warning"],       "func": gcf_160_either_rolling_sum_504d},
    "gcf_161_gc_ewm_intensity_5":               {"inputs": ["going_concern"],                        "func": gcf_161_gc_ewm_intensity_5},
    "gcf_162_aw_ewm_intensity_5":               {"inputs": ["audit_warning"],                        "func": gcf_162_aw_ewm_intensity_5},
    "gcf_163_gc_ewm_intensity_126":             {"inputs": ["going_concern"],                        "func": gcf_163_gc_ewm_intensity_126},
    "gcf_164_aw_ewm_intensity_126":             {"inputs": ["audit_warning"],                        "func": gcf_164_aw_ewm_intensity_126},
    "gcf_165_close_log_return_21d":             {"inputs": ["close"],                                "func": gcf_165_close_log_return_21d},
    "gcf_166_gc_active_at_price_low_504d":      {"inputs": ["going_concern", "close"],               "func": gcf_166_gc_active_at_price_low_504d},
    "gcf_167_aw_active_at_price_low_504d":      {"inputs": ["audit_warning", "close"],               "func": gcf_167_aw_active_at_price_low_504d},
    "gcf_168_both_active_at_price_low_252d":    {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_168_both_active_at_price_low_252d},
    "gcf_169_gc_onset_after_price_drop_63d":    {"inputs": ["going_concern", "close"],               "func": gcf_169_gc_onset_after_price_drop_63d},
    "gcf_170_aw_onset_after_price_drop_63d":    {"inputs": ["audit_warning", "close"],               "func": gcf_170_aw_onset_after_price_drop_63d},
    "gcf_171_gc_fraction_21d_vs_252d_ratio":    {"inputs": ["going_concern"],                        "func": gcf_171_gc_fraction_21d_vs_252d_ratio},
    "gcf_172_aw_fraction_21d_vs_252d_ratio":    {"inputs": ["audit_warning"],                        "func": gcf_172_aw_fraction_21d_vs_252d_ratio},
    "gcf_173_gc_days_at_5y_price_low":          {"inputs": ["going_concern", "close"],               "func": gcf_173_gc_days_at_5y_price_low},
    "gcf_174_aw_days_at_5y_price_low":          {"inputs": ["audit_warning", "close"],               "func": gcf_174_aw_days_at_5y_price_low},
    "gcf_175_distress_price_severity_504d":     {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_175_distress_price_severity_504d},
}
