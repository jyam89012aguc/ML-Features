"""
37_range_expansion — Base Features 001-075
Domain: true-range expansion near the low — TR/HL widening vs trailing averages,
        expansion z-scores and counts, ATR rising, consecutive expanding-range days,
        range expansion while price is near its lows, percentile ranks of TR ratios
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
    idx = np.arange(len(cond))
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    last = -1
    for i, v in enumerate(cond):
        if v:
            last = i
        if last >= 0:
            out.iloc[i] = i - last
    return out


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): TR vs ATR ratio — raw expansion magnitude ---

def rex_001_tr_ratio_atr5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 5-day ATR (immediate range-pop ratio)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_WEEK)
    return _safe_div(tr, atr)


def rex_002_tr_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(tr, atr)


def rex_003_tr_ratio_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 63-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return _safe_div(tr, atr)


def rex_004_tr_ratio_atr126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 126-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_HALF)
    return _safe_div(tr, atr)


def rex_005_tr_ratio_atr252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 252-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_YEAR)
    return _safe_div(tr, atr)


def rex_006_hl_ratio_hl5(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's H-L range divided by 5-day average H-L range."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_WEEK)
    return _safe_div(hl, avg)


def rex_007_hl_ratio_hl21(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's H-L range divided by 21-day average H-L range."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_MON)
    return _safe_div(hl, avg)


def rex_008_hl_ratio_hl63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's H-L range divided by 63-day average H-L range."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_QTR)
    return _safe_div(hl, avg)


def rex_009_hl_ratio_hl252(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's H-L range divided by 252-day average H-L range."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_YEAR)
    return _safe_div(hl, avg)


def rex_010_tr_log_ratio_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log of (TR / 21-day ATR) — compresses extreme spikes."""
    return np.log1p(rex_002_tr_ratio_atr21(close, high, low) - 1)


def rex_011_tr_ratio_ewm_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR divided by 21-day EWM-ATR."""
    tr  = _tr(close, high, low)
    ewm = _ewm_mean(tr, _TD_MON)
    return _safe_div(tr, ewm)


def rex_012_tr_ratio_median_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR divided by 63-day median TR (robust to outliers)."""
    tr  = _tr(close, high, low)
    med = _rolling_median(tr, _TD_QTR)
    return _safe_div(tr, med)


# --- Group B (013-025): TR z-score — statistical extremity of range ---

def rex_013_tr_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TR relative to 21-day mean and std."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_MON)
    s  = _rolling_std(tr, _TD_MON)
    return _safe_div(tr - m, s)


def rex_014_tr_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TR relative to 63-day mean and std."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_QTR)
    s  = _rolling_std(tr, _TD_QTR)
    return _safe_div(tr - m, s)


def rex_015_tr_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TR relative to 126-day mean and std."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_HALF)
    s  = _rolling_std(tr, _TD_HALF)
    return _safe_div(tr - m, s)


def rex_016_tr_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TR relative to 252-day mean and std."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_YEAR)
    s  = _rolling_std(tr, _TD_YEAR)
    return _safe_div(tr - m, s)


def rex_017_hl_zscore_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range relative to 21-day distribution."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_MON)
    s  = _rolling_std(hl, _TD_MON)
    return _safe_div(hl - m, s)


def rex_018_hl_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range relative to 63-day distribution."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_QTR)
    s  = _rolling_std(hl, _TD_QTR)
    return _safe_div(hl - m, s)


def rex_019_hl_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of H-L range relative to 252-day distribution."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_YEAR)
    s  = _rolling_std(hl, _TD_YEAR)
    return _safe_div(hl - m, s)


def rex_020_tr_zscore_clipped_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day TR z-score clipped to [-3, 10] — positive tail kept intact."""
    z = rex_013_tr_zscore_21d(close, high, low)
    return z.clip(lower=-3, upper=10)


def rex_021_tr_zscore_clipped_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day TR z-score clipped to [-3, 10]."""
    z = rex_014_tr_zscore_63d(close, high, low)
    return z.clip(lower=-3, upper=10)


