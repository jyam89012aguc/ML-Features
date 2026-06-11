"""
43_downside_deviation — Base Features 001-075
Domain: semi-variance and downside-only dispersion magnitude
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


def _pct_ret(s: pd.Series) -> pd.Series:
    """Daily simple-return series."""
    return s.pct_change(1)


def _downside_ret(close: pd.Series, threshold: float = 0.0) -> pd.Series:
    """Returns on days below threshold; NaN on other days (log-returns)."""
    r = _log_ret(close)
    return r.where(r < threshold, np.nan)


def _downside_sq(close: pd.Series, threshold: float = 0.0) -> pd.Series:
    """Squared log-returns on days below threshold; 0 on other days."""
    r = _log_ret(close)
    return (r ** 2).where(r < threshold, 0.0)


def _semi_std(s: pd.Series, w: int, threshold: float = 0.0) -> pd.Series:
    """Rolling semi-deviation: sqrt of mean squared below-threshold returns."""
    r = s if s.name != "close" else s
    below = (s ** 2).where(s < threshold, 0.0)
    mean_sq = below.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(mean_sq.clip(lower=0.0))


def _lpm(r: pd.Series, w: int, order: int, threshold: float = 0.0) -> pd.Series:
    """Rolling lower partial moment of given order."""
    below = ((threshold - r).clip(lower=0.0) ** order)
    return below.rolling(w, min_periods=max(1, w // 2)).mean()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Downside deviation (semi-deviation) at core windows ---

def dsd_001_semi_dev_21d(close: pd.Series) -> pd.Series:
    """21-day downside deviation: sqrt(mean of squared negative log-returns)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def dsd_002_semi_dev_63d(close: pd.Series) -> pd.Series:
    """63-day downside deviation (semi-deviation of log-returns below zero)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def dsd_003_semi_dev_126d(close: pd.Series) -> pd.Series:
    """126-day downside deviation (half-year semi-deviation of log-returns)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())


def dsd_004_semi_dev_252d(close: pd.Series) -> pd.Series:
    """252-day downside deviation (annual semi-deviation of log-returns)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())


def dsd_005_semi_dev_5d(close: pd.Series) -> pd.Series:
    """5-day (weekly) downside deviation of log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(_TD_WEEK, min_periods=1).mean())


def dsd_006_semi_dev_10d(close: pd.Series) -> pd.Series:
    """10-day downside deviation of log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.rolling(10, min_periods=5).mean())


def dsd_007_semi_dev_annualized_21d(close: pd.Series) -> pd.Series:
    """21-day semi-deviation annualized by sqrt(252)."""
    return dsd_001_semi_dev_21d(close) * np.sqrt(_TD_YEAR)


def dsd_008_semi_dev_annualized_63d(close: pd.Series) -> pd.Series:
    """63-day semi-deviation annualized by sqrt(252)."""
    return dsd_002_semi_dev_63d(close) * np.sqrt(_TD_YEAR)


def dsd_009_semi_dev_annualized_252d(close: pd.Series) -> pd.Series:
    """252-day semi-deviation annualized by sqrt(252)."""
    return dsd_004_semi_dev_252d(close) * np.sqrt(_TD_YEAR)


def dsd_010_semi_dev_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM-based downside deviation with span=21 (exponentially weighted semi-dev)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return np.sqrt(sq.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


# --- Group B (011-020): Semi-variance (squared semi-deviation) ---

def dsd_011_semi_variance_21d(close: pd.Series) -> pd.Series:
    """21-day semi-variance: mean squared negative log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_012_semi_variance_63d(close: pd.Series) -> pd.Series:
    """63-day semi-variance of log-returns below zero."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_013_semi_variance_252d(close: pd.Series) -> pd.Series:
    """252-day semi-variance of log-returns."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def dsd_014_semi_variance_126d(close: pd.Series) -> pd.Series:
    """126-day semi-variance of log-returns below zero."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean()


def dsd_015_semi_variance_5d(close: pd.Series) -> pd.Series:
    """5-day semi-variance of log-returns (short-term downside intensity)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.rolling(_TD_WEEK, min_periods=1).mean()


