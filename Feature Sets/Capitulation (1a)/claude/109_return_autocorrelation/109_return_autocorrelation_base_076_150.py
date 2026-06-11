"""
109_return_autocorrelation — Base Features 076-150
Domain: autocorrelation and serial-dependence structure of returns — higher-lag autocorrelation,
        absolute-return autocorrelation (volatility clustering), range-based serial structure,
        cross-lag AC patterns, Hurst exponent proxies, weighted AC metrics
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


def _log_returns(close: pd.Series) -> pd.Series:
    """Log returns of close price."""
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of series s at given lag over window w. NaN-safe."""
    def _ac(x):
        arr = x[~np.isnan(x)]
        if len(arr) < max(lag + 2, w // 2):
            return np.nan
        if len(arr) <= lag:
            return np.nan
        x1 = arr[:-lag]
        x2 = arr[lag:]
        if len(x1) < 2:
            return np.nan
        m1, m2 = x1.mean(), x2.mean()
        num = ((x1 - m1) * (x2 - m2)).mean()
        den = x1.std(ddof=0) * x2.std(ddof=0)
        if den < _EPS:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).apply(_ac, raw=True)


def _variance_ratio(s: pd.Series, w: int, k: int) -> pd.Series:
    """Rolling variance ratio: Var(k-period ret)/(k*Var(1-period ret))."""
    def _vr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(k + 2, w // 2):
            return np.nan
        var1 = np.var(arr[1:] - arr[:-1], ddof=1) if n > 1 else np.nan
        if n < k + 1:
            return np.nan
        kret = arr[k:] - arr[:-k]
        vark = np.var(kret, ddof=1) if len(kret) > 1 else np.nan
        if var1 is None or np.isnan(var1) or var1 < _EPS:
            return np.nan
        return vark / (k * var1)
    return s.rolling(w, min_periods=max(k + 2, w // 2)).apply(_vr, raw=True)


def _runs_ratio(s: pd.Series, w: int) -> pd.Series:
    """Rolling ratio of observed runs to expected runs."""
    def _rr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(4, w // 2):
            return np.nan
        signs = np.sign(arr)
        runs = 1
        for i in range(1, n):
            if signs[i] != signs[i - 1]:
                runs += 1
        n_pos = np.sum(signs > 0)
        n_neg = np.sum(signs < 0)
        if n_pos == 0 or n_neg == 0:
            return np.nan
        expected = (2.0 * n_pos * n_neg / n) + 1.0
        if expected < _EPS:
            return np.nan
        return runs / expected
    return s.rolling(w, min_periods=max(4, w // 2)).apply(_rr, raw=True)


def _hurst_rs(s: pd.Series, w: int) -> pd.Series:
    """Rolling R/S Hurst exponent estimate over window w. NaN-safe."""
    def _h(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(8, w // 2):
            return np.nan
        mean = arr.mean()
        deviations = arr - mean
        cumdev = np.cumsum(deviations)
        r = cumdev.max() - cumdev.min()
        s_std = arr.std(ddof=1)
        if s_std < _EPS or r <= 0:
            return np.nan
        return np.log(r / s_std) / np.log(n)
    return s.rolling(w, min_periods=max(8, w // 2)).apply(_h, raw=True)


def _sign_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of the sign of series s at given lag."""
    signs = np.sign(s)
    return _rolling_autocorr(signs, w, lag)


def _abs_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of |s| at given lag (volatility clustering proxy)."""
    return _rolling_autocorr(s.abs(), w, lag)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Absolute-return autocorrelation (volatility clustering) ---

def rac_076_abs_ac_lag1_21d(close: pd.Series) -> pd.Series:
    """Autocorrelation of |log-returns| at lag 1 over 21-day window (ARCH effect proxy)."""
    r = _log_returns(close)
    return _abs_autocorr(r, _TD_MON, 1)


def rac_077_abs_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of |log-returns| at lag 1 over 63-day window."""
    r = _log_returns(close)
    return _abs_autocorr(r, _TD_QTR, 1)


def rac_078_abs_ac_lag1_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of |log-returns| at lag 1 over 126-day window."""
    r = _log_returns(close)
    return _abs_autocorr(r, _TD_HALF, 1)


def rac_079_abs_ac_lag2_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of |log-returns| at lag 2 over 63-day window."""
    r = _log_returns(close)
    return _abs_autocorr(r, _TD_QTR, 2)


def rac_080_abs_ac_lag5_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of |log-returns| at lag 5 over 63-day window."""
    r = _log_returns(close)
    return _abs_autocorr(r, _TD_QTR, 5)


def rac_081_abs_ac_lag1_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day |AC lag 1| within 252-day distribution."""
    r = _log_returns(close)
    ac = _abs_autocorr(r, _TD_QTR, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_082_abs_ac_sum_lags1_5_63d(close: pd.Series) -> pd.Series:
    """Sum of |autocorrelation| of |returns| at lags 1-5 over 63-day window."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _abs_autocorr(r, _TD_QTR, lag).abs().fillna(0.0)
    return total


def rac_083_abs_ac_lag1_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day |returns| lag-1 AC vs 252-day distribution."""
    r = _log_returns(close)
    ac = _abs_autocorr(r, _TD_QTR, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def rac_084_squared_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of squared log-returns at lag 1 over 63-day window (GARCH proxy)."""
    r = _log_returns(close)
    return _rolling_autocorr(r ** 2, _TD_QTR, 1)


def rac_085_squared_ac_lag1_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of squared log-returns at lag 1 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r ** 2, _TD_HALF, 1)


# --- Group I (086-095): Higher-lag autocorrelations ---

def rac_086_ac_lag4_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 4 over 63-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 4)


def rac_087_ac_lag5_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 5 over 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 5)


def rac_088_ac_lag10_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 10 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 10)


def rac_089_ac_lag10_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 10 over 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 10)


def rac_090_ac_lag21_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 21 (monthly) over 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 21)


def rac_091_ac_lag2_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 2 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 2)


def rac_092_ac_lag3_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 3 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 3)


def rac_093_ac_lag4_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 4 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 4)


def rac_094_ac_lag2_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 2 over 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 2)


