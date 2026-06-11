"""
46_gap_structure — Base Features 001-075
Domain: overnight gap frequency, magnitude, fill behavior, distribution, and gap-type classification
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Gap = (open - prior_close) / prior_close. All features backward-looking only.
Gap-type taxonomy: common (small, inside range), breakaway (out of range, high vol),
  runaway (mid-trend, sustained vol), exhaustion (late-trend, climactic vol, fills quickly).
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight gap as fraction of prior close: (open - prior_close) / prior_close."""
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Gap pct clipped to positive (up gaps only; down days = 0)."""
    return _gap_pct(close, open_).clip(lower=0)


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Gap pct clipped to negative then abs (down gaps only; up days = 0)."""
    return _gap_pct(close, open_).clip(upper=0).abs()


# ── Gap-type classification helpers ───────────────────────────────────────────
# All use only trailing (backward-looking) data.
# Trend: 21-day linear slope of close; positive = uptrend, negative = downtrend.
# Range: trailing 21-day high/low band relative to prior close.
# Volume: current vs 21-day average.
# Gap filled within N days: evaluated with shift so only past bars inform current bar.

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Rolling sign of price trend: +1 uptrend, -1 downtrend, 0 flat."""
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Open relative to prior trailing range [0=at low, 1=at high].
    Uses prior w bars (shifted) so no look-ahead."""
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Current volume relative to trailing w-day average."""
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    """Fraction of trailing w bars where close is above its own w-bar rolling mean.
    Near 1.0 = well-established uptrend; near 0.0 = well-established downtrend."""
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _gap_filled_within_n(close: pd.Series, open_: pd.Series,
                          high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    """For each bar AT LEAST n days in the past, 1 if the gap was filled within n subsequent bars.
    Current bar value uses only data up to n bars ago (no look-ahead).
    Implemented by shifting the fill indicator forward by n then looking back."""
    prior_close = close.shift(1)
    gap = open_ - prior_close
    # On each bar t: was there a gap, and did price return to prior_close within n bars?
    # We compute a forward-fill signal then shift n to make it backward-looking at time t+n.
    # Instead: for bar t, check if any of [t..t+n-1] high/low touched prior_close.
    # Backward-safe version: compute rolling n-day max high and min low starting from bar t,
    # but shifted backward so at bar t we use bars [t-n .. t-1].
    # Equivalent: "did the gap that opened n bars ago get filled?"
    # Shift gap signal and OHLCV by n; then check if subsequent (current) bar's range covers it.
    gap_n_ago = gap.shift(n)
    prior_close_n_ago = prior_close.shift(n)
    # Rolling max high and min low over n bars ending at current bar
    roll_high = high.rolling(n, min_periods=1).max()
    roll_low = low.rolling(n, min_periods=1).min()
    up_filled = (gap_n_ago > 0) & (roll_low <= prior_close_n_ago)
    dn_filled = (gap_n_ago < 0) & (roll_high >= prior_close_n_ago)
    has_gap_n_ago = gap_n_ago.abs() > _EPS
    filled = ((up_filled | dn_filled) & has_gap_n_ago).astype(float)
    # Where there was no gap n days ago, return NaN
    return filled.where(has_gap_n_ago, np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw gap magnitude — daily and rolling mean ---

def gap_001_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight gap as % of prior close (signed: + up, - down)."""
    return _gap_pct(close, open)


def gap_002_gap_abs_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute overnight gap size as % of prior close."""
    return _gap_pct(close, open).abs()


def gap_003_gap_up_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Positive (up) gap size; zero on flat/down days."""
    return _gap_up(close, open)


def gap_004_gap_down_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Down gap magnitude (positive value); zero on flat/up days."""
    return _gap_down(close, open)


def gap_005_avg_gap_abs_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day average absolute gap size."""
    return _rolling_mean(_gap_pct(close, open).abs(), _TD_WEEK)


