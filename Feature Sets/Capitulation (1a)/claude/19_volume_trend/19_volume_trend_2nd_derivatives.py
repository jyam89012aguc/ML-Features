"""
19_volume_trend — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume-trend features — velocity / acceleration of trend behavior
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
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods."""
    def _slope(x):
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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _linslope_rsq(s: pd.Series, w: int) -> pd.Series:
    """Rolling R-squared of OLS line fit of s over w periods."""
    def _rsq(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        ss_tot = ((x - x_m) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        ss_res = (resid ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_rsq, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vtr_drv2_001_vol_ols_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume OLS slope (velocity of short-term trend)."""
    slope = _linslope(volume, _TD_MON)
    return slope.diff(_TD_WEEK)


def vtr_drv2_002_vol_ols_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume OLS slope (monthly velocity of medium trend)."""
    slope = _linslope(volume, _TD_QTR)
    return slope.diff(_TD_MON)


def vtr_drv2_003_logvol_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-volume OLS slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    return slope.diff(_TD_WEEK)


def vtr_drv2_004_logvol_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day log-volume OLS slope."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    return slope.diff(_TD_MON)


def vtr_drv2_005_vol_ema21_vs_ema63_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EMA21/EMA63 volume ratio (velocity of EMA crossover)."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vtr_drv2_006_vol_sma21_vs_sma63_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of SMA21/SMA63 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vtr_drv2_007_vol_rising_days_frac_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day rising-volume-day fraction."""
    frac = (volume > volume.shift(1)).astype(float)
    frac21 = _rolling_mean(frac, _TD_MON)
    return frac21.diff(_TD_WEEK)


def vtr_drv2_008_vol_rising_weeks_frac_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day rising-volume-week fraction."""
    frac = (volume.pct_change(_TD_WEEK) > 0).astype(float)
    frac63 = _rolling_mean(frac, _TD_QTR)
    return frac63.diff(_TD_MON)


def vtr_drv2_009_vol_trend_consistency_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume trend consistency score."""
    sign_chg = np.sign(volume - volume.shift(1))
    consistency = sign_chg.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum().abs() / _TD_MON
    return consistency.diff(_TD_WEEK)


def vtr_drv2_010_vol_net_drift_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume net drift."""
    drift = _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON).clip(lower=_EPS))
    return drift.diff(_TD_WEEK)


def vtr_drv2_011_vol_net_drift_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume net drift."""
    drift = _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).clip(lower=_EPS))
    return drift.diff(_TD_MON)


def vtr_drv2_012_vol_ema_crossover_score_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the EMA crossover alignment score."""
    s1 = (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)).astype(float)
    s2 = (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)).astype(float)
    s3 = (_ewm_mean(volume, _TD_QTR) > _ewm_mean(volume, _TD_YEAR)).astype(float)
    score = s1 + s2 + s3
    return score.diff(_TD_WEEK)


def vtr_drv2_013_vol_rsq_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day volume R-squared over trailing 21 days."""
    rsq = _linslope_rsq(volume, _TD_MON)
    return _linslope(rsq, _TD_MON)


def vtr_drv2_014_logvol_rsq_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day log-volume R-squared."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_QTR)
    return rsq.diff(_TD_MON)


def vtr_drv2_015_vol_21d_return_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume percent-return (acceleration of short drift)."""
    ret = volume.pct_change(_TD_MON)
    return ret.diff(_TD_WEEK)


def vtr_drv2_016_vol_63d_return_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume percent-return."""
    ret = volume.pct_change(_TD_QTR)
    return ret.diff(_TD_MON)


def vtr_drv2_017_logvol_21d_change_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-volume change."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_MON)
    return chg.diff(_TD_WEEK)


def vtr_drv2_018_logvol_63d_change_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day log-volume change."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_QTR)
    return chg.diff(_TD_MON)


def vtr_drv2_019_vol_ema21_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of EMA21 volume."""
    ema21 = _ewm_mean(volume, _TD_MON)
    slope = _linslope(ema21, _TD_MON)
    return slope.diff(_TD_WEEK)


def vtr_drv2_020_vol_slope_21d_norm_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the normalized 21-day volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return _linslope(slope_norm, _TD_QTR)


def vtr_drv2_021_logvol_slope_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    return _linslope(slope, _TD_QTR)


def vtr_drv2_022_vol_trend_regime_score_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the volume trend regime score (count of positive slopes)."""
    s = [(_linslope(volume, w) > 0).astype(float)
         for w in [_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR]]
    score = s[0] + s[1] + s[2] + s[3]
    return score.diff(_TD_WEEK)


def vtr_drv2_023_vol_sma21_vs_sma252_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of SMA21/SMA252 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vtr_drv2_024_vol_trend_price_divergence_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-vs-price slope sign divergence."""
    vs = np.sign(_linslope(volume, _TD_MON))
    ps = np.sign(_linslope(close, _TD_MON))
    divergence = vs - ps
    return divergence.diff(_TD_WEEK)


def vtr_drv2_025_vol_logslope_21d_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21-day log-volume slope vs 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    z = _safe_div(slope - m, s)
    return z.diff(_TD_WEEK)


# ── 2nd-Derivative Feature Functions 026-075 ─────────────────────────────────

def vtr_drv2_026_vol_ols_slope_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume OLS slope (monthly velocity of half-year trend)."""
    slope = _linslope(volume, _TD_HALF)
    return slope.diff(_TD_MON)


def vtr_drv2_027_vol_ols_slope_252d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day volume OLS slope (quarterly velocity of annual trend)."""
    slope = _linslope(volume, _TD_YEAR)
    return slope.diff(_TD_QTR)


def vtr_drv2_028_logvol_slope_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day log-volume OLS slope."""
    slope = _linslope(_log_safe(volume), _TD_HALF)
    return slope.diff(_TD_MON)


def vtr_drv2_029_logvol_slope_252d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day log-volume OLS slope."""
    slope = _linslope(_log_safe(volume), _TD_YEAR)
    return slope.diff(_TD_QTR)


def vtr_drv2_030_vol_ema5_vs_ema63_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EMA5/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vtr_drv2_031_vol_ema63_vs_ema252_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EMA63/EMA252 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vtr_drv2_032_vol_sma21_vs_sma126_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of SMA21/SMA126 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_HALF))
    return ratio.diff(_TD_MON)


def vtr_drv2_033_vol_sma63_vs_sma252_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of SMA63/SMA252 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vtr_drv2_034_vol_rising_days_frac_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day rising-volume-day fraction."""
    frac = (volume > volume.shift(1)).astype(float)
    frac63 = _rolling_mean(frac, _TD_QTR)
    return frac63.diff(_TD_MON)


def vtr_drv2_035_vol_rising_days_frac_252d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day rising-volume-day fraction."""
    frac = (volume > volume.shift(1)).astype(float)
    frac252 = _rolling_mean(frac, _TD_YEAR)
    return frac252.diff(_TD_QTR)


def vtr_drv2_036_vol_trend_consistency_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume trend consistency score."""
    sign_chg = np.sign(volume - volume.shift(1))
    consistency = sign_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum().abs() / _TD_QTR
    return consistency.diff(_TD_MON)


def vtr_drv2_037_vol_trend_consistency_252d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day volume trend consistency score."""
    sign_chg = np.sign(volume - volume.shift(1))
    consistency = sign_chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum().abs() / _TD_YEAR
    return consistency.diff(_TD_QTR)


def vtr_drv2_038_vol_net_drift_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume net drift."""
    drift = _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).clip(lower=_EPS))
    return drift.diff(_TD_WEEK)


