"""
45_panic_bar_signatures — Base Features 001-075
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Wide-range bar detection ---

def pbs_001_range_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 21-day average range (wide-range bar intensity)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return _safe_div(rng, avg)


def pbs_002_range_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 63-day average range."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_QTR)
    return _safe_div(rng, avg)


def pbs_003_range_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 252-day average range."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_YEAR)
    return _safe_div(rng, avg)


def pbs_004_wide_range_bar_flag_2x_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: bar range > 2x 21-day average range (discrete wide-range bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return (rng > 2.0 * avg).astype(float)


def pbs_005_wide_range_bar_flag_3x_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: bar range > 3x 21-day average range (extreme wide-range bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return (rng > 3.0 * avg).astype(float)


def pbs_006_wide_range_bar_flag_2x_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: bar range > 2x 63-day average range."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_QTR)
    return (rng > 2.0 * avg).astype(float)


def pbs_007_wide_range_down_bar_flag_2x_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: close < open AND range > 2x 21-day avg range (wide-range bear bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return ((close < open) & (rng > 2.0 * avg)).astype(float)


def pbs_008_wide_range_down_bar_flag_3x_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: close < open AND range > 3x 21-day avg range (extreme bear bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return ((close < open) & (rng > 3.0 * avg)).astype(float)


def pbs_009_range_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's bar range within trailing 252-day range distribution."""
    rng = _bar_range(high, low)
    return rng.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_010_range_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's bar range within trailing 63-day range distribution."""
    rng = _bar_range(high, low)
    return rng.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def pbs_011_range_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of bar range relative to 252-day rolling mean and std."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_YEAR)
    s = _rolling_std(rng, _TD_YEAR)
    return _safe_div(rng - m, s)


def pbs_012_range_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of bar range relative to 63-day rolling mean and std."""
    rng = _bar_range(high, low)
    m = _rolling_mean(rng, _TD_QTR)
    s = _rolling_std(rng, _TD_QTR)
    return _safe_div(rng - m, s)


def pbs_013_range_vs_21d_median(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range divided by 21-day median range."""
    rng = _bar_range(high, low)
    med = _rolling_median(rng, _TD_MON)
    return _safe_div(rng, med)


def pbs_014_range_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of bar range (all-history)."""
    rng = _bar_range(high, low)
    return rng.expanding(min_periods=5).rank(pct=True)


def pbs_015_range_multiple_above_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Excess range multiple: (range - avg_21d) / avg_21d, clipped at 0 below."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    excess = _safe_div(rng - avg, avg)
    return excess.clip(lower=0.0)


# --- Group B (016-030): Long-lower-tail / hammer capitulation patterns ---

def pbs_016_lower_tail_ratio_range(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail as fraction of total bar range."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    return _safe_div(lt, rng)


def pbs_017_lower_tail_ratio_21d_avg_range(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail divided by 21-day average bar range."""
    lt = _lower_tail(open, close, low)
    avg = _avg_range(high, low, _TD_MON)
    return _safe_div(lt, avg)


