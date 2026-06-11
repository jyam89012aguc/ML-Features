"""
43_downside_deviation — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative downside-deviation features — acceleration
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


def _log_ret(s: pd.Series) -> pd.Series:
    """Daily log-return series."""
    return np.log(s.clip(lower=_EPS)).diff(1)


def _lpm(r: pd.Series, w: int, order: int, threshold: float = 0.0) -> pd.Series:
    """Rolling lower partial moment of given order."""
    below = ((threshold - r).clip(lower=0.0) ** order)
    return below.rolling(w, min_periods=max(1, w // 2)).mean()


def _semi_dev_w(r: pd.Series, w: int) -> pd.Series:
    """Semi-deviation of log-returns below zero over window w."""
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(w, min_periods=max(1, w // 2)).mean())


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

def dsd_drv3_001_semi_dev_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day semi-deviation (acceleration of downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_002_semi_dev_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21-day semi-dev (jerk in downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    vel21 = sd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_003_semi_dev_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day semi-deviation (acceleration of medium-term risk)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_004_semi_dev_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day semi-deviation."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    vel21 = sd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_005_lpm2_vs0_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day LPM2 vs 0 (acceleration of semi-variance)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 2, 0.0)
    vel = lpm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_006_lpm1_vs0_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day LPM1 vs 0 (jerk in expected shortfall)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 1, 0.0)
    vel = lpm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_007_downside_upside_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day downside/upside vol ratio (acceleration of asymmetry)."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    ratio = _safe_div(dn, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_008_semi_dev_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day semi-dev."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    vel = sd.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dsd_drv3_009_semi_dev_63d_21d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day change in 63-day semi-dev."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    vel21 = sd.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def dsd_drv3_010_lpm3_vs0_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day LPM3 vs 0 (acceleration of cubic tail risk)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 3, 0.0)
    vel = lpm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_011_sortino_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Sortino ratio (acceleration of risk-adjusted return)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    sd = _semi_dev_w(r, _TD_MON)
    sortino = _safe_div(mu, sd)
    vel = sortino.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_012_semi_variance_norm_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day semi-variance share of total variance."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    tv = (r ** 2).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    ratio = _safe_div(sv, tv)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_013_semi_dev_21d_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day semi-dev z-score (jerk in extremity measure)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    mu = _rolling_mean(sd, _TD_YEAR)
    sig = _rolling_std(sd, _TD_YEAR)
    z = _safe_div(sd - mu, sig)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_014_lpm2_vs0_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day LPM2 vs 0."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 2, 0.0)
    vel21 = lpm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_015_vol_weighted_semi_dev_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol-weighted 21-day semi-dev (acceleration of vol-intensity)."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    sq = (r ** 2 * vol_norm).where(r < 0.0, 0.0)
    wt = vol_norm.where(r < 0.0, 0.0)
    num = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    den = wt.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    sd = np.sqrt(_safe_div(num, den).clip(lower=0.0))
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_016_semi_dev_ratio_21d_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/63d semi-dev ratio (acceleration of term-structure shift)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(sd21, sd63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_017_downside_vol_share_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day downside vol share (acceleration of asymmetry shift)."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    share = _safe_div(dn, dn + up)
    vel = share.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_018_lpm1_vs_mean_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day LPM1 vs rolling mean (jerk in mean shortfall)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    below = (mu - r).clip(lower=0.0)
    lpm1_mu = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = lpm1_mu.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_019_semi_dev_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day semi-dev (rate of slope change)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    slp = _linslope(sd, _TD_MON)
    return slp.diff(_TD_WEEK)


def dsd_drv3_020_semi_dev_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day semi-dev (jerk in long-run downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_YEAR)
    vel21 = sd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_021_lpm3_vs0_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day LPM3 vs 0 (jerk in tail risk)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 3, 0.0)
    vel21 = lpm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_022_semi_dev_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite semi-dev (avg normalized 21d/63d/252d)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    n21 = _safe_div(sd21, _rolling_mean(sd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(sd63, _rolling_mean(sd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(sd252, _rolling_mean(sd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_drv3_023_downside_upside_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down/up vol ratio."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(dn, up)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_drv3_024_semi_dev_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of 21-day semi-dev."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    slp = _linslope(sd, _TD_QTR)
    return slp.diff(_TD_WEEK)


def dsd_drv3_025_lpm1_vs_neg1pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day LPM1 vs -1% target (jerk in tail shortfall velocity)."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = (threshold - r).clip(lower=0.0)
    lpm = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = lpm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_REGISTRY_3RD_DERIVATIVES = {
    "dsd_drv3_001_semi_dev_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_001_semi_dev_21d_5d_diff_5d_diff},
    "dsd_drv3_002_semi_dev_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_002_semi_dev_21d_21d_diff_5d_diff},
    "dsd_drv3_003_semi_dev_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_003_semi_dev_63d_5d_diff_5d_diff},
    "dsd_drv3_004_semi_dev_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_004_semi_dev_63d_21d_diff_5d_diff},
    "dsd_drv3_005_lpm2_vs0_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_005_lpm2_vs0_21d_5d_diff_5d_diff},
    "dsd_drv3_006_lpm1_vs0_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_006_lpm1_vs0_21d_5d_diff_5d_diff},
    "dsd_drv3_007_downside_upside_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_007_downside_upside_ratio_21d_5d_diff_5d_diff},
    "dsd_drv3_008_semi_dev_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dsd_drv3_008_semi_dev_21d_5d_diff_slope_21d},
    "dsd_drv3_009_semi_dev_63d_21d_diff_slope_21d": {"inputs": ["close"], "func": dsd_drv3_009_semi_dev_63d_21d_diff_slope_21d},
    "dsd_drv3_010_lpm3_vs0_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_010_lpm3_vs0_21d_5d_diff_5d_diff},
    "dsd_drv3_011_sortino_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_011_sortino_ratio_21d_5d_diff_5d_diff},
    "dsd_drv3_012_semi_variance_norm_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_012_semi_variance_norm_21d_5d_diff_5d_diff},
    "dsd_drv3_013_semi_dev_21d_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_013_semi_dev_21d_zscore_5d_diff_5d_diff},
    "dsd_drv3_014_lpm2_vs0_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_014_lpm2_vs0_63d_21d_diff_5d_diff},
    "dsd_drv3_015_vol_weighted_semi_dev_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dsd_drv3_015_vol_weighted_semi_dev_21d_5d_diff_5d_diff},
    "dsd_drv3_016_semi_dev_ratio_21d_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_016_semi_dev_ratio_21d_63d_5d_diff_5d_diff},
    "dsd_drv3_017_downside_vol_share_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_017_downside_vol_share_21d_5d_diff_5d_diff},
    "dsd_drv3_018_lpm1_vs_mean_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_018_lpm1_vs_mean_21d_5d_diff_5d_diff},
    "dsd_drv3_019_semi_dev_21d_slope_5d_diff": {"inputs": ["close"], "func": dsd_drv3_019_semi_dev_21d_slope_5d_diff},
    "dsd_drv3_020_semi_dev_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_020_semi_dev_252d_21d_diff_5d_diff},
    "dsd_drv3_021_lpm3_vs0_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_021_lpm3_vs0_63d_21d_diff_5d_diff},
    "dsd_drv3_022_semi_dev_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_022_semi_dev_composite_5d_diff_5d_diff},
    "dsd_drv3_023_downside_upside_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_023_downside_upside_ratio_63d_21d_diff_5d_diff},
    "dsd_drv3_024_semi_dev_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": dsd_drv3_024_semi_dev_21d_slope_63d_5d_diff},
    "dsd_drv3_025_lpm1_vs_neg1pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_drv3_025_lpm1_vs_neg1pct_21d_5d_diff_5d_diff},
}