def vtr_drv2_039_vol_net_drift_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume net drift."""
    drift = _safe_div(volume - volume.shift(_TD_HALF), volume.shift(_TD_HALF).clip(lower=_EPS))
    return drift.diff(_TD_MON)


def vtr_drv2_040_vol_rsq_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume R-squared."""
    rsq = _linslope_rsq(volume, _TD_QTR)
    return rsq.diff(_TD_MON)


def vtr_drv2_041_vol_rsq_252d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day volume R-squared."""
    rsq = _linslope_rsq(volume, _TD_YEAR)
    return rsq.diff(_TD_QTR)


def vtr_drv2_042_logvol_rsq_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-volume R-squared."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_MON)
    return rsq.diff(_TD_WEEK)


def vtr_drv2_043_logvol_rsq_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day log-volume R-squared."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_HALF)
    return rsq.diff(_TD_MON)


def vtr_drv2_044_vol_ema21_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day OLS slope of EMA21 volume."""
    slope = _linslope(_ewm_mean(volume, _TD_MON), _TD_QTR)
    return slope.diff(_TD_MON)


def vtr_drv2_045_vol_ema63_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day OLS slope of EMA63 volume."""
    slope = _linslope(_ewm_mean(volume, _TD_QTR), _TD_QTR)
    return slope.diff(_TD_MON)


def vtr_drv2_046_vol_ema63_21d_change_norm_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the normalized 21-day change in EMA63 volume."""
    ema63 = _ewm_mean(volume, _TD_QTR)
    chg_norm = _safe_div(ema63 - ema63.shift(_TD_MON), ema63.shift(_TD_MON).clip(lower=_EPS))
    return chg_norm.diff(_TD_WEEK)


