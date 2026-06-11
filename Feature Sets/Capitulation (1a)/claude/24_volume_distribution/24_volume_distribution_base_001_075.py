"""
24_volume_distribution — Base Features 001-075
Domain: shape of the volume distribution — skewness, kurtosis, dispersion, quantile spreads,
        mean-vs-median gap, fat-tailedness, normalized rank dispersion of volume.
        Statistical moments and distributional shape of trailing volume only.
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Rolling skewness of volume ---

def vds_001_vol_skew_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of raw volume."""
    return _rolling_skew(volume, _TD_MON)


def vds_002_vol_skew_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of raw volume."""
    return _rolling_skew(volume, _TD_QTR)


def vds_003_vol_skew_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day skewness of raw volume."""
    return _rolling_skew(volume, _TD_HALF)


def vds_004_vol_skew_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of raw volume."""
    return _rolling_skew(volume, _TD_YEAR)


def vds_005_vol_log_skew_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of log-volume (reduces leverage of spikes)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_skew(lv, _TD_MON)


def vds_006_vol_log_skew_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_skew(lv, _TD_QTR)


def vds_007_vol_log_skew_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_skew(lv, _TD_YEAR)


def vds_008_vol_skew_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume skew within trailing 252-day distribution."""
    sk = _rolling_skew(volume, _TD_MON)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_009_vol_skew_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day skew vs its own 252-day mean/std."""
    sk = _rolling_skew(volume, _TD_QTR)
    m = _rolling_mean(sk, _TD_YEAR)
    s = _rolling_std(sk, _TD_YEAR)
    return _safe_div(sk - m, s)


def vds_010_vol_skew_sign_21d(volume: pd.Series) -> pd.Series:
    """Sign of 21-day volume skew (+1 right-tail, -1 left-tail, 0 symmetric)."""
    return np.sign(_rolling_skew(volume, _TD_MON))


# --- Group B (011-020): Rolling kurtosis of volume ---

def vds_011_vol_kurt_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day excess kurtosis of raw volume (fat-tailedness)."""
    return _rolling_kurt(volume, _TD_MON)


def vds_012_vol_kurt_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of raw volume."""
    return _rolling_kurt(volume, _TD_QTR)


def vds_013_vol_kurt_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day excess kurtosis of raw volume."""
    return _rolling_kurt(volume, _TD_HALF)


def vds_014_vol_kurt_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of raw volume."""
    return _rolling_kurt(volume, _TD_YEAR)


def vds_015_vol_log_kurt_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day excess kurtosis of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_kurt(lv, _TD_MON)


def vds_016_vol_log_kurt_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_kurt(lv, _TD_QTR)


def vds_017_vol_log_kurt_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_kurt(lv, _TD_YEAR)


def vds_018_vol_kurt_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day kurtosis within trailing 252-day distribution."""
    k = _rolling_kurt(volume, _TD_MON)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_019_vol_kurt_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day kurtosis vs its own 252-day mean/std."""
    k = _rolling_kurt(volume, _TD_QTR)
    m = _rolling_mean(k, _TD_YEAR)
    s = _rolling_std(k, _TD_YEAR)
    return _safe_div(k - m, s)


def vds_020_vol_kurt_gt3_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day excess kurtosis > 3 (highly leptokurtic volume distribution)."""
    return (_rolling_kurt(volume, _TD_MON) > 3).astype(float)


# --- Group C (021-030): Coefficient of variation and std/mean dispersion ---

def vds_021_vol_cv_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of volume over 21 days."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def vds_022_vol_cv_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 63 days."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def vds_023_vol_cv_126d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 126 days."""
    return _safe_div(_rolling_std(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))


def vds_024_vol_cv_252d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 252 days."""
    return _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))


def vds_025_vol_cv_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day CV within trailing 252-day distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_026_vol_cv_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day CV vs its own 252-day distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def vds_027_vol_log_std_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day std of log-volume (log-space dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_MON)


def vds_028_vol_log_std_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day std of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_QTR)


def vds_029_vol_log_std_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day std of log-volume."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_YEAR)


def vds_030_vol_cv_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day CV to 252-day CV (relative dispersion elevation)."""
    cv21 = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    cv252 = _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    return _safe_div(cv21, cv252)


# --- Group D (031-040): IQR and quantile spreads ---

def vds_031_vol_iqr_21d(volume: pd.Series) -> pd.Series:
    """Interquartile range (Q75 - Q25) of volume over 21 days."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    return q75 - q25


