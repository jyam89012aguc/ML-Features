"""
39_intraday_range — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative intraday range features — acceleration of
velocity concepts applied to range level, spread, and structure measures.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high - low, close)


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
# Each = diff/slope applied to a 2nd-derivative concept

def idr_drv3_001_range_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized range (acceleration of spread velocity)."""
    r = _hl_range_over_close(high, low, close)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_002_range_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of normalized range (monthly jerk)."""
    r = _hl_range_over_close(high, low, close)
    vel21 = r.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_003_avg_range_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day average range (acceleration of avg range velocity)."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_004_avg_range_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day average range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_QTR)
    vel21 = avg.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_005_range_zscore_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range z-score (jerk in z-score velocity)."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_006_range_zscore_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_QTR), _rolling_std(r, _TD_QTR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_007_body_range_ratio_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of body-to-range ratio (candle compactness acceleration)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    br = _safe_div(body, rng)
    vel = br.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_008_range_cv_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range coefficient of variation."""
    r = _hl_range_over_close(high, low, close)
    cv = _safe_div(_rolling_std(r, _TD_MON), _rolling_mean(r, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_009_range_5d_21d_ratio_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of the 5d/21d average range ratio."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(_rolling_mean(r, _TD_WEEK), _rolling_mean(r, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_010_range_slope_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OLS slope of range (slope acceleration)."""
    r = _hl_range_over_close(high, low, close)
    slp = _linslope(r, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_011_gap_over_range_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of gap-to-range ratio (acceleration of gap dominance change)."""
    gap = (open - close.shift(1)).abs()
    rng = (high - low).replace(0, np.nan)
    gr = _safe_div(gap, rng)
    vel = gr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_012_range_vol_corr_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range-volume correlation."""
    r = _hl_range_over_close(high, low, close)
    corr = r.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(volume)
    vel = corr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_013_rolling_spread_21d_5d_diff_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day rolling spread."""
    spread = _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON), close)
    vel = spread.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_drv3_014_avg_range_21d_5d_diff_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day change in 21-day avg range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_drv3_015_range_zscore_21d_5d_diff_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_drv3_016_range_cv_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day range coefficient of variation."""
    r = _hl_range_over_close(high, low, close)
    cv = _safe_div(_rolling_std(r, _TD_QTR), _rolling_mean(r, _TD_QTR))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_017_range_efficiency_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range efficiency (acceleration of path ratio)."""
    sum_range = _rolling_sum(high - low, _TD_MON).replace(0, np.nan)
    eff = _safe_div(close.diff(_TD_MON).abs(), sum_range)
    vel = eff.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_018_range_21d_63d_ratio_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21d/63d range ratio."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(_rolling_mean(r, _TD_MON), _rolling_mean(r, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_019_range_vs_avg_21d_5d_diff_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of range/avg_21d ratio."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(r, _rolling_mean(r, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_drv3_020_avg_range_252d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day average range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_YEAR)
    vel21 = avg.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_021_range_ewm21_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) normalized range."""
    ewm = _ewm_mean(_hl_range_over_close(high, low, close), _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_022_range_pct_rank_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day percentile rank of range."""
    r = _hl_range_over_close(high, low, close)
    rank = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_023_range_max_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day max range."""
    r = _hl_range_over_close(high, low, close)
    mx = _rolling_max(r, _TD_QTR)
    vel21 = mx.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_drv3_024_range_composite_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite range index (acceleration of composite velocity)."""
    r = _hl_range_over_close(high, low, close)
    a = _safe_div(r, _rolling_mean(r, _TD_MON))
    b = _safe_div(r, _rolling_mean(r, _TD_QTR))
    c = _safe_div(r, _rolling_mean(r, _TD_YEAR))
    composite = (a + b + c) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_drv3_025_range_slope_21d_5d_diff_slope(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 5-day change in 21-day range slope."""
    r = _hl_range_over_close(high, low, close)
    slp = _linslope(r, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return _linslope(vel, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_REGISTRY_3RD_DERIVATIVES = {
    "idr_drv3_001_range_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_001_range_5d_diff_5d_diff},
    "idr_drv3_002_range_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_002_range_21d_diff_5d_diff},
    "idr_drv3_003_avg_range_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_003_avg_range_21d_5d_diff_5d_diff},
    "idr_drv3_004_avg_range_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_004_avg_range_63d_21d_diff_5d_diff},
    "idr_drv3_005_range_zscore_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_005_range_zscore_21d_5d_diff_5d_diff},
    "idr_drv3_006_range_zscore_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_006_range_zscore_63d_5d_diff_5d_diff},
    "idr_drv3_007_body_range_ratio_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_drv3_007_body_range_ratio_5d_diff_5d_diff},
    "idr_drv3_008_range_cv_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_008_range_cv_21d_5d_diff_5d_diff},
    "idr_drv3_009_range_5d_21d_ratio_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_009_range_5d_21d_ratio_5d_diff_5d_diff},
    "idr_drv3_010_range_slope_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_010_range_slope_21d_5d_diff_5d_diff},
    "idr_drv3_011_gap_over_range_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_drv3_011_gap_over_range_5d_diff_5d_diff},
    "idr_drv3_012_range_vol_corr_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": idr_drv3_012_range_vol_corr_21d_5d_diff_5d_diff},
    "idr_drv3_013_rolling_spread_21d_5d_diff_slope": {"inputs": ["high", "low", "close"], "func": idr_drv3_013_rolling_spread_21d_5d_diff_slope},
    "idr_drv3_014_avg_range_21d_5d_diff_slope": {"inputs": ["high", "low", "close"], "func": idr_drv3_014_avg_range_21d_5d_diff_slope},
    "idr_drv3_015_range_zscore_21d_5d_diff_slope": {"inputs": ["high", "low", "close"], "func": idr_drv3_015_range_zscore_21d_5d_diff_slope},
    "idr_drv3_016_range_cv_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_016_range_cv_63d_21d_diff_5d_diff},
    "idr_drv3_017_range_efficiency_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_017_range_efficiency_21d_5d_diff_5d_diff},
    "idr_drv3_018_range_21d_63d_ratio_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_018_range_21d_63d_ratio_21d_diff_5d_diff},
    "idr_drv3_019_range_vs_avg_21d_5d_diff_slope": {"inputs": ["high", "low", "close"], "func": idr_drv3_019_range_vs_avg_21d_5d_diff_slope},
    "idr_drv3_020_avg_range_252d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_020_avg_range_252d_21d_diff_5d_diff},
    "idr_drv3_021_range_ewm21_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_021_range_ewm21_5d_diff_5d_diff},
    "idr_drv3_022_range_pct_rank_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_022_range_pct_rank_63d_5d_diff_5d_diff},
    "idr_drv3_023_range_max_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_023_range_max_63d_21d_diff_5d_diff},
    "idr_drv3_024_range_composite_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv3_024_range_composite_5d_diff_5d_diff},
    "idr_drv3_025_range_slope_21d_5d_diff_slope": {"inputs": ["high", "low", "close"], "func": idr_drv3_025_range_slope_21d_5d_diff_slope},
}
