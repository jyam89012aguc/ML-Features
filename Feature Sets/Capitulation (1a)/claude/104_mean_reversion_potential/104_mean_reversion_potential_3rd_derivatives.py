"""
104_mean_reversion_potential — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of the 2nd-derivative mean-reversion features —
        captures the inflection / exhaustion of the loading elastic spring
        (when displacement stops widening and reversion takes over).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _zscore(s: pd.Series, w: int) -> pd.Series:
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _stretch(close: pd.Series, w: int) -> pd.Series:
    return _safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))


def _ar1(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(5, w // 2)).corr(s.shift(1))


def _half_life(phi: pd.Series) -> pd.Series:
    p = phi.clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(2.0) / np.log(p)


def _efficiency_ratio(close: pd.Series, w: int) -> pd.Series:
    net = (close - close.shift(w)).abs()
    path = _rolling_sum(close.diff(1).abs(), w)
    return _safe_div(net, path)


def _variance_ratio(close: pd.Series, q: int, w: int) -> pd.Series:
    lr = _log_safe(close).diff(1)
    lrq = _log_safe(close).diff(q)
    var1 = _rolling_std(lr, w) ** 2
    varq = _rolling_std(lrq, w) ** 2
    return _safe_div(varq, var1 * q)


def _hurst_rs(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 16:
        return np.nan
    m = x.mean()
    dev = np.cumsum(x - m)
    rng = dev.max() - dev.min()
    s = x.std()
    if s <= 0 or rng <= 0:
        return np.nan
    return float(np.log(rng / s) / np.log(n))


def _hurst(close: pd.Series, w: int) -> pd.Series:
    lr = _log_safe(close).diff(1)
    return lr.rolling(w, min_periods=max(16, w // 2)).apply(_hurst_rs, raw=True)


def _accel(s: pd.Series, n: int = 5) -> pd.Series:
    """Second difference: rate of change of the n-day rate of change."""
    return s.diff(n).diff(n)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def mrp_drv3_001_stretch_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day stretch."""
    return _accel(_stretch(close, _TD_QTR))


