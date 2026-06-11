"""
08_decline_streaks — Base Features 001-075
Domain: consecutive down-day / down-week / down-month run lengths and streak severity
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """
    Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: each time cond is False, the group counter increments.
    Within a group of True values, cumcount gives the run length.
    Returns 0 on False rows and the current streak length on True rows.
    """
    c = cond.astype(int)
    # group id increments every time we are NOT in a True streak
    group = (~cond).cumsum()
    # cumcount within group (0-based), add 1 to get length
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (scalar apply)."""
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


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Current consecutive down-day streak (close < prior close) ---

def dstk_001_consec_down_days_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive days where close < prior close."""
    cond = close < close.shift(1)
    return _consec_streak(cond)


def dstk_002_consec_down_days_current_log(close: pd.Series) -> pd.Series:
    """Log1p of current down-day streak (compresses long tails)."""
    return np.log1p(dstk_001_consec_down_days_current(close))


def dstk_003_consec_down_days_norm_21d(close: pd.Series) -> pd.Series:
    """Current down-day streak normalized by 21-day average streak length."""
    streak = dstk_001_consec_down_days_current(close)
    avg = _rolling_mean(streak, _TD_MON)
    return _safe_div(streak, avg)


def dstk_004_consec_down_days_norm_63d(close: pd.Series) -> pd.Series:
    """Current down-day streak normalized by 63-day average streak length."""
    streak = dstk_001_consec_down_days_current(close)
    avg = _rolling_mean(streak, _TD_QTR)
    return _safe_div(streak, avg)


def dstk_005_consec_down_days_norm_252d(close: pd.Series) -> pd.Series:
    """Current down-day streak normalized by 252-day average streak length."""
    streak = dstk_001_consec_down_days_current(close)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_006_consec_down_days_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current down streak within trailing 252-day streak series."""
    streak = dstk_001_consec_down_days_current(close)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dstk_007_consec_down_days_gt5_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current down-day streak >= 5 (full week of red)."""
    return (dstk_001_consec_down_days_current(close) >= 5).astype(float)


def dstk_008_consec_down_days_gt10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current down-day streak >= 10 (two weeks of red)."""
    return (dstk_001_consec_down_days_current(close) >= 10).astype(float)


def dstk_009_consec_down_days_gt15_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current down-day streak >= 15 (three weeks of red)."""
    return (dstk_001_consec_down_days_current(close) >= 15).astype(float)


def dstk_010_consec_down_days_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum down-day streak (how extreme is the current record)."""
    streak = dstk_001_consec_down_days_current(close)
    return streak.expanding(min_periods=1).max()


# --- Group B (011-020): Max down-streak in rolling windows ---

def dstk_011_max_down_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day run within trailing 21 days."""
    cond = close < close.shift(1)
    return _rolling_max_streak(cond, _TD_MON)


def dstk_012_max_down_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day run within trailing 63 days."""
    cond = close < close.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_013_max_down_streak_126d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day run within trailing 126 days."""
    cond = close < close.shift(1)
    return _rolling_max_streak(cond, _TD_HALF)


def dstk_014_max_down_streak_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day run within trailing 252 days."""
    cond = close < close.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_015_max_down_streak_504d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day run within trailing 504 days."""
    cond = close < close.shift(1)
    return _rolling_max_streak(cond, 504)


def dstk_016_current_vs_max_streak_63d(close: pd.Series) -> pd.Series:
    """Current down-streak as fraction of 63-day maximum down-streak."""
    cur = dstk_001_consec_down_days_current(close)
    mx = dstk_012_max_down_streak_63d(close)
    return _safe_div(cur, mx)


def dstk_017_current_vs_max_streak_252d(close: pd.Series) -> pd.Series:
    """Current down-streak as fraction of 252-day maximum down-streak."""
    cur = dstk_001_consec_down_days_current(close)
    mx = dstk_014_max_down_streak_252d(close)
    return _safe_div(cur, mx)


def dstk_018_max_streak_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day max streak to 252-day max streak (recent intensity)."""
    return _safe_div(dstk_011_max_down_streak_21d(close), dstk_014_max_down_streak_252d(close))


def dstk_019_max_streak_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day max streak to 252-day max streak."""
    return _safe_div(dstk_012_max_down_streak_63d(close), dstk_014_max_down_streak_252d(close))


def dstk_020_max_streak_252d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day max down-streak (all-history)."""
    mx = dstk_014_max_down_streak_252d(close)
    return mx.expanding(min_periods=5).rank(pct=True)


