"""
29_consecutive_loss — Extended Features 001-075
Domain: consecutive-loss magnitude — new angles not covered by base 001-150:
    streak distribution moments, magnitude-weighted streaks, EWM-weighted run
    losses, cross-window ratios, high-low-open decompositions, regime flags,
    adaptive thresholds, overnight vs intraday breakdown, volume-on-loss-day
    concentration, and capitulation composite scores.
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
    """Group-id that increments each time cond flips to False."""
    return (~cond).cumsum()


def _cum_log_loss_in_run(close: pd.Series) -> pd.Series:
    """Cumulative log-return within current losing run (0 on non-loss days)."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = lr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def _completed_run_loss(close: pd.Series) -> pd.Series:
    """Total log-return of a completed run placed on the first non-run day; NaN elsewhere."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    return run_cum.shift(1).where(run_ended)


def _completed_run_len(close: pd.Series) -> pd.Series:
    """Length (days) of each completed run placed on the first non-run day; NaN elsewhere."""
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    length = cond.astype(int).groupby(grp).cumsum()
    run_ended = (~cond) & cond.shift(1).fillna(False)
    return length.shift(1).where(run_ended)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Streak-length distribution features ---

def ccl_ext_001_completed_run_len_avg_63d(close: pd.Series) -> pd.Series:
    """Average completed-run length (days) over trailing 63 days."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_QTR, min_periods=1).mean()


def ccl_ext_002_completed_run_len_avg_252d(close: pd.Series) -> pd.Series:
    """Average completed-run length over trailing 252 days."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_YEAR, min_periods=1).mean()


def ccl_ext_003_completed_run_len_max_63d(close: pd.Series) -> pd.Series:
    """Maximum completed-run length over trailing 63 days."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_QTR, min_periods=1).max()


def ccl_ext_004_completed_run_len_max_252d(close: pd.Series) -> pd.Series:
    """Maximum completed-run length over trailing 252 days."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_YEAR, min_periods=1).max()


def ccl_ext_005_completed_run_len_std_252d(close: pd.Series) -> pd.Series:
    """Std of completed-run lengths over trailing 252 days (distribution width)."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_YEAR, min_periods=2).std()


def ccl_ext_006_completed_run_len_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of completed-run lengths over 252 days (right-skew = long tail runs)."""
    rl = _completed_run_len(close)
    return rl.rolling(_TD_YEAR, min_periods=5).skew()


def ccl_ext_007_completed_run_len_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of completed-run lengths (extremity vs history)."""
    rl = _completed_run_len(close)
    return rl.expanding(min_periods=5).rank(pct=True)


def ccl_ext_008_current_run_len(close: pd.Series) -> pd.Series:
    """Current consecutive losing-day count (streak length to date)."""
    return _consec_streak(_is_loss_day(close))


def ccl_ext_009_current_run_len_vs_avg_252d(close: pd.Series) -> pd.Series:
    """Current run length divided by 252-day avg completed-run length."""
    cur = _consec_streak(_is_loss_day(close)).astype(float)
    avg = _completed_run_len(close).rolling(_TD_YEAR, min_periods=1).mean()
    return _safe_div(cur, avg)


def ccl_ext_010_current_run_len_vs_max_252d(close: pd.Series) -> pd.Series:
    """Current run length as fraction of 252-day max completed-run length."""
    cur = _consec_streak(_is_loss_day(close)).astype(float)
    mx = _completed_run_len(close).rolling(_TD_YEAR, min_periods=1).max()
    return _safe_div(cur, mx)


# --- Group B (011-020): Loss-magnitude-weighted streak features ---

def ccl_ext_011_loss_mag_weighted_streak_21d(close: pd.Series) -> pd.Series:
    """EWM-weighted sum of in-run daily log-losses over 21 days (recent days heavier)."""
    lr = _daily_log_ret(close)
    loss = lr.where(_is_loss_day(close), 0.0)
    return _ewm_mean(loss, _TD_MON) * _TD_MON


def ccl_ext_012_loss_mag_weighted_streak_63d(close: pd.Series) -> pd.Series:
    """EWM-weighted sum of in-run daily log-losses over 63 days."""
    lr = _daily_log_ret(close)
    loss = lr.where(_is_loss_day(close), 0.0)
    return _ewm_mean(loss, _TD_QTR) * _TD_QTR


