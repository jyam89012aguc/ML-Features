"""
06_low_proximity — Base Features 001-075
Domain: closeness to trailing minimum, new-low flags, and low-frequency behavior
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Anchors on the trailing LOW, not the high.
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-014): Distance above trailing rolling close-minimum ---

def lp_001_close_above_21d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 21-day trailing low (proximity to 1-month floor)."""
    m = _rolling_min(close, _TD_MON)
    return _safe_div(close - m, m)


def lp_002_close_above_63d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 63-day trailing low (proximity to 1-quarter floor)."""
    m = _rolling_min(close, _TD_QTR)
    return _safe_div(close - m, m)


def lp_003_close_above_126d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 126-day trailing low (half-year floor proximity)."""
    m = _rolling_min(close, _TD_HALF)
    return _safe_div(close - m, m)


def lp_004_close_above_252d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 252-day trailing low (1-year floor proximity)."""
    m = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - m, m)


def lp_005_close_above_504d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 504-day trailing low (2-year floor proximity)."""
    m = _rolling_min(close, 504)
    return _safe_div(close - m, m)


def lp_006_close_above_756d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 756-day trailing low (3-year floor proximity)."""
    m = _rolling_min(close, 756)
    return _safe_div(close - m, m)


def lp_007_close_above_1260d_min(close: pd.Series) -> pd.Series:
    """Percent close is above its 1260-day trailing low (5-year floor proximity)."""
    m = _rolling_min(close, 1260)
    return _safe_div(close - m, m)


def lp_008_close_above_expanding_min(close: pd.Series) -> pd.Series:
    """Percent close is above all-time expanding trailing low (ATL proximity)."""
    m = close.expanding(min_periods=1).min()
    return _safe_div(close - m, m)


def lp_009_log_close_above_252d_min(close: pd.Series) -> pd.Series:
    """Log-space distance of close above its 252-day low."""
    m = _rolling_min(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(m)


def lp_010_log_close_above_expanding_min(close: pd.Series) -> pd.Series:
    """Log-space distance of close above its all-time low."""
    m = close.expanding(min_periods=1).min()
    return _log_safe(close) - _log_safe(m)


def lp_011_low_above_252d_close_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low above 252-day close low (intraday proximity to floor)."""
    m = _rolling_min(close, _TD_YEAR)
    return _safe_div(low - m, m)


def lp_012_low_above_expanding_close_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low above all-time close low (all-time-low intraday brush)."""
    m = close.expanding(min_periods=1).min()
    return _safe_div(low - m, m)


def lp_013_low_above_252d_intraday_min(low: pd.Series) -> pd.Series:
    """Intraday low above 252-day trailing intraday low (true floor proximity)."""
    m = _rolling_min(low, _TD_YEAR)
    return _safe_div(low - m, m)


def lp_014_low_above_expanding_intraday_min(low: pd.Series) -> pd.Series:
    """Intraday low above all-time intraday low (deepest-ever-touch proximity)."""
    m = low.expanding(min_periods=1).min()
    return _safe_div(low - m, m)


# --- Group B (015-025): Is-at-new-low flags ---

def lp_015_is_21d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 21-day rolling minimum (new 1-month low)."""
    m = _rolling_min(close, _TD_MON)
    return (close <= m).astype(float)


def lp_016_is_63d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 63-day rolling minimum (new 1-quarter low)."""
    m = _rolling_min(close, _TD_QTR)
    return (close <= m).astype(float)


def lp_017_is_126d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 126-day rolling minimum (new half-year low)."""
    m = _rolling_min(close, _TD_HALF)
    return (close <= m).astype(float)


def lp_018_is_252d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 252-day rolling minimum (new 1-year low)."""
    m = _rolling_min(close, _TD_YEAR)
    return (close <= m).astype(float)


def lp_019_is_504d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 504-day rolling minimum (new 2-year low)."""
    m = _rolling_min(close, 504)
    return (close <= m).astype(float)


