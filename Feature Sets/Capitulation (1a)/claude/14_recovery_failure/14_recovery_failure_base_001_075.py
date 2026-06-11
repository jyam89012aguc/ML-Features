"""
14_recovery_failure — Base Features 001-100
Domain: failed recovery within an ongoing drawdown — failed bounces, lower-high structure,
retracement fractions of up-legs vs prior down-legs, and how quickly rallies roll over.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _local_peak(s: pd.Series, lookback: int) -> pd.Series:
    """Rolling lookback-period maximum of prior values (strict prior-bar peak)."""
    return s.shift(1).rolling(lookback, min_periods=max(1, lookback // 2)).max()


def _local_trough(s: pd.Series, lookback: int) -> pd.Series:
    """Rolling lookback-period minimum of prior values (strict prior-bar trough)."""
    return s.shift(1).rolling(lookback, min_periods=max(1, lookback // 2)).min()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Bounce magnitude relative to prior down-leg ---

def rfl_001_bounce_ret_5d(close: pd.Series) -> pd.Series:
    """5-day price return (raw bounce size over 1 week)."""
    return close.pct_change(_TD_WEEK)


def rfl_002_bounce_ret_10d(close: pd.Series) -> pd.Series:
    """10-day price return (2-week bounce window)."""
    return close.pct_change(10)


def rfl_003_bounce_ret_21d(close: pd.Series) -> pd.Series:
    """21-day price return (1-month bounce window)."""
    return close.pct_change(_TD_MON)


def rfl_004_prior_down_leg_5d(close: pd.Series) -> pd.Series:
    """Return from 10 days ago to 5 days ago (prior 5-day down leg)."""
    return _safe_div(close.shift(_TD_WEEK) - close.shift(10), close.shift(10))


def rfl_005_prior_down_leg_21d(close: pd.Series) -> pd.Series:
    """Return from 42 days ago to 21 days ago (prior 21-day down leg)."""
    return _safe_div(close.shift(_TD_MON) - close.shift(42), close.shift(42))


def rfl_006_bounce_retracement_ratio_5d(close: pd.Series) -> pd.Series:
    """5-day bounce divided by the prior 5-day decline (retracement fraction)."""
    bounce = close.pct_change(_TD_WEEK)
    prior_leg = rfl_004_prior_down_leg_5d(close)
    prior_decline = (-prior_leg).clip(lower=_EPS)
    return _safe_div(bounce, prior_decline)


def rfl_007_bounce_retracement_ratio_21d(close: pd.Series) -> pd.Series:
    """21-day bounce divided by the prior 21-day decline (monthly retracement fraction)."""
    bounce = close.pct_change(_TD_MON)
    prior_leg = rfl_005_prior_down_leg_21d(close)
    prior_decline = (-prior_leg).clip(lower=_EPS)
    return _safe_div(bounce, prior_decline)


def rfl_008_bounce_vs_21d_range(close: pd.Series) -> pd.Series:
    """5-day bounce as fraction of the 21-day high-low range."""
    rng = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    bounce = close - close.shift(_TD_WEEK)
    return _safe_div(bounce, rng.replace(0, np.nan))


def rfl_009_bounce_vs_63d_range(close: pd.Series) -> pd.Series:
    """10-day bounce as fraction of the 63-day close range."""
    rng = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    bounce = close - close.shift(10)
    return _safe_div(bounce, rng.replace(0, np.nan))


def rfl_010_bounce_vs_prior_peak_21d(close: pd.Series) -> pd.Series:
    """Current close relative to the 21-day prior rolling peak (lower-high metric)."""
    peak = _local_peak(close, _TD_MON)
    return _safe_div(close - peak, peak)


def rfl_011_bounce_vs_prior_peak_63d(close: pd.Series) -> pd.Series:
    """Current close relative to the 63-day prior rolling peak."""
    peak = _local_peak(close, _TD_QTR)
    return _safe_div(close - peak, peak)


def rfl_012_bounce_vs_prior_peak_126d(close: pd.Series) -> pd.Series:
    """Current close relative to the 126-day prior rolling peak."""
    peak = _local_peak(close, _TD_HALF)
    return _safe_div(close - peak, peak)


# --- Group B (013-025): High-based lower-high structure ---

def rfl_013_high_vs_prior_high_5d(high: pd.Series) -> pd.Series:
    """Today's high relative to the highest high over the prior 5 days (lower-high signal)."""
    prior_high = _local_peak(high, _TD_WEEK)
    return _safe_div(high - prior_high, prior_high)


def rfl_014_high_vs_prior_high_21d(high: pd.Series) -> pd.Series:
    """Today's high relative to the highest high over the prior 21 days."""
    prior_high = _local_peak(high, _TD_MON)
    return _safe_div(high - prior_high, prior_high)


