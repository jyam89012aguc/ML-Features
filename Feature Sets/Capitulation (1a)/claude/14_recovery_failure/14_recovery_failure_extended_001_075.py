"""
14_recovery_failure — Extended Features 001-075
Domain: failed recovery — extended variants including open-gap recovery failure,
        high-based bounce ratios at additional window lengths, rally failure z-scores,
        retracement fraction percentile ranks, volume-weighted bounce quality, EWM-smoothed
        failure metrics, cross-horizon lower-high composites, and capitulation recovery scores.
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
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
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
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
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
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _local_peak(s: pd.Series, lookback: int) -> pd.Series:
    return s.shift(1).rolling(lookback, min_periods=max(1, lookback // 2)).max()


def _local_trough(s: pd.Series, lookback: int) -> pd.Series:
    return s.shift(1).rolling(lookback, min_periods=max(1, lookback // 2)).min()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Open-price and gap-based bounce failure metrics ---

def rfl_ext_001_open_gap_up_5d(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day return from yesterday's close to today's open (gap-up component of bounce)."""
    return _safe_div(open - close.shift(1), close.shift(1))


def rfl_ext_002_open_vs_5d_prior_close(open: pd.Series, close: pd.Series) -> pd.Series:
    """Open price relative to close 5 days ago (bounce from 5d prior trough)."""
    return _safe_div(open - close.shift(_TD_WEEK), close.shift(_TD_WEEK))


def rfl_ext_003_close_vs_open_daily(open: pd.Series, close: pd.Series) -> pd.Series:
    """Daily close-to-open return (intraday follow-through of bounce)."""
    return _safe_div(close - open, open)


