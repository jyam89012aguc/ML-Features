"""
01_drawdown_depth — Extended Features 001-075
Domain: decline magnitude vs trailing highs — conditional drawdown risk, drawdown deviation,
        Burke-ratio variants, distribution shape, percentile ranks, anchor-price variants,
        log-drawdown z-scores, and rate-of-change of extended measures.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Net-new relative to base_001_075, base_076_150, 2nd_derivatives, 3rd_derivatives.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _dd_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    """Percentage drawdown of close from its w-day rolling high."""
    h = _rolling_max(close, w)
    return _safe_div(close - h, h)


# ── Scalar helpers for rolling apply ─────────────────────────────────────────

def _scalar_mean_worst_pct(arr: np.ndarray, pct: float) -> float:
    """Mean of the worst (most-negative) pct fraction of arr. Scalar output."""
    if len(arr) == 0:
        return np.nan
    n_tail = max(1, int(np.floor(len(arr) * pct)))
    sorted_arr = np.sort(arr)          # ascending: most negative first
    return float(np.mean(sorted_arr[:n_tail]))


def _scalar_quantile(arr: np.ndarray, q: float) -> float:
    """q-th quantile of arr. Scalar output."""
    if len(arr) == 0:
        return np.nan
    return float(np.nanquantile(arr, q))


def _scalar_mean_worst_n(arr: np.ndarray, n: int) -> float:
    """Mean of the N smallest (worst) values. Scalar output."""
    if len(arr) < n:
        return np.nan
    sorted_arr = np.sort(arr)
    return float(np.mean(sorted_arr[:n]))


def _scalar_sqrt_sum_sq(arr: np.ndarray) -> float:
    """Square root of sum of squared values. Scalar output."""
    if len(arr) == 0:
        return np.nan
    return float(np.sqrt(np.sum(arr ** 2)))


def _scalar_skew(arr: np.ndarray) -> float:
    """Sample skewness. Scalar output."""
    arr = arr[~np.isnan(arr)]
    if len(arr) < 3:
        return np.nan
    m = np.mean(arr)
    s = np.std(arr, ddof=1)
    if s < _EPS:
        return np.nan
    return float(np.mean(((arr - m) / s) ** 3))


def _scalar_kurt(arr: np.ndarray) -> float:
    """Excess kurtosis. Scalar output."""
    arr = arr[~np.isnan(arr)]
    if len(arr) < 4:
        return np.nan
    m = np.mean(arr)
    s = np.std(arr, ddof=1)
    if s < _EPS:
        return np.nan
    return float(np.mean(((arr - m) / s) ** 4) - 3.0)


def _scalar_downside_std(arr: np.ndarray, threshold: float = 0.0) -> float:
    """Std dev of values below threshold (semi-std). Scalar output."""
    below = arr[arr < threshold]
    if len(below) < 2:
        return np.nan
    return float(np.std(below, ddof=1))


# ── Group A (001-012): Conditional Drawdown-at-Risk (CDaR) ────────────────────
# CDaR = mean of worst X% of trailing drawdown series.
# Three quantile levels (5/10/20%), three windows (126/252/504), plus VaR quantiles.

def dd_ext_001_cdar_5pct_126d(close: pd.Series) -> pd.Series:
    """CDaR-5%: mean of worst 5% of 252d-drawdown series over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.05), raw=True)


def dd_ext_002_cdar_5pct_252d(close: pd.Series) -> pd.Series:
    """CDaR-5%: mean of worst 5% of 252d-drawdown series over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.05), raw=True)


def dd_ext_003_cdar_5pct_504d(close: pd.Series) -> pd.Series:
    """CDaR-5%: mean of worst 5% of 252d-drawdown series over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.05), raw=True)


def dd_ext_004_cdar_10pct_126d(close: pd.Series) -> pd.Series:
    """CDaR-10%: mean of worst 10% of 252d-drawdown series over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.10), raw=True)


def dd_ext_005_cdar_10pct_252d(close: pd.Series) -> pd.Series:
    """CDaR-10%: mean of worst 10% of 252d-drawdown series over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.10), raw=True)


