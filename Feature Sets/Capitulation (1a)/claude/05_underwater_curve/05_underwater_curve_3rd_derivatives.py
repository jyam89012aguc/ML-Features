"""
05_underwater_curve — 3rd Derivatives (Features drv3_001 to drv3_025)
Domain: rate of change of 2nd-derivative features (exhaustion / inflection signals)
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


# ── 3rd-derivative feature functions ─────────────────────────────────────────
# Each function re-derives the underlying 2nd-derivative concept, then applies
# an additional .diff(n) to capture inflection / exhaustion signals.

def uw_drv3_001_area_21d_accel_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 5-day-change-of-21d-area (jerk of short-term pain)."""
    base = _rolling_sum(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    vel = base.diff(5)
    return vel.diff(5)


def uw_drv3_002_area_63d_accel_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 21d-velocity of 63d area (jerk of quarterly pain)."""
    base = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    vel = base.diff(_TD_MON)
    return vel.diff(5)


def uw_drv3_003_area_252d_accel_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d-velocity of 252d area (jerk of annual pain)."""
    base = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    vel = base.diff(_TD_QTR)
    return vel.diff(_TD_MON)


def uw_drv3_004_pain_index_21d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 5d-velocity of 21d Pain Index (pain jerk)."""
    base = _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    vel = base.diff(5)
    return vel.diff(5)


def uw_drv3_005_pain_index_252d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of 252d Pain Index (monthly pain deceleration)."""
    base = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_006_ulcer_63d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 5d-velocity of 63d Ulcer Index (Ulcer jerk)."""
    uw = _uw_rolling(close, _TD_QTR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_QTR))
    vel = base.diff(5)
    return vel.diff(5)


def uw_drv3_007_ulcer_252d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of 252d Ulcer Index."""
    uw = _uw_rolling(close, _TD_YEAR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_008_ulcer_ath_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d-velocity of expanding ATH Ulcer Index."""
    uw = _uw_expanding(close)
    base = np.sqrt((uw ** 2).expanding(min_periods=1).mean())
    vel = base.diff(_TD_QTR)
    return vel.diff(_TD_MON)


def uw_drv3_009_area_ath_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of expanding ATH area."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_010_vol_adj_area_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of vol-adjusted 252d area."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    base = _safe_div(area, vol + _EPS)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_011_pain_index_63d_pct_chg_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-pct-change of 63d Pain Index (relative pain acceleration of acceleration)."""
    base = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    vel = base.pct_change(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_012_ulcer_252d_pct_chg_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d-pct-change of 252d Ulcer Index."""
    uw = _uw_rolling(close, _TD_YEAR)
    base = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    vel = base.pct_change(_TD_QTR)
    return vel.diff(_TD_MON)


def uw_drv3_013_area_21d_slope_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d OLS-slope of 21d area (curvature of pain trend)."""
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
    slope = base.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)
    return slope.diff(_TD_MON)


def uw_drv3_014_area_252d_slope_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d OLS-slope of 252d area (annual pain trend curvature)."""
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
    slope = base.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)
    return slope.diff(_TD_MON)


def uw_drv3_015_convexity_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of convexity score (inflection of curve shape)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    mdd = _uw_rolling(close, _TD_YEAR).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    base = _safe_div(area, (_TD_YEAR * mdd) + _EPS)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_016_area_ratio_63_252_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of 63d/252d area ratio."""
    a63 = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    a252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    base = _safe_div(a63, a252 + _EPS)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_017_intensity_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of depth*area intensity."""
    depth = _uw_rolling(close, _TD_YEAR).abs()
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    base = depth * area
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_018_vol_wt_area_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of volume-weighted 252d area."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    base = _rolling_sum(uw * v_norm, _TD_YEAR)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_019_pain_ath_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d-velocity of expanding ATH Pain Index."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).mean()
    vel = base.diff(_TD_QTR)
    return vel.diff(_TD_MON)


def uw_drv3_020_area_log_252d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of log-space 252d area."""
    peak = _rolling_max(close, _TD_YEAR)
    luw = np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS)).abs()
    base = _rolling_sum(luw, _TD_YEAR)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_021_dispersion_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of 252d depth std (dispersion jerk)."""
    base = _rolling_std(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_022_pain_momentum_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-change-in-momentum of 63d Pain Index (4th-order)."""
    pi63 = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    mom = pi63.diff(_TD_MON)
    accel = mom.diff(_TD_MON)
    return accel.diff(_TD_MON)


def uw_drv3_023_area_ath_pct_chg_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 63d-pct-change of ATH area."""
    base = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    vel = base.pct_change(_TD_QTR)
    return vel.diff(_TD_MON)


def uw_drv3_024_ulcer_ratio_accel_21d(close: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of 63d/252d Ulcer ratio."""
    ui63 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_QTR) ** 2, _TD_QTR))
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    base = _safe_div(ui63, ui252 + _EPS)
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


