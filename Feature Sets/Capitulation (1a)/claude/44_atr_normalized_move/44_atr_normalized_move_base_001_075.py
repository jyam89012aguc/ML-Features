"""
44_atr_normalized_move — Base Features 001-075
Domain: price moves expressed in ATR units — volatility-standardized move magnitudes
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prev_C|, |L-prev_C|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low - prev_c).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Rolling ATR over w periods."""
    return _rolling_mean(_tr(close, high, low), w)


def _atr_ewm(close: pd.Series, high: pd.Series, low: pd.Series, span: int) -> pd.Series:
    """EWM-smoothed ATR (Wilder style via ewm)."""
    return _ewm_mean(_tr(close, high, low), span)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Daily close-to-close move in ATR units ---

def atr_001_daily_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily close-to-close log-return divided by 14-day ATR (move in ATR14 units)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    return _safe_div(ret, atr)


def atr_002_daily_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily close-to-close log-return divided by 21-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(ret, atr)


def atr_003_daily_move_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily close-to-close log-return divided by 63-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, _TD_QTR)
    return _safe_div(ret, atr)


def atr_004_daily_move_atr_ewm14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return in EWM-ATR(14) units (Wilder-smoothed denominator)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    atr = _atr_ewm(close, high, low, 14)
    return _safe_div(ret, atr)


def atr_005_daily_abs_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute daily log-return in ATR14 units (unsigned move size)."""
    return atr_001_daily_move_atr14(close, high, low).abs()


def atr_006_daily_abs_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute daily log-return in ATR21 units."""
    return atr_002_daily_move_atr21(close, high, low).abs()


def atr_007_daily_down_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily down-move in ATR14 units; zero on up days."""
    raw = atr_001_daily_move_atr14(close, high, low)
    return raw.where(raw < 0, 0.0)


def atr_008_daily_up_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily up-move in ATR14 units; zero on down days."""
    raw = atr_001_daily_move_atr14(close, high, low)
    return raw.where(raw > 0, 0.0)


def atr_009_daily_move_atr14_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily ATR14-normalized move relative to 252-day history."""
    m = atr_001_daily_move_atr14(close, high, low)
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


def atr_010_daily_move_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's ATR14-normalized move in trailing 252-day window."""
    m = atr_001_daily_move_atr14(close, high, low)
    return m.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): N-day move in ATR units ---

