"""
110_tail_risk_evt — Base Features 001-075
Domain: extreme-value / tail-risk statistics of returns — Hill tail index and other
        tail-exponent estimators, peaks-over-threshold exceedance counts and magnitudes,
        Value-at-Risk and Expected Shortfall / CVaR at multiple confidence levels,
        VaR-breach frequency, generalized-Pareto-style tail scale,
        max-drawdown-of-returns, tail-fatness measures of the LEFT (downside) tail.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_returns(close: pd.Series) -> pd.Series:
    """Log returns; first element is NaN."""
    return np.log(close / close.shift(1))


def _neg_returns(close: pd.Series) -> pd.Series:
    """Negative log returns (losses are positive values)."""
    return -_log_returns(close)


def _rolling_var(close: pd.Series, w: int, q: float) -> pd.Series:
    """Rolling empirical Value-at-Risk at quantile q (loss convention, positive = loss).
    q=0.95 means the 95th percentile of losses."""
    r = _neg_returns(close)
    return r.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _rolling_es(close: pd.Series, w: int, q: float) -> pd.Series:
    """Rolling Expected Shortfall (CVaR) at confidence q — mean of losses exceeding VaR."""
    r = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        threshold = np.quantile(x, q)
        tail = x[x >= threshold]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return r.rolling(w, min_periods=max(2, w // 2)).apply(_es, raw=True)


def _hill_estimator(losses: np.ndarray, k: int) -> float:
    """Hill (1975) tail-index estimator using k upper-order statistics.
    Returns the tail exponent alpha (larger = lighter tail)."""
    x = losses[~np.isnan(losses)]
    if len(x) < k + 1 or k < 1:
        return np.nan
    x_sorted = np.sort(x)[::-1]  # descending
    top_k = x_sorted[:k]
    x_k1 = x_sorted[k]
    if x_k1 <= 0:
        return np.nan
    log_ratios = np.log(top_k / (x_k1 + _EPS))
    mean_log = np.mean(log_ratios)
    if mean_log <= 0:
        return np.nan
    return 1.0 / mean_log


def _rolling_hill(losses: pd.Series, w: int, k: int) -> pd.Series:
    """Rolling Hill estimator with window w and k order statistics."""
    def _apply(x):
        return _hill_estimator(x, k)
    return losses.rolling(w, min_periods=max(k + 2, w // 2)).apply(_apply, raw=True)


def _pot_exceedance_count(losses: pd.Series, w: int, threshold_q: float) -> pd.Series:
    """Count of exceedances above a threshold (peaks-over-threshold count)."""
    threshold = losses.rolling(w, min_periods=max(2, w // 2)).quantile(threshold_q)
    exceedance = (losses > threshold).astype(float)
    return _rolling_sum(exceedance, w)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Hill tail-index estimators at multiple windows ---

def evt_001_hill_63d_k10(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 63-day window, k=10 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_QTR, 10)


def evt_002_hill_63d_k5(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 63-day window, k=5 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_QTR, 5)


def evt_003_hill_126d_k15(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 126-day window, k=15 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_HALF, 15)


def evt_004_hill_126d_k10(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 126-day window, k=10 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_HALF, 10)


def evt_005_hill_252d_k20(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 252-day window, k=20 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_YEAR, 20)


def evt_006_hill_252d_k15(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 252-day window, k=15 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_YEAR, 15)


def evt_007_hill_252d_k10(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 252-day window, k=10 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_YEAR, 10)


def evt_008_hill_21d_k5(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 21-day window, k=5 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_MON, 5)


def evt_009_hill_63d_k15(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator over 63-day window, k=15 order statistics."""
    losses = _neg_returns(close)
    return _rolling_hill(losses, _TD_QTR, 15)