# --- Group C (021-030): Down-week and down-month streaks (aggregated periods) ---

def dstk_021_consec_down_weeks_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive 5-day periods where period-end close < period-start close."""
    weekly_ret = close.pct_change(_TD_WEEK)
    cond = weekly_ret < 0
    return _consec_streak(cond)


def dstk_022_max_down_weeks_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-week run within trailing 63 days."""
    weekly_ret = close.pct_change(_TD_WEEK)
    cond = weekly_ret < 0
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_023_max_down_weeks_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-week run within trailing 252 days."""
    weekly_ret = close.pct_change(_TD_WEEK)
    cond = weekly_ret < 0
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_024_consec_down_months_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive 21-day periods where period-end close < period-start close."""
    monthly_ret = close.pct_change(_TD_MON)
    cond = monthly_ret < 0
    return _consec_streak(cond)


def dstk_025_max_down_months_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-month run within trailing 252 days."""
    monthly_ret = close.pct_change(_TD_MON)
    cond = monthly_ret < 0
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_026_max_down_months_504d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-month run within trailing 504 days."""
    monthly_ret = close.pct_change(_TD_MON)
    cond = monthly_ret < 0
    return _rolling_max_streak(cond, 504)


def dstk_027_down_week_streak_norm_252d(close: pd.Series) -> pd.Series:
    """Current down-week streak normalized by 252-day avg."""
    streak = dstk_021_consec_down_weeks_current(close)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_028_down_month_streak_norm_252d(close: pd.Series) -> pd.Series:
    """Current down-month streak normalized by 252-day avg."""
    streak = dstk_024_consec_down_months_current(close)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_029_consec_down_qtrs_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive 63-day periods with negative return."""
    qtr_ret = close.pct_change(_TD_QTR)
    cond = qtr_ret < 0
    return _consec_streak(cond)


def dstk_030_down_week_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current down-week streak within trailing 252 days."""
    streak = dstk_021_consec_down_weeks_current(close)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (031-040): Close-below-MA streaks ---

