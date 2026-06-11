"""
28_return_distribution — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base return-distribution shape features — velocity of skewness,
        kurtosis, VaR/CVaR, Hurst exponent, Shannon entropy, permutation entropy,
        autocorrelation, tail distress composite, downside dispersion.
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


# ── Hurst scalar helper (self-contained) ─────────────────────────────────────

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
    rs = r / s
    return np.log(rs) / np.log(n)


# ── Shannon entropy scalar helper (self-contained) ────────────────────────────

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


# ── Autocorrelation scalar helper (self-contained) ───────────────────────────

def _autocorr_lag1_scalar(arr: np.ndarray) -> float:
    n = len(arr)
    if n <= 3:
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
        denom2 = n - k
        if denom2 <= 0:
            return np.nan
        lb += ac * ac / denom2
    return n * (n + 2) * lb


# ── Permutation entropy scalar helper (self-contained) ───────────────────────

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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rds_drv2_001_skew_logret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-return skewness (velocity of shape change)."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    return sk.diff(_TD_WEEK)


def rds_drv2_002_skew_logret_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day log-return skewness (monthly velocity)."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    return sk.diff(_TD_MON)


def rds_drv2_003_kurt_logret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-return kurtosis."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    return kt.diff(_TD_WEEK)


def rds_drv2_004_kurt_logret_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day log-return kurtosis."""
    kt = _rolling_kurt(_log_ret(close), _TD_QTR)
    return kt.diff(_TD_MON)


def rds_drv2_005_var_5pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day VaR-5% (velocity of tail worsening)."""
    v = _rolling_quantile(_log_ret(close), _TD_MON, 0.05)
    return v.diff(_TD_WEEK)


def rds_drv2_006_cvar_5pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day CVaR-5%."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    cv = r.where(r < q05, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return cv.diff(_TD_MON)


def rds_drv2_007_tail_ratio_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day tail ratio (5th/95th pct)."""
    r = _log_ret(close)
    tr = _safe_div(
        _rolling_quantile(r, _TD_QTR, 0.05).abs(),
        _rolling_quantile(r, _TD_QTR, 0.95).abs()
    )
    return tr.diff(_TD_MON)


def rds_drv2_008_down_vs_up_std_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day downside/upside std ratio."""
    r = _log_ret(close)
    ds = r.where(r < 0, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    us = r.where(r > 0, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    ratio = _safe_div(ds, us)
    return ratio.diff(_TD_WEEK)


def rds_drv2_009_jb_stat_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Jarque-Bera statistic."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    jb = (_TD_QTR / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
    return jb.diff(_TD_MON)


def rds_drv2_010_skew_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day skewness over trailing 63 days."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    return _linslope(sk, _TD_QTR)


def rds_drv2_011_kurt_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day kurtosis over trailing 63 days."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    return _linslope(kt, _TD_QTR)


def rds_drv2_012_var5pct_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day VaR-5% over trailing 63 days."""
    v = _rolling_quantile(_log_ret(close), _TD_MON, 0.05)
    return _linslope(v, _TD_QTR)


def rds_drv2_013_hurst_rs_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day R/S Hurst exponent (velocity of regime shift)."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    return h.diff(_TD_WEEK)


def rds_drv2_014_hurst_rs_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day R/S Hurst exponent."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    return h.diff(_TD_MON)


def rds_drv2_015_hurst_rs_63d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day R/S Hurst over trailing 63 days."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    return _linslope(h, _TD_QTR)


def rds_drv2_016_shannon_entropy_8bins_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Shannon entropy (8-bin) of log-returns."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    return e.diff(_TD_WEEK)


def rds_drv2_017_shannon_entropy_8bins_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Shannon entropy (8-bin)."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    return e.diff(_TD_MON)


def rds_drv2_018_shannon_entropy_63d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day Shannon entropy over trailing 63 days."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )
    return _linslope(e, _TD_QTR)


def rds_drv2_019_perm_entropy_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day permutation entropy (order 3)."""
    r = _log_ret(close)
    e = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _perm_entropy_order3, raw=True
    )
    return e.diff(_TD_WEEK)


def rds_drv2_020_autocorr_lag1_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day lag-1 autocorrelation of log-returns."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _autocorr_lag1_scalar, raw=True
    )
    return ac.diff(_TD_WEEK)


def rds_drv2_021_autocorr_lag1_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day lag-1 autocorrelation."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _autocorr_lag1_scalar, raw=True
    )
    return ac.diff(_TD_MON)


def rds_drv2_022_abs_ret_autocorr_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day |return| lag-1 autocorrelation (vol clustering velocity)."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _abs_autocorr_lag1_scalar, raw=True
    )
    return ac.diff(_TD_WEEK)


def rds_drv2_023_ljung_box_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Ljung-Box aggregate (autocorrelation structure velocity)."""
    r = _log_ret(close)
    lb = r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _ljung_box_scalar, raw=True
    )
    return lb.diff(_TD_WEEK)


def rds_drv2_024_tail_distress_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day tail distress composite ((-skew)*(kurt+3)*|VaR-5%|)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    v5 = _rolling_quantile(r, _TD_QTR, 0.05).abs()
    composite = (-sk) * (kt + 3.0) * v5
    return composite.diff(_TD_MON)