def vds_032_vol_iqr_63d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume over 63 days."""
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    q25 = _rolling_quantile(volume, _TD_QTR, 0.25)
    return q75 - q25


def vds_033_vol_iqr_252d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume over 252 days."""
    q75 = _rolling_quantile(volume, _TD_YEAR, 0.75)
    q25 = _rolling_quantile(volume, _TD_YEAR, 0.25)
    return q75 - q25


def vds_034_vol_iqr_norm_21d(volume: pd.Series) -> pd.Series:
    """IQR normalized by median over 21 days (relative interquartile range)."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    return _safe_div(q75 - q25, med)


def vds_035_vol_iqr_norm_63d(volume: pd.Series) -> pd.Series:
    """IQR normalized by median over 63 days."""
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    q25 = _rolling_quantile(volume, _TD_QTR, 0.25)
    med = _rolling_median(volume, _TD_QTR)
    return _safe_div(q75 - q25, med)


def vds_036_vol_90_10_spread_21d(volume: pd.Series) -> pd.Series:
    """90th-10th percentile spread of volume over 21 days."""
    q90 = _rolling_quantile(volume, _TD_MON, 0.90)
    q10 = _rolling_quantile(volume, _TD_MON, 0.10)
    return q90 - q10


def vds_037_vol_90_10_spread_63d(volume: pd.Series) -> pd.Series:
    """90th-10th percentile spread of volume over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    return q90 - q10


def vds_038_vol_90_10_spread_252d(volume: pd.Series) -> pd.Series:
    """90th-10th percentile spread of volume over 252 days."""
    q90 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    q10 = _rolling_quantile(volume, _TD_YEAR, 0.10)
    return q90 - q10


