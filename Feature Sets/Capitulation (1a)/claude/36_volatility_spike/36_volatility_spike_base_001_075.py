"""
36_volatility_spike — Base Features 001-075
Domain: realized volatility spikes vs trailing baseline — jumps in realized vol
        relative to trailing median/mean/z-score norms; spike counts; vol percentile
        ranks; EWMA vol surges; Parkinson/Garman-Klass range-vol spikes;
        short-window vs long-window vol ratios.
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
_ANN     = np.sqrt(_TD_YEAR)
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_ret(close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility = rolling std of log-returns * sqrt(252)."""
    return _rolling_std(_log_ret(close), w) * _ANN


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson high-low range estimator of annualized volatility."""
    hl2 = (np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2)
    pk = np.sqrt(_rolling_mean(hl2, w) / (4.0 * np.log(2.0))) * _ANN
    return pk


def _gk_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass annualized volatility estimator."""
    hl  = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    co  = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    return np.sqrt(_rolling_mean(gk_day, w) * _TD_YEAR)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Realized vol at multiple windows ---

def vsp_001_rvol_5d(close: pd.Series) -> pd.Series:
    """5-day realized volatility (annualized)."""
    return _realized_vol(close, _TD_WEEK)


def vsp_002_rvol_21d(close: pd.Series) -> pd.Series:
    """21-day realized volatility (annualized)."""
    return _realized_vol(close, _TD_MON)


def vsp_003_rvol_63d(close: pd.Series) -> pd.Series:
    """63-day realized volatility (annualized)."""
    return _realized_vol(close, _TD_QTR)


def vsp_004_rvol_126d(close: pd.Series) -> pd.Series:
    """126-day realized volatility (annualized)."""
    return _realized_vol(close, _TD_HALF)


def vsp_005_rvol_252d(close: pd.Series) -> pd.Series:
    """252-day realized volatility (annualized)."""
    return _realized_vol(close, _TD_YEAR)


def vsp_006_rvol_10d(close: pd.Series) -> pd.Series:
    """10-day realized volatility (annualized)."""
    return _realized_vol(close, 10)


def vsp_007_rvol_3d(close: pd.Series) -> pd.Series:
    """3-day realized volatility (annualized) — very short-term burst."""
    return _realized_vol(close, 3)


def vsp_008_rvol_42d(close: pd.Series) -> pd.Series:
    """42-day realized volatility (annualized) — 2-month window."""
    return _realized_vol(close, 42)


def vsp_009_rvol_5d_log(close: pd.Series) -> pd.Series:
    """Log of 5-day realized vol (linearizes heavy right tail)."""
    return np.log(vsp_001_rvol_5d(close).clip(lower=_EPS))


def vsp_010_rvol_21d_log(close: pd.Series) -> pd.Series:
    """Log of 21-day realized vol."""
    return np.log(vsp_002_rvol_21d(close).clip(lower=_EPS))


def vsp_011_rvol_63d_log(close: pd.Series) -> pd.Series:
    """Log of 63-day realized vol."""
    return np.log(vsp_003_rvol_63d(close).clip(lower=_EPS))


def vsp_012_rvol_252d_log(close: pd.Series) -> pd.Series:
    """Log of 252-day realized vol."""
    return np.log(vsp_005_rvol_252d(close).clip(lower=_EPS))


# --- Group B (013-024): Current vol vs trailing-median ratios ---

