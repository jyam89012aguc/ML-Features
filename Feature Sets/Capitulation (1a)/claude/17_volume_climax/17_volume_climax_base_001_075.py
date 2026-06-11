"""
17_volume_climax — Base Features 001-100
Domain: single-day extreme volume events — the largest volume day(s) in trailing windows,
their magnitude vs all other days, days-since the extreme event, whether today IS the
extreme day, the #1-vs-#2 volume gap, and climax-day price action (wide-range down bar).
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _days_since_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars since the rolling-window maximum occurred."""
    def _dsm(arr):
        idx = int(np.argmax(arr))
        return float(len(arr) - 1 - idx)
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_dsm, raw=True)


def _rolling_second_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling second-largest value over trailing w periods."""
    def _s2(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        return float(top2[0])
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_s2, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Max volume day magnitude in trailing windows ---

def vcx_001_max_vol_21d(volume: pd.Series) -> pd.Series:
    """Single largest volume in trailing 21 days (raw climax level)."""
    return _rolling_max(volume, _TD_MON)


def vcx_002_max_vol_63d(volume: pd.Series) -> pd.Series:
    """Single largest volume in trailing 63 days."""
    return _rolling_max(volume, _TD_QTR)


def vcx_003_max_vol_126d(volume: pd.Series) -> pd.Series:
    """Single largest volume in trailing 126 days."""
    return _rolling_max(volume, _TD_HALF)


def vcx_004_max_vol_252d(volume: pd.Series) -> pd.Series:
    """Single largest volume in trailing 252 days."""
    return _rolling_max(volume, _TD_YEAR)


def vcx_005_max_vol_21d_vs_mean(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day max volume to 21-day mean volume (climax multiple)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def vcx_006_max_vol_63d_vs_mean(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day max volume to 63-day mean volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def vcx_007_max_vol_126d_vs_mean(volume: pd.Series) -> pd.Series:
    """Ratio of 126-day max volume to 126-day mean volume."""
    return _safe_div(_rolling_max(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))


def vcx_008_max_vol_252d_vs_mean(volume: pd.Series) -> pd.Series:
    """Ratio of 252-day max volume to 252-day mean volume."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))