def ccl_ext_013_cum_loss_run_times_run_len(close: pd.Series) -> pd.Series:
    """Product of current-run cumulative loss magnitude and run length (severity * duration)."""
    cum = _cum_log_loss_in_run(close).abs()
    rlen = _consec_streak(_is_loss_day(close)).astype(float)
    return cum * rlen


def ccl_ext_014_loss_per_day_ewm63(close: pd.Series) -> pd.Series:
    """63-span EWM of daily loss magnitude on loss days (heavier recent weighting)."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    loss_only = lr.where(cond, 0.0)
    return _ewm_mean(loss_only, _TD_QTR)


def ccl_ext_015_avg_loss_per_run_day_weighted_252d(close: pd.Series) -> pd.Series:
    """252-day avg of (run_loss / run_len) weighting each run by its length."""
    rl = _completed_run_len(close)
    rls = _completed_run_loss(close)
    loss_per_day = _safe_div(rls.abs(), rl)
    return loss_per_day.rolling(_TD_YEAR, min_periods=1).mean()


def ccl_ext_016_cum_loss_run_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of current-run cumulative loss within 126-day distribution."""
    cum = _cum_log_loss_in_run(close)
    return cum.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)


def ccl_ext_017_cum_loss_run_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of current-run cumulative loss vs trailing 63-day distribution."""
    cum = _cum_log_loss_in_run(close)
    m = _rolling_mean(cum, _TD_QTR)
    s = _rolling_std(cum, _TD_QTR)
    return _safe_div(cum - m, s)


def ccl_ext_018_loss_concentration_top3_runs_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day total neg-return sum concentrated in 3 worst runs."""
    lr = _daily_log_ret(close)
    total_neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR).abs()
    rl = _completed_run_loss(close).abs().fillna(0.0)
    top3 = rl.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: np.sort(x[x > 0])[-3:].sum() if (x > 0).sum() >= 3 else np.nan,
        raw=True
    )
    return _safe_div(top3, total_neg)


def ccl_ext_019_loss_gt15pct_run_count_252d(close: pd.Series) -> pd.Series:
    """Count of completed runs with cumulative loss > 15% in trailing 252 days."""
    rl = _completed_run_loss(close)
    big = (rl.abs() > 0.15).astype(float).fillna(0.0)
    return _rolling_sum(big, _TD_YEAR)


def ccl_ext_020_loss_run_avg_ewm_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of most recent completed-run loss to 252-day EWM of run losses."""
    rl = _completed_run_loss(close)
    ewm = _ewm_mean(rl.fillna(0.0), _TD_YEAR)
    return _safe_div(rl, ewm.abs())


# --- Group C (021-030): Overnight gap vs intraday session decomposition ---

def ccl_ext_021_overnight_gap_loss_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of gap-down returns (open < prior close) over trailing 63 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum(gap.where(gap < 0, 0.0), _TD_QTR)


def ccl_ext_022_overnight_gap_loss_sum_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of gap-down returns over trailing 252 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum(gap.where(gap < 0, 0.0), _TD_YEAR)


def ccl_ext_023_intraday_session_loss_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of (open - close) / open on loss days over 63 days (intraday session losses)."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    return _rolling_sum(o2c.where(ret < 0, 0.0), _TD_QTR)


def ccl_ext_024_intraday_session_loss_sum_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of (open - close) / open on loss days over 252 days."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    return _rolling_sum(o2c.where(ret < 0, 0.0), _TD_YEAR)


def ccl_ext_025_gap_vs_session_loss_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of gap-down sum to intraday-session loss sum over 21 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    gap_sum = _rolling_sum(gap.where(gap < 0, 0.0), _TD_MON).abs()
    sess_sum = _rolling_sum(o2c.where(ret < 0, 0.0), _TD_MON).abs()
    return _safe_div(gap_sum, sess_sum)


def ccl_ext_026_gap_vs_session_loss_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of gap-down sum to intraday-session loss sum over 63 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    gap_sum = _rolling_sum(gap.where(gap < 0, 0.0), _TD_QTR).abs()
    sess_sum = _rolling_sum(o2c.where(ret < 0, 0.0), _TD_QTR).abs()
    return _safe_div(gap_sum, sess_sum)


def ccl_ext_027_gap_down_run_cum_loss(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative gap-down component within current losing run."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = gap.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def ccl_ext_028_close_low_spread_sum_loss_days_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of (close - low)/close on loss days over 252 days (selling tail in session)."""
    ret = _daily_log_ret(close)
    c2l = _safe_div(close - low, close)
    return _rolling_sum(c2l.where(ret < 0, 0.0), _TD_YEAR)