def rfl_ext_004_open_above_prior_close_streak(open: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days where open > prior close (gap-up or flat-open streak)."""
    return _consec_streak(open > close.shift(1))


def rfl_ext_005_open_gap_fail_count_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 'open gap-up then close lower than open' days in 21 days (intraday fade)."""
    gap_up = (open > close.shift(1)).astype(float)
    fade   = (close < open).astype(float)
    fail   = gap_up * fade
    return _rolling_sum(fail, _TD_MON)


def rfl_ext_006_open_gap_fail_fraction_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of open-gap-up days that closed below open in trailing 63 days."""
    gap_up = (open > close.shift(1)).astype(float)
    fade   = (close < open).astype(float)
    fail   = gap_up * fade
    gap_up_sum = _rolling_sum(gap_up, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(fail, _TD_QTR), gap_up_sum)


def rfl_ext_007_close_vs_prior_open_21d_bounce(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day bounce: close vs open 21 days ago (open-anchored monthly bounce)."""
    return _safe_div(close - open.shift(_TD_MON), open.shift(_TD_MON))


def rfl_ext_008_open_retracement_vs_prior_down_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Open-price-based 21d bounce / prior 21d decline (open retracement fraction)."""
    bounce = _safe_div(open - open.shift(_TD_MON), open.shift(_TD_MON))
    prior  = _safe_div(open.shift(_TD_MON) - open.shift(42), open.shift(42))
    prior_decline = (-prior).clip(lower=_EPS)
    return _safe_div(bounce, prior_decline)


def rfl_ext_009_high_vs_open_21d_range(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day high-to-open as fraction of 21d range (upper-shadow bounce quality)."""
    rng = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    upper_shadow = high - open
    return _safe_div(_rolling_mean(upper_shadow, _TD_WEEK), rng.replace(0, np.nan))


def rfl_ext_010_open_above_5d_max_high_flag(open: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: today's open exceeds the 5-day prior rolling max high (breakout gap attempt)."""
    prior_max_high = _local_peak(high, _TD_WEEK)
    return (open > prior_max_high).astype(float)


def rfl_ext_011_open_close_recovery_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 21 days where close > open (positive intraday days — recovery participation)."""
    return _rolling_count_true(close > open, _TD_MON) / _TD_MON


def rfl_ext_012_open_close_recovery_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63 days where close > open (positive intraday days)."""
    return _rolling_count_true(close > open, _TD_QTR) / _TD_QTR


# --- Group B (013-022): Extended retracement ratio variants ---

def rfl_ext_013_bounce_retracement_ratio_10d(close: pd.Series) -> pd.Series:
    """10-day bounce / prior 10-day decline (retracement fraction at 2-week horizon)."""
    bounce = close.pct_change(10)
    prior  = _safe_div(close.shift(10) - close.shift(20), close.shift(20))
    decline = (-prior).clip(lower=_EPS)
    return _safe_div(bounce, decline)


def rfl_ext_014_bounce_retracement_ratio_63d(close: pd.Series) -> pd.Series:
    """63-day bounce / prior 63-day decline (quarterly retracement)."""
    bounce = close.pct_change(_TD_QTR)
    prior  = _safe_div(close.shift(_TD_QTR) - close.shift(_TD_HALF), close.shift(_TD_HALF))
    decline = (-prior).clip(lower=_EPS)
    return _safe_div(bounce, decline)


def rfl_ext_015_bounce_vs_21d_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day bounce normalized by 21-day ATR (vol-adjusted bounce size)."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_MON)
    bounce = close - close.shift(_TD_WEEK)
    return _safe_div(bounce, atr)


def rfl_ext_016_bounce_vs_63d_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day bounce normalized by 63-day ATR."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_QTR)
    bounce = close - close.shift(_TD_MON)
    return _safe_div(bounce, atr)


def rfl_ext_017_bounce_ret_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day return within 252-day history."""
    ret5 = close.pct_change(_TD_WEEK)
    return ret5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_018_bounce_ret_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day return within 252-day history."""
    ret21 = close.pct_change(_TD_MON)
    return ret21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_019_bounce_retracement_ratio_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d retracement ratio within 252-day history."""
    bounce  = close.pct_change(_TD_WEEK)
    prior   = _safe_div(close.shift(_TD_WEEK) - close.shift(10), close.shift(10))
    decline = (-prior).clip(lower=_EPS)
    ratio   = _safe_div(bounce, decline)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_020_bounce_retracement_ratio_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 21d retracement fraction."""
    bounce  = close.pct_change(_TD_MON)
    prior   = _safe_div(close.shift(_TD_MON) - close.shift(42), close.shift(42))
    decline = (-prior).clip(lower=_EPS)
    ratio   = _safe_div(bounce, decline)
    return _zscore_rolling(ratio, _TD_YEAR)


def rfl_ext_021_bounce_vs_prior_peak_252d(close: pd.Series) -> pd.Series:
    """Current close relative to 252-day prior rolling peak (very-long-term lower-high)."""
    peak = _local_peak(close, _TD_YEAR)
    return _safe_div(close - peak, peak)


def rfl_ext_022_bounce_vs_prior_trough_21d(close: pd.Series) -> pd.Series:
    """Current close relative to prior 21-day trough (bounce from recent trough)."""
    trough = _local_trough(close, _TD_MON)
    return _safe_div(close - trough, trough.abs().replace(0, np.nan))


# --- Group C (023-032): Lower-high on high/open at additional horizons ---

def rfl_ext_023_high_vs_prior_high_63d_zscore(high: pd.Series) -> pd.Series:
    """Z-score (252d) of current high relative to prior 63-day high."""
    ratio = _safe_div(high - _local_peak(high, _TD_QTR), _local_peak(high, _TD_QTR))
    return _zscore_rolling(ratio, _TD_YEAR)


def rfl_ext_024_high_vs_prior_high_126d(high: pd.Series) -> pd.Series:
    """Today's high relative to the highest high over the prior 126 days."""
    prior_high = _local_peak(high, _TD_HALF)
    return _safe_div(high - prior_high, prior_high)


def rfl_ext_025_lower_high_count_126d(high: pd.Series) -> pd.Series:
    """Count of lower-high days in last 126 days."""
    return _rolling_count_true(high < high.shift(1), _TD_HALF)


def rfl_ext_026_lower_high_fraction_126d(high: pd.Series) -> pd.Series:
    """Fraction of last 126 days with a lower daily high."""
    return _rolling_count_true(high < high.shift(1), _TD_HALF) / _TD_HALF


def rfl_ext_027_lower_high_fraction_21d_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score (252d) of 21d lower-high fraction."""
    frac = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    return _zscore_rolling(frac, _TD_YEAR)


def rfl_ext_028_lower_high_fraction_63d_pct_rank_252d(high: pd.Series) -> pd.Series:
    """Percentile rank of 63d lower-high fraction within 252-day history."""
    frac = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_029_consec_lower_highs_21d_max(high: pd.Series) -> pd.Series:
    """Maximum consecutive-lower-high streak within trailing 21 days."""
    return _rolling_max_streak(high < high.shift(1), _TD_MON)


def rfl_ext_030_consec_lower_highs_63d_max(high: pd.Series) -> pd.Series:
    """Maximum consecutive-lower-high streak within trailing 63 days."""
    return _rolling_max_streak(high < high.shift(1), _TD_QTR)


def rfl_ext_031_open_vs_prior_open_lower_count_21d(open: pd.Series) -> pd.Series:
    """Count of lower-open days in trailing 21 days."""
    return _rolling_count_true(open < open.shift(1), _TD_MON)


def rfl_ext_032_open_vs_prior_open_lower_fraction_63d(open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where today's open < prior day's open."""
    return _rolling_count_true(open < open.shift(1), _TD_QTR) / _TD_QTR


# --- Group D (033-042): Rally-fail counting and z-scores ---

def rfl_ext_033_rally_fail_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of up-days followed by a down-day within 21 days."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    fail_sum = _rolling_sum(fail, _TD_MON)
    up_sum   = _rolling_sum(up.shift(1), _TD_MON).replace(0, np.nan)
    return _safe_div(fail_sum, up_sum)


def rfl_ext_034_rally_fail_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of up-days followed by a down-day within 63 days."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    fail_sum = _rolling_sum(fail, _TD_QTR)
    up_sum   = _rolling_sum(up.shift(1), _TD_QTR).replace(0, np.nan)
    return _safe_div(fail_sum, up_sum)


def rfl_ext_035_rally_fail_count_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of 21d rally-fail count."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    cnt  = _rolling_sum(fail, _TD_MON)
    return _zscore_rolling(cnt, _TD_YEAR)


def rfl_ext_036_three_day_rally_fail_count_21d(close: pd.Series) -> pd.Series:
    """Count of 3-day rallies (3 consecutive up-days) immediately followed by a down-day in 21d."""
    up   = (close > close.shift(1)).astype(float)
    three_up = (up * up.shift(1) * up.shift(2))
    down_next = (close.shift(1) > close).astype(float)
    fail = three_up.shift(1) * down_next
    return _rolling_sum(fail, _TD_MON)


def rfl_ext_037_two_day_rally_fail_count_63d(close: pd.Series) -> pd.Series:
    """Count of 2-day rallies immediately followed by a down-day in 63 days."""
    up   = (close > close.shift(1)).astype(float)
    two_up = up * up.shift(1)
    down_next = (close.shift(1) > close).astype(float)
    fail = two_up.shift(1) * down_next
    return _rolling_sum(fail, _TD_QTR)


def rfl_ext_038_rally_then_new_low_count_63d(close: pd.Series) -> pd.Series:
    """Count of up-days followed by a close at a new 21d low in 63 days."""
    up       = (close > close.shift(1)).astype(float)
    new_low  = (close == _rolling_min(close, _TD_MON)).astype(float)
    fail     = up.shift(1) * new_low
    return _rolling_sum(fail, _TD_QTR)


def rfl_ext_039_avg_bounce_before_fail_21d(close: pd.Series) -> pd.Series:
    """Average magnitude of up-day returns that are then followed by a down day (21d)."""
    ret  = close.pct_change(1)
    up   = (ret > 0).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    bounce_mag = (ret.shift(1) * fail)
    fail_sum   = _rolling_sum(fail, _TD_MON).replace(0, np.nan)
    return _safe_div(_rolling_sum(bounce_mag, _TD_MON), fail_sum)


def rfl_ext_040_rally_fail_fraction_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d rally-fail fraction within 252-day history."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    fail_sum = _rolling_sum(fail, _TD_MON)
    up_sum   = _rolling_sum(up.shift(1), _TD_MON).replace(0, np.nan)
    frac = _safe_div(fail_sum, up_sum)
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_041_net_up_vs_down_count_21d(close: pd.Series) -> pd.Series:
    """Net count (up-days minus down-days) in trailing 21 days."""
    up   = _rolling_count_true(close > close.shift(1), _TD_MON)
    down = _rolling_count_true(close < close.shift(1), _TD_MON)
    return up - down


def rfl_ext_042_net_up_vs_down_count_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of net up-minus-down count in 63 days."""
    up   = _rolling_count_true(close > close.shift(1), _TD_QTR)
    down = _rolling_count_true(close < close.shift(1), _TD_QTR)
    net  = up - down
    return _zscore_rolling(net, _TD_YEAR)


# --- Group E (043-052): Volume-weighted bounce quality ---

def rfl_ext_043_vol_on_up_days_vs_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average volume on up-days to average volume on down-days over 21 days."""
    up   = (close > close.shift(1)).astype(float)
    down = (close < close.shift(1)).astype(float)
    up_vol   = _safe_div(_rolling_sum(up * volume, _TD_MON),
                         _rolling_sum(up, _TD_MON).replace(0, np.nan))
    down_vol = _safe_div(_rolling_sum(down * volume, _TD_MON),
                         _rolling_sum(down, _TD_MON).replace(0, np.nan))
    return _safe_div(up_vol, down_vol)


def rfl_ext_044_vol_on_up_days_vs_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average volume on up-days to average volume on down-days over 63 days."""
    up   = (close > close.shift(1)).astype(float)
    down = (close < close.shift(1)).astype(float)
    up_vol   = _safe_div(_rolling_sum(up * volume, _TD_QTR),
                         _rolling_sum(up, _TD_QTR).replace(0, np.nan))
    down_vol = _safe_div(_rolling_sum(down * volume, _TD_QTR),
                         _rolling_sum(down, _TD_QTR).replace(0, np.nan))
    return _safe_div(up_vol, down_vol)


def rfl_ext_045_bounce_volume_ratio_5d_vs_decline_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day average volume to prior 21-day average volume (bounce volume vs prior trend)."""
    vol5  = _rolling_mean(volume, _TD_WEEK)
    vol21 = _rolling_mean(volume.shift(_TD_WEEK), _TD_MON)
    return _safe_div(vol5, vol21)


def rfl_ext_046_vol_weighted_bounce_ret_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 5-day bounce: sum(ret * vol) over 5d / sum(vol) over 5d."""
    ret = close.diff(1) / close.shift(1).replace(0, np.nan)
    return _safe_div(_rolling_sum(ret * volume, _TD_WEEK),
                     _rolling_sum(volume, _TD_WEEK))


def rfl_ext_047_vol_weighted_bounce_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21-day bounce: sum(ret * vol) / sum(vol) over 21 days."""
    ret = close.diff(1) / close.shift(1).replace(0, np.nan)
    return _safe_div(_rolling_sum(ret * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON))


def rfl_ext_048_vol_on_rally_fail_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on rally-fail days relative to 21d mean volume."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = up.shift(1) * down
    mean_vol = _rolling_mean(volume, _TD_MON).replace(0, np.nan)
    return _safe_div(_rolling_sum(fail * volume, _TD_MON),
                     _rolling_sum(fail, _TD_MON).replace(0, np.nan)) / mean_vol


def rfl_ext_049_vol_ratio_up_day_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of 21d up-day/down-day volume ratio."""
    up   = (close > close.shift(1)).astype(float)
    down = (close < close.shift(1)).astype(float)
    up_vol   = _safe_div(_rolling_sum(up * volume, _TD_MON),
                         _rolling_sum(up, _TD_MON).replace(0, np.nan))
    down_vol = _safe_div(_rolling_sum(down * volume, _TD_MON),
                         _rolling_sum(down, _TD_MON).replace(0, np.nan))
    ratio = _safe_div(up_vol, down_vol)
    return _zscore_rolling(ratio, _TD_YEAR)


def rfl_ext_050_vol_weighted_lower_high_fraction_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted lower-high fraction: sum(vol on lower-high days) / total 63d volume."""
    lower_h = (high < high.shift(1)).astype(float)
    return _safe_div(_rolling_sum(lower_h * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR))


# --- Group F (051-060): EWM-smoothed and additional recovery structure ---

def rfl_ext_051_ewm_bounce_ret_21d_span5(close: pd.Series) -> pd.Series:
    """EWM(span=5) of daily returns: short-term momentum smoothing for bounce quality."""
    ret = close.pct_change(1)
    return _ewm_mean(ret, _TD_WEEK)


def rfl_ext_052_ewm_bounce_ret_21d_span21(close: pd.Series) -> pd.Series:
    """EWM(span=21) of daily returns: monthly momentum smoothing."""
    ret = close.pct_change(1)
    return _ewm_mean(ret, _TD_MON)


def rfl_ext_053_bounce_vs_peak_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of current close relative to 21-day prior rolling peak."""
    peak  = _local_peak(close, _TD_MON)
    ratio = _safe_div(close - peak, peak)
    return _zscore_rolling(ratio, _TD_YEAR)


def rfl_ext_054_high_vs_prior_high_21d_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score (252d) of (high - prior 21d high) / prior 21d high."""
    ratio = _safe_div(high - _local_peak(high, _TD_MON), _local_peak(high, _TD_MON))
    return _zscore_rolling(ratio, _TD_YEAR)


def rfl_ext_055_peak_drawdown_from_63d_peak_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of drawdown from 63-day peak (failed-bounce depth)."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    return _zscore_rolling(dd, _TD_YEAR)


def rfl_ext_056_up_day_fraction_21d_ewm_span21(close: pd.Series) -> pd.Series:
    """EWM(span=21) of daily up-day indicator (smoothed up-day frequency)."""
    up = (close > close.shift(1)).astype(float)
    return _ewm_mean(up, _TD_MON)


def rfl_ext_057_rally_fail_consec_streak(close: pd.Series) -> pd.Series:
    """Consecutive days where each up-day was followed by a down-day (streak)."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail = (up.shift(1) * down) == 1.0
    return _consec_streak(fail)


def rfl_ext_058_down_after_up_retracement_21d_mean(close: pd.Series) -> pd.Series:
    """Mean of down-day returns (when preceded by an up-day) over 21 days — typical fade."""
    ret  = close.pct_change(1)
    up   = (ret.shift(1) > 0).astype(float)
    down_ret = ret * (ret < 0).astype(float) * up
    cnt  = _rolling_sum((down_ret != 0).astype(float), _TD_MON).replace(0, np.nan)
    return _safe_div(_rolling_sum(down_ret, _TD_MON), cnt)


def rfl_ext_059_max_up_streak_126d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-day streak within trailing 126 days."""
    return _rolling_max_streak(close > close.shift(1), _TD_HALF)


def rfl_ext_060_up_day_count_126d(close: pd.Series) -> pd.Series:
    """Count of up-days in last 126 days."""
    return _rolling_count_true(close > close.shift(1), _TD_HALF)


# --- Group G (061-068): Recovery failure from low-price anchors ---

def rfl_ext_061_low_vs_prior_low_21d(low: pd.Series) -> pd.Series:
    """Today's low relative to the lowest low over the prior 21 days (lower-low signal)."""
    prior_low = _local_trough(low, _TD_MON)
    return _safe_div(low - prior_low, prior_low.abs().replace(0, np.nan))


def rfl_ext_062_low_vs_prior_low_63d(low: pd.Series) -> pd.Series:
    """Today's low relative to the lowest low over the prior 63 days."""
    prior_low = _local_trough(low, _TD_QTR)
    return _safe_div(low - prior_low, prior_low.abs().replace(0, np.nan))


def rfl_ext_063_lower_low_count_21d(low: pd.Series) -> pd.Series:
    """Count of lower-low days in last 21 days."""
    return _rolling_count_true(low < low.shift(1), _TD_MON)


def rfl_ext_064_lower_low_count_63d(low: pd.Series) -> pd.Series:
    """Count of lower-low days in last 63 days."""
    return _rolling_count_true(low < low.shift(1), _TD_QTR)


def rfl_ext_065_lower_low_fraction_21d(low: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a lower daily low."""
    return _rolling_count_true(low < low.shift(1), _TD_MON) / _TD_MON


def rfl_ext_066_lower_low_fraction_63d_pct_rank_252d(low: pd.Series) -> pd.Series:
    """Percentile rank of 63d lower-low fraction within 252-day history."""
    frac = _rolling_count_true(low < low.shift(1), _TD_QTR) / _TD_QTR
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_ext_067_low_above_prior_low_streak(low: pd.Series) -> pd.Series:
    """Consecutive days where today's low is above prior day's low (recovery of lows)."""
    return _consec_streak(low > low.shift(1))


def rfl_ext_068_high_above_prior_high_streak(high: pd.Series) -> pd.Series:
    """Consecutive days where today's high is above prior day's high (higher-high streak)."""
    return _consec_streak(high > high.shift(1))


# --- Group H (069-075): Composites and capitulation recovery signals ---

def rfl_ext_069_composite_lower_high_lower_low_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Combined lower-high AND lower-low fraction over 63 days (simultaneous structure failure)."""
    lh = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    ll = _rolling_count_true(low < low.shift(1), _TD_QTR) / _TD_QTR
    return (lh + ll) / 2.0


def rfl_ext_070_recovery_failure_score_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Recovery failure score: pct-rank(rally-fail-fraction) + pct-rank(lower-high-fraction)
    within 252d, averaged. Higher = more persistent failure to recover."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    fail_frac = _safe_div(_rolling_sum(up.shift(1) * down, _TD_MON),
                          _rolling_sum(up.shift(1), _TD_MON).replace(0, np.nan))
    lh_frac   = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    r_ff = fail_frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r_lh = lh_frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    return (r_ff + r_lh) / 2.0


def rfl_ext_071_retracement_ratio_5d_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM(21d) of 5d retracement ratio (smoothed recent bounce quality)."""
    bounce  = close.pct_change(_TD_WEEK)
    prior   = _safe_div(close.shift(_TD_WEEK) - close.shift(10), close.shift(10))
    decline = (-prior).clip(lower=_EPS)
    ratio   = _safe_div(bounce, decline)
    return _ewm_mean(ratio, _TD_MON)


def rfl_ext_072_max_bounce_5d_in_63d_vs_mean_bounce(close: pd.Series) -> pd.Series:
    """Ratio of max 5d-return within 63 days to mean positive 5d-return over 63 days
    (concentration of bounce in single event vs distributed recovery)."""
    ret5 = close.pct_change(_TD_WEEK)
    max_ret = _rolling_max(ret5, _TD_QTR)
    mean_pos = ret5.clip(lower=0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(max_ret, mean_pos.replace(0, np.nan))


def rfl_ext_073_up_day_fraction_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score (252d) of up-day fraction over trailing 63 days."""
    frac = _rolling_count_true(close > close.shift(1), _TD_QTR) / _TD_QTR
    return _zscore_rolling(frac, _TD_YEAR)


def rfl_ext_074_lower_high_lower_low_composite_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score (252d) of combined lower-high-and-lower-low fraction over 63 days."""
    lh = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    ll = _rolling_count_true(low < low.shift(1), _TD_QTR) / _TD_QTR
    combo = (lh + ll) / 2.0
    return _zscore_rolling(combo, _TD_YEAR)


def rfl_ext_075_capitulation_recovery_failure_score(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation recovery failure composite: avg of pct-rank(rally-fail-fraction-21d),
    pct-rank(lower-high-fraction-63d), pct-rank(1-minus-up/down-volume-ratio-21d)
    within 252d. Higher = more persistent, volume-confirmed recovery failure."""
    up   = (close > close.shift(1)).astype(float)
    down = (close.shift(1) > close).astype(float)
    ff  = _safe_div(_rolling_sum(up.shift(1) * down, _TD_MON),
                    _rolling_sum(up.shift(1), _TD_MON).replace(0, np.nan))
    lhf = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    up_vol   = _safe_div(_rolling_sum(up * volume, _TD_MON),
                         _rolling_sum(up, _TD_MON).replace(0, np.nan))
    down_vol = _safe_div(_rolling_sum(down * volume, _TD_MON),
                         _rolling_sum(down, _TD_MON).replace(0, np.nan))
    vol_ratio = _safe_div(up_vol, down_vol)
    r_ff  = ff.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r_lhf = lhf.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    r_vol = (1.0 - vol_ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5))
    return (r_ff + r_lhf + r_vol) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

RECOVERY_FAILURE_EXTENDED_REGISTRY_001_075 = {
    "rfl_ext_001_open_gap_up_5d": {"inputs": ["open", "close"], "func": rfl_ext_001_open_gap_up_5d},
    "rfl_ext_002_open_vs_5d_prior_close": {"inputs": ["open", "close"], "func": rfl_ext_002_open_vs_5d_prior_close},
    "rfl_ext_003_close_vs_open_daily": {"inputs": ["open", "close"], "func": rfl_ext_003_close_vs_open_daily},
    "rfl_ext_004_open_above_prior_close_streak": {"inputs": ["open", "close"], "func": rfl_ext_004_open_above_prior_close_streak},
    "rfl_ext_005_open_gap_fail_count_21d": {"inputs": ["open", "close"], "func": rfl_ext_005_open_gap_fail_count_21d},
    "rfl_ext_006_open_gap_fail_fraction_63d": {"inputs": ["open", "close"], "func": rfl_ext_006_open_gap_fail_fraction_63d},
    "rfl_ext_007_close_vs_prior_open_21d_bounce": {"inputs": ["open", "close"], "func": rfl_ext_007_close_vs_prior_open_21d_bounce},
    "rfl_ext_008_open_retracement_vs_prior_down_21d": {"inputs": ["open", "close"], "func": rfl_ext_008_open_retracement_vs_prior_down_21d},
    "rfl_ext_009_high_vs_open_21d_range": {"inputs": ["open", "close", "high", "low"], "func": rfl_ext_009_high_vs_open_21d_range},
    "rfl_ext_010_open_above_5d_max_high_flag": {"inputs": ["open", "high"], "func": rfl_ext_010_open_above_5d_max_high_flag},
    "rfl_ext_011_open_close_recovery_21d": {"inputs": ["open", "close"], "func": rfl_ext_011_open_close_recovery_21d},
    "rfl_ext_012_open_close_recovery_63d": {"inputs": ["open", "close"], "func": rfl_ext_012_open_close_recovery_63d},
    "rfl_ext_013_bounce_retracement_ratio_10d": {"inputs": ["close"], "func": rfl_ext_013_bounce_retracement_ratio_10d},
    "rfl_ext_014_bounce_retracement_ratio_63d": {"inputs": ["close"], "func": rfl_ext_014_bounce_retracement_ratio_63d},
    "rfl_ext_015_bounce_vs_21d_atr": {"inputs": ["close", "high", "low"], "func": rfl_ext_015_bounce_vs_21d_atr},
    "rfl_ext_016_bounce_vs_63d_atr": {"inputs": ["close", "high", "low"], "func": rfl_ext_016_bounce_vs_63d_atr},
    "rfl_ext_017_bounce_ret_5d_pct_rank_252d": {"inputs": ["close"], "func": rfl_ext_017_bounce_ret_5d_pct_rank_252d},
    "rfl_ext_018_bounce_ret_21d_pct_rank_252d": {"inputs": ["close"], "func": rfl_ext_018_bounce_ret_21d_pct_rank_252d},
    "rfl_ext_019_bounce_retracement_ratio_5d_pct_rank_252d": {"inputs": ["close"], "func": rfl_ext_019_bounce_retracement_ratio_5d_pct_rank_252d},
    "rfl_ext_020_bounce_retracement_ratio_21d_zscore_252d": {"inputs": ["close"], "func": rfl_ext_020_bounce_retracement_ratio_21d_zscore_252d},
    "rfl_ext_021_bounce_vs_prior_peak_252d": {"inputs": ["close"], "func": rfl_ext_021_bounce_vs_prior_peak_252d},
    "rfl_ext_022_bounce_vs_prior_trough_21d": {"inputs": ["close"], "func": rfl_ext_022_bounce_vs_prior_trough_21d},
    "rfl_ext_023_high_vs_prior_high_63d_zscore": {"inputs": ["high"], "func": rfl_ext_023_high_vs_prior_high_63d_zscore},
    "rfl_ext_024_high_vs_prior_high_126d": {"inputs": ["high"], "func": rfl_ext_024_high_vs_prior_high_126d},
    "rfl_ext_025_lower_high_count_126d": {"inputs": ["high"], "func": rfl_ext_025_lower_high_count_126d},
    "rfl_ext_026_lower_high_fraction_126d": {"inputs": ["high"], "func": rfl_ext_026_lower_high_fraction_126d},
    "rfl_ext_027_lower_high_fraction_21d_zscore_252d": {"inputs": ["high"], "func": rfl_ext_027_lower_high_fraction_21d_zscore_252d},
    "rfl_ext_028_lower_high_fraction_63d_pct_rank_252d": {"inputs": ["high"], "func": rfl_ext_028_lower_high_fraction_63d_pct_rank_252d},
    "rfl_ext_029_consec_lower_highs_21d_max": {"inputs": ["high"], "func": rfl_ext_029_consec_lower_highs_21d_max},
    "rfl_ext_030_consec_lower_highs_63d_max": {"inputs": ["high"], "func": rfl_ext_030_consec_lower_highs_63d_max},
    "rfl_ext_031_open_vs_prior_open_lower_count_21d": {"inputs": ["open"], "func": rfl_ext_031_open_vs_prior_open_lower_count_21d},
    "rfl_ext_032_open_vs_prior_open_lower_fraction_63d": {"inputs": ["open"], "func": rfl_ext_032_open_vs_prior_open_lower_fraction_63d},
    "rfl_ext_033_rally_fail_fraction_21d": {"inputs": ["close"], "func": rfl_ext_033_rally_fail_fraction_21d},
    "rfl_ext_034_rally_fail_fraction_63d": {"inputs": ["close"], "func": rfl_ext_034_rally_fail_fraction_63d},
    "rfl_ext_035_rally_fail_count_21d_zscore_252d": {"inputs": ["close"], "func": rfl_ext_035_rally_fail_count_21d_zscore_252d},
    "rfl_ext_036_three_day_rally_fail_count_21d": {"inputs": ["close"], "func": rfl_ext_036_three_day_rally_fail_count_21d},
    "rfl_ext_037_two_day_rally_fail_count_63d": {"inputs": ["close"], "func": rfl_ext_037_two_day_rally_fail_count_63d},
    "rfl_ext_038_rally_then_new_low_count_63d": {"inputs": ["close"], "func": rfl_ext_038_rally_then_new_low_count_63d},
    "rfl_ext_039_avg_bounce_before_fail_21d": {"inputs": ["close"], "func": rfl_ext_039_avg_bounce_before_fail_21d},
    "rfl_ext_040_rally_fail_fraction_21d_pct_rank_252d": {"inputs": ["close"], "func": rfl_ext_040_rally_fail_fraction_21d_pct_rank_252d},
    "rfl_ext_041_net_up_vs_down_count_21d": {"inputs": ["close"], "func": rfl_ext_041_net_up_vs_down_count_21d},
    "rfl_ext_042_net_up_vs_down_count_63d_zscore_252d": {"inputs": ["close"], "func": rfl_ext_042_net_up_vs_down_count_63d_zscore_252d},
    "rfl_ext_043_vol_on_up_days_vs_down_days_21d": {"inputs": ["close", "volume"], "func": rfl_ext_043_vol_on_up_days_vs_down_days_21d},
    "rfl_ext_044_vol_on_up_days_vs_down_days_63d": {"inputs": ["close", "volume"], "func": rfl_ext_044_vol_on_up_days_vs_down_days_63d},
    "rfl_ext_045_bounce_volume_ratio_5d_vs_decline_21d": {"inputs": ["close", "volume"], "func": rfl_ext_045_bounce_volume_ratio_5d_vs_decline_21d},
    "rfl_ext_046_vol_weighted_bounce_ret_5d": {"inputs": ["close", "volume"], "func": rfl_ext_046_vol_weighted_bounce_ret_5d},
    "rfl_ext_047_vol_weighted_bounce_ret_21d": {"inputs": ["close", "volume"], "func": rfl_ext_047_vol_weighted_bounce_ret_21d},
    "rfl_ext_048_vol_on_rally_fail_days_21d": {"inputs": ["close", "volume"], "func": rfl_ext_048_vol_on_rally_fail_days_21d},
    "rfl_ext_049_vol_ratio_up_day_zscore_252d": {"inputs": ["close", "volume"], "func": rfl_ext_049_vol_ratio_up_day_zscore_252d},
    "rfl_ext_050_vol_weighted_lower_high_fraction_63d": {"inputs": ["high", "volume"], "func": rfl_ext_050_vol_weighted_lower_high_fraction_63d},
    "rfl_ext_051_ewm_bounce_ret_21d_span5": {"inputs": ["close"], "func": rfl_ext_051_ewm_bounce_ret_21d_span5},
    "rfl_ext_052_ewm_bounce_ret_21d_span21": {"inputs": ["close"], "func": rfl_ext_052_ewm_bounce_ret_21d_span21},
    "rfl_ext_053_bounce_vs_peak_zscore_252d": {"inputs": ["close"], "func": rfl_ext_053_bounce_vs_peak_zscore_252d},
    "rfl_ext_054_high_vs_prior_high_21d_zscore_252d": {"inputs": ["high"], "func": rfl_ext_054_high_vs_prior_high_21d_zscore_252d},
    "rfl_ext_055_peak_drawdown_from_63d_peak_zscore_252d": {"inputs": ["close"], "func": rfl_ext_055_peak_drawdown_from_63d_peak_zscore_252d},
    "rfl_ext_056_up_day_fraction_21d_ewm_span21": {"inputs": ["close"], "func": rfl_ext_056_up_day_fraction_21d_ewm_span21},
    "rfl_ext_057_rally_fail_consec_streak": {"inputs": ["close"], "func": rfl_ext_057_rally_fail_consec_streak},
    "rfl_ext_058_down_after_up_retracement_21d_mean": {"inputs": ["close"], "func": rfl_ext_058_down_after_up_retracement_21d_mean},
    "rfl_ext_059_max_up_streak_126d": {"inputs": ["close"], "func": rfl_ext_059_max_up_streak_126d},
    "rfl_ext_060_up_day_count_126d": {"inputs": ["close"], "func": rfl_ext_060_up_day_count_126d},
    "rfl_ext_061_low_vs_prior_low_21d": {"inputs": ["low"], "func": rfl_ext_061_low_vs_prior_low_21d},
    "rfl_ext_062_low_vs_prior_low_63d": {"inputs": ["low"], "func": rfl_ext_062_low_vs_prior_low_63d},
    "rfl_ext_063_lower_low_count_21d": {"inputs": ["low"], "func": rfl_ext_063_lower_low_count_21d},
    "rfl_ext_064_lower_low_count_63d": {"inputs": ["low"], "func": rfl_ext_064_lower_low_count_63d},
    "rfl_ext_065_lower_low_fraction_21d": {"inputs": ["low"], "func": rfl_ext_065_lower_low_fraction_21d},
    "rfl_ext_066_lower_low_fraction_63d_pct_rank_252d": {"inputs": ["low"], "func": rfl_ext_066_lower_low_fraction_63d_pct_rank_252d},
    "rfl_ext_067_low_above_prior_low_streak": {"inputs": ["low"], "func": rfl_ext_067_low_above_prior_low_streak},
    "rfl_ext_068_high_above_prior_high_streak": {"inputs": ["high"], "func": rfl_ext_068_high_above_prior_high_streak},
    "rfl_ext_069_composite_lower_high_lower_low_63d": {"inputs": ["high", "low"], "func": rfl_ext_069_composite_lower_high_lower_low_63d},
    "rfl_ext_070_recovery_failure_score_21d": {"inputs": ["close", "high"], "func": rfl_ext_070_recovery_failure_score_21d},
    "rfl_ext_071_retracement_ratio_5d_ewm_21d": {"inputs": ["close"], "func": rfl_ext_071_retracement_ratio_5d_ewm_21d},
    "rfl_ext_072_max_bounce_5d_in_63d_vs_mean_bounce": {"inputs": ["close"], "func": rfl_ext_072_max_bounce_5d_in_63d_vs_mean_bounce},
    "rfl_ext_073_up_day_fraction_63d_zscore_252d": {"inputs": ["close"], "func": rfl_ext_073_up_day_fraction_63d_zscore_252d},
    "rfl_ext_074_lower_high_lower_low_composite_zscore_252d": {"inputs": ["high", "low"], "func": rfl_ext_074_lower_high_lower_low_composite_zscore_252d},
    "rfl_ext_075_capitulation_recovery_failure_score": {"inputs": ["close", "high", "volume"], "func": rfl_ext_075_capitulation_recovery_failure_score},
}