def atr_011_5d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day log-return divided by 14-day ATR (weekly move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    atr = _atr(close, high, low, 14)
    return _safe_div(ret, atr)


def atr_012_21d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day log-return divided by 14-day ATR (monthly move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    atr = _atr(close, high, low, 14)
    return _safe_div(ret, atr)


def atr_013_63d_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day log-return divided by 21-day ATR (quarterly move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(ret, atr)


def atr_014_126d_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day log-return divided by 21-day ATR (half-year move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_HALF))
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(ret, atr)


def atr_015_252d_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day log-return divided by 21-day ATR (annual move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_YEAR))
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(ret, atr)


def atr_016_5d_abs_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute 5-day move in ATR14 units."""
    return atr_011_5d_move_atr14(close, high, low).abs()


def atr_017_21d_abs_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute 21-day move in ATR14 units."""
    return atr_012_21d_move_atr14(close, high, low).abs()


def atr_018_5d_move_atr5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day log-return divided by 5-day ATR (short-term normalized move)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    atr = _atr(close, high, low, _TD_WEEK)
    return _safe_div(ret, atr)


def atr_019_10d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day log-return divided by 14-day ATR (bi-weekly move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(10))
    atr = _atr(close, high, low, 14)
    return _safe_div(ret, atr)


def atr_020_63d_move_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day log-return divided by 63-day ATR (self-normalized quarterly move)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    atr = _atr(close, high, low, _TD_QTR)
    return _safe_div(ret, atr)


# --- Group C (021-030): Cumulative ATR-units traveled (path length) ---

def atr_021_cum_atr_traveled_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of absolute daily moves in ATR14 units over 5 days (path length)."""
    daily = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum(daily, _TD_WEEK)


def atr_022_cum_atr_traveled_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of absolute daily moves in ATR14 units over 21 days."""
    daily = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum(daily, _TD_MON)


def atr_023_cum_atr_traveled_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of absolute daily moves in ATR14 units over 63 days."""
    daily = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum(daily, _TD_QTR)


def atr_024_cum_atr_traveled_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of absolute daily moves in ATR14 units over 252 days."""
    daily = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum(daily, _TD_YEAR)


def atr_025_cum_down_atr_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative downward ATR-units traveled over 5 days (down path only)."""
    daily = atr_007_daily_down_move_atr14(close, high, low)
    return _rolling_sum(daily, _TD_WEEK)


def atr_026_cum_down_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative downward ATR-units traveled over 21 days."""
    daily = atr_007_daily_down_move_atr14(close, high, low)
    return _rolling_sum(daily, _TD_MON)


def atr_027_cum_down_atr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative downward ATR-units traveled over 63 days."""
    daily = atr_007_daily_down_move_atr14(close, high, low)
    return _rolling_sum(daily, _TD_QTR)


def atr_028_cum_up_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative upward ATR-units traveled over 21 days."""
    daily = atr_008_daily_up_move_atr14(close, high, low)
    return _rolling_sum(daily, _TD_MON)


def atr_029_down_vs_up_atr_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of cumulative down ATR-units to up ATR-units over 21 days."""
    down = atr_026_cum_down_atr_21d(close, high, low).abs()
    up = atr_028_cum_up_atr_21d(close, high, low).abs()
    return _safe_div(down, up)


def atr_030_down_vs_up_atr_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of cumulative down ATR-units to up ATR-units over 63 days."""
    daily_raw = atr_001_daily_move_atr14(close, high, low)
    down = daily_raw.where(daily_raw < 0, 0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum().abs()
    up = daily_raw.where(daily_raw > 0, 0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum().abs()
    return _safe_div(down, up)


# --- Group D (031-040): Distance from rolling high/low in ATR units ---

def atr_031_dist_from_52wk_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 252-day high expressed in ATR14 multiples."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_252, atr)


def atr_032_dist_from_52wk_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 252-day low expressed in ATR14 multiples."""
    low_252 = _rolling_min(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low_252, atr)


def atr_033_dist_from_21d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 21-day high in ATR14 units."""
    high_21 = _rolling_max(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_21, atr)


def atr_034_dist_from_21d_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 21-day low in ATR14 units."""
    low_21 = _rolling_min(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low_21, atr)


def atr_035_dist_from_63d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 63-day high in ATR14 units."""
    high_63 = _rolling_max(close, _TD_QTR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_63, atr)


def atr_036_dist_from_63d_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 63-day low in ATR14 units."""
    low_63 = _rolling_min(close, _TD_QTR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low_63, atr)


def atr_037_dist_from_126d_high_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 126-day high in ATR21 units."""
    high_126 = _rolling_max(close, _TD_HALF)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - high_126, atr)


def atr_038_dist_from_intraday_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below today's intraday high in ATR14 units."""
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high, atr)


def atr_039_dist_from_intraday_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above today's intraday low in ATR14 units."""
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low, atr)


def atr_040_dist_from_52wk_high_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 252-day high in ATR21 units."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - high_252, atr)


# --- Group E (041-050): ATR-normalized drawdown ---

def atr_041_drawdown_from_21d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown from 21-day rolling high expressed in ATR14 units (negative = below)."""
    high_21 = _rolling_max(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_21, atr)


def atr_042_drawdown_from_63d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown from 63-day rolling high in ATR14 units."""
    high_63 = _rolling_max(close, _TD_QTR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_63, atr)


def atr_043_drawdown_from_252d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown from 252-day rolling high in ATR14 units."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_252, atr)


def atr_044_drawdown_from_252d_high_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown from 252-day high normalized by longer 63-day ATR."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, _TD_QTR)
    return _safe_div(close - high_252, atr)


def atr_045_max_drawdown_atr14_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative daily ATR14-normalized move within trailing 21 days."""
    daily = atr_001_daily_move_atr14(close, high, low)
    return _rolling_min(daily, _TD_MON)


def atr_046_max_drawdown_atr14_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative daily ATR14-normalized move within trailing 63 days."""
    daily = atr_001_daily_move_atr14(close, high, low)
    return _rolling_min(daily, _TD_QTR)


def atr_047_max_drawdown_atr14_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Most negative daily ATR14-normalized move within trailing 252 days."""
    daily = atr_001_daily_move_atr14(close, high, low)
    return _rolling_min(daily, _TD_YEAR)


def atr_048_drawdown_vs_max_drawdown_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's ATR14 drawdown vs 252-day worst (ratio; 1.0 = new extreme)."""
    daily = atr_001_daily_move_atr14(close, high, low)
    worst = _rolling_min(daily, _TD_YEAR)
    return _safe_div(daily, worst.abs())


