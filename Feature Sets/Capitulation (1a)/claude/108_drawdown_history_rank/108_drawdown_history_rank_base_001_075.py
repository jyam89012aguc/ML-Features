"""
108_drawdown_history_rank — Base Features 001-075
Domain: current drawdown ranked against the ticker's own history —
        expanding/rolling percentile rank of drawdown depth and duration vs
        all prior drawdowns, worst-ever and worst-in-N-years flags, current
        drawdown vs ticker's historical max/median drawdown.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _expanding_max(s: pd.Series) -> pd.Series:
    """Expanding all-time maximum, min_periods=1."""
    return s.expanding(min_periods=1).max()


def _drawdown_from_expanding_peak(close: pd.Series) -> pd.Series:
    """Current drawdown as a fraction: (close - expanding_peak) / expanding_peak.
    Values are <= 0; 0 = at all-time high, -1 = total loss.
    """
    peak = _expanding_max(close)
    return _safe_div(close - peak, peak)


def _drawdown_depth_pct(close: pd.Series) -> pd.Series:
    """Absolute drawdown depth in percent (positive number).
    depth = (peak - close) / peak  >=  0.
    """
    peak = _expanding_max(close)
    return _safe_div(peak - close, peak.clip(lower=_EPS))


def _rolling_drawdown_from_peak(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from the rolling w-day high (fraction, >=0)."""
    roll_peak = _rolling_max(close, w)
    return _safe_div(roll_peak - close, roll_peak.clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw current drawdown depth at multiple windows ---

def dhr_001_expanding_drawdown_depth(close: pd.Series) -> pd.Series:
    """Current drawdown depth from the all-time expanding peak (fraction >=0)."""
    return _drawdown_depth_pct(close)


def dhr_002_drawdown_from_peak_252d(close: pd.Series) -> pd.Series:
    """Drawdown from 252-day rolling peak (1-year high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, _TD_YEAR)


def dhr_003_drawdown_from_peak_126d(close: pd.Series) -> pd.Series:
    """Drawdown from 126-day rolling peak (half-year high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, _TD_HALF)


def dhr_004_drawdown_from_peak_63d(close: pd.Series) -> pd.Series:
    """Drawdown from 63-day rolling peak (quarterly high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, _TD_QTR)


def dhr_005_drawdown_from_peak_21d(close: pd.Series) -> pd.Series:
    """Drawdown from 21-day rolling peak (monthly high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, _TD_MON)


def dhr_006_drawdown_from_peak_504d(close: pd.Series) -> pd.Series:
    """Drawdown from 504-day rolling peak (2-year high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, 504)


def dhr_007_drawdown_from_peak_756d(close: pd.Series) -> pd.Series:
    """Drawdown from 756-day rolling peak (3-year high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, 756)


def dhr_008_drawdown_from_peak_1260d(close: pd.Series) -> pd.Series:
    """Drawdown from 1260-day rolling peak (5-year high) — fraction >=0."""
    return _rolling_drawdown_from_peak(close, 1260)


def dhr_009_drawdown_signed_expanding(close: pd.Series) -> pd.Series:
    """Signed drawdown from expanding peak: (close-peak)/peak, <=0 at drawdown."""
    return _drawdown_from_expanding_peak(close)


def dhr_010_drawdown_log_expanding(close: pd.Series) -> pd.Series:
    """Log-scale drawdown from expanding peak: log(close/peak), <=0."""
    peak = _expanding_max(close)
    ratio = _safe_div(close, peak.clip(lower=_EPS))
    return np.log(ratio.clip(lower=_EPS))


# --- Group B (011-020): Expanding percentile rank of current drawdown depth ---

def dhr_011_expanding_pctrank_dd_depth(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of the current drawdown depth vs all prior depths.
    0 = least severe ever, 1 = worst ever (tied).
    """
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_012_rolling_pctrank_dd_depth_252d(close: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of drawdown depth vs trailing year."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_013_rolling_pctrank_dd_depth_504d(close: pd.Series) -> pd.Series:
    """504-day rolling percentile rank of drawdown depth vs trailing 2 years."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_014_rolling_pctrank_dd_depth_756d(close: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of drawdown depth vs trailing 3 years."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(756, min_periods=504).rank(pct=True)


def dhr_015_rolling_pctrank_dd_depth_1260d(close: pd.Series) -> pd.Series:
    """1260-day rolling percentile rank of drawdown depth vs trailing 5 years."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(1260, min_periods=756).rank(pct=True)


def dhr_016_rolling_pctrank_dd_depth_126d(close: pd.Series) -> pd.Series:
    """126-day rolling percentile rank of drawdown depth vs trailing half-year."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def dhr_017_rolling_pctrank_dd_depth_63d(close: pd.Series) -> pd.Series:
    """63-day rolling percentile rank of drawdown depth vs trailing quarter."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def dhr_018_expanding_zscore_dd_depth(close: pd.Series) -> pd.Series:
    """Expanding z-score of current drawdown depth relative to all-history distribution."""
    depth = _drawdown_depth_pct(close)
    m = depth.expanding(min_periods=2).mean()
    s = depth.expanding(min_periods=2).std()
    return _safe_div(depth - m, s)


def dhr_019_rolling_zscore_dd_depth_252d(close: pd.Series) -> pd.Series:
    """252-day rolling z-score of current drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def dhr_020_rolling_zscore_dd_depth_504d(close: pd.Series) -> pd.Series:
    """504-day rolling z-score of current drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = _rolling_mean(depth, 504)
    s = _rolling_std(depth, 504)
    return _safe_div(depth - m, s)


# --- Group C (021-030): Worst-ever and worst-in-N-years flags ---

def dhr_021_is_worst_ever_dd_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth equals the all-time maximum drawdown depth."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max()
    return (depth >= max_ever - _EPS).astype(float)


def dhr_022_is_worst_1yr_dd_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is the worst in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    prev_max = depth.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (depth >= prev_max.fillna(0) - _EPS).astype(float)


def dhr_023_is_worst_2yr_dd_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is the worst in trailing 504 days."""
    depth = _drawdown_depth_pct(close)
    prev_max = depth.shift(1).rolling(504, min_periods=1).max()
    return (depth >= prev_max.fillna(0) - _EPS).astype(float)


def dhr_024_is_worst_3yr_dd_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is the worst in trailing 756 days."""
    depth = _drawdown_depth_pct(close)
    prev_max = depth.shift(1).rolling(756, min_periods=1).max()
    return (depth >= prev_max.fillna(0) - _EPS).astype(float)


def dhr_025_is_worst_5yr_dd_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is the worst in trailing 1260 days."""
    depth = _drawdown_depth_pct(close)
    prev_max = depth.shift(1).rolling(1260, min_periods=1).max()
    return (depth >= prev_max.fillna(0) - _EPS).astype(float)


def dhr_026_is_top10pct_worst_ever_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth ranks in the top 10% worst expanding all-time."""
    depth = _drawdown_depth_pct(close)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    return (pct >= 0.90).astype(float)


def dhr_027_is_top10pct_worst_1yr_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown is in the top 10% worst of the trailing year."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (pct >= 0.90).astype(float)


def dhr_028_is_top10pct_worst_2yr_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown is in the top 10% worst of the trailing 2 years."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(504, min_periods=_TD_YEAR).rank(pct=True)
    return (pct >= 0.90).astype(float)


def dhr_029_is_top5pct_worst_ever_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown ranks in the top 5% worst expanding all-time."""
    depth = _drawdown_depth_pct(close)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    return (pct >= 0.95).astype(float)


def dhr_030_new_low_vs_prior_dd_max_252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds the prior-year maximum drawdown depth."""
    depth = _drawdown_depth_pct(close)
    prior_max = depth.shift(1).rolling(_TD_YEAR, min_periods=1).max().fillna(0)
    return (depth > prior_max).astype(float)


# --- Group D (031-040): Current vs historical max/median drawdown ---

def dhr_031_dd_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown as fraction of all-time max drawdown (1.0 = matching worst ever)."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(depth, max_ever)


def dhr_032_dd_vs_expanding_median_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown depth vs expanding median drawdown (how unusual is this drawdown)."""
    depth = _drawdown_depth_pct(close)
    med = depth.expanding(min_periods=2).median()
    return _safe_div(depth, med.clip(lower=_EPS))


def dhr_033_dd_vs_rolling_max_252d_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown vs 252-day rolling maximum drawdown ratio."""
    depth = _drawdown_depth_pct(close)
    max_1yr = _rolling_max(depth, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(depth, max_1yr)


def dhr_034_dd_vs_rolling_max_504d_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown vs 504-day rolling maximum drawdown ratio."""
    depth = _drawdown_depth_pct(close)
    max_2yr = _rolling_max(depth, 504).clip(lower=_EPS)
    return _safe_div(depth, max_2yr)


def dhr_035_dd_vs_rolling_mean_252d_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown depth vs 252-day rolling mean drawdown."""
    depth = _drawdown_depth_pct(close)
    mean_1yr = _rolling_mean(depth, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(depth, mean_1yr)


def dhr_036_dd_vs_rolling_mean_504d_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown depth vs 504-day rolling mean drawdown."""
    depth = _drawdown_depth_pct(close)
    mean_2yr = _rolling_mean(depth, 504).clip(lower=_EPS)
    return _safe_div(depth, mean_2yr)


def dhr_037_dd_excess_over_expanding_median(close: pd.Series) -> pd.Series:
    """Excess of current drawdown over expanding median drawdown (absolute, clipped to 0)."""
    depth = _drawdown_depth_pct(close)
    med = depth.expanding(min_periods=2).median()
    return (depth - med).clip(lower=0.0)


def dhr_038_dd_excess_over_expanding_75pct(close: pd.Series) -> pd.Series:
    """Excess of current drawdown over the expanding 75th-percentile drawdown."""
    depth = _drawdown_depth_pct(close)
    q75 = depth.expanding(min_periods=4).quantile(0.75)
    return (depth - q75).clip(lower=0.0)


def dhr_039_dd_excess_over_expanding_90pct(close: pd.Series) -> pd.Series:
    """Excess of current drawdown over the expanding 90th-percentile drawdown."""
    depth = _drawdown_depth_pct(close)
    q90 = depth.expanding(min_periods=10).quantile(0.90)
    return (depth - q90).clip(lower=0.0)


def dhr_040_dd_distance_from_expanding_max(close: pd.Series) -> pd.Series:
    """Distance between current drawdown and all-time worst drawdown (how close to record)."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max()
    return max_ever - depth


# --- Group E (041-050): Drawdown duration ranked against history ---

def dhr_041_current_dd_duration(close: pd.Series) -> pd.Series:
    """Days elapsed since the current drawdown began (since last all-time high)."""
    depth = _drawdown_depth_pct(close)
    at_high = (depth < _EPS).astype(int)
    group = at_high.cumsum()
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_high_idx = idx.where(at_high == 1).ffill().fillna(0)
    duration = idx - last_high_idx
    return duration.where(depth >= _EPS, 0.0)


def dhr_042_expanding_pctrank_dd_duration(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of current drawdown duration vs all-history durations."""
    dur = dhr_041_current_dd_duration(close)
    return dur.expanding(min_periods=2).rank(pct=True)


def dhr_043_rolling_pctrank_dd_duration_252d(close: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of current drawdown duration."""
    dur = dhr_041_current_dd_duration(close)
    return dur.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_044_rolling_pctrank_dd_duration_504d(close: pd.Series) -> pd.Series:
    """504-day rolling percentile rank of current drawdown duration."""
    dur = dhr_041_current_dd_duration(close)
    return dur.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_045_dd_duration_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown duration as fraction of the all-time longest drawdown duration."""
    dur = dhr_041_current_dd_duration(close)
    max_ever = dur.expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(dur, max_ever)


def dhr_046_dd_duration_vs_expanding_median_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown duration vs expanding median drawdown duration."""
    dur = dhr_041_current_dd_duration(close)
    med = dur.expanding(min_periods=2).median().clip(lower=_EPS)
    return _safe_div(dur, med)


def dhr_047_dd_duration_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of current drawdown duration relative to all-history."""
    dur = dhr_041_current_dd_duration(close)
    m = dur.expanding(min_periods=2).mean()
    s = dur.expanding(min_periods=2).std()
    return _safe_div(dur - m, s)


def dhr_048_dd_duration_rolling_zscore_252d(close: pd.Series) -> pd.Series:
    """252-day rolling z-score of current drawdown duration."""
    dur = dhr_041_current_dd_duration(close)
    m = _rolling_mean(dur, _TD_YEAR)
    s = _rolling_std(dur, _TD_YEAR)
    return _safe_div(dur - m, s)


def dhr_049_dd_duration_above_expanding_median_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown duration exceeds the expanding median duration."""
    dur = dhr_041_current_dd_duration(close)
    med = dur.expanding(min_periods=2).median()
    return (dur > med).astype(float)


def dhr_050_dd_duration_above_252d_max_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current duration exceeds the prior 252-day maximum duration."""
    dur = dhr_041_current_dd_duration(close)
    prior_max = dur.shift(1).rolling(_TD_YEAR, min_periods=1).max().fillna(0)
    return (dur > prior_max).astype(float)


# --- Group F (051-060): Combined depth+duration distress score vs history ---

def dhr_051_dd_depth_x_duration_raw(close: pd.Series) -> pd.Series:
    """Raw product of drawdown depth fraction and duration (days). Distress area."""
    depth = _drawdown_depth_pct(close)
    dur = dhr_041_current_dd_duration(close)
    return depth * dur


def dhr_052_expanding_pctrank_depth_x_duration(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of depth×duration product vs all history."""
    score = dhr_051_dd_depth_x_duration_raw(close)
    return score.expanding(min_periods=2).rank(pct=True)


def dhr_053_rolling_pctrank_depth_x_duration_252d(close: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of depth×duration product."""
    score = dhr_051_dd_depth_x_duration_raw(close)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_054_rolling_pctrank_depth_x_duration_504d(close: pd.Series) -> pd.Series:
    """504-day rolling percentile rank of depth×duration product."""
    score = dhr_051_dd_depth_x_duration_raw(close)
    return score.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_055_dd_composite_distress_score(close: pd.Series) -> pd.Series:
    """Composite: expanding pct-rank(depth) + expanding pct-rank(duration), 0-2 scale."""
    depth = _drawdown_depth_pct(close)
    dur = dhr_041_current_dd_duration(close)
    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    return r_depth + r_dur


def dhr_056_dd_composite_distress_pctrank_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of the composite distress score (depth+duration ranks)."""
    score = dhr_055_dd_composite_distress_score(close)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_057_dd_depth_expanding_75pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is in expanding top 25% (>=75th pct)."""
    depth = _drawdown_depth_pct(close)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    return (pct >= 0.75).astype(float)


def dhr_058_dd_depth_expanding_95pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is in expanding top 5% (>=95th pct)."""
    depth = _drawdown_depth_pct(close)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    return (pct >= 0.95).astype(float)


def dhr_059_dd_duration_expanding_75pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown duration is in expanding top 25% longest."""
    dur = dhr_041_current_dd_duration(close)
    pct = dur.expanding(min_periods=2).rank(pct=True)
    return (pct >= 0.75).astype(float)


def dhr_060_dd_both_depth_and_duration_top25pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: BOTH depth AND duration are in the expanding top 25% simultaneously."""
    depth = _drawdown_depth_pct(close)
    dur = dhr_041_current_dd_duration(close)
    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    return ((r_depth >= 0.75) & (r_dur >= 0.75)).astype(float)


# --- Group G (061-075): Multi-window depth comparisons and additional rank variants ---

def dhr_061_dd_depth_252d_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """252-day drawdown depth vs all-time max drawdown depth ratio."""
    dd_1yr = _rolling_drawdown_from_peak(close, _TD_YEAR)
    max_ever = _drawdown_depth_pct(close).expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(dd_1yr, max_ever)


def dhr_062_dd_depth_63d_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """63-day drawdown depth vs all-time max drawdown depth ratio."""
    dd_qtr = _rolling_drawdown_from_peak(close, _TD_QTR)
    max_ever = _drawdown_depth_pct(close).expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(dd_qtr, max_ever)


def dhr_063_dd_depth_21d_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """21-day drawdown depth vs all-time max drawdown depth ratio."""
    dd_mon = _rolling_drawdown_from_peak(close, _TD_MON)
    max_ever = _drawdown_depth_pct(close).expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(dd_mon, max_ever)


def dhr_064_rolling_max_dd_252d(close: pd.Series) -> pd.Series:
    """Rolling maximum drawdown depth achieved in the trailing 252-day window."""
    depth = _drawdown_depth_pct(close)
    return _rolling_max(depth, _TD_YEAR)


def dhr_065_rolling_max_dd_504d(close: pd.Series) -> pd.Series:
    """Rolling maximum drawdown depth achieved in the trailing 504-day window."""
    depth = _drawdown_depth_pct(close)
    return _rolling_max(depth, 504)


def dhr_066_rolling_max_dd_756d(close: pd.Series) -> pd.Series:
    """Rolling maximum drawdown depth achieved in the trailing 756-day window."""
    depth = _drawdown_depth_pct(close)
    return _rolling_max(depth, 756)


def dhr_067_expanding_max_dd(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum drawdown depth (worst ever seen)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=1).max()


def dhr_068_expanding_median_dd(close: pd.Series) -> pd.Series:
    """Expanding median drawdown depth (typical historical drawdown level)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=2).median()


def dhr_069_expanding_90pct_dd(close: pd.Series) -> pd.Series:
    """Expanding 90th-percentile drawdown depth (upper tail of historical drawdowns)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=10).quantile(0.90)


def dhr_070_expanding_75pct_dd(close: pd.Series) -> pd.Series:
    """Expanding 75th-percentile drawdown depth."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=4).quantile(0.75)


def dhr_071_dd_depth_above_expanding_90pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds the expanding 90th percentile."""
    depth = _drawdown_depth_pct(close)
    q90 = depth.expanding(min_periods=10).quantile(0.90)
    return (depth >= q90 - _EPS).astype(float)


def dhr_072_rolling_pctrank_dd_depth_756d(close: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of current drawdown depth (3-year context)."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(756, min_periods=504).rank(pct=True)


def dhr_073_dd_depth_vs_rolling_90pct_252d_excess(close: pd.Series) -> pd.Series:
    """Excess of current drawdown over the 252-day trailing 90th-pct drawdown, clipped to 0."""
    depth = _drawdown_depth_pct(close)
    q90_252d = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (depth - q90_252d).clip(lower=0.0)


def dhr_074_dd_depth_normalised_by_expanding_std(close: pd.Series) -> pd.Series:
    """Current drawdown depth normalized by expanding standard deviation of drawdown depths."""
    depth = _drawdown_depth_pct(close)
    s = depth.expanding(min_periods=2).std().clip(lower=_EPS)
    return _safe_div(depth, s)


def dhr_075_dd_depth_vs_expanding_mean_excess(close: pd.Series) -> pd.Series:
    """Excess of current drawdown depth over the expanding mean, clipped to 0."""
    depth = _drawdown_depth_pct(close)
    m = depth.expanding(min_periods=2).mean()
    return (depth - m).clip(lower=0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_HISTORY_RANK_REGISTRY_001_075 = {
    "dhr_001_expanding_drawdown_depth": {"inputs": ["close"], "func": dhr_001_expanding_drawdown_depth},
    "dhr_002_drawdown_from_peak_252d": {"inputs": ["close"], "func": dhr_002_drawdown_from_peak_252d},
    "dhr_003_drawdown_from_peak_126d": {"inputs": ["close"], "func": dhr_003_drawdown_from_peak_126d},
    "dhr_004_drawdown_from_peak_63d": {"inputs": ["close"], "func": dhr_004_drawdown_from_peak_63d},
    "dhr_005_drawdown_from_peak_21d": {"inputs": ["close"], "func": dhr_005_drawdown_from_peak_21d},
    "dhr_006_drawdown_from_peak_504d": {"inputs": ["close"], "func": dhr_006_drawdown_from_peak_504d},
    "dhr_007_drawdown_from_peak_756d": {"inputs": ["close"], "func": dhr_007_drawdown_from_peak_756d},
    "dhr_008_drawdown_from_peak_1260d": {"inputs": ["close"], "func": dhr_008_drawdown_from_peak_1260d},
    "dhr_009_drawdown_signed_expanding": {"inputs": ["close"], "func": dhr_009_drawdown_signed_expanding},
    "dhr_010_drawdown_log_expanding": {"inputs": ["close"], "func": dhr_010_drawdown_log_expanding},
    "dhr_011_expanding_pctrank_dd_depth": {"inputs": ["close"], "func": dhr_011_expanding_pctrank_dd_depth},
    "dhr_012_rolling_pctrank_dd_depth_252d": {"inputs": ["close"], "func": dhr_012_rolling_pctrank_dd_depth_252d},
    "dhr_013_rolling_pctrank_dd_depth_504d": {"inputs": ["close"], "func": dhr_013_rolling_pctrank_dd_depth_504d},
    "dhr_014_rolling_pctrank_dd_depth_756d": {"inputs": ["close"], "func": dhr_014_rolling_pctrank_dd_depth_756d},
    "dhr_015_rolling_pctrank_dd_depth_1260d": {"inputs": ["close"], "func": dhr_015_rolling_pctrank_dd_depth_1260d},
    "dhr_016_rolling_pctrank_dd_depth_126d": {"inputs": ["close"], "func": dhr_016_rolling_pctrank_dd_depth_126d},
    "dhr_017_rolling_pctrank_dd_depth_63d": {"inputs": ["close"], "func": dhr_017_rolling_pctrank_dd_depth_63d},
    "dhr_018_expanding_zscore_dd_depth": {"inputs": ["close"], "func": dhr_018_expanding_zscore_dd_depth},
    "dhr_019_rolling_zscore_dd_depth_252d": {"inputs": ["close"], "func": dhr_019_rolling_zscore_dd_depth_252d},
    "dhr_020_rolling_zscore_dd_depth_504d": {"inputs": ["close"], "func": dhr_020_rolling_zscore_dd_depth_504d},
    "dhr_021_is_worst_ever_dd_flag": {"inputs": ["close"], "func": dhr_021_is_worst_ever_dd_flag},
    "dhr_022_is_worst_1yr_dd_flag": {"inputs": ["close"], "func": dhr_022_is_worst_1yr_dd_flag},
    "dhr_023_is_worst_2yr_dd_flag": {"inputs": ["close"], "func": dhr_023_is_worst_2yr_dd_flag},
    "dhr_024_is_worst_3yr_dd_flag": {"inputs": ["close"], "func": dhr_024_is_worst_3yr_dd_flag},
    "dhr_025_is_worst_5yr_dd_flag": {"inputs": ["close"], "func": dhr_025_is_worst_5yr_dd_flag},
    "dhr_026_is_top10pct_worst_ever_flag": {"inputs": ["close"], "func": dhr_026_is_top10pct_worst_ever_flag},
    "dhr_027_is_top10pct_worst_1yr_flag": {"inputs": ["close"], "func": dhr_027_is_top10pct_worst_1yr_flag},
    "dhr_028_is_top10pct_worst_2yr_flag": {"inputs": ["close"], "func": dhr_028_is_top10pct_worst_2yr_flag},
    "dhr_029_is_top5pct_worst_ever_flag": {"inputs": ["close"], "func": dhr_029_is_top5pct_worst_ever_flag},
    "dhr_030_new_low_vs_prior_dd_max_252d_flag": {"inputs": ["close"], "func": dhr_030_new_low_vs_prior_dd_max_252d_flag},
    "dhr_031_dd_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_031_dd_vs_expanding_max_ratio},
    "dhr_032_dd_vs_expanding_median_ratio": {"inputs": ["close"], "func": dhr_032_dd_vs_expanding_median_ratio},
    "dhr_033_dd_vs_rolling_max_252d_ratio": {"inputs": ["close"], "func": dhr_033_dd_vs_rolling_max_252d_ratio},
    "dhr_034_dd_vs_rolling_max_504d_ratio": {"inputs": ["close"], "func": dhr_034_dd_vs_rolling_max_504d_ratio},
    "dhr_035_dd_vs_rolling_mean_252d_ratio": {"inputs": ["close"], "func": dhr_035_dd_vs_rolling_mean_252d_ratio},
    "dhr_036_dd_vs_rolling_mean_504d_ratio": {"inputs": ["close"], "func": dhr_036_dd_vs_rolling_mean_504d_ratio},
    "dhr_037_dd_excess_over_expanding_median": {"inputs": ["close"], "func": dhr_037_dd_excess_over_expanding_median},
    "dhr_038_dd_excess_over_expanding_75pct": {"inputs": ["close"], "func": dhr_038_dd_excess_over_expanding_75pct},
    "dhr_039_dd_excess_over_expanding_90pct": {"inputs": ["close"], "func": dhr_039_dd_excess_over_expanding_90pct},
    "dhr_040_dd_distance_from_expanding_max": {"inputs": ["close"], "func": dhr_040_dd_distance_from_expanding_max},
    "dhr_041_current_dd_duration": {"inputs": ["close"], "func": dhr_041_current_dd_duration},
    "dhr_042_expanding_pctrank_dd_duration": {"inputs": ["close"], "func": dhr_042_expanding_pctrank_dd_duration},
    "dhr_043_rolling_pctrank_dd_duration_252d": {"inputs": ["close"], "func": dhr_043_rolling_pctrank_dd_duration_252d},
    "dhr_044_rolling_pctrank_dd_duration_504d": {"inputs": ["close"], "func": dhr_044_rolling_pctrank_dd_duration_504d},
    "dhr_045_dd_duration_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_045_dd_duration_vs_expanding_max_ratio},
    "dhr_046_dd_duration_vs_expanding_median_ratio": {"inputs": ["close"], "func": dhr_046_dd_duration_vs_expanding_median_ratio},
    "dhr_047_dd_duration_expanding_zscore": {"inputs": ["close"], "func": dhr_047_dd_duration_expanding_zscore},
    "dhr_048_dd_duration_rolling_zscore_252d": {"inputs": ["close"], "func": dhr_048_dd_duration_rolling_zscore_252d},
    "dhr_049_dd_duration_above_expanding_median_flag": {"inputs": ["close"], "func": dhr_049_dd_duration_above_expanding_median_flag},
    "dhr_050_dd_duration_above_252d_max_flag": {"inputs": ["close"], "func": dhr_050_dd_duration_above_252d_max_flag},
    "dhr_051_dd_depth_x_duration_raw": {"inputs": ["close"], "func": dhr_051_dd_depth_x_duration_raw},
    "dhr_052_expanding_pctrank_depth_x_duration": {"inputs": ["close"], "func": dhr_052_expanding_pctrank_depth_x_duration},
    "dhr_053_rolling_pctrank_depth_x_duration_252d": {"inputs": ["close"], "func": dhr_053_rolling_pctrank_depth_x_duration_252d},
    "dhr_054_rolling_pctrank_depth_x_duration_504d": {"inputs": ["close"], "func": dhr_054_rolling_pctrank_depth_x_duration_504d},
    "dhr_055_dd_composite_distress_score": {"inputs": ["close"], "func": dhr_055_dd_composite_distress_score},
    "dhr_056_dd_composite_distress_pctrank_252d": {"inputs": ["close"], "func": dhr_056_dd_composite_distress_pctrank_252d},
    "dhr_057_dd_depth_expanding_75pct_flag": {"inputs": ["close"], "func": dhr_057_dd_depth_expanding_75pct_flag},
    "dhr_058_dd_depth_expanding_95pct_flag": {"inputs": ["close"], "func": dhr_058_dd_depth_expanding_95pct_flag},
    "dhr_059_dd_duration_expanding_75pct_flag": {"inputs": ["close"], "func": dhr_059_dd_duration_expanding_75pct_flag},
    "dhr_060_dd_both_depth_and_duration_top25pct_flag": {"inputs": ["close"], "func": dhr_060_dd_both_depth_and_duration_top25pct_flag},
    "dhr_061_dd_depth_252d_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_061_dd_depth_252d_vs_expanding_max_ratio},
    "dhr_062_dd_depth_63d_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_062_dd_depth_63d_vs_expanding_max_ratio},
    "dhr_063_dd_depth_21d_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_063_dd_depth_21d_vs_expanding_max_ratio},
    "dhr_064_rolling_max_dd_252d": {"inputs": ["close"], "func": dhr_064_rolling_max_dd_252d},
    "dhr_065_rolling_max_dd_504d": {"inputs": ["close"], "func": dhr_065_rolling_max_dd_504d},
    "dhr_066_rolling_max_dd_756d": {"inputs": ["close"], "func": dhr_066_rolling_max_dd_756d},
    "dhr_067_expanding_max_dd": {"inputs": ["close"], "func": dhr_067_expanding_max_dd},
    "dhr_068_expanding_median_dd": {"inputs": ["close"], "func": dhr_068_expanding_median_dd},
    "dhr_069_expanding_90pct_dd": {"inputs": ["close"], "func": dhr_069_expanding_90pct_dd},
    "dhr_070_expanding_75pct_dd": {"inputs": ["close"], "func": dhr_070_expanding_75pct_dd},
    "dhr_071_dd_depth_above_expanding_90pct_flag": {"inputs": ["close"], "func": dhr_071_dd_depth_above_expanding_90pct_flag},
    "dhr_072_rolling_pctrank_dd_depth_756d": {"inputs": ["close"], "func": dhr_072_rolling_pctrank_dd_depth_756d},
    "dhr_073_dd_depth_vs_rolling_90pct_252d_excess": {"inputs": ["close"], "func": dhr_073_dd_depth_vs_rolling_90pct_252d_excess},
    "dhr_074_dd_depth_normalised_by_expanding_std": {"inputs": ["close"], "func": dhr_074_dd_depth_normalised_by_expanding_std},
    "dhr_075_dd_depth_vs_expanding_mean_excess": {"inputs": ["close"], "func": dhr_075_dd_depth_vs_expanding_mean_excess},
}
