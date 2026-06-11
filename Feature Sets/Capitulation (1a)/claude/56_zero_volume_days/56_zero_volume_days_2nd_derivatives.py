"""
56_zero_volume_days — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base zero-volume / stale-price features
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — velocity of dead-session frequency and streak behavior
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
_NEAR_ZERO_K = 0.05
_STALE_TOL = 1e-8

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _zero_vol_flag(volume: pd.Series) -> pd.Series:
    return (volume == 0).astype(float)


def _near_zero_vol_flag(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    med = _rolling_median(volume.shift(1), w)
    return (volume < _NEAR_ZERO_K * med.clip(lower=_EPS)).astype(float)


def _stale_price_flag(close: pd.Series) -> pd.Series:
    return (close.diff(1).abs() < _STALE_TOL).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def zvd_drv2_001_zero_vol_frac_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day zero-volume fraction (velocity of dead-session rate)."""
    frac = _rolling_count_true(volume == 0, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def zvd_drv2_002_zero_vol_frac_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day zero-volume fraction (monthly velocity)."""
    frac = _rolling_count_true(volume == 0, _TD_MON) / _TD_MON
    return frac.diff(_TD_MON)


def zvd_drv2_003_stale_price_frac_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day stale-price fraction."""
    frac = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def zvd_drv2_004_stale_price_frac_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day stale-price fraction."""
    frac = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    return frac.diff(_TD_MON)


def zvd_drv2_005_near_zero_frac_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day near-zero-volume fraction."""
    frac = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def zvd_drv2_006_dead_session_frac_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day dead-session fraction (zero-vol OR stale)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    frac = _rolling_sum(dead, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def zvd_drv2_007_dead_session_frac_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day dead-session fraction."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    frac = _rolling_sum(dead, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def zvd_drv2_008_consec_stale_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current stale-price streak length."""
    streak = _consec_streak(_stale_price_flag(close) == 1)
    return streak.diff(_TD_WEEK)


def zvd_drv2_009_consec_near_zero_streak_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of current near-zero-volume streak length."""
    streak = _consec_streak(_near_zero_vol_flag(volume, _TD_MON) == 1)
    return streak.diff(_TD_WEEK)


def zvd_drv2_010_near_zero_frac_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day near-zero-volume fraction."""
    frac = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def zvd_drv2_011_vol_pct_median_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of volume-as-pct-of-21d-trailing-median."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    ratio = _safe_div(volume, med.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def zvd_drv2_012_vol_zscore_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume z-score."""
    mu = _rolling_mean(volume.shift(1), _TD_QTR)
    sigma = _rolling_std(volume.shift(1), _TD_QTR)
    z = _safe_div(volume - mu, sigma)
    return z.diff(_TD_WEEK)


def zvd_drv2_013_stale_count_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day stale-price count."""
    cnt = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON)
    return _linslope(cnt, _TD_QTR)


def zvd_drv2_014_near_zero_count_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day near-zero-vol count."""
    cnt = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON)
    return _linslope(cnt, _TD_QTR)


def zvd_drv2_015_dead_session_frac_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day dead-session fraction."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    frac = _rolling_sum(dead, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_QTR)


def zvd_drv2_016_zero_vol_frac_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day zero-volume fraction."""
    frac = _rolling_count_true(volume == 0, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def zvd_drv2_017_stale_frac_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day stale-price fraction."""
    frac = _rolling_count_true(_stale_price_flag(close) == 1, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def zvd_drv2_018_ewm_dead_session_21_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 dead-session rate."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    ewm = _ewm_mean(dead, _TD_MON)
    return ewm.diff(_TD_WEEK)


def zvd_drv2_019_near_zero_ewm21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 near-zero-volume rate."""
    nz = _near_zero_vol_flag(volume, _TD_MON)
    return _ewm_mean(nz, _TD_MON).diff(_TD_WEEK)


def zvd_drv2_020_stale_ewm21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 stale-price rate."""
    return _ewm_mean(_stale_price_flag(close), _TD_MON).diff(_TD_WEEK)


def zvd_drv2_021_dead_session_composite_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of composite dead-session score (21d fracs of zero+stale+near-zero)."""
    zvf = _rolling_count_true(volume == 0, _TD_MON) / _TD_MON
    spf = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    nzf = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    score = zvf + spf + nzf
    return score.diff(_TD_WEEK)


def zvd_drv2_022_dead_session_composite_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of composite dead-session score."""
    zvf = _rolling_count_true(volume == 0, _TD_MON) / _TD_MON
    spf = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    nzf = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    score = zvf + spf + nzf
    return score.diff(_TD_MON)


def zvd_drv2_023_near_zero_frac_21d_zscore_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of z-scored 21-day near-zero fraction (accelerating extremity)."""
    frac = _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON) / _TD_MON
    mu = _rolling_mean(frac, _TD_YEAR)
    sigma = _rolling_std(frac, _TD_YEAR)
    z = _safe_div(frac - mu, sigma)
    return z.diff(_TD_WEEK)


def zvd_drv2_024_stale_frac_21d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-scored 21-day stale-price fraction."""
    frac = _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON) / _TD_MON
    mu = _rolling_mean(frac, _TD_YEAR)
    sigma = _rolling_std(frac, _TD_YEAR)
    z = _safe_div(frac - mu, sigma)
    return z.diff(_TD_WEEK)


def zvd_drv2_025_dead_session_frac_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day dead-session fraction."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    frac = _rolling_sum(dead, _TD_MON) / _TD_MON
    return frac.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

ZERO_VOLUME_DAYS_REGISTRY_2ND_DERIVATIVES = {
    "zvd_drv2_001_zero_vol_frac_21d_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_001_zero_vol_frac_21d_5d_diff},
    "zvd_drv2_002_zero_vol_frac_21d_21d_diff": {"inputs": ["volume"], "func": zvd_drv2_002_zero_vol_frac_21d_21d_diff},
    "zvd_drv2_003_stale_price_frac_21d_5d_diff": {"inputs": ["close"], "func": zvd_drv2_003_stale_price_frac_21d_5d_diff},
    "zvd_drv2_004_stale_price_frac_21d_21d_diff": {"inputs": ["close"], "func": zvd_drv2_004_stale_price_frac_21d_21d_diff},
    "zvd_drv2_005_near_zero_frac_21d_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_005_near_zero_frac_21d_5d_diff},
    "zvd_drv2_006_dead_session_frac_21d_5d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_006_dead_session_frac_21d_5d_diff},
    "zvd_drv2_007_dead_session_frac_63d_21d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_007_dead_session_frac_63d_21d_diff},
    "zvd_drv2_008_consec_stale_streak_5d_diff": {"inputs": ["close"], "func": zvd_drv2_008_consec_stale_streak_5d_diff},
    "zvd_drv2_009_consec_near_zero_streak_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_009_consec_near_zero_streak_5d_diff},
    "zvd_drv2_010_near_zero_frac_63d_21d_diff": {"inputs": ["volume"], "func": zvd_drv2_010_near_zero_frac_63d_21d_diff},
    "zvd_drv2_011_vol_pct_median_21d_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_011_vol_pct_median_21d_5d_diff},
    "zvd_drv2_012_vol_zscore_63d_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_012_vol_zscore_63d_5d_diff},
    "zvd_drv2_013_stale_count_21d_slope_63d": {"inputs": ["close"], "func": zvd_drv2_013_stale_count_21d_slope_63d},
    "zvd_drv2_014_near_zero_count_21d_slope_63d": {"inputs": ["volume"], "func": zvd_drv2_014_near_zero_count_21d_slope_63d},
    "zvd_drv2_015_dead_session_frac_21d_slope_63d": {"inputs": ["close", "volume"], "func": zvd_drv2_015_dead_session_frac_21d_slope_63d},
    "zvd_drv2_016_zero_vol_frac_252d_21d_diff": {"inputs": ["volume"], "func": zvd_drv2_016_zero_vol_frac_252d_21d_diff},
    "zvd_drv2_017_stale_frac_252d_21d_diff": {"inputs": ["close"], "func": zvd_drv2_017_stale_frac_252d_21d_diff},
    "zvd_drv2_018_ewm_dead_session_21_5d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_018_ewm_dead_session_21_5d_diff},
    "zvd_drv2_019_near_zero_ewm21_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_019_near_zero_ewm21_5d_diff},
    "zvd_drv2_020_stale_ewm21_5d_diff": {"inputs": ["close"], "func": zvd_drv2_020_stale_ewm21_5d_diff},
    "zvd_drv2_021_dead_session_composite_5d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_021_dead_session_composite_5d_diff},
    "zvd_drv2_022_dead_session_composite_21d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_022_dead_session_composite_21d_diff},
    "zvd_drv2_023_near_zero_frac_21d_zscore_5d_diff": {"inputs": ["volume"], "func": zvd_drv2_023_near_zero_frac_21d_zscore_5d_diff},
    "zvd_drv2_024_stale_frac_21d_zscore_5d_diff": {"inputs": ["close"], "func": zvd_drv2_024_stale_frac_21d_zscore_5d_diff},
    "zvd_drv2_025_dead_session_frac_21d_21d_diff": {"inputs": ["close", "volume"], "func": zvd_drv2_025_dead_session_frac_21d_21d_diff},
}