def dd_ext_006_cdar_10pct_504d(close: pd.Series) -> pd.Series:
    """CDaR-10%: mean of worst 10% of 252d-drawdown series over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.10), raw=True)


def dd_ext_007_cdar_20pct_126d(close: pd.Series) -> pd.Series:
    """CDaR-20%: mean of worst 20% of 252d-drawdown series over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.20), raw=True)


def dd_ext_008_cdar_20pct_252d(close: pd.Series) -> pd.Series:
    """CDaR-20%: mean of worst 20% of 252d-drawdown series over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.20), raw=True)


def dd_ext_009_cdar_20pct_504d(close: pd.Series) -> pd.Series:
    """CDaR-20%: mean of worst 20% of 252d-drawdown series over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.20), raw=True)


def dd_ext_010_dd_var_q01_252d(close: pd.Series) -> pd.Series:
    """Drawdown VaR 1%: 1st-percentile of 252d-drawdown distribution over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_quantile(dd, _TD_YEAR, 0.01)


def dd_ext_011_dd_var_q05_504d(close: pd.Series) -> pd.Series:
    """Drawdown VaR 5%: 5th-percentile of 252d-drawdown distribution over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).quantile(0.05)


def dd_ext_012_dd_var_q10_252d(close: pd.Series) -> pd.Series:
    """Drawdown VaR 10%: 10th-percentile of 252d-drawdown distribution over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_quantile(dd, _TD_YEAR, 0.10)


# ── Group B (013-021): Drawdown Deviation ─────────────────────────────────────
# Rolling std of the drawdown series; downside drawdown deviation.

def dd_ext_013_dd_std_63d(close: pd.Series) -> pd.Series:
    """Rolling std of 252d-drawdown series over 63-day window (short-term dd volatility)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_std(dd, _TD_QTR)


def dd_ext_014_dd_std_126d(close: pd.Series) -> pd.Series:
    """Rolling std of 252d-drawdown series over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_std(dd, _TD_HALF)


def dd_ext_015_dd_std_504d(close: pd.Series) -> pd.Series:
    """Rolling std of 252d-drawdown series over 504-day window (long-term dd volatility)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_std(dd, 504)


def dd_ext_016_dd_downside_dev_63d(close: pd.Series) -> pd.Series:
    """Downside drawdown deviation: std of negative-only 252d-dd values over 63 days."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda x: _scalar_downside_std(x, threshold=0.0), raw=True)


def dd_ext_017_dd_downside_dev_126d(close: pd.Series) -> pd.Series:
    """Downside drawdown deviation over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_downside_std(x, threshold=0.0), raw=True)


def dd_ext_018_dd_downside_dev_252d(close: pd.Series) -> pd.Series:
    """Downside drawdown deviation over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_downside_std(x, threshold=0.0), raw=True)


def dd_ext_019_dd_std_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day dd std to 252-day dd std (short vs long volatility of drawdown)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    std_63  = _rolling_std(dd, _TD_QTR)
    std_252 = _rolling_std(dd, _TD_YEAR)
    return _safe_div(std_63, std_252)


def dd_ext_020_dd_downside_dev_ath_126d(close: pd.Series) -> pd.Series:
    """Downside deviation of ATH-drawdown series over 126-day window."""
    h  = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_downside_std(x, threshold=0.0), raw=True)


def dd_ext_021_dd_std_normalized_by_mean_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of 252d-drawdown: std / abs(mean) over 252-day window."""
    dd      = _dd_from_rolling_high(close, _TD_YEAR)
    std_252 = _rolling_std(dd, _TD_YEAR)
    mean_252 = _rolling_mean(dd, _TD_YEAR).abs()
    return _safe_div(std_252, mean_252)


# ── Group C (022-030): Average of N Worst Drawdown Days ───────────────────────

def dd_ext_022_avg_worst_5_dd_252d(close: pd.Series) -> pd.Series:
    """Mean of 5 worst (most-negative) 252d-drawdown days in trailing 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_n(x, 5), raw=True)


def dd_ext_023_avg_worst_10_dd_252d(close: pd.Series) -> pd.Series:
    """Mean of 10 worst 252d-drawdown days in trailing 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_n(x, 10), raw=True)