def evt_010_hill_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d Hill index to 252d Hill index (recent vs long-run tail heaviness)."""
    losses = _neg_returns(close)
    h63 = _rolling_hill(losses, _TD_QTR, 10)
    h252 = _rolling_hill(losses, _TD_YEAR, 15)
    return _safe_div(h63, h252.clip(lower=_EPS))


# --- Group B (011-020): Value-at-Risk at multiple windows and confidence levels ---

def evt_011_var95_21d(close: pd.Series) -> pd.Series:
    """Empirical 95th-percentile VaR (loss) over 21-day rolling window."""
    return _rolling_var(close, _TD_MON, 0.95)


def evt_012_var99_21d(close: pd.Series) -> pd.Series:
    """Empirical 99th-percentile VaR over 21-day rolling window."""
    return _rolling_var(close, _TD_MON, 0.99)


def evt_013_var95_63d(close: pd.Series) -> pd.Series:
    """Empirical 95th-percentile VaR over 63-day rolling window."""
    return _rolling_var(close, _TD_QTR, 0.95)


def evt_014_var99_63d(close: pd.Series) -> pd.Series:
    """Empirical 99th-percentile VaR over 63-day rolling window."""
    return _rolling_var(close, _TD_QTR, 0.99)


def evt_015_var95_126d(close: pd.Series) -> pd.Series:
    """Empirical 95th-percentile VaR over 126-day rolling window."""
    return _rolling_var(close, _TD_HALF, 0.95)


def evt_016_var99_126d(close: pd.Series) -> pd.Series:
    """Empirical 99th-percentile VaR over 126-day rolling window."""
    return _rolling_var(close, _TD_HALF, 0.99)


def evt_017_var95_252d(close: pd.Series) -> pd.Series:
    """Empirical 95th-percentile VaR over 252-day rolling window."""
    return _rolling_var(close, _TD_YEAR, 0.95)


def evt_018_var99_252d(close: pd.Series) -> pd.Series:
    """Empirical 99th-percentile VaR over 252-day rolling window."""
    return _rolling_var(close, _TD_YEAR, 0.99)


def evt_019_var975_63d(close: pd.Series) -> pd.Series:
    """Empirical 97.5th-percentile VaR over 63-day rolling window."""
    return _rolling_var(close, _TD_QTR, 0.975)


def evt_020_var90_63d(close: pd.Series) -> pd.Series:
    """Empirical 90th-percentile VaR over 63-day rolling window."""
    return _rolling_var(close, _TD_QTR, 0.90)


# --- Group C (021-030): Expected Shortfall / CVaR ---

def evt_021_es95_21d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 95% confidence over 21-day window."""
    return _rolling_es(close, _TD_MON, 0.95)


def evt_022_es99_21d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 99% confidence over 21-day window."""
    return _rolling_es(close, _TD_MON, 0.99)


def evt_023_es95_63d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 95% confidence over 63-day window."""
    return _rolling_es(close, _TD_QTR, 0.95)


def evt_024_es99_63d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 99% confidence over 63-day window."""
    return _rolling_es(close, _TD_QTR, 0.99)


def evt_025_es95_126d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 95% confidence over 126-day window."""
    return _rolling_es(close, _TD_HALF, 0.95)


def evt_026_es99_126d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 99% confidence over 126-day window."""
    return _rolling_es(close, _TD_HALF, 0.99)


def evt_027_es95_252d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 95% confidence over 252-day window."""
    return _rolling_es(close, _TD_YEAR, 0.95)


def evt_028_es99_252d(close: pd.Series) -> pd.Series:
    """Expected Shortfall at 99% confidence over 252-day window."""
    return _rolling_es(close, _TD_YEAR, 0.99)


def evt_029_es_vs_var_ratio_95_63d(close: pd.Series) -> pd.Series:
    """Ratio ES95 / VaR95 over 63 days (tail shape above VaR threshold)."""
    es = _rolling_es(close, _TD_QTR, 0.95)
    var = _rolling_var(close, _TD_QTR, 0.95)
    return _safe_div(es, var.clip(lower=_EPS))


