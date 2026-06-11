"""
48_open_close_dynamics — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base open-close session dynamics — velocity of intraday/overnight behavior
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def ocd_drv2_001_intraday_ret_mean_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean intraday return (velocity of intraday trend)."""
    mean21 = _rolling_mean(_intraday_ret(open, close), _TD_MON)
    return mean21.diff(_TD_WEEK)


def ocd_drv2_002_overnight_ret_mean_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean overnight return (velocity of overnight trend)."""
    mean21 = _rolling_mean(_overnight_ret(close, open), _TD_MON)
    return mean21.diff(_TD_WEEK)


def ocd_drv2_003_intraday_ret_sum_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday return sum."""
    s21 = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return s21.diff(_TD_WEEK)


def ocd_drv2_004_overnight_ret_sum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight return sum."""
    s21 = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return s21.diff(_TD_WEEK)


def ocd_drv2_005_intraday_vol_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday return standard deviation (vol velocity)."""
    std21 = _rolling_std(_intraday_ret(open, close), _TD_MON)
    return std21.diff(_TD_WEEK)


def ocd_drv2_006_overnight_vol_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight return standard deviation."""
    std21 = _rolling_std(_overnight_ret(close, open), _TD_MON)
    return std21.diff(_TD_WEEK)


def ocd_drv2_007_session_vol_ratio_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight/intraday vol ratio (shifting vol dominance)."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_MON)
    ratio = _safe_div(over_std, intra_std)
    return ratio.diff(_TD_WEEK)


def ocd_drv2_008_intraday_loss_sum_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday loss sum (acceleration of intraday pain)."""
    loss = _intraday_ret(open, close).clip(upper=0.0)
    s21 = _rolling_sum(loss, _TD_MON)
    return s21.diff(_TD_WEEK)


def ocd_drv2_009_overnight_loss_sum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight loss sum."""
    loss = _overnight_ret(close, open).clip(upper=0.0)
    s21 = _rolling_sum(loss, _TD_MON)
    return s21.diff(_TD_WEEK)


def ocd_drv2_010_both_session_loss_frac_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of fraction of both-session-loss days in 21-day window."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    frac = _rolling_count_true((intra < 0) & (over < 0), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ocd_drv2_011_giveback_frac_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday give-back fraction."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    frac = _rolling_count_true((over > 0) & (intra < 0), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ocd_drv2_012_intraday_mean_63d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day mean intraday return (monthly shift in intraday trend)."""
    mean63 = _rolling_mean(_intraday_ret(open, close), _TD_QTR)
    return mean63.diff(_TD_MON)


def ocd_drv2_013_overnight_mean_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day mean overnight return."""
    mean63 = _rolling_mean(_overnight_ret(close, open), _TD_QTR)
    return mean63.diff(_TD_MON)


def ocd_drv2_014_intraday_loss_sum_63d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day intraday loss sum."""
    loss = _intraday_ret(open, close).clip(upper=0.0)
    s63 = _rolling_sum(loss, _TD_QTR)
    return s63.diff(_TD_MON)


def ocd_drv2_015_overnight_loss_sum_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day overnight loss sum."""
    loss = _overnight_ret(close, open).clip(upper=0.0)
    s63 = _rolling_sum(loss, _TD_QTR)
    return s63.diff(_TD_MON)


def ocd_drv2_016_intraday_down_frac_21d_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day intraday down-day fraction."""
    r = _intraday_ret(open, close)
    frac = _rolling_count_true(r < 0, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_MON)


def ocd_drv2_017_overnight_down_frac_21d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day overnight down-day fraction."""
    r = _overnight_ret(close, open)
    frac = _rolling_count_true(r < 0, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_MON)


def ocd_drv2_018_intraday_cum_ret_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative intraday return."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return cum.diff(_TD_WEEK)


def ocd_drv2_019_overnight_cum_ret_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative overnight return."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return cum.diff(_TD_WEEK)


def ocd_drv2_020_intraday_vol_63d_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 63-day intraday return standard deviation."""
    std63 = _rolling_std(_intraday_ret(open, close), _TD_QTR)
    return std63.diff(_TD_MON)


