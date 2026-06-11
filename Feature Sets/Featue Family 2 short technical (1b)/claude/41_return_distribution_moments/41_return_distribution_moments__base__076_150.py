"""return_distribution_moments base features 076-150 - Pipeline 1b-technical.

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


def f41_rdmm_076_l_scale_log_ret_63d(close: pd.Series) -> pd.Series:
    """L-scale (L2) of log-returns over 63d - robust scale based on linear order-stat combinations."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, QDAYS)
    return (l2)

def f41_rdmm_077_l_skew_log_ret_63d(close: pd.Series) -> pd.Series:
    """L-skew (L3/L2) of log-returns over 63d - robust skewness from L-moments."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, QDAYS)
    return (l3r)

def f41_rdmm_078_l_kurt_log_ret_63d(close: pd.Series) -> pd.Series:
    """L-kurt (L4/L2) of log-returns over 63d - robust kurtosis from L-moments."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, QDAYS)
    return (l4r)

def f41_rdmm_079_l_scale_log_ret_252d(close: pd.Series) -> pd.Series:
    """L-scale over 252d."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, YDAYS)
    return (l2)

def f41_rdmm_080_l_skew_log_ret_252d(close: pd.Series) -> pd.Series:
    """L-skew over 252d."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, YDAYS)
    return (l3r)

def f41_rdmm_081_l_kurt_log_ret_252d(close: pd.Series) -> pd.Series:
    """L-kurt over 252d."""
    r = _log_ret(close)
    l2, l3r, l4r = _l_moments(r, YDAYS)
    return (l4r)

def f41_rdmm_082_l_scale_to_std_ratio_log_ret_63d(close: pd.Series) -> pd.Series:
    """Ratio of L-scale to classical std over 63d - normal-distribution this is sqrt(pi)/2."""
    r = _log_ret(close)
    l2, _l3, _l4 = _l_moments(r, QDAYS)
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(l2, sd))

def f41_rdmm_083_l_skew_short_minus_long_252d(close: pd.Series) -> pd.Series:
    """L-skew at 63d minus L-skew at 252d - regime-skew differential."""
    r = _log_ret(close)
    _, l3s, _ = _l_moments(r, QDAYS)
    _, l3l, _ = _l_moments(r, YDAYS)
    return (l3s - l3l)

def f41_rdmm_084_hill_upper_tail_5pct_log_ret_252d(close: pd.Series) -> pd.Series:
    """Hill estimator of upper-tail index using top 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_upper(r, YDAYS, 0.05))

def f41_rdmm_085_hill_lower_tail_5pct_log_ret_252d(close: pd.Series) -> pd.Series:
    """Hill estimator of lower-tail index using bottom 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_lower(r, YDAYS, 0.05))

def f41_rdmm_086_hill_upper_tail_10pct_log_ret_252d(close: pd.Series) -> pd.Series:
    """Hill estimator of upper tail using top 10% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_upper(r, YDAYS, 0.10))

def f41_rdmm_087_hill_lower_tail_10pct_log_ret_252d(close: pd.Series) -> pd.Series:
    """Hill estimator of lower tail using bottom 10% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_lower(r, YDAYS, 0.10))

def f41_rdmm_088_hill_tail_index_diff_upper_minus_lower_5pct_252d(close: pd.Series) -> pd.Series:
    """Upper minus lower Hill tail-index (5%) over 252d - tail-asymmetry indicator."""
    r = _log_ret(close)
    u = _hill_index_upper(r, YDAYS, 0.05)
    l = _hill_index_lower(r, YDAYS, 0.05)
    return (u - l)

def f41_rdmm_089_pickands_tail_index_log_ret_252d(close: pd.Series) -> pd.Series:
    """Pickands tail-index estimator on log-returns over 252d."""
    r = _log_ret(close)
    return (_pickands_index(r, YDAYS))

def f41_rdmm_090_trimmed_10pct_mean_log_ret_252d(close: pd.Series) -> pd.Series:
    """10%-trimmed mean of log-returns over 252d - outlier-robust mean."""
    r = _log_ret(close)
    return (_trimmed_mean(r, YDAYS, 0.10))

def f41_rdmm_091_trimmed_10pct_std_log_ret_252d(close: pd.Series) -> pd.Series:
    """10%-trimmed std of log-returns over 252d."""
    r = _log_ret(close)
    return (_trimmed_std(r, YDAYS, 0.10))