def gap_006_avg_gap_abs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average absolute gap size."""
    return _rolling_mean(_gap_pct(close, open).abs(), _TD_MON)


def gap_007_avg_gap_abs_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day average absolute gap size."""
    return _rolling_mean(_gap_pct(close, open).abs(), _TD_QTR)


def gap_008_avg_gap_abs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day average absolute gap size."""
    return _rolling_mean(_gap_pct(close, open).abs(), _TD_YEAR)


def gap_009_avg_signed_gap_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average signed gap (net overnight directional bias)."""
    return _rolling_mean(_gap_pct(close, open), _TD_MON)


def gap_010_avg_signed_gap_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day average signed gap."""
    return _rolling_mean(_gap_pct(close, open), _TD_QTR)


# --- Group B (011-020): Gap frequency — fraction of days with a meaningful gap ---

def gap_011_gap_up_freq_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a positive gap."""
    return _rolling_count_true(_gap_pct(close, open) > 0, _TD_MON) / _TD_MON


def gap_012_gap_down_freq_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a negative gap."""
    return _rolling_count_true(_gap_pct(close, open) < 0, _TD_MON) / _TD_MON


def gap_013_gap_up_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days with an up gap."""
    return _rolling_count_true(_gap_pct(close, open) > 0, _TD_QTR) / _TD_QTR


def gap_014_gap_down_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days with a down gap."""
    return _rolling_count_true(_gap_pct(close, open) < 0, _TD_QTR) / _TD_QTR


def gap_015_gap_up_freq_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 252 days with an up gap."""
    return _rolling_count_true(_gap_pct(close, open) > 0, _TD_YEAR) / _TD_YEAR


def gap_016_gap_down_freq_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 252 days with a down gap."""
    return _rolling_count_true(_gap_pct(close, open) < 0, _TD_YEAR) / _TD_YEAR


def gap_017_large_gap_freq_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days with abs-gap > 1%."""
    return _rolling_count_true(_gap_pct(close, open).abs() > 0.01, _TD_MON) / _TD_MON


def gap_018_large_gap_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days with abs-gap > 1%."""
    return _rolling_count_true(_gap_pct(close, open).abs() > 0.01, _TD_QTR) / _TD_QTR


def gap_019_large_gap_freq_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 252 days with abs-gap > 1%."""
    return _rolling_count_true(_gap_pct(close, open).abs() > 0.01, _TD_YEAR) / _TD_YEAR


def gap_020_gap_down_vs_up_freq_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of down-gap frequency to up-gap frequency over 63 days."""
    g = _gap_pct(close, open)
    up = _rolling_count_true(g > 0, _TD_QTR)
    dn = _rolling_count_true(g < 0, _TD_QTR)
    return _safe_div(dn, up)


# --- Group C (021-030): Gap magnitude distribution — std, median, quantiles ---

def gap_021_gap_std_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day standard deviation of signed gap (gap volatility)."""
    return _rolling_std(_gap_pct(close, open), _TD_MON)


def gap_022_gap_std_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day standard deviation of signed gap."""
    return _rolling_std(_gap_pct(close, open), _TD_QTR)


def gap_023_gap_std_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day standard deviation of signed gap."""
    return _rolling_std(_gap_pct(close, open), _TD_YEAR)


def gap_024_gap_median_abs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day median absolute gap size."""
    return _rolling_median(_gap_pct(close, open).abs(), _TD_MON)


def gap_025_gap_median_abs_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day median absolute gap size."""
    return _rolling_median(_gap_pct(close, open).abs(), _TD_QTR)


def gap_026_gap_median_abs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day median absolute gap size."""
    return _rolling_median(_gap_pct(close, open).abs(), _TD_YEAR)


def gap_027_gap_up_avg_mag_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of up-gaps only over 63 days."""
    ug = _gap_up(close, open)
    ug_nan = ug.where(ug > 0, np.nan)
    return ug_nan.rolling(_TD_QTR, min_periods=1).mean()


