"""
108_drawdown_history_rank — 2nd Derivatives (Features dhr_drv2_001-025)
Domain: rate of change of base drawdown-history-rank features —
        velocity of drawdown depth percentile ranks, duration ranks,
        recovery-needed ranks and related base signals.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dhr_drv2_001_dd_depth_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding drawdown depth (velocity of drawdown deepening)."""
    return _drawdown_depth_pct(close).diff(_TD_WEEK)


def dhr_drv2_002_dd_depth_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of expanding drawdown depth (monthly velocity)."""
    return _drawdown_depth_pct(close).diff(_TD_MON)


def dhr_drv2_003_expanding_pctrank_dd_depth_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank of drawdown depth."""
    pct = _drawdown_depth_pct(close).expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_004_rolling_pctrank_dd_depth_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling percentile rank of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_005_dd_depth_vs_expanding_max_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current drawdown as fraction of all-time max drawdown."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    ratio = _safe_div(depth, max_ever)
    return ratio.diff(_TD_WEEK)


def dhr_drv2_006_dd_duration_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current drawdown duration (velocity of duration growth)."""
    return _current_dd_duration(close).diff(_TD_WEEK)


def dhr_drv2_007_dd_duration_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of current drawdown duration."""
    return _current_dd_duration(close).diff(_TD_MON)


def dhr_drv2_008_expanding_pctrank_dd_duration_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank of drawdown duration."""
    dur = _current_dd_duration(close)
    pct = dur.expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_009_dd_depth_x_duration_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of depth×duration product (velocity of composite distress area)."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    score = depth * dur
    return score.diff(_TD_WEEK)


def dhr_drv2_010_expanding_pctrank_depth_x_dur_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding pct-rank of depth×duration score."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    score = depth * dur
    pct = score.expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_011_hwm_recovery_needed_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of percentage recovery needed to reach all-time high."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    return rec.diff(_TD_WEEK)


def dhr_drv2_012_expanding_pctrank_recovery_needed_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding pct-rank of recovery-needed percentage."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    pct = rec.expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_013_dd_vs_expanding_max_ratio_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of current drawdown as fraction of all-time max drawdown."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    ratio = _safe_div(depth, max_ever)
    return ratio.diff(_TD_MON)


def dhr_drv2_014_rolling_pctrank_price_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling percentile rank of price."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_015_expanding_pctrank_price_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank of price level."""
    pct = close.expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_016_dd_depth_expanding_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding z-score of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = depth.expanding(min_periods=2).mean()
    s = depth.expanding(min_periods=2).std()
    z = _safe_div(depth - m, s)
    return z.diff(_TD_WEEK)


def dhr_drv2_017_dd_depth_rolling_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling z-score of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    z = _safe_div(depth - m, s)
    return z.diff(_TD_WEEK)