def ccl_ext_029_high_open_spread_sum_loss_days_63d(close: pd.Series, high: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of (high - open)/open on loss days over 63 days (intraday reversal after gap)."""
    ret = _daily_log_ret(close)
    h2o = _safe_div(high - open, open)
    return _rolling_sum(h2o.where(ret < 0, 0.0), _TD_QTR)


def ccl_ext_030_body_to_range_ratio_loss_days_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Avg (|close-open| / (high-low)) on loss days over 21 days (body fill on down days)."""
    ret = _daily_log_ret(close)
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    return ratio.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


# --- Group D (031-040): Volume-on-loss-day concentration ---

def ccl_ext_031_vol_frac_on_loss_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(loss_vol, total_vol)


def ccl_ext_032_vol_frac_on_loss_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume occurring on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(loss_vol, total_vol)


def ccl_ext_033_vol_frac_on_loss_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day total volume occurring on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_YEAR)
    total_vol = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(loss_vol, total_vol)


def ccl_ext_034_vol_on_loss_days_vs_gain_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on loss days to avg volume on gain days over 21 days."""
    cond = _is_loss_day(close)
    avg_loss_vol = volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    avg_gain_vol = volume.where(~cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(avg_loss_vol, avg_gain_vol)


def ccl_ext_035_vol_on_loss_days_vs_gain_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on loss days to avg volume on gain days over 63 days."""
    cond = _is_loss_day(close)
    avg_loss_vol = volume.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    avg_gain_vol = volume.where(~cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(avg_loss_vol, avg_gain_vol)


def ccl_ext_036_run_vol_weighted_loss_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted completed-run losses over 63 days (loss * avg-vol-ratio)."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    w_lr = lr * vol_norm
    cum = w_lr.groupby(grp).cumsum().where(cond, 0.0)
    return _rolling_min(cum, _TD_QTR)


def ccl_ext_037_vol_surge_loss_day_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of loss days with volume > 1.5x 21-day avg over trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = _is_loss_day(close)
    high_vol = (volume > avg_vol * 1.5)
    flags = (cond & high_vol).astype(float)
    return _rolling_sum(flags, _TD_MON)


def ccl_ext_038_vol_surge_loss_day_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of loss days with volume > 1.5x 21-day avg over trailing 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = _is_loss_day(close)
    high_vol = (volume > avg_vol * 1.5)
    flags = (cond & high_vol).astype(float)
    return _rolling_sum(flags, _TD_QTR)


def ccl_ext_039_vol_surge_loss_neg_ret_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of negative log-returns on high-volume loss days over 63 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = _is_loss_day(close)
    high_vol = (volume > avg_vol * 1.5)
    return _rolling_sum(lr.where(cond & high_vol, 0.0), _TD_QTR)


def ccl_ext_040_vol_adjusted_cum_loss_run_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume-weighted current-run cumulative loss vs 252-day distribution."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = (lr * vol_norm).groupby(grp).cumsum().where(cond, 0.0)
    m = _rolling_mean(cum, _TD_YEAR)
    s = _rolling_std(cum, _TD_YEAR)
    return _safe_div(cum - m, s)


# --- Group E (041-050): Adaptive-threshold regime flags ---

def ccl_ext_041_loss_run_regime_flag_252d(close: pd.Series) -> pd.Series:
    """Regime flag: current-run cumulative loss exceeds 252-day median absolute run loss."""
    cum = _cum_log_loss_in_run(close)
    med = _rolling_median(cum.abs(), _TD_YEAR)
    return (cum.abs() > med).astype(float)


def ccl_ext_042_loss_run_severe_regime_flag_252d(close: pd.Series) -> pd.Series:
    """Severe regime flag: current-run loss exceeds 252-day 90th-pct abs run loss."""
    cum = _cum_log_loss_in_run(close)
    q90 = cum.abs().rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (cum.abs() > q90).astype(float)


def ccl_ext_043_neg_ret_sum_21d_above_252d_q90_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day neg-return sum magnitude exceeds 252-day 90th-pct."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    q90 = s21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (s21 > q90).astype(float)


def ccl_ext_044_neg_ret_sum_63d_above_252d_q90_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day neg-return sum magnitude exceeds 252-day 90th-pct."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR).abs()
    q90 = s63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (s63 > q90).astype(float)


def ccl_ext_045_consec_loss_days_above_avg_run_len_flag(close: pd.Series) -> pd.Series:
    """Flag: current streak length exceeds 252-day avg completed-run length."""
    cur = _consec_streak(_is_loss_day(close)).astype(float)
    avg_len = _completed_run_len(close).rolling(_TD_YEAR, min_periods=1).mean()
    return (cur > avg_len).astype(float)


def ccl_ext_046_loss_frac_21d_above_60pct_flag(close: pd.Series) -> pd.Series:
    """Flag: loss-day fraction over 21 days exceeds 60%."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    return (frac > 0.60).astype(float)


def ccl_ext_047_loss_frac_63d_above_55pct_flag(close: pd.Series) -> pd.Series:
    """Flag: loss-day fraction over 63 days exceeds 55%."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    return (frac > 0.55).astype(float)


def ccl_ext_048_consec_loss_day_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of days in a current losing run out of trailing 21 days."""
    cond = _is_loss_day(close)
    return _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON


def ccl_ext_049_consec_loss_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of loss days in trailing 63 days."""
    cond = _is_loss_day(close)
    return _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR


def ccl_ext_050_consec_loss_day_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of loss days in trailing 252 days."""
    cond = _is_loss_day(close)
    return _rolling_sum(cond.astype(float), _TD_YEAR) / _TD_YEAR


# --- Group F (051-060): Cross-window trend and ratio features ---

def ccl_ext_051_neg_ret_sum_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 5-day neg-return sum to 21-day neg-return sum."""
    lr = _daily_log_ret(close)
    s5  = _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK).abs()
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    return _safe_div(s5, s21)