def gap_028_gap_down_avg_mag_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of down-gaps only over 63 days."""
    dg = _gap_down(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    return dg_nan.rolling(_TD_QTR, min_periods=1).mean()


def gap_029_gap_up_avg_mag_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of up-gaps only over 252 days."""
    ug = _gap_up(close, open)
    ug_nan = ug.where(ug > 0, np.nan)
    return ug_nan.rolling(_TD_YEAR, min_periods=1).mean()


def gap_030_gap_down_avg_mag_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average magnitude of down-gaps only over 252 days."""
    dg = _gap_down(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    return dg_nan.rolling(_TD_YEAR, min_periods=1).mean()


# --- Group D (031-040): Largest gap in window — extremes ---

def gap_031_largest_up_gap_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest up-gap in trailing 21 days."""
    return _rolling_max(_gap_up(close, open), _TD_MON)


def gap_032_largest_up_gap_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest up-gap in trailing 63 days."""
    return _rolling_max(_gap_up(close, open), _TD_QTR)


def gap_033_largest_up_gap_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest up-gap in trailing 252 days."""
    return _rolling_max(_gap_up(close, open), _TD_YEAR)


def gap_034_largest_down_gap_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest down-gap magnitude in trailing 21 days."""
    return _rolling_max(_gap_down(close, open), _TD_MON)


def gap_035_largest_down_gap_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest down-gap magnitude in trailing 63 days."""
    return _rolling_max(_gap_down(close, open), _TD_QTR)


def gap_036_largest_down_gap_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest down-gap magnitude in trailing 252 days."""
    return _rolling_max(_gap_down(close, open), _TD_YEAR)


def gap_037_largest_abs_gap_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest absolute gap (either direction) in trailing 21 days."""
    return _rolling_max(_gap_pct(close, open).abs(), _TD_MON)


def gap_038_largest_abs_gap_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest absolute gap (either direction) in trailing 63 days."""
    return _rolling_max(_gap_pct(close, open).abs(), _TD_QTR)


def gap_039_largest_abs_gap_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Largest absolute gap (either direction) in trailing 252 days."""
    return _rolling_max(_gap_pct(close, open).abs(), _TD_YEAR)


def gap_040_today_gap_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of today's abs gap within trailing 252-day abs gap series."""
    abs_g = _gap_pct(close, open).abs()
    return abs_g.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Gap fill behavior ---

def gap_041_gap_fill_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's intraday range covers the overnight gap (gap filled), else 0."""
    prior_close = close.shift(1)
    gap = open - prior_close
    filled = pd.Series(0.0, index=close.index)
    up_fill = (gap > 0) & (low <= prior_close)
    dn_fill = (gap < 0) & (high >= prior_close)
    filled[up_fill | dn_fill] = 1.0
    return filled


def gap_042_gap_fill_freq_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 gapped days where gap was filled intraday."""
    filled = gap_041_gap_fill_flag(close, open, high, low)
    has_gap = (_gap_pct(close, open).abs() > _EPS).astype(float)
    fill_sum = _rolling_sum(filled, _TD_MON)
    gap_sum = _rolling_sum(has_gap, _TD_MON).clip(lower=1)
    return _safe_div(fill_sum, gap_sum)


def gap_043_gap_fill_freq_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 gapped days where gap was filled intraday."""
    filled = gap_041_gap_fill_flag(close, open, high, low)
    has_gap = (_gap_pct(close, open).abs() > _EPS).astype(float)
    fill_sum = _rolling_sum(filled, _TD_QTR)
    gap_sum = _rolling_sum(has_gap, _TD_QTR).clip(lower=1)
    return _safe_div(fill_sum, gap_sum)


