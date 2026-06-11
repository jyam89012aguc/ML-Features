"""
104_mean_reversion_potential — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base mean-reversion-potential features — captures
        how fast the equilibrium gap, overshoot and reversion structure are
        building (the loading of the elastic spring).
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def mrp_drv2_001_stretch_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day stretch (speed of equilibrium displacement)."""
    return _stretch(close, _TD_QTR).diff(5)


def mrp_drv2_002_stretch_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 252-day stretch."""
    return _stretch(close, _TD_YEAR).diff(5)


def mrp_drv2_003_max_stretch_below_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the most negative stretch across horizons."""
    parts = [_stretch(close, w) for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).min(axis=1).diff(5)


def mrp_drv2_004_reversion_gap_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 126-day equilibrium reversion gap."""
    ma = _rolling_mean(close, _TD_HALF)
    return _safe_div(ma - close, ma).diff(5)


def mrp_drv2_005_ar1_returns_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day return autocorrelation."""
    return _ar1(_daily_ret(close), _TD_QTR).diff(5)


def mrp_drv2_006_half_life_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day reversion half-life."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return _half_life(_ar1(detr, _TD_QTR)).diff(5)


def mrp_drv2_007_pct_b_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day Bollinger %B."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd).diff(5)


def mrp_drv2_008_band_overshoot_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day below-band overshoot magnitude."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    return overshoot.diff(5)


def mrp_drv2_009_hurst_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day Hurst exponent."""
    return _hurst(close, _TD_QTR).diff(5)


def mrp_drv2_010_efficiency_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day Kaufman efficiency ratio."""
    return _efficiency_ratio(close, _TD_QTR).diff(5)


def mrp_drv2_011_variance_ratio_5_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the VR(5) variance ratio over a 252-day window."""
    return _variance_ratio(close, 5, _TD_YEAR).diff(5)


def mrp_drv2_012_distance_below_mean_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the percent distance below the 252-day mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(close - ma, ma).clip(upper=0).diff(5)


def mrp_drv2_013_reversion_potential_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the reversion potential score (overshoot x speed)."""
    z = _stretch(close, _TD_QTR)
    score = (-z).clip(lower=0) * (1.0 - _ar1(close, _TD_QTR)).clip(lower=0)
    return score.diff(5)


def mrp_drv2_014_elastic_tension_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the elastic tension (signed squared stretch)."""
    s = _stretch(close, _TD_QTR)
    return (-(s.clip(upper=0) ** 2)).diff(5)


def mrp_drv2_015_stretch_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 252-day z-score of the 63-day stretch."""
    return _zscore(_stretch(close, _TD_QTR), _TD_YEAR).diff(5)


def mrp_drv2_016_distance_from_vwap_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the deviation from the 63-day volume-weighted mean price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _safe_div(close - vwap, vwap).diff(5)


def mrp_drv2_017_mean_reversion_strength_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of mean-reversion strength (negative detrended-price AR1)."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return (-_ar1(detr, _TD_QTR)).diff(5)


def mrp_drv2_018_below_lower_bollinger_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the distance below the 63-day lower Bollinger band."""
    return (_stretch(close, _TD_QTR) + 2.0).clip(upper=0).diff(5)


def mrp_drv2_019_cumulative_deviation_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day cumulative deviation from the mean."""
    ma = _rolling_mean(close, _TD_QTR)
    return _rolling_sum(_safe_div(close - ma, ma), _TD_QTR).diff(5)


def mrp_drv2_020_reversion_capitulation_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the mean-reversion capitulation composite score."""
    z = _stretch(close, _TD_QTR)
    overshoot = (-z).clip(lower=0) / 3.0
    below = _rolling_mean((close < _rolling_mean(close, _TD_YEAR)).astype(float), _TD_YEAR)
    detr = close - _rolling_mean(close, _TD_QTR)
    strength = (-_ar1(detr, _TD_QTR)).clip(lower=0)
    return (overshoot * (0.5 + below) * (0.5 + strength)).diff(5)


def mrp_drv2_021_stretch_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 63-day stretch (monthly displacement pace)."""
    return _stretch(close, _TD_QTR).diff(_TD_MON)


def mrp_drv2_022_master_index_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the master mean-reversion potential index."""
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close,
                    _rolling_mean(close, _TD_HALF)).clip(lower=0)
    overshoot = (-_stretch(close, _TD_QTR)).clip(lower=0) / 3.0
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0, upper=2.0) / 2.0
    return ((gap + overshoot) * (0.5 + speed)).diff(5)


def mrp_drv2_023_ou_theta_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the Ornstein-Uhlenbeck reversion rate theta."""
    detr = close - _rolling_mean(close, _TD_QTR)
    phi = _ar1(detr, _TD_QTR).clip(lower=_EPS, upper=1 - 1e-4)
    return (-np.log(phi)).diff(5)