def evt_030_es_vs_var_ratio_99_63d(close: pd.Series) -> pd.Series:
    """Ratio ES99 / VaR99 over 63 days."""
    es = _rolling_es(close, _TD_QTR, 0.99)
    var = _rolling_var(close, _TD_QTR, 0.99)
    return _safe_div(es, var.clip(lower=_EPS))


# --- Group D (031-040): Peaks-over-threshold exceedance counts ---

def evt_031_pot_count_95th_21d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding the rolling 95th-percentile threshold, 21-day window."""
    losses = _neg_returns(close)
    threshold = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).quantile(0.95)
    return _rolling_sum((losses > threshold).astype(float), _TD_MON)


def evt_032_pot_count_90th_21d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding the rolling 90th-percentile threshold, 21-day window."""
    losses = _neg_returns(close)
    threshold = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).quantile(0.90)
    return _rolling_sum((losses > threshold).astype(float), _TD_MON)


def evt_033_pot_count_95th_63d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding the rolling 95th-percentile threshold, 63-day window."""
    losses = _neg_returns(close)
    threshold = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    return _rolling_sum((losses > threshold).astype(float), _TD_QTR)


def evt_034_pot_count_99th_63d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding the rolling 99th-percentile threshold, 63-day window."""
    losses = _neg_returns(close)
    threshold = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.99)
    return _rolling_sum((losses > threshold).astype(float), _TD_QTR)


def evt_035_pot_count_95th_252d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding the rolling 95th-percentile threshold, 252-day window."""
    losses = _neg_returns(close)
    threshold = losses.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.95)
    return _rolling_sum((losses > threshold).astype(float), _TD_YEAR)


def evt_036_pot_mean_excess_95th_63d(close: pd.Series) -> pd.Series:
    """Mean excess loss above 95th-percentile threshold over 63-day window."""
    losses = _neg_returns(close)
    def _mean_excess(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x > thr]
        if len(tail) == 0:
            return np.nan
        return float(np.mean(tail) - thr)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_mean_excess, raw=True)


def evt_037_pot_mean_excess_99th_63d(close: pd.Series) -> pd.Series:
    """Mean excess loss above 99th-percentile threshold over 63-day window."""
    losses = _neg_returns(close)
    def _mean_excess_99(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.99)
        tail = x[x > thr]
        if len(tail) == 0:
            return np.nan
        return float(np.mean(tail) - thr)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_mean_excess_99, raw=True)


def evt_038_pot_mean_excess_95th_252d(close: pd.Series) -> pd.Series:
    """Mean excess loss above 95th-percentile threshold over 252-day window."""
    losses = _neg_returns(close)
    def _me_252(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x > thr]
        if len(tail) == 0:
            return np.nan
        return float(np.mean(tail) - thr)
    return losses.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(_me_252, raw=True)


def evt_039_pot_max_excess_95th_63d(close: pd.Series) -> pd.Series:
    """Maximum loss above 95th-percentile threshold over 63-day window."""
    losses = _neg_returns(close)
    def _max_excess(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x > thr]
        if len(tail) == 0:
            return 0.0
        return float(np.max(tail) - thr)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_max_excess, raw=True)


def evt_040_pot_scale_gpd_63d(close: pd.Series) -> pd.Series:
    """GPD-style tail scale: std of losses exceeding 90th percentile over 63 days."""
    losses = _neg_returns(close)
    def _gpd_scale(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.90)
        tail = x[x > thr]
        if len(tail) < 2:
            return np.nan
        return float(np.std(tail, ddof=1))
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_gpd_scale, raw=True)


# --- Group E (041-050): VaR breach frequency ---

def evt_041_var_breach_freq_95_21d_in_63d(close: pd.Series) -> pd.Series:
    """Frequency of VaR95(21d) breaches in trailing 63-day window."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_MON, 0.95)
    breach = (losses > var95.shift(1)).astype(float)
    return _rolling_sum(breach, _TD_QTR)


