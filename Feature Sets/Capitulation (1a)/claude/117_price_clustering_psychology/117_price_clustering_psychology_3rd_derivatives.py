"""
117_price_clustering_psychology — 3rd Derivatives (Features pcp_drv3_001-025)
Domain: rate of change of 2nd-derivative price-clustering-psychology features —
        acceleration of round-level proximity velocity, distress-zone transition
        acceleration, and digit-clustering dynamics acceleration.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def pcp_drv3_001_dist_to_dollar_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of dist-to-dollar (acceleration of round-level proximity velocity)."""
    vel = _dist_to_round(close, 1.0).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_002_dist_to_dollar_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of dist-to-dollar (jerk in monthly proximity)."""
    vel21 = _dist_to_round(close, 1.0).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pcp_drv3_003_dist_to_5dollar_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of dist-to-nearest-$5-level."""
    vel = _dist_to_round(close, 5.0).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_004_depth_below_5dollar_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of depth-below-$5 (jerk in distress depth)."""
    depth = (5.0 - close).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_005_depth_below_5dollar_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of depth-below-$5."""
    depth = (5.0 - close).clip(lower=0.0)
    vel21 = depth.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pcp_drv3_006_frac_near_dollar_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day fraction near whole dollar."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    frac = _rolling_sum(near, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_007_frac_sub5_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day fraction below $5 (acceleration of distress fraction)."""
    frac = _rolling_sum((close < 5.0).astype(float), _TD_QTR) / _TD_QTR
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_008_log_price_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of log-close (acceleration of log-price velocity)."""
    vel = np.log(close.clip(lower=_EPS)).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_009_log_price_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-return (jerk in monthly price change)."""
    vel21 = np.log(close.clip(lower=_EPS)).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pcp_drv3_010_close_pct_rank_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day pct-rank (acceleration of rank deterioration)."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_011_close_pct_rank_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 252-day pct-rank."""
    pct = close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel21 = pct.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pcp_drv3_012_dist_dollar_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of dist-to-dollar."""
    d = _dist_to_round(close, 1.0)
    m = _rolling_mean(d, _TD_YEAR)
    s = _rolling_std(d, _TD_YEAR)
    z = _safe_div(d - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_013_consec_sub5_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-days-below-$5 streak."""
    streak = _consec_streak(close < 5.0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_014_close_vs_expanding_min_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of close/expanding-min ratio."""
    exp_min = close.expanding(min_periods=1).min()
    ratio = _safe_div(close, exp_min.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_015_pct_from_52wk_low_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of pct-above-52wk-low."""
    mn = _rolling_min(close, _TD_YEAR)
    pct = _safe_div(close - mn, mn.clip(lower=_EPS))
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_016_dist_to_dollar_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (over 21d) of dist-to-dollar (rate of slope change)."""
    slope21 = _linslope(_dist_to_round(close, 1.0), _TD_MON)
    return slope21.diff(_TD_WEEK)


def pcp_drv3_017_round_magnet_score_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day round-level magnet score (jerk in clustering)."""
    normalized = 1.0 - (_dist_to_round(close, 1.0) / 0.5).clip(upper=1.0)
    score = _rolling_mean(normalized, _TD_MON)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_018_dist_to_5dollar_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of dist-to-$5-level."""
    vel21 = _dist_to_round(close, 5.0).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def pcp_drv3_019_dist_to_dollar_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5-day velocity of dist-to-dollar."""
    vel = _dist_to_round(close, 1.0).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pcp_drv3_020_depth_below_5dollar_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5-day velocity of depth-below-$5."""
    depth = (5.0 - close).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pcp_drv3_021_frac_near_dollar_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5-day velocity of 21-day near-dollar fraction."""
    near = (_dist_to_round(close, 1.0) <= 0.05).astype(float)
    frac = _rolling_sum(near, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def pcp_drv3_022_abs_distress_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of absolute price-level distress composite score."""
    score = (
        (close < 10.0).astype(float) +
        2.0 * (close < 5.0).astype(float) +
        3.0 * (close < 2.0).astype(float) +
        4.0 * (close < 1.0).astype(float)
    )
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_023_dollar_zone_descent_streak_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of dollar-zone-descent streak (jerk in zone descent)."""
    lower = (close.apply(np.floor) < close.shift(1).apply(np.floor))
    lower.iloc[0] = False
    streak = _consec_streak(lower)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def pcp_drv3_024_log_price_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 21-day log-return (trend in monthly price velocity)."""
    vel21 = np.log(close.clip(lower=_EPS)).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def pcp_drv3_025_frac_zero_cents_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day zero-cents fraction (jerk in digit clustering)."""
    flag = (close % 1.0 < 0.05).astype(float)
    frac = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_CLUSTERING_PSYCHOLOGY_REGISTRY_3RD_DERIVATIVES = {
    "pcp_drv3_001_dist_to_dollar_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_001_dist_to_dollar_5d_diff_5d_diff},
    "pcp_drv3_002_dist_to_dollar_21d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_002_dist_to_dollar_21d_diff_5d_diff},
    "pcp_drv3_003_dist_to_5dollar_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_003_dist_to_5dollar_5d_diff_5d_diff},
    "pcp_drv3_004_depth_below_5dollar_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_004_depth_below_5dollar_5d_diff_5d_diff},
    "pcp_drv3_005_depth_below_5dollar_21d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_005_depth_below_5dollar_21d_diff_5d_diff},
    "pcp_drv3_006_frac_near_dollar_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_006_frac_near_dollar_21d_5d_diff_5d_diff},
    "pcp_drv3_007_frac_sub5_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_007_frac_sub5_63d_5d_diff_5d_diff},
    "pcp_drv3_008_log_price_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_008_log_price_5d_diff_5d_diff},
    "pcp_drv3_009_log_price_21d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_009_log_price_21d_diff_5d_diff},
    "pcp_drv3_010_close_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_010_close_pct_rank_252d_5d_diff_5d_diff},
    "pcp_drv3_011_close_pct_rank_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_011_close_pct_rank_252d_21d_diff_5d_diff},
    "pcp_drv3_012_dist_dollar_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_012_dist_dollar_zscore_5d_diff_5d_diff},
    "pcp_drv3_013_consec_sub5_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_013_consec_sub5_5d_diff_5d_diff},
    "pcp_drv3_014_close_vs_expanding_min_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_014_close_vs_expanding_min_5d_diff_5d_diff},
    "pcp_drv3_015_pct_from_52wk_low_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_015_pct_from_52wk_low_5d_diff_5d_diff},
    "pcp_drv3_016_dist_to_dollar_slope_5d_diff": {"inputs": ["close"], "func": pcp_drv3_016_dist_to_dollar_slope_5d_diff},
    "pcp_drv3_017_round_magnet_score_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_017_round_magnet_score_21d_5d_diff_5d_diff},
    "pcp_drv3_018_dist_to_5dollar_21d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_018_dist_to_5dollar_21d_diff_5d_diff},
    "pcp_drv3_019_dist_to_dollar_5d_diff_slope_21d": {"inputs": ["close"], "func": pcp_drv3_019_dist_to_dollar_5d_diff_slope_21d},
    "pcp_drv3_020_depth_below_5dollar_5d_diff_slope_21d": {"inputs": ["close"], "func": pcp_drv3_020_depth_below_5dollar_5d_diff_slope_21d},
    "pcp_drv3_021_frac_near_dollar_5d_diff_slope_21d": {"inputs": ["close"], "func": pcp_drv3_021_frac_near_dollar_5d_diff_slope_21d},
    "pcp_drv3_022_abs_distress_score_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_022_abs_distress_score_5d_diff_5d_diff},
    "pcp_drv3_023_dollar_zone_descent_streak_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_023_dollar_zone_descent_streak_5d_diff_5d_diff},
    "pcp_drv3_024_log_price_21d_diff_slope_21d": {"inputs": ["close"], "func": pcp_drv3_024_log_price_21d_diff_slope_21d},
    "pcp_drv3_025_frac_zero_cents_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": pcp_drv3_025_frac_zero_cents_63d_5d_diff_5d_diff},
}
