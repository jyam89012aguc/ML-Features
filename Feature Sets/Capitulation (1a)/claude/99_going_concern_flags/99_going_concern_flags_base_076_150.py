"""
99_going_concern_flags — Base Features 076-200
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


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den."""
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
    """Trading days since the most recent 1 in flag; NaN before first occurrence."""
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
    """Count distinct flag onset episodes within a rolling window w."""
    onset = ((flag == 1) & (flag.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, w)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Lead/lag relationships and temporal sequencing ---

def gcf_076_aw_precedes_gc_within_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if audit-warning was active at any point in the prior 252 days before current GC onset."""
    gc_onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    aw_prior = _rolling_sum(audit_warning.astype(float).shift(1), _TD_YEAR)
    return (gc_onset * (aw_prior > 0)).astype(float)


def gcf_077_gc_lag_after_aw_onset_days(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """
    Days elapsed between most-recent audit-warning onset and most-recent GC onset.
    Positive = GC followed AW; NaN if either event not yet observed.
    """
    aw_onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    gc_onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    days_since_aw = _days_since_last_one(aw_onset)
    days_since_gc = _days_since_last_one(gc_onset)
    return days_since_aw - days_since_gc


def gcf_078_gc_active_after_aw_cleared(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if going-concern is active but audit-warning has been cleared (GC persists alone)."""
    return ((going_concern == 1) & (audit_warning == 0)).astype(float)


def gcf_079_aw_active_after_gc_cleared(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if audit-warning is active but going-concern has been cleared."""
    return ((audit_warning == 1) & (going_concern == 0)).astype(float)


def gcf_080_gc_reactivation_within_252d(going_concern: pd.Series) -> pd.Series:
    """1 on any going-concern onset when GC was also active in prior 252-day window."""
    gc_onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    prior_gc_sum = _rolling_sum(going_concern.astype(float).shift(1), _TD_YEAR)
    return (gc_onset * (prior_gc_sum > 0)).astype(float)


def gcf_081_aw_reactivation_within_252d(audit_warning: pd.Series) -> pd.Series:
    """1 on any audit-warning onset when AW was also active in prior 252-day window."""
    aw_onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    prior_aw_sum = _rolling_sum(audit_warning.astype(float).shift(1), _TD_YEAR)
    return (aw_onset * (prior_aw_sum > 0)).astype(float)


def gcf_082_gc_onset_count_expanding(going_concern: pd.Series) -> pd.Series:
    """Cumulative count of going-concern onset events over all history."""
    onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    return onset.expanding(min_periods=1).sum()


def gcf_083_aw_onset_count_expanding(audit_warning: pd.Series) -> pd.Series:
    """Cumulative count of audit-warning onset events over all history."""
    onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    return onset.expanding(min_periods=1).sum()


def gcf_084_gc_prior_1y_flag_before_current(going_concern: pd.Series) -> pd.Series:
    """GC flag value exactly 252 trading days ago (lagged annual snapshot)."""
    return going_concern.shift(_TD_YEAR).astype(float)


def gcf_085_aw_prior_1y_flag_before_current(audit_warning: pd.Series) -> pd.Series:
    """AW flag value exactly 252 trading days ago."""
    return audit_warning.shift(_TD_YEAR).astype(float)


def gcf_086_gc_prior_2y_flag_before_current(going_concern: pd.Series) -> pd.Series:
    """GC flag value exactly 504 trading days ago."""
    return going_concern.shift(_TD_2Y).astype(float)


def gcf_087_aw_prior_2y_flag_before_current(audit_warning: pd.Series) -> pd.Series:
    """AW flag value exactly 504 trading days ago."""
    return audit_warning.shift(_TD_2Y).astype(float)


def gcf_088_gc_new_this_year(going_concern: pd.Series) -> pd.Series:
    """1 if going-concern is currently active but was NOT active 252 days ago."""
    return ((going_concern == 1) & (going_concern.shift(_TD_YEAR).fillna(0) == 0)).astype(float)


def gcf_089_aw_new_this_year(audit_warning: pd.Series) -> pd.Series:
    """1 if audit-warning is currently active but was NOT active 252 days ago."""
    return ((audit_warning == 1) & (audit_warning.shift(_TD_YEAR).fillna(0) == 0)).astype(float)


def gcf_090_gc_cleared_this_year(going_concern: pd.Series) -> pd.Series:
    """1 if going-concern is currently OFF but WAS active 252 days ago."""
    return ((going_concern == 0) & (going_concern.shift(_TD_YEAR).fillna(0) == 1)).astype(float)


# --- Group G (091-105): Rolling z-scores and percentile ranks of flag intensity ---

def gcf_091_gc_fraction_63d_zscore_252d(going_concern: pd.Series) -> pd.Series:
    """Z-score of the 63-day GC fraction within a 252-day rolling window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_QTR)
    return _zscore_rolling(frac, _TD_YEAR)


def gcf_092_gc_fraction_252d_zscore_504d(going_concern: pd.Series) -> pd.Series:
    """Z-score of the 252-day GC fraction within a 504-day rolling window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    return _zscore_rolling(frac, _TD_2Y)


def gcf_093_aw_fraction_63d_zscore_252d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of the 63-day AW fraction within a 252-day rolling window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_QTR)
    return _zscore_rolling(frac, _TD_YEAR)


def gcf_094_aw_fraction_252d_zscore_504d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of the 252-day AW fraction within a 504-day rolling window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    return _zscore_rolling(frac, _TD_2Y)


def gcf_095_gc_streak_zscore_252d(going_concern: pd.Series) -> pd.Series:
    """Z-score of current GC streak length within a 252-day rolling window."""
    streak = _streak_length(going_concern)
    return _zscore_rolling(streak, _TD_YEAR)


def gcf_096_aw_streak_zscore_252d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of current AW streak length within a 252-day rolling window."""
    streak = _streak_length(audit_warning)
    return _zscore_rolling(streak, _TD_YEAR)


def gcf_097_gc_fraction_pct_rank_504d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of current GC fraction (63-day) within a 504-day window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_QTR)
    return _rolling_rank_pct(frac, _TD_2Y)


