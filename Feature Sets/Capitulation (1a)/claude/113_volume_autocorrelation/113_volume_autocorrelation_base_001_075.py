"""
113_volume_autocorrelation — Base Features 001-075
Domain: serial dependence / memory structure of volume — autocorrelation of volume
        and volume changes at multiple lags, volume clustering, volume persistence,
        partial autocorrelation, variance ratios, runs structure, long memory
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of series s at given lag over window w.
    NaN-safe: uses pandas rolling correlation between s and s.shift(lag).
    """
    s_lag = s.shift(lag)
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).corr(s_lag)


def _rolling_autocorr_nanmean(arr: np.ndarray, lag: int) -> float:
    """Pearson autocorrelation at given lag; NaN-safe helper for apply."""
    arr = arr[~np.isnan(arr)]
    n = len(arr)
    if n <= lag + 1:
        return np.nan
    x = arr[:-lag]
    y = arr[lag:]
    xm = x.mean()
    ym = y.mean()
    num = ((x - xm) * (y - ym)).sum()
    den = np.sqrt(((x - xm) ** 2).sum() * ((y - ym) ** 2).sum())
    if den < _EPS:
        return np.nan
    return num / den


def _log_volume(volume: pd.Series) -> pd.Series:
    """Natural log of volume; clips to EPS before log to avoid -inf."""
    return np.log(volume.clip(lower=_EPS))


