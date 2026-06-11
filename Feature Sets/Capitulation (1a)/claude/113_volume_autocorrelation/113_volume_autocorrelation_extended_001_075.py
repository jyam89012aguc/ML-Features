"""
113_volume_autocorrelation — Extended Features 001-075
Domain: deeper variants of volume serial-dependence — longer lags, wider windows,
        alternate volume transformations, cross-series AC structures, multi-scale
        memory composites, extreme-volume autocorrelation
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


def _pacf2(s: pd.Series, w: int) -> pd.Series:
    """Rolling PACF lag 2 via Yule-Walker 2nd order."""
    r1 = _rolling_autocorr(s, w, 1)
    r2 = _rolling_autocorr(s, w, 2)
    num = r2 - r1 * r1
    den = 1.0 - r1 * r1
    return _safe_div(num, den.replace(0, np.nan))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Longer lags / larger windows ---

def vac_ext_001_logvol_autocorr_lag10_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 10 (two-week)."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 10)


def vac_ext_002_logvol_autocorr_lag21_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume at lag 21 (monthly)."""
    return _rolling_autocorr(_log_volume(volume), _TD_QTR, 21)


def vac_ext_003_logvol_autocorr_lag63_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 63 (quarterly lag)."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 63)


def vac_ext_004_dvol_autocorr_lag21_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of log-volume changes at lag 21."""
    return _rolling_autocorr(_volume_change(volume), _TD_QTR, 21)


def vac_ext_005_dvol_autocorr_lag63_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume changes at lag 63."""
    return _rolling_autocorr(_volume_change(volume), _TD_YEAR, 63)


def vac_ext_006_logvol_ac_sum_lag1to10_252d(volume: pd.Series) -> pd.Series:
    """Sum of lag-1 through lag-10 autocorrelations of log-volume over 252 days."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_YEAR, lag).fillna(0.0) for lag in range(1, 11))
    return total


def vac_ext_007_logvol_ac_abs_sum_lag1to10_252d(volume: pd.Series) -> pd.Series:
    """Sum of absolute autocorrelations at lags 1-10 of log-volume over 252 days."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_YEAR, lag).abs().fillna(0.0) for lag in range(1, 11))
    return total


def vac_ext_008_vol_variance_ratio_126_1(volume: pd.Series) -> pd.Series:
    """Variance ratio: Var(126-day log-vol change) / (126 * Var(1-day)), 252d window."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_YEAR) ** 2
    dv126 = _log_volume(volume).diff(126)
    var126 = _rolling_std(dv126, _TD_YEAR) ** 2
    return _safe_div(var126, (126.0 * var1).replace(0, np.nan))


def vac_ext_009_vol_hurst_expanding(volume: pd.Series) -> pd.Series:
    """Expanding all-history R/S Hurst exponent of log-volume."""
    lv = _log_volume(volume)
    return lv.expanding(min_periods=16).apply(_hurst_rs, raw=True)


def vac_ext_010_dvol_hurst_252d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume changes over trailing 252-day window."""
    dv = _volume_change(volume)
    return dv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True)


def vac_ext_011_logvol_autocorr_lag2_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 2."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 2)


def vac_ext_012_logvol_autocorr_lag3_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of log-volume at lag 3."""
    return _rolling_autocorr(_log_volume(volume), _TD_YEAR, 3)


# --- Group B (013-022): Alternate volume transformations ---

def vac_ext_013_rawvol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of raw (unlogged) volume at lag 1."""
    return _rolling_autocorr(volume, _TD_QTR, 1)


def vac_ext_014_rawvol_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of raw volume at lag 5."""
    return _rolling_autocorr(volume, _TD_QTR, 5)


def vac_ext_015_vol_zscore_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of z-scored volume at lag 1."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    return _rolling_autocorr(z, _TD_QTR, 1)


def vac_ext_016_vol_zscore_autocorr_lag1_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of z-scored volume at lag 1."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_YEAR), _rolling_std(lv, _TD_YEAR))
    return _rolling_autocorr(z, _TD_YEAR, 1)


def vac_ext_017_vol_pct_rank_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of volume percentile rank at lag 1."""
    pr = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return _rolling_autocorr(pr, _TD_QTR, 1)


def vac_ext_018_vol_pct_rank_autocorr_lag1_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day autocorrelation of volume percentile rank at lag 1."""
    pr = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _rolling_autocorr(pr, _TD_YEAR, 1)


def vac_ext_019_vol_sq_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of squared log-volume at lag 1 (absolute level clustering)."""
    lv2 = _log_volume(volume) ** 2
    return _rolling_autocorr(lv2, _TD_QTR, 1)


def vac_ext_020_vol_sq_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of squared log-volume at lag 5."""
    lv2 = _log_volume(volume) ** 2
    return _rolling_autocorr(lv2, _TD_QTR, 5)


def vac_ext_021_vol_abs_change_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of absolute log-volume changes at lag 1."""
    abs_dv = _volume_change(volume).abs()
    return _rolling_autocorr(abs_dv, _TD_QTR, 1)


