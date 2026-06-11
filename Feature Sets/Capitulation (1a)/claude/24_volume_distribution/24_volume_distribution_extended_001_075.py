"""
24_volume_distribution — Extended Features 001-075
Domain: shape of the volume distribution — deeper variants on skewness, kurtosis,
        dispersion, quantile spreads; additional windows, EWM-smoothed moments,
        price-conditioned distributional shape, regime flags, z-scores,
        pct-ranks, multi-window composites, log-moment variants.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Skewness at additional windows and log-price-weighted volume ---

def vds_ext_001_vol_skew_5d(volume: pd.Series) -> pd.Series:
    """Rolling 5-day (weekly) skewness of raw volume."""
    return _rolling_skew(volume, _TD_WEEK)


def vds_ext_002_vol_log_skew_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day skewness of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_skew(lv, _TD_HALF)


def vds_ext_003_vol_skew_21d_pct_rank_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume skew within trailing 63-day distribution."""
    sk = _rolling_skew(volume, _TD_MON)
    return sk.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vds_ext_004_vol_skew_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day volume skew within trailing 252-day distribution."""
    sk = _rolling_skew(volume, _TD_QTR)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_005_dv_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of dollar-volume (close * volume)."""
    dv = close * volume
    return _rolling_skew(dv, _TD_MON)


def vds_ext_006_dv_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of dollar-volume."""
    dv = close * volume
    return _rolling_skew(dv, _TD_QTR)


def vds_ext_007_vol_skew_ewm21(volume: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) of the 21-day rolling volume skewness."""
    sk21 = _rolling_skew(volume, _TD_MON)
    return _ewm_mean(sk21, _TD_MON)


def vds_ext_008_vol_skew_21d_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume skew vs its own 126-day distribution."""
    sk = _rolling_skew(volume, _TD_MON)
    m = _rolling_mean(sk, _TD_HALF)
    s = _rolling_std(sk, _TD_HALF)
    return _safe_div(sk - m, s)


def vds_ext_009_vol_skew_acceleration_21d_63d(volume: pd.Series) -> pd.Series:
    """Change in 21-day volume skew over the last 63 days (skew drift)."""
    sk21 = _rolling_skew(volume, _TD_MON)
    return sk21 - sk21.shift(_TD_QTR)


def vds_ext_010_vol_positive_skew_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume skew > 2 (strongly right-skewed — potential spike)."""
    return (_rolling_skew(volume, _TD_MON) > 2.0).astype(float)


# --- Group B (011-020): Kurtosis at additional windows and novel variants ---

def vds_ext_011_vol_kurt_5d(volume: pd.Series) -> pd.Series:
    """Rolling 5-day (weekly) excess kurtosis of raw volume."""
    return _rolling_kurt(volume, _TD_WEEK)


def vds_ext_012_vol_log_kurt_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day excess kurtosis of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_kurt(lv, _TD_HALF)


def vds_ext_013_vol_kurt_21d_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day kurtosis vs its own 126-day (semi-annual) distribution."""
    k = _rolling_kurt(volume, _TD_MON)
    m = _rolling_mean(k, _TD_HALF)
    s = _rolling_std(k, _TD_HALF)
    return _safe_div(k - m, s)


def vds_ext_014_vol_kurt_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day kurtosis within trailing 252-day distribution."""
    k = _rolling_kurt(volume, _TD_QTR)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_015_vol_kurt_ewm21(volume: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) of the 21-day rolling volume kurtosis."""
    k21 = _rolling_kurt(volume, _TD_MON)
    return _ewm_mean(k21, _TD_MON)


def vds_ext_016_dv_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day excess kurtosis of dollar-volume."""
    dv = close * volume
    return _rolling_kurt(dv, _TD_MON)