def rac_095_ac_lag3_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 3 over 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 3)


# --- Group J (096-105): Hurst exponent and long-memory metrics ---

def rac_096_hurst_rs_63d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over 63-day window (0.5=random, >0.5=persistent)."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_QTR)


def rac_097_hurst_rs_126d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over 126-day window."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_HALF)


def rac_098_hurst_rs_252d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over 252-day window."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_YEAR)


def rac_099_hurst_rs_63d_minus_half(close: pd.Series) -> pd.Series:
    """R/S Hurst (63d) minus 0.5 (signed deviation from random walk)."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_QTR) - 0.5


def rac_100_hurst_rs_126d_minus_half(close: pd.Series) -> pd.Series:
    """R/S Hurst (126d) minus 0.5."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_HALF) - 0.5


def rac_101_hurst_rs_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Hurst R/S within its 252-day distribution."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_102_hurst_rs_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day Hurst R/S vs its 252-day distribution."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def rac_103_hurst_above_half_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: Hurst R/S (63d) > 0.5 (persistent / trending memory)."""
    r = _log_returns(close)
    return (_hurst_rs(r, _TD_QTR) > 0.5).astype(float)


def rac_104_hurst_below_half_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: Hurst R/S (63d) < 0.5 (anti-persistent / mean-reverting memory)."""
    r = _log_returns(close)
    return (_hurst_rs(r, _TD_QTR) < 0.5).astype(float)


def rac_105_hurst_rs_min_252d(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day Hurst R/S (most mean-reverting ever measured)."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return h.expanding(min_periods=_TD_QTR).min()


# --- Group K (106-115): Variance ratio extended grid ---

def rac_106_vr_2_252d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=2) over 252-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 2)


