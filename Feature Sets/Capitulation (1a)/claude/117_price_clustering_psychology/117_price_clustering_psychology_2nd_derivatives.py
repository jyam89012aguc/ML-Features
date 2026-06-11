"""
117_price_clustering_psychology — 2nd Derivatives (Features pcp_drv2_001-025)
Domain: rate of change of base price-clustering-psychology features — velocity of round-level
        proximity, distress-zone transitions, and digit-clustering dynamics.
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


def _dist_to_round(price: pd.Series, increment: float) -> pd.Series:
    """Absolute distance from price to the nearest multiple of increment."""
    mod = price % increment
    down = mod
    up = increment - mod
    return np.minimum(down, up)


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

def pcp_drv2_001_dist_to_dollar_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of distance-to-nearest-dollar (velocity of round-level proximity)."""
    return _dist_to_round(close, 1.0).diff(_TD_WEEK)


def pcp_drv2_002_dist_to_dollar_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of distance-to-nearest-dollar (monthly velocity)."""
    return _dist_to_round(close, 1.0).diff(_TD_MON)


def pcp_drv2_003_dist_to_5dollar_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of distance-to-nearest-$5-level."""
    return _dist_to_round(close, 5.0).diff(_TD_WEEK)


def pcp_drv2_004_dist_to_10dollar_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of distance-to-nearest-$10-level."""
    return _dist_to_round(close, 10.0).diff(_TD_WEEK)


def pcp_drv2_005_depth_below_5dollar_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of depth-below-$5 (how fast distress depth is deepening)."""
    depth = (5.0 - close).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def pcp_drv2_006_depth_below_5dollar_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of depth-below-$5."""
    depth = (5.0 - close).clip(lower=0.0)
    return depth.diff(_TD_MON)


def pcp_drv2_007_depth_below_1dollar_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of depth-below-$1 (velocity of penny-stock depth)."""
    depth = (1.0 - close).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def pcp_drv2_008_frac_near_dollar_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of closes within $0.05 of a whole dollar."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    frac = _rolling_sum(near, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def pcp_drv2_009_frac_near_dollar_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day fraction of closes near whole dollar."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    frac = _rolling_sum(near, _TD_MON) / _TD_MON
    return frac.diff(_TD_MON)


def pcp_drv2_010_frac_sub5_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day fraction of closes below $5."""
    frac = _rolling_sum((close < 5.0).astype(float), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_WEEK)


def pcp_drv2_011_consec_sub5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-close-below-$5 streak."""
    streak = _consec_streak(close < 5.0)
    return streak.diff(_TD_WEEK)


def pcp_drv2_012_consec_sub10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-close-below-$10 streak."""
    streak = _consec_streak(close < 10.0)
    return streak.diff(_TD_WEEK)


def pcp_drv2_013_close_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of close (velocity of rank deterioration)."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def pcp_drv2_014_close_pct_rank_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day percentile rank of close."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_MON)


def pcp_drv2_015_log_price_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-close (log return — velocity of price level change)."""
    return np.log(close.clip(lower=_EPS)).diff(_TD_WEEK)


def pcp_drv2_016_log_price_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of log-close (monthly log return)."""
    return np.log(close.clip(lower=_EPS)).diff(_TD_MON)


def pcp_drv2_017_dist_dollar_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-score of distance-to-dollar (velocity of z-score of proximity)."""
    d = _dist_to_round(close, 1.0)
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    z = _safe_div(d - m, s)
    return z.diff(_TD_WEEK)


def pcp_drv2_018_close_vs_expanding_min_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ratio close / expanding-min (velocity of all-time-low approach)."""
    exp_min = close.expanding(min_periods=1).min()
    ratio = _safe_div(close, exp_min.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def pcp_drv2_019_close_pct_from_52wk_low_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of pct-above-52wk-low (velocity of proximity to annual low)."""
    mn = _rolling_min(close, _TD_YEAR)
    pct = _safe_div(close - mn, mn.clip(lower=_EPS))
    return pct.diff(_TD_WEEK)


def pcp_drv2_020_round_magnet_score_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day round-level magnet score (velocity of clustering strength)."""
    normalized = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    score = _rolling_mean(normalized, _TD_MON)
    return score.diff(_TD_WEEK)


def pcp_drv2_021_dist_to_dollar_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of distance-to-nearest-dollar (trend in round proximity)."""
    return _linslope(_dist_to_round(close, 1.0), _TD_MON)


def pcp_drv2_022_dist_to_5dollar_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of distance-to-nearest-$5 level."""
    return _dist_to_round(close, 5.0).diff(_TD_MON)


def pcp_drv2_023_abs_distress_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of absolute price-level distress composite score."""
    score = (
        (close < 10.0).astype(float) +
        2.0 * (close < 5.0).astype(float) +
        3.0 * (close < 2.0).astype(float) +
        4.0 * (close < 1.0).astype(float)
    )
    return score.diff(_TD_WEEK)


