"""
41_range_compression — Base Features 001-075
Domain: range compression/squeeze — true-range narrowing, contraction ratios, NR4/NR7
        consecutive narrow-range days, Bollinger/Keltner squeeze, coil tightness,
        compress-after-expand capitulation tells. Range CONTRACTION only.
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

# --- Group A (001-010): True-range level vs trailing baseline ---

def rcp_001_tr_ratio_to_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's true range divided by 21-day mean TR (below 1 = compression)."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_mean(tr, _TD_MON))


def rcp_002_tr_ratio_to_63d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's true range divided by 63-day mean TR."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_mean(tr, _TD_QTR))


def rcp_003_tr_ratio_to_252d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's true range divided by 252-day mean TR."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_mean(tr, _TD_YEAR))


def rcp_004_hl_ratio_to_21d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range divided by 21-day mean high-low range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, _TD_MON))


def rcp_005_hl_ratio_to_63d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range divided by 63-day mean high-low range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, _TD_QTR))


def rcp_006_hl_ratio_to_252d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's high-low range divided by 252-day mean high-low range."""
    rng = high - low
    return _safe_div(rng, _rolling_mean(rng, _TD_YEAR))


def rcp_007_tr_pct_close_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR/close ratio vs 21-day mean TR/close ratio."""
    tr = _tr(close, high, low)
    tr_pct = _safe_div(tr, close)
    return _safe_div(tr_pct, _rolling_mean(tr_pct, _TD_MON))


def rcp_008_tr_pct_close_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR/close ratio vs 63-day mean TR/close ratio."""
    tr = _tr(close, high, low)
    tr_pct = _safe_div(tr, close)
    return _safe_div(tr_pct, _rolling_mean(tr_pct, _TD_QTR))


def rcp_009_tr_below_median_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's TR is below the 21-day median TR."""
    tr = _tr(close, high, low)
    med = _rolling_median(tr, _TD_MON)
    return (tr < med).astype(float)


def rcp_010_tr_below_median_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's TR is below the 63-day median TR."""
    tr = _tr(close, high, low)
    med = _rolling_median(tr, _TD_QTR)
    return (tr < med).astype(float)


# --- Group B (011-020): TR z-score compression signals ---

def rcp_011_tr_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 21-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_MON)
    s = _rolling_std(tr, _TD_MON)
    return _safe_div(tr - m, s)


def rcp_012_tr_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 63-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_QTR)
    s = _rolling_std(tr, _TD_QTR)
    return _safe_div(tr - m, s)


def rcp_013_tr_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 252-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_YEAR)
    s = _rolling_std(tr, _TD_YEAR)
    return _safe_div(tr - m, s)


def rcp_014_hl_zscore_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's high-low range vs 21-day distribution."""
    rng = high - low
    m = _rolling_mean(rng, _TD_MON)
    s = _rolling_std(rng, _TD_MON)
    return _safe_div(rng - m, s)


def rcp_015_hl_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's high-low range vs 63-day distribution."""
    rng = high - low
    m = _rolling_mean(rng, _TD_QTR)
    s = _rolling_std(rng, _TD_QTR)
    return _safe_div(rng - m, s)


def rcp_016_tr_pct_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 21-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def rcp_017_tr_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 63-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rcp_018_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 252-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_019_tr_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's TR."""
    tr = _tr(close, high, low)
    return tr.expanding(min_periods=5).rank(pct=True)


def rcp_020_hl_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's high-low range within trailing 252-day distribution."""
    rng = high - low
    return rng.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


# --- Group C (021-030): NR4 / NR7 consecutive narrow-range day counts ---

def rcp_021_nr4_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is narrower than each of the prior 3 days (NR4)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    return (rng < prev_max).astype(float)


def rcp_022_nr7_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's range is the narrowest in the last 7 days (NR7)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    return (rng < prev_max).astype(float)


def rcp_023_consec_nr4_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-day streak of NR4 days."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    cond = rng < prev_max
    return _consec_streak(cond)


def rcp_024_consec_nr7_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of NR7 days (inside-range coil)."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    cond = rng < prev_max
    return _consec_streak(cond)


def rcp_025_nr4_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 days within trailing 21 days."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    cond = rng < prev_max
    return _rolling_count_true(cond, _TD_MON)


