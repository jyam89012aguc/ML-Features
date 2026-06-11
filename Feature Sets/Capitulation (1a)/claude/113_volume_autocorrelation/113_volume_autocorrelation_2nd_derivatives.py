"""
113_volume_autocorrelation — 2nd Derivatives (Features vac_drv2_001-025)
Domain: rate of change of base volume autocorrelation features — velocity of serial-dependence
        structure changes in volume
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vac_drv2_001_logvol_ac1_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of rolling 63-day lag-1 log-volume autocorrelation (velocity of AC1 change)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.diff(_TD_WEEK)


def vac_drv2_002_logvol_ac1_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day lag-1 log-volume autocorrelation (monthly velocity)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.diff(_TD_MON)


def vac_drv2_003_dvol_ac1_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of rolling 63-day lag-1 volume-change autocorrelation."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    return ac.diff(_TD_WEEK)


def vac_drv2_004_logvol_ac5_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of rolling 63-day lag-5 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 5)
    return ac.diff(_TD_WEEK)


def vac_drv2_005_vol_hurst_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day Hurst exponent of log-volume (velocity of memory change)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    return h.diff(_TD_WEEK)


def vac_drv2_006_vol_hurst_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hurst exponent (monthly velocity of long-memory change)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    return h.diff(_TD_MON)


def vac_drv2_007_vol_vr5_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 5-day variance ratio of log-volume (velocity of persistence change)."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    return vr5.diff(_TD_WEEK)


def vac_drv2_008_vol_vr21_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the 21-day variance ratio of log-volume (monthly velocity)."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_HALF) ** 2
    dv21 = _log_volume(volume).diff(21)
    var21 = _rolling_std(dv21, _TD_HALF) ** 2
    vr21 = _safe_div(var21, (21.0 * var1).replace(0, np.nan))
    return vr21.diff(_TD_MON)


def vac_drv2_009_logvol_ac1_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of rolling 21-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    return ac.diff(_TD_WEEK)


def vac_drv2_010_logvol_ac_sum5_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the lag-1-to-5 autocorrelation sum of log-volume (63d)."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    return total.diff(_TD_WEEK)


def vac_drv2_011_vol_ac_composite_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day composite ACF score (lags 1-3 mean)."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    comp = (acs[0].fillna(0.0) + acs[1].fillna(0.0) + acs[2].fillna(0.0)) / 3.0
    return comp.diff(_TD_WEEK)


def vac_drv2_012_vol_mean_reversion_speed_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of mean-reversion speed (1 - rho_1) from 63-day window."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    speed = 1.0 - rho
    return speed.diff(_TD_WEEK)


def vac_drv2_013_vol_halflife_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume-shock half-life (velocity of persistence change)."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    rho_abs = rho.abs().clip(upper=1.0 - _EPS)
    ln_rho = np.log(rho_abs.clip(lower=_EPS))
    hl = _safe_div(pd.Series(-np.log(2.0), index=volume.index), ln_rho)
    return hl.diff(_TD_WEEK)


def vac_drv2_014_dvol_pacf_lag2_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day lag-2 PACF of log-volume changes."""
    dv = _volume_change(volume)
    r1 = _rolling_autocorr(dv, _TD_QTR, 1)
    r2 = _rolling_autocorr(dv, _TD_QTR, 2)
    num = r2 - r1 * r1
    den = 1.0 - r1 * r1
    pacf2 = _safe_div(num, den.replace(0, np.nan))
    return pacf2.diff(_TD_WEEK)


def vac_drv2_015_logvol_ac1_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day lag-1 log-volume autocorrelation (trend in AC)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return _linslope(ac, _TD_MON)


def vac_drv2_016_vol_hurst_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day Hurst exponent (trend in memory)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    return _linslope(h, _TD_MON)


def vac_drv2_017_logvol_ac_sign_flip_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of sign-flip count among lags 1-5 ACFs of log-volume (63d)."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 6)]
    flips = pd.Series(0.0, index=volume.index)
    for i in range(1, len(acs)):
        flips = flips + ((acs[i] * acs[i - 1]) < 0.0).astype(float).fillna(0.0)
    return flips.diff(_TD_WEEK)


