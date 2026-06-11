"""
43_downside_deviation — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base downside-deviation features — velocity of semi-variance
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dsd_drv2_001_semi_dev_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day semi-deviation (velocity of short-term downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    return sd.diff(_TD_WEEK)


def dsd_drv2_002_semi_dev_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day semi-deviation (monthly change in downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    return sd.diff(_TD_MON)


def dsd_drv2_003_semi_dev_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day semi-deviation (weekly velocity of medium-term downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    return sd.diff(_TD_WEEK)


def dsd_drv2_004_semi_dev_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day semi-deviation."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    return sd.diff(_TD_MON)


def dsd_drv2_005_semi_dev_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day semi-deviation (monthly change in annual downside vol)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_YEAR)
    return sd.diff(_TD_MON)


def dsd_drv2_006_lpm2_vs0_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day LPM2 vs target=0 (velocity of semi-variance)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 2, 0.0)
    return lpm.diff(_TD_WEEK)


def dsd_drv2_007_lpm2_vs0_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day LPM2 vs 0."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 2, 0.0)
    return lpm.diff(_TD_MON)


def dsd_drv2_008_lpm1_vs0_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day LPM1 vs 0 (velocity of expected shortfall)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 1, 0.0)
    return lpm.diff(_TD_WEEK)


def dsd_drv2_009_downside_upside_vol_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up vol ratio."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_WEEK)


def dsd_drv2_010_downside_upside_vol_ratio_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day down/up vol ratio."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_MON)


def dsd_drv2_011_semi_variance_norm_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day semi-variance as fraction of total variance."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    tv = (r ** 2).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    ratio = _safe_div(sv, tv)
    return ratio.diff(_TD_WEEK)


def dsd_drv2_012_lpm3_vs0_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day LPM3 vs 0 (velocity of cubic tail risk)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 3, 0.0)
    return lpm.diff(_TD_WEEK)


def dsd_drv2_013_semi_dev_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day semi-deviation over trailing 21 days."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    return _linslope(sd, _TD_MON)


def dsd_drv2_014_semi_dev_63d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day semi-deviation over trailing 63 days."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_QTR)
    return _linslope(sd, _TD_QTR)


def dsd_drv2_015_sortino_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Sortino ratio (velocity of risk-adjusted return)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    sd = _semi_dev_w(r, _TD_MON)
    sortino = _safe_div(mu, sd)
    return sortino.diff(_TD_WEEK)


def dsd_drv2_016_downside_vol_share_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day downside vol share."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    share = _safe_div(dn, dn + up)
    return share.diff(_TD_WEEK)


def dsd_drv2_017_lpm1_vs_mean_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day LPM1 vs rolling mean."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    below = (mu - r).clip(lower=0.0)
    lpm1_mu = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return lpm1_mu.diff(_TD_WEEK)


def dsd_drv2_018_semi_dev_21d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day semi-dev z-score (velocity of extremity)."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    mu = _rolling_mean(sd, _TD_YEAR)
    sig = _rolling_std(sd, _TD_YEAR)
    z = _safe_div(sd - mu, sig)
    return z.diff(_TD_WEEK)


def dsd_drv2_019_semi_dev_ratio_21d_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ratio of 21-day to 63-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(sd21, sd63)
    return ratio.diff(_TD_WEEK)


def dsd_drv2_020_vol_weighted_semi_dev_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted 21-day semi-deviation."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    sq = (r ** 2 * vol_norm).where(r < 0.0, 0.0)
    wt = vol_norm.where(r < 0.0, 0.0)
    num = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    den = wt.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    sd = np.sqrt(_safe_div(num, den).clip(lower=0.0))
    return sd.diff(_TD_WEEK)


def dsd_drv2_021_lpm2_vs0_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day LPM2 vs 0 (monthly change in annual semi-variance)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_YEAR, 2, 0.0)
    return lpm.diff(_TD_MON)


def dsd_drv2_022_semi_dev_composite_3window_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite semi-dev (avg of normalized 21d/63d/252d)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    n21 = _safe_div(sd21, _rolling_mean(sd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(sd63, _rolling_mean(sd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(sd252, _rolling_mean(sd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    return composite.diff(_TD_WEEK)


def dsd_drv2_023_lpm3_vs0_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day LPM3 vs 0 (monthly change in tail risk)."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 3, 0.0)
    return lpm.diff(_TD_MON)


def dsd_drv2_024_semi_dev_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day semi-deviation over trailing 63 days."""
    r = _log_ret(close)
    sd = _semi_dev_w(r, _TD_MON)
    return _linslope(sd, _TD_QTR)