def vsp_013_rvol5_vs_median21(close: pd.Series) -> pd.Series:
    """Ratio of 5-day vol to its 21-day trailing median (spike above short norm)."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_median(v, _TD_MON))


def vsp_014_rvol5_vs_median63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day vol to its 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_015_rvol5_vs_median252(close: pd.Series) -> pd.Series:
    """Ratio of 5-day vol to its 252-day trailing median."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_016_rvol21_vs_median63(close: pd.Series) -> pd.Series:
    """Ratio of 21-day vol to its 63-day trailing median."""
    v = vsp_002_rvol_21d(close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_017_rvol21_vs_median126(close: pd.Series) -> pd.Series:
    """Ratio of 21-day vol to its 126-day trailing median."""
    v = vsp_002_rvol_21d(close)
    return _safe_div(v, _rolling_median(v, _TD_HALF))


def vsp_018_rvol21_vs_median252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day vol to its 252-day trailing median."""
    v = vsp_002_rvol_21d(close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_019_rvol63_vs_median126(close: pd.Series) -> pd.Series:
    """Ratio of 63-day vol to its 126-day trailing median."""
    v = vsp_003_rvol_63d(close)
    return _safe_div(v, _rolling_median(v, _TD_HALF))


def vsp_020_rvol63_vs_median252(close: pd.Series) -> pd.Series:
    """Ratio of 63-day vol to its 252-day trailing median."""
    v = vsp_003_rvol_63d(close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_021_rvol5_vs_mean63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day vol to its 63-day trailing mean."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_mean(v, _TD_QTR))


def vsp_022_rvol5_vs_mean252(close: pd.Series) -> pd.Series:
    """Ratio of 5-day vol to its 252-day trailing mean."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_mean(v, _TD_YEAR))


def vsp_023_rvol21_vs_mean252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day vol to its 252-day trailing mean."""
    v = vsp_002_rvol_21d(close)
    return _safe_div(v, _rolling_mean(v, _TD_YEAR))


def vsp_024_rvol63_vs_mean252(close: pd.Series) -> pd.Series:
    """Ratio of 63-day vol to its 252-day trailing mean."""
    v = vsp_003_rvol_63d(close)
    return _safe_div(v, _rolling_mean(v, _TD_YEAR))


# --- Group C (025-036): Vol z-scores vs trailing distribution ---

def vsp_025_rvol5_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day vol relative to its trailing 63-day distribution."""
    v = vsp_001_rvol_5d(close)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    return _safe_div(v - m, s)


def vsp_026_rvol5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day vol relative to its trailing 252-day distribution."""
    v = vsp_001_rvol_5d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_027_rvol21_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day vol relative to its trailing 63-day distribution."""
    v = vsp_002_rvol_21d(close)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    return _safe_div(v - m, s)


def vsp_028_rvol21_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day vol relative to its trailing 126-day distribution."""
    v = vsp_002_rvol_21d(close)
    m = _rolling_mean(v, _TD_HALF)
    s = _rolling_std(v, _TD_HALF)
    return _safe_div(v - m, s)


def vsp_029_rvol21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day vol relative to its trailing 252-day distribution."""
    v = vsp_002_rvol_21d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_030_rvol63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day vol relative to its trailing 252-day distribution."""
    v = vsp_003_rvol_63d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_031_rvol5_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day vol relative to its trailing 126-day distribution."""
    v = vsp_001_rvol_5d(close)
    m = _rolling_mean(v, _TD_HALF)
    s = _rolling_std(v, _TD_HALF)
    return _safe_div(v - m, s)


def vsp_032_rvol10_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 10-day vol relative to its trailing 252-day distribution."""
    v = vsp_006_rvol_10d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_033_rvol5_vs_median63_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the 5d/63d-median ratio itself over 252 days."""
    ratio = vsp_014_rvol5_vs_median63(close)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def vsp_034_rvol21_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day vol using expanding mean and std (all-history norm)."""
    v = vsp_002_rvol_21d(close)
    m = v.expanding(min_periods=_TD_MON).mean()
    s = v.expanding(min_periods=_TD_MON).std()
    return _safe_div(v - m, s)


def vsp_035_rvol5_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 5-day vol using expanding mean and std."""
    v = vsp_001_rvol_5d(close)
    m = v.expanding(min_periods=_TD_WEEK).mean()
    s = v.expanding(min_periods=_TD_WEEK).std()
    return _safe_div(v - m, s)


def vsp_036_rvol63_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 63-day vol using expanding mean and std."""
    v = vsp_003_rvol_63d(close)
    m = v.expanding(min_periods=_TD_QTR).mean()
    s = v.expanding(min_periods=_TD_QTR).std()
    return _safe_div(v - m, s)


# --- Group D (037-048): Vol spike counts and spike-above-threshold flags ---

def vsp_037_spike_count_gt2x_median_21d(close: pd.Series) -> pd.Series:
    """Days in trailing 21d where 5-day vol > 2x its own 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 2.0 * med).astype(float)
    return _rolling_sum(is_spike, _TD_MON)


