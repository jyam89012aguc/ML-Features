"""
15_volume_blowoff — Base Features 001-100
Domain: volume spikes measured against a trailing baseline — blowoff volume.
Ratios, z-scores, percentile ranks of volume vs trailing median/mean; counts and
magnitudes of spike days; largest trailing spike; spike clustering and magnitude
relative to history.  Strictly spike-vs-baseline; no sustained-elevation,
single-day-climax-framing, or volume-collapse concepts.
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
    """Rolling mean with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    """Rolling median with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with min_periods = w//2."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """EWM mean with min_periods = span//2."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Natural log after clipping to _EPS."""
    return np.log(s.clip(lower=_EPS))


def _vol_ratio_vs_mean(volume: pd.Series, w: int) -> pd.Series:
    """Volume divided by its own trailing w-day mean (ratio vs mean baseline)."""
    baseline = _rolling_mean(volume, w)
    return _safe_div(volume, baseline)


def _vol_ratio_vs_median(volume: pd.Series, w: int) -> pd.Series:
    """Volume divided by its own trailing w-day median (ratio vs median baseline)."""
    baseline = _rolling_median(volume, w)
    return _safe_div(volume, baseline)


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    """Z-score of volume vs trailing w-day mean and std."""
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s)


def _spike_flag(volume: pd.Series, w: int, thresh: float) -> pd.Series:
    """Binary: 1 if volume/trailing-median > thresh, else 0."""
    ratio = _vol_ratio_vs_median(volume, w)
    return (ratio > thresh).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Volume ratio vs trailing mean baseline ---

def vb_001_vol_ratio_vs_mean_21d(volume: pd.Series) -> pd.Series:
    """Volume / 21-day trailing mean (blowoff ratio, mean baseline)."""
    return _vol_ratio_vs_mean(volume, _TD_MON)


def vb_002_vol_ratio_vs_mean_63d(volume: pd.Series) -> pd.Series:
    """Volume / 63-day trailing mean (quarterly mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, _TD_QTR)


def vb_003_vol_ratio_vs_mean_126d(volume: pd.Series) -> pd.Series:
    """Volume / 126-day trailing mean (half-year mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, _TD_HALF)


def vb_004_vol_ratio_vs_mean_252d(volume: pd.Series) -> pd.Series:
    """Volume / 252-day trailing mean (annual mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, _TD_YEAR)


def vb_005_vol_ratio_vs_mean_5d(volume: pd.Series) -> pd.Series:
    """Volume / 5-day trailing mean (very short mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, _TD_WEEK)


def vb_006_log_vol_ratio_vs_mean_21d(volume: pd.Series) -> pd.Series:
    """Log of volume / 21-day mean (log blowoff ratio, compresses tails)."""
    return np.log1p(_vol_ratio_vs_mean(volume, _TD_MON))


def vb_007_log_vol_ratio_vs_mean_63d(volume: pd.Series) -> pd.Series:
    """Log of volume / 63-day mean (log ratio, quarterly baseline)."""
    return np.log1p(_vol_ratio_vs_mean(volume, _TD_QTR))


def vb_008_log_vol_ratio_vs_mean_252d(volume: pd.Series) -> pd.Series:
    """Log of volume / 252-day mean (log ratio, annual baseline)."""
    return np.log1p(_vol_ratio_vs_mean(volume, _TD_YEAR))


def vb_009_vol_ratio_mean_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """21-day mean volume / 252-day mean volume (recent vs long-run baseline shift)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def vb_010_vol_ratio_mean_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """63-day mean volume / 252-day mean volume (quarterly vs annual baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))