def gap_044_gap_fill_freq_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 gapped days where gap was filled intraday."""
    filled = gap_041_gap_fill_flag(close, open, high, low)
    has_gap = (_gap_pct(close, open).abs() > _EPS).astype(float)
    fill_sum = _rolling_sum(filled, _TD_YEAR)
    gap_sum = _rolling_sum(has_gap, _TD_YEAR).clip(lower=1)
    return _safe_div(fill_sum, gap_sum)


def gap_045_up_gap_fill_freq_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of up-gap days (last 63) where up gap was filled."""
    prior_close = close.shift(1)
    gap = open - prior_close
    up_gap = (gap > 0).astype(float)
    up_filled = ((gap > 0) & (low <= prior_close)).astype(float)
    filled_sum = _rolling_sum(up_filled, _TD_QTR)
    up_sum = _rolling_sum(up_gap, _TD_QTR).clip(lower=1)
    return _safe_div(filled_sum, up_sum)


def gap_046_down_gap_fill_freq_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of down-gap days (last 63) where down gap was filled."""
    prior_close = close.shift(1)
    gap = open - prior_close
    dn_gap = (gap < 0).astype(float)
    dn_filled = ((gap < 0) & (high >= prior_close)).astype(float)
    filled_sum = _rolling_sum(dn_filled, _TD_QTR)
    dn_sum = _rolling_sum(dn_gap, _TD_QTR).clip(lower=1)
    return _safe_div(filled_sum, dn_sum)


def gap_047_down_gap_fill_freq_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of down-gap days (last 252) where down gap was filled."""
    prior_close = close.shift(1)
    gap = open - prior_close
    dn_gap = (gap < 0).astype(float)
    dn_filled = ((gap < 0) & (high >= prior_close)).astype(float)
    filled_sum = _rolling_sum(dn_filled, _TD_YEAR)
    dn_sum = _rolling_sum(dn_gap, _TD_YEAR).clip(lower=1)
    return _safe_div(filled_sum, dn_sum)


def gap_048_gap_not_filled_down_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today has a down gap that was NOT filled (gap stayed open)."""
    prior_close = close.shift(1)
    gap = open - prior_close
    not_filled = ((gap < 0) & (high < prior_close)).astype(float)
    return not_filled


def gap_049_gap_not_filled_down_freq_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days with unfilled down gaps."""
    return _rolling_mean(gap_048_gap_not_filled_down_flag(close, open, high, low), _TD_MON)


def gap_050_gap_not_filled_down_freq_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days with unfilled down gaps."""
    return _rolling_mean(gap_048_gap_not_filled_down_flag(close, open, high, low), _TD_QTR)


# --- Group F (051-060): Gap contribution to returns ---

def gap_051_gap_return_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of all overnight gap returns (signed) over trailing 21 days."""
    return _rolling_sum(_gap_pct(close, open), _TD_MON)


def gap_052_gap_return_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of all overnight gap returns (signed) over trailing 63 days."""
    return _rolling_sum(_gap_pct(close, open), _TD_QTR)


def gap_053_gap_return_sum_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of all overnight gap returns (signed) over trailing 252 days."""
    return _rolling_sum(_gap_pct(close, open), _TD_YEAR)


def gap_054_gap_up_return_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of positive gap returns over trailing 63 days."""
    return _rolling_sum(_gap_up(close, open), _TD_QTR)


def gap_055_gap_down_return_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of negative gap magnitudes over trailing 63 days (positive value)."""
    return _rolling_sum(_gap_down(close, open), _TD_QTR)


def gap_056_gap_down_return_sum_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of down-gap magnitudes over trailing 252 days."""
    return _rolling_sum(_gap_down(close, open), _TD_YEAR)


def gap_057_gap_net_bias_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Net overnight gap bias: sum of up gaps minus sum of down gaps, 63d."""
    return _rolling_sum(_gap_up(close, open), _TD_QTR) - _rolling_sum(_gap_down(close, open), _TD_QTR)


def gap_058_gap_total_abs_return_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Total absolute gap return over 63 days (all gap activity regardless of direction)."""
    return _rolling_sum(_gap_pct(close, open).abs(), _TD_QTR)


def gap_059_gap_total_abs_return_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Total absolute gap return over 252 days."""
    return _rolling_sum(_gap_pct(close, open).abs(), _TD_YEAR)


