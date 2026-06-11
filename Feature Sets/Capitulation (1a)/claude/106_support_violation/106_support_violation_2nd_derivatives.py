"""
106_support_violation — 2nd Derivatives (Features sv_drv2_001-025)
Domain: rate of change of base support-violation features — velocity of support-break
        depth, break counts, break duration, and distance-from-support dynamics.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _pct_depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    depth = (support - price).clip(lower=0.0)
    return _safe_div(depth, support.clip(lower=_EPS))


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def sv_drv2_001_pct_depth_252d_low_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of pct-depth below 252d trailing low (velocity of depth deepening)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return depth.diff(_TD_WEEK)


def sv_drv2_002_pct_depth_252d_low_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of pct-depth below 252d trailing low (monthly deepening rate)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return depth.diff(_TD_MON)


def sv_drv2_003_pct_depth_63d_low_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of pct-depth below 63d trailing low (fast breakdown velocity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return depth.diff(_TD_WEEK)


def sv_drv2_004_pct_depth_63d_low_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of pct-depth below 63d trailing low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return depth.diff(_TD_MON)


def sv_drv2_005_break_score_composite_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 3-timeframe support-break score (21d+63d+252d binary flags)."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    score = b21 + b63 + b252
    return score.diff(_TD_WEEK)


def sv_drv2_006_consec_below_252d_low_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-below-252d-low streak."""
    streak = _consec_streak(close < _prior_low(low, _TD_YEAR))
    return streak.diff(_TD_WEEK)


def sv_drv2_007_pct_depth_252d_low_zscore_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of z-score of pct-depth below 252d low (velocity of z-score)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    z = _safe_div(depth - m, s)
    return z.diff(_TD_WEEK)


def sv_drv2_008_break_count_252d_in_63d_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of break-count-below-252d-low-in-63d (change in break frequency)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    count63 = _rolling_sum(flag, _TD_QTR)
    return count63.diff(_TD_MON)


def sv_drv2_009_multi_depth_sum_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of multi-support depth sum (21d+63d+126d+252d pct-depths)."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d126 = _pct_depth_below(close, _prior_low(low, _TD_HALF))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    total = d21 + d63 + d126 + d252
    return total.diff(_TD_WEEK)


def sv_drv2_010_pct_depth_252d_low_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day OLS slope of pct-depth below 252d low (trend of depth over a month)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return _linslope(depth, _TD_MON)


def sv_drv2_011_pct_depth_63d_low_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day OLS slope of pct-depth below 63d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    return _linslope(depth, _TD_MON)


def sv_drv2_012_atr_norm_depth_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized depth below 252d low (velocity of ATR-scaled depth)."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    return norm.diff(_TD_WEEK)


