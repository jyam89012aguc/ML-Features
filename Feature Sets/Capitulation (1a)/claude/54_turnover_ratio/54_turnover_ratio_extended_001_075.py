"""
54_turnover_ratio -- Extended Features 001-075
Domain: long-horizon turnover-rate extremes via price/volume proxy -- deeper variants:
        skew/kurtosis of volume, volume streak composites, EWM cross-window ratios,
        volume momentum, intraday proxy turnover, distributional shape metrics,
        volume-adjusted price momentum, multi-window float-proxy composites.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- multi-year turnover extremes, illiquidity signals
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_TD_2YR  = 504
_TD_3YR  = 756
_EPS     = 1e-9


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

def _dollar_volume(close, volume):
    return close * volume

def _turnover_proxy(volume, window):
    return _safe_div(volume, _rolling_mean(volume, window))


# --- Group A (001-010): Volume skew and kurtosis ---

def tnv_ext_001_vol_skew_21d(close, volume):
    """21-day rolling skewness of volume."""
    return _roll_skew(volume, _TD_MON)

def tnv_ext_002_vol_skew_63d(close, volume):
    """63-day rolling skewness of volume."""
    return _roll_skew(volume, _TD_QTR)

def tnv_ext_003_vol_skew_126d(close, volume):
    """126-day rolling skewness of volume."""
    return _roll_skew(volume, _TD_HALF)

def tnv_ext_004_vol_kurt_63d(close, volume):
    """63-day rolling excess kurtosis of volume."""
    return _roll_kurt(volume, _TD_QTR)

def tnv_ext_005_vol_kurt_126d(close, volume):
    """126-day rolling excess kurtosis of volume."""
    return _roll_kurt(volume, _TD_HALF)

def tnv_ext_006_log_vol_skew_63d(close, volume):
    """63-day skewness of log(volume)."""
    return _roll_skew(_log_safe(volume), _TD_QTR)

def tnv_ext_007_log_vol_kurt_63d(close, volume):
    """63-day kurtosis of log(volume)."""
    return _roll_kurt(_log_safe(volume), _TD_QTR)

def tnv_ext_008_dvol_skew_63d(close, volume):
    """63-day skewness of dollar-volume."""
    return _roll_skew(_dollar_volume(close, volume), _TD_QTR)

def tnv_ext_009_dvol_kurt_63d(close, volume):
    """63-day kurtosis of dollar-volume."""
    return _roll_kurt(_dollar_volume(close, volume), _TD_QTR)

def tnv_ext_010_turnover_proxy_skew_252d(close, volume):
    """252-day skewness of turnover proxy (vol/252d_mean)."""
    return _roll_skew(_turnover_proxy(volume, _TD_YEAR), _TD_YEAR)


# --- Group B (011-020): Volume momentum and acceleration ---

def tnv_ext_011_vol_mom5(close, volume):
    """5-day change in volume."""
    return volume - volume.shift(5)

def tnv_ext_012_vol_mom21(close, volume):
    """21-day change in volume."""
    return volume - volume.shift(_TD_MON)

def tnv_ext_013_vol_sma5_vs_sma21(close, volume):
    """SMA5 / SMA21 of volume."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))

def tnv_ext_014_vol_sma21_vs_sma126(close, volume):
    """SMA21 / SMA126 of volume."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_HALF))

def tnv_ext_015_vol_ewma5_vs_ewma252(close, volume):
    """EWM5 / EWM252 of volume (very short vs annual)."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_YEAR))

