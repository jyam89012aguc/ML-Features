"""
113_volume_autocorrelation — Base Features 076-150
Domain: serial dependence / memory structure of volume — partial autocorrelation,
        long-memory / Hurst exponent of volume, z-score and rank of autocorrelation,
        cross-lag structures, volume mean-reversion speed, spectral memory proxies
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
    """Natural log of volume; clips to EPS before log."""
    return np.log(volume.clip(lower=_EPS))


def _volume_change(volume: pd.Series) -> pd.Series:
    """Day-over-day log change of volume."""
    return _log_volume(volume).diff(1)


def _pacf_lag1_ols(s: pd.Series, w: int) -> pd.Series:
    """Rolling partial autocorrelation at lag 1 via OLS (regress s_t on s_{t-1}).
    PACF lag 1 equals ACF lag 1 by definition; included for completeness.
    """
    return _rolling_autocorr(s, w, 1)


def _pacf_lag2_ols(s: pd.Series, w: int) -> pd.Series:
    """Rolling partial autocorrelation at lag 2 via OLS conditioning on lag 1.
    Approximation: r2 - r1^2 (Yule-Walker 2nd order).
    """
    r1 = _rolling_autocorr(s, w, 1)
    r2 = _rolling_autocorr(s, w, 2)
    num = r2 - r1 * r1
    den = 1.0 - r1 * r1
    return _safe_div(num, den.replace(0, np.nan))


def _pacf_lag3_ols(s: pd.Series, w: int) -> pd.Series:
    """Rolling partial autocorrelation at lag 3 via Yule-Walker approximation."""
    r1 = _rolling_autocorr(s, w, 1)
    r2 = _rolling_autocorr(s, w, 2)
    r3 = _rolling_autocorr(s, w, 3)
    num = r3 - r1 * r2 - r2 * r1 + r1 * r1 * r1
    den = 1.0 - r1 * r1 - r2 * r2 + r1 * r1 * r2
    return _safe_div(num, den.replace(0, np.nan))


def _hurst_rs(arr: np.ndarray) -> float:
    """R/S Hurst exponent estimate from a 1D array (NaN-safe).
    H > 0.5 = persistent, H < 0.5 = anti-persistent (mean-reverting).
    """
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Partial autocorrelation of log-volume ---

def vac_076_logvol_pacf_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day PACF of log-volume at lag 1."""
    return _pacf_lag1_ols(_log_volume(volume), _TD_MON)


def vac_077_logvol_pacf_lag2_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day PACF of log-volume at lag 2 (Yule-Walker 2nd order)."""
    return _pacf_lag2_ols(_log_volume(volume), _TD_MON)


def vac_078_logvol_pacf_lag3_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day PACF of log-volume at lag 3."""
    return _pacf_lag3_ols(_log_volume(volume), _TD_MON)


def vac_079_logvol_pacf_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume at lag 1."""
    return _pacf_lag1_ols(_log_volume(volume), _TD_QTR)


def vac_080_logvol_pacf_lag2_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume at lag 2."""
    return _pacf_lag2_ols(_log_volume(volume), _TD_QTR)


def vac_081_logvol_pacf_lag3_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume at lag 3."""
    return _pacf_lag3_ols(_log_volume(volume), _TD_QTR)


def vac_082_logvol_pacf_lag1_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day PACF of log-volume at lag 1."""
    return _pacf_lag1_ols(_log_volume(volume), _TD_HALF)


def vac_083_logvol_pacf_lag2_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day PACF of log-volume at lag 2."""
    return _pacf_lag2_ols(_log_volume(volume), _TD_HALF)


def vac_084_dvol_pacf_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume changes at lag 1."""
    return _pacf_lag1_ols(_volume_change(volume), _TD_QTR)


def vac_085_dvol_pacf_lag2_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume changes at lag 2."""
    return _pacf_lag2_ols(_volume_change(volume), _TD_QTR)


def vac_086_dvol_pacf_lag3_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day PACF of log-volume changes at lag 3."""
    return _pacf_lag3_ols(_volume_change(volume), _TD_QTR)


def vac_087_dvol_pacf_lag1_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day PACF of log-volume changes at lag 1."""
    return _pacf_lag1_ols(_volume_change(volume), _TD_HALF)


def vac_088_dvol_pacf_lag2_126d(volume: pd.Series) -> pd.Series:
    """Rolling 126-day PACF of log-volume changes at lag 2."""
    return _pacf_lag2_ols(_volume_change(volume), _TD_HALF)


def vac_089_logvol_pacf_lag2_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day PACF of log-volume at lag 2."""
    return _pacf_lag2_ols(_log_volume(volume), _TD_YEAR)


