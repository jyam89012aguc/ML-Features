"""
57_spread_proxy — Extended Features 001-075
Domain: HIGH-LOW SPREAD illiquidity estimators — additional effective bid-ask spread
        angles: parametric (Garman-Klass / Parkinson-style) spread proxies, close-position
        in range, range entropy, spread skew/kurtosis, spread quantile depths, spread
        drawup-from-min, log-spread variants, weekly-aggregated spreads, gap-asymmetry.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Rolling z-score of s over window w."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _parkinson_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson-style spread proxy: |log(high/low)| / sqrt(4*ln2)."""
    return (_log_safe(high) - _log_safe(low)).abs() / np.sqrt(4.0 * np.log(2.0))


def _gk_spread(high: pd.Series, low: pd.Series, close: pd.Series, open_: pd.Series) -> pd.Series:
    """Garman-Klass-style spread proxy: sqrt of GK volatility estimator (daily)."""
    hl = (_log_safe(high) - _log_safe(low)) ** 2
    co = (_log_safe(close) - _log_safe(open_)) ** 2
    var = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    return np.sqrt(var.clip(lower=0.0))


def _close_pos_in_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close within the daily high-low range, 0=at low, 1=at high."""
    return _safe_div(close - low, high - low)


def _hl_spread_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Simple (high-low)/close spread proxy."""
    return _safe_div(high - low, close)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Parkinson-style log-range spread proxy ---

def spr_ext_001_parkinson_spread_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily Parkinson log-range spread proxy."""
    return _parkinson_spread(high, low)


def spr_ext_002_parkinson_spread_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling mean of Parkinson spread proxy."""
    return _rolling_mean(_parkinson_spread(high, low), _TD_WEEK)


def spr_ext_003_parkinson_spread_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling mean of Parkinson spread proxy."""
    return _rolling_mean(_parkinson_spread(high, low), _TD_MON)


def spr_ext_004_parkinson_spread_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling mean of Parkinson spread proxy."""
    return _rolling_mean(_parkinson_spread(high, low), _TD_QTR)


def spr_ext_005_parkinson_spread_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day z-score of Parkinson spread proxy."""
    return _zscore(_parkinson_spread(high, low), _TD_QTR)


def spr_ext_006_parkinson_spread_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day z-score of Parkinson spread proxy."""
    return _zscore(_parkinson_spread(high, low), _TD_YEAR)


def spr_ext_007_parkinson_spread_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day percentile rank of Parkinson spread proxy."""
    return _pct_rank(_parkinson_spread(high, low), _TD_YEAR)


def spr_ext_008_parkinson_spread_vs_252d_baseline(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson spread divided by its 252-day mean baseline."""
    p = _parkinson_spread(high, low)
    return _safe_div(p, _rolling_mean(p, _TD_YEAR))


