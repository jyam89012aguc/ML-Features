"""
106_support_violation — Base Features 076-150
Domain: violation of historical support — congestion-zone lows, swing-low pivots,
        volume-confirmed breaks, ATR-normalized depths, support-rejection patterns,
        graduated break thresholds, and cross-timeframe support alignment.
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


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    """Trailing minimum of low over w days, shifted 1 so today is excluded."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    """Signed depth of price below support level (positive = below support)."""
    return (support - price).clip(lower=0.0)


def _pct_depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    """Percentage depth below support level (0 when at or above support)."""
    depth = (support - price).clip(lower=0.0)
    return _safe_div(depth, support.clip(lower=_EPS))


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Average True Range over w periods."""
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


def _swing_low(low: pd.Series, n: int) -> pd.Series:
    """Mark a bar as a swing low if it has the minimum low in the prior n bars (shifted)."""
    look_back_min = low.shift(1).rolling(n, min_periods=max(1, n // 2)).min()
    return look_back_min


def _congestion_low(low: pd.Series, high: pd.Series, w: int) -> pd.Series:
    """Estimate a congestion-zone low as the lower-quartile of lows over w days (shifted)."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).quantile(0.25)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Congestion-zone low support ---

def sv_076_close_depth_below_congestion_low_21d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Absolute depth of close below the 21-day congestion-zone low (lower quartile of lows)."""
    support = _congestion_low(low, high, _TD_MON)
    return _depth_below(close, support)


def sv_077_close_depth_below_congestion_low_63d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Absolute depth of close below the 63-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_QTR)
    return _depth_below(close, support)


def sv_078_close_pct_depth_below_congestion_low_63d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Percentage depth of close below the 63-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_QTR)
    return _pct_depth_below(close, support)


def sv_079_close_below_congestion_low_63d_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: close is below the 63-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_QTR)
    return (close < support).astype(float)


def sv_080_close_below_congestion_low_252d_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: close is below the 252-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_YEAR)
    return (close < support).astype(float)


def sv_081_close_pct_depth_below_congestion_low_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Percentage depth of close below the 252-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_YEAR)
    return _pct_depth_below(close, support)


def sv_082_consec_below_congestion_low_63d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 63-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_QTR)
    return _consec_streak(close < support)


def sv_083_breaks_below_congestion_low_63d_in_63d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close broke the 63d congestion-zone low."""
    flag = (close < _congestion_low(low, high, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def sv_084_congestion_break_depth_intensity_21d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """21-day sum of pct-depths below 63d congestion-zone low."""
    depth = _pct_depth_below(close, _congestion_low(low, high, _TD_QTR))
    return _rolling_sum(depth, _TD_MON)


def sv_085_congestion_low_63d_ratio(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Close divided by the 63-day congestion-zone low (below 1.0 = violated)."""
    support = _congestion_low(low, high, _TD_QTR)
    return _safe_div(close, support.clip(lower=_EPS))