def vtr_drv2_047_vol_126d_return_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume percent-return."""
    ret = volume.pct_change(_TD_HALF)
    return ret.diff(_TD_MON)


def vtr_drv2_048_vol_252d_return_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day volume percent-return."""
    ret = volume.pct_change(_TD_YEAR)
    return ret.diff(_TD_QTR)


def vtr_drv2_049_logvol_126d_change_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day log-volume change."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_HALF)
    return chg.diff(_TD_MON)


def vtr_drv2_050_logvol_252d_change_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 252-day log-volume change."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_YEAR)
    return chg.diff(_TD_QTR)


def vtr_drv2_051_vol_slope_21d_pct_rank_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the percentile rank of 21-day volume slope in 252-day window."""
    slope = _linslope(volume, _TD_MON)
    rank = slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vtr_drv2_052_vol_slope_63d_pct_rank_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the percentile rank of 63-day volume slope in 252-day window."""
    slope = _linslope(volume, _TD_QTR)
    rank = slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def vtr_drv2_053_vol_slope_21d_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the z-score of 21-day raw-volume slope vs 252-day distribution."""
    slope = _linslope(volume, _TD_MON)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    z = _safe_div(slope - m, s)
    return z.diff(_TD_WEEK)


def vtr_drv2_054_vol_slope_63d_zscore_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the z-score of 63-day raw-volume slope vs 252-day distribution."""
    slope = _linslope(volume, _TD_QTR)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    z = _safe_div(slope - m, s)
    return z.diff(_TD_MON)


def vtr_drv2_055_logvol_slope_63d_zscore_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the z-score of 63-day log-volume slope vs 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    z = _safe_div(slope - m, s)
    return z.diff(_TD_MON)


def vtr_drv2_056_vol_trend_score_composite_4window_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 4-window normalized volume slope composite."""
    def _norm_slope(w):
        sl = _linslope(volume, w)
        avg = _rolling_mean(volume, w).clip(lower=_EPS)
        return _safe_div(sl, avg)
    score = _norm_slope(_TD_MON) + _norm_slope(_TD_QTR) + _norm_slope(_TD_HALF) + _norm_slope(_TD_YEAR)
    return score.diff(_TD_WEEK)


def vtr_drv2_057_logvol_slope_composite_4window_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the sum of log-volume slopes over 4 windows."""
    lv = _log_safe(volume)
    score = (_linslope(lv, _TD_MON) + _linslope(lv, _TD_QTR)
             + _linslope(lv, _TD_HALF) + _linslope(lv, _TD_YEAR))
    return score.diff(_TD_WEEK)


