"""
29_consecutive_loss — Base Features 001-075
Domain: magnitude/severity of cumulative loss within losing runs — cumulative streak
    loss, worst-run loss, loss-per-run ratios, drawdown from runs, loss distribution.
    Does NOT count streak lengths (that is folder 08); measures LOSS DOLLAR/RETURN
    magnitude accumulated inside those runs.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_log_ret(close: pd.Series) -> pd.Series:
    return _log_safe(close) - _log_safe(close.shift(1))


def _is_loss_day(close: pd.Series) -> pd.Series:
    """Boolean Series: True on days where close < prior close."""
    return close < close.shift(1)


def _run_group(cond: pd.Series) -> pd.Series:
    """Group-id that increments each time cond flips to False (use for cumsum within run)."""
    return (~cond).cumsum()


def _cum_log_loss_in_run(close: pd.Series) -> pd.Series:
    """Cumulative log-return accumulated within each current losing run (negative on loss days, 0 otherwise)."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = lr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _run_loss_series(close: pd.Series) -> pd.Series:
    """At each bar, the total log-return of the most-recently COMPLETED run,
    available on the first non-run day (the day after the run ends).
    Uses only backward-looking shifts."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    # cumulative sum within each run
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    # a run is confirmed ended on the first day where today is NOT a loss but yesterday WAS
    run_ended = (~cond) & cond.shift(1).fillna(False)
    # peak cumulative loss of the completed run, known the day after it ends
    run_cum_final = run_cum.shift(1).where(run_ended)
    # carry the most-recent completed-run total forward; zero before any run completes
    return run_cum_final.ffill().fillna(0.0)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Cumulative log-return in the current losing run ---

def ccl_001_cum_loss_current_run(close: pd.Series) -> pd.Series:
    """Cumulative log-return inside the current losing run (0 on up days)."""
    return _cum_log_loss_in_run(close)


def ccl_002_cum_loss_current_run_abs(close: pd.Series) -> pd.Series:
    """Absolute cumulative log-loss in the current run."""
    return _cum_log_loss_in_run(close).abs()


def ccl_003_cum_loss_current_run_pct(close: pd.Series) -> pd.Series:
    """Cumulative simple-return (pct) inside the current losing run."""
    pr = close.pct_change(1)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = pr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def ccl_004_cum_loss_current_run_norm_21d(close: pd.Series) -> pd.Series:
    """Current-run cumulative loss normalized by 21-day average absolute run loss."""
    cum = _cum_log_loss_in_run(close)
    avg = _rolling_mean(cum.abs(), _TD_MON)
    return _safe_div(cum, avg)


def ccl_005_cum_loss_current_run_norm_63d(close: pd.Series) -> pd.Series:
    """Current-run cumulative loss normalized by 63-day average absolute run loss."""
    cum = _cum_log_loss_in_run(close)
    avg = _rolling_mean(cum.abs(), _TD_QTR)
    return _safe_div(cum, avg)


def ccl_006_cum_loss_current_run_norm_252d(close: pd.Series) -> pd.Series:
    """Current-run cumulative loss normalized by 252-day average absolute run loss."""
    cum = _cum_log_loss_in_run(close)
    avg = _rolling_mean(cum.abs(), _TD_YEAR)
    return _safe_div(cum, avg)


def ccl_007_cum_loss_current_run_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current-run cumulative loss within trailing 252-day values."""
    cum = _cum_log_loss_in_run(close)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_008_cum_loss_current_run_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    return cum.expanding(min_periods=5).rank(pct=True)


def ccl_009_cum_loss_current_run_log1p(close: pd.Series) -> pd.Series:
    """Log1p of absolute current-run cumulative loss (compresses long tail)."""
    return np.log1p(_cum_log_loss_in_run(close).abs())