def vb_011_vol_ratio_mean_5d_vs_21d(volume: pd.Series) -> pd.Series:
    """5-day mean / 21-day mean (very short vs monthly baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))


def vb_012_vol_ratio_mean_5d_vs_63d(volume: pd.Series) -> pd.Series:
    """5-day mean / 63-day mean (very short vs quarterly baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


def vb_013_vol_ewm_ratio_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """EWM21 / EWM63 of volume (exponentially weighted ratio, short vs long)."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))


def vb_014_vol_ewm_ratio_5d_vs_21d(volume: pd.Series) -> pd.Series:
    """EWM5 / EWM21 of volume (very short EWM vs monthly EWM)."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_MON))


def vb_015_vol_ratio_vs_mean_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day mean ratio within trailing 252-day distribution."""
    ratio = _vol_ratio_vs_mean(volume, _TD_MON)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (016-030): Volume ratio vs trailing median baseline ---

def vb_016_vol_ratio_vs_median_21d(volume: pd.Series) -> pd.Series:
    """Volume / 21-day trailing median (robust baseline ratio)."""
    return _vol_ratio_vs_median(volume, _TD_MON)


def vb_017_vol_ratio_vs_median_63d(volume: pd.Series) -> pd.Series:
    """Volume / 63-day trailing median (quarterly robust ratio)."""
    return _vol_ratio_vs_median(volume, _TD_QTR)


def vb_018_vol_ratio_vs_median_126d(volume: pd.Series) -> pd.Series:
    """Volume / 126-day trailing median (half-year robust ratio)."""
    return _vol_ratio_vs_median(volume, _TD_HALF)


def vb_019_vol_ratio_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Volume / 252-day trailing median (annual robust ratio)."""
    return _vol_ratio_vs_median(volume, _TD_YEAR)


def vb_020_log_vol_ratio_vs_median_21d(volume: pd.Series) -> pd.Series:
    """Log of volume / 21-day median (log robust ratio)."""
    return np.log1p(_vol_ratio_vs_median(volume, _TD_MON))


def vb_021_log_vol_ratio_vs_median_63d(volume: pd.Series) -> pd.Series:
    """Log of volume / 63-day median (log robust quarterly ratio)."""
    return np.log1p(_vol_ratio_vs_median(volume, _TD_QTR))


def vb_022_log_vol_ratio_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Log of volume / 252-day median (log robust annual ratio)."""
    return np.log1p(_vol_ratio_vs_median(volume, _TD_YEAR))


def vb_023_vol_ratio_vs_median_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day median ratio in trailing 252-day distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_024_vol_ratio_vs_median_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day median ratio in trailing 252-day distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_QTR)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_025_vol_ratio_vs_median_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of volume / 252-day median (all-history extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_YEAR)
    return ratio.expanding(min_periods=5).rank(pct=True)


def vb_026_vol_ratio_median_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """21-day median / 252-day median (recent baseline vs long-run median)."""
    return _safe_div(_rolling_median(volume, _TD_MON), _rolling_median(volume, _TD_YEAR))


def vb_027_vol_ratio_median_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """63-day median / 252-day median (quarterly vs annual median baseline)."""
    return _safe_div(_rolling_median(volume, _TD_QTR), _rolling_median(volume, _TD_YEAR))


def vb_028_vol_mean_vs_median_21d(volume: pd.Series) -> pd.Series:
    """21-day mean / 21-day median (skew proxy — high means spikes pulling mean up)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))


def vb_029_vol_mean_vs_median_63d(volume: pd.Series) -> pd.Series:
    """63-day mean / 63-day median (quarterly skew proxy from spikes)."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def vb_030_vol_mean_vs_median_252d(volume: pd.Series) -> pd.Series:
    """252-day mean / 252-day median (annual skew from blowoff spikes)."""
    return _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))


# --- Group C (031-045): Volume z-scores vs baseline ---

def vb_031_vol_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 21-day mean and std (short-window spike signal)."""
    return _vol_zscore(volume, _TD_MON)


def vb_032_vol_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 63-day mean and std (quarterly spike signal)."""
    return _vol_zscore(volume, _TD_QTR)


def vb_033_vol_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 126-day mean and std (half-year spike signal)."""
    return _vol_zscore(volume, _TD_HALF)


def vb_034_vol_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 252-day mean and std (annual spike signal)."""
    return _vol_zscore(volume, _TD_YEAR)


def vb_035_vol_zscore_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume z-score in trailing 252-day distribution."""
    z = _vol_zscore(volume, _TD_MON)
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_036_vol_zscore_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day volume z-score in trailing 252-day distribution."""
    z = _vol_zscore(volume, _TD_QTR)
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_037_vol_zscore_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day z-score (all-history extremity)."""
    z = _vol_zscore(volume, _TD_YEAR)
    return z.expanding(min_periods=5).rank(pct=True)


def vb_038_log_vol_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume vs 21-day log-vol mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_MON)
    s = _rolling_std(lv, _TD_MON)
    return _safe_div(lv - m, s)


def vb_039_log_vol_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume vs 63-day log-vol mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_QTR)
    s = _rolling_std(lv, _TD_QTR)
    return _safe_div(lv - m, s)


def vb_040_log_vol_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume vs 252-day log-vol mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_YEAR)
    s = _rolling_std(lv, _TD_YEAR)
    return _safe_div(lv - m, s)


def vb_041_vol_zscore_21d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume z-score > 2 (blowoff threshold)."""
    return (_vol_zscore(volume, _TD_MON) > 2.0).astype(float)


def vb_042_vol_zscore_21d_gt3_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume z-score > 3 (extreme blowoff threshold)."""
    return (_vol_zscore(volume, _TD_MON) > 3.0).astype(float)