def _volume_change(volume: pd.Series) -> pd.Series:
    """Day-over-day log change of volume."""
    return _log_volume(volume).diff(1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Raw rolling autocorrelation of log-volume at multiple lags ---

def vac_001_logvol_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume at lag 1."""
    return _rolling_autocorr(_log_volume(volume), _TD_MON, 1)


def vac_002_logvol_autocorr_lag2_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume at lag 2."""
    return _rolling_autocorr(_log_volume(volume), _TD_MON, 2)


def vac_003_logvol_autocorr_lag3_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume at lag 3."""
    return _rolling_autocorr(_log_volume(volume), _TD_MON, 3)


def vac_004_logvol_autocorr_lag5_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume at lag 5 (weekly)."""
    return _rolling_autocorr(_log_volume(volume), _TD_MON, 5)


def vac_005_logvol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 1."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)


def vac_006_logvol_autocorr_lag2_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 2."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 2)


def vac_007_logvol_autocorr_lag3_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 3."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 3)


def vac_008_logvol_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 5."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 5)


def vac_009_logvol_autocorr_lag10_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 10 (two-week)."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 10)


def vac_010_logvol_autocorr_lag1_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume at lag 1."""
    return _rolling_autocorr(_log_volume(volume), _TD_HALF, 1)


def vac_011_logvol_autocorr_lag5_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume at lag 5."""
    return _rolling_autocorr(_log_volume(volume), _TD_HALF, 5)


def vac_012_logvol_autocorr_lag21_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume at lag 21 (monthly)."""
    return _rolling_autocorr(_log_volume(volume), _TD_HALF, 21)


def vac_013_logvol_autocorr_lag1_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 1."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 1)


def vac_014_logvol_autocorr_lag5_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 5."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 5)


def vac_015_logvol_autocorr_lag21_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 21."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 21)


# --- Group B (016-030): Autocorrelation of log-volume changes (first differences) ---

def vac_016_dvol_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume changes at lag 1."""
    return _rolling_autocorr(_volume_change(volume), _TD_MON, 1)


def vac_017_dvol_autocorr_lag2_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume changes at lag 2."""
    return _rolling_autocorr(_volume_change(volume), _TD_MON, 2)


def vac_018_dvol_autocorr_lag3_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume changes at lag 3."""
    return _rolling_autocorr(_volume_change(volume), _TD_MON, 3)


def vac_019_dvol_autocorr_lag5_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of log-volume changes at lag 5."""
    return _rolling_autocorr(_volume_change(volume), _TD_MON, 5)


def vac_020_dvol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 1."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)


def vac_021_dvol_autocorr_lag2_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 2."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 2)


def vac_022_dvol_autocorr_lag3_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 3."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 3)


def vac_023_dvol_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 5."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 5)


def vac_024_dvol_autocorr_lag10_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 10."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 10)


def vac_025_dvol_autocorr_lag1_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume changes at lag 1."""
    return _rolling_autocorr(_volume_change(volume), _TD_HALF, 1)


def vac_026_dvol_autocorr_lag5_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume changes at lag 5."""
    return _rolling_autocorr(_volume_change(volume), _TD_HALF, 5)


def vac_027_dvol_autocorr_lag21_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of log-volume changes at lag 21."""
    return _rolling_autocorr(_volume_change(volume), _TD_HALF, 21)


def vac_028_dvol_autocorr_lag1_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume changes at lag 1."""
    return _rolling_autocorr(_volume_change(volume), _TD_YEAR, 1)


def vac_029_dvol_autocorr_lag5_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume changes at lag 5."""
    return _rolling_autocorr(_volume_change(volume), _TD_YEAR, 5)


def vac_030_dvol_autocorr_lag21_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume changes at lag 21."""
    return _rolling_autocorr(_volume_change(volume), _TD_YEAR, 21)


# --- Group C (031-040): Volume clustering — squared deviations autocorrelation ---

def vac_031_vol_sq_dev_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of squared log-volume deviations at lag 1 (GARCH-style clustering)."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_MON)) ** 2
    return _rolling_autocorr(dev, _TD_MON, 1)


def vac_032_vol_sq_dev_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of squared log-volume deviations at lag 1."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_QTR)) ** 2
    return _rolling_autocorr(dev, _TD_QTR, 1)


def vac_033_vol_sq_dev_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of squared log-volume deviations at lag 5."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_QTR)) ** 2
    return _rolling_autocorr(dev, _TD_QTR, 5)


def vac_034_vol_abs_dev_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of absolute log-volume deviations at lag 1."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_MON)).abs()
    return _rolling_autocorr(dev, _TD_MON, 1)


def vac_035_vol_abs_dev_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of absolute log-volume deviations at lag 1."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_QTR)).abs()
    return _rolling_autocorr(dev, _TD_QTR, 1)


def vac_036_vol_sq_dev_autocorr_lag1_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of squared log-volume deviations at lag 1."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_HALF)) ** 2
    return _rolling_autocorr(dev, _TD_HALF, 1)


def vac_037_vol_sq_dev_autocorr_lag2_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of squared log-volume deviations at lag 2."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_QTR)) ** 2
    return _rolling_autocorr(dev, _TD_QTR, 2)


def vac_038_vol_abs_dev_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of absolute log-volume deviations at lag 5."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_QTR)).abs()
    return _rolling_autocorr(dev, _TD_QTR, 5)


def vac_039_vol_sq_dev_autocorr_lag5_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of squared log-volume deviations at lag 5."""
    lv = _log_volume(volume)
    dev = (lv - _rolling_mean(lv, _TD_HALF)) ** 2
    return _rolling_autocorr(dev, _TD_HALF, 5)


def vac_040_vol_clustering_ratio_21d(volume: pd.Series) -> pd.Series:
    """Volume clustering ratio: variance of 5-day volume sums / (5 * daily variance), 21d window.
    Ratio > 1 implies clustering; < 1 implies mean-reversion.
    """
    lv = _log_volume(volume)
    var_daily = _rolling_std(lv, _TD_MON) ** 2
    vol5 = _rolling_sum(lv, _TD_WEEK)
    var_5 = _rolling_std(vol5, _TD_MON) ** 2
    return _safe_div(var_5, (5.0 * var_daily).replace(0, np.nan))


# --- Group D (041-050): Variance ratio tests of volume ---

def vac_041_vol_variance_ratio_5_1(volume: pd.Series) -> pd.Series:
    """Variance ratio: Var(5-day log-vol change) / (5 * Var(1-day log-vol change)), 63d window.
    Value > 1 = positive autocorrelation (persistence); < 1 = negative autocorrelation (mean-reversion).
    """
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    return _safe_div(var5, (5.0 * var1).replace(0, np.nan))


def vac_042_vol_variance_ratio_21_1(volume: pd.Series) -> pd.Series:
    """Variance ratio: Var(21-day log-vol change) / (21 * Var(1-day log-vol change)), 126d window."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_HALF) ** 2
    dv21 = _log_volume(volume).diff(21)
    var21 = _rolling_std(dv21, _TD_HALF) ** 2
    return _safe_div(var21, (21.0 * var1).replace(0, np.nan))


def vac_043_vol_variance_ratio_63_1(volume: pd.Series) -> pd.Series:
    """Variance ratio: Var(63-day log-vol change) / (63 * Var(1-day log-vol change)), 252d window."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_YEAR) ** 2
    dv63 = _log_volume(volume).diff(63)
    var63 = _rolling_std(dv63, _TD_YEAR) ** 2
    return _safe_div(var63, (63.0 * var1).replace(0, np.nan))


def vac_044_vol_variance_ratio_10_1(volume: pd.Series) -> pd.Series:
    """Variance ratio: Var(10-day log-vol change) / (10 * Var(1-day)), 63d window."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv10 = _log_volume(volume).diff(10)
    var10 = _rolling_std(dv10, _TD_QTR) ** 2
    return _safe_div(var10, (10.0 * var1).replace(0, np.nan))


def vac_045_vol_variance_ratio_5_1_126d(volume: pd.Series) -> pd.Series:
    """Variance ratio (5-day/1-day) computed over 126-day rolling window."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_HALF) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_HALF) ** 2
    return _safe_div(var5, (5.0 * var1).replace(0, np.nan))


def vac_046_vol_vr5_minus1_abs(volume: pd.Series) -> pd.Series:
    """Absolute deviation of 5-day/1-day variance ratio from 1 (distance from random walk)."""
    vr = vac_041_vol_variance_ratio_5_1(volume)
    return (vr - 1.0).abs()


def vac_047_vol_vr21_minus1_abs(volume: pd.Series) -> pd.Series:
    """Absolute deviation of 21-day/1-day variance ratio from 1."""
    vr = vac_042_vol_variance_ratio_21_1(volume)
    return (vr - 1.0).abs()


def vac_048_vol_vr5_sign(volume: pd.Series) -> pd.Series:
    """Sign of (VR5 - 1): +1 = persistent volume, -1 = mean-reverting volume, 63d."""
    vr = vac_041_vol_variance_ratio_5_1(volume)
    return np.sign(vr - 1.0).astype(float)


def vac_049_vol_vr21_sign(volume: pd.Series) -> pd.Series:
    """Sign of (VR21 - 1): +1 = persistent volume, -1 = mean-reverting volume, 126d."""
    vr = vac_042_vol_variance_ratio_21_1(volume)
    return np.sign(vr - 1.0).astype(float)


def vac_050_vol_vr5_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 5-day variance ratio within trailing 252-day distribution."""
    vr = vac_041_vol_variance_ratio_5_1(volume)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (051-060): Volume persistence / half-life ---

def vac_051_vol_halflife_21d(volume: pd.Series) -> pd.Series:
    """Half-life of volume shocks estimated via lag-1 autocorrelation over 21-day window.
    half_life = -ln(2) / ln(|rho|); returns NaN when |rho| >= 1 or <= 0.
    """
    rho = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    rho_abs = rho.abs().clip(upper=1.0 - _EPS)
    ln_rho = np.log(rho_abs.clip(lower=_EPS))
    return _safe_div(pd.Series(-np.log(2.0), index=volume.index), ln_rho)


def vac_052_vol_halflife_63d(volume: pd.Series) -> pd.Series:
    """Half-life of volume shocks estimated via lag-1 autocorrelation over 63-day window."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    rho_abs = rho.abs().clip(upper=1.0 - _EPS)
    ln_rho = np.log(rho_abs.clip(lower=_EPS))
    return _safe_div(pd.Series(-np.log(2.0), index=volume.index), ln_rho)


def vac_053_vol_halflife_126d(volume: pd.Series) -> pd.Series:
    """Half-life of volume shocks estimated via lag-1 autocorrelation over 126-day window."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_HALF, 1)
    rho_abs = rho.abs().clip(upper=1.0 - _EPS)
    ln_rho = np.log(rho_abs.clip(lower=_EPS))
    return _safe_div(pd.Series(-np.log(2.0), index=volume.index), ln_rho)


def vac_054_vol_ewm_decay_5d(volume: pd.Series) -> pd.Series:
    """EWM-smoothed log-volume (span=5) normalized by rolling mean — smoothed persistence signal."""
    lv = _log_volume(volume)
    ema5 = _ewm_mean(lv, _TD_WEEK)
    mu = _rolling_mean(lv, _TD_MON)
    return _safe_div(ema5 - mu, _rolling_std(lv, _TD_MON).replace(0, np.nan))


def vac_055_vol_ewm_decay_21d(volume: pd.Series) -> pd.Series:
    """EWM-smoothed log-volume (span=21) normalized by 63-day rolling mean."""
    lv = _log_volume(volume)
    ema21 = _ewm_mean(lv, _TD_MON)
    mu = _rolling_mean(lv, _TD_QTR)
    return _safe_div(ema21 - mu, _rolling_std(lv, _TD_QTR).replace(0, np.nan))


def vac_056_vol_autocorr_decay_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of lag-2 to lag-1 autocorrelation of log-volume (63d); measures geometric decay speed."""
    rho1 = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    rho2 = _rolling_autocorr(_log_volume(volume), _TD_QTR, 2)
    return _safe_div(rho2, rho1.replace(0, np.nan))


def vac_057_vol_autocorr_sum_lag1to5_63d(volume: pd.Series) -> pd.Series:
    """Sum of lag-1 through lag-5 autocorrelations of log-volume over 63 days (persistence score)."""
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0)
    return total