def ccl_ext_052_neg_ret_sum_63d_vs_126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 63-day neg-return sum to 126-day neg-return sum."""
    lr = _daily_log_ret(close)
    s63  = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR).abs()
    s126 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_HALF).abs()
    return _safe_div(s63, s126)


def ccl_ext_053_neg_ret_sum_21d_ewm_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day neg-return sum vs its EWM(63) smoothed value."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    ewm = _ewm_mean(s21, _TD_QTR)
    diff = s21 - ewm
    s = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff, s)


def ccl_ext_054_worst_run_loss_ratio_21d_vs_126d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day worst run loss to 126-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w21  = _rolling_min(cum, _TD_MON).abs()
    w126 = _rolling_min(cum, _TD_HALF).abs()
    return _safe_div(w21, w126)


def ccl_ext_055_worst_run_loss_ratio_126d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 126-day worst run loss to 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w126 = _rolling_min(cum, _TD_HALF).abs()
    w252 = _rolling_min(cum, _TD_YEAR).abs()
    return _safe_div(w126, w252)


def ccl_ext_056_neg_ret_count_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of 21-day loss-day count."""
    cond = _is_loss_day(close)
    cnt21 = _rolling_sum(cond.astype(float), _TD_MON)
    return cnt21.expanding(min_periods=5).rank(pct=True)


def ccl_ext_057_loss_day_count_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day loss-day count vs 252-day distribution."""
    cond = _is_loss_day(close)
    cnt = _rolling_sum(cond.astype(float), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def ccl_ext_058_loss_day_count_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day loss-day count vs 252-day distribution."""
    cond = _is_loss_day(close)
    cnt = _rolling_sum(cond.astype(float), _TD_QTR)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def ccl_ext_059_cum_loss_run_pct_of_52wk_neg_sum(close: pd.Series) -> pd.Series:
    """Current-run cumulative loss as fraction of 252-day total negative-return sum."""
    cum = _cum_log_loss_in_run(close)
    lr = _daily_log_ret(close)
    total_neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR).abs()
    return _safe_div(cum.abs(), total_neg)


def ccl_ext_060_avg_run_loss_vs_avg_gain_run_252d(close: pd.Series) -> pd.Series:
    """Ratio of avg completed-run loss to avg gain (from high to run end) over 252 days."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    run_loss = run_cum.shift(1).where(run_ended)
    avg_loss = run_loss.abs().rolling(_TD_YEAR, min_periods=1).mean()
    pos_ret = lr.where(lr > 0, np.nan)
    avg_gain = pos_ret.rolling(_TD_YEAR, min_periods=1).mean()
    return _safe_div(avg_loss, avg_gain)


# --- Group G (061-075): Composite distress scores and novel variants ---

def ccl_ext_061_capitulation_loss_score(close: pd.Series) -> pd.Series:
    """Capitulation score: sum of z-scores of 21d neg-sum, worst-63d-run, loss-day-frac-21d."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    return (_z(s21) + _z(w63) + _z(frac)) / 3.0