def vb_043_vol_zscore_63d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: 63-day volume z-score > 2 (quarterly blowoff threshold)."""
    return (_vol_zscore(volume, _TD_QTR) > 2.0).astype(float)


def vb_044_vol_zscore_252d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: 252-day volume z-score > 2 (annual blowoff threshold)."""
    return (_vol_zscore(volume, _TD_YEAR) > 2.0).astype(float)


def vb_045_vol_ratio_vs_median_21d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume > 2x 21-day median (2x median spike flag)."""
    return _spike_flag(volume, _TD_MON, 2.0)


# --- Group D (046-060): Spike count / frequency in rolling windows ---

def vb_046_spike_count_2x_median_21d(volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes (volume > 2x 21d median) in trailing 21 days."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_MON)


def vb_047_spike_count_2x_median_63d(volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes in trailing 63 days."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_QTR)


def vb_048_spike_count_2x_median_252d(volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes in trailing 252 days."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_049_spike_count_3x_median_63d(volume: pd.Series) -> pd.Series:
    """Count of 3x-median extreme spikes in trailing 63 days."""
    flag = _spike_flag(volume, _TD_MON, 3.0)
    return _rolling_count_true(flag > 0, _TD_QTR)


def vb_050_spike_count_3x_median_252d(volume: pd.Series) -> pd.Series:
    """Count of 3x-median extreme spikes in trailing 252 days."""
    flag = _spike_flag(volume, _TD_MON, 3.0)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_051_spike_fraction_2x_median_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with volume > 2x 21d median."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_MON) / _TD_MON


def vb_052_spike_fraction_2x_median_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with volume > 2x 21d median."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_QTR) / _TD_QTR


def vb_053_spike_fraction_2x_median_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with volume > 2x 21d median."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_YEAR) / _TD_YEAR


def vb_054_spike_count_zscore_gt2_21d(volume: pd.Series) -> pd.Series:
    """Count of z-score>2 spikes (21d baseline) in trailing 21 days."""
    flag = (_vol_zscore(volume, _TD_MON) > 2.0).astype(float)
    return _rolling_count_true(flag > 0, _TD_MON)


def vb_055_spike_count_zscore_gt2_63d(volume: pd.Series) -> pd.Series:
    """Count of z-score>2 spikes (21d baseline) in trailing 63 days."""
    flag = (_vol_zscore(volume, _TD_MON) > 2.0).astype(float)
    return _rolling_count_true(flag > 0, _TD_QTR)


def vb_056_spike_count_zscore_gt2_252d(volume: pd.Series) -> pd.Series:
    """Count of z-score>2 spikes (21d baseline) in trailing 252 days."""
    flag = (_vol_zscore(volume, _TD_MON) > 2.0).astype(float)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_057_spike_count_2x_mean_63d(volume: pd.Series) -> pd.Series:
    """Count of 2x-mean (21d mean) spikes in trailing 63 days."""
    flag = (_vol_ratio_vs_mean(volume, _TD_MON) > 2.0).astype(float)
    return _rolling_count_true(flag > 0, _TD_QTR)


def vb_058_spike_count_2x_mean_252d(volume: pd.Series) -> pd.Series:
    """Count of 2x-mean (21d mean) spikes in trailing 252 days."""
    flag = (_vol_ratio_vs_mean(volume, _TD_MON) > 2.0).astype(float)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_059_spike_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d spike-count-63d in 252-day distribution."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(flag > 0, _TD_QTR)
    return cnt63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_060_spike_count_2x_median_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21d spike count (all-history extremity)."""
    flag = _spike_flag(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_MON)
    return cnt.expanding(min_periods=5).rank(pct=True)


# --- Group E (061-075): Spike magnitude — largest spike and average spike size ---

def vb_061_max_vol_ratio_vs_median_21d(volume: pd.Series) -> pd.Series:
    """Max volume/21d-median ratio seen in trailing 21 days (largest recent spike)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _rolling_max(ratio, _TD_MON)


def vb_062_max_vol_ratio_vs_median_63d(volume: pd.Series) -> pd.Series:
    """Max volume/21d-median ratio seen in trailing 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _rolling_max(ratio, _TD_QTR)


def vb_063_max_vol_ratio_vs_median_126d(volume: pd.Series) -> pd.Series:
    """Max volume/21d-median ratio seen in trailing 126 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _rolling_max(ratio, _TD_HALF)


def vb_064_max_vol_ratio_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Max volume/21d-median ratio seen in trailing 252 days (annual spike record)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _rolling_max(ratio, _TD_YEAR)


def vb_065_current_vs_max_spike_63d(volume: pd.Series) -> pd.Series:
    """Current volume/21d-median ratio as fraction of 63-day maximum ratio."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    return _safe_div(ratio, mx63)


