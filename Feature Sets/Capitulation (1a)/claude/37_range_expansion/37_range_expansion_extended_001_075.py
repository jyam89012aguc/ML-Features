"""
37_range_expansion — Extended Features 001-075
Domain: true-range expansion near the low — deeper NR/WR variants (NR21, WR21,
        larger lookbacks, NR-then-WR breakout sequences, days-since, streaks,
        percentile ranks); range-expansion thrust bars and 2-bar/3-bar sequences;
        expansion in ATR units and as z-score; expansion in down vs up moves;
        gap-adjusted true range; high-low vs close-to-close range divergence;
        range expansion at/near new lows; opening-range expansion; range-of-ranges;
        volume-confirmed expansion; and rate-of-change & acceleration of expansion.
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prevC|, |L-prevC|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c     = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _days_since(cond: pd.Series) -> pd.Series:
    """Number of bars since the last True in cond (0 = today is True)."""
    out  = pd.Series(np.nan, index=cond.index, dtype=float)
    last = -1
    for i, v in enumerate(cond):
        if v:
            last = i
        if last >= 0:
            out.iloc[i] = i - last
    return out


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Deeper NR/WR lookbacks — NR21, WR21, NR14, WR14 ---

def rex_ext_001_nr14_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR14 flag: today's H-L range is the narrowest of the last 14 bars."""
    hl    = high - low
    min14 = hl.rolling(14, min_periods=7).min()
    return (hl <= min14).astype(float)


def rex_ext_002_wr14_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR14 flag: today's H-L range is the widest of the last 14 bars."""
    hl    = high - low
    max14 = hl.rolling(14, min_periods=7).max()
    return (hl >= max14).astype(float)


def rex_ext_003_nr21_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR21 flag: today's H-L range is the narrowest of the last 21 bars."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    return (hl <= min21).astype(float)


def rex_ext_004_wr21_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR21 flag: today's H-L range is the widest of the last 21 bars."""
    hl    = high - low
    max21 = hl.rolling(21, min_periods=11).max()
    return (hl >= max21).astype(float)