def gap_060_gap_down_share_of_total_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Down-gap magnitude as share of total absolute gap activity, 63d."""
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_QTR)
    tot_sum = _rolling_sum(_gap_pct(close, open).abs(), _TD_QTR).clip(lower=_EPS)
    return _safe_div(dn_sum, tot_sum)


# --- Group G (061-065): Normalized gap metrics, z-scores ---

def gap_061_gap_abs_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of today's abs gap vs 252-day distribution."""
    ag = _gap_pct(close, open).abs()
    m = _rolling_mean(ag, _TD_YEAR)
    s = _rolling_std(ag, _TD_YEAR)
    return _safe_div(ag - m, s)


def gap_062_gap_signed_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of today's signed gap vs 252-day distribution."""
    g = _gap_pct(close, open)
    m = _rolling_mean(g, _TD_YEAR)
    s = _rolling_std(g, _TD_YEAR)
    return _safe_div(g - m, s)


def gap_063_gap_abs_norm_63d_std(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's abs gap normalized by 63-day rolling std of abs gap."""
    ag = _gap_pct(close, open).abs()
    s = _rolling_std(ag, _TD_QTR)
    return _safe_div(ag, s)


def gap_064_gap_ewm_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-span EWM of signed gap (smoothed overnight drift)."""
    return _ewm_mean(_gap_pct(close, open), _TD_MON)


def gap_065_gap_vol_ratio_21d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day gap std to 252-day gap std (recent gap regime shift)."""
    ag = _gap_pct(close, open).abs()
    s21 = _rolling_std(ag, _TD_MON)
    s252 = _rolling_std(ag, _TD_YEAR)
    return _safe_div(s21, s252)


# --- Group H (066-075): Gap-type classification — common/breakaway/runaway/exhaustion ---
# Taxonomy (all backward-looking):
#   Common: small gap (< 0.5% abs), inside prior 21-day range, any volume.
#   Breakaway: gap outside prior 21-day range (range position < 0.1 or > 0.9),
#              volume elevated (> 1.2x avg), typically starting a new move.
#   Runaway: gap in the direction of the established trend (trend_dir matches gap dir),
#            mid-trend (trend maturity 0.3-0.7), volume moderate-to-high.
#   Exhaustion: gap in the direction of the established trend but late (maturity > 0.75 for
#               uptrend, < 0.25 for downtrend), volume climactic (> 1.5x avg);
#               tends to fill quickly (backward-confirmed).
# Down-gap variants are primary signals for capitulation.

def gap_066_common_gap_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's gap classifies as a common (area) gap: small (<0.5%) and inside prior 21d range."""
    g = _gap_pct(close, open)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    is_common = (ag > _EPS) & (ag < 0.005) & inside_range
    return is_common.astype(float)


def gap_067_breakaway_gap_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                volume: pd.Series) -> pd.Series:
    """1 if gap classifies as a breakaway: outside prior 21d range on elevated volume (>1.2x avg)."""
    g = _gap_pct(close, open)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open, _TD_MON)
    outside_range = (rng_pos <= 0.1) | (rng_pos >= 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    elevated_vol = vol_r > 1.2
    is_breakaway = (ag > 0.005) & outside_range & elevated_vol
    return is_breakaway.astype(float)


def gap_068_runaway_gap_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                              volume: pd.Series) -> pd.Series:
    """1 if gap classifies as a runaway (continuation): gap in trend direction, mid-trend, moderate vol."""
    g = _gap_pct(close, open)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    mid_trend = (maturity > 0.3) & (maturity < 0.72)
    rng_pos = _trailing_range_position(close, high, low, open, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    is_runaway = (ag > 0.005) & in_trend_dir & mid_trend & inside_range & (vol_r > 0.8)
    return is_runaway.astype(float)


def gap_069_exhaustion_gap_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                 volume: pd.Series) -> pd.Series:
    """1 if gap classifies as an exhaustion gap: late in extended trend on climactic volume (>1.5x avg)."""
    g = _gap_pct(close, open)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    # Exhaustion: late in uptrend (maturity > 0.75) or late in downtrend (maturity < 0.25)
    late_uptrend = (trend_dir > 0) & (maturity > 0.75)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    late_trend = late_uptrend | late_downtrend
    vol_r = _vol_ratio(volume, _TD_MON)
    climactic_vol = vol_r > 1.5
    is_exhaustion = (ag > 0.005) & in_trend_dir & late_trend & climactic_vol
    return is_exhaustion.astype(float)


