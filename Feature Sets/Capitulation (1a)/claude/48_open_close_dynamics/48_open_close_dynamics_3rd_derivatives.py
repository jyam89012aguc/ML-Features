"""
48_open_close_dynamics — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative session dynamics — acceleration of velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def ocd_drv3_001_intraday_mean_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean intraday return (acceleration of intraday trend)."""
    mean21 = _rolling_mean(_intraday_ret(open, close), _TD_MON)
    vel = mean21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_002_overnight_mean_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean overnight return (acceleration of overnight trend)."""
    mean21 = _rolling_mean(_overnight_ret(close, open), _TD_MON)
    vel = mean21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_003_intraday_vol_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day intraday vol (jerk in vol expansion)."""
    std21 = _rolling_std(_intraday_ret(open, close), _TD_MON)
    vel = std21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_004_overnight_vol_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day overnight vol."""
    std21 = _rolling_std(_overnight_ret(close, open), _TD_MON)
    vel = std21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_005_session_vol_ratio_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight/intraday vol ratio (acceleration of dominance shift)."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_MON)
    ratio = _safe_div(over_std, intra_std)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_006_intraday_loss_sum_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day intraday loss sum (jerk in intraday pain)."""
    loss = _intraday_ret(open, close).clip(upper=0.0)
    s21 = _rolling_sum(loss, _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_007_overnight_loss_sum_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day overnight loss sum."""
    loss = _overnight_ret(close, open).clip(upper=0.0)
    s21 = _rolling_sum(loss, _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_008_both_session_loss_frac_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of both-session-loss fraction (acceleration of dual-loss frequency)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    frac = _rolling_count_true((intra < 0) & (over < 0), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_009_giveback_frac_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of give-back fraction (jerk in give-back rate)."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    frac = _rolling_count_true((over > 0) & (intra < 0), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_010_intraday_mean_63d_21d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day mean intraday return."""
    mean63 = _rolling_mean(_intraday_ret(open, close), _TD_QTR)
    vel21 = mean63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_011_overnight_mean_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day mean overnight return."""
    mean63 = _rolling_mean(_overnight_ret(close, open), _TD_QTR)
    vel21 = mean63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_012_intraday_loss_sum_63d_21d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day intraday loss sum."""
    loss = _intraday_ret(open, close).clip(upper=0.0)
    s63 = _rolling_sum(loss, _TD_QTR)
    vel21 = s63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_013_overnight_loss_sum_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day overnight loss sum."""
    loss = _overnight_ret(close, open).clip(upper=0.0)
    s63 = _rolling_sum(loss, _TD_QTR)
    vel21 = s63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_014_intraday_down_frac_slope_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day intraday down-day fraction."""
    r = _intraday_ret(open, close)
    frac = _rolling_count_true(r < 0, _TD_MON) / _TD_MON
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def ocd_drv3_015_overnight_down_frac_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day overnight down-day fraction."""
    r = _overnight_ret(close, open)
    frac = _rolling_count_true(r < 0, _TD_MON) / _TD_MON
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def ocd_drv3_016_intraday_vol_63d_21d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day intraday vol."""
    std63 = _rolling_std(_intraday_ret(open, close), _TD_QTR)
    vel21 = std63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_017_overnight_vol_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day overnight vol."""
    std63 = _rolling_std(_overnight_ret(close, open), _TD_QTR)
    vel21 = std63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ocd_drv3_018_giveback_count_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day give-back count."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    cnt = _rolling_count_true((over > 0) & (intra < 0), _TD_MON)
    slp = _linslope(cnt, _TD_MON)
    return slp.diff(_TD_WEEK)


def ocd_drv3_019_recovery_count_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day intraday-recovery count."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    cnt = _rolling_count_true((over < 0) & (intra > 0), _TD_MON)
    slp = _linslope(cnt, _TD_MON)
    return slp.diff(_TD_WEEK)


def ocd_drv3_020_session_imbalance_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of (cum intraday - cum overnight) imbalance."""
    intra_cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    over_cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    imbalance = intra_cum - over_cum
    vel = imbalance.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_021_intraday_overnight_corr_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day intraday/overnight correlation."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    corr = intra.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(over)
    vel = corr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_022_intraday_cum_ret_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative intraday return."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    vel = cum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_023_overnight_cum_ret_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative overnight return."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    vel = cum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ocd_drv3_024_intraday_mean_21d_5d_diff_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day velocity of 21-day mean intraday return."""
    mean21 = _rolling_mean(_intraday_ret(open, close), _TD_MON)
    vel = mean21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ocd_drv3_025_overnight_mean_21d_5d_diff_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day velocity of 21-day mean overnight return."""
    mean21 = _rolling_mean(_overnight_ret(close, open), _TD_MON)
    vel = mean21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_REGISTRY_3RD_DERIVATIVES = {
    "ocd_drv3_001_intraday_mean_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_001_intraday_mean_21d_5d_diff_5d_diff},
    "ocd_drv3_002_overnight_mean_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_002_overnight_mean_21d_5d_diff_5d_diff},
    "ocd_drv3_003_intraday_vol_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_003_intraday_vol_21d_5d_diff_5d_diff},
    "ocd_drv3_004_overnight_vol_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_004_overnight_vol_21d_5d_diff_5d_diff},
    "ocd_drv3_005_session_vol_ratio_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_005_session_vol_ratio_5d_diff_5d_diff},
    "ocd_drv3_006_intraday_loss_sum_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_006_intraday_loss_sum_21d_5d_diff_5d_diff},
    "ocd_drv3_007_overnight_loss_sum_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_007_overnight_loss_sum_21d_5d_diff_5d_diff},
    "ocd_drv3_008_both_session_loss_frac_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_008_both_session_loss_frac_5d_diff_5d_diff},
    "ocd_drv3_009_giveback_frac_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_009_giveback_frac_5d_diff_5d_diff},
    "ocd_drv3_010_intraday_mean_63d_21d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_010_intraday_mean_63d_21d_diff_5d_diff},
    "ocd_drv3_011_overnight_mean_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_011_overnight_mean_63d_21d_diff_5d_diff},
    "ocd_drv3_012_intraday_loss_sum_63d_21d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_012_intraday_loss_sum_63d_21d_diff_5d_diff},
    "ocd_drv3_013_overnight_loss_sum_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_013_overnight_loss_sum_63d_21d_diff_5d_diff},
    "ocd_drv3_014_intraday_down_frac_slope_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_014_intraday_down_frac_slope_5d_diff},
    "ocd_drv3_015_overnight_down_frac_slope_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_015_overnight_down_frac_slope_5d_diff},
    "ocd_drv3_016_intraday_vol_63d_21d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_016_intraday_vol_63d_21d_diff_5d_diff},
    "ocd_drv3_017_overnight_vol_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_017_overnight_vol_63d_21d_diff_5d_diff},
    "ocd_drv3_018_giveback_count_slope_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_018_giveback_count_slope_5d_diff},
    "ocd_drv3_019_recovery_count_slope_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_019_recovery_count_slope_5d_diff},
    "ocd_drv3_020_session_imbalance_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_020_session_imbalance_5d_diff_5d_diff},
    "ocd_drv3_021_intraday_overnight_corr_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_021_intraday_overnight_corr_5d_diff_5d_diff},
    "ocd_drv3_022_intraday_cum_ret_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ocd_drv3_022_intraday_cum_ret_21d_5d_diff_5d_diff},
    "ocd_drv3_023_overnight_cum_ret_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ocd_drv3_023_overnight_cum_ret_21d_5d_diff_5d_diff},
    "ocd_drv3_024_intraday_mean_21d_5d_diff_slope_21d": {"inputs": ["open", "close"], "func": ocd_drv3_024_intraday_mean_21d_5d_diff_slope_21d},
    "ocd_drv3_025_overnight_mean_21d_5d_diff_slope_21d": {"inputs": ["close", "open"], "func": ocd_drv3_025_overnight_mean_21d_5d_diff_slope_21d},
}
