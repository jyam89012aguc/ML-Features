"""
106_support_violation — 3rd Derivatives (Features sv_drv3_001-025)
Domain: rate of change of 2nd-derivative support-violation features — acceleration of
        support-break depth velocity, break-count velocity, and distance-from-support
        jerk and curvature.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def sv_drv3_001_pct_depth_252d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of pct-depth below 252d low (acceleration of depth velocity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_002_pct_depth_252d_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of pct-depth below 252d low (jerk)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel21 = depth.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def sv_drv3_003_pct_depth_63d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of pct-depth below 63d low (acceleration of 63d depth velocity)."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_004_break_score_composite_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-timeframe break score (acceleration of break score velocity)."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    score = b21 + b63 + b252
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_005_consec_below_252d_low_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-days-below-252d-low streak."""
    streak = _consec_streak(close < _prior_low(low, _TD_YEAR))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_006_pct_depth_252d_zscore_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    z = _safe_div(depth - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_007_multi_depth_sum_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-support depth sum (4-level aggregate)."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d126 = _pct_depth_below(close, _prior_low(low, _TD_HALF))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    total = d21 + d63 + d126 + d252
    vel = total.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_008_atr_norm_depth_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR-normalized depth below 252d low."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    vel = norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_009_pct_depth_252d_slope_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    slope21 = _linslope(depth, _TD_MON)
    return slope21.diff(_TD_WEEK)


def sv_drv3_010_pct_depth_63d_slope_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of pct-depth below 63d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    slope21 = _linslope(depth, _TD_MON)
    return slope21.diff(_TD_WEEK)


def sv_drv3_011_break_intensity_252d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d rolling break intensity below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    intensity = _rolling_sum(depth, _TD_MON)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_012_break_intensity_63d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d rolling break intensity below 63d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    intensity = _rolling_sum(depth, _TD_MON)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_013_alignment_score_5tf_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-timeframe alignment score."""
    b5 = (close < _prior_low(low, _TD_WEEK)).astype(float)
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b126 = (close < _prior_low(low, _TD_HALF)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    score = b5 + b21 + b63 + b126 + b252
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_014_close_to_252d_low_ratio_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of close-to-252d-low ratio (acceleration of ratio change)."""
    support = _prior_low(low, _TD_YEAR)
    ratio = _safe_div(close, support.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_015_pct_depth_252d_21d_diff_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 21d-velocity of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel21 = depth.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def sv_drv3_016_break_count_252d_63d_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-change in 63d break count below 252d (acceleration of frequency change)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    count63 = _rolling_sum(flag, _TD_QTR)
    vel21 = count63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def sv_drv3_017_pct_depth_63d_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of pct-depth below 63d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    vel21 = depth.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def sv_drv3_018_pct_depth_252d_5d_diff_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    vel5 = depth.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def sv_drv3_019_atr_norm_depth_252d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in ATR-normalized depth below 252d low."""
    support = _prior_low(low, _TD_YEAR)
    raw_depth = (support - close).clip(lower=0.0)
    atr = _atr(high, low, close, 14)
    norm = _safe_div(raw_depth, atr.clip(lower=_EPS))
    vel21 = norm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def sv_drv3_020_break_recency_ewm_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM-decayed break flag (acceleration of recency score)."""
    flag = (close < _prior_low(low, _TD_YEAR)).astype(float)
    ewm_score = flag.ewm(span=_TD_QTR, min_periods=1, adjust=True).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_021_consec_below_252d_slope_21d_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of consecutive-days-below-252d streak."""
    streak = _consec_streak(close < _prior_low(low, _TD_YEAR))
    slope = _linslope(streak, _TD_MON)
    return slope.diff(_TD_WEEK)


def sv_drv3_022_multi_depth_sum_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21d-velocity of multi-support depth sum."""
    d21 = _pct_depth_below(close, _prior_low(low, _TD_MON))
    d63 = _pct_depth_below(close, _prior_low(low, _TD_QTR))
    d126 = _pct_depth_below(close, _prior_low(low, _TD_HALF))
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    total = d21 + d63 + d126 + d252
    vel21 = total.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def sv_drv3_023_pct_depth_252d_intensity_63d_5d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d intensity of pct-depth below 252d low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    intensity = _rolling_sum(depth, _TD_QTR)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_024_days_since_52wk_break_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-52wk-low-break (jerk in elapsed-time counter)."""
    flag = (low < _prior_low(low, _TD_YEAR)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    elapsed = (idx - last_idx).where(~low.isna(), np.nan)
    vel = elapsed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def sv_drv3_025_break_score_composite_21d_diff_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21d-velocity of 3-timeframe support break score."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    score = b21 + b63 + b252
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

SUPPORT_VIOLATION_REGISTRY_3RD_DERIVATIVES = {
    "sv_drv3_001_pct_depth_252d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_001_pct_depth_252d_5d_diff_5d_diff},
    "sv_drv3_002_pct_depth_252d_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_002_pct_depth_252d_21d_diff_5d_diff},
    "sv_drv3_003_pct_depth_63d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_003_pct_depth_63d_5d_diff_5d_diff},
    "sv_drv3_004_break_score_composite_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_004_break_score_composite_5d_diff_5d_diff},
    "sv_drv3_005_consec_below_252d_low_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_005_consec_below_252d_low_5d_diff_5d_diff},
    "sv_drv3_006_pct_depth_252d_zscore_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_006_pct_depth_252d_zscore_5d_diff_5d_diff},
    "sv_drv3_007_multi_depth_sum_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_007_multi_depth_sum_5d_diff_5d_diff},
    "sv_drv3_008_atr_norm_depth_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": sv_drv3_008_atr_norm_depth_252d_5d_diff_5d_diff},
    "sv_drv3_009_pct_depth_252d_slope_21d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_009_pct_depth_252d_slope_21d_5d_diff},
    "sv_drv3_010_pct_depth_63d_slope_21d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_010_pct_depth_63d_slope_21d_5d_diff},
    "sv_drv3_011_break_intensity_252d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_011_break_intensity_252d_5d_diff_5d_diff},
    "sv_drv3_012_break_intensity_63d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_012_break_intensity_63d_5d_diff_5d_diff},
    "sv_drv3_013_alignment_score_5tf_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_013_alignment_score_5tf_5d_diff_5d_diff},
    "sv_drv3_014_close_to_252d_low_ratio_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_014_close_to_252d_low_ratio_5d_diff_5d_diff},
    "sv_drv3_015_pct_depth_252d_21d_diff_slope_21d": {"inputs": ["close", "low"], "func": sv_drv3_015_pct_depth_252d_21d_diff_slope_21d},
    "sv_drv3_016_break_count_252d_63d_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_016_break_count_252d_63d_21d_diff_5d_diff},
    "sv_drv3_017_pct_depth_63d_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_017_pct_depth_63d_21d_diff_5d_diff},
    "sv_drv3_018_pct_depth_252d_5d_diff_slope_21d": {"inputs": ["close", "low"], "func": sv_drv3_018_pct_depth_252d_5d_diff_slope_21d},
    "sv_drv3_019_atr_norm_depth_252d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": sv_drv3_019_atr_norm_depth_252d_21d_diff_5d_diff},
    "sv_drv3_020_break_recency_ewm_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_020_break_recency_ewm_5d_diff_5d_diff},
    "sv_drv3_021_consec_below_252d_slope_21d_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_021_consec_below_252d_slope_21d_5d_diff},
    "sv_drv3_022_multi_depth_sum_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_022_multi_depth_sum_21d_diff_5d_diff},
    "sv_drv3_023_pct_depth_252d_intensity_63d_5d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_023_pct_depth_252d_intensity_63d_5d_diff_5d_diff},
    "sv_drv3_024_days_since_52wk_break_5d_diff_5d_diff": {"inputs": ["low"], "func": sv_drv3_024_days_since_52wk_break_5d_diff_5d_diff},
    "sv_drv3_025_break_score_composite_21d_diff_5d_diff": {"inputs": ["close", "low"], "func": sv_drv3_025_break_score_composite_21d_diff_5d_diff},
}
