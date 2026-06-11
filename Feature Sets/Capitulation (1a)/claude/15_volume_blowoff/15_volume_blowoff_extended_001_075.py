"""
15_volume_blowoff — Extended Features 001-075 (RVOL and deeper signal)
Domain: Relative Volume (RVOL) — volume / rolling mean baseline — and derived
blow-off intensity signals.  Covers RVOL at multiple horizons, RVOL vs median
baseline, cumulative RVOL, RVOL z-score, RVOL at multi-window highs, consecutive-
elevated-RVOL streaks, RVOL percentile ranks, days-since-RVOL-spike, dollar-RVOL,
EWM-baseline RVOL, volume acceleration on spike days, volume-spike on down days
(capitulation blow-off), largest RVOL in a window, blow-off-then-dryup sequences,
volume-spike clustering, and rate-of-change of RVOL.
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
    """Rolling mean with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    """Rolling median with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """EWM mean with min_periods = span//2."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Natural log after clipping to _EPS."""
    return np.log(s.clip(lower=_EPS))


def _rvol(volume: pd.Series, w: int) -> pd.Series:
    """Core RVOL: volume / trailing w-day rolling MEAN baseline."""
    return _safe_div(volume, _rolling_mean(volume, w))


def _rvol_median(volume: pd.Series, w: int) -> pd.Series:
    """RVOL vs trailing w-day rolling MEDIAN baseline (robust variant)."""
    return _safe_div(volume, _rolling_median(volume, w))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature Functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Core RVOL at standard horizons (mean baseline) ---

def vb_ext_001_rvol_5d(volume: pd.Series) -> pd.Series:
    """RVOL(5): volume / 5-day rolling mean — very-short-window relative volume."""
    return _rvol(volume, _TD_WEEK)


def vb_ext_002_rvol_10d(volume: pd.Series) -> pd.Series:
    """RVOL(10): volume / 10-day rolling mean — 2-week relative volume."""
    return _rvol(volume, 10)


def vb_ext_003_rvol_21d(volume: pd.Series) -> pd.Series:
    """RVOL(21): volume / 21-day rolling mean — monthly relative volume."""
    return _rvol(volume, _TD_MON)


def vb_ext_004_rvol_63d(volume: pd.Series) -> pd.Series:
    """RVOL(63): volume / 63-day rolling mean — quarterly relative volume."""
    return _rvol(volume, _TD_QTR)


def vb_ext_005_rvol_252d(volume: pd.Series) -> pd.Series:
    """RVOL(252): volume / 252-day rolling mean — annual relative volume."""
    return _rvol(volume, _TD_YEAR)


def vb_ext_006_rvol_median_5d(volume: pd.Series) -> pd.Series:
    """RVOL vs 5-day median baseline (robust very-short RVOL)."""
    return _rvol_median(volume, _TD_WEEK)


def vb_ext_007_rvol_median_10d(volume: pd.Series) -> pd.Series:
    """RVOL vs 10-day median baseline (robust 2-week RVOL)."""
    return _rvol_median(volume, 10)


def vb_ext_008_rvol_median_63d(volume: pd.Series) -> pd.Series:
    """RVOL vs 63-day median baseline (robust quarterly RVOL)."""
    return _rvol_median(volume, _TD_QTR)


def vb_ext_009_rvol_median_252d(volume: pd.Series) -> pd.Series:
    """RVOL vs 252-day median baseline (robust annual RVOL)."""
    return _rvol_median(volume, _TD_YEAR)


def vb_ext_010_log_rvol_5d(volume: pd.Series) -> pd.Series:
    """Log(1 + RVOL(5)): log-transformed 5-day RVOL (compresses extreme tails)."""
    return np.log1p(_rvol(volume, _TD_WEEK))


def vb_ext_011_log_rvol_21d(volume: pd.Series) -> pd.Series:
    """Log(1 + RVOL(21)): log-transformed 21-day RVOL."""
    return np.log1p(_rvol(volume, _TD_MON))


def vb_ext_012_log_rvol_63d(volume: pd.Series) -> pd.Series:
    """Log(1 + RVOL(63)): log-transformed 63-day RVOL."""
    return np.log1p(_rvol(volume, _TD_QTR))


def vb_ext_013_log_rvol_252d(volume: pd.Series) -> pd.Series:
    """Log(1 + RVOL(252)): log-transformed annual RVOL."""
    return np.log1p(_rvol(volume, _TD_YEAR))


