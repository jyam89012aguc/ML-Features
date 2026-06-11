"""
115_volatility_term_structure — 2nd Derivatives (Features vts_drv2_001-025)
Domain: rate of change of base vol term-structure features — velocity of vol-curve
        ratios, spreads, inversion signals, and curve shape metrics.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vts_drv2_001_rv5d_rv21d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/21d vol ratio (velocity of short-end term structure tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vts_drv2_002_rv21d_rv63d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/63d vol ratio (velocity of mid-curve tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vts_drv2_003_rv63d_rv252d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d/252d vol ratio (velocity of back-end tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vts_drv2_004_rv5d_rv21d_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5d - 21d) RV spread (how fast short spread is widening)."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    return spread.diff(_TD_WEEK)


def vts_drv2_005_rv5d_rv21d_spread_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5d - 21d) RV spread (monthly velocity of short spread)."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    return spread.diff(_TD_MON)


def vts_drv2_006_rv5d_rv252d_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of widest (5d - 252d) RV spread."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)
    return spread.diff(_TD_WEEK)


def vts_drv2_007_vol_curve_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-linear vol curve slope (5d to 252d)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    return slope.diff(_TD_WEEK)


def vts_drv2_008_vol_curve_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of log-linear vol curve slope (monthly velocity)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    return slope.diff(_TD_MON)


def vts_drv2_009_vol_curve_curvature_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol-curve curvature ((rv63/rv21)-(rv252/rv63))."""
    rv21 = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    rv63 = _realized_vol(close, _TD_QTR).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    curv = (rv63 / rv21) - (rv252 / rv63)
    return curv.diff(_TD_WEEK)


def vts_drv2_010_rv5d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d RV z-score vs 252d distribution."""
    rv = _realized_vol(close, _TD_WEEK)
    z = _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))
    return z.diff(_TD_WEEK)


def vts_drv2_011_rv5d_pct_rank_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d RV percentile rank within 252-day history."""
    rv = _realized_vol(close, _TD_WEEK)
    pct = rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def vts_drv2_012_rv5d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5d RV (monthly velocity of short-horizon vol level)."""
    return _realized_vol(close, _TD_WEEK).diff(_TD_MON)


def vts_drv2_013_rv21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d RV (velocity of monthly vol level)."""
    return _realized_vol(close, _TD_MON).diff(_TD_WEEK)


def vts_drv2_014_rv63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d RV (velocity of quarterly vol level)."""
    return _realized_vol(close, _TD_QTR).diff(_TD_WEEK)


def vts_drv2_015_rv252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252d RV (monthly velocity of long-horizon vol)."""
    return _realized_vol(close, _TD_YEAR).diff(_TD_MON)