def vac_ext_022_vol_abs_change_autocorr_lag5_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of absolute log-volume changes at lag 5."""
    abs_dv = _volume_change(volume).abs()
    return _rolling_autocorr(abs_dv, _TD_QTR, 5)


# --- Group C (023-032): Extreme-volume autocorrelation ---

def vac_ext_023_extreme_high_vol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of extreme-high-volume indicator (> 2 std above mean) at lag 1."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    flag = (z > 2.0).astype(float)
    return _rolling_autocorr(flag, _TD_QTR, 1)


def vac_ext_024_extreme_low_vol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of extreme-low-volume indicator (< -2 std below mean) at lag 1."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    flag = (z < -2.0).astype(float)
    return _rolling_autocorr(flag, _TD_QTR, 1)


def vac_ext_025_vol_above_1sigma_consec(volume: pd.Series) -> pd.Series:
    """Consecutive days volume is more than 1 std above its 63-day mean."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    return _consec_streak(z > 1.0)


def vac_ext_026_vol_above_2sigma_consec(volume: pd.Series) -> pd.Series:
    """Consecutive days volume is more than 2 std above its 63-day mean."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    return _consec_streak(z > 2.0)


def vac_ext_027_vol_extreme_high_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume is > 2 std above 63d mean."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    return _rolling_sum((z > 2.0).astype(float), _TD_QTR)


def vac_ext_028_vol_extreme_low_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume is > 2 std below 63d mean."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    return _rolling_sum((z < -2.0).astype(float), _TD_QTR)


def vac_ext_029_vol_extreme_high_run_max_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive extreme-high-volume run length (> 1.5 std) within trailing 252 days."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_YEAR), _rolling_std(lv, _TD_YEAR))
    above = (z > 1.5)

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


def vac_ext_030_vol_extreme_autocorr_asymmetry_63d(volume: pd.Series) -> pd.Series:
    """Asymmetry: lag-1 ACF of high-volume spikes minus lag-1 ACF of low-volume spikes (63d).
    Captures whether capitulation-era high-volume days cluster more than low-volume days.
    """
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    high = (z > 1.0).astype(float)
    low = (z < -1.0).astype(float)
    ac_high = _rolling_autocorr(high, _TD_QTR, 1)
    ac_low = _rolling_autocorr(low, _TD_QTR, 1)
    return ac_high.fillna(0.0) - ac_low.fillna(0.0)


def vac_ext_031_vol_spike_reversion_autocorr_lag2_63d(volume: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of extreme-high-volume indicator (63d): does spike cluster at t+2?"""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    flag = (z > 2.0).astype(float)
    return _rolling_autocorr(flag, _TD_QTR, 2)


def vac_ext_032_vol_spike_consecutive_rate_63d(volume: pd.Series) -> pd.Series:
    """Fraction of spike days (> 2 std) that are immediately followed by another spike day, 63d window."""
    lv = _log_volume(volume)
    z = _safe_div(lv - _rolling_mean(lv, _TD_QTR), _rolling_std(lv, _TD_QTR))
    spike = (z > 2.0).astype(float)
    consec = (spike * spike.shift(-1)).fillna(0.0)
    spike_sum = _rolling_sum(spike, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(consec, _TD_QTR), spike_sum)


# --- Group D (033-042): Multi-scale memory composites ---

def vac_ext_033_vol_ac_multiscale_mean_63d(volume: pd.Series) -> pd.Series:
    """Mean of lag-1 autocorrelations at windows 21, 63, and 126 days (multi-scale memory)."""
    lv = _log_volume(volume)
    a21 = _rolling_autocorr(lv, _TD_MON, 1)
    a63 = _rolling_autocorr(lv, _TD_QTR, 1)
    a126 = _rolling_autocorr(lv, _TD_HALF, 1)
    return (a21.fillna(0.0) + a63.fillna(0.0) + a126.fillna(0.0)) / 3.0


def vac_ext_034_vol_ac_multiscale_std(volume: pd.Series) -> pd.Series:
    """Std of lag-1 autocorrelations at windows 21, 63, 126 (variability across scales)."""
    lv = _log_volume(volume)
    vals = pd.DataFrame({
        "a21": _rolling_autocorr(lv, _TD_MON, 1),
        "a63": _rolling_autocorr(lv, _TD_QTR, 1),
        "a126": _rolling_autocorr(lv, _TD_HALF, 1),
    })
    return vals.std(axis=1)


def vac_ext_035_vol_ac_multiscale_range(volume: pd.Series) -> pd.Series:
    """Range of lag-1 autocorrelations across windows 21, 63, 126 (scale dispersion)."""
    lv = _log_volume(volume)
    a21 = _rolling_autocorr(lv, _TD_MON, 1)
    a63 = _rolling_autocorr(lv, _TD_QTR, 1)
    a126 = _rolling_autocorr(lv, _TD_HALF, 1)
    df = pd.DataFrame({"a21": a21, "a63": a63, "a126": a126})
    return df.max(axis=1) - df.min(axis=1)


