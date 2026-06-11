"""
28_return_distribution — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative return-distribution features — acceleration
        of velocity of skewness, kurtosis, VaR/CVaR, Hurst exponent, Shannon entropy,
        permutation entropy, autocorrelation, tail distress composite.
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


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


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


# ── Hurst R/S scalar (self-contained) ────────────────────────────────────────

def _hurst_rs_scalar(arr: np.ndarray) -> float:
    n = len(arr)
    if n < 8:
        return np.nan
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    mean_a = a.mean()
    dev = a - mean_a
    cumdev = np.cumsum(dev)
    r = cumdev.max() - cumdev.min()
    s = a.std(ddof=1)
    if s < _EPS or r < _EPS:
        return np.nan
    return np.log(r / s) / np.log(n)


# ── Shannon entropy scalar (self-contained) ───────────────────────────────────

def _shannon_8bins(arr: np.ndarray) -> float:
    a = arr[~np.isnan(arr)]
    if len(a) < 8:
        return np.nan
    mn, mx = a.min(), a.max()
    if mx - mn < _EPS:
        return 0.0
    bins = np.linspace(mn, mx, 9)
    counts, _ = np.histogram(a, bins=bins)
    total = counts.sum()
    if total == 0:
        return np.nan
    probs = counts / total
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log2(probs)))


# ── Autocorrelation scalar (self-contained) ───────────────────────────────────

def _autocorr_lag1_scalar(arr: np.ndarray) -> float:
    if len(arr) <= 3:
        return np.nan
    x = arr[:-1]
    y = arr[1:]
    mx, my = x.mean(), y.mean()
    num = ((x - mx) * (y - my)).sum()
    denom = np.sqrt(((x - mx) ** 2).sum() * ((y - my) ** 2).sum())
    if denom < _EPS:
        return np.nan
    return num / denom


def _abs_autocorr_lag1_scalar(arr: np.ndarray) -> float:
    return _autocorr_lag1_scalar(np.abs(arr))


def _ljung_box_scalar(arr: np.ndarray) -> float:
    n = len(arr)
    nlags = 5
    if n <= nlags + 2:
        return np.nan
    lb = 0.0
    for k in range(1, nlags + 1):
        a_k = arr[k:]
        a_0 = arr[:-k]
        mx, my = a_0.mean(), a_k.mean()
        num = ((a_0 - mx) * (a_k - my)).sum()
        denom = np.sqrt(((a_0 - mx) ** 2).sum() * ((a_k - my) ** 2).sum())
        if denom < _EPS:
            return np.nan
        ac = num / denom
        d = n - k
        if d <= 0:
            return np.nan
        lb += ac * ac / d
    return n * (n + 2) * lb


# ── Permutation entropy scalar (self-contained) ───────────────────────────────

def _perm_entropy_order3(arr: np.ndarray) -> float:
    from math import factorial
    a = arr[~np.isnan(arr)]
    n = len(a)
    order = 3
    if n < order + 2:
        return np.nan
    counts = {}
    for i in range(n - order + 1):
        pattern = tuple(np.argsort(a[i:i + order], kind='stable'))
        counts[pattern] = counts.get(pattern, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return np.nan
    probs = np.array(list(counts.values()), dtype=float) / total
    probs = probs[probs > 0]
    entropy = -np.sum(probs * np.log2(probs))
    max_entropy = np.log2(float(factorial(order)))
    if max_entropy < _EPS:
        return np.nan
    return entropy / max_entropy


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each = diff/slope of a 2nd-derivative concept (acceleration)

def rds_drv3_001_skew_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day skewness (acceleration of skew velocity)."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    vel = sk.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_002_skew_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21-day skewness (jerk in skew)."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    vel21 = sk.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_003_kurt_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day kurtosis (acceleration of kurtosis change)."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    vel = kt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_004_var_5pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VaR-5% (acceleration of tail worsening)."""
    v = _rolling_quantile(_log_ret(close), _TD_MON, 0.05)
    vel = v.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_005_cvar_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CVaR-5%."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    cv = r.where(r < q05, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_006_jb_stat_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day JB statistic."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    jb = (_TD_QTR / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
    vel21 = jb.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_007_tail_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day tail ratio."""
    r = _log_ret(close)
    tr = _safe_div(
        _rolling_quantile(r, _TD_QTR, 0.05).abs(),
        _rolling_quantile(r, _TD_QTR, 0.95).abs()
    )
    vel21 = tr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_008_down_up_std_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day downside/upside std ratio."""
    r = _log_ret(close)
    ds = r.where(r < 0, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    us = r.where(r > 0, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    ratio = _safe_div(ds, us)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_009_skew_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day skewness over 63 days (rate of slope change)."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    slp = _linslope(sk, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_drv3_010_kurt_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day kurtosis over 63 days."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    slp = _linslope(kt, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_drv3_011_hurst_rs_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day R/S Hurst (acceleration of regime-change velocity)."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    vel = h.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_012_hurst_rs_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day R/S Hurst (Hurst jerk)."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    vel21 = h.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_013_hurst_rs_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day Hurst over 63 days."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    slp = _linslope(h, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_drv3_014_shannon_entropy_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Shannon entropy (acceleration of entropy change)."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    vel = e.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_015_shannon_entropy_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day Shannon entropy (entropy jerk)."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    vel21 = e.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_016_shannon_entropy_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day Shannon entropy over 63 days."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    slp = _linslope(e, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_drv3_017_perm_entropy_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day permutation entropy (acceleration of disorder change)."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _perm_entropy_order3, raw=True
    )
    vel = e.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_018_autocorr_lag1_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day lag-1 autocorrelation (acceleration of AC change)."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _autocorr_lag1_scalar, raw=True
    )
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_019_autocorr_lag1_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day lag-1 autocorrelation (AC jerk)."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _autocorr_lag1_scalar, raw=True
    )
    vel21 = ac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_020_abs_ret_autocorr_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day |return| autocorrelation (vol clustering acceleration)."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _abs_autocorr_lag1_scalar, raw=True
    )
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_021_ljung_box_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Ljung-Box aggregate (AC structure acceleration)."""
    r = _log_ret(close)
    lb = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _ljung_box_scalar, raw=True
    )
    vel = lb.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_drv3_022_tail_distress_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day tail distress composite."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    v5 = _rolling_quantile(r, _TD_QTR, 0.05).abs()
    composite = (-sk) * (kt + 3.0) * v5
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_drv3_023_skew_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day skewness."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    vel = sk.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rds_drv3_024_hurst_entropy_composite_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Hurst*entropy composite (regime-disorder velocity)."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    composite = h * e
    return composite.diff(_TD_WEEK)


def rds_drv3_025_kurt_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day kurtosis."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    vel = kt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_REGISTRY_3RD_DERIVATIVES = {
    "rds_drv3_001_skew_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_001_skew_21d_5d_diff_5d_diff},
    "rds_drv3_002_skew_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_002_skew_21d_21d_diff_5d_diff},
    "rds_drv3_003_kurt_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_003_kurt_21d_5d_diff_5d_diff},
    "rds_drv3_004_var_5pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_004_var_5pct_21d_5d_diff_5d_diff},
    "rds_drv3_005_cvar_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_005_cvar_63d_21d_diff_5d_diff},
    "rds_drv3_006_jb_stat_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_006_jb_stat_63d_21d_diff_5d_diff},
    "rds_drv3_007_tail_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_007_tail_ratio_63d_21d_diff_5d_diff},
    "rds_drv3_008_down_up_std_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_008_down_up_std_ratio_21d_5d_diff_5d_diff},
    "rds_drv3_009_skew_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_drv3_009_skew_21d_slope_63d_5d_diff},
    "rds_drv3_010_kurt_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_drv3_010_kurt_21d_slope_63d_5d_diff},
    "rds_drv3_011_hurst_rs_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_011_hurst_rs_63d_5d_diff_5d_diff},
    "rds_drv3_012_hurst_rs_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_012_hurst_rs_63d_21d_diff_5d_diff},
    "rds_drv3_013_hurst_rs_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_drv3_013_hurst_rs_slope_63d_5d_diff},
    "rds_drv3_014_shannon_entropy_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_014_shannon_entropy_63d_5d_diff_5d_diff},
    "rds_drv3_015_shannon_entropy_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_015_shannon_entropy_63d_21d_diff_5d_diff},
    "rds_drv3_016_shannon_entropy_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_drv3_016_shannon_entropy_slope_63d_5d_diff},
    "rds_drv3_017_perm_entropy_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_017_perm_entropy_63d_5d_diff_5d_diff},
    "rds_drv3_018_autocorr_lag1_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_018_autocorr_lag1_63d_5d_diff_5d_diff},
    "rds_drv3_019_autocorr_lag1_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_019_autocorr_lag1_63d_21d_diff_5d_diff},
    "rds_drv3_020_abs_ret_autocorr_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_020_abs_ret_autocorr_63d_5d_diff_5d_diff},
    "rds_drv3_021_ljung_box_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_021_ljung_box_63d_5d_diff_5d_diff},
    "rds_drv3_022_tail_distress_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_drv3_022_tail_distress_63d_21d_diff_5d_diff},
    "rds_drv3_023_skew_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": rds_drv3_023_skew_21d_5d_diff_slope_21d},
    "rds_drv3_024_hurst_entropy_composite_63d_5d_diff": {"inputs": ["close"], "func": rds_drv3_024_hurst_entropy_composite_63d_5d_diff},
    "rds_drv3_025_kurt_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": rds_drv3_025_kurt_21d_5d_diff_slope_21d},
}
