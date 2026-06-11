"""
19_volume_trend — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative volume-trend features — inflection / exhaustion
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vtr_drv3_001_vol_ols_slope_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume slope (acceleration of trend velocity)."""
    slope = _linslope(volume, _TD_MON)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_002_vol_ols_slope_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day volume slope."""
    slope = _linslope(volume, _TD_QTR)
    vel = slope.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vtr_drv3_003_logvol_slope_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day log-volume slope (log-trend acceleration)."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_004_logvol_slope_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    vel = slope.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vtr_drv3_005_vol_ema21_vs_ema63_ratio_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21/EMA63 volume ratio (jerk in EMA crossover speed)."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_006_vol_rising_days_frac_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day rising-volume-day fraction."""
    frac = (volume > volume.shift(1)).astype(float)
    frac21 = _rolling_mean(frac, _TD_MON)
    vel = frac21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_007_vol_trend_consistency_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume trend consistency score."""
    sign_chg = np.sign(volume - volume.shift(1))
    consistency = sign_chg.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum().abs() / _TD_MON
    vel = consistency.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_008_vol_net_drift_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume net drift (jerk in drift momentum)."""
    drift = _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON).clip(lower=_EPS))
    vel = drift.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_009_vol_ema_crossover_score_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA crossover alignment score."""
    s1 = (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)).astype(float)
    s2 = (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)).astype(float)
    s3 = (_ewm_mean(volume, _TD_QTR) > _ewm_mean(volume, _TD_YEAR)).astype(float)
    score = s1 + s2 + s3
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_010_vol_21d_return_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume return (acceleration of return velocity)."""
    ret = volume.pct_change(_TD_MON)
    vel = ret.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_011_logvol_21d_change_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day log-volume change."""
    chg = _log_safe(volume) - _log_safe(volume).shift(_TD_MON)
    vel = chg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_012_vol_rsq_21d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day volume R-squared (rate of R-sq trend change)."""
    rsq = _linslope_rsq(volume, _TD_MON)
    slope_rsq = _linslope(rsq, _TD_MON)
    return slope_rsq.diff(_TD_WEEK)


def vtr_drv3_013_logvol_rsq_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day log-volume R-squared."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_QTR)
    vel21 = rsq.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vtr_drv3_014_vol_sma21_vs_sma63_ratio_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in SMA21/SMA63 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vtr_drv3_015_vol_ema21_slope_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day slope of EMA21 volume."""
    ema21 = _ewm_mean(volume, _TD_MON)
    slope = _linslope(ema21, _TD_MON)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_016_vol_slope_21d_norm_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope over 63d of normalized 21d volume slope."""
    slope_norm = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    slope_of_slope = _linslope(slope_norm, _TD_QTR)
    return slope_of_slope.diff(_TD_WEEK)


def vtr_drv3_017_logvol_slope_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope over 63d of 21-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    slope_of_slope = _linslope(slope, _TD_QTR)
    return slope_of_slope.diff(_TD_WEEK)


def vtr_drv3_018_vol_trend_regime_score_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume trend regime score (count of positive slopes)."""
    s = [(_linslope(volume, w) > 0).astype(float)
         for w in [_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR]]
    score = s[0] + s[1] + s[2] + s[3]
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_019_vol_sma21_vs_sma252_ratio_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in SMA21/SMA252 volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vtr_drv3_020_vol_logslope_21d_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 21-day log-volume slope."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    z = _safe_div(slope - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vtr_drv3_021_vol_rising_weeks_frac_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day rising-volume-week fraction."""
    frac = (volume.pct_change(_TD_WEEK) > 0).astype(float)
    frac63 = _rolling_mean(frac, _TD_QTR)
    vel21 = frac63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vtr_drv3_022_vol_net_drift_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day volume net drift."""
    drift = _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).clip(lower=_EPS))
    vel21 = drift.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vtr_drv3_023_logvol_slope_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope over 21d of 21-day log-volume slope (curvature)."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    slope_of_slope = _linslope(slope, _TD_MON)
    return slope_of_slope.diff(_TD_WEEK)


def vtr_drv3_024_vol_ema21_5d_change_norm_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of normalized 5-day change in EMA21 volume."""
    ema21 = _ewm_mean(volume, _TD_MON)
    chg_norm = _safe_div(ema21 - ema21.shift(_TD_WEEK), ema21.shift(_TD_WEEK).clip(lower=_EPS))
    return chg_norm.diff(_TD_WEEK)