def tnv_ext_016_vol_ewma21_vs_ewma504(close, volume):
    """EWM21 / EWM504 of volume."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_2YR))

def tnv_ext_017_log_vol_zscore_21d(close, volume):
    """21-day z-score of log(volume)."""
    return _zscore(_log_safe(volume), _TD_MON)

def tnv_ext_018_log_vol_zscore_63d(close, volume):
    """63-day z-score of log(volume)."""
    return _zscore(_log_safe(volume), _TD_QTR)

def tnv_ext_019_log_vol_pctrank_63d(close, volume):
    """63-day percentile rank of log(volume)."""
    return _pct_rank(_log_safe(volume), _TD_QTR)

def tnv_ext_020_log_vol_pctrank_252d(close, volume):
    """252-day percentile rank of log(volume)."""
    return _pct_rank(_log_safe(volume), _TD_YEAR)


# --- Group C (021-030): Turnover proxy variants ---

def tnv_ext_021_turnover_proxy_63d(close, volume):
    """Volume normalized by 63-day rolling mean (quarterly turnover proxy)."""
    return _turnover_proxy(volume, _TD_QTR)

def tnv_ext_022_turnover_proxy_126d(close, volume):
    """Volume normalized by 126-day rolling mean (semi-annual proxy)."""
    return _turnover_proxy(volume, _TD_HALF)

def tnv_ext_023_turnover_proxy_21d(close, volume):
    """Volume normalized by 21-day rolling mean (monthly proxy)."""
    return _turnover_proxy(volume, _TD_MON)

def tnv_ext_024_turnover_proxy_21d_pctrank_504d(close, volume):
    """504-day pctrank of 21d turnover proxy."""
    return _pct_rank(_turnover_proxy(volume, _TD_MON), _TD_2YR)

def tnv_ext_025_turnover_proxy_63d_zscore_252d(close, volume):
    """252-day z-score of 63d turnover proxy."""
    return _zscore(_turnover_proxy(volume, _TD_QTR), _TD_YEAR)

def tnv_ext_026_turnover_proxy_63d_pctrank_756d(close, volume):
    """756-day pctrank of 63d turnover proxy."""
    return _pct_rank(_turnover_proxy(volume, _TD_QTR), _TD_3YR)

def tnv_ext_027_turnover_proxy_252d_zscore_252d(close, volume):
    """252-day z-score of 252d turnover proxy."""
    return _zscore(_turnover_proxy(volume, _TD_YEAR), _TD_YEAR)

def tnv_ext_028_turnover_proxy_mom21(close, volume):
    """21-day change in 252d turnover proxy."""
    tp = _turnover_proxy(volume, _TD_YEAR)
    return tp - tp.shift(_TD_MON)

def tnv_ext_029_turnover_proxy_skew_63d(close, volume):
    """63-day skewness of 252d turnover proxy."""
    return _roll_skew(_turnover_proxy(volume, _TD_YEAR), _TD_QTR)

def tnv_ext_030_turnover_proxy_kurt_63d(close, volume):
    """63-day kurtosis of 252d turnover proxy."""
    return _roll_kurt(_turnover_proxy(volume, _TD_YEAR), _TD_QTR)


# --- Group D (031-040): Dollar-volume deepening ---

def tnv_ext_031_dvol_zscore_63d(close, volume):
    """63-day z-score of dollar-volume."""
    return _zscore(_dollar_volume(close, volume), _TD_QTR)

def tnv_ext_032_dvol_zscore_126d(close, volume):
    """126-day z-score of dollar-volume."""
    return _zscore(_dollar_volume(close, volume), _TD_HALF)

def tnv_ext_033_dvol_pctrank_126d(close, volume):
    """126-day percentile rank of dollar-volume."""
    return _pct_rank(_dollar_volume(close, volume), _TD_HALF)

def tnv_ext_034_dvol_sma5_vs_sma252(close, volume):
    """SMA5 / SMA252 of dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_WEEK), _rolling_mean(dv, _TD_YEAR))

def tnv_ext_035_dvol_sma21_vs_sma504(close, volume):
    """SMA21 / SMA504 of dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_2YR))

def tnv_ext_036_dvol_ewma21_vs_ewma252(close, volume):
    """EWM21 / EWM252 of dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_YEAR))

def tnv_ext_037_dvol_mom21(close, volume):
    """21-day change in dollar-volume."""
    dv = _dollar_volume(close, volume)
    return dv - dv.shift(_TD_MON)

def tnv_ext_038_dvol_skew_252d(close, volume):
    """252-day skewness of dollar-volume."""
    return _roll_skew(_dollar_volume(close, volume), _TD_YEAR)

def tnv_ext_039_log_dvol_zscore_63d(close, volume):
    """63-day z-score of log(dollar-volume)."""
    return _zscore(_log_safe(_dollar_volume(close, volume)), _TD_QTR)