def evt_042_var_breach_freq_99_21d_in_63d(close: pd.Series) -> pd.Series:
    """Frequency of VaR99(21d) breaches in trailing 63-day window."""
    losses = _neg_returns(close)
    var99 = _rolling_var(close, _TD_MON, 0.99)
    breach = (losses > var99.shift(1)).astype(float)
    return _rolling_sum(breach, _TD_QTR)


def evt_043_var_breach_freq_95_63d_in_252d(close: pd.Series) -> pd.Series:
    """Frequency of VaR95(63d) breaches in trailing 252-day window."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_QTR, 0.95)
    breach = (losses > var95.shift(1)).astype(float)
    return _rolling_sum(breach, _TD_YEAR)


def evt_044_var_breach_consec_21d(close: pd.Series) -> pd.Series:
    """Consecutive days that VaR95(21d) has been breached."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_MON, 0.95)
    breach = losses > var95.shift(1)
    return _consec_streak(breach)


def evt_045_var_breach_consec_63d(close: pd.Series) -> pd.Series:
    """Consecutive days that VaR95(63d) has been breached."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_QTR, 0.95)
    breach = losses > var95.shift(1)
    return _consec_streak(breach)


def evt_046_var_excess_magnitude_95_21d(close: pd.Series) -> pd.Series:
    """When VaR95(21d) is breached, magnitude of excess; 0 otherwise."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_MON, 0.95)
    excess = (losses - var95.shift(1)).clip(lower=0.0)
    return excess


def evt_047_var_excess_magnitude_99_63d(close: pd.Series) -> pd.Series:
    """When VaR99(63d) is breached, magnitude of excess; 0 otherwise."""
    losses = _neg_returns(close)
    var99 = _rolling_var(close, _TD_QTR, 0.99)
    excess = (losses - var99.shift(1)).clip(lower=0.0)
    return excess


def evt_048_var95_21d_normalized_by_std(close: pd.Series) -> pd.Series:
    """VaR95(21d) divided by rolling 21-day std of returns (tail-to-vol ratio)."""
    var95 = _rolling_var(close, _TD_MON, 0.95)
    ret_std = _rolling_std(_log_returns(close), _TD_MON)
    return _safe_div(var95, ret_std.clip(lower=_EPS))


def evt_049_var99_63d_normalized_by_std(close: pd.Series) -> pd.Series:
    """VaR99(63d) divided by rolling 63-day std (tail-to-vol ratio)."""
    var99 = _rolling_var(close, _TD_QTR, 0.99)
    ret_std = _rolling_std(_log_returns(close), _TD_QTR)
    return _safe_div(var99, ret_std.clip(lower=_EPS))


def evt_050_var_breach_freq_99_63d_in_252d(close: pd.Series) -> pd.Series:
    """Frequency of VaR99(63d) breaches in trailing 252-day window."""
    losses = _neg_returns(close)
    var99 = _rolling_var(close, _TD_QTR, 0.99)
    breach = (losses > var99.shift(1)).astype(float)
    return _rolling_sum(breach, _TD_YEAR)


# --- Group F (051-060): Max drawdown of returns, left tail size ---

def evt_051_max_loss_21d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss (negative log-return magnitude) over 21 days."""
    losses = _neg_returns(close)
    return _rolling_max(losses, _TD_MON)


def evt_052_max_loss_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss over 63 days."""
    losses = _neg_returns(close)
    return _rolling_max(losses, _TD_QTR)


