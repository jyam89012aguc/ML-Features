"""
06_low_proximity — Extended Features 001-075
Domain: closeness to trailing minimum, new-low flags, low-frequency behavior —
        deeper variants: volume-weighted proximity, log-space distances, percentile
        ranks, z-scores, smoothed floors, composite multi-window features,
        high/low/open anchors, ATR-normalised distances, streak overlays.
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
    return num / den.replace(0, np.nan)


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_tr(close, high, low), w)


def _consec_streak(cond: pd.Series) -> pd.Series:
    c     = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _vwap_rolling(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    return _safe_div(_rolling_sum(close * volume, w), _rolling_sum(volume, w))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Log-space distance to trailing low ---

def lp_ext_001_log_dist_21d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 21-day rolling min (log(close/min))."""
    return _log_safe(close) - _log_safe(_rolling_min(close, _TD_MON))


def lp_ext_002_log_dist_63d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 63-day rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, _TD_QTR))


def lp_ext_003_log_dist_126d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 126-day rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, _TD_HALF))


def lp_ext_004_log_dist_252d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 252-day rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, _TD_YEAR))


def lp_ext_005_log_dist_504d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 504-day (2yr) rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 504))


def lp_ext_006_log_dist_756d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 756-day (3yr) rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 756))


def lp_ext_007_log_dist_10d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 10-day rolling min (2-week floor)."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 10))


def lp_ext_008_log_dist_42d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 42-day (2-month) rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 42))


def lp_ext_009_log_dist_189d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 189-day (9-month) rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 189))


def lp_ext_010_log_dist_378d_min(close: pd.Series) -> pd.Series:
    """Log-space distance from close to 378-day (18-month) rolling min."""
    return _log_safe(close) - _log_safe(_rolling_min(close, 378))


# --- Group B (011-018): ATR-normalised distance to rolling low ---

def lp_ext_011_atr_norm_dist_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 21d_min) normalised by 21-day ATR."""
    mn  = _rolling_min(close, _TD_MON)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - mn, atr)


def lp_ext_012_atr_norm_dist_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 63d_min) normalised by 63-day ATR."""
    mn  = _rolling_min(close, _TD_QTR)
    atr = _atr(close, high, low, _TD_QTR)
    return _safe_div(close - mn, atr)


def lp_ext_013_atr_norm_dist_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 126d_min) normalised by 126-day ATR."""
    mn  = _rolling_min(close, _TD_HALF)
    atr = _atr(close, high, low, _TD_HALF)
    return _safe_div(close - mn, atr)


def lp_ext_014_atr_norm_dist_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 252d_min) normalised by 252-day ATR."""
    mn  = _rolling_min(close, _TD_YEAR)
    atr = _atr(close, high, low, _TD_YEAR)
    return _safe_div(close - mn, atr)


def lp_ext_015_atr_norm_dist_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 504d_min) normalised by 63-day ATR (2yr floor, short-window vol)."""
    mn  = _rolling_min(close, 504)
    atr = _atr(close, high, low, _TD_QTR)
    return _safe_div(close - mn, atr)


# --- Group C (016-024): Low-bar anchor (rolling min of low, not close) ---

def lp_ext_016_close_above_21d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct close is above 21-day rolling min of daily low (intraday floor proximity)."""
    mn = _rolling_min(low, _TD_MON)
    return _safe_div(close - mn, mn)


def lp_ext_017_close_above_63d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct close above 63-day rolling min of daily low."""
    mn = _rolling_min(low, _TD_QTR)
    return _safe_div(close - mn, mn)


def lp_ext_018_close_above_126d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct close above 126-day rolling min of daily low."""
    mn = _rolling_min(low, _TD_HALF)
    return _safe_div(close - mn, mn)


def lp_ext_019_close_above_252d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct close above 252-day rolling min of daily low (1yr intraday floor)."""
    mn = _rolling_min(low, _TD_YEAR)
    return _safe_div(close - mn, mn)


def lp_ext_020_close_above_504d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct close above 504-day rolling min of daily low (2yr intraday floor)."""
    mn = _rolling_min(low, 504)
    return _safe_div(close - mn, mn)


def lp_ext_021_log_close_above_21d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log pct close above 21-day rolling min of daily low."""
    mn = _rolling_min(low, _TD_MON)
    return _log_safe(close) - _log_safe(mn)


def lp_ext_022_log_close_above_252d_low_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log pct close above 252-day rolling min of daily low."""
    mn = _rolling_min(low, _TD_YEAR)
    return _log_safe(close) - _log_safe(mn)