def vac_ext_036_vol_hurst_multiscale_mean(volume: pd.Series) -> pd.Series:
    """Mean of Hurst exponents at 63-day, 126-day, 252-day windows (multi-scale long memory)."""
    lv = _log_volume(volume)
    h63 = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    h126 = lv.rolling(_TD_HALF, min_periods=max(8, _TD_HALF // 2)).apply(_hurst_rs, raw=True)
    h252 = lv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True)
    return (h63.fillna(0.5) + h126.fillna(0.5) + h252.fillna(0.5)) / 3.0


def vac_ext_037_vol_hurst_multiscale_trend(volume: pd.Series) -> pd.Series:
    """Trend direction in Hurst across scales: H_252d minus H_63d (long-range vs short-range memory)."""
    lv = _log_volume(volume)
    h63 = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    h252 = lv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True)
    return h252.fillna(0.5) - h63.fillna(0.5)


def vac_ext_038_vol_ac_trend_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Difference between 21-day and 252-day lag-1 log-volume ACF (short vs long-term persistence)."""
    lv = _log_volume(volume)
    a21 = _rolling_autocorr(lv, _TD_MON, 1)
    a252 = _rolling_autocorr(lv, _TD_YEAR, 1)
    return a21.fillna(0.0) - a252.fillna(0.0)


def vac_ext_039_vol_vr_multiscale_composite(volume: pd.Series) -> pd.Series:
    """Mean of variance ratios at 5-day, 21-day, 63-day lags (multi-scale persistence composite)."""
    dv = _volume_change(volume)
    lv = _log_volume(volume)

    var1_63 = _rolling_std(dv, _TD_QTR) ** 2
    vr5 = _safe_div(_rolling_std(lv.diff(5), _TD_QTR) ** 2, (5.0 * var1_63).replace(0, np.nan))

    var1_126 = _rolling_std(dv, _TD_HALF) ** 2
    vr21 = _safe_div(_rolling_std(lv.diff(21), _TD_HALF) ** 2, (21.0 * var1_126).replace(0, np.nan))

    var1_252 = _rolling_std(dv, _TD_YEAR) ** 2
    vr63 = _safe_div(_rolling_std(lv.diff(63), _TD_YEAR) ** 2, (63.0 * var1_252).replace(0, np.nan))

    return (vr5.fillna(1.0) + vr21.fillna(1.0) + vr63.fillna(1.0)) / 3.0


def vac_ext_040_vol_memory_regime_flag(volume: pd.Series) -> pd.Series:
    """Memory regime flag: 1 if 63-day Hurst > 0.6 (strong persistence), -1 if < 0.4 (anti-persistent), 0 otherwise."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    result = pd.Series(0.0, index=volume.index)
    result[h > 0.6] = 1.0
    result[h < 0.4] = -1.0
    return result


def vac_ext_041_vol_long_memory_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day Hurst exponent within expanding all-history distribution."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True)
    return h.expanding(min_periods=_TD_QTR).rank(pct=True)


def vac_ext_042_vol_ac_composite_6lags_252d(volume: pd.Series) -> pd.Series:
    """Sum of lag-1 through lag-6 autocorrelations of log-volume over 252-day window."""
    lv = _log_volume(volume)
    return sum(_rolling_autocorr(lv, _TD_YEAR, lag).fillna(0.0) for lag in range(1, 7))


# --- Group E (043-052): Z-scores and rank at additional windows ---

def vac_ext_043_logvol_ac1_126d_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 126-day lag-1 log-volume autocorrelation (all-history standardization)."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_HALF, 1)
    m = ac.expanding(min_periods=_TD_QTR).mean()
    s = ac.expanding(min_periods=_TD_QTR).std()
    return _safe_div(ac - m, s)


def vac_ext_044_logvol_ac1_252d_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_YEAR, 1)
    m = ac.expanding(min_periods=_TD_QTR).mean()
    s = ac.expanding(min_periods=_TD_QTR).std()
    return _safe_div(ac - m, s)


def vac_ext_045_vol_hurst_63d_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 63-day Hurst exponent (all-history standardization)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    m = h.expanding(min_periods=_TD_QTR).mean()
    s = h.expanding(min_periods=_TD_QTR).std()
    return _safe_div(h - m, s)