def dd_ext_024_avg_worst_5_dd_126d(close: pd.Series) -> pd.Series:
    """Mean of 5 worst 252d-drawdown days in trailing 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda x: _scalar_mean_worst_n(x, 5), raw=True)


def dd_ext_025_avg_worst_3_dd_63d(close: pd.Series) -> pd.Series:
    """Mean of 3 worst 252d-drawdown days in trailing 63-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda x: _scalar_mean_worst_n(x, 3), raw=True)


def dd_ext_026_avg_worst_20_dd_504d(close: pd.Series) -> pd.Series:
    """Mean of 20 worst 252d-drawdown days in trailing 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        lambda x: _scalar_mean_worst_n(x, 20), raw=True)


# ── Group D (027-033): Burke-ratio-style sqrt-sum-of-squared Drawdowns ────────

def dd_ext_027_burke_sqrt_sum_sq_dd_126d(close: pd.Series) -> pd.Series:
    """Burke denominator: sqrt(sum(dd^2)) of 252d-drawdown series over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _scalar_sqrt_sum_sq, raw=True)


def dd_ext_028_burke_sqrt_sum_sq_dd_252d(close: pd.Series) -> pd.Series:
    """Burke denominator: sqrt(sum(dd^2)) over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _scalar_sqrt_sum_sq, raw=True)


def dd_ext_029_burke_sqrt_sum_sq_dd_504d(close: pd.Series) -> pd.Series:
    """Burke denominator: sqrt(sum(dd^2)) over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        _scalar_sqrt_sum_sq, raw=True)


def dd_ext_030_burke_ratio_252d(close: pd.Series) -> pd.Series:
    """Burke-ratio proxy: mean 252d-return / sqrt(sum(dd^2)) over 252-day window."""
    dd    = _dd_from_rolling_high(close, _TD_YEAR)
    ret   = _daily_ret(close)
    mean_ret = _rolling_mean(ret, _TD_YEAR)
    burke_den = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _scalar_sqrt_sum_sq, raw=True)
    return _safe_div(mean_ret, burke_den.abs())


def dd_ext_031_burke_ratio_126d(close: pd.Series) -> pd.Series:
    """Burke-ratio proxy over 126-day window."""
    dd    = _dd_from_rolling_high(close, _TD_YEAR)
    ret   = _daily_ret(close)
    mean_ret = _rolling_mean(ret, _TD_HALF)
    burke_den = dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _scalar_sqrt_sum_sq, raw=True)
    return _safe_div(mean_ret, burke_den.abs())


# ── Group E (032-040): Drawdown Distribution Skew / Kurtosis ─────────────────

def dd_ext_032_dd_skew_126d(close: pd.Series) -> pd.Series:
    """Skewness of 252d-drawdown distribution over trailing 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _scalar_skew, raw=True)


def dd_ext_033_dd_skew_504d(close: pd.Series) -> pd.Series:
    """Skewness of 252d-drawdown distribution over trailing 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        _scalar_skew, raw=True)


def dd_ext_034_dd_kurtosis_126d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of 252d-drawdown distribution over 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _scalar_kurt, raw=True)


def dd_ext_035_dd_kurtosis_504d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of 252d-drawdown distribution over 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.rolling(504, min_periods=252).apply(
        _scalar_kurt, raw=True)


def dd_ext_036_dd_skew_expanding(close: pd.Series) -> pd.Series:
    """Expanding skewness of 252d-drawdown distribution (full-history tail shape)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.expanding(min_periods=_TD_MON).apply(_scalar_skew, raw=True)


def dd_ext_037_dd_kurtosis_expanding(close: pd.Series) -> pd.Series:
    """Expanding excess kurtosis of 252d-drawdown distribution."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return dd.expanding(min_periods=_TD_MON).apply(_scalar_kurt, raw=True)


# ── Group F (038-045): Drawdown Depth Percentile Ranks (more windows) ─────────

def dd_ext_038_dd_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d-drawdown within trailing 63-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_rank_pct(dd, _TD_QTR)


def dd_ext_039_dd_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d-drawdown within trailing 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_rank_pct(dd, _TD_HALF)


def dd_ext_040_dd_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d-drawdown within trailing 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_rank_pct(dd, 504)