def rex_022_tr_above_1std_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: TR exceeds 21-day mean + 1 std (moderate expansion event)."""
    return (rex_013_tr_zscore_21d(close, high, low) > 1.0).astype(float)


def rex_023_tr_above_2std_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: TR exceeds 21-day mean + 2 std (strong expansion event)."""
    return (rex_013_tr_zscore_21d(close, high, low) > 2.0).astype(float)


def rex_024_tr_above_2std_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: TR exceeds 63-day mean + 2 std."""
    return (rex_014_tr_zscore_63d(close, high, low) > 2.0).astype(float)


def rex_025_tr_above_3std_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: TR exceeds 252-day mean + 3 std (extreme expansion)."""
    return (rex_016_tr_zscore_252d(close, high, low) > 3.0).astype(float)


# --- Group C (026-038): Expansion-day counts over rolling windows ---

def rex_026_expansion_count_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 5 where TR > 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > atr, _TD_WEEK)


def rex_027_expansion_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 21 where TR > 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > atr, _TD_MON)


def rex_028_expansion_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 63 where TR > 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > atr, _TD_QTR)


def rex_029_expansion_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 252 where TR > 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > atr, _TD_YEAR)


def rex_030_strong_expansion_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 21 where TR > 2x 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(tr > 2 * atr, _TD_MON)


def rex_031_strong_expansion_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 63 where TR > 2x 63-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return _rolling_count_true(tr > 2 * atr, _TD_QTR)


def rex_032_expansion_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days where TR > 21-day ATR."""
    return rex_027_expansion_count_21d(close, high, low) / _TD_MON


def rex_033_expansion_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days where TR > 21-day ATR."""
    return rex_028_expansion_count_63d(close, high, low) / _TD_QTR


def rex_034_expansion_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days where TR > 21-day ATR."""
    return rex_029_expansion_count_252d(close, high, low) / _TD_YEAR


def rex_035_hl_expansion_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 21 where H-L > 21-day average H-L."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_MON)
    return _rolling_count_true(hl > avg, _TD_MON)


def rex_036_hl_expansion_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in last 63 where H-L > 63-day average H-L."""
    hl  = high - low
    avg = _rolling_mean(hl, _TD_QTR)
    return _rolling_count_true(hl > avg, _TD_QTR)


def rex_037_expansion_count_norm_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day expansion count normalized by 252-day average expansion count."""
    cnt21  = rex_027_expansion_count_21d(close, high, low)
    cnt252 = rex_029_expansion_count_252d(close, high, low)
    avg252 = _rolling_mean(cnt252, _TD_YEAR)
    return _safe_div(cnt21, avg252 / (_TD_YEAR / _TD_MON))


def rex_038_expansion_zscore_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 63-day expansion count relative to 252-day history."""
    cnt63 = rex_028_expansion_count_63d(close, high, low)
    m     = _rolling_mean(cnt63, _TD_YEAR)
    s     = _rolling_std(cnt63, _TD_YEAR)
    return _safe_div(cnt63 - m, s)


# --- Group D (039-050): Consecutive expanding-range days ---