def rac_107_vr_10_63d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=10) over 63-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 10)


def rac_108_vr_21_126d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=21) over 126-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 21)


def rac_109_vr_63_252d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=63) over 252-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 63)


def rac_110_vr_2_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day VR(k=2) vs its 252-day distribution."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    m = _rolling_mean(vr, _TD_YEAR)
    s = _rolling_std(vr, _TD_YEAR)
    return _safe_div(vr - m, s)


def rac_111_vr_5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 126-day VR(k=5) vs its 252-day distribution."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_HALF, 5)
    m = _rolling_mean(vr, _TD_YEAR)
    s = _rolling_std(vr, _TD_YEAR)
    return _safe_div(vr - m, s)


def rac_112_vr_ratio_10_to_2_252d(close: pd.Series) -> pd.Series:
    """Ratio VR(k=10)/VR(k=2) over 252-day window (shape of variance ratio term structure)."""
    lp = np.log(close.replace(0, np.nan))
    vr10 = _variance_ratio(lp, _TD_YEAR, 10)
    vr2 = _variance_ratio(lp, _TD_YEAR, 2)
    return _safe_div(vr10, vr2.clip(lower=_EPS))


def rac_113_vr_21_minus1_252d(close: pd.Series) -> pd.Series:
    """VR(k=21) minus 1 over 252-day window (monthly VR deviation from random walk)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 21) - 1.0


def rac_114_vr_5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 126-day VR(k=5) within its 252-day distribution."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_HALF, 5)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_115_vr_2_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day VR(k=2) (most mean-reverting ever)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    return vr.expanding(min_periods=_TD_QTR).min()


# --- Group L (116-125): Range-based and high/low serial structure ---

def rac_116_hl_range_ac_lag1_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Autocorrelation of (high-low)/close range at lag 1 over 21-day window."""
    rng = _safe_div(high - low, close)
    return _rolling_autocorr(rng, _TD_MON, 1)


def rac_117_hl_range_ac_lag1_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Autocorrelation of (high-low)/close range at lag 1 over 63-day window."""
    rng = _safe_div(high - low, close)
    return _rolling_autocorr(rng, _TD_QTR, 1)


def rac_118_oc_return_ac_lag1_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Autocorrelation of open-to-close return at lag 1 over 21-day window."""
    oc = np.log((close / open_).replace(0, np.nan))
    return _rolling_autocorr(oc, _TD_MON, 1)


def rac_119_oc_return_ac_lag1_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Autocorrelation of open-to-close return at lag 1 over 63-day window."""
    oc = np.log((close / open_).replace(0, np.nan))
    return _rolling_autocorr(oc, _TD_QTR, 1)


def rac_120_co_gap_ac_lag1_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Autocorrelation of close-to-open gap (overnight return) at lag 1 over 21-day window."""
    gap = np.log((open_ / close.shift(1)).replace(0, np.nan))
    return _rolling_autocorr(gap, _TD_MON, 1)


def rac_121_co_gap_ac_lag1_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Autocorrelation of close-to-open gap at lag 1 over 63-day window."""
    gap = np.log((open_ / close.shift(1)).replace(0, np.nan))
    return _rolling_autocorr(gap, _TD_QTR, 1)


def rac_122_hl_range_runs_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Runs ratio of above/below-median (high-low) range over 63-day window."""
    rng = _safe_div(high - low, close)
    med = _rolling_mean(rng, _TD_QTR)
    above = (rng > med).astype(float)
    above_ret = above - above.shift(1)
    return _runs_ratio(above_ret, _TD_QTR)


def rac_123_volume_ac_lag1_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Autocorrelation of log-volume at lag 1 over 21-day window."""
    lv = np.log(volume.replace(0, np.nan))
    return _rolling_autocorr(lv, _TD_MON, 1)


def rac_124_volume_ac_lag1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Autocorrelation of log-volume at lag 1 over 63-day window."""
    lv = np.log(volume.replace(0, np.nan))
    return _rolling_autocorr(lv, _TD_QTR, 1)