def dd_ext_041_ath_dd_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of ATH-drawdown within trailing 504-day window."""
    h  = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return _rolling_rank_pct(dd, 504)


def dd_ext_042_dd_pct_rank_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d-drawdown within trailing 21-day window."""
    dd = _dd_from_rolling_high(close, _TD_QTR)
    return _rolling_rank_pct(dd, _TD_MON)


# ── Group G (043-050): Max Drawdown in Window vs Current Drawdown ─────────────

def dd_ext_043_max_dd_in_63d_window(close: pd.Series) -> pd.Series:
    """Maximum (most-negative) 252d-drawdown value seen in trailing 63-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_min(dd, _TD_QTR)


def dd_ext_044_max_dd_in_126d_window(close: pd.Series) -> pd.Series:
    """Maximum (most-negative) 252d-drawdown value seen in trailing 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_min(dd, _TD_HALF)


def dd_ext_045_max_dd_in_504d_window(close: pd.Series) -> pd.Series:
    """Maximum (most-negative) 252d-drawdown value seen in trailing 504-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _rolling_min(dd, 504)


def dd_ext_046_current_vs_max_dd_63d(close: pd.Series) -> pd.Series:
    """Ratio of current 252d-drawdown to its 63-day minimum (recovery-from-worst)."""
    dd     = _dd_from_rolling_high(close, _TD_YEAR)
    max_dd = _rolling_min(dd, _TD_QTR)
    return _safe_div(dd, max_dd)


def dd_ext_047_current_vs_max_dd_126d(close: pd.Series) -> pd.Series:
    """Ratio of current 252d-drawdown to its 126-day minimum."""
    dd     = _dd_from_rolling_high(close, _TD_YEAR)
    max_dd = _rolling_min(dd, _TD_HALF)
    return _safe_div(dd, max_dd)


# ── Group H (048-056): Drawdown from Open / High / Typical-Price Anchors ──────

def dd_ext_048_dd_from_252d_open_high(open: pd.Series) -> pd.Series:
    """Drawdown of open price from 252-day rolling high of open prices."""
    h = _rolling_max(open, _TD_YEAR)
    return _safe_div(open - h, h)


def dd_ext_049_dd_from_504d_open_high(open: pd.Series) -> pd.Series:
    """Drawdown of open price from 504-day rolling high of open prices."""
    h = _rolling_max(open, 504)
    return _safe_div(open - h, h)


def dd_ext_050_dd_from_252d_intraday_high_anchor(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close drawdown from 252-day rolling max of intraday highs (worst intraday anchor)."""
    h = _rolling_max(high, _TD_YEAR)
    return _safe_div(close - h, h)