def sv_086_congestion_low_21d_pct_depth_zscore_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Z-score of pct-depth below 21d congestion low vs its 252d distribution."""
    depth = _pct_depth_below(close, _congestion_low(low, high, _TD_MON))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_087_congestion_low_252d_ratio(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Close divided by the 252-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_YEAR)
    return _safe_div(close, support.clip(lower=_EPS))


def sv_088_days_since_congestion_low_63d_break(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Days since close last broke the 63-day congestion-zone low."""
    flag = (close < _congestion_low(low, high, _TD_QTR)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def sv_089_low_below_congestion_low_63d_flag(low: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: today's low breaks below the 63-day congestion-zone low."""
    support = _congestion_low(low, high, _TD_QTR)
    return (low < support).astype(float)


def sv_090_congestion_low_multi_break_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: close simultaneously breaks both 21d and 63d congestion-zone lows."""
    s21 = _congestion_low(low, high, _TD_MON)
    s63 = _congestion_low(low, high, _TD_QTR)
    return ((close < s21) & (close < s63)).astype(float)


# --- Group G (091-105): Swing-low pivot support ---

def sv_091_close_depth_below_swing_low_5d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the 5-day swing-low pivot."""
    support = _swing_low(low, _TD_WEEK)
    return _depth_below(close, support)


def sv_092_close_depth_below_swing_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the 21-day swing-low pivot."""
    support = _swing_low(low, _TD_MON)
    return _depth_below(close, support)


def sv_093_close_depth_below_swing_low_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the 63-day swing-low pivot."""
    support = _swing_low(low, _TD_QTR)
    return _depth_below(close, support)


def sv_094_close_pct_depth_below_swing_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the 21-day swing-low pivot."""
    support = _swing_low(low, _TD_MON)
    return _pct_depth_below(close, support)


def sv_095_close_pct_depth_below_swing_low_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the 63-day swing-low pivot."""
    support = _swing_low(low, _TD_QTR)
    return _pct_depth_below(close, support)


def sv_096_close_below_swing_low_21d_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below the 21-day swing-low pivot."""
    support = _swing_low(low, _TD_MON)
    return (close < support).astype(float)


def sv_097_close_below_swing_low_63d_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below the 63-day swing-low pivot."""
    support = _swing_low(low, _TD_QTR)
    return (close < support).astype(float)


def sv_098_consec_below_swing_low_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 21-day swing-low pivot."""
    support = _swing_low(low, _TD_MON)
    return _consec_streak(close < support)


def sv_099_consec_below_swing_low_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 63-day swing-low pivot."""
    support = _swing_low(low, _TD_QTR)
    return _consec_streak(close < support)


def sv_100_swing_low_21d_depth_zscore_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of pct-depth below 21d swing-low vs its 252d distribution."""
    depth = _pct_depth_below(close, _swing_low(low, _TD_MON))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_101_swing_low_63d_depth_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth below 63d swing-low within 252d distribution."""
    depth = _pct_depth_below(close, _swing_low(low, _TD_QTR))
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_102_days_since_swing_low_21d_break(close: pd.Series, low: pd.Series) -> pd.Series:
    """Days since close last broke the 21-day swing-low pivot."""
    flag = (close < _swing_low(low, _TD_MON)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def sv_103_swing_low_break_count_63d_in_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close broke the 63d swing-low pivot."""
    flag = (close < _swing_low(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def sv_104_swing_low_composite_break_score(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of binary break flags for 5d, 21d, and 63d swing-low pivots."""
    b5 = (close < _swing_low(low, _TD_WEEK)).astype(float)
    b21 = (close < _swing_low(low, _TD_MON)).astype(float)
    b63 = (close < _swing_low(low, _TD_QTR)).astype(float)
    return b5 + b21 + b63


def sv_105_swing_low_63d_intensity_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day sum of pct-depths below 63d swing-low pivot (sustained violation intensity)."""
    depth = _pct_depth_below(close, _swing_low(low, _TD_QTR))
    return _rolling_sum(depth, _TD_MON)


# --- Group H (106-120): ATR-normalized support break depth ---

def sv_106_atr_norm_depth_below_21d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 21d trailing low, normalized by 14-day ATR."""
    support = _prior_low(low, _TD_MON)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_107_atr_norm_depth_below_63d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 63d trailing low, normalized by 14-day ATR."""
    support = _prior_low(low, _TD_QTR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_108_atr_norm_depth_below_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 252d trailing low, normalized by 14-day ATR."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_109_atr_norm_depth_below_63d_low_21atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 63d trailing low, normalized by 21-day ATR."""
    support = _prior_low(low, _TD_QTR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, _TD_MON)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_110_atr_multiples_below_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of ATR multiples (14d ATR) below the 252d trailing low."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_111_atr_norm_depth_below_126d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 126d trailing low, normalized by 14-day ATR."""
    support = _prior_low(low, _TD_HALF)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_112_atr_norm_depth_below_swing_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 21d swing-low pivot, normalized by 14-day ATR."""
    support = _swing_low(low, _TD_MON)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_113_atr_norm_depth_below_congestion_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 63d congestion-zone low, normalized by 14-day ATR."""
    support = _congestion_low(low, high, _TD_QTR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_114_bar_range_normalized_depth_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth below 252d trailing low as a multiple of today's bar range (H-L)."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    bar_range = (high - low).clip(lower=_EPS)
    return _safe_div(raw_depth, bar_range)


def sv_115_atr_norm_depth_below_252d_low_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR-normalized depth below 252d low vs 252d distribution."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    m = _rolling_mean(norm, _TD_YEAR)
    s = _rolling_std(norm, _TD_YEAR)
    return _safe_div(norm - m, s)


def sv_116_atr_norm_depth_21d_low_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of ATR-normalized depth below 21d low within 252d distribution."""
    support = _prior_low(low, _TD_MON)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    return norm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_117_max_atr_norm_depth_252d_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max ATR-normalized depth below 252d trailing low in trailing 21 days."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    return _rolling_max(norm, _TD_MON)


def sv_118_atr_norm_depth_below_252d_low_intensity_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling sum of ATR-normalized depth below 252d low (sustained violation)."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    return _rolling_sum(norm, _TD_QTR)


def sv_119_atr_multiples_below_126d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of 14d ATR multiples below the 126d trailing low."""
    support = _prior_low(low, _TD_HALF)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    return _safe_div(raw_depth, atr.clip(lower=_EPS))


def sv_120_atr_norm_close_range_on_break_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """On 252d-support break days: ATR-normalized range (H-L)/ATR as decisiveness proxy."""
    support = _prior_low(low, _TD_YEAR)
    broke = (close < support).astype(float)
    atr = _atr(high, low, close, 14)
    bar_range_norm = _safe_div(high - low, atr.clip(lower=_EPS))
    return bar_range_norm * broke


# --- Group I (121-135): Volume-confirmed breaks ---

def sv_121_volume_on_252d_low_break_ratio(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """On 252d-support break days: volume relative to 21-day average volume."""
    support = _prior_low(low, _TD_YEAR)
    broke = (close < support).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return vol_ratio * broke


def sv_122_high_volume_252d_break_flag(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 252d support broken AND volume is at least 1.5x 21d average."""
    support = _prior_low(low, _TD_YEAR)
    broke = (close < support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = volume > 1.5 * avg_vol
    return (broke & high_vol).astype(float)


def sv_123_high_volume_63d_break_flag(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 63d support broken AND volume is at least 1.5x 21d average."""
    support = _prior_low(low, _TD_QTR)
    broke = (close < support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = volume > 1.5 * avg_vol
    return (broke & high_vol).astype(float)


def sv_124_volume_weighted_break_depth_252d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-depth below 252d low multiplied by volume/avg-volume ratio (vol-weighted depth)."""
    support = _prior_low(low, _TD_YEAR)
    depth = _pct_depth_below(close, support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return depth * vol_ratio


def sv_125_volume_weighted_break_depth_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-depth below 63d low multiplied by volume ratio (vol-weighted depth)."""
    support = _prior_low(low, _TD_QTR)
    depth = _pct_depth_below(close, support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return depth * vol_ratio


def sv_126_sum_vol_weighted_depth_252d_in_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling sum of volume-weighted pct-depth below 252d low."""
    support = _prior_low(low, _TD_YEAR)
    depth = _pct_depth_below(close, support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    vw_depth = depth * vol_ratio
    return _rolling_sum(vw_depth, _TD_MON)


def sv_127_vol_surge_on_any_support_break(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on days where any of 21d/63d/252d support is broken (else 0)."""
    b21 = (close < _prior_low(low, _TD_MON))
    b63 = (close < _prior_low(low, _TD_QTR))
    b252 = (close < _prior_low(low, _TD_YEAR))
    any_break = (b21 | b63 | b252).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return vol_ratio * any_break


def sv_128_low_volume_failed_recovery_flag(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: below 252d support AND volume is below 21d average (feeble retest)."""
    support = _prior_low(low, _TD_YEAR)
    below = (close < support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    low_vol = volume < avg_vol
    return (below & low_vol).astype(float)


def sv_129_cumulative_vol_below_252d_low_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day cumulative volume on days where close is below 252d trailing low."""
    support = _prior_low(low, _TD_YEAR)
    below = (close < support).astype(float)
    return _rolling_sum(volume * below, _TD_MON)


def sv_130_cumulative_vol_below_63d_low_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day cumulative volume on days where close is below 63d trailing low."""
    support = _prior_low(low, _TD_QTR)
    below = (close < support).astype(float)
    return _rolling_sum(volume * below, _TD_QTR)


def sv_131_high_vol_consec_252d_breaks(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days: below 252d support AND above-average volume simultaneously."""
    support = _prior_low(low, _TD_YEAR)
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (close < support) & (volume > avg_vol)
    return _consec_streak(cond)


def sv_132_vol_ratio_on_63d_break_days_21d_avg(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average volume ratio on days that broke 63d support (persistence)."""
    support = _prior_low(low, _TD_QTR)
    broke = (close < support).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return _rolling_mean(vol_ratio * broke, _TD_MON)


def sv_133_vol_dollar_depth_252d_low(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted depth below 252d low: depth_in_dollars * volume."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    return raw_depth * volume


def sv_134_vol_dollar_depth_63d_low_21d_sum(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day cumulative dollar-volume-weighted depth below 63d low."""
    support = _prior_low(low, _TD_QTR)
    raw_depth = (support - close).clip(lower=0.0)
    dvd = raw_depth * volume
    return _rolling_sum(dvd, _TD_MON)


def sv_135_vol_above_avg_on_new_52wk_low(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on new 52-week low days (0 on non-new-low days)."""
    support = _prior_low(low, _TD_YEAR)
    new_low = (low < support).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return vol_ratio * new_low


# --- Group J (136-150): Cross-timeframe support alignment and graduated thresholds ---

def sv_136_support_alignment_score_3tf(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of timeframes (21d/63d/252d) where close is simultaneously below prior low."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return b21 + b63 + b252


def sv_137_support_alignment_score_5tf(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 5 timeframes (5d/21d/63d/126d/252d) where close is below prior low."""
    b5 = (close < _prior_low(low, _TD_WEEK)).astype(float)
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b126 = (close < _prior_low(low, _TD_HALF)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    return b5 + b21 + b63 + b126 + b252


def sv_138_longest_support_level_broken_lookback(close: pd.Series, low: pd.Series) -> pd.Series:
    """Longest lookback support level currently broken (0=none, 5,21,63,126,252,504)."""
    breaks = pd.Series(0.0, index=close.index)
    for w, val in [(504, 504.0), (_TD_YEAR, 252.0), (_TD_HALF, 126.0),
                   (_TD_QTR, 63.0), (_TD_MON, 21.0), (_TD_WEEK, 5.0)]:
        support = _prior_low(low, w) if w <= _TD_YEAR else low.shift(1).rolling(w, min_periods=126).min()
        is_broken = close < support
        breaks = breaks.where(~is_broken, val)
    return breaks


def sv_139_support_depth_gradient_21d_vs_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of pct-depth below 252d to pct-depth below 21d (longer-term dominance)."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON)).clip(lower=_EPS)
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _safe_div(d252, d21)


def sv_140_support_depth_gradient_63d_vs_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of pct-depth below 252d to pct-depth below 63d."""
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR)).clip(lower=_EPS)
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _safe_div(d252, d63)


def sv_141_below_half_52wk_range_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below the midpoint of the trailing 252d range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    midpoint = (h252 + l252) / 2.0
    return (close < midpoint).astype(float)


def sv_142_close_position_in_52wk_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in the 252d range: 0 = at low, 1 = at high."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    rng = (h252 - l252).clip(lower=_EPS)
    return _safe_div(close - l252, rng)


def sv_143_close_lower_quartile_52wk_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is in the lowest 25% of its trailing 252-day range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    lower_q = l252 + 0.25 * (h252 - l252)
    return (close <= lower_q).astype(float)


def sv_144_close_decile1_252d_range_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is in the lowest 10% of its trailing 252-day range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    lower_d1 = l252 + 0.10 * (h252 - l252)
    return (close <= lower_d1).astype(float)


def sv_145_pct_from_52wk_high_vs_depth_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: pct below 252d trailing low divided by pct from 252d high (relative positioning)."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    from_high = _safe_div(h252 - close, h252.clip(lower=_EPS))
    from_low = _pct_depth_below(close, l252)
    return _safe_div(from_low, from_high.clip(lower=_EPS))


def sv_146_support_break_acceleration_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of increase in pct-depth below 252d low: 5-day change of 21d mean depth."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    mean21 = _rolling_mean(depth, _TD_MON)
    return mean21.diff(_TD_WEEK)


def sv_147_support_break_duration_vs_max(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of consecutive days below 252d support to max such streak in 252d window."""
    below = close < _prior_low(low, _TD_YEAR)
    streak = _consec_streak(below)
    max_streak = _rolling_max(streak, _TD_YEAR)
    return _safe_div(streak, max_streak.clip(lower=_EPS))


def sv_148_support_violation_composite_score(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Composite: sum of normalized depths below 21d, 63d, 252d trailing + congestion lows."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    dcong63 = _pct_depth_below(close, _congestion_low(low, high, _TD_QTR))
    return d21 + d63 + d252 + dcong63


def sv_149_support_level_break_entropy_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 252d count of distinct support levels (21/63/126/252d) ever broken."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b126 = (close < _prior_low(low, _TD_HALF)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    any21 = _rolling_max(b21, _TD_YEAR)
    any63 = _rolling_max(b63, _TD_YEAR)
    any126 = _rolling_max(b126, _TD_YEAR)
    any252 = _rolling_max(b252, _TD_YEAR)
    return any21 + any63 + any126 + any252


def sv_150_support_violation_capitulation_score(close: pd.Series, low: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation composite: pct-depth below 252d low + vol-ratio + alignment score (normalized)."""
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS)).clip(upper=5.0) / 5.0
    b_score = (
        (close < _prior_low(low, _TD_MON)).astype(float) +
        (close < _prior_low(low, _TD_QTR)).astype(float) +
        (close < _prior_low(low, _TD_YEAR)).astype(float)
    ) / 3.0
    return d252 + vol_ratio + b_score


# ── Registry ──────────────────────────────────────────────────────────────────

SUPPORT_VIOLATION_REGISTRY_076_150 = {
    "sv_076_close_depth_below_congestion_low_21d": {"inputs": ["close", "low", "high"], "func": sv_076_close_depth_below_congestion_low_21d},
    "sv_077_close_depth_below_congestion_low_63d": {"inputs": ["close", "low", "high"], "func": sv_077_close_depth_below_congestion_low_63d},
    "sv_078_close_pct_depth_below_congestion_low_63d": {"inputs": ["close", "low", "high"], "func": sv_078_close_pct_depth_below_congestion_low_63d},
    "sv_079_close_below_congestion_low_63d_flag": {"inputs": ["close", "low", "high"], "func": sv_079_close_below_congestion_low_63d_flag},
    "sv_080_close_below_congestion_low_252d_flag": {"inputs": ["close", "low", "high"], "func": sv_080_close_below_congestion_low_252d_flag},
    "sv_081_close_pct_depth_below_congestion_low_252d": {"inputs": ["close", "low", "high"], "func": sv_081_close_pct_depth_below_congestion_low_252d},
    "sv_082_consec_below_congestion_low_63d": {"inputs": ["close", "low", "high"], "func": sv_082_consec_below_congestion_low_63d},
    "sv_083_breaks_below_congestion_low_63d_in_63d": {"inputs": ["close", "low", "high"], "func": sv_083_breaks_below_congestion_low_63d_in_63d},
    "sv_084_congestion_break_depth_intensity_21d": {"inputs": ["close", "low", "high"], "func": sv_084_congestion_break_depth_intensity_21d},
    "sv_085_congestion_low_63d_ratio": {"inputs": ["close", "low", "high"], "func": sv_085_congestion_low_63d_ratio},
    "sv_086_congestion_low_21d_pct_depth_zscore_252d": {"inputs": ["close", "low", "high"], "func": sv_086_congestion_low_21d_pct_depth_zscore_252d},
    "sv_087_congestion_low_252d_ratio": {"inputs": ["close", "low", "high"], "func": sv_087_congestion_low_252d_ratio},
    "sv_088_days_since_congestion_low_63d_break": {"inputs": ["close", "low", "high"], "func": sv_088_days_since_congestion_low_63d_break},
    "sv_089_low_below_congestion_low_63d_flag": {"inputs": ["low", "high"], "func": sv_089_low_below_congestion_low_63d_flag},
    "sv_090_congestion_low_multi_break_flag": {"inputs": ["close", "low", "high"], "func": sv_090_congestion_low_multi_break_flag},
    "sv_091_close_depth_below_swing_low_5d": {"inputs": ["close", "low"], "func": sv_091_close_depth_below_swing_low_5d},
    "sv_092_close_depth_below_swing_low_21d": {"inputs": ["close", "low"], "func": sv_092_close_depth_below_swing_low_21d},
    "sv_093_close_depth_below_swing_low_63d": {"inputs": ["close", "low"], "func": sv_093_close_depth_below_swing_low_63d},
    "sv_094_close_pct_depth_below_swing_low_21d": {"inputs": ["close", "low"], "func": sv_094_close_pct_depth_below_swing_low_21d},
    "sv_095_close_pct_depth_below_swing_low_63d": {"inputs": ["close", "low"], "func": sv_095_close_pct_depth_below_swing_low_63d},
    "sv_096_close_below_swing_low_21d_flag": {"inputs": ["close", "low"], "func": sv_096_close_below_swing_low_21d_flag},
    "sv_097_close_below_swing_low_63d_flag": {"inputs": ["close", "low"], "func": sv_097_close_below_swing_low_63d_flag},
    "sv_098_consec_below_swing_low_21d": {"inputs": ["close", "low"], "func": sv_098_consec_below_swing_low_21d},
    "sv_099_consec_below_swing_low_63d": {"inputs": ["close", "low"], "func": sv_099_consec_below_swing_low_63d},
    "sv_100_swing_low_21d_depth_zscore_252d": {"inputs": ["close", "low"], "func": sv_100_swing_low_21d_depth_zscore_252d},
    "sv_101_swing_low_63d_depth_pct_rank_252d": {"inputs": ["close", "low"], "func": sv_101_swing_low_63d_depth_pct_rank_252d},
    "sv_102_days_since_swing_low_21d_break": {"inputs": ["close", "low"], "func": sv_102_days_since_swing_low_21d_break},
    "sv_103_swing_low_break_count_63d_in_63d": {"inputs": ["close", "low"], "func": sv_103_swing_low_break_count_63d_in_63d},
    "sv_104_swing_low_composite_break_score": {"inputs": ["close", "low"], "func": sv_104_swing_low_composite_break_score},
    "sv_105_swing_low_63d_intensity_21d": {"inputs": ["close", "low"], "func": sv_105_swing_low_63d_intensity_21d},
    "sv_106_atr_norm_depth_below_21d_low": {"inputs": ["close", "high", "low"], "func": sv_106_atr_norm_depth_below_21d_low},
    "sv_107_atr_norm_depth_below_63d_low": {"inputs": ["close", "high", "low"], "func": sv_107_atr_norm_depth_below_63d_low},
    "sv_108_atr_norm_depth_below_252d_low": {"inputs": ["close", "high", "low"], "func": sv_108_atr_norm_depth_below_252d_low},
    "sv_109_atr_norm_depth_below_63d_low_21atr": {"inputs": ["close", "high", "low"], "func": sv_109_atr_norm_depth_below_63d_low_21atr},
    "sv_110_atr_multiples_below_252d_low": {"inputs": ["close", "high", "low"], "func": sv_110_atr_multiples_below_252d_low},
    "sv_111_atr_norm_depth_below_126d_low": {"inputs": ["close", "high", "low"], "func": sv_111_atr_norm_depth_below_126d_low},
    "sv_112_atr_norm_depth_below_swing_low_21d": {"inputs": ["close", "high", "low"], "func": sv_112_atr_norm_depth_below_swing_low_21d},
    "sv_113_atr_norm_depth_below_congestion_63d": {"inputs": ["close", "high", "low"], "func": sv_113_atr_norm_depth_below_congestion_63d},
    "sv_114_bar_range_normalized_depth_252d_low": {"inputs": ["close", "high", "low"], "func": sv_114_bar_range_normalized_depth_252d_low},
    "sv_115_atr_norm_depth_below_252d_low_zscore": {"inputs": ["close", "high", "low"], "func": sv_115_atr_norm_depth_below_252d_low_zscore},
    "sv_116_atr_norm_depth_21d_low_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": sv_116_atr_norm_depth_21d_low_pct_rank_252d},
    "sv_117_max_atr_norm_depth_252d_low_21d": {"inputs": ["close", "high", "low"], "func": sv_117_max_atr_norm_depth_252d_low_21d},
    "sv_118_atr_norm_depth_below_252d_low_intensity_63d": {"inputs": ["close", "high", "low"], "func": sv_118_atr_norm_depth_below_252d_low_intensity_63d},
    "sv_119_atr_multiples_below_126d_low": {"inputs": ["close", "high", "low"], "func": sv_119_atr_multiples_below_126d_low},
    "sv_120_atr_norm_close_range_on_break_252d": {"inputs": ["close", "high", "low"], "func": sv_120_atr_norm_close_range_on_break_252d},
    "sv_121_volume_on_252d_low_break_ratio": {"inputs": ["close", "low", "volume"], "func": sv_121_volume_on_252d_low_break_ratio},
    "sv_122_high_volume_252d_break_flag": {"inputs": ["close", "low", "volume"], "func": sv_122_high_volume_252d_break_flag},
    "sv_123_high_volume_63d_break_flag": {"inputs": ["close", "low", "volume"], "func": sv_123_high_volume_63d_break_flag},
    "sv_124_volume_weighted_break_depth_252d": {"inputs": ["close", "low", "volume"], "func": sv_124_volume_weighted_break_depth_252d},
    "sv_125_volume_weighted_break_depth_63d": {"inputs": ["close", "low", "volume"], "func": sv_125_volume_weighted_break_depth_63d},
    "sv_126_sum_vol_weighted_depth_252d_in_21d": {"inputs": ["close", "low", "volume"], "func": sv_126_sum_vol_weighted_depth_252d_in_21d},
    "sv_127_vol_surge_on_any_support_break": {"inputs": ["close", "low", "volume"], "func": sv_127_vol_surge_on_any_support_break},
    "sv_128_low_volume_failed_recovery_flag": {"inputs": ["close", "low", "volume"], "func": sv_128_low_volume_failed_recovery_flag},
    "sv_129_cumulative_vol_below_252d_low_21d": {"inputs": ["close", "low", "volume"], "func": sv_129_cumulative_vol_below_252d_low_21d},
    "sv_130_cumulative_vol_below_63d_low_63d": {"inputs": ["close", "low", "volume"], "func": sv_130_cumulative_vol_below_63d_low_63d},
    "sv_131_high_vol_consec_252d_breaks": {"inputs": ["close", "low", "volume"], "func": sv_131_high_vol_consec_252d_breaks},
    "sv_132_vol_ratio_on_63d_break_days_21d_avg": {"inputs": ["close", "low", "volume"], "func": sv_132_vol_ratio_on_63d_break_days_21d_avg},
    "sv_133_vol_dollar_depth_252d_low": {"inputs": ["close", "low", "volume"], "func": sv_133_vol_dollar_depth_252d_low},
    "sv_134_vol_dollar_depth_63d_low_21d_sum": {"inputs": ["close", "low", "volume"], "func": sv_134_vol_dollar_depth_63d_low_21d_sum},
    "sv_135_vol_above_avg_on_new_52wk_low": {"inputs": ["low", "volume"], "func": sv_135_vol_above_avg_on_new_52wk_low},
    "sv_136_support_alignment_score_3tf": {"inputs": ["close", "low"], "func": sv_136_support_alignment_score_3tf},
    "sv_137_support_alignment_score_5tf": {"inputs": ["close", "low"], "func": sv_137_support_alignment_score_5tf},
    "sv_138_longest_support_level_broken_lookback": {"inputs": ["close", "low"], "func": sv_138_longest_support_level_broken_lookback},
    "sv_139_support_depth_gradient_21d_vs_252d": {"inputs": ["close", "low"], "func": sv_139_support_depth_gradient_21d_vs_252d},
    "sv_140_support_depth_gradient_63d_vs_252d": {"inputs": ["close", "low"], "func": sv_140_support_depth_gradient_63d_vs_252d},
    "sv_141_below_half_52wk_range_flag": {"inputs": ["close", "high", "low"], "func": sv_141_below_half_52wk_range_flag},
    "sv_142_close_position_in_52wk_range": {"inputs": ["close", "high", "low"], "func": sv_142_close_position_in_52wk_range},
    "sv_143_close_lower_quartile_52wk_flag": {"inputs": ["close", "high", "low"], "func": sv_143_close_lower_quartile_52wk_flag},
    "sv_144_close_decile1_252d_range_flag": {"inputs": ["close", "high", "low"], "func": sv_144_close_decile1_252d_range_flag},
    "sv_145_pct_from_52wk_high_vs_depth_252d_low": {"inputs": ["close", "high", "low"], "func": sv_145_pct_from_52wk_high_vs_depth_252d_low},
    "sv_146_support_break_acceleration_21d": {"inputs": ["close", "low"], "func": sv_146_support_break_acceleration_21d},
    "sv_147_support_break_duration_vs_max": {"inputs": ["close", "low"], "func": sv_147_support_break_duration_vs_max},
    "sv_148_support_violation_composite_score": {"inputs": ["close", "low", "high"], "func": sv_148_support_violation_composite_score},
    "sv_149_support_level_break_entropy_252d": {"inputs": ["close", "low"], "func": sv_149_support_level_break_entropy_252d},
    "sv_150_support_violation_capitulation_score": {"inputs": ["close", "low", "high", "volume"], "func": sv_150_support_violation_capitulation_score},
}