def vds_039_vol_90_10_spread_norm_63d(volume: pd.Series) -> pd.Series:
    """90-10 spread normalized by median volume over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    med = _rolling_median(volume, _TD_QTR)
    return _safe_div(q90 - q10, med)


def vds_040_vol_95_05_spread_252d(volume: pd.Series) -> pd.Series:
    """95th-5th percentile spread of volume over 252 days (extreme-tail spread)."""
    q95 = _rolling_quantile(volume, _TD_YEAR, 0.95)
    q05 = _rolling_quantile(volume, _TD_YEAR, 0.05)
    return q95 - q05


# --- Group E (041-050): Mean-vs-median gap (distributional asymmetry) ---

def vds_041_vol_mean_minus_median_21d(volume: pd.Series) -> pd.Series:
    """Mean minus median of volume over 21 days (raw asymmetry)."""
    return _rolling_mean(volume, _TD_MON) - _rolling_median(volume, _TD_MON)


def vds_042_vol_mean_minus_median_63d(volume: pd.Series) -> pd.Series:
    """Mean minus median of volume over 63 days."""
    return _rolling_mean(volume, _TD_QTR) - _rolling_median(volume, _TD_QTR)


def vds_043_vol_mean_minus_median_252d(volume: pd.Series) -> pd.Series:
    """Mean minus median of volume over 252 days."""
    return _rolling_mean(volume, _TD_YEAR) - _rolling_median(volume, _TD_YEAR)


def vds_044_vol_mean_median_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of mean to median volume over 21 days (>1 = right-skewed distribution)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))


def vds_045_vol_mean_median_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of mean to median volume over 63 days."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def vds_046_vol_mean_median_ratio_252d(volume: pd.Series) -> pd.Series:
    """Ratio of mean to median volume over 252 days."""
    return _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))


def vds_047_vol_mean_median_gap_norm_21d(volume: pd.Series) -> pd.Series:
    """(Mean - median) / std of volume over 21 days (Pearson skewness approximation)."""
    m = _rolling_mean(volume, _TD_MON)
    med = _rolling_median(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(m - med, s)


def vds_048_vol_mean_median_gap_norm_63d(volume: pd.Series) -> pd.Series:
    """(Mean - median) / std of volume over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    med = _rolling_median(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(m - med, s)


def vds_049_vol_mean_median_gap_norm_252d(volume: pd.Series) -> pd.Series:
    """(Mean - median) / std of volume over 252 days."""
    m = _rolling_mean(volume, _TD_YEAR)
    med = _rolling_median(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    return _safe_div(m - med, s)


def vds_050_vol_median_to_q75_ratio_63d(volume: pd.Series) -> pd.Series:
    """Median / Q75 ratio over 63 days (upper half spread relative to center)."""
    med = _rolling_median(volume, _TD_QTR)
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    return _safe_div(med, q75)


# --- Group F (051-060): Fat-tailedness and extreme quantile measures ---

def vds_051_vol_tail_ratio_21d(volume: pd.Series) -> pd.Series:
    """Upper-tail fraction: Q90/Q50 ratio over 21 days."""
    q90 = _rolling_quantile(volume, _TD_MON, 0.90)
    q50 = _rolling_quantile(volume, _TD_MON, 0.50)
    return _safe_div(q90, q50)


def vds_052_vol_tail_ratio_63d(volume: pd.Series) -> pd.Series:
    """Upper-tail fraction: Q90/Q50 ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    return _safe_div(q90, q50)


def vds_053_vol_tail_ratio_252d(volume: pd.Series) -> pd.Series:
    """Upper-tail fraction: Q90/Q50 ratio over 252 days."""
    q90 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    q50 = _rolling_quantile(volume, _TD_YEAR, 0.50)
    return _safe_div(q90, q50)


def vds_054_vol_upper_lower_tail_ratio_63d(volume: pd.Series) -> pd.Series:
    """Asymmetry: (Q90-Q50) / (Q50-Q10) over 63 days (upper vs lower half)."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    return _safe_div(q90 - q50, q50 - q10)


def vds_055_vol_upper_lower_tail_ratio_252d(volume: pd.Series) -> pd.Series:
    """Asymmetry: (Q90-Q50) / (Q50-Q10) over 252 days."""
    q90 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    q50 = _rolling_quantile(volume, _TD_YEAR, 0.50)
    q10 = _rolling_quantile(volume, _TD_YEAR, 0.10)
    return _safe_div(q90 - q50, q50 - q10)


def vds_056_vol_q95_norm_63d(volume: pd.Series) -> pd.Series:
    """Q95 of volume normalized by Q50 over 63 days (right extreme vs center)."""
    q95 = _rolling_quantile(volume, _TD_QTR, 0.95)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    return _safe_div(q95, q50)


def vds_057_vol_q05_norm_63d(volume: pd.Series) -> pd.Series:
    """Q05 of volume normalized by Q50 over 63 days (left extreme vs center)."""
    q05 = _rolling_quantile(volume, _TD_QTR, 0.05)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    return _safe_div(q05, q50)


def vds_058_vol_q95_vs_q05_ratio_252d(volume: pd.Series) -> pd.Series:
    """Q95/Q05 ratio of volume over 252 days (total range ratio)."""
    q95 = _rolling_quantile(volume, _TD_YEAR, 0.95)
    q05 = _rolling_quantile(volume, _TD_YEAR, 0.05)
    return _safe_div(q95, q05)


def vds_059_vol_max_to_median_ratio_21d(volume: pd.Series) -> pd.Series:
    """Max volume / median volume over 21 days (single-spike dominance)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_median(volume, _TD_MON))


def vds_060_vol_max_to_median_ratio_63d(volume: pd.Series) -> pd.Series:
    """Max volume / median volume over 63 days."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


# --- Group G (061-075): Normalized rank dispersion of volume ---

def vds_061_vol_rank_std_21d(volume: pd.Series) -> pd.Series:
    """Std of within-window volume ranks over 21 days (rank dispersion)."""
    def _rank_std(arr):
        if len(arr) < 2:
            return np.nan
        ranks = pd.Series(arr).rank()
        return float(ranks.std())
    return volume.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_rank_std, raw=True)


def vds_062_vol_rank_std_63d(volume: pd.Series) -> pd.Series:
    """Std of within-window volume ranks over 63 days."""
    def _rank_std(arr):
        if len(arr) < 2:
            return np.nan
        ranks = pd.Series(arr).rank()
        return float(ranks.std())
    return volume.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_rank_std, raw=True)


def vds_063_vol_pct_rank_current_21d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def vds_064_vol_pct_rank_current_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vds_065_vol_pct_rank_current_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def vds_066_vol_rank_deviation_from_center_21d(volume: pd.Series) -> pd.Series:
    """Abs deviation of current volume pct-rank from 0.5 (distance from median rank)."""
    rank = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return (rank - 0.5).abs()


