"""
113_volume_autocorrelation — 3rd Derivatives (Features vac_drv3_001-025)
Domain: rate of change of 2nd-derivative volume autocorrelation features — acceleration
        of serial-dependence structure changes in volume
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of series s at given lag over window w."""
    s_lag = s.shift(lag)
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).corr(s_lag)


def _log_volume(volume: pd.Series) -> pd.Series:
    return np.log(volume.clip(lower=_EPS))


def _volume_change(volume: pd.Series) -> pd.Series:
    return _log_volume(volume).diff(1)


def _hurst_rs(arr: np.ndarray) -> float:
    """R/S Hurst exponent estimate; NaN-safe."""
    arr = arr[~np.isnan(arr)]
    n = len(arr)
    if n < 8:
        return np.nan
    mean_v = arr.mean()
    deviations = np.cumsum(arr - mean_v)
    R = deviations.max() - deviations.min()
    S = arr.std(ddof=1)
    if S < _EPS or R < _EPS:
        return np.nan
    return np.log(R / S) / np.log(n)


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
# Each 3rd derivative = diff/slope applied to a 2nd-derivative concept.

def vac_drv3_001_logvol_ac1_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day lag-1 log-volume AC (acceleration of AC1 velocity)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_002_logvol_ac1_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day lag-1 log-volume AC (jerk in monthly AC change)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    vel21 = ac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vac_drv3_003_dvol_ac1_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day lag-1 volume-change AC (acceleration of dvol AC1)."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_004_vol_hurst_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Hurst exponent (acceleration of memory velocity)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    vel = h.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_005_vol_hurst_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day Hurst exponent (jerk in memory trend)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    vel21 = h.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vac_drv3_006_vol_vr5_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day variance ratio (acceleration of VR5 velocity)."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    vel = vr5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_007_logvol_ac5_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day lag-5 log-volume AC (acceleration of lag-5 velocity)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 5)
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_008_logvol_ac_sum5_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of lag-1-to-5 AC sum of log-volume (63d)."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    vel = total.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_009_vol_ac_composite_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day composite ACF score (lags 1-3 mean)."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    comp = (acs[0].fillna(0.0) + acs[1].fillna(0.0) + acs[2].fillna(0.0)) / 3.0
    vel = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_010_vol_mean_reversion_speed_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of mean-reversion speed (1 - rho_1, 63d window)."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    speed = 1.0 - rho
    vel = speed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_011_logvol_ac1_63d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 63-day lag-1 log-volume AC."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    slope = _linslope(ac, _TD_MON)
    return slope.diff(_TD_WEEK)


def vac_drv3_012_vol_hurst_63d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 63-day Hurst exponent."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    slope = _linslope(h, _TD_MON)
    return slope.diff(_TD_WEEK)


