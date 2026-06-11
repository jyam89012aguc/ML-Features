"""autocorrelation_persistence d3 features 001-075 - Pipeline 1b-technical.

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

def _rolling_ar1(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        a = v[:-1]; b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_acf_lag(s, n, lag, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, max(2 * lag + 4, 20))
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < max(lag + 10, 20):
            return np.nan
        a = v[:-lag]; b = v[lag:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_pacf_lag(s, n, lag, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, max(2 * lag + 8, 30))
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < max(lag + 15, 30):
            return np.nan
        # Yule-Walker via autocovariances up to lag `lag`
        v = v - v.mean()
        gammas = np.array([np.dot(v[:nv - k], v[k:]) / nv for k in range(lag + 1)])
        if gammas[0] <= 0:
            return np.nan
        R = np.array([[gammas[abs(i - j)] for j in range(lag)] for i in range(lag)])
        r = gammas[1:lag + 1]
        try:
            phi = np.linalg.solve(R, r)
        except np.linalg.LinAlgError:
            return np.nan
        return float(phi[-1])
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _ljung_box_q(s, n, max_lag):
    mp = max(n // 3, max(2 * max_lag + 8, 30))
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < max(max_lag + 15, 30):
            return np.nan
        v = v - v.mean()
        denom = float(np.dot(v, v))
        if denom <= 0:
            return np.nan
        q = 0.0
        for k in range(1, max_lag + 1):
            rho_k = float(np.dot(v[:nv - k], v[k:]) / denom)
            q += (rho_k * rho_k) / (nv - k)
        return float(nv * (nv + 2) * q)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _variance_ratio(s, n, k):
    mp = max(n // 3, max(4 * k, 40))
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < max(3 * k + 5, 40):
            return np.nan
        var_1 = np.var(v, ddof=1)
        if var_1 <= 0:
            return np.nan
        if nv % k != 0:
            v = v[: (nv // k) * k]
            nv = v.size
        agg = v.reshape(-1, k).sum(axis=1)
        var_k = np.var(agg, ddof=1) / k
        return float(var_k / var_1)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hurst_rs(s, n):
    mp = max(n // 3, 60)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 60:
            return np.nan
        chunks = [c for c in [8, 16, 32, 64, 128] if c <= nv // 2]
        if len(chunks) < 3:
            return np.nan
        rs_vals = []
        for c in chunks:
            usable = (nv // c) * c
            sub = v[:usable].reshape(-1, c)
            mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1)
            rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1)
            ok = sd > 0
            if ok.sum() < 1:
                continue
            ratio = float((rng[ok] / sd[ok]).mean())
            if np.isfinite(ratio) and ratio > 0:
                rs_vals.append(ratio)
        if len(rs_vals) < 3:
            return np.nan
        used = chunks[:len(rs_vals)]
        x = np.log(np.array(used, dtype=float))
        y = np.log(np.array(rs_vals, dtype=float))
        if np.var(x) == 0:
            return np.nan
        return float(np.polyfit(x, y, 1)[0])
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _dfa_alpha(s, n):
    mp = max(n // 3, 60)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 60:
            return np.nan
        y = np.cumsum(v - v.mean())
        scales = [c for c in [8, 16, 32, 64] if c <= nv // 4]
        if len(scales) < 2:
            return np.nan
        f_vals = []
        for c in scales:
            n_seg = nv // c
            if n_seg < 2:
                continue
            yt = y[:n_seg * c].reshape(n_seg, c)
            x = np.arange(c, dtype=float)
            xm = x.mean(); xxs = ((x - xm) ** 2).sum()
            if xxs <= 0:
                continue
            seg_var = []
            for seg in yt:
                ym = seg.mean()
                slope = ((x - xm) * (seg - ym)).sum() / xxs
                inter = ym - slope * xm
                pred = inter + slope * x
                seg_var.append(((seg - pred) ** 2).mean())
            f_vals.append(np.sqrt(np.mean(seg_var)))
        if len(f_vals) < 2:
            return np.nan
        x_log = np.log(np.array(scales[:len(f_vals)], dtype=float))
        y_log = np.log(np.array(f_vals, dtype=float))
        if np.var(x_log) == 0:
            return np.nan
        return float(np.polyfit(x_log, y_log, 1)[0])
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _permutation_entropy(s, n, dim=3):
    mp = max(n // 3, 30)
    from math import factorial
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < dim + 5:
            return np.nan
        counts = {}
        for i in range(len(v) - dim + 1):
            pat = tuple(np.argsort(v[i:i + dim]).tolist())
            counts[pat] = counts.get(pat, 0) + 1
        total = sum(counts.values())
        if total == 0:
            return np.nan
        ent = 0.0
        for c in counts.values():
            p = c / total
            ent -= p * np.log(p)
        max_ent = np.log(float(factorial(dim)))
        return float(ent / max_ent) if max_ent > 0 else np.nan
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _sample_entropy(s, n, m=2, r_frac=0.2):
    mp = max(n // 3, 40)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < m + 5:
            return np.nan
        r = r_frac * np.std(v, ddof=1)
        if r <= 0:
            return np.nan
        def _count(em):
            X = np.array([v[i:i + em] for i in range(nv - em + 1)])
            cnt = 0
            for i in range(len(X)):
                d = np.max(np.abs(X - X[i]), axis=1)
                cnt += int((d <= r).sum() - 1)
            return cnt
        a = _count(m + 1)
        b = _count(m)
        if a <= 0 or b <= 0:
            return np.nan
        return float(-np.log(a / b))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _higuchi_fd(s, n, k_max=8):
    mp = max(n // 3, 40)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < k_max * 3 + 5:
            return np.nan
        L = []
        K = []
        for k in range(1, k_max + 1):
            Lk = []
            for m in range(k):
                idx = np.arange(m, nv, k)
                if len(idx) < 2:
                    continue
                Lm = np.sum(np.abs(np.diff(v[idx]))) * (nv - 1) / (((nv - m) // k) * k)
                Lk.append(Lm)
            if Lk:
                L.append(np.mean(Lk))
                K.append(k)
        if len(L) < 2:
            return np.nan
        x = np.log(1.0 / np.array(K, dtype=float))
        y = np.log(np.array(L, dtype=float))
        if np.var(x) == 0:
            return np.nan
        return float(np.polyfit(x, y, 1)[0])
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _katz_fd(s, n):
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 10:
            return np.nan
        L = np.sum(np.sqrt(1.0 + np.diff(v) ** 2))
        d = np.max(np.sqrt(np.arange(1, nv, dtype=float) ** 2 + (v[1:] - v[0]) ** 2))
        if L <= 0 or d <= 0:
            return np.nan
        return float(np.log10(nv) / (np.log10(d / L) + np.log10(nv)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _petrosian_fd(s, n):
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 10:
            return np.nan
        d = np.diff(v)
        sgn = np.sign(d)
        Nd = int((sgn[1:] != sgn[:-1]).sum())
        denom = np.log10(nv) + np.log10(nv / (nv + 0.4 * Nd))
        if denom == 0:
            return np.nan
        return float(np.log10(nv) / denom)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _spectral_entropy(s, n):
    mp = max(n // 3, 40)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 40:
            return np.nan
        v = v - v.mean()
        fft = np.fft.rfft(v)
        psd = (np.abs(fft) ** 2)
        psd = psd[1:]
        tot = psd.sum()
        if tot <= 0:
            return np.nan
        p = psd / tot
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(psd)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _spectral_centroid(s, n):
    mp = max(n // 3, 40)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 40:
            return np.nan
        v = v - v.mean()
        fft = np.fft.rfft(v)
        psd = (np.abs(fft) ** 2)[1:]
        if psd.sum() <= 0:
            return np.nan
        freqs = np.arange(1, len(psd) + 1, dtype=float) / float(v.size)
        return float((freqs * psd).sum() / psd.sum())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _gph_d_estimator(s, n, m_frac=0.5):
    mp = max(n // 3, 60)
    def _f(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 60:
            return np.nan
        v = v - v.mean()
        fft = np.fft.rfft(v)
        psd = (np.abs(fft) ** 2)[1:]
        m = max(int(nv ** m_frac), 5)
        if m >= len(psd):
            m = len(psd) - 1
        if m < 5:
            return np.nan
        freqs = 2.0 * np.pi * np.arange(1, m + 1, dtype=float) / nv
        x = np.log(2.0 * np.sin(freqs / 2.0))
        y = np.log(psd[:m])
        mask = np.isfinite(x) & np.isfinite(y)
        if mask.sum() < 5:
            return np.nan
        x = x[mask]; y = y[mask]
        if np.var(x) == 0:
            return np.nan
        slope = np.polyfit(x, y, 1)[0]
        return float(-slope)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def f42_acpe_001_ar1_log_ret_21d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of raw return over 21d."""
    x = _log_ret(close)
    return (_rolling_ar1(x, MDAYS)).diff().diff().diff()