def mrp_drv2_024_overshoot_below_atr_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the Keltner lower-channel overshoot in ATR units."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(),
                    (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_QTR)
    pos = _safe_div(close - _rolling_mean(close, _TD_QTR), atr)
    return (-(pos + 2.0)).clip(lower=0).diff(5)


def mrp_drv2_025_displacement_from_median_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the percent displacement from the 252-day median."""
    med = close.rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return _safe_div(close - med, med).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

MEAN_REVERSION_POTENTIAL_REGISTRY_2ND_DERIVATIVES = {
    "mrp_drv2_001_stretch_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_001_stretch_63d_5d_diff},
    "mrp_drv2_002_stretch_252d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_002_stretch_252d_5d_diff},
    "mrp_drv2_003_max_stretch_below_5d_diff": {"inputs": ["close"], "func": mrp_drv2_003_max_stretch_below_5d_diff},
    "mrp_drv2_004_reversion_gap_5d_diff": {"inputs": ["close"], "func": mrp_drv2_004_reversion_gap_5d_diff},
    "mrp_drv2_005_ar1_returns_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_005_ar1_returns_63d_5d_diff},
    "mrp_drv2_006_half_life_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_006_half_life_63d_5d_diff},
    "mrp_drv2_007_pct_b_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_007_pct_b_63d_5d_diff},
    "mrp_drv2_008_band_overshoot_5d_diff": {"inputs": ["close"], "func": mrp_drv2_008_band_overshoot_5d_diff},
    "mrp_drv2_009_hurst_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_009_hurst_63d_5d_diff},
    "mrp_drv2_010_efficiency_ratio_63d_5d_diff": {"inputs": ["close"], "func": mrp_drv2_010_efficiency_ratio_63d_5d_diff},
    "mrp_drv2_011_variance_ratio_5_5d_diff": {"inputs": ["close"], "func": mrp_drv2_011_variance_ratio_5_5d_diff},
    "mrp_drv2_012_distance_below_mean_5d_diff": {"inputs": ["close"], "func": mrp_drv2_012_distance_below_mean_5d_diff},
    "mrp_drv2_013_reversion_potential_score_5d_diff": {"inputs": ["close"], "func": mrp_drv2_013_reversion_potential_score_5d_diff},
    "mrp_drv2_014_elastic_tension_5d_diff": {"inputs": ["close"], "func": mrp_drv2_014_elastic_tension_5d_diff},
    "mrp_drv2_015_stretch_zscore_5d_diff": {"inputs": ["close"], "func": mrp_drv2_015_stretch_zscore_5d_diff},
    "mrp_drv2_016_distance_from_vwap_5d_diff": {"inputs": ["close", "volume"], "func": mrp_drv2_016_distance_from_vwap_5d_diff},
    "mrp_drv2_017_mean_reversion_strength_5d_diff": {"inputs": ["close"], "func": mrp_drv2_017_mean_reversion_strength_5d_diff},
    "mrp_drv2_018_below_lower_bollinger_5d_diff": {"inputs": ["close"], "func": mrp_drv2_018_below_lower_bollinger_5d_diff},
    "mrp_drv2_019_cumulative_deviation_5d_diff": {"inputs": ["close"], "func": mrp_drv2_019_cumulative_deviation_5d_diff},
    "mrp_drv2_020_reversion_capitulation_score_5d_diff": {"inputs": ["close"], "func": mrp_drv2_020_reversion_capitulation_score_5d_diff},
    "mrp_drv2_021_stretch_63d_21d_diff": {"inputs": ["close"], "func": mrp_drv2_021_stretch_63d_21d_diff},
    "mrp_drv2_022_master_index_5d_diff": {"inputs": ["close"], "func": mrp_drv2_022_master_index_5d_diff},
    "mrp_drv2_023_ou_theta_5d_diff": {"inputs": ["close"], "func": mrp_drv2_023_ou_theta_5d_diff},
    "mrp_drv2_024_overshoot_below_atr_5d_diff": {"inputs": ["close", "high", "low"], "func": mrp_drv2_024_overshoot_below_atr_5d_diff},
    "mrp_drv2_025_displacement_from_median_5d_diff": {"inputs": ["close"], "func": mrp_drv2_025_displacement_from_median_5d_diff},
}