def dstk_031_consec_close_below_sma21(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 21-day SMA."""
    ma = _rolling_mean(close, _TD_MON)
    cond = close < ma
    return _consec_streak(cond)


def dstk_032_consec_close_below_sma63(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 63-day SMA."""
    ma = _rolling_mean(close, _TD_QTR)
    cond = close < ma
    return _consec_streak(cond)


def dstk_033_consec_close_below_sma200(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 200-day SMA."""
    ma = _rolling_mean(close, 200)
    cond = close < ma
    return _consec_streak(cond)


def dstk_034_max_close_below_sma200_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days below 200-day SMA within trailing 252 days."""
    ma = _rolling_mean(close, 200)
    cond = close < ma
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_035_consec_close_below_ema21(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 21-day EMA."""
    ema = _ewm_mean(close, _TD_MON)
    cond = close < ema
    return _consec_streak(cond)


def dstk_036_consec_close_below_ema63(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 63-day EMA."""
    ema = _ewm_mean(close, _TD_QTR)
    cond = close < ema
    return _consec_streak(cond)


def dstk_037_consec_close_below_ema200(close: pd.Series) -> pd.Series:
    """Current consecutive days close < 200-day EMA."""
    ema = _ewm_mean(close, 200)
    cond = close < ema
    return _consec_streak(cond)


def dstk_038_below_sma200_streak_norm_252d(close: pd.Series) -> pd.Series:
    """Below-SMA200 streak normalized by 252-day average."""
    streak = dstk_033_consec_close_below_sma200(close)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_039_consec_close_below_open(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive days where close < open (bear candle streak)."""
    cond = close < open
    return _consec_streak(cond)


def dstk_040_max_close_below_open_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive bear-candle days within trailing 63 days."""
    cond = close < open
    return _rolling_max_streak(cond, _TD_QTR)


# --- Group E (041-050): Lower-low / lower-high streaks and new-low streaks ---

def dstk_041_consec_lower_lows(low: pd.Series) -> pd.Series:
    """Current consecutive days of lower intraday lows (each low < prior low)."""
    cond = low < low.shift(1)
    return _consec_streak(cond)


def dstk_042_consec_lower_highs(high: pd.Series) -> pd.Series:
    """Current consecutive days of lower intraday highs (each high < prior high)."""
    cond = high < high.shift(1)
    return _consec_streak(cond)


def dstk_043_consec_lower_lows_and_highs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where BOTH high and low are lower than prior day."""
    cond = (low < low.shift(1)) & (high < high.shift(1))
    return _consec_streak(cond)


def dstk_044_consec_new_21d_low_close(close: pd.Series) -> pd.Series:
    """Current consecutive days where close makes a new 21-day low."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    cond = close < roll_min
    return _consec_streak(cond)


def dstk_045_consec_new_63d_low_close(close: pd.Series) -> pd.Series:
    """Current consecutive days where close makes a new 63-day low."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    cond = close < roll_min
    return _consec_streak(cond)


def dstk_046_consec_new_252d_low_close(close: pd.Series) -> pd.Series:
    """Current consecutive days where close makes a new 252-day low."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    cond = close < roll_min
    return _consec_streak(cond)


def dstk_047_consec_new_low_intraday(low: pd.Series) -> pd.Series:
    """Current consecutive days where intraday low is below prior 21-day low."""
    roll_min = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    cond = low < roll_min
    return _consec_streak(cond)


def dstk_048_max_lower_low_streak_63d(low: pd.Series) -> pd.Series:
    """Maximum consecutive lower-low run within trailing 63 days."""
    cond = low < low.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_049_max_lower_low_streak_252d(low: pd.Series) -> pd.Series:
    """Maximum consecutive lower-low run within trailing 252 days."""
    cond = low < low.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_050_lower_low_streak_norm_252d(low: pd.Series) -> pd.Series:
    """Current lower-low streak normalized by 252-day average lower-low streak."""
    streak = dstk_041_consec_lower_lows(low)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


# --- Group F (051-060): Cumulative loss over streak and severity measures ---

def dstk_051_cum_return_current_down_streak(close: pd.Series) -> pd.Series:
    """Cumulative log-return accumulated over the current consecutive down-day streak."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    group = (~cond).cumsum()
    # sum log returns within current down-streak group
    cum = daily_log.groupby(group).cumsum()
    return cum.where(cond, 0.0)


def dstk_052_cum_return_current_down_streak_abs(close: pd.Series) -> pd.Series:
    """Absolute value of cumulative log-return over current down streak."""
    return dstk_051_cum_return_current_down_streak(close).abs()


def dstk_053_avg_daily_loss_current_streak(close: pd.Series) -> pd.Series:
    """Average daily log-return over the current down streak."""
    cum = dstk_051_cum_return_current_down_streak(close)
    length = dstk_001_consec_down_days_current(close)
    return _safe_div(cum, length)


def dstk_054_worst_streak_loss_63d(close: pd.Series) -> pd.Series:
    """Minimum (most negative) cumulative streak return seen within trailing 63 days."""
    cum = dstk_051_cum_return_current_down_streak(close)
    return _rolling_min(cum, _TD_QTR)


def dstk_055_worst_streak_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum cumulative streak return seen within trailing 252 days."""
    cum = dstk_051_cum_return_current_down_streak(close)
    return _rolling_min(cum, _TD_YEAR)


def dstk_056_current_streak_loss_vs_worst_252d(close: pd.Series) -> pd.Series:
    """Current streak cumulative loss as fraction of 252-day worst streak loss."""
    cur = dstk_051_cum_return_current_down_streak(close)
    worst = dstk_055_worst_streak_loss_252d(close)
    return _safe_div(cur, worst)


def dstk_057_streak_severity_sum_21d(close: pd.Series) -> pd.Series:
    """Sum of all down-day log-returns (only negative days) over trailing 21 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    down_only = daily_log.where(daily_log < 0, 0.0)
    return _rolling_sum(down_only, _TD_MON)


def dstk_058_streak_severity_sum_63d(close: pd.Series) -> pd.Series:
    """Sum of all down-day log-returns over trailing 63 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    down_only = daily_log.where(daily_log < 0, 0.0)
    return _rolling_sum(down_only, _TD_QTR)


def dstk_059_streak_severity_sum_252d(close: pd.Series) -> pd.Series:
    """Sum of all down-day log-returns over trailing 252 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    down_only = daily_log.where(daily_log < 0, 0.0)
    return _rolling_sum(down_only, _TD_YEAR)


def dstk_060_avg_down_day_return_252d(close: pd.Series) -> pd.Series:
    """Average daily log-return on down days over trailing 252 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    down_only = daily_log.where(daily_log < 0, np.nan)
    return down_only.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


# --- Group G (061-075): Down-up ratios, no-green-day indicators, volume streaks ---

def dstk_061_down_up_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of down-day count to up-day count in trailing 21 days."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_MON)
    up = _rolling_count_true(ret > 0, _TD_MON)
    return _safe_div(down, up)


def dstk_062_down_up_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of down-day count to up-day count in trailing 63 days."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_QTR)
    up = _rolling_count_true(ret > 0, _TD_QTR)
    return _safe_div(down, up)


def dstk_063_down_up_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of down-day count to up-day count in trailing 252 days."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_YEAR)
    up = _rolling_count_true(ret > 0, _TD_YEAR)
    return _safe_div(down, up)


def dstk_064_no_green_day_5d_flag(close: pd.Series) -> pd.Series:
    """Flag: zero up-days in the last 5 trading days."""
    ret = close.pct_change(1)
    up_count = _rolling_count_true(ret > 0, _TD_WEEK)
    return (up_count == 0).astype(float)


def dstk_065_no_green_day_10d_flag(close: pd.Series) -> pd.Series:
    """Flag: zero up-days in the last 10 trading days."""
    ret = close.pct_change(1)
    up_count = _rolling_count_true(ret > 0, 10)
    return (up_count == 0).astype(float)


def dstk_066_no_green_day_21d_count(close: pd.Series) -> pd.Series:
    """Count of up-days in last 21 days (low count = distress signal)."""
    ret = close.pct_change(1)
    return _rolling_count_true(ret > 0, _TD_MON)


def dstk_067_down_day_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were down."""
    ret = close.pct_change(1)
    return _rolling_count_true(ret < 0, _TD_MON) / _TD_MON


def dstk_068_down_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were down."""
    ret = close.pct_change(1)
    return _rolling_count_true(ret < 0, _TD_QTR) / _TD_QTR


def dstk_069_down_day_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days that were down."""
    ret = close.pct_change(1)
    return _rolling_count_true(ret < 0, _TD_YEAR) / _TD_YEAR


def dstk_070_consec_down_volume_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume is below prior-day volume (drying-up streak)."""
    cond = volume < volume.shift(1)
    return _consec_streak(cond)


def dstk_071_consec_up_volume_on_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive down-price days that also have above-average volume (panic selling)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (close < close.shift(1)) & (volume > avg_vol)
    return _consec_streak(cond)


def dstk_072_gap_down_streak_current(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive gap-down opens (open < prior close)."""
    cond = open < close.shift(1)
    return _consec_streak(cond)


def dstk_073_max_gap_down_streak_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive gap-down open streak within trailing 63 days."""
    cond = open < close.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_074_avg_down_streak_length_252d(close: pd.Series) -> pd.Series:
    """Average length of completed down-day streaks over trailing 252 days.
    Approximated as (down-day count) / (number of streak starts) in window."""
    ret = close.pct_change(1)
    is_down = (ret < 0).astype(float)
    is_start = ((ret < 0) & (ret.shift(1) >= 0)).astype(float)
    total_down = _rolling_sum(is_down, _TD_YEAR)
    num_starts = _rolling_sum(is_start, _TD_YEAR)
    return _safe_div(total_down, num_starts.clip(lower=1))


def dstk_075_down_streak_freq_252d(close: pd.Series) -> pd.Series:
    """Frequency of down-streak starts per 252 days (how often streaks begin)."""
    ret = close.pct_change(1)
    is_start = ((ret < 0) & (ret.shift(1) >= 0)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

DECLINE_STREAKS_REGISTRY_001_075 = {
    "dstk_001_consec_down_days_current": {"inputs": ["close"], "func": dstk_001_consec_down_days_current},
    "dstk_002_consec_down_days_current_log": {"inputs": ["close"], "func": dstk_002_consec_down_days_current_log},
    "dstk_003_consec_down_days_norm_21d": {"inputs": ["close"], "func": dstk_003_consec_down_days_norm_21d},
    "dstk_004_consec_down_days_norm_63d": {"inputs": ["close"], "func": dstk_004_consec_down_days_norm_63d},
    "dstk_005_consec_down_days_norm_252d": {"inputs": ["close"], "func": dstk_005_consec_down_days_norm_252d},
    "dstk_006_consec_down_days_pct_rank_252d": {"inputs": ["close"], "func": dstk_006_consec_down_days_pct_rank_252d},
    "dstk_007_consec_down_days_gt5_flag": {"inputs": ["close"], "func": dstk_007_consec_down_days_gt5_flag},
    "dstk_008_consec_down_days_gt10_flag": {"inputs": ["close"], "func": dstk_008_consec_down_days_gt10_flag},
    "dstk_009_consec_down_days_gt15_flag": {"inputs": ["close"], "func": dstk_009_consec_down_days_gt15_flag},
    "dstk_010_consec_down_days_expanding_max": {"inputs": ["close"], "func": dstk_010_consec_down_days_expanding_max},
    "dstk_011_max_down_streak_21d": {"inputs": ["close"], "func": dstk_011_max_down_streak_21d},
    "dstk_012_max_down_streak_63d": {"inputs": ["close"], "func": dstk_012_max_down_streak_63d},
    "dstk_013_max_down_streak_126d": {"inputs": ["close"], "func": dstk_013_max_down_streak_126d},
    "dstk_014_max_down_streak_252d": {"inputs": ["close"], "func": dstk_014_max_down_streak_252d},
    "dstk_015_max_down_streak_504d": {"inputs": ["close"], "func": dstk_015_max_down_streak_504d},
    "dstk_016_current_vs_max_streak_63d": {"inputs": ["close"], "func": dstk_016_current_vs_max_streak_63d},
    "dstk_017_current_vs_max_streak_252d": {"inputs": ["close"], "func": dstk_017_current_vs_max_streak_252d},
    "dstk_018_max_streak_21d_vs_252d_ratio": {"inputs": ["close"], "func": dstk_018_max_streak_21d_vs_252d_ratio},
    "dstk_019_max_streak_63d_vs_252d_ratio": {"inputs": ["close"], "func": dstk_019_max_streak_63d_vs_252d_ratio},
    "dstk_020_max_streak_252d_expanding_rank": {"inputs": ["close"], "func": dstk_020_max_streak_252d_expanding_rank},
    "dstk_021_consec_down_weeks_current": {"inputs": ["close"], "func": dstk_021_consec_down_weeks_current},
    "dstk_022_max_down_weeks_63d": {"inputs": ["close"], "func": dstk_022_max_down_weeks_63d},
    "dstk_023_max_down_weeks_252d": {"inputs": ["close"], "func": dstk_023_max_down_weeks_252d},
    "dstk_024_consec_down_months_current": {"inputs": ["close"], "func": dstk_024_consec_down_months_current},
    "dstk_025_max_down_months_252d": {"inputs": ["close"], "func": dstk_025_max_down_months_252d},
    "dstk_026_max_down_months_504d": {"inputs": ["close"], "func": dstk_026_max_down_months_504d},
    "dstk_027_down_week_streak_norm_252d": {"inputs": ["close"], "func": dstk_027_down_week_streak_norm_252d},
    "dstk_028_down_month_streak_norm_252d": {"inputs": ["close"], "func": dstk_028_down_month_streak_norm_252d},
    "dstk_029_consec_down_qtrs_current": {"inputs": ["close"], "func": dstk_029_consec_down_qtrs_current},
    "dstk_030_down_week_pct_rank_252d": {"inputs": ["close"], "func": dstk_030_down_week_pct_rank_252d},
    "dstk_031_consec_close_below_sma21": {"inputs": ["close"], "func": dstk_031_consec_close_below_sma21},
    "dstk_032_consec_close_below_sma63": {"inputs": ["close"], "func": dstk_032_consec_close_below_sma63},
    "dstk_033_consec_close_below_sma200": {"inputs": ["close"], "func": dstk_033_consec_close_below_sma200},
    "dstk_034_max_close_below_sma200_252d": {"inputs": ["close"], "func": dstk_034_max_close_below_sma200_252d},
    "dstk_035_consec_close_below_ema21": {"inputs": ["close"], "func": dstk_035_consec_close_below_ema21},
    "dstk_036_consec_close_below_ema63": {"inputs": ["close"], "func": dstk_036_consec_close_below_ema63},
    "dstk_037_consec_close_below_ema200": {"inputs": ["close"], "func": dstk_037_consec_close_below_ema200},
    "dstk_038_below_sma200_streak_norm_252d": {"inputs": ["close"], "func": dstk_038_below_sma200_streak_norm_252d},
    "dstk_039_consec_close_below_open": {"inputs": ["close", "open"], "func": dstk_039_consec_close_below_open},
    "dstk_040_max_close_below_open_63d": {"inputs": ["close", "open"], "func": dstk_040_max_close_below_open_63d},
    "dstk_041_consec_lower_lows": {"inputs": ["low"], "func": dstk_041_consec_lower_lows},
    "dstk_042_consec_lower_highs": {"inputs": ["high"], "func": dstk_042_consec_lower_highs},
    "dstk_043_consec_lower_lows_and_highs": {"inputs": ["high", "low"], "func": dstk_043_consec_lower_lows_and_highs},
    "dstk_044_consec_new_21d_low_close": {"inputs": ["close"], "func": dstk_044_consec_new_21d_low_close},
    "dstk_045_consec_new_63d_low_close": {"inputs": ["close"], "func": dstk_045_consec_new_63d_low_close},
    "dstk_046_consec_new_252d_low_close": {"inputs": ["close"], "func": dstk_046_consec_new_252d_low_close},
    "dstk_047_consec_new_low_intraday": {"inputs": ["low"], "func": dstk_047_consec_new_low_intraday},
    "dstk_048_max_lower_low_streak_63d": {"inputs": ["low"], "func": dstk_048_max_lower_low_streak_63d},
    "dstk_049_max_lower_low_streak_252d": {"inputs": ["low"], "func": dstk_049_max_lower_low_streak_252d},
    "dstk_050_lower_low_streak_norm_252d": {"inputs": ["low"], "func": dstk_050_lower_low_streak_norm_252d},
    "dstk_051_cum_return_current_down_streak": {"inputs": ["close"], "func": dstk_051_cum_return_current_down_streak},
    "dstk_052_cum_return_current_down_streak_abs": {"inputs": ["close"], "func": dstk_052_cum_return_current_down_streak_abs},
    "dstk_053_avg_daily_loss_current_streak": {"inputs": ["close"], "func": dstk_053_avg_daily_loss_current_streak},
    "dstk_054_worst_streak_loss_63d": {"inputs": ["close"], "func": dstk_054_worst_streak_loss_63d},
    "dstk_055_worst_streak_loss_252d": {"inputs": ["close"], "func": dstk_055_worst_streak_loss_252d},
    "dstk_056_current_streak_loss_vs_worst_252d": {"inputs": ["close"], "func": dstk_056_current_streak_loss_vs_worst_252d},
    "dstk_057_streak_severity_sum_21d": {"inputs": ["close"], "func": dstk_057_streak_severity_sum_21d},
    "dstk_058_streak_severity_sum_63d": {"inputs": ["close"], "func": dstk_058_streak_severity_sum_63d},
    "dstk_059_streak_severity_sum_252d": {"inputs": ["close"], "func": dstk_059_streak_severity_sum_252d},
    "dstk_060_avg_down_day_return_252d": {"inputs": ["close"], "func": dstk_060_avg_down_day_return_252d},
    "dstk_061_down_up_ratio_21d": {"inputs": ["close"], "func": dstk_061_down_up_ratio_21d},
    "dstk_062_down_up_ratio_63d": {"inputs": ["close"], "func": dstk_062_down_up_ratio_63d},
    "dstk_063_down_up_ratio_252d": {"inputs": ["close"], "func": dstk_063_down_up_ratio_252d},
    "dstk_064_no_green_day_5d_flag": {"inputs": ["close"], "func": dstk_064_no_green_day_5d_flag},
    "dstk_065_no_green_day_10d_flag": {"inputs": ["close"], "func": dstk_065_no_green_day_10d_flag},
    "dstk_066_no_green_day_21d_count": {"inputs": ["close"], "func": dstk_066_no_green_day_21d_count},
    "dstk_067_down_day_fraction_21d": {"inputs": ["close"], "func": dstk_067_down_day_fraction_21d},
    "dstk_068_down_day_fraction_63d": {"inputs": ["close"], "func": dstk_068_down_day_fraction_63d},
    "dstk_069_down_day_fraction_252d": {"inputs": ["close"], "func": dstk_069_down_day_fraction_252d},
    "dstk_070_consec_down_volume_days": {"inputs": ["close", "volume"], "func": dstk_070_consec_down_volume_days},
    "dstk_071_consec_up_volume_on_down_days": {"inputs": ["close", "volume"], "func": dstk_071_consec_up_volume_on_down_days},
    "dstk_072_gap_down_streak_current": {"inputs": ["close", "open"], "func": dstk_072_gap_down_streak_current},
    "dstk_073_max_gap_down_streak_63d": {"inputs": ["close", "open"], "func": dstk_073_max_gap_down_streak_63d},
    "dstk_074_avg_down_streak_length_252d": {"inputs": ["close"], "func": dstk_074_avg_down_streak_length_252d},
    "dstk_075_down_streak_freq_252d": {"inputs": ["close"], "func": dstk_075_down_streak_freq_252d},
}