def vcx_009_max_vol_21d_vs_median(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day max volume to 21-day median volume."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_median(volume, _TD_MON))


def vcx_010_max_vol_63d_vs_median(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day max volume to 63-day median volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def vcx_011_max_vol_252d_vs_median(volume: pd.Series) -> pd.Series:
    """Ratio of 252-day max volume to 252-day median volume."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))


def vcx_012_log_max_vol_252d(volume: pd.Series) -> pd.Series:
    """Log of the 252-day single-peak volume (compresses right tail)."""
    return _log_safe(_rolling_max(volume, _TD_YEAR))


# --- Group B (013-024): Days-since the climax volume day ---

def vcx_013_days_since_max_vol_21d(volume: pd.Series) -> pd.Series:
    """Days since the highest-volume day within the trailing 21-day window."""
    return _days_since_max(volume, _TD_MON)


def vcx_014_days_since_max_vol_63d(volume: pd.Series) -> pd.Series:
    """Days since the highest-volume day within the trailing 63-day window."""
    return _days_since_max(volume, _TD_QTR)


def vcx_015_days_since_max_vol_126d(volume: pd.Series) -> pd.Series:
    """Days since the highest-volume day within the trailing 126-day window."""
    return _days_since_max(volume, _TD_HALF)


def vcx_016_days_since_max_vol_252d(volume: pd.Series) -> pd.Series:
    """Days since the highest-volume day within the trailing 252-day window."""
    return _days_since_max(volume, _TD_YEAR)


def vcx_017_days_since_max_vol_21d_norm(volume: pd.Series) -> pd.Series:
    """Days-since-climax-21d normalized by window length (0=recent, 1=old)."""
    return _days_since_max(volume, _TD_MON) / _TD_MON


def vcx_018_days_since_max_vol_63d_norm(volume: pd.Series) -> pd.Series:
    """Days-since-climax-63d normalized by window length."""
    return _days_since_max(volume, _TD_QTR) / _TD_QTR


def vcx_019_days_since_max_vol_252d_norm(volume: pd.Series) -> pd.Series:
    """Days-since-climax-252d normalized by window length."""
    return _days_since_max(volume, _TD_YEAR) / _TD_YEAR


def vcx_020_log1p_days_since_max_vol_63d(volume: pd.Series) -> pd.Series:
    """Log1p of days-since-63d-climax (compresses long tails)."""
    return np.log1p(_days_since_max(volume, _TD_QTR))


def vcx_021_log1p_days_since_max_vol_252d(volume: pd.Series) -> pd.Series:
    """Log1p of days-since-252d-climax."""
    return np.log1p(_days_since_max(volume, _TD_YEAR))


def vcx_022_climax_recency_score_63d(volume: pd.Series) -> pd.Series:
    """Recency score: 1 if climax was today, decays as days_since / 63."""
    dsm = _days_since_max(volume, _TD_QTR)
    return (1.0 - dsm / _TD_QTR).clip(lower=0.0)


def vcx_023_climax_recency_score_252d(volume: pd.Series) -> pd.Series:
    """Recency score: 1 if climax was today, decays as days_since / 252."""
    dsm = _days_since_max(volume, _TD_YEAR)
    return (1.0 - dsm / _TD_YEAR).clip(lower=0.0)


def vcx_024_exp_decay_days_since_63d(volume: pd.Series) -> pd.Series:
    """Exponential decay of days-since-climax with half-life 21 days (63d window)."""
    dsm = _days_since_max(volume, _TD_QTR)
    return np.exp(-dsm / _TD_MON)


# --- Group C (025-036): Is-today-the-climax flag and related ---

def vcx_025_is_max_vol_day_21d(volume: pd.Series) -> pd.Series:
    """Flag: today is the single highest-volume day in the trailing 21-day window."""
    mx = _rolling_max(volume, _TD_MON)
    return (volume >= mx).astype(float)


def vcx_026_is_max_vol_day_63d(volume: pd.Series) -> pd.Series:
    """Flag: today is the single highest-volume day in the trailing 63-day window."""
    mx = _rolling_max(volume, _TD_QTR)
    return (volume >= mx).astype(float)


def vcx_027_is_max_vol_day_126d(volume: pd.Series) -> pd.Series:
    """Flag: today is the single highest-volume day in the trailing 126-day window."""
    mx = _rolling_max(volume, _TD_HALF)
    return (volume >= mx).astype(float)


def vcx_028_is_max_vol_day_252d(volume: pd.Series) -> pd.Series:
    """Flag: today is the single highest-volume day in the trailing 252-day window."""
    mx = _rolling_max(volume, _TD_YEAR)
    return (volume >= mx).astype(float)


def vcx_029_climax_flag_within_5d_21d(volume: pd.Series) -> pd.Series:
    """Flag: the 21-day climax day occurred within the last 5 trading days."""
    return (vcx_013_days_since_max_vol_21d(volume) <= _TD_WEEK).astype(float)


def vcx_030_climax_flag_within_5d_63d(volume: pd.Series) -> pd.Series:
    """Flag: the 63-day climax day occurred within the last 5 trading days."""
    return (vcx_014_days_since_max_vol_63d(volume) <= _TD_WEEK).astype(float)


def vcx_031_climax_flag_within_5d_252d(volume: pd.Series) -> pd.Series:
    """Flag: the 252-day climax day occurred within the last 5 trading days."""
    return (vcx_016_days_since_max_vol_252d(volume) <= _TD_WEEK).astype(float)


def vcx_032_climax_flag_within_21d_252d(volume: pd.Series) -> pd.Series:
    """Flag: the 252-day volume climax occurred within the last 21 trading days."""
    return (vcx_016_days_since_max_vol_252d(volume) <= _TD_MON).astype(float)


def vcx_033_consecutive_climax_days_21d(volume: pd.Series) -> pd.Series:
    """Count of trailing days where today ties or exceeds 21-day rolling max (climax run)."""
    mx = volume.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    return (volume >= mx).astype(float).rolling(_TD_WEEK, min_periods=1).sum()


def vcx_034_max_vol_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day max volume within trailing 252-day distribution."""
    mx21 = _rolling_max(volume, _TD_MON)
    return mx21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcx_035_max_vol_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day max volume within trailing 252-day distribution."""
    mx63 = _rolling_max(volume, _TD_QTR)
    return mx63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcx_036_today_vol_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume in the trailing 252-day volume distribution."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (037-048): #1 vs #2 volume gap (singularity of the climax) ---

def vcx_037_vol_top1_minus_top2_21d(volume: pd.Series) -> pd.Series:
    """Absolute gap between #1 and #2 volume days in trailing 21 days."""
    top1 = _rolling_max(volume, _TD_MON)
    top2 = _rolling_second_max(volume, _TD_MON)
    return top1 - top2


def vcx_038_vol_top1_minus_top2_63d(volume: pd.Series) -> pd.Series:
    """Absolute gap between #1 and #2 volume days in trailing 63 days."""
    top1 = _rolling_max(volume, _TD_QTR)
    top2 = _rolling_second_max(volume, _TD_QTR)
    return top1 - top2


def vcx_039_vol_top1_minus_top2_252d(volume: pd.Series) -> pd.Series:
    """Absolute gap between #1 and #2 volume days in trailing 252 days."""
    top1 = _rolling_max(volume, _TD_YEAR)
    top2 = _rolling_second_max(volume, _TD_YEAR)
    return top1 - top2


def vcx_040_vol_top1_over_top2_21d(volume: pd.Series) -> pd.Series:
    """Ratio of #1 to #2 volume in trailing 21 days (singularity index)."""
    top1 = _rolling_max(volume, _TD_MON)
    top2 = _rolling_second_max(volume, _TD_MON)
    return _safe_div(top1, top2)


def vcx_041_vol_top1_over_top2_63d(volume: pd.Series) -> pd.Series:
    """Ratio of #1 to #2 volume in trailing 63 days."""
    top1 = _rolling_max(volume, _TD_QTR)
    top2 = _rolling_second_max(volume, _TD_QTR)
    return _safe_div(top1, top2)


def vcx_042_vol_top1_over_top2_252d(volume: pd.Series) -> pd.Series:
    """Ratio of #1 to #2 volume in trailing 252 days."""
    top1 = _rolling_max(volume, _TD_YEAR)
    top2 = _rolling_second_max(volume, _TD_YEAR)
    return _safe_div(top1, top2)


def vcx_043_vol_top1_minus_top2_norm_mean_63d(volume: pd.Series) -> pd.Series:
    """63-day top1-top2 gap normalized by 63-day mean volume."""
    gap = vcx_038_vol_top1_minus_top2_63d(volume)
    avg = _rolling_mean(volume, _TD_QTR)
    return _safe_div(gap, avg)


def vcx_044_vol_top1_minus_top2_norm_mean_252d(volume: pd.Series) -> pd.Series:
    """252-day top1-top2 gap normalized by 252-day mean volume."""
    gap = vcx_039_vol_top1_minus_top2_252d(volume)
    avg = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(gap, avg)


def vcx_045_vol_top1_over_mean_minus_top2_over_mean_63d(volume: pd.Series) -> pd.Series:
    """Difference of top1/mean and top2/mean ratios in 63-day window."""
    avg = _rolling_mean(volume, _TD_QTR)
    r1 = _safe_div(_rolling_max(volume, _TD_QTR), avg)
    r2 = _safe_div(_rolling_second_max(volume, _TD_QTR), avg)
    return r1 - r2


def vcx_046_singularity_index_21d(volume: pd.Series) -> pd.Series:
    """Top1 volume minus mean of remaining days in 21-day window (isolation of peak)."""
    top1 = _rolling_max(volume, _TD_MON)
    total = _rolling_sum(volume, _TD_MON)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_MON - 1, index=volume.index, dtype=float))
    return _safe_div(top1 - mean_rest, mean_rest)


