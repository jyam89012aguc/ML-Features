"""
109_return_autocorrelation — 2nd Derivatives (Features rac_drv2_001-025)
Domain: rate of change of base return-autocorrelation features — velocity of serial-structure
        behavior, including velocity of autocorrelation, variance ratio, Hurst, runs ratio,
        sign autocorrelation, and Ljung-Box metrics
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


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation. NaN-safe."""
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
    """Rolling variance ratio. NaN-safe."""
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


def _hurst_rs(s: pd.Series, w: int) -> pd.Series:
    """Rolling R/S Hurst exponent. NaN-safe."""
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


def _runs_ratio(s: pd.Series, w: int) -> pd.Series:
    """Rolling runs ratio."""
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


def _ljung_box_stat(s: pd.Series, w: int, max_lag: int) -> pd.Series:
    """Rolling Ljung-Box Q-statistic."""
    def _lb(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(max_lag + 2, w // 2):
            return np.nan
        q = 0.0
        for k in range(1, max_lag + 1):
            x1 = arr[:-k]
            x2 = arr[k:]
            m1, m2 = x1.mean(), x2.mean()
            num = ((x1 - m1) * (x2 - m2)).mean()
            den = x1.std(ddof=0) * x2.std(ddof=0)
            rk = num / den if den > _EPS else 0.0
            q += rk ** 2 / (n - k)
        return n * (n + 2) * q
    return s.rolling(w, min_periods=max(max_lag + 2, w // 2)).apply(_lb, raw=True)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        arr = x[~np.isnan(x)]
        if len(arr) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rac_drv2_001_ac_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day lag-1 autocorrelation (velocity of AC lag-1 over 63d)."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 1).diff(_TD_WEEK)


def rac_drv2_002_ac_lag1_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day lag-1 autocorrelation (monthly velocity of AC lag-1)."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 1).diff(_TD_MON)


def rac_drv2_003_ac_lag1_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day lag-1 autocorrelation (fast AC velocity)."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_MON, 1).diff(_TD_WEEK)


def rac_drv2_004_vr5_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of VR(k=5) 126-day (velocity of variance ratio)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 5).diff(_TD_WEEK)


def rac_drv2_005_vr5_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of VR(k=5) 126-day (monthly VR velocity)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 5).diff(_TD_MON)


def rac_drv2_006_hurst_rs_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Hurst R/S (velocity of persistence structure)."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_QTR).diff(_TD_WEEK)


def rac_drv2_007_hurst_rs_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hurst R/S (monthly velocity of Hurst)."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_QTR).diff(_TD_MON)


def rac_drv2_008_runs_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day runs ratio (velocity of trend/chop structure)."""
    r = _log_returns(close)
    return _runs_ratio(r, _TD_QTR).diff(_TD_WEEK)


def rac_drv2_009_lb_q4_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day LB(4) Q-statistic (velocity of serial dependence)."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_QTR, 4).diff(_TD_WEEK)


def rac_drv2_010_lb_q4_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day LB(4) Q-statistic."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_QTR, 4).diff(_TD_MON)


def rac_drv2_011_sign_ac_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day sign-AC lag 1 (velocity of directional serial structure)."""
    r = _log_returns(close)
    return _rolling_autocorr(np.sign(r), _TD_QTR, 1).diff(_TD_WEEK)


def rac_drv2_012_abs_ac_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day |returns| lag-1 AC (velocity of volatility clustering)."""
    r = _log_returns(close)
    return _rolling_autocorr(r.abs(), _TD_QTR, 1).diff(_TD_WEEK)


def rac_drv2_013_ac_lag1_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day lag-1 AC time series."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return _linslope(ac, _TD_MON)


def rac_drv2_014_vr2_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day VR(k=2) (fast variance ratio velocity)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 2).diff(_TD_WEEK)


def rac_drv2_015_ac_sum_lags1_5_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of sum |AC lags 1-5| over 63-day window."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(r, _TD_QTR, lag).abs().fillna(0.0)
    return total.diff(_TD_WEEK)


def rac_drv2_016_hurst_rs_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 126-day Hurst R/S."""
    r = _log_returns(close)
    return _hurst_rs(r, _TD_HALF).diff(_TD_WEEK)


def rac_drv2_017_vr5_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day VR(k=5)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 5).diff(_TD_WEEK)


def rac_drv2_018_anti_persist_score_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of anti-persistence composite score (63d AC, VR, Hurst)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    neg_ac = -_rolling_autocorr(r, _TD_QTR, 1).fillna(0.0)
    neg_vr = (1.0 - _variance_ratio(lp, _TD_QTR, 5).fillna(1.0))
    neg_h = (0.5 - _hurst_rs(r, _TD_QTR).fillna(0.5))
    score = neg_ac + neg_vr + neg_h
    return score.diff(_TD_WEEK)


def rac_drv2_019_ac_lag1_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day lag-1 AC time series."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _linslope(ac, _TD_MON)


def rac_drv2_020_vr5_126d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 126-day VR(k=5) time series."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_HALF, 5)
    return _linslope(vr, _TD_MON)


def rac_drv2_021_runs_ratio_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day runs ratio."""
    r = _log_returns(close)
    return _runs_ratio(r, _TD_QTR).diff(_TD_MON)


def rac_drv2_022_ac_lag1_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of 63-day lag-1 AC."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    pct = ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def rac_drv2_023_hurst_rs_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day Hurst R/S time series."""
    r = _log_returns(close)
    h = _hurst_rs(r, _TD_QTR)
    return _linslope(h, _TD_MON)


def rac_drv2_024_consec_negative_ac_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-AC-lag1<0 streak (velocity of mean-reversion regime)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    streak = _consec_streak(ac < 0)
    return streak.diff(_TD_WEEK)


def rac_drv2_025_ac_lag1_63d_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of 63-day lag-1 AC."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    z = _safe_div(ac - m, s)
    return z.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_AUTOCORRELATION_REGISTRY_2ND_DERIVATIVES = {
    "rac_drv2_001_ac_lag1_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_001_ac_lag1_63d_5d_diff},
    "rac_drv2_002_ac_lag1_63d_21d_diff": {"inputs": ["close"], "func": rac_drv2_002_ac_lag1_63d_21d_diff},
    "rac_drv2_003_ac_lag1_21d_5d_diff": {"inputs": ["close"], "func": rac_drv2_003_ac_lag1_21d_5d_diff},
    "rac_drv2_004_vr5_126d_5d_diff": {"inputs": ["close"], "func": rac_drv2_004_vr5_126d_5d_diff},
    "rac_drv2_005_vr5_126d_21d_diff": {"inputs": ["close"], "func": rac_drv2_005_vr5_126d_21d_diff},
    "rac_drv2_006_hurst_rs_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_006_hurst_rs_63d_5d_diff},
    "rac_drv2_007_hurst_rs_63d_21d_diff": {"inputs": ["close"], "func": rac_drv2_007_hurst_rs_63d_21d_diff},
    "rac_drv2_008_runs_ratio_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_008_runs_ratio_63d_5d_diff},
    "rac_drv2_009_lb_q4_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_009_lb_q4_63d_5d_diff},
    "rac_drv2_010_lb_q4_63d_21d_diff": {"inputs": ["close"], "func": rac_drv2_010_lb_q4_63d_21d_diff},
    "rac_drv2_011_sign_ac_lag1_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_011_sign_ac_lag1_63d_5d_diff},
    "rac_drv2_012_abs_ac_lag1_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_012_abs_ac_lag1_63d_5d_diff},
    "rac_drv2_013_ac_lag1_63d_slope_21d": {"inputs": ["close"], "func": rac_drv2_013_ac_lag1_63d_slope_21d},
    "rac_drv2_014_vr2_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_014_vr2_63d_5d_diff},
    "rac_drv2_015_ac_sum_lags1_5_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_015_ac_sum_lags1_5_63d_5d_diff},
    "rac_drv2_016_hurst_rs_126d_5d_diff": {"inputs": ["close"], "func": rac_drv2_016_hurst_rs_126d_5d_diff},
    "rac_drv2_017_vr5_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_017_vr5_63d_5d_diff},
    "rac_drv2_018_anti_persist_score_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_018_anti_persist_score_63d_5d_diff},
    "rac_drv2_019_ac_lag1_21d_slope_21d": {"inputs": ["close"], "func": rac_drv2_019_ac_lag1_21d_slope_21d},
    "rac_drv2_020_vr5_126d_slope_21d": {"inputs": ["close"], "func": rac_drv2_020_vr5_126d_slope_21d},
    "rac_drv2_021_runs_ratio_63d_21d_diff": {"inputs": ["close"], "func": rac_drv2_021_runs_ratio_63d_21d_diff},
    "rac_drv2_022_ac_lag1_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": rac_drv2_022_ac_lag1_pct_rank_252d_5d_diff},
    "rac_drv2_023_hurst_rs_63d_slope_21d": {"inputs": ["close"], "func": rac_drv2_023_hurst_rs_63d_slope_21d},
    "rac_drv2_024_consec_negative_ac_lag1_63d_5d_diff": {"inputs": ["close"], "func": rac_drv2_024_consec_negative_ac_lag1_63d_5d_diff},
    "rac_drv2_025_ac_lag1_63d_zscore_252d_5d_diff": {"inputs": ["close"], "func": rac_drv2_025_ac_lag1_63d_zscore_252d_5d_diff},
}
