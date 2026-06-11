"""
40_close_location — 3rd Derivatives (Features clv_drv3_001-025)
Domain: rate of change of 2nd-derivative close-location concepts —
acceleration of velocity (jerk) in CLV behavior.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def clv_drv3_001_clv_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of CLV (acceleration of close-location velocity)."""
    vel = _clv_raw(close, high, low).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_002_clv_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day CLV velocity (jerk in monthly change)."""
    vel21 = _clv_raw(close, high, low).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_003_clv_sma21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV SMA (acceleration of smoothed CLV)."""
    vel = _rolling_mean(_clv_raw(close, high, low), _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_004_clv_sma63_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CLV SMA (jerk in quarterly trend)."""
    vel21 = _rolling_mean(_clv_raw(close, high, low), _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_005_frac_near_low_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day near-low fraction (jerk in bear-close rate)."""
    frac = _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_006_clv_cumsum_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV cumulative sum (jerk in A/D pressure)."""
    vel = _rolling_sum(_clv_raw(close, high, low), _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_007_clv_zscore_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV z-score (acceleration of extremity)."""
    clv = _clv_raw(close, high, low)
    z = _safe_div(clv - _rolling_mean(clv, _TD_MON), _rolling_std(clv, _TD_MON))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_008_clv_slope_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OLS slope of CLV (jerk of slope)."""
    slp = _linslope(_clv_raw(close, high, low), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_009_clv_zscore_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CLV z-score."""
    clv = _clv_raw(close, high, low)
    z = _safe_div(clv - _rolling_mean(clv, _TD_QTR), _rolling_std(clv, _TD_QTR))
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_010_consec_neg_clv_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive negative-CLV streak (acceleration)."""
    cond = _clv_raw(close, high, low) < 0
    vel = _consec_streak(cond).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_011_clv_bull_bear_ratio_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV bull/bear ratio."""
    clv = _clv_raw(close, high, low)
    pos = _rolling_sum(clv.where(clv > 0, 0.0), _TD_MON)
    neg = _rolling_sum(clv.where(clv < 0, 0.0).abs(), _TD_MON)
    ratio = _safe_div(pos, neg)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_012_clv_pct_rank_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day CLV percentile rank."""
    clv = _clv_raw(close, high, low)
    rank = clv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_013_frac_near_low_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day near-low fraction."""
    frac = _rolling_count_true(_close_frac(close, high, low) <= 0.25, _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_014_clv_slope_21d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day OLS slope of CLV (curvature)."""
    slp = _linslope(_clv_raw(close, high, low), _TD_MON)
    return _linslope(slp, _TD_MON)


def clv_drv3_015_clv_ema5_vs_ema21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of (5d EMA - 21d EMA) CLV spread."""
    clv = _clv_raw(close, high, low)
    spread = _ewm_mean(clv, _TD_WEEK) - _ewm_mean(clv, _TD_MON)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_016_clv_std_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV std (jerk in location volatility)."""
    std = _rolling_std(_clv_raw(close, high, low), _TD_MON)
    vel = std.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_017_clv_sum_neg_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day negative-CLV sum (jerk in bear pressure)."""
    clv = _clv_raw(close, high, low)
    neg = _rolling_sum(clv.where(clv < 0, 0.0), _TD_MON)
    vel = neg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_018_clv_slope_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CLV OLS slope."""
    slp = _linslope(_clv_raw(close, high, low), _TD_QTR)
    vel21 = slp.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_019_consec_near_low_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive near-low streak (acceleration)."""
    cond = _close_frac(close, high, low) <= 0.25
    vel = _consec_streak(cond).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_020_count_weak_days_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day weak-day count (ret<0 AND clv<0)."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    weak = (ret < 0) & (clv < 0)
    cnt = _rolling_count_true(weak, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_021_clv_on_down_days_avg_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of avg-CLV-on-down-days."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    avg = clv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    vel = avg.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def clv_drv3_022_clv_bb_width_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CLV Bollinger width."""
    width = 4.0 * _rolling_std(_clv_raw(close, high, low), _TD_MON)
    vel = width.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def clv_drv3_023_close_frac_sma21_5d_diff_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day velocity of close-fraction 21d SMA."""
    vel = _rolling_mean(_close_frac(close, high, low), _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def clv_drv3_024_clv_cumsum_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CLV cumulative sum."""
    vel21 = _rolling_sum(_clv_raw(close, high, low), _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def clv_drv3_025_clv_zscore_21d_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day CLV z-score over 63-day window."""
    clv = _clv_raw(close, high, low)
    z = _safe_div(clv - _rolling_mean(clv, _TD_MON), _rolling_std(clv, _TD_MON))
    slp = _linslope(z, _TD_QTR)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_REGISTRY_3RD_DERIVATIVES = {
    "clv_drv3_001_clv_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_001_clv_5d_diff_5d_diff},
    "clv_drv3_002_clv_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_002_clv_21d_diff_5d_diff},
    "clv_drv3_003_clv_sma21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_003_clv_sma21_5d_diff_5d_diff},
    "clv_drv3_004_clv_sma63_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_004_clv_sma63_21d_diff_5d_diff},
    "clv_drv3_005_frac_near_low_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_005_frac_near_low_21d_5d_diff_5d_diff},
    "clv_drv3_006_clv_cumsum_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_006_clv_cumsum_21d_5d_diff_5d_diff},
    "clv_drv3_007_clv_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_007_clv_zscore_21d_5d_diff_5d_diff},
    "clv_drv3_008_clv_slope_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_008_clv_slope_21d_5d_diff_5d_diff},
    "clv_drv3_009_clv_zscore_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_009_clv_zscore_63d_21d_diff_5d_diff},
    "clv_drv3_010_consec_neg_clv_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_010_consec_neg_clv_5d_diff_5d_diff},
    "clv_drv3_011_clv_bull_bear_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_011_clv_bull_bear_ratio_21d_5d_diff_5d_diff},
    "clv_drv3_012_clv_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_012_clv_pct_rank_252d_5d_diff_5d_diff},
    "clv_drv3_013_frac_near_low_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_013_frac_near_low_63d_21d_diff_5d_diff},
    "clv_drv3_014_clv_slope_21d_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_drv3_014_clv_slope_21d_slope_21d},
    "clv_drv3_015_clv_ema5_vs_ema21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_015_clv_ema5_vs_ema21_5d_diff_5d_diff},
    "clv_drv3_016_clv_std_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_016_clv_std_21d_5d_diff_5d_diff},
    "clv_drv3_017_clv_sum_neg_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_017_clv_sum_neg_21d_5d_diff_5d_diff},
    "clv_drv3_018_clv_slope_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_018_clv_slope_63d_21d_diff_5d_diff},
    "clv_drv3_019_consec_near_low_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_019_consec_near_low_5d_diff_5d_diff},
    "clv_drv3_020_count_weak_days_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_020_count_weak_days_21d_5d_diff_5d_diff},
    "clv_drv3_021_clv_on_down_days_avg_5d_diff_slope": {"inputs": ["close", "high", "low"], "func": clv_drv3_021_clv_on_down_days_avg_5d_diff_slope},
    "clv_drv3_022_clv_bb_width_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_022_clv_bb_width_21d_5d_diff_5d_diff},
    "clv_drv3_023_close_frac_sma21_5d_diff_slope": {"inputs": ["close", "high", "low"], "func": clv_drv3_023_close_frac_sma21_5d_diff_slope},
    "clv_drv3_024_clv_cumsum_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_024_clv_cumsum_63d_21d_diff_5d_diff},
    "clv_drv3_025_clv_zscore_21d_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_drv3_025_clv_zscore_21d_slope_5d_diff},
}