def f42_acpe_002_ar1_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of raw return over 63d."""
    x = _log_ret(close)
    return (_rolling_ar1(x, QDAYS)).diff().diff().diff()

def f42_acpe_003_ar1_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of raw return over 252d."""
    x = _log_ret(close)
    return (_rolling_ar1(x, YDAYS)).diff().diff().diff()

def f42_acpe_004_ar1_abs_log_ret_21d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of |return| (vol clustering) over 21d."""
    x = _log_ret(close).abs()
    return (_rolling_ar1(x, MDAYS)).diff().diff().diff()

def f42_acpe_005_ar1_abs_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of |return| (vol clustering) over 63d."""
    x = _log_ret(close).abs()
    return (_rolling_ar1(x, QDAYS)).diff().diff().diff()

def f42_acpe_006_ar1_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of |return| (vol clustering) over 252d."""
    x = _log_ret(close).abs()
    return (_rolling_ar1(x, YDAYS)).diff().diff().diff()

def f42_acpe_007_ar1_squared_log_ret_21d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of return^2 (ARCH persistence) over 21d."""
    x = _log_ret(close) ** 2
    return (_rolling_ar1(x, MDAYS)).diff().diff().diff()

def f42_acpe_008_ar1_squared_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of return^2 (ARCH persistence) over 63d."""
    x = _log_ret(close) ** 2
    return (_rolling_ar1(x, QDAYS)).diff().diff().diff()

def f42_acpe_009_ar1_squared_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of return^2 (ARCH persistence) over 252d."""
    x = _log_ret(close) ** 2
    return (_rolling_ar1(x, YDAYS)).diff().diff().diff()