def gcf_098_aw_fraction_pct_rank_504d(audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of current AW fraction (63-day) within a 504-day window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_QTR)
    return _rolling_rank_pct(frac, _TD_2Y)


def gcf_099_flag_sum_zscore_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Z-score of daily flag sum (0/1/2) within a 252-day rolling window."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _zscore_rolling(s, _TD_YEAR)


def gcf_100_flag_sum_pct_rank_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of daily flag sum within trailing 252-day window."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_rank_pct(s, _TD_YEAR)


def gcf_101_gc_expanding_zscore(going_concern: pd.Series) -> pd.Series:
    """Expanding z-score of going-concern flag (how extreme current value vs entire history)."""
    gc = going_concern.astype(float)
    m  = gc.expanding(min_periods=2).mean()
    sd = gc.expanding(min_periods=2).std()
    return _safe_div(gc - m, sd)


def gcf_102_aw_expanding_zscore(audit_warning: pd.Series) -> pd.Series:
    """Expanding z-score of audit-warning flag."""
    aw = audit_warning.astype(float)
    m  = aw.expanding(min_periods=2).mean()
    sd = aw.expanding(min_periods=2).std()
    return _safe_div(aw - m, sd)


def gcf_103_gc_streak_pct_rank_252d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of GC streak length within trailing 252-day window."""
    streak = _streak_length(going_concern)
    return _rolling_rank_pct(streak, _TD_YEAR)


def gcf_104_aw_streak_pct_rank_252d(audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of AW streak length within trailing 252-day window."""
    streak = _streak_length(audit_warning)
    return _rolling_rank_pct(streak, _TD_YEAR)


def gcf_105_gc_ewm_deviation_from_252d_mean(going_concern: pd.Series) -> pd.Series:
    """GC EWM (span=63) minus its 252-day rolling mean — momentum deviation."""
    ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    mean = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    return ewm - mean


# --- Group H (106-120): Price-flag interaction depth features ---

def gcf_106_close_rolling_min_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day minimum close price."""
    return _rolling_min(close, _TD_YEAR)


def gcf_107_close_rolling_min_504d(close: pd.Series) -> pd.Series:
    """Rolling 504-day minimum close price."""
    return _rolling_min(close, _TD_2Y)


def gcf_108_close_rolling_min_756d(close: pd.Series) -> pd.Series:
    """Rolling 756-day minimum close price."""
    return _rolling_min(close, _TD_3Y)


def gcf_109_close_pct_from_252d_min(close: pd.Series) -> pd.Series:
    """Percent of close above its 252-day rolling minimum (proximity to 1-year low)."""
    low = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - low, low)


def gcf_110_close_pct_from_504d_min(close: pd.Series) -> pd.Series:
    """Percent of close above its 504-day rolling minimum."""
    low = _rolling_min(close, _TD_2Y)
    return _safe_div(close - low, low)


def gcf_111_close_pct_from_756d_min(close: pd.Series) -> pd.Series:
    """Percent of close above its 756-day rolling minimum."""
    low = _rolling_min(close, _TD_3Y)
    return _safe_div(close - low, low)


def gcf_112_gc_flag_times_price_dd_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by percent drawdown from 252-day price high (interaction term)."""
    peak = _rolling_max(close, _TD_YEAR)
    dd_pct = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd_pct


def gcf_113_aw_flag_times_price_dd_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag multiplied by percent drawdown from 252-day price high."""
    peak = _rolling_max(close, _TD_YEAR)
    dd_pct = _safe_div(close - peak, peak)
    return audit_warning.astype(float) * dd_pct


def gcf_114_both_flags_times_price_dd_252d(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Both-flags indicator multiplied by 252-day price drawdown percent."""
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    peak = _rolling_max(close, _TD_YEAR)
    dd_pct = _safe_div(close - peak, peak)
    return both * dd_pct


