"""
18_volume_dryup — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume dry-up features — velocity of dryup deepening
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vdry_drv2_001_vol_ratio_21d_mean_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/21d-mean ratio (velocity of dryup relative to mean)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_002_vol_ratio_63d_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/63d-mean ratio (monthly velocity of medium-term dryup)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vdry_drv2_003_vol_zscore_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume z-score (quickening of dryup signal)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def vdry_drv2_004_vol_zscore_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume z-score."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_MON)


def vdry_drv2_005_consec_below_mean_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive-below-21d-mean streak length."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def vdry_drv2_006_consec_vol_declining_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive declining-volume streak."""
    cond = volume < volume.shift(1)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def vdry_drv2_007_vol_decay_from_63d_max_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/63d-max ratio (velocity of post-spike collapse)."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_008_vol_decay_from_63d_max_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/63d-max decay ratio over trailing 21 days."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    return _linslope(ratio, _TD_MON)


def vdry_drv2_009_frac_below_mean_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of fraction-of-21d-days-below-mean (velocity of breadth dryup)."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vdry_drv2_010_frac_below_mean_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of fraction of 63d below 63d-mean."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vdry_drv2_011_vol_21d_mean_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean volume (trend in the baseline itself)."""
    m21 = _rolling_mean(volume, _TD_MON)
    return m21.diff(_TD_WEEK)


def vdry_drv2_012_vol_63d_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day mean volume."""
    m63 = _rolling_mean(volume, _TD_QTR)
    return m63.diff(_TD_MON)


def vdry_drv2_013_vol_pct_rank_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol percentile rank in 63-day window."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vdry_drv2_014_vol_pct_rank_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol percentile rank in 252-day window."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def vdry_drv2_015_dollar_vol_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of dollar-volume / 63d-mean-dollar-volume ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_016_vol_82d_vs_252d_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d-mean/252d-mean volume ratio (short vs. long collapse velocity)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_017_vol_dryup_intensity_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day dryup-intensity (shortfall depth velocity)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    return intensity.diff(_TD_WEEK)


def vdry_drv2_018_vol_dryup_intensity_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day dryup-intensity."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_QTR)
    return intensity.diff(_TD_MON)


def vdry_drv2_019_vol_log_ratio_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of log(vol/63d-mean) over trailing 21 days."""
    log_ratio = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_QTR))
    return _linslope(log_ratio, _TD_MON)


def vdry_drv2_020_low_vol_down_day_count_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of low-vol down days in 21-day window."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    count = _rolling_count_true(cond, _TD_MON)
    return count.diff(_TD_WEEK)


def vdry_drv2_021_vol_21d_vs_252d_ratio_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21d/252d-mean vol ratio over trailing 21 days."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    return _linslope(ratio, _TD_MON)


def vdry_drv2_022_vol_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day volume z-score (long-horizon dryup velocity)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def vdry_drv2_023_consec_below_median_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive-below-63d-median streak."""
    cond = volume < _rolling_median(volume, _TD_QTR)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def vdry_drv2_024_seller_exhaustion_score_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of seller exhaustion score (low-vol down-day depth, 21d)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    depth = (1.0 - _safe_div(volume, mean21)).clip(lower=0.0)
    score = _rolling_sum(low_vol_down * depth, _TD_MON)
    return score.diff(_TD_WEEK)


def vdry_drv2_025_vol_dryup_composite_zscore_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of composite vol z-score (avg of 21d, 63d, 252d z-scores)."""
    z21 = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    z63 = _safe_div(volume - _rolling_mean(volume, _TD_QTR), _rolling_std(volume, _TD_QTR))
    z252 = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    composite = (z21 + z63 + z252) / 3.0
    return composite.diff(_TD_MON)


# --- drv2 026-035: Rate-of-change of EMA-based and log-ratio features ---

def vdry_drv2_026_vol_ratio_5d_ema_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/5d-EMA ratio (velocity of ultra-short dryup)."""
    ratio = _safe_div(volume, _ewm_mean(volume, _TD_WEEK))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_027_vol_ratio_126d_ema_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/126d-EMA ratio (velocity of semi-annual EMA dryup)."""
    ratio = _safe_div(volume, _ewm_mean(volume, _TD_HALF))
    return ratio.diff(_TD_MON)


def vdry_drv2_028_log_vol_ratio_21d_ema_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(vol/21d-EMA) (velocity of log dryup vs. EMA baseline)."""
    lr = _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_MON))
    return lr.diff(_TD_WEEK)