def spr_ext_009_parkinson_spread_expanding_max(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time maximum of Parkinson spread proxy."""
    return _parkinson_spread(high, low).expanding(min_periods=2).max()


def spr_ext_010_parkinson_spread_ewm_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM(span=21) of Parkinson spread proxy."""
    return _ewm_mean(_parkinson_spread(high, low), _TD_MON)


# --- Group B (011-020): Garman-Klass-style spread proxy ---

def spr_ext_011_gk_spread_daily(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Daily Garman-Klass-style spread proxy."""
    return _gk_spread(high, low, close, open)


def spr_ext_012_gk_spread_5d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day rolling mean of Garman-Klass spread proxy."""
    return _rolling_mean(_gk_spread(high, low, close, open), _TD_WEEK)


def spr_ext_013_gk_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling mean of Garman-Klass spread proxy."""
    return _rolling_mean(_gk_spread(high, low, close, open), _TD_MON)


def spr_ext_014_gk_spread_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling mean of Garman-Klass spread proxy."""
    return _rolling_mean(_gk_spread(high, low, close, open), _TD_QTR)


def spr_ext_015_gk_spread_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day z-score of Garman-Klass spread proxy."""
    return _zscore(_gk_spread(high, low, close, open), _TD_QTR)


def spr_ext_016_gk_spread_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day z-score of Garman-Klass spread proxy."""
    return _zscore(_gk_spread(high, low, close, open), _TD_YEAR)


def spr_ext_017_gk_spread_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day percentile rank of Garman-Klass spread proxy."""
    return _pct_rank(_gk_spread(high, low, close, open), _TD_YEAR)


def spr_ext_018_gk_spread_vs_252d_baseline(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Garman-Klass spread divided by its 252-day mean baseline."""
    g = _gk_spread(high, low, close, open)
    return _safe_div(g, _rolling_mean(g, _TD_YEAR))


def spr_ext_019_gk_vs_parkinson_spread_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21d-mean GK spread to 21d-mean Parkinson spread (estimator divergence)."""
    g = _rolling_mean(_gk_spread(high, low, close, open), _TD_MON)
    p = _rolling_mean(_parkinson_spread(high, low), _TD_MON)
    return _safe_div(g, p)


def spr_ext_020_gk_spread_expanding_max(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time maximum of Garman-Klass spread proxy."""
    return _gk_spread(high, low, close, open).expanding(min_periods=2).max()


# --- Group C (021-032): Close-position-in-range spread/distress proxies ---

def spr_ext_021_close_pos_in_range_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily position of close within the high-low range (0=low, 1=high)."""
    return _close_pos_in_range(high, low, close)


def spr_ext_022_close_pos_in_range_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day mean of close-position-in-range."""
    return _rolling_mean(_close_pos_in_range(high, low, close), _TD_WEEK)


def spr_ext_023_close_pos_in_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of close-position-in-range."""
    return _rolling_mean(_close_pos_in_range(high, low, close), _TD_MON)


def spr_ext_024_close_near_low_frac_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close finished in lowest 20% of range."""
    cp = _close_pos_in_range(high, low, close)
    return _rolling_sum((cp < 0.20).astype(float), _TD_MON) / _TD_MON


def spr_ext_025_close_near_low_frac_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close finished in lowest 20% of range."""
    cp = _close_pos_in_range(high, low, close)
    return _rolling_sum((cp < 0.20).astype(float), _TD_QTR) / _TD_QTR


def spr_ext_026_close_at_low_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days where close finished in lowest 20% of daily range."""
    cp = _close_pos_in_range(high, low, close)
    return _consec_streak(cp < 0.20)


def spr_ext_027_close_pos_in_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day z-score of close-position-in-range."""
    return _zscore(_close_pos_in_range(high, low, close), _TD_QTR)


def spr_ext_028_close_pos_in_range_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day percentile rank of close-position-in-range."""
    return _pct_rank(_close_pos_in_range(high, low, close), _TD_YEAR)


def spr_ext_029_low_close_pos_spread_proxy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d mean of (1 - close_pos) * HL spread — distressed-close weighted spread."""
    cp = _close_pos_in_range(high, low, close)
    hl = _hl_spread_raw(high, low, close)
    return _rolling_mean((1.0 - cp) * hl, _TD_MON)


def spr_ext_030_open_pos_in_range_daily(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Daily position of open within the high-low range (0=low, 1=high)."""
    return _safe_div(open - low, high - low)


def spr_ext_031_open_pos_in_range_21d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean of open-position-in-range."""
    return _rolling_mean(_safe_div(open - low, high - low), _TD_MON)


def spr_ext_032_close_minus_open_pos_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of (close_pos - open_pos) within range — intraday drift in range."""
    cp = _close_pos_in_range(high, low, close)
    op = _safe_div(open - low, high - low)
    return _rolling_mean(cp - op, _TD_MON)


# --- Group D (033-044): Spread distributional shape — skew, kurtosis, quantiles ---

def spr_ext_033_hl_spread_skew_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling skewness of HL spread proxy (tail asymmetry of spread spikes)."""
    return _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).skew()


def spr_ext_034_hl_spread_skew_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling skewness of HL spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def spr_ext_035_hl_spread_kurt_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of HL spread proxy (fat-tail spread risk)."""
    return _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def spr_ext_036_hl_spread_kurt_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling kurtosis of HL spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_YEAR, min_periods=_TD_QTR).kurt()


def spr_ext_037_hl_spread_q90_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling 90th percentile of HL spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.90)