def rfl_015_high_vs_prior_high_63d(high: pd.Series) -> pd.Series:
    """Today's high relative to the highest high over the prior 63 days."""
    prior_high = _local_peak(high, _TD_QTR)
    return _safe_div(high - prior_high, prior_high)


def rfl_016_consec_lower_highs_5d(high: pd.Series) -> pd.Series:
    """Consecutive days where today's 5-day max-high is below the prior 5-day max-high."""
    peak5 = high.rolling(_TD_WEEK, min_periods=1).max()
    cond = peak5 < peak5.shift(_TD_WEEK)
    return _consec_streak(cond)


def rfl_017_consec_lower_highs_daily(high: pd.Series) -> pd.Series:
    """Consecutive days where daily high is lower than prior day's high."""
    cond = high < high.shift(1)
    return _consec_streak(cond)


def rfl_018_lower_high_count_21d(high: pd.Series) -> pd.Series:
    """Count of lower-high days (daily high < prior-day high) in last 21 days."""
    return _rolling_count_true(high < high.shift(1), _TD_MON)


def rfl_019_lower_high_count_63d(high: pd.Series) -> pd.Series:
    """Count of lower-high days in last 63 days."""
    return _rolling_count_true(high < high.shift(1), _TD_QTR)


def rfl_020_lower_high_fraction_21d(high: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a lower daily high."""
    return _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON


def rfl_021_lower_high_fraction_63d(high: pd.Series) -> pd.Series:
    """Fraction of last 63 days with a lower daily high."""
    return _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR


def rfl_022_high_range_compression_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day high-of-highs to 21-day low-of-lows minus 1 (range shrinkage)."""
    hh = _rolling_max(high, _TD_MON)
    ll = _rolling_min(low, _TD_MON)
    rng = hh - ll
    prior_rng = rng.shift(_TD_MON)
    return _safe_div(rng - prior_rng, prior_rng.abs().replace(0, np.nan))


def rfl_023_peak_drawdown_from_21d_peak(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 21-day rolling peak (measures bounce failure depth)."""
    peak = _rolling_max(close, _TD_MON)
    return _safe_div(close - peak, peak)


def rfl_024_peak_drawdown_from_63d_peak(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 63-day rolling peak."""
    peak = _rolling_max(close, _TD_QTR)
    return _safe_div(close - peak, peak)


def rfl_025_peak_drawdown_from_126d_peak(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 126-day rolling peak."""
    peak = _rolling_max(close, _TD_HALF)
    return _safe_div(close - peak, peak)


# --- Group C (026-038): Up-day count, up-run length, and failed-rally flags ---

def rfl_026_consec_up_days_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive up days (close > prior close)."""
    return _consec_streak(close > close.shift(1))


def rfl_027_max_up_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day streak within trailing 21 days."""
    return _rolling_max_streak(close > close.shift(1), _TD_MON)


def rfl_028_max_up_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day streak within trailing 63 days."""
    return _rolling_max_streak(close > close.shift(1), _TD_QTR)


def rfl_029_up_day_count_21d(close: pd.Series) -> pd.Series:
    """Count of up days in last 21 days."""
    return _rolling_count_true(close > close.shift(1), _TD_MON)


def rfl_030_up_day_count_63d(close: pd.Series) -> pd.Series:
    """Count of up days in last 63 days."""
    return _rolling_count_true(close > close.shift(1), _TD_QTR)


def rfl_031_rally_fails_21d(close: pd.Series) -> pd.Series:
    """Count of 'failed rally' days in 21d: up day immediately followed by a down day."""
    up = (close > close.shift(1)).astype(float)
    down_next = (close.shift(1) > close).astype(float)
    fail = (up.shift(1) * down_next)
    return _rolling_sum(fail, _TD_MON)


def rfl_032_rally_fails_63d(close: pd.Series) -> pd.Series:
    """Count of failed-rally days (up then immediately down) in trailing 63 days."""
    up = (close > close.shift(1)).astype(float)
    down_next = (close.shift(1) > close).astype(float)
    fail = (up.shift(1) * down_next)
    return _rolling_sum(fail, _TD_QTR)


def rfl_033_up_day_ret_avg_21d(close: pd.Series) -> pd.Series:
    """Average log-return on up days over trailing 21 days."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    up_ret = log_ret.where(log_ret > 0, np.nan)
    return up_ret.rolling(_TD_MON, min_periods=1).mean()


def rfl_034_up_day_ret_avg_63d(close: pd.Series) -> pd.Series:
    """Average log-return on up days over trailing 63 days."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    up_ret = log_ret.where(log_ret > 0, np.nan)
    return up_ret.rolling(_TD_QTR, min_periods=1).mean()


def rfl_035_up_vs_down_day_magnitude_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day return to average down-day return magnitude, 21d."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    up_avg = log_ret.where(log_ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_avg = (-log_ret).where(log_ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(up_avg, dn_avg)


def rfl_036_up_vs_down_day_magnitude_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day return to average down-day return magnitude, 63d."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    up_avg = log_ret.where(log_ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_avg = (-log_ret).where(log_ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(up_avg, dn_avg)


def rfl_037_largest_single_bounce_21d(close: pd.Series) -> pd.Series:
    """Maximum single-day up return over trailing 21 days."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    return log_ret.rolling(_TD_MON, min_periods=1).max()


def rfl_038_largest_single_bounce_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day up return over trailing 63 days."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    return log_ret.rolling(_TD_QTR, min_periods=1).max()


# --- Group D (039-051): Bounce fade / rollover speed ---

def rfl_039_bounce_fade_5d_after_peak(close: pd.Series) -> pd.Series:
    """Return from 5-day prior local peak to today (measures post-peak fade)."""
    pk5 = _local_peak(close, _TD_WEEK)
    return _safe_div(close - pk5, pk5)


def rfl_040_bounce_fade_10d_after_peak(close: pd.Series) -> pd.Series:
    """Return from 10-day prior local peak to today."""
    pk10 = _local_peak(close, 10)
    return _safe_div(close - pk10, pk10)


def rfl_041_bounce_fade_21d_after_peak(close: pd.Series) -> pd.Series:
    """Return from 21-day prior local peak to today."""
    pk21 = _local_peak(close, _TD_MON)
    return _safe_div(close - pk21, pk21)


def rfl_042_close_below_5d_ago_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """How far close is below the high from 5 days ago (fade from intraday peak)."""
    return _safe_div(close - high.shift(_TD_WEEK), high.shift(_TD_WEEK))


def rfl_043_close_below_10d_ago_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """How far close is below the high from 10 days ago."""
    return _safe_div(close - high.shift(10), high.shift(10))


def rfl_044_close_vs_21d_high_pct(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close relative to the rolling 21-day high (distance from local high)."""
    hh21 = _rolling_max(high, _TD_MON)
    return _safe_div(close - hh21, hh21)


def rfl_045_close_vs_63d_high_pct(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close relative to the rolling 63-day high."""
    hh63 = _rolling_max(high, _TD_QTR)
    return _safe_div(close - hh63, hh63)


def rfl_046_up_streak_max_then_down_21d(close: pd.Series) -> pd.Series:
    """Max up-streak in last 21 days minus current up-streak (rally rollover indicator)."""
    mx = _rolling_max_streak(close > close.shift(1), _TD_MON)
    cur = _consec_streak(close > close.shift(1))
    return mx - cur


def rfl_047_bounce_reversal_count_21d(close: pd.Series) -> pd.Series:
    """Count of reversal days (close > prior open but close < prior close) in 21 days."""
    cond = (close > close.shift(1).shift(1)) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def rfl_048_intraday_reversal_count_21d(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """Count of days with high > 5d-high but close < open (intraday reversal) in 21d."""
    cond = (high > high.shift(1)) & (close < open)
    return _rolling_count_true(cond, _TD_MON)


def rfl_049_open_to_close_fade_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average (open - close) / open over last 5 days (fade from open to close)."""
    fade = _safe_div(open - close, open)
    return _rolling_mean(fade, _TD_WEEK)


def rfl_050_open_to_close_fade_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average open-to-close fade over last 21 days."""
    fade = _safe_div(open - close, open)
    return _rolling_mean(fade, _TD_MON)


def rfl_051_gap_up_fade_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-up opens that closed below prior close in trailing 21 days."""
    gap_up = open > close.shift(1)
    close_dn = close < close.shift(1)
    cond = gap_up & close_dn
    return _rolling_count_true(cond, _TD_MON)


# --- Group E (052-063): Retracement of down-leg (Fibonacci-style fractions) ---

def rfl_052_retracement_pct_of_63d_decline(close: pd.Series) -> pd.Series:
    """Close relative to 63-day trough, divided by (63d peak - 63d trough)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    rng = (pk - tr).replace(0, np.nan)
    return _safe_div(close - tr, rng)


def rfl_053_retracement_pct_of_126d_decline(close: pd.Series) -> pd.Series:
    """Close relative to 126-day trough, divided by (126d peak - 126d trough)."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    rng = (pk - tr).replace(0, np.nan)
    return _safe_div(close - tr, rng)


def rfl_054_retracement_pct_of_252d_decline(close: pd.Series) -> pd.Series:
    """Close relative to 252-day trough, divided by (252d peak - 252d trough)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rng = (pk - tr).replace(0, np.nan)
    return _safe_div(close - tr, rng)


def rfl_055_below_38pct_retracement_63d(close: pd.Series) -> pd.Series:
    """Flag: retracement fraction of 63d range < 38% (bounce failed to clear 38.2% Fib)."""
    r = rfl_052_retracement_pct_of_63d_decline(close)
    return (r < 0.382).astype(float)


def rfl_056_below_50pct_retracement_63d(close: pd.Series) -> pd.Series:
    """Flag: retracement fraction of 63d range < 50%."""
    r = rfl_052_retracement_pct_of_63d_decline(close)
    return (r < 0.50).astype(float)


def rfl_057_below_61pct_retracement_63d(close: pd.Series) -> pd.Series:
    """Flag: retracement fraction of 63d range < 61.8% (Fib level)."""
    r = rfl_052_retracement_pct_of_63d_decline(close)
    return (r < 0.618).astype(float)


def rfl_058_below_50pct_retracement_126d(close: pd.Series) -> pd.Series:
    """Flag: retracement fraction of 126d range < 50%."""
    r = rfl_053_retracement_pct_of_126d_decline(close)
    return (r < 0.50).astype(float)


def rfl_059_retracement_pct_21d_log(close: pd.Series) -> pd.Series:
    """Log1p of the 21d retracement fraction (compresses near-zero bounces)."""
    pk = _rolling_max(close, _TD_MON)
    tr = _rolling_min(close, _TD_MON)
    rng = (pk - tr).replace(0, np.nan)
    frac = _safe_div(close - tr, rng).clip(lower=0)
    return np.log1p(frac)


def rfl_060_up_leg_vs_down_leg_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 21d up-sum to 21d down-sum of log returns (net asymmetry)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    return _safe_div(up_sum, dn_sum.replace(0, np.nan))


def rfl_061_up_leg_vs_down_leg_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63d up-sum to 63d down-sum of log returns."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_sum = lr.where(lr > 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    dn_sum = (-lr).where(lr < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(up_sum, dn_sum.replace(0, np.nan))


def rfl_062_net_log_return_21d(close: pd.Series) -> pd.Series:
    """Net 21-day log return (positive = partial recovery, negative = continued decline)."""
    return _log_safe(close) - _log_safe(close.shift(_TD_MON))


def rfl_063_net_log_return_63d(close: pd.Series) -> pd.Series:
    """Net 63-day log return."""
    return _log_safe(close) - _log_safe(close.shift(_TD_QTR))


# --- Group F (064-075): Volume on bounces vs declines ---

def rfl_064_vol_on_up_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-days over last 21 days (demand side of bounces)."""
    ret = close.pct_change(1)
    return volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


def rfl_065_vol_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-days over last 21 days."""
    ret = close.pct_change(1)
    return volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


def rfl_066_vol_up_vs_down_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg up-day volume to avg down-day volume over 21 days."""
    up = rfl_064_vol_on_up_days_21d(close, volume)
    dn = rfl_065_vol_on_down_days_21d(close, volume)
    return _safe_div(up, dn)


def rfl_067_vol_up_vs_down_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg up-day volume to avg down-day volume over 63 days."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(up_vol, dn_vol)


def rfl_068_low_vol_bounce_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current up-streak exists AND avg volume < 21d average (weak bounce)."""
    streak = _consec_streak(close > close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((streak >= 2) & (volume < avg_vol)).astype(float)


def rfl_069_bounce_vol_norm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume over last 5 up days normalized by 21d avg volume."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(up_vol, avg_vol)


def rfl_070_bounce_vol_norm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up days in last 21d, normalized by 63d avg volume."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    avg_vol = _rolling_mean(volume, _TD_QTR)
    return _safe_div(up_vol, avg_vol)


def rfl_071_decline_vol_sum_vs_bounce_vol_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total volume on down days to total volume on up days, 21 days."""
    ret = close.pct_change(1)
    up_vol_sum = volume.where(ret > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn_vol_sum = volume.where(ret < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    return _safe_div(dn_vol_sum, up_vol_sum.replace(0, np.nan))


def rfl_072_decline_vol_sum_vs_bounce_vol_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total volume on down days to total volume on up days, 63 days."""
    ret = close.pct_change(1)
    up_vol_sum = volume.where(ret > 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    dn_vol_sum = volume.where(ret < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(dn_vol_sum, up_vol_sum.replace(0, np.nan))


def rfl_073_high_vol_decline_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with volume > 21d avg in last 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret < 0) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_MON)


def rfl_074_low_vol_up_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up days with volume < 21d avg in last 21 days (weak bounces)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret > 0) & (volume < avg_vol)
    return _rolling_count_true(cond, _TD_MON)


def rfl_075_vol_weighted_bounce_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average return on up days over 21 days."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, 0.0)
    vol_up = volume.where(ret > 0, 0.0)
    vol_up_sum = vol_up.rolling(_TD_MON, min_periods=1).sum()
    weighted = (up_ret * vol_up).rolling(_TD_MON, min_periods=1).sum()
    return _safe_div(weighted, vol_up_sum.replace(0, np.nan))


# --- Group M (151-175): Extended bounce/decline metrics ---

def rfl_151_bounce_ret_63d(close: pd.Series) -> pd.Series:
    """63-day price return (quarter-length bounce window)."""
    return close.pct_change(_TD_QTR)


def rfl_152_bounce_ret_126d(close: pd.Series) -> pd.Series:
    """126-day price return (half-year bounce window)."""
    return close.pct_change(_TD_HALF)


def rfl_153_prior_down_leg_63d(close: pd.Series) -> pd.Series:
    """Return from 126 days ago to 63 days ago (prior 63-day down leg)."""
    return _safe_div(close.shift(_TD_QTR) - close.shift(_TD_HALF), close.shift(_TD_HALF))


def rfl_154_bounce_retracement_ratio_63d(close: pd.Series) -> pd.Series:
    """63-day bounce divided by prior 63-day decline (quarter retracement fraction)."""
    bounce = close.pct_change(_TD_QTR)
    prior_leg = rfl_153_prior_down_leg_63d(close)
    prior_decline = (-prior_leg).clip(lower=_EPS)
    return _safe_div(bounce, prior_decline)


def rfl_155_high_vs_prior_high_126d(high: pd.Series) -> pd.Series:
    """Today's high relative to the highest high over the prior 126 days."""
    prior_high = _local_peak(high, _TD_HALF)
    return _safe_div(high - prior_high, prior_high)


def rfl_156_lower_high_count_126d(high: pd.Series) -> pd.Series:
    """Count of lower-high days in last 126 days."""
    return _rolling_count_true(high < high.shift(1), _TD_HALF)


def rfl_157_lower_high_fraction_126d(high: pd.Series) -> pd.Series:
    """Fraction of last 126 days with a lower daily high."""
    return _rolling_count_true(high < high.shift(1), _TD_HALF) / _TD_HALF


def rfl_158_up_day_count_126d(close: pd.Series) -> pd.Series:
    """Count of up days in last 126 days."""
    return _rolling_count_true(close > close.shift(1), _TD_HALF)


def rfl_159_up_day_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were up days."""
    return _rolling_count_true(close > close.shift(1), _TD_MON) / _TD_MON


def rfl_160_up_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were up days."""
    return _rolling_count_true(close > close.shift(1), _TD_QTR) / _TD_QTR


def rfl_161_down_day_ret_avg_21d(close: pd.Series) -> pd.Series:
    """Average log-return on down days over trailing 21 days (size of declines)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    dn_ret = lr.where(lr < 0, np.nan)
    return dn_ret.rolling(_TD_MON, min_periods=1).mean()


def rfl_162_down_day_ret_avg_63d(close: pd.Series) -> pd.Series:
    """Average log-return on down days over trailing 63 days."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    dn_ret = lr.where(lr < 0, np.nan)
    return dn_ret.rolling(_TD_QTR, min_periods=1).mean()


def rfl_163_largest_single_decline_21d(close: pd.Series) -> pd.Series:
    """Maximum single-day down return over trailing 21 days (worst daily loss)."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    return lr.rolling(_TD_MON, min_periods=1).min()


def rfl_164_largest_single_decline_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day down return over trailing 63 days."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    return lr.rolling(_TD_QTR, min_periods=1).min()


def rfl_165_max_down_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak within trailing 21 days."""
    from numpy import float64
    def _max_run(arr):
        mx = 0; cur = 0
        for v in arr:
            if v: cur += 1; mx = max(mx, cur)
            else: cur = 0
        return float(mx)
    cond = close < close.shift(1)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def rfl_166_max_down_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak within trailing 63 days."""
    def _max_run(arr):
        mx = 0; cur = 0
        for v in arr:
            if v: cur += 1; mx = max(mx, cur)
            else: cur = 0
        return float(mx)
    cond = close < close.shift(1)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def rfl_167_consec_down_days_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive down days (close < prior close)."""
    return _consec_streak(close < close.shift(1))


def rfl_168_bounce_vs_252d_range(close: pd.Series) -> pd.Series:
    """10-day bounce as fraction of the 252-day close range."""
    rng = _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR)
    bounce = close - close.shift(10)
    return _safe_div(bounce, rng.replace(0, np.nan))


def rfl_169_gap_up_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-up opens in trailing 21 days (open > prior close)."""
    return _rolling_count_true(open > close.shift(1), _TD_MON)


def rfl_170_gap_down_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down opens in trailing 21 days (open < prior close)."""
    return _rolling_count_true(open < close.shift(1), _TD_MON)


def rfl_171_close_vs_prior_open_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Avg (close - prior_open) / prior_open over last 21 days (multi-day body directionality)."""
    rel = _safe_div(close - open.shift(1), open.shift(1))
    return _rolling_mean(rel, _TD_MON)


def rfl_172_vol_weighted_bounce_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average return on up days over 63 days."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, 0.0)
    vol_up = volume.where(ret > 0, 0.0)
    vol_up_sum = vol_up.rolling(_TD_QTR, min_periods=1).sum()
    weighted = (up_ret * vol_up).rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(weighted, vol_up_sum.replace(0, np.nan))


def rfl_173_high_vol_decline_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with volume > 21d avg in last 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret < 0) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_QTR)


def rfl_174_low_vol_up_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up days with volume < 21d avg in last 63 days (weak bounces)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret > 0) & (volume < avg_vol)
    return _rolling_count_true(cond, _TD_QTR)


def rfl_175_vol_on_up_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-days over last 63 days (demand side of larger bounces)."""
    ret = close.pct_change(1)
    return volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()


# ── Registry ──────────────────────────────────────────────────────────────────

RECOVERY_FAILURE_REGISTRY_001_075 = {
    "rfl_001_bounce_ret_5d": {"inputs": ["close"], "func": rfl_001_bounce_ret_5d},
    "rfl_002_bounce_ret_10d": {"inputs": ["close"], "func": rfl_002_bounce_ret_10d},
    "rfl_003_bounce_ret_21d": {"inputs": ["close"], "func": rfl_003_bounce_ret_21d},
    "rfl_004_prior_down_leg_5d": {"inputs": ["close"], "func": rfl_004_prior_down_leg_5d},
    "rfl_005_prior_down_leg_21d": {"inputs": ["close"], "func": rfl_005_prior_down_leg_21d},
    "rfl_006_bounce_retracement_ratio_5d": {"inputs": ["close"], "func": rfl_006_bounce_retracement_ratio_5d},
    "rfl_007_bounce_retracement_ratio_21d": {"inputs": ["close"], "func": rfl_007_bounce_retracement_ratio_21d},
    "rfl_008_bounce_vs_21d_range": {"inputs": ["close"], "func": rfl_008_bounce_vs_21d_range},
    "rfl_009_bounce_vs_63d_range": {"inputs": ["close"], "func": rfl_009_bounce_vs_63d_range},
    "rfl_010_bounce_vs_prior_peak_21d": {"inputs": ["close"], "func": rfl_010_bounce_vs_prior_peak_21d},
    "rfl_011_bounce_vs_prior_peak_63d": {"inputs": ["close"], "func": rfl_011_bounce_vs_prior_peak_63d},
    "rfl_012_bounce_vs_prior_peak_126d": {"inputs": ["close"], "func": rfl_012_bounce_vs_prior_peak_126d},
    "rfl_013_high_vs_prior_high_5d": {"inputs": ["high"], "func": rfl_013_high_vs_prior_high_5d},
    "rfl_014_high_vs_prior_high_21d": {"inputs": ["high"], "func": rfl_014_high_vs_prior_high_21d},
    "rfl_015_high_vs_prior_high_63d": {"inputs": ["high"], "func": rfl_015_high_vs_prior_high_63d},
    "rfl_016_consec_lower_highs_5d": {"inputs": ["high"], "func": rfl_016_consec_lower_highs_5d},
    "rfl_017_consec_lower_highs_daily": {"inputs": ["high"], "func": rfl_017_consec_lower_highs_daily},
    "rfl_018_lower_high_count_21d": {"inputs": ["high"], "func": rfl_018_lower_high_count_21d},
    "rfl_019_lower_high_count_63d": {"inputs": ["high"], "func": rfl_019_lower_high_count_63d},
    "rfl_020_lower_high_fraction_21d": {"inputs": ["high"], "func": rfl_020_lower_high_fraction_21d},
    "rfl_021_lower_high_fraction_63d": {"inputs": ["high"], "func": rfl_021_lower_high_fraction_63d},
    "rfl_022_high_range_compression_21d": {"inputs": ["high", "low"], "func": rfl_022_high_range_compression_21d},
    "rfl_023_peak_drawdown_from_21d_peak": {"inputs": ["close"], "func": rfl_023_peak_drawdown_from_21d_peak},
    "rfl_024_peak_drawdown_from_63d_peak": {"inputs": ["close"], "func": rfl_024_peak_drawdown_from_63d_peak},
    "rfl_025_peak_drawdown_from_126d_peak": {"inputs": ["close"], "func": rfl_025_peak_drawdown_from_126d_peak},
    "rfl_026_consec_up_days_current": {"inputs": ["close"], "func": rfl_026_consec_up_days_current},
    "rfl_027_max_up_streak_21d": {"inputs": ["close"], "func": rfl_027_max_up_streak_21d},
    "rfl_028_max_up_streak_63d": {"inputs": ["close"], "func": rfl_028_max_up_streak_63d},
    "rfl_029_up_day_count_21d": {"inputs": ["close"], "func": rfl_029_up_day_count_21d},
    "rfl_030_up_day_count_63d": {"inputs": ["close"], "func": rfl_030_up_day_count_63d},
    "rfl_031_rally_fails_21d": {"inputs": ["close"], "func": rfl_031_rally_fails_21d},
    "rfl_032_rally_fails_63d": {"inputs": ["close"], "func": rfl_032_rally_fails_63d},
    "rfl_033_up_day_ret_avg_21d": {"inputs": ["close"], "func": rfl_033_up_day_ret_avg_21d},
    "rfl_034_up_day_ret_avg_63d": {"inputs": ["close"], "func": rfl_034_up_day_ret_avg_63d},
    "rfl_035_up_vs_down_day_magnitude_ratio_21d": {"inputs": ["close"], "func": rfl_035_up_vs_down_day_magnitude_ratio_21d},
    "rfl_036_up_vs_down_day_magnitude_ratio_63d": {"inputs": ["close"], "func": rfl_036_up_vs_down_day_magnitude_ratio_63d},
    "rfl_037_largest_single_bounce_21d": {"inputs": ["close"], "func": rfl_037_largest_single_bounce_21d},
    "rfl_038_largest_single_bounce_63d": {"inputs": ["close"], "func": rfl_038_largest_single_bounce_63d},
    "rfl_039_bounce_fade_5d_after_peak": {"inputs": ["close"], "func": rfl_039_bounce_fade_5d_after_peak},
    "rfl_040_bounce_fade_10d_after_peak": {"inputs": ["close"], "func": rfl_040_bounce_fade_10d_after_peak},
    "rfl_041_bounce_fade_21d_after_peak": {"inputs": ["close"], "func": rfl_041_bounce_fade_21d_after_peak},
    "rfl_042_close_below_5d_ago_high": {"inputs": ["close", "high"], "func": rfl_042_close_below_5d_ago_high},
    "rfl_043_close_below_10d_ago_high": {"inputs": ["close", "high"], "func": rfl_043_close_below_10d_ago_high},
    "rfl_044_close_vs_21d_high_pct": {"inputs": ["close", "high"], "func": rfl_044_close_vs_21d_high_pct},
    "rfl_045_close_vs_63d_high_pct": {"inputs": ["close", "high"], "func": rfl_045_close_vs_63d_high_pct},
    "rfl_046_up_streak_max_then_down_21d": {"inputs": ["close"], "func": rfl_046_up_streak_max_then_down_21d},
    "rfl_047_bounce_reversal_count_21d": {"inputs": ["close"], "func": rfl_047_bounce_reversal_count_21d},
    "rfl_048_intraday_reversal_count_21d": {"inputs": ["close", "open", "high"], "func": rfl_048_intraday_reversal_count_21d},
    "rfl_049_open_to_close_fade_5d": {"inputs": ["close", "open"], "func": rfl_049_open_to_close_fade_5d},
    "rfl_050_open_to_close_fade_21d": {"inputs": ["close", "open"], "func": rfl_050_open_to_close_fade_21d},
    "rfl_051_gap_up_fade_count_21d": {"inputs": ["close", "open"], "func": rfl_051_gap_up_fade_count_21d},
    "rfl_052_retracement_pct_of_63d_decline": {"inputs": ["close"], "func": rfl_052_retracement_pct_of_63d_decline},
    "rfl_053_retracement_pct_of_126d_decline": {"inputs": ["close"], "func": rfl_053_retracement_pct_of_126d_decline},
    "rfl_054_retracement_pct_of_252d_decline": {"inputs": ["close"], "func": rfl_054_retracement_pct_of_252d_decline},
    "rfl_055_below_38pct_retracement_63d": {"inputs": ["close"], "func": rfl_055_below_38pct_retracement_63d},
    "rfl_056_below_50pct_retracement_63d": {"inputs": ["close"], "func": rfl_056_below_50pct_retracement_63d},
    "rfl_057_below_61pct_retracement_63d": {"inputs": ["close"], "func": rfl_057_below_61pct_retracement_63d},
    "rfl_058_below_50pct_retracement_126d": {"inputs": ["close"], "func": rfl_058_below_50pct_retracement_126d},
    "rfl_059_retracement_pct_21d_log": {"inputs": ["close"], "func": rfl_059_retracement_pct_21d_log},
    "rfl_060_up_leg_vs_down_leg_ratio_21d": {"inputs": ["close"], "func": rfl_060_up_leg_vs_down_leg_ratio_21d},
    "rfl_061_up_leg_vs_down_leg_ratio_63d": {"inputs": ["close"], "func": rfl_061_up_leg_vs_down_leg_ratio_63d},
    "rfl_062_net_log_return_21d": {"inputs": ["close"], "func": rfl_062_net_log_return_21d},
    "rfl_063_net_log_return_63d": {"inputs": ["close"], "func": rfl_063_net_log_return_63d},
    "rfl_064_vol_on_up_days_21d": {"inputs": ["close", "volume"], "func": rfl_064_vol_on_up_days_21d},
    "rfl_065_vol_on_down_days_21d": {"inputs": ["close", "volume"], "func": rfl_065_vol_on_down_days_21d},
    "rfl_066_vol_up_vs_down_ratio_21d": {"inputs": ["close", "volume"], "func": rfl_066_vol_up_vs_down_ratio_21d},
    "rfl_067_vol_up_vs_down_ratio_63d": {"inputs": ["close", "volume"], "func": rfl_067_vol_up_vs_down_ratio_63d},
    "rfl_068_low_vol_bounce_flag_21d": {"inputs": ["close", "volume"], "func": rfl_068_low_vol_bounce_flag_21d},
    "rfl_069_bounce_vol_norm_5d": {"inputs": ["close", "volume"], "func": rfl_069_bounce_vol_norm_5d},
    "rfl_070_bounce_vol_norm_21d": {"inputs": ["close", "volume"], "func": rfl_070_bounce_vol_norm_21d},
    "rfl_071_decline_vol_sum_vs_bounce_vol_sum_21d": {"inputs": ["close", "volume"], "func": rfl_071_decline_vol_sum_vs_bounce_vol_sum_21d},
    "rfl_072_decline_vol_sum_vs_bounce_vol_sum_63d": {"inputs": ["close", "volume"], "func": rfl_072_decline_vol_sum_vs_bounce_vol_sum_63d},
    "rfl_073_high_vol_decline_count_21d": {"inputs": ["close", "volume"], "func": rfl_073_high_vol_decline_count_21d},
    "rfl_074_low_vol_up_day_count_21d": {"inputs": ["close", "volume"], "func": rfl_074_low_vol_up_day_count_21d},
    "rfl_075_vol_weighted_bounce_ret_21d": {"inputs": ["close", "volume"], "func": rfl_075_vol_weighted_bounce_ret_21d},
    "rfl_151_bounce_ret_63d": {"inputs": ["close"], "func": rfl_151_bounce_ret_63d},
    "rfl_152_bounce_ret_126d": {"inputs": ["close"], "func": rfl_152_bounce_ret_126d},
    "rfl_153_prior_down_leg_63d": {"inputs": ["close"], "func": rfl_153_prior_down_leg_63d},
    "rfl_154_bounce_retracement_ratio_63d": {"inputs": ["close"], "func": rfl_154_bounce_retracement_ratio_63d},
    "rfl_155_high_vs_prior_high_126d": {"inputs": ["high"], "func": rfl_155_high_vs_prior_high_126d},
    "rfl_156_lower_high_count_126d": {"inputs": ["high"], "func": rfl_156_lower_high_count_126d},
    "rfl_157_lower_high_fraction_126d": {"inputs": ["high"], "func": rfl_157_lower_high_fraction_126d},
    "rfl_158_up_day_count_126d": {"inputs": ["close"], "func": rfl_158_up_day_count_126d},
    "rfl_159_up_day_fraction_21d": {"inputs": ["close"], "func": rfl_159_up_day_fraction_21d},
    "rfl_160_up_day_fraction_63d": {"inputs": ["close"], "func": rfl_160_up_day_fraction_63d},
    "rfl_161_down_day_ret_avg_21d": {"inputs": ["close"], "func": rfl_161_down_day_ret_avg_21d},
    "rfl_162_down_day_ret_avg_63d": {"inputs": ["close"], "func": rfl_162_down_day_ret_avg_63d},
    "rfl_163_largest_single_decline_21d": {"inputs": ["close"], "func": rfl_163_largest_single_decline_21d},
    "rfl_164_largest_single_decline_63d": {"inputs": ["close"], "func": rfl_164_largest_single_decline_63d},
    "rfl_165_max_down_streak_21d": {"inputs": ["close"], "func": rfl_165_max_down_streak_21d},
    "rfl_166_max_down_streak_63d": {"inputs": ["close"], "func": rfl_166_max_down_streak_63d},
    "rfl_167_consec_down_days_current": {"inputs": ["close"], "func": rfl_167_consec_down_days_current},
    "rfl_168_bounce_vs_252d_range": {"inputs": ["close"], "func": rfl_168_bounce_vs_252d_range},
    "rfl_169_gap_up_count_21d": {"inputs": ["close", "open"], "func": rfl_169_gap_up_count_21d},
    "rfl_170_gap_down_count_21d": {"inputs": ["close", "open"], "func": rfl_170_gap_down_count_21d},
    "rfl_171_close_vs_prior_open_21d": {"inputs": ["close", "open"], "func": rfl_171_close_vs_prior_open_21d},
    "rfl_172_vol_weighted_bounce_ret_63d": {"inputs": ["close", "volume"], "func": rfl_172_vol_weighted_bounce_ret_63d},
    "rfl_173_high_vol_decline_count_63d": {"inputs": ["close", "volume"], "func": rfl_173_high_vol_decline_count_63d},
    "rfl_174_low_vol_up_day_count_63d": {"inputs": ["close", "volume"], "func": rfl_174_low_vol_up_day_count_63d},
    "rfl_175_vol_on_up_days_63d": {"inputs": ["close", "volume"], "func": rfl_175_vol_on_up_days_63d},
}