def gap_070_exhaustion_gap_down_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """1 if today is a DOWN exhaustion gap: late in a downtrend, climactic volume. Key capitulation signal."""
    g = _gap_pct(close, open)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    maturity = _trend_maturity(close, _TD_QTR)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    gap_is_down = g < 0
    vol_r = _vol_ratio(volume, _TD_MON)
    climactic_vol = vol_r > 1.5
    is_exhaustion_down = (ag > 0.005) & gap_is_down & late_downtrend & climactic_vol
    return is_exhaustion_down.astype(float)


def gap_071_breakaway_gap_down_flag(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """1 if today is a DOWN breakaway gap: open breaks below prior 21d range on elevated volume."""
    g = _gap_pct(close, open)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open, _TD_MON)
    breaks_below = rng_pos <= 0.1
    gap_is_down = g < 0
    vol_r = _vol_ratio(volume, _TD_MON)
    elevated_vol = vol_r > 1.2
    is_breakaway_down = (ag > 0.005) & gap_is_down & breaks_below & elevated_vol
    return is_breakaway_down.astype(float)


def gap_072_common_gap_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of common (area) gaps in trailing 63 days."""
    flag = gap_066_common_gap_flag(close, open, high, low)
    return _rolling_sum(flag, _TD_QTR)


def gap_073_breakaway_gap_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """Count of breakaway gaps in trailing 63 days."""
    flag = gap_067_breakaway_gap_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_QTR)


def gap_074_exhaustion_gap_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Count of exhaustion gaps in trailing 63 days."""
    flag = gap_069_exhaustion_gap_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_QTR)


