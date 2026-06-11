"""
06_low_proximity — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative low-proximity features
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes .diff / slope / pct-change of a 2nd-derivative proximity concept.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


def _stoch(close: pd.Series, w: int) -> pd.Series:
    h = _rolling_max(close, w)
    l = _rolling_min(close, w)
    return _safe_div(close - l, h - l)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def lp_drv3_001_dist_252d_min_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of (close-252d min)/min: 2nd-order acceleration of floor retreat."""
    m = _rolling_min(close, _TD_YEAR)
    dist = _safe_div(close - m, m)
    vel = dist.diff(5)
    return vel.diff(5)


def lp_drv3_002_stoch_252d_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of 252d stochastic (jerk in annual floor position)."""
    s = _stoch(close, _TD_YEAR)
    vel = s.diff(5)
    return vel.diff(5)


def lp_drv3_003_stoch_21d_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of 21d stochastic (jerk in monthly floor position)."""
    s = _stoch(close, _TD_MON)
    vel = s.diff(5)
    return vel.diff(5)


def lp_drv3_004_new_low_freq_252d_accel(close: pd.Series) -> pd.Series:
    """5d diff of 21d-diff of 252d new-low frequency (2nd order new-low rate change)."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    freq = _rolling_mean(flag, _TD_YEAR)
    vel = freq.diff(_TD_MON)
    return vel.diff(5)


def lp_drv3_005_log_dist_atl_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of log-distance from ATL (2nd order ATL proximity change)."""
    m = close.expanding(min_periods=1).min()
    log_dist = _log_safe(close) - _log_safe(m)
    vel = log_dist.diff(5)
    return vel.diff(5)


def lp_drv3_006_stoch_252d_slope_21d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d OLS slope of 252d stochastic (acceleration of annual floor trend)."""
    s = _stoch(close, _TD_YEAR)
    slope = _linslope(s, _TD_MON)
    return slope.diff(5)


def lp_drv3_007_stoch_63d_slope_21d_diff(close: pd.Series) -> pd.Series:
    """5d diff of 21d OLS slope of 63d stochastic (acceleration of quarterly floor trend)."""
    s = _stoch(close, _TD_QTR)
    slope = _linslope(s, _TD_MON)
    return slope.diff(5)


def lp_drv3_008_bollinger_pct_b_21d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of 21d Bollinger %B (2nd order lower-band approach)."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = ma - 2.0 * sd
    upper = ma + 2.0 * sd
    pct_b = _safe_div(close - lower, upper - lower)
    vel = pct_b.diff(5)
    return vel.diff(5)


def lp_drv3_009_new_low_count_63d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of 63d new-low count (2nd order clustering acceleration)."""
    flag = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    vel = cnt.diff(5)
    return vel.diff(5)


def lp_drv3_010_frac_5pct_min_252d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 21d-diff of fraction-within-5%-of-252d-min (floor-hugging acceleration)."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.05).astype(float)
    frac = _rolling_mean(near, _TD_YEAR)
    vel = frac.diff(_TD_MON)
    return vel.diff(5)


def lp_drv3_011_undercut_depth_252d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of prior-252d undercut depth (cascading undercut acceleration)."""
    prior_min = close.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    depth = _safe_div(close - prior_min, prior_min)
    vel = depth.diff(5)
    return vel.diff(5)


def lp_drv3_012_expanding_rank_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of expanding percentile rank (jerk into all-time-low territory)."""
    rank = close.expanding(min_periods=1).rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def lp_drv3_013_consecutive_252d_lows_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of consecutive-252d-new-low streak (streak jerk)."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(int).values
    streak = np.zeros(len(flag), dtype=float)
    cnt = 0
    for i in range(len(flag)):
        if flag[i] == 1:
            cnt += 1
        else:
            cnt = 0
        streak[i] = cnt
    s = pd.Series(streak, index=close.index)
    vel = s.diff(5)
    return vel.diff(5)