def ccl_010_cum_loss_current_run_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current-run cumulative loss vs trailing 252-day distribution."""
    cum = _cum_log_loss_in_run(close)
    m = _rolling_mean(cum, _TD_YEAR)
    s = _rolling_std(cum, _TD_YEAR)
    return _safe_div(cum - m, s)


def ccl_011_cum_loss_gt_5pct_flag(close: pd.Series) -> pd.Series:
    """Flag: current-run cumulative log-loss exceeds 5% (abs >= 0.05)."""
    return (_cum_log_loss_in_run(close).abs() >= 0.05).astype(float)


def ccl_012_cum_loss_gt_10pct_flag(close: pd.Series) -> pd.Series:
    """Flag: current-run cumulative log-loss exceeds 10% (abs >= 0.10)."""
    return (_cum_log_loss_in_run(close).abs() >= 0.10).astype(float)


# --- Group B (013-024): Worst (largest) cumulative run loss in trailing windows ---

def ccl_013_worst_run_loss_21d(close: pd.Series) -> pd.Series:
    """Minimum (most negative) cumulative run-loss seen in trailing 21 days."""
    cum = _cum_log_loss_in_run(close)
    return _rolling_min(cum, _TD_MON)


def ccl_014_worst_run_loss_63d(close: pd.Series) -> pd.Series:
    """Minimum cumulative run-loss in trailing 63 days."""
    cum = _cum_log_loss_in_run(close)
    return _rolling_min(cum, _TD_QTR)


def ccl_015_worst_run_loss_126d(close: pd.Series) -> pd.Series:
    """Minimum cumulative run-loss in trailing 126 days."""
    cum = _cum_log_loss_in_run(close)
    return _rolling_min(cum, _TD_HALF)


def ccl_016_worst_run_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum cumulative run-loss in trailing 252 days."""
    cum = _cum_log_loss_in_run(close)
    return _rolling_min(cum, _TD_YEAR)


def ccl_017_worst_run_loss_504d(close: pd.Series) -> pd.Series:
    """Minimum cumulative run-loss in trailing 504 days."""
    cum = _cum_log_loss_in_run(close)
    return _rolling_min(cum, 504)


def ccl_018_worst_run_loss_expanding(close: pd.Series) -> pd.Series:
    """All-time (expanding) minimum cumulative run-loss."""
    cum = _cum_log_loss_in_run(close)
    return cum.expanding(min_periods=1).min()


def ccl_019_current_vs_worst_run_loss_63d(close: pd.Series) -> pd.Series:
    """Current run loss as fraction of 63-day worst run loss."""
    cur  = _cum_log_loss_in_run(close)
    worst = _rolling_min(cur, _TD_QTR)
    return _safe_div(cur, worst.abs())


def ccl_020_current_vs_worst_run_loss_252d(close: pd.Series) -> pd.Series:
    """Current run loss as fraction of 252-day worst run loss."""
    cur   = _cum_log_loss_in_run(close)
    worst = _rolling_min(cur, _TD_YEAR)
    return _safe_div(cur, worst.abs())


def ccl_021_worst_run_loss_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day worst run loss to 252-day worst run loss (recent severity)."""
    cum = _cum_log_loss_in_run(close)
    w21  = _rolling_min(cum, _TD_MON)
    w252 = _rolling_min(cum, _TD_YEAR)
    return _safe_div(w21.abs(), w252.abs())


def ccl_022_worst_run_loss_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day worst run loss to 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w63  = _rolling_min(cum, _TD_QTR)
    w252 = _rolling_min(cum, _TD_YEAR)
    return _safe_div(w63.abs(), w252.abs())


def ccl_023_worst_run_loss_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w252 = _rolling_min(cum, _TD_YEAR)
    return w252.expanding(min_periods=5).rank(pct=True)


def ccl_024_worst_run_loss_252d_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w252 = _rolling_min(cum, _TD_YEAR)
    m = w252.expanding(min_periods=5).mean()
    s = w252.expanding(min_periods=5).std()
    return _safe_div(w252 - m, s)


# --- Group C (025-036): Sum of all negative returns in trailing windows ---

def ccl_025_neg_ret_sum_5d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 5 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK)


def ccl_026_neg_ret_sum_21d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 21 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)


def ccl_027_neg_ret_sum_63d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 63 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)


def ccl_028_neg_ret_sum_126d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 126 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_HALF)


def ccl_029_neg_ret_sum_252d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 252 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR)


def ccl_030_neg_ret_sum_21d_norm_252d(close: pd.Series) -> pd.Series:
    """21-day negative-return sum normalized by 252-day average."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    avg = _rolling_mean(s21.abs(), _TD_YEAR)
    return _safe_div(s21, avg)


