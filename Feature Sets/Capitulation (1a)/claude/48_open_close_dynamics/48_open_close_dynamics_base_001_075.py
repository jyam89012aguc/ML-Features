"""
48_open_close_dynamics — Base Features 001-075
Domain: open-to-close vs close-to-open session return decomposition — intraday vs overnight dynamics
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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


def _intraday_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log return from open to close (intraday session)."""
    return _log_safe(close) - _log_safe(open)


def _overnight_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log return from prior close to today's open (overnight session)."""
    return _log_safe(open) - _log_safe(close.shift(1))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Basic intraday return (open->close) ---

def ocd_001_intraday_log_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log return from open to close (intraday session return)."""
    return _intraday_ret(open, close)


def ocd_002_intraday_pct_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentage return from open to close."""
    return _safe_div(close - open, open)


def ocd_003_intraday_ret_abs(open: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of intraday log return."""
    return _intraday_ret(open, close).abs()


def ocd_004_intraday_ret_sign(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of intraday return: +1 if close > open, -1 if close < open, 0 otherwise."""
    r = _intraday_ret(open, close)
    return np.sign(r)


def ocd_005_intraday_loss_only(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday log return clamped to negative values only (0 on up days)."""
    r = _intraday_ret(open, close)
    return r.clip(upper=0.0)


def ocd_006_intraday_gain_only(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday log return clamped to positive values only (0 on down days)."""
    r = _intraday_ret(open, close)
    return r.clip(lower=0.0)


def ocd_007_intraday_ret_ewm5(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day EWM of intraday log return."""
    return _ewm_mean(_intraday_ret(open, close), _TD_WEEK)


def ocd_008_intraday_ret_ewm21(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EWM of intraday log return."""
    return _ewm_mean(_intraday_ret(open, close), _TD_MON)


def ocd_009_intraday_ret_zscore_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return relative to trailing 63-day distribution."""
    r = _intraday_ret(open, close)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


def ocd_010_intraday_ret_pct_rank_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's intraday return in trailing 63-day window."""
    r = _intraday_ret(open, close)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


# --- Group B (011-020): Basic overnight return (prior close->open) ---

def ocd_011_overnight_log_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log return from prior close to today's open (overnight session)."""
    return _overnight_ret(close, open)


def ocd_012_overnight_pct_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentage return from prior close to today's open."""
    return _safe_div(open - close.shift(1), close.shift(1))


def ocd_013_overnight_ret_abs(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute value of overnight log return."""
    return _overnight_ret(close, open).abs()


def ocd_014_overnight_ret_sign(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sign of overnight return: +1 if open > prior close, -1 otherwise."""
    r = _overnight_ret(close, open)
    return np.sign(r)


def ocd_015_overnight_loss_only(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight log return clamped to negative values (gap-down magnitude)."""
    r = _overnight_ret(close, open)
    return r.clip(upper=0.0)


def ocd_016_overnight_gain_only(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight log return clamped to positive values (gap-up magnitude)."""
    r = _overnight_ret(close, open)
    return r.clip(lower=0.0)


def ocd_017_overnight_ret_ewm5(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day EWM of overnight log return."""
    return _ewm_mean(_overnight_ret(close, open), _TD_WEEK)


def ocd_018_overnight_ret_ewm21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day EWM of overnight log return."""
    return _ewm_mean(_overnight_ret(close, open), _TD_MON)


def ocd_019_overnight_ret_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return relative to trailing 63-day distribution."""
    r = _overnight_ret(close, open)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


def ocd_020_overnight_ret_pct_rank_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return in trailing 63-day window."""
    r = _overnight_ret(close, open)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


# --- Group C (021-030): Session return ratios and decomposition ---

def ocd_021_intraday_vs_overnight_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of intraday return to overnight return (session dominance)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _safe_div(intra, over.abs() + _EPS)


def ocd_022_overnight_fraction_of_total_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight return as fraction of total daily log return."""
    total = _log_safe(close) - _log_safe(close.shift(1))
    over = _overnight_ret(close, open)
    return _safe_div(over, total.abs() + _EPS)


def ocd_023_intraday_fraction_of_total_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday return as fraction of total daily log return."""
    total = _log_safe(close) - _log_safe(close.shift(1))
    intra = _intraday_ret(open, close)
    return _safe_div(intra, total.abs() + _EPS)


def ocd_024_session_sign_agreement(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if intraday and overnight sessions have same sign, 0 otherwise."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return (np.sign(intra) == np.sign(over)).astype(float)


def ocd_025_both_sessions_negative(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if both intraday and overnight sessions are negative."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((intra < 0) & (over < 0)).astype(float)


def ocd_026_intraday_reverses_overnight_gain(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if overnight was positive but intraday was negative (reversal day)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over > 0) & (intra < 0)).astype(float)


def ocd_027_intraday_erases_overnight_loss(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if overnight negative but intraday positive (recovery from gap-down)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over < 0) & (intra > 0)).astype(float)


def ocd_028_intraday_amplifies_overnight_loss(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if both overnight and intraday are negative (compounding losses)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return ((over < 0) & (intra < 0)).astype(float)


def ocd_029_net_intraday_vs_overnight_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Difference: intraday log return minus overnight log return."""
    return _intraday_ret(open, close) - _overnight_ret(close, open)


def ocd_030_abs_intraday_minus_abs_overnight(close: pd.Series, open: pd.Series) -> pd.Series:
    """Abs intraday magnitude minus abs overnight magnitude (which session is larger)."""
    return _intraday_ret(open, close).abs() - _overnight_ret(close, open).abs()


# --- Group D (031-040): Rolling intraday return sums and averages ---

def ocd_031_intraday_ret_sum_5d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 5-day sum of intraday log returns."""
    return _rolling_sum(_intraday_ret(open, close), _TD_WEEK)


def ocd_032_intraday_ret_sum_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day sum of intraday log returns."""
    return _rolling_sum(_intraday_ret(open, close), _TD_MON)


def ocd_033_intraday_ret_sum_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of intraday log returns."""
    return _rolling_sum(_intraday_ret(open, close), _TD_QTR)


def ocd_034_intraday_ret_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of intraday log returns."""
    return _rolling_mean(_intraday_ret(open, close), _TD_MON)


def ocd_035_intraday_ret_mean_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day mean of intraday log returns."""
    return _rolling_mean(_intraday_ret(open, close), _TD_QTR)


def ocd_036_intraday_negative_ret_sum_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day sum of intraday losses only (negative intraday days)."""
    r = _intraday_ret(open, close)
    return _rolling_sum(r.clip(upper=0.0), _TD_MON)


def ocd_037_intraday_negative_ret_sum_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of intraday losses only."""
    r = _intraday_ret(open, close)
    return _rolling_sum(r.clip(upper=0.0), _TD_QTR)


def ocd_038_intraday_ret_std_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day standard deviation of intraday returns."""
    return _rolling_std(_intraday_ret(open, close), _TD_MON)


def ocd_039_intraday_ret_std_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of intraday returns."""
    return _rolling_std(_intraday_ret(open, close), _TD_QTR)


def ocd_040_intraday_down_day_fraction_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where intraday return was negative."""
    r = _intraday_ret(open, close)
    return _rolling_count_true(r < 0, _TD_MON) / _TD_MON


# --- Group E (041-050): Rolling overnight return sums and averages ---

def ocd_041_overnight_ret_sum_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 5-day sum of overnight log returns."""
    return _rolling_sum(_overnight_ret(close, open), _TD_WEEK)


def ocd_042_overnight_ret_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day sum of overnight log returns."""
    return _rolling_sum(_overnight_ret(close, open), _TD_MON)


def ocd_043_overnight_ret_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day sum of overnight log returns."""
    return _rolling_sum(_overnight_ret(close, open), _TD_QTR)


def ocd_044_overnight_ret_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day mean of overnight log returns."""
    return _rolling_mean(_overnight_ret(close, open), _TD_MON)


def ocd_045_overnight_ret_mean_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day mean of overnight log returns."""
    return _rolling_mean(_overnight_ret(close, open), _TD_QTR)


def ocd_046_overnight_negative_ret_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day sum of overnight losses only."""
    r = _overnight_ret(close, open)
    return _rolling_sum(r.clip(upper=0.0), _TD_MON)


def ocd_047_overnight_negative_ret_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day sum of overnight losses only."""
    r = _overnight_ret(close, open)
    return _rolling_sum(r.clip(upper=0.0), _TD_QTR)


def ocd_048_overnight_ret_std_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day standard deviation of overnight returns."""
    return _rolling_std(_overnight_ret(close, open), _TD_MON)


def ocd_049_overnight_ret_std_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of overnight returns."""
    return _rolling_std(_overnight_ret(close, open), _TD_QTR)


def ocd_050_overnight_down_day_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days where overnight return was negative."""
    r = _overnight_ret(close, open)
    return _rolling_count_true(r < 0, _TD_MON) / _TD_MON


# --- Group F (051-060): Consecutive session streaks ---

def ocd_051_consec_negative_intraday(open: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive days with negative intraday return (close < open)."""
    return _consec_streak(_intraday_ret(open, close) < 0)


def ocd_052_consec_negative_overnight(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive days with negative overnight return (open < prior close)."""
    return _consec_streak(_overnight_ret(close, open) < 0)


def ocd_053_consec_both_sessions_negative(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive days where both overnight and intraday are negative."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _consec_streak((intra < 0) & (over < 0))


def ocd_054_consec_intraday_reverses_overnight_gain(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current streak of days where intraday erases overnight gains."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _consec_streak((over > 0) & (intra < 0))


def ocd_055_max_negative_intraday_streak_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive negative-intraday-return days within trailing 21 days."""
    return _rolling_max_streak(_intraday_ret(open, close) < 0, _TD_MON)


def ocd_056_max_negative_intraday_streak_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive negative-intraday-return days within trailing 63 days."""
    return _rolling_max_streak(_intraday_ret(open, close) < 0, _TD_QTR)


def ocd_057_max_negative_overnight_streak_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Max consecutive negative-overnight-return days within trailing 21 days."""
    return _rolling_max_streak(_overnight_ret(close, open) < 0, _TD_MON)


def ocd_058_max_negative_overnight_streak_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Max consecutive negative-overnight-return days within trailing 63 days."""
    return _rolling_max_streak(_overnight_ret(close, open) < 0, _TD_QTR)


def ocd_059_consec_intraday_weaker_than_overnight(close: pd.Series, open: pd.Series) -> pd.Series:
    """Streak of days where intraday return is lower than overnight return."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _consec_streak(intra < over)


def ocd_060_consec_intraday_loss_sum_gt_overnight_gain(close: pd.Series, open: pd.Series) -> pd.Series:
    """Streak where intraday loss magnitude exceeds overnight gain magnitude."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _consec_streak((intra < 0) & (over > 0) & (intra.abs() > over.abs()))


# --- Group G (061-075): Volatility split and bearish structure ---

def ocd_061_intraday_vol_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday vol as fraction of total daily vol over 21 days."""
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_MON)
    total_std = _rolling_std(_log_safe(close) - _log_safe(close.shift(1)), _TD_MON)
    return _safe_div(intra_std, total_std + _EPS)


def ocd_062_overnight_vol_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight vol as fraction of total daily vol over 21 days."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_MON)
    total_std = _rolling_std(_log_safe(close) - _log_safe(close.shift(1)), _TD_MON)
    return _safe_div(over_std, total_std + _EPS)


def ocd_063_overnight_vs_intraday_vol_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight std to intraday std over trailing 21 days."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_MON)
    return _safe_div(over_std, intra_std)


def ocd_064_overnight_vs_intraday_vol_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight std to intraday std over trailing 63 days."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_QTR)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_QTR)
    return _safe_div(over_std, intra_std)


def ocd_065_full_bearish_day_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: 1 if open is day high AND close is day low (fully bearish candle)."""
    return ((open >= high) & (close <= low)).astype(float)


def ocd_066_full_bearish_day_count_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of fully bearish days (open=high, close=low) in trailing 21 days."""
    flag = ocd_065_full_bearish_day_flag(close, open, high, low)
    return _rolling_sum(flag, _TD_MON)


def ocd_067_full_bearish_day_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of fully bearish days in trailing 63 days."""
    flag = ocd_065_full_bearish_day_flag(close, open, high, low)
    return _rolling_sum(flag, _TD_QTR)


def ocd_068_open_is_high_flag(open: pd.Series, high: pd.Series) -> pd.Series:
    """Binary: 1 if open equals the day's high (all-day selling from the open)."""
    return (open >= high).astype(float)


def ocd_069_close_is_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: 1 if close equals the day's low (selling into close)."""
    return (close <= low).astype(float)


def ocd_070_open_is_high_fraction_21d(open: pd.Series, high: pd.Series) -> pd.Series:
    """Fraction of last 21 days where open was the high (bearish intraday structure)."""
    return _rolling_count_true(open >= high, _TD_MON) / _TD_MON


def ocd_071_close_is_low_fraction_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close was the low."""
    return _rolling_count_true(close <= low, _TD_MON) / _TD_MON


def ocd_072_intraday_giveback_of_overnight_gain_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean intraday return on days with positive overnight gap, trailing 21d."""
    over = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    intra_on_up_gap = intra.where(over > 0, np.nan)
    return intra_on_up_gap.rolling(_TD_MON, min_periods=1).mean()


def ocd_073_intraday_giveback_of_overnight_gain_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean intraday return on days with positive overnight gap, trailing 63d."""
    over = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    intra_on_up_gap = intra.where(over > 0, np.nan)
    return intra_on_up_gap.rolling(_TD_QTR, min_periods=1).mean()


def ocd_074_intraday_amplify_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where intraday amplified an overnight loss (both negative)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((intra < 0) & (over < 0), _TD_MON) / _TD_MON


def ocd_075_intraday_reversal_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where intraday reversed overnight direction."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    reversal = np.sign(intra) != np.sign(over)
    return _rolling_count_true(reversal, _TD_MON) / _TD_MON


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_REGISTRY_001_075 = {
    "ocd_001_intraday_log_ret": {"inputs": ["open", "close"], "func": ocd_001_intraday_log_ret},
    "ocd_002_intraday_pct_ret": {"inputs": ["open", "close"], "func": ocd_002_intraday_pct_ret},
    "ocd_003_intraday_ret_abs": {"inputs": ["open", "close"], "func": ocd_003_intraday_ret_abs},
    "ocd_004_intraday_ret_sign": {"inputs": ["open", "close"], "func": ocd_004_intraday_ret_sign},
    "ocd_005_intraday_loss_only": {"inputs": ["open", "close"], "func": ocd_005_intraday_loss_only},
    "ocd_006_intraday_gain_only": {"inputs": ["open", "close"], "func": ocd_006_intraday_gain_only},
    "ocd_007_intraday_ret_ewm5": {"inputs": ["open", "close"], "func": ocd_007_intraday_ret_ewm5},
    "ocd_008_intraday_ret_ewm21": {"inputs": ["open", "close"], "func": ocd_008_intraday_ret_ewm21},
    "ocd_009_intraday_ret_zscore_63d": {"inputs": ["open", "close"], "func": ocd_009_intraday_ret_zscore_63d},
    "ocd_010_intraday_ret_pct_rank_63d": {"inputs": ["open", "close"], "func": ocd_010_intraday_ret_pct_rank_63d},
    "ocd_011_overnight_log_ret": {"inputs": ["close", "open"], "func": ocd_011_overnight_log_ret},
    "ocd_012_overnight_pct_ret": {"inputs": ["close", "open"], "func": ocd_012_overnight_pct_ret},
    "ocd_013_overnight_ret_abs": {"inputs": ["close", "open"], "func": ocd_013_overnight_ret_abs},
    "ocd_014_overnight_ret_sign": {"inputs": ["close", "open"], "func": ocd_014_overnight_ret_sign},
    "ocd_015_overnight_loss_only": {"inputs": ["close", "open"], "func": ocd_015_overnight_loss_only},
    "ocd_016_overnight_gain_only": {"inputs": ["close", "open"], "func": ocd_016_overnight_gain_only},
    "ocd_017_overnight_ret_ewm5": {"inputs": ["close", "open"], "func": ocd_017_overnight_ret_ewm5},
    "ocd_018_overnight_ret_ewm21": {"inputs": ["close", "open"], "func": ocd_018_overnight_ret_ewm21},
    "ocd_019_overnight_ret_zscore_63d": {"inputs": ["close", "open"], "func": ocd_019_overnight_ret_zscore_63d},
    "ocd_020_overnight_ret_pct_rank_63d": {"inputs": ["close", "open"], "func": ocd_020_overnight_ret_pct_rank_63d},
    "ocd_021_intraday_vs_overnight_ratio": {"inputs": ["close", "open"], "func": ocd_021_intraday_vs_overnight_ratio},
    "ocd_022_overnight_fraction_of_total_ret": {"inputs": ["close", "open"], "func": ocd_022_overnight_fraction_of_total_ret},
    "ocd_023_intraday_fraction_of_total_ret": {"inputs": ["close", "open"], "func": ocd_023_intraday_fraction_of_total_ret},
    "ocd_024_session_sign_agreement": {"inputs": ["close", "open"], "func": ocd_024_session_sign_agreement},
    "ocd_025_both_sessions_negative": {"inputs": ["close", "open"], "func": ocd_025_both_sessions_negative},
    "ocd_026_intraday_reverses_overnight_gain": {"inputs": ["close", "open"], "func": ocd_026_intraday_reverses_overnight_gain},
    "ocd_027_intraday_erases_overnight_loss": {"inputs": ["close", "open"], "func": ocd_027_intraday_erases_overnight_loss},
    "ocd_028_intraday_amplifies_overnight_loss": {"inputs": ["close", "open"], "func": ocd_028_intraday_amplifies_overnight_loss},
    "ocd_029_net_intraday_vs_overnight_diff": {"inputs": ["close", "open"], "func": ocd_029_net_intraday_vs_overnight_diff},
    "ocd_030_abs_intraday_minus_abs_overnight": {"inputs": ["close", "open"], "func": ocd_030_abs_intraday_minus_abs_overnight},
    "ocd_031_intraday_ret_sum_5d": {"inputs": ["open", "close"], "func": ocd_031_intraday_ret_sum_5d},
    "ocd_032_intraday_ret_sum_21d": {"inputs": ["open", "close"], "func": ocd_032_intraday_ret_sum_21d},
    "ocd_033_intraday_ret_sum_63d": {"inputs": ["open", "close"], "func": ocd_033_intraday_ret_sum_63d},
    "ocd_034_intraday_ret_mean_21d": {"inputs": ["open", "close"], "func": ocd_034_intraday_ret_mean_21d},
    "ocd_035_intraday_ret_mean_63d": {"inputs": ["open", "close"], "func": ocd_035_intraday_ret_mean_63d},
    "ocd_036_intraday_negative_ret_sum_21d": {"inputs": ["open", "close"], "func": ocd_036_intraday_negative_ret_sum_21d},
    "ocd_037_intraday_negative_ret_sum_63d": {"inputs": ["open", "close"], "func": ocd_037_intraday_negative_ret_sum_63d},
    "ocd_038_intraday_ret_std_21d": {"inputs": ["open", "close"], "func": ocd_038_intraday_ret_std_21d},
    "ocd_039_intraday_ret_std_63d": {"inputs": ["open", "close"], "func": ocd_039_intraday_ret_std_63d},
    "ocd_040_intraday_down_day_fraction_21d": {"inputs": ["open", "close"], "func": ocd_040_intraday_down_day_fraction_21d},
    "ocd_041_overnight_ret_sum_5d": {"inputs": ["close", "open"], "func": ocd_041_overnight_ret_sum_5d},
    "ocd_042_overnight_ret_sum_21d": {"inputs": ["close", "open"], "func": ocd_042_overnight_ret_sum_21d},
    "ocd_043_overnight_ret_sum_63d": {"inputs": ["close", "open"], "func": ocd_043_overnight_ret_sum_63d},
    "ocd_044_overnight_ret_mean_21d": {"inputs": ["close", "open"], "func": ocd_044_overnight_ret_mean_21d},
    "ocd_045_overnight_ret_mean_63d": {"inputs": ["close", "open"], "func": ocd_045_overnight_ret_mean_63d},
    "ocd_046_overnight_negative_ret_sum_21d": {"inputs": ["close", "open"], "func": ocd_046_overnight_negative_ret_sum_21d},
    "ocd_047_overnight_negative_ret_sum_63d": {"inputs": ["close", "open"], "func": ocd_047_overnight_negative_ret_sum_63d},
    "ocd_048_overnight_ret_std_21d": {"inputs": ["close", "open"], "func": ocd_048_overnight_ret_std_21d},
    "ocd_049_overnight_ret_std_63d": {"inputs": ["close", "open"], "func": ocd_049_overnight_ret_std_63d},
    "ocd_050_overnight_down_day_fraction_21d": {"inputs": ["close", "open"], "func": ocd_050_overnight_down_day_fraction_21d},
    "ocd_051_consec_negative_intraday": {"inputs": ["open", "close"], "func": ocd_051_consec_negative_intraday},
    "ocd_052_consec_negative_overnight": {"inputs": ["close", "open"], "func": ocd_052_consec_negative_overnight},
    "ocd_053_consec_both_sessions_negative": {"inputs": ["close", "open"], "func": ocd_053_consec_both_sessions_negative},
    "ocd_054_consec_intraday_reverses_overnight_gain": {"inputs": ["close", "open"], "func": ocd_054_consec_intraday_reverses_overnight_gain},
    "ocd_055_max_negative_intraday_streak_21d": {"inputs": ["open", "close"], "func": ocd_055_max_negative_intraday_streak_21d},
    "ocd_056_max_negative_intraday_streak_63d": {"inputs": ["open", "close"], "func": ocd_056_max_negative_intraday_streak_63d},
    "ocd_057_max_negative_overnight_streak_21d": {"inputs": ["close", "open"], "func": ocd_057_max_negative_overnight_streak_21d},
    "ocd_058_max_negative_overnight_streak_63d": {"inputs": ["close", "open"], "func": ocd_058_max_negative_overnight_streak_63d},
    "ocd_059_consec_intraday_weaker_than_overnight": {"inputs": ["close", "open"], "func": ocd_059_consec_intraday_weaker_than_overnight},
    "ocd_060_consec_intraday_loss_sum_gt_overnight_gain": {"inputs": ["close", "open"], "func": ocd_060_consec_intraday_loss_sum_gt_overnight_gain},
    "ocd_061_intraday_vol_fraction_21d": {"inputs": ["close", "open"], "func": ocd_061_intraday_vol_fraction_21d},
    "ocd_062_overnight_vol_fraction_21d": {"inputs": ["close", "open"], "func": ocd_062_overnight_vol_fraction_21d},
    "ocd_063_overnight_vs_intraday_vol_ratio_21d": {"inputs": ["close", "open"], "func": ocd_063_overnight_vs_intraday_vol_ratio_21d},
    "ocd_064_overnight_vs_intraday_vol_ratio_63d": {"inputs": ["close", "open"], "func": ocd_064_overnight_vs_intraday_vol_ratio_63d},
    "ocd_065_full_bearish_day_flag": {"inputs": ["close", "open", "high", "low"], "func": ocd_065_full_bearish_day_flag},
    "ocd_066_full_bearish_day_count_21d": {"inputs": ["close", "open", "high", "low"], "func": ocd_066_full_bearish_day_count_21d},
    "ocd_067_full_bearish_day_count_63d": {"inputs": ["close", "open", "high", "low"], "func": ocd_067_full_bearish_day_count_63d},
    "ocd_068_open_is_high_flag": {"inputs": ["open", "high"], "func": ocd_068_open_is_high_flag},
    "ocd_069_close_is_low_flag": {"inputs": ["close", "low"], "func": ocd_069_close_is_low_flag},
    "ocd_070_open_is_high_fraction_21d": {"inputs": ["open", "high"], "func": ocd_070_open_is_high_fraction_21d},
    "ocd_071_close_is_low_fraction_21d": {"inputs": ["close", "low"], "func": ocd_071_close_is_low_fraction_21d},
    "ocd_072_intraday_giveback_of_overnight_gain_21d": {"inputs": ["close", "open"], "func": ocd_072_intraday_giveback_of_overnight_gain_21d},
    "ocd_073_intraday_giveback_of_overnight_gain_63d": {"inputs": ["close", "open"], "func": ocd_073_intraday_giveback_of_overnight_gain_63d},
    "ocd_074_intraday_amplify_fraction_21d": {"inputs": ["close", "open"], "func": ocd_074_intraday_amplify_fraction_21d},
    "ocd_075_intraday_reversal_fraction_21d": {"inputs": ["close", "open"], "func": ocd_075_intraday_reversal_fraction_21d},
}