def vds_ext_017_dv_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of dollar-volume."""
    dv = close * volume
    return _rolling_kurt(dv, _TD_QTR)


def vds_ext_018_vol_kurt_acceleration_21d_63d(volume: pd.Series) -> pd.Series:
    """Change in 21-day volume kurtosis over the last 63 days."""
    k21 = _rolling_kurt(volume, _TD_MON)
    return k21 - k21.shift(_TD_QTR)


def vds_ext_019_vol_kurt_21d_above_hist80_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume kurtosis exceeds its own 252-day 80th percentile."""
    k = _rolling_kurt(volume, _TD_MON)
    p80 = k.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    return (k > p80).astype(float)


def vds_ext_020_vol_kurt_21d_vs_63d_diff(volume: pd.Series) -> pd.Series:
    """21-day kurtosis minus 63-day kurtosis (recent fat-tail elevation)."""
    return _rolling_kurt(volume, _TD_MON) - _rolling_kurt(volume, _TD_QTR)


# --- Group C (021-030): CV and dispersion at shorter/longer windows ---

def vds_ext_021_vol_cv_5d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of volume over 5 days."""
    return _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_mean(volume, _TD_WEEK))


def vds_ext_022_vol_cv_5d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 5-day CV vs its own 252-day distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_mean(volume, _TD_WEEK))
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def vds_ext_023_vol_cv_63d_vs_126d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 63-day CV minus 126-day CV (medium vs semi-annual dispersion gap)."""
    cv63 = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    cv126 = _safe_div(_rolling_std(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))
    return cv63 - cv126


def vds_ext_024_vol_cv_ewm21(volume: pd.Series) -> pd.Series:
    """EWM (span=21) coefficient of variation of volume."""
    return _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))


def vds_ext_025_vol_cv_ewm63(volume: pd.Series) -> pd.Series:
    """EWM (span=63) coefficient of variation of volume."""
    return _safe_div(_ewm_std(volume, _TD_QTR), _ewm_mean(volume, _TD_QTR))


def vds_ext_026_vol_log_std_5d(volume: pd.Series) -> pd.Series:
    """Rolling 5-day std of log-volume (weekly log-dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_WEEK)


def vds_ext_027_vol_log_std_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day std of log-volume (semi-annual log-dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_HALF)


def vds_ext_028_vol_log_std_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day log-volume std within trailing 252-day distribution."""
    lv = np.log(volume.clip(lower=_EPS))
    s21 = _rolling_std(lv, _TD_MON)
    return s21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_029_vol_log_std_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day log-volume std vs its own 252-day distribution."""
    lv = np.log(volume.clip(lower=_EPS))
    s63 = _rolling_std(lv, _TD_QTR)
    m = _rolling_mean(s63, _TD_YEAR)
    s = _rolling_std(s63, _TD_YEAR)
    return _safe_div(s63 - m, s)


def vds_ext_030_dv_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of dollar-volume over 21 days (price-adjusted dispersion)."""
    dv = close * volume
    return _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))


# --- Group D (031-040): IQR at additional windows with z-scores and pct-ranks ---

def vds_ext_031_vol_iqr_5d(volume: pd.Series) -> pd.Series:
    """Interquartile range (Q75 - Q25) of volume over 5 days."""
    q75 = _rolling_quantile(volume, _TD_WEEK, 0.75)
    q25 = _rolling_quantile(volume, _TD_WEEK, 0.25)
    return q75 - q25


def vds_ext_032_vol_iqr_126d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume over 126 days."""
    q75 = _rolling_quantile(volume, _TD_HALF, 0.75)
    q25 = _rolling_quantile(volume, _TD_HALF, 0.25)
    return q75 - q25


def vds_ext_033_vol_iqr_norm_252d(volume: pd.Series) -> pd.Series:
    """IQR normalized by median volume over 252 days."""
    q75 = _rolling_quantile(volume, _TD_YEAR, 0.75)
    q25 = _rolling_quantile(volume, _TD_YEAR, 0.25)
    med = _rolling_median(volume, _TD_YEAR)
    return _safe_div(q75 - q25, med)


def vds_ext_034_vol_iqr_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day IQR vs its own 252-day distribution."""
    iqr = _rolling_quantile(volume, _TD_MON, 0.75) - _rolling_quantile(volume, _TD_MON, 0.25)
    m = _rolling_mean(iqr, _TD_YEAR)
    s = _rolling_std(iqr, _TD_YEAR)
    return _safe_div(iqr - m, s)