def dsd_016_semi_variance_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM semi-variance with span=63 (exponentially weighted quarterly)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    return sq.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_017_semi_variance_norm_by_total_var_21d(close: pd.Series) -> pd.Series:
    """21-day semi-variance as fraction of total variance (downside share of variance)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    tv = (r ** 2).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return _safe_div(sv, tv)


def dsd_018_semi_variance_norm_by_total_var_63d(close: pd.Series) -> pd.Series:
    """63-day semi-variance as fraction of total variance."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv = sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    tv = (r ** 2).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(sv, tv)


def dsd_019_semi_variance_norm_by_total_var_252d(close: pd.Series) -> pd.Series:
    """252-day semi-variance as fraction of total variance."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv = sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    tv = (r ** 2).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    return _safe_div(sv, tv)


def dsd_020_semi_variance_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day semi-variance within trailing 252-day distribution."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    sv21 = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return sv21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (021-030): Downside vs total volatility ratio ---

def dsd_021_down_to_total_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day downside deviation to total std-dev (semi-dev / std)."""
    sd = dsd_001_semi_dev_21d(close)
    total = _rolling_std(_log_ret(close), _TD_MON)
    return _safe_div(sd, total)


def dsd_022_down_to_total_vol_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day downside deviation to total std-dev."""
    sd = dsd_002_semi_dev_63d(close)
    total = _rolling_std(_log_ret(close), _TD_QTR)
    return _safe_div(sd, total)


def dsd_023_down_to_total_vol_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252-day downside deviation to total std-dev."""
    sd = dsd_004_semi_dev_252d(close)
    total = _rolling_std(_log_ret(close), _TD_YEAR)
    return _safe_div(sd, total)


def dsd_024_downside_upside_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 21 days (asymmetry of dispersion)."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn_std = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up_std = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return _safe_div(dn_std, up_std)


def dsd_025_downside_upside_vol_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 63 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn_std = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up_std = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return _safe_div(dn_std, up_std)


def dsd_026_downside_upside_vol_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of downside vol to upside vol over 252 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn_std = np.sqrt(dn_sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    up_std = np.sqrt(up_sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(dn_std, up_std)


def dsd_027_downside_vol_share_21d(close: pd.Series) -> pd.Series:
    """Downside vol as share of (downside + upside) vol over 21 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return _safe_div(dn, dn + up)


def dsd_028_downside_vol_share_63d(close: pd.Series) -> pd.Series:
    """Downside vol as share of (downside + upside) vol over 63 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return _safe_div(dn, dn + up)


def dsd_029_downside_vol_share_252d(close: pd.Series) -> pd.Series:
    """Downside vol as share of (downside + upside) vol over 252 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean())
    return _safe_div(dn, dn + up)


def dsd_030_semi_dev_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day semi-deviation within trailing 252-day distribution."""
    sd = dsd_001_semi_dev_21d(close)
    return sd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (031-040): Target-shortfall dispersion vs zero ---

def dsd_031_lpm1_vs0_21d(close: pd.Series) -> pd.Series:
    """21-day lower partial moment order-1 vs target=0 (expected shortfall below 0)."""
    r = _log_ret(close)
    return _lpm(r, _TD_MON, 1, 0.0)


def dsd_032_lpm1_vs0_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-1 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_QTR, 1, 0.0)


def dsd_033_lpm1_vs0_252d(close: pd.Series) -> pd.Series:
    """252-day LPM order-1 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_YEAR, 1, 0.0)


def dsd_034_lpm2_vs0_21d(close: pd.Series) -> pd.Series:
    """21-day lower partial moment order-2 vs target=0 (semi-variance variant)."""
    r = _log_ret(close)
    return _lpm(r, _TD_MON, 2, 0.0)


def dsd_035_lpm2_vs0_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-2 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_QTR, 2, 0.0)


def dsd_036_lpm2_vs0_252d(close: pd.Series) -> pd.Series:
    """252-day LPM order-2 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_YEAR, 2, 0.0)


def dsd_037_lpm3_vs0_21d(close: pd.Series) -> pd.Series:
    """21-day LPM order-3 vs target=0 (emphasises large downside events)."""
    r = _log_ret(close)
    return _lpm(r, _TD_MON, 3, 0.0)


def dsd_038_lpm3_vs0_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-3 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_QTR, 3, 0.0)


def dsd_039_lpm3_vs0_252d(close: pd.Series) -> pd.Series:
    """252-day LPM order-3 vs target=0."""
    r = _log_ret(close)
    return _lpm(r, _TD_YEAR, 3, 0.0)