def vdry_drv2_029_vol_5d_ema_vs_63d_ema_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5d-EMA/63d-EMA ratio (short vs. medium EMA spread velocity)."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_030_vol_21d_ema_vs_252d_ema_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d-EMA/252d-EMA ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vdry_drv2_031_log_vol_ratio_21d_mean_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of log(vol/21d-mean) over trailing 21 days."""
    lr = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_MON))
    return _linslope(lr, _TD_MON)


def vdry_drv2_032_log_vol_ratio_252d_mean_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(vol/252d-mean) (velocity of long-horizon log dryup)."""
    lr = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_YEAR))
    return lr.diff(_TD_WEEK)


def vdry_drv2_033_vol_zscore_5d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day volume z-score (ultra-short dryup velocity)."""
    m = _rolling_mean(volume, _TD_WEEK)
    s = _rolling_std(volume, _TD_WEEK)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def vdry_drv2_034_vol_zscore_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume z-score."""
    m = _rolling_mean(volume, _TD_HALF)
    s = _rolling_std(volume, _TD_HALF)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_MON)


def vdry_drv2_035_vol_below_p10_252d_flag_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of binary flag: vol < 10th-pctile of 252-day dist."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    flag = (volume < p10).astype(float)
    return flag.diff(_TD_MON)


# --- drv2 036-045: Rate-of-change of decay-from-max, count, and rank features ---

def vdry_drv2_036_vol_decay_from_21d_max_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/21d-max ratio (velocity of short post-peak decay)."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_MON))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_037_vol_decay_from_252d_max_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/252d-max ratio (monthly velocity of long-run decay)."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_YEAR))
    return ratio.diff(_TD_MON)


def vdry_drv2_038_vol_max_to_min_ratio_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day vol max/min ratio (spread velocity)."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_min(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_039_count_below_mean_252d_in_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of count of days < 252d-mean over trailing 252 days."""
    cond = volume < _rolling_mean(volume, _TD_YEAR)
    count = _rolling_count_true(cond, _TD_YEAR)
    return count.diff(_TD_MON)


def vdry_drv2_040_vol_pct_rank_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol percentile rank in 21-day window."""
    rank = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vdry_drv2_041_vol_pct_rank_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol percentile rank in 126-day window."""
    rank = volume.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def vdry_drv2_042_vol_126d_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day mean volume (semi-annual baseline trend velocity)."""
    m126 = _rolling_mean(volume, _TD_HALF)
    return m126.diff(_TD_MON)


def vdry_drv2_043_vol_252d_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day mean volume (annual baseline trend velocity)."""
    m252 = _rolling_mean(volume, _TD_YEAR)
    return m252.diff(_TD_MON)


def vdry_drv2_044_vol_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation (variability trend velocity)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vdry_drv2_045_vol_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return cv.diff(_TD_MON)


# --- drv2 046-055: Rate-of-change of dollar-volume and range-volume features ---

