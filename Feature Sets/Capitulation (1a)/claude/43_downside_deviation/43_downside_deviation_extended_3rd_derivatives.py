"""
43_downside_deviation — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative downside concepts — acceleration of
        MAR-threshold velocity, EWM semi-dev ratio momentum, VaR/CVaR velocity changes,
        downside skewness jerk, tail-ratio curvature, pain-index acceleration,
        and capitulation composite curvature.
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


def _log_ret(s: pd.Series) -> pd.Series:
    """Daily log-return series."""
    return np.log(s.clip(lower=_EPS)).diff(1)


def _semi_dev_w(r: pd.Series, w: int, thr: float = 0.0) -> pd.Series:
    """Rolling semi-deviation: sqrt(mean squared returns below thr)."""
    sq = (r ** 2).where(r < thr, 0.0)
    return np.sqrt(sq.rolling(w, min_periods=max(1, w // 2)).mean())


def _lpm(r: pd.Series, w: int, order: int, threshold: float = 0.0) -> pd.Series:
    """Rolling lower partial moment of given order."""
    below = ((threshold - r).clip(lower=0.0) ** order)
    return below.rolling(w, min_periods=max(1, w // 2)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = float(np.nanmean(x))
        num = float(((xi - xi_m) * (x - x_m)).sum())
        den = float(((xi - xi_m) ** 2).sum())
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each = diff/slope applied to a 2nd-derivative extended concept

def dsd_extdrv3_001_semi_dev_mar05pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d semi-dev vs MAR=+0.5%/day (acceleration of positive-target shortfall)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_002_semi_dev_ewm_span10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM semi-dev span=10 (acceleration of fast-decay downside vol)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd = np.sqrt(sq.ewm(span=10, min_periods=5).mean())
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_003_semi_dev_ewm_span63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM semi-dev span=63 (acceleration of quarterly-decay downside vol)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd = np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    vel = sd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_004_semi_dev_ewm_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM semi-dev ratio (span=10/span=63) — acceleration of regime shift."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    fast = np.sqrt(sq.ewm(span=10, min_periods=5).mean())
    slow = np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(fast, slow)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_005_var5_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d VaR at 5% (acceleration of tail quantile movement)."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    vel = var5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_006_var5_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d VaR at 5% (jerk in medium-term tail)."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    vel21 = var5.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_extdrv3_007_cvar5_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d CVaR at 5% (acceleration of expected tail loss)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    cvar = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = cvar.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_008_tail_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d tail ratio (acceleration of downside-upside tail curvature)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    q95 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.95)
    ratio = _safe_div(q05.abs(), q95.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_009_tail_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d tail ratio (jerk in medium-term tail asymmetry)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    q95 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.95)
    ratio = _safe_div(q05.abs(), q95.clip(lower=_EPS))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_extdrv3_010_downside_skew_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d downside skewness (acceleration of tail-shape change)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    skew = dn.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_011_downside_skew_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d downside skewness (jerk in skew regime)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    skew = dn.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    vel21 = skew.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_extdrv3_012_downside_count_frac_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d down-day fraction (acceleration of bear-day frequency)."""
    r = _log_ret(close)
    frac = (r < 0.0).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_013_downside_count_frac_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d down-day fraction."""
    r = _log_ret(close)
    frac = (r < 0.0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_extdrv3_014_downside_pain_index_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d pain index (acceleration of within-period drawdown pain)."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    peak = cum.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    pain = _rolling_mean(dd, _TD_MON)
    vel = pain.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_015_downside_pain_index_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d pain index (jerk in medium-term drawdown pain)."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    peak = cum.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    pain = _rolling_mean(dd, _TD_QTR)
    vel21 = pain.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dsd_extdrv3_016_sortino_mar05pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d Sortino vs MAR=+0.5%/day (acceleration of target-Sortino)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    mu = _rolling_mean(r, _TD_MON)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sortino = _safe_div(mu - mar, sd)
    vel = sortino.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_017_lpm2_ewm_span21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM LPM2 (span=21) — acceleration of EWM semi-variance."""
    r = _log_ret(close)
    below_sq = ((0.0 - r).clip(lower=0.0) ** 2)
    lpm = below_sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = lpm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_018_semi_dev_pct_rank_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d semi-dev pct-rank within 63d dist (acceleration of rank movement)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    pct = sd21.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_019_semi_dev_zscore_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d semi-dev z-score vs 126d dist (acceleration of z-score)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = _rolling_mean(sd21, _TD_HALF)
    sig = _rolling_std(sd21, _TD_HALF)
    z = _safe_div(sd21 - mu, sig)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_020_var5_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d VaR at 5% (rate of slope change in tail quantile)."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    slp = _linslope(var5, _TD_MON)
    return slp.diff(_TD_WEEK)


