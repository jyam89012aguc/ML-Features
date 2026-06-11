"""
05_underwater_curve — 2nd Derivatives (Features drv2_001 to drv2_025)
Domain: rate of change of base underwater-area features (acceleration of decline)
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Underwater series vs rolling w-day peak: (close/peak - 1), <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _uw_expanding(close: pd.Series) -> pd.Series:
    """Underwater series vs all-time expanding high: (close/ATH - 1), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Average True Range over w days."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


# ── 2nd-derivative feature functions ─────────────────────────────────────────
# Each function computes a base underwater-area concept, then applies .diff(n)
# to capture the VELOCITY / RATE-OF-CHANGE of that pain metric.

def uw_drv2_001_area_21d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in 21-day underwater area (short-term pain accumulation rate)."""
    base = _rolling_sum(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    return base.diff(5)


def uw_drv2_002_area_63d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 63-day underwater area (monthly pain growth rate)."""
    base = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return base.diff(_TD_MON)


def uw_drv2_003_area_252d_velocity_63d(close: pd.Series) -> pd.Series:
    """63-day change in 252-day underwater area (quarterly accumulation rate)."""
    base = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return base.diff(_TD_QTR)


def uw_drv2_004_pain_index_21d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in 21-day Pain Index (short-term mean-depth acceleration)."""
    base = _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    return base.diff(5)


def uw_drv2_005_pain_index_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252-day Pain Index (monthly deepening of annual pain)."""
    base = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return base.diff(_TD_MON)


def uw_drv2_006_ulcer_index_63d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in 63-day Ulcer Index (weekly Ulcer acceleration)."""
    uw = _uw_rolling(close, _TD_QTR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_QTR))
    return base.diff(5)


def uw_drv2_007_ulcer_index_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252-day Ulcer Index (monthly Ulcer acceleration)."""
    uw = _uw_rolling(close, _TD_YEAR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    return base.diff(_TD_MON)


def uw_drv2_008_ulcer_index_ath_velocity_63d(close: pd.Series) -> pd.Series:
    """63-day change in expanding ATH Ulcer Index (quarterly ATH distress growth)."""
    uw = _uw_expanding(close)
    base = np.sqrt((uw ** 2).expanding(min_periods=1).mean())
    return base.diff(_TD_QTR)


def uw_drv2_009_area_ath_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in expanding ATH area (monthly all-time pain rate)."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    return base.diff(_TD_MON)


def uw_drv2_010_vol_adj_area_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in vol-adjusted 252d area (momentum of volatility-normalized pain)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    base = _safe_div(area, vol + _EPS)
    return base.diff(_TD_MON)


def uw_drv2_011_pain_index_63d_pct_change_21d(close: pd.Series) -> pd.Series:
    """21-day percent change in 63-day Pain Index (relative acceleration)."""
    base = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return base.pct_change(_TD_MON)


def uw_drv2_012_ulcer_index_252d_pct_change_63d(close: pd.Series) -> pd.Series:
    """63-day percent change in 252-day Ulcer Index."""
    uw = _uw_rolling(close, _TD_YEAR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    return base.pct_change(_TD_QTR)


def uw_drv2_013_area_21d_slope_21d(close: pd.Series) -> pd.Series:
    """21-day OLS slope of the 21-day rolling area series (trend in short-term pain)."""
    base = _rolling_sum(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    n = _TD_MON
    def _slope(y: np.ndarray) -> float:
        m = len(y)
        if m < 2:
            return float('nan')
        xx = np.arange(m, dtype=float)
        xm, ym = xx.mean(), y.mean()
        den = float(np.sum((xx - xm) ** 2))
        return float(np.sum((xx - xm) * (y - ym))) / den if abs(den) > _EPS else float('nan')
    return base.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)


def uw_drv2_014_area_252d_slope_63d(close: pd.Series) -> pd.Series:
    """63-day OLS slope of the 252-day rolling area series."""
    base = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    n = _TD_QTR
    def _slope(y: np.ndarray) -> float:
        m = len(y)
        if m < 2:
            return float('nan')
        xx = np.arange(m, dtype=float)
        xm, ym = xx.mean(), y.mean()
        den = float(np.sum((xx - xm) ** 2))
        return float(np.sum((xx - xm) * (y - ym))) / den if abs(den) > _EPS else float('nan')
    return base.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)


def uw_drv2_015_convexity_score_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d area/convexity score (deepening or flattening of curve)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    mdd = _uw_rolling(close, _TD_YEAR).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    base = _safe_div(area, (_TD_YEAR * mdd) + _EPS)
    return base.diff(_TD_MON)


def uw_drv2_016_area_63d_vs_252d_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 63d/252d area ratio (acute vs chronic pain shift rate)."""
    a63 = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    a252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    base = _safe_div(a63, a252 + _EPS)
    return base.diff(_TD_MON)


def uw_drv2_017_intensity_depth_x_area_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in depth*area product over 252d (intensity acceleration)."""
    depth = _uw_rolling(close, _TD_YEAR).abs()
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    base = depth * area
    return base.diff(_TD_MON)


def uw_drv2_018_volume_weighted_area_252d_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in volume-weighted 252d area (volume-amplified pain growth)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    base = _rolling_sum(uw * v_norm, _TD_YEAR)
    return base.diff(_TD_MON)


def uw_drv2_019_pain_index_ath_velocity_63d(close: pd.Series) -> pd.Series:
    """63-day change in expanding ATH Pain Index."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).mean()
    return base.diff(_TD_QTR)


def uw_drv2_020_area_log_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in log-space 252d underwater area."""
    peak = _rolling_max(close, _TD_YEAR)
    luw = np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS)).abs()
    base = _rolling_sum(luw, _TD_YEAR)
    return base.diff(_TD_MON)