def f42_acpe_010_acf_log_ret_lag1_63d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 1 over 63d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, QDAYS, 1)).diff().diff().diff()

def f42_acpe_011_acf_log_ret_lag2_63d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 2 over 63d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, QDAYS, 2)).diff().diff().diff()

def f42_acpe_012_acf_log_ret_lag5_63d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 5 over 63d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, QDAYS, 5)).diff().diff().diff()

def f42_acpe_013_acf_log_ret_lag10_63d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 10 over 63d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, QDAYS, 10)).diff().diff().diff()

def f42_acpe_014_acf_log_ret_lag21_252d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 21 over 252d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, YDAYS, 21)).diff().diff().diff()

def f42_acpe_015_acf_log_ret_lag63_252d_d3(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 63 over 252d."""
    r = _log_ret(close)
    return (_rolling_acf_lag(r, YDAYS, 63)).diff().diff().diff()

def f42_acpe_016_acf_abs_log_ret_lag1_63d_d3(close: pd.Series) -> pd.Series:
    """ACF of abs_log_ret at lag 1 over 63d."""
    x = _log_ret(close).abs()
    return (_rolling_acf_lag(x, QDAYS, 1)).diff().diff().diff()

def f42_acpe_017_acf_abs_log_ret_lag5_63d_d3(close: pd.Series) -> pd.Series:
    """ACF of abs_log_ret at lag 5 over 63d."""
    x = _log_ret(close).abs()
    return (_rolling_acf_lag(x, QDAYS, 5)).diff().diff().diff()

def f42_acpe_018_acf_abs_log_ret_lag21_252d_d3(close: pd.Series) -> pd.Series:
    """ACF of abs_log_ret at lag 21 over 252d."""
    x = _log_ret(close).abs()
    return (_rolling_acf_lag(x, YDAYS, 21)).diff().diff().diff()

def f42_acpe_019_acf_abs_log_ret_lag63_252d_d3(close: pd.Series) -> pd.Series:
    """ACF of abs_log_ret at lag 63 over 252d."""
    x = _log_ret(close).abs()
    return (_rolling_acf_lag(x, YDAYS, 63)).diff().diff().diff()

def f42_acpe_020_acf_squared_log_ret_lag1_63d_d3(close: pd.Series) -> pd.Series:
    """ACF of squared_log_ret at lag 1 over 63d."""
    x = _log_ret(close) ** 2
    return (_rolling_acf_lag(x, QDAYS, 1)).diff().diff().diff()

def f42_acpe_021_acf_squared_log_ret_lag5_63d_d3(close: pd.Series) -> pd.Series:
    """ACF of squared_log_ret at lag 5 over 63d."""
    x = _log_ret(close) ** 2
    return (_rolling_acf_lag(x, QDAYS, 5)).diff().diff().diff()

def f42_acpe_022_ljung_box_q_lag10_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on log-returns over 63d."""
    r = _log_ret(close)
    return (_ljung_box_q(r, QDAYS, 10)).diff().diff().diff()

def f42_acpe_023_ljung_box_q_lag10_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on log-returns over 252d."""
    r = _log_ret(close)
    return (_ljung_box_q(r, YDAYS, 10)).diff().diff().diff()

def f42_acpe_024_ljung_box_q_lag10_abs_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on |r| over 63d."""
    x = _log_ret(close).abs()
    return (_ljung_box_q(x, QDAYS, 10)).diff().diff().diff()

def f42_acpe_025_ljung_box_q_lag10_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_ljung_box_q(x, YDAYS, 10)).diff().diff().diff()

def f42_acpe_026_ljung_box_q_lag10_squared_log_ret_63d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 10 on r^2 over 63d (ARCH test)."""
    x = _log_ret(close) ** 2
    return (_ljung_box_q(x, QDAYS, 10)).diff().diff().diff()

def f42_acpe_027_ljung_box_q_lag21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Ljung-Box Q at lag 21 on log-returns over 252d."""
    r = _log_ret(close)
    return (_ljung_box_q(r, YDAYS, 21)).diff().diff().diff()

def f42_acpe_028_var_ratio_lag2_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=2 of log-returns over 252d."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 2)).diff().diff().diff()