def vac_058_vol_autocorr_sum_lag1to5_126d(volume: pd.Series) -> pd.Series:
    """Sum of lag-1 through lag-5 autocorrelations of log-volume over 126 days."""
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(lv, _TD_HALF, lag).fillna(0.0)
    return total


def vac_059_vol_persistence_above_avg_21d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 21d where volume is above its 63d rolling mean (persistence of elevated volume)."""
    mu63 = _rolling_mean(volume, _TD_QTR)
    above = (volume > mu63).astype(float)
    return _rolling_sum(above, _TD_MON) / _TD_MON


def vac_060_vol_persistence_above_avg_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63d where volume is above its 252d rolling mean."""
    mu252 = _rolling_mean(volume, _TD_YEAR)
    above = (volume > mu252).astype(float)
    return _rolling_sum(above, _TD_QTR) / _TD_QTR


# --- Group F (061-075): Runs structure of high-volume days ---

def vac_061_high_vol_run_consec_21d(volume: pd.Series) -> pd.Series:
    """Consecutive days volume is above 63d rolling mean (current run length)."""
    mu = _rolling_mean(volume, _TD_QTR)
    return _consec_streak(volume > mu)


def vac_062_high_vol_run_consec_252d(volume: pd.Series) -> pd.Series:
    """Consecutive days volume is above 252d rolling mean."""
    mu = _rolling_mean(volume, _TD_YEAR)
    return _consec_streak(volume > mu)


