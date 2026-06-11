"""
25_momentum_decay — Base Features 001-075
Domain: trailing-return decay across horizons — momentum decay / cross-horizon return term structure
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


def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    """Log return over n periods."""
    return np.log(s.clip(lower=_EPS)) - np.log(s.shift(n).clip(lower=_EPS))


def _pct_ret(s: pd.Series, n: int) -> pd.Series:
    return s.pct_change(n)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw trailing returns at canonical horizons ---

def mdc_001_ret_5d(close: pd.Series) -> pd.Series:
    """5-day trailing log return (1-week momentum)."""
    return _log_ret(close, _TD_WEEK)


def mdc_002_ret_21d(close: pd.Series) -> pd.Series:
    """21-day trailing log return (1-month momentum)."""
    return _log_ret(close, _TD_MON)


def mdc_003_ret_63d(close: pd.Series) -> pd.Series:
    """63-day trailing log return (1-quarter momentum)."""
    return _log_ret(close, _TD_QTR)


def mdc_004_ret_126d(close: pd.Series) -> pd.Series:
    """126-day trailing log return (half-year momentum)."""
    return _log_ret(close, _TD_HALF)


def mdc_005_ret_252d(close: pd.Series) -> pd.Series:
    """252-day trailing log return (1-year momentum)."""
    return _log_ret(close, _TD_YEAR)


def mdc_006_ret_10d(close: pd.Series) -> pd.Series:
    """10-day trailing log return (2-week momentum)."""
    return _log_ret(close, 10)


def mdc_007_ret_42d(close: pd.Series) -> pd.Series:
    """42-day trailing log return (2-month momentum)."""
    return _log_ret(close, 42)


def mdc_008_ret_189d(close: pd.Series) -> pd.Series:
    """189-day trailing log return (3-quarter momentum)."""
    return _log_ret(close, 189)


def mdc_009_ret_5d_pct(close: pd.Series) -> pd.Series:
    """5-day simple percent return."""
    return _pct_ret(close, _TD_WEEK)


def mdc_010_ret_252d_pct(close: pd.Series) -> pd.Series:
    """252-day simple percent return (annual price change)."""
    return _pct_ret(close, _TD_YEAR)


# --- Group B (011-020): Short-minus-long return spreads (term structure decay) ---

def mdc_011_ret_5d_minus_21d(close: pd.Series) -> pd.Series:
    """5d return minus 21d return: positive = recent acceleration, negative = decay."""
    return _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)


def mdc_012_ret_21d_minus_63d(close: pd.Series) -> pd.Series:
    """21d return minus 63d return: decay of 1-month vs quarter momentum."""
    return _log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)


def mdc_013_ret_63d_minus_126d(close: pd.Series) -> pd.Series:
    """63d return minus 126d return: decay of quarterly vs half-year momentum."""
    return _log_ret(close, _TD_QTR) - _log_ret(close, _TD_HALF)


def mdc_014_ret_126d_minus_252d(close: pd.Series) -> pd.Series:
    """126d return minus 252d return: decay of half-year vs annual momentum."""
    return _log_ret(close, _TD_HALF) - _log_ret(close, _TD_YEAR)


def mdc_015_ret_5d_minus_63d(close: pd.Series) -> pd.Series:
    """5d return minus 63d return: short vs quarter-horizon spread."""
    return _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_QTR)


def mdc_016_ret_5d_minus_252d(close: pd.Series) -> pd.Series:
    """5d return minus 252d return: very-short vs annual spread (extreme decay signal)."""
    return _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_YEAR)


def mdc_017_ret_21d_minus_252d(close: pd.Series) -> pd.Series:
    """21d return minus 252d return: monthly vs annual momentum spread."""
    return _log_ret(close, _TD_MON) - _log_ret(close, _TD_YEAR)


def mdc_018_ret_63d_minus_252d(close: pd.Series) -> pd.Series:
    """63d return minus 252d return: quarterly vs annual momentum spread."""
    return _log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR)


def mdc_019_ret_10d_minus_126d(close: pd.Series) -> pd.Series:
    """10d return minus 126d return: 2-week vs half-year momentum spread."""
    return _log_ret(close, 10) - _log_ret(close, _TD_HALF)


def mdc_020_ret_42d_minus_189d(close: pd.Series) -> pd.Series:
    """42d return minus 189d return: 2-month vs 9-month spread."""
    return _log_ret(close, 42) - _log_ret(close, 189)


# --- Group C (021-030): Ratio of recent to older return (decay ratio) ---

def mdc_021_ret_5d_over_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5d return to 21d return; <1 means recent period weaker."""
    return _safe_div(_log_ret(close, _TD_WEEK), _log_ret(close, _TD_MON).abs() + _EPS)


