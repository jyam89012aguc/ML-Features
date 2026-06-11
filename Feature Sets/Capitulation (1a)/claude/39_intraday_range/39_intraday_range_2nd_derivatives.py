"""
39_intraday_range — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base intraday range features — velocity of range level and
structure concepts (5d/21d diffs and rolling OLS slopes of base range measures).
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def idr_drv2_001_range_over_close_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of normalized range (velocity of spread level)."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(_TD_WEEK)


def idr_drv2_002_range_over_close_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of normalized range (monthly velocity of spread level)."""
    r = _hl_range_over_close(high, low, close)
    return r.diff(_TD_MON)


def idr_drv2_003_avg_range_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day average normalized range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_MON)
    return avg.diff(_TD_WEEK)


def idr_drv2_004_avg_range_63d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day average normalized range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_QTR)
    return avg.diff(_TD_MON)


def idr_drv2_005_avg_range_252d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 252-day average normalized range."""
    avg = _rolling_mean(_hl_range_over_close(high, low, close), _TD_YEAR)
    return avg.diff(_TD_MON)


def idr_drv2_006_range_zscore_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day range z-score (accelerating extremity)."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    return z.diff(_TD_WEEK)


def idr_drv2_007_range_zscore_63d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 63-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_QTR), _rolling_std(r, _TD_QTR))
    return z.diff(_TD_WEEK)


def idr_drv2_008_range_vs_avg_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the ratio of today's range to its 21-day average."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(r, _rolling_mean(r, _TD_MON))
    return ratio.diff(_TD_WEEK)


def idr_drv2_009_body_to_range_ratio_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of body-to-range ratio (change in candle compactness)."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    br = _safe_div(body, rng)
    return br.diff(_TD_WEEK)


def idr_drv2_010_avg_body_range_21d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 21-day average body-to-range ratio."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    avg_br = _rolling_mean(_safe_div(body, rng), _TD_MON)
    return avg_br.diff(_TD_MON)


def idr_drv2_011_gap_over_range_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of gap-to-range ratio (change in gap dominance)."""
    gap = (open - close.shift(1)).abs()
    rng = (high - low).replace(0, np.nan)
    gr = _safe_div(gap, rng)
    return gr.diff(_TD_WEEK)


def idr_drv2_012_range_cv_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation of range."""
    r = _hl_range_over_close(high, low, close)
    cv = _safe_div(_rolling_std(r, _TD_MON), _rolling_mean(r, _TD_MON))
    return cv.diff(_TD_WEEK)


def idr_drv2_013_range_cv_63d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation of range."""
    r = _hl_range_over_close(high, low, close)
    cv = _safe_div(_rolling_std(r, _TD_QTR), _rolling_mean(r, _TD_QTR))
    return cv.diff(_TD_MON)


def idr_drv2_014_range_5d_21d_ratio_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 5d/21d range ratio (short horizon momentum change)."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(_rolling_mean(r, _TD_WEEK), _rolling_mean(r, _TD_MON))
    return ratio.diff(_TD_WEEK)


def idr_drv2_015_range_21d_63d_ratio_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of the 21d/63d range ratio."""
    r = _hl_range_over_close(high, low, close)
    ratio = _safe_div(_rolling_mean(r, _TD_MON), _rolling_mean(r, _TD_QTR))
    return ratio.diff(_TD_MON)


def idr_drv2_016_range_slope_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of range over 21 days (change in range trend slope)."""
    r = _hl_range_over_close(high, low, close)
    slp = _linslope(r, _TD_MON)
    return slp.diff(_TD_WEEK)


def idr_drv2_017_range_slope_63d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of range over 63 days."""
    r = _hl_range_over_close(high, low, close)
    slp = _linslope(r, _TD_QTR)
    return slp.diff(_TD_MON)


def idr_drv2_018_range_vol_corr_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day range-volume correlation."""
    r = _hl_range_over_close(high, low, close)
    corr = r.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(volume)
    return corr.diff(_TD_WEEK)