def rac_125_ret_vol_cross_ac_lag1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cross-autocorrelation: return_t vs volume_{t-1} lag 1 over 63-day window."""
    r = _log_returns(close)
    lv = np.log(volume.replace(0, np.nan))
    return _rolling_autocorr(r - lv.shift(1), _TD_QTR, 1)


# --- Group M (126-135): Weighted and decayed AC metrics ---

def rac_126_ac_lag1_ewm_diff_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM(21)-smoothed lag-1 AC (velocity of AC trend)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    sm = _ewm_mean(ac, _TD_MON)
    return sm.diff(_TD_WEEK)


def rac_127_ac_weighted_lags1_5_63d(close: pd.Series) -> pd.Series:
    """Lag-1-weighted sum of ACs (lags 1..5 weighted by 1/lag) over 63-day window."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        w = 1.0 / lag
        total = total + w * _rolling_autocorr(r, _TD_QTR, lag).fillna(0.0)
    return total


def rac_128_ac_decay_ratio_lags1_5_63d(close: pd.Series) -> pd.Series:
    """Ratio |AC lag 1| / (sum |AC lags 2-5|) over 63-day window (AC decay shape)."""
    r = _log_returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1).abs().fillna(0.0)
    rest = pd.Series(0.0, index=close.index)
    for lag in range(2, 6):
        rest = rest + _rolling_autocorr(r, _TD_QTR, lag).abs().fillna(0.0)
    return _safe_div(ac1, rest + _EPS)


def rac_129_sign_ac_lag1_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day sign-AC lag 1 within its 252-day distribution."""
    r = _log_returns(close)
    sac = _rolling_autocorr(np.sign(r), _TD_QTR, 1)
    return sac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_130_abs_ac_lag1_minus_sign_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """|AC(|r|, lag1)| - |AC(sign(r), lag1)| over 63-day window (magnitude vs direction AC)."""
    r = _log_returns(close)
    abs_ac = _abs_autocorr(r, _TD_QTR, 1)
    sign_ac = _rolling_autocorr(np.sign(r), _TD_QTR, 1)
    return abs_ac.abs() - sign_ac.abs()


def rac_131_ac_lag1_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Difference: 21-day AC lag 1 minus 63-day AC lag 1 (short vs long serial structure)."""
    r = _log_returns(close)
    ac21 = _rolling_autocorr(r, _TD_MON, 1)
    ac63 = _rolling_autocorr(r, _TD_QTR, 1)
    return ac21 - ac63


def rac_132_ac_lag1_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Difference: 63-day AC lag 1 minus 252-day AC lag 1."""
    r = _log_returns(close)
    ac63 = _rolling_autocorr(r, _TD_QTR, 1)
    ac252 = _rolling_autocorr(r, _TD_YEAR, 1)
    return ac63 - ac252


def rac_133_ac_lag1_trend_21d(close: pd.Series) -> pd.Series:
    """21-day OLS slope of the 21-day lag-1 AC time series (trend in serial structure)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    def _slope(x):
        arr = x[~np.isnan(x)]
        if len(arr) < 3:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den > _EPS else np.nan
    return ac.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(_slope, raw=True)


def rac_134_hurst_vs_vr5_diff_126d(close: pd.Series) -> pd.Series:
    """Hurst R/S (126d) minus VR(k=5) 126d (corroboration of persistence signal)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    h = _hurst_rs(r, _TD_HALF)
    vr = _variance_ratio(lp, _TD_HALF, 5)
    return h - vr


def rac_135_ac_lag1_times_hurst_126d(close: pd.Series) -> pd.Series:
    """Product of 63-day AC lag 1 and Hurst R/S (126d) (combined persistence score)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    h = _hurst_rs(r, _TD_HALF)
    return ac * h