def mrp_drv3_002_stretch_252d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 252-day stretch."""
    return _accel(_stretch(close, _TD_YEAR))


def mrp_drv3_003_max_stretch_below_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the most negative stretch across horizons."""
    parts = [_stretch(close, w) for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return _accel(pd.concat(parts, axis=1).min(axis=1))


def mrp_drv3_004_reversion_gap_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 126-day equilibrium reversion gap."""
    ma = _rolling_mean(close, _TD_HALF)
    return _accel(_safe_div(ma - close, ma))


def mrp_drv3_005_ar1_returns_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day return autocorrelation."""
    return _accel(_ar1(_daily_ret(close), _TD_QTR))


def mrp_drv3_006_half_life_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day reversion half-life."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return _accel(_half_life(_ar1(detr, _TD_QTR)))


def mrp_drv3_007_pct_b_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day Bollinger %B."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    return _accel(_safe_div(close - (ma - 2.0 * sd), 4.0 * sd))


def mrp_drv3_008_band_overshoot_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day below-band overshoot magnitude."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    return _accel(overshoot)


def mrp_drv3_009_hurst_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day Hurst exponent."""
    return _accel(_hurst(close, _TD_QTR))


def mrp_drv3_010_efficiency_ratio_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day Kaufman efficiency ratio."""
    return _accel(_efficiency_ratio(close, _TD_QTR))


def mrp_drv3_011_variance_ratio_5_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the VR(5) variance ratio over a 252-day window."""
    return _accel(_variance_ratio(close, 5, _TD_YEAR))


def mrp_drv3_012_distance_below_mean_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the percent distance below the 252-day mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _accel(_safe_div(close - ma, ma).clip(upper=0))


def mrp_drv3_013_reversion_potential_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the reversion potential score."""
    z = _stretch(close, _TD_QTR)
    score = (-z).clip(lower=0) * (1.0 - _ar1(close, _TD_QTR)).clip(lower=0)
    return _accel(score)


def mrp_drv3_014_elastic_tension_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the elastic tension (signed squared stretch)."""
    s = _stretch(close, _TD_QTR)
    return _accel(-(s.clip(upper=0) ** 2))


def mrp_drv3_015_stretch_zscore_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 252-day z-score of the 63-day stretch."""
    return _accel(_zscore(_stretch(close, _TD_QTR), _TD_YEAR))


def mrp_drv3_016_distance_from_vwap_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the deviation from the 63-day volume-weighted price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _accel(_safe_div(close - vwap, vwap))


def mrp_drv3_017_mean_reversion_strength_accel(close: pd.Series) -> pd.Series:
    """Acceleration of mean-reversion strength."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return _accel(-_ar1(detr, _TD_QTR))


def mrp_drv3_018_below_lower_bollinger_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the distance below the 63-day lower Bollinger band."""
    return _accel((_stretch(close, _TD_QTR) + 2.0).clip(upper=0))


def mrp_drv3_019_cumulative_deviation_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63-day cumulative deviation from the mean."""
    ma = _rolling_mean(close, _TD_QTR)
    return _accel(_rolling_sum(_safe_div(close - ma, ma), _TD_QTR))


def mrp_drv3_020_reversion_capitulation_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the mean-reversion capitulation composite score."""
    z = _stretch(close, _TD_QTR)
    overshoot = (-z).clip(lower=0) / 3.0
    below = _rolling_mean((close < _rolling_mean(close, _TD_YEAR)).astype(float), _TD_YEAR)
    detr = close - _rolling_mean(close, _TD_QTR)
    strength = (-_ar1(detr, _TD_QTR)).clip(lower=0)
    return _accel(overshoot * (0.5 + below) * (0.5 + strength))


def mrp_drv3_021_stretch_63d_21d_accel(close: pd.Series) -> pd.Series:
    """21-day-horizon acceleration of the 63-day stretch."""
    return _accel(_stretch(close, _TD_QTR), _TD_MON)


def mrp_drv3_022_master_index_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the master mean-reversion potential index."""
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close,
                    _rolling_mean(close, _TD_HALF)).clip(lower=0)
    overshoot = (-_stretch(close, _TD_QTR)).clip(lower=0) / 3.0
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0, upper=2.0) / 2.0
    return _accel((gap + overshoot) * (0.5 + speed))


def mrp_drv3_023_ou_theta_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the Ornstein-Uhlenbeck reversion rate theta."""
    detr = close - _rolling_mean(close, _TD_QTR)
    phi = _ar1(detr, _TD_QTR).clip(lower=_EPS, upper=1 - 1e-4)
    return _accel(-np.log(phi))


def mrp_drv3_024_efficiency_ratio_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 21-day Kaufman efficiency ratio."""
    return _accel(_efficiency_ratio(close, _TD_MON))


def mrp_drv3_025_displacement_from_median_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the percent displacement from the 252-day median."""
    med = close.rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return _accel(_safe_div(close - med, med))


# ── Registry ──────────────────────────────────────────────────────────────────

MEAN_REVERSION_POTENTIAL_REGISTRY_3RD_DERIVATIVES = {
    "mrp_drv3_001_stretch_63d_accel": {"inputs": ["close"], "func": mrp_drv3_001_stretch_63d_accel},
    "mrp_drv3_002_stretch_252d_accel": {"inputs": ["close"], "func": mrp_drv3_002_stretch_252d_accel},
    "mrp_drv3_003_max_stretch_below_accel": {"inputs": ["close"], "func": mrp_drv3_003_max_stretch_below_accel},
    "mrp_drv3_004_reversion_gap_accel": {"inputs": ["close"], "func": mrp_drv3_004_reversion_gap_accel},
    "mrp_drv3_005_ar1_returns_63d_accel": {"inputs": ["close"], "func": mrp_drv3_005_ar1_returns_63d_accel},
    "mrp_drv3_006_half_life_63d_accel": {"inputs": ["close"], "func": mrp_drv3_006_half_life_63d_accel},
    "mrp_drv3_007_pct_b_63d_accel": {"inputs": ["close"], "func": mrp_drv3_007_pct_b_63d_accel},
    "mrp_drv3_008_band_overshoot_accel": {"inputs": ["close"], "func": mrp_drv3_008_band_overshoot_accel},
    "mrp_drv3_009_hurst_63d_accel": {"inputs": ["close"], "func": mrp_drv3_009_hurst_63d_accel},
    "mrp_drv3_010_efficiency_ratio_63d_accel": {"inputs": ["close"], "func": mrp_drv3_010_efficiency_ratio_63d_accel},
    "mrp_drv3_011_variance_ratio_5_accel": {"inputs": ["close"], "func": mrp_drv3_011_variance_ratio_5_accel},
    "mrp_drv3_012_distance_below_mean_accel": {"inputs": ["close"], "func": mrp_drv3_012_distance_below_mean_accel},
    "mrp_drv3_013_reversion_potential_score_accel": {"inputs": ["close"], "func": mrp_drv3_013_reversion_potential_score_accel},
    "mrp_drv3_014_elastic_tension_accel": {"inputs": ["close"], "func": mrp_drv3_014_elastic_tension_accel},
    "mrp_drv3_015_stretch_zscore_accel": {"inputs": ["close"], "func": mrp_drv3_015_stretch_zscore_accel},
    "mrp_drv3_016_distance_from_vwap_accel": {"inputs": ["close", "volume"], "func": mrp_drv3_016_distance_from_vwap_accel},
    "mrp_drv3_017_mean_reversion_strength_accel": {"inputs": ["close"], "func": mrp_drv3_017_mean_reversion_strength_accel},
    "mrp_drv3_018_below_lower_bollinger_accel": {"inputs": ["close"], "func": mrp_drv3_018_below_lower_bollinger_accel},
    "mrp_drv3_019_cumulative_deviation_accel": {"inputs": ["close"], "func": mrp_drv3_019_cumulative_deviation_accel},
    "mrp_drv3_020_reversion_capitulation_score_accel": {"inputs": ["close"], "func": mrp_drv3_020_reversion_capitulation_score_accel},
    "mrp_drv3_021_stretch_63d_21d_accel": {"inputs": ["close"], "func": mrp_drv3_021_stretch_63d_21d_accel},
    "mrp_drv3_022_master_index_accel": {"inputs": ["close"], "func": mrp_drv3_022_master_index_accel},
    "mrp_drv3_023_ou_theta_accel": {"inputs": ["close"], "func": mrp_drv3_023_ou_theta_accel},
    "mrp_drv3_024_efficiency_ratio_21d_accel": {"inputs": ["close"], "func": mrp_drv3_024_efficiency_ratio_21d_accel},
    "mrp_drv3_025_displacement_from_median_accel": {"inputs": ["close"], "func": mrp_drv3_025_displacement_from_median_accel},
}