def vtr_drv2_058_vol_sma_alignment_score_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of SMA alignment score (count of in-order SMA pairs)."""
    s5 = _rolling_mean(volume, _TD_WEEK)
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    s252 = _rolling_mean(volume, _TD_YEAR)
    score = ((s5 > s21).astype(float) + (s21 > s63).astype(float)
             + (s63 > s252).astype(float))
    return score.diff(_TD_WEEK)


def vtr_drv2_059_vol_ema_crossover_score_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the EMA crossover alignment score."""
    s1 = (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)).astype(float)
    s2 = (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)).astype(float)
    s3 = (_ewm_mean(volume, _TD_QTR) > _ewm_mean(volume, _TD_YEAR)).astype(float)
    score = s1 + s2 + s3
    return score.diff(_TD_MON)


def vtr_drv2_060_vol_negative_slope_count_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the count of negative volume slopes (21d, 63d, 126d, 252d)."""
    s21 = (_linslope(volume, _TD_MON) < 0).astype(float)
    s63 = (_linslope(volume, _TD_QTR) < 0).astype(float)
    s126 = (_linslope(volume, _TD_HALF) < 0).astype(float)
    s252 = (_linslope(volume, _TD_YEAR) < 0).astype(float)
    score = s21 + s63 + s126 + s252
    return score.diff(_TD_WEEK)


def vtr_drv2_061_vol_slope_21d_norm_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the normalized 21-day volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return slope_norm.diff(_TD_WEEK)


def vtr_drv2_062_vol_slope_63d_norm_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the normalized 63-day volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return slope_norm.diff(_TD_MON)


def vtr_drv2_063_vol_slope_126d_norm_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the normalized 126-day volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF).clip(lower=_EPS))
    return slope_norm.diff(_TD_MON)


def vtr_drv2_064_vol_slope_252d_norm_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of the normalized 252-day volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return slope_norm.diff(_TD_QTR)


def vtr_drv2_065_vol_ema21_5d_change_norm_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the normalized 5-day change in EMA21 volume."""
    ema21 = _ewm_mean(volume, _TD_MON)
    chg_norm = _safe_div(ema21 - ema21.shift(_TD_WEEK), ema21.shift(_TD_WEEK).clip(lower=_EPS))
    return chg_norm.diff(_TD_MON)


def vtr_drv2_066_vol_sma_dispersion_21_63_252_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the SMA dispersion (std/mean of SMA21, SMA63, SMA252 volumes)."""
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    s252 = _rolling_mean(volume, _TD_YEAR)
    avg = (s21 + s63 + s252) / 3.0
    spread = ((s21 - avg)**2 + (s63 - avg)**2 + (s252 - avg)**2) / 3.0
    disp = _safe_div(spread**0.5, avg.clip(lower=_EPS))
    return disp.diff(_TD_WEEK)


def vtr_drv2_067_vol_trend_direction_composite_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of avg signed R-squared composite (21d, 63d, 252d volume trends)."""
    def _signed_rsq(w):
        rsq = _linslope_rsq(volume, w)
        sgn = np.sign(_linslope(volume, w))
        return rsq * sgn
    composite = (_signed_rsq(_TD_MON) + _signed_rsq(_TD_QTR) + _signed_rsq(_TD_YEAR)) / 3.0
    return composite.diff(_TD_WEEK)


def vtr_drv2_068_vol_trend_strength_index_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day log-volume trend-strength index."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_QTR)
    sgn = np.sign(_linslope(_log_safe(volume), _TD_QTR))
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    consistency = total_sign.abs() / _TD_QTR
    idx = rsq * sgn * consistency
    return idx.diff(_TD_WEEK)


