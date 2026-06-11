"""
43_downside_deviation — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended base downside-deviation concepts — velocity of
        MAR-threshold semi-deviations, EWM semi-dev ratios, VaR/CVaR measures,
        downside skewness, tail-ratio, pain-index, and capitulation composite.
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


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

def dsd_extdrv2_001_semi_dev_mar05pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d semi-dev vs MAR=+0.5%/day (velocity of positive-target shortfall)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return sd.diff(_TD_WEEK)


def dsd_extdrv2_002_semi_dev_mar05pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d semi-dev vs MAR=+0.5%/day."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return sd.diff(_TD_MON)


def dsd_extdrv2_003_semi_dev_ewm_span10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM semi-dev span=10 (velocity of fast-decay downside vol)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd = np.sqrt(sq.ewm(span=10, min_periods=5).mean())
    return sd.diff(_TD_WEEK)


def dsd_extdrv2_004_semi_dev_ewm_span63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM semi-dev span=63 (velocity of quarterly-decay downside vol)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd = np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return sd.diff(_TD_WEEK)


def dsd_extdrv2_005_semi_dev_ewm_span10_vs_span63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM semi-dev ratio (span=10 / span=63) — velocity of fast vs slow."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    fast = np.sqrt(sq.ewm(span=10, min_periods=5).mean())
    slow = np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    ratio = _safe_div(fast, slow)
    return ratio.diff(_TD_WEEK)


def dsd_extdrv2_006_var5_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d VaR at 5% (velocity of rolling tail quantile)."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    return var5.diff(_TD_WEEK)


def dsd_extdrv2_007_var5_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d VaR at 5% (monthly change in medium-term tail quantile)."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    return var5.diff(_TD_MON)


def dsd_extdrv2_008_cvar5_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d CVaR at 5% (velocity of expected tail loss)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    cvar = below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return cvar.diff(_TD_WEEK)


def dsd_extdrv2_009_tail_ratio_5pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d tail ratio (velocity of downside-to-upside tail asymmetry)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    q95 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.95)
    ratio = _safe_div(q05.abs(), q95.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def dsd_extdrv2_010_tail_ratio_5pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d tail ratio."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    q95 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.95)
    ratio = _safe_div(q05.abs(), q95.clip(lower=_EPS))
    return ratio.diff(_TD_MON)


def dsd_extdrv2_011_downside_skew_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d downside return skewness (velocity of tail-shape change)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    skew = dn.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()
    return skew.diff(_TD_WEEK)


def dsd_extdrv2_012_downside_skew_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d downside return skewness."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    skew = dn.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    return skew.diff(_TD_MON)


def dsd_extdrv2_013_downside_count_frac_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d down-day fraction (velocity of down-day frequency change)."""
    r = _log_ret(close)
    frac = (r < 0.0).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return frac.diff(_TD_WEEK)


def dsd_extdrv2_014_downside_count_frac_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d down-day fraction."""
    r = _log_ret(close)
    frac = (r < 0.0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return frac.diff(_TD_MON)


def dsd_extdrv2_015_downside_pain_index_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d downside pain index (velocity of within-period drawdown pain)."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    peak = cum.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    pain = _rolling_mean(dd, _TD_MON)
    return pain.diff(_TD_WEEK)


def dsd_extdrv2_016_downside_pain_index_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d downside pain index."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    peak = cum.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    pain = _rolling_mean(dd, _TD_QTR)
    return pain.diff(_TD_MON)


def dsd_extdrv2_017_sortino_mar05pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d Sortino vs MAR=+0.5%/day (velocity of positive-target risk-adj return)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    mu = _rolling_mean(r, _TD_MON)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    sd = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sortino = _safe_div(mu - mar, sd)
    return sortino.diff(_TD_WEEK)


def dsd_extdrv2_018_lpm2_ewm_span21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM LPM2 vs 0 (span=21) — velocity of EWM semi-variance."""
    r = _log_ret(close)
    below_sq = ((0.0 - r).clip(lower=0.0) ** 2)
    lpm = below_sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return lpm.diff(_TD_WEEK)


def dsd_extdrv2_019_semi_dev_21d_pct_rank_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d semi-dev percentile rank within 63d distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    pct = sd21.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return pct.diff(_TD_WEEK)