def gap_075_runaway_gap_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Count of runaway (continuation) gaps in trailing 63 days."""
    flag = gap_068_runaway_gap_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_REGISTRY_001_075 = {
    "gap_001_gap_pct": {"inputs": ["close", "open"], "func": gap_001_gap_pct},
    "gap_002_gap_abs_pct": {"inputs": ["close", "open"], "func": gap_002_gap_abs_pct},
    "gap_003_gap_up_pct": {"inputs": ["close", "open"], "func": gap_003_gap_up_pct},
    "gap_004_gap_down_pct": {"inputs": ["close", "open"], "func": gap_004_gap_down_pct},
    "gap_005_avg_gap_abs_5d": {"inputs": ["close", "open"], "func": gap_005_avg_gap_abs_5d},
    "gap_006_avg_gap_abs_21d": {"inputs": ["close", "open"], "func": gap_006_avg_gap_abs_21d},
    "gap_007_avg_gap_abs_63d": {"inputs": ["close", "open"], "func": gap_007_avg_gap_abs_63d},
    "gap_008_avg_gap_abs_252d": {"inputs": ["close", "open"], "func": gap_008_avg_gap_abs_252d},
    "gap_009_avg_signed_gap_21d": {"inputs": ["close", "open"], "func": gap_009_avg_signed_gap_21d},
    "gap_010_avg_signed_gap_63d": {"inputs": ["close", "open"], "func": gap_010_avg_signed_gap_63d},
    "gap_011_gap_up_freq_21d": {"inputs": ["close", "open"], "func": gap_011_gap_up_freq_21d},
    "gap_012_gap_down_freq_21d": {"inputs": ["close", "open"], "func": gap_012_gap_down_freq_21d},
    "gap_013_gap_up_freq_63d": {"inputs": ["close", "open"], "func": gap_013_gap_up_freq_63d},
    "gap_014_gap_down_freq_63d": {"inputs": ["close", "open"], "func": gap_014_gap_down_freq_63d},
    "gap_015_gap_up_freq_252d": {"inputs": ["close", "open"], "func": gap_015_gap_up_freq_252d},
    "gap_016_gap_down_freq_252d": {"inputs": ["close", "open"], "func": gap_016_gap_down_freq_252d},
    "gap_017_large_gap_freq_21d": {"inputs": ["close", "open"], "func": gap_017_large_gap_freq_21d},
    "gap_018_large_gap_freq_63d": {"inputs": ["close", "open"], "func": gap_018_large_gap_freq_63d},
    "gap_019_large_gap_freq_252d": {"inputs": ["close", "open"], "func": gap_019_large_gap_freq_252d},
    "gap_020_gap_down_vs_up_freq_ratio_63d": {"inputs": ["close", "open"], "func": gap_020_gap_down_vs_up_freq_ratio_63d},
    "gap_021_gap_std_21d": {"inputs": ["close", "open"], "func": gap_021_gap_std_21d},
    "gap_022_gap_std_63d": {"inputs": ["close", "open"], "func": gap_022_gap_std_63d},
    "gap_023_gap_std_252d": {"inputs": ["close", "open"], "func": gap_023_gap_std_252d},
    "gap_024_gap_median_abs_21d": {"inputs": ["close", "open"], "func": gap_024_gap_median_abs_21d},
    "gap_025_gap_median_abs_63d": {"inputs": ["close", "open"], "func": gap_025_gap_median_abs_63d},
    "gap_026_gap_median_abs_252d": {"inputs": ["close", "open"], "func": gap_026_gap_median_abs_252d},
    "gap_027_gap_up_avg_mag_63d": {"inputs": ["close", "open"], "func": gap_027_gap_up_avg_mag_63d},
    "gap_028_gap_down_avg_mag_63d": {"inputs": ["close", "open"], "func": gap_028_gap_down_avg_mag_63d},
    "gap_029_gap_up_avg_mag_252d": {"inputs": ["close", "open"], "func": gap_029_gap_up_avg_mag_252d},
    "gap_030_gap_down_avg_mag_252d": {"inputs": ["close", "open"], "func": gap_030_gap_down_avg_mag_252d},
    "gap_031_largest_up_gap_21d": {"inputs": ["close", "open"], "func": gap_031_largest_up_gap_21d},
    "gap_032_largest_up_gap_63d": {"inputs": ["close", "open"], "func": gap_032_largest_up_gap_63d},
    "gap_033_largest_up_gap_252d": {"inputs": ["close", "open"], "func": gap_033_largest_up_gap_252d},
    "gap_034_largest_down_gap_21d": {"inputs": ["close", "open"], "func": gap_034_largest_down_gap_21d},
    "gap_035_largest_down_gap_63d": {"inputs": ["close", "open"], "func": gap_035_largest_down_gap_63d},
    "gap_036_largest_down_gap_252d": {"inputs": ["close", "open"], "func": gap_036_largest_down_gap_252d},
    "gap_037_largest_abs_gap_21d": {"inputs": ["close", "open"], "func": gap_037_largest_abs_gap_21d},
    "gap_038_largest_abs_gap_63d": {"inputs": ["close", "open"], "func": gap_038_largest_abs_gap_63d},
    "gap_039_largest_abs_gap_252d": {"inputs": ["close", "open"], "func": gap_039_largest_abs_gap_252d},
    "gap_040_today_gap_pct_rank_252d": {"inputs": ["close", "open"], "func": gap_040_today_gap_pct_rank_252d},
    "gap_041_gap_fill_flag": {"inputs": ["close", "open", "high", "low"], "func": gap_041_gap_fill_flag},
    "gap_042_gap_fill_freq_21d": {"inputs": ["close", "open", "high", "low"], "func": gap_042_gap_fill_freq_21d},
    "gap_043_gap_fill_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_043_gap_fill_freq_63d},
    "gap_044_gap_fill_freq_252d": {"inputs": ["close", "open", "high", "low"], "func": gap_044_gap_fill_freq_252d},
    "gap_045_up_gap_fill_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_045_up_gap_fill_freq_63d},
    "gap_046_down_gap_fill_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_046_down_gap_fill_freq_63d},
    "gap_047_down_gap_fill_freq_252d": {"inputs": ["close", "open", "high", "low"], "func": gap_047_down_gap_fill_freq_252d},
    "gap_048_gap_not_filled_down_flag": {"inputs": ["close", "open", "high", "low"], "func": gap_048_gap_not_filled_down_flag},
    "gap_049_gap_not_filled_down_freq_21d": {"inputs": ["close", "open", "high", "low"], "func": gap_049_gap_not_filled_down_freq_21d},
    "gap_050_gap_not_filled_down_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_050_gap_not_filled_down_freq_63d},
    "gap_051_gap_return_sum_21d": {"inputs": ["close", "open"], "func": gap_051_gap_return_sum_21d},
    "gap_052_gap_return_sum_63d": {"inputs": ["close", "open"], "func": gap_052_gap_return_sum_63d},
    "gap_053_gap_return_sum_252d": {"inputs": ["close", "open"], "func": gap_053_gap_return_sum_252d},
    "gap_054_gap_up_return_sum_63d": {"inputs": ["close", "open"], "func": gap_054_gap_up_return_sum_63d},
    "gap_055_gap_down_return_sum_63d": {"inputs": ["close", "open"], "func": gap_055_gap_down_return_sum_63d},
    "gap_056_gap_down_return_sum_252d": {"inputs": ["close", "open"], "func": gap_056_gap_down_return_sum_252d},
    "gap_057_gap_net_bias_63d": {"inputs": ["close", "open"], "func": gap_057_gap_net_bias_63d},
    "gap_058_gap_total_abs_return_63d": {"inputs": ["close", "open"], "func": gap_058_gap_total_abs_return_63d},
    "gap_059_gap_total_abs_return_252d": {"inputs": ["close", "open"], "func": gap_059_gap_total_abs_return_252d},
    "gap_060_gap_down_share_of_total_63d": {"inputs": ["close", "open"], "func": gap_060_gap_down_share_of_total_63d},
    "gap_061_gap_abs_zscore_252d": {"inputs": ["close", "open"], "func": gap_061_gap_abs_zscore_252d},
    "gap_062_gap_signed_zscore_252d": {"inputs": ["close", "open"], "func": gap_062_gap_signed_zscore_252d},
    "gap_063_gap_abs_norm_63d_std": {"inputs": ["close", "open"], "func": gap_063_gap_abs_norm_63d_std},
    "gap_064_gap_ewm_21d": {"inputs": ["close", "open"], "func": gap_064_gap_ewm_21d},
    "gap_065_gap_vol_ratio_21d_vs_252d": {"inputs": ["close", "open"], "func": gap_065_gap_vol_ratio_21d_vs_252d},
    "gap_066_common_gap_flag": {"inputs": ["close", "open", "high", "low"], "func": gap_066_common_gap_flag},
    "gap_067_breakaway_gap_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_067_breakaway_gap_flag},
    "gap_068_runaway_gap_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_068_runaway_gap_flag},
    "gap_069_exhaustion_gap_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_069_exhaustion_gap_flag},
    "gap_070_exhaustion_gap_down_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_070_exhaustion_gap_down_flag},
    "gap_071_breakaway_gap_down_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_071_breakaway_gap_down_flag},
    "gap_072_common_gap_count_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_072_common_gap_count_63d},
    "gap_073_breakaway_gap_count_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_073_breakaway_gap_count_63d},
    "gap_074_exhaustion_gap_count_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_074_exhaustion_gap_count_63d},
    "gap_075_runaway_gap_count_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_075_runaway_gap_count_63d},
}
