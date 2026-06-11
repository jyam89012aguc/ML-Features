"""
40_close_location — 2nd Derivatives (Features clv_drv2_001-025)
Domain: rate of change of base close-location-value concepts — velocity /
acceleration of CLV behavior over multiple time horizons.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def clv_drv2_001_clv_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of CLV (velocity of close location)."""
    return _clv_raw(close, high, low).diff(_TD_WEEK)


def clv_drv2_002_clv_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of CLV (monthly velocity of close location)."""
    return _clv_raw(close, high, low).diff(_TD_MON)


def clv_drv2_003_clv_sma21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day CLV SMA (velocity of smoothed close location)."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_MON).diff(_TD_WEEK)


def clv_drv2_004_clv_sma63_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day CLV SMA (monthly change in quarterly location avg)."""
    return _rolling_mean(_clv_raw(close, high, low), _TD_QTR).diff(_TD_MON)


def clv_drv2_005_close_frac_sma21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day close-fraction SMA."""
    return _rolling_mean(_close_frac(close, high, low), _TD_MON).diff(_TD_WEEK)


def clv_drv2_006_frac_near_low_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day near-low fraction (velocity of bear-close frequency)."""
    frac = _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def clv_drv2_007_frac_near_low_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day near-low fraction."""
    frac = _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def clv_drv2_008_clv_cumsum_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative CLV sum (A/D pressure velocity)."""
    return _rolling_sum(_clv_raw(close, high, low), _TD_MON).diff(_TD_WEEK)


def clv_drv2_009_clv_cumsum_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day CLV cumulative sum."""
    return _rolling_sum(_clv_raw(close, high, low), _TD_QTR).diff(_TD_MON)


def clv_drv2_010_consec_neg_clv_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive negative-CLV streak length."""
    cond = _clv_raw(close, high, low) < 0
    return _consec_streak(cond).diff(_TD_WEEK)


def clv_drv2_011_consec_near_low_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive near-low-close streak."""
    cond = _close_frac(close, high, low) <= 0.25
    return _consec_streak(cond).diff(_TD_WEEK)


def clv_drv2_012_clv_zscore_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of CLV z-score (velocity of extremity change)."""
    clv = _clv_raw(close, high, low)
    z = _safe_div(clv - _rolling_mean(clv, _TD_MON), _rolling_std(clv, _TD_MON))
    return z.diff(_TD_WEEK)


def clv_drv2_013_clv_zscore_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day CLV z-score."""
    clv = _clv_raw(close, high, low)
    z = _safe_div(clv - _rolling_mean(clv, _TD_QTR), _rolling_std(clv, _TD_QTR))
    return z.diff(_TD_MON)


def clv_drv2_014_clv_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of CLV (acceleration of slope)."""
    slp = _linslope(_clv_raw(close, high, low), _TD_MON)
    return slp.diff(_TD_WEEK)


def clv_drv2_015_clv_slope_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day OLS slope of CLV."""
    slp = _linslope(_clv_raw(close, high, low), _TD_QTR)
    return slp.diff(_TD_MON)


def clv_drv2_016_clv_bull_bear_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day CLV bull/bear ratio (velocity of A/D sentiment)."""
    clv = _clv_raw(close, high, low)
    pos = _rolling_sum(clv.where(clv > 0, 0.0), _TD_MON)
    neg = _rolling_sum(clv.where(clv < 0, 0.0).abs(), _TD_MON)
    ratio = _safe_div(pos, neg)
    return ratio.diff(_TD_WEEK)


def clv_drv2_017_max_near_low_streak_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day max near-low close streak."""
    cond = _close_frac(close, high, low) <= 0.25
    mx = _rolling_max_streak(cond, _TD_QTR)
    return mx.diff(_TD_MON)


def clv_drv2_018_clv_pct_rank_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 252-day CLV percentile rank."""
    clv = _clv_raw(close, high, low)
    rank = clv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def clv_drv2_019_clv_ema5_vs_ema21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5d EMA - 21d EMA) CLV spread."""
    clv = _clv_raw(close, high, low)
    spread = _ewm_mean(clv, _TD_WEEK) - _ewm_mean(clv, _TD_MON)
    return spread.diff(_TD_WEEK)


def clv_drv2_020_clv_sum_neg_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day sum of negative CLV (velocity of bear pressure)."""
    clv = _clv_raw(close, high, low)
    neg = _rolling_sum(clv.where(clv < 0, 0.0), _TD_MON)
    return neg.diff(_TD_WEEK)


