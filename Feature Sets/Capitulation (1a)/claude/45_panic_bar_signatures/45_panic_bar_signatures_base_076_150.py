"""
45_panic_bar_signatures — Base Features 076-150
Domain: wide-range / long-tail / marubozu / climax single-bar panic pattern recognition
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _bar_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday price range (high - low)."""
    return high - low


def _lower_tail(open: pd.Series, close: pd.Series, low: pd.Series) -> pd.Series:
    """Lower wick = min(open, close) - low."""
    return pd.concat([open, close], axis=1).min(axis=1) - low


def _upper_tail(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Upper wick = high - max(open, close)."""
    return high - pd.concat([open, close], axis=1).max(axis=1)


def _body(open: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute candle body size."""
    return (close - open).abs()


def _avg_range(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Rolling average of bar range over w periods."""
    return _rolling_mean(_bar_range(high, low), w)


def _close_loc(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close location value in [0,1]: 0=at low, 1=at high."""
    rng = _bar_range(high, low)
    return _safe_div(close - low, rng)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Panic-bar recency and decay signals ---

def pbs_076_days_since_last_panic_bar(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Days since last panic bar (>2x avg range, close<open, clv<0.25)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


def pbs_077_days_since_last_hammer(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Days since last hammer bar (lower tail > 50% range)."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    flag = (_safe_div(lt, rng) > 0.50).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


def pbs_078_panic_bar_recency_decay_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Exponential decay score of panic bar recency with 21-day half-life."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def pbs_079_panic_bar_recency_decay_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Exponential decay score of panic bar recency with 5-day half-life."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    return flag.ewm(span=_TD_WEEK, min_periods=1).mean()


def pbs_080_exhaustion_bar_recency_decay_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Exponential decay of exhaustion bar recency with 21-day half-life."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    flag = ((rng > 2.0 * avg) & (lt_frac > 0.40)).astype(float)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def pbs_081_hammer_recency_decay_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Exponential decay of hammer bar recency with 21-day half-life."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    flag = (_safe_div(lt, rng) > 0.50).astype(float)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def pbs_082_wide_range_bar_ewm_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day EWM of wide-range bar flag (short-term panic bar density)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    return flag.ewm(span=_TD_WEEK, min_periods=1).mean()


def pbs_083_panic_cluster_flag_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 2+ panic bars in the last 5 days (panic cluster event)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    cnt = _rolling_sum(flag, _TD_WEEK)
    return (cnt >= 2).astype(float)


def pbs_084_panic_cluster_flag_10d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 3+ panic bars in the last 10 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    cnt = _rolling_sum(flag, 10)
    return (cnt >= 3).astype(float)


def pbs_085_panic_bar_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days that are panic bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


def pbs_086_panic_bar_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days that are panic bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def pbs_087_wide_range_bar_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days that are wide-range bars (>2x 21d avg)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def pbs_088_panic_bar_pct_rank_21d_freq(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day panic bar frequency in 252-day history."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    freq21 = _rolling_sum(flag, _TD_MON)
    return freq21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_089_days_since_last_outside_bar(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last outside bar (today high > prior high AND low < prior low)."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


def pbs_090_days_since_last_key_reversal_up(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Days since last key-reversal-up bar (new low + close above prior close)."""
    flag = ((low < low.shift(1)) & (close > close.shift(1))).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


# --- Group G (091-105): Volume-conditioned and marubozu/climax extended features ---

def pbs_091_panic_bar_volume_ratio(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume divided by 21-day avg volume on panic bar days, else NaN."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = (rng > 2.0 * avg) & (close < open) & (clv <= 0.25)
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    return ratio.where(is_panic, np.nan)


def pbs_092_wide_range_bar_vol_ratio(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on wide-range bars vs 21-day avg (measure of urgency)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    is_wide = rng > 2.0 * avg
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    return ratio.where(is_wide, np.nan)


def pbs_093_exhaustion_bar_vol_ratio(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on exhaustion bars (range>2x avg, lower tail>40%)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    is_exhaust = (rng > 2.0 * avg) & (lt_frac > 0.40)
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    return ratio.where(is_exhaust, np.nan)


def pbs_094_panic_bar_high_vol_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: panic bar AND volume > 2x 21-day avg (confirmed panic)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25) & (volume > 2.0 * avg_vol)).astype(float)


def pbs_095_bearish_marubozu_vol_confirmed_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: bearish marubozu (body>80% range) AND volume > 2x 21-day median (volume-confirmed full-conviction panic).
    The combination of no wick and extreme volume signals maximum selling conviction."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    med_vol = _rolling_median(volume, _TD_MON)
    return ((body_frac >= 0.80) & (close < open) & (volume > 2.0 * med_vol)).astype(float)


def pbs_096_panic_vol_intensity_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on panic bars in trailing 21 days (panic volume accumulation)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    panic_vol = volume * is_panic
    return _rolling_sum(panic_vol, _TD_MON)


def pbs_097_panic_vol_intensity_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on panic bars in trailing 63 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    panic_vol = volume * is_panic
    return _rolling_sum(panic_vol, _TD_QTR)


def pbs_098_panic_vol_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on panic bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    panic_vol = _rolling_sum(volume * is_panic, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(panic_vol, total_vol)


def pbs_099_wide_range_vol_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume on wide-range days (>2x avg) in trailing 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    is_wide = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(volume * is_wide, _TD_MON)


def pbs_100_range_times_volume_zscore(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (range * volume) product, a panic energy proxy."""
    rng = _bar_range(high, low)
    rv = rng * volume
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    return _safe_div(rv - m, s)


def pbs_101_range_times_volume_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of range*volume in trailing 252 days."""
    rng = _bar_range(high, low)
    rv = rng * volume
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_102_climax_intensity_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of climax intensity (range_z * vol_z) in 252-day distribution."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    intensity = rng_z * vol_z
    return intensity.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_103_down_climax_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down-climax bars (wide bear + extreme vol + clv<0.20) in trailing 21 days."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open) & (clv <= 0.20)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def pbs_104_down_climax_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down-climax bars in trailing 63 days."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    clv = _close_loc(close, high, low)
    flag = ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open) & (clv <= 0.20)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def pbs_105_days_since_last_selling_climax(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Days elapsed since last selling climax bar (wide range + extreme volume + close<open)."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open)).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


# --- Group H (106-120): Panic bar intensity combiners and composite scores ---

def pbs_106_range_lower_tail_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Combined score: log1p(range_ratio_21d) + log1p(lower_tail_ratio_21d)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_r = _safe_div(lt, avg)
    return np.log1p(rr.fillna(0)) + np.log1p(lt_r.fillna(0))


def pbs_107_panic_bar_composite_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Composite: range_zscore_252d * (1 - clv) * bear_flag."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m, s).clip(lower=0.0)
    clv = _close_loc(close, high, low)
    bear = (close < open).astype(float)
    return rng_z * (1.0 - clv.fillna(0.5)) * bear


def pbs_108_panic_bar_composite_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling average of composite panic bar score."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _rolling_mean(score, _TD_MON)


def pbs_109_panic_bar_composite_63d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling average of composite panic bar score."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _rolling_mean(score, _TD_QTR)


def pbs_110_panic_bar_composite_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of composite panic score in 252-day history."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_111_range_body_ratio(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Bar range divided by body size (high ratio = wide, small-body panic bar)."""
    rng = _bar_range(high, low)
    body = _body(open, close).clip(lower=_EPS)
    return _safe_div(rng, body)


def pbs_112_small_body_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: range > 2x avg AND body < 20% of range (doji-like panic bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    body = _body(open, close)
    body_frac = _safe_div(body, rng)
    return ((rng > 2.0 * avg) & (body_frac < 0.20)).astype(float)


def pbs_113_lower_tail_plus_range_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Score: (lower_tail / avg_range_21d) * (range / avg_range_21d)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_r = _safe_div(lt, avg)
    rr = _safe_div(rng, avg)
    return lt_r * rr


def pbs_114_lower_tail_plus_range_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of lower_tail*range score in 252 days."""
    score = pbs_113_lower_tail_plus_range_score(close, high, low, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_115_extreme_bear_bar_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Score for extreme downside bar: range_ratio * close_to_low_fraction."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    clv = _close_loc(close, high, low)
    return rr * (1.0 - clv.fillna(0.5))


def pbs_116_extreme_bear_bar_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of extreme bear bar score in 252 days."""
    score = pbs_115_extreme_bear_bar_score(close, high, low, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_117_upper_tail_suppression_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: upper tail < 10% of range (no rally rejection, directional panic bar)."""
    rng = _bar_range(high, low)
    ut = _upper_tail(open, close, high)
    ut_frac = _safe_div(ut, rng.clip(lower=_EPS))
    return (ut_frac < 0.10).astype(float)


def pbs_118_pure_bear_bar_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: close < open AND upper tail < 10% range AND lower tail < 10% range."""
    rng = _bar_range(high, low)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    ut_frac = _safe_div(ut, rng.clip(lower=_EPS))
    return ((close < open) & (lt_frac < 0.10) & (ut_frac < 0.10)).astype(float)


def pbs_119_pure_bear_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: pure bear bar (small wicks) AND range > 2x 21-day avg."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    ut_frac = _safe_div(ut, rng.clip(lower=_EPS))
    return ((close < open) & (lt_frac < 0.10) & (ut_frac < 0.10) & (rng > 2.0 * avg)).astype(float)


def pbs_120_panic_bar_score_ewm_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """EWM-21d of composite panic bar score (smooth trend in panic morphology)."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _ewm_mean(score, _TD_MON)


# --- Group I (121-135): Panic-bar statistics relative to recent lows ---

def pbs_121_wide_range_bar_at_new_21d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: wide-range bar (>2x avg) AND close at new 21-day low."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return ((rng > 2.0 * avg) & (close < roll_min)).astype(float)


def pbs_122_wide_range_bar_at_new_63d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: wide-range bar (>2x avg) AND close at new 63-day low."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return ((rng > 2.0 * avg) & (close < roll_min)).astype(float)


def pbs_123_wide_range_bar_at_new_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: wide-range bar AND close at new 252-day low (capitulation signal)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return ((rng > 2.0 * avg) & (close < roll_min)).astype(float)


def pbs_124_panic_bar_count_at_new_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of wide-range bars at new 21-day lows in trailing 21 days."""
    flag = pbs_121_wide_range_bar_at_new_21d_low(close, high, low)
    return _rolling_sum(flag, _TD_MON)


def pbs_125_panic_bar_count_at_new_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of wide-range bars at new 63-day lows in trailing 63 days."""
    flag = pbs_122_wide_range_bar_at_new_63d_low(close, high, low)
    return _rolling_sum(flag, _TD_QTR)


def pbs_126_marubozu_at_new_252d_low_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: bearish marubozu (body>80%) AND close at new 252-day low (capitulation marubozu).
    Marks the worst-conviction panic selling at multi-year lows."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return ((body_frac >= 0.80) & (close < open) & (close < roll_min)).astype(float)


def pbs_127_exhaustion_at_52wk_low_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: exhaustion bar (wide + lower-tail) AND close at new 52-week low."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return ((rng > 2.0 * avg) & (lt_frac > 0.40) & (close < roll_min)).astype(float)


def pbs_128_panic_range_at_prior_support(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: wide bar AND low within 2% of prior 63-day low (testing support)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    prior63_low = low.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    near_support = (low - prior63_low).abs() / prior63_low.clip(lower=_EPS) < 0.02
    return ((rng > 2.0 * avg) & near_support).astype(float)


def pbs_129_range_ratio_63d_median(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 63-day median range."""
    rng = _bar_range(high, low)
    med = _rolling_median(rng, _TD_QTR)
    return _safe_div(rng, med)


def pbs_130_range_ratio_252d_median(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 252-day median range."""
    rng = _bar_range(high, low)
    med = _rolling_median(rng, _TD_YEAR)
    return _safe_div(rng, med)


def pbs_131_close_dist_from_session_low_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close distance from session low as pct of close price."""
    return _safe_div(close - low, close.clip(lower=_EPS))


def pbs_132_close_dist_from_session_low_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of (close-low)/close in 252-day distribution."""
    dist = pbs_131_close_dist_from_session_low_pct(close, high, low)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_133_session_low_to_open_dist_pct(open: pd.Series, low: pd.Series) -> pd.Series:
    """(open - low) / open: how far below open did price trade (intraday sell-off depth)."""
    return _safe_div(open - low, open.clip(lower=_EPS)).clip(lower=0.0)


def pbs_134_session_low_below_open_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: session low > 3% below open AND range > 2x avg (deep intraday panic)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    depth = _safe_div(open - low, open.clip(lower=_EPS))
    return ((depth > 0.03) & (rng > 2.0 * avg)).astype(float)


def pbs_135_panic_bar_below_lower_bb(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: wide-range bear bar AND close below 2-sigma lower Bollinger Band."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    sma = _rolling_mean(close, _TD_MON)
    std = _rolling_std(close, _TD_MON)
    lower_bb = sma - 2.0 * std
    return ((rng > 2.0 * avg_rng) & (close < open) & (close < lower_bb)).astype(float)


# --- Group J (136-150): Multi-bar aggregates, climax/marubozu scores, normalized panic ---

def pbs_136_panic_score_max_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum panic composite score seen in trailing 21 days."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _rolling_max(score, _TD_MON)


def pbs_137_panic_score_max_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum panic composite score seen in trailing 63 days."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _rolling_max(score, _TD_QTR)


def pbs_138_panic_score_max_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum panic composite score seen in trailing 252 days."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return _rolling_max(score, _TD_YEAR)


def pbs_139_current_panic_vs_max_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Current panic score as fraction of 252-day max panic score."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    mx = _rolling_max(score, _TD_YEAR)
    return _safe_div(score, mx)


def pbs_140_range_ratio_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of daily range ratios (vs 21d avg) over trailing 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return _rolling_sum(rr, _TD_MON)


def pbs_141_range_ratio_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of daily range ratios over trailing 63 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    return _rolling_sum(rr, _TD_QTR)


def pbs_142_lower_tail_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of lower tails (abs dollar) over trailing 21 days."""
    lt = _lower_tail(open, close, low)
    return _rolling_sum(lt, _TD_MON)


def pbs_143_lower_tail_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of lower tails over trailing 63 days."""
    lt = _lower_tail(open, close, low)
    return _rolling_sum(lt, _TD_QTR)


def pbs_144_lower_tail_ratio_range_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of (lower_tail / range) ratio."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    return _rolling_mean(frac, _TD_MON)


def pbs_145_lower_tail_ratio_range_63d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63-day average of (lower_tail / range) ratio."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    frac = _safe_div(lt, rng.clip(lower=_EPS))
    return _rolling_mean(frac, _TD_QTR)


def pbs_146_clv_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average close location value (low avg = price persistently closing near lows)."""
    clv = _close_loc(close, high, low)
    return _rolling_mean(clv, _TD_MON)


def pbs_147_clv_63d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day average close location value."""
    clv = _close_loc(close, high, low)
    return _rolling_mean(clv, _TD_QTR)


def pbs_148_clv_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of CLV in 252-day distribution (low rank = panic close)."""
    clv = _close_loc(close, high, low)
    return clv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_149_panic_score_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of panic composite score (all-history)."""
    score = pbs_107_panic_bar_composite_score(close, high, low, open)
    return score.expanding(min_periods=5).rank(pct=True)


def pbs_150_panic_bar_regime_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Regime score: panic_bar_fraction_21d + exhaustion_score_21d_avg + vol_z_score."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = _close_loc(close, high, low)
    is_panic = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    pf21 = _rolling_sum(is_panic, _TD_MON) / _TD_MON
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    exh_score = _rolling_mean(_safe_div(rng, avg) * lt_frac, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    std_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, std_vol).clip(lower=0.0)
    return pf21 + exh_score.fillna(0.0) + vol_z.fillna(0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_REGISTRY_076_150 = {
    "pbs_076_days_since_last_panic_bar": {"inputs": ["close", "high", "low", "open"], "func": pbs_076_days_since_last_panic_bar},
    "pbs_077_days_since_last_hammer": {"inputs": ["close", "high", "low", "open"], "func": pbs_077_days_since_last_hammer},
    "pbs_078_panic_bar_recency_decay_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_078_panic_bar_recency_decay_21d},
    "pbs_079_panic_bar_recency_decay_5d": {"inputs": ["close", "high", "low", "open"], "func": pbs_079_panic_bar_recency_decay_5d},
    "pbs_080_exhaustion_bar_recency_decay_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_080_exhaustion_bar_recency_decay_21d},
    "pbs_081_hammer_recency_decay_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_081_hammer_recency_decay_21d},
    "pbs_082_wide_range_bar_ewm_5d": {"inputs": ["close", "high", "low"], "func": pbs_082_wide_range_bar_ewm_5d},
    "pbs_083_panic_cluster_flag_5d": {"inputs": ["close", "high", "low", "open"], "func": pbs_083_panic_cluster_flag_5d},
    "pbs_084_panic_cluster_flag_10d": {"inputs": ["close", "high", "low", "open"], "func": pbs_084_panic_cluster_flag_10d},
    "pbs_085_panic_bar_fraction_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_085_panic_bar_fraction_21d},
    "pbs_086_panic_bar_fraction_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_086_panic_bar_fraction_63d},
    "pbs_087_wide_range_bar_fraction_252d": {"inputs": ["close", "high", "low"], "func": pbs_087_wide_range_bar_fraction_252d},
    "pbs_088_panic_bar_pct_rank_21d_freq": {"inputs": ["close", "high", "low", "open"], "func": pbs_088_panic_bar_pct_rank_21d_freq},
    "pbs_089_days_since_last_outside_bar": {"inputs": ["high", "low"], "func": pbs_089_days_since_last_outside_bar},
    "pbs_090_days_since_last_key_reversal_up": {"inputs": ["close", "high", "low", "open"], "func": pbs_090_days_since_last_key_reversal_up},
    "pbs_091_panic_bar_volume_ratio": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_091_panic_bar_volume_ratio},
    "pbs_092_wide_range_bar_vol_ratio": {"inputs": ["close", "high", "low", "volume"], "func": pbs_092_wide_range_bar_vol_ratio},
    "pbs_093_exhaustion_bar_vol_ratio": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_093_exhaustion_bar_vol_ratio},
    "pbs_094_panic_bar_high_vol_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_094_panic_bar_high_vol_flag},
    "pbs_095_bearish_marubozu_vol_confirmed_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_095_bearish_marubozu_vol_confirmed_flag},
    "pbs_096_panic_vol_intensity_sum_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_096_panic_vol_intensity_sum_21d},
    "pbs_097_panic_vol_intensity_sum_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_097_panic_vol_intensity_sum_63d},
    "pbs_098_panic_vol_fraction_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_098_panic_vol_fraction_21d},
    "pbs_099_wide_range_vol_sum_21d": {"inputs": ["close", "high", "low", "volume"], "func": pbs_099_wide_range_vol_sum_21d},
    "pbs_100_range_times_volume_zscore": {"inputs": ["close", "high", "low", "volume"], "func": pbs_100_range_times_volume_zscore},
    "pbs_101_range_times_volume_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": pbs_101_range_times_volume_pct_rank_252d},
    "pbs_102_climax_intensity_pct_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_102_climax_intensity_pct_rank_252d},
    "pbs_103_down_climax_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_103_down_climax_count_21d},
    "pbs_104_down_climax_count_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_104_down_climax_count_63d},
    "pbs_105_days_since_last_selling_climax": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_105_days_since_last_selling_climax},
    "pbs_106_range_lower_tail_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_106_range_lower_tail_score},
    "pbs_107_panic_bar_composite_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_107_panic_bar_composite_score},
    "pbs_108_panic_bar_composite_21d_avg": {"inputs": ["close", "high", "low", "open"], "func": pbs_108_panic_bar_composite_21d_avg},
    "pbs_109_panic_bar_composite_63d_avg": {"inputs": ["close", "high", "low", "open"], "func": pbs_109_panic_bar_composite_63d_avg},
    "pbs_110_panic_bar_composite_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_110_panic_bar_composite_pct_rank_252d},
    "pbs_111_range_body_ratio": {"inputs": ["close", "high", "low", "open"], "func": pbs_111_range_body_ratio},
    "pbs_112_small_body_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_112_small_body_wide_range_flag},
    "pbs_113_lower_tail_plus_range_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_113_lower_tail_plus_range_score},
    "pbs_114_lower_tail_plus_range_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_114_lower_tail_plus_range_pct_rank_252d},
    "pbs_115_extreme_bear_bar_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_115_extreme_bear_bar_score},
    "pbs_116_extreme_bear_bar_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_116_extreme_bear_bar_pct_rank_252d},
    "pbs_117_upper_tail_suppression_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_117_upper_tail_suppression_flag},
    "pbs_118_pure_bear_bar_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_118_pure_bear_bar_flag},
    "pbs_119_pure_bear_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_119_pure_bear_wide_range_flag},
    "pbs_120_panic_bar_score_ewm_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_120_panic_bar_score_ewm_21d},
    "pbs_121_wide_range_bar_at_new_21d_low": {"inputs": ["close", "high", "low"], "func": pbs_121_wide_range_bar_at_new_21d_low},
    "pbs_122_wide_range_bar_at_new_63d_low": {"inputs": ["close", "high", "low"], "func": pbs_122_wide_range_bar_at_new_63d_low},
    "pbs_123_wide_range_bar_at_new_252d_low": {"inputs": ["close", "high", "low"], "func": pbs_123_wide_range_bar_at_new_252d_low},
    "pbs_124_panic_bar_count_at_new_low_21d": {"inputs": ["close", "high", "low"], "func": pbs_124_panic_bar_count_at_new_low_21d},
    "pbs_125_panic_bar_count_at_new_low_63d": {"inputs": ["close", "high", "low"], "func": pbs_125_panic_bar_count_at_new_low_63d},
    "pbs_126_marubozu_at_new_252d_low_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_126_marubozu_at_new_252d_low_flag},
    "pbs_127_exhaustion_at_52wk_low_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_127_exhaustion_at_52wk_low_flag},
    "pbs_128_panic_range_at_prior_support": {"inputs": ["close", "high", "low"], "func": pbs_128_panic_range_at_prior_support},
    "pbs_129_range_ratio_63d_median": {"inputs": ["close", "high", "low"], "func": pbs_129_range_ratio_63d_median},
    "pbs_130_range_ratio_252d_median": {"inputs": ["close", "high", "low"], "func": pbs_130_range_ratio_252d_median},
    "pbs_131_close_dist_from_session_low_pct": {"inputs": ["close", "high", "low"], "func": pbs_131_close_dist_from_session_low_pct},
    "pbs_132_close_dist_from_session_low_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": pbs_132_close_dist_from_session_low_pct_rank_252d},
    "pbs_133_session_low_to_open_dist_pct": {"inputs": ["open", "low"], "func": pbs_133_session_low_to_open_dist_pct},
    "pbs_134_session_low_below_open_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_134_session_low_below_open_wide_range_flag},
    "pbs_135_panic_bar_below_lower_bb": {"inputs": ["close", "high", "low", "open"], "func": pbs_135_panic_bar_below_lower_bb},
    "pbs_136_panic_score_max_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_136_panic_score_max_21d},
    "pbs_137_panic_score_max_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_137_panic_score_max_63d},
    "pbs_138_panic_score_max_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_138_panic_score_max_252d},
    "pbs_139_current_panic_vs_max_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_139_current_panic_vs_max_252d},
    "pbs_140_range_ratio_sum_21d": {"inputs": ["close", "high", "low"], "func": pbs_140_range_ratio_sum_21d},
    "pbs_141_range_ratio_sum_63d": {"inputs": ["close", "high", "low"], "func": pbs_141_range_ratio_sum_63d},
    "pbs_142_lower_tail_sum_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_142_lower_tail_sum_21d},
    "pbs_143_lower_tail_sum_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_143_lower_tail_sum_63d},
    "pbs_144_lower_tail_ratio_range_21d_avg": {"inputs": ["close", "high", "low", "open"], "func": pbs_144_lower_tail_ratio_range_21d_avg},
    "pbs_145_lower_tail_ratio_range_63d_avg": {"inputs": ["close", "high", "low", "open"], "func": pbs_145_lower_tail_ratio_range_63d_avg},
    "pbs_146_clv_21d_avg": {"inputs": ["close", "high", "low"], "func": pbs_146_clv_21d_avg},
    "pbs_147_clv_63d_avg": {"inputs": ["close", "high", "low"], "func": pbs_147_clv_63d_avg},
    "pbs_148_clv_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": pbs_148_clv_pct_rank_252d},
    "pbs_149_panic_score_expanding_rank": {"inputs": ["close", "high", "low", "open"], "func": pbs_149_panic_score_expanding_rank},
    "pbs_150_panic_bar_regime_score": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_150_panic_bar_regime_score},
}