def vds_067_vol_rank_deviation_from_center_63d(volume: pd.Series) -> pd.Series:
    """Abs deviation of current volume pct-rank from 0.5 over 63-day window."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank - 0.5).abs()


def vds_068_vol_top_decile_freq_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63d where volume ranks in top 10% of its own window."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank >= 0.90).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_069_vol_bottom_decile_freq_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63d where volume ranks in bottom 10% of its own window."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank <= 0.10).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_070_vol_top_decile_freq_252d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252d where volume ranks in top 10% of its 252d window."""
    rank = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return (rank >= 0.90).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vds_071_vol_rank_entropy_21d(volume: pd.Series) -> pd.Series:
    """Entropy-like rank spread: std of pct-ranks over rolling 21-day window-of-windows."""
    rank21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return _rolling_std(rank21, _TD_MON)


def vds_072_vol_rank_entropy_63d(volume: pd.Series) -> pd.Series:
    """Entropy-like rank spread: std of 21-day pct-ranks smoothed over 63 days."""
    rank21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return _rolling_std(rank21, _TD_QTR)


def vds_073_vol_above_median_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume exceeded the 21-day rolling median."""
    med = _rolling_median(volume, _TD_MON)
    return (volume > med).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vds_074_vol_above_median_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume exceeded the 63-day rolling median."""
    med = _rolling_median(volume, _TD_QTR)
    return (volume > med).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_075_vol_above_median_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume exceeded the 252-day rolling median."""
    med = _rolling_median(volume, _TD_YEAR)
    return (volume > med).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


# --- Group H (151-175): Quantile ratios, log-space IQR, above-mean fractions, misc ---

def vds_151_vol_q75_q25_ratio_21d(volume: pd.Series) -> pd.Series:
    """Q75/Q25 ratio of volume over 21 days (multiplicative IQR spread)."""
    return _safe_div(_rolling_quantile(volume, _TD_MON, 0.75), _rolling_quantile(volume, _TD_MON, 0.25))


def vds_152_vol_q75_q25_ratio_63d(volume: pd.Series) -> pd.Series:
    """Q75/Q25 ratio of volume over 63 days."""
    return _safe_div(_rolling_quantile(volume, _TD_QTR, 0.75), _rolling_quantile(volume, _TD_QTR, 0.25))


def vds_153_vol_q75_q25_ratio_252d(volume: pd.Series) -> pd.Series:
    """Q75/Q25 ratio of volume over 252 days."""
    return _safe_div(_rolling_quantile(volume, _TD_YEAR, 0.75), _rolling_quantile(volume, _TD_YEAR, 0.25))


def vds_154_vol_q90_q10_ratio_63d(volume: pd.Series) -> pd.Series:
    """Q90/Q10 ratio of volume over 63 days (extreme percentile spread ratio)."""
    return _safe_div(_rolling_quantile(volume, _TD_QTR, 0.90), _rolling_quantile(volume, _TD_QTR, 0.10))


def vds_155_vol_q90_q10_ratio_252d(volume: pd.Series) -> pd.Series:
    """Q90/Q10 ratio of volume over 252 days."""
    return _safe_div(_rolling_quantile(volume, _TD_YEAR, 0.90), _rolling_quantile(volume, _TD_YEAR, 0.10))


def vds_156_vol_min_to_median_ratio_21d(volume: pd.Series) -> pd.Series:
    """Min volume / median volume over 21 days (lower-tail thinness)."""
    return _safe_div(_rolling_min(volume, _TD_MON), _rolling_median(volume, _TD_MON))


def vds_157_vol_min_to_median_ratio_63d(volume: pd.Series) -> pd.Series:
    """Min volume / median volume over 63 days."""
    return _safe_div(_rolling_min(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def vds_158_vol_max_to_min_ratio_21d(volume: pd.Series) -> pd.Series:
    """Max/min ratio of volume over 21 days (total range in multiplicative terms)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_min(volume, _TD_MON))


def vds_159_vol_max_to_min_ratio_63d(volume: pd.Series) -> pd.Series:
    """Max/min ratio of volume over 63 days."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_min(volume, _TD_QTR))


def vds_160_vol_max_to_min_ratio_252d(volume: pd.Series) -> pd.Series:
    """Max/min ratio of volume over 252 days (full-year extreme range ratio)."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_min(volume, _TD_YEAR))