def evt_053_max_loss_252d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss over 252 days."""
    losses = _neg_returns(close)
    return _rolling_max(losses, _TD_YEAR)


def evt_054_max_loss_5d(close: pd.Series) -> pd.Series:
    """Maximum single-day loss over 5 days."""
    losses = _neg_returns(close)
    return _rolling_max(losses, _TD_WEEK)


def evt_055_sum_losses_above_2pct_21d(close: pd.Series) -> pd.Series:
    """Sum of daily losses > 2% in trailing 21 days."""
    losses = _neg_returns(close)
    big = losses.where(losses > 0.02, 0.0)
    return _rolling_sum(big, _TD_MON)


def evt_056_sum_losses_above_3pct_63d(close: pd.Series) -> pd.Series:
    """Sum of daily losses > 3% in trailing 63 days."""
    losses = _neg_returns(close)
    big = losses.where(losses > 0.03, 0.0)
    return _rolling_sum(big, _TD_QTR)


def evt_057_count_losses_above_2pct_21d(close: pd.Series) -> pd.Series:
    """Count of daily losses > 2% in trailing 21 days."""
    losses = _neg_returns(close)
    return _rolling_sum((losses > 0.02).astype(float), _TD_MON)


def evt_058_count_losses_above_3pct_63d(close: pd.Series) -> pd.Series:
    """Count of daily losses > 3% in trailing 63 days."""
    losses = _neg_returns(close)
    return _rolling_sum((losses > 0.03).astype(float), _TD_QTR)


def evt_059_count_losses_above_5pct_252d(close: pd.Series) -> pd.Series:
    """Count of daily losses > 5% in trailing 252 days."""
    losses = _neg_returns(close)
    return _rolling_sum((losses > 0.05).astype(float), _TD_YEAR)


def evt_060_loss_skewness_63d(close: pd.Series) -> pd.Series:
    """Skewness of daily log-return distribution over 63 days (negative = left tail)."""
    r = _log_returns(close)
    return r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


# --- Group G (061-075): Tail-fatness / kurtosis / excess measures ---

def evt_061_loss_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns over 63 days (fat-tail indicator)."""
    r = _log_returns(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def evt_062_loss_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns over 252 days."""
    r = _log_returns(close)
    return r.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()


def evt_063_lower_partial_moment1_63d(close: pd.Series) -> pd.Series:
    """Lower partial moment of order 1 (mean semi-deviation below zero) over 63 days."""
    r = _log_returns(close)
    below = r.where(r < 0.0, 0.0)
    return below.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean().abs()


def evt_064_lower_partial_moment2_63d(close: pd.Series) -> pd.Series:
    """Lower partial moment of order 2 (semi-variance below zero) over 63 days."""
    r = _log_returns(close)
    below = (r.where(r < 0.0, 0.0)) ** 2
    return below.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()


def evt_065_downside_deviation_21d(close: pd.Series) -> pd.Series:
    """Annualized downside deviation (sqrt of semi-variance) over 21 days."""
    r = _log_returns(close)
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_var = sq.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).mean()
    return np.sqrt(semi_var * _TD_YEAR)


def evt_066_downside_deviation_63d(close: pd.Series) -> pd.Series:
    """Annualized downside deviation over 63 days."""
    r = _log_returns(close)
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_var = sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return np.sqrt(semi_var * _TD_YEAR)


def evt_067_tail_ratio_95_5_63d(close: pd.Series) -> pd.Series:
    """Ratio of 95th to 5th percentile return (right-to-left tail asymmetry) over 63 days."""
    r = _log_returns(close)
    p95 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    p05 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.05)
    return _safe_div(p95.abs(), p05.abs().clip(lower=_EPS))


def evt_068_left_tail_weight_63d(close: pd.Series) -> pd.Series:
    """Weight of returns in bottom 5th percentile vs full distribution over 63 days."""
    r = _log_returns(close)
    def _left_weight(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        thr = np.quantile(x, 0.05)
        return float(np.sum(x <= thr) / len(x))
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_left_weight, raw=True)


def evt_069_left_tail_mean_63d(close: pd.Series) -> pd.Series:
    """Mean of returns in bottom 10th percentile over 63 days (left tail center)."""
    r = _log_returns(close)
    def _left_mean(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.10)
        tail = x[x <= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_left_mean, raw=True)


def evt_070_left_tail_std_63d(close: pd.Series) -> pd.Series:
    """Std of returns in bottom 10th percentile over 63 days (left tail dispersion)."""
    r = _log_returns(close)
    def _left_std(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.10)
        tail = x[x <= thr]
        if len(tail) < 2:
            return np.nan
        return float(np.std(tail, ddof=1))
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_left_std, raw=True)


def evt_071_loss_vol_ratio_63d(close: pd.Series) -> pd.Series:
    """Mean of positive losses divided by std of all returns (loss-to-vol ratio) over 63 days."""
    r = _log_returns(close)
    losses = _neg_returns(close)
    mean_loss = losses.where(losses > 0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    ret_std = _rolling_std(r, _TD_QTR)
    return _safe_div(mean_loss, ret_std.clip(lower=_EPS))


def evt_072_returns_drawdown_63d(close: pd.Series) -> pd.Series:
    """Max drawdown of daily log-returns cumsum over trailing 63 days (return path DD)."""
    r = _log_returns(close)
    def _ret_dd(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        cum = np.cumsum(x)
        peak = np.maximum.accumulate(cum)
        dd = cum - peak
        return float(np.min(dd))
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_ret_dd, raw=True)


def evt_073_returns_drawdown_252d(close: pd.Series) -> pd.Series:
    """Max drawdown of cumulative log-returns over trailing 252 days."""
    r = _log_returns(close)
    def _ret_dd252(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        cum = np.cumsum(x)
        peak = np.maximum.accumulate(cum)
        dd = cum - peak
        return float(np.min(dd))
    return r.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(_ret_dd252, raw=True)


def evt_074_tail_index_vs_long_run_ratio(close: pd.Series) -> pd.Series:
    """Hill index(63d,k=10) minus Hill index(252d,k=20): positive = heavier recent tail."""
    losses = _neg_returns(close)
    h63 = _rolling_hill(losses, _TD_QTR, 10)
    h252 = _rolling_hill(losses, _TD_YEAR, 20)
    return h252 - h63


def evt_075_extreme_loss_cluster_21d(close: pd.Series) -> pd.Series:
    """Count of days with loss > 1.5x rolling median loss in trailing 21 days."""
    losses = _neg_returns(close)
    med = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).median()
    threshold = 1.5 * med.clip(lower=_EPS)
    return _rolling_sum((losses > threshold).astype(float), _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TAIL_RISK_EVT_REGISTRY_001_075 = {
    "evt_001_hill_63d_k10": {"inputs": ["close"], "func": evt_001_hill_63d_k10},
    "evt_002_hill_63d_k5": {"inputs": ["close"], "func": evt_002_hill_63d_k5},
    "evt_003_hill_126d_k15": {"inputs": ["close"], "func": evt_003_hill_126d_k15},
    "evt_004_hill_126d_k10": {"inputs": ["close"], "func": evt_004_hill_126d_k10},
    "evt_005_hill_252d_k20": {"inputs": ["close"], "func": evt_005_hill_252d_k20},
    "evt_006_hill_252d_k15": {"inputs": ["close"], "func": evt_006_hill_252d_k15},
    "evt_007_hill_252d_k10": {"inputs": ["close"], "func": evt_007_hill_252d_k10},
    "evt_008_hill_21d_k5": {"inputs": ["close"], "func": evt_008_hill_21d_k5},
    "evt_009_hill_63d_k15": {"inputs": ["close"], "func": evt_009_hill_63d_k15},
    "evt_010_hill_ratio_63d_vs_252d": {"inputs": ["close"], "func": evt_010_hill_ratio_63d_vs_252d},
    "evt_011_var95_21d": {"inputs": ["close"], "func": evt_011_var95_21d},
    "evt_012_var99_21d": {"inputs": ["close"], "func": evt_012_var99_21d},
    "evt_013_var95_63d": {"inputs": ["close"], "func": evt_013_var95_63d},
    "evt_014_var99_63d": {"inputs": ["close"], "func": evt_014_var99_63d},
    "evt_015_var95_126d": {"inputs": ["close"], "func": evt_015_var95_126d},
    "evt_016_var99_126d": {"inputs": ["close"], "func": evt_016_var99_126d},
    "evt_017_var95_252d": {"inputs": ["close"], "func": evt_017_var95_252d},
    "evt_018_var99_252d": {"inputs": ["close"], "func": evt_018_var99_252d},
    "evt_019_var975_63d": {"inputs": ["close"], "func": evt_019_var975_63d},
    "evt_020_var90_63d": {"inputs": ["close"], "func": evt_020_var90_63d},
    "evt_021_es95_21d": {"inputs": ["close"], "func": evt_021_es95_21d},
    "evt_022_es99_21d": {"inputs": ["close"], "func": evt_022_es99_21d},
    "evt_023_es95_63d": {"inputs": ["close"], "func": evt_023_es95_63d},
    "evt_024_es99_63d": {"inputs": ["close"], "func": evt_024_es99_63d},
    "evt_025_es95_126d": {"inputs": ["close"], "func": evt_025_es95_126d},
    "evt_026_es99_126d": {"inputs": ["close"], "func": evt_026_es99_126d},
    "evt_027_es95_252d": {"inputs": ["close"], "func": evt_027_es95_252d},
    "evt_028_es99_252d": {"inputs": ["close"], "func": evt_028_es99_252d},
    "evt_029_es_vs_var_ratio_95_63d": {"inputs": ["close"], "func": evt_029_es_vs_var_ratio_95_63d},
    "evt_030_es_vs_var_ratio_99_63d": {"inputs": ["close"], "func": evt_030_es_vs_var_ratio_99_63d},
    "evt_031_pot_count_95th_21d": {"inputs": ["close"], "func": evt_031_pot_count_95th_21d},
    "evt_032_pot_count_90th_21d": {"inputs": ["close"], "func": evt_032_pot_count_90th_21d},
    "evt_033_pot_count_95th_63d": {"inputs": ["close"], "func": evt_033_pot_count_95th_63d},
    "evt_034_pot_count_99th_63d": {"inputs": ["close"], "func": evt_034_pot_count_99th_63d},
    "evt_035_pot_count_95th_252d": {"inputs": ["close"], "func": evt_035_pot_count_95th_252d},
    "evt_036_pot_mean_excess_95th_63d": {"inputs": ["close"], "func": evt_036_pot_mean_excess_95th_63d},
    "evt_037_pot_mean_excess_99th_63d": {"inputs": ["close"], "func": evt_037_pot_mean_excess_99th_63d},
    "evt_038_pot_mean_excess_95th_252d": {"inputs": ["close"], "func": evt_038_pot_mean_excess_95th_252d},
    "evt_039_pot_max_excess_95th_63d": {"inputs": ["close"], "func": evt_039_pot_max_excess_95th_63d},
    "evt_040_pot_scale_gpd_63d": {"inputs": ["close"], "func": evt_040_pot_scale_gpd_63d},
    "evt_041_var_breach_freq_95_21d_in_63d": {"inputs": ["close"], "func": evt_041_var_breach_freq_95_21d_in_63d},
    "evt_042_var_breach_freq_99_21d_in_63d": {"inputs": ["close"], "func": evt_042_var_breach_freq_99_21d_in_63d},
    "evt_043_var_breach_freq_95_63d_in_252d": {"inputs": ["close"], "func": evt_043_var_breach_freq_95_63d_in_252d},
    "evt_044_var_breach_consec_21d": {"inputs": ["close"], "func": evt_044_var_breach_consec_21d},
    "evt_045_var_breach_consec_63d": {"inputs": ["close"], "func": evt_045_var_breach_consec_63d},
    "evt_046_var_excess_magnitude_95_21d": {"inputs": ["close"], "func": evt_046_var_excess_magnitude_95_21d},
    "evt_047_var_excess_magnitude_99_63d": {"inputs": ["close"], "func": evt_047_var_excess_magnitude_99_63d},
    "evt_048_var95_21d_normalized_by_std": {"inputs": ["close"], "func": evt_048_var95_21d_normalized_by_std},
    "evt_049_var99_63d_normalized_by_std": {"inputs": ["close"], "func": evt_049_var99_63d_normalized_by_std},
    "evt_050_var_breach_freq_99_63d_in_252d": {"inputs": ["close"], "func": evt_050_var_breach_freq_99_63d_in_252d},
    "evt_051_max_loss_21d": {"inputs": ["close"], "func": evt_051_max_loss_21d},
    "evt_052_max_loss_63d": {"inputs": ["close"], "func": evt_052_max_loss_63d},
    "evt_053_max_loss_252d": {"inputs": ["close"], "func": evt_053_max_loss_252d},
    "evt_054_max_loss_5d": {"inputs": ["close"], "func": evt_054_max_loss_5d},
    "evt_055_sum_losses_above_2pct_21d": {"inputs": ["close"], "func": evt_055_sum_losses_above_2pct_21d},
    "evt_056_sum_losses_above_3pct_63d": {"inputs": ["close"], "func": evt_056_sum_losses_above_3pct_63d},
    "evt_057_count_losses_above_2pct_21d": {"inputs": ["close"], "func": evt_057_count_losses_above_2pct_21d},
    "evt_058_count_losses_above_3pct_63d": {"inputs": ["close"], "func": evt_058_count_losses_above_3pct_63d},
    "evt_059_count_losses_above_5pct_252d": {"inputs": ["close"], "func": evt_059_count_losses_above_5pct_252d},
    "evt_060_loss_skewness_63d": {"inputs": ["close"], "func": evt_060_loss_skewness_63d},
    "evt_061_loss_kurtosis_63d": {"inputs": ["close"], "func": evt_061_loss_kurtosis_63d},
    "evt_062_loss_kurtosis_252d": {"inputs": ["close"], "func": evt_062_loss_kurtosis_252d},
    "evt_063_lower_partial_moment1_63d": {"inputs": ["close"], "func": evt_063_lower_partial_moment1_63d},
    "evt_064_lower_partial_moment2_63d": {"inputs": ["close"], "func": evt_064_lower_partial_moment2_63d},
    "evt_065_downside_deviation_21d": {"inputs": ["close"], "func": evt_065_downside_deviation_21d},
    "evt_066_downside_deviation_63d": {"inputs": ["close"], "func": evt_066_downside_deviation_63d},
    "evt_067_tail_ratio_95_5_63d": {"inputs": ["close"], "func": evt_067_tail_ratio_95_5_63d},
    "evt_068_left_tail_weight_63d": {"inputs": ["close"], "func": evt_068_left_tail_weight_63d},
    "evt_069_left_tail_mean_63d": {"inputs": ["close"], "func": evt_069_left_tail_mean_63d},
    "evt_070_left_tail_std_63d": {"inputs": ["close"], "func": evt_070_left_tail_std_63d},
    "evt_071_loss_vol_ratio_63d": {"inputs": ["close"], "func": evt_071_loss_vol_ratio_63d},
    "evt_072_returns_drawdown_63d": {"inputs": ["close"], "func": evt_072_returns_drawdown_63d},
    "evt_073_returns_drawdown_252d": {"inputs": ["close"], "func": evt_073_returns_drawdown_252d},
    "evt_074_tail_index_vs_long_run_ratio": {"inputs": ["close"], "func": evt_074_tail_index_vs_long_run_ratio},
    "evt_075_extreme_loss_cluster_21d": {"inputs": ["close"], "func": evt_075_extreme_loss_cluster_21d},
}