def lp_020_is_1260d_new_low_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its 1260-day rolling minimum (new 5-year low)."""
    m = _rolling_min(close, 1260)
    return (close <= m).astype(float)


def lp_021_is_atl_close(close: pd.Series) -> pd.Series:
    """Binary flag: close equals its all-time (expanding) minimum — ATL touch."""
    m = close.expanding(min_periods=1).min()
    return (close <= m).astype(float)


def lp_022_is_252d_new_low_intraday(low: pd.Series) -> pd.Series:
    """Binary flag: intraday low equals its 252-day rolling minimum."""
    m = _rolling_min(low, _TD_YEAR)
    return (low <= m).astype(float)


def lp_023_is_atl_intraday(low: pd.Series) -> pd.Series:
    """Binary flag: intraday low equals its all-time intraday minimum."""
    m = low.expanding(min_periods=1).min()
    return (low <= m).astype(float)


def lp_024_simultaneous_new_lows_score(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of timeframes setting a new low simultaneously (21/63/252/504/ATL) 0-5."""
    s = (
        (close <= _rolling_min(close, _TD_MON)).astype(float) +
        (close <= _rolling_min(close, _TD_QTR)).astype(float) +
        (close <= _rolling_min(close, _TD_YEAR)).astype(float) +
        (close <= _rolling_min(close, 504)).astype(float) +
        (close <= close.expanding(min_periods=1).min()).astype(float)
    )
    return s


def lp_025_new_low_cascade_score(close: pd.Series) -> pd.Series:
    """Score 0-7: count of windows (21/63/126/252/504/756/1260) where close is at new low."""
    windows = [_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR, 504, 756, 1260]
    s = sum((close <= _rolling_min(close, w)).astype(float) for w in windows)
    return s


# --- Group C (026-035): New-low count and frequency in a window ---