def pcp_drv2_024_dollar_zone_descent_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of dollar-zone-descent consecutive streak."""
    lower = (close.apply(np.floor) < close.shift(1).apply(np.floor))
    lower.iloc[0] = False
    streak = _consec_streak(lower)
    return streak.diff(_TD_WEEK)


def pcp_drv2_025_frac_zero_cents_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day fraction of closes with zero-cents component."""
    flag = (close % 1.0 < 0.05).astype(float)
    frac = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_CLUSTERING_PSYCHOLOGY_REGISTRY_2ND_DERIVATIVES = {
    "pcp_drv2_001_dist_to_dollar_5d_diff": {"inputs": ["close"], "func": pcp_drv2_001_dist_to_dollar_5d_diff},
    "pcp_drv2_002_dist_to_dollar_21d_diff": {"inputs": ["close"], "func": pcp_drv2_002_dist_to_dollar_21d_diff},
    "pcp_drv2_003_dist_to_5dollar_5d_diff": {"inputs": ["close"], "func": pcp_drv2_003_dist_to_5dollar_5d_diff},
    "pcp_drv2_004_dist_to_10dollar_5d_diff": {"inputs": ["close"], "func": pcp_drv2_004_dist_to_10dollar_5d_diff},
    "pcp_drv2_005_depth_below_5dollar_5d_diff": {"inputs": ["close"], "func": pcp_drv2_005_depth_below_5dollar_5d_diff},
    "pcp_drv2_006_depth_below_5dollar_21d_diff": {"inputs": ["close"], "func": pcp_drv2_006_depth_below_5dollar_21d_diff},
    "pcp_drv2_007_depth_below_1dollar_5d_diff": {"inputs": ["close"], "func": pcp_drv2_007_depth_below_1dollar_5d_diff},
    "pcp_drv2_008_frac_near_dollar_21d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_008_frac_near_dollar_21d_5d_diff},
    "pcp_drv2_009_frac_near_dollar_21d_21d_diff": {"inputs": ["close"], "func": pcp_drv2_009_frac_near_dollar_21d_21d_diff},
    "pcp_drv2_010_frac_sub5_63d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_010_frac_sub5_63d_5d_diff},
    "pcp_drv2_011_consec_sub5_5d_diff": {"inputs": ["close"], "func": pcp_drv2_011_consec_sub5_5d_diff},
    "pcp_drv2_012_consec_sub10_5d_diff": {"inputs": ["close"], "func": pcp_drv2_012_consec_sub10_5d_diff},
    "pcp_drv2_013_close_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_013_close_pct_rank_252d_5d_diff},
    "pcp_drv2_014_close_pct_rank_252d_21d_diff": {"inputs": ["close"], "func": pcp_drv2_014_close_pct_rank_252d_21d_diff},
    "pcp_drv2_015_log_price_5d_diff": {"inputs": ["close"], "func": pcp_drv2_015_log_price_5d_diff},
    "pcp_drv2_016_log_price_21d_diff": {"inputs": ["close"], "func": pcp_drv2_016_log_price_21d_diff},
    "pcp_drv2_017_dist_dollar_zscore_252d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_017_dist_dollar_zscore_252d_5d_diff},
    "pcp_drv2_018_close_vs_expanding_min_ratio_5d_diff": {"inputs": ["close"], "func": pcp_drv2_018_close_vs_expanding_min_ratio_5d_diff},
    "pcp_drv2_019_close_pct_from_52wk_low_5d_diff": {"inputs": ["close"], "func": pcp_drv2_019_close_pct_from_52wk_low_5d_diff},
    "pcp_drv2_020_round_magnet_score_21d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_020_round_magnet_score_21d_5d_diff},
    "pcp_drv2_021_dist_to_dollar_slope_21d": {"inputs": ["close"], "func": pcp_drv2_021_dist_to_dollar_slope_21d},
    "pcp_drv2_022_dist_to_5dollar_21d_diff": {"inputs": ["close"], "func": pcp_drv2_022_dist_to_5dollar_21d_diff},
    "pcp_drv2_023_abs_distress_score_5d_diff": {"inputs": ["close"], "func": pcp_drv2_023_abs_distress_score_5d_diff},
    "pcp_drv2_024_dollar_zone_descent_streak_5d_diff": {"inputs": ["close"], "func": pcp_drv2_024_dollar_zone_descent_streak_5d_diff},
    "pcp_drv2_025_frac_zero_cents_63d_5d_diff": {"inputs": ["close"], "func": pcp_drv2_025_frac_zero_cents_63d_5d_diff},
}