def vtr_drv3_025_vol_trend_price_divergence_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume-vs-price slope sign divergence."""
    vs = np.sign(_linslope(volume, _TD_MON))
    ps = np.sign(_linslope(close, _TD_MON))
    divergence = vs - ps
    vel = divergence.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_TREND_REGISTRY_3RD_DERIVATIVES = {
    "vtr_drv3_001_vol_ols_slope_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_001_vol_ols_slope_21d_5d_diff_5d_diff},
    "vtr_drv3_002_vol_ols_slope_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_002_vol_ols_slope_63d_21d_diff_5d_diff},
    "vtr_drv3_003_logvol_slope_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_003_logvol_slope_21d_5d_diff_5d_diff},
    "vtr_drv3_004_logvol_slope_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_004_logvol_slope_63d_21d_diff_5d_diff},
    "vtr_drv3_005_vol_ema21_vs_ema63_ratio_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_005_vol_ema21_vs_ema63_ratio_5d_diff_5d_diff},
    "vtr_drv3_006_vol_rising_days_frac_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_006_vol_rising_days_frac_21d_5d_diff_5d_diff},
    "vtr_drv3_007_vol_trend_consistency_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_007_vol_trend_consistency_21d_5d_diff_5d_diff},
    "vtr_drv3_008_vol_net_drift_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_008_vol_net_drift_21d_5d_diff_5d_diff},
    "vtr_drv3_009_vol_ema_crossover_score_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_009_vol_ema_crossover_score_5d_diff_5d_diff},
    "vtr_drv3_010_vol_21d_return_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_010_vol_21d_return_5d_diff_5d_diff},
    "vtr_drv3_011_logvol_21d_change_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_011_logvol_21d_change_5d_diff_5d_diff},
    "vtr_drv3_012_vol_rsq_21d_slope_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_012_vol_rsq_21d_slope_5d_diff},
    "vtr_drv3_013_logvol_rsq_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_013_logvol_rsq_63d_21d_diff_5d_diff},
    "vtr_drv3_014_vol_sma21_vs_sma63_ratio_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_014_vol_sma21_vs_sma63_ratio_21d_diff_5d_diff},
    "vtr_drv3_015_vol_ema21_slope_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_015_vol_ema21_slope_21d_5d_diff_5d_diff},
    "vtr_drv3_016_vol_slope_21d_norm_slope_63d_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_016_vol_slope_21d_norm_slope_63d_5d_diff},
    "vtr_drv3_017_logvol_slope_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_017_logvol_slope_21d_slope_63d_5d_diff},
    "vtr_drv3_018_vol_trend_regime_score_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_018_vol_trend_regime_score_5d_diff_5d_diff},
    "vtr_drv3_019_vol_sma21_vs_sma252_ratio_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_019_vol_sma21_vs_sma252_ratio_21d_diff_5d_diff},
    "vtr_drv3_020_vol_logslope_21d_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_020_vol_logslope_21d_zscore_252d_5d_diff_5d_diff},
    "vtr_drv3_021_vol_rising_weeks_frac_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_021_vol_rising_weeks_frac_63d_21d_diff_5d_diff},
    "vtr_drv3_022_vol_net_drift_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_022_vol_net_drift_63d_21d_diff_5d_diff},
    "vtr_drv3_023_logvol_slope_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_023_logvol_slope_21d_slope_21d_5d_diff},
    "vtr_drv3_024_vol_ema21_5d_change_norm_5d_diff": {"inputs": ["volume"], "func": vtr_drv3_024_vol_ema21_5d_change_norm_5d_diff},
    "vtr_drv3_025_vol_trend_price_divergence_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vtr_drv3_025_vol_trend_price_divergence_21d_5d_diff_5d_diff},
}