def lp_026_new_low_count_21d(close: pd.Series) -> pd.Series:
    """Count of days in last 21 days where close made a new 21-day low."""
    flag = (close <= _rolling_min(close, _TD_MON)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def lp_027_new_low_count_63d(close: pd.Series) -> pd.Series:
    """Count of days in last 63 days where close made a new 63-day low."""
    flag = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def lp_028_new_low_count_252d(close: pd.Series) -> pd.Series:
    """Count of days in last 252 days where close made a new 252-day low."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lp_029_new_low_freq_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close was at a 21-day new low."""
    flag = (close <= _rolling_min(close, _TD_MON)).astype(float)
    return _rolling_mean(flag, _TD_MON)


def lp_030_new_low_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close was at a 63-day new low."""
    flag = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    return _rolling_mean(flag, _TD_QTR)


def lp_031_new_low_freq_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was at a 252-day new low."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def lp_032_new_low_count_intraday_63d(low: pd.Series) -> pd.Series:
    """Count of days in last 63 days where intraday low made a new 63-day low."""
    flag = (low <= _rolling_min(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def lp_033_new_low_count_intraday_252d(low: pd.Series) -> pd.Series:
    """Count of days in last 252 days where intraday low made a new 252-day low."""
    flag = (low <= _rolling_min(low, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lp_034_expanding_new_low_count(close: pd.Series) -> pd.Series:
    """Cumulative count of all-time new closing lows over the full history."""
    atl = close.expanding(min_periods=1).min()
    flag = (close <= atl).astype(float)
    return flag.cumsum()


def lp_035_new_low_acceleration_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day new-low frequency to 63-day new-low frequency (recency tilt)."""
    freq21 = _rolling_mean((close <= _rolling_min(close, _TD_MON)).astype(float), _TD_MON)
    freq63 = _rolling_mean((close <= _rolling_min(close, _TD_QTR)).astype(float), _TD_QTR)
    return _safe_div(freq21, freq63)


# --- Group D (036-045): Days since the trailing minimum was set ---

def lp_036_days_since_21d_min(close: pd.Series) -> pd.Series:
    """Days since the 21-day trailing close low was last set."""
    idx = pd.Series(np.arange(len(close)), index=close.index)

    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return len(x) - 1 - pos

    return close.rolling(_TD_MON, min_periods=1).apply(_last_min_age, raw=True)


def lp_037_days_since_63d_min(close: pd.Series) -> pd.Series:
    """Days since the 63-day trailing close low was last set."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return len(x) - 1 - pos

    return close.rolling(_TD_QTR, min_periods=1).apply(_last_min_age, raw=True)


def lp_038_days_since_252d_min(close: pd.Series) -> pd.Series:
    """Days since the 252-day trailing close low was last set."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return len(x) - 1 - pos

    return close.rolling(_TD_YEAR, min_periods=1).apply(_last_min_age, raw=True)


def lp_039_days_since_504d_min(close: pd.Series) -> pd.Series:
    """Days since the 504-day trailing close low was last set."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return len(x) - 1 - pos

    return close.rolling(504, min_periods=1).apply(_last_min_age, raw=True)


def lp_040_days_since_intraday_252d_min(low: pd.Series) -> pd.Series:
    """Days since the 252-day intraday low was last set."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return len(x) - 1 - pos

    return low.rolling(_TD_YEAR, min_periods=1).apply(_last_min_age, raw=True)


def lp_041_recency_of_min_21d_norm(close: pd.Series) -> pd.Series:
    """Normalized recency: days_since_21d_min / 21 (0=just set, 1=set at window start)."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return (len(x) - 1 - pos) / max(1, len(x) - 1)

    return close.rolling(_TD_MON, min_periods=1).apply(_last_min_age, raw=True)


def lp_042_recency_of_min_252d_norm(close: pd.Series) -> pd.Series:
    """Normalized recency: days_since_252d_min / 252 (0=just set, 1=set at window start)."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = np.argmin(x)
        return (len(x) - 1 - pos) / max(1, len(x) - 1)

    return close.rolling(_TD_YEAR, min_periods=1).apply(_last_min_age, raw=True)


# --- Group E (043-052): Fraction of recent days within X% of trailing low ---

def lp_043_frac_within_2pct_of_252d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 2% above the 252-day low."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.02).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_044_frac_within_5pct_of_252d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 5% above the 252-day low."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.05).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_045_frac_within_10pct_of_252d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 10% above the 252-day low."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.10).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_046_frac_within_2pct_of_63d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close was within 2% above the 63-day low."""
    m = _rolling_min(close, _TD_QTR)
    near = (close <= m * 1.02).astype(float)
    return _rolling_mean(near, _TD_QTR)


def lp_047_frac_within_5pct_of_63d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close was within 5% above the 63-day low."""
    m = _rolling_min(close, _TD_QTR)
    near = (close <= m * 1.05).astype(float)
    return _rolling_mean(near, _TD_QTR)


def lp_048_frac_within_5pct_of_504d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days where close was within 5% above the 504-day low."""
    m = _rolling_min(close, 504)
    near = (close <= m * 1.05).astype(float)
    return _rolling_mean(near, 504)