def vcx_047_singularity_index_63d(volume: pd.Series) -> pd.Series:
    """Top1 volume minus mean of remaining days in 63-day window."""
    top1 = _rolling_max(volume, _TD_QTR)
    total = _rolling_sum(volume, _TD_QTR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_QTR - 1, index=volume.index, dtype=float))
    return _safe_div(top1 - mean_rest, mean_rest)


def vcx_048_singularity_index_252d(volume: pd.Series) -> pd.Series:
    """Top1 volume minus mean of remaining days in 252-day window."""
    top1 = _rolling_max(volume, _TD_YEAR)
    total = _rolling_sum(volume, _TD_YEAR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_YEAR - 1, index=volume.index, dtype=float))
    return _safe_div(top1 - mean_rest, mean_rest)


# --- Group E (049-060): Climax-day price action (wide-range down bar) ---

def vcx_049_climax_day_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close-to-close return on the 21-day peak-volume day (negative = climax down bar)."""
    ret = close.pct_change(1)
    is_climax = vcx_025_is_max_vol_day_21d(volume)
    return ret.where(is_climax.astype(bool), np.nan).ffill()


def vcx_050_climax_day_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close-to-close return on the 63-day peak-volume day."""
    ret = close.pct_change(1)
    is_climax = vcx_026_is_max_vol_day_63d(volume)
    return ret.where(is_climax.astype(bool), np.nan).ffill()


def vcx_051_climax_day_return_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close-to-close return on the 252-day peak-volume day."""
    ret = close.pct_change(1)
    is_climax = vcx_028_is_max_vol_day_252d(volume)
    return ret.where(is_climax.astype(bool), np.nan).ffill()


def vcx_052_climax_day_range_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                  volume: pd.Series) -> pd.Series:
    """Intraday range (high-low)/close on the 21-day peak-volume day."""
    rng = _safe_div(high - low, close.shift(1))
    is_climax = vcx_025_is_max_vol_day_21d(volume)
    return rng.where(is_climax.astype(bool), np.nan).ffill()


def vcx_053_climax_day_range_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                  volume: pd.Series) -> pd.Series:
    """Intraday range (high-low)/close on the 63-day peak-volume day."""
    rng = _safe_div(high - low, close.shift(1))
    is_climax = vcx_026_is_max_vol_day_63d(volume)
    return rng.where(is_climax.astype(bool), np.nan).ffill()


def vcx_054_climax_day_range_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Intraday range (high-low)/close on the 252-day peak-volume day."""
    rng = _safe_div(high - low, close.shift(1))
    is_climax = vcx_028_is_max_vol_day_252d(volume)
    return rng.where(is_climax.astype(bool), np.nan).ffill()


