"""
24_volume_distribution — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative volume distribution features — acceleration of
        velocity in skew, kurtosis, CV, IQR, and tail-shape measures (inflection/exhaustion).
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vds_drv3_001_vol_skew_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume skew (acceleration of skew velocity)."""
    vel = _rolling_skew(volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_002_vol_skew_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21-day skew (jerk in monthly skew change)."""
    vel21 = _rolling_skew(volume, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_003_vol_kurt_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day kurtosis (acceleration of fat-tail change velocity)."""
    vel = _rolling_kurt(volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_004_vol_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CV (acceleration of dispersion velocity)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_005_vol_cv_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21-day CV."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_006_vol_iqr_norm_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized 21-day IQR (acceleration of IQR velocity)."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_n = _safe_div(q75 - q25, med)
    vel = iqr_n.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_007_vol_mean_median_ratio_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day mean/median ratio."""
    r = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_008_vol_skew_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day skew."""
    vel = _rolling_skew(volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vds_drv3_009_vol_kurt_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day kurtosis."""
    vel = _rolling_kurt(volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vds_drv3_010_vol_cv_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day CV."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vds_drv3_011_vol_skew_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day skew."""
    vel21 = _rolling_skew(volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_012_vol_kurt_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day kurtosis."""
    vel21 = _rolling_kurt(volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_013_vol_cv_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day CV."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_014_vol_90_10_spread_norm_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in normalized 90-10 spread over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    med = _rolling_median(volume, _TD_QTR)
    spread_n = _safe_div(q90 - q10, med)
    vel21 = spread_n.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_015_vol_skew_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day skew over 63 days (rate of slope change)."""
    slp = _linslope(_rolling_skew(volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_WEEK)


def vds_drv3_016_vol_kurt_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day kurtosis over 63 days."""
    slp = _linslope(_rolling_kurt(volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_WEEK)


def vds_drv3_017_vol_cv_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day CV over 63 days."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    slp = _linslope(cv, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vds_drv3_018_vol_log_std_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day log-volume std (acceleration of log-dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    vel = _rolling_std(lv, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_019_vol_ewm_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM-CV(21) (acceleration of exponentially weighted dispersion)."""
    cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_020_vol_tail_ratio_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Q90/Q50 tail ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    vel21 = _safe_div(q90, q50).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_021_vol_upper_lower_tail_ratio_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of tail-asymmetry ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    ratio = _safe_div(q90 - q50, q50 - q10)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vds_drv3_022_vol_shape_composite_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite shape score (acceleration of shape velocity)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    composite = (sk_z + k_z + cv_z) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vds_drv3_023_vol_skew_21d_21d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of 21-day skew."""
    vel21 = _rolling_skew(volume, _TD_MON).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def vds_drv3_024_vol_cv_21d_21d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of 21-day CV."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel21 = cv.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def vds_drv3_025_vol_mad_norm_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized MAD over 21 days (acceleration of robust dispersion)."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    mad_n = _safe_div(mad, m)
    vel = mad_n.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DISTRIBUTION_REGISTRY_3RD_DERIVATIVES = {
    "vds_drv3_001_vol_skew_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_001_vol_skew_21d_5d_diff_5d_diff},
    "vds_drv3_002_vol_skew_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_002_vol_skew_21d_21d_diff_5d_diff},
    "vds_drv3_003_vol_kurt_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_003_vol_kurt_21d_5d_diff_5d_diff},
    "vds_drv3_004_vol_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_004_vol_cv_21d_5d_diff_5d_diff},
    "vds_drv3_005_vol_cv_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_005_vol_cv_21d_21d_diff_5d_diff},
    "vds_drv3_006_vol_iqr_norm_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_006_vol_iqr_norm_21d_5d_diff_5d_diff},
    "vds_drv3_007_vol_mean_median_ratio_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_007_vol_mean_median_ratio_21d_5d_diff_5d_diff},
    "vds_drv3_008_vol_skew_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vds_drv3_008_vol_skew_21d_5d_diff_slope_21d},
    "vds_drv3_009_vol_kurt_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vds_drv3_009_vol_kurt_21d_5d_diff_slope_21d},
    "vds_drv3_010_vol_cv_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vds_drv3_010_vol_cv_21d_5d_diff_slope_21d},
    "vds_drv3_011_vol_skew_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_011_vol_skew_63d_21d_diff_5d_diff},
    "vds_drv3_012_vol_kurt_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_012_vol_kurt_63d_21d_diff_5d_diff},
    "vds_drv3_013_vol_cv_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_013_vol_cv_63d_21d_diff_5d_diff},
    "vds_drv3_014_vol_90_10_spread_norm_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_014_vol_90_10_spread_norm_63d_21d_diff_5d_diff},
    "vds_drv3_015_vol_skew_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vds_drv3_015_vol_skew_21d_slope_63d_5d_diff},
    "vds_drv3_016_vol_kurt_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vds_drv3_016_vol_kurt_21d_slope_63d_5d_diff},
    "vds_drv3_017_vol_cv_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vds_drv3_017_vol_cv_21d_slope_63d_5d_diff},
    "vds_drv3_018_vol_log_std_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_018_vol_log_std_21d_5d_diff_5d_diff},
    "vds_drv3_019_vol_ewm_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_019_vol_ewm_cv_21d_5d_diff_5d_diff},
    "vds_drv3_020_vol_tail_ratio_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_020_vol_tail_ratio_63d_21d_diff_5d_diff},
    "vds_drv3_021_vol_upper_lower_tail_ratio_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_021_vol_upper_lower_tail_ratio_63d_21d_diff_5d_diff},
    "vds_drv3_022_vol_shape_composite_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_022_vol_shape_composite_21d_5d_diff_5d_diff},
    "vds_drv3_023_vol_skew_21d_21d_diff_slope_21d": {"inputs": ["volume"], "func": vds_drv3_023_vol_skew_21d_21d_diff_slope_21d},
    "vds_drv3_024_vol_cv_21d_21d_diff_slope_21d": {"inputs": ["volume"], "func": vds_drv3_024_vol_cv_21d_21d_diff_slope_21d},
    "vds_drv3_025_vol_mad_norm_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vds_drv3_025_vol_mad_norm_21d_5d_diff_5d_diff},
}