def rcp_026_nr7_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 days within trailing 63 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    cond = rng < prev_max
    return _rolling_count_true(cond, _TD_QTR)


def rcp_027_nr4_fraction_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were NR4 days."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    cond = rng < prev_max
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def rcp_028_nr7_fraction_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were NR7 days."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    cond = rng < prev_max
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def rcp_029_inside_day_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today is an inside day (high < prior high AND low > prior low)."""
    cond = (high < high.shift(1)) & (low > low.shift(1))
    return cond.astype(float)


def rcp_030_consec_inside_days(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of inside days."""
    cond = (high < high.shift(1)) & (low > low.shift(1))
    return _consec_streak(cond)


# --- Group D (031-040): TR trailing minimum and days-since-minimum ---

def rcp_031_tr_min_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 21-day minimum true range (lowest range in recent period)."""
    tr = _tr(close, high, low)
    return _rolling_min(tr, _TD_MON)


def rcp_032_tr_min_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 63-day minimum true range."""
    tr = _tr(close, high, low)
    return _rolling_min(tr, _TD_QTR)


def rcp_033_tr_min_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 252-day minimum true range."""
    tr = _tr(close, high, low)
    return _rolling_min(tr, _TD_YEAR)


def rcp_034_tr_at_21d_min_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR equals the 21-day trailing minimum (at the tightest point)."""
    tr = _tr(close, high, low)
    mn = _rolling_min(tr, _TD_MON)
    return (tr <= mn * (1 + _EPS)).astype(float)


def rcp_035_tr_at_63d_min_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR equals the 63-day trailing minimum."""
    tr = _tr(close, high, low)
    mn = _rolling_min(tr, _TD_QTR)
    return (tr <= mn * (1 + _EPS)).astype(float)


def rcp_036_tr_vs_21d_min_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 21-day minimum TR (1.0 = at minimum, higher = not compressed)."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_min(tr, _TD_MON))


def rcp_037_tr_vs_63d_min_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 63-day minimum TR."""
    tr = _tr(close, high, low)
    return _safe_div(tr, _rolling_min(tr, _TD_QTR))


def rcp_038_hl_min_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 21-day minimum of the daily high-low range."""
    rng = high - low
    return _rolling_min(rng, _TD_MON)


def rcp_039_hl_min_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 63-day minimum of the daily high-low range."""
    rng = high - low
    return _rolling_min(rng, _TD_QTR)