def dsd_040_lpm1_vs0_5d(close: pd.Series) -> pd.Series:
    """5-day LPM order-1 vs target=0 (very short-term downside shortfall)."""
    r = _log_ret(close)
    return _lpm(r, _TD_WEEK, 1, 0.0)


# --- Group E (041-050): Target-shortfall dispersion vs rolling mean ---

def dsd_041_lpm1_vs_mean_21d(close: pd.Series) -> pd.Series:
    """21-day LPM order-1 vs rolling mean return (mean-relative shortfall)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    below = (mu - r).clip(lower=0.0)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_042_lpm1_vs_mean_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-1 vs rolling 63-day mean return."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    below = (mu - r).clip(lower=0.0)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_043_lpm1_vs_mean_252d(close: pd.Series) -> pd.Series:
    """252-day LPM order-1 vs rolling 252-day mean return."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_YEAR)
    below = (mu - r).clip(lower=0.0)
    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def dsd_044_lpm2_vs_mean_21d(close: pd.Series) -> pd.Series:
    """21-day LPM order-2 vs rolling mean (below-mean squared deviation)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    below = ((mu - r).clip(lower=0.0) ** 2)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_045_lpm2_vs_mean_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-2 vs rolling mean."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    below = ((mu - r).clip(lower=0.0) ** 2)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_046_lpm2_vs_mean_252d(close: pd.Series) -> pd.Series:
    """252-day LPM order-2 vs rolling mean (annual below-mean semi-variance)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_YEAR)
    below = ((mu - r).clip(lower=0.0) ** 2)
    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def dsd_047_lpm3_vs_mean_21d(close: pd.Series) -> pd.Series:
    """21-day LPM order-3 vs rolling mean (cubic below-mean shortfall)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    below = ((mu - r).clip(lower=0.0) ** 3)
    return below.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dsd_048_lpm3_vs_mean_63d(close: pd.Series) -> pd.Series:
    """63-day LPM order-3 vs rolling mean."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    below = ((mu - r).clip(lower=0.0) ** 3)
    return below.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dsd_049_lpm2_vs_mean_21d_sqrt(close: pd.Series) -> pd.Series:
    """Square root of 21-day LPM2 vs mean (below-mean semi-deviation)."""
    return np.sqrt(dsd_044_lpm2_vs_mean_21d(close).clip(lower=0.0))


def dsd_050_lpm2_vs_mean_63d_sqrt(close: pd.Series) -> pd.Series:
    """Square root of 63-day LPM2 vs mean (below-mean semi-deviation)."""
    return np.sqrt(dsd_045_lpm2_vs_mean_63d(close).clip(lower=0.0))


# --- Group F (051-060): Sortino-style downside risk ratios ---

def dsd_051_sortino_ratio_21d(close: pd.Series) -> pd.Series:
    """Sortino ratio over 21 days: mean return / downside-deviation (vs 0)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    sd = dsd_001_semi_dev_21d(close)
    return _safe_div(mu, sd)


def dsd_052_sortino_ratio_63d(close: pd.Series) -> pd.Series:
    """Sortino ratio over 63 days: mean return / 63-day semi-deviation."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    sd = dsd_002_semi_dev_63d(close)
    return _safe_div(mu, sd)


def dsd_053_sortino_ratio_252d(close: pd.Series) -> pd.Series:
    """Sortino ratio over 252 days: mean return / 252-day semi-deviation."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_YEAR)
    sd = dsd_004_semi_dev_252d(close)
    return _safe_div(mu, sd)


def dsd_054_sortino_vs_sharpe_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of Sortino to Sharpe over 63 days (< 1 = downside-heavy)."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    total = _rolling_std(r, _TD_QTR)
    sd = dsd_002_semi_dev_63d(close)
    sharpe = _safe_div(mu, total)
    sortino = _safe_div(mu, sd)
    return _safe_div(sortino, sharpe)


def dsd_055_sortino_vs_sharpe_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of Sortino to Sharpe over 252 days."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_YEAR)
    total = _rolling_std(r, _TD_YEAR)
    sd = dsd_004_semi_dev_252d(close)
    sharpe = _safe_div(mu, total)
    sortino = _safe_div(mu, sd)
    return _safe_div(sortino, sharpe)


def dsd_056_downside_risk_annualized_21d(close: pd.Series) -> pd.Series:
    """21-day semi-dev annualized * sqrt(252) (Sortino-style downside risk)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    daily_sv = sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return np.sqrt(daily_sv * _TD_YEAR)