def vds_ext_035_vol_iqr_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day IQR within trailing 252-day distribution."""
    iqr = _rolling_quantile(volume, _TD_QTR, 0.75) - _rolling_quantile(volume, _TD_QTR, 0.25)
    return iqr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_036_vol_90_10_spread_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day 90-10 percentile spread vs its 252-day distribution."""
    sp = _rolling_quantile(volume, _TD_MON, 0.90) - _rolling_quantile(volume, _TD_MON, 0.10)
    m = _rolling_mean(sp, _TD_YEAR)
    s = _rolling_std(sp, _TD_YEAR)
    return _safe_div(sp - m, s)


def vds_ext_037_vol_90_10_spread_126d(volume: pd.Series) -> pd.Series:
    """90th-10th percentile spread of volume over 126 days."""
    q90 = _rolling_quantile(volume, _TD_HALF, 0.90)
    q10 = _rolling_quantile(volume, _TD_HALF, 0.10)
    return q90 - q10


def vds_ext_038_vol_80_20_spread_21d(volume: pd.Series) -> pd.Series:
    """80th-20th percentile spread of volume over 21 days."""
    q80 = _rolling_quantile(volume, _TD_MON, 0.80)
    q20 = _rolling_quantile(volume, _TD_MON, 0.20)
    return q80 - q20


def vds_ext_039_vol_80_20_spread_norm_21d(volume: pd.Series) -> pd.Series:
    """80-20 spread normalized by median over 21 days."""
    q80 = _rolling_quantile(volume, _TD_MON, 0.80)
    q20 = _rolling_quantile(volume, _TD_MON, 0.20)
    med = _rolling_median(volume, _TD_MON)
    return _safe_div(q80 - q20, med)


def vds_ext_040_vol_iqr_ratio_63d_vs_126d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day IQR to 126-day IQR (medium vs semi-annual spread ratio)."""
    iqr63 = _rolling_quantile(volume, _TD_QTR, 0.75) - _rolling_quantile(volume, _TD_QTR, 0.25)
    iqr126 = _rolling_quantile(volume, _TD_HALF, 0.75) - _rolling_quantile(volume, _TD_HALF, 0.25)
    return _safe_div(iqr63, iqr126)


# --- Group E (041-050): Conditional (down-day vs up-day) distributional shape ---

def vds_ext_041_down_vol_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of down-day volume over 21 days (down-day volume dispersion)."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    m = _rolling_mean(down_vol, _TD_MON)
    s = _rolling_std(down_vol, _TD_MON)
    return _safe_div(s, m)


def vds_ext_042_up_vol_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of up-day volume over 21 days."""
    up_vol = volume.where(close.diff(1) > 0, np.nan)
    m = _rolling_mean(up_vol, _TD_MON)
    s = _rolling_std(up_vol, _TD_MON)
    return _safe_div(s, m)


def vds_ext_043_down_vol_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of volume on down days only."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    return _rolling_skew(down_vol, _TD_MON)


def vds_ext_044_down_vol_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day kurtosis of volume on down days only."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    return _rolling_kurt(down_vol, _TD_MON)


def vds_ext_045_down_vol_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of volume on down days only."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    return _rolling_skew(down_vol, _TD_QTR)


def vds_ext_046_down_vs_up_cv_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day CV to up-day CV over 21 days (bearish dispersion asymmetry)."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    up_vol = volume.where(close.diff(1) > 0, np.nan)
    down_cv = _safe_div(_rolling_std(down_vol, _TD_MON), _rolling_mean(down_vol, _TD_MON))
    up_cv = _safe_div(_rolling_std(up_vol, _TD_MON), _rolling_mean(up_vol, _TD_MON))
    return _safe_div(down_cv, up_cv)