def uw_drv3_025_composite_distress_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in the 21d-velocity of composite distress score (distress jerk)."""
    pi252 = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    area252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ret_vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    vol_adj = _safe_div(area252, ret_vol + _EPS).clip(upper=50)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    vol_wt = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs() * v_norm, _TD_YEAR)
    base = 0.25 * pi252 + 0.25 * ui252 + 0.25 * vol_adj / 50.0 + 0.25 * vol_wt
    vel = base.diff(_TD_MON)
    return vel.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

UNDERWATER_CURVE_REGISTRY_3RD_DERIVATIVES = {
    "uw_drv3_001_area_21d_accel_velocity_5d": {"inputs": ["close"], "func": uw_drv3_001_area_21d_accel_velocity_5d},
    "uw_drv3_002_area_63d_accel_velocity_5d": {"inputs": ["close"], "func": uw_drv3_002_area_63d_accel_velocity_5d},
    "uw_drv3_003_area_252d_accel_velocity_21d": {"inputs": ["close"], "func": uw_drv3_003_area_252d_accel_velocity_21d},
    "uw_drv3_004_pain_index_21d_accel_5d": {"inputs": ["close"], "func": uw_drv3_004_pain_index_21d_accel_5d},
    "uw_drv3_005_pain_index_252d_accel_21d": {"inputs": ["close"], "func": uw_drv3_005_pain_index_252d_accel_21d},
    "uw_drv3_006_ulcer_63d_accel_5d": {"inputs": ["close"], "func": uw_drv3_006_ulcer_63d_accel_5d},
    "uw_drv3_007_ulcer_252d_accel_21d": {"inputs": ["close"], "func": uw_drv3_007_ulcer_252d_accel_21d},
    "uw_drv3_008_ulcer_ath_accel_21d": {"inputs": ["close"], "func": uw_drv3_008_ulcer_ath_accel_21d},
    "uw_drv3_009_area_ath_accel_21d": {"inputs": ["close"], "func": uw_drv3_009_area_ath_accel_21d},
    "uw_drv3_010_vol_adj_area_accel_21d": {"inputs": ["close"], "func": uw_drv3_010_vol_adj_area_accel_21d},
    "uw_drv3_011_pain_index_63d_pct_chg_accel_21d": {"inputs": ["close"], "func": uw_drv3_011_pain_index_63d_pct_chg_accel_21d},
    "uw_drv3_012_ulcer_252d_pct_chg_accel_21d": {"inputs": ["close"], "func": uw_drv3_012_ulcer_252d_pct_chg_accel_21d},
    "uw_drv3_013_area_21d_slope_accel_21d": {"inputs": ["close"], "func": uw_drv3_013_area_21d_slope_accel_21d},
    "uw_drv3_014_area_252d_slope_accel_21d": {"inputs": ["close"], "func": uw_drv3_014_area_252d_slope_accel_21d},
    "uw_drv3_015_convexity_accel_21d": {"inputs": ["close"], "func": uw_drv3_015_convexity_accel_21d},
    "uw_drv3_016_area_ratio_63_252_accel_21d": {"inputs": ["close"], "func": uw_drv3_016_area_ratio_63_252_accel_21d},
    "uw_drv3_017_intensity_accel_21d": {"inputs": ["close"], "func": uw_drv3_017_intensity_accel_21d},
    "uw_drv3_018_vol_wt_area_accel_21d": {"inputs": ["close", "volume"], "func": uw_drv3_018_vol_wt_area_accel_21d},
    "uw_drv3_019_pain_ath_accel_21d": {"inputs": ["close"], "func": uw_drv3_019_pain_ath_accel_21d},
    "uw_drv3_020_area_log_252d_accel_21d": {"inputs": ["close"], "func": uw_drv3_020_area_log_252d_accel_21d},
    "uw_drv3_021_dispersion_accel_21d": {"inputs": ["close"], "func": uw_drv3_021_dispersion_accel_21d},
    "uw_drv3_022_pain_momentum_jerk_21d": {"inputs": ["close"], "func": uw_drv3_022_pain_momentum_jerk_21d},
    "uw_drv3_023_area_ath_pct_chg_accel_21d": {"inputs": ["close"], "func": uw_drv3_023_area_ath_pct_chg_accel_21d},
    "uw_drv3_024_ulcer_ratio_accel_21d": {"inputs": ["close"], "func": uw_drv3_024_ulcer_ratio_accel_21d},
    "uw_drv3_025_composite_distress_accel_21d": {"inputs": ["close", "volume"], "func": uw_drv3_025_composite_distress_accel_21d},
}
