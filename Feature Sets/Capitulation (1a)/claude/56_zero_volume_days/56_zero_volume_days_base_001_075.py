"""
56_zero_volume_days — Base Features 001-075
Domain: zero-volume / near-zero-volume days and stale-price (unchanged close) sessions
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — dead/illiquid sessions, no-trade and stale-price frequency
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
_NEAR_ZERO_K = 0.05   # volume < 5% of trailing median => "near-zero"
_STALE_TOL = 1e-8     # |close - prior_close| < this => stale price

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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: group id increments on each False; cumsum within group."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (scalar apply)."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _zero_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: volume == 0."""
    return (volume == 0).astype(float)


def _near_zero_vol_flag(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Binary flag: volume < _NEAR_ZERO_K * trailing-median volume (near-zero)."""
    med = _rolling_median(volume.shift(1), w)
    return (volume < _NEAR_ZERO_K * med.clip(lower=_EPS)).astype(float)


def _stale_price_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is unchanged from prior close (stale price)."""
    return (close.diff(1).abs() < _STALE_TOL).astype(float)


def _days_since_last_true(cond: pd.Series) -> pd.Series:
    """Days elapsed since the last True event (backward-looking)."""
    idx = np.arange(len(cond))
    last = pd.Series(np.nan, index=cond.index, dtype=float)
    last_true = np.full(len(cond), np.nan)
    prev = np.nan
    for i, v in enumerate(cond):
        if v:
            prev = idx[i]
        last_true[i] = prev
    result = idx - np.where(np.isnan(last_true), np.nan, last_true)
    return pd.Series(result, index=cond.index, dtype=float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Zero-volume day flag and basic counts ---

def zvd_001_zero_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's volume is exactly zero."""
    return _zero_vol_flag(volume)


def zvd_002_zero_vol_count_5d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in the trailing 5-day window."""
    return _rolling_count_true(volume == 0, _TD_WEEK)


def zvd_003_zero_vol_count_21d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in the trailing 21-day window."""
    return _rolling_count_true(volume == 0, _TD_MON)


def zvd_004_zero_vol_count_63d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in the trailing 63-day window."""
    return _rolling_count_true(volume == 0, _TD_QTR)


def zvd_005_zero_vol_count_126d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in the trailing 126-day window."""
    return _rolling_count_true(volume == 0, _TD_HALF)


def zvd_006_zero_vol_count_252d(volume: pd.Series) -> pd.Series:
    """Count of zero-volume days in the trailing 252-day window."""
    return _rolling_count_true(volume == 0, _TD_YEAR)


def zvd_007_zero_vol_frac_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with zero volume."""
    return zvd_003_zero_vol_count_21d(volume) / _TD_MON


def zvd_008_zero_vol_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero volume."""
    return zvd_004_zero_vol_count_63d(volume) / _TD_QTR


def zvd_009_zero_vol_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero volume."""
    return zvd_006_zero_vol_count_252d(volume) / _TD_YEAR


def zvd_010_zero_vol_expanding_count(volume: pd.Series) -> pd.Series:
    """Expanding total count of zero-volume days (all-history)."""
    return _zero_vol_flag(volume).expanding(min_periods=1).sum()


# --- Group B (011-020): Near-zero volume days (< 5% of trailing median) ---

def zvd_011_near_zero_vol_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: volume below 5% of 21-day trailing median (near-zero)."""
    return _near_zero_vol_flag(volume, _TD_MON)


def zvd_012_near_zero_vol_flag_63d_med(volume: pd.Series) -> pd.Series:
    """Binary flag: volume below 5% of 63-day trailing median volume."""
    return _near_zero_vol_flag(volume, _TD_QTR)


def zvd_013_near_zero_vol_count_5d(volume: pd.Series) -> pd.Series:
    """Count of near-zero-volume days in the trailing 5-day window."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_WEEK)


def zvd_014_near_zero_vol_count_21d(volume: pd.Series) -> pd.Series:
    """Count of near-zero-volume days in the trailing 21-day window."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_MON)


def zvd_015_near_zero_vol_count_63d(volume: pd.Series) -> pd.Series:
    """Count of near-zero-volume days in the trailing 63-day window."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_QTR)


def zvd_016_near_zero_vol_count_252d(volume: pd.Series) -> pd.Series:
    """Count of near-zero-volume days in the trailing 252-day window."""
    return _rolling_count_true(_near_zero_vol_flag(volume, _TD_MON) == 1, _TD_YEAR)


def zvd_017_near_zero_vol_frac_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with near-zero volume."""
    return zvd_014_near_zero_vol_count_21d(volume) / _TD_MON


def zvd_018_near_zero_vol_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with near-zero volume."""
    return zvd_015_near_zero_vol_count_63d(volume) / _TD_QTR


def zvd_019_near_zero_vol_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with near-zero volume."""
    return zvd_016_near_zero_vol_count_252d(volume) / _TD_YEAR


def zvd_020_zero_or_near_zero_vol_frac_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days that are zero or near-zero volume."""
    zflag = _zero_vol_flag(volume)
    nzflag = _near_zero_vol_flag(volume, _TD_MON)
    combined = ((zflag + nzflag) > 0).astype(float)
    return _rolling_sum(combined, _TD_MON) / _TD_MON


# --- Group C (021-030): Stale-price (unchanged close) day counts ---

def zvd_021_stale_price_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is exactly unchanged from prior close (stale price day)."""
    return _stale_price_flag(close)


def zvd_022_stale_price_count_5d(close: pd.Series) -> pd.Series:
    """Count of stale-price days in trailing 5-day window."""
    return _rolling_count_true(_stale_price_flag(close) == 1, _TD_WEEK)


def zvd_023_stale_price_count_21d(close: pd.Series) -> pd.Series:
    """Count of stale-price days in trailing 21-day window."""
    return _rolling_count_true(_stale_price_flag(close) == 1, _TD_MON)


def zvd_024_stale_price_count_63d(close: pd.Series) -> pd.Series:
    """Count of stale-price days in trailing 63-day window."""
    return _rolling_count_true(_stale_price_flag(close) == 1, _TD_QTR)


def zvd_025_stale_price_count_126d(close: pd.Series) -> pd.Series:
    """Count of stale-price days in trailing 126-day window."""
    return _rolling_count_true(_stale_price_flag(close) == 1, _TD_HALF)


def zvd_026_stale_price_count_252d(close: pd.Series) -> pd.Series:
    """Count of stale-price days in trailing 252-day window."""
    return _rolling_count_true(_stale_price_flag(close) == 1, _TD_YEAR)


def zvd_027_stale_price_frac_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with unchanged close price."""
    return zvd_023_stale_price_count_21d(close) / _TD_MON


def zvd_028_stale_price_frac_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days with unchanged close price."""
    return zvd_024_stale_price_count_63d(close) / _TD_QTR


def zvd_029_stale_price_frac_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days with unchanged close price."""
    return zvd_026_stale_price_count_252d(close) / _TD_YEAR


def zvd_030_stale_price_expanding_count(close: pd.Series) -> pd.Series:
    """Expanding total count of stale-price days (all-history)."""
    return _stale_price_flag(close).expanding(min_periods=1).sum()


# --- Group D (031-040): Consecutive zero/stale streaks ---

def zvd_031_consec_zero_vol_current(volume: pd.Series) -> pd.Series:
    """Current run of consecutive zero-volume days (backward-looking streak)."""
    return _consec_streak(volume == 0)


def zvd_032_consec_near_zero_vol_current(volume: pd.Series) -> pd.Series:
    """Current run of consecutive near-zero-volume days."""
    return _consec_streak(_near_zero_vol_flag(volume, _TD_MON) == 1)


def zvd_033_consec_stale_price_current(close: pd.Series) -> pd.Series:
    """Current run of consecutive stale-price (unchanged close) days."""
    return _consec_streak(_stale_price_flag(close) == 1)


def zvd_034_consec_zero_or_stale_current(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current run of consecutive days that are either zero-volume or stale-price."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0)
    return _consec_streak(dead)


def zvd_035_max_zero_vol_streak_21d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive zero-volume run in trailing 21-day window."""
    return _rolling_max_streak(volume == 0, _TD_MON)


def zvd_036_max_zero_vol_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive zero-volume run in trailing 63-day window."""
    return _rolling_max_streak(volume == 0, _TD_QTR)


def zvd_037_max_zero_vol_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive zero-volume run in trailing 252-day window."""
    return _rolling_max_streak(volume == 0, _TD_YEAR)


def zvd_038_max_stale_price_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive stale-price run in trailing 21-day window."""
    return _rolling_max_streak(_stale_price_flag(close) == 1, _TD_MON)


def zvd_039_max_stale_price_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive stale-price run in trailing 63-day window."""
    return _rolling_max_streak(_stale_price_flag(close) == 1, _TD_QTR)


def zvd_040_max_stale_price_streak_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive stale-price run in trailing 252-day window."""
    return _rolling_max_streak(_stale_price_flag(close) == 1, _TD_YEAR)


# --- Group E (041-050): Days-since-last zero/stale event ---

def zvd_041_days_since_last_zero_vol(volume: pd.Series) -> pd.Series:
    """Days elapsed since the most recent zero-volume day (backward-looking)."""
    return _days_since_last_true(volume == 0)


def zvd_042_days_since_last_near_zero_vol(volume: pd.Series) -> pd.Series:
    """Days elapsed since the most recent near-zero-volume day."""
    return _days_since_last_true(_near_zero_vol_flag(volume, _TD_MON) == 1)


def zvd_043_days_since_last_stale_price(close: pd.Series) -> pd.Series:
    """Days elapsed since the most recent stale-price (unchanged close) day."""
    return _days_since_last_true(_stale_price_flag(close) == 1)


def zvd_044_days_since_last_zero_vol_log(volume: pd.Series) -> pd.Series:
    """Log1p of days-since-last-zero-volume (compresses right tail)."""
    return np.log1p(zvd_041_days_since_last_zero_vol(volume))


def zvd_045_days_since_last_stale_log(close: pd.Series) -> pd.Series:
    """Log1p of days-since-last-stale-price."""
    return np.log1p(zvd_043_days_since_last_stale_price(close))


def zvd_046_days_since_zero_vol_norm_252d(volume: pd.Series) -> pd.Series:
    """Days-since-last-zero-vol normalized by 252-day average gap between events."""
    raw = zvd_041_days_since_last_zero_vol(volume)
    avg = _rolling_mean(raw, _TD_YEAR)
    return _safe_div(raw, avg)


def zvd_047_days_since_stale_norm_252d(close: pd.Series) -> pd.Series:
    """Days-since-last-stale normalized by 252-day average gap."""
    raw = zvd_043_days_since_last_stale_price(close)
    avg = _rolling_mean(raw, _TD_YEAR)
    return _safe_div(raw, avg)


def zvd_048_days_since_zero_vol_gt21_flag(volume: pd.Series) -> pd.Series:
    """Flag: no zero-volume day in the last 21 days (very illiquid-free period)."""
    return (zvd_041_days_since_last_zero_vol(volume) > _TD_MON).astype(float)


def zvd_049_days_since_stale_gt21_flag(close: pd.Series) -> pd.Series:
    """Flag: no stale-price day in the last 21 days."""
    return (zvd_043_days_since_last_stale_price(close) > _TD_MON).astype(float)


def zvd_050_days_since_zero_or_stale(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last day that was either zero-volume or stale-price."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0)
    return _days_since_last_true(dead)


# --- Group F (051-060): Dead-session clustering and doji-of-volume frequency ---

def zvd_051_zero_vol_cluster_5d_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day zero-vol count to 21-day zero-vol count (clustering)."""
    c5 = zvd_002_zero_vol_count_5d(volume)
    c21 = zvd_003_zero_vol_count_21d(volume)
    return _safe_div(c5, c21)


def zvd_052_stale_cluster_5d_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day stale-price count to 21-day stale-price count (clustering)."""
    c5 = zvd_022_stale_price_count_5d(close)
    c21 = zvd_023_stale_price_count_21d(close)
    return _safe_div(c5, c21)


def zvd_053_dead_session_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days classified as dead (zero-vol OR stale-price)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_MON) / _TD_MON


def zvd_054_dead_session_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days classified as dead (zero-vol OR stale-price)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_QTR) / _TD_QTR


def zvd_055_dead_session_frac_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days classified as dead (zero-vol OR stale-price)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_HALF) / _TD_HALF


def zvd_056_dead_session_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days classified as dead (zero-vol OR stale-price)."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    return _rolling_sum(dead, _TD_YEAR) / _TD_YEAR


def zvd_057_doji_volume_flag(close: pd.Series, open: pd.Series,
                              high: pd.Series, low: pd.Series,
                              volume: pd.Series) -> pd.Series:
    """Flag: flat OHLC doji-of-volume day (OHLC all equal AND near-zero volume)."""
    flat_price = ((high - low).abs() < _STALE_TOL) & ((open - close).abs() < _STALE_TOL)
    near_zero = _near_zero_vol_flag(volume, _TD_MON) == 1
    return (flat_price & near_zero).astype(float)


def zvd_058_doji_volume_count_21d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Count of doji-of-volume (flat OHLC + near-zero volume) days in 21-day window."""
    doji = zvd_057_doji_volume_flag(close, open, high, low, volume)
    return _rolling_sum(doji, _TD_MON)


def zvd_059_doji_volume_count_63d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Count of doji-of-volume days in 63-day window."""
    doji = zvd_057_doji_volume_flag(close, open, high, low, volume)
    return _rolling_sum(doji, _TD_QTR)


def zvd_060_doji_volume_frac_252d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days that are doji-of-volume sessions."""
    doji = zvd_057_doji_volume_flag(close, open, high, low, volume)
    return _rolling_sum(doji, _TD_YEAR) / _TD_YEAR


# --- Group G (061-075): Relative volume ratios, z-scores, and combined dead metrics ---

def zvd_061_vol_pct_of_trailing_median_21d(volume: pd.Series) -> pd.Series:
    """Today's volume as a fraction of 21-day trailing median volume."""
    med = _rolling_median(volume.shift(1), _TD_MON)
    return _safe_div(volume, med.clip(lower=_EPS))


def zvd_062_vol_pct_of_trailing_median_63d(volume: pd.Series) -> pd.Series:
    """Today's volume as a fraction of 63-day trailing median volume."""
    med = _rolling_median(volume.shift(1), _TD_QTR)
    return _safe_div(volume, med.clip(lower=_EPS))


def zvd_063_vol_pct_of_trailing_median_252d(volume: pd.Series) -> pd.Series:
    """Today's volume as a fraction of 252-day trailing median volume."""
    med = _rolling_median(volume.shift(1), _TD_YEAR)
    return _safe_div(volume, med.clip(lower=_EPS))


def zvd_064_zero_vol_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 252-day volume series."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def zvd_065_vol_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of today's volume relative to 63-day rolling mean and std."""
    mu = _rolling_mean(volume.shift(1), _TD_QTR)
    sigma = _rolling_std(volume.shift(1), _TD_QTR)
    return _safe_div(volume - mu, sigma)


def zvd_066_vol_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of today's volume relative to 252-day rolling mean and std."""
    mu = _rolling_mean(volume.shift(1), _TD_YEAR)
    sigma = _rolling_std(volume.shift(1), _TD_YEAR)
    return _safe_div(volume - mu, sigma)


def zvd_067_stale_and_zero_same_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: simultaneously zero volume AND stale price (double dead-session signal)."""
    return (_zero_vol_flag(volume) * _stale_price_flag(close))


def zvd_068_stale_and_near_zero_same_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: simultaneously near-zero volume AND stale price."""
    return (_near_zero_vol_flag(volume, _TD_MON) * _stale_price_flag(close))


def zvd_069_zero_vol_after_stale_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: zero-volume day immediately following a stale-price day."""
    return (_zero_vol_flag(volume) * _stale_price_flag(close).shift(1)).fillna(0.0)


def zvd_070_stale_after_zero_vol_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: stale-price day immediately following a zero-volume day."""
    return (_stale_price_flag(close) * _zero_vol_flag(volume).shift(1)).fillna(0.0)


def zvd_071_near_zero_vol_expanding_frac(volume: pd.Series) -> pd.Series:
    """Expanding fraction of all days with near-zero volume (all-history)."""
    nz = _near_zero_vol_flag(volume, _TD_MON)
    count = nz.expanding(min_periods=1).sum()
    total = pd.Series(np.arange(1, len(volume) + 1), index=volume.index, dtype=float)
    return _safe_div(count, total)


def zvd_072_stale_price_expanding_frac(close: pd.Series) -> pd.Series:
    """Expanding fraction of all days with stale price (all-history)."""
    sp = _stale_price_flag(close)
    count = sp.expanding(min_periods=1).sum()
    total = pd.Series(np.arange(1, len(close) + 1), index=close.index, dtype=float)
    return _safe_div(count, total)


def zvd_073_dead_session_count_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day dead-session count within 252-day history."""
    dead = ((_zero_vol_flag(volume) + _stale_price_flag(close)) > 0).astype(float)
    cnt21 = _rolling_sum(dead, _TD_MON)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def zvd_074_near_zero_vol_count_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day near-zero-vol count within trailing 252 days."""
    cnt21 = zvd_014_near_zero_vol_count_21d(volume)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def zvd_075_stale_price_count_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day stale-price count within trailing 252 days."""
    cnt21 = zvd_023_stale_price_count_21d(close)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

ZERO_VOLUME_DAYS_REGISTRY_001_075 = {
    "zvd_001_zero_vol_flag": {"inputs": ["volume"], "func": zvd_001_zero_vol_flag},
    "zvd_002_zero_vol_count_5d": {"inputs": ["volume"], "func": zvd_002_zero_vol_count_5d},
    "zvd_003_zero_vol_count_21d": {"inputs": ["volume"], "func": zvd_003_zero_vol_count_21d},
    "zvd_004_zero_vol_count_63d": {"inputs": ["volume"], "func": zvd_004_zero_vol_count_63d},
    "zvd_005_zero_vol_count_126d": {"inputs": ["volume"], "func": zvd_005_zero_vol_count_126d},
    "zvd_006_zero_vol_count_252d": {"inputs": ["volume"], "func": zvd_006_zero_vol_count_252d},
    "zvd_007_zero_vol_frac_21d": {"inputs": ["volume"], "func": zvd_007_zero_vol_frac_21d},
    "zvd_008_zero_vol_frac_63d": {"inputs": ["volume"], "func": zvd_008_zero_vol_frac_63d},
    "zvd_009_zero_vol_frac_252d": {"inputs": ["volume"], "func": zvd_009_zero_vol_frac_252d},
    "zvd_010_zero_vol_expanding_count": {"inputs": ["volume"], "func": zvd_010_zero_vol_expanding_count},
    "zvd_011_near_zero_vol_flag": {"inputs": ["volume"], "func": zvd_011_near_zero_vol_flag},
    "zvd_012_near_zero_vol_flag_63d_med": {"inputs": ["volume"], "func": zvd_012_near_zero_vol_flag_63d_med},
    "zvd_013_near_zero_vol_count_5d": {"inputs": ["volume"], "func": zvd_013_near_zero_vol_count_5d},
    "zvd_014_near_zero_vol_count_21d": {"inputs": ["volume"], "func": zvd_014_near_zero_vol_count_21d},
    "zvd_015_near_zero_vol_count_63d": {"inputs": ["volume"], "func": zvd_015_near_zero_vol_count_63d},
    "zvd_016_near_zero_vol_count_252d": {"inputs": ["volume"], "func": zvd_016_near_zero_vol_count_252d},
    "zvd_017_near_zero_vol_frac_21d": {"inputs": ["volume"], "func": zvd_017_near_zero_vol_frac_21d},
    "zvd_018_near_zero_vol_frac_63d": {"inputs": ["volume"], "func": zvd_018_near_zero_vol_frac_63d},
    "zvd_019_near_zero_vol_frac_252d": {"inputs": ["volume"], "func": zvd_019_near_zero_vol_frac_252d},
    "zvd_020_zero_or_near_zero_vol_frac_21d": {"inputs": ["volume"], "func": zvd_020_zero_or_near_zero_vol_frac_21d},
    "zvd_021_stale_price_flag": {"inputs": ["close"], "func": zvd_021_stale_price_flag},
    "zvd_022_stale_price_count_5d": {"inputs": ["close"], "func": zvd_022_stale_price_count_5d},
    "zvd_023_stale_price_count_21d": {"inputs": ["close"], "func": zvd_023_stale_price_count_21d},
    "zvd_024_stale_price_count_63d": {"inputs": ["close"], "func": zvd_024_stale_price_count_63d},
    "zvd_025_stale_price_count_126d": {"inputs": ["close"], "func": zvd_025_stale_price_count_126d},
    "zvd_026_stale_price_count_252d": {"inputs": ["close"], "func": zvd_026_stale_price_count_252d},
    "zvd_027_stale_price_frac_21d": {"inputs": ["close"], "func": zvd_027_stale_price_frac_21d},
    "zvd_028_stale_price_frac_63d": {"inputs": ["close"], "func": zvd_028_stale_price_frac_63d},
    "zvd_029_stale_price_frac_252d": {"inputs": ["close"], "func": zvd_029_stale_price_frac_252d},
    "zvd_030_stale_price_expanding_count": {"inputs": ["close"], "func": zvd_030_stale_price_expanding_count},
    "zvd_031_consec_zero_vol_current": {"inputs": ["volume"], "func": zvd_031_consec_zero_vol_current},
    "zvd_032_consec_near_zero_vol_current": {"inputs": ["volume"], "func": zvd_032_consec_near_zero_vol_current},
    "zvd_033_consec_stale_price_current": {"inputs": ["close"], "func": zvd_033_consec_stale_price_current},
    "zvd_034_consec_zero_or_stale_current": {"inputs": ["close", "volume"], "func": zvd_034_consec_zero_or_stale_current},
    "zvd_035_max_zero_vol_streak_21d": {"inputs": ["volume"], "func": zvd_035_max_zero_vol_streak_21d},
    "zvd_036_max_zero_vol_streak_63d": {"inputs": ["volume"], "func": zvd_036_max_zero_vol_streak_63d},
    "zvd_037_max_zero_vol_streak_252d": {"inputs": ["volume"], "func": zvd_037_max_zero_vol_streak_252d},
    "zvd_038_max_stale_price_streak_21d": {"inputs": ["close"], "func": zvd_038_max_stale_price_streak_21d},
    "zvd_039_max_stale_price_streak_63d": {"inputs": ["close"], "func": zvd_039_max_stale_price_streak_63d},
    "zvd_040_max_stale_price_streak_252d": {"inputs": ["close"], "func": zvd_040_max_stale_price_streak_252d},
    "zvd_041_days_since_last_zero_vol": {"inputs": ["volume"], "func": zvd_041_days_since_last_zero_vol},
    "zvd_042_days_since_last_near_zero_vol": {"inputs": ["volume"], "func": zvd_042_days_since_last_near_zero_vol},
    "zvd_043_days_since_last_stale_price": {"inputs": ["close"], "func": zvd_043_days_since_last_stale_price},
    "zvd_044_days_since_last_zero_vol_log": {"inputs": ["volume"], "func": zvd_044_days_since_last_zero_vol_log},
    "zvd_045_days_since_last_stale_log": {"inputs": ["close"], "func": zvd_045_days_since_last_stale_log},
    "zvd_046_days_since_zero_vol_norm_252d": {"inputs": ["volume"], "func": zvd_046_days_since_zero_vol_norm_252d},
    "zvd_047_days_since_stale_norm_252d": {"inputs": ["close"], "func": zvd_047_days_since_stale_norm_252d},
    "zvd_048_days_since_zero_vol_gt21_flag": {"inputs": ["volume"], "func": zvd_048_days_since_zero_vol_gt21_flag},
    "zvd_049_days_since_stale_gt21_flag": {"inputs": ["close"], "func": zvd_049_days_since_stale_gt21_flag},
    "zvd_050_days_since_zero_or_stale": {"inputs": ["close", "volume"], "func": zvd_050_days_since_zero_or_stale},
    "zvd_051_zero_vol_cluster_5d_21d": {"inputs": ["volume"], "func": zvd_051_zero_vol_cluster_5d_21d},
    "zvd_052_stale_cluster_5d_21d": {"inputs": ["close"], "func": zvd_052_stale_cluster_5d_21d},
    "zvd_053_dead_session_frac_21d": {"inputs": ["close", "volume"], "func": zvd_053_dead_session_frac_21d},
    "zvd_054_dead_session_frac_63d": {"inputs": ["close", "volume"], "func": zvd_054_dead_session_frac_63d},
    "zvd_055_dead_session_frac_126d": {"inputs": ["close", "volume"], "func": zvd_055_dead_session_frac_126d},
    "zvd_056_dead_session_frac_252d": {"inputs": ["close", "volume"], "func": zvd_056_dead_session_frac_252d},
    "zvd_057_doji_volume_flag": {"inputs": ["close", "open", "high", "low", "volume"], "func": zvd_057_doji_volume_flag},
    "zvd_058_doji_volume_count_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": zvd_058_doji_volume_count_21d},
    "zvd_059_doji_volume_count_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": zvd_059_doji_volume_count_63d},
    "zvd_060_doji_volume_frac_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": zvd_060_doji_volume_frac_252d},
    "zvd_061_vol_pct_of_trailing_median_21d": {"inputs": ["volume"], "func": zvd_061_vol_pct_of_trailing_median_21d},
    "zvd_062_vol_pct_of_trailing_median_63d": {"inputs": ["volume"], "func": zvd_062_vol_pct_of_trailing_median_63d},
    "zvd_063_vol_pct_of_trailing_median_252d": {"inputs": ["volume"], "func": zvd_063_vol_pct_of_trailing_median_252d},
    "zvd_064_zero_vol_pct_rank_252d": {"inputs": ["volume"], "func": zvd_064_zero_vol_pct_rank_252d},
    "zvd_065_vol_zscore_63d": {"inputs": ["volume"], "func": zvd_065_vol_zscore_63d},
    "zvd_066_vol_zscore_252d": {"inputs": ["volume"], "func": zvd_066_vol_zscore_252d},
    "zvd_067_stale_and_zero_same_day_flag": {"inputs": ["close", "volume"], "func": zvd_067_stale_and_zero_same_day_flag},
    "zvd_068_stale_and_near_zero_same_day_flag": {"inputs": ["close", "volume"], "func": zvd_068_stale_and_near_zero_same_day_flag},
    "zvd_069_zero_vol_after_stale_flag": {"inputs": ["close", "volume"], "func": zvd_069_zero_vol_after_stale_flag},
    "zvd_070_stale_after_zero_vol_flag": {"inputs": ["close", "volume"], "func": zvd_070_stale_after_zero_vol_flag},
    "zvd_071_near_zero_vol_expanding_frac": {"inputs": ["volume"], "func": zvd_071_near_zero_vol_expanding_frac},
    "zvd_072_stale_price_expanding_frac": {"inputs": ["close"], "func": zvd_072_stale_price_expanding_frac},
    "zvd_073_dead_session_count_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": zvd_073_dead_session_count_21d_pct_rank_252d},
    "zvd_074_near_zero_vol_count_21d_pct_rank_252d": {"inputs": ["volume"], "func": zvd_074_near_zero_vol_count_21d_pct_rank_252d},
    "zvd_075_stale_price_count_21d_pct_rank_252d": {"inputs": ["close"], "func": zvd_075_stale_price_count_21d_pct_rank_252d},
}