def rds_drv2_025_hurst_rs_minus_dfa_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (R/S Hurst - DFA Hurst) divergence (velocity of estimator gap)."""
    from math import factorial

    def _hurst_dfa_scalar(arr: np.ndarray) -> float:
        n = len(arr)
        if n < 16:
            return np.nan
        a = arr[~np.isnan(arr)]
        n = len(a)
        if n < 16:
            return np.nan
        profile = np.cumsum(a - a.mean())
        def _rms(profile, scale):
            nblocks = len(profile) // scale
            if nblocks < 2:
                return np.nan
            flucts = []
            for i in range(nblocks):
                seg = profile[i * scale:(i + 1) * scale]
                x = np.arange(scale, dtype=float)
                xm = x.mean()
                ym = seg.mean()
                denom = ((x - xm) ** 2).sum()
                if denom < _EPS:
                    flucts.append(seg.std())
                    continue
                slope = ((x - xm) * (seg - ym)).sum() / denom
                intercept = ym - slope * xm
                trend = intercept + slope * x
                residuals = seg - trend
                flucts.append(np.sqrt((residuals ** 2).mean()))
            return np.mean(flucts) if flucts else np.nan
        s1 = max(4, n // 4)
        s2 = max(8, n // 2)
        f1 = _rms(profile, s1)
        f2 = _rms(profile, s2)
        if f1 is None or f2 is None or np.isnan(f1) or np.isnan(f2):
            return np.nan
        if f1 < _EPS or f2 < _EPS:
            return np.nan
        return np.log(f2 / f1) / np.log(s2 / s1)

    r = _log_ret(close)
    h_rs = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    h_dfa = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_dfa_scalar, raw=True
    )
    div = h_rs - h_dfa
    return div.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_REGISTRY_2ND_DERIVATIVES = {
    "rds_drv2_001_skew_logret_21d_5d_diff": {"inputs": ["close"], "func": rds_drv2_001_skew_logret_21d_5d_diff},
    "rds_drv2_002_skew_logret_21d_21d_diff": {"inputs": ["close"], "func": rds_drv2_002_skew_logret_21d_21d_diff},
    "rds_drv2_003_kurt_logret_21d_5d_diff": {"inputs": ["close"], "func": rds_drv2_003_kurt_logret_21d_5d_diff},
    "rds_drv2_004_kurt_logret_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_004_kurt_logret_63d_21d_diff},
    "rds_drv2_005_var_5pct_21d_5d_diff": {"inputs": ["close"], "func": rds_drv2_005_var_5pct_21d_5d_diff},
    "rds_drv2_006_cvar_5pct_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_006_cvar_5pct_63d_21d_diff},
    "rds_drv2_007_tail_ratio_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_007_tail_ratio_63d_21d_diff},
    "rds_drv2_008_down_vs_up_std_ratio_21d_5d_diff": {"inputs": ["close"], "func": rds_drv2_008_down_vs_up_std_ratio_21d_5d_diff},
    "rds_drv2_009_jb_stat_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_009_jb_stat_63d_21d_diff},
    "rds_drv2_010_skew_21d_slope_63d": {"inputs": ["close"], "func": rds_drv2_010_skew_21d_slope_63d},
    "rds_drv2_011_kurt_21d_slope_63d": {"inputs": ["close"], "func": rds_drv2_011_kurt_21d_slope_63d},
    "rds_drv2_012_var5pct_21d_slope_63d": {"inputs": ["close"], "func": rds_drv2_012_var5pct_21d_slope_63d},
    "rds_drv2_013_hurst_rs_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_013_hurst_rs_63d_5d_diff},
    "rds_drv2_014_hurst_rs_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_014_hurst_rs_63d_21d_diff},
    "rds_drv2_015_hurst_rs_63d_slope_63d": {"inputs": ["close"], "func": rds_drv2_015_hurst_rs_63d_slope_63d},
    "rds_drv2_016_shannon_entropy_8bins_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_016_shannon_entropy_8bins_63d_5d_diff},
    "rds_drv2_017_shannon_entropy_8bins_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_017_shannon_entropy_8bins_63d_21d_diff},
    "rds_drv2_018_shannon_entropy_63d_slope_63d": {"inputs": ["close"], "func": rds_drv2_018_shannon_entropy_63d_slope_63d},
    "rds_drv2_019_perm_entropy_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_019_perm_entropy_63d_5d_diff},
    "rds_drv2_020_autocorr_lag1_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_020_autocorr_lag1_63d_5d_diff},
    "rds_drv2_021_autocorr_lag1_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_021_autocorr_lag1_63d_21d_diff},
    "rds_drv2_022_abs_ret_autocorr_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_022_abs_ret_autocorr_63d_5d_diff},
    "rds_drv2_023_ljung_box_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_023_ljung_box_63d_5d_diff},
    "rds_drv2_024_tail_distress_63d_21d_diff": {"inputs": ["close"], "func": rds_drv2_024_tail_distress_63d_21d_diff},
    "rds_drv2_025_hurst_rs_minus_dfa_63d_5d_diff": {"inputs": ["close"], "func": rds_drv2_025_hurst_rs_minus_dfa_63d_5d_diff},
}