# --- Group D (023-031): Percentile rank of proximity within rolling window ---

def lp_ext_023_prox_pctrank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within its 63-day range (0=at min, 1=at max)."""
    mn = _rolling_min(close, _TD_QTR)
    mx = _rolling_max(close, _TD_QTR)
    return _safe_div(close - mn, mx - mn)


def lp_ext_024_prox_pctrank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within its 126-day range."""
    mn = _rolling_min(close, _TD_HALF)
    mx = _rolling_max(close, _TD_HALF)
    return _safe_div(close - mn, mx - mn)


def lp_ext_025_prox_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within its 252-day range."""
    mn = _rolling_min(close, _TD_YEAR)
    mx = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - mn, mx - mn)


def lp_ext_026_prox_pctrank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within its 504-day range (2yr)."""
    mn = _rolling_min(close, 504)
    mx = _rolling_max(close, 504)
    return _safe_div(close - mn, mx - mn)


def lp_ext_027_prox_pctrank_756d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within its 756-day range (3yr)."""
    mn = _rolling_min(close, 756)
    mx = _rolling_max(close, 756)
    return _safe_div(close - mn, mx - mn)


def lp_ext_028_rolling_rank_63d(close: pd.Series) -> pd.Series:
    """Rolling rank-pct of close among its trailing 63 closes (order-stat proximity)."""
    return _rolling_rank_pct(close, _TD_QTR)


def lp_ext_029_rolling_rank_252d(close: pd.Series) -> pd.Series:
    """Rolling rank-pct of close among its trailing 252 closes."""
    return _rolling_rank_pct(close, _TD_YEAR)


def lp_ext_030_rolling_rank_504d(close: pd.Series) -> pd.Series:
    """Rolling rank-pct of close among its trailing 504 closes."""
    return _rolling_rank_pct(close, 504)


# --- Group E (031-038): Z-score proximity measures ---

def lp_ext_031_zscore_close_63d(close: pd.Series) -> pd.Series:
    """Z-score of close relative to its 63-day rolling mean/std."""
    return _zscore_rolling(close, _TD_QTR)


def lp_ext_032_zscore_close_126d(close: pd.Series) -> pd.Series:
    """Z-score of close relative to its 126-day rolling mean/std."""
    return _zscore_rolling(close, _TD_HALF)


def lp_ext_033_zscore_close_252d(close: pd.Series) -> pd.Series:
    """Z-score of close relative to its 252-day rolling mean/std."""
    return _zscore_rolling(close, _TD_YEAR)


def lp_ext_034_zscore_log_close_252d(close: pd.Series) -> pd.Series:
    """Z-score of log(close) relative to its 252-day rolling mean/std."""
    return _zscore_rolling(_log_safe(close), _TD_YEAR)


def lp_ext_035_zscore_log_close_504d(close: pd.Series) -> pd.Series:
    """Z-score of log(close) relative to its 504-day rolling mean/std."""
    return _zscore_rolling(_log_safe(close), 504)


def lp_ext_036_prox_zscore_21d_min(close: pd.Series) -> pd.Series:
    """Z-score of (close - 21d_min) over 63-day window."""
    prox = close - _rolling_min(close, _TD_MON)
    return _zscore_rolling(prox, _TD_QTR)


def lp_ext_037_prox_zscore_63d_min(close: pd.Series) -> pd.Series:
    """Z-score of (close - 63d_min) over 126-day window."""
    prox = close - _rolling_min(close, _TD_QTR)
    return _zscore_rolling(prox, _TD_HALF)


def lp_ext_038_prox_zscore_252d_min(close: pd.Series) -> pd.Series:
    """Z-score of (close - 252d_min) over 252-day window."""
    prox = close - _rolling_min(close, _TD_YEAR)
    return _zscore_rolling(prox, _TD_YEAR)


# --- Group F (039-046): Volume-weighted proximity ---

def lp_ext_039_vol_weighted_prox_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of (close - 21d_min)/21d_min over trailing 21 days."""
    prox = _safe_div(close - _rolling_min(close, _TD_MON), _rolling_min(close, _TD_MON))
    return _safe_div(_rolling_sum(prox * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def lp_ext_040_vol_weighted_prox_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of proximity to 63d min, over trailing 63 days."""
    prox = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return _safe_div(_rolling_sum(prox * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def lp_ext_041_vol_weighted_prox_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of proximity to 252d min, over trailing 252 days."""
    prox = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _safe_div(_rolling_sum(prox * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def lp_ext_042_vwap_vs_252d_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct that rolling 21-day VWAP is above the 252-day close low."""
    vwap = _vwap_rolling(close, volume, _TD_MON)
    mn   = _rolling_min(close, _TD_YEAR)
    return _safe_div(vwap - mn, mn)


def lp_ext_043_vwap_vs_63d_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct that rolling 21-day VWAP is above the 63-day close low."""
    vwap = _vwap_rolling(close, volume, _TD_MON)
    mn   = _rolling_min(close, _TD_QTR)
    return _safe_div(vwap - mn, mn)


def lp_ext_044_high_vol_day_prox_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close proximity to 63d min on days with above-median volume (else NaN, ffilled)."""
    mn     = _rolling_min(close, _TD_QTR)
    med_v  = _rolling_median(volume, _TD_QTR)
    prox   = _safe_div(close - mn, mn)
    masked = prox.where(volume >= med_v)
    return masked.ffill()


def lp_ext_045_low_vol_day_prox_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close proximity to 63d min on days with below-median volume (else NaN, ffilled)."""
    mn     = _rolling_min(close, _TD_QTR)
    med_v  = _rolling_median(volume, _TD_QTR)
    prox   = _safe_div(close - mn, mn)
    masked = prox.where(volume < med_v)
    return masked.ffill()


# --- Group G (046-054): EWM-smoothed proximity ---

def lp_ext_046_ewm_prox_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed proximity to 63d rolling min."""
    prox = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return _ewm_mean(prox, _TD_MON)


def lp_ext_047_ewm_prox_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed proximity to 252d rolling min."""
    prox = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _ewm_mean(prox, _TD_QTR)


def lp_ext_048_ewm_log_prox_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed log proximity to 63d rolling min."""
    log_prox = _log_safe(close) - _log_safe(_rolling_min(close, _TD_QTR))
    return _ewm_mean(log_prox, _TD_MON)


def lp_ext_049_ewm_log_prox_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed log proximity to 252d rolling min."""
    log_prox = _log_safe(close) - _log_safe(_rolling_min(close, _TD_YEAR))
    return _ewm_mean(log_prox, _TD_QTR)


def lp_ext_050_ewm_prox_126d(close: pd.Series) -> pd.Series:
    """EWM(126)-smoothed proximity to 504d rolling min."""
    prox = _safe_div(close - _rolling_min(close, 504), _rolling_min(close, 504))
    return _ewm_mean(prox, _TD_HALF)


# --- Group H (051-058): Streak overlays — time at floor ---

def lp_ext_051_consec_days_within1pct_21d_min(close: pd.Series) -> pd.Series:
    """Consecutive days where close is within 1% of its 21-day rolling min."""
    mn   = _rolling_min(close, _TD_MON)
    cond = _safe_div(close - mn, mn) <= 0.01
    return _consec_streak(cond)


def lp_ext_052_consec_days_within1pct_63d_min(close: pd.Series) -> pd.Series:
    """Consecutive days where close is within 1% of its 63-day rolling min."""
    mn   = _rolling_min(close, _TD_QTR)
    cond = _safe_div(close - mn, mn) <= 0.01
    return _consec_streak(cond)


def lp_ext_053_consec_days_within1pct_252d_min(close: pd.Series) -> pd.Series:
    """Consecutive days where close is within 1% of its 252-day rolling min."""
    mn   = _rolling_min(close, _TD_YEAR)
    cond = _safe_div(close - mn, mn) <= 0.01
    return _consec_streak(cond)


def lp_ext_054_consec_days_within5pct_252d_min(close: pd.Series) -> pd.Series:
    """Consecutive days where close is within 5% of its 252-day rolling min."""
    mn   = _rolling_min(close, _TD_YEAR)
    cond = _safe_div(close - mn, mn) <= 0.05
    return _consec_streak(cond)


def lp_ext_055_count_within2pct_63d_min_over_63d(close: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close was within 2% of rolling 63d min."""
    mn   = _rolling_min(close, _TD_QTR)
    flag = (_safe_div(close - mn, mn) <= 0.02).astype(float)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def lp_ext_056_count_within2pct_252d_min_over_252d(close: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where close was within 2% of rolling 252d min."""
    mn   = _rolling_min(close, _TD_YEAR)
    flag = (_safe_div(close - mn, mn) <= 0.02).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def lp_ext_057_pct_days_near_floor_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that close was within 3% of 63d min."""
    mn   = _rolling_min(close, _TD_QTR)
    flag = (_safe_div(close - mn, mn) <= 0.03).astype(float)
    cnt  = flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return cnt / _TD_QTR


def lp_ext_058_pct_days_near_floor_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days that close was within 3% of 252d min."""
    mn   = _rolling_min(close, _TD_YEAR)
    flag = (_safe_div(close - mn, mn) <= 0.03).astype(float)
    cnt  = flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    return cnt / _TD_YEAR


# --- Group I (059-065): Multi-window composite proximity scores ---

def lp_ext_059_multi_window_prox_avg(close: pd.Series) -> pd.Series:
    """Average of proximity-to-min across 21, 63, 126, 252d windows."""
    p1 = _safe_div(close - _rolling_min(close, _TD_MON),  _rolling_min(close, _TD_MON))
    p2 = _safe_div(close - _rolling_min(close, _TD_QTR),  _rolling_min(close, _TD_QTR))
    p3 = _safe_div(close - _rolling_min(close, _TD_HALF), _rolling_min(close, _TD_HALF))
    p4 = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return (p1 + p2 + p3 + p4) / 4.0


def lp_ext_060_multi_window_prox_min(close: pd.Series) -> pd.Series:
    """Minimum (most bearish) proximity across 21, 63, 126, 252d windows."""
    p1 = _safe_div(close - _rolling_min(close, _TD_MON),  _rolling_min(close, _TD_MON))
    p2 = _safe_div(close - _rolling_min(close, _TD_QTR),  _rolling_min(close, _TD_QTR))
    p3 = _safe_div(close - _rolling_min(close, _TD_HALF), _rolling_min(close, _TD_HALF))
    p4 = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return pd.concat([p1, p2, p3, p4], axis=1).min(axis=1)


def lp_ext_061_prox_ratio_21_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d proximity to 252d proximity (near-vs-far floor comparison)."""
    p21  = _safe_div(close - _rolling_min(close, _TD_MON),  _rolling_min(close, _TD_MON))
    p252 = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _safe_div(p21, p252 + _EPS)


def lp_ext_062_prox_ratio_63_to_504d(close: pd.Series) -> pd.Series:
    """Ratio of 63d proximity to 504d proximity (medium vs long floor)."""
    p63  = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    p504 = _safe_div(close - _rolling_min(close, 504),     _rolling_min(close, 504))
    return _safe_div(p63, p504 + _EPS)


def lp_ext_063_prox_acceleration_21_63d(close: pd.Series) -> pd.Series:
    """Change in 21d proximity vs 63d proximity (acceleration toward floor)."""
    p21 = _safe_div(close - _rolling_min(close, _TD_MON),  _rolling_min(close, _TD_MON))
    p63 = _safe_div(close - _rolling_min(close, _TD_QTR),  _rolling_min(close, _TD_QTR))
    return p21 - p63


def lp_ext_064_prox_momentum_21d(close: pd.Series) -> pd.Series:
    """21-day change in proximity-to-252d-min (increasing = moving toward floor)."""
    prox = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return prox - prox.shift(_TD_MON)


def lp_ext_065_prox_momentum_63d(close: pd.Series) -> pd.Series:
    """63-day change in proximity-to-252d-min."""
    prox = _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return prox - prox.shift(_TD_QTR)


# --- Group J (066-075): Open-anchor and high-anchor proximity variants ---

def lp_ext_066_open_above_252d_min(open: pd.Series, close: pd.Series) -> pd.Series:
    """Pct that open is above 252-day rolling close min."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(open - mn, mn)


def lp_ext_067_high_above_252d_min(high: pd.Series, close: pd.Series) -> pd.Series:
    """Pct that daily high is above 252-day rolling close min."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(high - mn, mn)


def lp_ext_068_low_above_252d_min(low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct that daily low is above 252-day rolling close min."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(low - mn, mn)


def lp_ext_069_close_low_spread_vs_252d_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """(close - low) normalised by 252-day rolling close min (intraday tail vs floor)."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - low, mn)


def lp_ext_070_high_low_range_vs_252d_min(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - low) / 252-day rolling close min (daily range relative to multi-year floor)."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(high - low, mn)


def lp_ext_071_rolling_min_slope_21d(close: pd.Series) -> pd.Series:
    """Rate of change of 63-day rolling min over 21 days (falling floor = negative)."""
    mn = _rolling_min(close, _TD_QTR)
    return _safe_div(mn - mn.shift(_TD_MON), mn.shift(_TD_MON))


def lp_ext_072_rolling_min_slope_63d(close: pd.Series) -> pd.Series:
    """Rate of change of 252-day rolling min over 63 days (structural floor drift)."""
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(mn - mn.shift(_TD_QTR), mn.shift(_TD_QTR))


def lp_ext_073_rolling_min_acc_21d(close: pd.Series) -> pd.Series:
    """Second derivative of 63d rolling min: change in slope over 21 days."""
    mn    = _rolling_min(close, _TD_QTR)
    slope = _safe_div(mn - mn.shift(_TD_MON), mn.shift(_TD_MON))
    return slope - slope.shift(_TD_MON)


def lp_ext_074_prox_ewm_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of EWM(21) proximity-to-63d-min, evaluated over 63d window."""
    prox = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    sm   = _ewm_mean(prox, _TD_MON)
    return _zscore_rolling(sm, _TD_QTR)


def lp_ext_075_prox_vol_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling correlation between proximity-to-63d-min and volume."""
    prox = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return prox.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(volume)


# ── Registry ──────────────────────────────────────────────────────────────────

LOW_PROXIMITY_EXTENDED_REGISTRY_001_075 = {
    "lp_ext_001_log_dist_21d_min":               {"inputs": ["close"],                      "func": lp_ext_001_log_dist_21d_min},
    "lp_ext_002_log_dist_63d_min":               {"inputs": ["close"],                      "func": lp_ext_002_log_dist_63d_min},
    "lp_ext_003_log_dist_126d_min":              {"inputs": ["close"],                      "func": lp_ext_003_log_dist_126d_min},
    "lp_ext_004_log_dist_252d_min":              {"inputs": ["close"],                      "func": lp_ext_004_log_dist_252d_min},
    "lp_ext_005_log_dist_504d_min":              {"inputs": ["close"],                      "func": lp_ext_005_log_dist_504d_min},
    "lp_ext_006_log_dist_756d_min":              {"inputs": ["close"],                      "func": lp_ext_006_log_dist_756d_min},
    "lp_ext_007_log_dist_10d_min":               {"inputs": ["close"],                      "func": lp_ext_007_log_dist_10d_min},
    "lp_ext_008_log_dist_42d_min":               {"inputs": ["close"],                      "func": lp_ext_008_log_dist_42d_min},
    "lp_ext_009_log_dist_189d_min":              {"inputs": ["close"],                      "func": lp_ext_009_log_dist_189d_min},
    "lp_ext_010_log_dist_378d_min":              {"inputs": ["close"],                      "func": lp_ext_010_log_dist_378d_min},
    "lp_ext_011_atr_norm_dist_21d":              {"inputs": ["close", "high", "low"],       "func": lp_ext_011_atr_norm_dist_21d},
    "lp_ext_012_atr_norm_dist_63d":              {"inputs": ["close", "high", "low"],       "func": lp_ext_012_atr_norm_dist_63d},
    "lp_ext_013_atr_norm_dist_126d":             {"inputs": ["close", "high", "low"],       "func": lp_ext_013_atr_norm_dist_126d},
    "lp_ext_014_atr_norm_dist_252d":             {"inputs": ["close", "high", "low"],       "func": lp_ext_014_atr_norm_dist_252d},
    "lp_ext_015_atr_norm_dist_504d":             {"inputs": ["close", "high", "low"],       "func": lp_ext_015_atr_norm_dist_504d},
    "lp_ext_016_close_above_21d_low_min":        {"inputs": ["close", "low"],               "func": lp_ext_016_close_above_21d_low_min},
    "lp_ext_017_close_above_63d_low_min":        {"inputs": ["close", "low"],               "func": lp_ext_017_close_above_63d_low_min},
    "lp_ext_018_close_above_126d_low_min":       {"inputs": ["close", "low"],               "func": lp_ext_018_close_above_126d_low_min},
    "lp_ext_019_close_above_252d_low_min":       {"inputs": ["close", "low"],               "func": lp_ext_019_close_above_252d_low_min},
    "lp_ext_020_close_above_504d_low_min":       {"inputs": ["close", "low"],               "func": lp_ext_020_close_above_504d_low_min},
    "lp_ext_021_log_close_above_21d_low_min":    {"inputs": ["close", "low"],               "func": lp_ext_021_log_close_above_21d_low_min},
    "lp_ext_022_log_close_above_252d_low_min":   {"inputs": ["close", "low"],               "func": lp_ext_022_log_close_above_252d_low_min},
    "lp_ext_023_prox_pctrank_63d":               {"inputs": ["close"],                      "func": lp_ext_023_prox_pctrank_63d},
    "lp_ext_024_prox_pctrank_126d":              {"inputs": ["close"],                      "func": lp_ext_024_prox_pctrank_126d},
    "lp_ext_025_prox_pctrank_252d":              {"inputs": ["close"],                      "func": lp_ext_025_prox_pctrank_252d},
    "lp_ext_026_prox_pctrank_504d":              {"inputs": ["close"],                      "func": lp_ext_026_prox_pctrank_504d},
    "lp_ext_027_prox_pctrank_756d":              {"inputs": ["close"],                      "func": lp_ext_027_prox_pctrank_756d},
    "lp_ext_028_rolling_rank_63d":               {"inputs": ["close"],                      "func": lp_ext_028_rolling_rank_63d},
    "lp_ext_029_rolling_rank_252d":              {"inputs": ["close"],                      "func": lp_ext_029_rolling_rank_252d},
    "lp_ext_030_rolling_rank_504d":              {"inputs": ["close"],                      "func": lp_ext_030_rolling_rank_504d},
    "lp_ext_031_zscore_close_63d":               {"inputs": ["close"],                      "func": lp_ext_031_zscore_close_63d},
    "lp_ext_032_zscore_close_126d":              {"inputs": ["close"],                      "func": lp_ext_032_zscore_close_126d},
    "lp_ext_033_zscore_close_252d":              {"inputs": ["close"],                      "func": lp_ext_033_zscore_close_252d},
    "lp_ext_034_zscore_log_close_252d":          {"inputs": ["close"],                      "func": lp_ext_034_zscore_log_close_252d},
    "lp_ext_035_zscore_log_close_504d":          {"inputs": ["close"],                      "func": lp_ext_035_zscore_log_close_504d},
    "lp_ext_036_prox_zscore_21d_min":            {"inputs": ["close"],                      "func": lp_ext_036_prox_zscore_21d_min},
    "lp_ext_037_prox_zscore_63d_min":            {"inputs": ["close"],                      "func": lp_ext_037_prox_zscore_63d_min},
    "lp_ext_038_prox_zscore_252d_min":           {"inputs": ["close"],                      "func": lp_ext_038_prox_zscore_252d_min},
    "lp_ext_039_vol_weighted_prox_21d":          {"inputs": ["close", "volume"],            "func": lp_ext_039_vol_weighted_prox_21d},
    "lp_ext_040_vol_weighted_prox_63d":          {"inputs": ["close", "volume"],            "func": lp_ext_040_vol_weighted_prox_63d},
    "lp_ext_041_vol_weighted_prox_252d":         {"inputs": ["close", "volume"],            "func": lp_ext_041_vol_weighted_prox_252d},
    "lp_ext_042_vwap_vs_252d_min":               {"inputs": ["close", "volume"],            "func": lp_ext_042_vwap_vs_252d_min},
    "lp_ext_043_vwap_vs_63d_min":                {"inputs": ["close", "volume"],            "func": lp_ext_043_vwap_vs_63d_min},
    "lp_ext_044_high_vol_day_prox_63d":          {"inputs": ["close", "volume"],            "func": lp_ext_044_high_vol_day_prox_63d},
    "lp_ext_045_low_vol_day_prox_63d":           {"inputs": ["close", "volume"],            "func": lp_ext_045_low_vol_day_prox_63d},
    "lp_ext_046_ewm_prox_21d":                   {"inputs": ["close"],                      "func": lp_ext_046_ewm_prox_21d},
    "lp_ext_047_ewm_prox_63d":                   {"inputs": ["close"],                      "func": lp_ext_047_ewm_prox_63d},
    "lp_ext_048_ewm_log_prox_21d":               {"inputs": ["close"],                      "func": lp_ext_048_ewm_log_prox_21d},
    "lp_ext_049_ewm_log_prox_63d":               {"inputs": ["close"],                      "func": lp_ext_049_ewm_log_prox_63d},
    "lp_ext_050_ewm_prox_126d":                  {"inputs": ["close"],                      "func": lp_ext_050_ewm_prox_126d},
    "lp_ext_051_consec_days_within1pct_21d_min": {"inputs": ["close"],                      "func": lp_ext_051_consec_days_within1pct_21d_min},
    "lp_ext_052_consec_days_within1pct_63d_min": {"inputs": ["close"],                      "func": lp_ext_052_consec_days_within1pct_63d_min},
    "lp_ext_053_consec_days_within1pct_252d_min":{"inputs": ["close"],                      "func": lp_ext_053_consec_days_within1pct_252d_min},
    "lp_ext_054_consec_days_within5pct_252d_min":{"inputs": ["close"],                      "func": lp_ext_054_consec_days_within5pct_252d_min},
    "lp_ext_055_count_within2pct_63d_min_over_63d": {"inputs": ["close"],                   "func": lp_ext_055_count_within2pct_63d_min_over_63d},
    "lp_ext_056_count_within2pct_252d_min_over_252d": {"inputs": ["close"],                 "func": lp_ext_056_count_within2pct_252d_min_over_252d},
    "lp_ext_057_pct_days_near_floor_63d":        {"inputs": ["close"],                      "func": lp_ext_057_pct_days_near_floor_63d},
    "lp_ext_058_pct_days_near_floor_252d":       {"inputs": ["close"],                      "func": lp_ext_058_pct_days_near_floor_252d},
    "lp_ext_059_multi_window_prox_avg":          {"inputs": ["close"],                      "func": lp_ext_059_multi_window_prox_avg},
    "lp_ext_060_multi_window_prox_min":          {"inputs": ["close"],                      "func": lp_ext_060_multi_window_prox_min},
    "lp_ext_061_prox_ratio_21_to_252d":          {"inputs": ["close"],                      "func": lp_ext_061_prox_ratio_21_to_252d},
    "lp_ext_062_prox_ratio_63_to_504d":          {"inputs": ["close"],                      "func": lp_ext_062_prox_ratio_63_to_504d},
    "lp_ext_063_prox_acceleration_21_63d":       {"inputs": ["close"],                      "func": lp_ext_063_prox_acceleration_21_63d},
    "lp_ext_064_prox_momentum_21d":              {"inputs": ["close"],                      "func": lp_ext_064_prox_momentum_21d},
    "lp_ext_065_prox_momentum_63d":              {"inputs": ["close"],                      "func": lp_ext_065_prox_momentum_63d},
    "lp_ext_066_open_above_252d_min":            {"inputs": ["open", "close"],              "func": lp_ext_066_open_above_252d_min},
    "lp_ext_067_high_above_252d_min":            {"inputs": ["high", "close"],              "func": lp_ext_067_high_above_252d_min},
    "lp_ext_068_low_above_252d_min":             {"inputs": ["low", "close"],               "func": lp_ext_068_low_above_252d_min},
    "lp_ext_069_close_low_spread_vs_252d_min":   {"inputs": ["close", "low"],               "func": lp_ext_069_close_low_spread_vs_252d_min},
    "lp_ext_070_high_low_range_vs_252d_min":     {"inputs": ["high", "low", "close"],       "func": lp_ext_070_high_low_range_vs_252d_min},
    "lp_ext_071_rolling_min_slope_21d":          {"inputs": ["close"],                      "func": lp_ext_071_rolling_min_slope_21d},
    "lp_ext_072_rolling_min_slope_63d":          {"inputs": ["close"],                      "func": lp_ext_072_rolling_min_slope_63d},
    "lp_ext_073_rolling_min_acc_21d":            {"inputs": ["close"],                      "func": lp_ext_073_rolling_min_acc_21d},
    "lp_ext_074_prox_ewm_zscore_63d":            {"inputs": ["close"],                      "func": lp_ext_074_prox_ewm_zscore_63d},
    "lp_ext_075_prox_vol_corr_63d":              {"inputs": ["close", "volume"],            "func": lp_ext_075_prox_vol_corr_63d},
}