def vts_drv2_016_rv5d_rv21d_ratio_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5d/21d vol ratio (monthly acceleration of short-end tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return ratio.diff(_TD_MON)


def vts_drv2_017_rv21d_rv63d_ratio_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    return ratio.diff(_TD_MON)


def vts_drv2_018_inversion_consec_5d21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-5d>21d-inverted streak."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    c = rv5.astype(float).copy()
    streak = (rv5 > rv21).astype(int)
    group = (rv5 <= rv21).cumsum()
    streak_s = streak.groupby(group).cumsum().astype(float)
    return streak_s.diff(_TD_WEEK)


def vts_drv2_019_vol_curve_butterfly_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol-curve butterfly (2*rv63 - rv21 - rv252)."""
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR)
    butterfly = 2.0 * rv63 - rv21 - rv252
    return butterfly.diff(_TD_WEEK)


def vts_drv2_020_rv5d_rv21d_spread_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the (5d-21d) RV spread (rate of spread widening)."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    return _linslope(spread, _TD_MON)


def vts_drv2_021_rv_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 3-horizon composite vol (5d+21d+63d)/3."""
    comp = (_realized_vol(close, _TD_WEEK)
            + _realized_vol(close, _TD_MON)
            + _realized_vol(close, _TD_QTR)) / 3.0
    return comp.diff(_TD_WEEK)


def vts_drv2_022_rv5d_rv63d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vts_drv2_023_rv5d_zscore_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5d RV z-score."""
    rv = _realized_vol(close, _TD_WEEK)
    z = _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))
    return _linslope(z, _TD_MON)


def vts_drv2_024_rv21d_rv252d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vts_drv2_025_rv5d_rv21d_spread_norm_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of normalized (5d-21d)/252d RV spread."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    spread_norm = (rv5 - rv21) / rv252
    return spread_norm.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_TERM_STRUCTURE_REGISTRY_2ND_DERIVATIVES = {
    "vts_drv2_001_rv5d_rv21d_ratio_5d_diff": {"inputs": ["close"], "func": vts_drv2_001_rv5d_rv21d_ratio_5d_diff},
    "vts_drv2_002_rv21d_rv63d_ratio_5d_diff": {"inputs": ["close"], "func": vts_drv2_002_rv21d_rv63d_ratio_5d_diff},
    "vts_drv2_003_rv63d_rv252d_ratio_5d_diff": {"inputs": ["close"], "func": vts_drv2_003_rv63d_rv252d_ratio_5d_diff},
    "vts_drv2_004_rv5d_rv21d_spread_5d_diff": {"inputs": ["close"], "func": vts_drv2_004_rv5d_rv21d_spread_5d_diff},
    "vts_drv2_005_rv5d_rv21d_spread_21d_diff": {"inputs": ["close"], "func": vts_drv2_005_rv5d_rv21d_spread_21d_diff},
    "vts_drv2_006_rv5d_rv252d_spread_5d_diff": {"inputs": ["close"], "func": vts_drv2_006_rv5d_rv252d_spread_5d_diff},
    "vts_drv2_007_vol_curve_slope_5d_diff": {"inputs": ["close"], "func": vts_drv2_007_vol_curve_slope_5d_diff},
    "vts_drv2_008_vol_curve_slope_21d_diff": {"inputs": ["close"], "func": vts_drv2_008_vol_curve_slope_21d_diff},
    "vts_drv2_009_vol_curve_curvature_5d_diff": {"inputs": ["close"], "func": vts_drv2_009_vol_curve_curvature_5d_diff},
    "vts_drv2_010_rv5d_zscore_5d_diff": {"inputs": ["close"], "func": vts_drv2_010_rv5d_zscore_5d_diff},
    "vts_drv2_011_rv5d_pct_rank_5d_diff": {"inputs": ["close"], "func": vts_drv2_011_rv5d_pct_rank_5d_diff},
    "vts_drv2_012_rv5d_21d_diff": {"inputs": ["close"], "func": vts_drv2_012_rv5d_21d_diff},
    "vts_drv2_013_rv21d_5d_diff": {"inputs": ["close"], "func": vts_drv2_013_rv21d_5d_diff},
    "vts_drv2_014_rv63d_5d_diff": {"inputs": ["close"], "func": vts_drv2_014_rv63d_5d_diff},
    "vts_drv2_015_rv252d_21d_diff": {"inputs": ["close"], "func": vts_drv2_015_rv252d_21d_diff},
    "vts_drv2_016_rv5d_rv21d_ratio_21d_diff": {"inputs": ["close"], "func": vts_drv2_016_rv5d_rv21d_ratio_21d_diff},
    "vts_drv2_017_rv21d_rv63d_ratio_21d_diff": {"inputs": ["close"], "func": vts_drv2_017_rv21d_rv63d_ratio_21d_diff},
    "vts_drv2_018_inversion_consec_5d21d_5d_diff": {"inputs": ["close"], "func": vts_drv2_018_inversion_consec_5d21d_5d_diff},
    "vts_drv2_019_vol_curve_butterfly_5d_diff": {"inputs": ["close"], "func": vts_drv2_019_vol_curve_butterfly_5d_diff},
    "vts_drv2_020_rv5d_rv21d_spread_slope_21d": {"inputs": ["close"], "func": vts_drv2_020_rv5d_rv21d_spread_slope_21d},
    "vts_drv2_021_rv_composite_5d_diff": {"inputs": ["close"], "func": vts_drv2_021_rv_composite_5d_diff},
    "vts_drv2_022_rv5d_rv63d_ratio_5d_diff": {"inputs": ["close"], "func": vts_drv2_022_rv5d_rv63d_ratio_5d_diff},
    "vts_drv2_023_rv5d_zscore_slope_21d": {"inputs": ["close"], "func": vts_drv2_023_rv5d_zscore_slope_21d},
    "vts_drv2_024_rv21d_rv252d_ratio_5d_diff": {"inputs": ["close"], "func": vts_drv2_024_rv21d_rv252d_ratio_5d_diff},
    "vts_drv2_025_rv5d_rv21d_spread_norm_5d_diff": {"inputs": ["close"], "func": vts_drv2_025_rv5d_rv21d_spread_norm_5d_diff},
}