def atr_049_drawdown_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's ATR14-move in trailing 252-day down-move distribution."""
    daily = atr_001_daily_move_atr14(close, high, low)
    return daily.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_050_drawdown_from_63d_high_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown from 63-day high in ATR21 units."""
    high_63 = _rolling_max(close, _TD_QTR)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - high_63, atr)


# --- Group F (051-060): Count of extreme ATR moves ---

def atr_051_count_gt2atr_moves_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with |daily move| > 2 ATR14 units in trailing 21 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum((m > 2).astype(float), _TD_MON)


def atr_052_count_gt3atr_moves_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with |daily move| > 3 ATR14 units in trailing 21 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum((m > 3).astype(float), _TD_MON)


def atr_053_count_gt2atr_moves_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with |daily move| > 2 ATR14 units in trailing 63 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum((m > 2).astype(float), _TD_QTR)


def atr_054_count_gt3atr_moves_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with |daily move| > 3 ATR14 units in trailing 63 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum((m > 3).astype(float), _TD_QTR)


def atr_055_count_gt2atr_moves_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with |daily move| > 2 ATR14 units in trailing 252 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_sum((m > 2).astype(float), _TD_YEAR)


def atr_056_count_gt2atr_down_moves_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of down days with move < -2 ATR14 units in trailing 21 days."""
    m = atr_001_daily_move_atr14(close, high, low)
    return _rolling_sum((m < -2).astype(float), _TD_MON)


def atr_057_count_gt2atr_down_moves_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of down days with move < -2 ATR14 units in trailing 63 days."""
    m = atr_001_daily_move_atr14(close, high, low)
    return _rolling_sum((m < -2).astype(float), _TD_QTR)


def atr_058_count_gt3atr_down_moves_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of down days with move < -3 ATR14 units in trailing 252 days."""
    m = atr_001_daily_move_atr14(close, high, low)
    return _rolling_sum((m < -3).astype(float), _TD_YEAR)


def atr_059_extreme_move_flag_gt2atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's |move| exceeds 2 ATR14 units."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return (m > 2).astype(float)


def atr_060_extreme_down_move_flag_gt2atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's down-move exceeds -2 ATR14 units."""
    m = atr_001_daily_move_atr14(close, high, low)
    return (m < -2).astype(float)


# --- Group G (061-075): ATR-units below moving averages and velocity ---

def atr_061_dist_below_sma21_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 21-day SMA in ATR14 units (negative = above MA)."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr)


def atr_062_dist_below_sma50_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 50-day SMA in ATR14 units."""
    ma = _rolling_mean(close, 50)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr)


def atr_063_dist_below_sma200_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 200-day SMA in ATR14 units."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr)


def atr_064_dist_below_ema21_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 21-day EMA in ATR14 units."""
    ema = _ewm_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ema, atr)


def atr_065_dist_below_ema63_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 63-day EMA in ATR14 units."""
    ema = _ewm_mean(close, _TD_QTR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ema, atr)


def atr_066_dist_below_sma200_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 200-day SMA in ATR21 units (alternative smoothing)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - ma, atr)


def atr_067_dist_below_sma63_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 63-day SMA in ATR14 units."""
    ma = _rolling_mean(close, _TD_QTR)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ma, atr)


def atr_068_dist_below_sma21_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 21-day SMA in ATR21 units (matched-window normalization)."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - ma, atr)


def atr_069_dist_below_ema200_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below 200-day EMA in ATR14 units."""
    ema = _ewm_mean(close, 200)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - ema, atr)


def atr_070_dist_below_sma200_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of SMA200 ATR14-distance in trailing 252-day window."""
    dist = atr_063_dist_below_sma200_atr14(close, high, low)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_071_largest_atr14_move_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Largest single-day |move| in ATR14 units within trailing 5 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_max(m, _TD_WEEK)


def atr_072_largest_atr14_move_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Largest single-day |move| in ATR14 units within trailing 21 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_max(m, _TD_MON)


def atr_073_largest_atr14_move_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Largest single-day |move| in ATR14 units within trailing 63 days."""
    m = atr_001_daily_move_atr14(close, high, low).abs()
    return _rolling_max(m, _TD_QTR)


def atr_074_largest_down_atr14_move_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Largest single-day down move (most negative) in ATR14 units in trailing 63 days."""
    m = atr_001_daily_move_atr14(close, high, low)
    return _rolling_min(m, _TD_QTR)


