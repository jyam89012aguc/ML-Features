"""
40_close_location — Extended 3rd Derivatives (Features clv_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative close-location concepts —
        acceleration of velocity (jerk) in VWCLV, shadow asymmetry,
        threshold-count, and regime feature series.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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


def _clv_raw(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    hl = high - low
    return _safe_div((close - low) - (high - close), hl)


def _close_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return _safe_div(close - low, high - low)


def _typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────

def clv_extdrv3_001_vwclv_avg_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VWCLV average (acceleration of vol-weighted CLV velocity)."""
    clv = _clv_raw(close, high, low)
    vw21 = _safe_div(_rolling_sum(clv * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = vw21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_002_vwclv_avg_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day VWCLV (jerk in quarterly VWCLV trend)."""
    clv = _clv_raw(close, high, low)
    vw63 = _safe_div(_rolling_sum(clv * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    vel21 = vw63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_extdrv3_003_clv_typical_sma21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day SMA of CLV(typical price)."""
    tp = _typical_price(close, high, low)
    hl = high - low
    clv_tp = _safe_div((tp - low) - (high - tp), hl)
    vel = _rolling_mean(clv_tp, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_004_clv_zscore_126d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day CLV z-score (acceleration of semi-annual z-score)."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, 126)
    s = _rolling_std(clv, 126)
    z = _safe_div(clv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_005_close_frac_zscore_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of close-fraction 63-day z-score."""
    cf = _close_frac(close, high, low)
    m = _rolling_mean(cf, _TD_QTR)
    s = _rolling_std(cf, _TD_QTR)
    z = _safe_div(cf - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_006_count_clv_lt_minus09_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day count CLV < -0.9 (acceleration of extreme-low frequency)."""
    cnt = _rolling_count_true(_clv_raw(close, high, low) < -0.9, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_007_shadow_ratio_sma21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day SMA of upper/lower shadow ratio."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    ratio = _safe_div(upper, lower)
    vel = _rolling_mean(ratio, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_008_range_asymmetry_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range asymmetry (acceleration of wick-direction bias)."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    vel = _rolling_mean(upper - lower, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_009_clv_iqr_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CLV IQR (jerk in dispersion change)."""
    clv = _clv_raw(close, high, low)
    q75 = clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    vel21 = iqr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_extdrv3_010_clv_depth_below_minus05_sum21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV depth below -0.5 (jerk in bearish intensity)."""
    clv = _clv_raw(close, high, low)
    depth = _rolling_sum((-0.5 - clv).clip(lower=0.0), _TD_MON)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_011_clv_depth_below_minus08_sum21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV depth below -0.8 (jerk in extreme bear pressure)."""
    clv = _clv_raw(close, high, low)
    depth = _rolling_sum((-0.8 - clv).clip(lower=0.0), _TD_MON)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_012_vwclv_neg_sum_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day negative vol*CLV sum."""
    clv = _clv_raw(close, high, low)
    neg = _rolling_sum((clv * volume).where(clv < 0, 0.0), _TD_QTR)
    vel21 = neg.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_extdrv3_013_clv_cap_score_63d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day CLV capitulation score (acceleration of distress)."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_QTR)
    frac_low = _rolling_count_true(cf <= 0.25, _TD_QTR) / _TD_QTR
    score = 0.5 * (1.0 - avg_clv) / 2.0 + 0.5 * frac_low
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_014_clv_ema10_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 10-day EMA of CLV (acceleration of short EMA velocity)."""
    vel = _ewm_mean(_clv_raw(close, high, low), 10).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_015_clv_sma10_vs_sma63_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of (CLV SMA10 - CLV SMA63) spread (acceleration of cross-window divergence)."""
    clv = _clv_raw(close, high, low)
    spread = _rolling_mean(clv, 10) - _rolling_mean(clv, _TD_QTR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_016_close_to_high_pct_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day avg close-to-high pct (jerk in upper-end gap)."""
    avg = _rolling_mean(_safe_div(close, high) - 1.0, _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_017_upper_shadow_sma21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day SMA of upper shadow fraction."""
    upper_sh = _safe_div(high - close, high - low)
    vel = _rolling_mean(upper_sh, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_018_hl_range_norm_sma21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day SMA of (high-low)/close (jerk in relative range)."""
    rng_norm = _safe_div(high - low, close)
    vel = _rolling_mean(rng_norm, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_019_clv_pct_rank_5d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day CLV percentile rank (acceleration of intraweek rank change)."""
    clv = _clv_raw(close, high, low)
    rank = clv.rolling(_TD_WEEK, min_periods=1).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_020_vwclv_slope_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OLS slope of VWCLV-5d (jerk of VWCLV trend)."""
    clv = _clv_raw(close, high, low)
    vw5 = _safe_div(_rolling_sum(clv * volume, _TD_WEEK), _rolling_sum(volume, _TD_WEEK))
    slp = _linslope(vw5, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_extdrv3_021_clv_cap_score_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day CLV capitulation score (curvature of distress)."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_QTR)
    frac_low = _rolling_count_true(cf <= 0.25, _TD_QTR) / _TD_QTR
    score = 0.5 * (1.0 - avg_clv) / 2.0 + 0.5 * frac_low
    return _linslope(score, _TD_MON)


def clv_extdrv3_022_shadow_ratio_sma21_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day shadow ratio SMA (curvature of wick direction)."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    ratio_sma = _rolling_mean(_safe_div(upper, lower), _TD_MON)
    return _linslope(ratio_sma, _TD_MON)


def clv_extdrv3_023_clv_depth_below_minus05_sum_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of cumulative CLV depth below -0.5 (trend of bearish intensity)."""
    clv = _clv_raw(close, high, low)
    depth = _rolling_sum((-0.5 - clv).clip(lower=0.0), _TD_MON)
    return _linslope(depth, _TD_MON)


def clv_extdrv3_024_close_frac_zscore_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day close-fraction z-score (curvature of fractional extremity)."""
    cf = _close_frac(close, high, low)
    m = _rolling_mean(cf, _TD_QTR)
    s = _rolling_std(cf, _TD_QTR)
    z = _safe_div(cf - m, s)
    return _linslope(z, _TD_MON)


def clv_extdrv3_025_vwclv_neg_sum_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day negative vol*CLV sum (trend of distribution acceleration)."""
    clv = _clv_raw(close, high, low)
    neg = _rolling_sum((clv * volume).where(clv < 0, 0.0), _TD_QTR)
    return _linslope(neg, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "clv_extdrv3_001_vwclv_avg_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": clv_extdrv3_001_vwclv_avg_21d_5d_diff_5d_diff},
    "clv_extdrv3_002_vwclv_avg_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": clv_extdrv3_002_vwclv_avg_63d_21d_diff_5d_diff},
    "clv_extdrv3_003_clv_typical_sma21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_003_clv_typical_sma21_5d_diff_5d_diff},
    "clv_extdrv3_004_clv_zscore_126d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_004_clv_zscore_126d_5d_diff_5d_diff},
    "clv_extdrv3_005_close_frac_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_005_close_frac_zscore_63d_5d_diff_5d_diff},
    "clv_extdrv3_006_count_clv_lt_minus09_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_006_count_clv_lt_minus09_21d_5d_diff_5d_diff},
    "clv_extdrv3_007_shadow_ratio_sma21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_007_shadow_ratio_sma21_5d_diff_5d_diff},
    "clv_extdrv3_008_range_asymmetry_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_008_range_asymmetry_21d_5d_diff_5d_diff},
    "clv_extdrv3_009_clv_iqr_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_009_clv_iqr_63d_21d_diff_5d_diff},
    "clv_extdrv3_010_clv_depth_below_minus05_sum21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_010_clv_depth_below_minus05_sum21d_5d_diff_5d_diff},
    "clv_extdrv3_011_clv_depth_below_minus08_sum21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_011_clv_depth_below_minus08_sum21d_5d_diff_5d_diff},
    "clv_extdrv3_012_vwclv_neg_sum_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": clv_extdrv3_012_vwclv_neg_sum_63d_21d_diff_5d_diff},
    "clv_extdrv3_013_clv_cap_score_63d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_013_clv_cap_score_63d_5d_diff_5d_diff},
    "clv_extdrv3_014_clv_ema10_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_014_clv_ema10_5d_diff_5d_diff},
    "clv_extdrv3_015_clv_sma10_vs_sma63_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_015_clv_sma10_vs_sma63_5d_diff_5d_diff},
    "clv_extdrv3_016_close_to_high_pct_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_016_close_to_high_pct_21d_5d_diff_5d_diff},
    "clv_extdrv3_017_upper_shadow_sma21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_017_upper_shadow_sma21_5d_diff_5d_diff},
    "clv_extdrv3_018_hl_range_norm_sma21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_018_hl_range_norm_sma21_5d_diff_5d_diff},
    "clv_extdrv3_019_clv_pct_rank_5d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_019_clv_pct_rank_5d_5d_diff_5d_diff},
    "clv_extdrv3_020_vwclv_slope_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": clv_extdrv3_020_vwclv_slope_21d_5d_diff_5d_diff},
    "clv_extdrv3_021_clv_cap_score_63d_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_021_clv_cap_score_63d_slope_21d},
    "clv_extdrv3_022_shadow_ratio_sma21_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_022_shadow_ratio_sma21_slope_21d},
    "clv_extdrv3_023_clv_depth_below_minus05_sum_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_023_clv_depth_below_minus05_sum_slope_21d},
    "clv_extdrv3_024_close_frac_zscore_63d_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_extdrv3_024_close_frac_zscore_63d_slope_21d},
    "clv_extdrv3_025_vwclv_neg_sum_63d_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_extdrv3_025_vwclv_neg_sum_63d_slope_21d},
}