def vb_ext_014_rvol_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """RVOL(5) / RVOL(252): ratio of very-short RVOL to annual RVOL (burst relative to trend)."""
    return _safe_div(_rvol(volume, _TD_WEEK), _rvol(volume, _TD_YEAR))


def vb_ext_015_rvol_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """RVOL(21) / RVOL(252): monthly RVOL relative to annual RVOL."""
    return _safe_div(_rvol(volume, _TD_MON), _rvol(volume, _TD_YEAR))


# --- Group B (016-025): RVOL z-scores ---

def vb_ext_016_rvol_zscore_21d_baseline(volume: pd.Series) -> pd.Series:
    """Z-score of RVOL(21) vs its own 63-day distribution (RVOL of RVOL spike)."""
    rvol21 = _rvol(volume, _TD_MON)
    m = _rolling_mean(rvol21, _TD_QTR)
    s = _rolling_std(rvol21, _TD_QTR)
    return _safe_div(rvol21 - m, s)


def vb_ext_017_rvol_zscore_63d_baseline(volume: pd.Series) -> pd.Series:
    """Z-score of RVOL(63) vs its own 252-day distribution."""
    rvol63 = _rvol(volume, _TD_QTR)
    m = _rolling_mean(rvol63, _TD_YEAR)
    s = _rolling_std(rvol63, _TD_YEAR)
    return _safe_div(rvol63 - m, s)


def vb_ext_018_rvol_zscore_5d_baseline(volume: pd.Series) -> pd.Series:
    """Z-score of RVOL(5) vs its own 63-day distribution (short-burst extremity)."""
    rvol5 = _rvol(volume, _TD_WEEK)
    m = _rolling_mean(rvol5, _TD_QTR)
    s = _rolling_std(rvol5, _TD_QTR)
    return _safe_div(rvol5 - m, s)


def vb_ext_019_rvol_zscore_252d_baseline(volume: pd.Series) -> pd.Series:
    """Z-score of RVOL(252) vs its expanding distribution (all-history RVOL extremity)."""
    rvol252 = _rvol(volume, _TD_YEAR)
    m = rvol252.expanding(min_periods=5).mean()
    s = rvol252.expanding(min_periods=5).std()
    return _safe_div(rvol252 - m, s)