def spr_ext_038_hl_spread_q90_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling 90th percentile of HL spread proxy."""
    return _hl_spread_raw(high, low, close).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)


def spr_ext_039_hl_spread_q10_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling 10th percentile of HL spread proxy (calm-state floor)."""
    return _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.10)


def spr_ext_040_hl_spread_iqr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day interquartile range of HL spread proxy (spread dispersion)."""
    hl = _hl_spread_raw(high, low, close)
    q75 = hl.rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.75)
    q25 = hl.rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.25)
    return q75 - q25


def spr_ext_041_hl_spread_q90_vs_median_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63d 90th-percentile HL spread to its 63d median (tail-to-center ratio)."""
    hl = _hl_spread_raw(high, low, close)
    q90 = hl.rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.90)
    med = _rolling_median(hl, _TD_QTR)
    return _safe_div(q90, med)


def spr_ext_042_cs_spread_skew_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling skewness of Corwin-Schultz-style log-range spread."""
    lr = (_log_safe(high) - _log_safe(low)).abs()
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def spr_ext_043_hl_spread_above_q90_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: daily HL spread above its trailing 252d 90th percentile."""
    hl = _hl_spread_raw(high, low, close)
    q90 = hl.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (hl > q90).astype(float)


def spr_ext_044_hl_spread_above_q90_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in 63d window where HL spread exceeds 252d 90th percentile."""
    hl = _hl_spread_raw(high, low, close)
    q90 = hl.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _rolling_sum((hl > q90).astype(float), _TD_QTR)


# --- Group E (045-056): Log-spread variants and spread drawup measures ---

def spr_ext_045_log_hl_spread_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of (1 + HL spread proxy) — compressed-tail spread measure."""
    return np.log1p(_hl_spread_raw(high, low, close))


def spr_ext_046_log_hl_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of log(1 + HL spread)."""
    return _rolling_mean(np.log1p(_hl_spread_raw(high, low, close)), _TD_MON)


def spr_ext_047_log_hl_spread_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day z-score of log(1 + HL spread)."""
    return _zscore(np.log1p(_hl_spread_raw(high, low, close)), _TD_YEAR)


def spr_ext_048_hl_spread_drawup_from_63d_min(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread minus its trailing 63d minimum (spread drawup from calm)."""
    hl = _hl_spread_raw(high, low, close)
    return hl - _rolling_min(hl, _TD_QTR)


def spr_ext_049_hl_spread_drawup_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread divided by its trailing 63d minimum (multiplicative drawup)."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, _rolling_min(hl, _TD_QTR))


def spr_ext_050_hl_spread_drawup_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread divided by its trailing 252d minimum."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, _rolling_min(hl, _TD_YEAR))


def spr_ext_051_hl_spread_range_position_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of current HL spread within its 63d min-max range (0=min, 1=max)."""
    hl = _hl_spread_raw(high, low, close)
    mn = _rolling_min(hl, _TD_QTR)
    mx = _rolling_max(hl, _TD_QTR)
    return _safe_div(hl - mn, mx - mn)


def spr_ext_052_hl_spread_range_position_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of current HL spread within its 252d min-max range."""
    hl = _hl_spread_raw(high, low, close)
    mn = _rolling_min(hl, _TD_YEAR)
    mx = _rolling_max(hl, _TD_YEAR)
    return _safe_div(hl - mn, mx - mn)


def spr_ext_053_cs_log_spread_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-range spread: log(high/low) — raw two-sided microstructure proxy."""
    return _log_safe(high) - _log_safe(low)


def spr_ext_054_cs_log_spread_drawup_ratio_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log-range spread divided by its trailing 252d minimum."""
    lr = (_log_safe(high) - _log_safe(low)).abs()
    return _safe_div(lr, _rolling_min(lr, _TD_YEAR))


def spr_ext_055_hl_spread_at_63d_max_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: current HL spread equals its trailing 63d maximum (fresh spread extreme)."""
    hl = _hl_spread_raw(high, low, close)
    return (hl >= _rolling_max(hl, _TD_QTR) - _EPS).astype(float)


def spr_ext_056_hl_spread_new_252d_max_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of new 252d-max HL spread days within trailing 63d window."""
    hl = _hl_spread_raw(high, low, close)
    is_max = (hl >= _rolling_max(hl, _TD_YEAR) - _EPS).astype(float)
    return _rolling_sum(is_max, _TD_QTR)


# --- Group F (057-066): Weekly-aggregated and multi-day spread proxies ---

def spr_ext_057_weekly_hl_spread_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day aggregated spread: (5d high - 5d low) / close (weekly range proxy)."""
    return _safe_div(_rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK), close)