def vac_ext_046_vol_vr5_pct_rank_expanding(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 5-day variance ratio (63d) across all history."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    return vr.expanding(min_periods=_TD_QTR).rank(pct=True)


def vac_ext_047_logvol_ac_sum5_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of lag-1-to-5 ACF sum of log-volume (63d) within 252-day distribution."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    return total.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_ext_048_dvol_ac1_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day lag-1 volume-change autocorrelation vs 252-day distribution."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_MON, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def vac_ext_049_logvol_pacf2_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day lag-2 PACF of log-volume vs 252-day distribution."""
    p2 = _pacf2(_log_volume(volume), _TD_QTR)
    m = _rolling_mean(p2, _TD_YEAR)
    s = _rolling_std(p2, _TD_YEAR)
    return _safe_div(p2 - m, s)


def vac_ext_050_vol_ac_composite_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day composite ACF score (lags 1-3 mean) vs 252-day distribution."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    comp = (acs[0].fillna(0.0) + acs[1].fillna(0.0) + acs[2].fillna(0.0)) / 3.0
    m = _rolling_mean(comp, _TD_YEAR)
    s = _rolling_std(comp, _TD_YEAR)
    return _safe_div(comp - m, s)


def vac_ext_051_vol_ac_composite_63d_min_252d(volume: pd.Series) -> pd.Series:
    """Minimum 63-day composite ACF score over trailing 252 days."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    comp = (acs[0].fillna(0.0) + acs[1].fillna(0.0) + acs[2].fillna(0.0)) / 3.0
    return _rolling_min(comp, _TD_YEAR)


def vac_ext_052_vol_ac_composite_63d_max_252d(volume: pd.Series) -> pd.Series:
    """Maximum 63-day composite ACF score over trailing 252 days."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    comp = (acs[0].fillna(0.0) + acs[1].fillna(0.0) + acs[2].fillna(0.0)) / 3.0
    return _rolling_max(comp, _TD_YEAR)


# --- Group F (053-062): Cross-series autocorrelation structures ---

def vac_ext_053_vol_ac1_vs_price_ac1_diff_63d(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between 63-day lag-1 log-volume ACF and 63-day lag-1 log-price ACF."""
    lv = _log_volume(volume)
    lp = np.log(close.clip(lower=_EPS))
    return (_rolling_autocorr(lv, _TD_QTR, 1) - _rolling_autocorr(lp, _TD_QTR, 1))


def vac_ext_054_vol_change_vs_return_ac1_diff_63d(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between 63-day lag-1 volume-change ACF and 63-day lag-1 return ACF."""
    dv = _volume_change(volume)
    ret = close.pct_change(1)
    return (_rolling_autocorr(dv, _TD_QTR, 1) - _rolling_autocorr(ret, _TD_QTR, 1))


def vac_ext_055_vol_ac1_vs_hilo_range_ac1_63d(volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference between 63-day lag-1 log-volume ACF and 63-day lag-1 log-range ACF."""
    lv = _log_volume(volume)
    lrange = np.log(((high - low).clip(lower=_EPS)))
    return (_rolling_autocorr(lv, _TD_QTR, 1) - _rolling_autocorr(lrange, _TD_QTR, 1))


def vac_ext_056_vol_ac1_63d_times_hurst_63d(volume: pd.Series) -> pd.Series:
    """Product of 63-day lag-1 log-volume ACF and 63-day Hurst exponent (combined persistence score)."""
    lv = _log_volume(volume)
    ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    return ac1.fillna(0.0) * h.fillna(0.5)


def vac_ext_057_vol_ac_sum5_vs_vr5_diff_63d(volume: pd.Series) -> pd.Series:
    """Difference between lag-1-to-5 ACF sum of log-volume and (VR5 - 1), 63d window."""
    lv = _log_volume(volume)
    ac_sum = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = lv.diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan)) - 1.0
    return ac_sum - vr5.fillna(0.0)


def vac_ext_058_vol_ac1_21d_zscore_vs_ac1_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day AC1 to 252-day AC1 of log-volume (short-memory surge vs long-baseline)."""
    lv = _log_volume(volume)
    a21 = _rolling_autocorr(lv, _TD_MON, 1)
    a252 = _rolling_autocorr(lv, _TD_YEAR, 1)
    return _safe_div(a21, a252.replace(0, np.nan))


def vac_ext_059_vol_ac_pct_rank_multiscale_mean(volume: pd.Series) -> pd.Series:
    """Mean of percentile ranks of lag-1 ACF at 21, 63, 252-day windows (vs their own 252d distributions)."""
    lv = _log_volume(volume)
    pr21 = _rolling_autocorr(lv, _TD_MON, 1).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    pr63 = _rolling_autocorr(lv, _TD_QTR, 1).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    pr252 = _rolling_autocorr(lv, _TD_YEAR, 1).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (pr21.fillna(0.5) + pr63.fillna(0.5) + pr252.fillna(0.5)) / 3.0


def vac_ext_060_vol_dvol_ac1_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day lag-1 dvol ACF to 63-day lag-1 log-volume ACF (level vs change memory ratio)."""
    lv = _log_volume(volume)
    dv = _volume_change(volume)
    return _safe_div(
        _rolling_autocorr(dv, _TD_QTR, 1),
        _rolling_autocorr(lv, _TD_QTR, 1).replace(0, np.nan)
    )