def tnv_ext_040_log_dvol_pctrank_504d(close, volume):
    """504-day percentile rank of log(dollar-volume)."""
    return _pct_rank(_log_safe(_dollar_volume(close, volume)), _TD_2YR)


# --- Group E (041-050): Vol conditioned on price direction ---

def tnv_ext_041_vol_down_day_sma63(close, volume):
    """63-day SMA of volume on down days."""
    dn = (close.pct_change(1) < 0).astype(float)
    return _safe_div(_rolling_sum(volume * dn, _TD_QTR), _rolling_sum(dn, _TD_QTR))

def tnv_ext_042_vol_up_day_sma63(close, volume):
    """63-day SMA of volume on up days."""
    up = (close.pct_change(1) >= 0).astype(float)
    return _safe_div(_rolling_sum(volume * up, _TD_QTR), _rolling_sum(up, _TD_QTR))

def tnv_ext_043_vol_down_vs_up_ratio_63d(close, volume):
    """63-day ratio: mean vol on down days / mean vol on up days."""
    dn = (close.pct_change(1) < 0).astype(float)
    up = 1.0 - dn
    dm = _safe_div(_rolling_sum(volume * dn, _TD_QTR), _rolling_sum(dn, _TD_QTR))
    um = _safe_div(_rolling_sum(volume * up, _TD_QTR), _rolling_sum(up, _TD_QTR))
    return _safe_div(dm, um)

def tnv_ext_044_vol_down_fraction_63d(close, volume):
    """Fraction of total 63d volume on down days."""
    dn = (close.pct_change(1) < 0).astype(float)
    return _safe_div(_rolling_sum(volume * dn, _TD_QTR), _rolling_sum(volume, _TD_QTR))

def tnv_ext_045_vol_down_fraction_126d(close, volume):
    """Fraction of total 126d volume on down days."""
    dn = (close.pct_change(1) < 0).astype(float)
    return _safe_div(_rolling_sum(volume * dn, _TD_HALF), _rolling_sum(volume, _TD_HALF))

def tnv_ext_046_vol_down_vs_up_pctrank_252d(close, volume):
    """252-day pctrank of down-vol-to-up-vol ratio."""
    dn = (close.pct_change(1) < 0).astype(float)
    up = 1.0 - dn
    dm = _safe_div(_rolling_sum(volume * dn, _TD_MON), _rolling_sum(dn, _TD_MON))
    um = _safe_div(_rolling_sum(volume * up, _TD_MON), _rolling_sum(up, _TD_MON))
    ratio = _safe_div(dm, um)
    return _pct_rank(ratio, _TD_YEAR)

