"""
14_recovery_failure — Base Features 076-200
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-088): EMA / SMA reclaim failures ---

def rfl_076_close_vs_ema5(close: pd.Series) -> pd.Series:
    """Close relative to 5-day EMA (below = short-term rally failed to hold)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    return _safe_div(close - ema5, ema5)


def rfl_077_close_vs_ema21(close: pd.Series) -> pd.Series:
    """Close relative to 21-day EMA."""
    ema21 = _ewm_mean(close, _TD_MON)
    return _safe_div(close - ema21, ema21)


def rfl_078_close_vs_sma21(close: pd.Series) -> pd.Series:
    """Close relative to 21-day SMA."""
    sma21 = _rolling_mean(close, _TD_MON)
    return _safe_div(close - sma21, sma21)


def rfl_079_close_vs_sma50(close: pd.Series) -> pd.Series:
    """Close relative to 50-day SMA."""
    sma50 = _rolling_mean(close, 50)
    return _safe_div(close - sma50, sma50)


def rfl_080_close_vs_sma200(close: pd.Series) -> pd.Series:
    """Close relative to 200-day SMA (distance from key long-term resistance)."""
    sma200 = _rolling_mean(close, 200)
    return _safe_div(close - sma200, sma200)


def rfl_081_consec_days_below_ema21(close: pd.Series) -> pd.Series:
    """Consecutive days close is below 21-day EMA."""
    ema21 = _ewm_mean(close, _TD_MON)
    return _consec_streak(close < ema21)


def rfl_082_consec_days_below_ema63(close: pd.Series) -> pd.Series:
    """Consecutive days close is below 63-day EMA."""
    ema63 = _ewm_mean(close, _TD_QTR)
    return _consec_streak(close < ema63)


def rfl_083_ema21_reclaim_attempts_63d(close: pd.Series) -> pd.Series:
    """Count of days where close crossed above EMA21 but failed within 5 days, 63d window."""
    ema21 = _ewm_mean(close, _TD_MON)
    cross_up = ((close > ema21) & (close.shift(1) <= ema21.shift(1))).astype(float)
    fail = (cross_up.shift(1) + cross_up.shift(2) + cross_up.shift(3) + cross_up.shift(4))
    fail_then_below = (fail > 0) & (close < ema21)
    return _rolling_count_true(fail_then_below, _TD_QTR)


def rfl_084_sma21_slope(close: pd.Series) -> pd.Series:
    """5-day slope of the 21-day SMA (direction and speed of trend)."""
    sma21 = _rolling_mean(close, _TD_MON)
    return sma21.diff(_TD_WEEK)


def rfl_085_sma63_slope(close: pd.Series) -> pd.Series:
    """5-day slope of the 63-day SMA."""
    sma63 = _rolling_mean(close, _TD_QTR)
    return sma63.diff(_TD_WEEK)


def rfl_086_ema21_slope(close: pd.Series) -> pd.Series:
    """5-day slope of the 21-day EMA."""
    ema21 = _ewm_mean(close, _TD_MON)
    return ema21.diff(_TD_WEEK)