def lp_drv3_014_stoch_21d_63d_slope_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d OLS slope of 21d stochastic (jerk in monthly floor trend)."""
    s = _stoch(close, _TD_MON)
    slope = _linslope(s, _TD_QTR)
    return slope.diff(5)


def lp_drv3_015_min_series_accel_21d_diff(close: pd.Series) -> pd.Series:
    """5d diff of acceleration of 21d rolling-min slope (3rd order floor erosion jerk)."""
    m = _rolling_min(close, _TD_MON)
    vel = m.diff(5)
    accel = vel.diff(5)
    return accel.diff(5)


def lp_drv3_016_composite_stoch_5d_diff_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of composite stochastic (jerk in composite floor position)."""
    composite = (
        0.40 * _stoch(close, _TD_MON) +
        0.30 * _stoch(close, _TD_QTR) +
        0.20 * _stoch(close, _TD_HALF) +
        0.10 * _stoch(close, _TD_YEAR)
    )
    vel = composite.diff(5)
    return vel.diff(5)


def lp_drv3_017_dist_atl_pct_change_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 21d-pct-change of distance above ATL (2nd order ATL proximity rate)."""
    m = close.expanding(min_periods=1).min()
    dist = (close - m).clip(lower=_EPS)
    vel = _safe_div(dist - dist.shift(_TD_MON), dist.shift(_TD_MON).abs())
    return vel.diff(5)


def lp_drv3_018_vol_adj_dist_252d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of vol-adjusted distance above 252d min (vol-norm jerk)."""
    m = _rolling_min(close, _TD_YEAR)
    raw = _safe_div(close - m, m)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    dist = _safe_div(raw, vol)
    vel = dist.diff(5)
    return vel.diff(5)


def lp_drv3_019_new_low_freq_21d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of 21d new-low frequency (short-term new-low rate jerk)."""
    flag = (close <= _rolling_min(close, _TD_MON)).astype(float)
    freq = _rolling_mean(flag, _TD_MON)
    vel = freq.diff(5)
    return vel.diff(5)


def lp_drv3_020_stoch_inversion_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of stochastic inversion flag (21d vs 252d inversion jerk)."""
    s21 = _stoch(close, _TD_MON)
    s252 = _stoch(close, _TD_YEAR)
    inv = (s21 < s252).astype(float)
    vel = inv.diff(5)
    return vel.diff(5)


def lp_drv3_021_atl_count_252d_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of 252d ATL-cluster count (ATL-touching-events jerk)."""
    flag = (close <= close.expanding(min_periods=1).min()).astype(float)
    cnt = _rolling_sum(flag, _TD_YEAR)
    vel = cnt.diff(5)
    return vel.diff(5)


def lp_drv3_022_stoch_252d_63d_slope_diff(close: pd.Series) -> pd.Series:
    """5d diff of 63d OLS slope of 252d stochastic (acceleration of annual position trend)."""
    s = _stoch(close, _TD_YEAR)
    slope = _linslope(s, _TD_QTR)
    return slope.diff(5)


def lp_drv3_023_min_series_accel_252d_diff(close: pd.Series) -> pd.Series:
    """5d diff of acceleration of 252d rolling-min slope (3rd order annual floor erosion jerk)."""
    m = _rolling_min(close, _TD_YEAR)
    vel = m.diff(5)
    accel = vel.diff(5)
    return accel.diff(5)


def lp_drv3_024_dist_63d_min_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of (close-63d min)/min (jerk in quarterly floor proximity)."""
    m = _rolling_min(close, _TD_QTR)
    dist = _safe_div(close - m, m)
    vel = dist.diff(5)
    return vel.diff(5)