def gcf_115_gc_flag_times_price_dd_expanding(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag times percent drawdown from all-time expanding price peak."""
    peak = close.expanding(min_periods=1).max()
    dd_pct = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd_pct


def gcf_116_aw_flag_times_price_dd_expanding(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag times percent drawdown from all-time expanding price peak."""
    peak = close.expanding(min_periods=1).max()
    dd_pct = _safe_div(close - peak, peak)
    return audit_warning.astype(float) * dd_pct


def gcf_117_gc_days_while_price_below_252d_ma(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where GC active AND close below 252-day MA."""
    ma = _rolling_mean(close, _TD_YEAR)
    joint = (going_concern.astype(float) * (close < ma).astype(float))
    return _rolling_sum(joint, _TD_YEAR)


def gcf_118_aw_days_while_price_below_252d_ma(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where AW active AND close below 252-day MA."""
    ma = _rolling_mean(close, _TD_YEAR)
    joint = (audit_warning.astype(float) * (close < ma).astype(float))
    return _rolling_sum(joint, _TD_YEAR)


def gcf_119_gc_weighted_log_price_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day mean of log(close) on going-concern flagged days only (NaN elsewhere)."""
    log_close = np.log(close.clip(lower=_EPS))
    flagged = log_close.where(going_concern == 1, other=np.nan)
    return flagged.rolling(_TD_YEAR, min_periods=1).mean()


def gcf_120_close_pct_rank_5y(close: pd.Series) -> pd.Series:
    """Percentile rank of close price within its trailing 5-year (1260-day) window."""
    return _rolling_rank_pct(close, _TD_5Y)


# --- Group I (121-135): Combined flag sums, ratios, and multi-window features ---

def gcf_121_gc_rolling_sum_1260d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 1260-day (5-year) window."""
    return _rolling_sum(going_concern.astype(float), _TD_5Y)


def gcf_122_aw_rolling_sum_1260d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 1260-day (5-year) window."""
    return _rolling_sum(audit_warning.astype(float), _TD_5Y)


def gcf_123_gc_fraction_1260d(going_concern: pd.Series) -> pd.Series:
    """Fraction of 5-year window where going-concern was active."""
    return _rolling_mean(going_concern.astype(float), _TD_5Y)


def gcf_124_aw_fraction_1260d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of 5-year window where audit-warning was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_5Y)


def gcf_125_gc_to_aw_fraction_ratio_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Ratio of 252-day GC fraction to 252-day AW fraction; captures relative severity."""
    gc_frac = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    aw_frac = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    return _safe_div(gc_frac, aw_frac)


def gcf_126_gc_fraction_change_63d_vs_252d(going_concern: pd.Series) -> pd.Series:
    """Difference of 63-day GC fraction minus 252-day GC fraction (recent vs annual)."""
    frac_63 = _rolling_mean(going_concern.astype(float), _TD_QTR)
    frac_252 = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    return frac_63 - frac_252


def gcf_127_aw_fraction_change_63d_vs_252d(audit_warning: pd.Series) -> pd.Series:
    """Difference of 63-day AW fraction minus 252-day AW fraction."""
    frac_63 = _rolling_mean(audit_warning.astype(float), _TD_QTR)
    frac_252 = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    return frac_63 - frac_252


def gcf_128_gc_fraction_252d_minus_504d(going_concern: pd.Series) -> pd.Series:
    """252-day GC fraction minus 504-day GC fraction (recent vs 2-year)."""
    frac_252 = _rolling_mean(going_concern.astype(float), _TD_YEAR)
    frac_504 = _rolling_mean(going_concern.astype(float), _TD_2Y)
    return frac_252 - frac_504


def gcf_129_aw_fraction_252d_minus_504d(audit_warning: pd.Series) -> pd.Series:
    """252-day AW fraction minus 504-day AW fraction."""
    frac_252 = _rolling_mean(audit_warning.astype(float), _TD_YEAR)
    frac_504 = _rolling_mean(audit_warning.astype(float), _TD_2Y)
    return frac_252 - frac_504


def gcf_130_gc_ewm_21_minus_ewm_252(going_concern: pd.Series) -> pd.Series:
    """Short EWM (span=21) minus long EWM (span=252) of GC flag — momentum cross."""
    short = _ewm_mean(going_concern.astype(float), _TD_MO)
    long_ = _ewm_mean(going_concern.astype(float), _TD_YEAR)
    return short - long_


def gcf_131_aw_ewm_21_minus_ewm_252(audit_warning: pd.Series) -> pd.Series:
    """Short EWM (span=21) minus long EWM (span=252) of AW flag."""
    short = _ewm_mean(audit_warning.astype(float), _TD_MO)
    long_ = _ewm_mean(audit_warning.astype(float), _TD_YEAR)
    return short - long_


def gcf_132_either_episodes_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of distinct 'either-flag' onset episodes in trailing 252-day window."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _count_episodes(either, _TD_YEAR)


def gcf_133_either_episodes_504d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Count of distinct 'either-flag' onset episodes in trailing 504-day window."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _count_episodes(either, _TD_2Y)


def gcf_134_combined_flagged_day_count_expanding(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Cumulative count of days EITHER flag was active over all history."""
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return either.expanding(min_periods=1).sum()


def gcf_135_flag_sum_rolling_mean_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """Rolling 63-day mean of the daily flag sum (0/1/2) — short-run intensity."""
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_mean(s, _TD_QTR)


# --- Group J (136-150): Close-price log-return features during flag periods ---

def gcf_136_log_return_1d(close: pd.Series) -> pd.Series:
    """Daily log return of close price."""
    return np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def gcf_137_gc_flagged_log_ret_sum_63d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of daily log returns on going-concern flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr * going_concern.astype(float)
    return _rolling_sum(flagged, _TD_QTR)


def gcf_138_aw_flagged_log_ret_sum_63d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of daily log returns on audit-warning flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr * audit_warning.astype(float)
    return _rolling_sum(flagged, _TD_QTR)


def gcf_139_gc_flagged_log_ret_sum_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day sum of daily log returns on going-concern flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr * going_concern.astype(float)
    return _rolling_sum(flagged, _TD_YEAR)


def gcf_140_aw_flagged_log_ret_sum_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day sum of daily log returns on audit-warning flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr * audit_warning.astype(float)
    return _rolling_sum(flagged, _TD_YEAR)


def gcf_141_close_log_return_63d(close: pd.Series) -> pd.Series:
    """63-day log return of close price (quarterly total return)."""
    return np.log(close.clip(lower=_EPS) / close.shift(_TD_QTR).clip(lower=_EPS))


def gcf_142_close_log_return_252d(close: pd.Series) -> pd.Series:
    """252-day log return of close price (annual total return)."""
    return np.log(close.clip(lower=_EPS) / close.shift(_TD_YEAR).clip(lower=_EPS))


def gcf_143_close_log_return_504d(close: pd.Series) -> pd.Series:
    """504-day log return of close price (2-year total return)."""
    return np.log(close.clip(lower=_EPS) / close.shift(_TD_2Y).clip(lower=_EPS))


def gcf_144_gc_flag_times_log_ret_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag level multiplied by 252-day log return (combined severity signal)."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(_TD_YEAR).clip(lower=_EPS))
    return going_concern.astype(float) * lr


def gcf_145_aw_flag_times_log_ret_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag level multiplied by 252-day log return."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(_TD_YEAR).clip(lower=_EPS))
    return audit_warning.astype(float) * lr


def gcf_146_close_rolling_std_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of daily log returns (short-run volatility)."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    return _rolling_std(lr, _TD_QTR)


def gcf_147_close_rolling_std_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day standard deviation of daily log returns (annual volatility)."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    return _rolling_std(lr, _TD_YEAR)


def gcf_148_gc_flag_times_volatility_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by 252-day realized volatility of log returns."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    vol = _rolling_std(lr, _TD_YEAR)
    return going_concern.astype(float) * vol


def gcf_149_aw_flag_times_volatility_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag multiplied by 252-day realized volatility of log returns."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    vol = _rolling_std(lr, _TD_YEAR)
    return audit_warning.astype(float) * vol


def gcf_150_audit_distress_severity_index(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite audit-distress severity index:
    (GC_ewm_63 * 2 + AW_ewm_63) / 3 * abs(pct_drawdown_from_expanding_peak).
    Combines flag intensity with price depth; higher = more distress.
    """
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    flag_intensity = (gc_ewm * 2.0 + aw_ewm) / 3.0
    peak = close.expanding(min_periods=1).max()
    dd_pct = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    return flag_intensity * dd_pct


# --- Group K (176-200): New windows, vol, and interaction features ---

def gcf_176_gc_aw_cleared_this_year(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """1 if BOTH flags are currently OFF but EITHER was active 252 days ago."""
    either_now = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    either_1y = ((going_concern.shift(_TD_YEAR).fillna(0) == 1) |
                 (audit_warning.shift(_TD_YEAR).fillna(0) == 1)).astype(float)
    return ((either_now == 0) & (either_1y == 1)).astype(float)


def gcf_177_gc_rolling_sum_5d(going_concern: pd.Series) -> pd.Series:
    """Count of going-concern flagged days in trailing 5-day (1-week) window."""
    return _rolling_sum(going_concern.astype(float), _TD_WK)


def gcf_178_aw_rolling_sum_5d(audit_warning: pd.Series) -> pd.Series:
    """Count of audit-warning flagged days in trailing 5-day window."""
    return _rolling_sum(audit_warning.astype(float), _TD_WK)


def gcf_179_gc_fraction_5d(going_concern: pd.Series) -> pd.Series:
    """Fraction of trailing 5-day window where going-concern flag was active."""
    return _rolling_mean(going_concern.astype(float), _TD_WK)


def gcf_180_aw_fraction_5d(audit_warning: pd.Series) -> pd.Series:
    """Fraction of trailing 5-day window where audit-warning flag was active."""
    return _rolling_mean(audit_warning.astype(float), _TD_WK)


def gcf_181_gc_streak_pct_rank_504d(going_concern: pd.Series) -> pd.Series:
    """Percentile rank of GC streak length within trailing 504-day window."""
    streak = _streak_length(going_concern)
    return _rolling_rank_pct(streak, _TD_2Y)


def gcf_182_aw_streak_pct_rank_504d(audit_warning: pd.Series) -> pd.Series:
    """Percentile rank of AW streak length within trailing 504-day window."""
    streak = _streak_length(audit_warning)
    return _rolling_rank_pct(streak, _TD_2Y)


def gcf_183_gc_fraction_126d_zscore_504d(going_concern: pd.Series) -> pd.Series:
    """Z-score of the 126-day GC fraction within a 504-day rolling window."""
    frac = _rolling_mean(going_concern.astype(float), _TD_2Q)
    return _zscore_rolling(frac, _TD_2Y)


def gcf_184_aw_fraction_126d_zscore_504d(audit_warning: pd.Series) -> pd.Series:
    """Z-score of the 126-day AW fraction within a 504-day rolling window."""
    frac = _rolling_mean(audit_warning.astype(float), _TD_2Q)
    return _zscore_rolling(frac, _TD_2Y)


def gcf_185_close_pct_from_1260d_min(close: pd.Series) -> pd.Series:
    """Percent of close above its 1260-day (5-year) rolling minimum."""
    low = _rolling_min(close, _TD_5Y)
    return _safe_div(close - low, low)


def gcf_186_close_rolling_max_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day maximum close price."""
    return _rolling_max(close, _TD_YEAR)


def gcf_187_close_rolling_max_504d(close: pd.Series) -> pd.Series:
    """Rolling 504-day maximum close price."""
    return _rolling_max(close, _TD_2Y)


def gcf_188_gc_flag_times_price_dd_504d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """GC flag multiplied by percent drawdown from 504-day price high."""
    peak = _rolling_max(close, _TD_2Y)
    dd_pct = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd_pct


def gcf_189_aw_flag_times_price_dd_504d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """AW flag multiplied by percent drawdown from 504-day price high."""
    peak = _rolling_max(close, _TD_2Y)
    dd_pct = _safe_div(close - peak, peak)
    return audit_warning.astype(float) * dd_pct


def gcf_190_gc_vol_during_flag_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day std of daily log returns on going-concern flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr.where(going_concern == 1, other=np.nan)
    return flagged.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()


def gcf_191_aw_vol_during_flag_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day std of daily log returns on audit-warning flagged days only."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    flagged = lr.where(audit_warning == 1, other=np.nan)
    return flagged.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()


def gcf_192_gc_days_below_63d_ma(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where GC active AND close below 63-day MA."""
    ma = _rolling_mean(close, _TD_QTR)
    joint = going_concern.astype(float) * (close < ma).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def gcf_193_aw_days_below_63d_ma(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where AW active AND close below 63-day MA."""
    ma = _rolling_mean(close, _TD_QTR)
    joint = audit_warning.astype(float) * (close < ma).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def gcf_194_close_vol_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day log-return volatility to 252-day log-return volatility."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    vol_63 = _rolling_std(lr, _TD_QTR)
    vol_252 = _rolling_std(lr, _TD_YEAR)
    return _safe_div(vol_63, vol_252)


def gcf_195_gc_flagged_neg_ret_count_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of negative-return days while going-concern flag active."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    neg_and_flagged = ((lr < 0) & (going_concern == 1)).astype(float)
    return _rolling_sum(neg_and_flagged, _TD_YEAR)


def gcf_196_aw_flagged_neg_ret_count_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day count of negative-return days while audit-warning flag active."""
    lr = np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    neg_and_flagged = ((lr < 0) & (audit_warning == 1)).astype(float)
    return _rolling_sum(neg_and_flagged, _TD_YEAR)


def gcf_197_gc_expanding_episode_rate(going_concern: pd.Series) -> pd.Series:
    """Expanding-window rate of GC onset episodes per 252 days (episodes / elapsed_years)."""
    onset = ((going_concern == 1) & (going_concern.shift(1).fillna(0) == 0)).astype(float)
    cum_episodes = onset.expanding(min_periods=1).sum()
    elapsed = pd.Series(np.arange(1, len(going_concern) + 1, dtype=float), index=going_concern.index)
    return _safe_div(cum_episodes * _TD_YEAR, elapsed)


def gcf_198_aw_expanding_episode_rate(audit_warning: pd.Series) -> pd.Series:
    """Expanding-window rate of AW onset episodes per 252 days."""
    onset = ((audit_warning == 1) & (audit_warning.shift(1).fillna(0) == 0)).astype(float)
    cum_episodes = onset.expanding(min_periods=1).sum()
    elapsed = pd.Series(np.arange(1, len(audit_warning) + 1, dtype=float), index=audit_warning.index)
    return _safe_div(cum_episodes * _TD_YEAR, elapsed)


def gcf_199_gc_aw_flag_product_ewm_63(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """EWM (span=63) of the product of GC * AW flag — smooth co-occurrence intensity."""
    product = going_concern.astype(float) * audit_warning.astype(float)
    return _ewm_mean(product, _TD_QTR)


def gcf_200_triple_distress_composite_504d(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    504-day composite: equally-weighted (gc_frac_504d, aw_frac_504d,
    abs pct drawdown from 504-day peak).  Wider window than gcf_075.
    """
    gc_frac = _rolling_mean(going_concern.astype(float), _TD_2Y)
    aw_frac = _rolling_mean(audit_warning.astype(float), _TD_2Y)
    peak = _rolling_max(close, _TD_2Y)
    dd_pct = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    return (gc_frac + aw_frac + dd_pct) / 3.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

GOING_CONCERN_FLAGS_REGISTRY_076_150 = {
    "gcf_076_aw_precedes_gc_within_252d":          {"inputs": ["going_concern", "audit_warning"],            "func": gcf_076_aw_precedes_gc_within_252d},
    "gcf_077_gc_lag_after_aw_onset_days":          {"inputs": ["going_concern", "audit_warning"],            "func": gcf_077_gc_lag_after_aw_onset_days},
    "gcf_078_gc_active_after_aw_cleared":          {"inputs": ["going_concern", "audit_warning"],            "func": gcf_078_gc_active_after_aw_cleared},
    "gcf_079_aw_active_after_gc_cleared":          {"inputs": ["going_concern", "audit_warning"],            "func": gcf_079_aw_active_after_gc_cleared},
    "gcf_080_gc_reactivation_within_252d":         {"inputs": ["going_concern"],                             "func": gcf_080_gc_reactivation_within_252d},
    "gcf_081_aw_reactivation_within_252d":         {"inputs": ["audit_warning"],                             "func": gcf_081_aw_reactivation_within_252d},
    "gcf_082_gc_onset_count_expanding":            {"inputs": ["going_concern"],                             "func": gcf_082_gc_onset_count_expanding},
    "gcf_083_aw_onset_count_expanding":            {"inputs": ["audit_warning"],                             "func": gcf_083_aw_onset_count_expanding},
    "gcf_084_gc_prior_1y_flag_before_current":     {"inputs": ["going_concern"],                             "func": gcf_084_gc_prior_1y_flag_before_current},
    "gcf_085_aw_prior_1y_flag_before_current":     {"inputs": ["audit_warning"],                             "func": gcf_085_aw_prior_1y_flag_before_current},
    "gcf_086_gc_prior_2y_flag_before_current":     {"inputs": ["going_concern"],                             "func": gcf_086_gc_prior_2y_flag_before_current},
    "gcf_087_aw_prior_2y_flag_before_current":     {"inputs": ["audit_warning"],                             "func": gcf_087_aw_prior_2y_flag_before_current},
    "gcf_088_gc_new_this_year":                    {"inputs": ["going_concern"],                             "func": gcf_088_gc_new_this_year},
    "gcf_089_aw_new_this_year":                    {"inputs": ["audit_warning"],                             "func": gcf_089_aw_new_this_year},
    "gcf_090_gc_cleared_this_year":                {"inputs": ["going_concern"],                             "func": gcf_090_gc_cleared_this_year},
    "gcf_091_gc_fraction_63d_zscore_252d":         {"inputs": ["going_concern"],                             "func": gcf_091_gc_fraction_63d_zscore_252d},
    "gcf_092_gc_fraction_252d_zscore_504d":        {"inputs": ["going_concern"],                             "func": gcf_092_gc_fraction_252d_zscore_504d},
    "gcf_093_aw_fraction_63d_zscore_252d":         {"inputs": ["audit_warning"],                             "func": gcf_093_aw_fraction_63d_zscore_252d},
    "gcf_094_aw_fraction_252d_zscore_504d":        {"inputs": ["audit_warning"],                             "func": gcf_094_aw_fraction_252d_zscore_504d},
    "gcf_095_gc_streak_zscore_252d":               {"inputs": ["going_concern"],                             "func": gcf_095_gc_streak_zscore_252d},
    "gcf_096_aw_streak_zscore_252d":               {"inputs": ["audit_warning"],                             "func": gcf_096_aw_streak_zscore_252d},
    "gcf_097_gc_fraction_pct_rank_504d":           {"inputs": ["going_concern"],                             "func": gcf_097_gc_fraction_pct_rank_504d},
    "gcf_098_aw_fraction_pct_rank_504d":           {"inputs": ["audit_warning"],                             "func": gcf_098_aw_fraction_pct_rank_504d},
    "gcf_099_flag_sum_zscore_252d":                {"inputs": ["going_concern", "audit_warning"],            "func": gcf_099_flag_sum_zscore_252d},
    "gcf_100_flag_sum_pct_rank_252d":              {"inputs": ["going_concern", "audit_warning"],            "func": gcf_100_flag_sum_pct_rank_252d},
    "gcf_101_gc_expanding_zscore":                 {"inputs": ["going_concern"],                             "func": gcf_101_gc_expanding_zscore},
    "gcf_102_aw_expanding_zscore":                 {"inputs": ["audit_warning"],                             "func": gcf_102_aw_expanding_zscore},
    "gcf_103_gc_streak_pct_rank_252d":             {"inputs": ["going_concern"],                             "func": gcf_103_gc_streak_pct_rank_252d},
    "gcf_104_aw_streak_pct_rank_252d":             {"inputs": ["audit_warning"],                             "func": gcf_104_aw_streak_pct_rank_252d},
    "gcf_105_gc_ewm_deviation_from_252d_mean":     {"inputs": ["going_concern"],                             "func": gcf_105_gc_ewm_deviation_from_252d_mean},
    "gcf_106_close_rolling_min_252d":              {"inputs": ["close"],                                     "func": gcf_106_close_rolling_min_252d},
    "gcf_107_close_rolling_min_504d":              {"inputs": ["close"],                                     "func": gcf_107_close_rolling_min_504d},
    "gcf_108_close_rolling_min_756d":              {"inputs": ["close"],                                     "func": gcf_108_close_rolling_min_756d},
    "gcf_109_close_pct_from_252d_min":             {"inputs": ["close"],                                     "func": gcf_109_close_pct_from_252d_min},
    "gcf_110_close_pct_from_504d_min":             {"inputs": ["close"],                                     "func": gcf_110_close_pct_from_504d_min},
    "gcf_111_close_pct_from_756d_min":             {"inputs": ["close"],                                     "func": gcf_111_close_pct_from_756d_min},
    "gcf_112_gc_flag_times_price_dd_252d":         {"inputs": ["going_concern", "close"],                    "func": gcf_112_gc_flag_times_price_dd_252d},
    "gcf_113_aw_flag_times_price_dd_252d":         {"inputs": ["audit_warning", "close"],                    "func": gcf_113_aw_flag_times_price_dd_252d},
    "gcf_114_both_flags_times_price_dd_252d":      {"inputs": ["going_concern", "audit_warning", "close"],   "func": gcf_114_both_flags_times_price_dd_252d},
    "gcf_115_gc_flag_times_price_dd_expanding":    {"inputs": ["going_concern", "close"],                    "func": gcf_115_gc_flag_times_price_dd_expanding},
    "gcf_116_aw_flag_times_price_dd_expanding":    {"inputs": ["audit_warning", "close"],                    "func": gcf_116_aw_flag_times_price_dd_expanding},
    "gcf_117_gc_days_while_price_below_252d_ma":   {"inputs": ["going_concern", "close"],                    "func": gcf_117_gc_days_while_price_below_252d_ma},
    "gcf_118_aw_days_while_price_below_252d_ma":   {"inputs": ["audit_warning", "close"],                    "func": gcf_118_aw_days_while_price_below_252d_ma},
    "gcf_119_gc_weighted_log_price_252d":          {"inputs": ["going_concern", "close"],                    "func": gcf_119_gc_weighted_log_price_252d},
    "gcf_120_close_pct_rank_5y":                   {"inputs": ["close"],                                     "func": gcf_120_close_pct_rank_5y},
    "gcf_121_gc_rolling_sum_1260d":                {"inputs": ["going_concern"],                             "func": gcf_121_gc_rolling_sum_1260d},
    "gcf_122_aw_rolling_sum_1260d":                {"inputs": ["audit_warning"],                             "func": gcf_122_aw_rolling_sum_1260d},
    "gcf_123_gc_fraction_1260d":                   {"inputs": ["going_concern"],                             "func": gcf_123_gc_fraction_1260d},
    "gcf_124_aw_fraction_1260d":                   {"inputs": ["audit_warning"],                             "func": gcf_124_aw_fraction_1260d},
    "gcf_125_gc_to_aw_fraction_ratio_252d":        {"inputs": ["going_concern", "audit_warning"],            "func": gcf_125_gc_to_aw_fraction_ratio_252d},
    "gcf_126_gc_fraction_change_63d_vs_252d":      {"inputs": ["going_concern"],                             "func": gcf_126_gc_fraction_change_63d_vs_252d},
    "gcf_127_aw_fraction_change_63d_vs_252d":      {"inputs": ["audit_warning"],                             "func": gcf_127_aw_fraction_change_63d_vs_252d},
    "gcf_128_gc_fraction_252d_minus_504d":         {"inputs": ["going_concern"],                             "func": gcf_128_gc_fraction_252d_minus_504d},
    "gcf_129_aw_fraction_252d_minus_504d":         {"inputs": ["audit_warning"],                             "func": gcf_129_aw_fraction_252d_minus_504d},
    "gcf_130_gc_ewm_21_minus_ewm_252":             {"inputs": ["going_concern"],                             "func": gcf_130_gc_ewm_21_minus_ewm_252},
    "gcf_131_aw_ewm_21_minus_ewm_252":             {"inputs": ["audit_warning"],                             "func": gcf_131_aw_ewm_21_minus_ewm_252},
    "gcf_132_either_episodes_252d":                {"inputs": ["going_concern", "audit_warning"],            "func": gcf_132_either_episodes_252d},
    "gcf_133_either_episodes_504d":                {"inputs": ["going_concern", "audit_warning"],            "func": gcf_133_either_episodes_504d},
    "gcf_134_combined_flagged_day_count_expanding":{"inputs": ["going_concern", "audit_warning"],            "func": gcf_134_combined_flagged_day_count_expanding},
    "gcf_135_flag_sum_rolling_mean_63d":           {"inputs": ["going_concern", "audit_warning"],            "func": gcf_135_flag_sum_rolling_mean_63d},
    "gcf_136_log_return_1d":                       {"inputs": ["close"],                                     "func": gcf_136_log_return_1d},
    "gcf_137_gc_flagged_log_ret_sum_63d":          {"inputs": ["going_concern", "close"],                    "func": gcf_137_gc_flagged_log_ret_sum_63d},
    "gcf_138_aw_flagged_log_ret_sum_63d":          {"inputs": ["audit_warning", "close"],                    "func": gcf_138_aw_flagged_log_ret_sum_63d},
    "gcf_139_gc_flagged_log_ret_sum_252d":         {"inputs": ["going_concern", "close"],                    "func": gcf_139_gc_flagged_log_ret_sum_252d},
    "gcf_140_aw_flagged_log_ret_sum_252d":         {"inputs": ["audit_warning", "close"],                    "func": gcf_140_aw_flagged_log_ret_sum_252d},
    "gcf_141_close_log_return_63d":                {"inputs": ["close"],                                     "func": gcf_141_close_log_return_63d},
    "gcf_142_close_log_return_252d":               {"inputs": ["close"],                                     "func": gcf_142_close_log_return_252d},
    "gcf_143_close_log_return_504d":               {"inputs": ["close"],                                     "func": gcf_143_close_log_return_504d},
    "gcf_144_gc_flag_times_log_ret_252d":          {"inputs": ["going_concern", "close"],                    "func": gcf_144_gc_flag_times_log_ret_252d},
    "gcf_145_aw_flag_times_log_ret_252d":          {"inputs": ["audit_warning", "close"],                    "func": gcf_145_aw_flag_times_log_ret_252d},
    "gcf_146_close_rolling_std_63d":               {"inputs": ["close"],                                     "func": gcf_146_close_rolling_std_63d},
    "gcf_147_close_rolling_std_252d":              {"inputs": ["close"],                                     "func": gcf_147_close_rolling_std_252d},
    "gcf_148_gc_flag_times_volatility_252d":       {"inputs": ["going_concern", "close"],                    "func": gcf_148_gc_flag_times_volatility_252d},
    "gcf_149_aw_flag_times_volatility_252d":       {"inputs": ["audit_warning", "close"],                    "func": gcf_149_aw_flag_times_volatility_252d},
    "gcf_150_audit_distress_severity_index":       {"inputs": ["going_concern", "audit_warning", "close"],   "func": gcf_150_audit_distress_severity_index},
    "gcf_176_gc_aw_cleared_this_year":             {"inputs": ["going_concern", "audit_warning"],            "func": gcf_176_gc_aw_cleared_this_year},
    "gcf_177_gc_rolling_sum_5d":                   {"inputs": ["going_concern"],                             "func": gcf_177_gc_rolling_sum_5d},
    "gcf_178_aw_rolling_sum_5d":                   {"inputs": ["audit_warning"],                             "func": gcf_178_aw_rolling_sum_5d},
    "gcf_179_gc_fraction_5d":                      {"inputs": ["going_concern"],                             "func": gcf_179_gc_fraction_5d},
    "gcf_180_aw_fraction_5d":                      {"inputs": ["audit_warning"],                             "func": gcf_180_aw_fraction_5d},
    "gcf_181_gc_streak_pct_rank_504d":             {"inputs": ["going_concern"],                             "func": gcf_181_gc_streak_pct_rank_504d},
    "gcf_182_aw_streak_pct_rank_504d":             {"inputs": ["audit_warning"],                             "func": gcf_182_aw_streak_pct_rank_504d},
    "gcf_183_gc_fraction_126d_zscore_504d":        {"inputs": ["going_concern"],                             "func": gcf_183_gc_fraction_126d_zscore_504d},
    "gcf_184_aw_fraction_126d_zscore_504d":        {"inputs": ["audit_warning"],                             "func": gcf_184_aw_fraction_126d_zscore_504d},
    "gcf_185_close_pct_from_1260d_min":            {"inputs": ["close"],                                     "func": gcf_185_close_pct_from_1260d_min},
    "gcf_186_close_rolling_max_252d":              {"inputs": ["close"],                                     "func": gcf_186_close_rolling_max_252d},
    "gcf_187_close_rolling_max_504d":              {"inputs": ["close"],                                     "func": gcf_187_close_rolling_max_504d},
    "gcf_188_gc_flag_times_price_dd_504d":         {"inputs": ["going_concern", "close"],                    "func": gcf_188_gc_flag_times_price_dd_504d},
    "gcf_189_aw_flag_times_price_dd_504d":         {"inputs": ["audit_warning", "close"],                    "func": gcf_189_aw_flag_times_price_dd_504d},
    "gcf_190_gc_vol_during_flag_252d":             {"inputs": ["going_concern", "close"],                    "func": gcf_190_gc_vol_during_flag_252d},
    "gcf_191_aw_vol_during_flag_252d":             {"inputs": ["audit_warning", "close"],                    "func": gcf_191_aw_vol_during_flag_252d},
    "gcf_192_gc_days_below_63d_ma":                {"inputs": ["going_concern", "close"],                    "func": gcf_192_gc_days_below_63d_ma},
    "gcf_193_aw_days_below_63d_ma":                {"inputs": ["audit_warning", "close"],                    "func": gcf_193_aw_days_below_63d_ma},
    "gcf_194_close_vol_ratio_63d_vs_252d":         {"inputs": ["close"],                                     "func": gcf_194_close_vol_ratio_63d_vs_252d},
    "gcf_195_gc_flagged_neg_ret_count_252d":       {"inputs": ["going_concern", "close"],                    "func": gcf_195_gc_flagged_neg_ret_count_252d},
    "gcf_196_aw_flagged_neg_ret_count_252d":       {"inputs": ["audit_warning", "close"],                    "func": gcf_196_aw_flagged_neg_ret_count_252d},
    "gcf_197_gc_expanding_episode_rate":           {"inputs": ["going_concern"],                             "func": gcf_197_gc_expanding_episode_rate},
    "gcf_198_aw_expanding_episode_rate":           {"inputs": ["audit_warning"],                             "func": gcf_198_aw_expanding_episode_rate},
    "gcf_199_gc_aw_flag_product_ewm_63":           {"inputs": ["going_concern", "audit_warning"],            "func": gcf_199_gc_aw_flag_product_ewm_63},
    "gcf_200_triple_distress_composite_504d":      {"inputs": ["going_concern", "audit_warning", "close"],   "func": gcf_200_triple_distress_composite_504d},
}