def f42_acpe_029_var_ratio_lag5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=5 of log-returns over 252d."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 5)).diff().diff().diff()

def f42_acpe_030_var_ratio_lag10_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=10 of log-returns over 252d."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 10)).diff().diff().diff()

def f42_acpe_031_var_ratio_lag21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=21 of log-returns over 252d."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 21)).diff().diff().diff()

def f42_acpe_032_var_ratio_lag63_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=63 of log-returns over 504d."""
    r = _log_ret(close)
    return (_variance_ratio(r, DDAYS_2Y, 63)).diff().diff().diff()

def f42_acpe_033_var_ratio_lag2_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance ratio at k=2 of |r| over 252d - vol persistence test."""
    x = _log_ret(close).abs()
    return (_variance_ratio(x, YDAYS, 2)).diff().diff().diff()

def f42_acpe_034_hurst_rs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Hurst exponent via R/S of log-returns over 252d."""
    r = _log_ret(close)
    return (_hurst_rs(r, YDAYS)).diff().diff().diff()

def f42_acpe_035_hurst_rs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Hurst R/S of log-returns over 504d."""
    r = _log_ret(close)
    return (_hurst_rs(r, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_036_hurst_rs_log_ret_1260d_d3(close: pd.Series) -> pd.Series:
    """Hurst R/S of log-returns over 1260d (5y)."""
    r = _log_ret(close)
    return (_hurst_rs(r, DDAYS_5Y)).diff().diff().diff()

def f42_acpe_037_hurst_rs_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Hurst R/S of |r| over 252d - long-memory in vol."""
    x = _log_ret(close).abs()
    return (_hurst_rs(x, YDAYS)).diff().diff().diff()

def f42_acpe_038_hurst_rs_abs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Hurst R/S of |r| over 504d."""
    x = _log_ret(close).abs()
    return (_hurst_rs(x, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_039_hurst_rs_abs_log_ret_1260d_d3(close: pd.Series) -> pd.Series:
    """Hurst R/S of |r| over 1260d."""
    x = _log_ret(close).abs()
    return (_hurst_rs(x, DDAYS_5Y)).diff().diff().diff()

def f42_acpe_040_dfa_alpha_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """DFA exponent (alpha) on log-returns over 252d."""
    r = _log_ret(close)
    return (_dfa_alpha(r, YDAYS)).diff().diff().diff()

def f42_acpe_041_dfa_alpha_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """DFA alpha on log-returns over 504d."""
    r = _log_ret(close)
    return (_dfa_alpha(r, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_042_dfa_alpha_log_ret_1260d_d3(close: pd.Series) -> pd.Series:
    """DFA alpha on log-returns over 1260d."""
    r = _log_ret(close)
    return (_dfa_alpha(r, DDAYS_5Y)).diff().diff().diff()

def f42_acpe_043_dfa_alpha_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """DFA alpha on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_dfa_alpha(x, YDAYS)).diff().diff().diff()

def f42_acpe_044_dfa_alpha_abs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """DFA alpha on |r| over 504d."""
    x = _log_ret(close).abs()
    return (_dfa_alpha(x, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_045_dfa_alpha_abs_log_ret_1260d_d3(close: pd.Series) -> pd.Series:
    """DFA alpha on |r| over 1260d."""
    x = _log_ret(close).abs()
    return (_dfa_alpha(x, DDAYS_5Y)).diff().diff().diff()

def f42_acpe_046_pacf_log_ret_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """Partial autocorrelation of log-returns at lag 1 over 252d."""
    r = _log_ret(close)
    return (_rolling_pacf_lag(r, YDAYS, 1)).diff().diff().diff()

def f42_acpe_047_pacf_log_ret_lag5_252d_d3(close: pd.Series) -> pd.Series:
    """PACF at lag 5 over 252d."""
    r = _log_ret(close)
    return (_rolling_pacf_lag(r, YDAYS, 5)).diff().diff().diff()

def f42_acpe_048_pacf_log_ret_lag10_252d_d3(close: pd.Series) -> pd.Series:
    """PACF at lag 10 over 252d."""
    r = _log_ret(close)
    return (_rolling_pacf_lag(r, YDAYS, 10)).diff().diff().diff()

def f42_acpe_049_pacf_log_ret_lag21_252d_d3(close: pd.Series) -> pd.Series:
    """PACF at lag 21 over 252d."""
    r = _log_ret(close)
    return (_rolling_pacf_lag(r, YDAYS, 21)).diff().diff().diff()

def f42_acpe_050_pacf_abs_log_ret_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """PACF of |r| at lag 1 over 252d."""
    x = _log_ret(close).abs()
    return (_rolling_pacf_lag(x, YDAYS, 1)).diff().diff().diff()

def f42_acpe_051_ar1_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of log-close itself over 252d - price-level persistence."""
    lc = _safe_log(close)
    return (_rolling_ar1(lc, YDAYS)).diff().diff().diff()

def f42_acpe_052_ar1_detrended_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of log-close minus its 252d mean - detrended persistence."""
    lc = _safe_log(close)
    mu = lc.rolling(YDAYS, min_periods=QDAYS).mean()
    detr = lc - mu
    return (_rolling_ar1(detr, YDAYS)).diff().diff().diff()

def f42_acpe_053_ar1_residual_from_lsma_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of residual log-close minus rolling LSMA (linear-reg trend) over 252d."""
    lc = _safe_log(close)
    def _lsma_t(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        num = ((x - xm) * (w - wm)).sum(); den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        sl = num / den; ic = wm - sl * xm
        return float(ic + sl * (len(w) - 1))
    lsma = lc.rolling(MDAYS, min_periods=10).apply(_lsma_t, raw=True)
    resid = lc - lsma
    return (_rolling_ar1(resid, YDAYS)).diff().diff().diff()

def f42_acpe_054_ar1_log_ret_minus_mean_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of return - rolling-mean residual over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    resid = r - mu
    return (_rolling_ar1(resid, YDAYS)).diff().diff().diff()

def f42_acpe_055_mean_reversion_half_life_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """Half-life implied by AR(1) of log-close over 252d (-log2/log|phi|)."""
    lc = _safe_log(close)
    phi = _rolling_ar1(lc, YDAYS).abs().clip(upper=0.999).replace(0, np.nan)
    hl = -np.log(2.0) / np.log(phi)
    return (hl).diff().diff().diff()

def f42_acpe_056_mean_reversion_speed_OU_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """Mean-reversion speed = 1-AR(1) of detrended log-close over 252d (OU lambda proxy)."""
    lc = _safe_log(close)
    mu = lc.rolling(YDAYS, min_periods=QDAYS).mean()
    detr = lc - mu
    return (1.0 - _rolling_ar1(detr, YDAYS)).diff().diff().diff()

def f42_acpe_057_variance_scaling_exponent_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Slope of log Var(k-period r) vs log k for k in {1,2,5,10,21} over 252d - 2H ideally."""
    r = _log_ret(close)
    def _vsx(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        x = np.array(xs); y = np.array(ys)
        if np.var(x) == 0:
            return np.nan
        return float(np.polyfit(x, y, 1)[0])
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_vsx, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_058_variance_scaling_exponent_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Variance-scaling exponent over 504d."""
    r = _log_ret(close)
    def _vsx(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21, 63]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        x = np.array(xs); y = np.array(ys)
        if np.var(x) == 0:
            return np.nan
        return float(np.polyfit(x, y, 1)[0])
    res = r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_vsx, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_059_variance_scaling_exponent_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Variance scaling exponent for |r| over 252d - vol-scaling memory."""
    x = _log_ret(close).abs()
    def _vsx(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        xa = np.array(xs); ya = np.array(ys)
        if np.var(xa) == 0:
            return np.nan
        return float(np.polyfit(xa, ya, 1)[0])
    res = x.rolling(YDAYS, min_periods=QDAYS).apply(_vsx, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_060_variance_scaling_exponent_abs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Variance scaling exponent for |r| over 504d."""
    x = _log_ret(close).abs()
    def _vsx(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21, 63]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        xa = np.array(xs); ya = np.array(ys)
        if np.var(xa) == 0:
            return np.nan
        return float(np.polyfit(xa, ya, 1)[0])
    res = x.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_vsx, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_061_variance_scaling_residual_norm_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Residual norm of variance-scaling regression over 252d - how well it fits a power law."""
    r = _log_ret(close)
    def _res(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        xa = np.array(xs); ya = np.array(ys)
        if np.var(xa) == 0:
            return np.nan
        p = np.polyfit(xa, ya, 1)
        pred = np.polyval(p, xa)
        return float(np.sqrt(np.mean((ya - pred) ** 2)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_res, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_062_variance_scaling_intercept_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Intercept of variance-scaling log-log regression over 252d."""
    r = _log_ret(close)
    def _inter(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        ks = [1, 2, 5, 10, 21]
        xs, ys = [], []
        for k in ks:
            if v.size < 3 * k:
                continue
            usable = (v.size // k) * k
            agg = v[:usable].reshape(-1, k).sum(axis=1)
            if agg.size < 5:
                continue
            vk = float(np.var(agg, ddof=1))
            if vk <= 0:
                continue
            xs.append(np.log(k)); ys.append(np.log(vk))
        if len(xs) < 3:
            return np.nan
        xa = np.array(xs); ya = np.array(ys)
        if np.var(xa) == 0:
            return np.nan
        return float(np.polyfit(xa, ya, 1)[1])
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_inter, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_063_sign_acf_lag1_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """ACF of sign(r) at lag 1 over 252d."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    return (_rolling_acf_lag(sg, YDAYS, 1)).diff().diff().diff()

def f42_acpe_064_sign_acf_lag5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """ACF of sign(r) at lag 5 over 252d."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    return (_rolling_acf_lag(sg, YDAYS, 5)).diff().diff().diff()

def f42_acpe_065_sign_acf_lag21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """ACF of sign(r) at lag 21 over 252d."""
    r = _log_ret(close)
    sg = np.sign(r).where(r.notna(), np.nan)
    return (_rolling_acf_lag(sg, YDAYS, 21)).diff().diff().diff()

def f42_acpe_066_runs_count_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Total count of sign-runs in log-returns over 252d."""
    r = _log_ret(close)
    def _rc(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sgn = np.where(v > 0, 1, -1)
        return float(1 + int((sgn[1:] != sgn[:-1]).sum()))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_rc, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_067_runs_expected_minus_observed_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Expected (under independence) minus observed run count over 252d - persistence direction."""
    r = _log_ret(close)
    def _diff(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30:
            return np.nan
        sgn = np.where(v > 0, 1, -1)
        n_pos = int((sgn > 0).sum()); n_neg = nv - n_pos
        if n_pos == 0 or n_neg == 0:
            return np.nan
        obs = 1 + int((sgn[1:] != sgn[:-1]).sum())
        exp = 2.0 * n_pos * n_neg / nv + 1.0
        return float(exp - obs)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_diff, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_068_wald_wolfowitz_z_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs-test z-stat over 252d."""
    r = _log_ret(close)
    def _ww(w):
        v = w[~np.isnan(w)]
        nv = v.size
        if nv < 30:
            return np.nan
        sgn = np.where(v > 0, 1, -1)
        n_pos = int((sgn > 0).sum()); n_neg = nv - n_pos
        if n_pos == 0 or n_neg == 0:
            return np.nan
        runs = 1 + int((sgn[1:] != sgn[:-1]).sum())
        mu = 2.0 * n_pos * n_neg / nv + 1.0
        var = (mu - 1.0) * (mu - 2.0) / (nv - 1.0)
        if var <= 0:
            return np.nan
        return float((runs - mu) / np.sqrt(var))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ww, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_069_dominant_period_pgram_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Period (in bars) of dominant Fourier frequency on 252d log-returns."""
    r = _log_ret(close)
    def _dp(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        fft = np.fft.rfft(v)
        psd = (np.abs(fft) ** 2)[1:]
        if psd.size == 0 or psd.sum() <= 0:
            return np.nan
        k = int(np.argmax(psd)) + 1
        return float(v.size / k)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_dp, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_070_spectral_entropy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Normalized Shannon entropy of the PSD of 252d log-returns."""
    r = _log_ret(close)
    return (_spectral_entropy(r, YDAYS)).diff().diff().diff()

def f42_acpe_071_low_freq_power_share_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Share of PSD power in frequencies below 0.1*Nyquist over 252d."""
    r = _log_ret(close)
    def _lf(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        if psd.sum() <= 0:
            return np.nan
        cutoff = max(int(0.1 * len(psd)), 1)
        return float(psd[:cutoff].sum() / psd.sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_lf, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_072_high_freq_power_share_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Share of PSD power in frequencies above 0.7*Nyquist over 252d."""
    r = _log_ret(close)
    def _hf(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        if psd.sum() <= 0:
            return np.nan
        cutoff = int(0.7 * len(psd))
        return float(psd[cutoff:].sum() / psd.sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_hf, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_073_spectral_centroid_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Spectral centroid (mean frequency weighted by PSD) over 252d."""
    r = _log_ret(close)
    return (_spectral_centroid(r, YDAYS)).diff().diff().diff()

def f42_acpe_074_spectral_skewness_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Skewness of PSD distribution across frequencies over 252d."""
    r = _log_ret(close)
    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        if psd.sum() <= 0:
            return np.nan
        p = psd / psd.sum()
        f = np.arange(1, len(psd) + 1, dtype=float)
        mu = (f * p).sum()
        sd = np.sqrt(((f - mu) ** 2 * p).sum())
        if sd <= 0:
            return np.nan
        return float((((f - mu) / sd) ** 3 * p).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sk, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_075_higuchi_fd_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of log-returns over 252d."""
    r = _log_ret(close)
    return (_higuchi_fd(r, YDAYS)).diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

AUTOCORRELATION_PERSISTENCE_D3_REGISTRY_001_075 = {
    "f42_acpe_001_ar1_log_ret_21d_d3": {"inputs": ["close"], "func": f42_acpe_001_ar1_log_ret_21d_d3},
    "f42_acpe_002_ar1_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_002_ar1_log_ret_63d_d3},
    "f42_acpe_003_ar1_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_003_ar1_log_ret_252d_d3},
    "f42_acpe_004_ar1_abs_log_ret_21d_d3": {"inputs": ["close"], "func": f42_acpe_004_ar1_abs_log_ret_21d_d3},
    "f42_acpe_005_ar1_abs_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_005_ar1_abs_log_ret_63d_d3},
    "f42_acpe_006_ar1_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_006_ar1_abs_log_ret_252d_d3},
    "f42_acpe_007_ar1_squared_log_ret_21d_d3": {"inputs": ["close"], "func": f42_acpe_007_ar1_squared_log_ret_21d_d3},
    "f42_acpe_008_ar1_squared_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_008_ar1_squared_log_ret_63d_d3},
    "f42_acpe_009_ar1_squared_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_009_ar1_squared_log_ret_252d_d3},
    "f42_acpe_010_acf_log_ret_lag1_63d_d3": {"inputs": ["close"], "func": f42_acpe_010_acf_log_ret_lag1_63d_d3},
    "f42_acpe_011_acf_log_ret_lag2_63d_d3": {"inputs": ["close"], "func": f42_acpe_011_acf_log_ret_lag2_63d_d3},
    "f42_acpe_012_acf_log_ret_lag5_63d_d3": {"inputs": ["close"], "func": f42_acpe_012_acf_log_ret_lag5_63d_d3},
    "f42_acpe_013_acf_log_ret_lag10_63d_d3": {"inputs": ["close"], "func": f42_acpe_013_acf_log_ret_lag10_63d_d3},
    "f42_acpe_014_acf_log_ret_lag21_252d_d3": {"inputs": ["close"], "func": f42_acpe_014_acf_log_ret_lag21_252d_d3},
    "f42_acpe_015_acf_log_ret_lag63_252d_d3": {"inputs": ["close"], "func": f42_acpe_015_acf_log_ret_lag63_252d_d3},
    "f42_acpe_016_acf_abs_log_ret_lag1_63d_d3": {"inputs": ["close"], "func": f42_acpe_016_acf_abs_log_ret_lag1_63d_d3},
    "f42_acpe_017_acf_abs_log_ret_lag5_63d_d3": {"inputs": ["close"], "func": f42_acpe_017_acf_abs_log_ret_lag5_63d_d3},
    "f42_acpe_018_acf_abs_log_ret_lag21_252d_d3": {"inputs": ["close"], "func": f42_acpe_018_acf_abs_log_ret_lag21_252d_d3},
    "f42_acpe_019_acf_abs_log_ret_lag63_252d_d3": {"inputs": ["close"], "func": f42_acpe_019_acf_abs_log_ret_lag63_252d_d3},
    "f42_acpe_020_acf_squared_log_ret_lag1_63d_d3": {"inputs": ["close"], "func": f42_acpe_020_acf_squared_log_ret_lag1_63d_d3},
    "f42_acpe_021_acf_squared_log_ret_lag5_63d_d3": {"inputs": ["close"], "func": f42_acpe_021_acf_squared_log_ret_lag5_63d_d3},
    "f42_acpe_022_ljung_box_q_lag10_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_022_ljung_box_q_lag10_log_ret_63d_d3},
    "f42_acpe_023_ljung_box_q_lag10_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_023_ljung_box_q_lag10_log_ret_252d_d3},
    "f42_acpe_024_ljung_box_q_lag10_abs_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_024_ljung_box_q_lag10_abs_log_ret_63d_d3},
    "f42_acpe_025_ljung_box_q_lag10_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_025_ljung_box_q_lag10_abs_log_ret_252d_d3},
    "f42_acpe_026_ljung_box_q_lag10_squared_log_ret_63d_d3": {"inputs": ["close"], "func": f42_acpe_026_ljung_box_q_lag10_squared_log_ret_63d_d3},
    "f42_acpe_027_ljung_box_q_lag21_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_027_ljung_box_q_lag21_log_ret_252d_d3},
    "f42_acpe_028_var_ratio_lag2_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_028_var_ratio_lag2_log_ret_252d_d3},
    "f42_acpe_029_var_ratio_lag5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_029_var_ratio_lag5_log_ret_252d_d3},
    "f42_acpe_030_var_ratio_lag10_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_030_var_ratio_lag10_log_ret_252d_d3},
    "f42_acpe_031_var_ratio_lag21_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_031_var_ratio_lag21_log_ret_252d_d3},
    "f42_acpe_032_var_ratio_lag63_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_032_var_ratio_lag63_log_ret_504d_d3},
    "f42_acpe_033_var_ratio_lag2_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_033_var_ratio_lag2_abs_log_ret_252d_d3},
    "f42_acpe_034_hurst_rs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_034_hurst_rs_log_ret_252d_d3},
    "f42_acpe_035_hurst_rs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_035_hurst_rs_log_ret_504d_d3},
    "f42_acpe_036_hurst_rs_log_ret_1260d_d3": {"inputs": ["close"], "func": f42_acpe_036_hurst_rs_log_ret_1260d_d3},
    "f42_acpe_037_hurst_rs_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_037_hurst_rs_abs_log_ret_252d_d3},
    "f42_acpe_038_hurst_rs_abs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_038_hurst_rs_abs_log_ret_504d_d3},
    "f42_acpe_039_hurst_rs_abs_log_ret_1260d_d3": {"inputs": ["close"], "func": f42_acpe_039_hurst_rs_abs_log_ret_1260d_d3},
    "f42_acpe_040_dfa_alpha_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_040_dfa_alpha_log_ret_252d_d3},
    "f42_acpe_041_dfa_alpha_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_041_dfa_alpha_log_ret_504d_d3},
    "f42_acpe_042_dfa_alpha_log_ret_1260d_d3": {"inputs": ["close"], "func": f42_acpe_042_dfa_alpha_log_ret_1260d_d3},
    "f42_acpe_043_dfa_alpha_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_043_dfa_alpha_abs_log_ret_252d_d3},
    "f42_acpe_044_dfa_alpha_abs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_044_dfa_alpha_abs_log_ret_504d_d3},
    "f42_acpe_045_dfa_alpha_abs_log_ret_1260d_d3": {"inputs": ["close"], "func": f42_acpe_045_dfa_alpha_abs_log_ret_1260d_d3},
    "f42_acpe_046_pacf_log_ret_lag1_252d_d3": {"inputs": ["close"], "func": f42_acpe_046_pacf_log_ret_lag1_252d_d3},
    "f42_acpe_047_pacf_log_ret_lag5_252d_d3": {"inputs": ["close"], "func": f42_acpe_047_pacf_log_ret_lag5_252d_d3},
    "f42_acpe_048_pacf_log_ret_lag10_252d_d3": {"inputs": ["close"], "func": f42_acpe_048_pacf_log_ret_lag10_252d_d3},
    "f42_acpe_049_pacf_log_ret_lag21_252d_d3": {"inputs": ["close"], "func": f42_acpe_049_pacf_log_ret_lag21_252d_d3},
    "f42_acpe_050_pacf_abs_log_ret_lag1_252d_d3": {"inputs": ["close"], "func": f42_acpe_050_pacf_abs_log_ret_lag1_252d_d3},
    "f42_acpe_051_ar1_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_051_ar1_log_close_252d_d3},
    "f42_acpe_052_ar1_detrended_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_052_ar1_detrended_log_close_252d_d3},
    "f42_acpe_053_ar1_residual_from_lsma_252d_d3": {"inputs": ["close"], "func": f42_acpe_053_ar1_residual_from_lsma_252d_d3},
    "f42_acpe_054_ar1_log_ret_minus_mean_252d_d3": {"inputs": ["close"], "func": f42_acpe_054_ar1_log_ret_minus_mean_252d_d3},
    "f42_acpe_055_mean_reversion_half_life_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_055_mean_reversion_half_life_log_close_252d_d3},
    "f42_acpe_056_mean_reversion_speed_OU_proxy_252d_d3": {"inputs": ["close"], "func": f42_acpe_056_mean_reversion_speed_OU_proxy_252d_d3},
    "f42_acpe_057_variance_scaling_exponent_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_057_variance_scaling_exponent_log_ret_252d_d3},
    "f42_acpe_058_variance_scaling_exponent_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_058_variance_scaling_exponent_log_ret_504d_d3},
    "f42_acpe_059_variance_scaling_exponent_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_059_variance_scaling_exponent_abs_log_ret_252d_d3},
    "f42_acpe_060_variance_scaling_exponent_abs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_060_variance_scaling_exponent_abs_log_ret_504d_d3},
    "f42_acpe_061_variance_scaling_residual_norm_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_061_variance_scaling_residual_norm_log_ret_252d_d3},
    "f42_acpe_062_variance_scaling_intercept_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_062_variance_scaling_intercept_log_ret_252d_d3},
    "f42_acpe_063_sign_acf_lag1_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_063_sign_acf_lag1_log_ret_252d_d3},
    "f42_acpe_064_sign_acf_lag5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_064_sign_acf_lag5_log_ret_252d_d3},
    "f42_acpe_065_sign_acf_lag21_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_065_sign_acf_lag21_log_ret_252d_d3},
    "f42_acpe_066_runs_count_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_066_runs_count_log_ret_252d_d3},
    "f42_acpe_067_runs_expected_minus_observed_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_067_runs_expected_minus_observed_log_ret_252d_d3},
    "f42_acpe_068_wald_wolfowitz_z_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_068_wald_wolfowitz_z_log_ret_252d_d3},
    "f42_acpe_069_dominant_period_pgram_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_069_dominant_period_pgram_log_ret_252d_d3},
    "f42_acpe_070_spectral_entropy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_070_spectral_entropy_log_ret_252d_d3},
    "f42_acpe_071_low_freq_power_share_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_071_low_freq_power_share_log_ret_252d_d3},
    "f42_acpe_072_high_freq_power_share_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_072_high_freq_power_share_log_ret_252d_d3},
    "f42_acpe_073_spectral_centroid_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_073_spectral_centroid_log_ret_252d_d3},
    "f42_acpe_074_spectral_skewness_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_074_spectral_skewness_log_ret_252d_d3},
    "f42_acpe_075_higuchi_fd_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_075_higuchi_fd_log_ret_252d_d3},
}