def ocd_drv2_021_overnight_vol_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day overnight return standard deviation."""
    std63 = _rolling_std(_overnight_ret(close, open), _TD_QTR)
    return std63.diff(_TD_MON)


def ocd_drv2_022_giveback_count_21d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day give-back count series."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    cnt = _rolling_count_true((over > 0) & (intra < 0), _TD_MON)
    return _linslope(cnt, _TD_MON)


def ocd_drv2_023_recovery_count_21d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day intraday-recovery count."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    cnt = _rolling_count_true((over < 0) & (intra > 0), _TD_MON)
    return _linslope(cnt, _TD_MON)


def ocd_drv2_024_session_imbalance_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day (intraday cum - overnight cum) imbalance."""
    intra_cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    over_cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    imbalance = intra_cum - over_cum
    return imbalance.diff(_TD_WEEK)


def ocd_drv2_025_intraday_overnight_corr_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday/overnight return correlation."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    corr = intra.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(over)
    return corr.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_REGISTRY_2ND_DERIVATIVES = {
    "ocd_drv2_001_intraday_ret_mean_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_001_intraday_ret_mean_21d_5d_diff},
    "ocd_drv2_002_overnight_ret_mean_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_002_overnight_ret_mean_21d_5d_diff},
    "ocd_drv2_003_intraday_ret_sum_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_003_intraday_ret_sum_21d_5d_diff},
    "ocd_drv2_004_overnight_ret_sum_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_004_overnight_ret_sum_21d_5d_diff},
    "ocd_drv2_005_intraday_vol_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_005_intraday_vol_21d_5d_diff},
    "ocd_drv2_006_overnight_vol_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_006_overnight_vol_21d_5d_diff},
    "ocd_drv2_007_session_vol_ratio_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_007_session_vol_ratio_21d_5d_diff},
    "ocd_drv2_008_intraday_loss_sum_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_008_intraday_loss_sum_21d_5d_diff},
    "ocd_drv2_009_overnight_loss_sum_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_009_overnight_loss_sum_21d_5d_diff},
    "ocd_drv2_010_both_session_loss_frac_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_010_both_session_loss_frac_21d_5d_diff},
    "ocd_drv2_011_giveback_frac_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_011_giveback_frac_21d_5d_diff},
    "ocd_drv2_012_intraday_mean_63d_21d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_012_intraday_mean_63d_21d_diff},
    "ocd_drv2_013_overnight_mean_63d_21d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_013_overnight_mean_63d_21d_diff},
    "ocd_drv2_014_intraday_loss_sum_63d_21d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_014_intraday_loss_sum_63d_21d_diff},
    "ocd_drv2_015_overnight_loss_sum_63d_21d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_015_overnight_loss_sum_63d_21d_diff},
    "ocd_drv2_016_intraday_down_frac_21d_slope_21d": {"inputs": ["open", "close"], "func": ocd_drv2_016_intraday_down_frac_21d_slope_21d},
    "ocd_drv2_017_overnight_down_frac_21d_slope_21d": {"inputs": ["close", "open"], "func": ocd_drv2_017_overnight_down_frac_21d_slope_21d},
    "ocd_drv2_018_intraday_cum_ret_21d_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_018_intraday_cum_ret_21d_5d_diff},
    "ocd_drv2_019_overnight_cum_ret_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_019_overnight_cum_ret_21d_5d_diff},
    "ocd_drv2_020_intraday_vol_63d_21d_diff": {"inputs": ["open", "close"], "func": ocd_drv2_020_intraday_vol_63d_21d_diff},
    "ocd_drv2_021_overnight_vol_63d_21d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_021_overnight_vol_63d_21d_diff},
    "ocd_drv2_022_giveback_count_21d_slope_21d": {"inputs": ["close", "open"], "func": ocd_drv2_022_giveback_count_21d_slope_21d},
    "ocd_drv2_023_recovery_count_21d_slope_21d": {"inputs": ["close", "open"], "func": ocd_drv2_023_recovery_count_21d_slope_21d},
    "ocd_drv2_024_session_imbalance_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_024_session_imbalance_21d_5d_diff},
    "ocd_drv2_025_intraday_overnight_corr_21d_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv2_025_intraday_overnight_corr_21d_5d_diff},
}