def vac_090_logvol_pacf_lag3_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day PACF of log-volume at lag 3."""
    return _pacf_lag3_ols(_log_volume(volume), _TD_YEAR)


# --- Group H (091-105): Hurst exponent of log-volume (long memory) ---

def vac_091_vol_hurst_63d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume over trailing 63-day window."""
    lv = _log_volume(volume)
    return lv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)


def vac_092_vol_hurst_126d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume over trailing 126-day window."""
    lv = _log_volume(volume)
    return lv.rolling(_TD_HALF, min_periods=max(8, _TD_HALF // 2)).apply(_hurst_rs, raw=True)


def vac_093_vol_hurst_252d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume over trailing 252-day window."""
    lv = _log_volume(volume)
    return lv.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(_hurst_rs, raw=True)


def vac_094_dvol_hurst_63d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume changes over trailing 63-day window."""
    dv = _volume_change(volume)
    return dv.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(_hurst_rs, raw=True)


def vac_095_dvol_hurst_126d(volume: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-volume changes over trailing 126-day window."""
    dv = _volume_change(volume)
    return dv.rolling(_TD_HALF, min_periods=max(8, _TD_HALF // 2)).apply(_hurst_rs, raw=True)


def vac_096_vol_hurst_above_half_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: 63-day Hurst exponent > 0.5 (persistent volume regime)."""
    return (vac_091_vol_hurst_63d(volume) > 0.5).astype(float)


def vac_097_vol_hurst_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day Hurst exponent relative to its 252-day distribution."""
    h = vac_091_vol_hurst_63d(volume)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def vac_098_vol_hurst_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Hurst exponent within trailing 252-day distribution."""
    h = vac_091_vol_hurst_63d(volume)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_099_vol_hurst_63d_minus_half(volume: pd.Series) -> pd.Series:
    """Deviation of 63-day Hurst exponent from 0.5 (random walk baseline)."""
    return vac_091_vol_hurst_63d(volume) - 0.5


def vac_100_vol_hurst_126d_minus_half(volume: pd.Series) -> pd.Series:
    """Deviation of 126-day Hurst exponent from 0.5."""
    return vac_092_vol_hurst_126d(volume) - 0.5


def vac_101_vol_hurst_252d_minus_half(volume: pd.Series) -> pd.Series:
    """Deviation of 252-day Hurst exponent from 0.5."""
    return vac_093_vol_hurst_252d(volume) - 0.5


def vac_102_vol_hurst_252d_pct_rank_expanding(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day Hurst exponent (all-time rank)."""
    h = vac_093_vol_hurst_252d(volume)
    return h.expanding(min_periods=_TD_QTR).rank(pct=True)


def vac_103_vol_hurst_trend_21d(volume: pd.Series) -> pd.Series:
    """21-day change in 63-day Hurst exponent (is memory increasing or decreasing?)."""
    h = vac_091_vol_hurst_63d(volume)
    return h.diff(_TD_MON)


def vac_104_vol_hurst_persistent_consec(volume: pd.Series) -> pd.Series:
    """Consecutive days 63-day Hurst exponent > 0.5 (persistent memory streak)."""
    return _consec_streak(vac_091_vol_hurst_63d(volume) > 0.5)


def vac_105_vol_hurst_antipersistent_consec(volume: pd.Series) -> pd.Series:
    """Consecutive days 63-day Hurst exponent < 0.5 (anti-persistent / mean-reverting streak)."""
    return _consec_streak(vac_091_vol_hurst_63d(volume) < 0.5)


# --- Group I (106-120): Z-scores and percentile ranks of autocorrelations ---

def vac_106_logvol_ac1_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day lag-1 log-volume autocorrelation vs 252-day distribution."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def vac_107_logvol_ac1_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day lag-1 log-volume autocorrelation vs 252-day distribution."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def vac_108_logvol_ac1_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day lag-1 log-volume autocorrelation within 252-day distribution."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_109_dvol_ac1_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day lag-1 volume-change autocorrelation vs 252-day distribution."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def vac_110_dvol_ac1_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day lag-1 volume-change autocorrelation within 252-day distribution."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_111_logvol_ac_sum5_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of lag-1-to-5 autocorrelation sum (63d) vs 252-day distribution."""
    lv = _log_volume(volume)
    total = sum(_rolling_autocorr(lv, _TD_QTR, lag).fillna(0.0) for lag in range(1, 6))
    m = _rolling_mean(total, _TD_YEAR)
    s = _rolling_std(total, _TD_YEAR)
    return _safe_div(total - m, s)


def vac_112_logvol_ac1_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day lag-1 log-volume autocorrelation within 252-day distribution."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_113_dvol_ac5_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day lag-5 volume-change autocorrelation vs 252-day distribution."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_QTR, 5)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def vac_114_vol_vr5_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 5-day variance ratio (63d) vs 252-day distribution."""
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    m = _rolling_mean(vr, _TD_YEAR)
    s = _rolling_std(vr, _TD_YEAR)
    return _safe_div(vr - m, s)


def vac_115_logvol_ac1_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding all-history z-score of 63-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    m = ac.expanding(min_periods=_TD_QTR).mean()
    s = ac.expanding(min_periods=_TD_QTR).std()
    return _safe_div(ac - m, s)


def vac_116_logvol_ac1_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63-day lag-1 log-volume autocorrelation."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return ac.expanding(min_periods=_TD_QTR).rank(pct=True)


def vac_117_logvol_ac1_new_high_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's 21-day lag-1 log-volume autocorrelation is a new 63d high."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    prev_max = ac.shift(1).rolling(_TD_QTR, min_periods=1).max()
    return (ac > prev_max).astype(float)


def vac_118_logvol_ac1_new_low_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's 21-day lag-1 log-volume autocorrelation is a new 63d low."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    prev_min = ac.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (ac < prev_min).astype(float)


def vac_119_logvol_ac1_63d_min_252d(volume: pd.Series) -> pd.Series:
    """Minimum 63-day lag-1 log-volume autocorrelation over trailing 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return _rolling_min(ac, _TD_YEAR)


def vac_120_logvol_ac1_63d_max_252d(volume: pd.Series) -> pd.Series:
    """Maximum 63-day lag-1 log-volume autocorrelation over trailing 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return _rolling_max(ac, _TD_YEAR)


# --- Group J (121-135): Cross-lag structural features ---

def vac_121_logvol_ac_lag5_minus_lag1_63d(volume: pd.Series) -> pd.Series:
    """Difference between lag-5 and lag-1 autocorrelations of log-volume (63d) — decay shape."""
    lv = _log_volume(volume)
    return _rolling_autocorr(lv, _TD_QTR, 5) - _rolling_autocorr(lv, _TD_QTR, 1)


def vac_122_dvol_ac_lag5_minus_lag1_63d(volume: pd.Series) -> pd.Series:
    """Difference between lag-5 and lag-1 autocorrelations of log-volume changes (63d)."""
    dv = _volume_change(volume)
    return _rolling_autocorr(dv, _TD_QTR, 5) - _rolling_autocorr(dv, _TD_QTR, 1)


def vac_123_logvol_ac_lag21_minus_lag1_126d(volume: pd.Series) -> pd.Series:
    """Difference between lag-21 and lag-1 autocorrelations of log-volume (126d)."""
    lv = _log_volume(volume)
    return _rolling_autocorr(lv, _TD_HALF, 21) - _rolling_autocorr(lv, _TD_HALF, 1)


def vac_124_logvol_ac_max_lag1to5_63d(volume: pd.Series) -> pd.Series:
    """Maximum autocorrelation among lags 1 through 5 of log-volume (63d)."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 6)]
    result = acs[0]
    for ac in acs[1:]:
        result = result.combine(ac, max)
    return result


def vac_125_logvol_ac_min_lag1to5_63d(volume: pd.Series) -> pd.Series:
    """Minimum autocorrelation among lags 1 through 5 of log-volume (63d)."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 6)]
    result = acs[0]
    for ac in acs[1:]:
        result = result.combine(ac, min)
    return result


def vac_126_logvol_ac_abs_sum_lag1to3_63d(volume: pd.Series) -> pd.Series:
    """Sum of absolute autocorrelations at lags 1, 2, 3 of log-volume (63d)."""
    lv = _log_volume(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 4):
        total = total + _rolling_autocorr(lv, _TD_QTR, lag).abs().fillna(0.0)
    return total


def vac_127_dvol_ac_abs_sum_lag1to3_63d(volume: pd.Series) -> pd.Series:
    """Sum of absolute autocorrelations at lags 1, 2, 3 of log-volume changes (63d)."""
    dv = _volume_change(volume)
    total = pd.Series(0.0, index=volume.index)
    for lag in range(1, 4):
        total = total + _rolling_autocorr(dv, _TD_QTR, lag).abs().fillna(0.0)
    return total


def vac_128_logvol_ac_sign_flip_count_5lags_63d(volume: pd.Series) -> pd.Series:
    """Count of sign changes among lags 1-5 autocorrelations of log-volume (63d).
    Measures whether autocorrelation alternates sign (oscillatory vs monotone decay).
    """
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 6)]
    flips = pd.Series(0.0, index=volume.index)
    for i in range(1, len(acs)):
        flip = ((acs[i] * acs[i - 1]) < 0.0).astype(float)
        flips = flips + flip.fillna(0.0)
    return flips


def vac_129_logvol_ac1_minus_pacf2_63d(volume: pd.Series) -> pd.Series:
    """ACF lag-1 minus PACF lag-2 of log-volume (63d) — pure lag-2 indirect effect."""
    lv = _log_volume(volume)
    ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    r1 = ac1
    r2 = _rolling_autocorr(lv, _TD_QTR, 2)
    num = r2 - r1 * r1
    den = 1.0 - r1 * r1
    pacf2 = _safe_div(num, den.replace(0, np.nan))
    return ac1 - pacf2


def vac_130_logvol_ac_portmanteau_stat_5lags_63d(volume: pd.Series) -> pd.Series:
    """Ljung-Box type portmanteau statistic for lags 1-5 of log-volume (63d).
    Sum of n*(n+2)*r_k^2/(n-k) for k=1..5 scaled by n; proxy for serial dependence significance.
    """
    lv = _log_volume(volume)
    n = _TD_QTR

    def _lb_stat(arr):
        arr = arr[~np.isnan(arr)]
        n_arr = len(arr)
        if n_arr < 12:
            return np.nan
        stat = 0.0
        for lag in range(1, 6):
            if n_arr <= lag:
                break
            x = arr[:-lag]
            y = arr[lag:]
            xm, ym = x.mean(), y.mean()
            dx = x - xm
            dy = y - ym
            denom = np.sqrt((dx ** 2).sum() * (dy ** 2).sum())
            rk = ((dx * dy).sum() / denom) if denom > _EPS else 0.0
            stat += n_arr * (n_arr + 2) * rk ** 2 / (n_arr - lag)
        return stat / n_arr

    return lv.rolling(n, min_periods=max(12, n // 2)).apply(_lb_stat, raw=True)


def vac_131_dvol_ac1_sign_consec_positive(volume: pd.Series) -> pd.Series:
    """Consecutive days the 21-day lag-1 volume-change autocorrelation is positive."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_MON, 1)
    return _consec_streak(ac > 0.0)


def vac_132_dvol_ac1_sign_consec_negative(volume: pd.Series) -> pd.Series:
    """Consecutive days the 21-day lag-1 volume-change autocorrelation is negative (mean-reversion streak)."""
    ac = _rolling_autocorr(_volume_change(volume), _TD_MON, 1)
    return _consec_streak(ac < 0.0)


def vac_133_logvol_ac1_63d_consec_positive(volume: pd.Series) -> pd.Series:
    """Consecutive days the 63-day lag-1 log-volume autocorrelation is positive."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return _consec_streak(ac > 0.0)


def vac_134_logvol_ac1_63d_above_median_flag(volume: pd.Series) -> pd.Series:
    """Flag: 63-day lag-1 log-volume autocorrelation is above its 252-day rolling median."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    med = ac.rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return (ac > med).astype(float)


def vac_135_logvol_ac1_63d_vs_ac5_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of lag-1 to lag-5 log-volume autocorrelation (63d) — persistence decay speed."""
    lv = _log_volume(volume)
    ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    ac5 = _rolling_autocorr(lv, _TD_QTR, 5)
    return _safe_div(ac1, ac5.replace(0, np.nan))


# --- Group K (136-150): Volume mean-reversion speed and spectral memory proxies ---

def vac_136_vol_mean_reversion_speed_21d(volume: pd.Series) -> pd.Series:
    """Mean-reversion speed: (1 - lag-1 autocorrelation) as fraction, 21d window.
    Higher = faster mean-reversion; 0 = random walk; negative = overshoot.
    """
    rho = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    return 1.0 - rho


def vac_137_vol_mean_reversion_speed_63d(volume: pd.Series) -> pd.Series:
    """Mean-reversion speed (1 - rho) computed from 63-day window."""
    rho = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return 1.0 - rho


def vac_138_vol_ar1_implied_innovation_21d(volume: pd.Series) -> pd.Series:
    """AR(1) implied innovation std: std(residuals) = std(lv) * sqrt(1 - rho^2), 21d."""
    lv = _log_volume(volume)
    rho = _rolling_autocorr(lv, _TD_MON, 1)
    sig = _rolling_std(lv, _TD_MON)
    return sig * (1.0 - rho ** 2).clip(lower=0.0) ** 0.5


def vac_139_vol_ar1_implied_innovation_63d(volume: pd.Series) -> pd.Series:
    """AR(1) implied innovation std over 63-day window."""
    lv = _log_volume(volume)
    rho = _rolling_autocorr(lv, _TD_QTR, 1)
    sig = _rolling_std(lv, _TD_QTR)
    return sig * (1.0 - rho ** 2).clip(lower=0.0) ** 0.5


def vac_140_vol_spectral_low_freq_ratio_63d(volume: pd.Series) -> pd.Series:
    """Low-frequency power ratio of log-volume: variance of 21d smoothed / total variance (63d window).
    Higher = more low-frequency (long-memory) content.
    """
    lv = _log_volume(volume)
    lv_smooth = _rolling_mean(lv, _TD_MON)
    var_smooth = _rolling_std(lv_smooth, _TD_QTR) ** 2
    var_total = _rolling_std(lv, _TD_QTR) ** 2
    return _safe_div(var_smooth, var_total.replace(0, np.nan))


def vac_141_vol_spectral_low_freq_ratio_252d(volume: pd.Series) -> pd.Series:
    """Low-frequency power ratio of log-volume over 252-day window."""
    lv = _log_volume(volume)
    lv_smooth = _rolling_mean(lv, _TD_MON)
    var_smooth = _rolling_std(lv_smooth, _TD_YEAR) ** 2
    var_total = _rolling_std(lv, _TD_YEAR) ** 2
    return _safe_div(var_smooth, var_total.replace(0, np.nan))


def vac_142_vol_ac1_21d_min_252d(volume: pd.Series) -> pd.Series:
    """Minimum 21-day lag-1 log-volume autocorrelation over trailing 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    return _rolling_min(ac, _TD_YEAR)


def vac_143_vol_ac1_21d_max_252d(volume: pd.Series) -> pd.Series:
    """Maximum 21-day lag-1 log-volume autocorrelation over trailing 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_MON, 1)
    return _rolling_max(ac, _TD_YEAR)


def vac_144_vol_ac1_63d_range_252d(volume: pd.Series) -> pd.Series:
    """Range (max - min) of 63-day lag-1 log-volume autocorrelation over 252 days."""
    ac = _rolling_autocorr(_log_volume(volume), _TD_QTR, 1)
    return _rolling_max(ac, _TD_YEAR) - _rolling_min(ac, _TD_YEAR)


def vac_145_vol_ac_composite_score_63d(volume: pd.Series) -> pd.Series:
    """Composite serial-dependence score: sum of lags 1-3 log-volume ACF divided by 3, 63d window."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_QTR, lag) for lag in range(1, 4)]
    total = acs[0].fillna(0.0)
    for ac in acs[1:]:
        total = total + ac.fillna(0.0)
    return total / 3.0


def vac_146_vol_ac_composite_score_126d(volume: pd.Series) -> pd.Series:
    """Composite serial-dependence score: sum of lags 1-3 log-volume ACF divided by 3, 126d window."""
    lv = _log_volume(volume)
    acs = [_rolling_autocorr(lv, _TD_HALF, lag) for lag in range(1, 4)]
    total = acs[0].fillna(0.0)
    for ac in acs[1:]:
        total = total + ac.fillna(0.0)
    return total / 3.0


def vac_147_vol_ac_composite_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day composite ACF score within 252-day distribution."""
    comp = vac_145_vol_ac_composite_score_63d(volume)
    return comp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vac_148_vol_hurst_vs_vr5_diff(volume: pd.Series) -> pd.Series:
    """Difference between 63-day Hurst exponent and (VR5 variance ratio) as memory divergence signal."""
    h = vac_091_vol_hurst_63d(volume)
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_QTR) ** 2
    dv5 = _log_volume(volume).diff(5)
    var5 = _rolling_std(dv5, _TD_QTR) ** 2
    vr5 = _safe_div(var5, (5.0 * var1).replace(0, np.nan))
    return h - vr5


def vac_149_dvol_ac1_vs_logvol_ac1_diff_63d(volume: pd.Series) -> pd.Series:
    """Difference between lag-1 ACF of log-volume changes and lag-1 ACF of log-volume (63d)."""
    lv = _log_volume(volume)
    dv = _volume_change(volume)
    return _rolling_autocorr(dv, _TD_QTR, 1) - _rolling_autocorr(lv, _TD_QTR, 1)


def vac_150_vol_long_memory_score(volume: pd.Series) -> pd.Series:
    """Long-memory composite: weighted average of Hurst-0.5 (126d), AC sum lags 1-5 (126d), and VR21-1 (126d).
    Higher absolute value = stronger memory (either persistent or anti-persistent).
    """
    h_dev = vac_100_vol_hurst_126d_minus_half(volume)
    lv = _log_volume(volume)
    ac_sum = sum(_rolling_autocorr(lv, _TD_HALF, lag).fillna(0.0) for lag in range(1, 6))
    dv = _volume_change(volume)
    var1 = _rolling_std(dv, _TD_HALF) ** 2
    dv21 = lv.diff(21)
    var21 = _rolling_std(dv21, _TD_HALF) ** 2
    vr21 = _safe_div(var21, (21.0 * var1).replace(0, np.nan)) - 1.0
    return h_dev.fillna(0.0) * 0.4 + (ac_sum / 5.0) * 0.4 + vr21.fillna(0.0) * 0.2


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AUTOCORRELATION_REGISTRY_076_150 = {
    "vac_076_logvol_pacf_lag1_21d": {"inputs": ["volume"], "func": vac_076_logvol_pacf_lag1_21d},
    "vac_077_logvol_pacf_lag2_21d": {"inputs": ["volume"], "func": vac_077_logvol_pacf_lag2_21d},
    "vac_078_logvol_pacf_lag3_21d": {"inputs": ["volume"], "func": vac_078_logvol_pacf_lag3_21d},
    "vac_079_logvol_pacf_lag1_63d": {"inputs": ["volume"], "func": vac_079_logvol_pacf_lag1_63d},
    "vac_080_logvol_pacf_lag2_63d": {"inputs": ["volume"], "func": vac_080_logvol_pacf_lag2_63d},
    "vac_081_logvol_pacf_lag3_63d": {"inputs": ["volume"], "func": vac_081_logvol_pacf_lag3_63d},
    "vac_082_logvol_pacf_lag1_126d": {"inputs": ["volume"], "func": vac_082_logvol_pacf_lag1_126d},
    "vac_083_logvol_pacf_lag2_126d": {"inputs": ["volume"], "func": vac_083_logvol_pacf_lag2_126d},
    "vac_084_dvol_pacf_lag1_63d": {"inputs": ["volume"], "func": vac_084_dvol_pacf_lag1_63d},
    "vac_085_dvol_pacf_lag2_63d": {"inputs": ["volume"], "func": vac_085_dvol_pacf_lag2_63d},
    "vac_086_dvol_pacf_lag3_63d": {"inputs": ["volume"], "func": vac_086_dvol_pacf_lag3_63d},
    "vac_087_dvol_pacf_lag1_126d": {"inputs": ["volume"], "func": vac_087_dvol_pacf_lag1_126d},
    "vac_088_dvol_pacf_lag2_126d": {"inputs": ["volume"], "func": vac_088_dvol_pacf_lag2_126d},
    "vac_089_logvol_pacf_lag2_252d": {"inputs": ["volume"], "func": vac_089_logvol_pacf_lag2_252d},
    "vac_090_logvol_pacf_lag3_252d": {"inputs": ["volume"], "func": vac_090_logvol_pacf_lag3_252d},
    "vac_091_vol_hurst_63d": {"inputs": ["volume"], "func": vac_091_vol_hurst_63d},
    "vac_092_vol_hurst_126d": {"inputs": ["volume"], "func": vac_092_vol_hurst_126d},
    "vac_093_vol_hurst_252d": {"inputs": ["volume"], "func": vac_093_vol_hurst_252d},
    "vac_094_dvol_hurst_63d": {"inputs": ["volume"], "func": vac_094_dvol_hurst_63d},
    "vac_095_dvol_hurst_126d": {"inputs": ["volume"], "func": vac_095_dvol_hurst_126d},
    "vac_096_vol_hurst_above_half_flag": {"inputs": ["volume"], "func": vac_096_vol_hurst_above_half_flag},
    "vac_097_vol_hurst_63d_zscore_252d": {"inputs": ["volume"], "func": vac_097_vol_hurst_63d_zscore_252d},
    "vac_098_vol_hurst_63d_pct_rank_252d": {"inputs": ["volume"], "func": vac_098_vol_hurst_63d_pct_rank_252d},
    "vac_099_vol_hurst_63d_minus_half": {"inputs": ["volume"], "func": vac_099_vol_hurst_63d_minus_half},
    "vac_100_vol_hurst_126d_minus_half": {"inputs": ["volume"], "func": vac_100_vol_hurst_126d_minus_half},
    "vac_101_vol_hurst_252d_minus_half": {"inputs": ["volume"], "func": vac_101_vol_hurst_252d_minus_half},
    "vac_102_vol_hurst_252d_pct_rank_expanding": {"inputs": ["volume"], "func": vac_102_vol_hurst_252d_pct_rank_expanding},
    "vac_103_vol_hurst_trend_21d": {"inputs": ["volume"], "func": vac_103_vol_hurst_trend_21d},
    "vac_104_vol_hurst_persistent_consec": {"inputs": ["volume"], "func": vac_104_vol_hurst_persistent_consec},
    "vac_105_vol_hurst_antipersistent_consec": {"inputs": ["volume"], "func": vac_105_vol_hurst_antipersistent_consec},
    "vac_106_logvol_ac1_21d_zscore_252d": {"inputs": ["volume"], "func": vac_106_logvol_ac1_21d_zscore_252d},
    "vac_107_logvol_ac1_63d_zscore_252d": {"inputs": ["volume"], "func": vac_107_logvol_ac1_63d_zscore_252d},
    "vac_108_logvol_ac1_63d_pct_rank_252d": {"inputs": ["volume"], "func": vac_108_logvol_ac1_63d_pct_rank_252d},
    "vac_109_dvol_ac1_63d_zscore_252d": {"inputs": ["volume"], "func": vac_109_dvol_ac1_63d_zscore_252d},
    "vac_110_dvol_ac1_63d_pct_rank_252d": {"inputs": ["volume"], "func": vac_110_dvol_ac1_63d_pct_rank_252d},
    "vac_111_logvol_ac_sum5_63d_zscore_252d": {"inputs": ["volume"], "func": vac_111_logvol_ac_sum5_63d_zscore_252d},
    "vac_112_logvol_ac1_21d_pct_rank_252d": {"inputs": ["volume"], "func": vac_112_logvol_ac1_21d_pct_rank_252d},
    "vac_113_dvol_ac5_63d_zscore_252d": {"inputs": ["volume"], "func": vac_113_dvol_ac5_63d_zscore_252d},
    "vac_114_vol_vr5_zscore_252d": {"inputs": ["volume"], "func": vac_114_vol_vr5_zscore_252d},
    "vac_115_logvol_ac1_expanding_zscore": {"inputs": ["volume"], "func": vac_115_logvol_ac1_expanding_zscore},
    "vac_116_logvol_ac1_expanding_pct_rank": {"inputs": ["volume"], "func": vac_116_logvol_ac1_expanding_pct_rank},
    "vac_117_logvol_ac1_new_high_63d_flag": {"inputs": ["volume"], "func": vac_117_logvol_ac1_new_high_63d_flag},
    "vac_118_logvol_ac1_new_low_63d_flag": {"inputs": ["volume"], "func": vac_118_logvol_ac1_new_low_63d_flag},
    "vac_119_logvol_ac1_63d_min_252d": {"inputs": ["volume"], "func": vac_119_logvol_ac1_63d_min_252d},
    "vac_120_logvol_ac1_63d_max_252d": {"inputs": ["volume"], "func": vac_120_logvol_ac1_63d_max_252d},
    "vac_121_logvol_ac_lag5_minus_lag1_63d": {"inputs": ["volume"], "func": vac_121_logvol_ac_lag5_minus_lag1_63d},
    "vac_122_dvol_ac_lag5_minus_lag1_63d": {"inputs": ["volume"], "func": vac_122_dvol_ac_lag5_minus_lag1_63d},
    "vac_123_logvol_ac_lag21_minus_lag1_126d": {"inputs": ["volume"], "func": vac_123_logvol_ac_lag21_minus_lag1_126d},
    "vac_124_logvol_ac_max_lag1to5_63d": {"inputs": ["volume"], "func": vac_124_logvol_ac_max_lag1to5_63d},
    "vac_125_logvol_ac_min_lag1to5_63d": {"inputs": ["volume"], "func": vac_125_logvol_ac_min_lag1to5_63d},
    "vac_126_logvol_ac_abs_sum_lag1to3_63d": {"inputs": ["volume"], "func": vac_126_logvol_ac_abs_sum_lag1to3_63d},
    "vac_127_dvol_ac_abs_sum_lag1to3_63d": {"inputs": ["volume"], "func": vac_127_dvol_ac_abs_sum_lag1to3_63d},
    "vac_128_logvol_ac_sign_flip_count_5lags_63d": {"inputs": ["volume"], "func": vac_128_logvol_ac_sign_flip_count_5lags_63d},
    "vac_129_logvol_ac1_minus_pacf2_63d": {"inputs": ["volume"], "func": vac_129_logvol_ac1_minus_pacf2_63d},
    "vac_130_logvol_ac_portmanteau_stat_5lags_63d": {"inputs": ["volume"], "func": vac_130_logvol_ac_portmanteau_stat_5lags_63d},
    "vac_131_dvol_ac1_sign_consec_positive": {"inputs": ["volume"], "func": vac_131_dvol_ac1_sign_consec_positive},
    "vac_132_dvol_ac1_sign_consec_negative": {"inputs": ["volume"], "func": vac_132_dvol_ac1_sign_consec_negative},
    "vac_133_logvol_ac1_63d_consec_positive": {"inputs": ["volume"], "func": vac_133_logvol_ac1_63d_consec_positive},
    "vac_134_logvol_ac1_63d_above_median_flag": {"inputs": ["volume"], "func": vac_134_logvol_ac1_63d_above_median_flag},
    "vac_135_logvol_ac1_63d_vs_ac5_63d_ratio": {"inputs": ["volume"], "func": vac_135_logvol_ac1_63d_vs_ac5_63d_ratio},
    "vac_136_vol_mean_reversion_speed_21d": {"inputs": ["volume"], "func": vac_136_vol_mean_reversion_speed_21d},
    "vac_137_vol_mean_reversion_speed_63d": {"inputs": ["volume"], "func": vac_137_vol_mean_reversion_speed_63d},
    "vac_138_vol_ar1_implied_innovation_21d": {"inputs": ["volume"], "func": vac_138_vol_ar1_implied_innovation_21d},
    "vac_139_vol_ar1_implied_innovation_63d": {"inputs": ["volume"], "func": vac_139_vol_ar1_implied_innovation_63d},
    "vac_140_vol_spectral_low_freq_ratio_63d": {"inputs": ["volume"], "func": vac_140_vol_spectral_low_freq_ratio_63d},
    "vac_141_vol_spectral_low_freq_ratio_252d": {"inputs": ["volume"], "func": vac_141_vol_spectral_low_freq_ratio_252d},
    "vac_142_vol_ac1_21d_min_252d": {"inputs": ["volume"], "func": vac_142_vol_ac1_21d_min_252d},
    "vac_143_vol_ac1_21d_max_252d": {"inputs": ["volume"], "func": vac_143_vol_ac1_21d_max_252d},
    "vac_144_vol_ac1_63d_range_252d": {"inputs": ["volume"], "func": vac_144_vol_ac1_63d_range_252d},
    "vac_145_vol_ac_composite_score_63d": {"inputs": ["volume"], "func": vac_145_vol_ac_composite_score_63d},
    "vac_146_vol_ac_composite_score_126d": {"inputs": ["volume"], "func": vac_146_vol_ac_composite_score_126d},
    "vac_147_vol_ac_composite_pct_rank_252d": {"inputs": ["volume"], "func": vac_147_vol_ac_composite_pct_rank_252d},
    "vac_148_vol_hurst_vs_vr5_diff": {"inputs": ["volume"], "func": vac_148_vol_hurst_vs_vr5_diff},
    "vac_149_dvol_ac1_vs_logvol_ac1_diff_63d": {"inputs": ["volume"], "func": vac_149_dvol_ac1_vs_logvol_ac1_diff_63d},
    "vac_150_vol_long_memory_score": {"inputs": ["volume"], "func": vac_150_vol_long_memory_score},
}