def rcp_040_days_since_tr_21d_min(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the last time TR equaled its 21-day minimum."""
    tr = _tr(close, high, low)
    mn = _rolling_min(tr, _TD_MON)
    at_min = (tr <= mn * (1 + _EPS)).astype(float)
    # days since last at-min: use cumsum gap trick
    group = at_min.cumsum()
    idx = pd.Series(range(len(tr)), index=tr.index, dtype=float)
    last_at_min_idx = idx.where(at_min == 1).groupby(group).transform("max")
    return (idx - last_at_min_idx).clip(lower=0)


# --- Group E (041-050): Bollinger Band width and squeeze signals ---

def rcp_041_bb_width_21d(close: pd.Series) -> pd.Series:
    """Bollinger Band width (2*std/mean) over 21-day window."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    return _safe_div(2.0 * s, m)


def rcp_042_bb_width_63d(close: pd.Series) -> pd.Series:
    """Bollinger Band width over 63-day window."""
    m = _rolling_mean(close, _TD_QTR)
    s = _rolling_std(close, _TD_QTR)
    return _safe_div(2.0 * s, m)


def rcp_043_bb_width_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """21-day Bollinger width divided by 252-day mean Bollinger width."""
    m21 = _rolling_mean(close, _TD_MON)
    s21 = _rolling_std(close, _TD_MON)
    bw21 = _safe_div(2.0 * s21, m21)
    return _safe_div(bw21, _rolling_mean(bw21, _TD_YEAR))


def rcp_044_bb_width_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day BB width within trailing 252-day distribution."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_045_bb_width_at_21d_min_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day BB width is at its lowest in the past 63 days (squeeze)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    mn63 = _rolling_min(bw, _TD_QTR)
    return (bw <= mn63 * (1 + _EPS)).astype(float)


def rcp_046_bb_squeeze_score_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """BB width minus Keltner Channel width — negative = squeeze (range < vol bands)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bb_width = _safe_div(2.0 * s, m)
    kc_width = _safe_div(2.0 * atr21, m)
    return bb_width - kc_width


def rcp_047_bb_squeeze_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: BB bands inside Keltner Channel (classic Bollinger squeeze)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bb_width = 2.0 * s
    kc_width = 2.0 * atr21
    return (bb_width < kc_width).astype(float)


def rcp_048_consec_bb_squeeze_days(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive day streak of Bollinger squeeze (BB inside KC)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    cond = 2.0 * s < 2.0 * atr21
    return _consec_streak(cond)


def rcp_049_bb_width_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 21-day BB width vs 252-day distribution of BB widths."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    mu = _rolling_mean(bw, _TD_YEAR)
    sigma = _rolling_std(bw, _TD_YEAR)
    return _safe_div(bw - mu, sigma)


def rcp_050_bb_width_ema_ratio(close: pd.Series) -> pd.Series:
    """21-day BB width divided by its 63-day EMA (fast vs slow Bollinger squeeze)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return _safe_div(bw, _ewm_mean(bw, _TD_QTR))


# --- Group F (051-060): Keltner Channel compression metrics ---

def rcp_051_keltner_width_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Keltner Channel width: 2*ATR21/mid normalized by midline."""
    tr = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    mid = _rolling_mean(close, _TD_MON)
    return _safe_div(2.0 * atr, mid)


def rcp_052_keltner_width_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Keltner Channel width using 63-day ATR and midline."""
    tr = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    mid = _rolling_mean(close, _TD_QTR)
    return _safe_div(2.0 * atr, mid)


def rcp_053_keltner_width_ratio_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day KC width vs 252-day mean KC width (relative compression)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mid21 = _rolling_mean(close, _TD_MON)
    kw21 = _safe_div(2.0 * atr21, mid21)
    return _safe_div(kw21, _rolling_mean(kw21, _TD_YEAR))


def rcp_054_keltner_width_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day KC width within trailing 252-day distribution."""
    tr = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    mid = _rolling_mean(close, _TD_MON)
    kw = _safe_div(2.0 * atr, mid)
    return kw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_055_atr21_vs_atr63_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR21 divided by ATR63 — below 1 signals recent range compression."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))


def rcp_056_atr21_vs_atr252_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR21 divided by ATR252 — below 1 signals short-term range compression."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))


def rcp_057_atr63_vs_atr252_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR63 divided by ATR252 — compression across medium term."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))


def rcp_058_atr21_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of ATR21 within trailing 252-day ATR21 distribution."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    return atr21.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_059_atr21_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR21 within trailing 252-day ATR21 distribution."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mu = _rolling_mean(atr21, _TD_YEAR)
    sigma = _rolling_std(atr21, _TD_YEAR)
    return _safe_div(atr21 - mu, sigma)


def rcp_060_atr21_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of ATR21."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    return atr21.expanding(min_periods=5).rank(pct=True)


# --- Group G (061-075): Consecutive narrowing range days and coil tightness ---

def rcp_061_consec_narrowing_tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current streak of days where TR < prior day TR (consecutive range narrowing)."""
    tr = _tr(close, high, low)
    cond = tr < tr.shift(1)
    return _consec_streak(cond)


def rcp_062_consec_narrowing_hl(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current streak of days where high-low range < prior day's high-low range."""
    rng = high - low
    cond = rng < rng.shift(1)
    return _consec_streak(cond)


def rcp_063_max_narrowing_tr_streak_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive narrowing-TR streak within trailing 21 days."""
    tr = _tr(close, high, low)
    cond = tr < tr.shift(1)
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def rcp_064_max_narrowing_tr_streak_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive narrowing-TR streak within trailing 63 days."""
    tr = _tr(close, high, low)
    cond = tr < tr.shift(1)
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def rcp_065_narrowing_tr_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days where TR was narrower than prior day."""
    tr = _tr(close, high, low)
    cond = tr < tr.shift(1)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def rcp_066_narrowing_tr_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days where TR was narrower than prior day."""
    tr = _tr(close, high, low)
    cond = tr < tr.shift(1)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def rcp_067_coil_tightness_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coil tightness: TR std / TR mean over 21 days (low = uniform tight range)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_MON), _rolling_mean(tr, _TD_MON))


