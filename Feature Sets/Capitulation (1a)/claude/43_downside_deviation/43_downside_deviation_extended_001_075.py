"""
43_downside_deviation — Extended Features 001-075
Domain: downside semi-deviation — additional MAR thresholds, high/low-anchored
        semi-variance, Sortino-style ratios on non-zero targets, downside percentile
        ranks at new windows, downside skewness, tail-ratio measures, EWM variants,
        realised-vol-ratio composites, regime-conditional z-scores and capitulation
        composite scores.  All net-new versus base_001_075 and base_076_150.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Semi-deviation with non-zero MAR thresholds ---

def dsd_ext_001_semi_dev_mar05pct_21d(close: pd.Series) -> pd.Series:
    """21d semi-dev vs MAR=+0.5%/day (shortfall below half-pct daily target)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_002_semi_dev_mar05pct_63d(close: pd.Series) -> pd.Series:
    """63d semi-dev vs MAR=+0.5%/day."""
    r = _log_ret(close)
    mar = np.log(1.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_ext_003_semi_dev_mar_neg05pct_21d(close: pd.Series) -> pd.Series:
    """21d semi-dev vs MAR=-0.5%/day (only catastrophic declines count)."""
    r = _log_ret(close)
    mar = np.log(1 - 0.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_004_semi_dev_mar_neg05pct_63d(close: pd.Series) -> pd.Series:
    """63d semi-dev vs MAR=-0.5%/day."""
    r = _log_ret(close)
    mar = np.log(1 - 0.005)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_ext_005_semi_dev_mar_neg3pct_21d(close: pd.Series) -> pd.Series:
    """21d semi-dev vs MAR=-3%/day (extreme tail only)."""
    r = _log_ret(close)
    mar = np.log(1 - 0.03)
    sq = ((r - mar) ** 2).where(r < mar, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_006_lpm2_mar05pct_63d(close: pd.Series) -> pd.Series:
    """63d LPM2 vs MAR=+0.5%/day (squared shortfall below positive target)."""
    r = _log_ret(close)
    mar = np.log(1.005)
    return _lpm(r, _TD_QTR, 2, mar)


def dsd_ext_007_lpm1_mar05pct_21d(close: pd.Series) -> pd.Series:
    """21d LPM1 vs MAR=+0.5%/day."""
    r = _log_ret(close)
    mar = np.log(1.005)
    return _lpm(r, _TD_MON, 1, mar)


def dsd_ext_008_lpm1_mar_neg3pct_63d(close: pd.Series) -> pd.Series:
    """63d LPM1 vs MAR=-3%/day (deep-tail expected shortfall)."""
    r = _log_ret(close)
    mar = np.log(1 - 0.03)
    return _lpm(r, _TD_QTR, 1, mar)


def dsd_ext_009_sortino_mar05pct_21d(close: pd.Series) -> pd.Series:
    """21d Sortino ratio vs MAR=+0.5%/day: (mean - MAR) / semi-dev-vs-MAR."""
    r = _log_ret(close)
    mar = np.log(1.005)
    mu = _rolling_mean(r, _TD_MON)
    sd = dsd_ext_001_semi_dev_mar05pct_21d(close)
    return _safe_div(mu - mar, sd)


def dsd_ext_010_sortino_mar05pct_63d(close: pd.Series) -> pd.Series:
    """63d Sortino ratio vs MAR=+0.5%/day."""
    r = _log_ret(close)
    mar = np.log(1.005)
    mu = _rolling_mean(r, _TD_QTR)
    sd = dsd_ext_002_semi_dev_mar05pct_63d(close)
    return _safe_div(mu - mar, sd)


# --- Group B (011-020): EWM semi-variance and LPM at new spans ---

def dsd_ext_011_semi_dev_ewm_span10(close: pd.Series) -> pd.Series:
    """EWM semi-deviation with span=10 (faster than span=21)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.ewm(span=10, min_periods=5).mean())


def dsd_ext_012_semi_dev_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM semi-deviation with span=63 (quarterly-speed decay)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_ext_013_semi_dev_ewm_span126(close: pd.Series) -> pd.Series:
    """EWM semi-deviation with span=126 (half-year speed decay)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())


def dsd_ext_014_semi_dev_ewm_span252(close: pd.Series) -> pd.Series:
    """EWM semi-deviation with span=252 (annual-speed decay)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())


def dsd_ext_015_lpm2_ewm_span21(close: pd.Series) -> pd.Series:
    """EWM LPM2 vs 0 with span=21 (exponentially-weighted semi-variance)."""
    r = _log_ret(close)
    below_sq = ((0.0 - r).clip(lower=0.0) ** 2)
    return below_sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_ext_016_lpm2_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM LPM2 vs 0 with span=63."""
    r = _log_ret(close)
    below_sq = ((0.0 - r).clip(lower=0.0) ** 2)
    return below_sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_ext_017_semi_dev_ewm_span10_vs_span63(close: pd.Series) -> pd.Series:
    """Ratio of EWM semi-dev span=10 to span=63 (fast vs slow EWM)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    fast = np.sqrt(sq.ewm(span=10, min_periods=5).mean())
    slow = np.sqrt(sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return _safe_div(fast, slow)


def dsd_ext_018_semi_dev_ewm_span21_vs_span252(close: pd.Series) -> pd.Series:
    """Ratio of EWM semi-dev span=21 to span=252 (short vs long EWM)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    fast = np.sqrt(sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    slow = np.sqrt(sq.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(fast, slow)


def dsd_ext_019_lpm1_ewm_span21(close: pd.Series) -> pd.Series:
    """EWM LPM1 vs 0 with span=21 (exponentially-weighted expected shortfall)."""
    r = _log_ret(close)
    below = (0.0 - r).clip(lower=0.0)
    return below.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_ext_020_lpm1_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM LPM1 vs 0 with span=63."""
    r = _log_ret(close)
    below = (0.0 - r).clip(lower=0.0)
    return below.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


# --- Group C (021-030): Downside percentile ranks at new window combos ---

def dsd_ext_021_semi_dev_21d_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day semi-dev within trailing 63-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return sd21.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def dsd_ext_022_semi_dev_21d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day semi-dev within trailing 126-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return sd21.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def dsd_ext_023_semi_dev_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day semi-dev within trailing 252-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return sd63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dsd_ext_024_semi_dev_63d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day semi-dev within trailing 504-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return sd63.rolling(504, min_periods=252).rank(pct=True)


def dsd_ext_025_semi_dev_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day semi-dev within trailing 504-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return sd252.rolling(504, min_periods=252).rank(pct=True)


def dsd_ext_026_lpm2_vs0_21d_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day LPM2 within trailing 63-day distribution."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 2, 0.0)
    return lpm.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def dsd_ext_027_lpm2_vs0_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day LPM2 within trailing 252-day distribution."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 2, 0.0)
    return lpm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dsd_ext_028_downside_upside_ratio_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day down/up vol ratio within 252-day distribution."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    ratio = _safe_div(dn, up)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dsd_ext_029_semi_dev_21d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day semi-dev."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return sd21.expanding(min_periods=5).rank(pct=True)


def dsd_ext_030_lpm1_vs0_21d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day LPM1 vs 0."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 1, 0.0)
    return lpm.expanding(min_periods=5).rank(pct=True)


# --- Group D (031-040): Z-scores at new window pairs ---

def dsd_ext_031_semi_dev_21d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day semi-dev within trailing 63-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = _rolling_mean(sd21, _TD_QTR)
    sig = _rolling_std(sd21, _TD_QTR)
    return _safe_div(sd21 - mu, sig)


def dsd_ext_032_semi_dev_21d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day semi-dev within trailing 126-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    mu = _rolling_mean(sd21, _TD_HALF)
    sig = _rolling_std(sd21, _TD_HALF)
    return _safe_div(sd21 - mu, sig)


def dsd_ext_033_semi_dev_63d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day semi-dev within trailing 126-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    mu = _rolling_mean(sd63, _TD_HALF)
    sig = _rolling_std(sd63, _TD_HALF)
    return _safe_div(sd63 - mu, sig)


def dsd_ext_034_semi_dev_63d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day semi-dev within trailing 504-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd63 = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    mu = _rolling_mean(sd63, 504)
    sig = _rolling_std(sd63, 504)
    return _safe_div(sd63 - mu, sig)


def dsd_ext_035_lpm2_vs0_21d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day LPM2 vs 0 within trailing 63-day distribution."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 2, 0.0)
    mu = _rolling_mean(lpm, _TD_QTR)
    sig = _rolling_std(lpm, _TD_QTR)
    return _safe_div(lpm - mu, sig)


def dsd_ext_036_lpm1_vs0_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day LPM1 vs 0 within trailing 252-day distribution."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_QTR, 1, 0.0)
    mu = _rolling_mean(lpm, _TD_YEAR)
    sig = _rolling_std(lpm, _TD_YEAR)
    return _safe_div(lpm - mu, sig)


def dsd_ext_037_downside_vol_share_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day downside vol share within trailing 252-day distribution."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    share = _safe_div(dn, dn + up)
    mu = _rolling_mean(share, _TD_YEAR)
    sig = _rolling_std(share, _TD_YEAR)
    return _safe_div(share - mu, sig)


def dsd_ext_038_sortino_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day Sortino ratio within trailing 252-day distribution."""
    r = _log_ret(close)
    mu_r = _rolling_mean(r, _TD_MON)
    sd = _semi_dev_w(r, _TD_MON)
    sortino = _safe_div(mu_r, sd)
    mu = _rolling_mean(sortino, _TD_YEAR)
    sig = _rolling_std(sortino, _TD_YEAR)
    return _safe_div(sortino - mu, sig)


def dsd_ext_039_semi_dev_21d_vs_252d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (21d semi-dev / 252d semi-dev) ratio within 252-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    sd252 = np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    ratio = _safe_div(sd21, sd252)
    mu = _rolling_mean(ratio, _TD_YEAR)
    sig = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - mu, sig)


def dsd_ext_040_lpm2_expanding_zscore_21d(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of 21-day LPM2 vs 0."""
    r = _log_ret(close)
    lpm = _lpm(r, _TD_MON, 2, 0.0)
    mu = lpm.expanding(min_periods=5).mean()
    sig = lpm.expanding(min_periods=5).std()
    return _safe_div(lpm - mu, sig)


# --- Group E (041-050): Downside skewness and higher moments ---

def dsd_ext_041_downside_skew_21d(close: pd.Series) -> pd.Series:
    """21-day skewness of negative log-returns only (downside tail shape)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def dsd_ext_042_downside_skew_63d(close: pd.Series) -> pd.Series:
    """63-day skewness of negative log-returns only."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def dsd_ext_043_downside_skew_252d(close: pd.Series) -> pd.Series:
    """252-day skewness of negative log-returns only."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def dsd_ext_044_downside_kurt_21d(close: pd.Series) -> pd.Series:
    """21-day excess kurtosis of negative log-returns (fat-tail measure)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()


def dsd_ext_045_downside_kurt_63d(close: pd.Series) -> pd.Series:
    """63-day excess kurtosis of negative log-returns."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def dsd_ext_046_downside_mean_21d(close: pd.Series) -> pd.Series:
    """21-day mean of negative log-returns (average loss day magnitude)."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_ext_047_downside_mean_63d(close: pd.Series) -> pd.Series:
    """63-day mean of negative log-returns."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    return dn.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_ext_048_downside_count_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of down days over 21-day window (proportion < 0 log-return)."""
    r = _log_ret(close)
    return (r < 0.0).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_ext_049_downside_count_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of down days over 63-day window."""
    r = _log_ret(close)
    return (r < 0.0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_ext_050_downside_count_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of down days over 252-day window."""
    r = _log_ret(close)
    return (r < 0.0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


# --- Group F (051-060): Tail ratio and CVaR-style measures ---

def dsd_ext_051_tail_ratio_5pct_21d(close: pd.Series) -> pd.Series:
    """21d tail ratio: abs(5th percentile return) / 95th percentile return."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    q95 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.95)
    return _safe_div(q05.abs(), q95.clip(lower=_EPS))


def dsd_ext_052_tail_ratio_5pct_63d(close: pd.Series) -> pd.Series:
    """63d tail ratio: abs(5th percentile) / 95th percentile."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    q95 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.95)
    return _safe_div(q05.abs(), q95.clip(lower=_EPS))


def dsd_ext_053_tail_ratio_5pct_252d(close: pd.Series) -> pd.Series:
    """252d tail ratio: abs(5th percentile) / 95th percentile."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    q95 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    return _safe_div(q05.abs(), q95.clip(lower=_EPS))


def dsd_ext_054_cvar5_21d(close: pd.Series) -> pd.Series:
    """21d conditional VaR at 5%: mean of returns below 5th percentile."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_ext_055_cvar5_63d(close: pd.Series) -> pd.Series:
    """63d conditional VaR at 5%: mean of returns in bottom 5% of 63d distribution."""
    r = _log_ret(close)
    q05 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    below = r.where(r <= q05, np.nan)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_ext_056_var5_21d(close: pd.Series) -> pd.Series:
    """21d VaR at 5% (5th percentile of rolling 21-day log-returns, negative sign)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)


def dsd_ext_057_var5_63d(close: pd.Series) -> pd.Series:
    """63d VaR at 5% (5th percentile of rolling 63-day log-returns)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)


def dsd_ext_058_var1_21d(close: pd.Series) -> pd.Series:
    """21d VaR at 1% (1st percentile of rolling 21-day log-returns)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.01)


def dsd_ext_059_var10_63d(close: pd.Series) -> pd.Series:
    """63d VaR at 10% (10th percentile of rolling 63-day log-returns)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)


def dsd_ext_060_downside_iqr_21d(close: pd.Series) -> pd.Series:
    """21d downside inter-quartile range: Q25 - Q05 of negative returns only."""
    r = _log_ret(close)
    dn = r.where(r < 0.0, np.nan)
    q25 = dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    q05 = dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    return (q25 - q05).abs()


# --- Group G (061-070): High/Low anchored downside measures at new windows ---

def dsd_ext_061_low_return_semi_dev_5d(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day semi-deviation of low-to-prior-close log-returns."""
    r = np.log((low / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_WEEK, min_periods=1).mean())


def dsd_ext_062_low_return_semi_dev_126d(close: pd.Series, low: pd.Series) -> pd.Series:
    """126-day semi-deviation of low-to-prior-close log-returns."""
    r = np.log((low / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())


def dsd_ext_063_open_to_close_semi_dev_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day semi-deviation of log(close/open) returns on down days."""
    r = np.log((close / open.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_064_open_to_close_semi_dev_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day semi-deviation of log(close/open) on down days."""
    r = np.log((close / open.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_ext_065_high_to_close_semi_dev_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """21-day semi-deviation of log(close/high): close below intraday high (slippage-risk)."""
    r = np.log((close / high.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_066_high_to_close_semi_dev_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """63-day semi-deviation of log(close/high)."""
    r = np.log((close / high.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_ext_067_gap_down_semi_dev_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day semi-deviation of gap-down opens (log(open/prior_close) when negative)."""
    r = np.log((open / close.shift(1)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_ext_068_gap_down_lpm1_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day LPM1 vs 0 of gap-down opens (expected gap shortfall)."""
    r = np.log((open / close.shift(1)).clip(lower=_EPS))
    return _lpm(r, _TD_QTR, 1, 0.0)


def dsd_ext_069_close_to_low_semi_dev_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """252-day semi-deviation of log(low/close) (annual intraday downside)."""
    r = np.log((low / close.clip(lower=_EPS)).clip(lower=_EPS))
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())


def dsd_ext_070_intraday_down_range_vs_close_semi_dev_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d semi-dev of (high - close) / close (upper-wick miss, daily disappointment)."""
    r = (high - close) / close.clip(lower=_EPS)
    sq = (r ** 2)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


# --- Group H (071-075): Multi-input downside composites and capitulation signals ---

def dsd_ext_071_vol_adjusted_semi_dev_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d semi-dev * log1p(normalized volume) composite (pain weighted by activity)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.replace(0, np.nan)).fillna(1.0)
    return sd21 * np.log1p(vol_norm)


def dsd_ext_072_downside_pain_index_21d(close: pd.Series) -> pd.Series:
    """21d downside pain index: sum of (cumulative return drawdown from period high)."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    peak = cum.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    return _rolling_mean(dd, _TD_MON)


def dsd_ext_073_downside_pain_index_63d(close: pd.Series) -> pd.Series:
    """63d downside pain index: mean absolute drawdown within rolling 63d window."""
    r = _log_ret(close).fillna(0.0)
    cum = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    peak = cum.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
    dd = (cum - peak).clip(upper=0.0).abs()
    return _rolling_mean(dd, _TD_QTR)


def dsd_ext_074_capitulation_semi_dev_composite(close: pd.Series) -> pd.Series:
    """Capitulation composite: weighted sum of normalized semi-dev, z-score, pct-rank.
    Score = (sd21/avg252) + z21_252.clip(-3,3)/3 + (1 - pct_rank252).
    Higher = more extreme downside dispersion."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sd21 = np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    avg252 = _rolling_mean(sd21, _TD_YEAR)
    norm = _safe_div(sd21, avg252.replace(0, np.nan))
    mu = _rolling_mean(sd21, _TD_YEAR)
    sig = _rolling_std(sd21, _TD_YEAR)
    z = _safe_div(sd21 - mu, sig).clip(-3.0, 3.0) / 3.0
    pct_rank = sd21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    return norm.fillna(1.0) + z.fillna(0.0) + (1.0 - pct_rank)


def dsd_ext_075_downside_upside_diff_norm_252d(close: pd.Series) -> pd.Series:
    """(Downside semi-dev - upside semi-dev) normalized by 252d avg, over 21d window.
    Positive = downside currently dominates historical average asymmetry."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    diff = dn - up
    avg = _rolling_mean(diff, _TD_YEAR)
    return _safe_div(diff, avg.abs().replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_EXTENDED_REGISTRY_001_075 = {
    "dsd_ext_001_semi_dev_mar05pct_21d": {"inputs": ["close"], "func": dsd_ext_001_semi_dev_mar05pct_21d},
    "dsd_ext_002_semi_dev_mar05pct_63d": {"inputs": ["close"], "func": dsd_ext_002_semi_dev_mar05pct_63d},
    "dsd_ext_003_semi_dev_mar_neg05pct_21d": {"inputs": ["close"], "func": dsd_ext_003_semi_dev_mar_neg05pct_21d},
    "dsd_ext_004_semi_dev_mar_neg05pct_63d": {"inputs": ["close"], "func": dsd_ext_004_semi_dev_mar_neg05pct_63d},
    "dsd_ext_005_semi_dev_mar_neg3pct_21d": {"inputs": ["close"], "func": dsd_ext_005_semi_dev_mar_neg3pct_21d},
    "dsd_ext_006_lpm2_mar05pct_63d": {"inputs": ["close"], "func": dsd_ext_006_lpm2_mar05pct_63d},
    "dsd_ext_007_lpm1_mar05pct_21d": {"inputs": ["close"], "func": dsd_ext_007_lpm1_mar05pct_21d},
    "dsd_ext_008_lpm1_mar_neg3pct_63d": {"inputs": ["close"], "func": dsd_ext_008_lpm1_mar_neg3pct_63d},
    "dsd_ext_009_sortino_mar05pct_21d": {"inputs": ["close"], "func": dsd_ext_009_sortino_mar05pct_21d},
    "dsd_ext_010_sortino_mar05pct_63d": {"inputs": ["close"], "func": dsd_ext_010_sortino_mar05pct_63d},
    "dsd_ext_011_semi_dev_ewm_span10": {"inputs": ["close"], "func": dsd_ext_011_semi_dev_ewm_span10},
    "dsd_ext_012_semi_dev_ewm_span63": {"inputs": ["close"], "func": dsd_ext_012_semi_dev_ewm_span63},
    "dsd_ext_013_semi_dev_ewm_span126": {"inputs": ["close"], "func": dsd_ext_013_semi_dev_ewm_span126},
    "dsd_ext_014_semi_dev_ewm_span252": {"inputs": ["close"], "func": dsd_ext_014_semi_dev_ewm_span252},
    "dsd_ext_015_lpm2_ewm_span21": {"inputs": ["close"], "func": dsd_ext_015_lpm2_ewm_span21},
    "dsd_ext_016_lpm2_ewm_span63": {"inputs": ["close"], "func": dsd_ext_016_lpm2_ewm_span63},
    "dsd_ext_017_semi_dev_ewm_span10_vs_span63": {"inputs": ["close"], "func": dsd_ext_017_semi_dev_ewm_span10_vs_span63},
    "dsd_ext_018_semi_dev_ewm_span21_vs_span252": {"inputs": ["close"], "func": dsd_ext_018_semi_dev_ewm_span21_vs_span252},
    "dsd_ext_019_lpm1_ewm_span21": {"inputs": ["close"], "func": dsd_ext_019_lpm1_ewm_span21},
    "dsd_ext_020_lpm1_ewm_span63": {"inputs": ["close"], "func": dsd_ext_020_lpm1_ewm_span63},
    "dsd_ext_021_semi_dev_21d_pct_rank_63d": {"inputs": ["close"], "func": dsd_ext_021_semi_dev_21d_pct_rank_63d},
    "dsd_ext_022_semi_dev_21d_pct_rank_126d": {"inputs": ["close"], "func": dsd_ext_022_semi_dev_21d_pct_rank_126d},
    "dsd_ext_023_semi_dev_63d_pct_rank_252d": {"inputs": ["close"], "func": dsd_ext_023_semi_dev_63d_pct_rank_252d},
    "dsd_ext_024_semi_dev_63d_pct_rank_504d": {"inputs": ["close"], "func": dsd_ext_024_semi_dev_63d_pct_rank_504d},
    "dsd_ext_025_semi_dev_252d_pct_rank_504d": {"inputs": ["close"], "func": dsd_ext_025_semi_dev_252d_pct_rank_504d},
    "dsd_ext_026_lpm2_vs0_21d_pct_rank_63d": {"inputs": ["close"], "func": dsd_ext_026_lpm2_vs0_21d_pct_rank_63d},
    "dsd_ext_027_lpm2_vs0_63d_pct_rank_252d": {"inputs": ["close"], "func": dsd_ext_027_lpm2_vs0_63d_pct_rank_252d},
    "dsd_ext_028_downside_upside_ratio_21d_pct_rank_252d": {"inputs": ["close"], "func": dsd_ext_028_downside_upside_ratio_21d_pct_rank_252d},
    "dsd_ext_029_semi_dev_21d_expanding_pct_rank": {"inputs": ["close"], "func": dsd_ext_029_semi_dev_21d_expanding_pct_rank},
    "dsd_ext_030_lpm1_vs0_21d_expanding_pct_rank": {"inputs": ["close"], "func": dsd_ext_030_lpm1_vs0_21d_expanding_pct_rank},
    "dsd_ext_031_semi_dev_21d_zscore_63d": {"inputs": ["close"], "func": dsd_ext_031_semi_dev_21d_zscore_63d},
    "dsd_ext_032_semi_dev_21d_zscore_126d": {"inputs": ["close"], "func": dsd_ext_032_semi_dev_21d_zscore_126d},
    "dsd_ext_033_semi_dev_63d_zscore_126d": {"inputs": ["close"], "func": dsd_ext_033_semi_dev_63d_zscore_126d},
    "dsd_ext_034_semi_dev_63d_zscore_504d": {"inputs": ["close"], "func": dsd_ext_034_semi_dev_63d_zscore_504d},
    "dsd_ext_035_lpm2_vs0_21d_zscore_63d": {"inputs": ["close"], "func": dsd_ext_035_lpm2_vs0_21d_zscore_63d},
    "dsd_ext_036_lpm1_vs0_63d_zscore_252d": {"inputs": ["close"], "func": dsd_ext_036_lpm1_vs0_63d_zscore_252d},
    "dsd_ext_037_downside_vol_share_63d_zscore_252d": {"inputs": ["close"], "func": dsd_ext_037_downside_vol_share_63d_zscore_252d},
    "dsd_ext_038_sortino_21d_zscore_252d": {"inputs": ["close"], "func": dsd_ext_038_sortino_21d_zscore_252d},
    "dsd_ext_039_semi_dev_21d_vs_252d_zscore_252d": {"inputs": ["close"], "func": dsd_ext_039_semi_dev_21d_vs_252d_zscore_252d},
    "dsd_ext_040_lpm2_expanding_zscore_21d": {"inputs": ["close"], "func": dsd_ext_040_lpm2_expanding_zscore_21d},
    "dsd_ext_041_downside_skew_21d": {"inputs": ["close"], "func": dsd_ext_041_downside_skew_21d},
    "dsd_ext_042_downside_skew_63d": {"inputs": ["close"], "func": dsd_ext_042_downside_skew_63d},
    "dsd_ext_043_downside_skew_252d": {"inputs": ["close"], "func": dsd_ext_043_downside_skew_252d},
    "dsd_ext_044_downside_kurt_21d": {"inputs": ["close"], "func": dsd_ext_044_downside_kurt_21d},
    "dsd_ext_045_downside_kurt_63d": {"inputs": ["close"], "func": dsd_ext_045_downside_kurt_63d},
    "dsd_ext_046_downside_mean_21d": {"inputs": ["close"], "func": dsd_ext_046_downside_mean_21d},
    "dsd_ext_047_downside_mean_63d": {"inputs": ["close"], "func": dsd_ext_047_downside_mean_63d},
    "dsd_ext_048_downside_count_fraction_21d": {"inputs": ["close"], "func": dsd_ext_048_downside_count_fraction_21d},
    "dsd_ext_049_downside_count_fraction_63d": {"inputs": ["close"], "func": dsd_ext_049_downside_count_fraction_63d},
    "dsd_ext_050_downside_count_fraction_252d": {"inputs": ["close"], "func": dsd_ext_050_downside_count_fraction_252d},
    "dsd_ext_051_tail_ratio_5pct_21d": {"inputs": ["close"], "func": dsd_ext_051_tail_ratio_5pct_21d},
    "dsd_ext_052_tail_ratio_5pct_63d": {"inputs": ["close"], "func": dsd_ext_052_tail_ratio_5pct_63d},
    "dsd_ext_053_tail_ratio_5pct_252d": {"inputs": ["close"], "func": dsd_ext_053_tail_ratio_5pct_252d},
    "dsd_ext_054_cvar5_21d": {"inputs": ["close"], "func": dsd_ext_054_cvar5_21d},
    "dsd_ext_055_cvar5_63d": {"inputs": ["close"], "func": dsd_ext_055_cvar5_63d},
    "dsd_ext_056_var5_21d": {"inputs": ["close"], "func": dsd_ext_056_var5_21d},
    "dsd_ext_057_var5_63d": {"inputs": ["close"], "func": dsd_ext_057_var5_63d},
    "dsd_ext_058_var1_21d": {"inputs": ["close"], "func": dsd_ext_058_var1_21d},
    "dsd_ext_059_var10_63d": {"inputs": ["close"], "func": dsd_ext_059_var10_63d},
    "dsd_ext_060_downside_iqr_21d": {"inputs": ["close"], "func": dsd_ext_060_downside_iqr_21d},
    "dsd_ext_061_low_return_semi_dev_5d": {"inputs": ["close", "low"], "func": dsd_ext_061_low_return_semi_dev_5d},
    "dsd_ext_062_low_return_semi_dev_126d": {"inputs": ["close", "low"], "func": dsd_ext_062_low_return_semi_dev_126d},
    "dsd_ext_063_open_to_close_semi_dev_21d": {"inputs": ["close", "open"], "func": dsd_ext_063_open_to_close_semi_dev_21d},
    "dsd_ext_064_open_to_close_semi_dev_63d": {"inputs": ["close", "open"], "func": dsd_ext_064_open_to_close_semi_dev_63d},
    "dsd_ext_065_high_to_close_semi_dev_21d": {"inputs": ["close", "high"], "func": dsd_ext_065_high_to_close_semi_dev_21d},
    "dsd_ext_066_high_to_close_semi_dev_63d": {"inputs": ["close", "high"], "func": dsd_ext_066_high_to_close_semi_dev_63d},
    "dsd_ext_067_gap_down_semi_dev_21d": {"inputs": ["close", "open"], "func": dsd_ext_067_gap_down_semi_dev_21d},
    "dsd_ext_068_gap_down_lpm1_63d": {"inputs": ["close", "open"], "func": dsd_ext_068_gap_down_lpm1_63d},
    "dsd_ext_069_close_to_low_semi_dev_252d": {"inputs": ["close", "low"], "func": dsd_ext_069_close_to_low_semi_dev_252d},
    "dsd_ext_070_intraday_down_range_vs_close_semi_dev_21d": {"inputs": ["close", "high", "low"], "func": dsd_ext_070_intraday_down_range_vs_close_semi_dev_21d},
    "dsd_ext_071_vol_adjusted_semi_dev_21d": {"inputs": ["close", "volume"], "func": dsd_ext_071_vol_adjusted_semi_dev_21d},
    "dsd_ext_072_downside_pain_index_21d": {"inputs": ["close"], "func": dsd_ext_072_downside_pain_index_21d},
    "dsd_ext_073_downside_pain_index_63d": {"inputs": ["close"], "func": dsd_ext_073_downside_pain_index_63d},
    "dsd_ext_074_capitulation_semi_dev_composite": {"inputs": ["close"], "func": dsd_ext_074_capitulation_semi_dev_composite},
    "dsd_ext_075_downside_upside_diff_norm_252d": {"inputs": ["close"], "func": dsd_ext_075_downside_upside_diff_norm_252d},
}