def vtr_drv2_069_vol_logslope_21d_expanding_zscore_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the expanding z-score of 21-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    m = slope.expanding(min_periods=5).mean()
    s = slope.expanding(min_periods=5).std()
    z = _safe_div(slope - m, s)
    return z.diff(_TD_WEEK)


def vtr_drv2_070_vol_logslope_63d_expanding_zscore_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the expanding z-score of 63-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    m = slope.expanding(min_periods=5).mean()
    s = slope.expanding(min_periods=5).std()
    z = _safe_div(slope - m, s)
    return z.diff(_TD_MON)


def vtr_drv2_071_vol_rising_months_frac_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the fraction of 21-day periods with rising cumulative volume (252d)."""
    monthly_vol = volume.pct_change(_TD_MON)
    rising = (monthly_vol > 0).astype(float)
    frac = _rolling_mean(rising, _TD_YEAR)
    return frac.diff(_TD_MON)


def vtr_drv2_072_vol_rising_weeks_count_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the count of 5-day periods with rising volume within 252 days."""
    weekly_ret = volume.pct_change(_TD_WEEK)
    rising = (weekly_ret > 0).astype(float)
    count = _rolling_sum(rising, _TD_YEAR)
    return count.diff(_TD_MON)


def vtr_drv2_073_vol_trend_price_divergence_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume-vs-price slope sign divergence."""
    vs = np.sign(_linslope(volume, _TD_QTR))
    ps = np.sign(_linslope(close, _TD_QTR))
    divergence = vs - ps
    return divergence.diff(_TD_MON)


def vtr_drv2_074_vol_up_trend_price_down_flag_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the flag: volume up-trending while price down-trending (21d)."""
    vs = _linslope(volume, _TD_MON)
    ps = _linslope(close, _TD_MON)
    flag = ((vs > 0) & (ps < 0)).astype(float)
    return flag.diff(_TD_WEEK)


