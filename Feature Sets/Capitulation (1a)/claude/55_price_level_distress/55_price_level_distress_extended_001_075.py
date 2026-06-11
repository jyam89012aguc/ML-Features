"""
55_price_level_distress -- Extended Features 001-075
Domain: absolute price level distress -- deeper variants: multi-threshold level flags,
        EWM price level normalization, price momentum at distress levels,
        log-price z-scores across windows, penny regime volume interaction,
        distress streak composites, close vs high/low level ratios,
        price acceleration, distributional shape of close level over time.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9
_LVL_1   = 1.0
_LVL_2   = 2.0
_LVL_3   = 3.0
_LVL_5   = 5.0
_LVL_10  = 10.0


def _safe_div(num, den):
    return num / den.replace(0, np.nan)

def _rolling_mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()

def _rolling_max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _rolling_median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()

def _ewm_mean(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()

def _log_safe(s):
    return np.log(s.clip(lower=_EPS))

def _zscore(s, w):
    mu = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)

def _pct_rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _consec_streak(cond):
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)

def _safe_skew(arr):
    a = arr[~np.isnan(arr)]
    if len(a) < 3:
        return np.nan
    mu = a.mean()
    sig = a.std(ddof=1)
    if sig < _EPS:
        return 0.0
    return float(((a - mu) ** 3).mean() / sig ** 3)

def _safe_kurt(arr):
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    mu = a.mean()
    sig = a.std(ddof=1)
    if sig < _EPS:
        return 0.0
    return float(((a - mu) ** 4).mean() / sig ** 4 - 3.0)

def _roll_skew(s, w):
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_safe_skew, raw=True)

def _roll_kurt(s, w):
    return s.rolling(w, min_periods=max(4, w // 2)).apply(_safe_kurt, raw=True)


# --- Group A (001-010): Log-price z-scores across windows ---

def pld_ext_001_log_close_zscore_5d(close, low):
    """5-day z-score of log(close)."""
    return _zscore(_log_safe(close), _TD_WEEK)

def pld_ext_002_log_close_zscore_21d(close, low):
    """21-day z-score of log(close)."""
    return _zscore(_log_safe(close), _TD_MON)

def pld_ext_003_log_close_zscore_63d(close, low):
    """63-day z-score of log(close)."""
    return _zscore(_log_safe(close), _TD_QTR)

def pld_ext_004_log_close_zscore_126d(close, low):
    """126-day z-score of log(close)."""
    return _zscore(_log_safe(close), _TD_HALF)

def pld_ext_005_log_close_pctrank_5d(close, low):
    """5-day percentile rank of log(close)."""
    return _pct_rank(_log_safe(close), _TD_WEEK)

def pld_ext_006_log_close_pctrank_63d(close, low):
    """63-day percentile rank of log(close)."""
    return _pct_rank(_log_safe(close), _TD_QTR)

def pld_ext_007_log_close_pctrank_126d(close, low):
    """126-day percentile rank of log(close)."""
    return _pct_rank(_log_safe(close), _TD_HALF)

def pld_ext_008_log_close_ewma5_vs_sma252(close, low):
    """EWM5 / SMA252 of log(close)."""
    lc = _log_safe(close)
    return _safe_div(_ewm_mean(lc, _TD_WEEK), _rolling_mean(lc, _TD_YEAR))

def pld_ext_009_log_close_sma21_vs_sma252(close, low):
    """SMA21 / SMA252 of log(close)."""
    lc = _log_safe(close)
    return _safe_div(_rolling_mean(lc, _TD_MON), _rolling_mean(lc, _TD_YEAR))

def pld_ext_010_log_close_skew_63d(close, low):
    """63-day rolling skewness of log(close)."""
    return _roll_skew(_log_safe(close), _TD_QTR)


# --- Group B (011-020): EWM close level normalization ---

def pld_ext_011_close_norm_ewm21(close, low):
    """Close / EWM21 of close (short-term level normalization)."""
    return _safe_div(close, _ewm_mean(close, _TD_MON))

def pld_ext_012_close_norm_ewm63(close, low):
    """Close / EWM63 of close."""
    return _safe_div(close, _ewm_mean(close, _TD_QTR))

def pld_ext_013_close_norm_ewm126(close, low):
    """Close / EWM126 of close."""
    return _safe_div(close, _ewm_mean(close, _TD_HALF))

def pld_ext_014_close_norm_ewm252(close, low):
    """Close / EWM252 of close."""
    return _safe_div(close, _ewm_mean(close, _TD_YEAR))

def pld_ext_015_close_ewm5_zscore_252d(close, low):
    """252-day z-score of EWM5 of close."""
    return _zscore(_ewm_mean(close, _TD_WEEK), _TD_YEAR)

def pld_ext_016_close_ewm21_zscore_252d(close, low):
    """252-day z-score of EWM21 of close."""
    return _zscore(_ewm_mean(close, _TD_MON), _TD_YEAR)

def pld_ext_017_close_sma5_vs_sma126(close, low):
    """SMA5 / SMA126 of close."""
    return _safe_div(_rolling_mean(close, _TD_WEEK), _rolling_mean(close, _TD_HALF))

def pld_ext_018_close_sma21_vs_sma126(close, low):
    """SMA21 / SMA126 of close."""
    return _safe_div(_rolling_mean(close, _TD_MON), _rolling_mean(close, _TD_HALF))

def pld_ext_019_close_level_pctrank_126d(close, low):
    """126-day percentile rank of close price."""
    return _pct_rank(close, _TD_HALF)

def pld_ext_020_close_level_pctrank_63d(close, low):
    """63-day percentile rank of close price."""
    return _pct_rank(close, _TD_QTR)


# --- Group C (021-030): Low price level variants ---

def pld_ext_021_low_pctrank_252d(close, low):
    """252-day percentile rank of daily low price."""
    return _pct_rank(low, _TD_YEAR)

def pld_ext_022_low_pctrank_63d(close, low):
    """63-day percentile rank of daily low price."""
    return _pct_rank(low, _TD_QTR)

def pld_ext_023_low_zscore_252d(close, low):
    """252-day z-score of daily low price."""
    return _zscore(low, _TD_YEAR)

def pld_ext_024_low_zscore_63d(close, low):
    """63-day z-score of daily low price."""
    return _zscore(low, _TD_QTR)

def pld_ext_025_low_vs_close_ratio(close, low):
    """Low / close ratio (1 = close at low; < 1 = tail recovery)."""
    return _safe_div(low, close.clip(lower=_EPS))

def pld_ext_026_low_vs_close_ratio_sma21(close, low):
    """21-day SMA of low/close ratio."""
    return _rolling_mean(_safe_div(low, close.clip(lower=_EPS)), _TD_MON)

def pld_ext_027_low_vs_close_ratio_sma63(close, low):
    """63-day SMA of low/close ratio."""
    return _rolling_mean(_safe_div(low, close.clip(lower=_EPS)), _TD_QTR)

def pld_ext_028_low_below_1_flag(close, low):
    """Flag: daily low < $1.00."""
    return (low < _LVL_1).astype(float)

def pld_ext_029_low_below_1_count_21d(close, low):
    """21-day count of days where daily low < $1.00."""
    return _rolling_sum((low < _LVL_1).astype(float), _TD_MON)

def pld_ext_030_low_below_5_count_63d(close, low):
    """63-day count of days where daily low < $5.00."""
    return _rolling_sum((low < _LVL_5).astype(float), _TD_QTR)


# --- Group D (031-040): Momentum at distress levels ---

def pld_ext_031_close_mom5(close, low):
    """5-day price momentum (close - close.shift(5))."""
    return close - close.shift(5)

def pld_ext_032_close_mom21(close, low):
    """21-day price momentum."""
    return close - close.shift(_TD_MON)

def pld_ext_033_close_mom63(close, low):
    """63-day price momentum."""
    return close - close.shift(_TD_QTR)

def pld_ext_034_close_pct_mom5(close, low):
    """5-day percentage price change."""
    return close.pct_change(5)

def pld_ext_035_close_pct_mom21(close, low):
    """21-day percentage price change."""
    return close.pct_change(_TD_MON)

def pld_ext_036_close_pct_mom63(close, low):
    """63-day percentage price change."""
    return close.pct_change(_TD_QTR)

def pld_ext_037_close_pct_mom126(close, low):
    """126-day percentage price change."""
    return close.pct_change(_TD_HALF)

def pld_ext_038_close_below5_and_falling_21d(close, low):
    """Fraction of 21d days: close < $5 AND close below 21d SMA."""
    flag = ((close < _LVL_5) & (close < _rolling_mean(close, _TD_MON))).astype(float)
    return _rolling_sum(flag, _TD_MON)

def pld_ext_039_close_below10_falling_fraction_63d(close, low):
    """63-day fraction of days where close < $10 and < 63d SMA."""
    flag = ((close < _LVL_10) & (close < _rolling_mean(close, _TD_QTR))).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR

def pld_ext_040_close_accel_21d(close, low):
    """Price acceleration: current 5d SMA change minus its 21d lagged value."""
    sma5 = _rolling_mean(close, _TD_WEEK)
    return sma5 - sma5.shift(_TD_MON)


# --- Group E (041-050): Distress threshold streaks and counts ---

def pld_ext_041_below_1_streak(close, low):
    """Consecutive days close < $1.00."""
    return _consec_streak(close < _LVL_1)

def pld_ext_042_below_3_streak(close, low):
    """Consecutive days close < $3.00."""
    return _consec_streak(close < _LVL_3)

def pld_ext_043_below_5_streak(close, low):
    """Consecutive days close < $5.00."""
    return _consec_streak(close < _LVL_5)

def pld_ext_044_below_10_streak(close, low):
    """Consecutive days close < $10.00."""
    return _consec_streak(close < _LVL_10)

def pld_ext_045_below_1_count_63d(close, low):
    """63-day count of days where close < $1.00."""
    return _rolling_sum((close < _LVL_1).astype(float), _TD_QTR)

def pld_ext_046_below_2_count_63d(close, low):
    """63-day count of days where close < $2.00."""
    return _rolling_sum((close < _LVL_2).astype(float), _TD_QTR)

def pld_ext_047_below_3_count_252d(close, low):
    """252-day count of days where close < $3.00."""
    return _rolling_sum((close < _LVL_3).astype(float), _TD_YEAR)

def pld_ext_048_below_5_fraction_252d(close, low):
    """Fraction of 252d days where close < $5.00."""
    return _rolling_sum((close < _LVL_5).astype(float), _TD_YEAR) / _TD_YEAR

def pld_ext_049_below_10_fraction_252d(close, low):
    """Fraction of 252d days where close < $10.00."""
    return _rolling_sum((close < _LVL_10).astype(float), _TD_YEAR) / _TD_YEAR

def pld_ext_050_distress_level_score(close, low):
    """Composite: sum of (below_1, below_2, below_3, below_5, below_10) flags."""
    f1 = (close < _LVL_1).astype(float)
    f2 = (close < _LVL_2).astype(float)
    f3 = (close < _LVL_3).astype(float)
    f5 = (close < _LVL_5).astype(float)
    f10 = (close < _LVL_10).astype(float)
    return f1 + f2 + f3 + f5 + f10


# --- Group F (051-060): Close vs min ratio deepening ---

def pld_ext_051_close_vs_min5_ratio(close, low):
    """Close / 5d rolling minimum close (how far off recent low)."""
    return _safe_div(close, _rolling_min(close, _TD_WEEK))

def pld_ext_052_close_vs_min21_zscore_252d(close, low):
    """252-day z-score of (close / 21d min)."""
    return _zscore(_safe_div(close, _rolling_min(close, _TD_MON)), _TD_YEAR)

def pld_ext_053_close_vs_min63_pctrank_252d(close, low):
    """252-day pctrank of (close / 63d min)."""
    return _pct_rank(_safe_div(close, _rolling_min(close, _TD_QTR)), _TD_YEAR)

def pld_ext_054_close_vs_min252_pctrank_252d(close, low):
    """252-day pctrank of (close / 252d min)."""
    return _pct_rank(_safe_div(close, _rolling_min(close, _TD_YEAR)), _TD_YEAR)

def pld_ext_055_close_at_min252_flag(close, low):
    """Flag: close equals its 252-day rolling minimum."""
    return (close <= _rolling_min(close, _TD_YEAR)).astype(float)

def pld_ext_056_close_at_min252_count_21d(close, low):
    """21-day count of days where close equals 252d rolling min."""
    flag = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_MON)

def pld_ext_057_low_at_min252_flag(close, low):
    """Flag: daily low equals its 252-day rolling minimum."""
    return (low <= _rolling_min(low, _TD_YEAR)).astype(float)

def pld_ext_058_close_below_low_sma21_flag(close, low):
    """Flag: close is below the 21d SMA of daily lows."""
    return (close < _rolling_mean(low, _TD_MON)).astype(float)

def pld_ext_059_close_below_low_sma63_count_63d(close, low):
    """63-day count where close < 63d SMA of daily lows."""
    flag = (close < _rolling_mean(low, _TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)

def pld_ext_060_log_close_kurt_63d(close, low):
    """63-day rolling excess kurtosis of log(close)."""
    return _roll_kurt(_log_safe(close), _TD_QTR)


# --- Group G (061-070): Volume-conditioned price distress ---

def pld_ext_061_close_below5_vol_fraction_21d(close, low, volume):
    """Fraction of 21d volume occurring when close < $5."""
    flag = (close < _LVL_5).astype(float)
    return _safe_div(_rolling_sum(volume * flag, _TD_MON), _rolling_sum(volume, _TD_MON))

def pld_ext_062_close_below5_vol_fraction_63d(close, low, volume):
    """Fraction of 63d volume occurring when close < $5."""
    flag = (close < _LVL_5).astype(float)
    return _safe_div(_rolling_sum(volume * flag, _TD_QTR), _rolling_sum(volume, _TD_QTR))

def pld_ext_063_close_below1_vol_fraction_252d(close, low, volume):
    """Fraction of 252d volume occurring when close < $1."""
    flag = (close < _LVL_1).astype(float)
    return _safe_div(_rolling_sum(volume * flag, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))

def pld_ext_064_dvol_when_below5_21d(close, low, volume):
    """Mean dollar-volume when close < $5 over 21 days."""
    flag = (close < _LVL_5).astype(float)
    dv = close * volume
    return _safe_div(_rolling_sum(dv * flag, _TD_MON), _rolling_sum(flag, _TD_MON))

def pld_ext_065_below5_high_vol_coincidence_21d(close, low, volume):
    """21-day count of days with close < $5 AND volume > median."""
    med_vol = _rolling_median(volume, _TD_MON)
    flag = ((close < _LVL_5) & (volume > med_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)

def pld_ext_066_below5_and_down_count_21d(close, low, volume):
    """21-day count of days with close < $5 AND daily return negative."""
    flag = ((close < _LVL_5) & (close.pct_change(1) < 0)).astype(float)
    return _rolling_sum(flag, _TD_MON)

def pld_ext_067_close_below5_dvol_zscore_252d(close, low, volume):
    """252-day z-score of dollar-volume on sub-$5 days."""
    flag = (close < _LVL_5).astype(float)
    dv = close * volume * flag
    return _zscore(dv, _TD_YEAR)

def pld_ext_068_close_pctrank_21d(close, low):
    """21-day percentile rank of close price."""
    return _pct_rank(close, _TD_MON)

def pld_ext_069_close_pctrank_5d(close, low):
    """5-day percentile rank of close price."""
    return _pct_rank(close, _TD_WEEK)

def pld_ext_070_close_sma5_vs_sma252(close, low):
    """SMA5 / SMA252 of close price."""
    return _safe_div(_rolling_mean(close, _TD_WEEK), _rolling_mean(close, _TD_YEAR))


# --- Group H (071-075): Cross-window distress composites ---

def pld_ext_071_close_level_skew_252d(close, low):
    """252-day rolling skewness of close price level."""
    return _roll_skew(close, _TD_YEAR)

def pld_ext_072_log_close_zscore_252d(close, low):
    """252-day z-score of log(close)."""
    return _zscore(_log_safe(close), _TD_YEAR)

def pld_ext_073_close_new_1yr_low_streak(close, low):
    """Consecutive days where close equals its 252d rolling minimum."""
    return _consec_streak(close <= _rolling_min(close, _TD_YEAR))

def pld_ext_074_distress_score_zscore_252d(close, low):
    """252-day z-score of distress level score (sum of threshold flags)."""
    score = ((close < _LVL_1).astype(float) + (close < _LVL_2).astype(float) +
             (close < _LVL_3).astype(float) + (close < _LVL_5).astype(float) +
             (close < _LVL_10).astype(float))
    return _zscore(score, _TD_YEAR)

def pld_ext_075_close_norm_252d_min_zscore(close, low):
    """Z-score of (close / 252d min) over 252d window."""
    ratio = _safe_div(close, _rolling_min(close, _TD_YEAR))
    return _zscore(ratio, _TD_YEAR)


PRICE_LEVEL_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "pld_ext_001_log_close_zscore_5d": {"inputs": ["close", "low"], "func": pld_ext_001_log_close_zscore_5d},
    "pld_ext_002_log_close_zscore_21d": {"inputs": ["close", "low"], "func": pld_ext_002_log_close_zscore_21d},
    "pld_ext_003_log_close_zscore_63d": {"inputs": ["close", "low"], "func": pld_ext_003_log_close_zscore_63d},
    "pld_ext_004_log_close_zscore_126d": {"inputs": ["close", "low"], "func": pld_ext_004_log_close_zscore_126d},
    "pld_ext_005_log_close_pctrank_5d": {"inputs": ["close", "low"], "func": pld_ext_005_log_close_pctrank_5d},
    "pld_ext_006_log_close_pctrank_63d": {"inputs": ["close", "low"], "func": pld_ext_006_log_close_pctrank_63d},
    "pld_ext_007_log_close_pctrank_126d": {"inputs": ["close", "low"], "func": pld_ext_007_log_close_pctrank_126d},
    "pld_ext_008_log_close_ewma5_vs_sma252": {"inputs": ["close", "low"], "func": pld_ext_008_log_close_ewma5_vs_sma252},
    "pld_ext_009_log_close_sma21_vs_sma252": {"inputs": ["close", "low"], "func": pld_ext_009_log_close_sma21_vs_sma252},
    "pld_ext_010_log_close_skew_63d": {"inputs": ["close", "low"], "func": pld_ext_010_log_close_skew_63d},
    "pld_ext_011_close_norm_ewm21": {"inputs": ["close", "low"], "func": pld_ext_011_close_norm_ewm21},
    "pld_ext_012_close_norm_ewm63": {"inputs": ["close", "low"], "func": pld_ext_012_close_norm_ewm63},
    "pld_ext_013_close_norm_ewm126": {"inputs": ["close", "low"], "func": pld_ext_013_close_norm_ewm126},
    "pld_ext_014_close_norm_ewm252": {"inputs": ["close", "low"], "func": pld_ext_014_close_norm_ewm252},
    "pld_ext_015_close_ewm5_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_015_close_ewm5_zscore_252d},
    "pld_ext_016_close_ewm21_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_016_close_ewm21_zscore_252d},
    "pld_ext_017_close_sma5_vs_sma126": {"inputs": ["close", "low"], "func": pld_ext_017_close_sma5_vs_sma126},
    "pld_ext_018_close_sma21_vs_sma126": {"inputs": ["close", "low"], "func": pld_ext_018_close_sma21_vs_sma126},
    "pld_ext_019_close_level_pctrank_126d": {"inputs": ["close", "low"], "func": pld_ext_019_close_level_pctrank_126d},
    "pld_ext_020_close_level_pctrank_63d": {"inputs": ["close", "low"], "func": pld_ext_020_close_level_pctrank_63d},
    "pld_ext_021_low_pctrank_252d": {"inputs": ["close", "low"], "func": pld_ext_021_low_pctrank_252d},
    "pld_ext_022_low_pctrank_63d": {"inputs": ["close", "low"], "func": pld_ext_022_low_pctrank_63d},
    "pld_ext_023_low_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_023_low_zscore_252d},
    "pld_ext_024_low_zscore_63d": {"inputs": ["close", "low"], "func": pld_ext_024_low_zscore_63d},
    "pld_ext_025_low_vs_close_ratio": {"inputs": ["close", "low"], "func": pld_ext_025_low_vs_close_ratio},
    "pld_ext_026_low_vs_close_ratio_sma21": {"inputs": ["close", "low"], "func": pld_ext_026_low_vs_close_ratio_sma21},
    "pld_ext_027_low_vs_close_ratio_sma63": {"inputs": ["close", "low"], "func": pld_ext_027_low_vs_close_ratio_sma63},
    "pld_ext_028_low_below_1_flag": {"inputs": ["close", "low"], "func": pld_ext_028_low_below_1_flag},
    "pld_ext_029_low_below_1_count_21d": {"inputs": ["close", "low"], "func": pld_ext_029_low_below_1_count_21d},
    "pld_ext_030_low_below_5_count_63d": {"inputs": ["close", "low"], "func": pld_ext_030_low_below_5_count_63d},
    "pld_ext_031_close_mom5": {"inputs": ["close", "low"], "func": pld_ext_031_close_mom5},
    "pld_ext_032_close_mom21": {"inputs": ["close", "low"], "func": pld_ext_032_close_mom21},
    "pld_ext_033_close_mom63": {"inputs": ["close", "low"], "func": pld_ext_033_close_mom63},
    "pld_ext_034_close_pct_mom5": {"inputs": ["close", "low"], "func": pld_ext_034_close_pct_mom5},
    "pld_ext_035_close_pct_mom21": {"inputs": ["close", "low"], "func": pld_ext_035_close_pct_mom21},
    "pld_ext_036_close_pct_mom63": {"inputs": ["close", "low"], "func": pld_ext_036_close_pct_mom63},
    "pld_ext_037_close_pct_mom126": {"inputs": ["close", "low"], "func": pld_ext_037_close_pct_mom126},
    "pld_ext_038_close_below5_and_falling_21d": {"inputs": ["close", "low"], "func": pld_ext_038_close_below5_and_falling_21d},
    "pld_ext_039_close_below10_falling_fraction_63d": {"inputs": ["close", "low"], "func": pld_ext_039_close_below10_falling_fraction_63d},
    "pld_ext_040_close_accel_21d": {"inputs": ["close", "low"], "func": pld_ext_040_close_accel_21d},
    "pld_ext_041_below_1_streak": {"inputs": ["close", "low"], "func": pld_ext_041_below_1_streak},
    "pld_ext_042_below_3_streak": {"inputs": ["close", "low"], "func": pld_ext_042_below_3_streak},
    "pld_ext_043_below_5_streak": {"inputs": ["close", "low"], "func": pld_ext_043_below_5_streak},
    "pld_ext_044_below_10_streak": {"inputs": ["close", "low"], "func": pld_ext_044_below_10_streak},
    "pld_ext_045_below_1_count_63d": {"inputs": ["close", "low"], "func": pld_ext_045_below_1_count_63d},
    "pld_ext_046_below_2_count_63d": {"inputs": ["close", "low"], "func": pld_ext_046_below_2_count_63d},
    "pld_ext_047_below_3_count_252d": {"inputs": ["close", "low"], "func": pld_ext_047_below_3_count_252d},
    "pld_ext_048_below_5_fraction_252d": {"inputs": ["close", "low"], "func": pld_ext_048_below_5_fraction_252d},
    "pld_ext_049_below_10_fraction_252d": {"inputs": ["close", "low"], "func": pld_ext_049_below_10_fraction_252d},
    "pld_ext_050_distress_level_score": {"inputs": ["close", "low"], "func": pld_ext_050_distress_level_score},
    "pld_ext_051_close_vs_min5_ratio": {"inputs": ["close", "low"], "func": pld_ext_051_close_vs_min5_ratio},
    "pld_ext_052_close_vs_min21_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_052_close_vs_min21_zscore_252d},
    "pld_ext_053_close_vs_min63_pctrank_252d": {"inputs": ["close", "low"], "func": pld_ext_053_close_vs_min63_pctrank_252d},
    "pld_ext_054_close_vs_min252_pctrank_252d": {"inputs": ["close", "low"], "func": pld_ext_054_close_vs_min252_pctrank_252d},
    "pld_ext_055_close_at_min252_flag": {"inputs": ["close", "low"], "func": pld_ext_055_close_at_min252_flag},
    "pld_ext_056_close_at_min252_count_21d": {"inputs": ["close", "low"], "func": pld_ext_056_close_at_min252_count_21d},
    "pld_ext_057_low_at_min252_flag": {"inputs": ["close", "low"], "func": pld_ext_057_low_at_min252_flag},
    "pld_ext_058_close_below_low_sma21_flag": {"inputs": ["close", "low"], "func": pld_ext_058_close_below_low_sma21_flag},
    "pld_ext_059_close_below_low_sma63_count_63d": {"inputs": ["close", "low"], "func": pld_ext_059_close_below_low_sma63_count_63d},
    "pld_ext_060_log_close_kurt_63d": {"inputs": ["close", "low"], "func": pld_ext_060_log_close_kurt_63d},
    "pld_ext_061_close_below5_vol_fraction_21d": {"inputs": ["close", "low", "volume"], "func": pld_ext_061_close_below5_vol_fraction_21d},
    "pld_ext_062_close_below5_vol_fraction_63d": {"inputs": ["close", "low", "volume"], "func": pld_ext_062_close_below5_vol_fraction_63d},
    "pld_ext_063_close_below1_vol_fraction_252d": {"inputs": ["close", "low", "volume"], "func": pld_ext_063_close_below1_vol_fraction_252d},
    "pld_ext_064_dvol_when_below5_21d": {"inputs": ["close", "low", "volume"], "func": pld_ext_064_dvol_when_below5_21d},
    "pld_ext_065_below5_high_vol_coincidence_21d": {"inputs": ["close", "low", "volume"], "func": pld_ext_065_below5_high_vol_coincidence_21d},
    "pld_ext_066_below5_and_down_count_21d": {"inputs": ["close", "low", "volume"], "func": pld_ext_066_below5_and_down_count_21d},
    "pld_ext_067_close_below5_dvol_zscore_252d": {"inputs": ["close", "low", "volume"], "func": pld_ext_067_close_below5_dvol_zscore_252d},
    "pld_ext_068_close_pctrank_21d": {"inputs": ["close", "low"], "func": pld_ext_068_close_pctrank_21d},
    "pld_ext_069_close_pctrank_5d": {"inputs": ["close", "low"], "func": pld_ext_069_close_pctrank_5d},
    "pld_ext_070_close_sma5_vs_sma252": {"inputs": ["close", "low"], "func": pld_ext_070_close_sma5_vs_sma252},
    "pld_ext_071_close_level_skew_252d": {"inputs": ["close", "low"], "func": pld_ext_071_close_level_skew_252d},
    "pld_ext_072_log_close_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_072_log_close_zscore_252d},
    "pld_ext_073_close_new_1yr_low_streak": {"inputs": ["close", "low"], "func": pld_ext_073_close_new_1yr_low_streak},
    "pld_ext_074_distress_score_zscore_252d": {"inputs": ["close", "low"], "func": pld_ext_074_distress_score_zscore_252d},
    "pld_ext_075_close_norm_252d_min_zscore": {"inputs": ["close", "low"], "func": pld_ext_075_close_norm_252d_min_zscore},
}