def lp_049_frac_within_10pct_of_504d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days where close was within 10% above the 504-day low."""
    m = _rolling_min(close, 504)
    near = (close <= m * 1.10).astype(float)
    return _rolling_mean(near, 504)


def lp_050_frac_within_1pct_of_252d_min(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 1% above the 252-day low (tight floor hugging)."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.01).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_051_frac_within_2pct_of_atl(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 2% of the all-time expanding low."""
    m = close.expanding(min_periods=1).min()
    near = (close <= m * 1.02).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_052_frac_within_5pct_of_atl(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was within 5% of the all-time expanding low."""
    m = close.expanding(min_periods=1).min()
    near = (close <= m * 1.05).astype(float)
    return _rolling_mean(near, _TD_YEAR)


# --- Group F (053-062): Stochastic-style percentile rank near 0 ---

def lp_053_stoch_pct_21d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 21-day range (0=at low, 1=at high)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    return _safe_div(close - l, h - l)


def lp_054_stoch_pct_63d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 63-day range."""
    h = _rolling_max(close, _TD_QTR)
    l = _rolling_min(close, _TD_QTR)
    return _safe_div(close - l, h - l)


def lp_055_stoch_pct_126d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 126-day range."""
    h = _rolling_max(close, _TD_HALF)
    l = _rolling_min(close, _TD_HALF)
    return _safe_div(close - l, h - l)


def lp_056_stoch_pct_252d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 252-day range."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - l, h - l)


def lp_057_stoch_pct_504d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 504-day range."""
    h = _rolling_max(close, 504)
    l = _rolling_min(close, 504)
    return _safe_div(close - l, h - l)


def lp_058_stoch_pct_1260d(close: pd.Series) -> pd.Series:
    """Stochastic position of close within 1260-day range."""
    h = _rolling_max(close, 1260)
    l = _rolling_min(close, 1260)
    return _safe_div(close - l, h - l)


def lp_059_stoch_pct_expanding(close: pd.Series) -> pd.Series:
    """Stochastic position of close within all-time (expanding) range."""
    h = close.expanding(min_periods=1).max()
    l = close.expanding(min_periods=1).min()
    return _safe_div(close - l, h - l)


def lp_060_stoch_pct_intraday_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic position using 252-day intraday high/low range."""
    h = _rolling_max(high, _TD_YEAR)
    l = _rolling_min(low, _TD_YEAR)
    return _safe_div(close - l, h - l)


def lp_061_stoch_pct_smoothed_3d(close: pd.Series) -> pd.Series:
    """3-day smoothed Stochastic %K within 21-day range (slow stochastic at bottom)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    raw = _safe_div(close - l, h - l)
    return _rolling_mean(raw, 3)


def lp_062_stoch_low_indicator_252d(close: pd.Series) -> pd.Series:
    """1 minus stochastic 252d position: how far close is from the top of its range (high = near bottom)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return 1.0 - _safe_div(close - l, h - l)


# --- Group G (063-075): Consecutive new-low streaks, undercuts, clustering ---

def lp_063_consecutive_21d_new_lows(close: pd.Series) -> pd.Series:
    """Consecutive days close has been at or below its 21-day trailing minimum."""
    flag = (close <= _rolling_min(close, _TD_MON)).astype(int)
    result = flag.copy().astype(float)
    arr = flag.values
    streak = np.zeros(len(arr), dtype=float)
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt = 0
        streak[i] = cnt
    return pd.Series(streak, index=close.index)


def lp_064_consecutive_252d_new_lows(close: pd.Series) -> pd.Series:
    """Consecutive days close has been at or below its 252-day trailing minimum."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(int)
    arr = flag.values
    streak = np.zeros(len(arr), dtype=float)
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt = 0
        streak[i] = cnt
    return pd.Series(streak, index=close.index)


def lp_065_max_consecutive_252d_lows_63d(close: pd.Series) -> pd.Series:
    """Max consecutive 252d-new-low days within trailing 63-day window."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)

    def _max_streak(x):
        cnt = 0
        best = 0
        for v in x:
            if v == 1.0:
                cnt += 1
                if cnt > best:
                    best = cnt
            else:
                cnt = 0
        return float(best)

    return flag.rolling(_TD_QTR, min_periods=1).apply(_max_streak, raw=True)


def lp_066_undercut_depth_21d(close: pd.Series) -> pd.Series:
    """How much close undercuts the prior-21-day low (negative = new low depth)."""
    prior_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    return _safe_div(close - prior_min, prior_min)


def lp_067_undercut_depth_63d(close: pd.Series) -> pd.Series:
    """How much close undercuts the prior-63-day low."""
    prior_min = close.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return _safe_div(close - prior_min, prior_min)


def lp_068_undercut_depth_252d(close: pd.Series) -> pd.Series:
    """How much close undercuts the prior-252-day low (depth of capitulation undercut)."""
    prior_min = close.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return _safe_div(close - prior_min, prior_min)


def lp_069_low_cluster_density_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Density of intraday lows near the 21-day close low (fraction within 2%)."""
    m = _rolling_min(close, _TD_MON)
    near = (low <= m * 1.02).astype(float)
    return _rolling_mean(near, _TD_MON)


def lp_070_low_cluster_density_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Density of intraday lows near the 252-day close low (fraction within 2%)."""
    m = _rolling_min(close, _TD_YEAR)
    near = (low <= m * 1.02).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def lp_071_floor_touch_intensity_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Volume-unweighted floor-touch intensity: count of intraday low touches within 3% of 21d min per 21 days."""
    m = _rolling_min(close, _TD_MON)
    touch = (low <= m * 1.03).astype(float)
    return _rolling_sum(touch, _TD_MON)


def lp_072_floor_touch_intensity_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of intraday low touches within 3% of 63d min per 63 days."""
    m = _rolling_min(close, _TD_QTR)
    touch = (low <= m * 1.03).astype(float)
    return _rolling_sum(touch, _TD_QTR)


def lp_073_new_low_vol_premium_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on 252d new-low days relative to avg volume (capitulation volume signature)."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_ratio = _safe_div(volume, avg_vol)
    weighted = vol_ratio * flag
    total_flag = _rolling_sum(flag, _TD_YEAR).replace(0, np.nan)
    return _rolling_sum(weighted, _TD_YEAR) / total_flag


def lp_074_atr_dist_to_252d_min(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 252-day low expressed in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    m = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - m, atr)


def lp_075_composite_low_proximity_score(close: pd.Series) -> pd.Series:
    """Composite proximity score: equal-weight of stoch 21d, 63d, 252d positions (0=at floor)."""
    s21 = _safe_div(close - _rolling_min(close, _TD_MON),
                    _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON))
    s63 = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    s252 = _safe_div(close - _rolling_min(close, _TD_YEAR),
                     _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    return (s21.fillna(0.5) + s63.fillna(0.5) + s252.fillna(0.5)) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

LOW_PROXIMITY_REGISTRY_001_075 = {
    "lp_001_close_above_21d_min": {"inputs": ["close"], "func": lp_001_close_above_21d_min},
    "lp_002_close_above_63d_min": {"inputs": ["close"], "func": lp_002_close_above_63d_min},
    "lp_003_close_above_126d_min": {"inputs": ["close"], "func": lp_003_close_above_126d_min},
    "lp_004_close_above_252d_min": {"inputs": ["close"], "func": lp_004_close_above_252d_min},
    "lp_005_close_above_504d_min": {"inputs": ["close"], "func": lp_005_close_above_504d_min},
    "lp_006_close_above_756d_min": {"inputs": ["close"], "func": lp_006_close_above_756d_min},
    "lp_007_close_above_1260d_min": {"inputs": ["close"], "func": lp_007_close_above_1260d_min},
    "lp_008_close_above_expanding_min": {"inputs": ["close"], "func": lp_008_close_above_expanding_min},
    "lp_009_log_close_above_252d_min": {"inputs": ["close"], "func": lp_009_log_close_above_252d_min},
    "lp_010_log_close_above_expanding_min": {"inputs": ["close"], "func": lp_010_log_close_above_expanding_min},
    "lp_011_low_above_252d_close_min": {"inputs": ["close", "low"], "func": lp_011_low_above_252d_close_min},
    "lp_012_low_above_expanding_close_min": {"inputs": ["close", "low"], "func": lp_012_low_above_expanding_close_min},
    "lp_013_low_above_252d_intraday_min": {"inputs": ["low"], "func": lp_013_low_above_252d_intraday_min},
    "lp_014_low_above_expanding_intraday_min": {"inputs": ["low"], "func": lp_014_low_above_expanding_intraday_min},
    "lp_015_is_21d_new_low_close": {"inputs": ["close"], "func": lp_015_is_21d_new_low_close},
    "lp_016_is_63d_new_low_close": {"inputs": ["close"], "func": lp_016_is_63d_new_low_close},
    "lp_017_is_126d_new_low_close": {"inputs": ["close"], "func": lp_017_is_126d_new_low_close},
    "lp_018_is_252d_new_low_close": {"inputs": ["close"], "func": lp_018_is_252d_new_low_close},
    "lp_019_is_504d_new_low_close": {"inputs": ["close"], "func": lp_019_is_504d_new_low_close},
    "lp_020_is_1260d_new_low_close": {"inputs": ["close"], "func": lp_020_is_1260d_new_low_close},
    "lp_021_is_atl_close": {"inputs": ["close"], "func": lp_021_is_atl_close},
    "lp_022_is_252d_new_low_intraday": {"inputs": ["low"], "func": lp_022_is_252d_new_low_intraday},
    "lp_023_is_atl_intraday": {"inputs": ["low"], "func": lp_023_is_atl_intraday},
    "lp_024_simultaneous_new_lows_score": {"inputs": ["close", "low"], "func": lp_024_simultaneous_new_lows_score},
    "lp_025_new_low_cascade_score": {"inputs": ["close"], "func": lp_025_new_low_cascade_score},
    "lp_026_new_low_count_21d": {"inputs": ["close"], "func": lp_026_new_low_count_21d},
    "lp_027_new_low_count_63d": {"inputs": ["close"], "func": lp_027_new_low_count_63d},
    "lp_028_new_low_count_252d": {"inputs": ["close"], "func": lp_028_new_low_count_252d},
    "lp_029_new_low_freq_21d": {"inputs": ["close"], "func": lp_029_new_low_freq_21d},
    "lp_030_new_low_freq_63d": {"inputs": ["close"], "func": lp_030_new_low_freq_63d},
    "lp_031_new_low_freq_252d": {"inputs": ["close"], "func": lp_031_new_low_freq_252d},
    "lp_032_new_low_count_intraday_63d": {"inputs": ["low"], "func": lp_032_new_low_count_intraday_63d},
    "lp_033_new_low_count_intraday_252d": {"inputs": ["low"], "func": lp_033_new_low_count_intraday_252d},
    "lp_034_expanding_new_low_count": {"inputs": ["close"], "func": lp_034_expanding_new_low_count},
    "lp_035_new_low_acceleration_ratio": {"inputs": ["close"], "func": lp_035_new_low_acceleration_ratio},
    "lp_036_days_since_21d_min": {"inputs": ["close"], "func": lp_036_days_since_21d_min},
    "lp_037_days_since_63d_min": {"inputs": ["close"], "func": lp_037_days_since_63d_min},
    "lp_038_days_since_252d_min": {"inputs": ["close"], "func": lp_038_days_since_252d_min},
    "lp_039_days_since_504d_min": {"inputs": ["close"], "func": lp_039_days_since_504d_min},
    "lp_040_days_since_intraday_252d_min": {"inputs": ["low"], "func": lp_040_days_since_intraday_252d_min},
    "lp_041_recency_of_min_21d_norm": {"inputs": ["close"], "func": lp_041_recency_of_min_21d_norm},
    "lp_042_recency_of_min_252d_norm": {"inputs": ["close"], "func": lp_042_recency_of_min_252d_norm},
    "lp_043_frac_within_2pct_of_252d_min": {"inputs": ["close"], "func": lp_043_frac_within_2pct_of_252d_min},
    "lp_044_frac_within_5pct_of_252d_min": {"inputs": ["close"], "func": lp_044_frac_within_5pct_of_252d_min},
    "lp_045_frac_within_10pct_of_252d_min": {"inputs": ["close"], "func": lp_045_frac_within_10pct_of_252d_min},
    "lp_046_frac_within_2pct_of_63d_min": {"inputs": ["close"], "func": lp_046_frac_within_2pct_of_63d_min},
    "lp_047_frac_within_5pct_of_63d_min": {"inputs": ["close"], "func": lp_047_frac_within_5pct_of_63d_min},
    "lp_048_frac_within_5pct_of_504d_min": {"inputs": ["close"], "func": lp_048_frac_within_5pct_of_504d_min},
    "lp_049_frac_within_10pct_of_504d_min": {"inputs": ["close"], "func": lp_049_frac_within_10pct_of_504d_min},
    "lp_050_frac_within_1pct_of_252d_min": {"inputs": ["close"], "func": lp_050_frac_within_1pct_of_252d_min},
    "lp_051_frac_within_2pct_of_atl": {"inputs": ["close"], "func": lp_051_frac_within_2pct_of_atl},
    "lp_052_frac_within_5pct_of_atl": {"inputs": ["close"], "func": lp_052_frac_within_5pct_of_atl},
    "lp_053_stoch_pct_21d": {"inputs": ["close"], "func": lp_053_stoch_pct_21d},
    "lp_054_stoch_pct_63d": {"inputs": ["close"], "func": lp_054_stoch_pct_63d},
    "lp_055_stoch_pct_126d": {"inputs": ["close"], "func": lp_055_stoch_pct_126d},
    "lp_056_stoch_pct_252d": {"inputs": ["close"], "func": lp_056_stoch_pct_252d},
    "lp_057_stoch_pct_504d": {"inputs": ["close"], "func": lp_057_stoch_pct_504d},
    "lp_058_stoch_pct_1260d": {"inputs": ["close"], "func": lp_058_stoch_pct_1260d},
    "lp_059_stoch_pct_expanding": {"inputs": ["close"], "func": lp_059_stoch_pct_expanding},
    "lp_060_stoch_pct_intraday_252d": {"inputs": ["high", "low", "close"], "func": lp_060_stoch_pct_intraday_252d},
    "lp_061_stoch_pct_smoothed_3d": {"inputs": ["close"], "func": lp_061_stoch_pct_smoothed_3d},
    "lp_062_stoch_low_indicator_252d": {"inputs": ["close"], "func": lp_062_stoch_low_indicator_252d},
    "lp_063_consecutive_21d_new_lows": {"inputs": ["close"], "func": lp_063_consecutive_21d_new_lows},
    "lp_064_consecutive_252d_new_lows": {"inputs": ["close"], "func": lp_064_consecutive_252d_new_lows},
    "lp_065_max_consecutive_252d_lows_63d": {"inputs": ["close"], "func": lp_065_max_consecutive_252d_lows_63d},
    "lp_066_undercut_depth_21d": {"inputs": ["close"], "func": lp_066_undercut_depth_21d},
    "lp_067_undercut_depth_63d": {"inputs": ["close"], "func": lp_067_undercut_depth_63d},
    "lp_068_undercut_depth_252d": {"inputs": ["close"], "func": lp_068_undercut_depth_252d},
    "lp_069_low_cluster_density_21d": {"inputs": ["close", "low"], "func": lp_069_low_cluster_density_21d},
    "lp_070_low_cluster_density_252d": {"inputs": ["close", "low"], "func": lp_070_low_cluster_density_252d},
    "lp_071_floor_touch_intensity_21d": {"inputs": ["close", "low"], "func": lp_071_floor_touch_intensity_21d},
    "lp_072_floor_touch_intensity_63d": {"inputs": ["close", "low"], "func": lp_072_floor_touch_intensity_63d},
    "lp_073_new_low_vol_premium_252d": {"inputs": ["close", "volume"], "func": lp_073_new_low_vol_premium_252d},
    "lp_074_atr_dist_to_252d_min": {"inputs": ["close", "high", "low"], "func": lp_074_atr_dist_to_252d_min},
    "lp_075_composite_low_proximity_score": {"inputs": ["close"], "func": lp_075_composite_low_proximity_score},
}