def vb_066_current_vs_max_spike_252d(volume: pd.Series) -> pd.Series:
    """Current volume/21d-median ratio as fraction of 252-day maximum ratio."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(ratio, mx252)


def vb_067_max_spike_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """21-day max spike ratio / 252-day max spike ratio (recent vs all-time extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx21 = _rolling_max(ratio, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(mx21, mx252)


def vb_068_max_spike_63d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """63-day max spike ratio / 252-day max spike ratio."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(mx63, mx252)


def vb_069_avg_spike_magnitude_21d(volume: pd.Series) -> pd.Series:
    """Mean volume/21d-median ratio on spike days only, over 21 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_ratio = ratio.where(ratio > 2.0, np.nan)
    return spike_ratio.rolling(_TD_MON, min_periods=1).mean()


def vb_070_avg_spike_magnitude_63d(volume: pd.Series) -> pd.Series:
    """Mean volume/21d-median ratio on spike days only, over 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_ratio = ratio.where(ratio > 2.0, np.nan)
    return spike_ratio.rolling(_TD_QTR, min_periods=1).mean()


def vb_071_avg_spike_magnitude_252d(volume: pd.Series) -> pd.Series:
    """Mean volume/21d-median ratio on spike days only, over 252 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_ratio = ratio.where(ratio > 2.0, np.nan)
    return spike_ratio.rolling(_TD_YEAR, min_periods=1).mean()


def vb_072_max_zscore_21d_window(volume: pd.Series) -> pd.Series:
    """Max 21-day z-score of volume seen in trailing 63 days."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_max(z, _TD_QTR)


def vb_073_max_zscore_252d_window(volume: pd.Series) -> pd.Series:
    """Max 21-day z-score of volume seen in trailing 252 days (annual spike record)."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_max(z, _TD_YEAR)


def vb_074_current_spike_ratio_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume/21d-median ratio in trailing 252-day dist."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vb_075_max_spike_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day max spike ratio (all-history extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return mx252.expanding(min_periods=5).rank(pct=True)


# --- Group F-ext (151-165): Volume-price spread and range-normalized spike signals ---

def vb_151_vol_ratio_vs_median_5d(volume: pd.Series) -> pd.Series:
    """Volume / 5-day trailing median (ultra-short robust baseline ratio)."""
    return _vol_ratio_vs_median(volume, _TD_WEEK)


def vb_152_vol_ratio_vs_median_126d(volume: pd.Series) -> pd.Series:
    """Volume / 126-day trailing median (half-year robust baseline ratio)."""
    return _vol_ratio_vs_median(volume, _TD_HALF)


def vb_153_vol_ratio_vs_mean_10d(volume: pd.Series) -> pd.Series:
    """Volume / 10-day trailing mean (bi-weekly mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, 10)


def vb_154_vol_ratio_vs_median_10d(volume: pd.Series) -> pd.Series:
    """Volume / 10-day trailing median (bi-weekly robust ratio)."""
    return _vol_ratio_vs_median(volume, 10)


def vb_155_log_vol_ratio_vs_median_5d(volume: pd.Series) -> pd.Series:
    """Log of volume / 5-day median (log blowoff ratio on ultra-short baseline)."""
    return np.log1p(_vol_ratio_vs_median(volume, _TD_WEEK))


def vb_156_log_vol_ratio_vs_median_126d(volume: pd.Series) -> pd.Series:
    """Log of volume / 126-day median (log robust half-year ratio)."""
    return np.log1p(_vol_ratio_vs_median(volume, _TD_HALF))


def vb_157_vol_ratio_median_5d_vs_63d(volume: pd.Series) -> pd.Series:
    """5-day median / 63-day median (ultra-short vs quarterly baseline shift)."""
    return _safe_div(_rolling_median(volume, _TD_WEEK), _rolling_median(volume, _TD_QTR))


def vb_158_vol_ratio_median_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """5-day median / 252-day median (ultra-short vs annual baseline shift)."""
    return _safe_div(_rolling_median(volume, _TD_WEEK), _rolling_median(volume, _TD_YEAR))


def vb_159_vol_ratio_median_126d_vs_252d(volume: pd.Series) -> pd.Series:
    """126-day median / 252-day median (half-year vs annual baseline shift)."""
    return _safe_div(_rolling_median(volume, _TD_HALF), _rolling_median(volume, _TD_YEAR))


def vb_160_vol_zscore_5d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 5-day mean and std (ultra-short spike signal)."""
    return _vol_zscore(volume, _TD_WEEK)


def vb_161_vol_zscore_10d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 10-day mean and std (bi-weekly spike signal)."""
    return _vol_zscore(volume, 10)


def vb_162_vol_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 126-day mean and std (half-year baseline z-score)."""
    return _vol_zscore(volume, _TD_HALF)


def vb_163_vol_zscore_5d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: 5-day volume z-score > 2 (ultra-short blowoff threshold)."""
    return (_vol_zscore(volume, _TD_WEEK) > 2.0).astype(float)


def vb_164_vol_zscore_126d_gt2_flag(volume: pd.Series) -> pd.Series:
    """Flag: 126-day volume z-score > 2 (half-year blowoff threshold)."""
    return (_vol_zscore(volume, _TD_HALF) > 2.0).astype(float)


def vb_165_vol_ratio_vs_median_21d_gt15_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume > 1.5x 21-day median (lower threshold spike flag)."""
    return _spike_flag(volume, _TD_MON, 1.5)


# --- Group G-ext (166-175): Spike quantile/tail and vol-momentum constructions ---

def vb_166_vol_99th_pct_252d_norm_median(volume: pd.Series) -> pd.Series:
    """99th-percentile volume over 252d normalized by 252d median (extreme tail)."""
    p99 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.99)
    med = _rolling_median(volume, _TD_YEAR)
    return _safe_div(p99, med)


def vb_167_vol_10th_pct_63d_norm_median(volume: pd.Series) -> pd.Series:
    """10th-percentile volume over 63d normalized by 63d median (thin-volume trough)."""
    p10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    med = _rolling_median(volume, _TD_QTR)
    return _safe_div(p10, med)


def vb_168_spike_count_15x_median_63d(volume: pd.Series) -> pd.Series:
    """Count of 1.5x-median spikes in trailing 63 days (lower-threshold frequency)."""
    flag = _spike_flag(volume, _TD_MON, 1.5)
    return _rolling_count_true(flag > 0, _TD_QTR)


def vb_169_spike_count_15x_median_252d(volume: pd.Series) -> pd.Series:
    """Count of 1.5x-median spikes in trailing 252 days."""
    flag = _spike_flag(volume, _TD_MON, 1.5)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_170_spike_count_4x_median_252d(volume: pd.Series) -> pd.Series:
    """Count of 4x-median ultra-extreme spikes in trailing 252 days."""
    flag = _spike_flag(volume, _TD_MON, 4.0)
    return _rolling_count_true(flag > 0, _TD_YEAR)


def vb_171_vol_ratio_vs_mean_126d(volume: pd.Series) -> pd.Series:
    """Volume / 126-day trailing mean (half-year mean baseline ratio)."""
    return _vol_ratio_vs_mean(volume, _TD_HALF)


def vb_172_vol_ewm_ratio_21d_vs_126d(volume: pd.Series) -> pd.Series:
    """EWM21 / EWM126 of volume (short vs half-year exponential baseline)."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_HALF))


def vb_173_vol_ewm_ratio_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """EWM63 / EWM252 of volume (quarterly vs annual exponential baseline)."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))


def vb_174_vol_ratio_vs_median_21d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of vol/21d-median ratio in trailing 504-day distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def vb_175_vol_zscore_252d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day volume z-score in 504-day distribution."""
    z = _vol_zscore(volume, _TD_YEAR)
    return z.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_BLOWOFF_REGISTRY_001_075 = {
    "vb_001_vol_ratio_vs_mean_21d": {"inputs": ["volume"], "func": vb_001_vol_ratio_vs_mean_21d},
    "vb_002_vol_ratio_vs_mean_63d": {"inputs": ["volume"], "func": vb_002_vol_ratio_vs_mean_63d},
    "vb_003_vol_ratio_vs_mean_126d": {"inputs": ["volume"], "func": vb_003_vol_ratio_vs_mean_126d},
    "vb_004_vol_ratio_vs_mean_252d": {"inputs": ["volume"], "func": vb_004_vol_ratio_vs_mean_252d},
    "vb_005_vol_ratio_vs_mean_5d": {"inputs": ["volume"], "func": vb_005_vol_ratio_vs_mean_5d},
    "vb_006_log_vol_ratio_vs_mean_21d": {"inputs": ["volume"], "func": vb_006_log_vol_ratio_vs_mean_21d},
    "vb_007_log_vol_ratio_vs_mean_63d": {"inputs": ["volume"], "func": vb_007_log_vol_ratio_vs_mean_63d},
    "vb_008_log_vol_ratio_vs_mean_252d": {"inputs": ["volume"], "func": vb_008_log_vol_ratio_vs_mean_252d},
    "vb_009_vol_ratio_mean_21d_vs_252d": {"inputs": ["volume"], "func": vb_009_vol_ratio_mean_21d_vs_252d},
    "vb_010_vol_ratio_mean_63d_vs_252d": {"inputs": ["volume"], "func": vb_010_vol_ratio_mean_63d_vs_252d},
    "vb_011_vol_ratio_mean_5d_vs_21d": {"inputs": ["volume"], "func": vb_011_vol_ratio_mean_5d_vs_21d},
    "vb_012_vol_ratio_mean_5d_vs_63d": {"inputs": ["volume"], "func": vb_012_vol_ratio_mean_5d_vs_63d},
    "vb_013_vol_ewm_ratio_21d_vs_63d": {"inputs": ["volume"], "func": vb_013_vol_ewm_ratio_21d_vs_63d},
    "vb_014_vol_ewm_ratio_5d_vs_21d": {"inputs": ["volume"], "func": vb_014_vol_ewm_ratio_5d_vs_21d},
    "vb_015_vol_ratio_vs_mean_21d_pct_rank_252d": {"inputs": ["volume"], "func": vb_015_vol_ratio_vs_mean_21d_pct_rank_252d},
    "vb_016_vol_ratio_vs_median_21d": {"inputs": ["volume"], "func": vb_016_vol_ratio_vs_median_21d},
    "vb_017_vol_ratio_vs_median_63d": {"inputs": ["volume"], "func": vb_017_vol_ratio_vs_median_63d},
    "vb_018_vol_ratio_vs_median_126d": {"inputs": ["volume"], "func": vb_018_vol_ratio_vs_median_126d},
    "vb_019_vol_ratio_vs_median_252d": {"inputs": ["volume"], "func": vb_019_vol_ratio_vs_median_252d},
    "vb_020_log_vol_ratio_vs_median_21d": {"inputs": ["volume"], "func": vb_020_log_vol_ratio_vs_median_21d},
    "vb_021_log_vol_ratio_vs_median_63d": {"inputs": ["volume"], "func": vb_021_log_vol_ratio_vs_median_63d},
    "vb_022_log_vol_ratio_vs_median_252d": {"inputs": ["volume"], "func": vb_022_log_vol_ratio_vs_median_252d},
    "vb_023_vol_ratio_vs_median_21d_pct_rank_252d": {"inputs": ["volume"], "func": vb_023_vol_ratio_vs_median_21d_pct_rank_252d},
    "vb_024_vol_ratio_vs_median_63d_pct_rank_252d": {"inputs": ["volume"], "func": vb_024_vol_ratio_vs_median_63d_pct_rank_252d},
    "vb_025_vol_ratio_vs_median_252d_expanding_rank": {"inputs": ["volume"], "func": vb_025_vol_ratio_vs_median_252d_expanding_rank},
    "vb_026_vol_ratio_median_21d_vs_252d": {"inputs": ["volume"], "func": vb_026_vol_ratio_median_21d_vs_252d},
    "vb_027_vol_ratio_median_63d_vs_252d": {"inputs": ["volume"], "func": vb_027_vol_ratio_median_63d_vs_252d},
    "vb_028_vol_mean_vs_median_21d": {"inputs": ["volume"], "func": vb_028_vol_mean_vs_median_21d},
    "vb_029_vol_mean_vs_median_63d": {"inputs": ["volume"], "func": vb_029_vol_mean_vs_median_63d},
    "vb_030_vol_mean_vs_median_252d": {"inputs": ["volume"], "func": vb_030_vol_mean_vs_median_252d},
    "vb_031_vol_zscore_21d": {"inputs": ["volume"], "func": vb_031_vol_zscore_21d},
    "vb_032_vol_zscore_63d": {"inputs": ["volume"], "func": vb_032_vol_zscore_63d},
    "vb_033_vol_zscore_126d": {"inputs": ["volume"], "func": vb_033_vol_zscore_126d},
    "vb_034_vol_zscore_252d": {"inputs": ["volume"], "func": vb_034_vol_zscore_252d},
    "vb_035_vol_zscore_21d_pct_rank_252d": {"inputs": ["volume"], "func": vb_035_vol_zscore_21d_pct_rank_252d},
    "vb_036_vol_zscore_63d_pct_rank_252d": {"inputs": ["volume"], "func": vb_036_vol_zscore_63d_pct_rank_252d},
    "vb_037_vol_zscore_252d_expanding_rank": {"inputs": ["volume"], "func": vb_037_vol_zscore_252d_expanding_rank},
    "vb_038_log_vol_zscore_21d": {"inputs": ["volume"], "func": vb_038_log_vol_zscore_21d},
    "vb_039_log_vol_zscore_63d": {"inputs": ["volume"], "func": vb_039_log_vol_zscore_63d},
    "vb_040_log_vol_zscore_252d": {"inputs": ["volume"], "func": vb_040_log_vol_zscore_252d},
    "vb_041_vol_zscore_21d_gt2_flag": {"inputs": ["volume"], "func": vb_041_vol_zscore_21d_gt2_flag},
    "vb_042_vol_zscore_21d_gt3_flag": {"inputs": ["volume"], "func": vb_042_vol_zscore_21d_gt3_flag},
    "vb_043_vol_zscore_63d_gt2_flag": {"inputs": ["volume"], "func": vb_043_vol_zscore_63d_gt2_flag},
    "vb_044_vol_zscore_252d_gt2_flag": {"inputs": ["volume"], "func": vb_044_vol_zscore_252d_gt2_flag},
    "vb_045_vol_ratio_vs_median_21d_gt2_flag": {"inputs": ["volume"], "func": vb_045_vol_ratio_vs_median_21d_gt2_flag},
    "vb_046_spike_count_2x_median_21d": {"inputs": ["volume"], "func": vb_046_spike_count_2x_median_21d},
    "vb_047_spike_count_2x_median_63d": {"inputs": ["volume"], "func": vb_047_spike_count_2x_median_63d},
    "vb_048_spike_count_2x_median_252d": {"inputs": ["volume"], "func": vb_048_spike_count_2x_median_252d},
    "vb_049_spike_count_3x_median_63d": {"inputs": ["volume"], "func": vb_049_spike_count_3x_median_63d},
    "vb_050_spike_count_3x_median_252d": {"inputs": ["volume"], "func": vb_050_spike_count_3x_median_252d},
    "vb_051_spike_fraction_2x_median_21d": {"inputs": ["volume"], "func": vb_051_spike_fraction_2x_median_21d},
    "vb_052_spike_fraction_2x_median_63d": {"inputs": ["volume"], "func": vb_052_spike_fraction_2x_median_63d},
    "vb_053_spike_fraction_2x_median_252d": {"inputs": ["volume"], "func": vb_053_spike_fraction_2x_median_252d},
    "vb_054_spike_count_zscore_gt2_21d": {"inputs": ["volume"], "func": vb_054_spike_count_zscore_gt2_21d},
    "vb_055_spike_count_zscore_gt2_63d": {"inputs": ["volume"], "func": vb_055_spike_count_zscore_gt2_63d},
    "vb_056_spike_count_zscore_gt2_252d": {"inputs": ["volume"], "func": vb_056_spike_count_zscore_gt2_252d},
    "vb_057_spike_count_2x_mean_63d": {"inputs": ["volume"], "func": vb_057_spike_count_2x_mean_63d},
    "vb_058_spike_count_2x_mean_252d": {"inputs": ["volume"], "func": vb_058_spike_count_2x_mean_252d},
    "vb_059_spike_pct_rank_252d": {"inputs": ["volume"], "func": vb_059_spike_pct_rank_252d},
    "vb_060_spike_count_2x_median_21d_expanding_rank": {"inputs": ["volume"], "func": vb_060_spike_count_2x_median_21d_expanding_rank},
    "vb_061_max_vol_ratio_vs_median_21d": {"inputs": ["volume"], "func": vb_061_max_vol_ratio_vs_median_21d},
    "vb_062_max_vol_ratio_vs_median_63d": {"inputs": ["volume"], "func": vb_062_max_vol_ratio_vs_median_63d},
    "vb_063_max_vol_ratio_vs_median_126d": {"inputs": ["volume"], "func": vb_063_max_vol_ratio_vs_median_126d},
    "vb_064_max_vol_ratio_vs_median_252d": {"inputs": ["volume"], "func": vb_064_max_vol_ratio_vs_median_252d},
    "vb_065_current_vs_max_spike_63d": {"inputs": ["volume"], "func": vb_065_current_vs_max_spike_63d},
    "vb_066_current_vs_max_spike_252d": {"inputs": ["volume"], "func": vb_066_current_vs_max_spike_252d},
    "vb_067_max_spike_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vb_067_max_spike_21d_vs_252d_ratio},
    "vb_068_max_spike_63d_vs_252d_ratio": {"inputs": ["volume"], "func": vb_068_max_spike_63d_vs_252d_ratio},
    "vb_069_avg_spike_magnitude_21d": {"inputs": ["volume"], "func": vb_069_avg_spike_magnitude_21d},
    "vb_070_avg_spike_magnitude_63d": {"inputs": ["volume"], "func": vb_070_avg_spike_magnitude_63d},
    "vb_071_avg_spike_magnitude_252d": {"inputs": ["volume"], "func": vb_071_avg_spike_magnitude_252d},
    "vb_072_max_zscore_21d_window": {"inputs": ["volume"], "func": vb_072_max_zscore_21d_window},
    "vb_073_max_zscore_252d_window": {"inputs": ["volume"], "func": vb_073_max_zscore_252d_window},
    "vb_074_current_spike_ratio_pct_rank_252d": {"inputs": ["volume"], "func": vb_074_current_spike_ratio_pct_rank_252d},
    "vb_075_max_spike_252d_expanding_rank": {"inputs": ["volume"], "func": vb_075_max_spike_252d_expanding_rank},
    "vb_151_vol_ratio_vs_median_5d": {"inputs": ["volume"], "func": vb_151_vol_ratio_vs_median_5d},
    "vb_152_vol_ratio_vs_median_126d": {"inputs": ["volume"], "func": vb_152_vol_ratio_vs_median_126d},
    "vb_153_vol_ratio_vs_mean_10d": {"inputs": ["volume"], "func": vb_153_vol_ratio_vs_mean_10d},
    "vb_154_vol_ratio_vs_median_10d": {"inputs": ["volume"], "func": vb_154_vol_ratio_vs_median_10d},
    "vb_155_log_vol_ratio_vs_median_5d": {"inputs": ["volume"], "func": vb_155_log_vol_ratio_vs_median_5d},
    "vb_156_log_vol_ratio_vs_median_126d": {"inputs": ["volume"], "func": vb_156_log_vol_ratio_vs_median_126d},
    "vb_157_vol_ratio_median_5d_vs_63d": {"inputs": ["volume"], "func": vb_157_vol_ratio_median_5d_vs_63d},
    "vb_158_vol_ratio_median_5d_vs_252d": {"inputs": ["volume"], "func": vb_158_vol_ratio_median_5d_vs_252d},
    "vb_159_vol_ratio_median_126d_vs_252d": {"inputs": ["volume"], "func": vb_159_vol_ratio_median_126d_vs_252d},
    "vb_160_vol_zscore_5d": {"inputs": ["volume"], "func": vb_160_vol_zscore_5d},
    "vb_161_vol_zscore_10d": {"inputs": ["volume"], "func": vb_161_vol_zscore_10d},
    "vb_162_vol_zscore_126d": {"inputs": ["volume"], "func": vb_162_vol_zscore_126d},
    "vb_163_vol_zscore_5d_gt2_flag": {"inputs": ["volume"], "func": vb_163_vol_zscore_5d_gt2_flag},
    "vb_164_vol_zscore_126d_gt2_flag": {"inputs": ["volume"], "func": vb_164_vol_zscore_126d_gt2_flag},
    "vb_165_vol_ratio_vs_median_21d_gt15_flag": {"inputs": ["volume"], "func": vb_165_vol_ratio_vs_median_21d_gt15_flag},
    "vb_166_vol_99th_pct_252d_norm_median": {"inputs": ["volume"], "func": vb_166_vol_99th_pct_252d_norm_median},
    "vb_167_vol_10th_pct_63d_norm_median": {"inputs": ["volume"], "func": vb_167_vol_10th_pct_63d_norm_median},
    "vb_168_spike_count_15x_median_63d": {"inputs": ["volume"], "func": vb_168_spike_count_15x_median_63d},
    "vb_169_spike_count_15x_median_252d": {"inputs": ["volume"], "func": vb_169_spike_count_15x_median_252d},
    "vb_170_spike_count_4x_median_252d": {"inputs": ["volume"], "func": vb_170_spike_count_4x_median_252d},
    "vb_171_vol_ratio_vs_mean_126d": {"inputs": ["volume"], "func": vb_171_vol_ratio_vs_mean_126d},
    "vb_172_vol_ewm_ratio_21d_vs_126d": {"inputs": ["volume"], "func": vb_172_vol_ewm_ratio_21d_vs_126d},
    "vb_173_vol_ewm_ratio_63d_vs_252d": {"inputs": ["volume"], "func": vb_173_vol_ewm_ratio_63d_vs_252d},
    "vb_174_vol_ratio_vs_median_21d_pct_rank_504d": {"inputs": ["volume"], "func": vb_174_vol_ratio_vs_median_21d_pct_rank_504d},
    "vb_175_vol_zscore_252d_pct_rank_504d": {"inputs": ["volume"], "func": vb_175_vol_zscore_252d_pct_rank_504d},
}
