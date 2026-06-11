"""
39_intraday_range — Base Features 001-075
Domain: daily high-low spread level and day-to-day structure — intraday range as a
normalized level, average range over windows, range variability, range vs body,
range vs gap, range distribution, typical-price range, and range autocorrelation.
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


def _hl_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Raw daily high-low range."""
    return high - low


def _hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily high-low range normalized by close price."""
    return _safe_div(high - low, close)


def _typical_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Typical price = (H + L + C) / 3."""
    return (high + low + close) / 3.0


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw and close-normalized daily range level ---

def idr_001_hl_range_raw(high: pd.Series, low: pd.Series) -> pd.Series:
    """Raw high-low range in price units."""
    return _hl_range(high, low)


def idr_002_hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High-low range divided by closing price (fractional spread)."""
    return _hl_range_over_close(high, low, close)


def idr_003_hl_range_over_open(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """High-low range divided by open price."""
    return _safe_div(high - low, open)


def idr_004_hl_range_over_midpoint(high: pd.Series, low: pd.Series) -> pd.Series:
    """High-low range divided by the day's midpoint ((H+L)/2)."""
    mid = (high + low) / 2.0
    return _safe_div(high - low, mid)


def idr_005_hl_range_over_typical(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High-low range divided by typical price (H+L+C)/3."""
    tp = _typical_price(high, low, close)
    return _safe_div(high - low, tp)


def idr_006_hl_range_log(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of high-low range normalized by close (log fractional spread)."""
    r = _hl_range_over_close(high, low, close).clip(lower=_EPS)
    return np.log(r)


def idr_007_hl_range_pct_of_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High-low range as a percentage of close (×100)."""
    return _hl_range_over_close(high, low, close) * 100.0


def idr_008_hl_range_over_prior_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High-low range divided by prior day's close."""
    return _safe_div(high - low, close.shift(1))


def idr_009_hl_range_daily_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Day-over-day change in close-normalized high-low range."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(1)


def idr_010_hl_range_pct_change_1d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percent change in normalized range vs prior day."""
    r = _hl_range_over_close(high, low, close)
    return r.pct_change(1)


# --- Group B (011-020): Rolling average range over multiple windows ---

def idr_011_avg_range_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), _TD_WEEK)


def idr_012_avg_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), _TD_MON)


def idr_013_avg_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), _TD_QTR)


def idr_014_avg_range_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), _TD_HALF)


def idr_015_avg_range_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), _TD_YEAR)


def idr_016_avg_range_raw_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average of raw (price-unit) high-low range."""
    return _rolling_mean(_hl_range(high, low), _TD_MON)


def idr_017_avg_range_raw_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day average of raw high-low range."""
    return _rolling_mean(_hl_range(high, low), _TD_QTR)


def idr_018_avg_range_ewm_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=21) of close-normalized range."""
    return _ewm_mean(_hl_range_over_close(high, low, close), _TD_MON)


def idr_019_avg_range_ewm_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=63) of close-normalized range."""
    return _ewm_mean(_hl_range_over_close(high, low, close), _TD_QTR)


def idr_020_avg_range_median_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling median of close-normalized range."""
    return _rolling_median(_hl_range_over_close(high, low, close), _TD_MON)


# --- Group C (021-030): Range level relative to its own history ---

def idr_021_range_vs_avg_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 5-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, _TD_WEEK))


def idr_022_range_vs_avg_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 21-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, _TD_MON))


def idr_023_range_vs_avg_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 63-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, _TD_QTR))


def idr_024_range_vs_avg_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 252-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, _TD_YEAR))


def idr_025_range_pct_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 21 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def idr_026_range_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 63 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def idr_027_range_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 252 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def idr_028_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 21-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_MON)
    s = _rolling_std(r, _TD_MON)
    return _safe_div(r - m, s)


def idr_029_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 63-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


def idr_030_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 252-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


# --- Group D (031-040): Range variability / stability ---

def idr_031_range_std_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day standard deviation of close-normalized range."""
    return _rolling_std(_hl_range_over_close(high, low, close), _TD_MON)


def idr_032_range_std_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day standard deviation of close-normalized range."""
    return _rolling_std(_hl_range_over_close(high, low, close), _TD_QTR)


def idr_033_range_cv_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of normalized range over 21 days (std/mean)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_std(r, _TD_MON), _rolling_mean(r, _TD_MON))


def idr_034_range_cv_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of normalized range over 63 days."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_std(r, _TD_QTR), _rolling_mean(r, _TD_QTR))


