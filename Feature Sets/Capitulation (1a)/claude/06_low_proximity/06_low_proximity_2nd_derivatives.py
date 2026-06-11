"""
06_low_proximity — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base low-proximity / new-low features
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes a .diff(n) or slope/pct-change of a base proximity concept.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def lp_drv2_001_dist_252d_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (close - 252d min)/min: velocity of moving away from the floor."""
    m = _rolling_min(close, _TD_YEAR)
    dist = _safe_div(close - m, m)
    return dist.diff(5)


def lp_drv2_002_dist_63d_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (close - 63d min)/min: quarterly floor-proximity velocity."""
    m = _rolling_min(close, _TD_QTR)
    dist = _safe_div(close - m, m)
    return dist.diff(5)


def lp_drv2_003_stoch_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d stochastic position (rate of change of annual floor position)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    return s.diff(5)


def lp_drv2_004_stoch_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d stochastic (short-term floor proximity velocity)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    return s.diff(5)


def lp_drv2_005_new_low_freq_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d new-low frequency (acceleration of new-low occurrence rate)."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    freq = _rolling_mean(flag, _TD_YEAR)
    return freq.diff(5)


def lp_drv2_006_new_low_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d new-low count (acceleration of quarterly new-low clustering)."""
    flag = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(5)


def lp_drv2_007_log_dist_atl_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log distance above expanding all-time low (log-velocity from ATL)."""
    m = close.expanding(min_periods=1).min()
    log_dist = _log_safe(close) - _log_safe(m)
    return log_dist.diff(5)


def lp_drv2_008_stoch_252d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 252d stochastic over trailing 21 days (short-term trend of annual position)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    return _linslope(s, _TD_MON)


def lp_drv2_009_stoch_63d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 63d stochastic over trailing 21 days."""
    h = _rolling_max(close, _TD_QTR)
    l = _rolling_min(close, _TD_QTR)
    s = _safe_div(close - l, h - l)
    return _linslope(s, _TD_MON)


def lp_drv2_010_bollinger_pct_b_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d Bollinger %B (speed of approach to lower band)."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = ma - 2.0 * sd
    upper = ma + 2.0 * sd
    pct_b = _safe_div(close - lower, upper - lower)
    return pct_b.diff(5)


def lp_drv2_011_frac_within_5pct_min_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of fraction-within-5%-of-252d-min (change in floor-hugging intensity)."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.05).astype(float)
    frac = _rolling_mean(near, _TD_YEAR)
    return frac.diff(_TD_MON)


def lp_drv2_012_stoch_21d_63d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 21d stochastic over trailing 63 days (quarterly trend of monthly position)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    return _linslope(s, _TD_QTR)


def lp_drv2_013_consecutive_252d_lows_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-252d-new-low streak (streak acceleration)."""
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
    return s.diff(5)


def lp_drv2_014_expanding_pct_rank_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank (speed of descent into all-time-low territory)."""
    rank = close.expanding(min_periods=1).rank(pct=True)
    return rank.diff(5)


def lp_drv2_015_undercut_depth_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of prior-252d-low undercut depth (acceleration of successive undercuts)."""
    prior_min = close.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    depth = _safe_div(close - prior_min, prior_min)
    return depth.diff(5)


def lp_drv2_016_dist_atl_pct_change_21d(close: pd.Series) -> pd.Series:
    """21-day pct change in distance above ATL (relative rate of ATL approach)."""
    m = close.expanding(min_periods=1).min()
    dist = (close - m).clip(lower=_EPS)
    return _safe_div(dist - dist.shift(_TD_MON), dist.shift(_TD_MON).abs())


def lp_drv2_017_new_low_freq_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d new-low frequency (short-term new-low acceleration)."""
    flag = (close <= _rolling_min(close, _TD_MON)).astype(float)
    freq = _rolling_mean(flag, _TD_MON)
    return freq.diff(5)


def lp_drv2_018_stoch_21d_21d_pct_change(close: pd.Series) -> pd.Series:
    """21-day percent change in 21d stochastic (monthly rate of floor approach)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l).clip(lower=_EPS)
    return _safe_div(s - s.shift(_TD_MON), s.shift(_TD_MON).abs())


def lp_drv2_019_min_series_accel_21d(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d rolling-min slope (acceleration of floor erosion)."""
    m = _rolling_min(close, _TD_MON)
    slope = m.diff(5)
    return slope.diff(5)


def lp_drv2_020_min_series_accel_252d(close: pd.Series) -> pd.Series:
    """5-day diff of the 252d rolling-min slope (acceleration of annual floor erosion)."""
    m = _rolling_min(close, _TD_YEAR)
    slope = m.diff(5)
    return slope.diff(5)


def lp_drv2_021_stoch_inversion_21_252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of stochastic inversion flag (21d vs 252d inversion dynamics)."""
    h21 = _rolling_max(close, _TD_MON)
    l21 = _rolling_min(close, _TD_MON)
    s21 = _safe_div(close - l21, h21 - l21)
    h252 = _rolling_max(close, _TD_YEAR)
    l252 = _rolling_min(close, _TD_YEAR)
    s252 = _safe_div(close - l252, h252 - l252)
    inv = (s21 < s252).astype(float)
    return inv.diff(5)


def lp_drv2_022_vol_adj_dist_252d_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol-adjusted distance above 252d min (vol-normalized floor proximity change)."""
    m = _rolling_min(close, _TD_YEAR)
    raw = _safe_div(close - m, m)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    dist = _safe_div(raw, vol)
    return dist.diff(5)