def vds_161_vol_above_mean_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume exceeded the 21-day rolling mean."""
    mn = _rolling_mean(volume, _TD_MON)
    return (volume > mn).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vds_162_vol_above_mean_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume exceeded the 63-day rolling mean."""
    mn = _rolling_mean(volume, _TD_QTR)
    return (volume > mn).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_163_vol_above_mean_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume exceeded the 252-day rolling mean."""
    mn = _rolling_mean(volume, _TD_YEAR)
    return (volume > mn).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vds_164_vol_log_iqr_norm_21d(volume: pd.Series) -> pd.Series:
    """Normalized IQR of log-volume over 21 days (log-space relative spread)."""
    lv = np.log(volume.clip(lower=_EPS))
    q75 = _rolling_quantile(lv, _TD_MON, 0.75)
    q25 = _rolling_quantile(lv, _TD_MON, 0.25)
    med = _rolling_median(lv, _TD_MON)
    return _safe_div(q75 - q25, med.abs().clip(lower=_EPS))


def vds_165_vol_log_iqr_norm_63d(volume: pd.Series) -> pd.Series:
    """Normalized IQR of log-volume over 63 days."""
    lv = np.log(volume.clip(lower=_EPS))
    q75 = _rolling_quantile(lv, _TD_QTR, 0.75)
    q25 = _rolling_quantile(lv, _TD_QTR, 0.25)
    med = _rolling_median(lv, _TD_QTR)
    return _safe_div(q75 - q25, med.abs().clip(lower=_EPS))


def vds_166_vol_pct_rank_current_5d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 5-day window."""
    return volume.rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).rank(pct=True)


def vds_167_vol_pct_rank_current_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within trailing 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def vds_168_vol_bottom_decile_freq_252d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252d where volume ranks in bottom 10%."""
    rank = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return (rank <= 0.10).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vds_169_vol_top_quintile_freq_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63d where volume ranks in top 20%."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank >= 0.80).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_170_vol_bottom_quintile_freq_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63d where volume ranks in bottom 20%."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank <= 0.20).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_171_vol_log_cv_21d(volume: pd.Series) -> pd.Series:
    """CV of log-volume (log-std / |log-mean|) over 21 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _safe_div(_rolling_std(lv, _TD_MON), _rolling_mean(lv, _TD_MON).abs().clip(lower=_EPS))


def vds_172_vol_log_cv_63d(volume: pd.Series) -> pd.Series:
    """CV of log-volume over 63 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _safe_div(_rolling_std(lv, _TD_QTR), _rolling_mean(lv, _TD_QTR).abs().clip(lower=_EPS))


def vds_173_vol_log_cv_252d(volume: pd.Series) -> pd.Series:
    """CV of log-volume over 252 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _safe_div(_rolling_std(lv, _TD_YEAR), _rolling_mean(lv, _TD_YEAR).abs().clip(lower=_EPS))