def vds_ext_047_down_vol_mean_median_gap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean minus median of down-day volume over 21 days."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    return _rolling_mean(down_vol, _TD_MON) - _rolling_median(down_vol, _TD_MON)


def vds_ext_048_up_vol_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of volume on up days only."""
    up_vol = volume.where(close.diff(1) > 0, np.nan)
    return _rolling_skew(up_vol, _TD_MON)


def vds_ext_049_down_vol_tail_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Q90/Q50 of down-day volume over 21 days (upper-tail weight of bearish volume)."""
    down_vol = volume.where(close.diff(1) < 0, np.nan)
    q90 = _rolling_quantile(down_vol, _TD_MON, 0.90)
    q50 = _rolling_quantile(down_vol, _TD_MON, 0.50)
    return _safe_div(q90, q50)


def vds_ext_050_vol_skew_kurt_interaction_21d(volume: pd.Series) -> pd.Series:
    """Product of 21-day skewness and kurtosis (joint distributional extremity)."""
    sk = _rolling_skew(volume, _TD_MON)
    kt = _rolling_kurt(volume, _TD_MON)
    return sk * kt


# --- Group F (051-060): Regime flags and streaks ---

def vds_ext_051_vol_cv_above_hist80_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day CV exceeds its own 252-day 80th percentile (high dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    p80 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    return (cv > p80).astype(float)


def vds_ext_052_vol_skew_above_hist90_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume skew exceeds its own 252-day 90th percentile."""
    sk = _rolling_skew(volume, _TD_MON)
    p90 = sk.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (sk > p90).astype(float)


def vds_ext_053_vol_kurt_above_hist90_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume kurtosis exceeds its own 252-day 90th percentile."""
    k = _rolling_kurt(volume, _TD_MON)
    p90 = k.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (k > p90).astype(float)


def vds_ext_054_consec_days_cv21_above_hist75(volume: pd.Series) -> pd.Series:
    """Consecutive days 21-day CV has exceeded its own 252-day 75th percentile."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    p75 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    return _consec_streak(cv > p75)


def vds_ext_055_consec_days_skew21_positive(volume: pd.Series) -> pd.Series:
    """Consecutive days 21-day volume skew has been positive (right-tailed)."""
    sk = _rolling_skew(volume, _TD_MON)
    return _consec_streak(sk > 0.0)


def vds_ext_056_consec_days_kurt21_above3(volume: pd.Series) -> pd.Series:
    """Consecutive days 21-day excess kurtosis has been above 3 (fat-tail streak)."""
    k = _rolling_kurt(volume, _TD_MON)
    return _consec_streak(k > 3.0)


def vds_ext_057_distribution_distress_flag_21d(volume: pd.Series) -> pd.Series:
    """Composite flag: skew > p80 AND kurt > p80 simultaneously over 21 days (0/1)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    sk_p80 = sk.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    k_p80 = k.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    return ((sk > sk_p80) & (k > k_p80)).astype(float)


def vds_ext_058_distribution_distress_score_21d(volume: pd.Series) -> pd.Series:
    """Regime score: count of {CV > p75, skew > p75, kurt > p75} conditions met (0-3)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    cv_p75 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    sk_p75 = sk.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    k_p75 = k.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    return ((cv > cv_p75).astype(float) +
            (sk > sk_p75).astype(float) +
            (k > k_p75).astype(float))


def vds_ext_059_vol_cv_21d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day volume CV."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.expanding(min_periods=1).rank(pct=True)


def vds_ext_060_vol_skew_21d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day volume skewness."""
    sk = _rolling_skew(volume, _TD_MON)
    return sk.expanding(min_periods=3).rank(pct=True)


# --- Group G (061-075): Multi-window composites and novel moments ---

def vds_ext_061_vol_kurt_21d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day volume kurtosis."""
    k = _rolling_kurt(volume, _TD_MON)
    return k.expanding(min_periods=4).rank(pct=True)


def vds_ext_062_vol_iqr_norm_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day IQR/median within trailing 252-day distribution."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_norm = _safe_div(q75 - q25, med)
    return iqr_norm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_063_vol_mean_median_gap_norm_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of (mean-median)/std over 21 days within 252-day distribution."""
    m = _rolling_mean(volume, _TD_MON)
    med = _rolling_median(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    gap = _safe_div(m - med, s)
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_064_vol_tail_ratio_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Q90/Q50 tail ratio within trailing 252-day distribution."""
    q90 = _rolling_quantile(volume, _TD_MON, 0.90)
    q50 = _rolling_quantile(volume, _TD_MON, 0.50)
    tr = _safe_div(q90, q50)
    return tr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_ext_065_vol_skew_vs_kurt_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day skewness to (1 + kurtosis) — normalized shape asymmetry."""
    sk = _rolling_skew(volume, _TD_MON)
    kt = _rolling_kurt(volume, _TD_MON)
    return _safe_div(sk, (1.0 + kt.abs()))


def vds_ext_066_vol_log_mean_minus_log_median_21d(volume: pd.Series) -> pd.Series:
    """Difference: mean(log-vol) minus log(median-vol) over 21 days (log-space asymmetry)."""
    lv = np.log(volume.clip(lower=_EPS))
    log_mean = _rolling_mean(lv, _TD_MON)
    log_median = _rolling_median(lv, _TD_MON)
    return log_mean - log_median


def vds_ext_067_vol_log_mean_minus_log_median_63d(volume: pd.Series) -> pd.Series:
    """Mean(log-vol) minus log(median-vol) over 63 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_mean(lv, _TD_QTR) - _rolling_median(lv, _TD_QTR)


def vds_ext_068_vol_cv_acceleration_21d_63d(volume: pd.Series) -> pd.Series:
    """Change in 21-day CV over the last 63 days (CV acceleration)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv - cv.shift(_TD_QTR)


def vds_ext_069_vol_skew_21d_vs_63d_diff(volume: pd.Series) -> pd.Series:
    """21-day skew minus 63-day skew (recent skew elevation)."""
    return _rolling_skew(volume, _TD_MON) - _rolling_skew(volume, _TD_QTR)


def vds_ext_070_vol_kurt_126d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """126-day kurtosis minus 252-day kurtosis (semi-annual vs annual fat-tail gap)."""
    return _rolling_kurt(volume, _TD_HALF) - _rolling_kurt(volume, _TD_YEAR)


def vds_ext_071_vol_pct_rank_current_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def vds_ext_072_vol_above_q90_freq_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume exceeded the 252-day 90th percentile."""
    q90_252 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    return (volume > q90_252).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vds_ext_073_vol_below_q10_freq_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume was below the 252-day 10th percentile."""
    q10_252 = _rolling_quantile(volume, _TD_YEAR, 0.10)
    return (volume < q10_252).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vds_ext_074_vol_distribution_composite_zscore_21d(volume: pd.Series) -> pd.Series:
    """Composite z-score: average of CV z-score, skew z-score, kurt z-score (21d vs 252d)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk = _rolling_skew(volume, _TD_MON)
    kt = _rolling_kurt(volume, _TD_MON)
    def _z(s):
        m = _rolling_mean(s, _TD_YEAR)
        st = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, st)
    return (_z(cv) + _z(sk) + _z(kt)) / 3.0


def vds_ext_075_vol_capitulation_distribution_composite(volume: pd.Series) -> pd.Series:
    """Capitulation distribution composite: average pct-rank of CV, skew, kurt (21d, 252d).
    Higher = more extreme / fat-tailed / right-skewed volume distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk = _rolling_skew(volume, _TD_MON)
    kt = _rolling_kurt(volume, _TD_MON)
    cv_rank = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    sk_rank = sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    kt_rank = kt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (cv_rank.fillna(0.5) + sk_rank.fillna(0.5) + kt_rank.fillna(0.5)) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DISTRIBUTION_EXTENDED_REGISTRY_001_075 = {
    "vds_ext_001_vol_skew_5d": {"inputs": ["volume"], "func": vds_ext_001_vol_skew_5d},
    "vds_ext_002_vol_log_skew_126d": {"inputs": ["volume"], "func": vds_ext_002_vol_log_skew_126d},
    "vds_ext_003_vol_skew_21d_pct_rank_63d": {"inputs": ["volume"], "func": vds_ext_003_vol_skew_21d_pct_rank_63d},
    "vds_ext_004_vol_skew_63d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_004_vol_skew_63d_pct_rank_252d},
    "vds_ext_005_dv_skew_21d": {"inputs": ["close", "volume"], "func": vds_ext_005_dv_skew_21d},
    "vds_ext_006_dv_skew_63d": {"inputs": ["close", "volume"], "func": vds_ext_006_dv_skew_63d},
    "vds_ext_007_vol_skew_ewm21": {"inputs": ["volume"], "func": vds_ext_007_vol_skew_ewm21},
    "vds_ext_008_vol_skew_21d_zscore_126d": {"inputs": ["volume"], "func": vds_ext_008_vol_skew_21d_zscore_126d},
    "vds_ext_009_vol_skew_acceleration_21d_63d": {"inputs": ["volume"], "func": vds_ext_009_vol_skew_acceleration_21d_63d},
    "vds_ext_010_vol_positive_skew_flag_21d": {"inputs": ["volume"], "func": vds_ext_010_vol_positive_skew_flag_21d},
    "vds_ext_011_vol_kurt_5d": {"inputs": ["volume"], "func": vds_ext_011_vol_kurt_5d},
    "vds_ext_012_vol_log_kurt_126d": {"inputs": ["volume"], "func": vds_ext_012_vol_log_kurt_126d},
    "vds_ext_013_vol_kurt_21d_zscore_126d": {"inputs": ["volume"], "func": vds_ext_013_vol_kurt_21d_zscore_126d},
    "vds_ext_014_vol_kurt_63d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_014_vol_kurt_63d_pct_rank_252d},
    "vds_ext_015_vol_kurt_ewm21": {"inputs": ["volume"], "func": vds_ext_015_vol_kurt_ewm21},
    "vds_ext_016_dv_kurt_21d": {"inputs": ["close", "volume"], "func": vds_ext_016_dv_kurt_21d},
    "vds_ext_017_dv_kurt_63d": {"inputs": ["close", "volume"], "func": vds_ext_017_dv_kurt_63d},
    "vds_ext_018_vol_kurt_acceleration_21d_63d": {"inputs": ["volume"], "func": vds_ext_018_vol_kurt_acceleration_21d_63d},
    "vds_ext_019_vol_kurt_21d_above_hist80_flag": {"inputs": ["volume"], "func": vds_ext_019_vol_kurt_21d_above_hist80_flag},
    "vds_ext_020_vol_kurt_21d_vs_63d_diff": {"inputs": ["volume"], "func": vds_ext_020_vol_kurt_21d_vs_63d_diff},
    "vds_ext_021_vol_cv_5d": {"inputs": ["volume"], "func": vds_ext_021_vol_cv_5d},
    "vds_ext_022_vol_cv_5d_zscore_252d": {"inputs": ["volume"], "func": vds_ext_022_vol_cv_5d_zscore_252d},
    "vds_ext_023_vol_cv_63d_vs_126d_diff": {"inputs": ["volume"], "func": vds_ext_023_vol_cv_63d_vs_126d_diff},
    "vds_ext_024_vol_cv_ewm21": {"inputs": ["volume"], "func": vds_ext_024_vol_cv_ewm21},
    "vds_ext_025_vol_cv_ewm63": {"inputs": ["volume"], "func": vds_ext_025_vol_cv_ewm63},
    "vds_ext_026_vol_log_std_5d": {"inputs": ["volume"], "func": vds_ext_026_vol_log_std_5d},
    "vds_ext_027_vol_log_std_126d": {"inputs": ["volume"], "func": vds_ext_027_vol_log_std_126d},
    "vds_ext_028_vol_log_std_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_028_vol_log_std_21d_pct_rank_252d},
    "vds_ext_029_vol_log_std_63d_zscore_252d": {"inputs": ["volume"], "func": vds_ext_029_vol_log_std_63d_zscore_252d},
    "vds_ext_030_dv_cv_21d": {"inputs": ["close", "volume"], "func": vds_ext_030_dv_cv_21d},
    "vds_ext_031_vol_iqr_5d": {"inputs": ["volume"], "func": vds_ext_031_vol_iqr_5d},
    "vds_ext_032_vol_iqr_126d": {"inputs": ["volume"], "func": vds_ext_032_vol_iqr_126d},
    "vds_ext_033_vol_iqr_norm_252d": {"inputs": ["volume"], "func": vds_ext_033_vol_iqr_norm_252d},
    "vds_ext_034_vol_iqr_21d_zscore_252d": {"inputs": ["volume"], "func": vds_ext_034_vol_iqr_21d_zscore_252d},
    "vds_ext_035_vol_iqr_63d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_035_vol_iqr_63d_pct_rank_252d},
    "vds_ext_036_vol_90_10_spread_21d_zscore_252d": {"inputs": ["volume"], "func": vds_ext_036_vol_90_10_spread_21d_zscore_252d},
    "vds_ext_037_vol_90_10_spread_126d": {"inputs": ["volume"], "func": vds_ext_037_vol_90_10_spread_126d},
    "vds_ext_038_vol_80_20_spread_21d": {"inputs": ["volume"], "func": vds_ext_038_vol_80_20_spread_21d},
    "vds_ext_039_vol_80_20_spread_norm_21d": {"inputs": ["volume"], "func": vds_ext_039_vol_80_20_spread_norm_21d},
    "vds_ext_040_vol_iqr_ratio_63d_vs_126d": {"inputs": ["volume"], "func": vds_ext_040_vol_iqr_ratio_63d_vs_126d},
    "vds_ext_041_down_vol_cv_21d": {"inputs": ["close", "volume"], "func": vds_ext_041_down_vol_cv_21d},
    "vds_ext_042_up_vol_cv_21d": {"inputs": ["close", "volume"], "func": vds_ext_042_up_vol_cv_21d},
    "vds_ext_043_down_vol_skew_21d": {"inputs": ["close", "volume"], "func": vds_ext_043_down_vol_skew_21d},
    "vds_ext_044_down_vol_kurt_21d": {"inputs": ["close", "volume"], "func": vds_ext_044_down_vol_kurt_21d},
    "vds_ext_045_down_vol_skew_63d": {"inputs": ["close", "volume"], "func": vds_ext_045_down_vol_skew_63d},
    "vds_ext_046_down_vs_up_cv_ratio_21d": {"inputs": ["close", "volume"], "func": vds_ext_046_down_vs_up_cv_ratio_21d},
    "vds_ext_047_down_vol_mean_median_gap_21d": {"inputs": ["close", "volume"], "func": vds_ext_047_down_vol_mean_median_gap_21d},
    "vds_ext_048_up_vol_skew_21d": {"inputs": ["close", "volume"], "func": vds_ext_048_up_vol_skew_21d},
    "vds_ext_049_down_vol_tail_ratio_21d": {"inputs": ["close", "volume"], "func": vds_ext_049_down_vol_tail_ratio_21d},
    "vds_ext_050_vol_skew_kurt_interaction_21d": {"inputs": ["volume"], "func": vds_ext_050_vol_skew_kurt_interaction_21d},
    "vds_ext_051_vol_cv_above_hist80_flag_21d": {"inputs": ["volume"], "func": vds_ext_051_vol_cv_above_hist80_flag_21d},
    "vds_ext_052_vol_skew_above_hist90_flag_21d": {"inputs": ["volume"], "func": vds_ext_052_vol_skew_above_hist90_flag_21d},
    "vds_ext_053_vol_kurt_above_hist90_flag_21d": {"inputs": ["volume"], "func": vds_ext_053_vol_kurt_above_hist90_flag_21d},
    "vds_ext_054_consec_days_cv21_above_hist75": {"inputs": ["volume"], "func": vds_ext_054_consec_days_cv21_above_hist75},
    "vds_ext_055_consec_days_skew21_positive": {"inputs": ["volume"], "func": vds_ext_055_consec_days_skew21_positive},
    "vds_ext_056_consec_days_kurt21_above3": {"inputs": ["volume"], "func": vds_ext_056_consec_days_kurt21_above3},
    "vds_ext_057_distribution_distress_flag_21d": {"inputs": ["volume"], "func": vds_ext_057_distribution_distress_flag_21d},
    "vds_ext_058_distribution_distress_score_21d": {"inputs": ["volume"], "func": vds_ext_058_distribution_distress_score_21d},
    "vds_ext_059_vol_cv_21d_expanding_pct_rank": {"inputs": ["volume"], "func": vds_ext_059_vol_cv_21d_expanding_pct_rank},
    "vds_ext_060_vol_skew_21d_expanding_pct_rank": {"inputs": ["volume"], "func": vds_ext_060_vol_skew_21d_expanding_pct_rank},
    "vds_ext_061_vol_kurt_21d_expanding_pct_rank": {"inputs": ["volume"], "func": vds_ext_061_vol_kurt_21d_expanding_pct_rank},
    "vds_ext_062_vol_iqr_norm_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_062_vol_iqr_norm_21d_pct_rank_252d},
    "vds_ext_063_vol_mean_median_gap_norm_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_063_vol_mean_median_gap_norm_21d_pct_rank_252d},
    "vds_ext_064_vol_tail_ratio_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_ext_064_vol_tail_ratio_21d_pct_rank_252d},
    "vds_ext_065_vol_skew_vs_kurt_ratio_21d": {"inputs": ["volume"], "func": vds_ext_065_vol_skew_vs_kurt_ratio_21d},
    "vds_ext_066_vol_log_mean_minus_log_median_21d": {"inputs": ["volume"], "func": vds_ext_066_vol_log_mean_minus_log_median_21d},
    "vds_ext_067_vol_log_mean_minus_log_median_63d": {"inputs": ["volume"], "func": vds_ext_067_vol_log_mean_minus_log_median_63d},
    "vds_ext_068_vol_cv_acceleration_21d_63d": {"inputs": ["volume"], "func": vds_ext_068_vol_cv_acceleration_21d_63d},
    "vds_ext_069_vol_skew_21d_vs_63d_diff": {"inputs": ["volume"], "func": vds_ext_069_vol_skew_21d_vs_63d_diff},
    "vds_ext_070_vol_kurt_126d_vs_252d_diff": {"inputs": ["volume"], "func": vds_ext_070_vol_kurt_126d_vs_252d_diff},
    "vds_ext_071_vol_pct_rank_current_126d": {"inputs": ["volume"], "func": vds_ext_071_vol_pct_rank_current_126d},
    "vds_ext_072_vol_above_q90_freq_21d": {"inputs": ["volume"], "func": vds_ext_072_vol_above_q90_freq_21d},
    "vds_ext_073_vol_below_q10_freq_21d": {"inputs": ["volume"], "func": vds_ext_073_vol_below_q10_freq_21d},
    "vds_ext_074_vol_distribution_composite_zscore_21d": {"inputs": ["volume"], "func": vds_ext_074_vol_distribution_composite_zscore_21d},
    "vds_ext_075_vol_capitulation_distribution_composite": {"inputs": ["volume"], "func": vds_ext_075_vol_capitulation_distribution_composite},
}