def atr_075_atr_velocity_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rolling mean of signed ATR14-normalized daily moves (ATR-unit velocity)."""
    m = atr_001_daily_move_atr14(close, high, low)
    return _rolling_mean(m, _TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_REGISTRY_001_075 = {
    "atr_001_daily_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_001_daily_move_atr14},
    "atr_002_daily_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_002_daily_move_atr21},
    "atr_003_daily_move_atr63": {"inputs": ["close", "high", "low"], "func": atr_003_daily_move_atr63},
    "atr_004_daily_move_atr_ewm14": {"inputs": ["close", "high", "low"], "func": atr_004_daily_move_atr_ewm14},
    "atr_005_daily_abs_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_005_daily_abs_move_atr14},
    "atr_006_daily_abs_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_006_daily_abs_move_atr21},
    "atr_007_daily_down_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_007_daily_down_move_atr14},
    "atr_008_daily_up_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_008_daily_up_move_atr14},
    "atr_009_daily_move_atr14_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_009_daily_move_atr14_zscore_252d},
    "atr_010_daily_move_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_010_daily_move_atr14_pct_rank_252d},
    "atr_011_5d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_011_5d_move_atr14},
    "atr_012_21d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_012_21d_move_atr14},
    "atr_013_63d_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_013_63d_move_atr21},
    "atr_014_126d_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_014_126d_move_atr21},
    "atr_015_252d_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_015_252d_move_atr21},
    "atr_016_5d_abs_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_016_5d_abs_move_atr14},
    "atr_017_21d_abs_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_017_21d_abs_move_atr14},
    "atr_018_5d_move_atr5": {"inputs": ["close", "high", "low"], "func": atr_018_5d_move_atr5},
    "atr_019_10d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_019_10d_move_atr14},
    "atr_020_63d_move_atr63": {"inputs": ["close", "high", "low"], "func": atr_020_63d_move_atr63},
    "atr_021_cum_atr_traveled_5d": {"inputs": ["close", "high", "low"], "func": atr_021_cum_atr_traveled_5d},
    "atr_022_cum_atr_traveled_21d": {"inputs": ["close", "high", "low"], "func": atr_022_cum_atr_traveled_21d},
    "atr_023_cum_atr_traveled_63d": {"inputs": ["close", "high", "low"], "func": atr_023_cum_atr_traveled_63d},
    "atr_024_cum_atr_traveled_252d": {"inputs": ["close", "high", "low"], "func": atr_024_cum_atr_traveled_252d},
    "atr_025_cum_down_atr_5d": {"inputs": ["close", "high", "low"], "func": atr_025_cum_down_atr_5d},
    "atr_026_cum_down_atr_21d": {"inputs": ["close", "high", "low"], "func": atr_026_cum_down_atr_21d},
    "atr_027_cum_down_atr_63d": {"inputs": ["close", "high", "low"], "func": atr_027_cum_down_atr_63d},
    "atr_028_cum_up_atr_21d": {"inputs": ["close", "high", "low"], "func": atr_028_cum_up_atr_21d},
    "atr_029_down_vs_up_atr_ratio_21d": {"inputs": ["close", "high", "low"], "func": atr_029_down_vs_up_atr_ratio_21d},
    "atr_030_down_vs_up_atr_ratio_63d": {"inputs": ["close", "high", "low"], "func": atr_030_down_vs_up_atr_ratio_63d},
    "atr_031_dist_from_52wk_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_031_dist_from_52wk_high_atr14},
    "atr_032_dist_from_52wk_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_032_dist_from_52wk_low_atr14},
    "atr_033_dist_from_21d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_033_dist_from_21d_high_atr14},
    "atr_034_dist_from_21d_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_034_dist_from_21d_low_atr14},
    "atr_035_dist_from_63d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_035_dist_from_63d_high_atr14},
    "atr_036_dist_from_63d_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_036_dist_from_63d_low_atr14},
    "atr_037_dist_from_126d_high_atr21": {"inputs": ["close", "high", "low"], "func": atr_037_dist_from_126d_high_atr21},
    "atr_038_dist_from_intraday_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_038_dist_from_intraday_high_atr14},
    "atr_039_dist_from_intraday_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_039_dist_from_intraday_low_atr14},
    "atr_040_dist_from_52wk_high_atr21": {"inputs": ["close", "high", "low"], "func": atr_040_dist_from_52wk_high_atr21},
    "atr_041_drawdown_from_21d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_041_drawdown_from_21d_high_atr14},
    "atr_042_drawdown_from_63d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_042_drawdown_from_63d_high_atr14},
    "atr_043_drawdown_from_252d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_043_drawdown_from_252d_high_atr14},
    "atr_044_drawdown_from_252d_high_atr63": {"inputs": ["close", "high", "low"], "func": atr_044_drawdown_from_252d_high_atr63},
    "atr_045_max_drawdown_atr14_21d": {"inputs": ["close", "high", "low"], "func": atr_045_max_drawdown_atr14_21d},
    "atr_046_max_drawdown_atr14_63d": {"inputs": ["close", "high", "low"], "func": atr_046_max_drawdown_atr14_63d},
    "atr_047_max_drawdown_atr14_252d": {"inputs": ["close", "high", "low"], "func": atr_047_max_drawdown_atr14_252d},
    "atr_048_drawdown_vs_max_drawdown_252d": {"inputs": ["close", "high", "low"], "func": atr_048_drawdown_vs_max_drawdown_252d},
    "atr_049_drawdown_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_049_drawdown_atr14_pct_rank_252d},
    "atr_050_drawdown_from_63d_high_atr21": {"inputs": ["close", "high", "low"], "func": atr_050_drawdown_from_63d_high_atr21},
    "atr_051_count_gt2atr_moves_21d": {"inputs": ["close", "high", "low"], "func": atr_051_count_gt2atr_moves_21d},
    "atr_052_count_gt3atr_moves_21d": {"inputs": ["close", "high", "low"], "func": atr_052_count_gt3atr_moves_21d},
    "atr_053_count_gt2atr_moves_63d": {"inputs": ["close", "high", "low"], "func": atr_053_count_gt2atr_moves_63d},
    "atr_054_count_gt3atr_moves_63d": {"inputs": ["close", "high", "low"], "func": atr_054_count_gt3atr_moves_63d},
    "atr_055_count_gt2atr_moves_252d": {"inputs": ["close", "high", "low"], "func": atr_055_count_gt2atr_moves_252d},
    "atr_056_count_gt2atr_down_moves_21d": {"inputs": ["close", "high", "low"], "func": atr_056_count_gt2atr_down_moves_21d},
    "atr_057_count_gt2atr_down_moves_63d": {"inputs": ["close", "high", "low"], "func": atr_057_count_gt2atr_down_moves_63d},
    "atr_058_count_gt3atr_down_moves_252d": {"inputs": ["close", "high", "low"], "func": atr_058_count_gt3atr_down_moves_252d},
    "atr_059_extreme_move_flag_gt2atr": {"inputs": ["close", "high", "low"], "func": atr_059_extreme_move_flag_gt2atr},
    "atr_060_extreme_down_move_flag_gt2atr": {"inputs": ["close", "high", "low"], "func": atr_060_extreme_down_move_flag_gt2atr},
    "atr_061_dist_below_sma21_atr14": {"inputs": ["close", "high", "low"], "func": atr_061_dist_below_sma21_atr14},
    "atr_062_dist_below_sma50_atr14": {"inputs": ["close", "high", "low"], "func": atr_062_dist_below_sma50_atr14},
    "atr_063_dist_below_sma200_atr14": {"inputs": ["close", "high", "low"], "func": atr_063_dist_below_sma200_atr14},
    "atr_064_dist_below_ema21_atr14": {"inputs": ["close", "high", "low"], "func": atr_064_dist_below_ema21_atr14},
    "atr_065_dist_below_ema63_atr14": {"inputs": ["close", "high", "low"], "func": atr_065_dist_below_ema63_atr14},
    "atr_066_dist_below_sma200_atr21": {"inputs": ["close", "high", "low"], "func": atr_066_dist_below_sma200_atr21},
    "atr_067_dist_below_sma63_atr14": {"inputs": ["close", "high", "low"], "func": atr_067_dist_below_sma63_atr14},
    "atr_068_dist_below_sma21_atr21": {"inputs": ["close", "high", "low"], "func": atr_068_dist_below_sma21_atr21},
    "atr_069_dist_below_ema200_atr14": {"inputs": ["close", "high", "low"], "func": atr_069_dist_below_ema200_atr14},
    "atr_070_dist_below_sma200_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_070_dist_below_sma200_pct_rank_252d},
    "atr_071_largest_atr14_move_5d": {"inputs": ["close", "high", "low"], "func": atr_071_largest_atr14_move_5d},
    "atr_072_largest_atr14_move_21d": {"inputs": ["close", "high", "low"], "func": atr_072_largest_atr14_move_21d},
    "atr_073_largest_atr14_move_63d": {"inputs": ["close", "high", "low"], "func": atr_073_largest_atr14_move_63d},
    "atr_074_largest_down_atr14_move_63d": {"inputs": ["close", "high", "low"], "func": atr_074_largest_down_atr14_move_63d},
    "atr_075_atr_velocity_5d": {"inputs": ["close", "high", "low"], "func": atr_075_atr_velocity_5d},
}