def vdry_drv2_046_dollar_vol_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of dollar-volume / 21d-mean-dollar-volume ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_047_dollar_vol_ratio_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of dollar-volume / 252d-mean-dollar-volume ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vdry_drv2_048_dollar_vol_zscore_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of dollar-volume 63-day z-score."""
    dv = close * volume
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_WEEK)


def vdry_drv2_049_range_vol_ratio_63d_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (high-low)*volume / 63d-mean-range-volume ratio."""
    rv = (high - low) * volume
    ratio = _safe_div(rv, _rolling_mean(rv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_050_range_vol_zscore_63d_21d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of (high-low)*volume 63-day z-score."""
    rv = (high - low) * volume
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    z = _safe_div(rv - m, s)
    return z.diff(_TD_MON)


def vdry_drv2_051_body_vol_ratio_21d_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of abs(close-open)*volume / 21d-mean-body-volume ratio."""
    bv = (close - open).abs() * volume
    ratio = _safe_div(bv, _rolling_mean(bv, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_052_body_vol_zscore_63d_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of abs(close-open)*volume 63-day z-score."""
    bv = (close - open).abs() * volume
    m = _rolling_mean(bv, _TD_QTR)
    s = _rolling_std(bv, _TD_QTR)
    z = _safe_div(bv - m, s)
    return z.diff(_TD_WEEK)


def vdry_drv2_053_vol_contraction_5d_vs_63d_max_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5d-mean/63d-max ratio (velocity of post-spike short-term decay)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume.shift(1), _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vdry_drv2_054_vol_contraction_21d_vs_252d_max_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d-mean/252d-max ratio (monthly velocity of long decay)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_max(volume.shift(1), _TD_YEAR))
    return ratio.diff(_TD_MON)


def vdry_drv2_055_vol_dryup_intensity_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day dryup intensity (annual shortfall depth velocity)."""
    m252 = _rolling_mean(volume, _TD_YEAR)
    shortfall = (1.0 - _safe_div(volume, m252)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_YEAR)
    return intensity.diff(_TD_MON)


# --- drv2 056-065: Slope-based 2nd derivatives (OLS over varying windows) ---

def vdry_drv2_056_vol_ratio_21d_mean_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/21d-mean ratio over trailing 63 days."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _linslope(ratio, _TD_QTR)


def vdry_drv2_057_vol_zscore_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day vol z-score over trailing 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    return _linslope(z, _TD_QTR)


def vdry_drv2_058_vol_zscore_252d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252-day vol z-score over trailing 63 days."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    return _linslope(z, _TD_QTR)


def vdry_drv2_059_vol_pct_rank_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day vol percentile rank over trailing 21 days."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return _linslope(rank, _TD_MON)


def vdry_drv2_060_vol_pct_rank_252d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252-day vol percentile rank over trailing 63 days."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_QTR)


def vdry_drv2_061_vol_dryup_intensity_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day dryup intensity over trailing 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_QTR)
    return _linslope(intensity, _TD_QTR)


def vdry_drv2_062_dollar_vol_ratio_63d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar-volume/63d-mean ratio over trailing 21 days."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    return _linslope(ratio, _TD_MON)


def vdry_drv2_063_vol_decay_from_63d_max_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/63d-max ratio over trailing 63 days."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    return _linslope(ratio, _TD_QTR)


def vdry_drv2_064_vol_21d_mean_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day mean volume over trailing 63 days."""
    m21 = _rolling_mean(volume, _TD_MON)
    return _linslope(m21, _TD_QTR)


def vdry_drv2_065_vol_63d_mean_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day mean volume over trailing 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    return _linslope(m63, _TD_QTR)


# --- drv2 066-075: Mixed-window diffs and price-context velocity features ---

def vdry_drv2_066_vol_ratio_21d_mean_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of vol/21d-mean ratio (quarterly velocity of dryup)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_QTR)


def vdry_drv2_067_vol_dryup_intensity_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day dryup intensity (monthly velocity of shortfall depth)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    return intensity.diff(_TD_MON)


def vdry_drv2_068_vol_breadth_dryup_score_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of fraction: last 21d both below 63d-mean AND below prior-day vol."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (volume < mean63) & (volume < volume.shift(1))
    score = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return score.diff(_TD_WEEK)


def vdry_drv2_069_vol_ratio_on_down_vs_up_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of avg-vol-down-days/avg-vol-up-days ratio over 21 days."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_WEEK)


def vdry_drv2_070_seller_exhaustion_score_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of seller exhaustion score."""
    mean21 = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    depth = (1.0 - _safe_div(volume, mean21)).clip(lower=0.0)
    score = _rolling_sum(low_vol_down * depth, _TD_MON)
    return score.diff(_TD_MON)


def vdry_drv2_071_low_vol_on_down_close_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of low-vol down-close days in 63-day window."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    count = _rolling_count_true(cond, _TD_QTR)
    return count.diff(_TD_WEEK)


def vdry_drv2_072_vol_dryup_distress_index_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of vol dryup distress index (streak * depth * down-frac)."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = volume < mean63
    streak = _consec_streak(cond)
    depth = (1.0 - _safe_div(volume, mean63)).clip(lower=0.0)
    ret = close.pct_change(1)
    dn_frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    index = streak * depth * dn_frac
    return index.diff(_TD_WEEK)


def vdry_drv2_073_vol_log_ratio_63d_ema_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(vol/63d-EMA) (EMA-anchored log dryup velocity)."""
    lr = _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_QTR))
    return lr.diff(_TD_WEEK)


def vdry_drv2_074_vol_zscore_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day vol z-score over trailing 63 days."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return _linslope(z, _TD_QTR)


def vdry_drv2_075_vol_dryup_breadth_score_multi_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of multi-window below-mean flag count (5d/21d/63d/252d means)."""
    f1 = (volume < _rolling_mean(volume, _TD_WEEK)).astype(float)
    f2 = (volume < _rolling_mean(volume, _TD_MON)).astype(float)
    f3 = (volume < _rolling_mean(volume, _TD_QTR)).astype(float)
    f4 = (volume < _rolling_mean(volume, _TD_YEAR)).astype(float)
    score = f1 + f2 + f3 + f4
    return score.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DRYUP_REGISTRY_2ND_DERIVATIVES = {
    "vdry_drv2_001_vol_ratio_21d_mean_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_001_vol_ratio_21d_mean_5d_diff},
    "vdry_drv2_002_vol_ratio_63d_mean_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_002_vol_ratio_63d_mean_21d_diff},
    "vdry_drv2_003_vol_zscore_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_003_vol_zscore_21d_5d_diff},
    "vdry_drv2_004_vol_zscore_63d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_004_vol_zscore_63d_21d_diff},
    "vdry_drv2_005_consec_below_mean_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_005_consec_below_mean_21d_5d_diff},
    "vdry_drv2_006_consec_vol_declining_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_006_consec_vol_declining_5d_diff},
    "vdry_drv2_007_vol_decay_from_63d_max_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_007_vol_decay_from_63d_max_5d_diff},
    "vdry_drv2_008_vol_decay_from_63d_max_slope_21d": {"inputs": ["volume"], "func": vdry_drv2_008_vol_decay_from_63d_max_slope_21d},
    "vdry_drv2_009_frac_below_mean_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_009_frac_below_mean_21d_5d_diff},
    "vdry_drv2_010_frac_below_mean_63d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_010_frac_below_mean_63d_21d_diff},
    "vdry_drv2_011_vol_21d_mean_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_011_vol_21d_mean_5d_diff},
    "vdry_drv2_012_vol_63d_mean_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_012_vol_63d_mean_21d_diff},
    "vdry_drv2_013_vol_pct_rank_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_013_vol_pct_rank_63d_5d_diff},
    "vdry_drv2_014_vol_pct_rank_252d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_014_vol_pct_rank_252d_21d_diff},
    "vdry_drv2_015_dollar_vol_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_015_dollar_vol_ratio_63d_5d_diff},
    "vdry_drv2_016_vol_82d_vs_252d_ratio_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_016_vol_82d_vs_252d_ratio_5d_diff},
    "vdry_drv2_017_vol_dryup_intensity_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_017_vol_dryup_intensity_21d_5d_diff},
    "vdry_drv2_018_vol_dryup_intensity_63d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_018_vol_dryup_intensity_63d_21d_diff},
    "vdry_drv2_019_vol_log_ratio_63d_slope_21d": {"inputs": ["volume"], "func": vdry_drv2_019_vol_log_ratio_63d_slope_21d},
    "vdry_drv2_020_low_vol_down_day_count_21d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_020_low_vol_down_day_count_21d_5d_diff},
    "vdry_drv2_021_vol_21d_vs_252d_ratio_slope_21d": {"inputs": ["volume"], "func": vdry_drv2_021_vol_21d_vs_252d_ratio_slope_21d},
    "vdry_drv2_022_vol_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_022_vol_zscore_252d_5d_diff},
    "vdry_drv2_023_consec_below_median_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_023_consec_below_median_63d_5d_diff},
    "vdry_drv2_024_seller_exhaustion_score_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_024_seller_exhaustion_score_5d_diff},
    "vdry_drv2_025_vol_dryup_composite_zscore_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_025_vol_dryup_composite_zscore_21d_diff},
    "vdry_drv2_026_vol_ratio_5d_ema_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_026_vol_ratio_5d_ema_5d_diff},
    "vdry_drv2_027_vol_ratio_126d_ema_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_027_vol_ratio_126d_ema_21d_diff},
    "vdry_drv2_028_log_vol_ratio_21d_ema_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_028_log_vol_ratio_21d_ema_5d_diff},
    "vdry_drv2_029_vol_5d_ema_vs_63d_ema_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_029_vol_5d_ema_vs_63d_ema_5d_diff},
    "vdry_drv2_030_vol_21d_ema_vs_252d_ema_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_030_vol_21d_ema_vs_252d_ema_21d_diff},
    "vdry_drv2_031_log_vol_ratio_21d_mean_slope_21d": {"inputs": ["volume"], "func": vdry_drv2_031_log_vol_ratio_21d_mean_slope_21d},
    "vdry_drv2_032_log_vol_ratio_252d_mean_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_032_log_vol_ratio_252d_mean_5d_diff},
    "vdry_drv2_033_vol_zscore_5d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_033_vol_zscore_5d_5d_diff},
    "vdry_drv2_034_vol_zscore_126d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_034_vol_zscore_126d_21d_diff},
    "vdry_drv2_035_vol_below_p10_252d_flag_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_035_vol_below_p10_252d_flag_21d_diff},
    "vdry_drv2_036_vol_decay_from_21d_max_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_036_vol_decay_from_21d_max_5d_diff},
    "vdry_drv2_037_vol_decay_from_252d_max_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_037_vol_decay_from_252d_max_21d_diff},
    "vdry_drv2_038_vol_max_to_min_ratio_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_038_vol_max_to_min_ratio_63d_5d_diff},
    "vdry_drv2_039_count_below_mean_252d_in_252d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_039_count_below_mean_252d_in_252d_21d_diff},
    "vdry_drv2_040_vol_pct_rank_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_040_vol_pct_rank_21d_5d_diff},
    "vdry_drv2_041_vol_pct_rank_126d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_041_vol_pct_rank_126d_21d_diff},
    "vdry_drv2_042_vol_126d_mean_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_042_vol_126d_mean_21d_diff},
    "vdry_drv2_043_vol_252d_mean_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_043_vol_252d_mean_21d_diff},
    "vdry_drv2_044_vol_cv_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_044_vol_cv_21d_5d_diff},
    "vdry_drv2_045_vol_cv_63d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_045_vol_cv_63d_21d_diff},
    "vdry_drv2_046_dollar_vol_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_046_dollar_vol_ratio_21d_5d_diff},
    "vdry_drv2_047_dollar_vol_ratio_252d_21d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_047_dollar_vol_ratio_252d_21d_diff},
    "vdry_drv2_048_dollar_vol_zscore_63d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_048_dollar_vol_zscore_63d_5d_diff},
    "vdry_drv2_049_range_vol_ratio_63d_5d_diff": {"inputs": ["high", "low", "volume"], "func": vdry_drv2_049_range_vol_ratio_63d_5d_diff},
    "vdry_drv2_050_range_vol_zscore_63d_21d_diff": {"inputs": ["high", "low", "volume"], "func": vdry_drv2_050_range_vol_zscore_63d_21d_diff},
    "vdry_drv2_051_body_vol_ratio_21d_5d_diff": {"inputs": ["close", "open", "volume"], "func": vdry_drv2_051_body_vol_ratio_21d_5d_diff},
    "vdry_drv2_052_body_vol_zscore_63d_5d_diff": {"inputs": ["close", "open", "volume"], "func": vdry_drv2_052_body_vol_zscore_63d_5d_diff},
    "vdry_drv2_053_vol_contraction_5d_vs_63d_max_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_053_vol_contraction_5d_vs_63d_max_5d_diff},
    "vdry_drv2_054_vol_contraction_21d_vs_252d_max_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_054_vol_contraction_21d_vs_252d_max_21d_diff},
    "vdry_drv2_055_vol_dryup_intensity_252d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_055_vol_dryup_intensity_252d_21d_diff},
    "vdry_drv2_056_vol_ratio_21d_mean_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_056_vol_ratio_21d_mean_slope_63d},
    "vdry_drv2_057_vol_zscore_63d_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_057_vol_zscore_63d_slope_63d},
    "vdry_drv2_058_vol_zscore_252d_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_058_vol_zscore_252d_slope_63d},
    "vdry_drv2_059_vol_pct_rank_63d_slope_21d": {"inputs": ["volume"], "func": vdry_drv2_059_vol_pct_rank_63d_slope_21d},
    "vdry_drv2_060_vol_pct_rank_252d_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_060_vol_pct_rank_252d_slope_63d},
    "vdry_drv2_061_vol_dryup_intensity_63d_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_061_vol_dryup_intensity_63d_slope_63d},
    "vdry_drv2_062_dollar_vol_ratio_63d_slope_21d": {"inputs": ["close", "volume"], "func": vdry_drv2_062_dollar_vol_ratio_63d_slope_21d},
    "vdry_drv2_063_vol_decay_from_63d_max_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_063_vol_decay_from_63d_max_slope_63d},
    "vdry_drv2_064_vol_21d_mean_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_064_vol_21d_mean_slope_63d},
    "vdry_drv2_065_vol_63d_mean_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_065_vol_63d_mean_slope_63d},
    "vdry_drv2_066_vol_ratio_21d_mean_63d_diff": {"inputs": ["volume"], "func": vdry_drv2_066_vol_ratio_21d_mean_63d_diff},
    "vdry_drv2_067_vol_dryup_intensity_21d_21d_diff": {"inputs": ["volume"], "func": vdry_drv2_067_vol_dryup_intensity_21d_21d_diff},
    "vdry_drv2_068_vol_breadth_dryup_score_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_068_vol_breadth_dryup_score_21d_5d_diff},
    "vdry_drv2_069_vol_ratio_on_down_vs_up_21d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_069_vol_ratio_on_down_vs_up_21d_5d_diff},
    "vdry_drv2_070_seller_exhaustion_score_21d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_070_seller_exhaustion_score_21d_diff},
    "vdry_drv2_071_low_vol_on_down_close_63d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_071_low_vol_on_down_close_63d_5d_diff},
    "vdry_drv2_072_vol_dryup_distress_index_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv2_072_vol_dryup_distress_index_5d_diff},
    "vdry_drv2_073_vol_log_ratio_63d_ema_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_073_vol_log_ratio_63d_ema_5d_diff},
    "vdry_drv2_074_vol_zscore_21d_slope_63d": {"inputs": ["volume"], "func": vdry_drv2_074_vol_zscore_21d_slope_63d},
    "vdry_drv2_075_vol_dryup_breadth_score_multi_5d_diff": {"inputs": ["volume"], "func": vdry_drv2_075_vol_dryup_breadth_score_multi_5d_diff},
}
