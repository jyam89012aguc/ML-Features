"""
108_drawdown_history_rank — 3rd Derivatives (Features dhr_drv3_001-025)
Domain: rate of change of 2nd-derivative drawdown-history-rank features —
        acceleration of drawdown depth/rank velocity, jerk in distress metrics.
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


def _expanding_max(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _drawdown_depth_pct(close: pd.Series) -> pd.Series:
    """Absolute drawdown depth from expanding peak (fraction >= 0)."""
    peak = _expanding_max(close)
    return _safe_div(peak - close, peak.clip(lower=_EPS))


def _current_dd_duration(close: pd.Series) -> pd.Series:
    """Days elapsed since the current drawdown began."""
    depth = _drawdown_depth_pct(close)
    at_high = (depth < _EPS).astype(int)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_high_idx = idx.where(at_high == 1).ffill().fillna(0)
    duration = idx - last_high_idx
    return duration.where(depth >= _EPS, 0.0)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def dhr_drv3_001_dd_depth_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown depth (acceleration of deepening velocity)."""
    vel = _drawdown_depth_pct(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_002_dd_depth_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of drawdown depth (jerk in monthly rate)."""
    vel21 = _drawdown_depth_pct(close).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dhr_drv3_003_expanding_pctrank_dd_depth_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding pct-rank of drawdown depth (acceleration of rank change)."""
    pct = _drawdown_depth_pct(close).expanding(min_periods=2).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_004_rolling_pctrank_dd_depth_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day rolling pct-rank of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_005_dd_depth_vs_max_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown-vs-all-time-max ratio (jerk in severity approach)."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    ratio = _safe_div(depth, max_ever)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_006_dd_duration_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown duration (acceleration of duration growth)."""
    vel = _current_dd_duration(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_007_dd_duration_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of drawdown duration."""
    vel21 = _current_dd_duration(close).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dhr_drv3_008_expanding_pctrank_dd_duration_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding pct-rank of drawdown duration."""
    dur = _current_dd_duration(close)
    pct = dur.expanding(min_periods=2).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_009_dd_depth_x_duration_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of depth×duration product (acceleration of distress area change)."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    score = depth * dur
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_010_pctrank_depth_x_dur_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding pct-rank of depth×duration."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    pct = (depth * dur).expanding(min_periods=2).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_011_hwm_recovery_needed_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of percentage recovery needed (acceleration of distress widening)."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    vel = rec.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_012_pctrank_recovery_needed_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding pct-rank of recovery needed."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    pct = rec.expanding(min_periods=2).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_013_dd_depth_expanding_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding z-score of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = depth.expanding(min_periods=2).mean()
    s = depth.expanding(min_periods=2).std()
    z = _safe_div(depth - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_014_dd_depth_rolling_zscore_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day rolling z-score of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    z = _safe_div(depth - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_015_consec_days_in_dd_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive drawdown days (acceleration of streak growth)."""
    streak = _consec_streak(_drawdown_depth_pct(close) > _EPS)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_016_rolling_pctrank_price_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day rolling pct-rank of price level."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_017_dd_depth_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of drawdown depth."""
    vel21 = _drawdown_depth_pct(close).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def dhr_drv3_018_dd_depth_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of drawdown depth."""
    vel5 = _drawdown_depth_pct(close).diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def dhr_drv3_019_pctrank_dd_depth_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day rolling pct-rank of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel21 = pct.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dhr_drv3_020_fraction_uw_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day underwater fraction."""
    depth = _drawdown_depth_pct(close)
    frac = _rolling_sum((depth > _EPS).astype(float), _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dhr_drv3_021_dd_composite_distress_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite distress score (depth+duration pct-rank sum)."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    score = depth.expanding(min_periods=2).rank(pct=True) + dur.expanding(min_periods=2).rank(pct=True)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_022_dd_depth_5d_diff_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of drawdown depth (smoothed accel)."""
    vel5 = _drawdown_depth_pct(close).diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def dhr_drv3_023_pctrank_recovery_needed_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day rolling pct-rank of recovery needed."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    pct = rec.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_024_dd_depth_vs_median_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown-depth-vs-expanding-median ratio."""
    depth = _drawdown_depth_pct(close)
    med = depth.expanding(min_periods=2).median().clip(lower=_EPS)
    ratio = _safe_div(depth, med)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dhr_drv3_025_expanding_pctrank_price_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of expanding price pct-rank."""
    pct = close.expanding(min_periods=2).rank(pct=True)
    vel21 = pct.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_HISTORY_RANK_REGISTRY_3RD_DERIVATIVES = {
    "dhr_drv3_001_dd_depth_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_001_dd_depth_5d_diff_5d_diff},
    "dhr_drv3_002_dd_depth_21d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_002_dd_depth_21d_diff_5d_diff},
    "dhr_drv3_003_expanding_pctrank_dd_depth_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_003_expanding_pctrank_dd_depth_5d_diff_5d_diff},
    "dhr_drv3_004_rolling_pctrank_dd_depth_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_004_rolling_pctrank_dd_depth_252d_5d_diff_5d_diff},
    "dhr_drv3_005_dd_depth_vs_max_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_005_dd_depth_vs_max_ratio_5d_diff_5d_diff},
    "dhr_drv3_006_dd_duration_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_006_dd_duration_5d_diff_5d_diff},
    "dhr_drv3_007_dd_duration_21d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_007_dd_duration_21d_diff_5d_diff},
    "dhr_drv3_008_expanding_pctrank_dd_duration_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_008_expanding_pctrank_dd_duration_5d_diff_5d_diff},
    "dhr_drv3_009_dd_depth_x_duration_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_009_dd_depth_x_duration_5d_diff_5d_diff},
    "dhr_drv3_010_pctrank_depth_x_dur_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_010_pctrank_depth_x_dur_5d_diff_5d_diff},
    "dhr_drv3_011_hwm_recovery_needed_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_011_hwm_recovery_needed_5d_diff_5d_diff},
    "dhr_drv3_012_pctrank_recovery_needed_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_012_pctrank_recovery_needed_5d_diff_5d_diff},
    "dhr_drv3_013_dd_depth_expanding_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_013_dd_depth_expanding_zscore_5d_diff_5d_diff},
    "dhr_drv3_014_dd_depth_rolling_zscore_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_014_dd_depth_rolling_zscore_252d_5d_diff_5d_diff},
    "dhr_drv3_015_consec_days_in_dd_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_015_consec_days_in_dd_5d_diff_5d_diff},
    "dhr_drv3_016_rolling_pctrank_price_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_016_rolling_pctrank_price_252d_5d_diff_5d_diff},
    "dhr_drv3_017_dd_depth_21d_diff_slope_21d": {"inputs": ["close"], "func": dhr_drv3_017_dd_depth_21d_diff_slope_21d},
    "dhr_drv3_018_dd_depth_5d_diff_slope_21d": {"inputs": ["close"], "func": dhr_drv3_018_dd_depth_5d_diff_slope_21d},
    "dhr_drv3_019_pctrank_dd_depth_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_019_pctrank_dd_depth_252d_21d_diff_5d_diff},
    "dhr_drv3_020_fraction_uw_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_020_fraction_uw_252d_21d_diff_5d_diff},
    "dhr_drv3_021_dd_composite_distress_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_021_dd_composite_distress_5d_diff_5d_diff},
    "dhr_drv3_022_dd_depth_5d_diff_5d_slope_21d": {"inputs": ["close"], "func": dhr_drv3_022_dd_depth_5d_diff_5d_slope_21d},
    "dhr_drv3_023_pctrank_recovery_needed_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_023_pctrank_recovery_needed_252d_5d_diff_5d_diff},
    "dhr_drv3_024_dd_depth_vs_median_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_024_dd_depth_vs_median_ratio_5d_diff_5d_diff},
    "dhr_drv3_025_expanding_pctrank_price_21d_diff_5d_diff": {"inputs": ["close"], "func": dhr_drv3_025_expanding_pctrank_price_21d_diff_5d_diff},
}