def rex_ext_005_nr21_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR21 days in the trailing 63-day window."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    flag  = (hl <= min21).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_006_wr21_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR21 days in the trailing 63-day window."""
    hl    = high - low
    max21 = hl.rolling(21, min_periods=11).max()
    flag  = (hl >= max21).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_007_days_since_nr21(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars since the most recent NR21 day (0 = today is NR21)."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    flag  = (hl <= min21)
    return _days_since(flag)


def rex_ext_008_days_since_wr21(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars since the most recent WR21 day (0 = today is WR21)."""
    hl    = high - low
    max21 = hl.rolling(21, min_periods=11).max()
    flag  = (hl >= max21)
    return _days_since(flag)


def rex_ext_009_nr21_consec_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive NR21 streak length (sustained deep contraction)."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    flag  = (hl <= min21)
    return _consec_streak(flag)


def rex_ext_010_nr21_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's H-L within 252-day window (how narrow relative to history)."""
    hl = high - low
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-018): NR-then-WR breakout sequences ---

def rex_ext_011_nr4_then_wr7_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: yesterday was NR4 AND today is WR7 (deep squeeze -> wide expansion)."""
    hl    = high - low
    min4  = hl.rolling(4, min_periods=2).min()
    max7  = hl.rolling(7, min_periods=4).max()
    was_nr4  = hl.shift(1) <= min4.shift(1)
    is_wr7   = hl >= max7
    return (was_nr4 & is_wr7).astype(float)


def rex_ext_012_nr7_then_wr7_within_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: at least one NR7 in last 5 bars AND today is WR7."""
    hl    = high - low
    min7  = hl.rolling(7, min_periods=4).min()
    max7  = hl.rolling(7, min_periods=4).max()
    was_nr7_5d = _rolling_count_true((hl <= min7), _TD_WEEK).shift(1) >= 1
    is_wr7     = hl >= max7
    return (was_nr7_5d & is_wr7).astype(float)


def rex_ext_013_nr7_then_wr7_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7->WR7 breakout events (NR7 followed immediately by WR7) in last 63 days."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    max7 = hl.rolling(7, min_periods=4).max()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    is_wr7  = (hl >= max7)
    flag    = (was_nr7 & is_wr7).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_014_days_since_nr_wr_breakout(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last NR7->WR7 breakout (0 = today is NR7->WR7 breakout)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    max7 = hl.rolling(7, min_periods=4).max()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    is_wr7  = (hl >= max7)
    flag    = was_nr7 & is_wr7
    return _days_since(flag)


def rex_ext_015_nr21_then_expansion_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: yesterday was NR21 AND today's range > 1.5x yesterday's range."""
    hl      = high - low
    min21   = hl.rolling(21, min_periods=11).min()
    was_nr21 = hl.shift(1) <= min21.shift(1)
    expanded = hl >= 1.5 * hl.shift(1)
    return (was_nr21 & expanded).astype(float)


def rex_ext_016_nr14_then_wr14_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: yesterday was NR14 AND today is WR14 (14-bar contraction-to-expansion)."""
    hl    = high - low
    min14 = hl.rolling(14, min_periods=7).min()
    max14 = hl.rolling(14, min_periods=7).max()
    was_nr14 = hl.shift(1) <= min14.shift(1)
    is_wr14  = hl >= max14
    return (was_nr14 & is_wr14).astype(float)


def rex_ext_017_nr_wr_breakout_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7->WR7 breakout events in trailing 252 days."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    max7 = hl.rolling(7, min_periods=4).max()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    is_wr7  = (hl >= max7)
    flag    = (was_nr7 & is_wr7).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def rex_ext_018_wr4_after_nr7_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of today's H-L to the prior NR7 H-L when today is WR4 (expansion magnitude)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    max4 = hl.rolling(4, min_periods=2).max()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    is_wr4  = (hl >= max4)
    nr7_hl  = hl.shift(1).where(was_nr7, np.nan).ffill()
    result  = _safe_div(hl, nr7_hl)
    return result.where(is_wr4, np.nan)


# --- Group C (019-026): Thrust bars and multi-bar range-expansion sequences ---

def rex_ext_019_thrust_bar_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Thrust bar: TR > 1.5x ATR21 AND close in upper 25% of today's range (bullish thrust)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    hl   = (high - low).replace(0, np.nan)
    pos  = (close - low) / hl
    return ((tr > 1.5 * atr) & (pos >= 0.75)).astype(float)


def rex_ext_020_bearish_thrust_bar_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish thrust bar: TR > 1.5x ATR21 AND close in lower 25% of today's range."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    hl   = (high - low).replace(0, np.nan)
    pos  = (close - low) / hl
    return ((tr > 1.5 * atr) & (pos <= 0.25)).astype(float)


def rex_ext_021_two_bar_range_expansion_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: both today and yesterday have TR > ATR21 (2-bar expansion sequence)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    exp  = tr > atr
    return (exp & exp.shift(1)).astype(float)


def rex_ext_022_three_bar_range_expansion_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today, yesterday, and 2 days ago all have TR > ATR21 (3-bar expansion run)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    exp  = tr > atr
    return (exp & exp.shift(1) & exp.shift(2)).astype(float)


def rex_ext_023_two_bar_sequence_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 2-bar TR expansion sequences starting in last 21 days."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    flag = ((tr > atr) & (tr.shift(1) > atr.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_ext_024_three_bar_sequence_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 3-bar TR expansion sequences in last 63 days."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    exp  = tr > atr
    flag = (exp & exp.shift(1) & exp.shift(2)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_025_bearish_thrust_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bearish thrust bars in last 21 days."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    hl   = (high - low).replace(0, np.nan)
    pos  = (close - low) / hl
    flag = ((tr > 1.5 * atr) & (pos <= 0.25)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_ext_026_bearish_thrust_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bearish thrust bars in last 63 days."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    hl   = (high - low).replace(0, np.nan)
    pos  = (close - low) / hl
    flag = ((tr > 1.5 * atr) & (pos <= 0.25)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


# --- Group D (027-034): Expansion in ATR units and as z-score (new angles) ---

def rex_ext_027_tr_minus_atr21_in_atr_units(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Excess of TR above ATR21, expressed in ATR21 units (how many ATRs above baseline)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(tr - atr, atr)


def rex_ext_028_tr_excess_above_atr63_in_atr_units(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Excess of TR above ATR63, expressed in ATR63 units."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return _safe_div(tr - atr, atr).clip(lower=0)


def rex_ext_029_hl_zscore_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range relative to 126-day distribution (semi-annual context)."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_HALF)
    s  = _rolling_std(hl, _TD_HALF)
    return _safe_div(hl - m, s)


def rex_ext_030_tr_zscore_ewm21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TR using EWM mean and std with span=21 (EWM-based standardization)."""
    tr = _tr(close, high, low)
    m  = _ewm_mean(tr, _TD_MON)
    s  = tr.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    return _safe_div(tr - m, s)


def rex_ext_031_tr_above_3x_atr63_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: TR > 3x 63-day ATR (extreme expansion vs medium baseline)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return (tr > 3 * atr).astype(float)


def rex_ext_032_tr_above_2x_atr63_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TR > 2x ATR63 events in trailing 21 days."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return _rolling_count_true(tr > 2 * atr, _TD_MON)


def rex_ext_033_tr_above_1_5x_atr21_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TR > 1.5x ATR21 events in trailing 63 days (moderate spikes)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > 1.5 * atr, _TD_QTR)


def rex_ext_034_tr_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 126-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


# --- Group E (035-042): Down-move vs up-move range decomposition ---

def rex_ext_035_down_range_vs_tr_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of TR attributed to downside: (prevClose - low) / TR when down, else 0."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_comp = (prev_c - low).clip(lower=0)
    return _safe_div(down_comp, tr)


def rex_ext_036_up_range_vs_tr_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of TR attributed to upside: (high - prevClose) / TR when up, else 0."""
    prev_c  = close.shift(1)
    tr      = _tr(close, high, low)
    up_comp = (high - prev_c).clip(lower=0)
    return _safe_div(up_comp, tr)


def rex_ext_037_down_range_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average fraction of TR from downside component."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_comp = _safe_div((prev_c - low).clip(lower=0), tr)
    return _rolling_mean(down_comp, _TD_MON)


def rex_ext_038_down_vs_up_range_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day avg down-component to 21-day avg up-component of TR."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_frac = _safe_div((prev_c - low).clip(lower=0), tr)
    up_frac   = _safe_div((high - prev_c).clip(lower=0), tr)
    d_avg = _rolling_mean(down_frac, _TD_MON)
    u_avg = _rolling_mean(up_frac,   _TD_MON)
    return _safe_div(d_avg, u_avg)


def rex_ext_039_bearish_expansion_down_component_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (prevClose - low) relative to 63-day distribution (downside range extremity)."""
    prev_c    = close.shift(1)
    down_comp = (prev_c - low).clip(lower=0)
    m = _rolling_mean(down_comp, _TD_QTR)
    s = _rolling_std(down_comp, _TD_QTR)
    return _safe_div(down_comp - m, s)


def rex_ext_040_close_in_lower_half_expansion_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 21 days: TR > ATR21 AND close below midpoint of bar (bearish expansion)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    mid  = (high + low) / 2.0
    flag = ((tr > atr) & (close < mid)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_ext_041_close_in_lower_half_expansion_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 63 days: TR > ATR21 AND close below midpoint of bar."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    mid  = (high + low) / 2.0
    flag = ((tr > atr) & (close < mid)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_042_down_expansion_consec(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days of TR > ATR21 AND close below midpoint (bearish expansion streak)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    mid  = (high + low) / 2.0
    cond = (tr > atr) & (close < mid)
    return _consec_streak(cond)


# --- Group F (043-050): Gap-adjusted true range ---

def rex_ext_043_gap_adjusted_tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gap-adjusted TR: only the intraday H-L component (TR minus pure overnight gap size)."""
    hl     = high - low
    prev_c = close.shift(1)
    gap    = (high.clip(lower=prev_c) - low.clip(upper=prev_c)).clip(lower=0)
    return hl + gap


def rex_ext_044_overnight_gap_size(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute overnight gap: |open - prevClose| (pure gap contribution)."""
    return (open - close.shift(1)).abs()


def rex_ext_045_overnight_gap_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight gap size as ratio to 21-day ATR."""
    gap = (open - close.shift(1)).abs()
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(gap, atr)


def rex_ext_046_gap_adjusted_tr_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """H-L / ATR21 (intraday component only, normalized); different from TR/ATR21 by gap exclusion."""
    hl  = high - low
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(hl, atr)


def rex_ext_047_gap_adjusted_tr_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range (gap-adjusted intraday) relative to 63-day distribution."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_QTR)
    s  = _rolling_std(hl, _TD_QTR)
    return _safe_div(hl - m, s)


def rex_ext_048_gap_down_magnitude_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of downward gap: (prevClose - open) when open < prevClose, else 0."""
    prev_c  = close.shift(1)
    gap_dn  = (prev_c - open).clip(lower=0)
    return _rolling_mean(gap_dn, _TD_MON)


def rex_ext_049_gap_down_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days in last 21 where stock gapped down AND TR > ATR21."""
    prev_c  = close.shift(1)
    tr      = _tr(close, high, low)
    atr     = _rolling_mean(tr, _TD_MON)
    gap_dn  = open < prev_c
    flag    = (gap_dn & (tr > atr)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_ext_050_gap_down_expansion_zscore(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of gap-down magnitude relative to 63-day distribution."""
    prev_c = close.shift(1)
    gap_dn = (prev_c - open).clip(lower=0)
    m      = _rolling_mean(gap_dn, _TD_QTR)
    s      = _rolling_std(gap_dn, _TD_QTR)
    return _safe_div(gap_dn - m, s)


# --- Group G (051-058): HL vs close-to-close range divergence ---

def rex_ext_051_hl_vs_cc_range_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of H-L range to |close - prevClose| (intraday vs overnight price movement)."""
    hl = high - low
    cc = (close - close.shift(1)).abs()
    return _safe_div(hl, cc.replace(0, np.nan))


def rex_ext_052_hl_vs_cc_divergence_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (H-L - |close-prevClose|) normalized by ATR21 (sustained divergence)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs()
    diff = hl - cc
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    return _safe_div(_rolling_mean(diff, _TD_MON), atr)


def rex_ext_053_cc_range_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of close-to-close absolute change relative to 21-day distribution."""
    cc = (close - close.shift(1)).abs()
    m  = _rolling_mean(cc, _TD_MON)
    s  = _rolling_std(cc, _TD_MON)
    return _safe_div(cc - m, s)


def rex_ext_054_cc_range_vs_atr21_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-to-close range as ratio to ATR21 (how much of ATR is realized close-to-close)."""
    cc  = (close - close.shift(1)).abs()
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(cc, atr)


def rex_ext_055_hl_cc_divergence_expanding_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 63 days where H-L > 1.5x |close-prevClose| (intraday-dominated expansion)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs().replace(0, np.nan)
    flag = (hl > 1.5 * cc).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_ext_056_cc_range_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of |close-prevClose| within trailing 252-day distribution."""
    cc = (close - close.shift(1)).abs()
    return cc.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_ext_057_hl_minus_cc_21d_avg_in_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average of (H-L minus |C-pC|) in ATR21 units (persistent intraday excess)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs()
    diff = (hl - cc).clip(lower=0)
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    return _safe_div(_rolling_mean(diff, _TD_MON), atr)


def rex_ext_058_cc_range_expansion_consec(close: pd.Series) -> pd.Series:
    """Consecutive days where |close-prevClose| exceeds its own 21-day average."""
    cc  = (close - close.shift(1)).abs()
    avg = _rolling_mean(cc, _TD_MON)
    return _consec_streak(cc > avg)


# --- Group H (059-063): Range expansion at/near new lows ---

def rex_ext_059_expansion_at_52wk_low_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today is a 252-day closing low AND TR > ATR21 (new-annual-low on big range)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo   = _rolling_min(close, _TD_YEAR)
    at_lo = close <= lo
    return (at_lo & (tr > atr)).astype(float)


def rex_ext_060_expansion_near_low10pct_21d_atr2x(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 21 days: TR > 2x ATR21 AND close in lowest 10% of 252-day range."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    lo  = _rolling_min(close, _TD_YEAR)
    hi  = _rolling_max(close, _TD_YEAR)
    rng = (hi - lo).replace(0, np.nan)
    pos = (close - lo) / rng
    return _rolling_count_true((tr > 2 * atr) & (pos <= 0.10), _TD_MON)


def rex_ext_061_range_at_new_low_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Score: TR/ATR21 * (1 - close-position in 63d range), floored at 0 (distress composite)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = ((close - lo63) / rng).clip(0, 1)
    return ratio * (1 - pos)


def rex_ext_062_expansion_at_new_low_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 252 days where close was at 252-day low AND TR > ATR21."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo   = _rolling_min(close, _TD_YEAR)
    flag = ((close <= lo) & (tr > atr)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def rex_ext_063_days_since_expansion_at_new_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last event where close was at 252-day low AND TR > ATR21."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo   = _rolling_min(close, _TD_YEAR)
    flag = (close <= lo) & (tr > atr)
    return _days_since(flag)


# --- Group I (064-068): Opening-range expansion ---

def rex_ext_064_open_to_high_range_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """(High - Open) as ratio to ATR21 (upside opening-range expansion)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div((high - open).clip(lower=0), atr)


def rex_ext_065_open_to_low_range_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """(Open - Low) as ratio to ATR21 (downside opening-range expansion)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div((open - low).clip(lower=0), atr)


def rex_ext_066_opening_range_expansion_down_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: (Open - Low) > 0.5x ATR21 AND close < open (bearish opening-range expansion)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    down = (open - low) > 0.5 * atr
    bear = close < open
    return (down & bear).astype(float)


def rex_ext_067_open_to_low_range_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of (Open - Low) normalized by ATR21 (persistent downside opening range)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    r   = _safe_div((open - low).clip(lower=0), atr)
    return _rolling_mean(r, _TD_MON)


def rex_ext_068_opening_down_expansion_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Count of last 63 days: (Open-Low) > 0.5x ATR21 AND close < open."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    down = (open - low) > 0.5 * atr
    bear = close < open
    return _rolling_count_true(down & bear, _TD_QTR)


# --- Group J (069-072): Range-of-ranges ---

def rex_ext_069_range_of_ranges_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 21-day max TR minus rolling 21-day min TR (spread of range extremes)."""
    tr     = _tr(close, high, low)
    max_tr = _rolling_max(tr, _TD_MON)
    min_tr = _rolling_min(tr, _TD_MON)
    return max_tr - min_tr


def rex_ext_070_range_of_ranges_63d_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day range-of-ranges normalized by 63-day ATR (how wide is the TR dispersion)."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_QTR)
    ror    = _rolling_max(tr, _TD_QTR) - _rolling_min(tr, _TD_QTR)
    return _safe_div(ror, atr)


def rex_ext_071_ror_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day range-of-ranges within trailing 252-day history."""
    tr   = _tr(close, high, low)
    ror  = _rolling_max(tr, _TD_MON) - _rolling_min(tr, _TD_MON)
    m    = _rolling_mean(ror, _TD_YEAR)
    s    = _rolling_std(ror, _TD_YEAR)
    return _safe_div(ror - m, s)


def rex_ext_072_ror_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day range-of-ranges within trailing 252 days."""
    tr  = _tr(close, high, low)
    ror = _rolling_max(tr, _TD_MON) - _rolling_min(tr, _TD_MON)
    return ror.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group K (073-075): Volume-confirmed expansion (new angles) ---

def rex_ext_073_vol_surge_on_expansion_ratio(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume on expansion days to volume on non-expansion days (21d window)."""
    tr      = _tr(close, high, low)
    atr     = _rolling_mean(tr, _TD_MON)
    is_exp  = tr > atr
    v_exp   = volume.where(is_exp,  np.nan).rolling(_TD_MON, min_periods=1).mean()
    v_no    = volume.where(~is_exp, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(v_exp, v_no)


def rex_ext_074_vol_weighted_tr_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume-weighted TR relative to 63-day distribution of VW-TR."""
    tr   = _tr(close, high, low)
    vwtr = _safe_div(tr * volume, _rolling_mean(volume, _TD_QTR))
    m    = _rolling_mean(vwtr, _TD_QTR)
    s    = _rolling_std(vwtr, _TD_QTR)
    return _safe_div(vwtr - m, s)


def rex_ext_075_high_vol_bearish_expansion_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: TR/ATR21 * vol/avgVol21 * (1 - close_pos_in_bar) — capitulation intensity."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_MON)
    avg_v  = _rolling_mean(volume, _TD_MON)
    hl     = (high - low).replace(0, np.nan)
    pos    = (close - low) / hl
    tr_r   = _safe_div(tr, atr)
    vol_r  = _safe_div(volume, avg_v)
    bear_r = (1 - pos.clip(0, 1))
    return tr_r * vol_r * bear_r


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_EXTENDED_REGISTRY_001_075 = {
    "rex_ext_001_nr14_flag": {"inputs": ["high", "low"], "func": rex_ext_001_nr14_flag},
    "rex_ext_002_wr14_flag": {"inputs": ["high", "low"], "func": rex_ext_002_wr14_flag},
    "rex_ext_003_nr21_flag": {"inputs": ["high", "low"], "func": rex_ext_003_nr21_flag},
    "rex_ext_004_wr21_flag": {"inputs": ["high", "low"], "func": rex_ext_004_wr21_flag},
    "rex_ext_005_nr21_count_63d": {"inputs": ["high", "low"], "func": rex_ext_005_nr21_count_63d},
    "rex_ext_006_wr21_count_63d": {"inputs": ["high", "low"], "func": rex_ext_006_wr21_count_63d},
    "rex_ext_007_days_since_nr21": {"inputs": ["high", "low"], "func": rex_ext_007_days_since_nr21},
    "rex_ext_008_days_since_wr21": {"inputs": ["high", "low"], "func": rex_ext_008_days_since_wr21},
    "rex_ext_009_nr21_consec_streak": {"inputs": ["high", "low"], "func": rex_ext_009_nr21_consec_streak},
    "rex_ext_010_nr21_pct_rank_252d": {"inputs": ["high", "low"], "func": rex_ext_010_nr21_pct_rank_252d},
    "rex_ext_011_nr4_then_wr7_flag": {"inputs": ["high", "low"], "func": rex_ext_011_nr4_then_wr7_flag},
    "rex_ext_012_nr7_then_wr7_within_5d": {"inputs": ["high", "low"], "func": rex_ext_012_nr7_then_wr7_within_5d},
    "rex_ext_013_nr7_then_wr7_count_63d": {"inputs": ["high", "low"], "func": rex_ext_013_nr7_then_wr7_count_63d},
    "rex_ext_014_days_since_nr_wr_breakout": {"inputs": ["high", "low"], "func": rex_ext_014_days_since_nr_wr_breakout},
    "rex_ext_015_nr21_then_expansion_flag": {"inputs": ["high", "low"], "func": rex_ext_015_nr21_then_expansion_flag},
    "rex_ext_016_nr14_then_wr14_flag": {"inputs": ["high", "low"], "func": rex_ext_016_nr14_then_wr14_flag},
    "rex_ext_017_nr_wr_breakout_count_252d": {"inputs": ["high", "low"], "func": rex_ext_017_nr_wr_breakout_count_252d},
    "rex_ext_018_wr4_after_nr7_ratio": {"inputs": ["high", "low"], "func": rex_ext_018_wr4_after_nr7_ratio},
    "rex_ext_019_thrust_bar_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_019_thrust_bar_flag},
    "rex_ext_020_bearish_thrust_bar_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_020_bearish_thrust_bar_flag},
    "rex_ext_021_two_bar_range_expansion_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_021_two_bar_range_expansion_flag},
    "rex_ext_022_three_bar_range_expansion_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_022_three_bar_range_expansion_flag},
    "rex_ext_023_two_bar_sequence_count_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_023_two_bar_sequence_count_21d},
    "rex_ext_024_three_bar_sequence_count_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_024_three_bar_sequence_count_63d},
    "rex_ext_025_bearish_thrust_count_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_025_bearish_thrust_count_21d},
    "rex_ext_026_bearish_thrust_count_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_026_bearish_thrust_count_63d},
    "rex_ext_027_tr_minus_atr21_in_atr_units": {"inputs": ["close", "high", "low"], "func": rex_ext_027_tr_minus_atr21_in_atr_units},
    "rex_ext_028_tr_excess_above_atr63_in_atr_units": {"inputs": ["close", "high", "low"], "func": rex_ext_028_tr_excess_above_atr63_in_atr_units},
    "rex_ext_029_hl_zscore_126d": {"inputs": ["high", "low"], "func": rex_ext_029_hl_zscore_126d},
    "rex_ext_030_tr_zscore_ewm21": {"inputs": ["close", "high", "low"], "func": rex_ext_030_tr_zscore_ewm21},
    "rex_ext_031_tr_above_3x_atr63_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_031_tr_above_3x_atr63_flag},
    "rex_ext_032_tr_above_2x_atr63_count_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_032_tr_above_2x_atr63_count_21d},
    "rex_ext_033_tr_above_1_5x_atr21_count_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_033_tr_above_1_5x_atr21_count_63d},
    "rex_ext_034_tr_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": rex_ext_034_tr_pct_rank_126d},
    "rex_ext_035_down_range_vs_tr_ratio": {"inputs": ["close", "high", "low"], "func": rex_ext_035_down_range_vs_tr_ratio},
    "rex_ext_036_up_range_vs_tr_ratio": {"inputs": ["close", "high", "low"], "func": rex_ext_036_up_range_vs_tr_ratio},
    "rex_ext_037_down_range_21d_avg": {"inputs": ["close", "high", "low"], "func": rex_ext_037_down_range_21d_avg},
    "rex_ext_038_down_vs_up_range_ratio": {"inputs": ["close", "high", "low"], "func": rex_ext_038_down_vs_up_range_ratio},
    "rex_ext_039_bearish_expansion_down_component_zscore": {"inputs": ["close", "high", "low"], "func": rex_ext_039_bearish_expansion_down_component_zscore},
    "rex_ext_040_close_in_lower_half_expansion_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_040_close_in_lower_half_expansion_21d},
    "rex_ext_041_close_in_lower_half_expansion_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_041_close_in_lower_half_expansion_63d},
    "rex_ext_042_down_expansion_consec": {"inputs": ["close", "high", "low"], "func": rex_ext_042_down_expansion_consec},
    "rex_ext_043_gap_adjusted_tr": {"inputs": ["close", "high", "low"], "func": rex_ext_043_gap_adjusted_tr},
    "rex_ext_044_overnight_gap_size": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_044_overnight_gap_size},
    "rex_ext_045_overnight_gap_ratio_atr21": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_045_overnight_gap_ratio_atr21},
    "rex_ext_046_gap_adjusted_tr_ratio_atr21": {"inputs": ["close", "high", "low"], "func": rex_ext_046_gap_adjusted_tr_ratio_atr21},
    "rex_ext_047_gap_adjusted_tr_zscore_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_047_gap_adjusted_tr_zscore_63d},
    "rex_ext_048_gap_down_magnitude_21d_avg": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_048_gap_down_magnitude_21d_avg},
    "rex_ext_049_gap_down_count_21d": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_049_gap_down_count_21d},
    "rex_ext_050_gap_down_expansion_zscore": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_050_gap_down_expansion_zscore},
    "rex_ext_051_hl_vs_cc_range_ratio": {"inputs": ["close", "high", "low"], "func": rex_ext_051_hl_vs_cc_range_ratio},
    "rex_ext_052_hl_vs_cc_divergence_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_052_hl_vs_cc_divergence_21d},
    "rex_ext_053_cc_range_zscore_21d": {"inputs": ["close"], "func": rex_ext_053_cc_range_zscore_21d},
    "rex_ext_054_cc_range_vs_atr21_ratio": {"inputs": ["close", "high", "low"], "func": rex_ext_054_cc_range_vs_atr21_ratio},
    "rex_ext_055_hl_cc_divergence_expanding_63d": {"inputs": ["close", "high", "low"], "func": rex_ext_055_hl_cc_divergence_expanding_63d},
    "rex_ext_056_cc_range_pct_rank_252d": {"inputs": ["close"], "func": rex_ext_056_cc_range_pct_rank_252d},
    "rex_ext_057_hl_minus_cc_21d_avg_in_atr": {"inputs": ["close", "high", "low"], "func": rex_ext_057_hl_minus_cc_21d_avg_in_atr},
    "rex_ext_058_cc_range_expansion_consec": {"inputs": ["close"], "func": rex_ext_058_cc_range_expansion_consec},
    "rex_ext_059_expansion_at_52wk_low_flag": {"inputs": ["close", "high", "low"], "func": rex_ext_059_expansion_at_52wk_low_flag},
    "rex_ext_060_expansion_near_low10pct_21d_atr2x": {"inputs": ["close", "high", "low"], "func": rex_ext_060_expansion_near_low10pct_21d_atr2x},
    "rex_ext_061_range_at_new_low_score": {"inputs": ["close", "high", "low"], "func": rex_ext_061_range_at_new_low_score},
    "rex_ext_062_expansion_at_new_low_count_252d": {"inputs": ["close", "high", "low"], "func": rex_ext_062_expansion_at_new_low_count_252d},
    "rex_ext_063_days_since_expansion_at_new_low": {"inputs": ["close", "high", "low"], "func": rex_ext_063_days_since_expansion_at_new_low},
    "rex_ext_064_open_to_high_range_ratio_atr21": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_064_open_to_high_range_ratio_atr21},
    "rex_ext_065_open_to_low_range_ratio_atr21": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_065_open_to_low_range_ratio_atr21},
    "rex_ext_066_opening_range_expansion_down_flag": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_066_opening_range_expansion_down_flag},
    "rex_ext_067_open_to_low_range_21d_avg": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_067_open_to_low_range_21d_avg},
    "rex_ext_068_opening_down_expansion_count_63d": {"inputs": ["close", "high", "low", "open"], "func": rex_ext_068_opening_down_expansion_count_63d},
    "rex_ext_069_range_of_ranges_21d": {"inputs": ["close", "high", "low"], "func": rex_ext_069_range_of_ranges_21d},
    "rex_ext_070_range_of_ranges_63d_norm": {"inputs": ["close", "high", "low"], "func": rex_ext_070_range_of_ranges_63d_norm},
    "rex_ext_071_ror_zscore_252d": {"inputs": ["close", "high", "low"], "func": rex_ext_071_ror_zscore_252d},
    "rex_ext_072_ror_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rex_ext_072_ror_pct_rank_252d},
    "rex_ext_073_vol_surge_on_expansion_ratio": {"inputs": ["close", "high", "low", "volume"], "func": rex_ext_073_vol_surge_on_expansion_ratio},
    "rex_ext_074_vol_weighted_tr_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": rex_ext_074_vol_weighted_tr_zscore_63d},
    "rex_ext_075_high_vol_bearish_expansion_score": {"inputs": ["close", "high", "low", "volume"], "func": rex_ext_075_high_vol_bearish_expansion_score},
}