def dsd_extdrv2_020_semi_dev_21d_zscore_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d semi-dev z-score vs 126-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = _rolling_mean(sd21, _TD_HALF)
    sig = _rolling_std(sd21, _TD_HALF)
    z = _safe_div(sd21 - mu, sig)
    return z.diff(_TD_WEEK)


def dsd_extdrv2_021_var5_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d rolling VaR at 5%."""
    r = _log_ret(close)
    var5 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    return _linslope(var5, _TD_MON)


def dsd_extdrv2_022_cvar5_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d CVaR at 5% (monthly change in expected tail loss)."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    cvar = below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return cvar.diff(_TD_MON)


def dsd_extdrv2_023_downside_kurt_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d downside kurtosis (velocity of fat-tail emergence)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    kurt = dn.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()
    return kurt.diff(_TD_WEEK)


def dsd_extdrv2_024_capitulation_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of capitulation composite (sd21 norm + z-score + pct-rank combo)."""
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
    return composite.diff(_TD_WEEK)


def dsd_extdrv2_025_downside_count_frac_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252d down-day fraction (monthly change in annual bear-day rate)."""
    r = _log_ret(close)
    frac = (r < 0.0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    return frac.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "dsd_extdrv2_001_semi_dev_mar05pct_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_001_semi_dev_mar05pct_21d_5d_diff},
    "dsd_extdrv2_002_semi_dev_mar05pct_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_002_semi_dev_mar05pct_63d_21d_diff},
    "dsd_extdrv2_003_semi_dev_ewm_span10_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_003_semi_dev_ewm_span10_5d_diff},
    "dsd_extdrv2_004_semi_dev_ewm_span63_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_004_semi_dev_ewm_span63_5d_diff},
    "dsd_extdrv2_005_semi_dev_ewm_span10_vs_span63_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_005_semi_dev_ewm_span10_vs_span63_5d_diff},
    "dsd_extdrv2_006_var5_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_006_var5_21d_5d_diff},
    "dsd_extdrv2_007_var5_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_007_var5_63d_21d_diff},
    "dsd_extdrv2_008_cvar5_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_008_cvar5_21d_5d_diff},
    "dsd_extdrv2_009_tail_ratio_5pct_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_009_tail_ratio_5pct_21d_5d_diff},
    "dsd_extdrv2_010_tail_ratio_5pct_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_010_tail_ratio_5pct_63d_21d_diff},
    "dsd_extdrv2_011_downside_skew_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_011_downside_skew_21d_5d_diff},
    "dsd_extdrv2_012_downside_skew_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_012_downside_skew_63d_21d_diff},
    "dsd_extdrv2_013_downside_count_frac_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_013_downside_count_frac_21d_5d_diff},
    "dsd_extdrv2_014_downside_count_frac_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_014_downside_count_frac_63d_21d_diff},
    "dsd_extdrv2_015_downside_pain_index_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_015_downside_pain_index_21d_5d_diff},
    "dsd_extdrv2_016_downside_pain_index_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_016_downside_pain_index_63d_21d_diff},
    "dsd_extdrv2_017_sortino_mar05pct_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_017_sortino_mar05pct_21d_5d_diff},
    "dsd_extdrv2_018_lpm2_ewm_span21_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_018_lpm2_ewm_span21_5d_diff},
    "dsd_extdrv2_019_semi_dev_21d_pct_rank_63d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_019_semi_dev_21d_pct_rank_63d_5d_diff},
    "dsd_extdrv2_020_semi_dev_21d_zscore_126d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_020_semi_dev_21d_zscore_126d_5d_diff},
    "dsd_extdrv2_021_var5_21d_slope_21d": {"inputs": ["close"], "func": dsd_extdrv2_021_var5_21d_slope_21d},
    "dsd_extdrv2_022_cvar5_63d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_022_cvar5_63d_21d_diff},
    "dsd_extdrv2_023_downside_kurt_21d_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_023_downside_kurt_21d_5d_diff},
    "dsd_extdrv2_024_capitulation_composite_5d_diff": {"inputs": ["close"], "func": dsd_extdrv2_024_capitulation_composite_5d_diff},
    "dsd_extdrv2_025_downside_count_frac_252d_21d_diff": {"inputs": ["close"], "func": dsd_extdrv2_025_downside_count_frac_252d_21d_diff},
}