def vcx_055_climax_down_bar_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 63-day peak-volume day had a negative close-to-close return."""
    ret = close.pct_change(1)
    is_climax = vcx_026_is_max_vol_day_63d(volume)
    flag = (is_climax.astype(bool) & (ret < 0)).astype(float)
    return flag.where(is_climax.astype(bool), np.nan).ffill()


def vcx_056_climax_down_bar_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 252-day peak-volume day had a negative close-to-close return."""
    ret = close.pct_change(1)
    is_climax = vcx_028_is_max_vol_day_252d(volume)
    flag = (is_climax.astype(bool) & (ret < 0)).astype(float)
    return flag.where(is_climax.astype(bool), np.nan).ffill()


def vcx_057_climax_day_close_position_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Close position within range on 21-day climax day (0=low, 1=high)."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    is_climax = vcx_025_is_max_vol_day_21d(volume)
    return pos.where(is_climax.astype(bool), np.nan).ffill()


def vcx_058_climax_day_close_position_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Close position within range on 252-day climax day (0=low, 1=high)."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    is_climax = vcx_028_is_max_vol_day_252d(volume)
    return pos.where(is_climax.astype(bool), np.nan).ffill()


def vcx_059_climax_day_true_range_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """True range (normalized by prior close) on the 63-day peak-volume day."""
    tr = _tr(close, high, low)
    tr_norm = _safe_div(tr, close.shift(1))
    is_climax = vcx_026_is_max_vol_day_63d(volume)
    return tr_norm.where(is_climax.astype(bool), np.nan).ffill()


def vcx_060_climax_day_true_range_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """True range (normalized by prior close) on the 252-day peak-volume day."""
    tr = _tr(close, high, low)
    tr_norm = _safe_div(tr, close.shift(1))
    is_climax = vcx_028_is_max_vol_day_252d(volume)
    return tr_norm.where(is_climax.astype(bool), np.nan).ffill()


# --- Group F (061-075): Climax-volume z-score, expanding records, ratios ---

def vcx_061_max_vol_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day peak volume within trailing 252-day distribution of peak volumes."""
    mx21 = _rolling_max(volume, _TD_MON)
    m = _rolling_mean(mx21, _TD_YEAR)
    s = _rolling_std(mx21, _TD_YEAR)
    return _safe_div(mx21 - m, s)


def vcx_062_max_vol_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day peak volume within trailing 252-day distribution."""
    mx63 = _rolling_max(volume, _TD_QTR)
    m = _rolling_mean(mx63, _TD_YEAR)
    s = _rolling_std(mx63, _TD_YEAR)
    return _safe_div(mx63 - m, s)


def vcx_063_today_vol_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of today's volume within trailing 252-day distribution."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    return _safe_div(volume - m, s)


def vcx_064_today_vol_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of today's volume within trailing 63-day distribution."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(volume - m, s)


def vcx_065_expanding_max_vol(volume: pd.Series) -> pd.Series:
    """Expanding all-time max volume (absolute historical climax level)."""
    return volume.expanding(min_periods=1).max()


def vcx_066_today_vol_vs_expanding_max(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of all-time expanding max volume."""
    return _safe_div(volume, vcx_065_expanding_max_vol(volume))


def vcx_067_max_vol_252d_vs_expanding_max(volume: pd.Series) -> pd.Series:
    """252-day peak volume as fraction of expanding all-time peak volume."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), vcx_065_expanding_max_vol(volume))


def vcx_068_expanding_max_vol_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of today's volume (how extreme vs all history)."""
    return volume.expanding(min_periods=5).rank(pct=True)


def vcx_069_max_vol_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day peak to 252-day peak (how recent is the largest climax)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_max(volume, _TD_YEAR))


def vcx_070_max_vol_63d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day peak to 252-day peak volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_max(volume, _TD_YEAR))


def vcx_071_max_vol_126d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 126-day peak to 252-day peak volume."""
    return _safe_div(_rolling_max(volume, _TD_HALF), _rolling_max(volume, _TD_YEAR))


def vcx_072_max_vol_21d_log_ratio_252d(volume: pd.Series) -> pd.Series:
    """Log ratio of 21-day peak to 252-day peak volume."""
    return _log_safe(_rolling_max(volume, _TD_MON)) - _log_safe(_rolling_max(volume, _TD_YEAR))


def vcx_073_climax_vol_share_of_total_21d(volume: pd.Series) -> pd.Series:
    """Peak-day volume as fraction of total 21-day cumulative volume."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def vcx_074_climax_vol_share_of_total_63d(volume: pd.Series) -> pd.Series:
    """Peak-day volume as fraction of total 63-day cumulative volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def vcx_075_climax_vol_share_of_total_252d(volume: pd.Series) -> pd.Series:
    """Peak-day volume as fraction of total 252-day cumulative volume."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