def dd_ext_051_dd_from_504d_intraday_high_anchor(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close drawdown from 504-day rolling max of intraday highs."""
    h = _rolling_max(high, 504)
    return _safe_div(close - h, h)


def dd_ext_052_dd_typical_from_252d_typical_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Typical price (H+L+C)/3 drawdown from 252-day rolling high of typical price."""
    typical = (high + low + close) / 3.0
    h = _rolling_max(typical, _TD_YEAR)
    return _safe_div(typical - h, h)


def dd_ext_053_dd_typical_from_504d_typical_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Typical price drawdown from 504-day rolling high of typical price."""
    typical = (high + low + close) / 3.0
    h = _rolling_max(typical, 504)
    return _safe_div(typical - h, h)


def dd_ext_054_dd_typical_from_ath_typical(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Typical price drawdown from all-time high of typical price."""
    typical = (high + low + close) / 3.0
    h = typical.expanding(min_periods=1).max()
    return _safe_div(typical - h, h)


def dd_ext_055_dd_midpoint_from_252d_midpoint_high(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily midpoint (H+L)/2 drawdown from 252-day rolling high of midpoints."""
    mid = (high + low) / 2.0
    h = _rolling_max(mid, _TD_YEAR)
    return _safe_div(mid - h, h)


def dd_ext_056_log_dd_from_252d_open_high(open: pd.Series) -> pd.Series:
    """Log-space drawdown of open from 252-day rolling high of open prices."""
    h = _rolling_max(open, _TD_YEAR)
    return _log_safe(open) - _log_safe(h)


# ── Group I (057-063): Log-Drawdown Variants ──────────────────────────────────

def dd_ext_057_log_dd_from_126d_high(close: pd.Series) -> pd.Series:
    """Log-space drawdown of close from 126-day rolling close high."""
    h = _rolling_max(close, _TD_HALF)
    return _log_safe(close) - _log_safe(h)


def dd_ext_058_log_dd_from_63d_high(close: pd.Series) -> pd.Series:
    """Log-space drawdown of close from 63-day rolling close high."""
    h = _rolling_max(close, _TD_QTR)
    return _log_safe(close) - _log_safe(h)


def dd_ext_059_log_dd_from_504d_high(close: pd.Series) -> pd.Series:
    """Log-space drawdown of close from 504-day rolling close high (negative)."""
    h = _rolling_max(close, 504)
    return _log_safe(close) - _log_safe(h)


def dd_ext_060_log_dd_typical_from_252d_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log-space drawdown of typical price from 252-day typical-price high."""
    typical = (high + low + close) / 3.0
    h = _rolling_max(typical, _TD_YEAR)
    return _log_safe(typical) - _log_safe(h)


def dd_ext_061_log_dd_abs_252d(close: pd.Series) -> pd.Series:
    """Absolute (positive) log-distance of close below 252-day rolling high."""
    h = _rolling_max(close, _TD_YEAR)
    return (_log_safe(h) - _log_safe(close)).clip(lower=0.0)


def dd_ext_062_log_dd_abs_ath(close: pd.Series) -> pd.Series:
    """Absolute (positive) log-distance of close below all-time high."""
    h = close.expanding(min_periods=1).max()
    return (_log_safe(h) - _log_safe(close)).clip(lower=0.0)


# ── Group J (063-069): Drawdown Depth Z-scores at More Windows ────────────────

def dd_ext_063_dd_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 252d-drawdown over trailing 63-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _zscore_rolling(dd, _TD_QTR)


def dd_ext_064_dd_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 252d-drawdown over trailing 126-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    return _zscore_rolling(dd, _TD_HALF)


def dd_ext_065_ath_dd_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of ATH-drawdown over trailing 126-day window."""
    h  = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return _zscore_rolling(dd, _TD_HALF)


def dd_ext_066_ath_dd_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of ATH-drawdown over trailing 504-day window."""
    h  = close.expanding(min_periods=1).max()
    dd = _safe_div(close - h, h)
    return _zscore_rolling(dd, 504)


def dd_ext_067_log_dd_ath_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of log-ATH-drawdown magnitude over trailing 252-day window."""
    h  = close.expanding(min_periods=1).max()
    log_dd_abs = (_log_safe(h) - _log_safe(close)).clip(lower=0.0)
    return _zscore_rolling(log_dd_abs, _TD_YEAR)


def dd_ext_068_log_dd_252d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of log-252d-drawdown magnitude over trailing 504-day window."""
    h  = _rolling_max(close, _TD_YEAR)
    log_dd_abs = (_log_safe(h) - _log_safe(close)).clip(lower=0.0)
    return _zscore_rolling(log_dd_abs, 504)


def dd_ext_069_cdar_10pct_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the CDaR-10%/252d series over its own trailing 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    cdar = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.10), raw=True)
    return _zscore_rolling(cdar, _TD_YEAR)


# ── Group K (070-075): Rate-of-Change of Extended Features ────────────────────

def dd_ext_070_cdar_5pct_252d_5d_roc(close: pd.Series) -> pd.Series:
    """5-day diff of CDaR-5%/252d (rate of change of tail-drawdown risk)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    cdar = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_mean_worst_pct(x, 0.05), raw=True)
    return cdar.diff(5)


def dd_ext_071_dd_downside_dev_252d_5d_roc(close: pd.Series) -> pd.Series:
    """5-day diff of 252d downside drawdown deviation (pace of deviation change)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    dev = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda x: _scalar_downside_std(x, threshold=0.0), raw=True)
    return dev.diff(5)