def dhr_drv2_018_consec_days_in_dd_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive drawdown days streak."""
    streak = _consec_streak(_drawdown_depth_pct(close) > _EPS)
    return streak.diff(_TD_WEEK)


def dhr_drv2_019_fraction_time_uw_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day fraction of time spent underwater."""
    depth = _drawdown_depth_pct(close)
    frac = _rolling_sum((depth > _EPS).astype(float), _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def dhr_drv2_020_pctrank_dd_depth_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day rolling percentile rank of drawdown depth."""
    depth = _drawdown_depth_pct(close)
    pct = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_MON)


def dhr_drv2_021_dd_composite_distress_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite distress score (sum of depth+duration pct-ranks)."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    score = r_depth + r_dur
    return score.diff(_TD_WEEK)


def dhr_drv2_022_dd_depth_slope_5d_over_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day OLS slope of drawdown depth."""
    slope5 = _linslope(_drawdown_depth_pct(close), _TD_WEEK)
    return _linslope(slope5, _TD_MON)


def dhr_drv2_023_pctrank_recovery_needed_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling pct-rank of percentage recovery needed."""
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    pct = rec.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dhr_drv2_024_dd_depth_vs_expanding_median_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the ratio current drawdown depth vs expanding median."""
    depth = _drawdown_depth_pct(close)
    med = depth.expanding(min_periods=2).median().clip(lower=_EPS)
    ratio = _safe_div(depth, med)
    return ratio.diff(_TD_WEEK)


def dhr_drv2_025_pctrank_price_expanding_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of expanding percentile rank of price level."""
    pct = close.expanding(min_periods=2).rank(pct=True)
    return pct.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_HISTORY_RANK_REGISTRY_2ND_DERIVATIVES = {
    "dhr_drv2_001_dd_depth_5d_diff": {"inputs": ["close"], "func": dhr_drv2_001_dd_depth_5d_diff},
    "dhr_drv2_002_dd_depth_21d_diff": {"inputs": ["close"], "func": dhr_drv2_002_dd_depth_21d_diff},
    "dhr_drv2_003_expanding_pctrank_dd_depth_5d_diff": {"inputs": ["close"], "func": dhr_drv2_003_expanding_pctrank_dd_depth_5d_diff},
    "dhr_drv2_004_rolling_pctrank_dd_depth_252d_5d_diff": {"inputs": ["close"], "func": dhr_drv2_004_rolling_pctrank_dd_depth_252d_5d_diff},
    "dhr_drv2_005_dd_depth_vs_expanding_max_ratio_5d_diff": {"inputs": ["close"], "func": dhr_drv2_005_dd_depth_vs_expanding_max_ratio_5d_diff},
    "dhr_drv2_006_dd_duration_5d_diff": {"inputs": ["close"], "func": dhr_drv2_006_dd_duration_5d_diff},
    "dhr_drv2_007_dd_duration_21d_diff": {"inputs": ["close"], "func": dhr_drv2_007_dd_duration_21d_diff},
    "dhr_drv2_008_expanding_pctrank_dd_duration_5d_diff": {"inputs": ["close"], "func": dhr_drv2_008_expanding_pctrank_dd_duration_5d_diff},
    "dhr_drv2_009_dd_depth_x_duration_5d_diff": {"inputs": ["close"], "func": dhr_drv2_009_dd_depth_x_duration_5d_diff},
    "dhr_drv2_010_expanding_pctrank_depth_x_dur_5d_diff": {"inputs": ["close"], "func": dhr_drv2_010_expanding_pctrank_depth_x_dur_5d_diff},
    "dhr_drv2_011_hwm_recovery_needed_5d_diff": {"inputs": ["close"], "func": dhr_drv2_011_hwm_recovery_needed_5d_diff},
    "dhr_drv2_012_expanding_pctrank_recovery_needed_5d_diff": {"inputs": ["close"], "func": dhr_drv2_012_expanding_pctrank_recovery_needed_5d_diff},
    "dhr_drv2_013_dd_vs_expanding_max_ratio_21d_diff": {"inputs": ["close"], "func": dhr_drv2_013_dd_vs_expanding_max_ratio_21d_diff},
    "dhr_drv2_014_rolling_pctrank_price_252d_5d_diff": {"inputs": ["close"], "func": dhr_drv2_014_rolling_pctrank_price_252d_5d_diff},
    "dhr_drv2_015_expanding_pctrank_price_5d_diff": {"inputs": ["close"], "func": dhr_drv2_015_expanding_pctrank_price_5d_diff},
    "dhr_drv2_016_dd_depth_expanding_zscore_5d_diff": {"inputs": ["close"], "func": dhr_drv2_016_dd_depth_expanding_zscore_5d_diff},
    "dhr_drv2_017_dd_depth_rolling_zscore_252d_5d_diff": {"inputs": ["close"], "func": dhr_drv2_017_dd_depth_rolling_zscore_252d_5d_diff},
    "dhr_drv2_018_consec_days_in_dd_5d_diff": {"inputs": ["close"], "func": dhr_drv2_018_consec_days_in_dd_5d_diff},
    "dhr_drv2_019_fraction_time_uw_252d_21d_diff": {"inputs": ["close"], "func": dhr_drv2_019_fraction_time_uw_252d_21d_diff},
    "dhr_drv2_020_pctrank_dd_depth_252d_21d_diff": {"inputs": ["close"], "func": dhr_drv2_020_pctrank_dd_depth_252d_21d_diff},
    "dhr_drv2_021_dd_composite_distress_score_5d_diff": {"inputs": ["close"], "func": dhr_drv2_021_dd_composite_distress_score_5d_diff},
    "dhr_drv2_022_dd_depth_slope_5d_over_21d": {"inputs": ["close"], "func": dhr_drv2_022_dd_depth_slope_5d_over_21d},
    "dhr_drv2_023_pctrank_recovery_needed_252d_5d_diff": {"inputs": ["close"], "func": dhr_drv2_023_pctrank_recovery_needed_252d_5d_diff},
    "dhr_drv2_024_dd_depth_vs_expanding_median_ratio_5d_diff": {"inputs": ["close"], "func": dhr_drv2_024_dd_depth_vs_expanding_median_ratio_5d_diff},
    "dhr_drv2_025_pctrank_price_expanding_21d_diff": {"inputs": ["close"], "func": dhr_drv2_025_pctrank_price_expanding_21d_diff},
}