def rcp_068_coil_tightness_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coil tightness: TR std / TR mean over 63 days."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR))


def rcp_069_inside_day_fraction_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were inside days."""
    cond = (high < high.shift(1)) & (low > low.shift(1))
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def rcp_070_inside_day_fraction_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were inside days."""
    cond = (high < high.shift(1)) & (low > low.shift(1))
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def rcp_071_tr_declining_vs_21d_mean_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: current TR is below 21-day mean AND below prior-day TR (double compression)."""
    tr = _tr(close, high, low)
    mean21 = _rolling_mean(tr, _TD_MON)
    cond = (tr < mean21) & (tr < tr.shift(1))
    return cond.astype(float)


def rcp_072_nr4_consec_and_bb_squeeze(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Combined score: NR4 streak * BB squeeze flag (coil + vol squeeze)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4_streak = _consec_streak(rng < prev_max)
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze_flag = (2.0 * s < 2.0 * atr21).astype(float)
    return nr4_streak * squeeze_flag


def rcp_073_close_range_within_21d_hl(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close price position within 21-day high-low channel (tightening = compression)."""
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    channel = h21 - l21
    return _safe_div(close - l21, channel)


def rcp_074_21d_hl_channel_width_ratio_to_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day high-low channel width as fraction of 252-day channel width."""
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _rolling_min(low, _TD_YEAR)
    w21 = h21 - l21
    w252 = h252 - l252
    return _safe_div(w21, w252)


def rcp_075_63d_hl_channel_width_ratio_to_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day high-low channel width as fraction of 252-day channel width."""
    h63 = _rolling_max(high, _TD_QTR)
    l63 = _rolling_min(low, _TD_QTR)
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _rolling_min(low, _TD_YEAR)
    w63 = h63 - l63
    w252 = h252 - l252
    return _safe_div(w63, w252)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_REGISTRY_001_075 = {
    "rcp_001_tr_ratio_to_21d_mean": {"inputs": ["close", "high", "low"], "func": rcp_001_tr_ratio_to_21d_mean},
    "rcp_002_tr_ratio_to_63d_mean": {"inputs": ["close", "high", "low"], "func": rcp_002_tr_ratio_to_63d_mean},
    "rcp_003_tr_ratio_to_252d_mean": {"inputs": ["close", "high", "low"], "func": rcp_003_tr_ratio_to_252d_mean},
    "rcp_004_hl_ratio_to_21d_mean": {"inputs": ["high", "low"], "func": rcp_004_hl_ratio_to_21d_mean},
    "rcp_005_hl_ratio_to_63d_mean": {"inputs": ["high", "low"], "func": rcp_005_hl_ratio_to_63d_mean},
    "rcp_006_hl_ratio_to_252d_mean": {"inputs": ["high", "low"], "func": rcp_006_hl_ratio_to_252d_mean},
    "rcp_007_tr_pct_close_ratio_21d": {"inputs": ["close", "high", "low"], "func": rcp_007_tr_pct_close_ratio_21d},
    "rcp_008_tr_pct_close_ratio_63d": {"inputs": ["close", "high", "low"], "func": rcp_008_tr_pct_close_ratio_63d},
    "rcp_009_tr_below_median_21d_flag": {"inputs": ["close", "high", "low"], "func": rcp_009_tr_below_median_21d_flag},
    "rcp_010_tr_below_median_63d_flag": {"inputs": ["close", "high", "low"], "func": rcp_010_tr_below_median_63d_flag},
    "rcp_011_tr_zscore_21d": {"inputs": ["close", "high", "low"], "func": rcp_011_tr_zscore_21d},
    "rcp_012_tr_zscore_63d": {"inputs": ["close", "high", "low"], "func": rcp_012_tr_zscore_63d},
    "rcp_013_tr_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_013_tr_zscore_252d},
    "rcp_014_hl_zscore_21d": {"inputs": ["high", "low"], "func": rcp_014_hl_zscore_21d},
    "rcp_015_hl_zscore_63d": {"inputs": ["high", "low"], "func": rcp_015_hl_zscore_63d},
    "rcp_016_tr_pct_rank_21d": {"inputs": ["close", "high", "low"], "func": rcp_016_tr_pct_rank_21d},
    "rcp_017_tr_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": rcp_017_tr_pct_rank_63d},
    "rcp_018_tr_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rcp_018_tr_pct_rank_252d},
    "rcp_019_tr_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": rcp_019_tr_expanding_pct_rank},
    "rcp_020_hl_pct_rank_252d": {"inputs": ["high", "low"], "func": rcp_020_hl_pct_rank_252d},
    "rcp_021_nr4_flag": {"inputs": ["high", "low"], "func": rcp_021_nr4_flag},
    "rcp_022_nr7_flag": {"inputs": ["high", "low"], "func": rcp_022_nr7_flag},
    "rcp_023_consec_nr4_streak": {"inputs": ["high", "low"], "func": rcp_023_consec_nr4_streak},
    "rcp_024_consec_nr7_streak": {"inputs": ["high", "low"], "func": rcp_024_consec_nr7_streak},
    "rcp_025_nr4_count_21d": {"inputs": ["high", "low"], "func": rcp_025_nr4_count_21d},
    "rcp_026_nr7_count_63d": {"inputs": ["high", "low"], "func": rcp_026_nr7_count_63d},
    "rcp_027_nr4_fraction_21d": {"inputs": ["high", "low"], "func": rcp_027_nr4_fraction_21d},
    "rcp_028_nr7_fraction_63d": {"inputs": ["high", "low"], "func": rcp_028_nr7_fraction_63d},
    "rcp_029_inside_day_flag": {"inputs": ["high", "low"], "func": rcp_029_inside_day_flag},
    "rcp_030_consec_inside_days": {"inputs": ["high", "low"], "func": rcp_030_consec_inside_days},
    "rcp_031_tr_min_21d": {"inputs": ["close", "high", "low"], "func": rcp_031_tr_min_21d},
    "rcp_032_tr_min_63d": {"inputs": ["close", "high", "low"], "func": rcp_032_tr_min_63d},
    "rcp_033_tr_min_252d": {"inputs": ["close", "high", "low"], "func": rcp_033_tr_min_252d},
    "rcp_034_tr_at_21d_min_flag": {"inputs": ["close", "high", "low"], "func": rcp_034_tr_at_21d_min_flag},
    "rcp_035_tr_at_63d_min_flag": {"inputs": ["close", "high", "low"], "func": rcp_035_tr_at_63d_min_flag},
    "rcp_036_tr_vs_21d_min_ratio": {"inputs": ["close", "high", "low"], "func": rcp_036_tr_vs_21d_min_ratio},
    "rcp_037_tr_vs_63d_min_ratio": {"inputs": ["close", "high", "low"], "func": rcp_037_tr_vs_63d_min_ratio},
    "rcp_038_hl_min_21d": {"inputs": ["high", "low"], "func": rcp_038_hl_min_21d},
    "rcp_039_hl_min_63d": {"inputs": ["high", "low"], "func": rcp_039_hl_min_63d},
    "rcp_040_days_since_tr_21d_min": {"inputs": ["close", "high", "low"], "func": rcp_040_days_since_tr_21d_min},
    "rcp_041_bb_width_21d": {"inputs": ["close"], "func": rcp_041_bb_width_21d},
    "rcp_042_bb_width_63d": {"inputs": ["close"], "func": rcp_042_bb_width_63d},
    "rcp_043_bb_width_21d_vs_252d_ratio": {"inputs": ["close"], "func": rcp_043_bb_width_21d_vs_252d_ratio},
    "rcp_044_bb_width_pct_rank_252d": {"inputs": ["close"], "func": rcp_044_bb_width_pct_rank_252d},
    "rcp_045_bb_width_at_21d_min_flag": {"inputs": ["close"], "func": rcp_045_bb_width_at_21d_min_flag},
    "rcp_046_bb_squeeze_score_21d": {"inputs": ["close", "high", "low"], "func": rcp_046_bb_squeeze_score_21d},
    "rcp_047_bb_squeeze_flag_21d": {"inputs": ["close", "high", "low"], "func": rcp_047_bb_squeeze_flag_21d},
    "rcp_048_consec_bb_squeeze_days": {"inputs": ["close", "high", "low"], "func": rcp_048_consec_bb_squeeze_days},
    "rcp_049_bb_width_zscore_252d": {"inputs": ["close"], "func": rcp_049_bb_width_zscore_252d},
    "rcp_050_bb_width_ema_ratio": {"inputs": ["close"], "func": rcp_050_bb_width_ema_ratio},
    "rcp_051_keltner_width_21d": {"inputs": ["close", "high", "low"], "func": rcp_051_keltner_width_21d},
    "rcp_052_keltner_width_63d": {"inputs": ["close", "high", "low"], "func": rcp_052_keltner_width_63d},
    "rcp_053_keltner_width_ratio_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": rcp_053_keltner_width_ratio_21d_vs_252d},
    "rcp_054_keltner_width_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rcp_054_keltner_width_pct_rank_252d},
    "rcp_055_atr21_vs_atr63_ratio": {"inputs": ["close", "high", "low"], "func": rcp_055_atr21_vs_atr63_ratio},
    "rcp_056_atr21_vs_atr252_ratio": {"inputs": ["close", "high", "low"], "func": rcp_056_atr21_vs_atr252_ratio},
    "rcp_057_atr63_vs_atr252_ratio": {"inputs": ["close", "high", "low"], "func": rcp_057_atr63_vs_atr252_ratio},
    "rcp_058_atr21_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rcp_058_atr21_pct_rank_252d},
    "rcp_059_atr21_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_059_atr21_zscore_252d},
    "rcp_060_atr21_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": rcp_060_atr21_expanding_pct_rank},
    "rcp_061_consec_narrowing_tr": {"inputs": ["close", "high", "low"], "func": rcp_061_consec_narrowing_tr},
    "rcp_062_consec_narrowing_hl": {"inputs": ["high", "low"], "func": rcp_062_consec_narrowing_hl},
    "rcp_063_max_narrowing_tr_streak_21d": {"inputs": ["close", "high", "low"], "func": rcp_063_max_narrowing_tr_streak_21d},
    "rcp_064_max_narrowing_tr_streak_63d": {"inputs": ["close", "high", "low"], "func": rcp_064_max_narrowing_tr_streak_63d},
    "rcp_065_narrowing_tr_fraction_21d": {"inputs": ["close", "high", "low"], "func": rcp_065_narrowing_tr_fraction_21d},
    "rcp_066_narrowing_tr_fraction_63d": {"inputs": ["close", "high", "low"], "func": rcp_066_narrowing_tr_fraction_63d},
    "rcp_067_coil_tightness_21d": {"inputs": ["close", "high", "low"], "func": rcp_067_coil_tightness_21d},
    "rcp_068_coil_tightness_63d": {"inputs": ["close", "high", "low"], "func": rcp_068_coil_tightness_63d},
    "rcp_069_inside_day_fraction_21d": {"inputs": ["high", "low"], "func": rcp_069_inside_day_fraction_21d},
    "rcp_070_inside_day_fraction_63d": {"inputs": ["high", "low"], "func": rcp_070_inside_day_fraction_63d},
    "rcp_071_tr_declining_vs_21d_mean_flag": {"inputs": ["close", "high", "low"], "func": rcp_071_tr_declining_vs_21d_mean_flag},
    "rcp_072_nr4_consec_and_bb_squeeze": {"inputs": ["close", "high", "low"], "func": rcp_072_nr4_consec_and_bb_squeeze},
    "rcp_073_close_range_within_21d_hl": {"inputs": ["close", "high", "low"], "func": rcp_073_close_range_within_21d_hl},
    "rcp_074_21d_hl_channel_width_ratio_to_252d": {"inputs": ["close", "high", "low"], "func": rcp_074_21d_hl_channel_width_ratio_to_252d},
    "rcp_075_63d_hl_channel_width_ratio_to_252d": {"inputs": ["close", "high", "low"], "func": rcp_075_63d_hl_channel_width_ratio_to_252d},
}
