"""
41_range_compression — Extended Features 001-075
Domain: range compression/squeeze — new windows, compression ratio variants, NR-bar
        counts on alternate lookbacks, range-percentile compression flags,
        expansion-to-compression transition counters, compression z-scores on
        alternate baselines, volume-weighted range, intraday tightness, Donchian
        contraction, log-range metrics, entropy-of-range, EWM ATR variants,
        open-range compression, and multi-signal capitulation composites.
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


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): New window TR ratio variants (10d, 126d, EWM) ---

def rcp_ext_001_tr_ratio_to_10d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 10-day mean TR (two-week compression ratio)."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_mean(tr, 10))


def rcp_ext_002_tr_ratio_to_126d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 126-day (half-year) mean TR."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_mean(tr, _TD_HALF))


def rcp_ext_003_hl_ratio_to_10d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range divided by 10-day mean high-low range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, 10))


def rcp_ext_004_hl_ratio_to_126d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range divided by 126-day mean high-low range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, _TD_HALF))


def rcp_ext_005_tr_ewm_ratio_span21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by its 21-period EWM mean (EWM-smoothed compression ratio)."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _ewm_mean(tr, _TD_MON))


def rcp_ext_006_tr_ewm_ratio_span63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by its 63-period EWM mean."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _ewm_mean(tr, _TD_QTR))


def rcp_ext_007_atr10_vs_atr63_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR10 divided by ATR63 — 2-week vs quarterly compression ratio."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_QTR))


def rcp_ext_008_atr10_vs_atr252_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR10 divided by ATR252 — 2-week vs annual compression ratio."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_YEAR))


def rcp_ext_009_atr126_vs_atr252_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR126 divided by ATR252 — half-year vs annual compression ratio."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_HALF), _rolling_mean(tr, _TD_YEAR))


def rcp_ext_010_tr_below_median_10d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's TR is below the 10-day median TR."""
    tr = _tr(close, high, low)
    return (tr < _rolling_median(tr, 10)).astype(float)


# --- Group B (011-020): NR-bar variants with alternate lookbacks ---

def rcp_ext_011_nr3_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is narrower than each of the prior 2 days (NR3)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2)], axis=1).max(axis=1)
    return (rng < prev_max).astype(float)


def rcp_ext_012_nr10_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is the narrowest in the last 10 days (NR10)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    return (rng < prev_max).astype(float)


def rcp_ext_013_nr14_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is the narrowest in the last 14 days (NR14)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(13, min_periods=6).max()
    return (rng < prev_max).astype(float)


def rcp_ext_014_nr21_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is the narrowest in the last 21 days (NR21)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(20, min_periods=10).max()
    return (rng < prev_max).astype(float)


def rcp_ext_015_consec_nr3_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-day streak of NR3 days."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2)], axis=1).max(axis=1)
    return _consec_streak(rng < prev_max)


def rcp_ext_016_consec_nr10_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of NR10 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    return _consec_streak(rng < prev_max)


def rcp_ext_017_nr4_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 days within trailing 63 days."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    return _rolling_count_true(rng < prev_max, _TD_QTR)


def rcp_ext_018_nr7_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 days within trailing 21 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    return _rolling_count_true(rng < prev_max, _TD_MON)


def rcp_ext_019_nr10_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR10 days within trailing 63 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(9, min_periods=4).max()
    return _rolling_count_true(rng < prev_max, _TD_QTR)


def rcp_ext_020_nr14_fraction_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were NR14 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(13, min_periods=6).max()
    return _rolling_count_true(rng < prev_max, _TD_QTR) / _TD_QTR


# --- Group C (021-030): TR percentile compression flags and counts ---

def rcp_ext_021_tr_below_10th_pct_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 10th percentile of trailing 63-day distribution."""
    tr = _tr(close, high, low)
    p10 = tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    return (tr <= p10).astype(float)


def rcp_ext_022_tr_below_25th_pct_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 25th percentile of trailing 63-day distribution."""
    tr = _tr(close, high, low)
    p25 = tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return (tr <= p25).astype(float)