# --- Group N (136-150): Cross-lag, rolling min/max of AC, and distress composites ---

def rac_136_ac_lag1_min_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of the 21-day lag-1 AC."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_min(ac, _TD_YEAR)


def rac_137_ac_lag1_max_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day maximum of the 21-day lag-1 AC."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_max(ac, _TD_YEAR)


def rac_138_ac_lag1_range_252d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 21-day lag-1 AC over 252-day window (AC volatility)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_max(ac, _TD_YEAR) - _rolling_min(ac, _TD_YEAR)


def rac_139_vr2_min_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of the 63-day VR(k=2)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    return _rolling_min(vr, _TD_YEAR)


def rac_140_hurst_rs_min_252d_expanding(close: pd.Series) -> pd.Series:
    """Expanding minimum of 126-day Hurst R/S (all-time minimum memory structure)."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_HALF)
    return h.expanding(min_periods=_TD_HALF).min()


def rac_141_consec_days_vr5_below1_126d(close: pd.Series) -> pd.Series:
    """Consecutive days where 126-day VR(k=5) < 1 (mean-reversion regime persistence)."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_HALF, 5)
    return _consec_streak(vr < 1.0)


def rac_142_consec_days_ac_lag1_negative_63d(close: pd.Series) -> pd.Series:
    """Consecutive days where 63-day lag-1 AC < 0."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return _consec_streak(ac < 0)


def rac_143_anti_persist_score_63d(close: pd.Series) -> pd.Series:
    """Anti-persistence score: -AC_lag1 + (1-VR5) + (0.5-Hurst) over 63d / half windows."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    neg_ac = -_rolling_autocorr(r, _TD_QTR, 1).fillna(0.0)
    neg_vr = (1.0 - _variance_ratio(lp, _TD_QTR, 5).fillna(1.0))
    neg_h = (0.5 - _hurst_rs(r, _TD_QTR).fillna(0.5))
    return neg_ac + neg_vr + neg_h


def rac_144_persist_score_63d(close: pd.Series) -> pd.Series:
    """Persistence score: AC_lag1 + (VR5-1) + (Hurst-0.5) over 63d windows."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1).fillna(0.0)
    vr = (_variance_ratio(lp, _TD_QTR, 5).fillna(1.0) - 1.0)
    h = (_hurst_rs(r, _TD_QTR).fillna(0.5) - 0.5)
    return ac + vr + h


def rac_145_ac_lag1_depth_below_neg01_63d(close: pd.Series) -> pd.Series:
    """Depth of 63-day lag-1 AC below -0.1 (degree of mean-reversion signal, clipped 0)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return (-0.1 - ac).clip(lower=0.0)