def idr_drv2_019_range_up_vs_down_ratio_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of ratio of avg range on up days to avg range on down days (21d)."""
    r = _hl_range_over_close(high, low, close)
    is_up = close > close.shift(1)
    is_dn = close < close.shift(1)
    up_r = r.where(is_up, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn_r = r.where(is_dn, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(up_r, dn_r)
    return ratio.diff(_TD_WEEK)


def idr_drv2_020_rolling_spread_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling H-L spread normalized by close."""
    spread = _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON), close)
    return spread.diff(_TD_WEEK)


def idr_drv2_021_range_efficiency_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day range efficiency (abs return / summed range)."""
    sum_range = _rolling_sum(high - low, _TD_MON).replace(0, np.nan)
    eff = _safe_div(close.diff(_TD_MON).abs(), sum_range)
    return eff.diff(_TD_WEEK)


def idr_drv2_022_avg_range_ewm21_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of normalized range."""
    ewm = _ewm_mean(_hl_range_over_close(high, low, close), _TD_MON)
    return ewm.diff(_TD_WEEK)


def idr_drv2_023_range_pct_rank_63d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 63-day percentile rank of range."""
    r = _hl_range_over_close(high, low, close)
    rank = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def idr_drv2_024_range_max_63d_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day max normalized range (regime extreme change)."""
    r = _hl_range_over_close(high, low, close)
    mx = _rolling_max(r, _TD_QTR)
    return mx.diff(_TD_MON)


def idr_drv2_025_range_composite_index_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of composite range index (avg of 21d, 63d, 252d relative levels)."""
    r = _hl_range_over_close(high, low, close)
    a = _safe_div(r, _rolling_mean(r, _TD_MON))
    b = _safe_div(r, _rolling_mean(r, _TD_QTR))
    c = _safe_div(r, _rolling_mean(r, _TD_YEAR))
    composite = (a + b + c) / 3.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_REGISTRY_2ND_DERIVATIVES = {
    "idr_drv2_001_range_over_close_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_001_range_over_close_5d_diff},
    "idr_drv2_002_range_over_close_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_002_range_over_close_21d_diff},
    "idr_drv2_003_avg_range_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_003_avg_range_21d_5d_diff},
    "idr_drv2_004_avg_range_63d_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_004_avg_range_63d_21d_diff},
    "idr_drv2_005_avg_range_252d_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_005_avg_range_252d_21d_diff},
    "idr_drv2_006_range_zscore_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_006_range_zscore_21d_5d_diff},
    "idr_drv2_007_range_zscore_63d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_007_range_zscore_63d_5d_diff},
    "idr_drv2_008_range_vs_avg_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_008_range_vs_avg_21d_5d_diff},
    "idr_drv2_009_body_to_range_ratio_5d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_drv2_009_body_to_range_ratio_5d_diff},
    "idr_drv2_010_avg_body_range_21d_21d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_drv2_010_avg_body_range_21d_21d_diff},
    "idr_drv2_011_gap_over_range_5d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_drv2_011_gap_over_range_5d_diff},
    "idr_drv2_012_range_cv_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_012_range_cv_21d_5d_diff},
    "idr_drv2_013_range_cv_63d_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_013_range_cv_63d_21d_diff},
    "idr_drv2_014_range_5d_21d_ratio_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_014_range_5d_21d_ratio_5d_diff},
    "idr_drv2_015_range_21d_63d_ratio_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_015_range_21d_63d_ratio_21d_diff},
    "idr_drv2_016_range_slope_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_016_range_slope_21d_5d_diff},
    "idr_drv2_017_range_slope_63d_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_017_range_slope_63d_21d_diff},
    "idr_drv2_018_range_vol_corr_21d_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": idr_drv2_018_range_vol_corr_21d_5d_diff},
    "idr_drv2_019_range_up_vs_down_ratio_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_019_range_up_vs_down_ratio_21d_5d_diff},
    "idr_drv2_020_rolling_spread_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_020_rolling_spread_21d_5d_diff},
    "idr_drv2_021_range_efficiency_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_021_range_efficiency_21d_5d_diff},
    "idr_drv2_022_avg_range_ewm21_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_022_avg_range_ewm21_5d_diff},
    "idr_drv2_023_range_pct_rank_63d_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_023_range_pct_rank_63d_5d_diff},
    "idr_drv2_024_range_max_63d_21d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_024_range_max_63d_21d_diff},
    "idr_drv2_025_range_composite_index_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_drv2_025_range_composite_index_5d_diff},
}