def vac_drv3_013_logvol_ac1_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day lag-1 log-volume AC (acceleration of short-window AC)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_014_dvol_pacf_lag2_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day lag-2 PACF of volume changes."""
    dv = _volume_change(volume)
    r1 = _rolling_autocorr(dv, _TD_QTR, 1)
    r2 = _rolling_autocorr(dv, _TD_QTR, 2)
    num = r2 - r1 * r1
    den = 1.0 - r1 * r1
    pacf2 = _safe_div(num, den.replace(0, np.nan))
    vel = pacf2.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_015_vol_clustering_ratio_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume clustering ratio (21d window)."""
    lv = _log_volume(volume)
    var_daily = _rolling_std(lv, _TD_MON) ** 2
    vol5 = _rolling_sum(lv, _TD_WEEK)
    var_5 = _rolling_std(vol5, _TD_MON) ** 2
    ratio = _safe_div(var_5, (5.0 * var_daily).replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_016_vol_persistence_frac_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of fraction of days volume above 63d mean in 21d window."""
    mu63 = _rolling_mean(volume, _TD_QTR)
    frac = _rolling_sum((volume > mu63).astype(float), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_017_logvol_ac1_63d_21d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of 63-day log-volume AC1."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    vel21 = ac.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def vac_drv3_018_vol_hurst_63d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63-day Hurst exponent."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    vel5 = h.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def vac_drv3_019_dvol_ac1_63d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63-day dvol AC1."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    vel = ac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vac_drv3_020_logvol_ac_sum5_63d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of lag-1-to-5 AC sum (63d)."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    vel = total.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vac_drv3_021_vol_vr5_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of the 5-day variance ratio."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    vel = vr5.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vac_drv3_022_logvol_ac1_63d_abs_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of absolute value of 63-day lag-1 AC (acceleration of AC magnitude)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1).abs()
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_023_vol_mean_reversion_speed_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in mean-reversion speed."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    speed = 1.0 - rho
    vel21 = speed.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vac_drv3_024_logvol_ac_abs_sum_lag1to3_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of sum of absolute ACFs at lags 1-3 log-volume (63d)."""
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 4):
        total = total + _rolling_autocorr(lv, _TD_QTR, lag).abs().fillna(0.0)
    vel = total.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vac_drv3_025_vol_vr21_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of the 21-day variance ratio."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_HALF) ** 2
    dv21 = _log_volume(volume).diff(21)
    var21 = _rolling_std(dv21, _TD_HALF) ** 2
    vr21 = _safe_div(var21, (21.0 * var1).replace(0, np.nan))
    vel21 = vr21.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AUTOCORRELATION_REGISTRY_3RD_DERIVATIVES = {
    "vac_drv3_001_logvol_ac1_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_001_logvol_ac1_63d_5d_diff_5d_diff},
    "vac_drv3_002_logvol_ac1_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_002_logvol_ac1_63d_21d_diff_5d_diff},
    "vac_drv3_003_dvol_ac1_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_003_dvol_ac1_63d_5d_diff_5d_diff},
    "vac_drv3_004_vol_hurst_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_004_vol_hurst_63d_5d_diff_5d_diff},
    "vac_drv3_005_vol_hurst_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_005_vol_hurst_63d_21d_diff_5d_diff},
    "vac_drv3_006_vol_vr5_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_006_vol_vr5_5d_diff_5d_diff},
    "vac_drv3_007_logvol_ac5_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_007_logvol_ac5_63d_5d_diff_5d_diff},
    "vac_drv3_008_logvol_ac_sum5_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_008_logvol_ac_sum5_63d_5d_diff_5d_diff},
    "vac_drv3_009_vol_ac_composite_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_009_vol_ac_composite_63d_5d_diff_5d_diff},
    "vac_drv3_010_vol_mean_reversion_speed_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_010_vol_mean_reversion_speed_5d_diff_5d_diff},
    "vac_drv3_011_logvol_ac1_63d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vac_drv3_011_logvol_ac1_63d_slope_21d_5d_diff},
    "vac_drv3_012_vol_hurst_63d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vac_drv3_012_vol_hurst_63d_slope_21d_5d_diff},
    "vac_drv3_013_logvol_ac1_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_013_logvol_ac1_21d_5d_diff_5d_diff},
    "vac_drv3_014_dvol_pacf_lag2_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_014_dvol_pacf_lag2_63d_5d_diff_5d_diff},
    "vac_drv3_015_vol_clustering_ratio_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_015_vol_clustering_ratio_5d_diff_5d_diff},
    "vac_drv3_016_vol_persistence_frac_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_016_vol_persistence_frac_5d_diff_5d_diff},
    "vac_drv3_017_logvol_ac1_63d_21d_diff_slope_21d": {"inputs": ["volume"], "func": vac_drv3_017_logvol_ac1_63d_21d_diff_slope_21d},
    "vac_drv3_018_vol_hurst_63d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vac_drv3_018_vol_hurst_63d_5d_diff_slope_21d},
    "vac_drv3_019_dvol_ac1_63d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vac_drv3_019_dvol_ac1_63d_5d_diff_slope_21d},
    "vac_drv3_020_logvol_ac_sum5_63d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vac_drv3_020_logvol_ac_sum5_63d_5d_diff_slope_21d},
    "vac_drv3_021_vol_vr5_5d_diff_slope_21d": {"inputs": ["volume"], "func": vac_drv3_021_vol_vr5_5d_diff_slope_21d},
    "vac_drv3_022_logvol_ac1_63d_abs_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_022_logvol_ac1_63d_abs_5d_diff_5d_diff},
    "vac_drv3_023_vol_mean_reversion_speed_21d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_023_vol_mean_reversion_speed_21d_diff_5d_diff},
    "vac_drv3_024_logvol_ac_abs_sum_lag1to3_5d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_024_logvol_ac_abs_sum_lag1to3_5d_diff_5d_diff},
    "vac_drv3_025_vol_vr21_21d_diff_5d_diff": {"inputs": ["volume"], "func": vac_drv3_025_vol_vr21_21d_diff_5d_diff},
}