def rac_146_runs_ratio_min_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of the 63-day runs ratio."""
    r = _log_returns(close)
    rr = _runs_ratio(r, _TD_QTR)
    return _rolling_min(rr, _TD_YEAR)


def rac_147_abs_ac_lag1_trend_21d(close: pd.Series) -> pd.Series:
    """21-day OLS slope of 21-day |returns| lag-1 AC (trend in volatility clustering)."""
    r = _log_returns(close)
    aac = _abs_autocorr(r, _TD_MON, 1)
    def _slope(x):
        arr = x[~np.isnan(x)]
        if len(arr) < 3:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den > _EPS else np.nan
    return aac.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(_slope, raw=True)


def rac_148_lb_q4_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day LB(4) Q-stat vs its 252-day distribution."""
    r = _log_returns(close)
    def _lb(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < 6:
            return np.nan
        q = 0.0
        for k in range(1, 5):
            x1 = arr[:-k]
            x2 = arr[k:]
            m1, m2 = x1.mean(), x2.mean()
            num = ((x1 - m1) * (x2 - m2)).mean()
            den = x1.std(ddof=0) * x2.std(ddof=0)
            rk = num / den if den > _EPS else 0.0
            q += rk ** 2 / (n - k)
        return n * (n + 2) * q
    q_stat = r.rolling(_TD_MON, min_periods=max(6, _TD_MON // 2)).apply(_lb, raw=True)
    m = _rolling_mean(q_stat, _TD_YEAR)
    s = _rolling_std(q_stat, _TD_YEAR)
    return _safe_div(q_stat - m, s)


def rac_149_sign_ac_lag1_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Difference: 21-day sign-AC lag 1 minus 63-day sign-AC lag 1."""
    r = _log_returns(close)
    sac21 = _rolling_autocorr(np.sign(r), _TD_MON, 1)
    sac63 = _rolling_autocorr(np.sign(r), _TD_QTR, 1)
    return sac21 - sac63


def rac_150_serial_structure_composite_252d(close: pd.Series) -> pd.Series:
    """Long-run composite: (AC_lag1 + VR(5)-1 + Hurst-0.5) averaged over 252d AC/VR/Hurst."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_YEAR, 1).fillna(0.0)
    vr = (_variance_ratio(lp, _TD_YEAR, 5).fillna(1.0) - 1.0)
    h = (_hurst_rs(r, _TD_YEAR).fillna(0.5) - 0.5)
    return (ac + vr + h) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_AUTOCORRELATION_REGISTRY_076_150 = {
    "rac_076_abs_ac_lag1_21d": {"inputs": ["close"], "func": rac_076_abs_ac_lag1_21d},
    "rac_077_abs_ac_lag1_63d": {"inputs": ["close"], "func": rac_077_abs_ac_lag1_63d},
    "rac_078_abs_ac_lag1_126d": {"inputs": ["close"], "func": rac_078_abs_ac_lag1_126d},
    "rac_079_abs_ac_lag2_63d": {"inputs": ["close"], "func": rac_079_abs_ac_lag2_63d},
    "rac_080_abs_ac_lag5_63d": {"inputs": ["close"], "func": rac_080_abs_ac_lag5_63d},
    "rac_081_abs_ac_lag1_pct_rank_252d": {"inputs": ["close"], "func": rac_081_abs_ac_lag1_pct_rank_252d},
    "rac_082_abs_ac_sum_lags1_5_63d": {"inputs": ["close"], "func": rac_082_abs_ac_sum_lags1_5_63d},
    "rac_083_abs_ac_lag1_zscore_252d": {"inputs": ["close"], "func": rac_083_abs_ac_lag1_zscore_252d},
    "rac_084_squared_ac_lag1_63d": {"inputs": ["close"], "func": rac_084_squared_ac_lag1_63d},
    "rac_085_squared_ac_lag1_126d": {"inputs": ["close"], "func": rac_085_squared_ac_lag1_126d},
    "rac_086_ac_lag4_63d": {"inputs": ["close"], "func": rac_086_ac_lag4_63d},
    "rac_087_ac_lag5_252d": {"inputs": ["close"], "func": rac_087_ac_lag5_252d},
    "rac_088_ac_lag10_126d": {"inputs": ["close"], "func": rac_088_ac_lag10_126d},
    "rac_089_ac_lag10_252d": {"inputs": ["close"], "func": rac_089_ac_lag10_252d},
    "rac_090_ac_lag21_252d": {"inputs": ["close"], "func": rac_090_ac_lag21_252d},
    "rac_091_ac_lag2_126d": {"inputs": ["close"], "func": rac_091_ac_lag2_126d},
    "rac_092_ac_lag3_126d": {"inputs": ["close"], "func": rac_092_ac_lag3_126d},
    "rac_093_ac_lag4_126d": {"inputs": ["close"], "func": rac_093_ac_lag4_126d},
    "rac_094_ac_lag2_252d": {"inputs": ["close"], "func": rac_094_ac_lag2_252d},
    "rac_095_ac_lag3_252d": {"inputs": ["close"], "func": rac_095_ac_lag3_252d},
    "rac_096_hurst_rs_63d": {"inputs": ["close"], "func": rac_096_hurst_rs_63d},
    "rac_097_hurst_rs_126d": {"inputs": ["close"], "func": rac_097_hurst_rs_126d},
    "rac_098_hurst_rs_252d": {"inputs": ["close"], "func": rac_098_hurst_rs_252d},
    "rac_099_hurst_rs_63d_minus_half": {"inputs": ["close"], "func": rac_099_hurst_rs_63d_minus_half},
    "rac_100_hurst_rs_126d_minus_half": {"inputs": ["close"], "func": rac_100_hurst_rs_126d_minus_half},
    "rac_101_hurst_rs_63d_pct_rank_252d": {"inputs": ["close"], "func": rac_101_hurst_rs_63d_pct_rank_252d},
    "rac_102_hurst_rs_63d_zscore_252d": {"inputs": ["close"], "func": rac_102_hurst_rs_63d_zscore_252d},
    "rac_103_hurst_above_half_flag_63d": {"inputs": ["close"], "func": rac_103_hurst_above_half_flag_63d},
    "rac_104_hurst_below_half_flag_63d": {"inputs": ["close"], "func": rac_104_hurst_below_half_flag_63d},
    "rac_105_hurst_rs_min_252d": {"inputs": ["close"], "func": rac_105_hurst_rs_min_252d},
    "rac_106_vr_2_252d": {"inputs": ["close"], "func": rac_106_vr_2_252d},
    "rac_107_vr_10_63d": {"inputs": ["close"], "func": rac_107_vr_10_63d},
    "rac_108_vr_21_126d": {"inputs": ["close"], "func": rac_108_vr_21_126d},
    "rac_109_vr_63_252d": {"inputs": ["close"], "func": rac_109_vr_63_252d},
    "rac_110_vr_2_zscore_252d": {"inputs": ["close"], "func": rac_110_vr_2_zscore_252d},
    "rac_111_vr_5_zscore_252d": {"inputs": ["close"], "func": rac_111_vr_5_zscore_252d},
    "rac_112_vr_ratio_10_to_2_252d": {"inputs": ["close"], "func": rac_112_vr_ratio_10_to_2_252d},
    "rac_113_vr_21_minus1_252d": {"inputs": ["close"], "func": rac_113_vr_21_minus1_252d},
    "rac_114_vr_5_pct_rank_252d": {"inputs": ["close"], "func": rac_114_vr_5_pct_rank_252d},
    "rac_115_vr_2_expanding_min": {"inputs": ["close"], "func": rac_115_vr_2_expanding_min},
    "rac_116_hl_range_ac_lag1_21d": {"inputs": ["close", "high", "low"], "func": rac_116_hl_range_ac_lag1_21d},
    "rac_117_hl_range_ac_lag1_63d": {"inputs": ["close", "high", "low"], "func": rac_117_hl_range_ac_lag1_63d},
    "rac_118_oc_return_ac_lag1_21d": {"inputs": ["close", "open"], "func": rac_118_oc_return_ac_lag1_21d},
    "rac_119_oc_return_ac_lag1_63d": {"inputs": ["close", "open"], "func": rac_119_oc_return_ac_lag1_63d},
    "rac_120_co_gap_ac_lag1_21d": {"inputs": ["close", "open"], "func": rac_120_co_gap_ac_lag1_21d},
    "rac_121_co_gap_ac_lag1_63d": {"inputs": ["close", "open"], "func": rac_121_co_gap_ac_lag1_63d},
    "rac_122_hl_range_runs_ratio_63d": {"inputs": ["close", "high", "low"], "func": rac_122_hl_range_runs_ratio_63d},
    "rac_123_volume_ac_lag1_21d": {"inputs": ["close", "volume"], "func": rac_123_volume_ac_lag1_21d},
    "rac_124_volume_ac_lag1_63d": {"inputs": ["close", "volume"], "func": rac_124_volume_ac_lag1_63d},
    "rac_125_ret_vol_cross_ac_lag1_63d": {"inputs": ["close", "volume"], "func": rac_125_ret_vol_cross_ac_lag1_63d},
    "rac_126_ac_lag1_ewm_diff_5d": {"inputs": ["close"], "func": rac_126_ac_lag1_ewm_diff_5d},
    "rac_127_ac_weighted_lags1_5_63d": {"inputs": ["close"], "func": rac_127_ac_weighted_lags1_5_63d},
    "rac_128_ac_decay_ratio_lags1_5_63d": {"inputs": ["close"], "func": rac_128_ac_decay_ratio_lags1_5_63d},
    "rac_129_sign_ac_lag1_pct_rank_252d": {"inputs": ["close"], "func": rac_129_sign_ac_lag1_pct_rank_252d},
    "rac_130_abs_ac_lag1_minus_sign_ac_lag1_63d": {"inputs": ["close"], "func": rac_130_abs_ac_lag1_minus_sign_ac_lag1_63d},
    "rac_131_ac_lag1_21d_vs_63d": {"inputs": ["close"], "func": rac_131_ac_lag1_21d_vs_63d},
    "rac_132_ac_lag1_63d_vs_252d": {"inputs": ["close"], "func": rac_132_ac_lag1_63d_vs_252d},
    "rac_133_ac_lag1_trend_21d": {"inputs": ["close"], "func": rac_133_ac_lag1_trend_21d},
    "rac_134_hurst_vs_vr5_diff_126d": {"inputs": ["close"], "func": rac_134_hurst_vs_vr5_diff_126d},
    "rac_135_ac_lag1_times_hurst_126d": {"inputs": ["close"], "func": rac_135_ac_lag1_times_hurst_126d},
    "rac_136_ac_lag1_min_252d": {"inputs": ["close"], "func": rac_136_ac_lag1_min_252d},
    "rac_137_ac_lag1_max_252d": {"inputs": ["close"], "func": rac_137_ac_lag1_max_252d},
    "rac_138_ac_lag1_range_252d": {"inputs": ["close"], "func": rac_138_ac_lag1_range_252d},
    "rac_139_vr2_min_252d": {"inputs": ["close"], "func": rac_139_vr2_min_252d},
    "rac_140_hurst_rs_min_252d_expanding": {"inputs": ["close"], "func": rac_140_hurst_rs_min_252d_expanding},
    "rac_141_consec_days_vr5_below1_126d": {"inputs": ["close"], "func": rac_141_consec_days_vr5_below1_126d},
    "rac_142_consec_days_ac_lag1_negative_63d": {"inputs": ["close"], "func": rac_142_consec_days_ac_lag1_negative_63d},
    "rac_143_anti_persist_score_63d": {"inputs": ["close"], "func": rac_143_anti_persist_score_63d},
    "rac_144_persist_score_63d": {"inputs": ["close"], "func": rac_144_persist_score_63d},
    "rac_145_ac_lag1_depth_below_neg01_63d": {"inputs": ["close"], "func": rac_145_ac_lag1_depth_below_neg01_63d},
    "rac_146_runs_ratio_min_252d": {"inputs": ["close"], "func": rac_146_runs_ratio_min_252d},
    "rac_147_abs_ac_lag1_trend_21d": {"inputs": ["close"], "func": rac_147_abs_ac_lag1_trend_21d},
    "rac_148_lb_q4_21d_zscore_252d": {"inputs": ["close"], "func": rac_148_lb_q4_21d_zscore_252d},
    "rac_149_sign_ac_lag1_21d_vs_63d": {"inputs": ["close"], "func": rac_149_sign_ac_lag1_21d_vs_63d},
    "rac_150_serial_structure_composite_252d": {"inputs": ["close"], "func": rac_150_serial_structure_composite_252d},
}
