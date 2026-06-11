"""
18_volume_dryup — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative volume dry-up features — acceleration of dryup velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each = diff/slope applied to a 2nd-derivative concept

def vdry_drv3_001_vol_ratio_21d_mean_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/21d-mean ratio (jerk in dryup acceleration)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_002_vol_zscore_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume z-score (acceleration of dryup signal)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_003_vol_zscore_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day volume z-score."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_004_consec_below_mean_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-below-21d-mean streak."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_005_consec_vol_declining_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-declining-volume streak."""
    cond = volume < volume.shift(1)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_006_vol_decay_from_63d_max_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/63d-max ratio (jerk in post-spike collapse)."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_007_vol_decay_from_63d_max_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/63d-max ratio over 21 days."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_008_frac_below_mean_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of fraction-below-21d-mean (jerk in breadth dryup)."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_009_vol_21d_mean_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean volume (jerk in baseline trend)."""
    m21 = _rolling_mean(volume, _TD_MON)
    vel = m21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_010_vol_63d_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day mean volume."""
    m63 = _rolling_mean(volume, _TD_QTR)
    vel21 = m63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vdry_drv3_011_vol_pct_rank_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day volume percentile rank."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_012_dollar_vol_ratio_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of dollar-volume / 63d-mean ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_013_vol_21d_vs_252d_ratio_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d-mean/252d-mean vol ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_014_vol_dryup_intensity_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day dryup intensity (shortfall depth jerk)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_015_vol_dryup_intensity_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day dryup intensity."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_QTR)
    vel21 = intensity.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vdry_drv3_016_vol_log_ratio_63d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of log(vol/63d-mean) over 21 days."""
    log_ratio = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_QTR))
    slp = _linslope(log_ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_017_vol_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day volume z-score."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_018_low_vol_down_day_count_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of count of low-vol down days in 21-day window."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    count = _rolling_count_true(cond, _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_019_vol_21d_vs_252d_ratio_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d/252d vol-mean ratio over 21 days."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_020_consec_below_median_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-below-63d-median streak."""
    cond = volume < _rolling_median(volume, _TD_QTR)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_021_seller_exhaustion_score_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of seller exhaustion score (acceleration of exhaustion signal)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    depth = (1.0 - _safe_div(volume, mean21)).clip(lower=0.0)
    score = _rolling_sum(low_vol_down * depth, _TD_MON)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_022_vol_dryup_composite_zscore_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in composite vol z-score."""
    z21 = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    z63 = _safe_div(volume - _rolling_mean(volume, _TD_QTR), _rolling_std(volume, _TD_QTR))
    z252 = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    composite = (z21 + z63 + z252) / 3.0
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vdry_drv3_023_frac_below_mean_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in fraction of 63d below 63d-mean."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vdry_drv3_024_vol_ratio_63d_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in vol/63d-mean ratio."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vdry_drv3_025_vol_pct_rank_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day vol percentile rank."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel21 = rank.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- drv3 026-035: 3rd derivatives of EMA-based 2nd-derivative features ---

def vdry_drv3_026_vol_ratio_5d_ema_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/5d-EMA ratio (jerk in ultra-short dryup velocity)."""
    ratio = _safe_div(volume, _ewm_mean(volume, _TD_WEEK))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_027_vol_ratio_126d_ema_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in vol/126d-EMA ratio."""
    ratio = _safe_div(volume, _ewm_mean(volume, _TD_HALF))
    vel = ratio.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_028_log_vol_ratio_21d_ema_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(vol/21d-EMA) (jerk in EMA log-ratio velocity)."""
    lr = _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_MON))
    vel = lr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_029_vol_5d_ema_vs_63d_ema_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d-EMA/63d-EMA ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_030_vol_21d_ema_vs_252d_ema_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21d-EMA/252d-EMA ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_031_vol_zscore_5d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day volume z-score (ultra-short dryup jerk)."""
    m = _rolling_mean(volume, _TD_WEEK)
    s = _rolling_std(volume, _TD_WEEK)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_032_vol_zscore_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126-day volume z-score."""
    m = _rolling_mean(volume, _TD_HALF)
    s = _rolling_std(volume, _TD_HALF)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_033_log_vol_ratio_21d_mean_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of log(vol/21d-mean) over 21 days."""
    lr = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_MON))
    slp = _linslope(lr, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_034_log_vol_ratio_252d_mean_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(vol/252d-mean)."""
    lr = _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_YEAR))
    vel = lr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_035_vol_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day coefficient of variation of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- drv3 036-045: 3rd derivatives of decay-from-max and count-based features ---