def vds_174_vol_cv_5d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 5 days (very short-term dispersion)."""
    return _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_mean(volume, _TD_WEEK))


def vds_175_vol_iqr_norm_252d(volume: pd.Series) -> pd.Series:
    """IQR normalized by median over 252 days (long-run relative interquartile range)."""
    q75 = _rolling_quantile(volume, _TD_YEAR, 0.75)
    q25 = _rolling_quantile(volume, _TD_YEAR, 0.25)
    med = _rolling_median(volume, _TD_YEAR)
    return _safe_div(q75 - q25, med)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DISTRIBUTION_REGISTRY_001_075 = {
    "vds_001_vol_skew_21d": {"inputs": ["volume"], "func": vds_001_vol_skew_21d},
    "vds_002_vol_skew_63d": {"inputs": ["volume"], "func": vds_002_vol_skew_63d},
    "vds_003_vol_skew_126d": {"inputs": ["volume"], "func": vds_003_vol_skew_126d},
    "vds_004_vol_skew_252d": {"inputs": ["volume"], "func": vds_004_vol_skew_252d},
    "vds_005_vol_log_skew_21d": {"inputs": ["volume"], "func": vds_005_vol_log_skew_21d},
    "vds_006_vol_log_skew_63d": {"inputs": ["volume"], "func": vds_006_vol_log_skew_63d},
    "vds_007_vol_log_skew_252d": {"inputs": ["volume"], "func": vds_007_vol_log_skew_252d},
    "vds_008_vol_skew_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_008_vol_skew_21d_pct_rank_252d},
    "vds_009_vol_skew_63d_zscore_252d": {"inputs": ["volume"], "func": vds_009_vol_skew_63d_zscore_252d},
    "vds_010_vol_skew_sign_21d": {"inputs": ["volume"], "func": vds_010_vol_skew_sign_21d},
    "vds_011_vol_kurt_21d": {"inputs": ["volume"], "func": vds_011_vol_kurt_21d},
    "vds_012_vol_kurt_63d": {"inputs": ["volume"], "func": vds_012_vol_kurt_63d},
    "vds_013_vol_kurt_126d": {"inputs": ["volume"], "func": vds_013_vol_kurt_126d},
    "vds_014_vol_kurt_252d": {"inputs": ["volume"], "func": vds_014_vol_kurt_252d},
    "vds_015_vol_log_kurt_21d": {"inputs": ["volume"], "func": vds_015_vol_log_kurt_21d},
    "vds_016_vol_log_kurt_63d": {"inputs": ["volume"], "func": vds_016_vol_log_kurt_63d},
    "vds_017_vol_log_kurt_252d": {"inputs": ["volume"], "func": vds_017_vol_log_kurt_252d},
    "vds_018_vol_kurt_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_018_vol_kurt_21d_pct_rank_252d},
    "vds_019_vol_kurt_63d_zscore_252d": {"inputs": ["volume"], "func": vds_019_vol_kurt_63d_zscore_252d},
    "vds_020_vol_kurt_gt3_flag_21d": {"inputs": ["volume"], "func": vds_020_vol_kurt_gt3_flag_21d},
    "vds_021_vol_cv_21d": {"inputs": ["volume"], "func": vds_021_vol_cv_21d},
    "vds_022_vol_cv_63d": {"inputs": ["volume"], "func": vds_022_vol_cv_63d},
    "vds_023_vol_cv_126d": {"inputs": ["volume"], "func": vds_023_vol_cv_126d},
    "vds_024_vol_cv_252d": {"inputs": ["volume"], "func": vds_024_vol_cv_252d},
    "vds_025_vol_cv_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_025_vol_cv_21d_pct_rank_252d},
    "vds_026_vol_cv_63d_zscore_252d": {"inputs": ["volume"], "func": vds_026_vol_cv_63d_zscore_252d},
    "vds_027_vol_log_std_21d": {"inputs": ["volume"], "func": vds_027_vol_log_std_21d},
    "vds_028_vol_log_std_63d": {"inputs": ["volume"], "func": vds_028_vol_log_std_63d},
    "vds_029_vol_log_std_252d": {"inputs": ["volume"], "func": vds_029_vol_log_std_252d},
    "vds_030_vol_cv_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vds_030_vol_cv_ratio_21d_vs_252d},
    "vds_031_vol_iqr_21d": {"inputs": ["volume"], "func": vds_031_vol_iqr_21d},
    "vds_032_vol_iqr_63d": {"inputs": ["volume"], "func": vds_032_vol_iqr_63d},
    "vds_033_vol_iqr_252d": {"inputs": ["volume"], "func": vds_033_vol_iqr_252d},
    "vds_034_vol_iqr_norm_21d": {"inputs": ["volume"], "func": vds_034_vol_iqr_norm_21d},
    "vds_035_vol_iqr_norm_63d": {"inputs": ["volume"], "func": vds_035_vol_iqr_norm_63d},
    "vds_036_vol_90_10_spread_21d": {"inputs": ["volume"], "func": vds_036_vol_90_10_spread_21d},
    "vds_037_vol_90_10_spread_63d": {"inputs": ["volume"], "func": vds_037_vol_90_10_spread_63d},
    "vds_038_vol_90_10_spread_252d": {"inputs": ["volume"], "func": vds_038_vol_90_10_spread_252d},
    "vds_039_vol_90_10_spread_norm_63d": {"inputs": ["volume"], "func": vds_039_vol_90_10_spread_norm_63d},
    "vds_040_vol_95_05_spread_252d": {"inputs": ["volume"], "func": vds_040_vol_95_05_spread_252d},
    "vds_041_vol_mean_minus_median_21d": {"inputs": ["volume"], "func": vds_041_vol_mean_minus_median_21d},
    "vds_042_vol_mean_minus_median_63d": {"inputs": ["volume"], "func": vds_042_vol_mean_minus_median_63d},
    "vds_043_vol_mean_minus_median_252d": {"inputs": ["volume"], "func": vds_043_vol_mean_minus_median_252d},
    "vds_044_vol_mean_median_ratio_21d": {"inputs": ["volume"], "func": vds_044_vol_mean_median_ratio_21d},
    "vds_045_vol_mean_median_ratio_63d": {"inputs": ["volume"], "func": vds_045_vol_mean_median_ratio_63d},
    "vds_046_vol_mean_median_ratio_252d": {"inputs": ["volume"], "func": vds_046_vol_mean_median_ratio_252d},
    "vds_047_vol_mean_median_gap_norm_21d": {"inputs": ["volume"], "func": vds_047_vol_mean_median_gap_norm_21d},
    "vds_048_vol_mean_median_gap_norm_63d": {"inputs": ["volume"], "func": vds_048_vol_mean_median_gap_norm_63d},
    "vds_049_vol_mean_median_gap_norm_252d": {"inputs": ["volume"], "func": vds_049_vol_mean_median_gap_norm_252d},
    "vds_050_vol_median_to_q75_ratio_63d": {"inputs": ["volume"], "func": vds_050_vol_median_to_q75_ratio_63d},
    "vds_051_vol_tail_ratio_21d": {"inputs": ["volume"], "func": vds_051_vol_tail_ratio_21d},
    "vds_052_vol_tail_ratio_63d": {"inputs": ["volume"], "func": vds_052_vol_tail_ratio_63d},
    "vds_053_vol_tail_ratio_252d": {"inputs": ["volume"], "func": vds_053_vol_tail_ratio_252d},
    "vds_054_vol_upper_lower_tail_ratio_63d": {"inputs": ["volume"], "func": vds_054_vol_upper_lower_tail_ratio_63d},
    "vds_055_vol_upper_lower_tail_ratio_252d": {"inputs": ["volume"], "func": vds_055_vol_upper_lower_tail_ratio_252d},
    "vds_056_vol_q95_norm_63d": {"inputs": ["volume"], "func": vds_056_vol_q95_norm_63d},
    "vds_057_vol_q05_norm_63d": {"inputs": ["volume"], "func": vds_057_vol_q05_norm_63d},
    "vds_058_vol_q95_vs_q05_ratio_252d": {"inputs": ["volume"], "func": vds_058_vol_q95_vs_q05_ratio_252d},
    "vds_059_vol_max_to_median_ratio_21d": {"inputs": ["volume"], "func": vds_059_vol_max_to_median_ratio_21d},
    "vds_060_vol_max_to_median_ratio_63d": {"inputs": ["volume"], "func": vds_060_vol_max_to_median_ratio_63d},
    "vds_061_vol_rank_std_21d": {"inputs": ["volume"], "func": vds_061_vol_rank_std_21d},
    "vds_062_vol_rank_std_63d": {"inputs": ["volume"], "func": vds_062_vol_rank_std_63d},
    "vds_063_vol_pct_rank_current_21d": {"inputs": ["volume"], "func": vds_063_vol_pct_rank_current_21d},
    "vds_064_vol_pct_rank_current_63d": {"inputs": ["volume"], "func": vds_064_vol_pct_rank_current_63d},
    "vds_065_vol_pct_rank_current_252d": {"inputs": ["volume"], "func": vds_065_vol_pct_rank_current_252d},
    "vds_066_vol_rank_deviation_from_center_21d": {"inputs": ["volume"], "func": vds_066_vol_rank_deviation_from_center_21d},
    "vds_067_vol_rank_deviation_from_center_63d": {"inputs": ["volume"], "func": vds_067_vol_rank_deviation_from_center_63d},
    "vds_068_vol_top_decile_freq_63d": {"inputs": ["volume"], "func": vds_068_vol_top_decile_freq_63d},
    "vds_069_vol_bottom_decile_freq_63d": {"inputs": ["volume"], "func": vds_069_vol_bottom_decile_freq_63d},
    "vds_070_vol_top_decile_freq_252d": {"inputs": ["volume"], "func": vds_070_vol_top_decile_freq_252d},
    "vds_071_vol_rank_entropy_21d": {"inputs": ["volume"], "func": vds_071_vol_rank_entropy_21d},
    "vds_072_vol_rank_entropy_63d": {"inputs": ["volume"], "func": vds_072_vol_rank_entropy_63d},
    "vds_073_vol_above_median_fraction_21d": {"inputs": ["volume"], "func": vds_073_vol_above_median_fraction_21d},
    "vds_074_vol_above_median_fraction_63d": {"inputs": ["volume"], "func": vds_074_vol_above_median_fraction_63d},
    "vds_075_vol_above_median_fraction_252d": {"inputs": ["volume"], "func": vds_075_vol_above_median_fraction_252d},
    # --- New features 151-175 ---
    "vds_151_vol_q75_q25_ratio_21d": {"inputs": ["volume"], "func": vds_151_vol_q75_q25_ratio_21d},
    "vds_152_vol_q75_q25_ratio_63d": {"inputs": ["volume"], "func": vds_152_vol_q75_q25_ratio_63d},
    "vds_153_vol_q75_q25_ratio_252d": {"inputs": ["volume"], "func": vds_153_vol_q75_q25_ratio_252d},
    "vds_154_vol_q90_q10_ratio_63d": {"inputs": ["volume"], "func": vds_154_vol_q90_q10_ratio_63d},
    "vds_155_vol_q90_q10_ratio_252d": {"inputs": ["volume"], "func": vds_155_vol_q90_q10_ratio_252d},
    "vds_156_vol_min_to_median_ratio_21d": {"inputs": ["volume"], "func": vds_156_vol_min_to_median_ratio_21d},
    "vds_157_vol_min_to_median_ratio_63d": {"inputs": ["volume"], "func": vds_157_vol_min_to_median_ratio_63d},
    "vds_158_vol_max_to_min_ratio_21d": {"inputs": ["volume"], "func": vds_158_vol_max_to_min_ratio_21d},
    "vds_159_vol_max_to_min_ratio_63d": {"inputs": ["volume"], "func": vds_159_vol_max_to_min_ratio_63d},
    "vds_160_vol_max_to_min_ratio_252d": {"inputs": ["volume"], "func": vds_160_vol_max_to_min_ratio_252d},
    "vds_161_vol_above_mean_fraction_21d": {"inputs": ["volume"], "func": vds_161_vol_above_mean_fraction_21d},
    "vds_162_vol_above_mean_fraction_63d": {"inputs": ["volume"], "func": vds_162_vol_above_mean_fraction_63d},
    "vds_163_vol_above_mean_fraction_252d": {"inputs": ["volume"], "func": vds_163_vol_above_mean_fraction_252d},
    "vds_164_vol_log_iqr_norm_21d": {"inputs": ["volume"], "func": vds_164_vol_log_iqr_norm_21d},
    "vds_165_vol_log_iqr_norm_63d": {"inputs": ["volume"], "func": vds_165_vol_log_iqr_norm_63d},
    "vds_166_vol_pct_rank_current_5d": {"inputs": ["volume"], "func": vds_166_vol_pct_rank_current_5d},
    "vds_167_vol_pct_rank_current_126d": {"inputs": ["volume"], "func": vds_167_vol_pct_rank_current_126d},
    "vds_168_vol_bottom_decile_freq_252d": {"inputs": ["volume"], "func": vds_168_vol_bottom_decile_freq_252d},
    "vds_169_vol_top_quintile_freq_63d": {"inputs": ["volume"], "func": vds_169_vol_top_quintile_freq_63d},
    "vds_170_vol_bottom_quintile_freq_63d": {"inputs": ["volume"], "func": vds_170_vol_bottom_quintile_freq_63d},
    "vds_171_vol_log_cv_21d": {"inputs": ["volume"], "func": vds_171_vol_log_cv_21d},
    "vds_172_vol_log_cv_63d": {"inputs": ["volume"], "func": vds_172_vol_log_cv_63d},
    "vds_173_vol_log_cv_252d": {"inputs": ["volume"], "func": vds_173_vol_log_cv_252d},
    "vds_174_vol_cv_5d": {"inputs": ["volume"], "func": vds_174_vol_cv_5d},
    "vds_175_vol_iqr_norm_252d": {"inputs": ["volume"], "func": vds_175_vol_iqr_norm_252d},
}