# --- Group G (061-075): Capitulation-targeted volume memory features ---

def vac_ext_061_vol_ac1_21d_new_low_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's 21-day lag-1 log-volume autocorrelation is a 252-day low."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    prev_min = ac.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (ac < prev_min).astype(float)


def vac_ext_062_vol_hurst_63d_new_high_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's 63-day Hurst exponent is a 252-day high (peak persistence)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    prev_max = h.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (h > prev_max).astype(float)


def vac_ext_063_vol_vr5_new_high_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's 5-day variance ratio (63d) is a 252-day high (maximum volume persistence)."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    prev_max = vr.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (vr > prev_max).astype(float)


def vac_ext_064_vol_high_persistence_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum run of consecutive days where 21-day lag-1 AC > 0.3 within trailing 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    above = (ac > 0.3)

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


def vac_ext_065_vol_rapid_ac_change_flag(volume: pd.Series) -> pd.Series:
    """Flag: the 5-day change in 63-day lag-1 log-volume ACF exceeds 1.5 std of that change."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    d5 = ac.diff(_TD_WEEK)
    threshold = _rolling_std(d5, _TD_YEAR) * 1.5
    return (d5.abs() > threshold).astype(float)


def vac_ext_066_vol_memory_dispersion_score(volume: pd.Series) -> pd.Series:
    """Dispersion of log-volume ACF across lags 1, 5, 21 within 63d window (std across lags).
    High dispersion = memory decays rapidly or oscillates; low = flat memory structure.
    """
    lv = _log_volume(volume)
    a1 = _rolling_autocorr(lv, _TD_QTR, 1)
    a5 = _rolling_autocorr(lv, _TD_QTR, 5)
    a21 = _rolling_autocorr(lv, _TD_QTR, 21)
    df = pd.DataFrame({"a1": a1, "a5": a5, "a21": a21})
    return df.std(axis=1)


def vac_ext_067_vol_antipers_intensity_63d(volume: pd.Series) -> pd.Series:
    """Anti-persistence intensity: sum of negative autocorrelations across lags 1-5 (63d).
    Large negative value = strong mean-reversion in volume.
    """
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 6):
        ac = _rolling_autocorr(lv, _TD_QTR, lag)
        total = total + ac.where(ac < 0, 0.0).fillna(0.0)
    return total


def vac_ext_068_vol_pers_intensity_63d(volume: pd.Series) -> pd.Series:
    """Persistence intensity: sum of positive autocorrelations across lags 1-5 (63d).
    Large positive value = strong persistence in volume.
    """
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 6):
        ac = _rolling_autocorr(lv, _TD_QTR, lag)
        total = total + ac.where(ac > 0, 0.0).fillna(0.0)
    return total


def vac_ext_069_vol_ac1_63d_vs_halflife_ratio(volume: pd.Series) -> pd.Series:
    """Ratio: 63-day lag-1 log-volume ACF divided by half-life (in days) from 63-day window.
    Normalizes correlation strength by time-scale.
    """
    lv = _log_volume(volume)
    ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    rho_abs = ac1.abs().clip(upper=1.0 - _EPS)
    ln_rho = np.log(rho_abs.clip(lower=_EPS))
    hl = _safe_div(pd.Series(-np.log(2.0), index=volume.index), ln_rho)
    return _safe_div(ac1, hl.replace(0, np.nan))


def vac_ext_070_vol_ac_capitulation_composite(volume: pd.Series) -> pd.Series:
    """Capitulation-focused composite: weighted score of Hurst deviation, VR5 deviation, and AC1 magnitude.
    All normalized to [0, ~1] scale. Higher = more unusual persistent volume memory.
    hurst_comp = abs(H - 0.5) / 0.5; vr_comp = abs(VR5 - 1).clip(0,2)/2; ac_comp = abs(AC1_63d).clip(0,1).
    """
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True).fillna(0.5)
    hurst_comp = ((h - 0.5).abs() / 0.5).clip(upper=1.0)

    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = lv.diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan)).fillna(1.0)
    vr_comp = ((vr5 - 1.0).abs().clip(upper=2.0)) / 2.0

    ac1 = _rolling_autocorr(lv, _TD_QTR, 1).abs().clip(upper=1.0).fillna(0.0)

    return hurst_comp * 0.4 + vr_comp * 0.3 + ac1 * 0.3


def vac_ext_071_vol_long_memory_above_half_21d_frac(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days where 63-day Hurst exponent > 0.5 (persistent memory days)."""
    lv = _log_volume(volume)
    h = lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)
    flag = (h > 0.5).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