def lp_drv2_023_stoch_252d_63d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 252d stochastic over trailing 63 days (quarterly trend of annual position)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    return _linslope(s, _TD_QTR)


def lp_drv2_024_atl_count_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d ATL-cluster count (acceleration of all-time-low-touching events)."""
    flag = (close <= close.expanding(min_periods=1).min()).astype(float)
    cnt = _rolling_sum(flag, _TD_YEAR)
    return cnt.diff(5)


def lp_drv2_025_composite_stoch_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite weighted stochastic (40%*21d + 30%*63d + 20%*126d + 10%*252d)."""
    def _stoch(w):
        h = _rolling_max(close, w)
        l = _rolling_min(close, w)
        return _safe_div(close - l, h - l)
    composite = 0.40 * _stoch(_TD_MON) + 0.30 * _stoch(_TD_QTR) + 0.20 * _stoch(_TD_HALF) + 0.10 * _stoch(_TD_YEAR)
    return composite.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

LOW_PROXIMITY_REGISTRY_2ND_DERIVATIVES = {
    "lp_drv2_001_dist_252d_min_5d_diff": {"inputs": ["close"], "func": lp_drv2_001_dist_252d_min_5d_diff},
    "lp_drv2_002_dist_63d_min_5d_diff": {"inputs": ["close"], "func": lp_drv2_002_dist_63d_min_5d_diff},
    "lp_drv2_003_stoch_252d_5d_diff": {"inputs": ["close"], "func": lp_drv2_003_stoch_252d_5d_diff},
    "lp_drv2_004_stoch_21d_5d_diff": {"inputs": ["close"], "func": lp_drv2_004_stoch_21d_5d_diff},
    "lp_drv2_005_new_low_freq_252d_5d_diff": {"inputs": ["close"], "func": lp_drv2_005_new_low_freq_252d_5d_diff},
    "lp_drv2_006_new_low_count_63d_5d_diff": {"inputs": ["close"], "func": lp_drv2_006_new_low_count_63d_5d_diff},
    "lp_drv2_007_log_dist_atl_5d_diff": {"inputs": ["close"], "func": lp_drv2_007_log_dist_atl_5d_diff},
    "lp_drv2_008_stoch_252d_21d_slope": {"inputs": ["close"], "func": lp_drv2_008_stoch_252d_21d_slope},
    "lp_drv2_009_stoch_63d_21d_slope": {"inputs": ["close"], "func": lp_drv2_009_stoch_63d_21d_slope},
    "lp_drv2_010_bollinger_pct_b_21d_5d_diff": {"inputs": ["close"], "func": lp_drv2_010_bollinger_pct_b_21d_5d_diff},
    "lp_drv2_011_frac_within_5pct_min_252d_21d_diff": {"inputs": ["close"], "func": lp_drv2_011_frac_within_5pct_min_252d_21d_diff},
    "lp_drv2_012_stoch_21d_63d_slope": {"inputs": ["close"], "func": lp_drv2_012_stoch_21d_63d_slope},
    "lp_drv2_013_consecutive_252d_lows_5d_diff": {"inputs": ["close"], "func": lp_drv2_013_consecutive_252d_lows_5d_diff},
    "lp_drv2_014_expanding_pct_rank_5d_diff": {"inputs": ["close"], "func": lp_drv2_014_expanding_pct_rank_5d_diff},
    "lp_drv2_015_undercut_depth_252d_5d_diff": {"inputs": ["close"], "func": lp_drv2_015_undercut_depth_252d_5d_diff},
    "lp_drv2_016_dist_atl_pct_change_21d": {"inputs": ["close"], "func": lp_drv2_016_dist_atl_pct_change_21d},
    "lp_drv2_017_new_low_freq_21d_5d_diff": {"inputs": ["close"], "func": lp_drv2_017_new_low_freq_21d_5d_diff},
    "lp_drv2_018_stoch_21d_21d_pct_change": {"inputs": ["close"], "func": lp_drv2_018_stoch_21d_21d_pct_change},
    "lp_drv2_019_min_series_accel_21d": {"inputs": ["close"], "func": lp_drv2_019_min_series_accel_21d},
    "lp_drv2_020_min_series_accel_252d": {"inputs": ["close"], "func": lp_drv2_020_min_series_accel_252d},
    "lp_drv2_021_stoch_inversion_21_252_5d_diff": {"inputs": ["close"], "func": lp_drv2_021_stoch_inversion_21_252_5d_diff},
    "lp_drv2_022_vol_adj_dist_252d_min_5d_diff": {"inputs": ["close"], "func": lp_drv2_022_vol_adj_dist_252d_min_5d_diff},
    "lp_drv2_023_stoch_252d_63d_slope": {"inputs": ["close"], "func": lp_drv2_023_stoch_252d_63d_slope},
    "lp_drv2_024_atl_count_252d_5d_diff": {"inputs": ["close"], "func": lp_drv2_024_atl_count_252d_5d_diff},
    "lp_drv2_025_composite_stoch_5d_diff": {"inputs": ["close"], "func": lp_drv2_025_composite_stoch_5d_diff},
}