def vac_drv2_018_vol_persistence_frac_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of fraction of days volume above 63d mean in trailing 21d window."""
    mu63 = _rolling_mean(volume, _TD_QTR)
    frac = _rolling_sum((volume > mu63).astype(float), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vac_drv2_019_vol_vr5_zscore_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of z-score of 5-day variance ratio vs 252-day distribution."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    m = _rolling_mean(vr, _TD_YEAR)
    s = _rolling_std(vr, _TD_YEAR)
    z = _safe_div(vr - m, s)
    return z.diff(_TD_WEEK)


def vac_drv2_020_logvol_ac1_63d_abs_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of absolute value of 63-day lag-1 log-volume ACF (velocity of AC magnitude)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1).abs()
    return ac.diff(_TD_WEEK)


def vac_drv2_021_dvol_ac1_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day lag-1 volume-change autocorrelation (monthly velocity)."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    return ac.diff(_TD_MON)


def vac_drv2_022_vol_clustering_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of volume clustering ratio (21d Var(5d sum) / 5*Var(daily))."""
    lv = _log_volume(volume)
    var_daily = _rolling_std(lv, _TD_MON) ** 2
    vol5 = _rolling_sum(lv, _TD_WEEK)
    var_5 = _rolling_std(vol5, _TD_MON) ** 2
    ratio = _safe_div(var_5, (5.0 * var_daily).replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def vac_drv2_023_logvol_ac1_63d_consec_positive_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive-positive-AC1 streak (AC1 build-up velocity)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    streak = _consec_streak(ac > 0.0)
    return streak.diff(_TD_WEEK)


def vac_drv2_024_vol_hurst_63d_pct_rank_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 63-day Hurst exponent within 252-day distribution."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    pr = h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pr.diff(_TD_WEEK)


def vac_drv2_025_logvol_ac_abs_sum_lag1to3_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of sum of absolute ACFs at lags 1-3 of log-volume (63d) — velocity of dependence magnitude."""
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 4):
        total = total + _rolling_autocorr(lv, _TD_QTR, lag).abs().fillna(0.0)
    return total.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AUTOCORRELATION_REGISTRY_2ND_DERIVATIVES = {
    "vac_drv2_001_logvol_ac1_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_001_logvol_ac1_63d_5d_diff},
    "vac_drv2_002_logvol_ac1_63d_21d_diff": {"inputs": ["volume"], "func": vac_drv2_002_logvol_ac1_63d_21d_diff},
    "vac_drv2_003_dvol_ac1_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_003_dvol_ac1_63d_5d_diff},
    "vac_drv2_004_logvol_ac5_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_004_logvol_ac5_63d_5d_diff},
    "vac_drv2_005_vol_hurst_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_005_vol_hurst_63d_5d_diff},
    "vac_drv2_006_vol_hurst_63d_21d_diff": {"inputs": ["volume"], "func": vac_drv2_006_vol_hurst_63d_21d_diff},
    "vac_drv2_007_vol_vr5_5d_diff": {"inputs": ["volume"], "func": vac_drv2_007_vol_vr5_5d_diff},
    "vac_drv2_008_vol_vr21_21d_diff": {"inputs": ["volume"], "func": vac_drv2_008_vol_vr21_21d_diff},
    "vac_drv2_009_logvol_ac1_21d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_009_logvol_ac1_21d_5d_diff},
    "vac_drv2_010_logvol_ac_sum5_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_010_logvol_ac_sum5_63d_5d_diff},
    "vac_drv2_011_vol_ac_composite_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_011_vol_ac_composite_63d_5d_diff},
    "vac_drv2_012_vol_mean_reversion_speed_5d_diff": {"inputs": ["volume"], "func": vac_drv2_012_vol_mean_reversion_speed_5d_diff},
    "vac_drv2_013_vol_halflife_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_013_vol_halflife_63d_5d_diff},
    "vac_drv2_014_dvol_pacf_lag2_63d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_014_dvol_pacf_lag2_63d_5d_diff},
    "vac_drv2_015_logvol_ac1_63d_slope_21d": {"inputs": ["volume"], "func": vac_drv2_015_logvol_ac1_63d_slope_21d},
    "vac_drv2_016_vol_hurst_63d_slope_21d": {"inputs": ["volume"], "func": vac_drv2_016_vol_hurst_63d_slope_21d},
    "vac_drv2_017_logvol_ac_sign_flip_5d_diff": {"inputs": ["volume"], "func": vac_drv2_017_logvol_ac_sign_flip_5d_diff},
    "vac_drv2_018_vol_persistence_frac_21d_5d_diff": {"inputs": ["volume"], "func": vac_drv2_018_vol_persistence_frac_21d_5d_diff},
    "vac_drv2_019_vol_vr5_zscore_5d_diff": {"inputs": ["volume"], "func": vac_drv2_019_vol_vr5_zscore_5d_diff},
    "vac_drv2_020_logvol_ac1_63d_abs_5d_diff": {"inputs": ["volume"], "func": vac_drv2_020_logvol_ac1_63d_abs_5d_diff},
    "vac_drv2_021_dvol_ac1_63d_21d_diff": {"inputs": ["volume"], "func": vac_drv2_021_dvol_ac1_63d_21d_diff},
    "vac_drv2_022_vol_clustering_ratio_5d_diff": {"inputs": ["volume"], "func": vac_drv2_022_vol_clustering_ratio_5d_diff},
    "vac_drv2_023_logvol_ac1_63d_consec_positive_5d_diff": {"inputs": ["volume"], "func": vac_drv2_023_logvol_ac1_63d_consec_positive_5d_diff},
    "vac_drv2_024_vol_hurst_63d_pct_rank_5d_diff": {"inputs": ["volume"], "func": vac_drv2_024_vol_hurst_63d_pct_rank_5d_diff},
    "vac_drv2_025_logvol_ac_abs_sum_lag1to3_5d_diff": {"inputs": ["volume"], "func": vac_drv2_025_logvol_ac_abs_sum_lag1to3_5d_diff},
}