def dd_ext_072_burke_sqrt_sum_sq_dd_252d_5d_roc(close: pd.Series) -> pd.Series:
    """5-day diff of Burke denominator (sqrt-sum-sq-dd) over 252-day window."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    burke = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _scalar_sqrt_sum_sq, raw=True)
    return burke.diff(5)


def dd_ext_073_dd_skew_126d_5d_roc(close: pd.Series) -> pd.Series:
    """5-day diff of 126-day drawdown skewness (changing tail asymmetry)."""
    dd = _dd_from_rolling_high(close, _TD_YEAR)
    skew_s = dd.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _scalar_skew, raw=True)
    return skew_s.diff(5)


def dd_ext_074_dd_typical_252d_5d_roc(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of typical-price 252d-drawdown (rate of typical-price distress change)."""
    typical = (high + low + close) / 3.0
    h = _rolling_max(typical, _TD_YEAR)
    dd_typ = _safe_div(typical - h, h)
    return dd_typ.diff(5)


def dd_ext_075_dd_std_252d_5d_roc(close: pd.Series) -> pd.Series:
    """5-day diff of 252d drawdown std (pace of drawdown-volatility change)."""
    dd  = _dd_from_rolling_high(close, _TD_YEAR)
    std = _rolling_std(dd, _TD_YEAR)
    return std.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DEPTH_EXTENDED_REGISTRY_001_075 = {
    "dd_ext_001_cdar_5pct_126d":                    {"inputs": ["close"],              "func": dd_ext_001_cdar_5pct_126d},
    "dd_ext_002_cdar_5pct_252d":                    {"inputs": ["close"],              "func": dd_ext_002_cdar_5pct_252d},
    "dd_ext_003_cdar_5pct_504d":                    {"inputs": ["close"],              "func": dd_ext_003_cdar_5pct_504d},
    "dd_ext_004_cdar_10pct_126d":                   {"inputs": ["close"],              "func": dd_ext_004_cdar_10pct_126d},
    "dd_ext_005_cdar_10pct_252d":                   {"inputs": ["close"],              "func": dd_ext_005_cdar_10pct_252d},
    "dd_ext_006_cdar_10pct_504d":                   {"inputs": ["close"],              "func": dd_ext_006_cdar_10pct_504d},
    "dd_ext_007_cdar_20pct_126d":                   {"inputs": ["close"],              "func": dd_ext_007_cdar_20pct_126d},
    "dd_ext_008_cdar_20pct_252d":                   {"inputs": ["close"],              "func": dd_ext_008_cdar_20pct_252d},
    "dd_ext_009_cdar_20pct_504d":                   {"inputs": ["close"],              "func": dd_ext_009_cdar_20pct_504d},
    "dd_ext_010_dd_var_q01_252d":                   {"inputs": ["close"],              "func": dd_ext_010_dd_var_q01_252d},
    "dd_ext_011_dd_var_q05_504d":                   {"inputs": ["close"],              "func": dd_ext_011_dd_var_q05_504d},
    "dd_ext_012_dd_var_q10_252d":                   {"inputs": ["close"],              "func": dd_ext_012_dd_var_q10_252d},
    "dd_ext_013_dd_std_63d":                        {"inputs": ["close"],              "func": dd_ext_013_dd_std_63d},
    "dd_ext_014_dd_std_126d":                       {"inputs": ["close"],              "func": dd_ext_014_dd_std_126d},
    "dd_ext_015_dd_std_504d":                       {"inputs": ["close"],              "func": dd_ext_015_dd_std_504d},
    "dd_ext_016_dd_downside_dev_63d":               {"inputs": ["close"],              "func": dd_ext_016_dd_downside_dev_63d},
    "dd_ext_017_dd_downside_dev_126d":              {"inputs": ["close"],              "func": dd_ext_017_dd_downside_dev_126d},
    "dd_ext_018_dd_downside_dev_252d":              {"inputs": ["close"],              "func": dd_ext_018_dd_downside_dev_252d},
    "dd_ext_019_dd_std_ratio_63d_to_252d":          {"inputs": ["close"],              "func": dd_ext_019_dd_std_ratio_63d_to_252d},
    "dd_ext_020_dd_downside_dev_ath_126d":          {"inputs": ["close"],              "func": dd_ext_020_dd_downside_dev_ath_126d},
    "dd_ext_021_dd_std_normalized_by_mean_252d":    {"inputs": ["close"],              "func": dd_ext_021_dd_std_normalized_by_mean_252d},
    "dd_ext_022_avg_worst_5_dd_252d":               {"inputs": ["close"],              "func": dd_ext_022_avg_worst_5_dd_252d},
    "dd_ext_023_avg_worst_10_dd_252d":              {"inputs": ["close"],              "func": dd_ext_023_avg_worst_10_dd_252d},
    "dd_ext_024_avg_worst_5_dd_126d":               {"inputs": ["close"],              "func": dd_ext_024_avg_worst_5_dd_126d},
    "dd_ext_025_avg_worst_3_dd_63d":                {"inputs": ["close"],              "func": dd_ext_025_avg_worst_3_dd_63d},
    "dd_ext_026_avg_worst_20_dd_504d":              {"inputs": ["close"],              "func": dd_ext_026_avg_worst_20_dd_504d},
    "dd_ext_027_burke_sqrt_sum_sq_dd_126d":         {"inputs": ["close"],              "func": dd_ext_027_burke_sqrt_sum_sq_dd_126d},
    "dd_ext_028_burke_sqrt_sum_sq_dd_252d":         {"inputs": ["close"],              "func": dd_ext_028_burke_sqrt_sum_sq_dd_252d},
    "dd_ext_029_burke_sqrt_sum_sq_dd_504d":         {"inputs": ["close"],              "func": dd_ext_029_burke_sqrt_sum_sq_dd_504d},
    "dd_ext_030_burke_ratio_252d":                  {"inputs": ["close"],              "func": dd_ext_030_burke_ratio_252d},
    "dd_ext_031_burke_ratio_126d":                  {"inputs": ["close"],              "func": dd_ext_031_burke_ratio_126d},
    "dd_ext_032_dd_skew_126d":                      {"inputs": ["close"],              "func": dd_ext_032_dd_skew_126d},
    "dd_ext_033_dd_skew_504d":                      {"inputs": ["close"],              "func": dd_ext_033_dd_skew_504d},
    "dd_ext_034_dd_kurtosis_126d":                  {"inputs": ["close"],              "func": dd_ext_034_dd_kurtosis_126d},
    "dd_ext_035_dd_kurtosis_504d":                  {"inputs": ["close"],              "func": dd_ext_035_dd_kurtosis_504d},
    "dd_ext_036_dd_skew_expanding":                 {"inputs": ["close"],              "func": dd_ext_036_dd_skew_expanding},
    "dd_ext_037_dd_kurtosis_expanding":             {"inputs": ["close"],              "func": dd_ext_037_dd_kurtosis_expanding},
    "dd_ext_038_dd_pct_rank_63d":                   {"inputs": ["close"],              "func": dd_ext_038_dd_pct_rank_63d},
    "dd_ext_039_dd_pct_rank_126d":                  {"inputs": ["close"],              "func": dd_ext_039_dd_pct_rank_126d},
    "dd_ext_040_dd_pct_rank_504d":                  {"inputs": ["close"],              "func": dd_ext_040_dd_pct_rank_504d},
    "dd_ext_041_ath_dd_pct_rank_504d":              {"inputs": ["close"],              "func": dd_ext_041_ath_dd_pct_rank_504d},
    "dd_ext_042_dd_pct_rank_21d":                   {"inputs": ["close"],              "func": dd_ext_042_dd_pct_rank_21d},
    "dd_ext_043_max_dd_in_63d_window":              {"inputs": ["close"],              "func": dd_ext_043_max_dd_in_63d_window},
    "dd_ext_044_max_dd_in_126d_window":             {"inputs": ["close"],              "func": dd_ext_044_max_dd_in_126d_window},
    "dd_ext_045_max_dd_in_504d_window":             {"inputs": ["close"],              "func": dd_ext_045_max_dd_in_504d_window},
    "dd_ext_046_current_vs_max_dd_63d":             {"inputs": ["close"],              "func": dd_ext_046_current_vs_max_dd_63d},
    "dd_ext_047_current_vs_max_dd_126d":            {"inputs": ["close"],              "func": dd_ext_047_current_vs_max_dd_126d},
    "dd_ext_048_dd_from_252d_open_high":            {"inputs": ["open"],               "func": dd_ext_048_dd_from_252d_open_high},
    "dd_ext_049_dd_from_504d_open_high":            {"inputs": ["open"],               "func": dd_ext_049_dd_from_504d_open_high},
    "dd_ext_050_dd_from_252d_intraday_high_anchor": {"inputs": ["close", "high"],      "func": dd_ext_050_dd_from_252d_intraday_high_anchor},
    "dd_ext_051_dd_from_504d_intraday_high_anchor": {"inputs": ["close", "high"],      "func": dd_ext_051_dd_from_504d_intraday_high_anchor},
    "dd_ext_052_dd_typical_from_252d_typical_high": {"inputs": ["close", "high", "low"], "func": dd_ext_052_dd_typical_from_252d_typical_high},
    "dd_ext_053_dd_typical_from_504d_typical_high": {"inputs": ["close", "high", "low"], "func": dd_ext_053_dd_typical_from_504d_typical_high},
    "dd_ext_054_dd_typical_from_ath_typical":       {"inputs": ["close", "high", "low"], "func": dd_ext_054_dd_typical_from_ath_typical},
    "dd_ext_055_dd_midpoint_from_252d_midpoint_high": {"inputs": ["high", "low"],      "func": dd_ext_055_dd_midpoint_from_252d_midpoint_high},
    "dd_ext_056_log_dd_from_252d_open_high":        {"inputs": ["open"],               "func": dd_ext_056_log_dd_from_252d_open_high},
    "dd_ext_057_log_dd_from_126d_high":             {"inputs": ["close"],              "func": dd_ext_057_log_dd_from_126d_high},
    "dd_ext_058_log_dd_from_63d_high":              {"inputs": ["close"],              "func": dd_ext_058_log_dd_from_63d_high},
    "dd_ext_059_log_dd_from_504d_high":             {"inputs": ["close"],              "func": dd_ext_059_log_dd_from_504d_high},
    "dd_ext_060_log_dd_typical_from_252d_high":     {"inputs": ["close", "high", "low"], "func": dd_ext_060_log_dd_typical_from_252d_high},
    "dd_ext_061_log_dd_abs_252d":                   {"inputs": ["close"],              "func": dd_ext_061_log_dd_abs_252d},
    "dd_ext_062_log_dd_abs_ath":                    {"inputs": ["close"],              "func": dd_ext_062_log_dd_abs_ath},
    "dd_ext_063_dd_zscore_63d":                     {"inputs": ["close"],              "func": dd_ext_063_dd_zscore_63d},
    "dd_ext_064_dd_zscore_126d":                    {"inputs": ["close"],              "func": dd_ext_064_dd_zscore_126d},
    "dd_ext_065_ath_dd_zscore_126d":                {"inputs": ["close"],              "func": dd_ext_065_ath_dd_zscore_126d},
    "dd_ext_066_ath_dd_zscore_504d":                {"inputs": ["close"],              "func": dd_ext_066_ath_dd_zscore_504d},
    "dd_ext_067_log_dd_ath_zscore_252d":            {"inputs": ["close"],              "func": dd_ext_067_log_dd_ath_zscore_252d},
    "dd_ext_068_log_dd_252d_zscore_504d":           {"inputs": ["close"],              "func": dd_ext_068_log_dd_252d_zscore_504d},
    "dd_ext_069_cdar_10pct_zscore_252d":            {"inputs": ["close"],              "func": dd_ext_069_cdar_10pct_zscore_252d},
    "dd_ext_070_cdar_5pct_252d_5d_roc":             {"inputs": ["close"],              "func": dd_ext_070_cdar_5pct_252d_5d_roc},
    "dd_ext_071_dd_downside_dev_252d_5d_roc":       {"inputs": ["close"],              "func": dd_ext_071_dd_downside_dev_252d_5d_roc},
    "dd_ext_072_burke_sqrt_sum_sq_dd_252d_5d_roc":  {"inputs": ["close"],              "func": dd_ext_072_burke_sqrt_sum_sq_dd_252d_5d_roc},
    "dd_ext_073_dd_skew_126d_5d_roc":               {"inputs": ["close"],              "func": dd_ext_073_dd_skew_126d_5d_roc},
    "dd_ext_074_dd_typical_252d_5d_roc":            {"inputs": ["close", "high", "low"], "func": dd_ext_074_dd_typical_252d_5d_roc},
    "dd_ext_075_dd_std_252d_5d_roc":                {"inputs": ["close"],              "func": dd_ext_075_dd_std_252d_5d_roc},
}
