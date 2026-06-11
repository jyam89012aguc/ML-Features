"""
114_overnight_intraday_split — 3rd Derivatives (Features ois_drv3_001-025)
Domain: rate of change of 2nd-derivative overnight/intraday features — acceleration
        of session-return velocity, jerk in gap distress, acceleration of vol shifts
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _overnight_ret(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight return: prior close -> today open."""
    return open_ / close.shift(1) - 1.0


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return: today open -> today close."""
    return close / open_ - 1.0


def _total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close -> today close."""
    return close.pct_change(1)


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

def ois_drv3_001_overnight_ret_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight return (acceleration of gap velocity)."""
    vel = _overnight_ret(close, open).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_002_intraday_ret_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of intraday return (acceleration of intraday velocity)."""
    vel = _intraday_ret(open, close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_003_overnight_ret_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of overnight return (jerk in monthly gap trend)."""
    vel21 = _overnight_ret(close, open).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ois_drv3_004_intraday_ret_21d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of intraday return."""
    vel21 = _intraday_ret(open, close).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ois_drv3_005_cum_overnight_ret_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative overnight return (jerk in overnight pressure)."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    vel = cum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_006_cum_intraday_ret_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative intraday return."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    vel = cum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_007_overnight_vol_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day overnight vol (acceleration of vol change)."""
    vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    vel = vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_008_intraday_vol_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day intraday vol."""
    vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    vel = vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_009_overnight_distress_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight distress score (jerk in distress deepening)."""
    dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_010_intraday_distress_21d_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of intraday distress score."""
    dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_011_overnight_vol_ratio_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight/intraday vol ratio."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    ratio = _safe_div(on_vol, intra_vol.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_012_overnight_negative_frac_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d overnight negative day fraction."""
    frac = _rolling_sum((_overnight_ret(close, open) < 0).astype(float), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_013_intraday_negative_frac_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d intraday negative day fraction."""
    frac = _rolling_sum((_intraday_ret(open, close) < 0).astype(float), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_014_overnight_share_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight cumulative share of 21-day total return."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    tot = _rolling_sum(_total_ret(close), _TD_MON)
    share = _safe_div(on, tot.replace(0, np.nan))
    vel = share.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_015_gap_persistence_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight gap persistence ratio (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    gap_down = on < 0
    persistent = (gap_down & (intra < 0)).astype(float)
    gap_cnt = _rolling_sum(gap_down.astype(float), _TD_MON)
    pers_cnt = _rolling_sum(persistent, _TD_MON)
    pers_ratio = _safe_div(pers_cnt, gap_cnt.replace(0, np.nan))
    vel = pers_ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_016_reversal_frac_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of intraday reversal fraction."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    rev = ((np.sign(on) != np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)
    frac = _rolling_sum(rev, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_017_overnight_zscore_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight return 63d z-score."""
    on = _overnight_ret(close, open)
    m = _rolling_mean(on, _TD_QTR)
    s = _rolling_std(on, _TD_QTR)
    z = _safe_div(on - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_018_intraday_zscore_5d_diff_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of intraday return 63d z-score."""
    intra = _intraday_ret(open, close)
    m = _rolling_mean(intra, _TD_QTR)
    s = _rolling_std(intra, _TD_QTR)
    z = _safe_div(intra - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_019_overnight_distress_21d_diff_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of overnight distress."""
    dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    vel21 = dist.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def ois_drv3_020_intraday_distress_21d_diff_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of intraday distress."""
    dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    vel21 = dist.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def ois_drv3_021_overnight_vol_5d_diff_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of overnight vol."""
    vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    vel5 = vol.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def ois_drv3_022_intraday_vol_5d_diff_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of intraday vol."""
    vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    vel5 = vol.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def ois_drv3_023_cum_overnight_21d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21d cumulative overnight return."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    vel21 = cum.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ois_drv3_024_overnight_down_consec_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight down consecutive streak."""
    streak = _consec_streak(_overnight_ret(close, open) < 0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ois_drv3_025_overnight_vs_intraday_distress_ratio_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight-to-intraday distress ratio."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0).abs(), _TD_QTR)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0).abs(), _TD_QTR)
    ratio = _safe_div(on_dist, intra_dist.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OVERNIGHT_INTRADAY_SPLIT_REGISTRY_3RD_DERIVATIVES = {
    "ois_drv3_001_overnight_ret_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_001_overnight_ret_5d_diff_5d_diff},
    "ois_drv3_002_intraday_ret_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_002_intraday_ret_5d_diff_5d_diff},
    "ois_drv3_003_overnight_ret_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_003_overnight_ret_21d_diff_5d_diff},
    "ois_drv3_004_intraday_ret_21d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_004_intraday_ret_21d_diff_5d_diff},
    "ois_drv3_005_cum_overnight_ret_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_005_cum_overnight_ret_21d_5d_diff_5d_diff},
    "ois_drv3_006_cum_intraday_ret_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_006_cum_intraday_ret_21d_5d_diff_5d_diff},
    "ois_drv3_007_overnight_vol_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_007_overnight_vol_21d_5d_diff_5d_diff},
    "ois_drv3_008_intraday_vol_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_008_intraday_vol_21d_5d_diff_5d_diff},
    "ois_drv3_009_overnight_distress_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_009_overnight_distress_21d_5d_diff_5d_diff},
    "ois_drv3_010_intraday_distress_21d_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_010_intraday_distress_21d_5d_diff_5d_diff},
    "ois_drv3_011_overnight_vol_ratio_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_011_overnight_vol_ratio_5d_diff_5d_diff},
    "ois_drv3_012_overnight_negative_frac_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_012_overnight_negative_frac_5d_diff_5d_diff},
    "ois_drv3_013_intraday_negative_frac_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_013_intraday_negative_frac_5d_diff_5d_diff},
    "ois_drv3_014_overnight_share_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_014_overnight_share_5d_diff_5d_diff},
    "ois_drv3_015_gap_persistence_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_015_gap_persistence_5d_diff_5d_diff},
    "ois_drv3_016_reversal_frac_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_016_reversal_frac_5d_diff_5d_diff},
    "ois_drv3_017_overnight_zscore_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_017_overnight_zscore_5d_diff_5d_diff},
    "ois_drv3_018_intraday_zscore_5d_diff_5d_diff": {"inputs": ["open", "close"], "func": ois_drv3_018_intraday_zscore_5d_diff_5d_diff},
    "ois_drv3_019_overnight_distress_21d_diff_slope_21d": {"inputs": ["close", "open"], "func": ois_drv3_019_overnight_distress_21d_diff_slope_21d},
    "ois_drv3_020_intraday_distress_21d_diff_slope_21d": {"inputs": ["open", "close"], "func": ois_drv3_020_intraday_distress_21d_diff_slope_21d},
    "ois_drv3_021_overnight_vol_5d_diff_slope_21d": {"inputs": ["close", "open"], "func": ois_drv3_021_overnight_vol_5d_diff_slope_21d},
    "ois_drv3_022_intraday_vol_5d_diff_slope_21d": {"inputs": ["open", "close"], "func": ois_drv3_022_intraday_vol_5d_diff_slope_21d},
    "ois_drv3_023_cum_overnight_21d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_023_cum_overnight_21d_21d_diff_5d_diff},
    "ois_drv3_024_overnight_down_consec_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_024_overnight_down_consec_5d_diff_5d_diff},
    "ois_drv3_025_overnight_vs_intraday_distress_ratio_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ois_drv3_025_overnight_vs_intraday_distress_ratio_5d_diff_5d_diff},
}