def ccl_ext_062_loss_persistence_score_21d(close: pd.Series) -> pd.Series:
    """Loss persistence: loss-day-frac * abs(21d neg-sum) / 252d avg abs neg-sum."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    avg252 = _rolling_mean(s21, _TD_YEAR)
    return _safe_div(s21, avg252) * frac


def ccl_ext_063_loss_acceleration_score_21d(close: pd.Series) -> pd.Series:
    """Acceleration score: ratio of 5-day neg-sum to 21-day neg-sum (recent surge fraction)."""
    lr = _daily_log_ret(close)
    s5  = _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK).abs()
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    return _safe_div(s5, s21)


def ccl_ext_064_loss_breadth_score_63d(close: pd.Series) -> pd.Series:
    """Breadth score: loss-day-frac * run-frequency over 63 days (breadth of losing)."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    freq = _rolling_sum(is_start, _TD_QTR)
    return frac * freq


def ccl_ext_065_var_1pct_daily_loss_252d(close: pd.Series) -> pd.Series:
    """1% VaR of daily log-returns over trailing 252 days (annual tail loss)."""
    lr = _daily_log_ret(close)
    return lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.01)


def ccl_ext_066_var_1pct_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day 1%-VaR within 252-day distribution."""
    lr = _daily_log_ret(close)
    var1 = lr.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.01)
    return var1.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_ext_067_cvar_1pct_daily_loss_63d(close: pd.Series) -> pd.Series:
    """CVaR at 1% (avg of bottom-1% log-returns) over 63 days."""
    lr = _daily_log_ret(close)
    q1 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.01)
    tail = lr.where(lr <= q1, np.nan)
    return tail.rolling(_TD_QTR, min_periods=1).mean()


def ccl_ext_068_cvar_1pct_daily_loss_252d(close: pd.Series) -> pd.Series:
    """CVaR at 1% (avg of bottom-1% log-returns) over 252 days."""
    lr = _daily_log_ret(close)
    q1 = lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.01)
    tail = lr.where(lr <= q1, np.nan)
    return tail.rolling(_TD_YEAR, min_periods=1).mean()


def ccl_ext_069_loss_run_entropy_252d(close: pd.Series) -> pd.Series:
    """Approximate entropy of run-loss distribution over 252 days (Shannon entropy of quantiles)."""
    rl = _completed_run_loss(close).abs().fillna(0.0)
    def _entropy(x):
        x = x[x > 0]
        if len(x) < 2:
            return np.nan
        total = x.sum()
        if total <= 0:
            return np.nan
        p = x / total
        return -np.sum(p * np.log(p + _EPS))
    return rl.rolling(_TD_YEAR, min_periods=5).apply(_entropy, raw=True)


def ccl_ext_070_neg_ret_sum_21d_vol_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day vol-weighted neg-return sum vs 252-day distribution."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    s21 = _rolling_sum(w_loss, _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    return _safe_div(s21 - m, s)


def ccl_ext_071_high_vol_loss_day_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-rank of count of high-volume (>1.5x avg) loss days over 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = _is_loss_day(close)
    high_vol = (volume > avg_vol * 1.5)
    cnt = _rolling_sum((cond & high_vol).astype(float), _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_ext_072_atr_normalized_neg_ret_sum_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of ATR(14)-normalized negative returns over 252 days."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    norm = _safe_div(lr, atr14)
    return _rolling_sum(norm.where(lr < 0, 0.0), _TD_YEAR)


def ccl_ext_073_worst_atr_normalized_loss_day_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Worst single-day ATR-normalized log-loss over trailing 252 days."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    norm = _safe_div(lr, atr14)
    return _rolling_min(norm, _TD_YEAR)


def ccl_ext_074_cum_loss_run_vol_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-rank of current-run vol-weighted cumulative loss within 252-day distribution."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = (lr * vol_norm).groupby(grp).cumsum().where(cond, 0.0)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_ext_075_distress_composite_4factor(close: pd.Series, volume: pd.Series) -> pd.Series:
    """4-factor distress composite: avg z-score of [21d-neg-sum, 63d-worst-run,
    vol-frac-on-loss-63d, loss-day-frac-21d] — higher = more capitulation."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    cond = _is_loss_day(close)
    loss_vol = _rolling_sum(volume * cond.astype(float), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    vfrac = _safe_div(loss_vol, total_vol)
    lfrac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    return (_z(s21) + _z(w63) + _z(vfrac) + _z(lfrac)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_EXTENDED_REGISTRY_001_075 = {
    "ccl_ext_001_completed_run_len_avg_63d": {"inputs": ["close"], "func": ccl_ext_001_completed_run_len_avg_63d},
    "ccl_ext_002_completed_run_len_avg_252d": {"inputs": ["close"], "func": ccl_ext_002_completed_run_len_avg_252d},
    "ccl_ext_003_completed_run_len_max_63d": {"inputs": ["close"], "func": ccl_ext_003_completed_run_len_max_63d},
    "ccl_ext_004_completed_run_len_max_252d": {"inputs": ["close"], "func": ccl_ext_004_completed_run_len_max_252d},
    "ccl_ext_005_completed_run_len_std_252d": {"inputs": ["close"], "func": ccl_ext_005_completed_run_len_std_252d},
    "ccl_ext_006_completed_run_len_skew_252d": {"inputs": ["close"], "func": ccl_ext_006_completed_run_len_skew_252d},
    "ccl_ext_007_completed_run_len_pct_rank_252d": {"inputs": ["close"], "func": ccl_ext_007_completed_run_len_pct_rank_252d},
    "ccl_ext_008_current_run_len": {"inputs": ["close"], "func": ccl_ext_008_current_run_len},
    "ccl_ext_009_current_run_len_vs_avg_252d": {"inputs": ["close"], "func": ccl_ext_009_current_run_len_vs_avg_252d},
    "ccl_ext_010_current_run_len_vs_max_252d": {"inputs": ["close"], "func": ccl_ext_010_current_run_len_vs_max_252d},
    "ccl_ext_011_loss_mag_weighted_streak_21d": {"inputs": ["close"], "func": ccl_ext_011_loss_mag_weighted_streak_21d},
    "ccl_ext_012_loss_mag_weighted_streak_63d": {"inputs": ["close"], "func": ccl_ext_012_loss_mag_weighted_streak_63d},
    "ccl_ext_013_cum_loss_run_times_run_len": {"inputs": ["close"], "func": ccl_ext_013_cum_loss_run_times_run_len},
    "ccl_ext_014_loss_per_day_ewm63": {"inputs": ["close"], "func": ccl_ext_014_loss_per_day_ewm63},
    "ccl_ext_015_avg_loss_per_run_day_weighted_252d": {"inputs": ["close"], "func": ccl_ext_015_avg_loss_per_run_day_weighted_252d},
    "ccl_ext_016_cum_loss_run_pct_rank_126d": {"inputs": ["close"], "func": ccl_ext_016_cum_loss_run_pct_rank_126d},
    "ccl_ext_017_cum_loss_run_zscore_63d": {"inputs": ["close"], "func": ccl_ext_017_cum_loss_run_zscore_63d},
    "ccl_ext_018_loss_concentration_top3_runs_252d": {"inputs": ["close"], "func": ccl_ext_018_loss_concentration_top3_runs_252d},
    "ccl_ext_019_loss_gt15pct_run_count_252d": {"inputs": ["close"], "func": ccl_ext_019_loss_gt15pct_run_count_252d},
    "ccl_ext_020_loss_run_avg_ewm_ratio_252d": {"inputs": ["close"], "func": ccl_ext_020_loss_run_avg_ewm_ratio_252d},
    "ccl_ext_021_overnight_gap_loss_sum_63d": {"inputs": ["close", "open"], "func": ccl_ext_021_overnight_gap_loss_sum_63d},
    "ccl_ext_022_overnight_gap_loss_sum_252d": {"inputs": ["close", "open"], "func": ccl_ext_022_overnight_gap_loss_sum_252d},
    "ccl_ext_023_intraday_session_loss_sum_63d": {"inputs": ["close", "open"], "func": ccl_ext_023_intraday_session_loss_sum_63d},
    "ccl_ext_024_intraday_session_loss_sum_252d": {"inputs": ["close", "open"], "func": ccl_ext_024_intraday_session_loss_sum_252d},
    "ccl_ext_025_gap_vs_session_loss_ratio_21d": {"inputs": ["close", "open"], "func": ccl_ext_025_gap_vs_session_loss_ratio_21d},
    "ccl_ext_026_gap_vs_session_loss_ratio_63d": {"inputs": ["close", "open"], "func": ccl_ext_026_gap_vs_session_loss_ratio_63d},
    "ccl_ext_027_gap_down_run_cum_loss": {"inputs": ["close", "open"], "func": ccl_ext_027_gap_down_run_cum_loss},
    "ccl_ext_028_close_low_spread_sum_loss_days_252d": {"inputs": ["close", "low"], "func": ccl_ext_028_close_low_spread_sum_loss_days_252d},
    "ccl_ext_029_high_open_spread_sum_loss_days_63d": {"inputs": ["close", "high", "open"], "func": ccl_ext_029_high_open_spread_sum_loss_days_63d},
    "ccl_ext_030_body_to_range_ratio_loss_days_21d": {"inputs": ["close", "high", "low", "open"], "func": ccl_ext_030_body_to_range_ratio_loss_days_21d},
    "ccl_ext_031_vol_frac_on_loss_days_21d": {"inputs": ["close", "volume"], "func": ccl_ext_031_vol_frac_on_loss_days_21d},
    "ccl_ext_032_vol_frac_on_loss_days_63d": {"inputs": ["close", "volume"], "func": ccl_ext_032_vol_frac_on_loss_days_63d},
    "ccl_ext_033_vol_frac_on_loss_days_252d": {"inputs": ["close", "volume"], "func": ccl_ext_033_vol_frac_on_loss_days_252d},
    "ccl_ext_034_vol_on_loss_days_vs_gain_days_21d": {"inputs": ["close", "volume"], "func": ccl_ext_034_vol_on_loss_days_vs_gain_days_21d},
    "ccl_ext_035_vol_on_loss_days_vs_gain_days_63d": {"inputs": ["close", "volume"], "func": ccl_ext_035_vol_on_loss_days_vs_gain_days_63d},
    "ccl_ext_036_run_vol_weighted_loss_63d": {"inputs": ["close", "volume"], "func": ccl_ext_036_run_vol_weighted_loss_63d},
    "ccl_ext_037_vol_surge_loss_day_flag_21d": {"inputs": ["close", "volume"], "func": ccl_ext_037_vol_surge_loss_day_flag_21d},
    "ccl_ext_038_vol_surge_loss_day_flag_63d": {"inputs": ["close", "volume"], "func": ccl_ext_038_vol_surge_loss_day_flag_63d},
    "ccl_ext_039_vol_surge_loss_neg_ret_sum_63d": {"inputs": ["close", "volume"], "func": ccl_ext_039_vol_surge_loss_neg_ret_sum_63d},
    "ccl_ext_040_vol_adjusted_cum_loss_run_zscore": {"inputs": ["close", "volume"], "func": ccl_ext_040_vol_adjusted_cum_loss_run_zscore},
    "ccl_ext_041_loss_run_regime_flag_252d": {"inputs": ["close"], "func": ccl_ext_041_loss_run_regime_flag_252d},
    "ccl_ext_042_loss_run_severe_regime_flag_252d": {"inputs": ["close"], "func": ccl_ext_042_loss_run_severe_regime_flag_252d},
    "ccl_ext_043_neg_ret_sum_21d_above_252d_q90_flag": {"inputs": ["close"], "func": ccl_ext_043_neg_ret_sum_21d_above_252d_q90_flag},
    "ccl_ext_044_neg_ret_sum_63d_above_252d_q90_flag": {"inputs": ["close"], "func": ccl_ext_044_neg_ret_sum_63d_above_252d_q90_flag},
    "ccl_ext_045_consec_loss_days_above_avg_run_len_flag": {"inputs": ["close"], "func": ccl_ext_045_consec_loss_days_above_avg_run_len_flag},
    "ccl_ext_046_loss_frac_21d_above_60pct_flag": {"inputs": ["close"], "func": ccl_ext_046_loss_frac_21d_above_60pct_flag},
    "ccl_ext_047_loss_frac_63d_above_55pct_flag": {"inputs": ["close"], "func": ccl_ext_047_loss_frac_63d_above_55pct_flag},
    "ccl_ext_048_consec_loss_day_fraction_21d": {"inputs": ["close"], "func": ccl_ext_048_consec_loss_day_fraction_21d},
    "ccl_ext_049_consec_loss_day_fraction_63d": {"inputs": ["close"], "func": ccl_ext_049_consec_loss_day_fraction_63d},
    "ccl_ext_050_consec_loss_day_fraction_252d": {"inputs": ["close"], "func": ccl_ext_050_consec_loss_day_fraction_252d},
    "ccl_ext_051_neg_ret_sum_5d_vs_21d_ratio": {"inputs": ["close"], "func": ccl_ext_051_neg_ret_sum_5d_vs_21d_ratio},
    "ccl_ext_052_neg_ret_sum_63d_vs_126d_ratio": {"inputs": ["close"], "func": ccl_ext_052_neg_ret_sum_63d_vs_126d_ratio},
    "ccl_ext_053_neg_ret_sum_21d_ewm_zscore": {"inputs": ["close"], "func": ccl_ext_053_neg_ret_sum_21d_ewm_zscore},
    "ccl_ext_054_worst_run_loss_ratio_21d_vs_126d": {"inputs": ["close"], "func": ccl_ext_054_worst_run_loss_ratio_21d_vs_126d},
    "ccl_ext_055_worst_run_loss_ratio_126d_vs_252d": {"inputs": ["close"], "func": ccl_ext_055_worst_run_loss_ratio_126d_vs_252d},
    "ccl_ext_056_neg_ret_count_pct_rank_252d": {"inputs": ["close"], "func": ccl_ext_056_neg_ret_count_pct_rank_252d},
    "ccl_ext_057_loss_day_count_21d_zscore_252d": {"inputs": ["close"], "func": ccl_ext_057_loss_day_count_21d_zscore_252d},
    "ccl_ext_058_loss_day_count_63d_zscore_252d": {"inputs": ["close"], "func": ccl_ext_058_loss_day_count_63d_zscore_252d},
    "ccl_ext_059_cum_loss_run_pct_of_52wk_neg_sum": {"inputs": ["close"], "func": ccl_ext_059_cum_loss_run_pct_of_52wk_neg_sum},
    "ccl_ext_060_avg_run_loss_vs_avg_gain_run_252d": {"inputs": ["close"], "func": ccl_ext_060_avg_run_loss_vs_avg_gain_run_252d},
    "ccl_ext_061_capitulation_loss_score": {"inputs": ["close"], "func": ccl_ext_061_capitulation_loss_score},
    "ccl_ext_062_loss_persistence_score_21d": {"inputs": ["close"], "func": ccl_ext_062_loss_persistence_score_21d},
    "ccl_ext_063_loss_acceleration_score_21d": {"inputs": ["close"], "func": ccl_ext_063_loss_acceleration_score_21d},
    "ccl_ext_064_loss_breadth_score_63d": {"inputs": ["close"], "func": ccl_ext_064_loss_breadth_score_63d},
    "ccl_ext_065_var_1pct_daily_loss_252d": {"inputs": ["close"], "func": ccl_ext_065_var_1pct_daily_loss_252d},
    "ccl_ext_066_var_1pct_21d_pct_rank_252d": {"inputs": ["close"], "func": ccl_ext_066_var_1pct_21d_pct_rank_252d},
    "ccl_ext_067_cvar_1pct_daily_loss_63d": {"inputs": ["close"], "func": ccl_ext_067_cvar_1pct_daily_loss_63d},
    "ccl_ext_068_cvar_1pct_daily_loss_252d": {"inputs": ["close"], "func": ccl_ext_068_cvar_1pct_daily_loss_252d},
    "ccl_ext_069_loss_run_entropy_252d": {"inputs": ["close"], "func": ccl_ext_069_loss_run_entropy_252d},
    "ccl_ext_070_neg_ret_sum_21d_vol_zscore": {"inputs": ["close", "volume"], "func": ccl_ext_070_neg_ret_sum_21d_vol_zscore},
    "ccl_ext_071_high_vol_loss_day_pct_rank": {"inputs": ["close", "volume"], "func": ccl_ext_071_high_vol_loss_day_pct_rank},
    "ccl_ext_072_atr_normalized_neg_ret_sum_252d": {"inputs": ["close", "high", "low"], "func": ccl_ext_072_atr_normalized_neg_ret_sum_252d},
    "ccl_ext_073_worst_atr_normalized_loss_day_252d": {"inputs": ["close", "high", "low"], "func": ccl_ext_073_worst_atr_normalized_loss_day_252d},
    "ccl_ext_074_cum_loss_run_vol_pct_rank": {"inputs": ["close", "volume"], "func": ccl_ext_074_cum_loss_run_vol_pct_rank},
    "ccl_ext_075_distress_composite_4factor": {"inputs": ["close", "volume"], "func": ccl_ext_075_distress_composite_4factor},
}
