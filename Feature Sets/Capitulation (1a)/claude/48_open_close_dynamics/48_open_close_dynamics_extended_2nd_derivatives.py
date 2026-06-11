"""
48_open_close_dynamics — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended open-close session dynamic features — velocity of
        new extended base concepts (new window z-scores, weak-open/close streaks,
        cumulative loss paths, vol-session interactions, regime flags, sortino ratios).
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _intraday_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log return from open to close."""
    return _log_safe(close) - _log_safe(open)


def _overnight_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log return from prior close to today's open."""
    return _log_safe(open) - _log_safe(close.shift(1))


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


# ── 2nd-Derivative Feature Functions (extended base concepts) ─────────────────

def ocd_extdrv2_001_intraday_ret_zscore_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the intraday-return 21-day z-score (velocity of intraday z-score)."""
    r = _intraday_ret(open, close)
    z = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    return z.diff(_TD_WEEK)


def ocd_extdrv2_002_overnight_ret_zscore_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the overnight-return 21-day z-score."""
    r = _overnight_ret(close, open)
    z = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    return z.diff(_TD_WEEK)


def ocd_extdrv2_003_intraday_ret_zscore_126d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of the intraday-return 126-day z-score (monthly shift)."""
    r = _intraday_ret(open, close)
    z = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))
    return z.diff(_TD_MON)


def ocd_extdrv2_004_overnight_ret_zscore_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of the overnight-return 126-day z-score."""
    r = _overnight_ret(close, open)
    z = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))
    return z.diff(_TD_MON)


def ocd_extdrv2_005_intraday_vol_126d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 126-day intraday volatility (half-year vol velocity)."""
    std126 = _rolling_std(_intraday_ret(open, close), _TD_HALF)
    return std126.diff(_TD_MON)


def ocd_extdrv2_006_overnight_vol_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 126-day overnight volatility."""
    std126 = _rolling_std(_overnight_ret(close, open), _TD_HALF)
    return std126.diff(_TD_MON)