def rcp_ext_023_tr_below_10th_pct_126d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 10th percentile of trailing 126-day distribution."""
    tr = _tr(close, high, low)
    p10 = tr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).quantile(0.10)
    return (tr <= p10).astype(float)


def rcp_ext_024_tr_below_5th_pct_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 5th percentile of trailing 252-day distribution."""
    tr = _tr(close, high, low)
    p5 = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    return (tr <= p5).astype(float)


def rcp_ext_025_tr_extreme_compression_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where TR was below 10th percentile of 252-day distribution."""
    tr = _tr(close, high, low)
    p10 = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    cond = tr <= p10
    return _rolling_count_true(cond, _TD_QTR)


def rcp_ext_026_hl_below_10th_pct_252d_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's HL range is in the bottom 10th percentile of trailing 252-day HL distribution."""
    rng = high - low
    p10 = rng.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (rng <= p10).astype(float)


def rcp_ext_027_hl_pct_rank_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 63-day HL distribution."""
    rng = high - low
    return rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rcp_ext_028_hl_pct_rank_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 126-day HL distribution."""
    rng = high - low
    return rng.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def rcp_ext_029_tr_consec_below_5pct_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days TR has been in the bottom 5th percentile of 252-day TR distribution."""
    tr = _tr(close, high, low)
    p5 = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    cond = tr <= p5
    return _consec_streak(cond)


def rcp_ext_030_tr_consec_below_25pct_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days TR has been in the bottom 25th percentile of 63-day TR distribution."""
    tr = _tr(close, high, low)
    p25 = tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    cond = tr <= p25
    return _consec_streak(cond)


# --- Group D (031-040): Expansion-to-compression transition counters ---

def rcp_ext_031_expand_to_compress_transition_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of expand-to-compress transitions in trailing 63 days (TR crosses below 21d mean from above)."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    was_above = tr.shift(1) >= mean21.shift(1)
    now_below = tr < mean21
    transition = (was_above & now_below).astype(float)
    return _rolling_sum(transition, _TD_QTR)


def rcp_ext_032_expand_to_compress_transition_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of expand-to-compress transitions in trailing 21 days."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    was_above = tr.shift(1) >= mean21.shift(1)
    now_below = tr < mean21
    transition = (was_above & now_below).astype(float)
    return _rolling_sum(transition, _TD_MON)


def rcp_ext_033_bb_squeeze_entry_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of BB squeeze entry events (BB enters KC from above) in trailing 63 days."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    in_squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    was_out = (in_squeeze.shift(1).fillna(0.0) == 0.0)
    entry = (was_out & (in_squeeze == 1.0)).astype(float)
    return _rolling_sum(entry, _TD_QTR)


def rcp_ext_034_atr21_crosses_below_atr63_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of times ATR21 crosses below ATR63 in trailing 63 days."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    was_above = atr21.shift(1) >= atr63.shift(1)
    now_below = atr21 < atr63
    cross = (was_above & now_below).astype(float)
    return _rolling_sum(cross, _TD_QTR)