def mdc_022_ret_21d_over_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21d return to 63d return magnitude."""
    return _safe_div(_log_ret(close, _TD_MON), _log_ret(close, _TD_QTR).abs() + _EPS)


def mdc_023_ret_63d_over_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d return to 252d return magnitude."""
    return _safe_div(_log_ret(close, _TD_QTR), _log_ret(close, _TD_YEAR).abs() + _EPS)


def mdc_024_ret_5d_over_126d(close: pd.Series) -> pd.Series:
    """Ratio of 5d return to 126d return magnitude."""
    return _safe_div(_log_ret(close, _TD_WEEK), _log_ret(close, _TD_HALF).abs() + _EPS)


def mdc_025_ret_126d_over_252d(close: pd.Series) -> pd.Series:
    """Ratio of 126d to 252d return; below 0.5 signals back-half underperformance."""
    return _safe_div(_log_ret(close, _TD_HALF), _log_ret(close, _TD_YEAR).abs() + _EPS)


def mdc_026_ret_21d_over_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d to 252d return; extreme negative = recent month worst period."""
    return _safe_div(_log_ret(close, _TD_MON), _log_ret(close, _TD_YEAR).abs() + _EPS)


def mdc_027_ret_first_half_252d(close: pd.Series) -> pd.Series:
    """Return over the first half of the trailing year (252-126d horizon)."""
    return _log_ret(close.shift(_TD_HALF), _TD_HALF)


def mdc_028_ret_second_half_252d(close: pd.Series) -> pd.Series:
    """Return over the second half of trailing year (most recent 126d)."""
    return _log_ret(close, _TD_HALF)


def mdc_029_second_half_minus_first_half_252d(close: pd.Series) -> pd.Series:
    """Difference: second-half vs first-half annual return (decay within the year)."""
    return mdc_028_ret_second_half_252d(close) - mdc_027_ret_first_half_252d(close)


def mdc_030_ret_recent_quarter_vs_prior_quarter(close: pd.Series) -> pd.Series:
    """Most-recent 63d return minus prior 63d return (63-126d horizon)."""
    recent = _log_ret(close, _TD_QTR)
    prior = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    return recent - prior


# --- Group D (031-040): Monotonic decay flags and slope of return term structure ---

def mdc_031_ret_term_structure_slope_5_252(close: pd.Series) -> pd.Series:
    """OLS slope of log-return on log(horizon) across 5/21/63/126/252d (term structure slope)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    horizons = np.log([_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR])
    horizons = horizons - horizons.mean()
    def ts_slope(row):
        vals = np.array(row, dtype=float)
        if np.any(np.isnan(vals)):
            return np.nan
        vals_m = vals.mean()
        num = (horizons * (vals - vals_m)).sum()
        den = (horizons ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    df = pd.concat([r5, r21, r63, r126, r252], axis=1)
    return df.apply(ts_slope, axis=1)


def mdc_032_ret_monotonic_decay_flag(close: pd.Series) -> pd.Series:
    """Flag: returns are monotonically weakening from 252d to 5d (full decay)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    # r252 > r126 > r63 > r21 > r5 means returns shrink as horizon shrinks
    flag = (r252 > r126) & (r126 > r63) & (r63 > r21) & (r21 > r5)
    return flag.astype(float)


def mdc_033_ret_monotonic_negative_all_horizons(close: pd.Series) -> pd.Series:
    """Flag: returns are negative at ALL five horizons (5/21/63/126/252d)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return ((r5 < 0) & (r21 < 0) & (r63 < 0) & (r126 < 0) & (r252 < 0)).astype(float)


def mdc_034_ret_negative_count_5horizons(close: pd.Series) -> pd.Series:
    """Count of negative returns across 5d/21d/63d/126d/252d horizons (0-5)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return ((r5 < 0).astype(float) + (r21 < 0).astype(float) +
            (r63 < 0).astype(float) + (r126 < 0).astype(float) +
            (r252 < 0).astype(float))


def mdc_035_ret_sign_flip_short_to_long(close: pd.Series) -> pd.Series:
    """Flag: short horizon (5d) negative AND long horizon (252d) positive (momentum lost)."""
    return ((mdc_001_ret_5d(close) < 0) & (mdc_005_ret_252d(close) > 0)).astype(float)


def mdc_036_ret_sign_flip_month_to_year(close: pd.Series) -> pd.Series:
    """Flag: 21d negative AND 252d positive (monthly decay from annual trend)."""
    return ((mdc_002_ret_21d(close) < 0) & (mdc_005_ret_252d(close) > 0)).astype(float)


def mdc_037_ret_sign_flip_quarter_to_year(close: pd.Series) -> pd.Series:
    """Flag: 63d negative AND 252d positive (quarterly decay from annual trend)."""
    return ((mdc_003_ret_63d(close) < 0) & (mdc_005_ret_252d(close) > 0)).astype(float)


def mdc_038_ret_sign_flip_half_to_year(close: pd.Series) -> pd.Series:
    """Flag: 126d negative AND 252d positive (half-year reversal within annual trend)."""
    return ((mdc_004_ret_126d(close) < 0) & (mdc_005_ret_252d(close) > 0)).astype(float)


def mdc_039_ret_all_short_neg_long_pos(close: pd.Series) -> pd.Series:
    """Flag: 5d AND 21d AND 63d all negative while 252d positive (deep decay)."""
    r5 = mdc_001_ret_5d(close)
    r21 = mdc_002_ret_21d(close)
    r63 = mdc_003_ret_63d(close)
    r252 = mdc_005_ret_252d(close)
    return ((r5 < 0) & (r21 < 0) & (r63 < 0) & (r252 > 0)).astype(float)


def mdc_040_ret_decay_acceleration_short(close: pd.Series) -> pd.Series:
    """(5d ret - 21d ret) / |21d ret|: relative decay acceleration at short end."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    return _safe_div(r5 - r21, r21.abs() + _EPS)


# --- Group E (041-050): Momentum half-life and decay speed measures ---

def mdc_041_momentum_halflife_proxy(close: pd.Series) -> pd.Series:
    """Ratio 126d/252d return: if <0.5, momentum halved in back half of year."""
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return _safe_div(r126, r252.replace(0, np.nan))


def mdc_042_momentum_quarter_contribution(close: pd.Series) -> pd.Series:
    """Fraction of annual return from last quarter: r63/r252."""
    return _safe_div(_log_ret(close, _TD_QTR), _log_ret(close, _TD_YEAR).replace(0, np.nan))


def mdc_043_momentum_month_contribution(close: pd.Series) -> pd.Series:
    """Fraction of annual return from last month: r21/r252."""
    return _safe_div(_log_ret(close, _TD_MON), _log_ret(close, _TD_YEAR).replace(0, np.nan))


def mdc_044_momentum_week_contribution(close: pd.Series) -> pd.Series:
    """Fraction of annual return from last week: r5/r252."""
    return _safe_div(_log_ret(close, _TD_WEEK), _log_ret(close, _TD_YEAR).replace(0, np.nan))


def mdc_045_return_decay_ratio_5_to_63(close: pd.Series) -> pd.Series:
    """5d return as fraction of 63d return (near-term contribution to quarter)."""
    return _safe_div(_log_ret(close, _TD_WEEK), _log_ret(close, _TD_QTR).replace(0, np.nan))


def mdc_046_annualized_ret_5d(close: pd.Series) -> pd.Series:
    """5d log return annualized to 252d (compares momentum run-rate to annual)."""
    return _log_ret(close, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)


def mdc_047_annualized_ret_21d(close: pd.Series) -> pd.Series:
    """21d log return annualized."""
    return _log_ret(close, _TD_MON) * (_TD_YEAR / _TD_MON)


def mdc_048_annualized_ret_63d(close: pd.Series) -> pd.Series:
    """63d log return annualized."""
    return _log_ret(close, _TD_QTR) * (_TD_YEAR / _TD_QTR)


def mdc_049_annualized_ret_126d(close: pd.Series) -> pd.Series:
    """126d log return annualized."""
    return _log_ret(close, _TD_HALF) * (_TD_YEAR / _TD_HALF)


def mdc_050_annualized_spread_5d_vs_252d(close: pd.Series) -> pd.Series:
    """Annualized 5d minus realized 252d: measures current run-rate vs annual."""
    return mdc_046_annualized_ret_5d(close) - _log_ret(close, _TD_YEAR)


# --- Group F (051-060): Rolling mean of multi-horizon returns (smoothed decay) ---

def mdc_051_rolling_mean_ret_5d_21d(close: pd.Series) -> pd.Series:
    """21-day rolling mean of 5d log returns (smoothed short-term momentum level)."""
    return _rolling_mean(_log_ret(close, _TD_WEEK), _TD_MON)


def mdc_052_rolling_mean_ret_5d_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of 5d log returns."""
    return _rolling_mean(_log_ret(close, _TD_WEEK), _TD_QTR)


def mdc_053_rolling_mean_ret_21d_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of 21d log returns (smoothed monthly momentum)."""
    return _rolling_mean(_log_ret(close, _TD_MON), _TD_QTR)


def mdc_054_rolling_mean_ret_21d_252d(close: pd.Series) -> pd.Series:
    """252-day rolling mean of 21d log returns."""
    return _rolling_mean(_log_ret(close, _TD_MON), _TD_YEAR)


def mdc_055_rolling_mean_ret_63d_252d(close: pd.Series) -> pd.Series:
    """252-day rolling mean of 63d log returns (long-run quarterly momentum)."""
    return _rolling_mean(_log_ret(close, _TD_QTR), _TD_YEAR)


def mdc_056_rolling_std_ret_5d_21d(close: pd.Series) -> pd.Series:
    """21-day rolling std of 5d returns (volatility of short-term momentum)."""
    return _rolling_std(_log_ret(close, _TD_WEEK), _TD_MON)


def mdc_057_rolling_std_ret_21d_63d(close: pd.Series) -> pd.Series:
    """63-day rolling std of 21d returns."""
    return _rolling_std(_log_ret(close, _TD_MON), _TD_QTR)


def mdc_058_rolling_min_ret_5d_63d(close: pd.Series) -> pd.Series:
    """63-day rolling minimum of 5d returns (worst short-term momentum in quarter)."""
    return _rolling_min(_log_ret(close, _TD_WEEK), _TD_QTR)


def mdc_059_rolling_min_ret_21d_252d(close: pd.Series) -> pd.Series:
    """252-day rolling minimum of 21d returns (worst monthly momentum in year)."""
    return _rolling_min(_log_ret(close, _TD_MON), _TD_YEAR)


def mdc_060_rolling_min_ret_63d_252d(close: pd.Series) -> pd.Series:
    """252-day rolling minimum of 63d returns (worst quarterly momentum in year)."""
    return _rolling_min(_log_ret(close, _TD_QTR), _TD_YEAR)


# --- Group G (061-075): Z-scores, ranks, and normalized decay measures ---

def mdc_061_ret_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 5d return vs trailing 252-day distribution of 5d returns."""
    r = _log_ret(close, _TD_WEEK)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def mdc_062_ret_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 21d return vs trailing 252-day distribution."""
    r = _log_ret(close, _TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def mdc_063_ret_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 63d return vs trailing 252-day distribution."""
    r = _log_ret(close, _TD_QTR)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def mdc_064_ret_126d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 126d return vs trailing 252-day distribution."""
    r = _log_ret(close, _TD_HALF)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def mdc_065_ret_5d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5d return within trailing 252-day distribution."""
    return _log_ret(close, _TD_WEEK).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_066_ret_21d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21d return within trailing 252-day distribution."""
    return _log_ret(close, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_067_ret_63d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 63d return within trailing 252-day distribution."""
    return _log_ret(close, _TD_QTR).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_068_spread_5_21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5d-minus-21d spread vs its 252-day distribution."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)
    m = _rolling_mean(spread, _TD_YEAR)
    s = _rolling_std(spread, _TD_YEAR)
    return _safe_div(spread - m, s)


def mdc_069_spread_21_63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d-minus-63d spread vs its 252-day distribution."""
    spread = _log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)
    m = _rolling_mean(spread, _TD_YEAR)
    s = _rolling_std(spread, _TD_YEAR)
    return _safe_div(spread - m, s)


def mdc_070_spread_63_252_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d-minus-252d spread vs its 252-day distribution."""
    spread = _log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR)
    m = _rolling_mean(spread, _TD_YEAR)
    s = _rolling_std(spread, _TD_YEAR)
    return _safe_div(spread - m, s)


def mdc_071_ret_5d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding-window z-score of 5d return (extremity vs full history)."""
    r = _log_ret(close, _TD_WEEK)
    m = r.expanding(min_periods=_TD_MON).mean()
    s = r.expanding(min_periods=_TD_MON).std()
    return _safe_div(r - m, s)


def mdc_072_ret_21d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding-window z-score of 21d return."""
    r = _log_ret(close, _TD_MON)
    m = r.expanding(min_periods=_TD_QTR).mean()
    s = r.expanding(min_periods=_TD_QTR).std()
    return _safe_div(r - m, s)


def mdc_073_ret_63d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding-window z-score of 63d return."""
    r = _log_ret(close, _TD_QTR)
    m = r.expanding(min_periods=_TD_HALF).mean()
    s = r.expanding(min_periods=_TD_HALF).std()
    return _safe_div(r - m, s)


def mdc_074_decay_composite_score(close: pd.Series) -> pd.Series:
    """Composite decay: avg z-score of 5d, 21d, 63d returns (all below normal = capitulation)."""
    z5 = mdc_061_ret_5d_zscore_252d(close)
    z21 = mdc_062_ret_21d_zscore_252d(close)
    z63 = mdc_063_ret_63d_zscore_252d(close)
    return (z5 + z21 + z63) / 3.0


def mdc_075_ret_252d_expanding_pctrank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d return (all-time worst annual periods)."""
    return _log_ret(close, _TD_YEAR).expanding(min_periods=_TD_YEAR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DECAY_REGISTRY_001_075 = {
    "mdc_001_ret_5d": {"inputs": ["close"], "func": mdc_001_ret_5d},
    "mdc_002_ret_21d": {"inputs": ["close"], "func": mdc_002_ret_21d},
    "mdc_003_ret_63d": {"inputs": ["close"], "func": mdc_003_ret_63d},
    "mdc_004_ret_126d": {"inputs": ["close"], "func": mdc_004_ret_126d},
    "mdc_005_ret_252d": {"inputs": ["close"], "func": mdc_005_ret_252d},
    "mdc_006_ret_10d": {"inputs": ["close"], "func": mdc_006_ret_10d},
    "mdc_007_ret_42d": {"inputs": ["close"], "func": mdc_007_ret_42d},
    "mdc_008_ret_189d": {"inputs": ["close"], "func": mdc_008_ret_189d},
    "mdc_009_ret_5d_pct": {"inputs": ["close"], "func": mdc_009_ret_5d_pct},
    "mdc_010_ret_252d_pct": {"inputs": ["close"], "func": mdc_010_ret_252d_pct},
    "mdc_011_ret_5d_minus_21d": {"inputs": ["close"], "func": mdc_011_ret_5d_minus_21d},
    "mdc_012_ret_21d_minus_63d": {"inputs": ["close"], "func": mdc_012_ret_21d_minus_63d},
    "mdc_013_ret_63d_minus_126d": {"inputs": ["close"], "func": mdc_013_ret_63d_minus_126d},
    "mdc_014_ret_126d_minus_252d": {"inputs": ["close"], "func": mdc_014_ret_126d_minus_252d},
    "mdc_015_ret_5d_minus_63d": {"inputs": ["close"], "func": mdc_015_ret_5d_minus_63d},
    "mdc_016_ret_5d_minus_252d": {"inputs": ["close"], "func": mdc_016_ret_5d_minus_252d},
    "mdc_017_ret_21d_minus_252d": {"inputs": ["close"], "func": mdc_017_ret_21d_minus_252d},
    "mdc_018_ret_63d_minus_252d": {"inputs": ["close"], "func": mdc_018_ret_63d_minus_252d},
    "mdc_019_ret_10d_minus_126d": {"inputs": ["close"], "func": mdc_019_ret_10d_minus_126d},
    "mdc_020_ret_42d_minus_189d": {"inputs": ["close"], "func": mdc_020_ret_42d_minus_189d},
    "mdc_021_ret_5d_over_21d": {"inputs": ["close"], "func": mdc_021_ret_5d_over_21d},
    "mdc_022_ret_21d_over_63d": {"inputs": ["close"], "func": mdc_022_ret_21d_over_63d},
    "mdc_023_ret_63d_over_252d": {"inputs": ["close"], "func": mdc_023_ret_63d_over_252d},
    "mdc_024_ret_5d_over_126d": {"inputs": ["close"], "func": mdc_024_ret_5d_over_126d},
    "mdc_025_ret_126d_over_252d": {"inputs": ["close"], "func": mdc_025_ret_126d_over_252d},
    "mdc_026_ret_21d_over_252d": {"inputs": ["close"], "func": mdc_026_ret_21d_over_252d},
    "mdc_027_ret_first_half_252d": {"inputs": ["close"], "func": mdc_027_ret_first_half_252d},
    "mdc_028_ret_second_half_252d": {"inputs": ["close"], "func": mdc_028_ret_second_half_252d},
    "mdc_029_second_half_minus_first_half_252d": {"inputs": ["close"], "func": mdc_029_second_half_minus_first_half_252d},
    "mdc_030_ret_recent_quarter_vs_prior_quarter": {"inputs": ["close"], "func": mdc_030_ret_recent_quarter_vs_prior_quarter},
    "mdc_031_ret_term_structure_slope_5_252": {"inputs": ["close"], "func": mdc_031_ret_term_structure_slope_5_252},
    "mdc_032_ret_monotonic_decay_flag": {"inputs": ["close"], "func": mdc_032_ret_monotonic_decay_flag},
    "mdc_033_ret_monotonic_negative_all_horizons": {"inputs": ["close"], "func": mdc_033_ret_monotonic_negative_all_horizons},
    "mdc_034_ret_negative_count_5horizons": {"inputs": ["close"], "func": mdc_034_ret_negative_count_5horizons},
    "mdc_035_ret_sign_flip_short_to_long": {"inputs": ["close"], "func": mdc_035_ret_sign_flip_short_to_long},
    "mdc_036_ret_sign_flip_month_to_year": {"inputs": ["close"], "func": mdc_036_ret_sign_flip_month_to_year},
    "mdc_037_ret_sign_flip_quarter_to_year": {"inputs": ["close"], "func": mdc_037_ret_sign_flip_quarter_to_year},
    "mdc_038_ret_sign_flip_half_to_year": {"inputs": ["close"], "func": mdc_038_ret_sign_flip_half_to_year},
    "mdc_039_ret_all_short_neg_long_pos": {"inputs": ["close"], "func": mdc_039_ret_all_short_neg_long_pos},
    "mdc_040_ret_decay_acceleration_short": {"inputs": ["close"], "func": mdc_040_ret_decay_acceleration_short},
    "mdc_041_momentum_halflife_proxy": {"inputs": ["close"], "func": mdc_041_momentum_halflife_proxy},
    "mdc_042_momentum_quarter_contribution": {"inputs": ["close"], "func": mdc_042_momentum_quarter_contribution},
    "mdc_043_momentum_month_contribution": {"inputs": ["close"], "func": mdc_043_momentum_month_contribution},
    "mdc_044_momentum_week_contribution": {"inputs": ["close"], "func": mdc_044_momentum_week_contribution},
    "mdc_045_return_decay_ratio_5_to_63": {"inputs": ["close"], "func": mdc_045_return_decay_ratio_5_to_63},
    "mdc_046_annualized_ret_5d": {"inputs": ["close"], "func": mdc_046_annualized_ret_5d},
    "mdc_047_annualized_ret_21d": {"inputs": ["close"], "func": mdc_047_annualized_ret_21d},
    "mdc_048_annualized_ret_63d": {"inputs": ["close"], "func": mdc_048_annualized_ret_63d},
    "mdc_049_annualized_ret_126d": {"inputs": ["close"], "func": mdc_049_annualized_ret_126d},
    "mdc_050_annualized_spread_5d_vs_252d": {"inputs": ["close"], "func": mdc_050_annualized_spread_5d_vs_252d},
    "mdc_051_rolling_mean_ret_5d_21d": {"inputs": ["close"], "func": mdc_051_rolling_mean_ret_5d_21d},
    "mdc_052_rolling_mean_ret_5d_63d": {"inputs": ["close"], "func": mdc_052_rolling_mean_ret_5d_63d},
    "mdc_053_rolling_mean_ret_21d_63d": {"inputs": ["close"], "func": mdc_053_rolling_mean_ret_21d_63d},
    "mdc_054_rolling_mean_ret_21d_252d": {"inputs": ["close"], "func": mdc_054_rolling_mean_ret_21d_252d},
    "mdc_055_rolling_mean_ret_63d_252d": {"inputs": ["close"], "func": mdc_055_rolling_mean_ret_63d_252d},
    "mdc_056_rolling_std_ret_5d_21d": {"inputs": ["close"], "func": mdc_056_rolling_std_ret_5d_21d},
    "mdc_057_rolling_std_ret_21d_63d": {"inputs": ["close"], "func": mdc_057_rolling_std_ret_21d_63d},
    "mdc_058_rolling_min_ret_5d_63d": {"inputs": ["close"], "func": mdc_058_rolling_min_ret_5d_63d},
    "mdc_059_rolling_min_ret_21d_252d": {"inputs": ["close"], "func": mdc_059_rolling_min_ret_21d_252d},
    "mdc_060_rolling_min_ret_63d_252d": {"inputs": ["close"], "func": mdc_060_rolling_min_ret_63d_252d},
    "mdc_061_ret_5d_zscore_252d": {"inputs": ["close"], "func": mdc_061_ret_5d_zscore_252d},
    "mdc_062_ret_21d_zscore_252d": {"inputs": ["close"], "func": mdc_062_ret_21d_zscore_252d},
    "mdc_063_ret_63d_zscore_252d": {"inputs": ["close"], "func": mdc_063_ret_63d_zscore_252d},
    "mdc_064_ret_126d_zscore_252d": {"inputs": ["close"], "func": mdc_064_ret_126d_zscore_252d},
    "mdc_065_ret_5d_pctrank_252d": {"inputs": ["close"], "func": mdc_065_ret_5d_pctrank_252d},
    "mdc_066_ret_21d_pctrank_252d": {"inputs": ["close"], "func": mdc_066_ret_21d_pctrank_252d},
    "mdc_067_ret_63d_pctrank_252d": {"inputs": ["close"], "func": mdc_067_ret_63d_pctrank_252d},
    "mdc_068_spread_5_21_zscore_252d": {"inputs": ["close"], "func": mdc_068_spread_5_21_zscore_252d},
    "mdc_069_spread_21_63_zscore_252d": {"inputs": ["close"], "func": mdc_069_spread_21_63_zscore_252d},
    "mdc_070_spread_63_252_zscore_252d": {"inputs": ["close"], "func": mdc_070_spread_63_252_zscore_252d},
    "mdc_071_ret_5d_expanding_zscore": {"inputs": ["close"], "func": mdc_071_ret_5d_expanding_zscore},
    "mdc_072_ret_21d_expanding_zscore": {"inputs": ["close"], "func": mdc_072_ret_21d_expanding_zscore},
    "mdc_073_ret_63d_expanding_zscore": {"inputs": ["close"], "func": mdc_073_ret_63d_expanding_zscore},
    "mdc_074_decay_composite_score": {"inputs": ["close"], "func": mdc_074_decay_composite_score},
    "mdc_075_ret_252d_expanding_pctrank": {"inputs": ["close"], "func": mdc_075_ret_252d_expanding_pctrank},
}
