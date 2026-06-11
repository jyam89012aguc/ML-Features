"""return_distribution_moments d2 features 001-075 - Pipeline 1b-technical.

150 distinct hypotheses across __base__001_075.py and __base__076_150.py.
Each feature encodes a *different concept*.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers - no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _log_ret(close):
    return _safe_log(close).diff()

def _rolling_skew(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).skew()


def _rolling_kurt(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).kurt()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _rolling_median(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).median()


def _rolling_mad_mean(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    m = s.rolling(n, min_periods=min_periods).mean()
    return (s - m).abs().rolling(n, min_periods=min_periods).mean()


def _rolling_medad(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    med = s.rolling(n, min_periods=min_periods).median()
    return (s - med).abs().rolling(n, min_periods=min_periods).median()


def _bowley_skew(s, n):
    q1 = _rolling_q(s, n, 0.25)
    q2 = _rolling_q(s, n, 0.50)
    q3 = _rolling_q(s, n, 0.75)
    return _safe_div((q3 + q1 - 2.0 * q2), (q3 - q1))


def _moors_kurt(s, n):
    e1 = _rolling_q(s, n, 0.125)
    e2 = _rolling_q(s, n, 0.250)
    e3 = _rolling_q(s, n, 0.375)
    e5 = _rolling_q(s, n, 0.625)
    e6 = _rolling_q(s, n, 0.750)
    e7 = _rolling_q(s, n, 0.875)
    return _safe_div((e7 - e5) + (e3 - e1), e6 - e2)


def _jarque_bera(s, n):
    mp = max(n // 3, 10)
    sk = s.rolling(n, min_periods=mp).skew()
    kt = s.rolling(n, min_periods=mp).kurt()
    cnt = s.rolling(n, min_periods=mp).count()
    return (cnt / 6.0) * (sk ** 2 + 0.25 * (kt ** 2))


def _ks_stat_normal(s, n):
    mp = max(n // 3, 20)
    def _f(w):
        valid = ~np.isnan(w)
        v = w[valid]
        if v.size < mp:
            return np.nan
        mu = v.mean(); sd = v.std()
        if sd == 0:
            return np.nan
        z = (np.sort(v) - mu) / sd
        from math import erf, sqrt
        cdf = 0.5 * (1.0 + np.array([erf(zi / sqrt(2.0)) for zi in z]))
        ec = np.arange(1, len(v) + 1, dtype=float) / float(len(v))
        return float(max(np.max(np.abs(cdf - ec)), np.max(np.abs(cdf - (ec - 1.0 / len(v))))))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _ad_stat_normal(s, n):
    mp = max(n // 3, 20)
    def _f(w):
        valid = ~np.isnan(w)
        v = w[valid]
        if v.size < mp:
            return np.nan
        mu = v.mean(); sd = v.std()
        if sd == 0:
            return np.nan
        z = np.sort((v - mu) / sd)
        from math import erf, sqrt, log
        cdf = 0.5 * (1.0 + np.array([erf(zi / sqrt(2.0)) for zi in z]))
        cdf = np.clip(cdf, 1e-12, 1.0 - 1e-12)
        nv = len(v)
        i = np.arange(1, nv + 1, dtype=float)
        s_sum = ((2.0 * i - 1.0) * (np.log(cdf) + np.log(1.0 - cdf[::-1]))).sum()
        return float(-nv - s_sum / nv)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _shapiro_w_proxy(s, n):
    """Simplified Shapiro-Wilk-like W using ordered-stat correlation with normal scores."""
    mp = max(n // 3, 20)
    def _f(w):
        valid = ~np.isnan(w)
        v = np.sort(w[valid])
        nv = v.size
        if nv < mp:
            return np.nan
        from math import sqrt
        from math import erf
        # Blom plotting positions
        a = (np.arange(1, nv + 1, dtype=float) - 3.0 / 8.0) / (nv + 0.25)
        # Inverse normal via Beasley-Springer rational approx (simplified): use sqrt2 * erfinv
        # We approximate via Newton on erf
        z = np.empty(nv)
        for j in range(nv):
            p = a[j]
            # initial guess
            t = np.sqrt(-2.0 * np.log(min(p, 1.0 - p)))
            x = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (
                1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t ** 3)
            z[j] = -x if p < 0.5 else x
        vmean = v.mean(); zmean = 0.0
        num = ((z - zmean) * (v - vmean)).sum()
        denv = ((v - vmean) ** 2).sum()
        denz = ((z - zmean) ** 2).sum()
        if denv <= 0 or denz <= 0:
            return np.nan
        return float((num * num) / (denv * denz))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _trimmed_mean(s, n, alpha=0.1):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = int(alpha * v.size)
        if v.size - 2 * k <= 0:
            return np.nan
        return float(v[k:v.size - k].mean())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _trimmed_std(s, n, alpha=0.1):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = int(alpha * v.size)
        if v.size - 2 * k <= 1:
            return np.nan
        return float(v[k:v.size - k].std(ddof=1))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _trimmed_skew(s, n, alpha=0.1):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = int(alpha * v.size)
        v = v[k:v.size - k]
        if v.size < 3:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        return float(((v - mu) ** 3).mean() / sd ** 3)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _trimmed_kurt(s, n, alpha=0.1):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = int(alpha * v.size)
        v = v[k:v.size - k]
        if v.size < 4:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        return float(((v - mu) ** 4).mean() / sd ** 4 - 3.0)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _winsor_mean(s, n, alpha=0.05):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        lo = np.quantile(v, alpha); hi = np.quantile(v, 1.0 - alpha)
        v = np.clip(v, lo, hi)
        return float(v.mean())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _winsor_std(s, n, alpha=0.05):
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        lo = np.quantile(v, alpha); hi = np.quantile(v, 1.0 - alpha)
        v = np.clip(v, lo, hi)
        return float(v.std(ddof=1)) if v.size > 1 else np.nan
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hill_index_upper(s, n, k_frac=0.05):
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = max(int(k_frac * v.size), 5)
        if k >= v.size:
            return np.nan
        thr = v[v.size - k - 1]
        tail = v[v.size - k:]
        if thr <= 0 or (tail <= 0).any():
            return np.nan
        return float(1.0 / np.mean(np.log(tail / thr)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hill_index_lower(s, n, k_frac=0.05):
    """Hill on left tail using |negative side|."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        v = -v
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        k = max(int(k_frac * v.size), 5)
        if k >= v.size:
            return np.nan
        thr = v[v.size - k - 1]
        tail = v[v.size - k:]
        if thr <= 0 or (tail <= 0).any():
            return np.nan
        return float(1.0 / np.mean(np.log(tail / thr)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _pickands_index(s, n):
    mp = max(n // 3, 60)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return np.nan
        v = np.sort(v)
        nv = v.size
        k = nv // 4
        if k < 2 or 4 * k > nv:
            return np.nan
        num = v[nv - k] - v[nv - 2 * k]
        den = v[nv - 2 * k] - v[nv - 4 * k]
        if den <= 0:
            return np.nan
        return float((1.0 / np.log(2.0)) * np.log(num / den))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _l_moments(s, n):
    """Return L2/L3/L4 ratios = L-scale, L-skew, L-kurt as a 3-tuple of Series."""
    mp = max(n // 3, 10)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < mp:
            return (np.nan, np.nan, np.nan)
        nv = v.size
        v = np.sort(v)
        i = np.arange(1, nv + 1, dtype=float)
        b0 = v.mean()
        b1 = ((i - 1) / (nv - 1) * v).mean() if nv > 1 else np.nan
        b2 = ((i - 1) * (i - 2) / ((nv - 1) * (nv - 2)) * v).mean() if nv > 2 else np.nan
        b3 = ((i - 1) * (i - 2) * (i - 3) / ((nv - 1) * (nv - 2) * (nv - 3)) * v).mean() if nv > 3 else np.nan
        l1 = b0
        l2 = 2 * b1 - b0
        l3 = 6 * b2 - 6 * b1 + b0 if nv > 2 else np.nan
        l4 = 20 * b3 - 30 * b2 + 12 * b1 - b0 if nv > 3 else np.nan
        if not np.isfinite(l2) or l2 == 0:
            return (np.nan, np.nan, np.nan)
        return (float(l2), float(l3 / l2) if np.isfinite(l3) else np.nan,
                float(l4 / l2) if np.isfinite(l4) else np.nan)
    # apply once then split
    arr = s.values
    out2 = np.full(len(arr), np.nan); out3 = np.full(len(arr), np.nan); out4 = np.full(len(arr), np.nan)
    for i in range(len(arr)):
        lo = max(0, i - n + 1)
        v2, v3, v4 = _f(arr[lo:i + 1])
        out2[i], out3[i], out4[i] = v2, v3, v4
    return (pd.Series(out2, index=s.index), pd.Series(out3, index=s.index),
            pd.Series(out4, index=s.index))


def _runs_test_z(s, n):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < mp:
            return np.nan
        sgn = np.where(v > 0, 1, -1)
        n_pos = int((sgn > 0).sum()); n_neg = nv - n_pos
        if n_pos == 0 or n_neg == 0:
            return np.nan
        runs = 1 + int((sgn[1:] != sgn[:-1]).sum())
        mu = 2.0 * n_pos * n_neg / nv + 1.0
        var = (mu - 1.0) * (mu - 2.0) / (nv - 1.0) if nv > 1 else 0.0
        if var <= 0:
            return np.nan
        return float((runs - mu) / np.sqrt(var))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def f41_rdmm_001_mean_log_ret_21d_monthly_drift_d2(close: pd.Series) -> pd.Series:
    """Mean of daily log-returns over 21d - drift at that horizon."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_002_mean_log_ret_63d_quarterly_drift_d2(close: pd.Series) -> pd.Series:
    """Mean of daily log-returns over 63d - drift at that horizon."""
    r = _log_ret(close)
    return (r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_003_mean_log_ret_252d_annual_drift_d2(close: pd.Series) -> pd.Series:
    """Mean of daily log-returns over 252d - drift at that horizon."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_004_std_log_ret_21d_monthly_vol_d2(close: pd.Series) -> pd.Series:
    """Std of daily log-returns over 21d - realized vol at that horizon."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).std()).diff().diff()

def f41_rdmm_005_std_log_ret_63d_quarterly_vol_d2(close: pd.Series) -> pd.Series:
    """Std of daily log-returns over 63d - realized vol at that horizon."""
    r = _log_ret(close)
    return (r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).std()).diff().diff()

def f41_rdmm_006_std_log_ret_252d_annual_vol_d2(close: pd.Series) -> pd.Series:
    """Std of daily log-returns over 252d - realized vol at that horizon."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).std()).diff().diff()

def f41_rdmm_007_skew_log_ret_21d_monthly_skew_d2(close: pd.Series) -> pd.Series:
    """Skewness of daily log-returns over 21d - asymmetry at that scale."""
    r = _log_ret(close)
    return (_rolling_skew(r, MDAYS)).diff().diff()

def f41_rdmm_008_skew_log_ret_63d_quarterly_skew_d2(close: pd.Series) -> pd.Series:
    """Skewness of daily log-returns over 63d - asymmetry at that scale."""
    r = _log_ret(close)
    return (_rolling_skew(r, QDAYS)).diff().diff()

def f41_rdmm_009_skew_log_ret_252d_annual_skew_d2(close: pd.Series) -> pd.Series:
    """Skewness of daily log-returns over 252d - asymmetry at that scale."""
    r = _log_ret(close)
    return (_rolling_skew(r, YDAYS)).diff().diff()

def f41_rdmm_010_excess_kurt_log_ret_21d_monthly_kurt_d2(close: pd.Series) -> pd.Series:
    """Excess kurtosis (Fisher) of daily log-returns over 21d - tail fatness."""
    r = _log_ret(close)
    return (_rolling_kurt(r, MDAYS)).diff().diff()

def f41_rdmm_011_excess_kurt_log_ret_63d_quarterly_kurt_d2(close: pd.Series) -> pd.Series:
    """Excess kurtosis (Fisher) of daily log-returns over 63d - tail fatness."""
    r = _log_ret(close)
    return (_rolling_kurt(r, QDAYS)).diff().diff()

def f41_rdmm_012_excess_kurt_log_ret_252d_annual_kurt_d2(close: pd.Series) -> pd.Series:
    """Excess kurtosis (Fisher) of daily log-returns over 252d - tail fatness."""
    r = _log_ret(close)
    return (_rolling_kurt(r, YDAYS)).diff().diff()

def f41_rdmm_013_cv_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/|mean|) of log-returns over 21d - signal-to-noise of drift."""
    r = _log_ret(close)
    m = r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean().abs()
    sd = r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).std()
    return (_safe_div(sd, m)).diff().diff()

def f41_rdmm_014_cv_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/|mean|) of log-returns over 63d - signal-to-noise of drift."""
    r = _log_ret(close)
    m = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean().abs()
    sd = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).std()
    return (_safe_div(sd, m)).diff().diff()

def f41_rdmm_015_cv_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/|mean|) of log-returns over 252d - signal-to-noise of drift."""
    r = _log_ret(close)
    m = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean().abs()
    sd = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).std()
    return (_safe_div(sd, m)).diff().diff()

def f41_rdmm_016_mad_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of log-returns over 21d - robust scale."""
    r = _log_ret(close)
    return (_rolling_mad_mean(r, MDAYS)).diff().diff()

def f41_rdmm_017_mad_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of log-returns over 63d - robust scale."""
    r = _log_ret(close)
    return (_rolling_mad_mean(r, QDAYS)).diff().diff()

def f41_rdmm_018_mad_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean absolute deviation of log-returns over 252d - robust scale."""
    r = _log_ret(close)
    return (_rolling_mad_mean(r, YDAYS)).diff().diff()

def f41_rdmm_019_medad_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Median absolute deviation of log-returns over 21d - heavy-tail-robust scale."""
    r = _log_ret(close)
    return (_rolling_medad(r, MDAYS)).diff().diff()

def f41_rdmm_020_medad_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Median absolute deviation of log-returns over 63d - heavy-tail-robust scale."""
    r = _log_ret(close)
    return (_rolling_medad(r, QDAYS)).diff().diff()

def f41_rdmm_021_medad_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Median absolute deviation of log-returns over 252d - heavy-tail-robust scale."""
    r = _log_ret(close)
    return (_rolling_medad(r, YDAYS)).diff().diff()

def f41_rdmm_022_range_over_std_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """(Max-Min)/Std of log-returns over 21d - distribution-spread proxy for tail width."""
    r = _log_ret(close)
    hi = r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).max()
    lo = r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).min()
    sd = r.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).std()
    return (_safe_div(hi - lo, sd)).diff().diff()

def f41_rdmm_023_range_over_std_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """(Max-Min)/Std of log-returns over 63d - distribution-spread proxy for tail width."""
    r = _log_ret(close)
    hi = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).max()
    lo = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).min()
    sd = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).std()
    return (_safe_div(hi - lo, sd)).diff().diff()

def f41_rdmm_024_range_over_std_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """(Max-Min)/Std of log-returns over 252d - distribution-spread proxy for tail width."""
    r = _log_ret(close)
    hi = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).max()
    lo = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).min()
    sd = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).std()
    return (_safe_div(hi - lo, sd)).diff().diff()

def f41_rdmm_025_bowley_skew_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Bowley quantile-based skewness of log-returns over 21d - robust skew."""
    r = _log_ret(close)
    return (_bowley_skew(r, MDAYS)).diff().diff()

def f41_rdmm_026_bowley_skew_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Bowley quantile-based skewness of log-returns over 63d - robust skew."""
    r = _log_ret(close)
    return (_bowley_skew(r, QDAYS)).diff().diff()

def f41_rdmm_027_bowley_skew_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Bowley quantile-based skewness of log-returns over 252d - robust skew."""
    r = _log_ret(close)
    return (_bowley_skew(r, YDAYS)).diff().diff()

def f41_rdmm_028_moors_kurt_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Moors octile-based kurtosis of log-returns over 21d - robust kurt."""
    r = _log_ret(close)
    return (_moors_kurt(r, MDAYS)).diff().diff()

def f41_rdmm_029_moors_kurt_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Moors octile-based kurtosis of log-returns over 63d - robust kurt."""
    r = _log_ret(close)
    return (_moors_kurt(r, QDAYS)).diff().diff()

def f41_rdmm_030_moors_kurt_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Moors octile-based kurtosis of log-returns over 252d - robust kurt."""
    r = _log_ret(close)
    return (_moors_kurt(r, YDAYS)).diff().diff()

def f41_rdmm_031_jarque_bera_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Jarque-Bera statistic on 63d log-returns - skew+kurt joint normality test."""
    r = _log_ret(close)
    return (_jarque_bera(r, QDAYS)).diff().diff()

def f41_rdmm_032_anderson_darling_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Anderson-Darling statistic vs Normal on 63d log-returns - tail-weighted normality test."""
    r = _log_ret(close)
    return (_ad_stat_normal(r, QDAYS)).diff().diff()

def f41_rdmm_033_ks_lilliefors_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Kolmogorov-Smirnov (Lilliefors) statistic on 63d log-returns - uniform-weight normality test."""
    r = _log_ret(close)
    return (_ks_stat_normal(r, QDAYS)).diff().diff()

def f41_rdmm_034_shapiro_w_proxy_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Shapiro-Wilk-like W proxy on 63d log-returns - order-stat correlation with normal quantiles."""
    r = _log_ret(close)
    return (_shapiro_w_proxy(r, QDAYS)).diff().diff()

def f41_rdmm_035_jarque_bera_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Jarque-Bera on 252d log-returns - annual-horizon normality."""
    r = _log_ret(close)
    return (_jarque_bera(r, YDAYS)).diff().diff()

def f41_rdmm_036_anderson_darling_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Anderson-Darling on 252d log-returns."""
    r = _log_ret(close)
    return (_ad_stat_normal(r, YDAYS)).diff().diff()

def f41_rdmm_037_ks_lilliefors_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """KS-Lilliefors on 252d log-returns."""
    r = _log_ret(close)
    return (_ks_stat_normal(r, YDAYS)).diff().diff()

def f41_rdmm_038_shapiro_w_proxy_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Shapiro-Wilk-like W on 252d log-returns."""
    r = _log_ret(close)
    return (_shapiro_w_proxy(r, YDAYS)).diff().diff()

def f41_rdmm_039_pct_positive_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Fraction of positive log-returns over 21d."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    return (pos.rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_040_pct_positive_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of positive log-returns over 63d."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    return (pos.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_041_pct_positive_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of positive log-returns over 252d."""
    r = _log_ret(close)
    pos = (r > 0).astype(float).where(r.notna(), np.nan)
    return (pos.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()).diff().diff()

def f41_rdmm_042_downside_semidev_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Downside semi-deviation of log-returns over 21d - sqrt(E[min(0,r)^2])."""
    r = _log_ret(close)
    neg = r.where(r < 0, 0.0)
    v = (neg ** 2).rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_043_downside_semidev_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Downside semi-deviation of log-returns over 63d - sqrt(E[min(0,r)^2])."""
    r = _log_ret(close)
    neg = r.where(r < 0, 0.0)
    v = (neg ** 2).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_044_downside_semidev_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Downside semi-deviation of log-returns over 252d - sqrt(E[min(0,r)^2])."""
    r = _log_ret(close)
    neg = r.where(r < 0, 0.0)
    v = (neg ** 2).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_045_upside_semidev_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Upside semi-deviation of log-returns over 21d - sqrt(E[max(0,r)^2])."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0)
    v = (pos ** 2).rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_046_upside_semidev_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Upside semi-deviation of log-returns over 63d - sqrt(E[max(0,r)^2])."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0)
    v = (pos ** 2).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_047_upside_semidev_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Upside semi-deviation of log-returns over 252d - sqrt(E[max(0,r)^2])."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0)
    v = (pos ** 2).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    return (np.sqrt(v)).diff().diff()

def f41_rdmm_048_vol_asym_up_over_down_ratio_log_ret_21d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upside-semidev to downside-semidev of log-returns over 21d - vol asymmetry."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0); neg = r.where(r < 0, 0.0)
    up = np.sqrt((pos ** 2).rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean())
    dn = np.sqrt((neg ** 2).rolling(MDAYS, min_periods=max(MDAYS // 3, 10)).mean())
    return (_safe_div(up, dn)).diff().diff()

def f41_rdmm_049_vol_asym_up_over_down_ratio_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upside-semidev to downside-semidev of log-returns over 63d - vol asymmetry."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0); neg = r.where(r < 0, 0.0)
    up = np.sqrt((pos ** 2).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean())
    dn = np.sqrt((neg ** 2).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean())
    return (_safe_div(up, dn)).diff().diff()

def f41_rdmm_050_vol_asym_up_over_down_ratio_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upside-semidev to downside-semidev of log-returns over 252d - vol asymmetry."""
    r = _log_ret(close)
    pos = r.where(r > 0, 0.0); neg = r.where(r < 0, 0.0)
    up = np.sqrt((pos ** 2).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean())
    dn = np.sqrt((neg ** 2).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean())
    return (_safe_div(up, dn)).diff().diff()

def f41_rdmm_051_mean_overnight_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of overnight log-returns (open/prior close) over 63d - gap-only drift."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (on.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f41_rdmm_052_std_overnight_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Std of overnight log-returns over 63d - gap-only vol."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (on.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f41_rdmm_053_skew_overnight_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of overnight log-returns over 63d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_rolling_skew(on, QDAYS)).diff().diff()

def f41_rdmm_054_excess_kurt_overnight_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Excess kurtosis of overnight log-returns over 63d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_rolling_kurt(on, QDAYS)).diff().diff()

def f41_rdmm_055_mean_intraday_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of intraday log-returns (close/open) over 63d - session-only drift."""
    intr = _safe_log(close) - _safe_log(open)
    return (intr.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f41_rdmm_056_std_intraday_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Std of intraday log-returns over 63d - session-only vol."""
    intr = _safe_log(close) - _safe_log(open)
    return (intr.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f41_rdmm_057_skew_intraday_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of intraday log-returns over 63d."""
    intr = _safe_log(close) - _safe_log(open)
    return (_rolling_skew(intr, QDAYS)).diff().diff()

def f41_rdmm_058_excess_kurt_intraday_log_ret_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Excess kurtosis of intraday log-returns over 63d."""
    intr = _safe_log(close) - _safe_log(open)
    return (_rolling_kurt(intr, QDAYS)).diff().diff()

def f41_rdmm_059_mean_tr_norm_close_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of true-range / close over 63d - drift in range-based return proxy."""
    tr = _safe_div(_true_range(high, low, close), close)
    return (tr.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f41_rdmm_060_std_tr_norm_close_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of true-range / close over 63d."""
    tr = _safe_div(_true_range(high, low, close), close)
    return (tr.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f41_rdmm_061_iqr_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Interquartile range of log-returns over 63d."""
    r = _log_ret(close)
    q3 = _rolling_q(r, QDAYS, 0.75); q1 = _rolling_q(r, QDAYS, 0.25)
    return (q3 - q1).diff().diff()

def f41_rdmm_062_iqr_over_std_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """IQR / std of log-returns over 63d - normal-distribution this is ~1.349."""
    r = _log_ret(close)
    q3 = _rolling_q(r, QDAYS, 0.75); q1 = _rolling_q(r, QDAYS, 0.25)
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(q3 - q1, sd)).diff().diff()

def f41_rdmm_063_p90_minus_p10_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """P90-P10 range of log-returns over 63d - deeper-quantile spread."""
    r = _log_ret(close)
    hi = _rolling_q(r, QDAYS, 0.90); lo = _rolling_q(r, QDAYS, 0.10)
    return (hi - lo).diff().diff()

def f41_rdmm_064_p99_minus_p1_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """P99-P1 spread of log-returns over 252d - extreme-quantile spread."""
    r = _log_ret(close)
    hi = _rolling_q(r, YDAYS, 0.99); lo = _rolling_q(r, YDAYS, 0.01)
    return (hi - lo).diff().diff()

def f41_rdmm_065_median_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Median log-return over 63d - robust center."""
    r = _log_ret(close)
    return (_rolling_median(r, QDAYS)).diff().diff()

def f41_rdmm_066_median_minus_mean_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Median minus mean of log-returns over 63d - sign-of-skew diagnostic."""
    r = _log_ret(close)
    med = _rolling_median(r, QDAYS); mu = r.rolling(QDAYS, min_periods=MDAYS).mean()
    return (med - mu).diff().diff()

def f41_rdmm_067_fifth_std_moment_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Standardized 5th central moment of log-returns over 63d."""
    r = _log_ret(close)
    mu = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    sd = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).std()
    m = ((r - mu) ** 5).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    return (_safe_div(m, sd ** 5)).diff().diff()

def f41_rdmm_068_sixth_std_moment_log_ret_63d_d2(close: pd.Series) -> pd.Series:
    """Standardized 6th central moment of log-returns over 63d."""
    r = _log_ret(close)
    mu = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    sd = r.rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).std()
    m = ((r - mu) ** 6).rolling(QDAYS, min_periods=max(QDAYS // 3, 10)).mean()
    return (_safe_div(m, sd ** 6)).diff().diff()

def f41_rdmm_069_fifth_std_moment_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Standardized 5th central moment of log-returns over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    sd = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).std()
    m = ((r - mu) ** 5).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    return (_safe_div(m, sd ** 5)).diff().diff()

def f41_rdmm_070_sixth_std_moment_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Standardized 6th central moment of log-returns over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    sd = r.rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).std()
    m = ((r - mu) ** 6).rolling(YDAYS, min_periods=max(YDAYS // 3, 10)).mean()
    return (_safe_div(m, sd ** 6)).diff().diff()

def f41_rdmm_071_bipower_var_63d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Bipower variation = (pi/2)*sum |r_t|*|r_{t-1}| over 63d - jump-robust vol."""
    r = _log_ret(close).abs()
    bp = (r * r.shift(1)).rolling(QDAYS, min_periods=MDAYS).sum() * (np.pi / 2.0)
    return (bp).diff().diff()

def f41_rdmm_072_bipower_var_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Bipower variation over 252d - long-horizon jump-robust vol."""
    r = _log_ret(close).abs()
    bp = (r * r.shift(1)).rolling(YDAYS, min_periods=QDAYS).sum() * (np.pi / 2.0)
    return (bp).diff().diff()

def f41_rdmm_073_jump_component_63d_rv_minus_bpv_d2(close: pd.Series) -> pd.Series:
    """Realized variance minus bipower over 63d - jump activity captured."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    ar = r.abs()
    bp = (ar * ar.shift(1)).rolling(QDAYS, min_periods=MDAYS).sum() * (np.pi / 2.0)
    return ((rv - bp).clip(lower=0.0)).diff().diff()

def f41_rdmm_074_jump_component_252d_rv_minus_bpv_d2(close: pd.Series) -> pd.Series:
    """Realized variance minus bipower over 252d - annual jump activity."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    ar = r.abs()
    bp = (ar * ar.shift(1)).rolling(YDAYS, min_periods=QDAYS).sum() * (np.pi / 2.0)
    return ((rv - bp).clip(lower=0.0)).diff().diff()

def f41_rdmm_075_realized_quarticity_63d_log_ret_d2(close: pd.Series) -> pd.Series:
    """Realized quarticity = (n/3)*sum r^4 over 63d - asymptotic variance of RV."""
    r = _log_ret(close)
    rq = (r ** 4).rolling(QDAYS, min_periods=MDAYS).sum() * (QDAYS / 3.0)
    return (rq).diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

RETURN_DISTRIBUTION_MOMENTS_D2_REGISTRY_001_075 = {
    "f41_rdmm_001_mean_log_ret_21d_monthly_drift_d2": {"inputs": ["close"], "func": f41_rdmm_001_mean_log_ret_21d_monthly_drift_d2},
    "f41_rdmm_002_mean_log_ret_63d_quarterly_drift_d2": {"inputs": ["close"], "func": f41_rdmm_002_mean_log_ret_63d_quarterly_drift_d2},
    "f41_rdmm_003_mean_log_ret_252d_annual_drift_d2": {"inputs": ["close"], "func": f41_rdmm_003_mean_log_ret_252d_annual_drift_d2},
    "f41_rdmm_004_std_log_ret_21d_monthly_vol_d2": {"inputs": ["close"], "func": f41_rdmm_004_std_log_ret_21d_monthly_vol_d2},
    "f41_rdmm_005_std_log_ret_63d_quarterly_vol_d2": {"inputs": ["close"], "func": f41_rdmm_005_std_log_ret_63d_quarterly_vol_d2},
    "f41_rdmm_006_std_log_ret_252d_annual_vol_d2": {"inputs": ["close"], "func": f41_rdmm_006_std_log_ret_252d_annual_vol_d2},
    "f41_rdmm_007_skew_log_ret_21d_monthly_skew_d2": {"inputs": ["close"], "func": f41_rdmm_007_skew_log_ret_21d_monthly_skew_d2},
    "f41_rdmm_008_skew_log_ret_63d_quarterly_skew_d2": {"inputs": ["close"], "func": f41_rdmm_008_skew_log_ret_63d_quarterly_skew_d2},
    "f41_rdmm_009_skew_log_ret_252d_annual_skew_d2": {"inputs": ["close"], "func": f41_rdmm_009_skew_log_ret_252d_annual_skew_d2},
    "f41_rdmm_010_excess_kurt_log_ret_21d_monthly_kurt_d2": {"inputs": ["close"], "func": f41_rdmm_010_excess_kurt_log_ret_21d_monthly_kurt_d2},
    "f41_rdmm_011_excess_kurt_log_ret_63d_quarterly_kurt_d2": {"inputs": ["close"], "func": f41_rdmm_011_excess_kurt_log_ret_63d_quarterly_kurt_d2},
    "f41_rdmm_012_excess_kurt_log_ret_252d_annual_kurt_d2": {"inputs": ["close"], "func": f41_rdmm_012_excess_kurt_log_ret_252d_annual_kurt_d2},
    "f41_rdmm_013_cv_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_013_cv_log_ret_21d_d2},
    "f41_rdmm_014_cv_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_014_cv_log_ret_63d_d2},
    "f41_rdmm_015_cv_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_015_cv_log_ret_252d_d2},
    "f41_rdmm_016_mad_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_016_mad_log_ret_21d_d2},
    "f41_rdmm_017_mad_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_017_mad_log_ret_63d_d2},
    "f41_rdmm_018_mad_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_018_mad_log_ret_252d_d2},
    "f41_rdmm_019_medad_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_019_medad_log_ret_21d_d2},
    "f41_rdmm_020_medad_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_020_medad_log_ret_63d_d2},
    "f41_rdmm_021_medad_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_021_medad_log_ret_252d_d2},
    "f41_rdmm_022_range_over_std_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_022_range_over_std_log_ret_21d_d2},
    "f41_rdmm_023_range_over_std_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_023_range_over_std_log_ret_63d_d2},
    "f41_rdmm_024_range_over_std_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_024_range_over_std_log_ret_252d_d2},
    "f41_rdmm_025_bowley_skew_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_025_bowley_skew_log_ret_21d_d2},
    "f41_rdmm_026_bowley_skew_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_026_bowley_skew_log_ret_63d_d2},
    "f41_rdmm_027_bowley_skew_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_027_bowley_skew_log_ret_252d_d2},
    "f41_rdmm_028_moors_kurt_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_028_moors_kurt_log_ret_21d_d2},
    "f41_rdmm_029_moors_kurt_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_029_moors_kurt_log_ret_63d_d2},
    "f41_rdmm_030_moors_kurt_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_030_moors_kurt_log_ret_252d_d2},
    "f41_rdmm_031_jarque_bera_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_031_jarque_bera_log_ret_63d_d2},
    "f41_rdmm_032_anderson_darling_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_032_anderson_darling_log_ret_63d_d2},
    "f41_rdmm_033_ks_lilliefors_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_033_ks_lilliefors_log_ret_63d_d2},
    "f41_rdmm_034_shapiro_w_proxy_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_034_shapiro_w_proxy_log_ret_63d_d2},
    "f41_rdmm_035_jarque_bera_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_035_jarque_bera_log_ret_252d_d2},
    "f41_rdmm_036_anderson_darling_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_036_anderson_darling_log_ret_252d_d2},
    "f41_rdmm_037_ks_lilliefors_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_037_ks_lilliefors_log_ret_252d_d2},
    "f41_rdmm_038_shapiro_w_proxy_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_038_shapiro_w_proxy_log_ret_252d_d2},
    "f41_rdmm_039_pct_positive_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_039_pct_positive_log_ret_21d_d2},
    "f41_rdmm_040_pct_positive_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_040_pct_positive_log_ret_63d_d2},
    "f41_rdmm_041_pct_positive_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_041_pct_positive_log_ret_252d_d2},
    "f41_rdmm_042_downside_semidev_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_042_downside_semidev_log_ret_21d_d2},
    "f41_rdmm_043_downside_semidev_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_043_downside_semidev_log_ret_63d_d2},
    "f41_rdmm_044_downside_semidev_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_044_downside_semidev_log_ret_252d_d2},
    "f41_rdmm_045_upside_semidev_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_045_upside_semidev_log_ret_21d_d2},
    "f41_rdmm_046_upside_semidev_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_046_upside_semidev_log_ret_63d_d2},
    "f41_rdmm_047_upside_semidev_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_047_upside_semidev_log_ret_252d_d2},
    "f41_rdmm_048_vol_asym_up_over_down_ratio_log_ret_21d_d2": {"inputs": ["close"], "func": f41_rdmm_048_vol_asym_up_over_down_ratio_log_ret_21d_d2},
    "f41_rdmm_049_vol_asym_up_over_down_ratio_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_049_vol_asym_up_over_down_ratio_log_ret_63d_d2},
    "f41_rdmm_050_vol_asym_up_over_down_ratio_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_050_vol_asym_up_over_down_ratio_log_ret_252d_d2},
    "f41_rdmm_051_mean_overnight_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_051_mean_overnight_log_ret_63d_d2},
    "f41_rdmm_052_std_overnight_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_052_std_overnight_log_ret_63d_d2},
    "f41_rdmm_053_skew_overnight_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_053_skew_overnight_log_ret_63d_d2},
    "f41_rdmm_054_excess_kurt_overnight_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_054_excess_kurt_overnight_log_ret_63d_d2},
    "f41_rdmm_055_mean_intraday_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_055_mean_intraday_log_ret_63d_d2},
    "f41_rdmm_056_std_intraday_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_056_std_intraday_log_ret_63d_d2},
    "f41_rdmm_057_skew_intraday_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_057_skew_intraday_log_ret_63d_d2},
    "f41_rdmm_058_excess_kurt_intraday_log_ret_63d_d2": {"inputs": ["open", "close"], "func": f41_rdmm_058_excess_kurt_intraday_log_ret_63d_d2},
    "f41_rdmm_059_mean_tr_norm_close_63d_d2": {"inputs": ["high", "low", "close"], "func": f41_rdmm_059_mean_tr_norm_close_63d_d2},
    "f41_rdmm_060_std_tr_norm_close_63d_d2": {"inputs": ["high", "low", "close"], "func": f41_rdmm_060_std_tr_norm_close_63d_d2},
    "f41_rdmm_061_iqr_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_061_iqr_log_ret_63d_d2},
    "f41_rdmm_062_iqr_over_std_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_062_iqr_over_std_log_ret_63d_d2},
    "f41_rdmm_063_p90_minus_p10_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_063_p90_minus_p10_log_ret_63d_d2},
    "f41_rdmm_064_p99_minus_p1_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_064_p99_minus_p1_log_ret_252d_d2},
    "f41_rdmm_065_median_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_065_median_log_ret_63d_d2},
    "f41_rdmm_066_median_minus_mean_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_066_median_minus_mean_log_ret_63d_d2},
    "f41_rdmm_067_fifth_std_moment_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_067_fifth_std_moment_log_ret_63d_d2},
    "f41_rdmm_068_sixth_std_moment_log_ret_63d_d2": {"inputs": ["close"], "func": f41_rdmm_068_sixth_std_moment_log_ret_63d_d2},
    "f41_rdmm_069_fifth_std_moment_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_069_fifth_std_moment_log_ret_252d_d2},
    "f41_rdmm_070_sixth_std_moment_log_ret_252d_d2": {"inputs": ["close"], "func": f41_rdmm_070_sixth_std_moment_log_ret_252d_d2},
    "f41_rdmm_071_bipower_var_63d_log_ret_d2": {"inputs": ["close"], "func": f41_rdmm_071_bipower_var_63d_log_ret_d2},
    "f41_rdmm_072_bipower_var_252d_log_ret_d2": {"inputs": ["close"], "func": f41_rdmm_072_bipower_var_252d_log_ret_d2},
    "f41_rdmm_073_jump_component_63d_rv_minus_bpv_d2": {"inputs": ["close"], "func": f41_rdmm_073_jump_component_63d_rv_minus_bpv_d2},
    "f41_rdmm_074_jump_component_252d_rv_minus_bpv_d2": {"inputs": ["close"], "func": f41_rdmm_074_jump_component_252d_rv_minus_bpv_d2},
    "f41_rdmm_075_realized_quarticity_63d_log_ret_d2": {"inputs": ["close"], "func": f41_rdmm_075_realized_quarticity_63d_log_ret_d2},
}