def vb_ext_020_rvol_median_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of RVOL-vs-median(21) vs its 63-day distribution."""
    r = _rvol_median(volume, _TD_MON)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


# --- Group C (021-030): Cumulative RVOL over short windows ---

def vb_ext_021_cumrvol_5d(volume: pd.Series) -> pd.Series:
    """Sum of RVOL(21) over trailing 5 days (cumulative very-short RVOL energy)."""
    rvol = _rvol(volume, _TD_MON)
    return _rolling_sum(rvol, _TD_WEEK)


def vb_ext_022_cumrvol_10d(volume: pd.Series) -> pd.Series:
    """Sum of RVOL(21) over trailing 10 days (cumulative 2-week RVOL energy)."""
    rvol = _rvol(volume, _TD_MON)
    return rvol.rolling(10, min_periods=5).sum()


def vb_ext_023_cumrvol_21d(volume: pd.Series) -> pd.Series:
    """Sum of RVOL(21) over trailing 21 days (cumulative monthly RVOL energy)."""
    rvol = _rvol(volume, _TD_MON)
    return _rolling_sum(rvol, _TD_MON)


def vb_ext_024_cumrvol_5d_norm_252d(volume: pd.Series) -> pd.Series:
    """5-day cumulative RVOL(21) normalized by 252-day mean of 5d cumulative RVOL."""
    rvol = _rvol(volume, _TD_MON)
    cum5 = _rolling_sum(rvol, _TD_WEEK)
    avg = _rolling_mean(cum5, _TD_YEAR)
    return _safe_div(cum5, avg)


def vb_ext_025_cumrvol_10d_norm_252d(volume: pd.Series) -> pd.Series:
    """10-day cumulative RVOL(21) normalized by 252-day average."""
    rvol = _rvol(volume, _TD_MON)
    cum10 = rvol.rolling(10, min_periods=5).sum()
    avg = _rolling_mean(cum10, _TD_YEAR)
    return _safe_div(cum10, avg)


def vb_ext_026_cumrvol_median_5d(volume: pd.Series) -> pd.Series:
    """Sum of RVOL-vs-median(21) over trailing 5 days (robust cumulative short RVOL)."""
    r = _rvol_median(volume, _TD_MON)
    return _rolling_sum(r, _TD_WEEK)


def vb_ext_027_cumrvol_excess_above_1_5d(volume: pd.Series) -> pd.Series:
    """Sum of (RVOL(5) - 1).clip(0) over trailing 5 days (only count RVOL > 1 as excess)."""
    rvol5 = _rvol(volume, _TD_WEEK)
    excess = (rvol5 - 1.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_WEEK)


def vb_ext_028_cumrvol_excess_above_1_21d(volume: pd.Series) -> pd.Series:
    """Sum of (RVOL(21) - 1).clip(0) over trailing 21 days (monthly above-average excess)."""
    rvol21 = _rvol(volume, _TD_MON)
    excess = (rvol21 - 1.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_MON)


def vb_ext_029_cumrvol_excess_above_15_21d(volume: pd.Series) -> pd.Series:
    """Sum of (RVOL(21) - 1.5).clip(0) over trailing 21 days (elevated-RVOL excess)."""
    rvol21 = _rvol(volume, _TD_MON)
    excess = (rvol21 - 1.5).clip(lower=0.0)
    return _rolling_sum(excess, _TD_MON)


def vb_ext_030_cumrvol_excess_above_2_5d(volume: pd.Series) -> pd.Series:
    """Sum of (RVOL(5) - 2).clip(0) over 5 days (extreme-burst RVOL excess)."""
    rvol5 = _rvol(volume, _TD_WEEK)
    excess = (rvol5 - 2.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_WEEK)


# --- Group D (031-040): RVOL at multi-window highs ---

def vb_ext_031_rvol_21d_at_21d_high(volume: pd.Series) -> pd.Series:
    """Max RVOL(21) seen in trailing 21 days (21-day RVOL high)."""
    return _rolling_max(_rvol(volume, _TD_MON), _TD_MON)


def vb_ext_032_rvol_21d_at_63d_high(volume: pd.Series) -> pd.Series:
    """Max RVOL(21) seen in trailing 63 days (quarterly RVOL high)."""
    return _rolling_max(_rvol(volume, _TD_MON), _TD_QTR)


def vb_ext_033_rvol_21d_at_252d_high(volume: pd.Series) -> pd.Series:
    """Max RVOL(21) seen in trailing 252 days (annual RVOL high)."""
    return _rolling_max(_rvol(volume, _TD_MON), _TD_YEAR)


def vb_ext_034_rvol_5d_at_21d_high(volume: pd.Series) -> pd.Series:
    """Max RVOL(5) seen in trailing 21 days (monthly short-burst RVOL high)."""
    return _rolling_max(_rvol(volume, _TD_WEEK), _TD_MON)


def vb_ext_035_rvol_5d_at_63d_high(volume: pd.Series) -> pd.Series:
    """Max RVOL(5) seen in trailing 63 days (quarterly short-burst RVOL high)."""
    return _rolling_max(_rvol(volume, _TD_WEEK), _TD_QTR)


def vb_ext_036_current_rvol_21d_vs_21d_high(volume: pd.Series) -> pd.Series:
    """Current RVOL(21) / max RVOL(21) over trailing 21 days (proximity to recent high)."""
    r = _rvol(volume, _TD_MON)
    return _safe_div(r, _rolling_max(r, _TD_MON))


def vb_ext_037_current_rvol_21d_vs_63d_high(volume: pd.Series) -> pd.Series:
    """Current RVOL(21) / max RVOL(21) over trailing 63 days."""
    r = _rvol(volume, _TD_MON)
    return _safe_div(r, _rolling_max(r, _TD_QTR))


def vb_ext_038_current_rvol_21d_vs_252d_high(volume: pd.Series) -> pd.Series:
    """Current RVOL(21) / max RVOL(21) over trailing 252 days."""
    r = _rvol(volume, _TD_MON)
    return _safe_div(r, _rolling_max(r, _TD_YEAR))


def vb_ext_039_rvol_21d_pct_rank_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of RVOL(21) within trailing 63-day RVOL distribution."""
    r = _rvol(volume, _TD_MON)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vb_ext_040_rvol_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of RVOL(21) within trailing 252-day RVOL distribution."""
    r = _rvol(volume, _TD_MON)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): RVOL percentile ranks and streaks ---

def vb_ext_041_rvol_5d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of RVOL(5) within trailing 252-day distribution."""
    r = _rvol(volume, _TD_WEEK)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_ext_042_rvol_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of RVOL(252) — all-history RVOL extremity."""
    r = _rvol(volume, _TD_YEAR)
    return r.expanding(min_periods=5).rank(pct=True)


def vb_ext_043_rvol_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of RVOL(21) — all-history extremity on monthly RVOL."""
    r = _rvol(volume, _TD_MON)
    return r.expanding(min_periods=5).rank(pct=True)