def lp_drv3_025_stoch_ratio_21_252_accel(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of ratio of 21d stochastic to 252d stochastic (cross-scale jerk)."""
    s21 = _stoch(close, _TD_MON)
    s252 = _stoch(close, _TD_YEAR)
    ratio = _safe_div(s21, s252.replace(0, np.nan))
    vel = ratio.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

LOW_PROXIMITY_REGISTRY_3RD_DERIVATIVES = {
    "lp_drv3_001_dist_252d_min_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_001_dist_252d_min_5d_diff_accel},
    "lp_drv3_002_stoch_252d_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_002_stoch_252d_5d_diff_accel},
    "lp_drv3_003_stoch_21d_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_003_stoch_21d_5d_diff_accel},
    "lp_drv3_004_new_low_freq_252d_accel": {"inputs": ["close"], "func": lp_drv3_004_new_low_freq_252d_accel},
    "lp_drv3_005_log_dist_atl_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_005_log_dist_atl_5d_diff_accel},
    "lp_drv3_006_stoch_252d_slope_21d_diff": {"inputs": ["close"], "func": lp_drv3_006_stoch_252d_slope_21d_diff},
    "lp_drv3_007_stoch_63d_slope_21d_diff": {"inputs": ["close"], "func": lp_drv3_007_stoch_63d_slope_21d_diff},
    "lp_drv3_008_bollinger_pct_b_21d_accel": {"inputs": ["close"], "func": lp_drv3_008_bollinger_pct_b_21d_accel},
    "lp_drv3_009_new_low_count_63d_accel": {"inputs": ["close"], "func": lp_drv3_009_new_low_count_63d_accel},
    "lp_drv3_010_frac_5pct_min_252d_accel": {"inputs": ["close"], "func": lp_drv3_010_frac_5pct_min_252d_accel},
    "lp_drv3_011_undercut_depth_252d_accel": {"inputs": ["close"], "func": lp_drv3_011_undercut_depth_252d_accel},
    "lp_drv3_012_expanding_rank_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_012_expanding_rank_5d_diff_accel},
    "lp_drv3_013_consecutive_252d_lows_accel": {"inputs": ["close"], "func": lp_drv3_013_consecutive_252d_lows_accel},
    "lp_drv3_014_stoch_21d_63d_slope_diff": {"inputs": ["close"], "func": lp_drv3_014_stoch_21d_63d_slope_diff},
    "lp_drv3_015_min_series_accel_21d_diff": {"inputs": ["close"], "func": lp_drv3_015_min_series_accel_21d_diff},
    "lp_drv3_016_composite_stoch_5d_diff_accel": {"inputs": ["close"], "func": lp_drv3_016_composite_stoch_5d_diff_accel},
    "lp_drv3_017_dist_atl_pct_change_accel": {"inputs": ["close"], "func": lp_drv3_017_dist_atl_pct_change_accel},
    "lp_drv3_018_vol_adj_dist_252d_accel": {"inputs": ["close"], "func": lp_drv3_018_vol_adj_dist_252d_accel},
    "lp_drv3_019_new_low_freq_21d_accel": {"inputs": ["close"], "func": lp_drv3_019_new_low_freq_21d_accel},
    "lp_drv3_020_stoch_inversion_accel": {"inputs": ["close"], "func": lp_drv3_020_stoch_inversion_accel},
    "lp_drv3_021_atl_count_252d_accel": {"inputs": ["close"], "func": lp_drv3_021_atl_count_252d_accel},
    "lp_drv3_022_stoch_252d_63d_slope_diff": {"inputs": ["close"], "func": lp_drv3_022_stoch_252d_63d_slope_diff},
    "lp_drv3_023_min_series_accel_252d_diff": {"inputs": ["close"], "func": lp_drv3_023_min_series_accel_252d_diff},
    "lp_drv3_024_dist_63d_min_accel": {"inputs": ["close"], "func": lp_drv3_024_dist_63d_min_accel},
    "lp_drv3_025_stoch_ratio_21_252_accel": {"inputs": ["close"], "func": lp_drv3_025_stoch_ratio_21_252_accel},
}