# --- Group G_ext (151-175): Additional climax dimensions ---

def vcx_151_vol_above_1pt5x_mean_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where volume exceeded 1.5x the 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    return (volume >= 1.5 * mean63).astype(float).rolling(_TD_MON, min_periods=1).sum()


def vcx_152_vol_above_2x_mean_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume exceeded 2x the 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    return (volume >= 2.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def vcx_153_vol_above_3x_mean_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume exceeded 3x the 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    return (volume >= 3.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def vcx_154_climax_day_open_vs_low_63d(low: pd.Series, open: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """(open - low) / low on the 63-day peak-volume day (gap-down open signature)."""
    gap_low = _safe_div(open - low, low)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return gap_low.where(is_climax, np.nan).ffill()


def vcx_155_climax_day_high_vs_open_252d(high: pd.Series, open: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """(high - open) / open on the 252-day peak-volume day (intraday bounce off open)."""
    bounce = _safe_div(high - open, open)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return bounce.where(is_climax, np.nan).ffill()


def vcx_156_max_vol_5d_vs_mean_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day max volume to 21-day mean volume (very-short climax pulse)."""
    return _safe_div(_rolling_max(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))


def vcx_157_vol_iqr_21d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume in trailing 21 days (dispersion around mean)."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    return q75 - q25


def vcx_158_vol_iqr_63d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume in trailing 63 days."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def vcx_159_vol_coeff_variation_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of volume in trailing 21 days."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def vcx_160_vol_coeff_variation_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of volume in trailing 63 days."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def vcx_161_climax_day_ret_abs_x_range_63d(high: pd.Series, low: pd.Series,
                                            close: pd.Series, volume: pd.Series) -> pd.Series:
    """abs(return) * normalized_range on 63-day climax day (panic intensity)."""
    ret_abs = close.pct_change(1).abs()
    rng = _safe_div(high - low, close.shift(1))
    score = ret_abs * rng
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return score.where(is_climax, np.nan).ffill()


def vcx_162_climax_day_ret_abs_x_range_252d(high: pd.Series, low: pd.Series,
                                             close: pd.Series, volume: pd.Series) -> pd.Series:
    """abs(return) * normalized_range on 252-day climax day."""
    ret_abs = close.pct_change(1).abs()
    rng = _safe_div(high - low, close.shift(1))
    score = ret_abs * rng
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return score.where(is_climax, np.nan).ffill()


def vcx_163_vol_skew_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of volume (right-tail climax asymmetry)."""
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def vcx_164_vol_skew_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of volume."""
    return volume.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vcx_165_vol_skew_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of volume."""
    return volume.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def vcx_166_max_vol_5d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 5-day peak volume (ultra-short climax recency)."""
    mx5 = _rolling_max(volume, _TD_WEEK)
    return mx5.expanding(min_periods=5).rank(pct=True)


def vcx_167_today_vol_vs_ewm21(volume: pd.Series) -> pd.Series:
    """Today's volume divided by 21-day EMA of volume."""
    return _safe_div(volume, volume.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())


def vcx_168_today_vol_vs_ewm63(volume: pd.Series) -> pd.Series:
    """Today's volume divided by 63-day EMA of volume."""
    return _safe_div(volume, volume.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())


def vcx_169_climax_day_lower_shadow_252d(low: pd.Series, close: pd.Series,
                                          open: pd.Series, volume: pd.Series) -> pd.Series:
    """Lower shadow (min(open,close) - low) normalized by prior close on 252d climax day."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    shadow = _safe_div(body_bot - low, close.shift(1))
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return shadow.where(is_climax, np.nan).ffill()


def vcx_170_climax_day_upper_shadow_252d(high: pd.Series, close: pd.Series,
                                          open: pd.Series, volume: pd.Series) -> pd.Series:
    """Upper shadow (high - max(open,close)) normalized by prior close on 252d climax day."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    shadow = _safe_div(high - body_top, close.shift(1))
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return shadow.where(is_climax, np.nan).ffill()


def vcx_171_vol_p90_vs_mean_21d(volume: pd.Series) -> pd.Series:
    """90th percentile of 21-day volume divided by 21-day mean (tail heaviness)."""
    p90 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.9)
    return _safe_div(p90, _rolling_mean(volume, _TD_MON))


def vcx_172_vol_p90_vs_mean_63d(volume: pd.Series) -> pd.Series:
    """90th percentile of 63-day volume divided by 63-day mean."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.9)
    return _safe_div(p90, _rolling_mean(volume, _TD_QTR))


def vcx_173_climax_vol_above_exp_max_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume exceeds the prior expanding all-time max volume."""
    prior_exp_max = volume.shift(1).expanding(min_periods=1).max()
    return (volume > prior_exp_max).astype(float)


def vcx_174_exp_decay_days_since_252d(volume: pd.Series) -> pd.Series:
    """Exponential decay of days-since-252d-climax with half-life 63 days."""
    dsm = _days_since_max(volume, _TD_YEAR)
    return np.exp(-dsm / _TD_QTR)


def vcx_175_max_vol_5d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day peak volume to 252-day peak (short-horizon climax share)."""
    return _safe_div(_rolling_max(volume, _TD_WEEK), _rolling_max(volume, _TD_YEAR))


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CLIMAX_REGISTRY_001_075 = {
    "vcx_001_max_vol_21d": {"inputs": ["volume"], "func": vcx_001_max_vol_21d},
    "vcx_002_max_vol_63d": {"inputs": ["volume"], "func": vcx_002_max_vol_63d},
    "vcx_003_max_vol_126d": {"inputs": ["volume"], "func": vcx_003_max_vol_126d},
    "vcx_004_max_vol_252d": {"inputs": ["volume"], "func": vcx_004_max_vol_252d},
    "vcx_005_max_vol_21d_vs_mean": {"inputs": ["volume"], "func": vcx_005_max_vol_21d_vs_mean},
    "vcx_006_max_vol_63d_vs_mean": {"inputs": ["volume"], "func": vcx_006_max_vol_63d_vs_mean},
    "vcx_007_max_vol_126d_vs_mean": {"inputs": ["volume"], "func": vcx_007_max_vol_126d_vs_mean},
    "vcx_008_max_vol_252d_vs_mean": {"inputs": ["volume"], "func": vcx_008_max_vol_252d_vs_mean},
    "vcx_009_max_vol_21d_vs_median": {"inputs": ["volume"], "func": vcx_009_max_vol_21d_vs_median},
    "vcx_010_max_vol_63d_vs_median": {"inputs": ["volume"], "func": vcx_010_max_vol_63d_vs_median},
    "vcx_011_max_vol_252d_vs_median": {"inputs": ["volume"], "func": vcx_011_max_vol_252d_vs_median},
    "vcx_012_log_max_vol_252d": {"inputs": ["volume"], "func": vcx_012_log_max_vol_252d},
    "vcx_013_days_since_max_vol_21d": {"inputs": ["volume"], "func": vcx_013_days_since_max_vol_21d},
    "vcx_014_days_since_max_vol_63d": {"inputs": ["volume"], "func": vcx_014_days_since_max_vol_63d},
    "vcx_015_days_since_max_vol_126d": {"inputs": ["volume"], "func": vcx_015_days_since_max_vol_126d},
    "vcx_016_days_since_max_vol_252d": {"inputs": ["volume"], "func": vcx_016_days_since_max_vol_252d},
    "vcx_017_days_since_max_vol_21d_norm": {"inputs": ["volume"], "func": vcx_017_days_since_max_vol_21d_norm},
    "vcx_018_days_since_max_vol_63d_norm": {"inputs": ["volume"], "func": vcx_018_days_since_max_vol_63d_norm},
    "vcx_019_days_since_max_vol_252d_norm": {"inputs": ["volume"], "func": vcx_019_days_since_max_vol_252d_norm},
    "vcx_020_log1p_days_since_max_vol_63d": {"inputs": ["volume"], "func": vcx_020_log1p_days_since_max_vol_63d},
    "vcx_021_log1p_days_since_max_vol_252d": {"inputs": ["volume"], "func": vcx_021_log1p_days_since_max_vol_252d},
    "vcx_022_climax_recency_score_63d": {"inputs": ["volume"], "func": vcx_022_climax_recency_score_63d},
    "vcx_023_climax_recency_score_252d": {"inputs": ["volume"], "func": vcx_023_climax_recency_score_252d},
    "vcx_024_exp_decay_days_since_63d": {"inputs": ["volume"], "func": vcx_024_exp_decay_days_since_63d},
    "vcx_025_is_max_vol_day_21d": {"inputs": ["volume"], "func": vcx_025_is_max_vol_day_21d},
    "vcx_026_is_max_vol_day_63d": {"inputs": ["volume"], "func": vcx_026_is_max_vol_day_63d},
    "vcx_027_is_max_vol_day_126d": {"inputs": ["volume"], "func": vcx_027_is_max_vol_day_126d},
    "vcx_028_is_max_vol_day_252d": {"inputs": ["volume"], "func": vcx_028_is_max_vol_day_252d},
    "vcx_029_climax_flag_within_5d_21d": {"inputs": ["volume"], "func": vcx_029_climax_flag_within_5d_21d},
    "vcx_030_climax_flag_within_5d_63d": {"inputs": ["volume"], "func": vcx_030_climax_flag_within_5d_63d},
    "vcx_031_climax_flag_within_5d_252d": {"inputs": ["volume"], "func": vcx_031_climax_flag_within_5d_252d},
    "vcx_032_climax_flag_within_21d_252d": {"inputs": ["volume"], "func": vcx_032_climax_flag_within_21d_252d},
    "vcx_033_consecutive_climax_days_21d": {"inputs": ["volume"], "func": vcx_033_consecutive_climax_days_21d},
    "vcx_034_max_vol_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcx_034_max_vol_21d_pct_rank_252d},
    "vcx_035_max_vol_63d_pct_rank_252d": {"inputs": ["volume"], "func": vcx_035_max_vol_63d_pct_rank_252d},
    "vcx_036_today_vol_pct_rank_252d": {"inputs": ["volume"], "func": vcx_036_today_vol_pct_rank_252d},
    "vcx_037_vol_top1_minus_top2_21d": {"inputs": ["volume"], "func": vcx_037_vol_top1_minus_top2_21d},
    "vcx_038_vol_top1_minus_top2_63d": {"inputs": ["volume"], "func": vcx_038_vol_top1_minus_top2_63d},
    "vcx_039_vol_top1_minus_top2_252d": {"inputs": ["volume"], "func": vcx_039_vol_top1_minus_top2_252d},
    "vcx_040_vol_top1_over_top2_21d": {"inputs": ["volume"], "func": vcx_040_vol_top1_over_top2_21d},
    "vcx_041_vol_top1_over_top2_63d": {"inputs": ["volume"], "func": vcx_041_vol_top1_over_top2_63d},
    "vcx_042_vol_top1_over_top2_252d": {"inputs": ["volume"], "func": vcx_042_vol_top1_over_top2_252d},
    "vcx_043_vol_top1_minus_top2_norm_mean_63d": {"inputs": ["volume"], "func": vcx_043_vol_top1_minus_top2_norm_mean_63d},
    "vcx_044_vol_top1_minus_top2_norm_mean_252d": {"inputs": ["volume"], "func": vcx_044_vol_top1_minus_top2_norm_mean_252d},
    "vcx_045_vol_top1_over_mean_minus_top2_over_mean_63d": {"inputs": ["volume"], "func": vcx_045_vol_top1_over_mean_minus_top2_over_mean_63d},
    "vcx_046_singularity_index_21d": {"inputs": ["volume"], "func": vcx_046_singularity_index_21d},
    "vcx_047_singularity_index_63d": {"inputs": ["volume"], "func": vcx_047_singularity_index_63d},
    "vcx_048_singularity_index_252d": {"inputs": ["volume"], "func": vcx_048_singularity_index_252d},
    "vcx_049_climax_day_return_21d": {"inputs": ["close", "volume"], "func": vcx_049_climax_day_return_21d},
    "vcx_050_climax_day_return_63d": {"inputs": ["close", "volume"], "func": vcx_050_climax_day_return_63d},
    "vcx_051_climax_day_return_252d": {"inputs": ["close", "volume"], "func": vcx_051_climax_day_return_252d},
    "vcx_052_climax_day_range_21d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_052_climax_day_range_21d},
    "vcx_053_climax_day_range_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_053_climax_day_range_63d},
    "vcx_054_climax_day_range_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_054_climax_day_range_252d},
    "vcx_055_climax_down_bar_flag_63d": {"inputs": ["close", "volume"], "func": vcx_055_climax_down_bar_flag_63d},
    "vcx_056_climax_down_bar_flag_252d": {"inputs": ["close", "volume"], "func": vcx_056_climax_down_bar_flag_252d},
    "vcx_057_climax_day_close_position_21d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_057_climax_day_close_position_21d},
    "vcx_058_climax_day_close_position_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_058_climax_day_close_position_252d},
    "vcx_059_climax_day_true_range_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_059_climax_day_true_range_63d},
    "vcx_060_climax_day_true_range_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_060_climax_day_true_range_252d},
    "vcx_061_max_vol_21d_zscore_252d": {"inputs": ["volume"], "func": vcx_061_max_vol_21d_zscore_252d},
    "vcx_062_max_vol_63d_zscore_252d": {"inputs": ["volume"], "func": vcx_062_max_vol_63d_zscore_252d},
    "vcx_063_today_vol_zscore_252d": {"inputs": ["volume"], "func": vcx_063_today_vol_zscore_252d},
    "vcx_064_today_vol_zscore_63d": {"inputs": ["volume"], "func": vcx_064_today_vol_zscore_63d},
    "vcx_065_expanding_max_vol": {"inputs": ["volume"], "func": vcx_065_expanding_max_vol},
    "vcx_066_today_vol_vs_expanding_max": {"inputs": ["volume"], "func": vcx_066_today_vol_vs_expanding_max},
    "vcx_067_max_vol_252d_vs_expanding_max": {"inputs": ["volume"], "func": vcx_067_max_vol_252d_vs_expanding_max},
    "vcx_068_expanding_max_vol_rank": {"inputs": ["volume"], "func": vcx_068_expanding_max_vol_rank},
    "vcx_069_max_vol_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcx_069_max_vol_21d_vs_252d_ratio},
    "vcx_070_max_vol_63d_vs_252d_ratio": {"inputs": ["volume"], "func": vcx_070_max_vol_63d_vs_252d_ratio},
    "vcx_071_max_vol_126d_vs_252d_ratio": {"inputs": ["volume"], "func": vcx_071_max_vol_126d_vs_252d_ratio},
    "vcx_072_max_vol_21d_log_ratio_252d": {"inputs": ["volume"], "func": vcx_072_max_vol_21d_log_ratio_252d},
    "vcx_073_climax_vol_share_of_total_21d": {"inputs": ["volume"], "func": vcx_073_climax_vol_share_of_total_21d},
    "vcx_074_climax_vol_share_of_total_63d": {"inputs": ["volume"], "func": vcx_074_climax_vol_share_of_total_63d},
    "vcx_075_climax_vol_share_of_total_252d": {"inputs": ["volume"], "func": vcx_075_climax_vol_share_of_total_252d},
    "vcx_151_vol_above_1pt5x_mean_count_21d": {"inputs": ["volume"], "func": vcx_151_vol_above_1pt5x_mean_count_21d},
    "vcx_152_vol_above_2x_mean_count_63d": {"inputs": ["volume"], "func": vcx_152_vol_above_2x_mean_count_63d},
    "vcx_153_vol_above_3x_mean_count_63d": {"inputs": ["volume"], "func": vcx_153_vol_above_3x_mean_count_63d},
    "vcx_154_climax_day_open_vs_low_63d": {"inputs": ["low", "open", "volume"], "func": vcx_154_climax_day_open_vs_low_63d},
    "vcx_155_climax_day_high_vs_open_252d": {"inputs": ["high", "open", "volume"], "func": vcx_155_climax_day_high_vs_open_252d},
    "vcx_156_max_vol_5d_vs_mean_21d": {"inputs": ["volume"], "func": vcx_156_max_vol_5d_vs_mean_21d},
    "vcx_157_vol_iqr_21d": {"inputs": ["volume"], "func": vcx_157_vol_iqr_21d},
    "vcx_158_vol_iqr_63d": {"inputs": ["volume"], "func": vcx_158_vol_iqr_63d},
    "vcx_159_vol_coeff_variation_21d": {"inputs": ["volume"], "func": vcx_159_vol_coeff_variation_21d},
    "vcx_160_vol_coeff_variation_63d": {"inputs": ["volume"], "func": vcx_160_vol_coeff_variation_63d},
    "vcx_161_climax_day_ret_abs_x_range_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_161_climax_day_ret_abs_x_range_63d},
    "vcx_162_climax_day_ret_abs_x_range_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_162_climax_day_ret_abs_x_range_252d},
    "vcx_163_vol_skew_21d": {"inputs": ["volume"], "func": vcx_163_vol_skew_21d},
    "vcx_164_vol_skew_63d": {"inputs": ["volume"], "func": vcx_164_vol_skew_63d},
    "vcx_165_vol_skew_252d": {"inputs": ["volume"], "func": vcx_165_vol_skew_252d},
    "vcx_166_max_vol_5d_expanding_pct_rank": {"inputs": ["volume"], "func": vcx_166_max_vol_5d_expanding_pct_rank},
    "vcx_167_today_vol_vs_ewm21": {"inputs": ["volume"], "func": vcx_167_today_vol_vs_ewm21},
    "vcx_168_today_vol_vs_ewm63": {"inputs": ["volume"], "func": vcx_168_today_vol_vs_ewm63},
    "vcx_169_climax_day_lower_shadow_252d": {"inputs": ["low", "close", "open", "volume"], "func": vcx_169_climax_day_lower_shadow_252d},
    "vcx_170_climax_day_upper_shadow_252d": {"inputs": ["high", "close", "open", "volume"], "func": vcx_170_climax_day_upper_shadow_252d},
    "vcx_171_vol_p90_vs_mean_21d": {"inputs": ["volume"], "func": vcx_171_vol_p90_vs_mean_21d},
    "vcx_172_vol_p90_vs_mean_63d": {"inputs": ["volume"], "func": vcx_172_vol_p90_vs_mean_63d},
    "vcx_173_climax_vol_above_exp_max_flag": {"inputs": ["volume"], "func": vcx_173_climax_vol_above_exp_max_flag},
    "vcx_174_exp_decay_days_since_252d": {"inputs": ["volume"], "func": vcx_174_exp_decay_days_since_252d},
    "vcx_175_max_vol_5d_vs_252d_ratio": {"inputs": ["volume"], "func": vcx_175_max_vol_5d_vs_252d_ratio},
}