def ccl_031_neg_ret_sum_63d_norm_252d(close: pd.Series) -> pd.Series:
    """63-day negative-return sum normalized by 252-day average."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    avg = _rolling_mean(s63.abs(), _TD_YEAR)
    return _safe_div(s63, avg)


def ccl_032_neg_ret_sum_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day negative-return sum within 252-day distribution."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return s21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_033_neg_ret_sum_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day negative-return sum vs 252-day distribution."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    return _safe_div(s21 - m, s)


def ccl_034_neg_vs_pos_ret_sum_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of absolute negative-return sum to positive-return sum over 21 days."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_MON)
    return _safe_div(neg, pos)


def ccl_035_neg_vs_pos_ret_sum_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of absolute negative-return sum to positive-return sum over 63 days."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_QTR)
    return _safe_div(neg, pos)


def ccl_036_neg_vs_pos_ret_sum_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of absolute negative-return sum to positive-return sum over 252 days."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_YEAR)
    return _safe_div(neg, pos)


# --- Group D (037-048): Loss accumulated per losing run and per-run averages ---

def _completed_run_loss_series(close: pd.Series) -> pd.Series:
    """Return a Series with the completed run's total log-loss placed on the
    first non-run day (the day after the run ends) and NaN elsewhere.
    Strictly backward-looking — no negative shifts."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    return run_cum.shift(1).where(run_ended)


def ccl_037_avg_run_loss_21d(close: pd.Series) -> pd.Series:
    """Average cumulative log-loss per losing run (runs completed) over 21 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_MON, min_periods=1).mean()


def ccl_038_avg_run_loss_63d(close: pd.Series) -> pd.Series:
    """Average cumulative log-loss per losing run over 63 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_QTR, min_periods=1).mean()


def ccl_039_avg_run_loss_252d(close: pd.Series) -> pd.Series:
    """Average cumulative log-loss per losing run over 252 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=1).mean()


def ccl_040_worst_single_run_loss_63d(close: pd.Series) -> pd.Series:
    """Minimum (worst) completed run loss seen over trailing 63 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_QTR, min_periods=1).min()


def ccl_041_worst_single_run_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum completed run loss seen over trailing 252 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=1).min()


def ccl_042_worst_single_run_loss_expanding(close: pd.Series) -> pd.Series:
    """All-time worst single completed run loss (expanding minimum)."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.expanding(min_periods=1).min()


def ccl_043_run_loss_count_gt5pct_63d(close: pd.Series) -> pd.Series:
    """Count of completed runs with cumulative loss > 5% (abs) in trailing 63 days."""
    run_loss = _completed_run_loss_series(close)
    big = (run_loss.abs() > 0.05).astype(float).fillna(0.0)
    return _rolling_sum(big, _TD_QTR)


def ccl_044_run_loss_count_gt10pct_63d(close: pd.Series) -> pd.Series:
    """Count of completed runs with cumulative loss > 10% in trailing 63 days."""
    run_loss = _completed_run_loss_series(close)
    big = (run_loss.abs() > 0.10).astype(float).fillna(0.0)
    return _rolling_sum(big, _TD_QTR)


def ccl_045_run_loss_count_gt10pct_252d(close: pd.Series) -> pd.Series:
    """Count of completed runs with cumulative loss > 10% in trailing 252 days."""
    run_loss = _completed_run_loss_series(close)
    big = (run_loss.abs() > 0.10).astype(float).fillna(0.0)
    return _rolling_sum(big, _TD_YEAR)


def ccl_046_run_loss_std_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of completed run losses over trailing 252 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=1).std()


def ccl_047_run_loss_median_252d(close: pd.Series) -> pd.Series:
    """Median completed run loss over trailing 252 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=1).median()