def dsd_057_downside_risk_annualized_63d(close: pd.Series) -> pd.Series:
    """63-day semi-dev annualized * sqrt(252)."""
    r = _log_ret(close)
    sq = (r ** 2).where(r < 0.0, 0.0)
    daily_sv = sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return np.sqrt(daily_sv * _TD_YEAR)


def dsd_058_lpm1_sortino_21d(close: pd.Series) -> pd.Series:
    """Sortino using LPM1 as denominator over 21 days."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_MON)
    lpm1 = _lpm(r, _TD_MON, 1, 0.0)
    return _safe_div(mu, lpm1)


def dsd_059_lpm1_sortino_63d(close: pd.Series) -> pd.Series:
    """Sortino using LPM1 as denominator over 63 days."""
    r = _log_ret(close)
    mu = _rolling_mean(r, _TD_QTR)
    lpm1 = _lpm(r, _TD_QTR, 1, 0.0)
    return _safe_div(mu, lpm1)


def dsd_060_downside_risk_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day annualized downside risk within trailing 252 days."""
    dr = dsd_056_downside_risk_annualized_21d(close)
    return dr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (061-075): Z-scores and regime signals for downside dispersion ---

def dsd_061_semi_dev_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day semi-deviation within trailing 252-day distribution."""
    sd = dsd_001_semi_dev_21d(close)
    mu = _rolling_mean(sd, _TD_YEAR)
    sig = _rolling_std(sd, _TD_YEAR)
    return _safe_div(sd - mu, sig)


def dsd_062_semi_dev_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day semi-deviation within trailing 252-day distribution."""
    sd = dsd_002_semi_dev_63d(close)
    mu = _rolling_mean(sd, _TD_YEAR)
    sig = _rolling_std(sd, _TD_YEAR)
    return _safe_div(sd - mu, sig)


def dsd_063_semi_dev_252d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day semi-deviation (all-history extremity)."""
    sd = dsd_004_semi_dev_252d(close)
    mu = sd.expanding(min_periods=5).mean()
    sig = sd.expanding(min_periods=5).std()
    return _safe_div(sd - mu, sig)


def dsd_064_lpm2_vs0_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day LPM2 within 252-day distribution."""
    lpm = dsd_034_lpm2_vs0_21d(close)
    mu = _rolling_mean(lpm, _TD_YEAR)
    sig = _rolling_std(lpm, _TD_YEAR)
    return _safe_div(lpm - mu, sig)


def dsd_065_downside_upside_vol_ratio_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day down/up vol ratio within trailing 252-day history."""
    ratio = dsd_024_downside_upside_vol_ratio_21d(close)
    mu = _rolling_mean(ratio, _TD_YEAR)
    sig = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - mu, sig)


def dsd_066_semi_dev_21d_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-history maximum of 21-day semi-deviation."""
    sd = dsd_001_semi_dev_21d(close)
    return sd.expanding(min_periods=1).max()


def dsd_067_semi_dev_21d_vs_expanding_max(close: pd.Series) -> pd.Series:
    """21-day semi-dev as fraction of its all-history maximum (extremity measure)."""
    sd = dsd_001_semi_dev_21d(close)
    exp_max = sd.expanding(min_periods=1).max()
    return _safe_div(sd, exp_max)


def dsd_068_semi_dev_21d_gt2x_252d_avg_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day semi-deviation > 2x its 252-day average (extreme downside vol)."""
    sd = dsd_001_semi_dev_21d(close)
    avg = _rolling_mean(sd, _TD_YEAR)
    return (sd > 2.0 * avg).astype(float)


def dsd_069_semi_dev_21d_gt3x_252d_avg_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day semi-deviation > 3x its 252-day average (crisis-level downside vol)."""
    sd = dsd_001_semi_dev_21d(close)
    avg = _rolling_mean(sd, _TD_YEAR)
    return (sd > 3.0 * avg).astype(float)