def dsd_extdrv3_021_cvar5_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d CVaR at 5%."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    cvar = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = cvar.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dsd_extdrv3_022_downside_kurt_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d downside kurtosis (acceleration of fat-tail emergence)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    kurt = dn.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()
    vel = kurt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_023_capitulation_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of capitulation composite (acceleration of distress score)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    avg252 = _rolling_mean(sd21, _TD_YEAR)
    norm = _safe_div(sd21, avg252.replace(0, np.nan))
    mu = _rolling_mean(sd21, _TD_YEAR)
    sig = _rolling_std(sd21, _TD_YEAR)
    z = _safe_div(sd21 - mu, sig).clip(-3.0, 3.0) / 3.0
    pct_rank = sd21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    composite = norm.fillna(1.0) + z.fillna(0.0) + (1.0 - pct_rank)
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dsd_extdrv3_024_semi_dev_mar05pct_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d MAR=+0.5% semi-dev (rate-of-slope-change of positive-target shortfall)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    slp = _linslope(sd, _TD_MON)
    return slp.diff(_TD_WEEK)


def dsd_extdrv3_025_downside_pain_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d pain index (rate of slope change of drawdown pain)."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    peak = cum.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    pain = _rolling_mean(dd, _TD_MON)
    slp = _linslope(pain, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "dsd_extdrv3_001_semi_dev_mar05pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_001_semi_dev_mar05pct_21d_5d_diff_5d_diff},
    "dsd_extdrv3_002_semi_dev_ewm_span10_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_002_semi_dev_ewm_span10_5d_diff_5d_diff},
    "dsd_extdrv3_003_semi_dev_ewm_span63_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_003_semi_dev_ewm_span63_5d_diff_5d_diff},
    "dsd_extdrv3_004_semi_dev_ewm_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_004_semi_dev_ewm_ratio_5d_diff_5d_diff},
    "dsd_extdrv3_005_var5_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_005_var5_21d_5d_diff_5d_diff},
    "dsd_extdrv3_006_var5_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_006_var5_63d_21d_diff_5d_diff},
    "dsd_extdrv3_007_cvar5_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_007_cvar5_21d_5d_diff_5d_diff},
    "dsd_extdrv3_008_tail_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_008_tail_ratio_21d_5d_diff_5d_diff},
    "dsd_extdrv3_009_tail_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_009_tail_ratio_63d_21d_diff_5d_diff},
    "dsd_extdrv3_010_downside_skew_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_010_downside_skew_21d_5d_diff_5d_diff},
    "dsd_extdrv3_011_downside_skew_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_011_downside_skew_63d_21d_diff_5d_diff},
    "dsd_extdrv3_012_downside_count_frac_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_012_downside_count_frac_21d_5d_diff_5d_diff},
    "dsd_extdrv3_013_downside_count_frac_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_013_downside_count_frac_63d_21d_diff_5d_diff},
    "dsd_extdrv3_014_downside_pain_index_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_014_downside_pain_index_21d_5d_diff_5d_diff},
    "dsd_extdrv3_015_downside_pain_index_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_015_downside_pain_index_63d_21d_diff_5d_diff},
    "dsd_extdrv3_016_sortino_mar05pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_016_sortino_mar05pct_21d_5d_diff_5d_diff},
    "dsd_extdrv3_017_lpm2_ewm_span21_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_017_lpm2_ewm_span21_5d_diff_5d_diff},
    "dsd_extdrv3_018_semi_dev_pct_rank_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_018_semi_dev_pct_rank_63d_5d_diff_5d_diff},
    "dsd_extdrv3_019_semi_dev_zscore_126d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_019_semi_dev_zscore_126d_5d_diff_5d_diff},
    "dsd_extdrv3_020_var5_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_020_var5_21d_slope_21d_5d_diff},
    "dsd_extdrv3_021_cvar5_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dsd_extdrv3_021_cvar5_21d_5d_diff_slope_21d},
    "dsd_extdrv3_022_downside_kurt_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_022_downside_kurt_21d_5d_diff_5d_diff},
    "dsd_extdrv3_023_capitulation_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_023_capitulation_composite_5d_diff_5d_diff},
    "dsd_extdrv3_024_semi_dev_mar05pct_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_024_semi_dev_mar05pct_21d_slope_21d_5d_diff},
    "dsd_extdrv3_025_downside_pain_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv3_025_downside_pain_21d_slope_21d_5d_diff},
}