def ccl_048_run_loss_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of completed run losses over trailing 252 days (left tail = bad)."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=5).skew()


# --- Group E (049-060): Loss per unit streak-length ratios ---

def ccl_049_loss_per_day_current_run(close: pd.Series) -> pd.Series:
    """Average daily log-loss per day within the current losing run."""
    cum = _cum_log_loss_in_run(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    length = cond.astype(int).groupby(grp).cumsum().astype(float)
    return _safe_div(cum, length.where(cond, np.nan))


def ccl_050_loss_per_day_current_run_abs(close: pd.Series) -> pd.Series:
    """Absolute average daily log-loss per day in the current run."""
    return ccl_049_loss_per_day_current_run(close).abs()


def ccl_051_loss_per_day_worst_run_63d(close: pd.Series) -> pd.Series:
    """Worst (most negative) loss-per-day ratio across runs in trailing 63 days."""
    return _rolling_min(ccl_049_loss_per_day_current_run(close), _TD_QTR)


def ccl_052_loss_per_day_worst_run_252d(close: pd.Series) -> pd.Series:
    """Worst loss-per-day ratio across runs in trailing 252 days."""
    return _rolling_min(ccl_049_loss_per_day_current_run(close), _TD_YEAR)


def ccl_053_loss_per_day_avg_21d(close: pd.Series) -> pd.Series:
    """Average loss-per-day ratio over 21 days (all days, not just run days)."""
    lr = _daily_log_ret(close)
    return _rolling_mean(lr.where(lr < 0, 0.0), _TD_MON)


def ccl_054_loss_per_day_avg_63d(close: pd.Series) -> pd.Series:
    """Average loss-per-day ratio over 63 days."""
    lr = _daily_log_ret(close)
    return _rolling_mean(lr.where(lr < 0, 0.0), _TD_QTR)


def ccl_055_loss_per_day_avg_252d(close: pd.Series) -> pd.Series:
    """Average loss-per-day ratio over 252 days."""
    lr = _daily_log_ret(close)
    return _rolling_mean(lr.where(lr < 0, 0.0), _TD_YEAR)


def ccl_056_loss_per_day_ewm21(close: pd.Series) -> pd.Series:
    """21-day EWM average of daily loss magnitude on loss days only."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    loss_only = lr.where(cond, np.nan)
    return _ewm_mean(loss_only.fillna(0.0), _TD_MON)


def ccl_057_avg_loss_day_vs_avg_gain_day_21d(close: pd.Series) -> pd.Series:
    """Ratio of avg daily loss magnitude to avg daily gain over 21 days."""
    lr = _daily_log_ret(close)
    avg_loss = lr.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean().abs()
    avg_gain = lr.where(lr > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(avg_loss, avg_gain)


def ccl_058_avg_loss_day_vs_avg_gain_day_63d(close: pd.Series) -> pd.Series:
    """Ratio of avg daily loss magnitude to avg daily gain over 63 days."""
    lr = _daily_log_ret(close)
    avg_loss = lr.where(lr < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean().abs()
    avg_gain = lr.where(lr > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(avg_loss, avg_gain)


def ccl_059_avg_loss_day_vs_avg_gain_day_252d(close: pd.Series) -> pd.Series:
    """Ratio of avg daily loss magnitude to avg daily gain over 252 days."""
    lr = _daily_log_ret(close)
    avg_loss = lr.where(lr < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean().abs()
    avg_gain = lr.where(lr > 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(avg_loss, avg_gain)


def ccl_060_current_run_loss_vs_avg_loss_per_day_252d(close: pd.Series) -> pd.Series:
    """Current run cumulative loss divided by 252-day avg loss-per-day."""
    cum = _cum_log_loss_in_run(close)
    lr = _daily_log_ret(close)
    avg_loss_day = lr.where(lr < 0, 0.0).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(cum, avg_loss_day.abs())


# --- Group F (061-075): Drawdown attributable to loss runs, distribution & vol-weighted ---

def ccl_061_run_loss_drawdown_contribution_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day total return that comes from loss-day moves."""
    lr = _daily_log_ret(close)
    total = _rolling_sum(lr, _TD_MON)
    loss_part = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return _safe_div(loss_part, total.abs())


def ccl_062_run_loss_drawdown_contribution_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day total return that comes from loss-day moves."""
    lr = _daily_log_ret(close)
    total = _rolling_sum(lr, _TD_QTR)
    loss_part = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    return _safe_div(loss_part, total.abs())


def ccl_063_run_loss_drawdown_contribution_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day total return that comes from loss-day moves."""
    lr = _daily_log_ret(close)
    total = _rolling_sum(lr, _TD_YEAR)
    loss_part = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR)
    return _safe_div(loss_part, total.abs())