def dsd_070_semi_dev_21d_norm_252d_avg(close: pd.Series) -> pd.Series:
    """21-day semi-deviation normalized by its 252-day rolling average."""
    sd = dsd_001_semi_dev_21d(close)
    avg = _rolling_mean(sd, _TD_YEAR)
    return _safe_div(sd, avg)


def dsd_071_semi_dev_63d_norm_252d_avg(close: pd.Series) -> pd.Series:
    """63-day semi-deviation normalized by its 252-day rolling average."""
    sd = dsd_002_semi_dev_63d(close)
    avg = _rolling_mean(sd, _TD_YEAR)
    return _safe_div(sd, avg)


def dsd_072_lpm1_vs0_21d_norm_252d_avg(close: pd.Series) -> pd.Series:
    """21-day LPM1 vs 0 normalized by its 252-day rolling average."""
    lpm = dsd_031_lpm1_vs0_21d(close)
    avg = _rolling_mean(lpm, _TD_YEAR)
    return _safe_div(lpm, avg)


def dsd_073_lpm2_vs0_63d_norm_252d_avg(close: pd.Series) -> pd.Series:
    """63-day LPM2 vs 0 normalized by its 252-day rolling average."""
    lpm = dsd_035_lpm2_vs0_63d(close)
    avg = _rolling_mean(lpm, _TD_YEAR)
    return _safe_div(lpm, avg)