def clv_drv2_021_clv_std_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day CLV standard deviation (volatility of location)."""
    return _rolling_std(_clv_raw(close, high, low), _TD_MON).diff(_TD_WEEK)


def clv_drv2_022_count_weak_days_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day weak-day count (ret<0 AND clv<0)."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    weak = (ret < 0) & (clv < 0)
    cnt = _rolling_count_true(weak, _TD_MON)
    return cnt.diff(_TD_WEEK)


def clv_drv2_023_clv_on_down_days_avg_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of avg CLV on down-price days (21d window)."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    avg = clv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return avg.diff(_TD_WEEK)


def clv_drv2_024_clv_bb_width_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day CLV Bollinger bandwidth."""
    width = 4.0 * _rolling_std(_clv_raw(close, high, low), _TD_MON)
    return width.diff(_TD_WEEK)


def clv_drv2_025_close_frac_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of close-fraction."""
    slp = _linslope(_close_frac(close, high, low), _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_REGISTRY_2ND_DERIVATIVES = {
    "clv_drv2_001_clv_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_001_clv_5d_diff_5d_diff},
    "clv_drv2_002_clv_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_002_clv_21d_diff},
    "clv_drv2_003_clv_sma21_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_003_clv_sma21_5d_diff},
    "clv_drv2_004_clv_sma63_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_004_clv_sma63_21d_diff},
    "clv_drv2_005_close_frac_sma21_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_005_close_frac_sma21_5d_diff},
    "clv_drv2_006_frac_near_low_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_006_frac_near_low_21d_5d_diff},
    "clv_drv2_007_frac_near_low_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_007_frac_near_low_63d_21d_diff},
    "clv_drv2_008_clv_cumsum_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_008_clv_cumsum_21d_5d_diff},
    "clv_drv2_009_clv_cumsum_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_009_clv_cumsum_63d_21d_diff},
    "clv_drv2_010_consec_neg_clv_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_010_consec_neg_clv_5d_diff},
    "clv_drv2_011_consec_near_low_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_011_consec_near_low_5d_diff},
    "clv_drv2_012_clv_zscore_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_012_clv_zscore_21d_5d_diff},
    "clv_drv2_013_clv_zscore_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_013_clv_zscore_63d_21d_diff},
    "clv_drv2_014_clv_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_014_clv_slope_21d_5d_diff},
    "clv_drv2_015_clv_slope_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_015_clv_slope_63d_21d_diff},
    "clv_drv2_016_clv_bull_bear_ratio_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_016_clv_bull_bear_ratio_21d_5d_diff},
    "clv_drv2_017_max_near_low_streak_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_017_max_near_low_streak_63d_21d_diff},
    "clv_drv2_018_clv_pct_rank_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_018_clv_pct_rank_252d_5d_diff},
    "clv_drv2_019_clv_ema5_vs_ema21_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_019_clv_ema5_vs_ema21_5d_diff},
    "clv_drv2_020_clv_sum_neg_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_020_clv_sum_neg_21d_5d_diff},
    "clv_drv2_021_clv_std_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_021_clv_std_21d_5d_diff},
    "clv_drv2_022_count_weak_days_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_022_count_weak_days_21d_5d_diff},
    "clv_drv2_023_clv_on_down_days_avg_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_023_clv_on_down_days_avg_21d_5d_diff},
    "clv_drv2_024_clv_bb_width_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_024_clv_bb_width_21d_5d_diff},
    "clv_drv2_025_close_frac_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv2_025_close_frac_slope_21d_5d_diff},
}