def rfl_087_ema_spread_5_21(close: pd.Series) -> pd.Series:
    """Spread between 5-day EMA and 21-day EMA (short vs intermediate trend gap)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema21 = _ewm_mean(close, _TD_MON)
    return _safe_div(ema5 - ema21, ema21)


def rfl_088_ema_spread_21_63(close: pd.Series) -> pd.Series:
    """Spread between 21-day EMA and 63-day EMA."""
    ema21 = _ewm_mean(close, _TD_MON)
    ema63 = _ewm_mean(close, _TD_QTR)
    return _safe_div(ema21 - ema63, ema63)


# --- Group H (089-101): Lower-high vs lower-low structure metrics ---

def rfl_089_lower_high_lower_low_both_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with both lower-high AND lower-low in trailing 21 days."""
    cond = (high < high.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def rfl_090_lower_high_lower_low_both_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with both lower-high AND lower-low in trailing 63 days."""
    cond = (high < high.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


def rfl_091_high_low_ratio_compression_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21d high-of-highs to 21d low-of-lows (tight = compressed range)."""
    hh = _rolling_max(high, _TD_MON)
    ll = _rolling_min(low, _TD_MON)
    return _safe_div(hh, ll)


def rfl_092_high_low_ratio_compression_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 63d high-of-highs to 63d low-of-lows."""
    hh = _rolling_max(high, _TD_QTR)
    ll = _rolling_min(low, _TD_QTR)
    return _safe_div(hh, ll)


def rfl_093_lower_close_higher_high_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of 'fake breakout' days: higher high but lower close, 21d."""
    cond = (high > high.shift(1)) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def rfl_094_lower_close_higher_high_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of fake breakout days over 63 days."""
    cond = (high > high.shift(1)) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


def rfl_095_high_to_close_ratio_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Avg ratio of daily high to daily close over 21 days (close near high = strength)."""
    ratio = _safe_div(close, high)
    return _rolling_mean(ratio, _TD_MON)


def rfl_096_high_to_close_ratio_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Avg ratio of daily high to daily close over 63 days."""
    ratio = _safe_div(close, high)
    return _rolling_mean(ratio, _TD_QTR)


def rfl_097_low_to_close_ratio_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Avg ratio of daily low to daily close over 21 days (high = close near low)."""
    ratio = _safe_div(low, close)
    return _rolling_mean(ratio, _TD_MON)


def rfl_098_low_to_close_ratio_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Avg ratio of daily low to daily close over 63 days."""
    ratio = _safe_div(low, close)
    return _rolling_mean(ratio, _TD_QTR)


def rfl_099_open_high_close_range_fraction_21d(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """Avg (high - close)/(high - open) over 21 days (close distance from intraday high)."""
    num = (high - close).clip(lower=0)
    den = (high - open).abs().replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()


def rfl_100_consec_close_near_daily_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Streak of days closing in bottom 25% of daily range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _consec_streak(pos <= 0.25)


def rfl_101_upper_shadow_ratio_21d(close: pd.Series, open: pd.Series, high: pd.Series) -> pd.Series:
    """Avg upper shadow (high - max(open,close)) / daily range over 21 days."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    upper = (high - body_top).clip(lower=0)
    rng = (high - pd.concat([open, close], axis=1).min(axis=1)).replace(0, np.nan)
    return _safe_div(upper, rng).rolling(_TD_MON, min_periods=1).mean()


# --- Group I (102-114): Z-score and rank normalizations of bounce metrics ---

def rfl_102_bounce_ret_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day return within trailing 252-day distribution."""
    r = close.pct_change(_TD_WEEK)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rfl_103_bounce_ret_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day return within trailing 252-day distribution."""
    r = close.pct_change(_TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rfl_104_retracement_pct_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d retracement fraction within 252-day distribution."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    rng = (pk - tr).replace(0, np.nan)
    frac = _safe_div(close - tr, rng)
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def rfl_105_bounce_ret_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day return within trailing 252 days."""
    r = close.pct_change(_TD_WEEK)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_106_up_down_ratio_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d up/down count ratio within 252 days."""
    ret = close.pct_change(1)
    up = _rolling_count_true(ret > 0, _TD_MON)
    dn = _rolling_count_true(ret < 0, _TD_MON)
    ratio = _safe_div(up, dn.replace(0, np.nan))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_107_vol_bounce_ratio_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of up/down volume ratio within trailing 252 days."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def rfl_108_lower_high_fraction_21d_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score of lower-high fraction (21d) vs 252d distribution."""
    frac = _rolling_count_true(high < high.shift(1), _TD_MON) / _TD_MON
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def rfl_109_bounce_fade_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d bounce fade vs 252d distribution."""
    pk21 = _local_peak(close, _TD_MON)
    fade = _safe_div(close - pk21, pk21)
    m = _rolling_mean(fade, _TD_YEAR)
    s = _rolling_std(fade, _TD_YEAR)
    return _safe_div(fade - m, s)


def rfl_110_retracement_63d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d retracement fraction (all-history extremity)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    rng = (pk - tr).replace(0, np.nan)
    frac = _safe_div(close - tr, rng)
    return frac.expanding(min_periods=5).rank(pct=True)


def rfl_111_net_ret_21d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of net 21-day log return."""
    lr = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return lr.expanding(min_periods=5).rank(pct=True)


def rfl_112_up_down_vol_ratio_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63d up/down volume ratio within 252 days."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_113_ema_spread_5_21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA5-EMA21 spread within 252 days."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema21 = _ewm_mean(close, _TD_MON)
    spread = _safe_div(ema5 - ema21, ema21)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rfl_114_lower_high_count_63d_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score of 63d lower-high count within 252-day distribution."""
    cnt = _rolling_count_true(high < high.shift(1), _TD_QTR)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


# --- Group J (115-127): Composite recovery-failure scores ---

def rfl_115_bounce_failure_score_21d(close: pd.Series) -> pd.Series:
    """Composite: avg of (1 - retracement_63d, lower_high_frac_21d, bounce_fade_21d normalized)."""
    pk63 = _rolling_max(close, _TD_QTR)
    tr63 = _rolling_min(close, _TD_QTR)
    rng63 = (pk63 - tr63).replace(0, np.nan)
    retr = _safe_div(close - tr63, rng63).clip(0, 1)
    lh_frac = _rolling_count_true(close > close.shift(1), _TD_MON) / _TD_MON
    fade = _safe_div(close - _local_peak(close, _TD_MON), _local_peak(close, _TD_MON)).fillna(0)
    return (1 - retr) * 0.4 + (1 - lh_frac) * 0.3 + (-fade).clip(lower=0) * 0.3


def rfl_116_bounce_quality_vol_adjusted_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d bounce return times up-volume ratio (quality-adjusted bounce)."""
    bounce = close.pct_change(_TD_WEEK)
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    vol_ratio = _safe_div(up_vol, dn_vol.replace(0, np.nan)).fillna(0)
    return bounce * vol_ratio


def rfl_117_failed_rally_rate_63d(close: pd.Series) -> pd.Series:
    """Fraction of up days in 63d that were immediately followed by a down day."""
    up = (close > close.shift(1)).astype(float)
    fail = (up.shift(1) * (close < close.shift(1)).astype(float))
    up_sum = _rolling_sum(up.shift(1), _TD_QTR)
    fail_sum = _rolling_sum(fail, _TD_QTR)
    return _safe_div(fail_sum, up_sum.replace(0, np.nan))


def rfl_118_retracement_decay_score(close: pd.Series) -> pd.Series:
    """21d retracement pct minus 63d retracement pct (bounce shrinking over time)."""
    pk21 = _rolling_max(close, _TD_MON)
    tr21 = _rolling_min(close, _TD_MON)
    r21 = _safe_div(close - tr21, (pk21 - tr21).replace(0, np.nan))
    pk63 = _rolling_max(close, _TD_QTR)
    tr63 = _rolling_min(close, _TD_QTR)
    r63 = _safe_div(close - tr63, (pk63 - tr63).replace(0, np.nan))
    return r21 - r63


def rfl_119_recovery_failure_composite_63d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined signal: lower_high_frac + (1-retracement) + (1-vol_up_ratio), 63d."""
    lh_frac = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    retr = _safe_div(close - tr, (pk - tr).replace(0, np.nan)).clip(0, 1)
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    vol_ratio = _safe_div(up_vol, dn_vol.replace(0, np.nan)).clip(0, 2) / 2
    return lh_frac * 0.35 + (1 - retr) * 0.35 + (1 - vol_ratio) * 0.30


def rfl_120_up_ret_sum_vs_dn_ret_sum_21d(close: pd.Series) -> pd.Series:
    """Ratio of summed up-day returns to summed down-day return magnitudes, 21d."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up = lr.where(lr > 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    dn = (-lr).where(lr < 0, 0.0).rolling(_TD_MON, min_periods=1).sum()
    return _safe_div(up, dn.replace(0, np.nan))


def rfl_121_up_ret_sum_vs_dn_ret_sum_63d(close: pd.Series) -> pd.Series:
    """Ratio of summed up-day returns to summed down-day magnitudes, 63d."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up = lr.where(lr > 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    dn = (-lr).where(lr < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(up, dn.replace(0, np.nan))


def rfl_122_max_bounce_then_fade_21d(close: pd.Series) -> pd.Series:
    """Max up-streak in 21d times (21d peak drawdown) — measures size and failure of best bounce."""
    max_up = _rolling_max_streak(close > close.shift(1), _TD_MON)
    peak = _rolling_max(close, _TD_MON)
    fade = _safe_div(close - peak, peak).abs()
    return max_up * fade


def rfl_123_high_vol_bounce_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume up days (vol > 21d avg) in last 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret > 0) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_MON)


def rfl_124_high_vol_bounce_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume up days in last 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret > 0) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_QTR)


def rfl_125_bounce_to_decline_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of up/down volume ratio (63d) within 252d distribution."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(up_vol, dn_vol)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def rfl_126_close_to_range_position_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 21d high-low range (0 = at low, 1 = at high)."""
    hh = _rolling_max(high, _TD_MON)
    ll = _rolling_min(low, _TD_MON)
    rng = (hh - ll).replace(0, np.nan)
    return _safe_div(close - ll, rng)


def rfl_127_close_to_range_position_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 63d high-low range."""
    hh = _rolling_max(high, _TD_QTR)
    ll = _rolling_min(low, _TD_QTR)
    rng = (hh - ll).replace(0, np.nan)
    return _safe_div(close - ll, rng)


# --- Group K (128-138): Intraday bounce failure signals ---

def rfl_128_intraday_bounce_fraction_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (close - low) / (open - low) over 21 days (fraction of intraday range recovered)."""
    num = (close - low).clip(lower=0)
    den = (open - low).abs().replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()


def rfl_129_intraday_bounce_fraction_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (close - low) / (open - low) over 63 days."""
    num = (close - low).clip(lower=0)
    den = (open - low).abs().replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_QTR, min_periods=1).mean()


def rfl_130_open_gap_up_then_close_down_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21d gap-up opens that closed below prior close."""
    gap_up = (open > close.shift(1)).astype(float)
    fail = (gap_up * (close < close.shift(1)).astype(float))
    gap_count = _rolling_sum(gap_up, _TD_MON)
    fail_count = _rolling_sum(fail, _TD_MON)
    return _safe_div(fail_count, gap_count.replace(0, np.nan))


def rfl_131_open_gap_up_then_close_down_frac_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63d gap-up opens that closed below prior close."""
    gap_up = (open > close.shift(1)).astype(float)
    fail = (gap_up * (close < close.shift(1)).astype(float))
    gap_count = _rolling_sum(gap_up, _TD_QTR)
    fail_count = _rolling_sum(fail, _TD_QTR)
    return _safe_div(fail_count, gap_count.replace(0, np.nan))


def rfl_132_consec_gap_up_fail(close: pd.Series, open: pd.Series) -> pd.Series:
    """Consecutive days of gap-up opens that close below prior close."""
    cond = (open > close.shift(1)) & (close < close.shift(1))
    return _consec_streak(cond)


def rfl_133_high_minus_open_over_range_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (high - open) / (high - low) over 21 days (early strength that fades)."""
    num = (high - open).clip(lower=0)
    den = (high - low).replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()


def rfl_134_close_minus_open_over_range_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (close - open) / (high - low) over 21 days (net body as range fraction)."""
    num = close - open
    den = (high - low).replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_MON, min_periods=1).mean()


def rfl_135_close_minus_open_over_range_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (close - open) / (high - low) over 63 days."""
    num = close - open
    den = (high - low).replace(0, np.nan)
    return _safe_div(num, den).rolling(_TD_QTR, min_periods=1).mean()


def rfl_136_intraday_high_reversal_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Avg (high - close) / close over 21 days (how much is given back from intraday high)."""
    ret_from_high = _safe_div(high - close, close)
    return _rolling_mean(ret_from_high, _TD_MON)


def rfl_137_intraday_high_reversal_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Avg (high - close) / close over 63 days."""
    ret_from_high = _safe_div(high - close, close)
    return _rolling_mean(ret_from_high, _TD_QTR)


def rfl_138_upper_wick_fraction_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg upper wick as fraction of total range over 21 days."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    upper = (high - body_top).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(upper, rng).rolling(_TD_MON, min_periods=1).mean()


# --- Group L (139-150): Long-window lower-high and recovery metrics ---

def rfl_139_high_below_21d_ago_high_count_63d(high: pd.Series) -> pd.Series:
    """Count of days in 63d where today's high < high from 21 days prior."""
    cond = high < high.shift(_TD_MON)
    return _rolling_count_true(cond, _TD_QTR)


def rfl_140_high_below_63d_ago_high_count_126d(high: pd.Series) -> pd.Series:
    """Count of days in 126d where today's high < high from 63 days prior."""
    cond = high < high.shift(_TD_QTR)
    return _rolling_count_true(cond, _TD_HALF)


def rfl_141_close_below_21d_ago_close_count_63d(close: pd.Series) -> pd.Series:
    """Count of days in 63d where close < close from 21 days prior."""
    cond = close < close.shift(_TD_MON)
    return _rolling_count_true(cond, _TD_QTR)


def rfl_142_close_pct_from_52wk_high(close: pd.Series) -> pd.Series:
    """Current close as fraction of 252-day rolling high (distance from annual high)."""
    hh252 = _rolling_max(close, _TD_YEAR)
    return _safe_div(close, hh252)


def rfl_143_close_pct_from_126d_high(close: pd.Series) -> pd.Series:
    """Current close as fraction of 126-day rolling high."""
    hh126 = _rolling_max(close, _TD_HALF)
    return _safe_div(close, hh126)


def rfl_144_close_pct_from_63d_high(close: pd.Series) -> pd.Series:
    """Current close as fraction of 63-day rolling high."""
    hh63 = _rolling_max(close, _TD_QTR)
    return _safe_div(close, hh63)


def rfl_145_retracement_vs_prior_bounce_21d(close: pd.Series) -> pd.Series:
    """21d return divided by the absolute 21d return from 21 days earlier."""
    r_now = close.pct_change(_TD_MON)
    r_prior = r_now.shift(_TD_MON).abs().replace(0, np.nan)
    return _safe_div(r_now, r_prior)


def rfl_146_bounce_decay_score_63d(close: pd.Series) -> pd.Series:
    """Rate at which the trailing 21d max-bounce has decayed vs 63d max-bounce."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    mx21 = log_ret.rolling(_TD_MON, min_periods=1).max()
    mx63 = log_ret.rolling(_TD_QTR, min_periods=1).max()
    return _safe_div(mx21, mx63.replace(0, np.nan))


def rfl_147_lower_high_streak_21d_norm(high: pd.Series) -> pd.Series:
    """Consecutive lower-highs normalized by 252d avg of that streak."""
    streak = _consec_streak(high < high.shift(1))
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg.replace(0, np.nan))


def rfl_148_avg_bounce_per_decline_63d(close: pd.Series) -> pd.Series:
    """Avg up-day return divided by avg down-day return magnitude in 63d."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_avg = lr.where(lr > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_avg = (-lr).where(lr < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(up_avg, dn_avg.replace(0, np.nan))


def rfl_149_bounce_attempt_count_63d(close: pd.Series) -> pd.Series:
    """Count of distinct up-day streaks (bounce starts) in trailing 63 days."""
    ret = close.pct_change(1)
    is_start = ((ret > 0) & (ret.shift(1) <= 0)).astype(float)
    return _rolling_sum(is_start, _TD_QTR)


def rfl_150_failed_bounce_composite_126d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """126d composite: (1-retracement_126d) * lower_high_frac_63d * (1-vol_up_ratio_63d)."""
    pk = _rolling_max(close, _TD_HALF)
    tr = _rolling_min(close, _TD_HALF)
    retr = _safe_div(close - tr, (pk - tr).replace(0, np.nan)).clip(0, 1)
    lh_frac = _rolling_count_true(high < high.shift(1), _TD_QTR) / _TD_QTR
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    vol_ratio = (_safe_div(up_vol, dn_vol.replace(0, np.nan))).clip(0, 2) / 2
    return (1 - retr) * lh_frac * (1 - vol_ratio)


# --- Group M2 (176-200): Candlestick structure, MA variants, composites ---

def rfl_176_lower_wick_fraction_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg lower wick as fraction of total range over 21 days (tail buying support)."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    lower = (body_bot - low).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(lower, rng).rolling(_TD_MON, min_periods=1).mean()


def rfl_177_lower_wick_fraction_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg lower wick as fraction of total range over 63 days."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    lower = (body_bot - low).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(lower, rng).rolling(_TD_QTR, min_periods=1).mean()


def rfl_178_body_to_range_ratio_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg candle body size / daily range over 21 days (decreasing = indecision)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body, rng).rolling(_TD_MON, min_periods=1).mean()


def rfl_179_body_to_range_ratio_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg candle body size / daily range over 63 days."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body, rng).rolling(_TD_QTR, min_periods=1).mean()


def rfl_180_close_vs_sma63(close: pd.Series) -> pd.Series:
    """Close relative to 63-day SMA."""
    sma63 = _rolling_mean(close, _TD_QTR)
    return _safe_div(close - sma63, sma63)


def rfl_181_close_vs_sma126(close: pd.Series) -> pd.Series:
    """Close relative to 126-day SMA."""
    sma126 = _rolling_mean(close, _TD_HALF)
    return _safe_div(close - sma126, sma126)


def rfl_182_ema_spread_5_63(close: pd.Series) -> pd.Series:
    """Spread between 5-day EMA and 63-day EMA (short vs long-term gap)."""
    ema5 = _ewm_mean(close, _TD_WEEK)
    ema63 = _ewm_mean(close, _TD_QTR)
    return _safe_div(ema5 - ema63, ema63)


def rfl_183_consec_days_below_sma50(close: pd.Series) -> pd.Series:
    """Consecutive days close is below 50-day SMA."""
    sma50 = _rolling_mean(close, 50)
    return _consec_streak(close < sma50)


def rfl_184_consec_days_below_sma200(close: pd.Series) -> pd.Series:
    """Consecutive days close is below 200-day SMA."""
    sma200 = _rolling_mean(close, 200)
    return _consec_streak(close < sma200)


def rfl_185_close_below_sma_cross_count_63d(close: pd.Series) -> pd.Series:
    """Count of times close crossed below 21d SMA in trailing 63 days."""
    sma21 = _rolling_mean(close, _TD_MON)
    cross_below = ((close < sma21) & (close.shift(1) >= sma21.shift(1))).astype(float)
    return _rolling_sum(cross_below, _TD_QTR)


def rfl_186_lower_close_lower_low_both_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with both lower-close AND lower-low in trailing 21 days."""
    cond = (close < close.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_MON)


def rfl_187_lower_close_lower_low_both_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with both lower-close AND lower-low in trailing 63 days."""
    cond = (close < close.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_QTR)


def rfl_188_open_below_prior_low_count_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < prior day's low in trailing 21 days (gap-down exhaustion)."""
    return _rolling_count_true(open < low.shift(1), _TD_MON)


def rfl_189_close_position_in_daily_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg close position within daily high-low range over 21 days (0=low, 1=high)."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _rolling_mean(pos, _TD_MON)


def rfl_190_close_position_in_daily_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg close position within daily high-low range over 63 days."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _rolling_mean(pos, _TD_QTR)


def rfl_191_median_bounce_ret_21d(close: pd.Series) -> pd.Series:
    """Median single-day log-return on up-days over trailing 21 days."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_ret = lr.where(lr > 0, np.nan)
    return up_ret.rolling(_TD_MON, min_periods=1).median()


def rfl_192_median_bounce_ret_63d(close: pd.Series) -> pd.Series:
    """Median single-day log-return on up-days over trailing 63 days."""
    lr = _log_safe(close) - _log_safe(close.shift(1))
    up_ret = lr.where(lr > 0, np.nan)
    return up_ret.rolling(_TD_QTR, min_periods=1).median()


def rfl_193_high_vol_bounce_count_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume up days (vol > 21d avg) in last 126 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    cond = (ret > 0) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_HALF)


def rfl_194_vol_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-days over last 63 days."""
    ret = close.pct_change(1)
    return volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def rfl_195_vol_trend_21d(volume: pd.Series) -> pd.Series:
    """21-day volume relative to its 63-day average (expanding or shrinking participation)."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg63 = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg21, avg63)


def rfl_196_intraday_range_contraction_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg daily range divided by 63-day avg daily range (contraction signal)."""
    daily_rng = high - low
    avg21 = _rolling_mean(daily_rng, _TD_MON)
    avg63 = _rolling_mean(daily_rng, _TD_QTR)
    return _safe_div(avg21, avg63)


def rfl_197_intraday_range_contraction_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day avg daily range divided by 126-day avg daily range."""
    daily_rng = high - low
    avg63 = _rolling_mean(daily_rng, _TD_QTR)
    avg126 = _rolling_mean(daily_rng, _TD_HALF)
    return _safe_div(avg63, avg126)


def rfl_198_close_to_range_position_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 126d high-low range (0 = at low, 1 = at high)."""
    hh = _rolling_max(high, _TD_HALF)
    ll = _rolling_min(low, _TD_HALF)
    rng = (hh - ll).replace(0, np.nan)
    return _safe_div(close - ll, rng)


def rfl_199_bounce_failure_score_63d(close: pd.Series) -> pd.Series:
    """Composite: avg of (1 - retracement_126d, lower_high_frac_63d, up_day_frac_63d inverted)."""
    pk126 = _rolling_max(close, _TD_HALF)
    tr126 = _rolling_min(close, _TD_HALF)
    retr = _safe_div(close - tr126, (pk126 - tr126).replace(0, np.nan)).clip(0, 1)
    lh_frac = _rolling_count_true(close > close.shift(1), _TD_QTR) / _TD_QTR
    fade = _safe_div(close - _local_peak(close, _TD_QTR), _local_peak(close, _TD_QTR)).fillna(0)
    return (1 - retr) * 0.4 + (1 - lh_frac) * 0.3 + (-fade).clip(lower=0) * 0.3


def rfl_200_recovery_failure_composite_126d_v2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """126d composite v2: weighted sum of lower-high frac, distance from 126d high, and vol imbalance."""
    lh_frac = _rolling_count_true(high < high.shift(1), _TD_HALF) / _TD_HALF
    hh126 = _rolling_max(high, _TD_HALF)
    dist = _safe_div(hh126 - close, hh126).clip(0, 1)
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_HALF, min_periods=1).mean()
    dn_vol = volume.where(ret < 0, np.nan).rolling(_TD_HALF, min_periods=1).mean()
    vol_imbal = (1 - (_safe_div(up_vol, dn_vol.replace(0, np.nan))).clip(0, 2) / 2)
    return lh_frac * 0.35 + dist * 0.40 + vol_imbal * 0.25