def dsd_074_down_up_semi_dev_diff_21d(close: pd.Series) -> pd.Series:
    """Absolute difference between downside and upside semi-deviation over 21 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return (dn - up).abs()


def dsd_075_down_up_semi_dev_diff_63d(close: pd.Series) -> pd.Series:
    """Absolute difference between downside and upside semi-deviation over 63 days."""
    r = _log_ret(close)
    dn_sq = (r ** 2).where(r < 0.0, 0.0)
    up_sq = (r ** 2).where(r > 0.0, 0.0)
    dn = np.sqrt(dn_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    up = np.sqrt(up_sq.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return (dn - up).abs()


# ── Registry ──────────────────────────────────────────────────────────────────

DOWNSIDE_DEVIATION_REGISTRY_001_075 = {
    "dsd_001_semi_dev_21d": {"inputs": ["close"], "func": dsd_001_semi_dev_21d},
    "dsd_002_semi_dev_63d": {"inputs": ["close"], "func": dsd_002_semi_dev_63d},
    "dsd_003_semi_dev_126d": {"inputs": ["close"], "func": dsd_003_semi_dev_126d},
    "dsd_004_semi_dev_252d": {"inputs": ["close"], "func": dsd_004_semi_dev_252d},
    "dsd_005_semi_dev_5d": {"inputs": ["close"], "func": dsd_005_semi_dev_5d},
    "dsd_006_semi_dev_10d": {"inputs": ["close"], "func": dsd_006_semi_dev_10d},
    "dsd_007_semi_dev_annualized_21d": {"inputs": ["close"], "func": dsd_007_semi_dev_annualized_21d},
    "dsd_008_semi_dev_annualized_63d": {"inputs": ["close"], "func": dsd_008_semi_dev_annualized_63d},
    "dsd_009_semi_dev_annualized_252d": {"inputs": ["close"], "func": dsd_009_semi_dev_annualized_252d},
    "dsd_010_semi_dev_ewm_21d": {"inputs": ["close"], "func": dsd_010_semi_dev_ewm_21d},
    "dsd_011_semi_variance_21d": {"inputs": ["close"], "func": dsd_011_semi_variance_21d},
    "dsd_012_semi_variance_63d": {"inputs": ["close"], "func": dsd_012_semi_variance_63d},
    "dsd_013_semi_variance_252d": {"inputs": ["close"], "func": dsd_013_semi_variance_252d},
    "dsd_014_semi_variance_126d": {"inputs": ["close"], "func": dsd_014_semi_variance_126d},
    "dsd_015_semi_variance_5d": {"inputs": ["close"], "func": dsd_015_semi_variance_5d},
    "dsd_016_semi_variance_ewm_span63": {"inputs": ["close"], "func": dsd_016_semi_variance_ewm_span63},
    "dsd_017_semi_variance_norm_by_total_var_21d": {"inputs": ["close"], "func": dsd_017_semi_variance_norm_by_total_var_21d},
    "dsd_018_semi_variance_norm_by_total_var_63d": {"inputs": ["close"], "func": dsd_018_semi_variance_norm_by_total_var_63d},
    "dsd_019_semi_variance_norm_by_total_var_252d": {"inputs": ["close"], "func": dsd_019_semi_variance_norm_by_total_var_252d},
    "dsd_020_semi_variance_pct_rank_252d": {"inputs": ["close"], "func": dsd_020_semi_variance_pct_rank_252d},
    "dsd_021_down_to_total_vol_ratio_21d": {"inputs": ["close"], "func": dsd_021_down_to_total_vol_ratio_21d},
    "dsd_022_down_to_total_vol_ratio_63d": {"inputs": ["close"], "func": dsd_022_down_to_total_vol_ratio_63d},
    "dsd_023_down_to_total_vol_ratio_252d": {"inputs": ["close"], "func": dsd_023_down_to_total_vol_ratio_252d},
    "dsd_024_downside_upside_vol_ratio_21d": {"inputs": ["close"], "func": dsd_024_downside_upside_vol_ratio_21d},
    "dsd_025_downside_upside_vol_ratio_63d": {"inputs": ["close"], "func": dsd_025_downside_upside_vol_ratio_63d},
    "dsd_026_downside_upside_vol_ratio_252d": {"inputs": ["close"], "func": dsd_026_downside_upside_vol_ratio_252d},
    "dsd_027_downside_vol_share_21d": {"inputs": ["close"], "func": dsd_027_downside_vol_share_21d},
    "dsd_028_downside_vol_share_63d": {"inputs": ["close"], "func": dsd_028_downside_vol_share_63d},
    "dsd_029_downside_vol_share_252d": {"inputs": ["close"], "func": dsd_029_downside_vol_share_252d},
    "dsd_030_semi_dev_21d_pct_rank_252d": {"inputs": ["close"], "func": dsd_030_semi_dev_21d_pct_rank_252d},
    "dsd_031_lpm1_vs0_21d": {"inputs": ["close"], "func": dsd_031_lpm1_vs0_21d},
    "dsd_032_lpm1_vs0_63d": {"inputs": ["close"], "func": dsd_032_lpm1_vs0_63d},
    "dsd_033_lpm1_vs0_252d": {"inputs": ["close"], "func": dsd_033_lpm1_vs0_252d},
    "dsd_034_lpm2_vs0_21d": {"inputs": ["close"], "func": dsd_034_lpm2_vs0_21d},
    "dsd_035_lpm2_vs0_63d": {"inputs": ["close"], "func": dsd_035_lpm2_vs0_63d},
    "dsd_036_lpm2_vs0_252d": {"inputs": ["close"], "func": dsd_036_lpm2_vs0_252d},
    "dsd_037_lpm3_vs0_21d": {"inputs": ["close"], "func": dsd_037_lpm3_vs0_21d},
    "dsd_038_lpm3_vs0_63d": {"inputs": ["close"], "func": dsd_038_lpm3_vs0_63d},
    "dsd_039_lpm3_vs0_252d": {"inputs": ["close"], "func": dsd_039_lpm3_vs0_252d},
    "dsd_040_lpm1_vs0_5d": {"inputs": ["close"], "func": dsd_040_lpm1_vs0_5d},
    "dsd_041_lpm1_vs_mean_21d": {"inputs": ["close"], "func": dsd_041_lpm1_vs_mean_21d},
    "dsd_042_lpm1_vs_mean_63d": {"inputs": ["close"], "func": dsd_042_lpm1_vs_mean_63d},
    "dsd_043_lpm1_vs_mean_252d": {"inputs": ["close"], "func": dsd_043_lpm1_vs_mean_252d},
    "dsd_044_lpm2_vs_mean_21d": {"inputs": ["close"], "func": dsd_044_lpm2_vs_mean_21d},
    "dsd_045_lpm2_vs_mean_63d": {"inputs": ["close"], "func": dsd_045_lpm2_vs_mean_63d},
    "dsd_046_lpm2_vs_mean_252d": {"inputs": ["close"], "func": dsd_046_lpm2_vs_mean_252d},
    "dsd_047_lpm3_vs_mean_21d": {"inputs": ["close"], "func": dsd_047_lpm3_vs_mean_21d},
    "dsd_048_lpm3_vs_mean_63d": {"inputs": ["close"], "func": dsd_048_lpm3_vs_mean_63d},
    "dsd_049_lpm2_vs_mean_21d_sqrt": {"inputs": ["close"], "func": dsd_049_lpm2_vs_mean_21d_sqrt},
    "dsd_050_lpm2_vs_mean_63d_sqrt": {"inputs": ["close"], "func": dsd_050_lpm2_vs_mean_63d_sqrt},
    "dsd_051_sortino_ratio_21d": {"inputs": ["close"], "func": dsd_051_sortino_ratio_21d},
    "dsd_052_sortino_ratio_63d": {"inputs": ["close"], "func": dsd_052_sortino_ratio_63d},
    "dsd_053_sortino_ratio_252d": {"inputs": ["close"], "func": dsd_053_sortino_ratio_252d},
    "dsd_054_sortino_vs_sharpe_ratio_63d": {"inputs": ["close"], "func": dsd_054_sortino_vs_sharpe_ratio_63d},
    "dsd_055_sortino_vs_sharpe_ratio_252d": {"inputs": ["close"], "func": dsd_055_sortino_vs_sharpe_ratio_252d},
    "dsd_056_downside_risk_annualized_21d": {"inputs": ["close"], "func": dsd_056_downside_risk_annualized_21d},
    "dsd_057_downside_risk_annualized_63d": {"inputs": ["close"], "func": dsd_057_downside_risk_annualized_63d},
    "dsd_058_lpm1_sortino_21d": {"inputs": ["close"], "func": dsd_058_lpm1_sortino_21d},
    "dsd_059_lpm1_sortino_63d": {"inputs": ["close"], "func": dsd_059_lpm1_sortino_63d},
    "dsd_060_downside_risk_pct_rank_252d": {"inputs": ["close"], "func": dsd_060_downside_risk_pct_rank_252d},
    "dsd_061_semi_dev_21d_zscore_252d": {"inputs": ["close"], "func": dsd_061_semi_dev_21d_zscore_252d},
    "dsd_062_semi_dev_63d_zscore_252d": {"inputs": ["close"], "func": dsd_062_semi_dev_63d_zscore_252d},
    "dsd_063_semi_dev_252d_expanding_zscore": {"inputs": ["close"], "func": dsd_063_semi_dev_252d_expanding_zscore},
    "dsd_064_lpm2_vs0_21d_zscore_252d": {"inputs": ["close"], "func": dsd_064_lpm2_vs0_21d_zscore_252d},
    "dsd_065_downside_upside_vol_ratio_21d_zscore_252d": {"inputs": ["close"], "func": dsd_065_downside_upside_vol_ratio_21d_zscore_252d},
    "dsd_066_semi_dev_21d_expanding_max": {"inputs": ["close"], "func": dsd_066_semi_dev_21d_expanding_max},
    "dsd_067_semi_dev_21d_vs_expanding_max": {"inputs": ["close"], "func": dsd_067_semi_dev_21d_vs_expanding_max},
    "dsd_068_semi_dev_21d_gt2x_252d_avg_flag": {"inputs": ["close"], "func": dsd_068_semi_dev_21d_gt2x_252d_avg_flag},
    "dsd_069_semi_dev_21d_gt3x_252d_avg_flag": {"inputs": ["close"], "func": dsd_069_semi_dev_21d_gt3x_252d_avg_flag},
    "dsd_070_semi_dev_21d_norm_252d_avg": {"inputs": ["close"], "func": dsd_070_semi_dev_21d_norm_252d_avg},
    "dsd_071_semi_dev_63d_norm_252d_avg": {"inputs": ["close"], "func": dsd_071_semi_dev_63d_norm_252d_avg},
    "dsd_072_lpm1_vs0_21d_norm_252d_avg": {"inputs": ["close"], "func": dsd_072_lpm1_vs0_21d_norm_252d_avg},
    "dsd_073_lpm2_vs0_63d_norm_252d_avg": {"inputs": ["close"], "func": dsd_073_lpm2_vs0_63d_norm_252d_avg},
    "dsd_074_down_up_semi_dev_diff_21d": {"inputs": ["close"], "func": dsd_074_down_up_semi_dev_diff_21d},
    "dsd_075_down_up_semi_dev_diff_63d": {"inputs": ["close"], "func": dsd_075_down_up_semi_dev_diff_63d},
}