def ocd_extdrv2_007_intraday_overnight_corr_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 126-day intraday/overnight correlation (correlation shift)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    corr = intra.rolling(_TD_HALF, min_periods=max(5, _TD_HALF // 2)).corr(over)
    return corr.diff(_TD_MON)


def ocd_extdrv2_008_weak_open_fraction_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day weak-open fraction (acceleration in gap-down frequency)."""
    flag = (open < close.shift(1)).astype(float)
    frac = _rolling_count_true(flag.astype(bool), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ocd_extdrv2_009_weak_close_fraction_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day weak-close fraction."""
    cond = (close < open) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ocd_extdrv2_010_intraday_loss_fraction_63d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day intraday loss fraction."""
    r = _intraday_ret(open, close)
    frac = _rolling_count_true(r < 0, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def ocd_extdrv2_011_overnight_loss_fraction_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day overnight loss fraction."""
    r = _overnight_ret(close, open)
    frac = _rolling_count_true(r < 0, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def ocd_extdrv2_012_cum_intraday_loss_126d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 126-day cumulative intraday losses (velocity of loss accumulation)."""
    cum = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_HALF)
    return cum.diff(_TD_MON)


def ocd_extdrv2_013_cum_overnight_loss_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 126-day cumulative overnight losses."""
    cum = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_HALF)
    return cum.diff(_TD_MON)


def ocd_extdrv2_014_intraday_overnight_vol_ratio_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 126-day intraday/overnight vol ratio."""
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_HALF)
    over_std = _rolling_std(_overnight_ret(close, open), _TD_HALF)
    ratio = _safe_div(intra_std, over_std + _EPS)
    return ratio.diff(_TD_MON)


def ocd_extdrv2_015_intraday_sortino_proxy_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day intraday Sortino-style ratio (momentum of risk-adjusted return)."""
    r = _intraday_ret(open, close)
    mean_r = _rolling_mean(r, _TD_MON)
    loss_r = r.where(r < 0, np.nan)
    down_std = loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    sortino = _safe_div(mean_r, down_std + _EPS)
    return sortino.diff(_TD_WEEK)


def ocd_extdrv2_016_overnight_sortino_proxy_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day overnight Sortino-style ratio."""
    r = _overnight_ret(close, open)
    mean_r = _rolling_mean(r, _TD_MON)
    loss_r = r.where(r < 0, np.nan)
    down_std = loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    sortino = _safe_div(mean_r, down_std + _EPS)
    return sortino.diff(_TD_WEEK)


def ocd_extdrv2_017_intraday_median_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day intraday return median."""
    med = _rolling_median(_intraday_ret(open, close), _TD_MON)
    return med.diff(_TD_WEEK)


def ocd_extdrv2_018_overnight_median_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day overnight return median."""
    med = _rolling_median(_overnight_ret(close, open), _TD_MON)
    return med.diff(_TD_WEEK)


def ocd_extdrv2_019_intraday_mean_minus_median_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of (intraday mean - median) skew proxy over 21 days (velocity of skew)."""
    r = _intraday_ret(open, close)
    skew = _rolling_mean(r, _TD_MON) - _rolling_median(r, _TD_MON)
    return skew.diff(_TD_WEEK)


def ocd_extdrv2_020_intraday_ewm63_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day EWM of intraday return (velocity of slow-smoothed drift)."""
    ewm63 = _ewm_mean(_intraday_ret(open, close), _TD_QTR)
    return ewm63.diff(_TD_WEEK)


def ocd_extdrv2_021_overnight_ewm63_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 63-day EWM of overnight return."""
    ewm63 = _ewm_mean(_overnight_ret(close, open), _TD_QTR)
    return ewm63.diff(_TD_WEEK)


def ocd_extdrv2_022_intraday_pct_rank_21d_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day intraday-return percentile rank."""
    r = _intraday_ret(open, close)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return _linslope(pct, _TD_MON)


def ocd_extdrv2_023_overnight_pct_rank_21d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day overnight-return percentile rank."""
    r = _overnight_ret(close, open)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return _linslope(pct, _TD_MON)


def ocd_extdrv2_024_both_sessions_neg_frac_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day both-sessions-negative fraction."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    frac = _rolling_count_true((intra < 0) & (over < 0), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def ocd_extdrv2_025_intraday_negative_vol_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday downside volatility (velocity of downside vol)."""
    r = _intraday_ret(open, close)
    loss_r = r.where(r < 0, np.nan)
    down_std = loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return down_std.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "ocd_extdrv2_001_intraday_ret_zscore_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_001_intraday_ret_zscore_21d_5d_diff},
    "ocd_extdrv2_002_overnight_ret_zscore_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_002_overnight_ret_zscore_21d_5d_diff},
    "ocd_extdrv2_003_intraday_ret_zscore_126d_21d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_003_intraday_ret_zscore_126d_21d_diff},
    "ocd_extdrv2_004_overnight_ret_zscore_126d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_004_overnight_ret_zscore_126d_21d_diff},
    "ocd_extdrv2_005_intraday_vol_126d_21d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_005_intraday_vol_126d_21d_diff},
    "ocd_extdrv2_006_overnight_vol_126d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_006_overnight_vol_126d_21d_diff},
    "ocd_extdrv2_007_intraday_overnight_corr_126d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_007_intraday_overnight_corr_126d_21d_diff},
    "ocd_extdrv2_008_weak_open_fraction_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_008_weak_open_fraction_21d_5d_diff},
    "ocd_extdrv2_009_weak_close_fraction_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_009_weak_close_fraction_21d_5d_diff},
    "ocd_extdrv2_010_intraday_loss_fraction_63d_21d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_010_intraday_loss_fraction_63d_21d_diff},
    "ocd_extdrv2_011_overnight_loss_fraction_63d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_011_overnight_loss_fraction_63d_21d_diff},
    "ocd_extdrv2_012_cum_intraday_loss_126d_21d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_012_cum_intraday_loss_126d_21d_diff},
    "ocd_extdrv2_013_cum_overnight_loss_126d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_013_cum_overnight_loss_126d_21d_diff},
    "ocd_extdrv2_014_intraday_overnight_vol_ratio_126d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_014_intraday_overnight_vol_ratio_126d_21d_diff},
    "ocd_extdrv2_015_intraday_sortino_proxy_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_015_intraday_sortino_proxy_21d_5d_diff},
    "ocd_extdrv2_016_overnight_sortino_proxy_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_016_overnight_sortino_proxy_21d_5d_diff},
    "ocd_extdrv2_017_intraday_median_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_017_intraday_median_21d_5d_diff},
    "ocd_extdrv2_018_overnight_median_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_018_overnight_median_21d_5d_diff},
    "ocd_extdrv2_019_intraday_mean_minus_median_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_019_intraday_mean_minus_median_21d_5d_diff},
    "ocd_extdrv2_020_intraday_ewm63_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_020_intraday_ewm63_5d_diff},
    "ocd_extdrv2_021_overnight_ewm63_5d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_021_overnight_ewm63_5d_diff},
    "ocd_extdrv2_022_intraday_pct_rank_21d_slope_21d": {"inputs": ["open", "close"], "func": ocd_extdrv2_022_intraday_pct_rank_21d_slope_21d},
    "ocd_extdrv2_023_overnight_pct_rank_21d_slope_21d": {"inputs": ["close", "open"], "func": ocd_extdrv2_023_overnight_pct_rank_21d_slope_21d},
    "ocd_extdrv2_024_both_sessions_neg_frac_63d_21d_diff": {"inputs": ["close", "open"], "func": ocd_extdrv2_024_both_sessions_neg_frac_63d_21d_diff},
    "ocd_extdrv2_025_intraday_negative_vol_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_extdrv2_025_intraday_negative_vol_21d_5d_diff},
}