def vac_ext_072_vol_ac_portmanteau_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of the Ljung-Box portmanteau stat (lags 1-5, 63d) within 252-day distribution."""

    def _lb_stat(arr):
        arr = arr[~np.isnan(arr)]
        n_arr = len(arr)
        if n_arr < 12:
            return np.nan
        stat = 0.0
        _eps = 1e-9
        for lag in range(1, 6):
            if n_arr <= lag:
                break
            x = arr[:-lag]
            y = arr[lag:]
            xm, ym = x.mean(), y.mean()
            dx = x - xm
            dy = y - ym
            denom = np.sqrt((dx ** 2).sum() * (dy ** 2).sum())
            rk = ((dx * dy).sum() / denom) if denom > _eps else 0.0
            stat += n_arr * (n_arr + 2) * rk ** 2 / (n_arr - lag)
        return stat / n_arr

    lv = _log_volume(volume)
    lb = lv.rolling(_TD_QTR, min_periods=max(12, _TD_QTR // 2)).apply(_lb_stat, raw=True)
    return lb.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_ext_073_vol_ac1_63d_expanding_min(volume: pd.Series) -> pd.Series:
    """All-time expanding minimum of 63-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.expanding(min_periods=_TD_QTR).min()


def vac_ext_074_vol_ac1_63d_expanding_max(volume: pd.Series) -> pd.Series:
    """All-time expanding maximum of 63-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.expanding(min_periods=_TD_QTR).max()


def vac_ext_075_vol_memory_score_multiscale(volume: pd.Series) -> pd.Series:
    """Multi-scale volume memory score: 0.3*(H_252-0.5) + 0.3*(AC1_252d) + 0.2*(VR126-1) + 0.2*(AC_sum5_252d/5).
    Positive = persistent volume memory (capitulation-consistent); negative = mean-reverting.
    """
    lv = _log_volume(volume)
    h = lv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True).fillna(0.5)
    ac1_252 = _rolling_autocorr(lv, _TD_YEAR, 1).fillna(0.0)

    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_YEAR) ** 2
    dv126 = lv.diff(126)
    var126 = _rolling_std(dv126, _TD_YEAR) ** 2
    vr126 = _safe_div(var126, (126.0 * var1).replace(0, np.nan)).fillna(1.0) - 1.0

    ac_sum5 = sum(_rolling_autocorr(lv, _TD_YEAR, lag).fillna(0.0) for lag in range(1, 6)) / 5.0

    return (h - 0.5) * 0.3 + ac1_252 * 0.3 + vr126.clip(-1.0, 1.0) * 0.2 + ac_sum5 * 0.2


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AUTOCORRELATION_EXTENDED_REGISTRY_001_075 = {
    "vac_ext_001_logvol_autocorr_lag10_252d": {"inputs": ["volume"], "func": vac_ext_001_logvol_autocorr_lag10_252d},
    "vac_ext_002_logvol_autocorr_lag21_63d": {"inputs": ["volume"], "func": vac_ext_002_logvol_autocorr_lag21_63d},
    "vac_ext_003_logvol_autocorr_lag63_252d": {"inputs": ["volume"], "func": vac_ext_003_logvol_autocorr_lag63_252d},
    "vac_ext_004_dvol_autocorr_lag21_63d": {"inputs": ["volume"], "func": vac_ext_004_dvol_autocorr_lag21_63d},
    "vac_ext_005_dvol_autocorr_lag63_252d": {"inputs": ["volume"], "func": vac_ext_005_dvol_autocorr_lag63_252d},
    "vac_ext_006_logvol_ac_sum_lag1to10_252d": {"inputs": ["volume"], "func": vac_ext_006_logvol_ac_sum_lag1to10_252d},
    "vac_ext_007_logvol_ac_abs_sum_lag1to10_252d": {"inputs": ["volume"], "func": vac_ext_007_logvol_ac_abs_sum_lag1to10_252d},
    "vac_ext_008_vol_variance_ratio_126_1": {"inputs": ["volume"], "func": vac_ext_008_vol_variance_ratio_126_1},
    "vac_ext_009_vol_hurst_expanding": {"inputs": ["volume"], "func": vac_ext_009_vol_hurst_expanding},
    "vac_ext_010_dvol_hurst_252d": {"inputs": ["volume"], "func": vac_ext_010_dvol_hurst_252d},
    "vac_ext_011_logvol_autocorr_lag2_252d": {"inputs": ["volume"], "func": vac_ext_011_logvol_autocorr_lag2_252d},
    "vac_ext_012_logvol_autocorr_lag3_252d": {"inputs": ["volume"], "func": vac_ext_012_logvol_autocorr_lag3_252d},
    "vac_ext_013_rawvol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_013_rawvol_autocorr_lag1_63d},
    "vac_ext_014_rawvol_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_ext_014_rawvol_autocorr_lag5_63d},
    "vac_ext_015_vol_zscore_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_015_vol_zscore_autocorr_lag1_63d},
    "vac_ext_016_vol_zscore_autocorr_lag1_252d": {"inputs": ["volume"], "func": vac_ext_016_vol_zscore_autocorr_lag1_252d},
    "vac_ext_017_vol_pct_rank_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_017_vol_pct_rank_autocorr_lag1_63d},
    "vac_ext_018_vol_pct_rank_autocorr_lag1_252d": {"inputs": ["volume"], "func": vac_ext_018_vol_pct_rank_autocorr_lag1_252d},
    "vac_ext_019_vol_sq_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_019_vol_sq_autocorr_lag1_63d},
    "vac_ext_020_vol_sq_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_ext_020_vol_sq_autocorr_lag5_63d},
    "vac_ext_021_vol_abs_change_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_021_vol_abs_change_autocorr_lag1_63d},
    "vac_ext_022_vol_abs_change_autocorr_lag5_63d": {"inputs": ["volume"], "func": vac_ext_022_vol_abs_change_autocorr_lag5_63d},
    "vac_ext_023_extreme_high_vol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_023_extreme_high_vol_autocorr_lag1_63d},
    "vac_ext_024_extreme_low_vol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vac_ext_024_extreme_low_vol_autocorr_lag1_63d},
    "vac_ext_025_vol_above_1sigma_consec": {"inputs": ["volume"], "func": vac_ext_025_vol_above_1sigma_consec},
    "vac_ext_026_vol_above_2sigma_consec": {"inputs": ["volume"], "func": vac_ext_026_vol_above_2sigma_consec},
    "vac_ext_027_vol_extreme_high_count_63d": {"inputs": ["volume"], "func": vac_ext_027_vol_extreme_high_count_63d},
    "vac_ext_028_vol_extreme_low_count_63d": {"inputs": ["volume"], "func": vac_ext_028_vol_extreme_low_count_63d},
    "vac_ext_029_vol_extreme_high_run_max_252d": {"inputs": ["volume"], "func": vac_ext_029_vol_extreme_high_run_max_252d},
    "vac_ext_030_vol_extreme_autocorr_asymmetry_63d": {"inputs": ["volume"], "func": vac_ext_030_vol_extreme_autocorr_asymmetry_63d},
    "vac_ext_031_vol_spike_reversion_autocorr_lag2_63d": {"inputs": ["volume"], "func": vac_ext_031_vol_spike_reversion_autocorr_lag2_63d},
    "vac_ext_032_vol_spike_consecutive_rate_63d": {"inputs": ["volume"], "func": vac_ext_032_vol_spike_consecutive_rate_63d},
    "vac_ext_033_vol_ac_multiscale_mean_63d": {"inputs": ["volume"], "func": vac_ext_033_vol_ac_multiscale_mean_63d},
    "vac_ext_034_vol_ac_multiscale_std": {"inputs": ["volume"], "func": vac_ext_034_vol_ac_multiscale_std},
    "vac_ext_035_vol_ac_multiscale_range": {"inputs": ["volume"], "func": vac_ext_035_vol_ac_multiscale_range},
    "vac_ext_036_vol_hurst_multiscale_mean": {"inputs": ["volume"], "func": vac_ext_036_vol_hurst_multiscale_mean},
    "vac_ext_037_vol_hurst_multiscale_trend": {"inputs": ["volume"], "func": vac_ext_037_vol_hurst_multiscale_trend},
    "vac_ext_038_vol_ac_trend_21d_vs_252d": {"inputs": ["volume"], "func": vac_ext_038_vol_ac_trend_21d_vs_252d},
    "vac_ext_039_vol_vr_multiscale_composite": {"inputs": ["volume"], "func": vac_ext_039_vol_vr_multiscale_composite},
    "vac_ext_040_vol_memory_regime_flag": {"inputs": ["volume"], "func": vac_ext_040_vol_memory_regime_flag},
    "vac_ext_041_vol_long_memory_pct_rank_252d": {"inputs": ["volume"], "func": vac_ext_041_vol_long_memory_pct_rank_252d},
    "vac_ext_042_vol_ac_composite_6lags_252d": {"inputs": ["volume"], "func": vac_ext_042_vol_ac_composite_6lags_252d},
    "vac_ext_043_logvol_ac1_126d_zscore_expanding": {"inputs": ["volume"], "func": vac_ext_043_logvol_ac1_126d_zscore_expanding},
    "vac_ext_044_logvol_ac1_252d_zscore_expanding": {"inputs": ["volume"], "func": vac_ext_044_logvol_ac1_252d_zscore_expanding},
    "vac_ext_045_vol_hurst_63d_zscore_expanding": {"inputs": ["volume"], "func": vac_ext_045_vol_hurst_63d_zscore_expanding},
    "vac_ext_046_vol_vr5_pct_rank_expanding": {"inputs": ["volume"], "func": vac_ext_046_vol_vr5_pct_rank_expanding},
    "vac_ext_047_logvol_ac_sum5_63d_pct_rank_252d": {"inputs": ["volume"], "func": vac_ext_047_logvol_ac_sum5_63d_pct_rank_252d},
    "vac_ext_048_dvol_ac1_21d_zscore_252d": {"inputs": ["volume"], "func": vac_ext_048_dvol_ac1_21d_zscore_252d},
    "vac_ext_049_logvol_pacf2_63d_zscore_252d": {"inputs": ["volume"], "func": vac_ext_049_logvol_pacf2_63d_zscore_252d},
    "vac_ext_050_vol_ac_composite_63d_zscore_252d": {"inputs": ["volume"], "func": vac_ext_050_vol_ac_composite_63d_zscore_252d},
    "vac_ext_051_vol_ac_composite_63d_min_252d": {"inputs": ["volume"], "func": vac_ext_051_vol_ac_composite_63d_min_252d},
    "vac_ext_052_vol_ac_composite_63d_max_252d": {"inputs": ["volume"], "func": vac_ext_052_vol_ac_composite_63d_max_252d},
    "vac_ext_053_vol_ac1_vs_price_ac1_diff_63d": {"inputs": ["volume", "close"], "func": vac_ext_053_vol_ac1_vs_price_ac1_diff_63d},
    "vac_ext_054_vol_change_vs_return_ac1_diff_63d": {"inputs": ["volume", "close"], "func": vac_ext_054_vol_change_vs_return_ac1_diff_63d},
    "vac_ext_055_vol_ac1_vs_hilo_range_ac1_63d": {"inputs": ["volume", "high", "low"], "func": vac_ext_055_vol_ac1_vs_hilo_range_ac1_63d},
    "vac_ext_056_vol_ac1_63d_times_hurst_63d": {"inputs": ["volume"], "func": vac_ext_056_vol_ac1_63d_times_hurst_63d},
    "vac_ext_057_vol_ac_sum5_vs_vr5_diff_63d": {"inputs": ["volume"], "func": vac_ext_057_vol_ac_sum5_vs_vr5_diff_63d},
    "vac_ext_058_vol_ac1_21d_zscore_vs_ac1_252d": {"inputs": ["volume"], "func": vac_ext_058_vol_ac1_21d_zscore_vs_ac1_252d},
    "vac_ext_059_vol_ac_pct_rank_multiscale_mean": {"inputs": ["volume"], "func": vac_ext_059_vol_ac_pct_rank_multiscale_mean},
    "vac_ext_060_vol_dvol_ac1_ratio_63d": {"inputs": ["volume"], "func": vac_ext_060_vol_dvol_ac1_ratio_63d},
    "vac_ext_061_vol_ac1_21d_new_low_252d_flag": {"inputs": ["volume"], "func": vac_ext_061_vol_ac1_21d_new_low_252d_flag},
    "vac_ext_062_vol_hurst_63d_new_high_252d_flag": {"inputs": ["volume"], "func": vac_ext_062_vol_hurst_63d_new_high_252d_flag},
    "vac_ext_063_vol_vr5_new_high_252d_flag": {"inputs": ["volume"], "func": vac_ext_063_vol_vr5_new_high_252d_flag},
    "vac_ext_064_vol_high_persistence_streak_252d": {"inputs": ["volume"], "func": vac_ext_064_vol_high_persistence_streak_252d},
    "vac_ext_065_vol_rapid_ac_change_flag": {"inputs": ["volume"], "func": vac_ext_065_vol_rapid_ac_change_flag},
    "vac_ext_066_vol_memory_dispersion_score": {"inputs": ["volume"], "func": vac_ext_066_vol_memory_dispersion_score},
    "vac_ext_067_vol_antipers_intensity_63d": {"inputs": ["volume"], "func": vac_ext_067_vol_antipers_intensity_63d},
    "vac_ext_068_vol_pers_intensity_63d": {"inputs": ["volume"], "func": vac_ext_068_vol_pers_intensity_63d},
    "vac_ext_069_vol_ac1_63d_vs_halflife_ratio": {"inputs": ["volume"], "func": vac_ext_069_vol_ac1_63d_vs_halflife_ratio},
    "vac_ext_070_vol_ac_capitulation_composite": {"inputs": ["volume"], "func": vac_ext_070_vol_ac_capitulation_composite},
    "vac_ext_071_vol_long_memory_above_half_21d_frac": {"inputs": ["volume"], "func": vac_ext_071_vol_long_memory_above_half_21d_frac},
    "vac_ext_072_vol_ac_portmanteau_pct_rank_252d": {"inputs": ["volume"], "func": vac_ext_072_vol_ac_portmanteau_pct_rank_252d},
    "vac_ext_073_vol_ac1_63d_expanding_min": {"inputs": ["volume"], "func": vac_ext_073_vol_ac1_63d_expanding_min},
    "vac_ext_074_vol_ac1_63d_expanding_max": {"inputs": ["volume"], "func": vac_ext_074_vol_ac1_63d_expanding_max},
    "vac_ext_075_vol_memory_score_multiscale": {"inputs": ["volume"], "func": vac_ext_075_vol_memory_score_multiscale},
}