def rcp_ext_035_days_since_last_bb_squeeze_entry(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the last BB squeeze entry event."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    in_squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    was_out = (in_squeeze.shift(1).fillna(0.0) == 0.0)
    entry = (was_out & (in_squeeze == 1.0)).astype(float)
    idx = pd.Series(range(len(entry)), index=entry.index, dtype=float)
    last_idx = idx.where(entry == 1).ffill().fillna(0.0)
    return (idx - last_idx).where(~in_squeeze.isna(), np.nan)


def rcp_ext_036_hl_channel_cross_below_50pct_252d_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of times 21d HL channel/252d HL channel ratio crosses below 0.5 in trailing 21d."""
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _rolling_min(low, _TD_YEAR)
    ratio = _safe_div(h21 - l21, h252 - l252)
    was_above = ratio.shift(1) >= 0.5
    now_below = ratio < 0.5
    cross = (was_above & now_below).astype(float)
    return _rolling_sum(cross, _TD_MON)


def rcp_ext_037_nr7_to_expansion_transition_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7-to-expansion transitions (NR7 day followed by wider-than-21d-mean) in 63d."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7 = rng < prev_max
    mean21 = _rolling_mean(rng, _TD_MON)
    was_nr7 = nr7.shift(1)
    now_expanded = rng > mean21
    transition = (was_nr7 & now_expanded).astype(float)
    return _rolling_sum(transition, _TD_QTR)


def rcp_ext_038_consec_compress_expand_cycles_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of complete compress-then-expand cycles in trailing 63 days."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    below = (tr < mean21).astype(int)
    transitions = below.diff().abs()
    return _rolling_sum(transitions.where(transitions > 0, 0), _TD_QTR) / 2.0


def rcp_ext_039_atr21_new_63d_low_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ATR21 just made a new 63-day low (fresh compression extreme)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mn63 = atr21.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (atr21 < mn63).astype(float)


def rcp_ext_040_atr21_new_252d_low_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ATR21 just made a new 252-day low (rare maximal compression)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mn252 = atr21.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (atr21 < mn252).astype(float)


# --- Group E (041-050): Compression z-scores on alternate baselines ---

def rcp_ext_041_tr_zscore_10d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 10-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, 10)
    s = _rolling_std(tr, 10)
    return _safe_div(tr - m, s)


def rcp_ext_042_tr_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 126-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_HALF)
    s = _rolling_std(tr, _TD_HALF)
    return _safe_div(tr - m, s)


def rcp_ext_043_atr10_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR10 within trailing 252-day ATR10 distribution."""
    tr = _tr(close, high, low)
    atr10 = _rolling_mean(tr, 10)
    mu = _rolling_mean(atr10, _TD_YEAR)
    sigma = _rolling_std(atr10, _TD_YEAR)
    return _safe_div(atr10 - mu, sigma)


def rcp_ext_044_atr126_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR126 within trailing 252-day ATR126 distribution."""
    tr = _tr(close, high, low)
    atr126 = _rolling_mean(tr, _TD_HALF)
    mu = _rolling_mean(atr126, _TD_YEAR)
    sigma = _rolling_std(atr126, _TD_YEAR)
    return _safe_div(atr126 - mu, sigma)


def rcp_ext_045_hl_zscore_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's HL range vs trailing 126-day distribution."""
    rng = high - low
    m = _rolling_mean(rng, _TD_HALF)
    s = _rolling_std(rng, _TD_HALF)
    return _safe_div(rng - m, s)


def rcp_ext_046_bb_width_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of current 21-day BB width vs trailing 63-day distribution of BB widths."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    mu = _rolling_mean(bw, _TD_QTR)
    sigma = _rolling_std(bw, _TD_QTR)
    return _safe_div(bw - mu, sigma)


def rcp_ext_047_bb_width_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day BB width vs 252-day distribution of 63-day BB widths."""
    m = _rolling_mean(close, _TD_QTR)
    s = _rolling_std(close, _TD_QTR)
    bw = _safe_div(2.0 * s, m)
    mu = _rolling_mean(bw, _TD_YEAR)
    sigma = _rolling_std(bw, _TD_YEAR)
    return _safe_div(bw - mu, sigma)


def rcp_ext_048_tr_ewm_zscore_span63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM z-score of today's TR using span-63 EWM mean and std."""
    tr = _tr(close, high, low)
    mu = _ewm_mean(tr, _TD_QTR)
    sigma = _ewm_std(tr, _TD_QTR)
    return _safe_div(tr - mu, sigma)


def rcp_ext_049_atr21_ewm_zscore_span126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM z-score of ATR21 using span-126 EWM mean and std."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mu = _ewm_mean(atr21, _TD_HALF)
    sigma = _ewm_std(atr21, _TD_HALF)
    return _safe_div(atr21 - mu, sigma)


def rcp_ext_050_hl_zscore_10d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's HL range vs trailing 10-day distribution."""
    rng = high - low
    m = _rolling_mean(rng, 10)
    s = _rolling_std(rng, 10)
    return _safe_div(rng - m, s)


# --- Group F (051-060): Volume-weighted range compression metrics ---

def rcp_ext_051_vwap_range_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """VWAP-normalized range: (H-L)/VWAP_21d as fraction of 252d mean (range vs price level)."""
    vwap21 = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    rng_pct = _safe_div(high - low, vwap21)
    return _safe_div(rng_pct, _rolling_mean(rng_pct, _TD_YEAR))


def rcp_ext_052_vol_weighted_tr_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted TR today vs volume-weighted ATR21 (high-vol days dominate baseline)."""
    tr = _tr(close, high, low)
    vwtr = _safe_div(_rolling_sum(tr * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _safe_div(tr, vwtr)


def rcp_ext_053_low_vol_days_fraction_narrow_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where TR < 21d median AND volume < 21d median (silent coil)."""
    tr = _tr(close, high, low)
    med_tr = _rolling_median(tr, _TD_MON)
    med_vol = _rolling_median(volume, _TD_MON)
    cond = (tr < med_tr) & (volume < med_vol)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def rcp_ext_054_vol_surge_before_squeeze_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of trailing 5d avg volume to 21d avg volume, when TR < 21d mean (capitulation setup)."""
    tr = _tr(close, high, low)
    avg_tr21 = _rolling_mean(tr, _TD_MON)
    avg_vol21 = _rolling_mean(volume, _TD_MON)
    avg_vol5 = _rolling_mean(volume, _TD_WEEK)
    vol_surge = _safe_div(avg_vol5, avg_vol21)
    compressed = (tr < avg_tr21).astype(float)
    return vol_surge * compressed


def rcp_ext_055_nr7_with_below_avg_vol_count_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of NR7 days with below-average volume in trailing 21 days (quiet coil frequency)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7 = rng < prev_max
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = nr7 & (volume < avg_vol)
    return _rolling_count_true(cond, _TD_MON)


def rcp_ext_056_vol_compression_ratio_5d_vs_63d(volume: pd.Series) -> pd.Series:
    """5-day mean volume divided by 63-day mean volume (volume drying up = coil)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


def rcp_ext_057_vol_std_compression_63d(volume: pd.Series) -> pd.Series:
    """5-day volume std divided by 63-day volume std (low ratio = volume clustering/quiet)."""
    return _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_std(volume, _TD_QTR))