def rex_039_consec_expanding_tr_days(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where TR > prior day's TR."""
    tr   = _tr(close, high, low)
    cond = tr > tr.shift(1)
    return _consec_streak(cond)


def rex_040_consec_tr_above_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where TR > 21-day ATR."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    cond = tr > atr
    return _consec_streak(cond)


def rex_041_consec_tr_above_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where TR > 63-day ATR."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_QTR)
    cond = tr > atr
    return _consec_streak(cond)


def rex_042_consec_hl_expanding(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where H-L range > prior day's H-L range."""
    hl   = high - low
    cond = hl > hl.shift(1)
    return _consec_streak(cond)


def rex_043_consec_hl_above_avg21(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where H-L > 21-day average H-L."""
    hl   = high - low
    avg  = _rolling_mean(hl, _TD_MON)
    cond = hl > avg
    return _consec_streak(cond)


def rex_044_max_consec_expanding_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive expanding-TR run within trailing 21 days."""
    tr   = _tr(close, high, low)
    cond = tr > tr.shift(1)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def rex_045_max_consec_expanding_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive expanding-TR run within trailing 63 days."""
    tr   = _tr(close, high, low)
    cond = tr > tr.shift(1)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def rex_046_consec_expanding_tr_norm_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current expanding-TR streak normalized by 21-day average streak."""
    s   = rex_039_consec_expanding_tr_days(close, high, low)
    avg = _rolling_mean(s, _TD_MON)
    return _safe_div(s, avg)


def rex_047_consec_expanding_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of expanding-TR streak within trailing 252-day streak series."""
    s = rex_039_consec_expanding_tr_days(close, high, low)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_048_consec_tr_above_2x_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where TR > 2x 21-day ATR."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    cond = tr > 2 * atr
    return _consec_streak(cond)


def rex_049_consec_expanding_tr_flag_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: at least 3 of last 5 days had TR > prior TR."""
    tr  = _tr(close, high, low)
    exp = (tr > tr.shift(1)).astype(float)
    return (_rolling_sum(exp, _TD_WEEK) >= 3).astype(float)


def rex_050_consec_hl_expanding_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of current H-L expanding streak within trailing 252 days."""
    s = rex_042_consec_hl_expanding(high, low)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (051-062): Range expansion while price is near its lows ---

def rex_051_tr_ratio_atr21_near_low21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR/ATR21 ratio, masked to zero when close is NOT in lowest 20% of 21-day range."""
    ratio   = rex_002_tr_ratio_atr21(close, high, low)
    lo21    = _rolling_min(close, _TD_MON)
    hi21    = _rolling_max(close, _TD_MON)
    rng21   = (hi21 - lo21).replace(0, np.nan)
    pos     = (close - lo21) / rng21
    return ratio.where(pos <= 0.20, 0.0)


def rex_052_tr_ratio_atr21_near_low63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR/ATR21, masked to zero when close is NOT in lowest 20% of 63-day range."""
    ratio = rex_002_tr_ratio_atr21(close, high, low)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng63 = (hi63 - lo63).replace(0, np.nan)
    pos   = (close - lo63) / rng63
    return ratio.where(pos <= 0.20, 0.0)


def rex_053_tr_zscore_21d_near_low63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TR z-score (21d), masked to zero when price NOT in lowest 20% of 63-day range."""
    z    = rex_013_tr_zscore_21d(close, high, low)
    lo63 = _rolling_min(close, _TD_QTR)
    hi63 = _rolling_max(close, _TD_QTR)
    rng  = (hi63 - lo63).replace(0, np.nan)
    pos  = (close - lo63) / rng
    return z.where(pos <= 0.20, 0.0)


def rex_054_expansion_near_low_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 21 days where TR > ATR21 AND close in lowest 20% of 63-day range."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo63 = _rolling_min(close, _TD_QTR)
    hi63 = _rolling_max(close, _TD_QTR)
    rng  = (hi63 - lo63).replace(0, np.nan)
    pos  = (close - lo63) / rng
    cond = (tr > atr) & (pos <= 0.20)
    return _rolling_count_true(cond, _TD_MON)


def rex_055_expansion_near_low_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 63 days where TR > ATR21 AND close in lowest 20% of 63-day range."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo63 = _rolling_min(close, _TD_QTR)
    hi63 = _rolling_max(close, _TD_QTR)
    rng  = (hi63 - lo63).replace(0, np.nan)
    pos  = (close - lo63) / rng
    cond = (tr > atr) & (pos <= 0.20)
    return _rolling_count_true(cond, _TD_QTR)


def rex_056_expansion_near_low_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 252 days where TR > ATR21 AND close in lowest 20% of 252-day range."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo   = _rolling_min(close, _TD_YEAR)
    hi   = _rolling_max(close, _TD_YEAR)
    rng  = (hi - lo).replace(0, np.nan)
    pos  = (close - lo) / rng
    cond = (tr > atr) & (pos <= 0.20)
    return _rolling_count_true(cond, _TD_YEAR)


def rex_057_consec_expansion_near_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days of TR > ATR21 while close in lowest 20% of 63-day range."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    lo63 = _rolling_min(close, _TD_QTR)
    hi63 = _rolling_max(close, _TD_QTR)
    rng  = (hi63 - lo63).replace(0, np.nan)
    pos  = (close - lo63) / rng
    cond = (tr > atr) & (pos <= 0.20)
    return _consec_streak(cond)


def rex_058_tr_near_low_vs_not_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of avg TR near lows to avg TR not near lows over 63 days."""
    tr   = _tr(close, high, low)
    lo63 = _rolling_min(close, _TD_QTR)
    hi63 = _rolling_max(close, _TD_QTR)
    rng  = (hi63 - lo63).replace(0, np.nan)
    pos  = (close - lo63) / rng
    near = pos <= 0.20
    tr_near = tr.where(near, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    tr_far  = tr.where(~near, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(tr_near, tr_far)


def rex_059_expansion_near_52wk_low_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 21 days where TR > ATR21 AND close in lowest 10% of 252-day range."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    lo  = _rolling_min(close, _TD_YEAR)
    hi  = _rolling_max(close, _TD_YEAR)
    rng = (hi - lo).replace(0, np.nan)
    pos = (close - lo) / rng
    cond = (tr > atr) & (pos <= 0.10)
    return _rolling_count_true(cond, _TD_MON)


def rex_060_tr_ratio_low_pct_interaction_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Product of TR/ATR21 and (1 - close position in 21-day range) as distress score."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo21  = _rolling_min(close, _TD_MON)
    hi21  = _rolling_max(close, _TD_MON)
    rng   = (hi21 - lo21).replace(0, np.nan)
    pos   = (close - lo21) / rng
    return ratio * (1 - pos.clip(0, 1))


def rex_061_expansion_near_low_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day near-low expansion count over 63-day history."""
    cnt = rex_054_expansion_near_low_count_21d(close, high, low)
    m   = _rolling_mean(cnt, _TD_QTR)
    s   = _rolling_std(cnt, _TD_QTR)
    return _safe_div(cnt - m, s)


def rex_062_expansion_near_low_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 63-day near-low expansion count over 252-day history."""
    cnt = rex_055_expansion_near_low_count_63d(close, high, low)
    m   = _rolling_mean(cnt, _TD_YEAR)
    s   = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


# --- Group F (063-075): ATR level/trend, largest TR, percentile ranks ---

def rex_063_atr21_pct_of_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day ATR as a percentage of closing price (normalized volatility)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(atr, close) * 100.0


def rex_064_atr63_pct_of_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day ATR as a percentage of closing price."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return _safe_div(atr, close) * 100.0


def rex_065_atr21_rising_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: 21-day ATR today > 21-day ATR 5 days ago."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return (atr > atr.shift(_TD_WEEK)).astype(float)


def rex_066_atr21_rising_21d_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 21 days where 21-day ATR was rising (ATR > ATR 5d ago)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    rising = atr > atr.shift(_TD_WEEK)
    return _rolling_count_true(rising, _TD_MON)


def rex_067_atr21_vs_atr63_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR to 63-day ATR (recent vs medium-term vol level)."""
    tr  = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))


def rex_068_atr5_vs_atr63_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 63-day ATR (short burst vs medium baseline)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_QTR))