def vb_ext_044_consec_elevated_rvol_5d_gt1(volume: pd.Series) -> pd.Series:
    """Consecutive days with RVOL(5) > 1.0 (above average volume streak)."""
    cond = _rvol(volume, _TD_WEEK) > 1.0
    return _consec_streak(cond)


def vb_ext_045_consec_elevated_rvol_21d_gt15(volume: pd.Series) -> pd.Series:
    """Consecutive days with RVOL(21) > 1.5 (elevated-volume streak vs 21d mean)."""
    cond = _rvol(volume, _TD_MON) > 1.5
    return _consec_streak(cond)


def vb_ext_046_consec_elevated_rvol_21d_gt2(volume: pd.Series) -> pd.Series:
    """Consecutive days with RVOL(21) > 2.0 (high-RVOL streak, mean baseline)."""
    cond = _rvol(volume, _TD_MON) > 2.0
    return _consec_streak(cond)


def vb_ext_047_consec_elevated_rvol_63d_gt15(volume: pd.Series) -> pd.Series:
    """Consecutive days with RVOL(63) > 1.5 (elevated-volume streak vs quarterly mean)."""
    cond = _rvol(volume, _TD_QTR) > 1.5
    return _consec_streak(cond)


def vb_ext_048_consec_elevated_rvol_252d_gt15(volume: pd.Series) -> pd.Series:
    """Consecutive days with RVOL(252) > 1.5 (elevated-volume streak vs annual mean)."""
    cond = _rvol(volume, _TD_YEAR) > 1.5
    return _consec_streak(cond)


def vb_ext_049_rvol_spike_count_gt15_21d(volume: pd.Series) -> pd.Series:
    """Count of days with RVOL(21) > 1.5 in trailing 21 days."""
    return _rolling_count_true(_rvol(volume, _TD_MON) > 1.5, _TD_MON)


def vb_ext_050_rvol_spike_count_gt15_63d(volume: pd.Series) -> pd.Series:
    """Count of days with RVOL(21) > 1.5 in trailing 63 days."""
    return _rolling_count_true(_rvol(volume, _TD_MON) > 1.5, _TD_QTR)


# --- Group F (051-060): Days-since-RVOL-spike ---

def vb_ext_051_days_since_rvol_5d_gt2(volume: pd.Series) -> pd.Series:
    """Days since last RVOL(5) > 2.0 event (inter-spike spacing, 5d baseline)."""
    flag = (_rvol(volume, _TD_WEEK) > 2.0).astype(float)
    not_spike = (flag == 0).astype(int)
    group = flag.cumsum()
    return not_spike.groupby(group).cumsum().astype(float)


def vb_ext_052_days_since_rvol_21d_gt15(volume: pd.Series) -> pd.Series:
    """Days since last RVOL(21) > 1.5 event."""
    flag = (_rvol(volume, _TD_MON) > 1.5).astype(float)
    not_spike = (flag == 0).astype(int)
    group = flag.cumsum()
    return not_spike.groupby(group).cumsum().astype(float)


def vb_ext_053_days_since_rvol_21d_gt2(volume: pd.Series) -> pd.Series:
    """Days since last RVOL(21) > 2.0 event (high-RVOL recency, mean baseline)."""
    flag = (_rvol(volume, _TD_MON) > 2.0).astype(float)
    not_spike = (flag == 0).astype(int)
    group = flag.cumsum()
    return not_spike.groupby(group).cumsum().astype(float)


def vb_ext_054_days_since_rvol_63d_gt15(volume: pd.Series) -> pd.Series:
    """Days since last RVOL(63) > 1.5 event (quarterly-baseline high-RVOL recency)."""
    flag = (_rvol(volume, _TD_QTR) > 1.5).astype(float)
    not_spike = (flag == 0).astype(int)
    group = flag.cumsum()
    return not_spike.groupby(group).cumsum().astype(float)


# --- Group G (055-062): Dollar-RVOL ---

def vb_ext_055_dollar_rvol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-RVOL(21): (close * volume) / rolling_mean(close * volume, 21d)."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_MON))