def rcp_ext_058_price_range_per_unit_vol_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean of (H-L)/volume — range efficiency per unit of volume traded."""
    rng = high - low
    eff = _safe_div(rng, volume.replace(0, np.nan))
    return _rolling_mean(eff, _TD_MON)


def rcp_ext_059_vol_weighted_nr4_fraction_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted NR4 fraction: sum of volume on NR4 days / total volume in 21d."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = rng < prev_max
    vol_on_nr4 = volume.where(nr4, 0.0)
    return _safe_div(_rolling_sum(vol_on_nr4, _TD_MON), _rolling_sum(volume, _TD_MON))


def rcp_ext_060_quiet_squeeze_streak(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with TR below 21d mean AND volume below 63d mean (deep quiet coil)."""
    tr = _tr(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    cond = (tr < avg_tr) & (volume < avg_vol)
    return _consec_streak(cond)


# --- Group G (061-075): Log-range, open-range, Donchian, EWM BB, multi-signal composites ---

def rcp_ext_061_log_tr_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of log(TR) within trailing 252-day log(TR) distribution."""
    log_tr = _log_safe(_tr(close, high, low))
    mu = _rolling_mean(log_tr, _TD_YEAR)
    sigma = _rolling_std(log_tr, _TD_YEAR)
    return _safe_div(log_tr - mu, sigma)


def rcp_ext_062_log_tr_ratio_to_252d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(TR) minus 252-day mean of log(TR) (log-scale compression depth)."""
    log_tr = _log_safe(_tr(close, high, low))
    return log_tr - _rolling_mean(log_tr, _TD_YEAR)


def rcp_ext_063_log_hl_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of log(H-L) within trailing 63-day log(H-L) distribution."""
    log_rng = _log_safe(high - low)
    mu = _rolling_mean(log_rng, _TD_QTR)
    sigma = _rolling_std(log_rng, _TD_QTR)
    return _safe_div(log_rng - mu, sigma)


def rcp_ext_064_open_to_close_range_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of |open-close| within trailing 63-day distribution (body compression)."""
    body = (close - open).abs()
    mu = _rolling_mean(body, _TD_QTR)
    sigma = _rolling_std(body, _TD_QTR)
    return _safe_div(body - mu, sigma)


def rcp_ext_065_open_range_fraction_of_hl_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of |open-close|/HL within trailing 63-day distribution."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    mu = _rolling_mean(ratio, _TD_QTR)
    sigma = _rolling_std(ratio, _TD_QTR)
    return _safe_div(ratio - mu, sigma)


def rcp_ext_066_donchian_width_10d_vs_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day Donchian channel width divided by 63-day Donchian channel width."""
    w10 = _rolling_max(high, 10) - _rolling_min(low, 10)
    w63 = _rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)
    return _safe_div(w10, w63)


def rcp_ext_067_donchian_width_21d_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Donchian channel width within trailing 252-day distribution."""
    w21 = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    return w21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_ext_068_donchian_width_63d_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Donchian channel width within trailing 252-day distribution."""
    w63 = _rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)
    return w63.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_ext_069_ewm_bb_width_span21_vs_span63(close: pd.Series) -> pd.Series:
    """EWM BB width (span 21) divided by EWM BB width (span 63) (short vs long EWM squeeze)."""
    mu21 = _ewm_mean(close, _TD_MON)
    sd21 = _ewm_std(close, _TD_MON)
    bw21 = _safe_div(2.0 * sd21, mu21)
    mu63 = _ewm_mean(close, _TD_QTR)
    sd63 = _ewm_std(close, _TD_QTR)
    bw63 = _safe_div(2.0 * sd63, mu63)
    return _safe_div(bw21, bw63)


def rcp_ext_070_ewm_bb_squeeze_flag_span21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: EWM (span 21) BB width < EWM (span 21) KC width (EWM Bollinger squeeze)."""
    tr = _tr(close, high, low)
    atr_ewm = _ewm_mean(tr, _TD_MON)
    mu = _ewm_mean(close, _TD_MON)
    sd = _ewm_std(close, _TD_MON)
    return (2.0 * sd < 2.0 * atr_ewm).astype(float)


def rcp_ext_071_compression_depth_3signal_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: avg of TR/10d_min, ATR21/ATR252, BB_pct_rank_126d (lower = more compressed)."""
    tr = _tr(close, high, low)
    tr_vs_min = _safe_div(tr, _rolling_min(tr, 10))
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    bb_rank = bw.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)
    return (tr_vs_min + atr_ratio + bb_rank) / 3.0


def rcp_ext_072_capitulation_coil_index(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation coil index: ATR21/ATR252 * (1-vol_5d/vol_63d).clip(0,1) * nr7_flag."""
    tr = _tr(close, high, low)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    vol_ratio = (1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))).clip(lower=0, upper=1)
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7_flag = (rng < prev_max).astype(float)
    return atr_ratio * vol_ratio * nr7_flag