def rex_069_atr21_vs_atr252_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR to 252-day ATR (current vs annual baseline)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))


def rex_070_max_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum TR over trailing 21 days (largest range day)."""
    tr = _tr(close, high, low)
    return _rolling_max(tr, _TD_MON)


def rex_071_max_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum TR over trailing 63 days."""
    tr = _tr(close, high, low)
    return _rolling_max(tr, _TD_QTR)


def rex_072_max_tr_21d_vs_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max 21-day TR divided by 63-day ATR (spike height vs baseline)."""
    tr   = _tr(close, high, low)
    mx21 = _rolling_max(tr, _TD_MON)
    atr  = _rolling_mean(tr, _TD_QTR)
    return _safe_div(mx21, atr)


def rex_073_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 252-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_074_tr_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 63-day TR series."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rex_075_recent_range_vs_prior_baseline(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day average TR to prior 63-day average TR (new vs old baseline)."""
    tr     = _tr(close, high, low)
    recent = _rolling_mean(tr, _TD_WEEK)
    prior  = _rolling_mean(tr.shift(_TD_WEEK), _TD_QTR)
    return _safe_div(recent, prior)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_REGISTRY_001_075 = {
    "rex_001_tr_ratio_atr5": {"inputs": ["close", "high", "low"], "func": rex_001_tr_ratio_atr5},
    "rex_002_tr_ratio_atr21": {"inputs": ["close", "high", "low"], "func": rex_002_tr_ratio_atr21},
    "rex_003_tr_ratio_atr63": {"inputs": ["close", "high", "low"], "func": rex_003_tr_ratio_atr63},
    "rex_004_tr_ratio_atr126": {"inputs": ["close", "high", "low"], "func": rex_004_tr_ratio_atr126},
    "rex_005_tr_ratio_atr252": {"inputs": ["close", "high", "low"], "func": rex_005_tr_ratio_atr252},
    "rex_006_hl_ratio_hl5": {"inputs": ["high", "low"], "func": rex_006_hl_ratio_hl5},
    "rex_007_hl_ratio_hl21": {"inputs": ["high", "low"], "func": rex_007_hl_ratio_hl21},
    "rex_008_hl_ratio_hl63": {"inputs": ["high", "low"], "func": rex_008_hl_ratio_hl63},
    "rex_009_hl_ratio_hl252": {"inputs": ["high", "low"], "func": rex_009_hl_ratio_hl252},
    "rex_010_tr_log_ratio_atr21": {"inputs": ["close", "high", "low"], "func": rex_010_tr_log_ratio_atr21},
    "rex_011_tr_ratio_ewm_atr21": {"inputs": ["close", "high", "low"], "func": rex_011_tr_ratio_ewm_atr21},
    "rex_012_tr_ratio_median_atr63": {"inputs": ["close", "high", "low"], "func": rex_012_tr_ratio_median_atr63},
    "rex_013_tr_zscore_21d": {"inputs": ["close", "high", "low"], "func": rex_013_tr_zscore_21d},
    "rex_014_tr_zscore_63d": {"inputs": ["close", "high", "low"], "func": rex_014_tr_zscore_63d},
    "rex_015_tr_zscore_126d": {"inputs": ["close", "high", "low"], "func": rex_015_tr_zscore_126d},
    "rex_016_tr_zscore_252d": {"inputs": ["close", "high", "low"], "func": rex_016_tr_zscore_252d},
    "rex_017_hl_zscore_21d": {"inputs": ["high", "low"], "func": rex_017_hl_zscore_21d},
    "rex_018_hl_zscore_63d": {"inputs": ["high", "low"], "func": rex_018_hl_zscore_63d},
    "rex_019_hl_zscore_252d": {"inputs": ["high", "low"], "func": rex_019_hl_zscore_252d},
    "rex_020_tr_zscore_clipped_21d": {"inputs": ["close", "high", "low"], "func": rex_020_tr_zscore_clipped_21d},
    "rex_021_tr_zscore_clipped_63d": {"inputs": ["close", "high", "low"], "func": rex_021_tr_zscore_clipped_63d},
    "rex_022_tr_above_1std_21d_flag": {"inputs": ["close", "high", "low"], "func": rex_022_tr_above_1std_21d_flag},
    "rex_023_tr_above_2std_21d_flag": {"inputs": ["close", "high", "low"], "func": rex_023_tr_above_2std_21d_flag},
    "rex_024_tr_above_2std_63d_flag": {"inputs": ["close", "high", "low"], "func": rex_024_tr_above_2std_63d_flag},
    "rex_025_tr_above_3std_252d_flag": {"inputs": ["close", "high", "low"], "func": rex_025_tr_above_3std_252d_flag},
    "rex_026_expansion_count_5d": {"inputs": ["close", "high", "low"], "func": rex_026_expansion_count_5d},
    "rex_027_expansion_count_21d": {"inputs": ["close", "high", "low"], "func": rex_027_expansion_count_21d},
    "rex_028_expansion_count_63d": {"inputs": ["close", "high", "low"], "func": rex_028_expansion_count_63d},
    "rex_029_expansion_count_252d": {"inputs": ["close", "high", "low"], "func": rex_029_expansion_count_252d},
    "rex_030_strong_expansion_count_21d": {"inputs": ["close", "high", "low"], "func": rex_030_strong_expansion_count_21d},
    "rex_031_strong_expansion_count_63d": {"inputs": ["close", "high", "low"], "func": rex_031_strong_expansion_count_63d},
    "rex_032_expansion_fraction_21d": {"inputs": ["close", "high", "low"], "func": rex_032_expansion_fraction_21d},
    "rex_033_expansion_fraction_63d": {"inputs": ["close", "high", "low"], "func": rex_033_expansion_fraction_63d},
    "rex_034_expansion_fraction_252d": {"inputs": ["close", "high", "low"], "func": rex_034_expansion_fraction_252d},
    "rex_035_hl_expansion_count_21d": {"inputs": ["high", "low"], "func": rex_035_hl_expansion_count_21d},
    "rex_036_hl_expansion_count_63d": {"inputs": ["high", "low"], "func": rex_036_hl_expansion_count_63d},
    "rex_037_expansion_count_norm_21d": {"inputs": ["close", "high", "low"], "func": rex_037_expansion_count_norm_21d},
    "rex_038_expansion_zscore_count_63d": {"inputs": ["close", "high", "low"], "func": rex_038_expansion_zscore_count_63d},
    "rex_039_consec_expanding_tr_days": {"inputs": ["close", "high", "low"], "func": rex_039_consec_expanding_tr_days},
    "rex_040_consec_tr_above_atr21": {"inputs": ["close", "high", "low"], "func": rex_040_consec_tr_above_atr21},
    "rex_041_consec_tr_above_atr63": {"inputs": ["close", "high", "low"], "func": rex_041_consec_tr_above_atr63},
    "rex_042_consec_hl_expanding": {"inputs": ["high", "low"], "func": rex_042_consec_hl_expanding},
    "rex_043_consec_hl_above_avg21": {"inputs": ["high", "low"], "func": rex_043_consec_hl_above_avg21},
    "rex_044_max_consec_expanding_tr_21d": {"inputs": ["close", "high", "low"], "func": rex_044_max_consec_expanding_tr_21d},
    "rex_045_max_consec_expanding_tr_63d": {"inputs": ["close", "high", "low"], "func": rex_045_max_consec_expanding_tr_63d},
    "rex_046_consec_expanding_tr_norm_21d": {"inputs": ["close", "high", "low"], "func": rex_046_consec_expanding_tr_norm_21d},
    "rex_047_consec_expanding_tr_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rex_047_consec_expanding_tr_pct_rank_252d},
    "rex_048_consec_tr_above_2x_atr21": {"inputs": ["close", "high", "low"], "func": rex_048_consec_tr_above_2x_atr21},
    "rex_049_consec_expanding_tr_flag_5d": {"inputs": ["close", "high", "low"], "func": rex_049_consec_expanding_tr_flag_5d},
    "rex_050_consec_hl_expanding_pct_rank_252d": {"inputs": ["high", "low"], "func": rex_050_consec_hl_expanding_pct_rank_252d},
    "rex_051_tr_ratio_atr21_near_low21": {"inputs": ["close", "high", "low"], "func": rex_051_tr_ratio_atr21_near_low21},
    "rex_052_tr_ratio_atr21_near_low63": {"inputs": ["close", "high", "low"], "func": rex_052_tr_ratio_atr21_near_low63},
    "rex_053_tr_zscore_21d_near_low63": {"inputs": ["close", "high", "low"], "func": rex_053_tr_zscore_21d_near_low63},
    "rex_054_expansion_near_low_count_21d": {"inputs": ["close", "high", "low"], "func": rex_054_expansion_near_low_count_21d},
    "rex_055_expansion_near_low_count_63d": {"inputs": ["close", "high", "low"], "func": rex_055_expansion_near_low_count_63d},
    "rex_056_expansion_near_low_count_252d": {"inputs": ["close", "high", "low"], "func": rex_056_expansion_near_low_count_252d},
    "rex_057_consec_expansion_near_low": {"inputs": ["close", "high", "low"], "func": rex_057_consec_expansion_near_low},
    "rex_058_tr_near_low_vs_not_ratio_63d": {"inputs": ["close", "high", "low"], "func": rex_058_tr_near_low_vs_not_ratio_63d},
    "rex_059_expansion_near_52wk_low_count_21d": {"inputs": ["close", "high", "low"], "func": rex_059_expansion_near_52wk_low_count_21d},
    "rex_060_tr_ratio_low_pct_interaction_21d": {"inputs": ["close", "high", "low"], "func": rex_060_tr_ratio_low_pct_interaction_21d},
    "rex_061_expansion_near_low_zscore_63d": {"inputs": ["close", "high", "low"], "func": rex_061_expansion_near_low_zscore_63d},
    "rex_062_expansion_near_low_zscore_252d": {"inputs": ["close", "high", "low"], "func": rex_062_expansion_near_low_zscore_252d},
    "rex_063_atr21_pct_of_close": {"inputs": ["close", "high", "low"], "func": rex_063_atr21_pct_of_close},
    "rex_064_atr63_pct_of_close": {"inputs": ["close", "high", "low"], "func": rex_064_atr63_pct_of_close},
    "rex_065_atr21_rising_flag": {"inputs": ["close", "high", "low"], "func": rex_065_atr21_rising_flag},
    "rex_066_atr21_rising_21d_count": {"inputs": ["close", "high", "low"], "func": rex_066_atr21_rising_21d_count},
    "rex_067_atr21_vs_atr63_ratio": {"inputs": ["close", "high", "low"], "func": rex_067_atr21_vs_atr63_ratio},
    "rex_068_atr5_vs_atr63_ratio": {"inputs": ["close", "high", "low"], "func": rex_068_atr5_vs_atr63_ratio},
    "rex_069_atr21_vs_atr252_ratio": {"inputs": ["close", "high", "low"], "func": rex_069_atr21_vs_atr252_ratio},
    "rex_070_max_tr_21d": {"inputs": ["close", "high", "low"], "func": rex_070_max_tr_21d},
    "rex_071_max_tr_63d": {"inputs": ["close", "high", "low"], "func": rex_071_max_tr_63d},
    "rex_072_max_tr_21d_vs_atr63": {"inputs": ["close", "high", "low"], "func": rex_072_max_tr_21d_vs_atr63},
    "rex_073_tr_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rex_073_tr_pct_rank_252d},
    "rex_074_tr_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": rex_074_tr_pct_rank_63d},
    "rex_075_recent_range_vs_prior_baseline": {"inputs": ["close", "high", "low"], "func": rex_075_recent_range_vs_prior_baseline},
}