def vb_ext_056_dollar_rvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-RVOL(63): (close * volume) / rolling_mean(close * volume, 63d)."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_QTR))


def vb_ext_057_dollar_rvol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-RVOL(252): (close * volume) / rolling_mean(close * volume, 252d)."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_YEAR))


def vb_ext_058_dollar_rvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of dollar-RVOL(21) in trailing 252-day distribution."""
    dv = close * volume
    dr = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return dr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (059-065): Volume vs EWM baseline (RVOL-EWM) ---

def vb_ext_059_rvol_ewm_21d(volume: pd.Series) -> pd.Series:
    """Volume / EWM(span=21) baseline — exponentially-weighted RVOL(21)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_MON))


def vb_ext_060_rvol_ewm_63d(volume: pd.Series) -> pd.Series:
    """Volume / EWM(span=63) baseline — exponentially-weighted RVOL(63)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_QTR))


def vb_ext_061_rvol_ewm_252d(volume: pd.Series) -> pd.Series:
    """Volume / EWM(span=252) baseline — exponentially-weighted annual RVOL."""
    return _safe_div(volume, _ewm_mean(volume, _TD_YEAR))


def vb_ext_062_rvol_ewm_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """EWM-RVOL(5) / EWM-RVOL(252): short EWM ratio vs long EWM ratio (burst signal)."""
    return _safe_div(
        _safe_div(volume, _ewm_mean(volume, _TD_WEEK)),
        _safe_div(volume, _ewm_mean(volume, _TD_YEAR)),
    )


# --- Group I (063-068): Volume acceleration on spike days ---

def vb_ext_063_rvol_accel_5d(volume: pd.Series) -> pd.Series:
    """5-day first difference of RVOL(21) (acceleration/velocity of RVOL(21))."""
    return _rvol(volume, _TD_MON).diff(_TD_WEEK)


def vb_ext_064_rvol_accel_21d(volume: pd.Series) -> pd.Series:
    """21-day first difference of RVOL(21) (monthly rate of change of RVOL)."""
    return _rvol(volume, _TD_MON).diff(_TD_MON)


def vb_ext_065_rvol_5d_accel_on_rvol_gt15(volume: pd.Series) -> pd.Series:
    """5-day RVOL(21) change, masked to days where RVOL(21) > 1.5 (spike-day acceleration)."""
    r = _rvol(volume, _TD_MON)
    accel = r.diff(_TD_WEEK)
    return accel.where(r > 1.5, 0.0)


def vb_ext_066_rvol_acceleration_ewm21_5d(volume: pd.Series) -> pd.Series:
    """5-day diff of EWM-RVOL(21) (acceleration of exponentially-smoothed RVOL)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_MON)).diff(_TD_WEEK)


# --- Group J (067-071): RVOL on down days (capitulation blow-off) ---

def vb_ext_067_rvol_21d_mean_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean RVOL(21) on down-close days in trailing 21 days (capitulation signal)."""
    ret = close.pct_change(1)
    r = _rvol(volume, _TD_MON)
    r_dn = r.where(ret < 0, np.nan)
    return r_dn.rolling(_TD_MON, min_periods=1).mean()


def vb_ext_068_rvol_21d_mean_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean RVOL(21) on down-close days in trailing 63 days."""
    ret = close.pct_change(1)
    r = _rvol(volume, _TD_MON)
    r_dn = r.where(ret < 0, np.nan)
    return r_dn.rolling(_TD_QTR, min_periods=1).mean()


def vb_ext_069_rvol_spike_gt15_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of RVOL(21) > 1.5 events on down days in trailing 63 days."""
    ret = close.pct_change(1)
    cond = ((_rvol(volume, _TD_MON) > 1.5) & (ret < 0)).astype(float)
    return _rolling_count_true(cond > 0, _TD_QTR)


def vb_ext_070_rvol_capitulation_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of RVOL(21) on down days only, over 21 days (capitulation RVOL energy)."""
    ret = close.pct_change(1)
    r = _rvol(volume, _TD_MON)
    r_dn = r.where(ret < 0, 0.0)
    return _rolling_sum(r_dn, _TD_MON)