def vac_063_high_vol_runs_count_63d(volume: pd.Series) -> pd.Series:
    """Count of distinct high-volume run starts (cross above 63d mean) in trailing 63 days."""
    mu = _rolling_mean(volume, _TD_QTR)
    entry = ((volume > mu) & (volume.shift(1) <= mu)).astype(float)
    return _rolling_sum(entry, _TD_QTR)


def vac_064_high_vol_runs_count_252d(volume: pd.Series) -> pd.Series:
    """Count of distinct high-volume run starts in trailing 252 days."""
    mu = _rolling_mean(volume, _TD_YEAR)
    entry = ((volume > mu) & (volume.shift(1) <= mu)).astype(float)
    return _rolling_sum(entry, _TD_YEAR)


def vac_065_vol_runs_above_2x_mean_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume exceeded 2x its 63d mean."""
    mu = _rolling_mean(volume, _TD_QTR)
    flag = (volume > 2.0 * mu).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vac_066_vol_runs_above_2x_mean_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume exceeded 2x its 252d mean."""
    mu = _rolling_mean(volume, _TD_YEAR)
    flag = (volume > 2.0 * mu).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def vac_067_low_vol_consec_streak(volume: pd.Series) -> pd.Series:
    """Consecutive days volume is below its 63d rolling mean (low-volume run length)."""
    mu = _rolling_mean(volume, _TD_QTR)
    return _consec_streak(volume < mu)


def vac_068_vol_runs_alternation_rate_63d(volume: pd.Series) -> pd.Series:
    """Fraction of consecutive pairs (t, t-1) where volume switches above/below 63d mean in 63d window.
    High value = frequent alternation (mean-reverting); low = persistent runs.
    """
    mu = _rolling_mean(volume, _TD_QTR)
    above = (volume > mu).astype(float)
    flip = (above != above.shift(1)).astype(float)
    return _rolling_sum(flip, _TD_QTR) / (_TD_QTR - 1)