def idr_035_range_max_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum normalized range over trailing 21 days."""
    return _rolling_max(_hl_range_over_close(high, low, close), _TD_MON)


def idr_036_range_max_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum normalized range over trailing 63 days."""
    return _rolling_max(_hl_range_over_close(high, low, close), _TD_QTR)


def idr_037_range_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum normalized range over trailing 252 days."""
    return _rolling_max(_hl_range_over_close(high, low, close), _TD_YEAR)


def idr_038_range_min_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum normalized range over trailing 21 days."""
    return _rolling_min(_hl_range_over_close(high, low, close), _TD_MON)


def idr_039_range_min_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum normalized range over trailing 63 days."""
    return _rolling_min(_hl_range_over_close(high, low, close), _TD_QTR)


def idr_040_range_max_to_min_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day max normalized range to 21-day min (spread of range)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(_rolling_max(r, _TD_MON), _rolling_min(r, _TD_MON).clip(lower=_EPS))


# --- Group E (041-050): Range vs candle body and wick structure ---

def idr_041_body_to_range_ratio(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute candle body divided by high-low range (how much of range is body)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body, rng)


def idr_042_avg_body_to_range_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of body-to-range ratio."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(body, rng), _TD_MON)


def idr_043_avg_body_to_range_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day average of body-to-range ratio."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(body, rng), _TD_QTR)


def idr_044_upper_wick_to_range(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Upper wick as fraction of total range (max(open,close) to high)."""
    top_body = pd.concat([close, open], axis=1).max(axis=1)
    upper_wick = high - top_body
    rng = (high - low).replace(0, np.nan)
    return _safe_div(upper_wick, rng)


def idr_045_lower_wick_to_range(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Lower wick as fraction of total range (low to min(open,close))."""
    bot_body = pd.concat([close, open], axis=1).min(axis=1)
    lower_wick = bot_body - low
    rng = (high - low).replace(0, np.nan)
    return _safe_div(lower_wick, rng)


def idr_046_avg_upper_wick_fraction_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average upper wick as fraction of range."""
    top_body = pd.concat([close, open], axis=1).max(axis=1)
    upper_wick = high - top_body
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(upper_wick, rng), _TD_MON)


def idr_047_avg_lower_wick_fraction_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average lower wick as fraction of range."""
    bot_body = pd.concat([close, open], axis=1).min(axis=1)
    lower_wick = bot_body - low
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(lower_wick, rng), _TD_MON)


def idr_048_range_minus_body_over_close(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Total wick length (range minus body) normalized by close."""
    rng = high - low
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    return _safe_div(wick, close)


def idr_049_avg_total_wick_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average total wick normalized by close."""
    rng = high - low
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    return _rolling_mean(_safe_div(wick, close), _TD_MON)


def idr_050_body_range_ratio_vs_avg_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's body-to-range ratio vs 63-day average (high = tight candles)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    br = _safe_div(body, rng)
    return _safe_div(br, _rolling_mean(br, _TD_QTR))


# --- Group F (051-060): Range vs gap (overnight gap) ---

def idr_051_gap_over_range(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight gap (open - prior close) as fraction of today's range."""
    gap = (open - close.shift(1)).abs()
    rng = (high - low).replace(0, np.nan)
    return _safe_div(gap, rng)


def idr_052_avg_gap_over_range_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of gap-to-range ratio."""
    gap = (open - close.shift(1)).abs()
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(gap, rng), _TD_MON)


def idr_053_avg_gap_over_range_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day average of gap-to-range ratio."""
    gap = (open - close.shift(1)).abs()
    rng = (high - low).replace(0, np.nan)
    return _rolling_mean(_safe_div(gap, rng), _TD_QTR)