def vb_ext_071_rvol_down_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean RVOL(21) on down days / mean RVOL(21) on up days over 63 days."""
    ret = close.pct_change(1)
    r = _rvol(volume, _TD_MON)
    dn = r.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up = r.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(dn, up)


# --- Group K (072-075): Blow-off / dryup sequences and clustering ---

def vb_ext_072_rvol_blowoff_then_dryup_5d(volume: pd.Series) -> pd.Series:
    """Blow-off-then-dryup: max RVOL(21) last 5d * (1 - current RVOL(21)) clipped at 0.
    Captures a recent spike followed by today being below average (dryup)."""
    r = _rvol(volume, _TD_MON)
    max5 = _rolling_max(r, _TD_WEEK)
    dryup = (1.0 - r).clip(lower=0.0)
    return max5 * dryup


def vb_ext_073_rvol_spike_cluster_count_3d_window_21d(volume: pd.Series) -> pd.Series:
    """Count of 3-day windows (within trailing 21d) containing at least one RVOL(21)>1.5.
    Proxy for volume-spike clustering density at the 3-day granularity."""
    flag = (_rvol(volume, _TD_MON) > 1.5).astype(float)
    has_spike_3d = flag.rolling(3, min_periods=1).max()
    return _rolling_sum(has_spike_3d, _TD_MON)


def vb_ext_074_rvol_roc_5d_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of 5-day rate-of-change of RVOL(21) vs its 63-day distribution."""
    roc = _rvol(volume, _TD_MON).diff(_TD_WEEK)
    m = _rolling_mean(roc, _TD_QTR)
    s = _rolling_std(roc, _TD_QTR)
    return _safe_div(roc - m, s)