def ccl_064_run_loss_pct_of_trailing_high_21d(close: pd.Series) -> pd.Series:
    """Current run cumulative loss as pct of 21-day trailing high price."""
    cum_pct = ccl_003_cum_loss_current_run_pct(close)
    high21 = _rolling_max(close, _TD_MON)
    curr_vs_high = _safe_div(close - high21, high21)
    return curr_vs_high.where(_is_loss_day(close), 0.0)


def ccl_065_run_loss_pct_of_trailing_high_63d(close: pd.Series) -> pd.Series:
    """Current run cumulative loss as pct of 63-day trailing high price."""
    high63 = _rolling_max(close, _TD_QTR)
    curr_vs_high = _safe_div(close - high63, high63)
    return curr_vs_high.where(_is_loss_day(close), 0.0)


def ccl_066_neg_ret_sum_vol_weighted_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative returns over 21 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    return _rolling_sum(w_loss, _TD_MON)


def ccl_067_neg_ret_sum_vol_weighted_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative returns over 63 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    return _rolling_sum(w_loss, _TD_QTR)


def ccl_068_neg_ret_sum_vol_weighted_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative returns over 252 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    return _rolling_sum(w_loss, _TD_YEAR)


def ccl_069_current_run_vol_weighted_loss(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted cumulative log-loss in the current losing run."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    w_lr = lr * vol_norm
    cum = w_lr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def ccl_070_current_run_atr_normalized_loss(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR(14)-normalized cumulative loss in the current run."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    norm_lr = _safe_div(lr, atr14)
    cum = norm_lr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def ccl_071_worst_run_loss_atr_normalized_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day worst ATR-normalized run loss."""
    atr_cum = ccl_070_current_run_atr_normalized_loss(close, high, low)
    return _rolling_min(atr_cum, _TD_YEAR)


def ccl_072_run_loss_iqr_252d(close: pd.Series) -> pd.Series:
    """Interquartile range of completed run losses over 252 days (dispersion)."""
    run_loss = _completed_run_loss_series(close)
    q75 = run_loss.rolling(_TD_YEAR, min_periods=5).quantile(0.75)
    q25 = run_loss.rolling(_TD_YEAR, min_periods=5).quantile(0.25)
    return q75 - q25


def ccl_073_run_loss_90th_pct_252d(close: pd.Series) -> pd.Series:
    """90th-percentile (worst tail) of completed run losses over 252 days."""
    run_loss = _completed_run_loss_series(close)
    return run_loss.rolling(_TD_YEAR, min_periods=5).quantile(0.10)


def ccl_074_neg_ret_ewm_sum_21d(close: pd.Series) -> pd.Series:
    """EWM(21-span) of daily negative returns summed over 21 days."""
    lr = _daily_log_ret(close)
    loss_only = lr.where(lr < 0, 0.0)
    return _ewm_mean(loss_only, _TD_MON) * _TD_MON


def ccl_075_cum_loss_current_run_open_adjusted(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current-run loss measured from prior-close to current-open (gap component)."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = gap.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_REGISTRY_001_075 = {
    "ccl_001_cum_loss_current_run": {"inputs": ["close"], "func": ccl_001_cum_loss_current_run},
    "ccl_002_cum_loss_current_run_abs": {"inputs": ["close"], "func": ccl_002_cum_loss_current_run_abs},
    "ccl_003_cum_loss_current_run_pct": {"inputs": ["close"], "func": ccl_003_cum_loss_current_run_pct},
    "ccl_004_cum_loss_current_run_norm_21d": {"inputs": ["close"], "func": ccl_004_cum_loss_current_run_norm_21d},
    "ccl_005_cum_loss_current_run_norm_63d": {"inputs": ["close"], "func": ccl_005_cum_loss_current_run_norm_63d},
    "ccl_006_cum_loss_current_run_norm_252d": {"inputs": ["close"], "func": ccl_006_cum_loss_current_run_norm_252d},
    "ccl_007_cum_loss_current_run_pct_rank_252d": {"inputs": ["close"], "func": ccl_007_cum_loss_current_run_pct_rank_252d},
    "ccl_008_cum_loss_current_run_expanding_rank": {"inputs": ["close"], "func": ccl_008_cum_loss_current_run_expanding_rank},
    "ccl_009_cum_loss_current_run_log1p": {"inputs": ["close"], "func": ccl_009_cum_loss_current_run_log1p},
    "ccl_010_cum_loss_current_run_zscore_252d": {"inputs": ["close"], "func": ccl_010_cum_loss_current_run_zscore_252d},
    "ccl_011_cum_loss_gt_5pct_flag": {"inputs": ["close"], "func": ccl_011_cum_loss_gt_5pct_flag},
    "ccl_012_cum_loss_gt_10pct_flag": {"inputs": ["close"], "func": ccl_012_cum_loss_gt_10pct_flag},
    "ccl_013_worst_run_loss_21d": {"inputs": ["close"], "func": ccl_013_worst_run_loss_21d},
    "ccl_014_worst_run_loss_63d": {"inputs": ["close"], "func": ccl_014_worst_run_loss_63d},
    "ccl_015_worst_run_loss_126d": {"inputs": ["close"], "func": ccl_015_worst_run_loss_126d},
    "ccl_016_worst_run_loss_252d": {"inputs": ["close"], "func": ccl_016_worst_run_loss_252d},
    "ccl_017_worst_run_loss_504d": {"inputs": ["close"], "func": ccl_017_worst_run_loss_504d},
    "ccl_018_worst_run_loss_expanding": {"inputs": ["close"], "func": ccl_018_worst_run_loss_expanding},
    "ccl_019_current_vs_worst_run_loss_63d": {"inputs": ["close"], "func": ccl_019_current_vs_worst_run_loss_63d},
    "ccl_020_current_vs_worst_run_loss_252d": {"inputs": ["close"], "func": ccl_020_current_vs_worst_run_loss_252d},
    "ccl_021_worst_run_loss_21d_vs_252d": {"inputs": ["close"], "func": ccl_021_worst_run_loss_21d_vs_252d},
    "ccl_022_worst_run_loss_63d_vs_252d": {"inputs": ["close"], "func": ccl_022_worst_run_loss_63d_vs_252d},
    "ccl_023_worst_run_loss_252d_pct_rank_504d": {"inputs": ["close"], "func": ccl_023_worst_run_loss_252d_pct_rank_504d},
    "ccl_024_worst_run_loss_252d_zscore_expanding": {"inputs": ["close"], "func": ccl_024_worst_run_loss_252d_zscore_expanding},
    "ccl_025_neg_ret_sum_5d": {"inputs": ["close"], "func": ccl_025_neg_ret_sum_5d},
    "ccl_026_neg_ret_sum_21d": {"inputs": ["close"], "func": ccl_026_neg_ret_sum_21d},
    "ccl_027_neg_ret_sum_63d": {"inputs": ["close"], "func": ccl_027_neg_ret_sum_63d},
    "ccl_028_neg_ret_sum_126d": {"inputs": ["close"], "func": ccl_028_neg_ret_sum_126d},
    "ccl_029_neg_ret_sum_252d": {"inputs": ["close"], "func": ccl_029_neg_ret_sum_252d},
    "ccl_030_neg_ret_sum_21d_norm_252d": {"inputs": ["close"], "func": ccl_030_neg_ret_sum_21d_norm_252d},
    "ccl_031_neg_ret_sum_63d_norm_252d": {"inputs": ["close"], "func": ccl_031_neg_ret_sum_63d_norm_252d},
    "ccl_032_neg_ret_sum_21d_pct_rank_252d": {"inputs": ["close"], "func": ccl_032_neg_ret_sum_21d_pct_rank_252d},
    "ccl_033_neg_ret_sum_21d_zscore_252d": {"inputs": ["close"], "func": ccl_033_neg_ret_sum_21d_zscore_252d},
    "ccl_034_neg_vs_pos_ret_sum_ratio_21d": {"inputs": ["close"], "func": ccl_034_neg_vs_pos_ret_sum_ratio_21d},
    "ccl_035_neg_vs_pos_ret_sum_ratio_63d": {"inputs": ["close"], "func": ccl_035_neg_vs_pos_ret_sum_ratio_63d},
    "ccl_036_neg_vs_pos_ret_sum_ratio_252d": {"inputs": ["close"], "func": ccl_036_neg_vs_pos_ret_sum_ratio_252d},
    "ccl_037_avg_run_loss_21d": {"inputs": ["close"], "func": ccl_037_avg_run_loss_21d},
    "ccl_038_avg_run_loss_63d": {"inputs": ["close"], "func": ccl_038_avg_run_loss_63d},
    "ccl_039_avg_run_loss_252d": {"inputs": ["close"], "func": ccl_039_avg_run_loss_252d},
    "ccl_040_worst_single_run_loss_63d": {"inputs": ["close"], "func": ccl_040_worst_single_run_loss_63d},
    "ccl_041_worst_single_run_loss_252d": {"inputs": ["close"], "func": ccl_041_worst_single_run_loss_252d},
    "ccl_042_worst_single_run_loss_expanding": {"inputs": ["close"], "func": ccl_042_worst_single_run_loss_expanding},
    "ccl_043_run_loss_count_gt5pct_63d": {"inputs": ["close"], "func": ccl_043_run_loss_count_gt5pct_63d},
    "ccl_044_run_loss_count_gt10pct_63d": {"inputs": ["close"], "func": ccl_044_run_loss_count_gt10pct_63d},
    "ccl_045_run_loss_count_gt10pct_252d": {"inputs": ["close"], "func": ccl_045_run_loss_count_gt10pct_252d},
    "ccl_046_run_loss_std_252d": {"inputs": ["close"], "func": ccl_046_run_loss_std_252d},
    "ccl_047_run_loss_median_252d": {"inputs": ["close"], "func": ccl_047_run_loss_median_252d},
    "ccl_048_run_loss_skew_252d": {"inputs": ["close"], "func": ccl_048_run_loss_skew_252d},
    "ccl_049_loss_per_day_current_run": {"inputs": ["close"], "func": ccl_049_loss_per_day_current_run},
    "ccl_050_loss_per_day_current_run_abs": {"inputs": ["close"], "func": ccl_050_loss_per_day_current_run_abs},
    "ccl_051_loss_per_day_worst_run_63d": {"inputs": ["close"], "func": ccl_051_loss_per_day_worst_run_63d},
    "ccl_052_loss_per_day_worst_run_252d": {"inputs": ["close"], "func": ccl_052_loss_per_day_worst_run_252d},
    "ccl_053_loss_per_day_avg_21d": {"inputs": ["close"], "func": ccl_053_loss_per_day_avg_21d},
    "ccl_054_loss_per_day_avg_63d": {"inputs": ["close"], "func": ccl_054_loss_per_day_avg_63d},
    "ccl_055_loss_per_day_avg_252d": {"inputs": ["close"], "func": ccl_055_loss_per_day_avg_252d},
    "ccl_056_loss_per_day_ewm21": {"inputs": ["close"], "func": ccl_056_loss_per_day_ewm21},
    "ccl_057_avg_loss_day_vs_avg_gain_day_21d": {"inputs": ["close"], "func": ccl_057_avg_loss_day_vs_avg_gain_day_21d},
    "ccl_058_avg_loss_day_vs_avg_gain_day_63d": {"inputs": ["close"], "func": ccl_058_avg_loss_day_vs_avg_gain_day_63d},
    "ccl_059_avg_loss_day_vs_avg_gain_day_252d": {"inputs": ["close"], "func": ccl_059_avg_loss_day_vs_avg_gain_day_252d},
    "ccl_060_current_run_loss_vs_avg_loss_per_day_252d": {"inputs": ["close"], "func": ccl_060_current_run_loss_vs_avg_loss_per_day_252d},
    "ccl_061_run_loss_drawdown_contribution_21d": {"inputs": ["close"], "func": ccl_061_run_loss_drawdown_contribution_21d},
    "ccl_062_run_loss_drawdown_contribution_63d": {"inputs": ["close"], "func": ccl_062_run_loss_drawdown_contribution_63d},
    "ccl_063_run_loss_drawdown_contribution_252d": {"inputs": ["close"], "func": ccl_063_run_loss_drawdown_contribution_252d},
    "ccl_064_run_loss_pct_of_trailing_high_21d": {"inputs": ["close"], "func": ccl_064_run_loss_pct_of_trailing_high_21d},
    "ccl_065_run_loss_pct_of_trailing_high_63d": {"inputs": ["close"], "func": ccl_065_run_loss_pct_of_trailing_high_63d},
    "ccl_066_neg_ret_sum_vol_weighted_21d": {"inputs": ["close", "volume"], "func": ccl_066_neg_ret_sum_vol_weighted_21d},
    "ccl_067_neg_ret_sum_vol_weighted_63d": {"inputs": ["close", "volume"], "func": ccl_067_neg_ret_sum_vol_weighted_63d},
    "ccl_068_neg_ret_sum_vol_weighted_252d": {"inputs": ["close", "volume"], "func": ccl_068_neg_ret_sum_vol_weighted_252d},
    "ccl_069_current_run_vol_weighted_loss": {"inputs": ["close", "volume"], "func": ccl_069_current_run_vol_weighted_loss},
    "ccl_070_current_run_atr_normalized_loss": {"inputs": ["close", "high", "low"], "func": ccl_070_current_run_atr_normalized_loss},
    "ccl_071_worst_run_loss_atr_normalized_252d": {"inputs": ["close", "high", "low"], "func": ccl_071_worst_run_loss_atr_normalized_252d},
    "ccl_072_run_loss_iqr_252d": {"inputs": ["close"], "func": ccl_072_run_loss_iqr_252d},
    "ccl_073_run_loss_90th_pct_252d": {"inputs": ["close"], "func": ccl_073_run_loss_90th_pct_252d},
    "ccl_074_neg_ret_ewm_sum_21d": {"inputs": ["close"], "func": ccl_074_neg_ret_ewm_sum_21d},
    "ccl_075_cum_loss_current_run_open_adjusted": {"inputs": ["close", "open"], "func": ccl_075_cum_loss_current_run_open_adjusted},
}