def idr_054_intraday_range_ex_gap(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday range minus overnight gap, normalized by close (pure intraday move)."""
    rng = high - low
    gap = (open - close.shift(1)).abs()
    ex_gap = (rng - gap).clip(lower=0)
    return _safe_div(ex_gap, close)


def idr_055_avg_range_ex_gap_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of gap-adjusted intraday range normalized by close."""
    rng = high - low
    gap = (open - close.shift(1)).abs()
    ex_gap = (rng - gap).clip(lower=0)
    return _rolling_mean(_safe_div(ex_gap, close), _TD_MON)


def idr_056_gap_fraction_of_prior_range(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's gap as fraction of prior day's high-low range."""
    gap = (open - close.shift(1)).abs()
    prior_rng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    return _safe_div(gap, prior_rng)


def idr_057_open_in_prior_range(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Open's position within prior day's range: (open - prior_low)/(prior_high - prior_low)."""
    prior_rng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    return _safe_div(open - low.shift(1), prior_rng).clip(0, 1)


def idr_058_avg_open_in_prior_range_21d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of open's position within prior day's range."""
    prior_rng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    pos = _safe_div(open - low.shift(1), prior_rng).clip(0, 1)
    return _rolling_mean(pos, _TD_MON)


def idr_059_range_to_gap_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average ratio of range to absolute gap (range dominance)."""
    gap = (open - close.shift(1)).abs().replace(0, np.nan)
    rng = high - low
    return _rolling_mean(_safe_div(rng, gap), _TD_MON)


def idr_060_gap_coverage_ratio(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of prior-day range covered by today's range (overlap)."""
    overlap_hi = pd.concat([high, high.shift(1)], axis=1).min(axis=1)
    overlap_lo = pd.concat([low, low.shift(1)], axis=1).max(axis=1)
    overlap = (overlap_hi - overlap_lo).clip(lower=0)
    prior_rng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    return _safe_div(overlap, prior_rng)


# --- Group G (061-075): Typical-price range, distribution, and autocorrelation ---

def idr_061_typical_price_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day range of the typical price: max(TP) - min(TP), normalized by close."""
    tp = _typical_price(high, low, close)
    tp_range = _rolling_max(tp, _TD_MON) - _rolling_min(tp, _TD_MON)
    return _safe_div(tp_range, close)


def idr_062_typical_price_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day range of typical price normalized by close."""
    tp = _typical_price(high, low, close)
    tp_range = _rolling_max(tp, _TD_QTR) - _rolling_min(tp, _TD_QTR)
    return _safe_div(tp_range, close)


def idr_063_hl_range_to_typical_price_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily range as fraction of typical price."""
    tp = _typical_price(high, low, close)
    return _safe_div(high - low, tp)


def idr_064_avg_typical_range_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day average of daily range as fraction of typical price."""
    tp = _typical_price(high, low, close)
    return _rolling_mean(_safe_div(high - low, tp), _TD_MON)


def idr_065_range_above_median_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in trailing 21 days where range exceeds 21-day median range."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_MON)
    above = (r > med).astype(float)
    return _rolling_sum(above, _TD_MON)


def idr_066_range_above_median_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in trailing 63 days where range exceeds 63-day median range."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_QTR)
    above = (r > med).astype(float)
    return _rolling_sum(above, _TD_QTR)


def idr_067_range_above_2x_median_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with range > 2x 21-day median range (extreme days)."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_MON)
    above = (r > 2.0 * med).astype(float)
    return _rolling_sum(above, _TD_MON)


def idr_068_range_autocorr_lag1_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation (lag-1) of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        lambda x: float(np.corrcoef(x[:-1], x[1:])[0, 1]) if len(x) > 2 else np.nan, raw=True
    )


def idr_069_range_autocorr_lag1_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation (lag-1) of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(
        lambda x: float(np.corrcoef(x[:-1], x[1:])[0, 1]) if len(x) > 2 else np.nan, raw=True
    )


def idr_070_range_skew_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling skewness of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def idr_071_range_skew_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling skewness of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def idr_072_range_kurt_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling excess kurtosis of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def idr_073_range_high_regime_flag_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: current range above 75th percentile of trailing 252-day range distribution."""
    r = _hl_range_over_close(high, low, close)
    p75 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    return (r > p75).astype(float)


def idr_074_range_expanding_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of normalized range (historical extremity benchmark)."""
    r = _hl_range_over_close(high, low, close)
    return r.expanding(min_periods=1).max()


def idr_075_range_expanding_pct_rank(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding percentile rank of today's normalized range (all-history context)."""
    r = _hl_range_over_close(high, low, close)
    return r.expanding(min_periods=1).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_REGISTRY_001_075 = {
    "idr_001_hl_range_raw": {"inputs": ["high", "low"], "func": idr_001_hl_range_raw},
    "idr_002_hl_range_over_close": {"inputs": ["high", "low", "close"], "func": idr_002_hl_range_over_close},
    "idr_003_hl_range_over_open": {"inputs": ["high", "low", "open"], "func": idr_003_hl_range_over_open},
    "idr_004_hl_range_over_midpoint": {"inputs": ["high", "low"], "func": idr_004_hl_range_over_midpoint},
    "idr_005_hl_range_over_typical": {"inputs": ["high", "low", "close"], "func": idr_005_hl_range_over_typical},
    "idr_006_hl_range_log": {"inputs": ["high", "low", "close"], "func": idr_006_hl_range_log},
    "idr_007_hl_range_pct_of_price": {"inputs": ["high", "low", "close"], "func": idr_007_hl_range_pct_of_price},
    "idr_008_hl_range_over_prior_close": {"inputs": ["high", "low", "close"], "func": idr_008_hl_range_over_prior_close},
    "idr_009_hl_range_daily_diff": {"inputs": ["high", "low", "close"], "func": idr_009_hl_range_daily_diff},
    "idr_010_hl_range_pct_change_1d": {"inputs": ["high", "low", "close"], "func": idr_010_hl_range_pct_change_1d},
    "idr_011_avg_range_5d": {"inputs": ["high", "low", "close"], "func": idr_011_avg_range_5d},
    "idr_012_avg_range_21d": {"inputs": ["high", "low", "close"], "func": idr_012_avg_range_21d},
    "idr_013_avg_range_63d": {"inputs": ["high", "low", "close"], "func": idr_013_avg_range_63d},
    "idr_014_avg_range_126d": {"inputs": ["high", "low", "close"], "func": idr_014_avg_range_126d},
    "idr_015_avg_range_252d": {"inputs": ["high", "low", "close"], "func": idr_015_avg_range_252d},
    "idr_016_avg_range_raw_21d": {"inputs": ["high", "low"], "func": idr_016_avg_range_raw_21d},
    "idr_017_avg_range_raw_63d": {"inputs": ["high", "low"], "func": idr_017_avg_range_raw_63d},
    "idr_018_avg_range_ewm_21d": {"inputs": ["high", "low", "close"], "func": idr_018_avg_range_ewm_21d},
    "idr_019_avg_range_ewm_63d": {"inputs": ["high", "low", "close"], "func": idr_019_avg_range_ewm_63d},
    "idr_020_avg_range_median_21d": {"inputs": ["high", "low", "close"], "func": idr_020_avg_range_median_21d},
    "idr_021_range_vs_avg_5d": {"inputs": ["high", "low", "close"], "func": idr_021_range_vs_avg_5d},
    "idr_022_range_vs_avg_21d": {"inputs": ["high", "low", "close"], "func": idr_022_range_vs_avg_21d},
    "idr_023_range_vs_avg_63d": {"inputs": ["high", "low", "close"], "func": idr_023_range_vs_avg_63d},
    "idr_024_range_vs_avg_252d": {"inputs": ["high", "low", "close"], "func": idr_024_range_vs_avg_252d},
    "idr_025_range_pct_rank_21d": {"inputs": ["high", "low", "close"], "func": idr_025_range_pct_rank_21d},
    "idr_026_range_pct_rank_63d": {"inputs": ["high", "low", "close"], "func": idr_026_range_pct_rank_63d},
    "idr_027_range_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": idr_027_range_pct_rank_252d},
    "idr_028_range_zscore_21d": {"inputs": ["high", "low", "close"], "func": idr_028_range_zscore_21d},
    "idr_029_range_zscore_63d": {"inputs": ["high", "low", "close"], "func": idr_029_range_zscore_63d},
    "idr_030_range_zscore_252d": {"inputs": ["high", "low", "close"], "func": idr_030_range_zscore_252d},
    "idr_031_range_std_21d": {"inputs": ["high", "low", "close"], "func": idr_031_range_std_21d},
    "idr_032_range_std_63d": {"inputs": ["high", "low", "close"], "func": idr_032_range_std_63d},
    "idr_033_range_cv_21d": {"inputs": ["high", "low", "close"], "func": idr_033_range_cv_21d},
    "idr_034_range_cv_63d": {"inputs": ["high", "low", "close"], "func": idr_034_range_cv_63d},
    "idr_035_range_max_21d": {"inputs": ["high", "low", "close"], "func": idr_035_range_max_21d},
    "idr_036_range_max_63d": {"inputs": ["high", "low", "close"], "func": idr_036_range_max_63d},
    "idr_037_range_max_252d": {"inputs": ["high", "low", "close"], "func": idr_037_range_max_252d},
    "idr_038_range_min_21d": {"inputs": ["high", "low", "close"], "func": idr_038_range_min_21d},
    "idr_039_range_min_63d": {"inputs": ["high", "low", "close"], "func": idr_039_range_min_63d},
    "idr_040_range_max_to_min_ratio_21d": {"inputs": ["high", "low", "close"], "func": idr_040_range_max_to_min_ratio_21d},
    "idr_041_body_to_range_ratio": {"inputs": ["high", "low", "close", "open"], "func": idr_041_body_to_range_ratio},
    "idr_042_avg_body_to_range_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_042_avg_body_to_range_21d},
    "idr_043_avg_body_to_range_63d": {"inputs": ["high", "low", "close", "open"], "func": idr_043_avg_body_to_range_63d},
    "idr_044_upper_wick_to_range": {"inputs": ["high", "low", "close", "open"], "func": idr_044_upper_wick_to_range},
    "idr_045_lower_wick_to_range": {"inputs": ["high", "low", "close", "open"], "func": idr_045_lower_wick_to_range},
    "idr_046_avg_upper_wick_fraction_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_046_avg_upper_wick_fraction_21d},
    "idr_047_avg_lower_wick_fraction_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_047_avg_lower_wick_fraction_21d},
    "idr_048_range_minus_body_over_close": {"inputs": ["high", "low", "close", "open"], "func": idr_048_range_minus_body_over_close},
    "idr_049_avg_total_wick_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_049_avg_total_wick_21d},
    "idr_050_body_range_ratio_vs_avg_63d": {"inputs": ["high", "low", "close", "open"], "func": idr_050_body_range_ratio_vs_avg_63d},
    "idr_051_gap_over_range": {"inputs": ["high", "low", "close", "open"], "func": idr_051_gap_over_range},
    "idr_052_avg_gap_over_range_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_052_avg_gap_over_range_21d},
    "idr_053_avg_gap_over_range_63d": {"inputs": ["high", "low", "close", "open"], "func": idr_053_avg_gap_over_range_63d},
    "idr_054_intraday_range_ex_gap": {"inputs": ["high", "low", "close", "open"], "func": idr_054_intraday_range_ex_gap},
    "idr_055_avg_range_ex_gap_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_055_avg_range_ex_gap_21d},
    "idr_056_gap_fraction_of_prior_range": {"inputs": ["high", "low", "close", "open"], "func": idr_056_gap_fraction_of_prior_range},
    "idr_057_open_in_prior_range": {"inputs": ["high", "low", "open"], "func": idr_057_open_in_prior_range},
    "idr_058_avg_open_in_prior_range_21d": {"inputs": ["high", "low", "open"], "func": idr_058_avg_open_in_prior_range_21d},
    "idr_059_range_to_gap_ratio_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_059_range_to_gap_ratio_21d},
    "idr_060_gap_coverage_ratio": {"inputs": ["high", "low", "close", "open"], "func": idr_060_gap_coverage_ratio},
    "idr_061_typical_price_range_21d": {"inputs": ["high", "low", "close"], "func": idr_061_typical_price_range_21d},
    "idr_062_typical_price_range_63d": {"inputs": ["high", "low", "close"], "func": idr_062_typical_price_range_63d},
    "idr_063_hl_range_to_typical_price_ratio": {"inputs": ["high", "low", "close"], "func": idr_063_hl_range_to_typical_price_ratio},
    "idr_064_avg_typical_range_ratio_21d": {"inputs": ["high", "low", "close"], "func": idr_064_avg_typical_range_ratio_21d},
    "idr_065_range_above_median_count_21d": {"inputs": ["high", "low", "close"], "func": idr_065_range_above_median_count_21d},
    "idr_066_range_above_median_count_63d": {"inputs": ["high", "low", "close"], "func": idr_066_range_above_median_count_63d},
    "idr_067_range_above_2x_median_21d": {"inputs": ["high", "low", "close"], "func": idr_067_range_above_2x_median_21d},
    "idr_068_range_autocorr_lag1_21d": {"inputs": ["high", "low", "close"], "func": idr_068_range_autocorr_lag1_21d},
    "idr_069_range_autocorr_lag1_63d": {"inputs": ["high", "low", "close"], "func": idr_069_range_autocorr_lag1_63d},
    "idr_070_range_skew_63d": {"inputs": ["high", "low", "close"], "func": idr_070_range_skew_63d},
    "idr_071_range_skew_252d": {"inputs": ["high", "low", "close"], "func": idr_071_range_skew_252d},
    "idr_072_range_kurt_63d": {"inputs": ["high", "low", "close"], "func": idr_072_range_kurt_63d},
    "idr_073_range_high_regime_flag_21d": {"inputs": ["high", "low", "close"], "func": idr_073_range_high_regime_flag_21d},
    "idr_074_range_expanding_max": {"inputs": ["high", "low", "close"], "func": idr_074_range_expanding_max},
    "idr_075_range_expanding_pct_rank": {"inputs": ["high", "low", "close"], "func": idr_075_range_expanding_pct_rank},
}