def vb_ext_075_rvol_21d_gt2_flag_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of RVOL(21)-spike flag (RVOL > 2.0, mean baseline) count over 21d
    within trailing 252-day distribution — combines RVOL threshold with rank."""
    flag = (_rvol(volume, _TD_MON) > 2.0).astype(float)
    cnt21 = _rolling_count_true(flag > 0, _TD_MON)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_BLOWOFF_EXTENDED_REGISTRY_001_075 = {
    "vb_ext_001_rvol_5d": {"inputs": ["volume"], "func": vb_ext_001_rvol_5d},
    "vb_ext_002_rvol_10d": {"inputs": ["volume"], "func": vb_ext_002_rvol_10d},
    "vb_ext_003_rvol_21d": {"inputs": ["volume"], "func": vb_ext_003_rvol_21d},
    "vb_ext_004_rvol_63d": {"inputs": ["volume"], "func": vb_ext_004_rvol_63d},
    "vb_ext_005_rvol_252d": {"inputs": ["volume"], "func": vb_ext_005_rvol_252d},
    "vb_ext_006_rvol_median_5d": {"inputs": ["volume"], "func": vb_ext_006_rvol_median_5d},
    "vb_ext_007_rvol_median_10d": {"inputs": ["volume"], "func": vb_ext_007_rvol_median_10d},
    "vb_ext_008_rvol_median_63d": {"inputs": ["volume"], "func": vb_ext_008_rvol_median_63d},
    "vb_ext_009_rvol_median_252d": {"inputs": ["volume"], "func": vb_ext_009_rvol_median_252d},
    "vb_ext_010_log_rvol_5d": {"inputs": ["volume"], "func": vb_ext_010_log_rvol_5d},
    "vb_ext_011_log_rvol_21d": {"inputs": ["volume"], "func": vb_ext_011_log_rvol_21d},
    "vb_ext_012_log_rvol_63d": {"inputs": ["volume"], "func": vb_ext_012_log_rvol_63d},
    "vb_ext_013_log_rvol_252d": {"inputs": ["volume"], "func": vb_ext_013_log_rvol_252d},
    "vb_ext_014_rvol_5d_vs_252d": {"inputs": ["volume"], "func": vb_ext_014_rvol_5d_vs_252d},
    "vb_ext_015_rvol_21d_vs_252d": {"inputs": ["volume"], "func": vb_ext_015_rvol_21d_vs_252d},
    "vb_ext_016_rvol_zscore_21d_baseline": {"inputs": ["volume"], "func": vb_ext_016_rvol_zscore_21d_baseline},
    "vb_ext_017_rvol_zscore_63d_baseline": {"inputs": ["volume"], "func": vb_ext_017_rvol_zscore_63d_baseline},
    "vb_ext_018_rvol_zscore_5d_baseline": {"inputs": ["volume"], "func": vb_ext_018_rvol_zscore_5d_baseline},
    "vb_ext_019_rvol_zscore_252d_baseline": {"inputs": ["volume"], "func": vb_ext_019_rvol_zscore_252d_baseline},
    "vb_ext_020_rvol_median_zscore_21d": {"inputs": ["volume"], "func": vb_ext_020_rvol_median_zscore_21d},
    "vb_ext_021_cumrvol_5d": {"inputs": ["volume"], "func": vb_ext_021_cumrvol_5d},
    "vb_ext_022_cumrvol_10d": {"inputs": ["volume"], "func": vb_ext_022_cumrvol_10d},
    "vb_ext_023_cumrvol_21d": {"inputs": ["volume"], "func": vb_ext_023_cumrvol_21d},
    "vb_ext_024_cumrvol_5d_norm_252d": {"inputs": ["volume"], "func": vb_ext_024_cumrvol_5d_norm_252d},
    "vb_ext_025_cumrvol_10d_norm_252d": {"inputs": ["volume"], "func": vb_ext_025_cumrvol_10d_norm_252d},
    "vb_ext_026_cumrvol_median_5d": {"inputs": ["volume"], "func": vb_ext_026_cumrvol_median_5d},
    "vb_ext_027_cumrvol_excess_above_1_5d": {"inputs": ["volume"], "func": vb_ext_027_cumrvol_excess_above_1_5d},
    "vb_ext_028_cumrvol_excess_above_1_21d": {"inputs": ["volume"], "func": vb_ext_028_cumrvol_excess_above_1_21d},
    "vb_ext_029_cumrvol_excess_above_15_21d": {"inputs": ["volume"], "func": vb_ext_029_cumrvol_excess_above_15_21d},
    "vb_ext_030_cumrvol_excess_above_2_5d": {"inputs": ["volume"], "func": vb_ext_030_cumrvol_excess_above_2_5d},
    "vb_ext_031_rvol_21d_at_21d_high": {"inputs": ["volume"], "func": vb_ext_031_rvol_21d_at_21d_high},
    "vb_ext_032_rvol_21d_at_63d_high": {"inputs": ["volume"], "func": vb_ext_032_rvol_21d_at_63d_high},
    "vb_ext_033_rvol_21d_at_252d_high": {"inputs": ["volume"], "func": vb_ext_033_rvol_21d_at_252d_high},
    "vb_ext_034_rvol_5d_at_21d_high": {"inputs": ["volume"], "func": vb_ext_034_rvol_5d_at_21d_high},
    "vb_ext_035_rvol_5d_at_63d_high": {"inputs": ["volume"], "func": vb_ext_035_rvol_5d_at_63d_high},
    "vb_ext_036_current_rvol_21d_vs_21d_high": {"inputs": ["volume"], "func": vb_ext_036_current_rvol_21d_vs_21d_high},
    "vb_ext_037_current_rvol_21d_vs_63d_high": {"inputs": ["volume"], "func": vb_ext_037_current_rvol_21d_vs_63d_high},
    "vb_ext_038_current_rvol_21d_vs_252d_high": {"inputs": ["volume"], "func": vb_ext_038_current_rvol_21d_vs_252d_high},
    "vb_ext_039_rvol_21d_pct_rank_63d": {"inputs": ["volume"], "func": vb_ext_039_rvol_21d_pct_rank_63d},
    "vb_ext_040_rvol_21d_pct_rank_252d": {"inputs": ["volume"], "func": vb_ext_040_rvol_21d_pct_rank_252d},
    "vb_ext_041_rvol_5d_pct_rank_252d": {"inputs": ["volume"], "func": vb_ext_041_rvol_5d_pct_rank_252d},
    "vb_ext_042_rvol_252d_expanding_rank": {"inputs": ["volume"], "func": vb_ext_042_rvol_252d_expanding_rank},
    "vb_ext_043_rvol_21d_expanding_rank": {"inputs": ["volume"], "func": vb_ext_043_rvol_21d_expanding_rank},
    "vb_ext_044_consec_elevated_rvol_5d_gt1": {"inputs": ["volume"], "func": vb_ext_044_consec_elevated_rvol_5d_gt1},
    "vb_ext_045_consec_elevated_rvol_21d_gt15": {"inputs": ["volume"], "func": vb_ext_045_consec_elevated_rvol_21d_gt15},
    "vb_ext_046_consec_elevated_rvol_21d_gt2": {"inputs": ["volume"], "func": vb_ext_046_consec_elevated_rvol_21d_gt2},
    "vb_ext_047_consec_elevated_rvol_63d_gt15": {"inputs": ["volume"], "func": vb_ext_047_consec_elevated_rvol_63d_gt15},
    "vb_ext_048_consec_elevated_rvol_252d_gt15": {"inputs": ["volume"], "func": vb_ext_048_consec_elevated_rvol_252d_gt15},
    "vb_ext_049_rvol_spike_count_gt15_21d": {"inputs": ["volume"], "func": vb_ext_049_rvol_spike_count_gt15_21d},
    "vb_ext_050_rvol_spike_count_gt15_63d": {"inputs": ["volume"], "func": vb_ext_050_rvol_spike_count_gt15_63d},
    "vb_ext_051_days_since_rvol_5d_gt2": {"inputs": ["volume"], "func": vb_ext_051_days_since_rvol_5d_gt2},
    "vb_ext_052_days_since_rvol_21d_gt15": {"inputs": ["volume"], "func": vb_ext_052_days_since_rvol_21d_gt15},
    "vb_ext_053_days_since_rvol_21d_gt2": {"inputs": ["volume"], "func": vb_ext_053_days_since_rvol_21d_gt2},
    "vb_ext_054_days_since_rvol_63d_gt15": {"inputs": ["volume"], "func": vb_ext_054_days_since_rvol_63d_gt15},
    "vb_ext_055_dollar_rvol_21d": {"inputs": ["close", "volume"], "func": vb_ext_055_dollar_rvol_21d},
    "vb_ext_056_dollar_rvol_63d": {"inputs": ["close", "volume"], "func": vb_ext_056_dollar_rvol_63d},
    "vb_ext_057_dollar_rvol_252d": {"inputs": ["close", "volume"], "func": vb_ext_057_dollar_rvol_252d},
    "vb_ext_058_dollar_rvol_pct_rank_252d": {"inputs": ["close", "volume"], "func": vb_ext_058_dollar_rvol_pct_rank_252d},
    "vb_ext_059_rvol_ewm_21d": {"inputs": ["volume"], "func": vb_ext_059_rvol_ewm_21d},
    "vb_ext_060_rvol_ewm_63d": {"inputs": ["volume"], "func": vb_ext_060_rvol_ewm_63d},
    "vb_ext_061_rvol_ewm_252d": {"inputs": ["volume"], "func": vb_ext_061_rvol_ewm_252d},
    "vb_ext_062_rvol_ewm_5d_vs_252d": {"inputs": ["volume"], "func": vb_ext_062_rvol_ewm_5d_vs_252d},
    "vb_ext_063_rvol_accel_5d": {"inputs": ["volume"], "func": vb_ext_063_rvol_accel_5d},
    "vb_ext_064_rvol_accel_21d": {"inputs": ["volume"], "func": vb_ext_064_rvol_accel_21d},
    "vb_ext_065_rvol_5d_accel_on_rvol_gt15": {"inputs": ["volume"], "func": vb_ext_065_rvol_5d_accel_on_rvol_gt15},
    "vb_ext_066_rvol_acceleration_ewm21_5d": {"inputs": ["volume"], "func": vb_ext_066_rvol_acceleration_ewm21_5d},
    "vb_ext_067_rvol_21d_mean_on_down_days_21d": {"inputs": ["close", "volume"], "func": vb_ext_067_rvol_21d_mean_on_down_days_21d},
    "vb_ext_068_rvol_21d_mean_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_ext_068_rvol_21d_mean_on_down_days_63d},
    "vb_ext_069_rvol_spike_gt15_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_ext_069_rvol_spike_gt15_on_down_days_63d},
    "vb_ext_070_rvol_capitulation_score_21d": {"inputs": ["close", "volume"], "func": vb_ext_070_rvol_capitulation_score_21d},
    "vb_ext_071_rvol_down_up_ratio_63d": {"inputs": ["close", "volume"], "func": vb_ext_071_rvol_down_up_ratio_63d},
    "vb_ext_072_rvol_blowoff_then_dryup_5d": {"inputs": ["volume"], "func": vb_ext_072_rvol_blowoff_then_dryup_5d},
    "vb_ext_073_rvol_spike_cluster_count_3d_window_21d": {"inputs": ["volume"], "func": vb_ext_073_rvol_spike_cluster_count_3d_window_21d},
    "vb_ext_074_rvol_roc_5d_zscore_63d": {"inputs": ["volume"], "func": vb_ext_074_rvol_roc_5d_zscore_63d},
    "vb_ext_075_rvol_21d_gt2_flag_pct_rank_252d": {"inputs": ["volume"], "func": vb_ext_075_rvol_21d_gt2_flag_pct_rank_252d},
}