def vac_069_vol_runs_alternation_rate_252d(volume: pd.Series) -> pd.Series:
    """Fraction of consecutive pairs where volume switches above/below 252d mean in 252d window."""
    mu = _rolling_mean(volume, _TD_YEAR)
    above = (volume > mu).astype(float)
    flip = (above != above.shift(1)).astype(float)
    return _rolling_sum(flip, _TD_YEAR) / (_TD_YEAR - 1)


def vac_070_max_high_vol_run_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive high-volume run length within trailing 63 days."""
    mu = _rolling_mean(volume, _TD_QTR)
    above = (volume > mu)

    def _max_run(arr):
        arr = arr[~np.isnan(arr)]
        mx, cur = 0, 0
        for v in arr:
            if v > 0.5:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return above.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def vac_071_max_high_vol_run_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive high-volume run length within trailing 252 days."""
    mu = _rolling_mean(volume, _TD_YEAR)
    above = (volume > mu)

    def _max_run(arr):
        arr = arr[~np.isnan(arr)]
        mx, cur = 0, 0
        for v in arr:
            if v > 0.5:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return above.astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def vac_072_vol_sign_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Autocorrelation of binary high/low volume sign (above/below 63d mean) at lag 1, 63d window."""
    mu = _rolling_mean(volume, _TD_QTR)
    sign = (volume > mu).astype(float) * 2.0 - 1.0
    return _rolling_autocorr(sign, _TD_QTR, 1)


def vac_073_vol_sign_autocorr_lag1_252d(volume: pd.Series) -> pd.Series:
    """Autocorrelation of binary high/low volume sign at lag 1, 252d window."""
    mu = _rolling_mean(volume, _TD_YEAR)
    sign = (volume > mu).astype(float) * 2.0 - 1.0
    return _rolling_autocorr(sign, _TD_YEAR, 1)


def vac_074_vol_sign_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Autocorrelation of binary volume sign at lag 5, 63d window."""
    mu = _rolling_mean(volume, _TD_QTR)
    sign = (volume > mu).astype(float) * 2.0 - 1.0
    return _rolling_autocorr(sign, _TD_QTR, 5)