def vdry_drv3_036_vol_decay_from_21d_max_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/21d-max ratio (jerk in short post-peak decay)."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_037_vol_decay_from_252d_max_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in vol/252d-max ratio."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_YEAR))
    vel = ratio.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_038_vol_max_to_min_ratio_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day vol max/min ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_min(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_039_vol_pct_rank_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol percentile rank."""
    rank = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_040_vol_pct_rank_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126-day vol percentile rank."""
    rank = volume.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_041_vol_126d_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126-day mean volume."""
    m126 = _rolling_mean(volume, _TD_HALF)
    vel = m126.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_042_vol_252d_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day mean volume."""
    m252 = _rolling_mean(volume, _TD_YEAR)
    vel = m252.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_043_vol_cv_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day coefficient of variation."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    vel = cv.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_044_vol_dryup_intensity_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day dryup intensity."""
    m252 = _rolling_mean(volume, _TD_YEAR)
    shortfall = (1.0 - _safe_div(volume, m252)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_YEAR)
    vel = intensity.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_045_vol_breadth_dryup_score_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d breadth dryup score (below 63d-mean + declining)."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (volume < mean63) & (volume < volume.shift(1))
    score = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- drv3 046-055: 3rd derivatives of dollar-volume, range-volume, body-volume ---

def vdry_drv3_046_dollar_vol_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of dollar-volume / 21d-mean ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_047_dollar_vol_ratio_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in dollar-volume / 252d-mean ratio."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_YEAR))
    vel = ratio.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_048_dollar_vol_zscore_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of dollar-volume 63-day z-score."""
    dv = close * volume
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_049_range_vol_ratio_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (high-low)*volume / 63d-mean ratio."""
    rv = (high - low) * volume
    ratio = _safe_div(rv, _rolling_mean(rv, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_050_range_vol_zscore_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in range-volume 63-day z-score."""
    rv = (high - low) * volume
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    z = _safe_div(rv - m, s)
    vel = z.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_051_body_vol_ratio_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of abs(close-open)*volume / 21d-mean ratio."""
    bv = (close - open).abs() * volume
    ratio = _safe_div(bv, _rolling_mean(bv, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_052_body_vol_zscore_63d_5d_diff_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of body-volume 63-day z-score."""
    bv = (close - open).abs() * volume
    m = _rolling_mean(bv, _TD_QTR)
    s = _rolling_std(bv, _TD_QTR)
    z = _safe_div(bv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_053_vol_contraction_5d_vs_63d_max_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d-mean/63d-max ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume.shift(1), _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_054_vol_contraction_21d_vs_252d_max_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21d-mean/252d-max ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_max(volume.shift(1), _TD_YEAR))
    vel = ratio.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_055_vol_dryup_intensity_63d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day dryup intensity over 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_QTR)
    slp = _linslope(intensity, _TD_QTR)
    return slp.diff(_TD_WEEK)


# --- drv3 056-065: 3rd derivatives of slope-based 2nd derivatives ---

def vdry_drv3_056_vol_ratio_21d_mean_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/21d-mean ratio over 63 days."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_057_vol_zscore_63d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day vol z-score over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    slp = _linslope(z, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_058_vol_zscore_252d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day vol z-score over 63 days."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    slp = _linslope(z, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_059_vol_pct_rank_63d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day vol percentile rank over 21 days."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    slp = _linslope(rank, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_060_vol_pct_rank_252d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day vol percentile rank over 63 days."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    slp = _linslope(rank, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_061_vol_21d_mean_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day mean volume over 63 days."""
    m21 = _rolling_mean(volume, _TD_MON)
    slp = _linslope(m21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_062_vol_63d_mean_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day mean volume over 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    slp = _linslope(m63, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_063_dollar_vol_ratio_63d_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of dollar-volume/63d-mean ratio over 21 days."""
    dv = close * volume
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_064_vol_decay_from_63d_max_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/63d-max ratio over 63 days."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vdry_drv3_065_vol_zscore_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day vol z-score over 63 days."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    slp = _linslope(z, _TD_QTR)
    return slp.diff(_TD_WEEK)


# --- drv3 066-075: 3rd derivatives of price-context and mixed 2nd derivatives ---

def vdry_drv3_066_vol_ratio_21d_mean_63d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day change in vol/21d-mean ratio."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_QTR)
    return vel.diff(_TD_WEEK)


def vdry_drv3_067_vol_dryup_intensity_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day dryup intensity."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    vel = intensity.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_068_vol_ratio_on_down_vs_up_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of avg-vol-down/avg-vol-up ratio over 21 days."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(dn, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_069_seller_exhaustion_score_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in seller exhaustion score."""
    mean21 = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    depth = (1.0 - _safe_div(volume, mean21)).clip(lower=0.0)
    score = _rolling_sum(low_vol_down * depth, _TD_MON)
    vel = score.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vdry_drv3_070_low_vol_on_down_close_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of count of low-vol down-close days in 63-day window."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    count = _rolling_count_true(cond, _TD_QTR)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_071_vol_dryup_distress_index_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol dryup distress index."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = volume < mean63
    streak = _consec_streak(cond)
    depth = (1.0 - _safe_div(volume, mean63)).clip(lower=0.0)
    ret = close.pct_change(1)
    dn_frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    index = streak * depth * dn_frac
    vel = index.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_072_vol_log_ratio_63d_ema_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(vol/63d-EMA)."""
    lr = _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_QTR))
    vel = lr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_073_vol_dryup_breadth_score_multi_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-window below-mean flag count."""
    f1 = (volume < _rolling_mean(volume, _TD_WEEK)).astype(float)
    f2 = (volume < _rolling_mean(volume, _TD_MON)).astype(float)
    f3 = (volume < _rolling_mean(volume, _TD_QTR)).astype(float)
    f4 = (volume < _rolling_mean(volume, _TD_YEAR)).astype(float)
    score = f1 + f2 + f3 + f4
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vdry_drv3_074_vol_dryup_composite_zscore_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of composite vol z-score (21d/63d/252d avg) over 21 days."""
    z21 = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    z63 = _safe_div(volume - _rolling_mean(volume, _TD_QTR), _rolling_std(volume, _TD_QTR))
    z252 = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    composite = (z21 + z63 + z252) / 3.0
    slp = _linslope(composite, _TD_MON)
    return slp.diff(_TD_WEEK)


def vdry_drv3_075_vol_dryup_intensity_21d_5d_diff_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 5-day change in 21-day dryup intensity (medium-term acceleration)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DRYUP_REGISTRY_3RD_DERIVATIVES = {
    "vdry_drv3_001_vol_ratio_21d_mean_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_001_vol_ratio_21d_mean_5d_diff_5d_diff},
    "vdry_drv3_002_vol_zscore_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_002_vol_zscore_21d_5d_diff_5d_diff},
    "vdry_drv3_003_vol_zscore_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_003_vol_zscore_63d_21d_diff_5d_diff},
    "vdry_drv3_004_consec_below_mean_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_004_consec_below_mean_21d_5d_diff_5d_diff},
    "vdry_drv3_005_consec_vol_declining_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_005_consec_vol_declining_5d_diff_5d_diff},
    "vdry_drv3_006_vol_decay_from_63d_max_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_006_vol_decay_from_63d_max_5d_diff_5d_diff},
    "vdry_drv3_007_vol_decay_from_63d_max_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_007_vol_decay_from_63d_max_slope_5d_diff},
    "vdry_drv3_008_frac_below_mean_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_008_frac_below_mean_21d_5d_diff_5d_diff},
    "vdry_drv3_009_vol_21d_mean_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_009_vol_21d_mean_5d_diff_5d_diff},
    "vdry_drv3_010_vol_63d_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_010_vol_63d_mean_21d_diff_5d_diff},
    "vdry_drv3_011_vol_pct_rank_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_011_vol_pct_rank_63d_5d_diff_5d_diff},
    "vdry_drv3_012_dollar_vol_ratio_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_012_dollar_vol_ratio_63d_5d_diff_5d_diff},
    "vdry_drv3_013_vol_21d_vs_252d_ratio_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_013_vol_21d_vs_252d_ratio_5d_diff_5d_diff},
    "vdry_drv3_014_vol_dryup_intensity_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_014_vol_dryup_intensity_21d_5d_diff_5d_diff},
    "vdry_drv3_015_vol_dryup_intensity_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_015_vol_dryup_intensity_63d_21d_diff_5d_diff},
    "vdry_drv3_016_vol_log_ratio_63d_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_016_vol_log_ratio_63d_slope_5d_diff},
    "vdry_drv3_017_vol_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_017_vol_zscore_252d_5d_diff_5d_diff},
    "vdry_drv3_018_low_vol_down_day_count_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_018_low_vol_down_day_count_5d_diff_5d_diff},
    "vdry_drv3_019_vol_21d_vs_252d_ratio_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_019_vol_21d_vs_252d_ratio_slope_5d_diff},
    "vdry_drv3_020_consec_below_median_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_020_consec_below_median_63d_5d_diff_5d_diff},
    "vdry_drv3_021_seller_exhaustion_score_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_021_seller_exhaustion_score_5d_diff_5d_diff},
    "vdry_drv3_022_vol_dryup_composite_zscore_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_022_vol_dryup_composite_zscore_21d_diff_5d_diff},
    "vdry_drv3_023_frac_below_mean_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_023_frac_below_mean_63d_21d_diff_5d_diff},
    "vdry_drv3_024_vol_ratio_63d_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_024_vol_ratio_63d_mean_21d_diff_5d_diff},
    "vdry_drv3_025_vol_pct_rank_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_025_vol_pct_rank_252d_21d_diff_5d_diff},
    "vdry_drv3_026_vol_ratio_5d_ema_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_026_vol_ratio_5d_ema_5d_diff_5d_diff},
    "vdry_drv3_027_vol_ratio_126d_ema_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_027_vol_ratio_126d_ema_21d_diff_5d_diff},
    "vdry_drv3_028_log_vol_ratio_21d_ema_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_028_log_vol_ratio_21d_ema_5d_diff_5d_diff},
    "vdry_drv3_029_vol_5d_ema_vs_63d_ema_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_029_vol_5d_ema_vs_63d_ema_5d_diff_5d_diff},
    "vdry_drv3_030_vol_21d_ema_vs_252d_ema_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_030_vol_21d_ema_vs_252d_ema_21d_diff_5d_diff},
    "vdry_drv3_031_vol_zscore_5d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_031_vol_zscore_5d_5d_diff_5d_diff},
    "vdry_drv3_032_vol_zscore_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_032_vol_zscore_126d_21d_diff_5d_diff},
    "vdry_drv3_033_log_vol_ratio_21d_mean_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_033_log_vol_ratio_21d_mean_slope_5d_diff},
    "vdry_drv3_034_log_vol_ratio_252d_mean_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_034_log_vol_ratio_252d_mean_5d_diff_5d_diff},
    "vdry_drv3_035_vol_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_035_vol_cv_21d_5d_diff_5d_diff},
    "vdry_drv3_036_vol_decay_from_21d_max_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_036_vol_decay_from_21d_max_5d_diff_5d_diff},
    "vdry_drv3_037_vol_decay_from_252d_max_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_037_vol_decay_from_252d_max_21d_diff_5d_diff},
    "vdry_drv3_038_vol_max_to_min_ratio_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_038_vol_max_to_min_ratio_63d_5d_diff_5d_diff},
    "vdry_drv3_039_vol_pct_rank_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_039_vol_pct_rank_21d_5d_diff_5d_diff},
    "vdry_drv3_040_vol_pct_rank_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_040_vol_pct_rank_126d_21d_diff_5d_diff},
    "vdry_drv3_041_vol_126d_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_041_vol_126d_mean_21d_diff_5d_diff},
    "vdry_drv3_042_vol_252d_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_042_vol_252d_mean_21d_diff_5d_diff},
    "vdry_drv3_043_vol_cv_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_043_vol_cv_63d_21d_diff_5d_diff},
    "vdry_drv3_044_vol_dryup_intensity_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_044_vol_dryup_intensity_252d_21d_diff_5d_diff},
    "vdry_drv3_045_vol_breadth_dryup_score_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_045_vol_breadth_dryup_score_21d_5d_diff_5d_diff},
    "vdry_drv3_046_dollar_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_046_dollar_vol_ratio_21d_5d_diff_5d_diff},
    "vdry_drv3_047_dollar_vol_ratio_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_047_dollar_vol_ratio_252d_21d_diff_5d_diff},
    "vdry_drv3_048_dollar_vol_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_048_dollar_vol_zscore_63d_5d_diff_5d_diff},
    "vdry_drv3_049_range_vol_ratio_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "volume"], "func": vdry_drv3_049_range_vol_ratio_63d_5d_diff_5d_diff},
    "vdry_drv3_050_range_vol_zscore_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "volume"], "func": vdry_drv3_050_range_vol_zscore_63d_21d_diff_5d_diff},
    "vdry_drv3_051_body_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "volume"], "func": vdry_drv3_051_body_vol_ratio_21d_5d_diff_5d_diff},
    "vdry_drv3_052_body_vol_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "open", "volume"], "func": vdry_drv3_052_body_vol_zscore_63d_5d_diff_5d_diff},
    "vdry_drv3_053_vol_contraction_5d_vs_63d_max_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_053_vol_contraction_5d_vs_63d_max_5d_diff_5d_diff},
    "vdry_drv3_054_vol_contraction_21d_vs_252d_max_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_054_vol_contraction_21d_vs_252d_max_21d_diff_5d_diff},
    "vdry_drv3_055_vol_dryup_intensity_63d_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_055_vol_dryup_intensity_63d_slope_5d_diff},
    "vdry_drv3_056_vol_ratio_21d_mean_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_056_vol_ratio_21d_mean_slope_63d_5d_diff},
    "vdry_drv3_057_vol_zscore_63d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_057_vol_zscore_63d_slope_63d_5d_diff},
    "vdry_drv3_058_vol_zscore_252d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_058_vol_zscore_252d_slope_63d_5d_diff},
    "vdry_drv3_059_vol_pct_rank_63d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_059_vol_pct_rank_63d_slope_21d_5d_diff},
    "vdry_drv3_060_vol_pct_rank_252d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_060_vol_pct_rank_252d_slope_63d_5d_diff},
    "vdry_drv3_061_vol_21d_mean_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_061_vol_21d_mean_slope_63d_5d_diff},
    "vdry_drv3_062_vol_63d_mean_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_062_vol_63d_mean_slope_63d_5d_diff},
    "vdry_drv3_063_dollar_vol_ratio_63d_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_063_dollar_vol_ratio_63d_slope_21d_5d_diff},
    "vdry_drv3_064_vol_decay_from_63d_max_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_064_vol_decay_from_63d_max_slope_63d_5d_diff},
    "vdry_drv3_065_vol_zscore_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_065_vol_zscore_21d_slope_63d_5d_diff},
    "vdry_drv3_066_vol_ratio_21d_mean_63d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_066_vol_ratio_21d_mean_63d_diff_5d_diff},
    "vdry_drv3_067_vol_dryup_intensity_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_067_vol_dryup_intensity_21d_21d_diff_5d_diff},
    "vdry_drv3_068_vol_ratio_on_down_vs_up_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_068_vol_ratio_on_down_vs_up_21d_5d_diff_5d_diff},
    "vdry_drv3_069_seller_exhaustion_score_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_069_seller_exhaustion_score_21d_diff_5d_diff},
    "vdry_drv3_070_low_vol_on_down_close_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_070_low_vol_on_down_close_63d_5d_diff_5d_diff},
    "vdry_drv3_071_vol_dryup_distress_index_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vdry_drv3_071_vol_dryup_distress_index_5d_diff_5d_diff},
    "vdry_drv3_072_vol_log_ratio_63d_ema_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_072_vol_log_ratio_63d_ema_5d_diff_5d_diff},
    "vdry_drv3_073_vol_dryup_breadth_score_multi_5d_diff_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_073_vol_dryup_breadth_score_multi_5d_diff_5d_diff},
    "vdry_drv3_074_vol_dryup_composite_zscore_slope_5d_diff": {"inputs": ["volume"], "func": vdry_drv3_074_vol_dryup_composite_zscore_slope_5d_diff},
    "vdry_drv3_075_vol_dryup_intensity_21d_5d_diff_21d_diff": {"inputs": ["volume"], "func": vdry_drv3_075_vol_dryup_intensity_21d_5d_diff_21d_diff},
}