def sv_drv2_013_atr_norm_depth_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized depth below 63d low."""
    support = _prior_low(low, _TD_QTR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    return norm.diff(_TD_WEEK)


def sv_drv2_014_break_intensity_252d_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling sum of pct-depths below 252d low (intensity velocity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    intensity = _rolling_sum(depth, _TD_MON)
    return intensity.diff(_TD_WEEK)


def sv_drv2_015_break_intensity_63d_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling sum of pct-depths below 63d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    intensity = _rolling_sum(depth, _TD_MON)
    return intensity.diff(_TD_WEEK)


def sv_drv2_016_alignment_score_5tf_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-timeframe support alignment score."""
    b5 = (close < _prior_low(low, _TD_WEEK)).astype(float)
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b126 = (close < _prior_low(low, _TD_HALF)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    score = b5 + b21 + b63 + b126 + b252
    return score.diff(_TD_WEEK)


def sv_drv2_017_close_to_252d_low_ratio_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of close-to-252d-low ratio (rate of ratio change)."""
    support = _prior_low(low, _TD_YEAR)
    ratio = _safe_div(close, support.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def sv_drv2_018_fraction_below_252d_in_252d_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of fraction-below-252d-low-in-252d (change in long-run fraction)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    frac = _rolling_sum(flag, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def sv_drv2_019_pct_depth_252d_low_21d_diff_slope(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 21d-velocity of pct-depth below 252d low (acceleration)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel21 = depth.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def sv_drv2_020_break_recency_score_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of EWM-decayed break flag (velocity of recency-weighted score)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    ewm_score = flag.ewm(span=_TD_QTR, min_periods=1, adjust=True).mean()
    return ewm_score.diff(_TD_WEEK)


def sv_drv2_021_consec_below_63d_low_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-below-63d-low streak."""
    streak = _consec_streak(close < _prior_low(low, _TD_QTR))
    return streak.diff(_TD_WEEK)


def sv_drv2_022_pct_depth_252d_low_5d_diff_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel5 = depth.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def sv_drv2_023_multi_depth_sum_21d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of multi-support depth sum (4-level pct-depth aggregate)."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d126 = _pct_depth_below(close, _prior_low(low, _TD_HALF))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    total = d21 + d63 + d126 + d252
    return total.diff(_TD_MON)


def sv_drv2_024_days_since_52wk_break_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of days-since-last-52wk-low-break (how fast recency counter changes)."""
    flag = (low < _prior_low(low, _TD_YEAR)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    elapsed = (idx - last_idx).where(~low.isna(), np.nan)
    return elapsed.diff(_TD_WEEK)


def sv_drv2_025_pct_depth_252d_low_intensity_63d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63d rolling sum of pct-depth below 252d low (intensity velocity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    intensity = _rolling_sum(depth, _TD_QTR)
    return intensity.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

SUPPORT_VIOLATION_REGISTRY_2ND_DERIVATIVES = {
    "sv_drv2_001_pct_depth_252d_low_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_001_pct_depth_252d_low_5d_diff},
    "sv_drv2_002_pct_depth_252d_low_21d_diff": {"inputs": ["close", "low"], "func": sv_drv2_002_pct_depth_252d_low_21d_diff},
    "sv_drv2_003_pct_depth_63d_low_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_003_pct_depth_63d_low_5d_diff},
    "sv_drv2_004_pct_depth_63d_low_21d_diff": {"inputs": ["close", "low"], "func": sv_drv2_004_pct_depth_63d_low_21d_diff},
    "sv_drv2_005_break_score_composite_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_005_break_score_composite_5d_diff},
    "sv_drv2_006_consec_below_252d_low_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_006_consec_below_252d_low_5d_diff},
    "sv_drv2_007_pct_depth_252d_low_zscore_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_007_pct_depth_252d_low_zscore_5d_diff},
    "sv_drv2_008_break_count_252d_in_63d_21d_diff": {"inputs": ["close", "low"], "func": sv_drv2_008_break_count_252d_in_63d_21d_diff},
    "sv_drv2_009_multi_depth_sum_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_009_multi_depth_sum_5d_diff},
    "sv_drv2_010_pct_depth_252d_low_slope_21d": {"inputs": ["close", "low"], "func": sv_drv2_010_pct_depth_252d_low_slope_21d},
    "sv_drv2_011_pct_depth_63d_low_slope_21d": {"inputs": ["close", "low"], "func": sv_drv2_011_pct_depth_63d_low_slope_21d},
    "sv_drv2_012_atr_norm_depth_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": sv_drv2_012_atr_norm_depth_252d_5d_diff},
    "sv_drv2_013_atr_norm_depth_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": sv_drv2_013_atr_norm_depth_63d_5d_diff},
    "sv_drv2_014_break_intensity_252d_21d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_014_break_intensity_252d_21d_5d_diff},
    "sv_drv2_015_break_intensity_63d_21d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_015_break_intensity_63d_21d_5d_diff},
    "sv_drv2_016_alignment_score_5tf_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_016_alignment_score_5tf_5d_diff},
    "sv_drv2_017_close_to_252d_low_ratio_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_017_close_to_252d_low_ratio_5d_diff},
    "sv_drv2_018_fraction_below_252d_in_252d_21d_diff": {"inputs": ["close", "low"], "func": sv_drv2_018_fraction_below_252d_in_252d_21d_diff},
    "sv_drv2_019_pct_depth_252d_low_21d_diff_slope": {"inputs": ["close", "low"], "func": sv_drv2_019_pct_depth_252d_low_21d_diff_slope},
    "sv_drv2_020_break_recency_score_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_020_break_recency_score_5d_diff},
    "sv_drv2_021_consec_below_63d_low_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_021_consec_below_63d_low_5d_diff},
    "sv_drv2_022_pct_depth_252d_low_5d_diff_slope_21d": {"inputs": ["close", "low"], "func": sv_drv2_022_pct_depth_252d_low_5d_diff_slope_21d},
    "sv_drv2_023_multi_depth_sum_21d_diff": {"inputs": ["close", "low"], "func": sv_drv2_023_multi_depth_sum_21d_diff},
    "sv_drv2_024_days_since_52wk_break_5d_diff": {"inputs": ["low"], "func": sv_drv2_024_days_since_52wk_break_5d_diff},
    "sv_drv2_025_pct_depth_252d_low_intensity_63d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv2_025_pct_depth_252d_low_intensity_63d_5d_diff},
}