def spr_ext_058_monthly_hl_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day aggregated spread: (21d high - 21d low) / close (monthly range proxy)."""
    return _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON), close)


def spr_ext_059_weekly_spread_vs_daily_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5d-aggregated spread to 5x mean daily HL spread (range clustering)."""
    weekly = _safe_div(_rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK), close)
    daily5 = 5.0 * _rolling_mean(_hl_spread_raw(high, low, close), _TD_WEEK)
    return _safe_div(weekly, daily5)


def spr_ext_060_weekly_hl_spread_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day z-score of 5-day aggregated spread proxy."""
    weekly = _safe_div(_rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK), close)
    return _zscore(weekly, _TD_YEAR)


def spr_ext_061_monthly_hl_spread_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day percentile rank of 21-day aggregated spread proxy."""
    monthly = _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON), close)
    return _pct_rank(monthly, _TD_YEAR)


def spr_ext_062_two_day_hl_spread_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-day spread: (2d high - 2d low) / close."""
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    return _safe_div(h2 - l2, close)


def spr_ext_063_two_day_hl_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of two-day spread proxy."""
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(_safe_div(h2 - l2, close), _TD_MON)


def spr_ext_064_monthly_spread_vs_weekly_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d-aggregated spread to 5d-aggregated spread (range-horizon scaling)."""
    monthly = _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON), close)
    weekly = _safe_div(_rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK), close)
    return _safe_div(monthly, weekly)


def spr_ext_065_weekly_spread_widening_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days where 5d-aggregated spread exceeds its prior value."""
    weekly = _safe_div(_rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK), close)
    return _consec_streak(weekly > weekly.shift(1))


def spr_ext_066_quarterly_hl_spread_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day aggregated spread: (63d high - 63d low) / close (quarterly range proxy)."""
    return _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR), close)


# --- Group G (067-075): Gap-asymmetry, intraday/overnight decomposition, composites ---

def spr_ext_067_overnight_spread_signed_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of signed overnight gap: (open - prior_close)/prior_close."""
    prior = close.shift(1)
    return _rolling_mean(_safe_div(open - prior, prior), _TD_MON)


def spr_ext_068_gap_spread_asymmetry_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 63d mean down-gap magnitude to 63d mean up-gap magnitude."""
    prior = close.shift(1)
    gap = _safe_div(open - prior, prior)
    down = gap.where(gap < 0, np.nan).abs().rolling(_TD_QTR, min_periods=5).mean()
    up = gap.where(gap > 0, np.nan).rolling(_TD_QTR, min_periods=5).mean()
    return _safe_div(down, up)


def spr_ext_069_intraday_spread_pct_open_21d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of intraday range relative to open: (high-low)/open."""
    return _rolling_mean(_safe_div(high - low, open.replace(0, np.nan)), _TD_MON)