def dsd_drv2_025_lpm1_vs_neg1pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day LPM1 vs -1% target (velocity of tail shortfall)."""
    r = _log_ret(close)
    threshold = np.log(1 - 0.01)
    below = (threshold - r).clip(lower=0.0)
    lpm = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return lpm.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_REGISTRY_2ND_DERIVATIVES = {
    "dsd_drv2_001_semi_dev_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_001_semi_dev_21d_5d_diff},
    "dsd_drv2_002_semi_dev_21d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_002_semi_dev_21d_21d_diff},
    "dsd_drv2_003_semi_dev_63d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_003_semi_dev_63d_5d_diff},
    "dsd_drv2_004_semi_dev_63d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_004_semi_dev_63d_21d_diff},
    "dsd_drv2_005_semi_dev_252d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_005_semi_dev_252d_21d_diff},
    "dsd_drv2_006_lpm2_vs0_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_006_lpm2_vs0_21d_5d_diff},
    "dsd_drv2_007_lpm2_vs0_63d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_007_lpm2_vs0_63d_21d_diff},
    "dsd_drv2_008_lpm1_vs0_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_008_lpm1_vs0_21d_5d_diff},
    "dsd_drv2_009_downside_upside_vol_ratio_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_009_downside_upside_vol_ratio_21d_5d_diff},
    "dsd_drv2_010_downside_upside_vol_ratio_63d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_010_downside_upside_vol_ratio_63d_21d_diff},
    "dsd_drv2_011_semi_variance_norm_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_011_semi_variance_norm_21d_5d_diff},
    "dsd_drv2_012_lpm3_vs0_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_012_lpm3_vs0_21d_5d_diff},
    "dsd_drv2_013_semi_dev_21d_slope_21d": {"inputs": ["close"], "func": dsd_drv2_013_semi_dev_21d_slope_21d},
    "dsd_drv2_014_semi_dev_63d_slope_63d": {"inputs": ["close"], "func": dsd_drv2_014_semi_dev_63d_slope_63d},
    "dsd_drv2_015_sortino_ratio_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_015_sortino_ratio_21d_5d_diff},
    "dsd_drv2_016_downside_vol_share_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_016_downside_vol_share_21d_5d_diff},
    "dsd_drv2_017_lpm1_vs_mean_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_017_lpm1_vs_mean_21d_5d_diff},
    "dsd_drv2_018_semi_dev_21d_zscore_5d_diff": {"inputs": ["close"], "func": dsd_drv2_018_semi_dev_21d_zscore_5d_diff},
    "dsd_drv2_019_semi_dev_ratio_21d_63d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_019_semi_dev_ratio_21d_63d_5d_diff},
    "dsd_drv2_020_vol_weighted_semi_dev_21d_5d_diff": {"inputs": ["close", "volume"], "func": dsd_drv2_020_vol_weighted_semi_dev_21d_5d_diff},
    "dsd_drv2_021_lpm2_vs0_252d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_021_lpm2_vs0_252d_21d_diff},
    "dsd_drv2_022_semi_dev_composite_3window_5d_diff": {"inputs": ["close"], "func": dsd_drv2_022_semi_dev_composite_3window_5d_diff},
    "dsd_drv2_023_lpm3_vs0_63d_21d_diff": {"inputs": ["close"], "func": dsd_drv2_023_lpm3_vs0_63d_21d_diff},
    "dsd_drv2_024_semi_dev_21d_slope_63d": {"inputs": ["close"], "func": dsd_drv2_024_semi_dev_21d_slope_63d},
    "dsd_drv2_025_lpm1_vs_neg1pct_21d_5d_diff": {"inputs": ["close"], "func": dsd_drv2_025_lpm1_vs_neg1pct_21d_5d_diff},
}