def tnv_ext_047_vol_down_fraction_zscore_252d(close, volume):
    """252-day z-score of 21d down-vol fraction."""
    dn = (close.pct_change(1) < 0).astype(float)
    frac = _safe_div(_rolling_sum(volume * dn, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _zscore(frac, _TD_YEAR)

def tnv_ext_048_dvol_down_fraction_252d(close, volume):
    """Fraction of 252d dollar-volume on down days."""
    dv = _dollar_volume(close, volume)
    dn = (close.pct_change(1) < 0).astype(float)
    return _safe_div(_rolling_sum(dv * dn, _TD_YEAR), _rolling_sum(dv, _TD_YEAR))

def tnv_ext_049_vol_down_pctrank_252d(close, volume):
    """252-day pctrank of volume on down days."""
    dn = (close.pct_change(1) < 0).astype(float)
    vol_dn = volume * dn
    return _pct_rank(vol_dn, _TD_YEAR)

def tnv_ext_050_vol_down_zscore_252d(close, volume):
    """252-day z-score of volume on down days."""
    dn = (close.pct_change(1) < 0).astype(float)
    return _zscore(volume * dn, _TD_YEAR)


# --- Group F (051-060): Streak and regime features ---

def tnv_ext_051_vol_above_252d_mean_consec(close, volume):
    """Consecutive days where volume > its 252d mean."""
    return _consec_streak(volume > _rolling_mean(volume, _TD_YEAR))

def tnv_ext_052_vol_below_252d_mean_consec(close, volume):
    """Consecutive days where volume < its 252d mean."""
    return _consec_streak(volume < _rolling_mean(volume, _TD_YEAR))

def tnv_ext_053_vol_below_504d_mean_consec(close, volume):
    """Consecutive days where volume < its 504d mean."""
    return _consec_streak(volume < _rolling_mean(volume, _TD_2YR))

def tnv_ext_054_vol_pctrank_252d_below50_consec(close, volume):
    """Consecutive days where vol pctrank(252d) < 0.5."""
    return _consec_streak(_pct_rank(volume, _TD_YEAR) < 0.5)

def tnv_ext_055_low_turnover_fraction_504d(close, volume):
    """Fraction of 504d days where vol < 50% of 504d mean (low turnover)."""
    tp504 = _turnover_proxy(volume, _TD_2YR)
    return _rolling_sum((tp504 < 0.5).astype(float), _TD_2YR) / _TD_2YR

def tnv_ext_056_high_turnover_streak_504d(close, volume):
    """Consecutive days where vol > 2x its 504d mean."""
    return _consec_streak(volume > 2.0 * _rolling_mean(volume, _TD_2YR))

def tnv_ext_057_vol_new_126d_low_flag(close, volume):
    """Flag: volume is at its 126-day minimum."""
    return (volume <= _rolling_min(volume, _TD_HALF)).astype(float)

def tnv_ext_058_vol_new_252d_low_count_63d(close, volume):
    """63-day count of days where volume hits a 252-day low."""
    flag = (volume <= _rolling_min(volume, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_QTR)

def tnv_ext_059_dvol_new_252d_low_flag(close, volume):
    """Flag: dollar-volume at its 252-day minimum."""
    dv = _dollar_volume(close, volume)
    return (dv <= _rolling_min(dv, _TD_YEAR)).astype(float)

def tnv_ext_060_vol_range_252d(close, volume):
    """252-day max volume minus 252d min volume (range of turnover)."""
    return _rolling_max(volume, _TD_YEAR) - _rolling_min(volume, _TD_YEAR)


# --- Group G (061-070): EWM ratio and composites ---

def tnv_ext_061_vol_ewma5(close, volume):
    """5-day EWM of volume."""
    return _ewm_mean(volume, _TD_WEEK)

def tnv_ext_062_vol_ewma63(close, volume):
    """63-day EWM of volume."""
    return _ewm_mean(volume, _TD_QTR)

def tnv_ext_063_vol_ewma126(close, volume):
    """126-day EWM of volume."""
    return _ewm_mean(volume, _TD_HALF)

def tnv_ext_064_vol_ewma5_vs_ewma504(close, volume):
    """EWM5 / EWM504 of volume."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_2YR))

def tnv_ext_065_vol_ewma63_vs_ewma504(close, volume):
    """EWM63 / EWM504 of volume."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_2YR))

def tnv_ext_066_dvol_ewma5_vs_ewma504(close, volume):
    """EWM5 / EWM504 of dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_WEEK), _ewm_mean(dv, _TD_2YR))

def tnv_ext_067_vol_std_ratio_21_252(close, volume):
    """Ratio of 21d std to 252d std of volume (short/long vol ratio)."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_std(volume, _TD_YEAR))

def tnv_ext_068_vol_std_ratio_63_504(close, volume):
    """Ratio of 63d std to 504d std of volume."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_std(volume, _TD_2YR))

def tnv_ext_069_log_vol_ewma21_vs_sma252(close, volume):
    """EWM21 / SMA252 of log(volume)."""
    lv = _log_safe(volume)
    return _safe_div(_ewm_mean(lv, _TD_MON), _rolling_mean(lv, _TD_YEAR))

def tnv_ext_070_turnover_proxy_252d_consec_below1(close, volume):
    """Consecutive days where turnover proxy(252d) < 1 (below annual avg)."""
    return _consec_streak(_turnover_proxy(volume, _TD_YEAR) < 1.0)


# --- Group H (071-075): Multi-window composite distress ---

def tnv_ext_071_vol_pctrank_21d(close, volume):
    """21-day percentile rank of volume."""
    return _pct_rank(volume, _TD_MON)

def tnv_ext_072_vol_pctrank_63d(close, volume):
    """63-day percentile rank of volume."""
    return _pct_rank(volume, _TD_QTR)

def tnv_ext_073_dvol_pctrank_21d(close, volume):
    """21-day percentile rank of dollar-volume."""
    return _pct_rank(_dollar_volume(close, volume), _TD_MON)

def tnv_ext_074_vol_max_to_mean_252d(close, volume):
    """252-day max volume / 252d mean (spike intensity)."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))

def tnv_ext_075_turnover_composite_skew_252d(close, volume):
    """Composite: z-score of vol + z-score of dvol (252d), normalized by 2."""
    zv = _zscore(volume, _TD_YEAR)
    zd = _zscore(_dollar_volume(close, volume), _TD_YEAR)
    return (zv.fillna(0.0) + zd.fillna(0.0)) / 2.0


TURNOVER_RATIO_EXTENDED_REGISTRY_001_075 = {
    "tnv_ext_001_vol_skew_21d": {"inputs": ["close", "volume"], "func": tnv_ext_001_vol_skew_21d},
    "tnv_ext_002_vol_skew_63d": {"inputs": ["close", "volume"], "func": tnv_ext_002_vol_skew_63d},
    "tnv_ext_003_vol_skew_126d": {"inputs": ["close", "volume"], "func": tnv_ext_003_vol_skew_126d},
    "tnv_ext_004_vol_kurt_63d": {"inputs": ["close", "volume"], "func": tnv_ext_004_vol_kurt_63d},
    "tnv_ext_005_vol_kurt_126d": {"inputs": ["close", "volume"], "func": tnv_ext_005_vol_kurt_126d},
    "tnv_ext_006_log_vol_skew_63d": {"inputs": ["close", "volume"], "func": tnv_ext_006_log_vol_skew_63d},
    "tnv_ext_007_log_vol_kurt_63d": {"inputs": ["close", "volume"], "func": tnv_ext_007_log_vol_kurt_63d},
    "tnv_ext_008_dvol_skew_63d": {"inputs": ["close", "volume"], "func": tnv_ext_008_dvol_skew_63d},
    "tnv_ext_009_dvol_kurt_63d": {"inputs": ["close", "volume"], "func": tnv_ext_009_dvol_kurt_63d},
    "tnv_ext_010_turnover_proxy_skew_252d": {"inputs": ["close", "volume"], "func": tnv_ext_010_turnover_proxy_skew_252d},
    "tnv_ext_011_vol_mom5": {"inputs": ["close", "volume"], "func": tnv_ext_011_vol_mom5},
    "tnv_ext_012_vol_mom21": {"inputs": ["close", "volume"], "func": tnv_ext_012_vol_mom21},
    "tnv_ext_013_vol_sma5_vs_sma21": {"inputs": ["close", "volume"], "func": tnv_ext_013_vol_sma5_vs_sma21},
    "tnv_ext_014_vol_sma21_vs_sma126": {"inputs": ["close", "volume"], "func": tnv_ext_014_vol_sma21_vs_sma126},
    "tnv_ext_015_vol_ewma5_vs_ewma252": {"inputs": ["close", "volume"], "func": tnv_ext_015_vol_ewma5_vs_ewma252},
    "tnv_ext_016_vol_ewma21_vs_ewma504": {"inputs": ["close", "volume"], "func": tnv_ext_016_vol_ewma21_vs_ewma504},
    "tnv_ext_017_log_vol_zscore_21d": {"inputs": ["close", "volume"], "func": tnv_ext_017_log_vol_zscore_21d},
    "tnv_ext_018_log_vol_zscore_63d": {"inputs": ["close", "volume"], "func": tnv_ext_018_log_vol_zscore_63d},
    "tnv_ext_019_log_vol_pctrank_63d": {"inputs": ["close", "volume"], "func": tnv_ext_019_log_vol_pctrank_63d},
    "tnv_ext_020_log_vol_pctrank_252d": {"inputs": ["close", "volume"], "func": tnv_ext_020_log_vol_pctrank_252d},
    "tnv_ext_021_turnover_proxy_63d": {"inputs": ["close", "volume"], "func": tnv_ext_021_turnover_proxy_63d},
    "tnv_ext_022_turnover_proxy_126d": {"inputs": ["close", "volume"], "func": tnv_ext_022_turnover_proxy_126d},
    "tnv_ext_023_turnover_proxy_21d": {"inputs": ["close", "volume"], "func": tnv_ext_023_turnover_proxy_21d},
    "tnv_ext_024_turnover_proxy_21d_pctrank_504d": {"inputs": ["close", "volume"], "func": tnv_ext_024_turnover_proxy_21d_pctrank_504d},
    "tnv_ext_025_turnover_proxy_63d_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_ext_025_turnover_proxy_63d_zscore_252d},
    "tnv_ext_026_turnover_proxy_63d_pctrank_756d": {"inputs": ["close", "volume"], "func": tnv_ext_026_turnover_proxy_63d_pctrank_756d},
    "tnv_ext_027_turnover_proxy_252d_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_ext_027_turnover_proxy_252d_zscore_252d},
    "tnv_ext_028_turnover_proxy_mom21": {"inputs": ["close", "volume"], "func": tnv_ext_028_turnover_proxy_mom21},
    "tnv_ext_029_turnover_proxy_skew_63d": {"inputs": ["close", "volume"], "func": tnv_ext_029_turnover_proxy_skew_63d},
    "tnv_ext_030_turnover_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": tnv_ext_030_turnover_proxy_kurt_63d},
    "tnv_ext_031_dvol_zscore_63d": {"inputs": ["close", "volume"], "func": tnv_ext_031_dvol_zscore_63d},
    "tnv_ext_032_dvol_zscore_126d": {"inputs": ["close", "volume"], "func": tnv_ext_032_dvol_zscore_126d},
    "tnv_ext_033_dvol_pctrank_126d": {"inputs": ["close", "volume"], "func": tnv_ext_033_dvol_pctrank_126d},
    "tnv_ext_034_dvol_sma5_vs_sma252": {"inputs": ["close", "volume"], "func": tnv_ext_034_dvol_sma5_vs_sma252},
    "tnv_ext_035_dvol_sma21_vs_sma504": {"inputs": ["close", "volume"], "func": tnv_ext_035_dvol_sma21_vs_sma504},
    "tnv_ext_036_dvol_ewma21_vs_ewma252": {"inputs": ["close", "volume"], "func": tnv_ext_036_dvol_ewma21_vs_ewma252},
    "tnv_ext_037_dvol_mom21": {"inputs": ["close", "volume"], "func": tnv_ext_037_dvol_mom21},
    "tnv_ext_038_dvol_skew_252d": {"inputs": ["close", "volume"], "func": tnv_ext_038_dvol_skew_252d},
    "tnv_ext_039_log_dvol_zscore_63d": {"inputs": ["close", "volume"], "func": tnv_ext_039_log_dvol_zscore_63d},
    "tnv_ext_040_log_dvol_pctrank_504d": {"inputs": ["close", "volume"], "func": tnv_ext_040_log_dvol_pctrank_504d},
    "tnv_ext_041_vol_down_day_sma63": {"inputs": ["close", "volume"], "func": tnv_ext_041_vol_down_day_sma63},
    "tnv_ext_042_vol_up_day_sma63": {"inputs": ["close", "volume"], "func": tnv_ext_042_vol_up_day_sma63},
    "tnv_ext_043_vol_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": tnv_ext_043_vol_down_vs_up_ratio_63d},
    "tnv_ext_044_vol_down_fraction_63d": {"inputs": ["close", "volume"], "func": tnv_ext_044_vol_down_fraction_63d},
    "tnv_ext_045_vol_down_fraction_126d": {"inputs": ["close", "volume"], "func": tnv_ext_045_vol_down_fraction_126d},
    "tnv_ext_046_vol_down_vs_up_pctrank_252d": {"inputs": ["close", "volume"], "func": tnv_ext_046_vol_down_vs_up_pctrank_252d},
    "tnv_ext_047_vol_down_fraction_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_ext_047_vol_down_fraction_zscore_252d},
    "tnv_ext_048_dvol_down_fraction_252d": {"inputs": ["close", "volume"], "func": tnv_ext_048_dvol_down_fraction_252d},
    "tnv_ext_049_vol_down_pctrank_252d": {"inputs": ["close", "volume"], "func": tnv_ext_049_vol_down_pctrank_252d},
    "tnv_ext_050_vol_down_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_ext_050_vol_down_zscore_252d},
    "tnv_ext_051_vol_above_252d_mean_consec": {"inputs": ["close", "volume"], "func": tnv_ext_051_vol_above_252d_mean_consec},
    "tnv_ext_052_vol_below_252d_mean_consec": {"inputs": ["close", "volume"], "func": tnv_ext_052_vol_below_252d_mean_consec},
    "tnv_ext_053_vol_below_504d_mean_consec": {"inputs": ["close", "volume"], "func": tnv_ext_053_vol_below_504d_mean_consec},
    "tnv_ext_054_vol_pctrank_252d_below50_consec": {"inputs": ["close", "volume"], "func": tnv_ext_054_vol_pctrank_252d_below50_consec},
    "tnv_ext_055_low_turnover_fraction_504d": {"inputs": ["close", "volume"], "func": tnv_ext_055_low_turnover_fraction_504d},
    "tnv_ext_056_high_turnover_streak_504d": {"inputs": ["close", "volume"], "func": tnv_ext_056_high_turnover_streak_504d},
    "tnv_ext_057_vol_new_126d_low_flag": {"inputs": ["close", "volume"], "func": tnv_ext_057_vol_new_126d_low_flag},
    "tnv_ext_058_vol_new_252d_low_count_63d": {"inputs": ["close", "volume"], "func": tnv_ext_058_vol_new_252d_low_count_63d},
    "tnv_ext_059_dvol_new_252d_low_flag": {"inputs": ["close", "volume"], "func": tnv_ext_059_dvol_new_252d_low_flag},
    "tnv_ext_060_vol_range_252d": {"inputs": ["close", "volume"], "func": tnv_ext_060_vol_range_252d},
    "tnv_ext_061_vol_ewma5": {"inputs": ["close", "volume"], "func": tnv_ext_061_vol_ewma5},
    "tnv_ext_062_vol_ewma63": {"inputs": ["close", "volume"], "func": tnv_ext_062_vol_ewma63},
    "tnv_ext_063_vol_ewma126": {"inputs": ["close", "volume"], "func": tnv_ext_063_vol_ewma126},
    "tnv_ext_064_vol_ewma5_vs_ewma504": {"inputs": ["close", "volume"], "func": tnv_ext_064_vol_ewma5_vs_ewma504},
    "tnv_ext_065_vol_ewma63_vs_ewma504": {"inputs": ["close", "volume"], "func": tnv_ext_065_vol_ewma63_vs_ewma504},
    "tnv_ext_066_dvol_ewma5_vs_ewma504": {"inputs": ["close", "volume"], "func": tnv_ext_066_dvol_ewma5_vs_ewma504},
    "tnv_ext_067_vol_std_ratio_21_252": {"inputs": ["close", "volume"], "func": tnv_ext_067_vol_std_ratio_21_252},
    "tnv_ext_068_vol_std_ratio_63_504": {"inputs": ["close", "volume"], "func": tnv_ext_068_vol_std_ratio_63_504},
    "tnv_ext_069_log_vol_ewma21_vs_sma252": {"inputs": ["close", "volume"], "func": tnv_ext_069_log_vol_ewma21_vs_sma252},
    "tnv_ext_070_turnover_proxy_252d_consec_below1": {"inputs": ["close", "volume"], "func": tnv_ext_070_turnover_proxy_252d_consec_below1},
    "tnv_ext_071_vol_pctrank_21d": {"inputs": ["close", "volume"], "func": tnv_ext_071_vol_pctrank_21d},
    "tnv_ext_072_vol_pctrank_63d": {"inputs": ["close", "volume"], "func": tnv_ext_072_vol_pctrank_63d},
    "tnv_ext_073_dvol_pctrank_21d": {"inputs": ["close", "volume"], "func": tnv_ext_073_dvol_pctrank_21d},
    "tnv_ext_074_vol_max_to_mean_252d": {"inputs": ["close", "volume"], "func": tnv_ext_074_vol_max_to_mean_252d},
    "tnv_ext_075_turnover_composite_skew_252d": {"inputs": ["close", "volume"], "func": tnv_ext_075_turnover_composite_skew_252d},
}
