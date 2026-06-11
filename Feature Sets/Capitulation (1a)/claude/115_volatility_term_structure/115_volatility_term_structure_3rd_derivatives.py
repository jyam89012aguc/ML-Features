"""
115_volatility_term_structure — 3rd Derivatives (Features vts_drv3_001-025)
Domain: rate of change of 2nd-derivative vol term-structure features — acceleration
        of vol-curve ratio velocity, spread widening jerk, curve slope acceleration.
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


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (std of log-returns) over w days."""
    lr = np.log(close / close.shift(1))
    rv = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return rv * np.sqrt(_TD_YEAR)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (NaN-safe)."""
    def _slope(x):
        v = x[~np.isnan(x)]
        if len(v) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(v), dtype=float)
        xi_m = xi.mean()
        x_m = v.mean()
        num = ((xi - xi_m) * (v - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vts_drv3_001_rv5d_rv21d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/21d vol ratio (acceleration of short-end tilt velocity)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_002_rv21d_rv63d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/63d vol ratio (acceleration of mid-curve tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_003_rv63d_rv252d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d/252d vol ratio (back-end tilt acceleration)."""
    ratio = _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_004_rv5d_rv21d_spread_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d-21d) RV spread (jerk in spread widening)."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_005_rv5d_rv252d_spread_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of widest (5d-252d) spread."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_006_vol_curve_slope_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of log-linear vol curve slope (curve slope acceleration)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_007_vol_curve_slope_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day vol curve slope change (jerk in monthly slope velocity)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    vel21 = slope.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_008_vol_curve_curvature_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of vol-curve curvature (acceleration of curvature velocity)."""
    rv21 = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    rv63 = _realized_vol(close, _TD_QTR).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    curv = (rv63 / rv21) - (rv252 / rv63)
    vel = curv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_009_rv5d_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d RV z-score (z-score velocity acceleration)."""
    rv = _realized_vol(close, _TD_WEEK)
    z = _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_010_rv5d_rv21d_ratio_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 5d/21d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_011_rv21d_rv63d_ratio_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_012_rv5d_rv21d_spread_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of (5d-21d) spread."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    vel21 = spread.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_013_rv_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-horizon composite vol (5d+21d+63d)/3."""
    comp = (_realized_vol(close, _TD_WEEK)
            + _realized_vol(close, _TD_MON)
            + _realized_vol(close, _TD_QTR)) / 3.0
    vel = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_014_rv5d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 5d RV (jerk in monthly short-vol change)."""
    vel21 = _realized_vol(close, _TD_WEEK).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_015_rv21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d RV level (acceleration of monthly vol velocity)."""
    vel = _realized_vol(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_016_rv5d_rv21d_spread_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope-over-21d of (5d-21d) spread."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    slope = _linslope(spread, _TD_MON)
    return slope.diff(_TD_WEEK)


def vts_drv3_017_rv5d_rv63d_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_018_rv5d_pct_rank_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d RV percentile rank (pct-rank velocity acceleration)."""
    rv = _realized_vol(close, _TD_WEEK)
    pct = rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_019_rv5d_rv21d_ratio_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 5d/21d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vts_drv3_020_vol_curve_slope_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of vol curve slope."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    vel = slope.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vts_drv3_021_rv21d_rv63d_ratio_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vts_drv3_022_rv5d_rv21d_spread_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of (5d-21d) spread."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    vel = spread.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vts_drv3_023_rv63d_rv252d_ratio_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d/252d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vts_drv3_024_vol_curve_butterfly_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of vol-curve butterfly (2*rv63 - rv21 - rv252)."""
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR)
    butterfly = 2.0 * rv63 - rv21 - rv252
    vel = butterfly.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vts_drv3_025_rv5d_rv21d_spread_norm_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized (5d-21d)/252d spread."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    spread_norm = (rv5 - rv21) / rv252
    vel = spread_norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_TERM_STRUCTURE_REGISTRY_3RD_DERIVATIVES = {
    "vts_drv3_001_rv5d_rv21d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_001_rv5d_rv21d_ratio_5d_diff_5d_diff},
    "vts_drv3_002_rv21d_rv63d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_002_rv21d_rv63d_ratio_5d_diff_5d_diff},
    "vts_drv3_003_rv63d_rv252d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_003_rv63d_rv252d_ratio_5d_diff_5d_diff},
    "vts_drv3_004_rv5d_rv21d_spread_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_004_rv5d_rv21d_spread_5d_diff_5d_diff},
    "vts_drv3_005_rv5d_rv252d_spread_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_005_rv5d_rv252d_spread_5d_diff_5d_diff},
    "vts_drv3_006_vol_curve_slope_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_006_vol_curve_slope_5d_diff_5d_diff},
    "vts_drv3_007_vol_curve_slope_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_007_vol_curve_slope_21d_diff_5d_diff},
    "vts_drv3_008_vol_curve_curvature_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_008_vol_curve_curvature_5d_diff_5d_diff},
    "vts_drv3_009_rv5d_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_009_rv5d_zscore_5d_diff_5d_diff},
    "vts_drv3_010_rv5d_rv21d_ratio_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_010_rv5d_rv21d_ratio_21d_diff_5d_diff},
    "vts_drv3_011_rv21d_rv63d_ratio_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_011_rv21d_rv63d_ratio_21d_diff_5d_diff},
    "vts_drv3_012_rv5d_rv21d_spread_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_012_rv5d_rv21d_spread_21d_diff_5d_diff},
    "vts_drv3_013_rv_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_013_rv_composite_5d_diff_5d_diff},
    "vts_drv3_014_rv5d_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_014_rv5d_21d_diff_5d_diff},
    "vts_drv3_015_rv21d_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_015_rv21d_5d_diff_5d_diff},
    "vts_drv3_016_rv5d_rv21d_spread_slope_21d_5d_diff": {"inputs": ["close"], "func": vts_drv3_016_rv5d_rv21d_spread_slope_21d_5d_diff},
    "vts_drv3_017_rv5d_rv63d_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_017_rv5d_rv63d_ratio_5d_diff_5d_diff},
    "vts_drv3_018_rv5d_pct_rank_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_018_rv5d_pct_rank_5d_diff_5d_diff},
    "vts_drv3_019_rv5d_rv21d_ratio_5d_diff_slope_21d": {"inputs": ["close"], "func": vts_drv3_019_rv5d_rv21d_ratio_5d_diff_slope_21d},
    "vts_drv3_020_vol_curve_slope_5d_diff_slope_21d": {"inputs": ["close"], "func": vts_drv3_020_vol_curve_slope_5d_diff_slope_21d},
    "vts_drv3_021_rv21d_rv63d_ratio_5d_diff_slope_21d": {"inputs": ["close"], "func": vts_drv3_021_rv21d_rv63d_ratio_5d_diff_slope_21d},
    "vts_drv3_022_rv5d_rv21d_spread_5d_diff_slope_21d": {"inputs": ["close"], "func": vts_drv3_022_rv5d_rv21d_spread_5d_diff_slope_21d},
    "vts_drv3_023_rv63d_rv252d_ratio_21d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_023_rv63d_rv252d_ratio_21d_diff_5d_diff},
    "vts_drv3_024_vol_curve_butterfly_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_024_vol_curve_butterfly_5d_diff_5d_diff},
    "vts_drv3_025_rv5d_rv21d_spread_norm_5d_diff_5d_diff": {"inputs": ["close"], "func": vts_drv3_025_rv5d_rv21d_spread_norm_5d_diff_5d_diff},
}