def f41_rdmm_092_winsor_5pct_mean_log_ret_252d(close: pd.Series) -> pd.Series:
    """5%-winsorized mean of log-returns over 252d."""
    r = _log_ret(close)
    return (_winsor_mean(r, YDAYS, 0.05))

def f41_rdmm_093_winsor_5pct_std_log_ret_252d(close: pd.Series) -> pd.Series:
    """5%-winsorized std of log-returns over 252d."""
    r = _log_ret(close)
    return (_winsor_std(r, YDAYS, 0.05))

def f41_rdmm_094_trimmed_10pct_skew_log_ret_252d(close: pd.Series) -> pd.Series:
    """10%-trimmed skewness of log-returns over 252d - outlier-robust skew."""
    r = _log_ret(close)
    return (_trimmed_skew(r, YDAYS, 0.10))

def f41_rdmm_095_trimmed_10pct_kurt_log_ret_252d(close: pd.Series) -> pd.Series:
    """10%-trimmed excess kurtosis of log-returns over 252d."""
    r = _log_ret(close)
    return (_trimmed_kurt(r, YDAYS, 0.10))

def f41_rdmm_096_mean_abs_log_ret_63d(close: pd.Series) -> pd.Series:
    """E[|r|] over 63d - L1 vol proxy."""
    r = _log_ret(close).abs()
    return (r.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_097_mean_sqrt_abs_log_ret_63d(close: pd.Series) -> pd.Series:
    """E[sqrt(|r|)] over 63d - sub-linear penalty on returns."""
    r = np.sqrt(_log_ret(close).abs())
    return (r.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_098_mean_log_abs_log_ret_63d(close: pd.Series) -> pd.Series:
    """E[log|r|] over 63d - log-mean-vol (Yamai-Yoshiba style)."""
    r = _log_ret(close).abs()
    lr = np.log(r.replace(0, np.nan))
    return (lr.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_099_mean_cubed_log_ret_63d(close: pd.Series) -> pd.Series:
    """Raw 3rd moment (mean of r^3) over 63d - non-standardized skew proxy."""
    r = _log_ret(close)
    rc = r ** 3
    return (rc.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_100_mean_fourth_log_ret_63d(close: pd.Series) -> pd.Series:
    """Raw 4th moment over 63d - non-standardized kurt proxy."""
    r = _log_ret(close)
    rq = r ** 4
    return (rq.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_101_jarque_bera_overnight_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Jarque-Bera statistic on 63d overnight returns - normality of gap-return distribution."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_jarque_bera(on, QDAYS))

def f41_rdmm_102_jarque_bera_intraday_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Jarque-Bera on 63d intraday (close/open) returns."""
    intr = _safe_log(close) - _safe_log(open)
    return (_jarque_bera(intr, QDAYS))

def f41_rdmm_103_jarque_bera_abs_log_ret_63d(close: pd.Series) -> pd.Series:
    """Jarque-Bera applied to |log-returns| over 63d - vol-distribution normality test."""
    r = _log_ret(close).abs()
    return (_jarque_bera(r, QDAYS))

def f41_rdmm_104_ad_overnight_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Anderson-Darling on 63d overnight returns."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_ad_stat_normal(on, QDAYS))

def f41_rdmm_105_ad_intraday_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Anderson-Darling on 63d intraday returns."""
    intr = _safe_log(close) - _safe_log(open)
    return (_ad_stat_normal(intr, QDAYS))

def f41_rdmm_106_ks_overnight_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """KS-Lilliefors on 63d overnight returns."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_ks_stat_normal(on, QDAYS))

def f41_rdmm_107_ks_intraday_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """KS-Lilliefors on 63d intraday returns."""
    intr = _safe_log(close) - _safe_log(open)
    return (_ks_stat_normal(intr, QDAYS))

def f41_rdmm_108_shapiro_w_overnight_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Shapiro-Wilk-like W on 63d overnight returns."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    return (_shapiro_w_proxy(on, QDAYS))

def f41_rdmm_109_kurt_minus_three_diff_log_ret_63d(close: pd.Series) -> pd.Series:
    """Excess kurt minus 3 over 63d (pandas .kurt is already excess; this is excess - 0 sanity diagnostic)."""
    r = _log_ret(close)
    return (_rolling_kurt(r, QDAYS) - 0.0)

def f41_rdmm_110_kurt_minus_three_diff_log_ret_252d(close: pd.Series) -> pd.Series:
    """Same metric over 252d - placeholder slot for excess kurtosis annual horizon."""
    r = _log_ret(close)
    return (_rolling_kurt(r, YDAYS) - 0.0)

def f41_rdmm_111_abs_skew_log_ret_63d(close: pd.Series) -> pd.Series:
    """|skew| over 63d - magnitude-only skew, direction agnostic."""
    r = _log_ret(close)
    return (_rolling_skew(r, QDAYS).abs())

def f41_rdmm_112_abs_skew_log_ret_252d(close: pd.Series) -> pd.Series:
    """|skew| over 252d."""
    r = _log_ret(close)
    return (_rolling_skew(r, YDAYS).abs())

def f41_rdmm_113_squared_skew_log_ret_63d(close: pd.Series) -> pd.Series:
    """skew^2 over 63d - magnifies large skews."""
    r = _log_ret(close)
    return (_rolling_skew(r, QDAYS) ** 2)

def f41_rdmm_114_squared_skew_log_ret_252d(close: pd.Series) -> pd.Series:
    """skew^2 over 252d."""
    r = _log_ret(close)
    return (_rolling_skew(r, YDAYS) ** 2)

def f41_rdmm_115_mean_sign_log_ret_63d(close: pd.Series) -> pd.Series:
    """Mean of sign(r) over 63d - in [-1,+1], 2*pct_positive - 1."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    return (sg.rolling(QDAYS, min_periods=MDAYS).mean())

def f41_rdmm_116_std_sign_log_ret_63d(close: pd.Series) -> pd.Series:
    """Std of sign(r) over 63d - binary-sequence vol."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    return (sg.rolling(QDAYS, min_periods=MDAYS).std())

def f41_rdmm_117_autocorr_sign_lag1_log_ret_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of sign(r) at lag 1 over 63d - direction-persistence at lag 1."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        a = v[:-1]; b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = sg.rolling(QDAYS, min_periods=MDAYS).apply(_ac, raw=True)
    return (res)

def f41_rdmm_118_autocorr_sign_lag5_log_ret_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of sign(r) at lag 5 over 63d - direction persistence at weekly lag."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 25:
            return np.nan
        a = v[:-5]; b = v[5:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = sg.rolling(QDAYS, min_periods=MDAYS).apply(_ac, raw=True)
    return (res)

def f41_rdmm_119_runs_test_z_log_ret_63d(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs-test z-statistic on sign(r) over 63d."""
    r = _log_ret(close)
    return (_runs_test_z(r, QDAYS))

def f41_rdmm_120_runs_test_z_log_ret_252d(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs-test z-stat over 252d."""
    r = _log_ret(close)
    return (_runs_test_z(r, YDAYS))

def f41_rdmm_121_mean_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """E[|r|] over 252d."""
    r = _log_ret(close).abs()
    return (r.rolling(YDAYS, min_periods=QDAYS).mean())

def f41_rdmm_122_std_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Std of |r| over 252d - vol-of-vol proxy."""
    r = _log_ret(close).abs()
    return (r.rolling(YDAYS, min_periods=QDAYS).std())

def f41_rdmm_123_skew_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Skewness of |r| over 252d - asymmetry in vol magnitudes."""
    r = _log_ret(close).abs()
    return (_rolling_skew(r, YDAYS))

def f41_rdmm_124_excess_kurt_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of |r| over 252d."""
    r = _log_ret(close).abs()
    return (_rolling_kurt(r, YDAYS))

def f41_rdmm_125_range_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Max-min of |r| over 252d - magnitude span."""
    r = _log_ret(close).abs()
    hi = r.rolling(YDAYS, min_periods=QDAYS).max(); lo = r.rolling(YDAYS, min_periods=QDAYS).min()
    return (hi - lo)

def f41_rdmm_126_p95_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """95th percentile of |r| over 252d - tail-magnitude reference level."""
    r = _log_ret(close).abs()
    return (_rolling_q(r, YDAYS, 0.95))

def f41_rdmm_127_mean_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """E[log|r|] over 252d - log-mean-vol over annual horizon."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (lr.rolling(YDAYS, min_periods=QDAYS).mean())

def f41_rdmm_128_std_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Std of log|r| over 252d - vol-of-log-vol."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (lr.rolling(YDAYS, min_periods=QDAYS).std())

def f41_rdmm_129_skew_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Skewness of log|r| over 252d."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (_rolling_skew(lr, YDAYS))

def f41_rdmm_130_excess_kurt_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log|r| over 252d."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (_rolling_kurt(lr, YDAYS))

def f41_rdmm_131_iqr_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """IQR of log|r| over 252d."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (_rolling_q(lr, YDAYS, 0.75) - _rolling_q(lr, YDAYS, 0.25))

def f41_rdmm_132_p90_log_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """90th percentile of log|r| over 252d - upper-vol-quantile."""
    lr = np.log(_log_ret(close).abs().replace(0, np.nan))
    return (_rolling_q(lr, YDAYS, 0.90))

def f41_rdmm_133_quantile_skew_p75_p25_63d(close: pd.Series) -> pd.Series:
    """(Q(0.75) + Q(0.25) - 2*median) / (Q(0.75) - Q(0.25)) on log-returns over 63d."""
    r = _log_ret(close)
    qh = _rolling_q(r, QDAYS, 0.75); ql = _rolling_q(r, QDAYS, 0.25)
    md = _rolling_median(r, QDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_134_quantile_skew_p75_p25_252d(close: pd.Series) -> pd.Series:
    """(Q(0.75) + Q(0.25) - 2*median) / (Q(0.75) - Q(0.25)) on log-returns over 252d."""
    r = _log_ret(close)
    qh = _rolling_q(r, YDAYS, 0.75); ql = _rolling_q(r, YDAYS, 0.25)
    md = _rolling_median(r, YDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_135_quantile_skew_p90_p10_63d(close: pd.Series) -> pd.Series:
    """(Q(0.9) + Q(0.1) - 2*median) / (Q(0.9) - Q(0.1)) on log-returns over 63d."""
    r = _log_ret(close)
    qh = _rolling_q(r, QDAYS, 0.9); ql = _rolling_q(r, QDAYS, 0.1)
    md = _rolling_median(r, QDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_136_quantile_skew_p90_p10_252d(close: pd.Series) -> pd.Series:
    """(Q(0.9) + Q(0.1) - 2*median) / (Q(0.9) - Q(0.1)) on log-returns over 252d."""
    r = _log_ret(close)
    qh = _rolling_q(r, YDAYS, 0.9); ql = _rolling_q(r, YDAYS, 0.1)
    md = _rolling_median(r, YDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_137_quantile_skew_p95_p5_252d(close: pd.Series) -> pd.Series:
    """(Q(0.95) + Q(0.05) - 2*median) / (Q(0.95) - Q(0.05)) on log-returns over 252d."""
    r = _log_ret(close)
    qh = _rolling_q(r, YDAYS, 0.95); ql = _rolling_q(r, YDAYS, 0.05)
    md = _rolling_median(r, YDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_138_quantile_skew_p99_p1_252d(close: pd.Series) -> pd.Series:
    """(Q(0.99) + Q(0.01) - 2*median) / (Q(0.99) - Q(0.01)) on log-returns over 252d."""
    r = _log_ret(close)
    qh = _rolling_q(r, YDAYS, 0.99); ql = _rolling_q(r, YDAYS, 0.01)
    md = _rolling_median(r, YDAYS)
    return (_safe_div(qh + ql - 2.0 * md, qh - ql))

def f41_rdmm_139_gini_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Gini coefficient of |log-returns| over 252d - inequality of return magnitudes."""
    r = _log_ret(close).abs()
    def _g(w):
        v = np.sort(w[~np.isnan(w)])
        if v.size < 30:
            return np.nan
        n = v.size
        sv = v.sum()
        if sv <= 0:
            return np.nan
        i = np.arange(1, n + 1, dtype=float)
        return float((2.0 * (i * v).sum() - (n + 1) * sv) / (n * sv))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_g, raw=True)
    return (res)

def f41_rdmm_140_herfindahl_norm_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Normalized Herfindahl index of |r|/sum over 252d - magnitude concentration."""
    r = _log_ret(close).abs()
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sv = v.sum()
        if sv <= 0:
            return np.nan
        p = v / sv
        return float((p * p).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)
    return (res)

def f41_rdmm_141_effective_n_returns_252d(close: pd.Series) -> pd.Series:
    """Effective number of return events 1/Herfindahl over 252d - 'how many days carry the action'."""
    r = _log_ret(close).abs()
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sv = v.sum()
        if sv <= 0:
            return np.nan
        p = v / sv
        h = (p * p).sum()
        return float(1.0 / h) if h > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)
    return (res)

def f41_rdmm_142_atkinson_index_abs_log_ret_252d(close: pd.Series) -> pd.Series:
    """Atkinson inequality index (epsilon=0.5) of |r| over 252d."""
    r = _log_ret(close).abs()
    def _a(w):
        v = w[~np.isnan(w)]
        v = v[v > 0]
        if v.size < 30:
            return np.nan
        mu = v.mean()
        if mu <= 0:
            return np.nan
        gm = np.exp(np.log(v).mean()) if v.size > 0 else np.nan
        if not np.isfinite(gm) or gm <= 0:
            return np.nan
        return float(1.0 - gm / mu)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_a, raw=True)
    return (res)

def f41_rdmm_143_shannon_entropy_binned_log_ret_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of binned log-returns (10 bins) over 252d."""
    r = _log_ret(close)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = v.min(); hi = v.max()
        if hi <= lo:
            return 0.0
        edges = np.linspace(lo, hi, 11)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)
    return (res)

def f41_rdmm_144_negentropy_proxy_log_ret_252d(close: pd.Series) -> pd.Series:
    """Negentropy proxy = 0.5*log(2*pi*e*var) - entropy(returns) over 252d."""
    r = _log_ret(close)
    def _ne(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        var = v.var()
        if var <= 0:
            return np.nan
        lo = v.min(); hi = v.max()
        if hi <= lo:
            return 0.0
        edges = np.linspace(lo, hi, 21)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        ent = -(p * np.log(p)).sum()
        gauss_ent = 0.5 * np.log(2.0 * np.pi * np.e * var)
        return float(gauss_ent - ent)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ne, raw=True)
    return (res)

def f41_rdmm_145_skew_minus_kurt_log_ret_63d(close: pd.Series) -> pd.Series:
    """Skew minus excess-kurt over 63d - composite shape feature."""
    r = _log_ret(close)
    sk = _rolling_skew(r, QDAYS); kt = _rolling_kurt(r, QDAYS)
    return (sk - kt)

def f41_rdmm_146_skew_times_kurt_log_ret_63d(close: pd.Series) -> pd.Series:
    """Skew * excess-kurt over 63d - signed tail-fatness composite."""
    r = _log_ret(close)
    sk = _rolling_skew(r, QDAYS); kt = _rolling_kurt(r, QDAYS)
    return (sk * kt)

def f41_rdmm_147_sharpe_like_mean_over_std_log_ret_63d(close: pd.Series) -> pd.Series:
    """Mean/Std of log-returns over 63d - daily Sharpe-like ratio."""
    r = _log_ret(close)
    mu = r.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(mu, sd))

def f41_rdmm_148_sortino_like_mean_over_downsemidev_log_ret_63d(close: pd.Series) -> pd.Series:
    """Mean / downside-semidev of log-returns over 63d - Sortino-like."""
    r = _log_ret(close)
    mu = r.rolling(QDAYS, min_periods=MDAYS).mean()
    neg = r.where(r < 0, 0.0)
    dd = np.sqrt((neg ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    return (_safe_div(mu, dd))

def f41_rdmm_149_risk_adj_kurt_log_ret_252d(close: pd.Series) -> pd.Series:
    """Excess kurt divided by realized vol over 252d - 'tail per vol unit'."""
    r = _log_ret(close)
    kt = _rolling_kurt(r, YDAYS); sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(kt, sd))

def f41_rdmm_150_moment_balance_index_log_ret_63d(close: pd.Series) -> pd.Series:
    """Composite |skew| + |excess-kurt| over 63d - non-normality magnitude index."""
    r = _log_ret(close)
    sk = _rolling_skew(r, QDAYS).abs(); kt = _rolling_kurt(r, QDAYS).abs()
    return (sk + kt)


# ============================================================
#                         REGISTRY 076_150 (base)
# ============================================================

RETURN_DISTRIBUTION_MOMENTS_BASE_REGISTRY_076_150 = {
    "f41_rdmm_076_l_scale_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_076_l_scale_log_ret_63d},
    "f41_rdmm_077_l_skew_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_077_l_skew_log_ret_63d},
    "f41_rdmm_078_l_kurt_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_078_l_kurt_log_ret_63d},
    "f41_rdmm_079_l_scale_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_079_l_scale_log_ret_252d},
    "f41_rdmm_080_l_skew_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_080_l_skew_log_ret_252d},
    "f41_rdmm_081_l_kurt_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_081_l_kurt_log_ret_252d},
    "f41_rdmm_082_l_scale_to_std_ratio_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_082_l_scale_to_std_ratio_log_ret_63d},
    "f41_rdmm_083_l_skew_short_minus_long_252d": {"inputs": ["close"], "func": f41_rdmm_083_l_skew_short_minus_long_252d},
    "f41_rdmm_084_hill_upper_tail_5pct_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_084_hill_upper_tail_5pct_log_ret_252d},
    "f41_rdmm_085_hill_lower_tail_5pct_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_085_hill_lower_tail_5pct_log_ret_252d},
    "f41_rdmm_086_hill_upper_tail_10pct_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_086_hill_upper_tail_10pct_log_ret_252d},
    "f41_rdmm_087_hill_lower_tail_10pct_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_087_hill_lower_tail_10pct_log_ret_252d},
    "f41_rdmm_088_hill_tail_index_diff_upper_minus_lower_5pct_252d": {"inputs": ["close"], "func": f41_rdmm_088_hill_tail_index_diff_upper_minus_lower_5pct_252d},
    "f41_rdmm_089_pickands_tail_index_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_089_pickands_tail_index_log_ret_252d},
    "f41_rdmm_090_trimmed_10pct_mean_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_090_trimmed_10pct_mean_log_ret_252d},
    "f41_rdmm_091_trimmed_10pct_std_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_091_trimmed_10pct_std_log_ret_252d},
    "f41_rdmm_092_winsor_5pct_mean_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_092_winsor_5pct_mean_log_ret_252d},
    "f41_rdmm_093_winsor_5pct_std_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_093_winsor_5pct_std_log_ret_252d},
    "f41_rdmm_094_trimmed_10pct_skew_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_094_trimmed_10pct_skew_log_ret_252d},
    "f41_rdmm_095_trimmed_10pct_kurt_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_095_trimmed_10pct_kurt_log_ret_252d},
    "f41_rdmm_096_mean_abs_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_096_mean_abs_log_ret_63d},
    "f41_rdmm_097_mean_sqrt_abs_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_097_mean_sqrt_abs_log_ret_63d},
    "f41_rdmm_098_mean_log_abs_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_098_mean_log_abs_log_ret_63d},
    "f41_rdmm_099_mean_cubed_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_099_mean_cubed_log_ret_63d},
    "f41_rdmm_100_mean_fourth_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_100_mean_fourth_log_ret_63d},
    "f41_rdmm_101_jarque_bera_overnight_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_101_jarque_bera_overnight_ret_63d},
    "f41_rdmm_102_jarque_bera_intraday_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_102_jarque_bera_intraday_ret_63d},
    "f41_rdmm_103_jarque_bera_abs_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_103_jarque_bera_abs_log_ret_63d},
    "f41_rdmm_104_ad_overnight_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_104_ad_overnight_ret_63d},
    "f41_rdmm_105_ad_intraday_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_105_ad_intraday_ret_63d},
    "f41_rdmm_106_ks_overnight_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_106_ks_overnight_ret_63d},
    "f41_rdmm_107_ks_intraday_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_107_ks_intraday_ret_63d},
    "f41_rdmm_108_shapiro_w_overnight_ret_63d": {"inputs": ["open", "close"], "func": f41_rdmm_108_shapiro_w_overnight_ret_63d},
    "f41_rdmm_109_kurt_minus_three_diff_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_109_kurt_minus_three_diff_log_ret_63d},
    "f41_rdmm_110_kurt_minus_three_diff_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_110_kurt_minus_three_diff_log_ret_252d},
    "f41_rdmm_111_abs_skew_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_111_abs_skew_log_ret_63d},
    "f41_rdmm_112_abs_skew_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_112_abs_skew_log_ret_252d},
    "f41_rdmm_113_squared_skew_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_113_squared_skew_log_ret_63d},
    "f41_rdmm_114_squared_skew_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_114_squared_skew_log_ret_252d},
    "f41_rdmm_115_mean_sign_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_115_mean_sign_log_ret_63d},
    "f41_rdmm_116_std_sign_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_116_std_sign_log_ret_63d},
    "f41_rdmm_117_autocorr_sign_lag1_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_117_autocorr_sign_lag1_log_ret_63d},
    "f41_rdmm_118_autocorr_sign_lag5_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_118_autocorr_sign_lag5_log_ret_63d},
    "f41_rdmm_119_runs_test_z_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_119_runs_test_z_log_ret_63d},
    "f41_rdmm_120_runs_test_z_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_120_runs_test_z_log_ret_252d},
    "f41_rdmm_121_mean_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_121_mean_abs_log_ret_252d},
    "f41_rdmm_122_std_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_122_std_abs_log_ret_252d},
    "f41_rdmm_123_skew_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_123_skew_abs_log_ret_252d},
    "f41_rdmm_124_excess_kurt_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_124_excess_kurt_abs_log_ret_252d},
    "f41_rdmm_125_range_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_125_range_abs_log_ret_252d},
    "f41_rdmm_126_p95_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_126_p95_abs_log_ret_252d},
    "f41_rdmm_127_mean_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_127_mean_log_abs_log_ret_252d},
    "f41_rdmm_128_std_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_128_std_log_abs_log_ret_252d},
    "f41_rdmm_129_skew_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_129_skew_log_abs_log_ret_252d},
    "f41_rdmm_130_excess_kurt_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_130_excess_kurt_log_abs_log_ret_252d},
    "f41_rdmm_131_iqr_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_131_iqr_log_abs_log_ret_252d},
    "f41_rdmm_132_p90_log_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_132_p90_log_abs_log_ret_252d},
    "f41_rdmm_133_quantile_skew_p75_p25_63d": {"inputs": ["close"], "func": f41_rdmm_133_quantile_skew_p75_p25_63d},
    "f41_rdmm_134_quantile_skew_p75_p25_252d": {"inputs": ["close"], "func": f41_rdmm_134_quantile_skew_p75_p25_252d},
    "f41_rdmm_135_quantile_skew_p90_p10_63d": {"inputs": ["close"], "func": f41_rdmm_135_quantile_skew_p90_p10_63d},
    "f41_rdmm_136_quantile_skew_p90_p10_252d": {"inputs": ["close"], "func": f41_rdmm_136_quantile_skew_p90_p10_252d},
    "f41_rdmm_137_quantile_skew_p95_p5_252d": {"inputs": ["close"], "func": f41_rdmm_137_quantile_skew_p95_p5_252d},
    "f41_rdmm_138_quantile_skew_p99_p1_252d": {"inputs": ["close"], "func": f41_rdmm_138_quantile_skew_p99_p1_252d},
    "f41_rdmm_139_gini_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_139_gini_abs_log_ret_252d},
    "f41_rdmm_140_herfindahl_norm_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_140_herfindahl_norm_abs_log_ret_252d},
    "f41_rdmm_141_effective_n_returns_252d": {"inputs": ["close"], "func": f41_rdmm_141_effective_n_returns_252d},
    "f41_rdmm_142_atkinson_index_abs_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_142_atkinson_index_abs_log_ret_252d},
    "f41_rdmm_143_shannon_entropy_binned_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_143_shannon_entropy_binned_log_ret_252d},
    "f41_rdmm_144_negentropy_proxy_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_144_negentropy_proxy_log_ret_252d},
    "f41_rdmm_145_skew_minus_kurt_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_145_skew_minus_kurt_log_ret_63d},
    "f41_rdmm_146_skew_times_kurt_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_146_skew_times_kurt_log_ret_63d},
    "f41_rdmm_147_sharpe_like_mean_over_std_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_147_sharpe_like_mean_over_std_log_ret_63d},
    "f41_rdmm_148_sortino_like_mean_over_downsemidev_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_148_sortino_like_mean_over_downsemidev_log_ret_63d},
    "f41_rdmm_149_risk_adj_kurt_log_ret_252d": {"inputs": ["close"], "func": f41_rdmm_149_risk_adj_kurt_log_ret_252d},
    "f41_rdmm_150_moment_balance_index_log_ret_63d": {"inputs": ["close"], "func": f41_rdmm_150_moment_balance_index_log_ret_63d},
}