def spr_ext_070_overnight_to_intraday_spread_ratio_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series
) -> pd.Series:
    """63d ratio of |overnight gap| spread to intraday HL spread (where price moves)."""
    over = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    intra = _hl_spread_raw(high, low, close)
    return _safe_div(_rolling_mean(over, _TD_QTR), _rolling_mean(intra, _TD_QTR))


def spr_ext_071_gap_spread_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day z-score of absolute overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _zscore(gap, _TD_YEAR)


def spr_ext_072_total_spread_intraday_plus_overnight_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series
) -> pd.Series:
    """21d mean of total spread = intraday HL spread + |overnight gap| spread."""
    intra = _hl_spread_raw(high, low, close)
    over = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _rolling_mean(intra + over, _TD_MON)


def spr_ext_073_spread_widening_acceleration_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d change of the 5d-mean HL spread (spread-widening acceleration)."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_WEEK).diff(_TD_MON)


def spr_ext_074_hl_spread_persistence_above_median_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days HL spread stayed above its 252d median (sustained stress)."""
    hl = _hl_spread_raw(high, low, close)
    med = _rolling_median(hl, _TD_YEAR)
    return _rolling_sum((hl > med).astype(float), _TD_QTR) / _TD_QTR


def spr_ext_075_spread_capitulation_composite(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series
) -> pd.Series:
    """Capitulation composite: avg of normalized HL-spread pct-rank, Parkinson z-score,
    GK z-score and overnight-gap z-score. Higher = more extreme illiquidity distress."""
    hl_pr = _pct_rank(_hl_spread_raw(high, low, close), _TD_YEAR).fillna(0.5)
    pk_z = _zscore(_parkinson_spread(high, low), _TD_YEAR).clip(-3.0, 3.0) / 3.0
    gk_z = _zscore(_gk_spread(high, low, close, open), _TD_YEAR).clip(-3.0, 3.0) / 3.0
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    gap_z = _zscore(gap, _TD_YEAR).clip(-3.0, 3.0) / 3.0
    return (hl_pr + pk_z.fillna(0.0) + gk_z.fillna(0.0) + gap_z.fillna(0.0)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

SPREAD_PROXY_EXTENDED_REGISTRY_001_075 = {
    "spr_ext_001_parkinson_spread_daily": {"inputs": ["high", "low"], "func": spr_ext_001_parkinson_spread_daily},
    "spr_ext_002_parkinson_spread_5d": {"inputs": ["high", "low"], "func": spr_ext_002_parkinson_spread_5d},
    "spr_ext_003_parkinson_spread_21d": {"inputs": ["high", "low"], "func": spr_ext_003_parkinson_spread_21d},
    "spr_ext_004_parkinson_spread_63d": {"inputs": ["high", "low"], "func": spr_ext_004_parkinson_spread_63d},
    "spr_ext_005_parkinson_spread_zscore_63d": {"inputs": ["high", "low"], "func": spr_ext_005_parkinson_spread_zscore_63d},
    "spr_ext_006_parkinson_spread_zscore_252d": {"inputs": ["high", "low"], "func": spr_ext_006_parkinson_spread_zscore_252d},
    "spr_ext_007_parkinson_spread_pct_rank_252d": {"inputs": ["high", "low"], "func": spr_ext_007_parkinson_spread_pct_rank_252d},
    "spr_ext_008_parkinson_spread_vs_252d_baseline": {"inputs": ["high", "low"], "func": spr_ext_008_parkinson_spread_vs_252d_baseline},
    "spr_ext_009_parkinson_spread_expanding_max": {"inputs": ["high", "low"], "func": spr_ext_009_parkinson_spread_expanding_max},
    "spr_ext_010_parkinson_spread_ewm_21d": {"inputs": ["high", "low"], "func": spr_ext_010_parkinson_spread_ewm_21d},
    "spr_ext_011_gk_spread_daily": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_011_gk_spread_daily},
    "spr_ext_012_gk_spread_5d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_012_gk_spread_5d},
    "spr_ext_013_gk_spread_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_013_gk_spread_21d},
    "spr_ext_014_gk_spread_63d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_014_gk_spread_63d},
    "spr_ext_015_gk_spread_zscore_63d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_015_gk_spread_zscore_63d},
    "spr_ext_016_gk_spread_zscore_252d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_016_gk_spread_zscore_252d},
    "spr_ext_017_gk_spread_pct_rank_252d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_017_gk_spread_pct_rank_252d},
    "spr_ext_018_gk_spread_vs_252d_baseline": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_018_gk_spread_vs_252d_baseline},
    "spr_ext_019_gk_vs_parkinson_spread_ratio_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_019_gk_vs_parkinson_spread_ratio_21d},
    "spr_ext_020_gk_spread_expanding_max": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_020_gk_spread_expanding_max},
    "spr_ext_021_close_pos_in_range_daily": {"inputs": ["high", "low", "close"], "func": spr_ext_021_close_pos_in_range_daily},
    "spr_ext_022_close_pos_in_range_5d": {"inputs": ["high", "low", "close"], "func": spr_ext_022_close_pos_in_range_5d},
    "spr_ext_023_close_pos_in_range_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_023_close_pos_in_range_21d},
    "spr_ext_024_close_near_low_frac_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_024_close_near_low_frac_21d},
    "spr_ext_025_close_near_low_frac_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_025_close_near_low_frac_63d},
    "spr_ext_026_close_at_low_streak": {"inputs": ["high", "low", "close"], "func": spr_ext_026_close_at_low_streak},
    "spr_ext_027_close_pos_in_range_zscore_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_027_close_pos_in_range_zscore_63d},
    "spr_ext_028_close_pos_in_range_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_028_close_pos_in_range_pct_rank_252d},
    "spr_ext_029_low_close_pos_spread_proxy_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_029_low_close_pos_spread_proxy_21d},
    "spr_ext_030_open_pos_in_range_daily": {"inputs": ["high", "low", "open"], "func": spr_ext_030_open_pos_in_range_daily},
    "spr_ext_031_open_pos_in_range_21d": {"inputs": ["high", "low", "open"], "func": spr_ext_031_open_pos_in_range_21d},
    "spr_ext_032_close_minus_open_pos_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_032_close_minus_open_pos_21d},
    "spr_ext_033_hl_spread_skew_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_033_hl_spread_skew_63d},
    "spr_ext_034_hl_spread_skew_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_034_hl_spread_skew_252d},
    "spr_ext_035_hl_spread_kurt_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_035_hl_spread_kurt_63d},
    "spr_ext_036_hl_spread_kurt_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_036_hl_spread_kurt_252d},
    "spr_ext_037_hl_spread_q90_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_037_hl_spread_q90_63d},
    "spr_ext_038_hl_spread_q90_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_038_hl_spread_q90_252d},
    "spr_ext_039_hl_spread_q10_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_039_hl_spread_q10_63d},
    "spr_ext_040_hl_spread_iqr_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_040_hl_spread_iqr_63d},
    "spr_ext_041_hl_spread_q90_vs_median_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_041_hl_spread_q90_vs_median_63d},
    "spr_ext_042_cs_spread_skew_252d": {"inputs": ["high", "low"], "func": spr_ext_042_cs_spread_skew_252d},
    "spr_ext_043_hl_spread_above_q90_flag": {"inputs": ["high", "low", "close"], "func": spr_ext_043_hl_spread_above_q90_flag},
    "spr_ext_044_hl_spread_above_q90_count_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_044_hl_spread_above_q90_count_63d},
    "spr_ext_045_log_hl_spread_daily": {"inputs": ["high", "low", "close"], "func": spr_ext_045_log_hl_spread_daily},
    "spr_ext_046_log_hl_spread_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_046_log_hl_spread_21d},
    "spr_ext_047_log_hl_spread_zscore_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_047_log_hl_spread_zscore_252d},
    "spr_ext_048_hl_spread_drawup_from_63d_min": {"inputs": ["high", "low", "close"], "func": spr_ext_048_hl_spread_drawup_from_63d_min},
    "spr_ext_049_hl_spread_drawup_ratio_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_049_hl_spread_drawup_ratio_63d},
    "spr_ext_050_hl_spread_drawup_ratio_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_050_hl_spread_drawup_ratio_252d},
    "spr_ext_051_hl_spread_range_position_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_051_hl_spread_range_position_63d},
    "spr_ext_052_hl_spread_range_position_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_052_hl_spread_range_position_252d},
    "spr_ext_053_cs_log_spread_daily": {"inputs": ["high", "low"], "func": spr_ext_053_cs_log_spread_daily},
    "spr_ext_054_cs_log_spread_drawup_ratio_252d": {"inputs": ["high", "low"], "func": spr_ext_054_cs_log_spread_drawup_ratio_252d},
    "spr_ext_055_hl_spread_at_63d_max_flag": {"inputs": ["high", "low", "close"], "func": spr_ext_055_hl_spread_at_63d_max_flag},
    "spr_ext_056_hl_spread_new_252d_max_count_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_056_hl_spread_new_252d_max_count_63d},
    "spr_ext_057_weekly_hl_spread_5d": {"inputs": ["high", "low", "close"], "func": spr_ext_057_weekly_hl_spread_5d},
    "spr_ext_058_monthly_hl_spread_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_058_monthly_hl_spread_21d},
    "spr_ext_059_weekly_spread_vs_daily_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_059_weekly_spread_vs_daily_ratio_21d},
    "spr_ext_060_weekly_hl_spread_zscore_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_060_weekly_hl_spread_zscore_252d},
    "spr_ext_061_monthly_hl_spread_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_ext_061_monthly_hl_spread_pct_rank_252d},
    "spr_ext_062_two_day_hl_spread_daily": {"inputs": ["high", "low", "close"], "func": spr_ext_062_two_day_hl_spread_daily},
    "spr_ext_063_two_day_hl_spread_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_063_two_day_hl_spread_21d},
    "spr_ext_064_monthly_spread_vs_weekly_ratio": {"inputs": ["high", "low", "close"], "func": spr_ext_064_monthly_spread_vs_weekly_ratio},
    "spr_ext_065_weekly_spread_widening_streak": {"inputs": ["high", "low", "close"], "func": spr_ext_065_weekly_spread_widening_streak},
    "spr_ext_066_quarterly_hl_spread_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_066_quarterly_hl_spread_63d},
    "spr_ext_067_overnight_spread_signed_21d": {"inputs": ["close", "open"], "func": spr_ext_067_overnight_spread_signed_21d},
    "spr_ext_068_gap_spread_asymmetry_63d": {"inputs": ["close", "open"], "func": spr_ext_068_gap_spread_asymmetry_63d},
    "spr_ext_069_intraday_spread_pct_open_21d": {"inputs": ["high", "low", "open"], "func": spr_ext_069_intraday_spread_pct_open_21d},
    "spr_ext_070_overnight_to_intraday_spread_ratio_63d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_070_overnight_to_intraday_spread_ratio_63d},
    "spr_ext_071_gap_spread_zscore_252d": {"inputs": ["close", "open"], "func": spr_ext_071_gap_spread_zscore_252d},
    "spr_ext_072_total_spread_intraday_plus_overnight_21d": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_072_total_spread_intraday_plus_overnight_21d},
    "spr_ext_073_spread_widening_acceleration_21d": {"inputs": ["high", "low", "close"], "func": spr_ext_073_spread_widening_acceleration_21d},
    "spr_ext_074_hl_spread_persistence_above_median_63d": {"inputs": ["high", "low", "close"], "func": spr_ext_074_hl_spread_persistence_above_median_63d},
    "spr_ext_075_spread_capitulation_composite": {"inputs": ["high", "low", "close", "open"], "func": spr_ext_075_spread_capitulation_composite},
}