def rcp_ext_073_multi_window_compression_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Multi-window score: avg of TR/10d_mean, TR/21d_mean, TR/63d_mean, TR/252d_mean."""
    tr = _tr(close, high, low)
    r10 = _safe_div(tr, _rolling_mean(tr, 10))
    r21 = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    r63 = _safe_div(tr, _rolling_mean(tr, _TD_QTR))
    r252 = _safe_div(tr, _rolling_mean(tr, _TD_YEAR))
    return (r10 + r21 + r63 + r252) / 4.0


def rcp_ext_074_squeeze_intensity_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Squeeze intensity: fraction of 63d in BB squeeze * ATR21 pct_rank inversion (1-rank)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    squeeze_frac = _rolling_mean(squeeze, _TD_QTR)
    atr_rank = atr21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return squeeze_frac * (1.0 - atr_rank.fillna(0.5))


def rcp_ext_075_deep_coil_flag_4signals(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: all 4 signals active — ATR21<ATR63, BB squeeze, NR7, volume<21d avg."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bb_sq = (2.0 * s < 2.0 * atr21)
    atr_comp = (atr21 < atr63)
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7 = rng < prev_max
    avg_vol = _rolling_mean(volume, _TD_MON)
    low_vol = (volume < avg_vol)
    return (bb_sq & atr_comp & nr7 & low_vol).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_EXTENDED_REGISTRY_001_075 = {
    "rcp_ext_001_tr_ratio_to_10d_mean": {"inputs": ["close", "high", "low"], "func": rcp_ext_001_tr_ratio_to_10d_mean},
    "rcp_ext_002_tr_ratio_to_126d_mean": {"inputs": ["close", "high", "low"], "func": rcp_ext_002_tr_ratio_to_126d_mean},
    "rcp_ext_003_hl_ratio_to_10d_mean": {"inputs": ["high", "low"], "func": rcp_ext_003_hl_ratio_to_10d_mean},
    "rcp_ext_004_hl_ratio_to_126d_mean": {"inputs": ["high", "low"], "func": rcp_ext_004_hl_ratio_to_126d_mean},
    "rcp_ext_005_tr_ewm_ratio_span21": {"inputs": ["close", "high", "low"], "func": rcp_ext_005_tr_ewm_ratio_span21},
    "rcp_ext_006_tr_ewm_ratio_span63": {"inputs": ["close", "high", "low"], "func": rcp_ext_006_tr_ewm_ratio_span63},
    "rcp_ext_007_atr10_vs_atr63_ratio": {"inputs": ["close", "high", "low"], "func": rcp_ext_007_atr10_vs_atr63_ratio},
    "rcp_ext_008_atr10_vs_atr252_ratio": {"inputs": ["close", "high", "low"], "func": rcp_ext_008_atr10_vs_atr252_ratio},
    "rcp_ext_009_atr126_vs_atr252_ratio": {"inputs": ["close", "high", "low"], "func": rcp_ext_009_atr126_vs_atr252_ratio},
    "rcp_ext_010_tr_below_median_10d_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_010_tr_below_median_10d_flag},
    "rcp_ext_011_nr3_flag": {"inputs": ["high", "low"], "func": rcp_ext_011_nr3_flag},
    "rcp_ext_012_nr10_flag": {"inputs": ["high", "low"], "func": rcp_ext_012_nr10_flag},
    "rcp_ext_013_nr14_flag": {"inputs": ["high", "low"], "func": rcp_ext_013_nr14_flag},
    "rcp_ext_014_nr21_flag": {"inputs": ["high", "low"], "func": rcp_ext_014_nr21_flag},
    "rcp_ext_015_consec_nr3_streak": {"inputs": ["high", "low"], "func": rcp_ext_015_consec_nr3_streak},
    "rcp_ext_016_consec_nr10_streak": {"inputs": ["high", "low"], "func": rcp_ext_016_consec_nr10_streak},
    "rcp_ext_017_nr4_count_63d": {"inputs": ["high", "low"], "func": rcp_ext_017_nr4_count_63d},
    "rcp_ext_018_nr7_count_21d": {"inputs": ["high", "low"], "func": rcp_ext_018_nr7_count_21d},
    "rcp_ext_019_nr10_count_63d": {"inputs": ["high", "low"], "func": rcp_ext_019_nr10_count_63d},
    "rcp_ext_020_nr14_fraction_63d": {"inputs": ["high", "low"], "func": rcp_ext_020_nr14_fraction_63d},
    "rcp_ext_021_tr_below_10th_pct_63d_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_021_tr_below_10th_pct_63d_flag},
    "rcp_ext_022_tr_below_25th_pct_63d_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_022_tr_below_25th_pct_63d_flag},
    "rcp_ext_023_tr_below_10th_pct_126d_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_023_tr_below_10th_pct_126d_flag},
    "rcp_ext_024_tr_below_5th_pct_252d_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_024_tr_below_5th_pct_252d_flag},
    "rcp_ext_025_tr_extreme_compression_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_025_tr_extreme_compression_count_63d},
    "rcp_ext_026_hl_below_10th_pct_252d_flag": {"inputs": ["high", "low"], "func": rcp_ext_026_hl_below_10th_pct_252d_flag},
    "rcp_ext_027_hl_pct_rank_63d": {"inputs": ["high", "low"], "func": rcp_ext_027_hl_pct_rank_63d},
    "rcp_ext_028_hl_pct_rank_126d": {"inputs": ["high", "low"], "func": rcp_ext_028_hl_pct_rank_126d},
    "rcp_ext_029_tr_consec_below_5pct_252d": {"inputs": ["close", "high", "low"], "func": rcp_ext_029_tr_consec_below_5pct_252d},
    "rcp_ext_030_tr_consec_below_25pct_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_030_tr_consec_below_25pct_63d},
    "rcp_ext_031_expand_to_compress_transition_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_031_expand_to_compress_transition_count_63d},
    "rcp_ext_032_expand_to_compress_transition_count_21d": {"inputs": ["close", "high", "low"], "func": rcp_ext_032_expand_to_compress_transition_count_21d},
    "rcp_ext_033_bb_squeeze_entry_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_033_bb_squeeze_entry_count_63d},
    "rcp_ext_034_atr21_crosses_below_atr63_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_034_atr21_crosses_below_atr63_count_63d},
    "rcp_ext_035_days_since_last_bb_squeeze_entry": {"inputs": ["close", "high", "low"], "func": rcp_ext_035_days_since_last_bb_squeeze_entry},
    "rcp_ext_036_hl_channel_cross_below_50pct_252d_count_21d": {"inputs": ["close", "high", "low"], "func": rcp_ext_036_hl_channel_cross_below_50pct_252d_count_21d},
    "rcp_ext_037_nr7_to_expansion_transition_count_63d": {"inputs": ["high", "low"], "func": rcp_ext_037_nr7_to_expansion_transition_count_63d},
    "rcp_ext_038_consec_compress_expand_cycles_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_038_consec_compress_expand_cycles_63d},
    "rcp_ext_039_atr21_new_63d_low_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_039_atr21_new_63d_low_flag},
    "rcp_ext_040_atr21_new_252d_low_flag": {"inputs": ["close", "high", "low"], "func": rcp_ext_040_atr21_new_252d_low_flag},
    "rcp_ext_041_tr_zscore_10d": {"inputs": ["close", "high", "low"], "func": rcp_ext_041_tr_zscore_10d},
    "rcp_ext_042_tr_zscore_126d": {"inputs": ["close", "high", "low"], "func": rcp_ext_042_tr_zscore_126d},
    "rcp_ext_043_atr10_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_ext_043_atr10_zscore_252d},
    "rcp_ext_044_atr126_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_ext_044_atr126_zscore_252d},
    "rcp_ext_045_hl_zscore_126d": {"inputs": ["high", "low"], "func": rcp_ext_045_hl_zscore_126d},
    "rcp_ext_046_bb_width_zscore_63d": {"inputs": ["close"], "func": rcp_ext_046_bb_width_zscore_63d},
    "rcp_ext_047_bb_width_63d_zscore_252d": {"inputs": ["close"], "func": rcp_ext_047_bb_width_63d_zscore_252d},
    "rcp_ext_048_tr_ewm_zscore_span63": {"inputs": ["close", "high", "low"], "func": rcp_ext_048_tr_ewm_zscore_span63},
    "rcp_ext_049_atr21_ewm_zscore_span126": {"inputs": ["close", "high", "low"], "func": rcp_ext_049_atr21_ewm_zscore_span126},
    "rcp_ext_050_hl_zscore_10d": {"inputs": ["high", "low"], "func": rcp_ext_050_hl_zscore_10d},
    "rcp_ext_051_vwap_range_ratio_21d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_051_vwap_range_ratio_21d},
    "rcp_ext_052_vol_weighted_tr_ratio_21d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_052_vol_weighted_tr_ratio_21d},
    "rcp_ext_053_low_vol_days_fraction_narrow_21d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_053_low_vol_days_fraction_narrow_21d},
    "rcp_ext_054_vol_surge_before_squeeze_score": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_054_vol_surge_before_squeeze_score},
    "rcp_ext_055_nr7_with_below_avg_vol_count_21d": {"inputs": ["high", "low", "volume"], "func": rcp_ext_055_nr7_with_below_avg_vol_count_21d},
    "rcp_ext_056_vol_compression_ratio_5d_vs_63d": {"inputs": ["volume"], "func": rcp_ext_056_vol_compression_ratio_5d_vs_63d},
    "rcp_ext_057_vol_std_compression_63d": {"inputs": ["volume"], "func": rcp_ext_057_vol_std_compression_63d},
    "rcp_ext_058_price_range_per_unit_vol_21d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_058_price_range_per_unit_vol_21d},
    "rcp_ext_059_vol_weighted_nr4_fraction_21d": {"inputs": ["high", "low", "volume"], "func": rcp_ext_059_vol_weighted_nr4_fraction_21d},
    "rcp_ext_060_quiet_squeeze_streak": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_060_quiet_squeeze_streak},
    "rcp_ext_061_log_tr_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_ext_061_log_tr_zscore_252d},
    "rcp_ext_062_log_tr_ratio_to_252d_mean": {"inputs": ["close", "high", "low"], "func": rcp_ext_062_log_tr_ratio_to_252d_mean},
    "rcp_ext_063_log_hl_zscore_63d": {"inputs": ["high", "low"], "func": rcp_ext_063_log_hl_zscore_63d},
    "rcp_ext_064_open_to_close_range_zscore_63d": {"inputs": ["close", "open"], "func": rcp_ext_064_open_to_close_range_zscore_63d},
    "rcp_ext_065_open_range_fraction_of_hl_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": rcp_ext_065_open_range_fraction_of_hl_zscore_63d},
    "rcp_ext_066_donchian_width_10d_vs_63d": {"inputs": ["high", "low"], "func": rcp_ext_066_donchian_width_10d_vs_63d},
    "rcp_ext_067_donchian_width_21d_pct_rank_252d": {"inputs": ["high", "low"], "func": rcp_ext_067_donchian_width_21d_pct_rank_252d},
    "rcp_ext_068_donchian_width_63d_pct_rank_252d": {"inputs": ["high", "low"], "func": rcp_ext_068_donchian_width_63d_pct_rank_252d},
    "rcp_ext_069_ewm_bb_width_span21_vs_span63": {"inputs": ["close"], "func": rcp_ext_069_ewm_bb_width_span21_vs_span63},
    "rcp_ext_070_ewm_bb_squeeze_flag_span21": {"inputs": ["close", "high", "low"], "func": rcp_ext_070_ewm_bb_squeeze_flag_span21},
    "rcp_ext_071_compression_depth_3signal_composite": {"inputs": ["close", "high", "low"], "func": rcp_ext_071_compression_depth_3signal_composite},
    "rcp_ext_072_capitulation_coil_index": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_072_capitulation_coil_index},
    "rcp_ext_073_multi_window_compression_score": {"inputs": ["close", "high", "low"], "func": rcp_ext_073_multi_window_compression_score},
    "rcp_ext_074_squeeze_intensity_score_63d": {"inputs": ["close", "high", "low"], "func": rcp_ext_074_squeeze_intensity_score_63d},
    "rcp_ext_075_deep_coil_flag_4signals": {"inputs": ["close", "high", "low", "volume"], "func": rcp_ext_075_deep_coil_flag_4signals},
}