# ── Registry ──────────────────────────────────────────────────────────────────

RECOVERY_FAILURE_REGISTRY_076_150 = {
    "rfl_076_close_vs_ema5": {"inputs": ["close"], "func": rfl_076_close_vs_ema5},
    "rfl_077_close_vs_ema21": {"inputs": ["close"], "func": rfl_077_close_vs_ema21},
    "rfl_078_close_vs_sma21": {"inputs": ["close"], "func": rfl_078_close_vs_sma21},
    "rfl_079_close_vs_sma50": {"inputs": ["close"], "func": rfl_079_close_vs_sma50},
    "rfl_080_close_vs_sma200": {"inputs": ["close"], "func": rfl_080_close_vs_sma200},
    "rfl_081_consec_days_below_ema21": {"inputs": ["close"], "func": rfl_081_consec_days_below_ema21},
    "rfl_082_consec_days_below_ema63": {"inputs": ["close"], "func": rfl_082_consec_days_below_ema63},
    "rfl_083_ema21_reclaim_attempts_63d": {"inputs": ["close"], "func": rfl_083_ema21_reclaim_attempts_63d},
    "rfl_084_sma21_slope": {"inputs": ["close"], "func": rfl_084_sma21_slope},
    "rfl_085_sma63_slope": {"inputs": ["close"], "func": rfl_085_sma63_slope},
    "rfl_086_ema21_slope": {"inputs": ["close"], "func": rfl_086_ema21_slope},
    "rfl_087_ema_spread_5_21": {"inputs": ["close"], "func": rfl_087_ema_spread_5_21},
    "rfl_088_ema_spread_21_63": {"inputs": ["close"], "func": rfl_088_ema_spread_21_63},
    "rfl_089_lower_high_lower_low_both_21d": {"inputs": ["high", "low"], "func": rfl_089_lower_high_lower_low_both_21d},
    "rfl_090_lower_high_lower_low_both_63d": {"inputs": ["high", "low"], "func": rfl_090_lower_high_lower_low_both_63d},
    "rfl_091_high_low_ratio_compression_21d": {"inputs": ["high", "low"], "func": rfl_091_high_low_ratio_compression_21d},
    "rfl_092_high_low_ratio_compression_63d": {"inputs": ["high", "low"], "func": rfl_092_high_low_ratio_compression_63d},
    "rfl_093_lower_close_higher_high_21d": {"inputs": ["close", "high"], "func": rfl_093_lower_close_higher_high_21d},
    "rfl_094_lower_close_higher_high_63d": {"inputs": ["close", "high"], "func": rfl_094_lower_close_higher_high_63d},
    "rfl_095_high_to_close_ratio_21d": {"inputs": ["close", "high"], "func": rfl_095_high_to_close_ratio_21d},
    "rfl_096_high_to_close_ratio_63d": {"inputs": ["close", "high"], "func": rfl_096_high_to_close_ratio_63d},
    "rfl_097_low_to_close_ratio_21d": {"inputs": ["close", "low"], "func": rfl_097_low_to_close_ratio_21d},
    "rfl_098_low_to_close_ratio_63d": {"inputs": ["close", "low"], "func": rfl_098_low_to_close_ratio_63d},
    "rfl_099_open_high_close_range_fraction_21d": {"inputs": ["close", "open", "high"], "func": rfl_099_open_high_close_range_fraction_21d},
    "rfl_100_consec_close_near_daily_low_21d": {"inputs": ["close", "high", "low"], "func": rfl_100_consec_close_near_daily_low_21d},
    "rfl_101_upper_shadow_ratio_21d": {"inputs": ["close", "open", "high"], "func": rfl_101_upper_shadow_ratio_21d},
    "rfl_102_bounce_ret_5d_zscore_252d": {"inputs": ["close"], "func": rfl_102_bounce_ret_5d_zscore_252d},
    "rfl_103_bounce_ret_21d_zscore_252d": {"inputs": ["close"], "func": rfl_103_bounce_ret_21d_zscore_252d},
    "rfl_104_retracement_pct_63d_zscore_252d": {"inputs": ["close"], "func": rfl_104_retracement_pct_63d_zscore_252d},
    "rfl_105_bounce_ret_5d_pct_rank_252d": {"inputs": ["close"], "func": rfl_105_bounce_ret_5d_pct_rank_252d},
    "rfl_106_up_down_ratio_21d_pct_rank_252d": {"inputs": ["close"], "func": rfl_106_up_down_ratio_21d_pct_rank_252d},
    "rfl_107_vol_bounce_ratio_zscore_252d": {"inputs": ["close", "volume"], "func": rfl_107_vol_bounce_ratio_zscore_252d},
    "rfl_108_lower_high_fraction_21d_zscore_252d": {"inputs": ["high"], "func": rfl_108_lower_high_fraction_21d_zscore_252d},
    "rfl_109_bounce_fade_21d_zscore_252d": {"inputs": ["close"], "func": rfl_109_bounce_fade_21d_zscore_252d},
    "rfl_110_retracement_63d_expanding_rank": {"inputs": ["close"], "func": rfl_110_retracement_63d_expanding_rank},
    "rfl_111_net_ret_21d_expanding_rank": {"inputs": ["close"], "func": rfl_111_net_ret_21d_expanding_rank},
    "rfl_112_up_down_vol_ratio_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": rfl_112_up_down_vol_ratio_63d_pct_rank_252d},
    "rfl_113_ema_spread_5_21_pct_rank_252d": {"inputs": ["close"], "func": rfl_113_ema_spread_5_21_pct_rank_252d},
    "rfl_114_lower_high_count_63d_zscore_252d": {"inputs": ["high"], "func": rfl_114_lower_high_count_63d_zscore_252d},
    "rfl_115_bounce_failure_score_21d": {"inputs": ["close"], "func": rfl_115_bounce_failure_score_21d},
    "rfl_116_bounce_quality_vol_adjusted_21d": {"inputs": ["close", "volume"], "func": rfl_116_bounce_quality_vol_adjusted_21d},
    "rfl_117_failed_rally_rate_63d": {"inputs": ["close"], "func": rfl_117_failed_rally_rate_63d},
    "rfl_118_retracement_decay_score": {"inputs": ["close"], "func": rfl_118_retracement_decay_score},
    "rfl_119_recovery_failure_composite_63d": {"inputs": ["close", "high", "volume"], "func": rfl_119_recovery_failure_composite_63d},
    "rfl_120_up_ret_sum_vs_dn_ret_sum_21d": {"inputs": ["close"], "func": rfl_120_up_ret_sum_vs_dn_ret_sum_21d},
    "rfl_121_up_ret_sum_vs_dn_ret_sum_63d": {"inputs": ["close"], "func": rfl_121_up_ret_sum_vs_dn_ret_sum_63d},
    "rfl_122_max_bounce_then_fade_21d": {"inputs": ["close"], "func": rfl_122_max_bounce_then_fade_21d},
    "rfl_123_high_vol_bounce_count_21d": {"inputs": ["close", "volume"], "func": rfl_123_high_vol_bounce_count_21d},
    "rfl_124_high_vol_bounce_count_63d": {"inputs": ["close", "volume"], "func": rfl_124_high_vol_bounce_count_63d},
    "rfl_125_bounce_to_decline_vol_zscore_63d": {"inputs": ["close", "volume"], "func": rfl_125_bounce_to_decline_vol_zscore_63d},
    "rfl_126_close_to_range_position_21d": {"inputs": ["close", "high", "low"], "func": rfl_126_close_to_range_position_21d},
    "rfl_127_close_to_range_position_63d": {"inputs": ["close", "high", "low"], "func": rfl_127_close_to_range_position_63d},
    "rfl_128_intraday_bounce_fraction_21d": {"inputs": ["close", "open", "low"], "func": rfl_128_intraday_bounce_fraction_21d},
    "rfl_129_intraday_bounce_fraction_63d": {"inputs": ["close", "open", "low"], "func": rfl_129_intraday_bounce_fraction_63d},
    "rfl_130_open_gap_up_then_close_down_frac_21d": {"inputs": ["close", "open"], "func": rfl_130_open_gap_up_then_close_down_frac_21d},
    "rfl_131_open_gap_up_then_close_down_frac_63d": {"inputs": ["close", "open"], "func": rfl_131_open_gap_up_then_close_down_frac_63d},
    "rfl_132_consec_gap_up_fail": {"inputs": ["close", "open"], "func": rfl_132_consec_gap_up_fail},
    "rfl_133_high_minus_open_over_range_21d": {"inputs": ["close", "open", "high", "low"], "func": rfl_133_high_minus_open_over_range_21d},
    "rfl_134_close_minus_open_over_range_21d": {"inputs": ["close", "open", "high", "low"], "func": rfl_134_close_minus_open_over_range_21d},
    "rfl_135_close_minus_open_over_range_63d": {"inputs": ["close", "open", "high", "low"], "func": rfl_135_close_minus_open_over_range_63d},
    "rfl_136_intraday_high_reversal_21d": {"inputs": ["close", "high"], "func": rfl_136_intraday_high_reversal_21d},
    "rfl_137_intraday_high_reversal_63d": {"inputs": ["close", "high"], "func": rfl_137_intraday_high_reversal_63d},
    "rfl_138_upper_wick_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": rfl_138_upper_wick_fraction_21d},
    "rfl_139_high_below_21d_ago_high_count_63d": {"inputs": ["high"], "func": rfl_139_high_below_21d_ago_high_count_63d},
    "rfl_140_high_below_63d_ago_high_count_126d": {"inputs": ["high"], "func": rfl_140_high_below_63d_ago_high_count_126d},
    "rfl_141_close_below_21d_ago_close_count_63d": {"inputs": ["close"], "func": rfl_141_close_below_21d_ago_close_count_63d},
    "rfl_142_close_pct_from_52wk_high": {"inputs": ["close"], "func": rfl_142_close_pct_from_52wk_high},
    "rfl_143_close_pct_from_126d_high": {"inputs": ["close"], "func": rfl_143_close_pct_from_126d_high},
    "rfl_144_close_pct_from_63d_high": {"inputs": ["close"], "func": rfl_144_close_pct_from_63d_high},
    "rfl_145_retracement_vs_prior_bounce_21d": {"inputs": ["close"], "func": rfl_145_retracement_vs_prior_bounce_21d},
    "rfl_146_bounce_decay_score_63d": {"inputs": ["close"], "func": rfl_146_bounce_decay_score_63d},
    "rfl_147_lower_high_streak_21d_norm": {"inputs": ["high"], "func": rfl_147_lower_high_streak_21d_norm},
    "rfl_148_avg_bounce_per_decline_63d": {"inputs": ["close"], "func": rfl_148_avg_bounce_per_decline_63d},
    "rfl_149_bounce_attempt_count_63d": {"inputs": ["close"], "func": rfl_149_bounce_attempt_count_63d},
    "rfl_150_failed_bounce_composite_126d": {"inputs": ["close", "high", "volume"], "func": rfl_150_failed_bounce_composite_126d},
    "rfl_176_lower_wick_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": rfl_176_lower_wick_fraction_21d},
    "rfl_177_lower_wick_fraction_63d": {"inputs": ["close", "open", "high", "low"], "func": rfl_177_lower_wick_fraction_63d},
    "rfl_178_body_to_range_ratio_21d": {"inputs": ["close", "open", "high", "low"], "func": rfl_178_body_to_range_ratio_21d},
    "rfl_179_body_to_range_ratio_63d": {"inputs": ["close", "open", "high", "low"], "func": rfl_179_body_to_range_ratio_63d},
    "rfl_180_close_vs_sma63": {"inputs": ["close"], "func": rfl_180_close_vs_sma63},
    "rfl_181_close_vs_sma126": {"inputs": ["close"], "func": rfl_181_close_vs_sma126},
    "rfl_182_ema_spread_5_63": {"inputs": ["close"], "func": rfl_182_ema_spread_5_63},
    "rfl_183_consec_days_below_sma50": {"inputs": ["close"], "func": rfl_183_consec_days_below_sma50},
    "rfl_184_consec_days_below_sma200": {"inputs": ["close"], "func": rfl_184_consec_days_below_sma200},
    "rfl_185_close_below_sma_cross_count_63d": {"inputs": ["close"], "func": rfl_185_close_below_sma_cross_count_63d},
    "rfl_186_lower_close_lower_low_both_21d": {"inputs": ["close", "low"], "func": rfl_186_lower_close_lower_low_both_21d},
    "rfl_187_lower_close_lower_low_both_63d": {"inputs": ["close", "low"], "func": rfl_187_lower_close_lower_low_both_63d},
    "rfl_188_open_below_prior_low_count_21d": {"inputs": ["open", "low"], "func": rfl_188_open_below_prior_low_count_21d},
    "rfl_189_close_position_in_daily_range_21d": {"inputs": ["close", "high", "low"], "func": rfl_189_close_position_in_daily_range_21d},
    "rfl_190_close_position_in_daily_range_63d": {"inputs": ["close", "high", "low"], "func": rfl_190_close_position_in_daily_range_63d},
    "rfl_191_median_bounce_ret_21d": {"inputs": ["close"], "func": rfl_191_median_bounce_ret_21d},
    "rfl_192_median_bounce_ret_63d": {"inputs": ["close"], "func": rfl_192_median_bounce_ret_63d},
    "rfl_193_high_vol_bounce_count_126d": {"inputs": ["close", "volume"], "func": rfl_193_high_vol_bounce_count_126d},
    "rfl_194_vol_on_down_days_63d": {"inputs": ["close", "volume"], "func": rfl_194_vol_on_down_days_63d},
    "rfl_195_vol_trend_21d": {"inputs": ["volume"], "func": rfl_195_vol_trend_21d},
    "rfl_196_intraday_range_contraction_21d": {"inputs": ["high", "low"], "func": rfl_196_intraday_range_contraction_21d},
    "rfl_197_intraday_range_contraction_63d": {"inputs": ["high", "low"], "func": rfl_197_intraday_range_contraction_63d},
    "rfl_198_close_to_range_position_126d": {"inputs": ["close", "high", "low"], "func": rfl_198_close_to_range_position_126d},
    "rfl_199_bounce_failure_score_63d": {"inputs": ["close"], "func": rfl_199_bounce_failure_score_63d},
    "rfl_200_recovery_failure_composite_126d_v2": {"inputs": ["close", "high", "volume"], "func": rfl_200_recovery_failure_composite_126d_v2},
}
