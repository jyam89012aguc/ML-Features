"""
46_gap_structure — Extended Features 001-075
Domain: overnight gap frequency, magnitude, fill dynamics, type z-scores, direction persistence,
        gap-adjusted returns, overnight-return distribution, and gap vs prior-day range.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features backward-looking only. Self-contained: numpy/pandas only.
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
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight gap as fraction of prior close: (open - prior_close) / prior_close."""
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(lower=0)


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(upper=0).abs()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Gap-type classification helpers ───────────────────────────────────────────

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True,
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _exhaustion_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                               low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    maturity = _trend_maturity(close, _TD_QTR)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & late_downtrend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                              low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & (rng_pos <= 0.1) & (vol_r > 1.2)).astype(float)


def _runaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                      low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    mid_trend = (maturity > 0.3) & (maturity < 0.72)
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & mid_trend & inside_range & (vol_r > 0.8)).astype(float)


def _exhaustion_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                         low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    late_uptrend = (trend_dir > 0) & (maturity > 0.75)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    late_trend = late_uptrend | late_downtrend
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & late_trend & (vol_r > 1.5)).astype(float)


def _common_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                     low: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    return ((ag > _EPS) & (ag < 0.005) & inside_range).astype(float)


def _breakaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series,
                        low: pd.Series, volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    outside_range = (rng_pos <= 0.1) | (rng_pos >= 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & outside_range & (vol_r > 1.2)).astype(float)


def _days_since_flag(flag: pd.Series, max_lookback: int = _TD_YEAR) -> pd.Series:
    """Days elapsed since last True bar; NaN if none in trailing max_lookback bars."""
    flag_arr = flag.values.astype(float)
    result = np.full(len(flag_arr), np.nan)
    for i in range(len(flag_arr)):
        start = max(0, i - max_lookback + 1)
        sub = flag_arr[start: i + 1]
        hits = np.where(sub > 0)[0]
        if len(hits) > 0:
            result[i] = float(len(sub) - 1 - hits[-1])
    return pd.Series(result, index=flag.index)


def _prior_day_range_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Prior day's high-low range as pct of prior close."""
    pc = close.shift(1).abs().clip(lower=_EPS)
    return _safe_div(high.shift(1) - low.shift(1), pc)