def uw_drv2_021_area_dispersion_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d depth std (widening/narrowing of pain distribution)."""
    base = _rolling_std(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return base.diff(_TD_MON)


def uw_drv2_022_pain_momentum_63d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 63d Pain Index momentum (jerk of pain)."""
    pi63 = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    base = pi63.diff(_TD_MON)
    return base.diff(_TD_MON)


def uw_drv2_023_area_ath_pct_change_63d(close: pd.Series) -> pd.Series:
    """63-day percent change in expanding ATH area (acceleration relative to level)."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    return base.pct_change(_TD_QTR)


def uw_drv2_024_ulcer_63d_vs_252d_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in ratio of 63d to 252d Ulcer Index (short vs long severity shift)."""
    ui63 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_QTR) ** 2, _TD_QTR))
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    base = _safe_div(ui63, ui252 + _EPS)
    return base.diff(_TD_MON)


def uw_drv2_025_composite_distress_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in composite distress score (multi-factor pain acceleration)."""
    pi252 = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    area252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ret_vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    vol_adj = _safe_div(area252, ret_vol + _EPS).clip(upper=50)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    vol_wt = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs() * v_norm, _TD_YEAR)
    base = 0.25 * pi252 + 0.25 * ui252 + 0.25 * vol_adj / 50.0 + 0.25 * vol_wt
    return base.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

UNDERWATER_CURVE_REGISTRY_2ND_DERIVATIVES = {
    "uw_drv2_001_area_21d_velocity_5d": {"inputs": ["close"], "func": uw_drv2_001_area_21d_velocity_5d},
    "uw_drv2_002_area_63d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_002_area_63d_velocity_21d},
    "uw_drv2_003_area_252d_velocity_63d": {"inputs": ["close"], "func": uw_drv2_003_area_252d_velocity_63d},
    "uw_drv2_004_pain_index_21d_velocity_5d": {"inputs": ["close"], "func": uw_drv2_004_pain_index_21d_velocity_5d},
    "uw_drv2_005_pain_index_252d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_005_pain_index_252d_velocity_21d},
    "uw_drv2_006_ulcer_index_63d_velocity_5d": {"inputs": ["close"], "func": uw_drv2_006_ulcer_index_63d_velocity_5d},
    "uw_drv2_007_ulcer_index_252d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_007_ulcer_index_252d_velocity_21d},
    "uw_drv2_008_ulcer_index_ath_velocity_63d": {"inputs": ["close"], "func": uw_drv2_008_ulcer_index_ath_velocity_63d},
    "uw_drv2_009_area_ath_velocity_21d": {"inputs": ["close"], "func": uw_drv2_009_area_ath_velocity_21d},
    "uw_drv2_010_vol_adj_area_252d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_010_vol_adj_area_252d_velocity_21d},
    "uw_drv2_011_pain_index_63d_pct_change_21d": {"inputs": ["close"], "func": uw_drv2_011_pain_index_63d_pct_change_21d},
    "uw_drv2_012_ulcer_index_252d_pct_change_63d": {"inputs": ["close"], "func": uw_drv2_012_ulcer_index_252d_pct_change_63d},
    "uw_drv2_013_area_21d_slope_21d": {"inputs": ["close"], "func": uw_drv2_013_area_21d_slope_21d},
    "uw_drv2_014_area_252d_slope_63d": {"inputs": ["close"], "func": uw_drv2_014_area_252d_slope_63d},
    "uw_drv2_015_convexity_score_velocity_21d": {"inputs": ["close"], "func": uw_drv2_015_convexity_score_velocity_21d},
    "uw_drv2_016_area_63d_vs_252d_ratio_velocity_21d": {"inputs": ["close"], "func": uw_drv2_016_area_63d_vs_252d_ratio_velocity_21d},
    "uw_drv2_017_intensity_depth_x_area_252d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_017_intensity_depth_x_area_252d_velocity_21d},
    "uw_drv2_018_volume_weighted_area_252d_velocity_21d": {"inputs": ["close", "volume"], "func": uw_drv2_018_volume_weighted_area_252d_velocity_21d},
    "uw_drv2_019_pain_index_ath_velocity_63d": {"inputs": ["close"], "func": uw_drv2_019_pain_index_ath_velocity_63d},
    "uw_drv2_020_area_log_252d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_020_area_log_252d_velocity_21d},
    "uw_drv2_021_area_dispersion_velocity_21d": {"inputs": ["close"], "func": uw_drv2_021_area_dispersion_velocity_21d},
    "uw_drv2_022_pain_momentum_63d_velocity_21d": {"inputs": ["close"], "func": uw_drv2_022_pain_momentum_63d_velocity_21d},
    "uw_drv2_023_area_ath_pct_change_63d": {"inputs": ["close"], "func": uw_drv2_023_area_ath_pct_change_63d},
    "uw_drv2_024_ulcer_63d_vs_252d_ratio_velocity_21d": {"inputs": ["close"], "func": uw_drv2_024_ulcer_63d_vs_252d_ratio_velocity_21d},
    "uw_drv2_025_composite_distress_velocity_21d": {"inputs": ["close", "volume"], "func": uw_drv2_025_composite_distress_velocity_21d},
}