def vtr_drv2_075_vol_ema21_vs_ema252_ratio_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of z-score of EMA21/EMA252 volume ratio vs 252-day distribution."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    z = _safe_div(ratio - m, s)
    return z.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_TREND_REGISTRY_2ND_DERIVATIVES = {
    "vtr_drv2_001_vol_ols_slope_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_001_vol_ols_slope_21d_5d_diff},
    "vtr_drv2_002_vol_ols_slope_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_002_vol_ols_slope_63d_21d_diff},
    "vtr_drv2_003_logvol_slope_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_003_logvol_slope_21d_5d_diff},
    "vtr_drv2_004_logvol_slope_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_004_logvol_slope_63d_21d_diff},
    "vtr_drv2_005_vol_ema21_vs_ema63_ratio_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_005_vol_ema21_vs_ema63_ratio_5d_diff},
    "vtr_drv2_006_vol_sma21_vs_sma63_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_006_vol_sma21_vs_sma63_ratio_21d_diff},
    "vtr_drv2_007_vol_rising_days_frac_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_007_vol_rising_days_frac_21d_5d_diff},
    "vtr_drv2_008_vol_rising_weeks_frac_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_008_vol_rising_weeks_frac_63d_21d_diff},
    "vtr_drv2_009_vol_trend_consistency_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_009_vol_trend_consistency_21d_5d_diff},
    "vtr_drv2_010_vol_net_drift_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_010_vol_net_drift_21d_5d_diff},
    "vtr_drv2_011_vol_net_drift_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_011_vol_net_drift_63d_21d_diff},
    "vtr_drv2_012_vol_ema_crossover_score_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_012_vol_ema_crossover_score_5d_diff},
    "vtr_drv2_013_vol_rsq_21d_slope_21d": {"inputs": ["volume"], "func": vtr_drv2_013_vol_rsq_21d_slope_21d},
    "vtr_drv2_014_logvol_rsq_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_014_logvol_rsq_63d_21d_diff},
    "vtr_drv2_015_vol_21d_return_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_015_vol_21d_return_5d_diff},
    "vtr_drv2_016_vol_63d_return_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_016_vol_63d_return_21d_diff},
    "vtr_drv2_017_logvol_21d_change_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_017_logvol_21d_change_5d_diff},
    "vtr_drv2_018_logvol_63d_change_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_018_logvol_63d_change_21d_diff},
    "vtr_drv2_019_vol_ema21_slope_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_019_vol_ema21_slope_21d_5d_diff},
    "vtr_drv2_020_vol_slope_21d_norm_slope_63d": {"inputs": ["volume"], "func": vtr_drv2_020_vol_slope_21d_norm_slope_63d},
    "vtr_drv2_021_logvol_slope_21d_slope_63d": {"inputs": ["volume"], "func": vtr_drv2_021_logvol_slope_21d_slope_63d},
    "vtr_drv2_022_vol_trend_regime_score_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_022_vol_trend_regime_score_5d_diff},
    "vtr_drv2_023_vol_sma21_vs_sma252_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_023_vol_sma21_vs_sma252_ratio_21d_diff},
    "vtr_drv2_024_vol_trend_price_divergence_21d_5d_diff": {"inputs": ["close", "volume"], "func": vtr_drv2_024_vol_trend_price_divergence_21d_5d_diff},
    "vtr_drv2_025_vol_logslope_21d_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_025_vol_logslope_21d_zscore_252d_5d_diff},
    "vtr_drv2_026_vol_ols_slope_126d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_026_vol_ols_slope_126d_21d_diff},
    "vtr_drv2_027_vol_ols_slope_252d_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_027_vol_ols_slope_252d_63d_diff},
    "vtr_drv2_028_logvol_slope_126d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_028_logvol_slope_126d_21d_diff},
    "vtr_drv2_029_logvol_slope_252d_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_029_logvol_slope_252d_63d_diff},
    "vtr_drv2_030_vol_ema5_vs_ema63_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_030_vol_ema5_vs_ema63_ratio_21d_diff},
    "vtr_drv2_031_vol_ema63_vs_ema252_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_031_vol_ema63_vs_ema252_ratio_21d_diff},
    "vtr_drv2_032_vol_sma21_vs_sma126_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_032_vol_sma21_vs_sma126_ratio_21d_diff},
    "vtr_drv2_033_vol_sma63_vs_sma252_ratio_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_033_vol_sma63_vs_sma252_ratio_21d_diff},
    "vtr_drv2_034_vol_rising_days_frac_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_034_vol_rising_days_frac_63d_21d_diff},
    "vtr_drv2_035_vol_rising_days_frac_252d_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_035_vol_rising_days_frac_252d_63d_diff},
    "vtr_drv2_036_vol_trend_consistency_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_036_vol_trend_consistency_63d_21d_diff},
    "vtr_drv2_037_vol_trend_consistency_252d_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_037_vol_trend_consistency_252d_63d_diff},
    "vtr_drv2_038_vol_net_drift_63d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_038_vol_net_drift_63d_5d_diff},
    "vtr_drv2_039_vol_net_drift_126d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_039_vol_net_drift_126d_21d_diff},
    "vtr_drv2_040_vol_rsq_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_040_vol_rsq_63d_21d_diff},
    "vtr_drv2_041_vol_rsq_252d_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_041_vol_rsq_252d_63d_diff},
    "vtr_drv2_042_logvol_rsq_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_042_logvol_rsq_21d_5d_diff},
    "vtr_drv2_043_logvol_rsq_126d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_043_logvol_rsq_126d_21d_diff},
    "vtr_drv2_044_vol_ema21_slope_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_044_vol_ema21_slope_63d_21d_diff},
    "vtr_drv2_045_vol_ema63_slope_63d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_045_vol_ema63_slope_63d_21d_diff},
    "vtr_drv2_046_vol_ema63_21d_change_norm_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_046_vol_ema63_21d_change_norm_5d_diff},
    "vtr_drv2_047_vol_126d_return_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_047_vol_126d_return_21d_diff},
    "vtr_drv2_048_vol_252d_return_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_048_vol_252d_return_63d_diff},
    "vtr_drv2_049_logvol_126d_change_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_049_logvol_126d_change_21d_diff},
    "vtr_drv2_050_logvol_252d_change_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_050_logvol_252d_change_63d_diff},
    "vtr_drv2_051_vol_slope_21d_pct_rank_252d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_051_vol_slope_21d_pct_rank_252d_5d_diff},
    "vtr_drv2_052_vol_slope_63d_pct_rank_252d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_052_vol_slope_63d_pct_rank_252d_21d_diff},
    "vtr_drv2_053_vol_slope_21d_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_053_vol_slope_21d_zscore_252d_5d_diff},
    "vtr_drv2_054_vol_slope_63d_zscore_252d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_054_vol_slope_63d_zscore_252d_21d_diff},
    "vtr_drv2_055_logvol_slope_63d_zscore_252d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_055_logvol_slope_63d_zscore_252d_21d_diff},
    "vtr_drv2_056_vol_trend_score_composite_4window_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_056_vol_trend_score_composite_4window_5d_diff},
    "vtr_drv2_057_logvol_slope_composite_4window_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_057_logvol_slope_composite_4window_5d_diff},
    "vtr_drv2_058_vol_sma_alignment_score_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_058_vol_sma_alignment_score_5d_diff},
    "vtr_drv2_059_vol_ema_crossover_score_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_059_vol_ema_crossover_score_21d_diff},
    "vtr_drv2_060_vol_negative_slope_count_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_060_vol_negative_slope_count_5d_diff},
    "vtr_drv2_061_vol_slope_21d_norm_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_061_vol_slope_21d_norm_5d_diff},
    "vtr_drv2_062_vol_slope_63d_norm_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_062_vol_slope_63d_norm_21d_diff},
    "vtr_drv2_063_vol_slope_126d_norm_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_063_vol_slope_126d_norm_21d_diff},
    "vtr_drv2_064_vol_slope_252d_norm_63d_diff": {"inputs": ["volume"], "func": vtr_drv2_064_vol_slope_252d_norm_63d_diff},
    "vtr_drv2_065_vol_ema21_5d_change_norm_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_065_vol_ema21_5d_change_norm_21d_diff},
    "vtr_drv2_066_vol_sma_dispersion_21_63_252_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_066_vol_sma_dispersion_21_63_252_5d_diff},
    "vtr_drv2_067_vol_trend_direction_composite_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_067_vol_trend_direction_composite_5d_diff},
    "vtr_drv2_068_vol_trend_strength_index_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_068_vol_trend_strength_index_5d_diff},
    "vtr_drv2_069_vol_logslope_21d_expanding_zscore_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_069_vol_logslope_21d_expanding_zscore_5d_diff},
    "vtr_drv2_070_vol_logslope_63d_expanding_zscore_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_070_vol_logslope_63d_expanding_zscore_21d_diff},
    "vtr_drv2_071_vol_rising_months_frac_252d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_071_vol_rising_months_frac_252d_21d_diff},
    "vtr_drv2_072_vol_rising_weeks_count_252d_21d_diff": {"inputs": ["volume"], "func": vtr_drv2_072_vol_rising_weeks_count_252d_21d_diff},
    "vtr_drv2_073_vol_trend_price_divergence_63d_21d_diff": {"inputs": ["close", "volume"], "func": vtr_drv2_073_vol_trend_price_divergence_63d_21d_diff},
    "vtr_drv2_074_vol_up_trend_price_down_flag_21d_5d_diff": {"inputs": ["close", "volume"], "func": vtr_drv2_074_vol_up_trend_price_down_flag_21d_5d_diff},
    "vtr_drv2_075_vol_ema21_vs_ema252_ratio_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vtr_drv2_075_vol_ema21_vs_ema252_ratio_zscore_252d_5d_diff},
}