def pbs_018_lower_tail_ratio_63d_avg_range(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail divided by 63-day average bar range."""
    lt = _lower_tail(open, close, low)
    avg = _avg_range(high, low, _TD_QTR)
    return _safe_div(lt, avg)


def pbs_019_hammer_flag_lt50pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 50% of bar range (classic hammer morphology)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    return (_safe_div(lt, rng) > 0.50).astype(float)


def pbs_020_hammer_flag_lt60pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 60% of bar range (strong hammer)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    return (_safe_div(lt, rng) > 0.60).astype(float)


def pbs_021_hammer_flag_lt70pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 70% of bar range (very strong hammer)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    return (_safe_div(lt, rng) > 0.70).astype(float)


def pbs_022_long_lower_tail_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 50% of range AND range > 2x 21-day avg (panic hammer)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return ((_safe_div(lt, rng) > 0.50) & (rng > 2.0 * avg)).astype(float)


def pbs_023_lower_tail_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of lower tail length vs 252-day distribution."""
    lt = _lower_tail(open, close, low)
    m = _rolling_mean(lt, _TD_YEAR)
    s = _rolling_std(lt, _TD_YEAR)
    return _safe_div(lt - m, s)


def pbs_024_lower_tail_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of lower tail in trailing 252-day distribution."""
    lt = _lower_tail(open, close, low)
    return lt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_025_lower_tail_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of lower tail in trailing 63-day distribution."""
    lt = _lower_tail(open, close, low)
    return lt.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def pbs_026_lower_tail_vs_upper_tail_ratio(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail divided by upper tail (high ratio = downside wick dominance)."""
    lt = _lower_tail(open, close, low)
    ut = _upper_tail(open, close, high)
    return _safe_div(lt, ut.clip(lower=_EPS))


def pbs_027_lower_tail_ratio_body(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail divided by body size."""
    lt = _lower_tail(open, close, low)
    body = _body(open, close).clip(lower=_EPS)
    return _safe_div(lt, body)


def pbs_028_lower_tail_gt2x_body_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 2x body (pin bar / rejection candle)."""
    lt = _lower_tail(open, close, low)
    body = _body(open, close).clip(lower=_EPS)
    return (lt > 2.0 * body).astype(float)


def pbs_029_lower_tail_abs_21d_multiple(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Lower tail divided by 21-day average lower tail."""
    lt = _lower_tail(open, close, low)
    avg_lt = _rolling_mean(lt, _TD_MON)
    return _safe_div(lt, avg_lt)


def pbs_030_lower_tail_down_bar_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: lower tail > 50% of range AND close < open (bearish hammer)."""
    lt = _lower_tail(open, close, low)
    rng = _bar_range(high, low)
    return ((_safe_div(lt, rng) > 0.50) & (close < open)).astype(float)


# --- Group C (031-045): Wide-range down bars closing near the low ---

def pbs_031_close_location_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close location value: (close-low)/(high-low), 0=at low, 1=at high."""
    rng = _bar_range(high, low)
    return _safe_div(close - low, rng)


def pbs_032_close_near_low_flag_10pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close within bottom 10% of bar range (panic close near low)."""
    clv = pbs_031_close_location_value(close, high, low)
    return (clv <= 0.10).astype(float)


def pbs_033_close_near_low_flag_20pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close within bottom 20% of bar range."""
    clv = pbs_031_close_location_value(close, high, low)
    return (clv <= 0.20).astype(float)


def pbs_034_wide_down_close_low_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: close < open AND close near low 20% AND range > 2x 21-day avg."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = pbs_031_close_location_value(close, high, low)
    return ((close < open) & (clv <= 0.20) & (rng > 2.0 * avg)).astype(float)


def pbs_035_wide_down_close_low_flag_3x(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: close < open AND close near low 20% AND range > 3x 21-day avg."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = pbs_031_close_location_value(close, high, low)
    return ((close < open) & (clv <= 0.20) & (rng > 3.0 * avg)).astype(float)


def pbs_036_down_close_low_range_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Panic close score: range_ratio_21d * (1 - close_location) * bear_bar."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    clv = pbs_031_close_location_value(close, high, low)
    bear = (close < open).astype(float)
    return rr * (1.0 - clv.fillna(0.5)) * bear


def pbs_037_gap_down_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: gap-down open below prior close AND range > 2x 21-day avg."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    gap_down = open < close.shift(1)
    return (gap_down & (rng > 2.0 * avg)).astype(float)


def pbs_038_close_below_prior_low_wide_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < prior low AND range > 2x 21-day avg (breakdown + wide bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    return ((close < low.shift(1)) & (rng > 2.0 * avg)).astype(float)


def pbs_039_range_pct_close_loss(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Product of range ratio and absolute pct close-to-open loss on bear bars."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    pct_loss = ((open - close) / open.clip(lower=_EPS)).clip(lower=0.0)
    return rr * pct_loss


def pbs_040_wide_range_bar_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of wide-range bars (>2x 21-day avg) in trailing 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(flag, _TD_MON)


def pbs_041_wide_range_bar_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of wide-range bars (>2x 21-day avg) in trailing 63 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def pbs_042_wide_range_down_bar_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of wide-range bear bars (>2x avg, close<open) in trailing 21 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = ((rng > 2.0 * avg) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def pbs_043_wide_range_down_bar_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of wide-range bear bars (>2x avg, close<open) in trailing 63 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = ((rng > 2.0 * avg) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def pbs_044_panic_bar_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of panic bars (>2x avg range, close<open, clv<0.25) in 252 days."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    clv = pbs_031_close_location_value(close, high, low)
    flag = ((rng > 2.0 * avg) & (close < open) & (clv <= 0.25)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def pbs_045_days_since_last_wide_range_bar(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since most recent wide-range bar (>2x 21-day avg)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    flag = (rng > 2.0 * avg).astype(float)
    idx = np.arange(len(flag), dtype=float)
    last = flag.where(flag > 0).expanding().apply(
        lambda x: idx[np.where(x > 0)[0][-1]] if np.any(x > 0) else np.nan, raw=False)
    return (pd.Series(idx, index=flag.index) - last).clip(lower=0.0)


# --- Group D (046-057): Exhaustion bars (huge range + close off the low) ---

def pbs_046_exhaustion_bar_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: range > 2x avg AND lower tail > 40% range (exhaustion / spring bar)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng)
    return ((rng > 2.0 * avg) & (lt_frac > 0.40)).astype(float)


def pbs_047_exhaustion_bar_flag_strong(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: range > 2x avg AND lower tail > 50% range AND close in upper 40% (reversal)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng)
    clv = pbs_031_close_location_value(close, high, low)
    return ((rng > 2.0 * avg) & (lt_frac > 0.50) & (clv >= 0.60)).astype(float)


def pbs_048_exhaustion_close_up_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: range > 2x avg AND close > open AND lower tail > 40% range."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng)
    return ((rng > 2.0 * avg) & (close > open) & (lt_frac > 0.40)).astype(float)


def pbs_049_exhaustion_bar_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Exhaustion score: range_ratio_21d * lower_tail_fraction (continuous)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    rr = _safe_div(rng, avg)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    return rr * lt_frac


def pbs_050_exhaustion_bar_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of exhaustion bars (>2x avg, lower tail >40% range) in 63 days."""
    flag = pbs_046_exhaustion_bar_flag(close, high, low, open)
    return _rolling_sum(flag, _TD_QTR)


def pbs_051_exhaustion_bar_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of exhaustion bars in trailing 252 days."""
    flag = pbs_046_exhaustion_bar_flag(close, high, low, open)
    return _rolling_sum(flag, _TD_YEAR)


def pbs_052_exhaustion_score_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of exhaustion bar score vs 252-day distribution."""
    score = pbs_049_exhaustion_bar_score(close, high, low, open)
    m = _rolling_mean(score, _TD_YEAR)
    s = _rolling_std(score, _TD_YEAR)
    return _safe_div(score - m, s)


def pbs_053_exhaustion_bar_3x_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: range > 3x avg AND lower tail > 40% range (extreme exhaustion)."""
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng)
    return ((rng > 3.0 * avg) & (lt_frac > 0.40)).astype(float)


def pbs_054_exhaustion_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of exhaustion bar score in trailing 252-day distribution."""
    score = pbs_049_exhaustion_bar_score(close, high, low, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def pbs_055_outside_bar_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's high > prior high AND today's low < prior low (outside bar)."""
    return ((high > high.shift(1)) & (low < low.shift(1))).astype(float)


def pbs_056_outside_bar_down_close_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: outside bar with close < open (bearish engulfing-style)."""
    ob = pbs_055_outside_bar_flag(high, low)
    return ((ob > 0) & (close < open)).astype(float)


def pbs_057_key_reversal_up_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: new intraday low then close above prior close (key reversal up / capitulation reversal)."""
    new_low = low < low.shift(1)
    close_above_prior = close > close.shift(1)
    return (new_low & close_above_prior).astype(float)


# --- Group E (058-075): Marubozu bars — full-conviction bars with minimal wicks ---

def pbs_058_body_range_ratio(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Body divided by bar range (marubozu degree: 1.0 = perfect marubozu, 0 = doji)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    return _safe_div(body, rng.clip(lower=_EPS))


def pbs_059_bearish_marubozu_flag_90pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: body/range > 90% AND close < open (near-perfect bearish marubozu = full-conviction panic selling)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((body_frac >= 0.90) & (close < open)).astype(float)


def pbs_060_bearish_marubozu_flag_80pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: body/range > 80% AND close < open (strong bearish marubozu)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((body_frac >= 0.80) & (close < open)).astype(float)


def pbs_061_bullish_marubozu_flag_90pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: body/range > 90% AND close > open (bullish marubozu = potential capitulation end)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((body_frac >= 0.90) & (close > open)).astype(float)


def pbs_062_bullish_marubozu_flag_80pct(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: body/range > 80% AND close > open (strong bullish marubozu)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((body_frac >= 0.80) & (close > open)).astype(float)


def pbs_063_bearish_marubozu_wide_range_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: bearish marubozu (body>80% range) AND range > 2x 21d avg (extreme panic selling bar)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    avg = _avg_range(high, low, _TD_MON)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    return ((body_frac >= 0.80) & (close < open) & (rng > 2.0 * avg)).astype(float)


def pbs_064_marubozu_near_low_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: bearish marubozu body/range>80% AND close at new 21-day low (marubozu near low)."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    prior_low_21 = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return ((body_frac >= 0.80) & (close < open) & (close < prior_low_21)).astype(float)


def pbs_065_bearish_marubozu_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bearish marubozu bars (body>80% range, close<open) in trailing 21 days."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((body_frac >= 0.80) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def pbs_066_bearish_marubozu_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bearish marubozu bars in trailing 63 days."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((body_frac >= 0.80) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def pbs_067_bearish_marubozu_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bearish marubozu bars in trailing 252 days."""
    body = _body(open, close)
    rng = _bar_range(high, low)
    body_frac = _safe_div(body, rng.clip(lower=_EPS))
    flag = ((body_frac >= 0.80) & (close < open)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


# --- Group F (068-075): Climax bars — wide range + extreme volume + directional close ---

def pbs_068_volume_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 21-day rolling mean and std (volume surge detection)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(volume - m, s)


def pbs_069_selling_climax_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: selling climax = wide-range bear bar (>2x avg) AND volume > 2x median AND close < open.
    Selling climax combines abnormal range expansion with extreme volume and directional down close."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    return ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open)).astype(float)


def pbs_070_climax_intensity_score(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax intensity = range_zscore_252d * volume_zscore_21d (continuous, clipped at 0).
    Captures bars that are simultaneously extreme in price range and volume."""
    rng = _bar_range(high, low)
    m_rng = _rolling_mean(rng, _TD_YEAR)
    s_rng = _rolling_std(rng, _TD_YEAR)
    rng_z = _safe_div(rng - m_rng, s_rng).clip(lower=0.0)
    m_vol = _rolling_mean(volume, _TD_MON)
    s_vol = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m_vol, s_vol).clip(lower=0.0)
    return rng_z * vol_z


def pbs_071_down_climax_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: down-climax = selling climax with close in bottom 20% of range.
    Full-conviction down: wide range + extreme volume + close near session low."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    clv = _safe_div(close - low, rng.clip(lower=_EPS))
    return ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (close < open) & (clv <= 0.20)).astype(float)


def pbs_072_climax_with_lower_wick_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: climax bar (wide range + extreme volume) with long lower wick (>40% range).
    Classic capitulation reversal: extreme selling volume but buyers emerge intraday."""
    rng = _bar_range(high, low)
    avg_rng = _avg_range(high, low, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    lt = _lower_tail(open, close, low)
    lt_frac = _safe_div(lt, rng.clip(lower=_EPS))
    return ((rng > 2.0 * avg_rng) & (volume > 2.0 * med_vol) & (lt_frac > 0.40)).astype(float)


def pbs_073_climax_bar_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling climax bars in trailing 21 days."""
    flag = pbs_069_selling_climax_flag(close, high, low, open, volume)
    return _rolling_sum(flag, _TD_MON)


def pbs_074_climax_bar_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling climax bars in trailing 63 days."""
    flag = pbs_069_selling_climax_flag(close, high, low, open, volume)
    return _rolling_sum(flag, _TD_QTR)


def pbs_075_climax_bar_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling climax bars in trailing 252 days."""
    flag = pbs_069_selling_climax_flag(close, high, low, open, volume)
    return _rolling_sum(flag, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

PANIC_BAR_SIGNATURES_REGISTRY_001_075 = {
    "pbs_001_range_ratio_21d": {"inputs": ["close", "high", "low"], "func": pbs_001_range_ratio_21d},
    "pbs_002_range_ratio_63d": {"inputs": ["close", "high", "low"], "func": pbs_002_range_ratio_63d},
    "pbs_003_range_ratio_252d": {"inputs": ["close", "high", "low"], "func": pbs_003_range_ratio_252d},
    "pbs_004_wide_range_bar_flag_2x_21d": {"inputs": ["close", "high", "low"], "func": pbs_004_wide_range_bar_flag_2x_21d},
    "pbs_005_wide_range_bar_flag_3x_21d": {"inputs": ["close", "high", "low"], "func": pbs_005_wide_range_bar_flag_3x_21d},
    "pbs_006_wide_range_bar_flag_2x_63d": {"inputs": ["close", "high", "low"], "func": pbs_006_wide_range_bar_flag_2x_63d},
    "pbs_007_wide_range_down_bar_flag_2x_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_007_wide_range_down_bar_flag_2x_21d},
    "pbs_008_wide_range_down_bar_flag_3x_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_008_wide_range_down_bar_flag_3x_21d},
    "pbs_009_range_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": pbs_009_range_pct_rank_252d},
    "pbs_010_range_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": pbs_010_range_pct_rank_63d},
    "pbs_011_range_zscore_252d": {"inputs": ["close", "high", "low"], "func": pbs_011_range_zscore_252d},
    "pbs_012_range_zscore_63d": {"inputs": ["close", "high", "low"], "func": pbs_012_range_zscore_63d},
    "pbs_013_range_vs_21d_median": {"inputs": ["close", "high", "low"], "func": pbs_013_range_vs_21d_median},
    "pbs_014_range_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": pbs_014_range_expanding_pct_rank},
    "pbs_015_range_multiple_above_avg_21d": {"inputs": ["close", "high", "low"], "func": pbs_015_range_multiple_above_avg_21d},
    "pbs_016_lower_tail_ratio_range": {"inputs": ["close", "high", "low", "open"], "func": pbs_016_lower_tail_ratio_range},
    "pbs_017_lower_tail_ratio_21d_avg_range": {"inputs": ["close", "high", "low", "open"], "func": pbs_017_lower_tail_ratio_21d_avg_range},
    "pbs_018_lower_tail_ratio_63d_avg_range": {"inputs": ["close", "high", "low", "open"], "func": pbs_018_lower_tail_ratio_63d_avg_range},
    "pbs_019_hammer_flag_lt50pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_019_hammer_flag_lt50pct},
    "pbs_020_hammer_flag_lt60pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_020_hammer_flag_lt60pct},
    "pbs_021_hammer_flag_lt70pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_021_hammer_flag_lt70pct},
    "pbs_022_long_lower_tail_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_022_long_lower_tail_wide_range_flag},
    "pbs_023_lower_tail_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_023_lower_tail_zscore_252d},
    "pbs_024_lower_tail_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_024_lower_tail_pct_rank_252d},
    "pbs_025_lower_tail_pct_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_025_lower_tail_pct_rank_63d},
    "pbs_026_lower_tail_vs_upper_tail_ratio": {"inputs": ["close", "high", "low", "open"], "func": pbs_026_lower_tail_vs_upper_tail_ratio},
    "pbs_027_lower_tail_ratio_body": {"inputs": ["close", "high", "low", "open"], "func": pbs_027_lower_tail_ratio_body},
    "pbs_028_lower_tail_gt2x_body_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_028_lower_tail_gt2x_body_flag},
    "pbs_029_lower_tail_abs_21d_multiple": {"inputs": ["close", "high", "low", "open"], "func": pbs_029_lower_tail_abs_21d_multiple},
    "pbs_030_lower_tail_down_bar_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_030_lower_tail_down_bar_flag},
    "pbs_031_close_location_value": {"inputs": ["close", "high", "low"], "func": pbs_031_close_location_value},
    "pbs_032_close_near_low_flag_10pct": {"inputs": ["close", "high", "low"], "func": pbs_032_close_near_low_flag_10pct},
    "pbs_033_close_near_low_flag_20pct": {"inputs": ["close", "high", "low"], "func": pbs_033_close_near_low_flag_20pct},
    "pbs_034_wide_down_close_low_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_034_wide_down_close_low_flag},
    "pbs_035_wide_down_close_low_flag_3x": {"inputs": ["close", "high", "low", "open"], "func": pbs_035_wide_down_close_low_flag_3x},
    "pbs_036_down_close_low_range_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_036_down_close_low_range_score},
    "pbs_037_gap_down_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_037_gap_down_wide_range_flag},
    "pbs_038_close_below_prior_low_wide_range": {"inputs": ["close", "high", "low"], "func": pbs_038_close_below_prior_low_wide_range},
    "pbs_039_range_pct_close_loss": {"inputs": ["close", "high", "low", "open"], "func": pbs_039_range_pct_close_loss},
    "pbs_040_wide_range_bar_count_21d": {"inputs": ["close", "high", "low"], "func": pbs_040_wide_range_bar_count_21d},
    "pbs_041_wide_range_bar_count_63d": {"inputs": ["close", "high", "low"], "func": pbs_041_wide_range_bar_count_63d},
    "pbs_042_wide_range_down_bar_count_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_042_wide_range_down_bar_count_21d},
    "pbs_043_wide_range_down_bar_count_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_043_wide_range_down_bar_count_63d},
    "pbs_044_panic_bar_count_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_044_panic_bar_count_252d},
    "pbs_045_days_since_last_wide_range_bar": {"inputs": ["close", "high", "low"], "func": pbs_045_days_since_last_wide_range_bar},
    "pbs_046_exhaustion_bar_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_046_exhaustion_bar_flag},
    "pbs_047_exhaustion_bar_flag_strong": {"inputs": ["close", "high", "low", "open"], "func": pbs_047_exhaustion_bar_flag_strong},
    "pbs_048_exhaustion_close_up_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_048_exhaustion_close_up_flag},
    "pbs_049_exhaustion_bar_score": {"inputs": ["close", "high", "low", "open"], "func": pbs_049_exhaustion_bar_score},
    "pbs_050_exhaustion_bar_count_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_050_exhaustion_bar_count_63d},
    "pbs_051_exhaustion_bar_count_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_051_exhaustion_bar_count_252d},
    "pbs_052_exhaustion_score_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_052_exhaustion_score_zscore_252d},
    "pbs_053_exhaustion_bar_3x_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_053_exhaustion_bar_3x_range_flag},
    "pbs_054_exhaustion_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_054_exhaustion_pct_rank_252d},
    "pbs_055_outside_bar_flag": {"inputs": ["high", "low"], "func": pbs_055_outside_bar_flag},
    "pbs_056_outside_bar_down_close_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_056_outside_bar_down_close_flag},
    "pbs_057_key_reversal_up_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_057_key_reversal_up_flag},
    "pbs_058_body_range_ratio": {"inputs": ["close", "high", "low", "open"], "func": pbs_058_body_range_ratio},
    "pbs_059_bearish_marubozu_flag_90pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_059_bearish_marubozu_flag_90pct},
    "pbs_060_bearish_marubozu_flag_80pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_060_bearish_marubozu_flag_80pct},
    "pbs_061_bullish_marubozu_flag_90pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_061_bullish_marubozu_flag_90pct},
    "pbs_062_bullish_marubozu_flag_80pct": {"inputs": ["close", "high", "low", "open"], "func": pbs_062_bullish_marubozu_flag_80pct},
    "pbs_063_bearish_marubozu_wide_range_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_063_bearish_marubozu_wide_range_flag},
    "pbs_064_marubozu_near_low_flag": {"inputs": ["close", "high", "low", "open"], "func": pbs_064_marubozu_near_low_flag},
    "pbs_065_bearish_marubozu_count_21d": {"inputs": ["close", "high", "low", "open"], "func": pbs_065_bearish_marubozu_count_21d},
    "pbs_066_bearish_marubozu_count_63d": {"inputs": ["close", "high", "low", "open"], "func": pbs_066_bearish_marubozu_count_63d},
    "pbs_067_bearish_marubozu_count_252d": {"inputs": ["close", "high", "low", "open"], "func": pbs_067_bearish_marubozu_count_252d},
    "pbs_068_volume_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_068_volume_zscore_21d},
    "pbs_069_selling_climax_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_069_selling_climax_flag},
    "pbs_070_climax_intensity_score": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_070_climax_intensity_score},
    "pbs_071_down_climax_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_071_down_climax_flag},
    "pbs_072_climax_with_lower_wick_flag": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_072_climax_with_lower_wick_flag},
    "pbs_073_climax_bar_count_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_073_climax_bar_count_21d},
    "pbs_074_climax_bar_count_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_074_climax_bar_count_63d},
    "pbs_075_climax_bar_count_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": pbs_075_climax_bar_count_252d},
}