def vsp_038_spike_count_gt2x_median_63d(close: pd.Series) -> pd.Series:
    """Days in trailing 63d where 5-day vol > 2x its 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 2.0 * med).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


def vsp_039_spike_count_gt2x_median_252d(close: pd.Series) -> pd.Series:
    """Days in trailing 252d where 5-day vol > 2x its 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 2.0 * med).astype(float)
    return _rolling_sum(is_spike, _TD_YEAR)


def vsp_040_spike_flag_gt2x_median63(close: pd.Series) -> pd.Series:
    """Binary flag: today's 5-day vol > 2x its 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    return (v > 2.0 * med).astype(float)


def vsp_041_spike_flag_gt3x_median63(close: pd.Series) -> pd.Series:
    """Binary flag: today's 5-day vol > 3x its 63-day trailing median."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    return (v > 3.0 * med).astype(float)


def vsp_042_spike_flag_gt2x_mean252(close: pd.Series) -> pd.Series:
    """Binary flag: today's 5-day vol > 2x its 252-day trailing mean."""
    v = vsp_001_rvol_5d(close)
    mn = _rolling_mean(v, _TD_YEAR)
    return (v > 2.0 * mn).astype(float)


def vsp_043_spike_count_zscore_gt2_21d(close: pd.Series) -> pd.Series:
    """Days in trailing 21d where 5-day vol z-score (252d) > 2.0."""
    z = vsp_026_rvol5_zscore_252d(close)
    return _rolling_sum((z > 2.0).astype(float), _TD_MON)


def vsp_044_spike_count_zscore_gt2_63d(close: pd.Series) -> pd.Series:
    """Days in trailing 63d where 5-day vol z-score (252d) > 2.0."""
    z = vsp_026_rvol5_zscore_252d(close)
    return _rolling_sum((z > 2.0).astype(float), _TD_QTR)


def vsp_045_spike_count_zscore_gt2_252d(close: pd.Series) -> pd.Series:
    """Days in trailing 252d where 5-day vol z-score (252d) > 2.0."""
    z = vsp_026_rvol5_zscore_252d(close)
    return _rolling_sum((z > 2.0).astype(float), _TD_YEAR)


def vsp_046_spike_freq_21d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days that are vol spikes (>2x 63d median)."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 2.0 * med).astype(float)
    return _rolling_mean(is_spike, _TD_MON)


def vsp_047_spike_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that are vol spikes (>2x 63d median)."""
    v = vsp_001_rvol_5d(close)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 2.0 * med).astype(float)
    return _rolling_mean(is_spike, _TD_QTR)


def vsp_048_spike_flag_gt15pct_abs(close: pd.Series) -> pd.Series:
    """Binary flag: 5-day annualized vol > 0.15 absolute threshold."""
    return (vsp_001_rvol_5d(close) > 0.15).astype(float)


# --- Group E (049-060): Trailing maximum vol and percentile ranks ---

def vsp_049_rvol5_max_21d(close: pd.Series) -> pd.Series:
    """Largest 5-day realized vol seen in trailing 21 days."""
    return _rolling_max(vsp_001_rvol_5d(close), _TD_MON)


def vsp_050_rvol5_max_63d(close: pd.Series) -> pd.Series:
    """Largest 5-day realized vol seen in trailing 63 days."""
    return _rolling_max(vsp_001_rvol_5d(close), _TD_QTR)


def vsp_051_rvol5_max_252d(close: pd.Series) -> pd.Series:
    """Largest 5-day realized vol seen in trailing 252 days."""
    return _rolling_max(vsp_001_rvol_5d(close), _TD_YEAR)


def vsp_052_rvol21_max_252d(close: pd.Series) -> pd.Series:
    """Largest 21-day realized vol seen in trailing 252 days."""
    return _rolling_max(vsp_002_rvol_21d(close), _TD_YEAR)


def vsp_053_rvol5_vs_max_63d(close: pd.Series) -> pd.Series:
    """Current 5-day vol as fraction of its 63-day rolling maximum."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_max(v, _TD_QTR))