def vac_075_vol_runlength_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current high-volume run length within trailing 252-day distribution."""
    run = vac_061_high_vol_run_consec_21d(volume)
    return run.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AUTOCORRELATION_REGISTRY_001_075 = {
    "vac_001_logvol_autocorr_lag1_21d": {"inputs": ["volume"], "func": vac_001_logvol_autocorr_lag1_21d},
    "vac_002_logvol_autocorr_lag2_21d": {"inputs": ["volume"], "func": vac_002_logvol_autocorr_lag2_21d},
    "vac_003_logvol_autocorr_lag3_21d": {"inputs": ["volume"], "func": vac_003_logvol_autocorr_lag3_21d},
    "vac_004_logvol_autocorr_lag5_21d": {"inputs": ["volume"], "func": vac_004_logvol_autocorr_lag5_21d},
    "vac_005_logvol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_005_logvol_autocorr_lag1_63d},
    "vac_006_logvol_autocorr_lag2_63d": {"inputs": ["volume"], "func": vac_006_logvol_autocorr_lag2_63d},
    "vac_007_logvol_autocorr_lag3_63d": {"inputs": ["volume"], "func": vac_007_logvol_autocorr_lag3_63d},
    "vac_008_logvol_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_008_logvol_autocorr_lag5_63d},
    "vac_009_logvol_autocorr_lag10_63d": {"inputs": ["volume"], "func": vac_009_logvol_autocorr_lag10_63d},
    "vac_010_logvol_autocorr_lag1_126d": {"inputs": ["volume"], "func": vac_010_logvol_autocorr_lag1_126d},
    "vac_011_logvol_autocorr_lag5_126d": {"inputs": ["volume"], "func": vac_011_logvol_autocorr_lag5_126d},
    "vac_012_logvol_autocorr_lag21_126d": {"inputs": ["volume"], "func": vac_012_logvol_autocorr_lag21_126d},
    "vac_013_logvol_autocorr_lag1_252d": {"inputs": ["volume"], "func": vac_013_logvol_autocorr_lag1_252d},
    "vac_014_logvol_autocorr_lag5_252d": {"inputs": ["volume"], "func": vac_014_logvol_autocorr_lag5_252d},
    "vac_015_logvol_autocorr_lag21_252d": {"inputs": ["volume"], "func": vac_015_logvol_autocorr_lag21_252d},
    "vac_016_dvol_autocorr_lag1_21d": {"inputs": ["volume"], "func": vac_016_dvol_autocorr_lag1_21d},
    "vac_017_dvol_autocorr_lag2_21d": {"inputs": ["volume"], "func": vac_017_dvol_autocorr_lag2_21d},
    "vac_018_dvol_autocorr_lag3_21d": {"inputs": ["volume"], "func": vac_018_dvol_autocorr_lag3_21d},
    "vac_019_dvol_autocorr_lag5_21d": {"inputs": ["volume"], "func": vac_019_dvol_autocorr_lag5_21d},
    "vac_020_dvol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_020_dvol_autocorr_lag1_63d},
    "vac_021_dvol_autocorr_lag2_63d": {"inputs": ["volume"], "func": vac_021_dvol_autocorr_lag2_63d},
    "vac_022_dvol_autocorr_lag3_63d": {"inputs": ["volume"], "func": vac_022_dvol_autocorr_lag3_63d},
    "vac_023_dvol_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_023_dvol_autocorr_lag5_63d},
    "vac_024_dvol_autocorr_lag10_63d": {"inputs": ["volume"], "func": vac_024_dvol_autocorr_lag10_63d},
    "vac_025_dvol_autocorr_lag1_126d": {"inputs": ["volume"], "func": vac_025_dvol_autocorr_lag1_126d},
    "vac_026_dvol_autocorr_lag5_126d": {"inputs": ["volume"], "func": vac_026_dvol_autocorr_lag5_126d},
    "vac_027_dvol_autocorr_lag21_126d": {"inputs": ["volume"], "func": vac_027_dvol_autocorr_lag21_126d},
    "vac_028_dvol_autocorr_lag1_252d": {"inputs": ["volume"], "func": vac_028_dvol_autocorr_lag1_252d},
    "vac_029_dvol_autocorr_lag5_252d": {"inputs": ["volume"], "func": vac_029_dvol_autocorr_lag5_252d},
    "vac_030_dvol_autocorr_lag21_252d": {"inputs": ["volume"], "func": vac_030_dvol_autocorr_lag21_252d},
    "vac_031_vol_sq_dev_autocorr_lag1_21d": {"inputs": ["volume"], "func": vac_031_vol_sq_dev_autocorr_lag1_21d},
    "vac_032_vol_sq_dev_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_032_vol_sq_dev_autocorr_lag1_63d},
    "vac_033_vol_sq_dev_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_033_vol_sq_dev_autocorr_lag5_63d},
    "vac_034_vol_abs_dev_autocorr_lag1_21d": {"inputs": ["volume"], "func": vac_034_vol_abs_dev_autocorr_lag1_21d},
    "vac_035_vol_abs_dev_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_035_vol_abs_dev_autocorr_lag1_63d},
    "vac_036_vol_sq_dev_autocorr_lag1_126d": {"inputs": ["volume"], "func": vac_036_vol_sq_dev_autocorr_lag1_126d},
    "vac_037_vol_sq_dev_autocorr_lag2_63d": {"inputs": ["volume"], "func": vac_037_vol_sq_dev_autocorr_lag2_63d},
    "vac_038_vol_abs_dev_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_038_vol_abs_dev_autocorr_lag5_63d},
    "vac_039_vol_sq_dev_autocorr_lag5_126d": {"inputs": ["volume"], "func": vac_039_vol_sq_dev_autocorr_lag5_126d},
    "vac_040_vol_clustering_ratio_21d": {"inputs": ["volume"], "func": vac_040_vol_clustering_ratio_21d},
    "vac_041_vol_variance_ratio_5_1": {"inputs": ["volume"], "func": vac_041_vol_variance_ratio_5_1},
    "vac_042_vol_variance_ratio_21_1": {"inputs": ["volume"], "func": vac_042_vol_variance_ratio_21_1},
    "vac_043_vol_variance_ratio_63_1": {"inputs": ["volume"], "func": vac_043_vol_variance_ratio_63_1},
    "vac_044_vol_variance_ratio_10_1": {"inputs": ["volume"], "func": vac_044_vol_variance_ratio_10_1},
    "vac_045_vol_variance_ratio_5_1_126d": {"inputs": ["volume"], "func": vac_045_vol_variance_ratio_5_1_126d},
    "vac_046_vol_vr5_minus1_abs": {"inputs": ["volume"], "func": vac_046_vol_vr5_minus1_abs},
    "vac_047_vol_vr21_minus1_abs": {"inputs": ["volume"], "func": vac_047_vol_vr21_minus1_abs},
    "vac_048_vol_vr5_sign": {"inputs": ["volume"], "func": vac_048_vol_vr5_sign},
    "vac_049_vol_vr21_sign": {"inputs": ["volume"], "func": vac_049_vol_vr21_sign},
    "vac_050_vol_vr5_pct_rank_252d": {"inputs": ["volume"], "func": vac_050_vol_vr5_pct_rank_252d},
    "vac_051_vol_halflife_21d": {"inputs": ["volume"], "func": vac_051_vol_halflife_21d},
    "vac_052_vol_halflife_63d": {"inputs": ["volume"], "func": vac_052_vol_halflife_63d},
    "vac_053_vol_halflife_126d": {"inputs": ["volume"], "func": vac_053_vol_halflife_126d},
    "vac_054_vol_ewm_decay_5d": {"inputs": ["volume"], "func": vac_054_vol_ewm_decay_5d},
    "vac_055_vol_ewm_decay_21d": {"inputs": ["volume"], "func": vac_055_vol_ewm_decay_21d},
    "vac_056_vol_autocorr_decay_ratio": {"inputs": ["volume"], "func": vac_056_vol_autocorr_decay_ratio},
    "vac_057_vol_autocorr_sum_lag1to5_63d": {"inputs": ["volume"], "func": vac_057_vol_autocorr_sum_lag1to5_63d},
    "vac_058_vol_autocorr_sum_lag1to5_126d": {"inputs": ["volume"], "func": vac_058_vol_autocorr_sum_lag1to5_126d},
    "vac_059_vol_persistence_above_avg_21d": {"inputs": ["volume"], "func": vac_059_vol_persistence_above_avg_21d},
    "vac_060_vol_persistence_above_avg_63d": {"inputs": ["volume"], "func": vac_060_vol_persistence_above_avg_63d},
    "vac_061_high_vol_run_consec_21d": {"inputs": ["volume"], "func": vac_061_high_vol_run_consec_21d},
    "vac_062_high_vol_run_consec_252d": {"inputs": ["volume"], "func": vac_062_high_vol_run_consec_252d},
    "vac_063_high_vol_runs_count_63d": {"inputs": ["volume"], "func": vac_063_high_vol_runs_count_63d},
    "vac_064_high_vol_runs_count_252d": {"inputs": ["volume"], "func": vac_064_high_vol_runs_count_252d},
    "vac_065_vol_runs_above_2x_mean_count_63d": {"inputs": ["volume"], "func": vac_065_vol_runs_above_2x_mean_count_63d},
    "vac_066_vol_runs_above_2x_mean_count_252d": {"inputs": ["volume"], "func": vac_066_vol_runs_above_2x_mean_count_252d},
    "vac_067_low_vol_consec_streak": {"inputs": ["volume"], "func": vac_067_low_vol_consec_streak},
    "vac_068_vol_runs_alternation_rate_63d": {"inputs": ["volume"], "func": vac_068_vol_runs_alternation_rate_63d},
    "vac_069_vol_runs_alternation_rate_252d": {"inputs": ["volume"], "func": vac_069_vol_runs_alternation_rate_252d},
    "vac_070_max_high_vol_run_63d": {"inputs": ["volume"], "func": vac_070_max_high_vol_run_63d},
    "vac_071_max_high_vol_run_252d": {"inputs": ["volume"], "func": vac_071_max_high_vol_run_252d},
    "vac_072_vol_sign_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_072_vol_sign_autocorr_lag1_63d},
    "vac_073_vol_sign_autocorr_lag1_252d": {"inputs": ["volume"], "func": vac_073_vol_sign_autocorr_lag1_252d},
    "vac_074_vol_sign_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_074_vol_sign_autocorr_lag5_63d},
    "vac_075_vol_runlength_pct_rank_252d": {"inputs": ["volume"], "func": vac_075_vol_runlength_pct_rank_252d},
}