def _atr_pct(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Rolling ATR as pct of prior close."""
    tr = pd.concat(
        [high - low,
         (high - close.shift(1)).abs(),
         (low - close.shift(1)).abs()],
        axis=1,
    ).max(axis=1)
    pc = close.shift(1).abs().clip(lower=_EPS)
    return _rolling_mean(tr, w) / pc


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Per-type magnitude z-scores (new: z-score within type) ---

def gap_ext_001_exhaustion_down_mag_zscore_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of today's down-exhaustion gap magnitude vs 252d distribution of that type."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    return _safe_div(mag_on_type - m, s.clip(lower=_EPS))


def gap_ext_002_breakaway_down_mag_zscore_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of today's down-breakaway gap magnitude vs 252d within-type distribution."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    return _safe_div(mag_on_type - m, s.clip(lower=_EPS))


def gap_ext_003_runaway_down_mag_zscore_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of today's runaway down-gap magnitude vs 252d within-type distribution."""
    run_flag = _runaway_gap_flag(close, open, high, low, volume)
    g = _gap_pct(close, open)
    dg = _gap_down(close, open)
    combined = (run_flag > 0) & (g < 0)
    mag_on_type = dg.where(combined, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    return _safe_div(mag_on_type - m, s.clip(lower=_EPS))


def gap_ext_004_common_gap_mag_zscore_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Z-score of today's common gap abs-magnitude vs 252d within-type distribution."""
    flag = _common_gap_flag(close, open, high, low)
    ag = _gap_pct(close, open).abs()
    mag_on_type = ag.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_YEAR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_YEAR, min_periods=2).std()
    return _safe_div(mag_on_type - m, s.clip(lower=_EPS))


def gap_ext_005_exhaustion_down_mag_zscore_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of today's down-exhaustion gap magnitude vs 63d within-type distribution."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_type = dg.where(flag > 0, np.nan)
    m = mag_on_type.rolling(_TD_QTR, min_periods=1).mean()
    s = mag_on_type.rolling(_TD_QTR, min_periods=2).std()
    return _safe_div(mag_on_type - m, s.clip(lower=_EPS))


# --- Group B (006-015): Per-type fill-time distributions (new windows / types) ---

def gap_ext_006_exhaustion_down_fill_21d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fraction of down-exhaustion gaps (21 days ago) that filled within 21 days. Backward-safe."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    flag_shifted = flag.shift(_TD_MON)
    prior_close_shifted = close.shift(1).shift(_TD_MON)
    roll_high = high.rolling(_TD_MON, min_periods=1).max()
    dn_filled = (flag_shifted > 0) & (roll_high >= prior_close_shifted)
    has_flag = (flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(dn_filled.astype(float), _TD_HALF),
        _rolling_sum(has_flag, _TD_HALF).clip(lower=1),
    )


def gap_ext_007_breakaway_down_fill_21d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fraction of down-breakaway gaps (21 days ago) that filled within 21 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    flag_shifted = flag.shift(_TD_MON)
    prior_close_shifted = close.shift(1).shift(_TD_MON)
    roll_high = high.rolling(_TD_MON, min_periods=1).max()
    dn_filled = (flag_shifted > 0) & (roll_high >= prior_close_shifted)
    has_flag = (flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(dn_filled.astype(float), _TD_HALF),
        _rolling_sum(has_flag, _TD_HALF).clip(lower=1),
    )


def gap_ext_008_runaway_fill_10d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fraction of runaway gaps (10 days ago) that filled within 10 days."""
    n = 10
    flag = _runaway_gap_flag(close, open, high, low, volume)
    flag_shifted = flag.shift(n)
    g_shifted = _gap_pct(close, open).shift(n)
    prior_close_shifted = close.shift(1).shift(n)
    roll_high = high.rolling(n, min_periods=1).max()
    roll_low = low.rolling(n, min_periods=1).min()
    up_filled = (g_shifted > 0) & (roll_low <= prior_close_shifted)
    dn_filled = (g_shifted < 0) & (roll_high >= prior_close_shifted)
    filled = ((up_filled | dn_filled) & (flag_shifted > 0)).astype(float)
    has_flag = (flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(filled, _TD_QTR),
        _rolling_sum(has_flag, _TD_QTR).clip(lower=1),
    )


def gap_ext_009_exhaustion_any_fill_10d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fraction of any-direction exhaustion gaps (10 days ago) filled within 10 days."""
    n = 10
    flag = _exhaustion_gap_flag(close, open, high, low, volume)
    flag_shifted = flag.shift(n)
    g_shifted = _gap_pct(close, open).shift(n)
    prior_close_shifted = close.shift(1).shift(n)
    roll_high = high.rolling(n, min_periods=1).max()
    roll_low = low.rolling(n, min_periods=1).min()
    up_filled = (g_shifted > 0) & (roll_low <= prior_close_shifted)
    dn_filled = (g_shifted < 0) & (roll_high >= prior_close_shifted)
    filled = ((up_filled | dn_filled) & (flag_shifted > 0)).astype(float)
    has_flag = (flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(filled, _TD_QTR),
        _rolling_sum(has_flag, _TD_QTR).clip(lower=1),
    )


def gap_ext_010_common_gap_fill_5d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fraction of common gaps (5 days ago) that filled within 5 days."""
    n = _TD_WEEK
    flag = _common_gap_flag(close, open, high, low)
    flag_shifted = flag.shift(n)
    g_shifted = _gap_pct(close, open).shift(n)
    prior_close_shifted = close.shift(1).shift(n)
    roll_high = high.rolling(n, min_periods=1).max()
    roll_low = low.rolling(n, min_periods=1).min()
    up_filled = (g_shifted > 0) & (roll_low <= prior_close_shifted)
    dn_filled = (g_shifted < 0) & (roll_high >= prior_close_shifted)
    filled = ((up_filled | dn_filled) & (flag_shifted > 0)).astype(float)
    has_flag = (flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(filled, _TD_QTR),
        _rolling_sum(has_flag, _TD_QTR).clip(lower=1),
    )


# --- Group C (011-017): Per-type volume profiles (new: vol on each type at various windows) ---

def gap_ext_011_exhaustion_down_vol_zscore_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Z-score of today's volume vs 63d avg volume on down-exhaustion days only."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    vol_on_type = volume.where(flag > 0, np.nan)
    m = vol_on_type.rolling(_TD_QTR, min_periods=1).mean()
    s = vol_on_type.rolling(_TD_QTR, min_periods=2).std()
    return _safe_div(volume.where(flag > 0, np.nan) - m, s.clip(lower=_EPS))


def gap_ext_012_runaway_vol_avg_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Average vol-ratio on runaway gap days over 63 days."""
    flag = _runaway_gap_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    return vol_on_type.rolling(_TD_QTR, min_periods=1).mean()


def gap_ext_013_common_gap_vol_avg_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Average vol-ratio on common gap days over 63 days."""
    flag = _common_gap_flag(close, open, high, low)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    return vol_on_type.rolling(_TD_QTR, min_periods=1).mean()


def gap_ext_014_exhaustion_down_vol_avg_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Average vol-ratio on down-exhaustion days over 252 days."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    return vol_on_type.rolling(_TD_YEAR, min_periods=1).mean()


def gap_ext_015_breakaway_down_vol_avg_252d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Average vol-ratio on down-breakaway days over 252 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_type = vol_r.where(flag > 0, np.nan)
    return vol_on_type.rolling(_TD_YEAR, min_periods=1).mean()


# --- Group D (016-020): Days-since per type at additional windows ---

def gap_ext_016_days_since_breakaway_gap_any(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Days since last any-direction breakaway gap; NaN if none in 252 days."""
    flag = _breakaway_gap_flag(close, open, high, low, volume)
    return _days_since_flag(flag, _TD_YEAR)


def gap_ext_017_days_since_runaway_gap_any(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Days since last any-direction runaway gap; NaN if none in 252 days."""
    flag = _runaway_gap_flag(close, open, high, low, volume)
    return _days_since_flag(flag, _TD_YEAR)


def gap_ext_018_days_since_common_gap(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since last common (area) gap; NaN if none in 252 days."""
    flag = _common_gap_flag(close, open, high, low)
    return _days_since_flag(flag, _TD_YEAR)


def gap_ext_019_days_since_large_gap_down(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Days since last down gap with abs-magnitude > 2%; NaN if none in 252 days."""
    g = _gap_pct(close, open)
    flag = (g < -0.02).astype(float)
    return _days_since_flag(flag, _TD_YEAR)


def gap_ext_020_days_since_large_gap_up(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Days since last up gap with abs-magnitude > 2%; NaN if none in 252 days."""
    g = _gap_pct(close, open)
    flag = (g > 0.02).astype(float)
    return _days_since_flag(flag, _TD_YEAR)


# --- Group E (021-027): Gap-fill dynamics — partial fill, unfilled overhang, nearest unfilled ---

def gap_ext_021_partial_fill_fraction_5d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """For each bar with a gap, fraction of gap recovered intraday (partial fill), 5d look-back.
    On a down gap: max(0, high - open) / abs(gap_price). Averaged over 5 days."""
    prior_close = close.shift(1)
    gap_price = open - prior_close  # signed
    dn_gap = gap_price < 0
    up_gap = gap_price > 0
    # Down gap partial fill: how much did high recover above open toward prior_close?
    dn_recover = (high - open).clip(lower=0)
    dn_full = gap_price.abs().clip(lower=_EPS)
    dn_frac = _safe_div(dn_recover, dn_full).clip(0.0, 1.0)
    # Up gap partial fill: how much did low fill back toward prior_close?
    up_recover = (open - low).clip(lower=0)
    up_full = gap_price.abs().clip(lower=_EPS)
    up_frac = _safe_div(up_recover, up_full).clip(0.0, 1.0)
    partial = pd.Series(np.nan, index=close.index)
    partial = partial.where(~dn_gap, dn_frac)
    partial = partial.where(~up_gap, up_frac)
    return partial.rolling(_TD_WEEK, min_periods=1).mean()


def gap_ext_022_partial_fill_fraction_21d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day rolling average of intraday partial gap-fill fraction."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    dn_gap = gap_price < 0
    up_gap = gap_price > 0
    dn_frac = _safe_div((high - open).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    up_frac = _safe_div((open - low).clip(lower=0), gap_price.abs().clip(lower=_EPS)).clip(0.0, 1.0)
    partial = pd.Series(np.nan, index=close.index)
    partial = partial.where(~dn_gap, dn_frac)
    partial = partial.where(~up_gap, up_frac)
    return partial.rolling(_TD_MON, min_periods=1).mean()


def gap_ext_023_unfilled_down_gap_count_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of unfilled down gaps remaining in the trailing 63-day window.
    A gap from day t is 'unfilled' if high in [t..today] never reached prior_close(t)."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    dn_gap = (gap_price < 0).astype(float)
    # On day t: was the high in [t..today] >= prior_close_t? (filled = 1)
    # We evaluate this the backward-safe way: for each day, look at the gap from n days ago
    # and check whether the rolling high since that day covers it. We do this for n=1..63.
    # Efficient vectorized: unfilled_today = dn_gap AND rolling max high from t to today < prior_close_t
    # Instead we track: for each current bar, how many prior dn gaps in past 63d are still open?
    # We approximate: a dn gap on day t is unfilled at bar i iff roll_high(t..i) < prior_close_t.
    # Since we can't do this per-origin-bar easily without a loop, we use a proxy:
    # count of down-gap days in [i-63..i] whose prior_close > rolling high from that day to today.
    # We use a scalar rolling check: for offset k in 1..63, was the gap at bar[i-k] filled?
    # We precompute filled_at_k = dn_gap.shift(k) & (roll_high_k >= prior_close_shifted_k)
    w = _TD_QTR
    total_unfilled = pd.Series(0.0, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        dg_k = (gap_price.shift(k) < 0)
        # rolling max high from k bars ago to today = rolling max over k bars
        rh_k = high.rolling(k, min_periods=1).max()
        filled_k = dg_k & (rh_k >= pc_k)
        unfilled_k = (dg_k & ~filled_k).astype(float)
        total_unfilled = total_unfilled + unfilled_k
    return total_unfilled


def gap_ext_024_unfilled_up_gap_count_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of unfilled up gaps remaining in the trailing 63-day window."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    w = _TD_QTR
    total_unfilled = pd.Series(0.0, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        ug_k = (gap_price.shift(k) > 0)
        rl_k = low.rolling(k, min_periods=1).min()
        filled_k = ug_k & (rl_k <= pc_k)
        unfilled_k = (ug_k & ~filled_k).astype(float)
        total_unfilled = total_unfilled + unfilled_k
    return total_unfilled


def gap_ext_025_nearest_unfilled_down_gap_distance(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Distance (in pct of current close) to the nearest unfilled down gap's prior_close level.
    Looks back up to 63 days. NaN if no unfilled down gap exists."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    w = _TD_QTR
    result = pd.Series(np.nan, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        dg_k = gap_price.shift(k) < 0
        rh_k = high.rolling(k, min_periods=1).max()
        unfilled_k = dg_k & (rh_k < pc_k)
        dist_k = _safe_div((close - pc_k).abs(), close.abs().clip(lower=_EPS))
        # Keep the nearest (smallest distance) unfilled gap
        result = result.where(~unfilled_k | (result <= dist_k), dist_k)
    return result


def gap_ext_026_nearest_unfilled_up_gap_distance(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Distance (pct of current close) to nearest unfilled up gap's prior_close level, back 63 days."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    w = _TD_QTR
    result = pd.Series(np.nan, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        ug_k = gap_price.shift(k) > 0
        rl_k = low.rolling(k, min_periods=1).min()
        unfilled_k = ug_k & (rl_k > pc_k)
        dist_k = _safe_div((close - pc_k).abs(), close.abs().clip(lower=_EPS))
        result = result.where(~unfilled_k | (result <= dist_k), dist_k)
    return result


def gap_ext_027_unfilled_down_gap_overhang_magnitude(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Sum of all unfilled down-gap magnitudes (as pct of respective prior_close) in trailing 63 days.
    Measures total overhead supply from open gaps."""
    prior_close = close.shift(1)
    gap_price = open - prior_close
    w = _TD_QTR
    total_mag = pd.Series(0.0, index=close.index)
    for k in range(1, w + 1):
        pc_k = prior_close.shift(k)
        gp_k = gap_price.shift(k)
        dg_k = gp_k < 0
        rh_k = high.rolling(k, min_periods=1).max()
        unfilled_k = dg_k & (rh_k < pc_k)
        mag_k = _safe_div(gp_k.abs(), pc_k.abs().clip(lower=_EPS))
        total_mag = total_mag + mag_k.where(unfilled_k, 0.0).fillna(0.0)
    return total_mag


# --- Group F (028-034): Cumulative gap contribution to total return ---

def gap_ext_028_gap_cumret_vs_total_cumret_126d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """126-day cumulative gap return as fraction of 126-day total cumulative return."""
    gap_sum = _rolling_sum(_gap_pct(close, open), _TD_HALF)
    total_sum = _rolling_sum(close.pct_change(1), _TD_HALF)
    return _safe_div(gap_sum, total_sum.replace(0, np.nan))


def gap_ext_029_gap_down_cumret_share_126d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Down-gap cumulative magnitude as share of total 126-day absolute return."""
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_HALF)
    tot_abs = _rolling_sum(close.pct_change(1).abs(), _TD_HALF).clip(lower=_EPS)
    return _safe_div(dn_sum, tot_abs)


def gap_ext_030_gap_up_cumret_share_126d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Up-gap cumulative magnitude as share of total 126-day absolute return."""
    up_sum = _rolling_sum(_gap_up(close, open), _TD_HALF)
    tot_abs = _rolling_sum(close.pct_change(1).abs(), _TD_HALF).clip(lower=_EPS)
    return _safe_div(up_sum, tot_abs)


def gap_ext_031_gap_net_contribution_126d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Net overnight gap contribution to 126d return: (up_gap_sum - down_gap_sum) / total_abs_ret."""
    up_sum = _rolling_sum(_gap_up(close, open), _TD_HALF)
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_HALF)
    tot_abs = _rolling_sum(close.pct_change(1).abs(), _TD_HALF).clip(lower=_EPS)
    return _safe_div(up_sum - dn_sum, tot_abs)


def gap_ext_032_gap_adjusted_return_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day total return minus 21-day cumulative gap return (intraday-only component)."""
    total_ret = _rolling_sum(close.pct_change(1), _TD_MON)
    gap_ret = _rolling_sum(_gap_pct(close, open), _TD_MON)
    return total_ret - gap_ret


def gap_ext_033_gap_adjusted_return_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """63-day total return minus 63-day cumulative gap return (intraday-only component)."""
    total_ret = _rolling_sum(close.pct_change(1), _TD_QTR)
    gap_ret = _rolling_sum(_gap_pct(close, open), _TD_QTR)
    return total_ret - gap_ret


def gap_ext_034_gap_vs_raw_return_divergence_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Absolute difference between 63d gap-adjusted return and 63d raw return, normalized by raw return std."""
    total_ret = _rolling_sum(close.pct_change(1), _TD_QTR)
    gap_ret = _rolling_sum(_gap_pct(close, open), _TD_QTR)
    intra = total_ret - gap_ret
    ret_std = _rolling_std(close.pct_change(1), _TD_QTR).clip(lower=_EPS)
    return _safe_div((intra - total_ret).abs(), ret_std)


# --- Group G (035-041): Gap direction persistence and reversal signatures ---

def gap_ext_035_consecutive_same_dir_gap_run(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Current run length of consecutive same-direction gaps (+ = up streak, - = down streak)."""
    g = _gap_pct(close, open)
    g_dir = np.sign(g)
    run = pd.Series(0.0, index=close.index)
    arr = g_dir.values
    result = np.zeros(len(arr))
    for i in range(1, len(arr)):
        if arr[i] == 0:
            result[i] = 0.0
        elif arr[i] == arr[i - 1] and arr[i] != 0:
            result[i] = result[i - 1] + arr[i]
        else:
            result[i] = arr[i]
    return pd.Series(result, index=close.index)


def gap_ext_036_max_down_gap_run_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Maximum consecutive down-gap run length in trailing 21 days."""
    g = _gap_pct(close, open)
    is_dn = (g < 0).astype(float)
    # Build run-length series of consecutive down days
    run = is_dn.copy()
    run_arr = is_dn.values.copy()
    rl = np.zeros(len(run_arr))
    for i in range(len(run_arr)):
        if run_arr[i] > 0:
            rl[i] = (rl[i - 1] + 1) if i > 0 else 1.0
        else:
            rl[i] = 0.0
    rl_s = pd.Series(rl, index=close.index)
    return rl_s.rolling(_TD_MON, min_periods=1).max()


def gap_ext_037_max_up_gap_run_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Maximum consecutive up-gap run length in trailing 21 days."""
    g = _gap_pct(close, open)
    is_up = (g > 0).astype(float)
    run_arr = is_up.values.copy()
    rl = np.zeros(len(run_arr))
    for i in range(len(run_arr)):
        if run_arr[i] > 0:
            rl[i] = (rl[i - 1] + 1) if i > 0 else 1.0
        else:
            rl[i] = 0.0
    rl_s = pd.Series(rl, index=close.index)
    return rl_s.rolling(_TD_MON, min_periods=1).max()


def gap_ext_038_gap_down_then_close_up_flag(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """1 if today has a down gap AND close > prior_close (gap-down then close-up reversal signal)."""
    g = _gap_pct(close, open)
    prior_close = close.shift(1)
    return ((g < 0) & (close > prior_close)).astype(float)


def gap_ext_039_gap_down_then_close_up_freq_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day frequency of down-gap / close-up reversal days."""
    return _rolling_mean(gap_ext_038_gap_down_then_close_up_flag(close, open), _TD_MON)


def gap_ext_040_gap_down_then_close_up_freq_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """63-day frequency of down-gap / close-up reversal days."""
    return _rolling_mean(gap_ext_038_gap_down_then_close_up_flag(close, open), _TD_QTR)


def gap_ext_041_gap_up_then_close_down_freq_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """63-day frequency of up-gap / close-below-prior reversal days (fade-the-gap pattern)."""
    g = _gap_pct(close, open)
    prior_close = close.shift(1)
    flag = ((g > 0) & (close < prior_close)).astype(float)
    return _rolling_mean(flag, _TD_QTR)


# --- Group H (042-047): Gap volatility — dispersion features not in existing set ---

def gap_ext_042_gap_iqr_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """63-day interquartile range of signed gap (robust gap dispersion)."""
    g = _gap_pct(close, open)
    q75 = g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def gap_ext_043_gap_iqr_252d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """252-day IQR of signed gap."""
    g = _gap_pct(close, open)
    q75 = g.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = g.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def gap_ext_044_gap_down_dispersion_ratio_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Ratio of std of down-gap magnitudes to std of up-gap magnitudes over 63 days."""
    dg = _gap_down(close, open)
    ug = _gap_up(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    ug_nan = ug.where(ug > 0, np.nan)
    std_dn = dg_nan.rolling(_TD_QTR, min_periods=2).std()
    std_up = ug_nan.rolling(_TD_QTR, min_periods=2).std()
    return _safe_div(std_dn, std_up.clip(lower=_EPS))


def gap_ext_045_gap_kurtosis_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """63-day excess kurtosis of signed gap distribution (fat-tail measure)."""
    g = _gap_pct(close, open)
    m = _rolling_mean(g, _TD_QTR)
    s = _rolling_std(g, _TD_QTR).clip(lower=_EPS)
    z = _safe_div(g - m, s)
    return z.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda x: float(np.mean(x ** 4)) - 3.0, raw=True
    )


def gap_ext_046_gap_std_short_vs_long_ratio(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Ratio of 5-day gap std to 63-day gap std (very short vs medium regime shift)."""
    ag = _gap_pct(close, open)
    s5 = _rolling_std(ag, _TD_WEEK)
    s63 = _rolling_std(ag, _TD_QTR)
    return _safe_div(s5, s63.clip(lower=_EPS))


def gap_ext_047_gap_down_std_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Standard deviation of down-gap magnitudes over 63 days."""
    dg = _gap_down(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    return dg_nan.rolling(_TD_QTR, min_periods=2).std()


# --- Group I (048-053): Gap vs prior-day range ---

def gap_ext_048_gap_vs_prior_range_ratio(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Today's abs gap as fraction of prior day's high-low range."""
    ag = _gap_pct(close, open).abs()
    prior_range = _prior_day_range_pct(close, high, low).clip(lower=_EPS)
    return _safe_div(ag, prior_range)


def gap_ext_049_gap_vs_prior_range_ratio_21d_avg(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day average of abs-gap / prior-day-range ratio."""
    return _rolling_mean(gap_ext_048_gap_vs_prior_range_ratio(close, open, high, low), _TD_MON)


def gap_ext_050_gap_vs_prior_range_ratio_63d_avg(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """63-day average of abs-gap / prior-day-range ratio."""
    return _rolling_mean(gap_ext_048_gap_vs_prior_range_ratio(close, open, high, low), _TD_QTR)


def gap_ext_051_gap_exceeds_prior_range_freq_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fraction of 63 days where abs gap exceeds prior day's full H-L range."""
    ratio = gap_ext_048_gap_vs_prior_range_ratio(close, open, high, low)
    return _rolling_count_true(ratio > 1.0, _TD_QTR) / _TD_QTR


def gap_ext_052_gap_down_vs_prior_range_63d_avg(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """63-day average of down-gap magnitude / prior-day-range (down-gap severity vs range)."""
    dg = _gap_down(close, open)
    prior_range = _prior_day_range_pct(close, high, low).clip(lower=_EPS)
    ratio = _safe_div(dg, prior_range)
    return _rolling_mean(ratio, _TD_QTR)


def gap_ext_053_open_outside_prior_range_freq_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fraction of 63 days where open is outside prior day's H-L range (any direction)."""
    outside = ((open > high.shift(1)) | (open < low.shift(1))).astype(float)
    return _rolling_count_true(outside > 0, _TD_QTR) / _TD_QTR


# --- Group J (054-060): Overnight return distribution features ---

def gap_ext_054_overnight_ret_percentile_126d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Percentile rank of today's signed gap within trailing 126-day signed gap distribution."""
    g = _gap_pct(close, open)
    return g.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def gap_ext_055_gap_down_percentile_rank_252d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Percentile rank of today's down-gap magnitude within 252-day down-gap distribution."""
    dg = _gap_down(close, open)
    dg_nan = dg.where(dg > 0, np.nan)
    return dg_nan.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).rank(pct=True)


def gap_ext_056_overnight_ret_5pct_threshold_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """5th-percentile threshold of overnight return in trailing 63 days (left tail level)."""
    g = _gap_pct(close, open)
    return g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)


def gap_ext_057_overnight_ret_95pct_threshold_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """95th-percentile threshold of overnight return in trailing 63 days (right tail level)."""
    g = _gap_pct(close, open)
    return g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.95)


def gap_ext_058_overnight_ret_left_tail_mass_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Fraction of 63-day overnight returns below -2% (left-tail probability mass)."""
    g = _gap_pct(close, open)
    return _rolling_count_true(g < -0.02, _TD_QTR) / _TD_QTR


def gap_ext_059_overnight_ret_right_tail_mass_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Fraction of 63-day overnight returns above +2% (right-tail probability mass)."""
    g = _gap_pct(close, open)
    return _rolling_count_true(g > 0.02, _TD_QTR) / _TD_QTR


def gap_ext_060_overnight_ret_tail_asymmetry_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Left-tail mass minus right-tail mass (>0 = more large down gaps than up gaps)."""
    return gap_ext_058_overnight_ret_left_tail_mass_63d(close, open) - \
           gap_ext_059_overnight_ret_right_tail_mass_63d(close, open)


# --- Group K (061-068): Consecutive gap run statistics ---

def gap_ext_061_down_gap_run_freq_3plus_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Fraction of 63-day windows containing a run of 3+ consecutive down gaps."""
    g = _gap_pct(close, open)
    is_dn = (g < 0).astype(float).values
    rl = np.zeros(len(is_dn))
    for i in range(len(is_dn)):
        rl[i] = (rl[i - 1] + 1) if (i > 0 and is_dn[i] > 0) else (1.0 if is_dn[i] > 0 else 0.0)
    rl_s = pd.Series(rl, index=close.index)
    run3 = (rl_s >= 3).astype(float)
    return _rolling_count_true(run3 > 0, _TD_QTR) / _TD_QTR


def gap_ext_062_up_gap_run_freq_3plus_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Fraction of 63-day windows with a run of 3+ consecutive up gaps."""
    g = _gap_pct(close, open)
    is_up = (g > 0).astype(float).values
    rl = np.zeros(len(is_up))
    for i in range(len(is_up)):
        rl[i] = (rl[i - 1] + 1) if (i > 0 and is_up[i] > 0) else (1.0 if is_up[i] > 0 else 0.0)
    rl_s = pd.Series(rl, index=close.index)
    run3 = (rl_s >= 3).astype(float)
    return _rolling_count_true(run3 > 0, _TD_QTR) / _TD_QTR


def gap_ext_063_avg_down_gap_run_length_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Average length of consecutive down-gap runs in trailing 63 days."""
    g = _gap_pct(close, open)
    is_dn = (g < 0).astype(float).values
    rl = np.zeros(len(is_dn))
    for i in range(len(is_dn)):
        rl[i] = (rl[i - 1] + 1) if (i > 0 and is_dn[i] > 0) else (1.0 if is_dn[i] > 0 else 0.0)
    # Detect end-of-run (last day of each run, or single-day run)
    run_end = np.zeros(len(rl))
    for i in range(len(rl)):
        if rl[i] > 0 and (i + 1 >= len(rl) or rl[i + 1] == 0 or is_dn[i + 1] == 0):
            run_end[i] = rl[i]
    run_end_s = pd.Series(run_end, index=close.index)
    run_end_nonzero = run_end_s.where(run_end_s > 0, np.nan)
    return run_end_nonzero.rolling(_TD_QTR, min_periods=1).mean()


def gap_ext_064_down_gap_run_momentum_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """21-day sum of down-gap run lengths (runs weighted by length — momentum of streaks)."""
    g = _gap_pct(close, open)
    is_dn = (g < 0).astype(float).values
    rl = np.zeros(len(is_dn))
    for i in range(len(is_dn)):
        rl[i] = (rl[i - 1] + 1) if (i > 0 and is_dn[i] > 0) else (1.0 if is_dn[i] > 0 else 0.0)
    rl_s = pd.Series(rl, index=close.index)
    return _rolling_sum(rl_s, _TD_MON)


# --- Group L (065-071): Gap frequency rate-of-change and acceleration ---

def gap_ext_065_gap_freq_roc_21d_to_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Rate of change: 21-day gap frequency vs 63-day gap frequency (recent vs medium-term)."""
    g = _gap_pct(close, open)
    has_gap = (g.abs() > _EPS).astype(float)
    freq21 = _rolling_sum(has_gap, _TD_MON) / _TD_MON
    freq63 = _rolling_sum(has_gap, _TD_QTR) / _TD_QTR
    return _safe_div(freq21 - freq63, freq63.clip(lower=_EPS))


def gap_ext_066_gap_down_freq_roc_21d_to_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Rate of change: 21-day down-gap frequency vs 63-day down-gap frequency."""
    g = _gap_pct(close, open)
    freq21 = _rolling_count_true(g < 0, _TD_MON) / _TD_MON
    freq63 = _rolling_count_true(g < 0, _TD_QTR) / _TD_QTR
    return _safe_div(freq21 - freq63, freq63.clip(lower=_EPS))


def gap_ext_067_gap_magnitude_roc_5d_to_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """Rate of change: 5-day avg abs-gap vs 21-day avg abs-gap (very recent vs monthly)."""
    ag = _gap_pct(close, open).abs()
    avg5 = _rolling_mean(ag, _TD_WEEK)
    avg21 = _rolling_mean(ag, _TD_MON)
    return _safe_div(avg5 - avg21, avg21.clip(lower=_EPS))


def gap_ext_068_gap_down_magnitude_acceleration_21d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """OLS slope of rolling 5-day avg down-gap magnitude over trailing 21 days (acceleration)."""
    dg = _gap_down(close, open)
    avg5 = _rolling_mean(dg, _TD_WEEK)
    return _linslope(avg5, _TD_MON)


def gap_ext_069_gap_freq_acceleration_slope_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """OLS slope of rolling 21-day any-gap frequency over trailing 63 days."""
    g = _gap_pct(close, open)
    has_gap = (g.abs() > _EPS).astype(float)
    freq21 = _rolling_sum(has_gap, _TD_MON) / _TD_MON
    return _linslope(freq21, _TD_QTR)


def gap_ext_070_gap_down_freq_acceleration_slope_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """OLS slope of rolling 21-day down-gap frequency over trailing 63 days."""
    g = _gap_pct(close, open)
    freq21 = _rolling_count_true(g < 0, _TD_MON) / _TD_MON
    return _linslope(freq21, _TD_QTR)


# --- Group M (071-075): Additional net-new composite / gap-type timing features ---

def gap_ext_071_exhaustion_down_count_126d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Count of down-exhaustion gaps in trailing 126 days (half-year window, not in existing set)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_HALF)


def gap_ext_072_breakaway_down_count_126d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Count of down-breakaway gaps in trailing 126 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_HALF)


def gap_ext_073_gap_type_down_distress_score_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """63-day weighted distress score (exhaustion-down=3, breakaway-down=2, runaway-down=1).
    Distinct from existing 21d score in file 2 by window and weights."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    run_flag = _runaway_gap_flag(close, open, high, low, volume)
    g = _gap_pct(close, open)
    run_dn = ((run_flag > 0) & (g < 0)).astype(float)
    score = 3.0 * ex_dn + 2.0 * ba_dn + 1.0 * run_dn
    return _rolling_sum(score, _TD_QTR)


def gap_ext_074_gap_type_cluster_flag(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """1 if both an exhaustion-down and a breakaway-down gap occurred in the trailing 5 days
    (cluster of high-severity gap types = capitulation cluster signal)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    ex_in_5d = _rolling_sum(ex_dn, _TD_WEEK) > 0
    ba_in_5d = _rolling_sum(ba_dn, _TD_WEEK) > 0
    return (ex_in_5d & ba_in_5d).astype(float)


def gap_ext_075_gap_type_cluster_freq_63d(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """63-day frequency of gap-type cluster days (exhaustion-down + breakaway-down within 5d)."""
    cluster = gap_ext_074_gap_type_cluster_flag(close, open, high, low, volume)
    return _rolling_count_true(cluster > 0, _TD_QTR) / _TD_QTR


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_EXTENDED_REGISTRY_001_075 = {
    "gap_ext_001_exhaustion_down_mag_zscore_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_001_exhaustion_down_mag_zscore_252d},
    "gap_ext_002_breakaway_down_mag_zscore_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_002_breakaway_down_mag_zscore_252d},
    "gap_ext_003_runaway_down_mag_zscore_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_003_runaway_down_mag_zscore_252d},
    "gap_ext_004_common_gap_mag_zscore_252d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_004_common_gap_mag_zscore_252d},
    "gap_ext_005_exhaustion_down_mag_zscore_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_005_exhaustion_down_mag_zscore_63d},
    "gap_ext_006_exhaustion_down_fill_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_006_exhaustion_down_fill_21d},
    "gap_ext_007_breakaway_down_fill_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_007_breakaway_down_fill_21d},
    "gap_ext_008_runaway_fill_10d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_008_runaway_fill_10d},
    "gap_ext_009_exhaustion_any_fill_10d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_009_exhaustion_any_fill_10d},
    "gap_ext_010_common_gap_fill_5d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_010_common_gap_fill_5d},
    "gap_ext_011_exhaustion_down_vol_zscore_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_011_exhaustion_down_vol_zscore_63d},
    "gap_ext_012_runaway_vol_avg_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_012_runaway_vol_avg_63d},
    "gap_ext_013_common_gap_vol_avg_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_013_common_gap_vol_avg_63d},
    "gap_ext_014_exhaustion_down_vol_avg_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_014_exhaustion_down_vol_avg_252d},
    "gap_ext_015_breakaway_down_vol_avg_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_015_breakaway_down_vol_avg_252d},
    "gap_ext_016_days_since_breakaway_gap_any": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_016_days_since_breakaway_gap_any},
    "gap_ext_017_days_since_runaway_gap_any": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_017_days_since_runaway_gap_any},
    "gap_ext_018_days_since_common_gap": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_018_days_since_common_gap},
    "gap_ext_019_days_since_large_gap_down": {"inputs": ["close", "open"], "func": gap_ext_019_days_since_large_gap_down},
    "gap_ext_020_days_since_large_gap_up": {"inputs": ["close", "open"], "func": gap_ext_020_days_since_large_gap_up},
    "gap_ext_021_partial_fill_fraction_5d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_021_partial_fill_fraction_5d},
    "gap_ext_022_partial_fill_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_022_partial_fill_fraction_21d},
    "gap_ext_023_unfilled_down_gap_count_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_023_unfilled_down_gap_count_63d},
    "gap_ext_024_unfilled_up_gap_count_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_024_unfilled_up_gap_count_63d},
    "gap_ext_025_nearest_unfilled_down_gap_distance": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_025_nearest_unfilled_down_gap_distance},
    "gap_ext_026_nearest_unfilled_up_gap_distance": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_026_nearest_unfilled_up_gap_distance},
    "gap_ext_027_unfilled_down_gap_overhang_magnitude": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_027_unfilled_down_gap_overhang_magnitude},
    "gap_ext_028_gap_cumret_vs_total_cumret_126d": {"inputs": ["close", "open"], "func": gap_ext_028_gap_cumret_vs_total_cumret_126d},
    "gap_ext_029_gap_down_cumret_share_126d": {"inputs": ["close", "open"], "func": gap_ext_029_gap_down_cumret_share_126d},
    "gap_ext_030_gap_up_cumret_share_126d": {"inputs": ["close", "open"], "func": gap_ext_030_gap_up_cumret_share_126d},
    "gap_ext_031_gap_net_contribution_126d": {"inputs": ["close", "open"], "func": gap_ext_031_gap_net_contribution_126d},
    "gap_ext_032_gap_adjusted_return_21d": {"inputs": ["close", "open"], "func": gap_ext_032_gap_adjusted_return_21d},
    "gap_ext_033_gap_adjusted_return_63d": {"inputs": ["close", "open"], "func": gap_ext_033_gap_adjusted_return_63d},
    "gap_ext_034_gap_vs_raw_return_divergence_63d": {"inputs": ["close", "open"], "func": gap_ext_034_gap_vs_raw_return_divergence_63d},
    "gap_ext_035_consecutive_same_dir_gap_run": {"inputs": ["close", "open"], "func": gap_ext_035_consecutive_same_dir_gap_run},
    "gap_ext_036_max_down_gap_run_21d": {"inputs": ["close", "open"], "func": gap_ext_036_max_down_gap_run_21d},
    "gap_ext_037_max_up_gap_run_21d": {"inputs": ["close", "open"], "func": gap_ext_037_max_up_gap_run_21d},
    "gap_ext_038_gap_down_then_close_up_flag": {"inputs": ["close", "open"], "func": gap_ext_038_gap_down_then_close_up_flag},
    "gap_ext_039_gap_down_then_close_up_freq_21d": {"inputs": ["close", "open"], "func": gap_ext_039_gap_down_then_close_up_freq_21d},
    "gap_ext_040_gap_down_then_close_up_freq_63d": {"inputs": ["close", "open"], "func": gap_ext_040_gap_down_then_close_up_freq_63d},
    "gap_ext_041_gap_up_then_close_down_freq_63d": {"inputs": ["close", "open"], "func": gap_ext_041_gap_up_then_close_down_freq_63d},
    "gap_ext_042_gap_iqr_63d": {"inputs": ["close", "open"], "func": gap_ext_042_gap_iqr_63d},
    "gap_ext_043_gap_iqr_252d": {"inputs": ["close", "open"], "func": gap_ext_043_gap_iqr_252d},
    "gap_ext_044_gap_down_dispersion_ratio_63d": {"inputs": ["close", "open"], "func": gap_ext_044_gap_down_dispersion_ratio_63d},
    "gap_ext_045_gap_kurtosis_63d": {"inputs": ["close", "open"], "func": gap_ext_045_gap_kurtosis_63d},
    "gap_ext_046_gap_std_short_vs_long_ratio": {"inputs": ["close", "open"], "func": gap_ext_046_gap_std_short_vs_long_ratio},
    "gap_ext_047_gap_down_std_63d": {"inputs": ["close", "open"], "func": gap_ext_047_gap_down_std_63d},
    "gap_ext_048_gap_vs_prior_range_ratio": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_048_gap_vs_prior_range_ratio},
    "gap_ext_049_gap_vs_prior_range_ratio_21d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_049_gap_vs_prior_range_ratio_21d_avg},
    "gap_ext_050_gap_vs_prior_range_ratio_63d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_050_gap_vs_prior_range_ratio_63d_avg},
    "gap_ext_051_gap_exceeds_prior_range_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_051_gap_exceeds_prior_range_freq_63d},
    "gap_ext_052_gap_down_vs_prior_range_63d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_052_gap_down_vs_prior_range_63d_avg},
    "gap_ext_053_open_outside_prior_range_freq_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_ext_053_open_outside_prior_range_freq_63d},
    "gap_ext_054_overnight_ret_percentile_126d": {"inputs": ["close", "open"], "func": gap_ext_054_overnight_ret_percentile_126d},
    "gap_ext_055_gap_down_percentile_rank_252d": {"inputs": ["close", "open"], "func": gap_ext_055_gap_down_percentile_rank_252d},
    "gap_ext_056_overnight_ret_5pct_threshold_63d": {"inputs": ["close", "open"], "func": gap_ext_056_overnight_ret_5pct_threshold_63d},
    "gap_ext_057_overnight_ret_95pct_threshold_63d": {"inputs": ["close", "open"], "func": gap_ext_057_overnight_ret_95pct_threshold_63d},
    "gap_ext_058_overnight_ret_left_tail_mass_63d": {"inputs": ["close", "open"], "func": gap_ext_058_overnight_ret_left_tail_mass_63d},
    "gap_ext_059_overnight_ret_right_tail_mass_63d": {"inputs": ["close", "open"], "func": gap_ext_059_overnight_ret_right_tail_mass_63d},
    "gap_ext_060_overnight_ret_tail_asymmetry_63d": {"inputs": ["close", "open"], "func": gap_ext_060_overnight_ret_tail_asymmetry_63d},
    "gap_ext_061_down_gap_run_freq_3plus_63d": {"inputs": ["close", "open"], "func": gap_ext_061_down_gap_run_freq_3plus_63d},
    "gap_ext_062_up_gap_run_freq_3plus_63d": {"inputs": ["close", "open"], "func": gap_ext_062_up_gap_run_freq_3plus_63d},
    "gap_ext_063_avg_down_gap_run_length_63d": {"inputs": ["close", "open"], "func": gap_ext_063_avg_down_gap_run_length_63d},
    "gap_ext_064_down_gap_run_momentum_21d": {"inputs": ["close", "open"], "func": gap_ext_064_down_gap_run_momentum_21d},
    "gap_ext_065_gap_freq_roc_21d_to_63d": {"inputs": ["close", "open"], "func": gap_ext_065_gap_freq_roc_21d_to_63d},
    "gap_ext_066_gap_down_freq_roc_21d_to_63d": {"inputs": ["close", "open"], "func": gap_ext_066_gap_down_freq_roc_21d_to_63d},
    "gap_ext_067_gap_magnitude_roc_5d_to_21d": {"inputs": ["close", "open"], "func": gap_ext_067_gap_magnitude_roc_5d_to_21d},
    "gap_ext_068_gap_down_magnitude_acceleration_21d": {"inputs": ["close", "open"], "func": gap_ext_068_gap_down_magnitude_acceleration_21d},
    "gap_ext_069_gap_freq_acceleration_slope_63d": {"inputs": ["close", "open"], "func": gap_ext_069_gap_freq_acceleration_slope_63d},
    "gap_ext_070_gap_down_freq_acceleration_slope_63d": {"inputs": ["close", "open"], "func": gap_ext_070_gap_down_freq_acceleration_slope_63d},
    "gap_ext_071_exhaustion_down_count_126d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_071_exhaustion_down_count_126d},
    "gap_ext_072_breakaway_down_count_126d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_072_breakaway_down_count_126d},
    "gap_ext_073_gap_type_down_distress_score_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_073_gap_type_down_distress_score_63d},
    "gap_ext_074_gap_type_cluster_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_074_gap_type_cluster_flag},
    "gap_ext_075_gap_type_cluster_freq_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_ext_075_gap_type_cluster_freq_63d},
}