def vsp_054_rvol5_vs_max_252d(close: pd.Series) -> pd.Series:
    """Current 5-day vol as fraction of its 252-day rolling maximum."""
    v = vsp_001_rvol_5d(close)
    return _safe_div(v, _rolling_max(v, _TD_YEAR))


def vsp_055_rvol21_vs_max_252d(close: pd.Series) -> pd.Series:
    """Current 21-day vol as fraction of its 252-day rolling maximum."""
    v = vsp_002_rvol_21d(close)
    return _safe_div(v, _rolling_max(v, _TD_YEAR))


def vsp_056_rvol5_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day vol within trailing 63-day series."""
    v = vsp_001_rvol_5d(close)
    return v.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def vsp_057_rvol5_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day vol within trailing 126-day series."""
    v = vsp_001_rvol_5d(close)
    return v.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def vsp_058_rvol5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day vol within trailing 252-day series."""
    v = vsp_001_rvol_5d(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_059_rvol21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21-day vol within trailing 252-day series."""
    v = vsp_002_rvol_21d(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_060_rvol5_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 5-day vol (all-history)."""
    v = vsp_001_rvol_5d(close)
    return v.expanding(min_periods=_TD_MON).rank(pct=True)


# --- Group F (061-070): EWMA vol surges ---

def vsp_061_ewma_vol_5d(close: pd.Series) -> pd.Series:
    """EWMA (span=5) of daily absolute log-returns (EWMA vol proxy)."""
    lr = _log_ret(close).abs()
    return _ewm_mean(lr, _TD_WEEK) * _ANN


def vsp_062_ewma_vol_21d(close: pd.Series) -> pd.Series:
    """EWMA (span=21) of daily absolute log-returns (EWMA vol proxy)."""
    lr = _log_ret(close).abs()
    return _ewm_mean(lr, _TD_MON) * _ANN


def vsp_063_ewma_vol_63d(close: pd.Series) -> pd.Series:
    """EWMA (span=63) of daily absolute log-returns (EWMA vol proxy)."""
    lr = _log_ret(close).abs()
    return _ewm_mean(lr, _TD_QTR) * _ANN


def vsp_064_ewma_vol5_vs_ewma_vol63(close: pd.Series) -> pd.Series:
    """Ratio of EWMA-5 vol to EWMA-63 vol (surge detection)."""
    return _safe_div(vsp_061_ewma_vol_5d(close), vsp_063_ewma_vol_63d(close))


def vsp_065_ewma_vol5_vs_ewma_vol21(close: pd.Series) -> pd.Series:
    """Ratio of EWMA-5 vol to EWMA-21 vol (very short-term vs monthly surge)."""
    return _safe_div(vsp_061_ewma_vol_5d(close), vsp_062_ewma_vol_21d(close))


def vsp_066_ewma_vol_std_surge_63d(close: pd.Series) -> pd.Series:
    """EWMA-5 vol minus 63-day rolling mean of EWMA-63 vol (raw surge level)."""
    e5 = vsp_061_ewma_vol_5d(close)
    e63 = vsp_063_ewma_vol_63d(close)
    return e5 - _rolling_mean(e63, _TD_QTR)


def vsp_067_ewma_vol21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWMA-21 vol relative to its 252-day rolling distribution."""
    v = vsp_062_ewma_vol_21d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_068_ewma_vol5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EWMA-5 vol within trailing 252-day series."""
    v = vsp_061_ewma_vol_5d(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_069_ewma_vol_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWMA-5/EWMA-63 vol ratio over 252 days."""
    ratio = vsp_064_ewma_vol5_vs_ewma_vol63(close)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def vsp_070_ewma_vol5_vs_median_252d(close: pd.Series) -> pd.Series:
    """EWMA-5 vol divided by its 252-day trailing median."""
    v = vsp_061_ewma_vol_5d(close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


# --- Group G (071-075): Short-window vs long-window vol ratios ---

def vsp_071_rvol5_vs_rvol63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 63-day realized vol."""
    return _safe_div(vsp_001_rvol_5d(close), vsp_003_rvol_63d(close))


def vsp_072_rvol5_vs_rvol252(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 252-day realized vol."""
    return _safe_div(vsp_001_rvol_5d(close), vsp_005_rvol_252d(close))


def vsp_073_rvol21_vs_rvol252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day realized vol to 252-day realized vol."""
    return _safe_div(vsp_002_rvol_21d(close), vsp_005_rvol_252d(close))


def vsp_074_rvol5_vs_rvol126(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 126-day realized vol."""
    return _safe_div(vsp_001_rvol_5d(close), vsp_004_rvol_126d(close))


def vsp_075_rvol10_vs_rvol252(close: pd.Series) -> pd.Series:
    """Ratio of 10-day realized vol to 252-day realized vol."""
    return _safe_div(vsp_006_rvol_10d(close), vsp_005_rvol_252d(close))


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_REGISTRY_001_075 = {
    "vsp_001_rvol_5d": {"inputs": ["close"], "func": vsp_001_rvol_5d},
    "vsp_002_rvol_21d": {"inputs": ["close"], "func": vsp_002_rvol_21d},
    "vsp_003_rvol_63d": {"inputs": ["close"], "func": vsp_003_rvol_63d},
    "vsp_004_rvol_126d": {"inputs": ["close"], "func": vsp_004_rvol_126d},
    "vsp_005_rvol_252d": {"inputs": ["close"], "func": vsp_005_rvol_252d},
    "vsp_006_rvol_10d": {"inputs": ["close"], "func": vsp_006_rvol_10d},
    "vsp_007_rvol_3d": {"inputs": ["close"], "func": vsp_007_rvol_3d},
    "vsp_008_rvol_42d": {"inputs": ["close"], "func": vsp_008_rvol_42d},
    "vsp_009_rvol_5d_log": {"inputs": ["close"], "func": vsp_009_rvol_5d_log},
    "vsp_010_rvol_21d_log": {"inputs": ["close"], "func": vsp_010_rvol_21d_log},
    "vsp_011_rvol_63d_log": {"inputs": ["close"], "func": vsp_011_rvol_63d_log},
    "vsp_012_rvol_252d_log": {"inputs": ["close"], "func": vsp_012_rvol_252d_log},
    "vsp_013_rvol5_vs_median21": {"inputs": ["close"], "func": vsp_013_rvol5_vs_median21},
    "vsp_014_rvol5_vs_median63": {"inputs": ["close"], "func": vsp_014_rvol5_vs_median63},
    "vsp_015_rvol5_vs_median252": {"inputs": ["close"], "func": vsp_015_rvol5_vs_median252},
    "vsp_016_rvol21_vs_median63": {"inputs": ["close"], "func": vsp_016_rvol21_vs_median63},
    "vsp_017_rvol21_vs_median126": {"inputs": ["close"], "func": vsp_017_rvol21_vs_median126},
    "vsp_018_rvol21_vs_median252": {"inputs": ["close"], "func": vsp_018_rvol21_vs_median252},
    "vsp_019_rvol63_vs_median126": {"inputs": ["close"], "func": vsp_019_rvol63_vs_median126},
    "vsp_020_rvol63_vs_median252": {"inputs": ["close"], "func": vsp_020_rvol63_vs_median252},
    "vsp_021_rvol5_vs_mean63": {"inputs": ["close"], "func": vsp_021_rvol5_vs_mean63},
    "vsp_022_rvol5_vs_mean252": {"inputs": ["close"], "func": vsp_022_rvol5_vs_mean252},
    "vsp_023_rvol21_vs_mean252": {"inputs": ["close"], "func": vsp_023_rvol21_vs_mean252},
    "vsp_024_rvol63_vs_mean252": {"inputs": ["close"], "func": vsp_024_rvol63_vs_mean252},
    "vsp_025_rvol5_zscore_63d": {"inputs": ["close"], "func": vsp_025_rvol5_zscore_63d},
    "vsp_026_rvol5_zscore_252d": {"inputs": ["close"], "func": vsp_026_rvol5_zscore_252d},
    "vsp_027_rvol21_zscore_63d": {"inputs": ["close"], "func": vsp_027_rvol21_zscore_63d},
    "vsp_028_rvol21_zscore_126d": {"inputs": ["close"], "func": vsp_028_rvol21_zscore_126d},
    "vsp_029_rvol21_zscore_252d": {"inputs": ["close"], "func": vsp_029_rvol21_zscore_252d},
    "vsp_030_rvol63_zscore_252d": {"inputs": ["close"], "func": vsp_030_rvol63_zscore_252d},
    "vsp_031_rvol5_zscore_126d": {"inputs": ["close"], "func": vsp_031_rvol5_zscore_126d},
    "vsp_032_rvol10_zscore_252d": {"inputs": ["close"], "func": vsp_032_rvol10_zscore_252d},
    "vsp_033_rvol5_vs_median63_zscore": {"inputs": ["close"], "func": vsp_033_rvol5_vs_median63_zscore},
    "vsp_034_rvol21_expanding_zscore": {"inputs": ["close"], "func": vsp_034_rvol21_expanding_zscore},
    "vsp_035_rvol5_expanding_zscore": {"inputs": ["close"], "func": vsp_035_rvol5_expanding_zscore},
    "vsp_036_rvol63_expanding_zscore": {"inputs": ["close"], "func": vsp_036_rvol63_expanding_zscore},
    "vsp_037_spike_count_gt2x_median_21d": {"inputs": ["close"], "func": vsp_037_spike_count_gt2x_median_21d},
    "vsp_038_spike_count_gt2x_median_63d": {"inputs": ["close"], "func": vsp_038_spike_count_gt2x_median_63d},
    "vsp_039_spike_count_gt2x_median_252d": {"inputs": ["close"], "func": vsp_039_spike_count_gt2x_median_252d},
    "vsp_040_spike_flag_gt2x_median63": {"inputs": ["close"], "func": vsp_040_spike_flag_gt2x_median63},
    "vsp_041_spike_flag_gt3x_median63": {"inputs": ["close"], "func": vsp_041_spike_flag_gt3x_median63},
    "vsp_042_spike_flag_gt2x_mean252": {"inputs": ["close"], "func": vsp_042_spike_flag_gt2x_mean252},
    "vsp_043_spike_count_zscore_gt2_21d": {"inputs": ["close"], "func": vsp_043_spike_count_zscore_gt2_21d},
    "vsp_044_spike_count_zscore_gt2_63d": {"inputs": ["close"], "func": vsp_044_spike_count_zscore_gt2_63d},
    "vsp_045_spike_count_zscore_gt2_252d": {"inputs": ["close"], "func": vsp_045_spike_count_zscore_gt2_252d},
    "vsp_046_spike_freq_21d": {"inputs": ["close"], "func": vsp_046_spike_freq_21d},
    "vsp_047_spike_freq_63d": {"inputs": ["close"], "func": vsp_047_spike_freq_63d},
    "vsp_048_spike_flag_gt15pct_abs": {"inputs": ["close"], "func": vsp_048_spike_flag_gt15pct_abs},
    "vsp_049_rvol5_max_21d": {"inputs": ["close"], "func": vsp_049_rvol5_max_21d},
    "vsp_050_rvol5_max_63d": {"inputs": ["close"], "func": vsp_050_rvol5_max_63d},
    "vsp_051_rvol5_max_252d": {"inputs": ["close"], "func": vsp_051_rvol5_max_252d},
    "vsp_052_rvol21_max_252d": {"inputs": ["close"], "func": vsp_052_rvol21_max_252d},
    "vsp_053_rvol5_vs_max_63d": {"inputs": ["close"], "func": vsp_053_rvol5_vs_max_63d},
    "vsp_054_rvol5_vs_max_252d": {"inputs": ["close"], "func": vsp_054_rvol5_vs_max_252d},
    "vsp_055_rvol21_vs_max_252d": {"inputs": ["close"], "func": vsp_055_rvol21_vs_max_252d},
    "vsp_056_rvol5_pct_rank_63d": {"inputs": ["close"], "func": vsp_056_rvol5_pct_rank_63d},
    "vsp_057_rvol5_pct_rank_126d": {"inputs": ["close"], "func": vsp_057_rvol5_pct_rank_126d},
    "vsp_058_rvol5_pct_rank_252d": {"inputs": ["close"], "func": vsp_058_rvol5_pct_rank_252d},
    "vsp_059_rvol21_pct_rank_252d": {"inputs": ["close"], "func": vsp_059_rvol21_pct_rank_252d},
    "vsp_060_rvol5_expanding_pct_rank": {"inputs": ["close"], "func": vsp_060_rvol5_expanding_pct_rank},
    "vsp_061_ewma_vol_5d": {"inputs": ["close"], "func": vsp_061_ewma_vol_5d},
    "vsp_062_ewma_vol_21d": {"inputs": ["close"], "func": vsp_062_ewma_vol_21d},
    "vsp_063_ewma_vol_63d": {"inputs": ["close"], "func": vsp_063_ewma_vol_63d},
    "vsp_064_ewma_vol5_vs_ewma_vol63": {"inputs": ["close"], "func": vsp_064_ewma_vol5_vs_ewma_vol63},
    "vsp_065_ewma_vol5_vs_ewma_vol21": {"inputs": ["close"], "func": vsp_065_ewma_vol5_vs_ewma_vol21},
    "vsp_066_ewma_vol_std_surge_63d": {"inputs": ["close"], "func": vsp_066_ewma_vol_std_surge_63d},
    "vsp_067_ewma_vol21_zscore_252d": {"inputs": ["close"], "func": vsp_067_ewma_vol21_zscore_252d},
    "vsp_068_ewma_vol5_pct_rank_252d": {"inputs": ["close"], "func": vsp_068_ewma_vol5_pct_rank_252d},
    "vsp_069_ewma_vol_ratio_zscore_252d": {"inputs": ["close"], "func": vsp_069_ewma_vol_ratio_zscore_252d},
    "vsp_070_ewma_vol5_vs_median_252d": {"inputs": ["close"], "func": vsp_070_ewma_vol5_vs_median_252d},
    "vsp_071_rvol5_vs_rvol63": {"inputs": ["close"], "func": vsp_071_rvol5_vs_rvol63},
    "vsp_072_rvol5_vs_rvol252": {"inputs": ["close"], "func": vsp_072_rvol5_vs_rvol252},
    "vsp_073_rvol21_vs_rvol252": {"inputs": ["close"], "func": vsp_073_rvol21_vs_rvol252},
    "vsp_074_rvol5_vs_rvol126": {"inputs": ["close"], "func": vsp_074_rvol5_vs_rvol126},
    "vsp_075_rvol10_vs_rvol252": {"inputs": ["close"], "func": vsp_075_rvol10_vs_rvol252},
}
