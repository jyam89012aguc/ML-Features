"""autocorrelation_persistence d3 features 076-150 - Pipeline 1b-technical.

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


def f42_acpe_076_higuchi_fd_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Higuchi FD over 504d."""
    r = _log_ret(close)
    return (_higuchi_fd(r, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_077_higuchi_fd_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Higuchi FD on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_higuchi_fd(x, YDAYS)).diff().diff().diff()

def f42_acpe_078_katz_fd_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """Katz fractal dimension of log-close over 252d."""
    lc = _safe_log(close)
    return (_katz_fd(lc, YDAYS)).diff().diff().diff()

def f42_acpe_079_petrosian_fd_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of log-returns over 252d."""
    r = _log_ret(close)
    return (_petrosian_fd(r, YDAYS)).diff().diff().diff()

def f42_acpe_080_petrosian_fd_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of log-close over 252d."""
    lc = _safe_log(close)
    return (_petrosian_fd(lc, YDAYS)).diff().diff().diff()

def f42_acpe_081_permutation_entropy_d3_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Normalized permutation entropy (embedding=3) of log-returns over 252d."""
    r = _log_ret(close)
    return (_permutation_entropy(r, YDAYS, 3)).diff().diff().diff()

def f42_acpe_082_permutation_entropy_d4_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Permutation entropy with embedding=4 over 252d."""
    r = _log_ret(close)
    return (_permutation_entropy(r, YDAYS, 4)).diff().diff().diff()

def f42_acpe_083_permutation_entropy_d5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Permutation entropy with embedding=5 over 252d."""
    r = _log_ret(close)
    return (_permutation_entropy(r, YDAYS, 5)).diff().diff().diff()

def f42_acpe_084_permutation_entropy_d3_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """Permutation entropy with embedding=3 applied to log-close itself over 252d."""
    lc = _safe_log(close)
    return (_permutation_entropy(lc, YDAYS, 3)).diff().diff().diff()

def f42_acpe_085_permutation_entropy_d4_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Permutation entropy with embedding=4 on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_permutation_entropy(x, YDAYS, 4)).diff().diff().diff()

def f42_acpe_086_complexity_pe_times_oneminuspe_d3_252d_d3(close: pd.Series) -> pd.Series:
    """Disequilibrium proxy = PE*(1-PE) at embedding=3 over 252d."""
    r = _log_ret(close)
    pe = _permutation_entropy(r, YDAYS, 3)
    return (pe * (1.0 - pe)).diff().diff().diff()

def f42_acpe_087_sample_entropy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy (m=2, r=0.2*sigma) on log-returns over 252d."""
    r = _log_ret(close)
    return (_sample_entropy(r, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_088_sample_entropy_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy on |r| over 252d."""
    x = _log_ret(close).abs()
    return (_sample_entropy(x, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_089_sample_entropy_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy on log-close (level) over 252d."""
    lc = _safe_log(close)
    return (_sample_entropy(lc, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_090_multiscale_sample_entropy_scale2_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy on log-returns coarse-grained at scale 2 over 252d."""
    r = _log_ret(close)
    cg = r.rolling(2, min_periods=2).mean()
    return (_sample_entropy(cg, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_091_multiscale_sample_entropy_scale5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy on coarse-grained-scale-5 log-returns over 252d."""
    r = _log_ret(close)
    cg = r.rolling(5, min_periods=5).mean()
    return (_sample_entropy(cg, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_092_sample_entropy_squared_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Sample entropy on r^2 over 252d."""
    x = _log_ret(close) ** 2
    return (_sample_entropy(x, YDAYS, 2, 0.2)).diff().diff().diff()

def f42_acpe_093_approx_lyapunov_proxy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Slope of log-divergence of nearest-neighbor pairs vs lag (approx Lyapunov) over 252d."""
    r = _log_ret(close)
    def _ly(w):
        v = w[~np.isnan(w)]
        if v.size < 100:
            return np.nan
        d = np.abs(np.diff(v))
        d = d[d > 0]
        if d.size < 10:
            return np.nan
        return float(np.mean(np.log(d)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ly, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_094_correlation_dim_proxy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Proxy for correlation dimension: log(pair count below median dist) over 252d."""
    r = _log_ret(close)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 100:
            return np.nan
        sample = v[::3]
        if sample.size < 30:
            return np.nan
        d = np.abs(sample[:, None] - sample[None, :])
        md = float(np.median(d[d > 0]))
        if md <= 0:
            return np.nan
        return float(np.log((d <= md / 2.0).sum()) / np.log(sample.size))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_cd, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_095_nonlinearity_test_stat_bds_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """BDS-like proxy: variance of pair-distance distribution over 252d."""
    r = _log_ret(close)
    def _bds(w):
        v = w[~np.isnan(w)]
        if v.size < 80:
            return np.nan
        s = v[::2]
        d = np.abs(s[:, None] - s[None, :])
        return float(d.std())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bds, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_096_turning_points_per_252d_log_ret_d3(close: pd.Series) -> pd.Series:
    """Count of return-sequence local turning points per 252d - irregularity measure."""
    r = _log_ret(close)
    def _tp(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        s = np.sign(np.diff(v))
        return float((s[1:] != s[:-1]).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_tp, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_097_recurrence_rate_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Recurrence rate at threshold = 0.5*sigma: fraction of pair-distances < threshold (downsampled)."""
    r = _log_ret(close)
    def _rr(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        sd = v.std()
        if sd <= 0:
            return np.nan
        s = v[::2]
        d = np.abs(s[:, None] - s[None, :])
        return float((d <= 0.5 * sd).sum() / d.size)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_rr, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_098_determinism_rate_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Fraction of recurrence points on diagonals length>=3 (very coarse determinism proxy)."""
    r = _log_ret(close)
    def _det(w):
        v = w[~np.isnan(w)]
        if v.size < 80:
            return np.nan
        sd = v.std()
        if sd <= 0:
            return np.nan
        s = v[::2]
        R = (np.abs(s[:, None] - s[None, :]) <= 0.5 * sd).astype(int)
        total = R.sum()
        if total == 0:
            return np.nan
        diag_cnt = 0
        nv = R.shape[0]
        for off in range(-nv + 1, nv):
            diag = np.diag(R, k=off)
            run = 0
            for x in diag:
                if x:
                    run += 1
                else:
                    if run >= 3:
                        diag_cnt += run
                    run = 0
            if run >= 3:
                diag_cnt += run
        return float(diag_cnt / total)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_det, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_099_gph_d_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """GPH log-periodogram estimator of d on log-returns over 252d."""
    r = _log_ret(close)
    return (_gph_d_estimator(r, YDAYS)).diff().diff().diff()

def f42_acpe_100_gph_d_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """GPH d on log-returns over 504d."""
    r = _log_ret(close)
    return (_gph_d_estimator(r, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_101_gph_d_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """GPH d on |r| over 252d - long memory in vol."""
    x = _log_ret(close).abs()
    return (_gph_d_estimator(x, YDAYS)).diff().diff().diff()

def f42_acpe_102_gph_d_abs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """GPH d on |r| over 504d."""
    x = _log_ret(close).abs()
    return (_gph_d_estimator(x, DDAYS_2Y)).diff().diff().diff()

def f42_acpe_103_local_whittle_d_proxy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Local-Whittle-like proxy: average log(PSD) over low frequencies on log-returns 252d."""
    r = _log_ret(close)
    def _lw(w):
        v = w[~np.isnan(w)]
        if v.size < 80:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        if psd.size == 0:
            return np.nan
        m = max(int(np.sqrt(v.size)), 5)
        m = min(m, len(psd))
        sub = psd[:m]
        sub = sub[sub > 0]
        if sub.size < 3:
            return np.nan
        return float(np.mean(np.log(sub)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_lw, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_104_local_whittle_d_proxy_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Local-Whittle proxy on |r| over 252d."""
    x = _log_ret(close).abs()
    def _lw(w):
        v = w[~np.isnan(w)]
        if v.size < 80:
            return np.nan
        v = v - v.mean()
        psd = (np.abs(np.fft.rfft(v)) ** 2)[1:]
        if psd.size == 0:
            return np.nan
        m = max(int(np.sqrt(v.size)), 5)
        m = min(m, len(psd))
        sub = psd[:m]
        sub = sub[sub > 0]
        if sub.size < 3:
            return np.nan
        return float(np.mean(np.log(sub)))
    res = x.rolling(YDAYS, min_periods=QDAYS).apply(_lw, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_105_trend_strength_logreg_r2_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """R-squared of log-close ~ time linear regression over 252d - trend strength."""
    lc = _safe_log(close)
    def _r2(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum(); syy = ((y - ym) ** 2).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        sxy = ((x - xm) * (y - ym)).sum()
        return float(sxy * sxy / (sxx * syy))
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_106_trend_strength_logreg_r2_log_close_63d_d3(close: pd.Series) -> pd.Series:
    """R-squared of log-close ~ time linear regression over 63d."""
    lc = _safe_log(close)
    def _r2(w):
        valid = ~np.isnan(w)
        if valid.sum() < 15:
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum(); syy = ((y - ym) ** 2).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        sxy = ((x - xm) * (y - ym)).sum()
        return float(sxy * sxy / (sxx * syy))
    res = lc.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_107_trend_strength_signed_log_close_252d_d3(close: pd.Series) -> pd.Series:
    """R^2 * sign(slope) of log-close trend over 252d - signed trend strength."""
    lc = _safe_log(close)
    def _sr2(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum(); syy = ((y - ym) ** 2).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        sxy = ((x - xm) * (y - ym)).sum()
        r2 = sxy * sxy / (sxx * syy)
        return float(r2 * np.sign(sxy))
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_sr2, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_108_trend_strength_signed_log_close_63d_d3(close: pd.Series) -> pd.Series:
    """R^2 * sign(slope) of log-close trend over 63d."""
    lc = _safe_log(close)
    def _sr2(w):
        valid = ~np.isnan(w)
        if valid.sum() < 15:
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum(); syy = ((y - ym) ** 2).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        sxy = ((x - xm) * (y - ym)).sum()
        r2 = sxy * sxy / (sxx * syy)
        return float(r2 * np.sign(sxy))
    res = lc.rolling(QDAYS, min_periods=MDAYS).apply(_sr2, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_109_mass_index_log_ret_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass-Index-like proxy: sum of high-low EMA9 / EMA9 of EMA9 of high-low, over 252d."""
    diff = high - low
    ema9 = diff.ewm(span=9, adjust=False, min_periods=5).mean()
    ema9_ema9 = ema9.ewm(span=9, adjust=False, min_periods=5).mean()
    ratio = _safe_div(ema9, ema9_ema9)
    return (ratio.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f42_acpe_110_acceleration_persistence_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """AR(1) of diff(log_ret) over 252d - persistence of return-acceleration."""
    r = _log_ret(close)
    ac = r.diff()
    return (_rolling_ar1(ac, YDAYS)).diff().diff().diff()

def f42_acpe_111_corr_1d_to_5d_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d correlation between 1d and 5d log-returns - aggregation persistence."""
    r = _log_ret(close)
    rf = r.rolling(5).sum()
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(rf)).diff().diff().diff()

def f42_acpe_112_corr_1d_to_21d_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """252d correlation between 1d and 21d aggregated log-returns."""
    r = _log_ret(close)
    rf = r.rolling(21).sum()
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(rf)).diff().diff().diff()

def f42_acpe_113_corr_1d_to_63d_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """252d correlation between 1d and 63d aggregated log-returns."""
    r = _log_ret(close)
    rf = r.rolling(63).sum()
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(rf)).diff().diff().diff()

def f42_acpe_114_corr_1d_to_5d_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """252d correlation between 1d and 5d aggregated |r| - vol-aggregation persistence."""
    x = _log_ret(close).abs()
    xf = x.rolling(5).sum()
    return (x.rolling(YDAYS, min_periods=QDAYS).corr(xf)).diff().diff().diff()

def f42_acpe_115_corr_1d_to_21d_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """252d correlation between 1d and 21d aggregated |r|."""
    x = _log_ret(close).abs()
    xf = x.rolling(21).sum()
    return (x.rolling(YDAYS, min_periods=QDAYS).corr(xf)).diff().diff().diff()

def f42_acpe_116_cross_lag_persistence_index_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of |ACF(r,k)| for k in {1,5,21} over 252d - cross-lag persistence intensity."""
    r = _log_ret(close)
    acf1 = _rolling_acf_lag(r, YDAYS, 1).abs()
    acf5 = _rolling_acf_lag(r, YDAYS, 5).abs()
    acf21 = _rolling_acf_lag(r, YDAYS, 21).abs()
    return (acf1 + acf5 + acf21).diff().diff().diff()

def f42_acpe_117_block_variance_ratio_block5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Var of 5-bar blocks / 5 * Var(1-bar) over 252d - simplified Lo-MacKinlay."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 5)).diff().diff().diff()

def f42_acpe_118_block_variance_ratio_block10_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Same with block=10."""
    r = _log_ret(close)
    return (_variance_ratio(r, YDAYS, 10)).diff().diff().diff()

def f42_acpe_119_block_variance_ratio_block21_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    """Same with block=21 over 504d."""
    r = _log_ret(close)
    return (_variance_ratio(r, DDAYS_2Y, 21)).diff().diff().diff()

def f42_acpe_120_block_skew_var_block5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Var of 5-bar block sums vs first/last halves over 252d."""
    r = _log_ret(close)
    def _bv(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        if v.size % 5 != 0:
            v = v[: (v.size // 5) * 5]
        if v.size < 30:
            return np.nan
        agg = v.reshape(-1, 5).sum(axis=1)
        return float(np.var(agg, ddof=1))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bv, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_121_moving_block_acf_lag1_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Mean of moving-block (size=21) ACF(1) estimates over 252d."""
    r = _log_ret(close)
    def _mb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        acs = []
        for i in range(0, v.size - 21, 10):
            seg = v[i:i + 21]
            if seg.std() == 0 or seg.size < 21:
                continue
            a = seg[:-1]; b = seg[1:]
            if a.std() == 0 or b.std() == 0:
                continue
            acs.append(float(np.corrcoef(a, b)[0, 1]))
        return float(np.mean(acs)) if acs else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_mb, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_122_circular_block_acf_lag1_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Circular-block ACF(1) over 252d using simple wrap-around."""
    r = _log_ret(close)
    def _cb(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        a = v; b = np.roll(v, -1)
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_cb, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_123_mutual_info_lag1_binned_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Mutual information at lag 1 of binned (10-bin) log-returns over 252d."""
    r = _log_ret(close)
    def _mi(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        a = v[:-1]; b = v[1:]
        bins = 10
        H, _, _ = np.histogram2d(a, b, bins=bins)
        P = H / H.sum()
        Pa = P.sum(axis=1); Pb = P.sum(axis=0)
        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if P[i, j] > 0 and Pa[i] > 0 and Pb[j] > 0:
                    mi += P[i, j] * np.log(P[i, j] / (Pa[i] * Pb[j]))
        return float(mi)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_mi, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_124_mutual_info_lag5_binned_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Mutual information at lag 5 of binned log-returns over 252d."""
    r = _log_ret(close)
    def _mi(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        a = v[:-5]; b = v[5:]
        bins = 10
        H, _, _ = np.histogram2d(a, b, bins=bins)
        P = H / H.sum()
        Pa = P.sum(axis=1); Pb = P.sum(axis=0)
        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if P[i, j] > 0 and Pa[i] > 0 and Pb[j] > 0:
                    mi += P[i, j] * np.log(P[i, j] / (Pa[i] * Pb[j]))
        return float(mi)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_mi, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_125_transfer_entropy_proxy_252d_d3(close: pd.Series) -> pd.Series:
    """Crude transfer-entropy proxy: MI(r_t, r_{t-1}, r_{t-2}) over 252d."""
    r = _log_ret(close)
    def _te(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        a = v[2:]; b = v[1:-1]; c = v[:-2]
        bins = 5
        Habc, _ = np.histogramdd(np.array([a, b, c]).T, bins=bins)
        if Habc.sum() == 0:
            return np.nan
        P = Habc / Habc.sum()
        P_bc = P.sum(axis=0)
        P_ab = P.sum(axis=2)
        P_b = P.sum(axis=(0, 2))
        te = 0.0
        for i in range(bins):
            for j in range(bins):
                for k in range(bins):
                    if P[i, j, k] > 0 and P_bc[j, k] > 0 and P_b[j] > 0 and P_ab[i, j] > 0:
                        te += P[i, j, k] * np.log((P[i, j, k] * P_b[j]) / (P_ab[i, j] * P_bc[j, k]))
        return float(te)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_te, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_126_kl_divergence_to_normal_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """KL divergence of binned log-return distribution to fitted normal over 252d."""
    r = _log_ret(close)
    def _kl(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        p, _ = np.histogram(v, bins=edges, density=True)
        mids = 0.5 * (edges[:-1] + edges[1:])
        q = (1.0 / (sd * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((mids - mu) / sd) ** 2)
        mask = (p > 0) & (q > 0)
        return float(np.sum(p[mask] * np.log(p[mask] / q[mask])) * (edges[1] - edges[0]))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_kl, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_127_shannon_entropy_binned_log_ret_252d_acpe_d3(close: pd.Series) -> pd.Series:
    """Shannon entropy of binned log-returns (20 bins) over 252d."""
    r = _log_ret(close)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_128_tsallis_entropy_q2_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Tsallis entropy (q=2) of binned log-returns over 252d."""
    r = _log_ret(close)
    def _ts(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        return float((1.0 - (p ** 2).sum()))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)
    return (res).diff().diff().diff()

def f42_acpe_129_wavelet_variance_high_freq_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of (close - SMA5) over 252d - high-frequency component variance."""
    ma5 = close.rolling(5, min_periods=3).mean()
    hf = close - ma5
    return (hf.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f42_acpe_130_wavelet_variance_med_freq_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of (SMA5 - SMA21) over 252d - medium-frequency component variance."""
    ma5 = close.rolling(5, min_periods=3).mean()
    ma21 = close.rolling(21, min_periods=10).mean()
    mf = ma5 - ma21
    return (mf.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f42_acpe_131_wavelet_variance_low_freq_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of (SMA21 - SMA63) over 252d - low-frequency component variance."""
    ma21 = close.rolling(21, min_periods=10).mean()
    ma63 = close.rolling(63, min_periods=21).mean()
    lf = ma21 - ma63
    return (lf.rolling(YDAYS, min_periods=QDAYS).var()).diff().diff().diff()

def f42_acpe_132_wavelet_high_to_low_freq_var_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Ratio of high-freq to low-freq variance proxies over 252d."""
    ma5 = close.rolling(5, min_periods=3).mean()
    ma21 = close.rolling(21, min_periods=10).mean()
    ma63 = close.rolling(63, min_periods=21).mean()
    hf = (close - ma5).rolling(YDAYS, min_periods=QDAYS).var()
    lf = (ma21 - ma63).rolling(YDAYS, min_periods=QDAYS).var()
    return (_safe_div(hf, lf)).diff().diff().diff()

def f42_acpe_133_wavelet_energy_concentration_high_252d_d3(close: pd.Series) -> pd.Series:
    """Share of energy in high-freq component over 252d (HF / (HF+MF+LF))."""
    ma5 = close.rolling(5, min_periods=3).mean()
    ma21 = close.rolling(21, min_periods=10).mean()
    ma63 = close.rolling(63, min_periods=21).mean()
    hf = (close - ma5).rolling(YDAYS, min_periods=QDAYS).var()
    mf = (ma5 - ma21).rolling(YDAYS, min_periods=QDAYS).var()
    lf = (ma21 - ma63).rolling(YDAYS, min_periods=QDAYS).var()
    return (_safe_div(hf, hf + mf + lf)).diff().diff().diff()

def f42_acpe_134_wavelet_dominant_scale_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: 0 if HF largest, 1 if MF, 2 if LF (categorical-like) over 252d."""
    ma5 = close.rolling(5, min_periods=3).mean()
    ma21 = close.rolling(21, min_periods=10).mean()
    ma63 = close.rolling(63, min_periods=21).mean()
    hf = (close - ma5).rolling(YDAYS, min_periods=QDAYS).var()
    mf = (ma5 - ma21).rolling(YDAYS, min_periods=QDAYS).var()
    lf = (ma21 - ma63).rolling(YDAYS, min_periods=QDAYS).var()
    stacked = pd.concat([hf.rename('hf'), mf.rename('mf'), lf.rename('lf')], axis=1)
    name_to_idx = {'hf': 0.0, 'mf': 1.0, 'lf': 2.0}
    dom = stacked.fillna(-np.inf).idxmax(axis=1).map(name_to_idx).where(stacked.notna().any(axis=1), np.nan).astype(float)
    return (dom.where(stacked.notna().all(axis=1), np.nan)).diff().diff().diff()

def f42_acpe_135_close_to_close_acf_lag1_504d_d3(close: pd.Series) -> pd.Series:
    """ACF(1) of log-close levels over 504d."""
    lc = _safe_log(close)
    return (_rolling_acf_lag(lc, DDAYS_2Y, 1)).diff().diff().diff()

def f42_acpe_136_hl_ratio_acf_lag1_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """ACF(1) of high/low ratio over 252d - intraday-range persistence."""
    hl = _safe_div(high, low)
    return (_rolling_acf_lag(hl, YDAYS, 1)).diff().diff().diff()

def f42_acpe_137_range_acf_lag1_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ACF(1) of (high-low)/close over 252d."""
    rng = _safe_div(high - low, close)
    return (_rolling_acf_lag(rng, YDAYS, 1)).diff().diff().diff()

def f42_acpe_138_volume_acf_lag1_252d_d3(volume: pd.Series) -> pd.Series:
    """ACF(1) of log-volume over 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (_rolling_acf_lag(lv, YDAYS, 1)).diff().diff().diff()

def f42_acpe_139_dollar_volume_acf_lag1_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ACF(1) of log(close*volume) over 252d."""
    ldv = _safe_log((close * volume).replace(0, np.nan))
    return (_rolling_acf_lag(ldv, YDAYS, 1)).diff().diff().diff()

def f42_acpe_140_signed_dollar_flow_acf_lag1_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ACF(1) of sign(log_ret) * dollar_volume over 252d."""
    r = _log_ret(close)
    sg = np.sign(r)
    sdf = sg * (close * volume)
    return (_rolling_acf_lag(sdf, YDAYS, 1)).diff().diff().diff()

def f42_acpe_141_half_life_persistence_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Half-life implied by |AR(1)| of log-ret over 252d (-log2/log|phi|)."""
    r = _log_ret(close)
    phi = _rolling_ar1(r, YDAYS).abs().clip(upper=0.999).replace(0, np.nan)
    return (-np.log(2.0) / np.log(phi)).diff().diff().diff()

def f42_acpe_142_half_life_persistence_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Half-life implied by AR(1) of |r| over 252d - vol persistence half-life."""
    x = _log_ret(close).abs()
    phi = _rolling_ar1(x, YDAYS).abs().clip(upper=0.999).replace(0, np.nan)
    return (-np.log(2.0) / np.log(phi)).diff().diff().diff()

def f42_acpe_143_integrated_abs_acf_log_ret_lags1to10_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of |ACF(r, k)| for k=1..10 over 252d - total persistence intensity."""
    r = _log_ret(close)
    total = pd.Series(0.0, index=close.index)
    for k in range(1, 11):
        total = total.add(_rolling_acf_lag(r, YDAYS, k).abs(), fill_value=0.0)
    return (total).diff().diff().diff()

def f42_acpe_144_integrated_abs_acf_abs_log_ret_lags1to10_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of |ACF(|r|, k)| for k=1..10 over 252d - total vol persistence."""
    x = _log_ret(close).abs()
    total = pd.Series(0.0, index=close.index)
    for k in range(1, 11):
        total = total.add(_rolling_acf_lag(x, YDAYS, k).abs(), fill_value=0.0)
    return (total).diff().diff().diff()

def f42_acpe_145_persistence_decay_slope_log_log_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Slope of log|ACF(k)| vs log(k) for k=1..10 on log-returns over 252d - power-law decay."""
    r = _log_ret(close)
    acs = [_rolling_acf_lag(r, YDAYS, k).abs().replace(0, np.nan) for k in range(1, 11)]
    df_acs = pd.concat([s.rename(i) for i, s in enumerate(acs)], axis=1)
    log_k = np.log(np.arange(1, 11, dtype=float))
    log_k_m = log_k.mean(); log_k_var = ((log_k - log_k_m) ** 2).sum()
    def _sl(row):
        if np.isnan(row).any():
            return np.nan
        y = np.log(row)
        if not np.isfinite(y).all():
            return np.nan
        ym = y.mean()
        return float(((log_k - log_k_m) * (y - ym)).sum() / log_k_var)
    vals = df_acs.values
    out = np.array([_sl(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f42_acpe_146_persistence_decay_slope_log_log_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    """Same persistence-decay slope but for |r| over 252d."""
    x = _log_ret(close).abs()
    acs = [_rolling_acf_lag(x, YDAYS, k).abs().replace(0, np.nan) for k in range(1, 11)]
    df_acs = pd.concat([s.rename(i) for i, s in enumerate(acs)], axis=1)
    log_k = np.log(np.arange(1, 11, dtype=float))
    log_k_m = log_k.mean(); log_k_var = ((log_k - log_k_m) ** 2).sum()
    def _sl(row):
        if np.isnan(row).any():
            return np.nan
        y = np.log(row)
        if not np.isfinite(y).all():
            return np.nan
        ym = y.mean()
        return float(((log_k - log_k_m) * (y - ym)).sum() / log_k_var)
    vals = df_acs.values
    out = np.array([_sl(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f42_acpe_147_composite_persistence_zscore_ar1_hurst_vr_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of z-scored AR1, Hurst-0.5, (VR-1) over 252d - composite persistence indicator."""
    r = _log_ret(close)
    ar1 = _rolling_ar1(r, YDAYS)
    hu = _hurst_rs(r, YDAYS) - 0.5
    vr = _variance_ratio(r, YDAYS, 5) - 1.0
    z1 = _rolling_zscore(ar1, YDAYS)
    z2 = _rolling_zscore(hu, YDAYS)
    z3 = _rolling_zscore(vr, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff().diff()

def f42_acpe_148_anti_persistence_indicator_hurst_lt_half_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: Hurst < 0.5 over 252d - mean-reverting regime."""
    r = _log_ret(close)
    hu = _hurst_rs(r, YDAYS)
    return ((hu < 0.5).astype(float).where(hu.notna(), np.nan)).diff().diff().diff()

def f42_acpe_149_random_walk_indicator_hurst_near_half_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: |Hurst - 0.5| < 0.05 over 252d - random-walk-like regime."""
    r = _log_ret(close)
    hu = _hurst_rs(r, YDAYS)
    return (((hu - 0.5).abs() < 0.05).astype(float).where(hu.notna(), np.nan)).diff().diff().diff()

def f42_acpe_150_trending_indicator_hurst_gt_half_and_ar1_pos_252d_d3(close: pd.Series) -> pd.Series:
    """Indicator: Hurst > 0.5 AND AR(1) > 0 over 252d - persistent-trend regime."""
    r = _log_ret(close)
    hu = _hurst_rs(r, YDAYS)
    ar = _rolling_ar1(r, YDAYS)
    return (((hu > 0.5) & (ar > 0)).astype(float).where(hu.notna() & ar.notna(), np.nan)).diff().diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d3)
# ============================================================

AUTOCORRELATION_PERSISTENCE_D3_REGISTRY_076_150 = {
    "f42_acpe_076_higuchi_fd_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_076_higuchi_fd_log_ret_504d_d3},
    "f42_acpe_077_higuchi_fd_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_077_higuchi_fd_abs_log_ret_252d_d3},
    "f42_acpe_078_katz_fd_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_078_katz_fd_log_close_252d_d3},
    "f42_acpe_079_petrosian_fd_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_079_petrosian_fd_log_ret_252d_d3},
    "f42_acpe_080_petrosian_fd_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_080_petrosian_fd_log_close_252d_d3},
    "f42_acpe_081_permutation_entropy_d3_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_081_permutation_entropy_d3_log_ret_252d_d3},
    "f42_acpe_082_permutation_entropy_d4_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_082_permutation_entropy_d4_log_ret_252d_d3},
    "f42_acpe_083_permutation_entropy_d5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_083_permutation_entropy_d5_log_ret_252d_d3},
    "f42_acpe_084_permutation_entropy_d3_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_084_permutation_entropy_d3_log_close_252d_d3},
    "f42_acpe_085_permutation_entropy_d4_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_085_permutation_entropy_d4_abs_log_ret_252d_d3},
    "f42_acpe_086_complexity_pe_times_oneminuspe_d3_252d_d3": {"inputs": ["close"], "func": f42_acpe_086_complexity_pe_times_oneminuspe_d3_252d_d3},
    "f42_acpe_087_sample_entropy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_087_sample_entropy_log_ret_252d_d3},
    "f42_acpe_088_sample_entropy_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_088_sample_entropy_abs_log_ret_252d_d3},
    "f42_acpe_089_sample_entropy_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_089_sample_entropy_log_close_252d_d3},
    "f42_acpe_090_multiscale_sample_entropy_scale2_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_090_multiscale_sample_entropy_scale2_log_ret_252d_d3},
    "f42_acpe_091_multiscale_sample_entropy_scale5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_091_multiscale_sample_entropy_scale5_log_ret_252d_d3},
    "f42_acpe_092_sample_entropy_squared_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_092_sample_entropy_squared_log_ret_252d_d3},
    "f42_acpe_093_approx_lyapunov_proxy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_093_approx_lyapunov_proxy_log_ret_252d_d3},
    "f42_acpe_094_correlation_dim_proxy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_094_correlation_dim_proxy_log_ret_252d_d3},
    "f42_acpe_095_nonlinearity_test_stat_bds_proxy_252d_d3": {"inputs": ["close"], "func": f42_acpe_095_nonlinearity_test_stat_bds_proxy_252d_d3},
    "f42_acpe_096_turning_points_per_252d_log_ret_d3": {"inputs": ["close"], "func": f42_acpe_096_turning_points_per_252d_log_ret_d3},
    "f42_acpe_097_recurrence_rate_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_097_recurrence_rate_log_ret_252d_d3},
    "f42_acpe_098_determinism_rate_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_098_determinism_rate_log_ret_252d_d3},
    "f42_acpe_099_gph_d_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_099_gph_d_log_ret_252d_d3},
    "f42_acpe_100_gph_d_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_100_gph_d_log_ret_504d_d3},
    "f42_acpe_101_gph_d_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_101_gph_d_abs_log_ret_252d_d3},
    "f42_acpe_102_gph_d_abs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_102_gph_d_abs_log_ret_504d_d3},
    "f42_acpe_103_local_whittle_d_proxy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_103_local_whittle_d_proxy_log_ret_252d_d3},
    "f42_acpe_104_local_whittle_d_proxy_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_104_local_whittle_d_proxy_abs_log_ret_252d_d3},
    "f42_acpe_105_trend_strength_logreg_r2_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_105_trend_strength_logreg_r2_log_close_252d_d3},
    "f42_acpe_106_trend_strength_logreg_r2_log_close_63d_d3": {"inputs": ["close"], "func": f42_acpe_106_trend_strength_logreg_r2_log_close_63d_d3},
    "f42_acpe_107_trend_strength_signed_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_107_trend_strength_signed_log_close_252d_d3},
    "f42_acpe_108_trend_strength_signed_log_close_63d_d3": {"inputs": ["close"], "func": f42_acpe_108_trend_strength_signed_log_close_63d_d3},
    "f42_acpe_109_mass_index_log_ret_252d_d3": {"inputs": ["high", "low"], "func": f42_acpe_109_mass_index_log_ret_252d_d3},
    "f42_acpe_110_acceleration_persistence_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_110_acceleration_persistence_log_ret_252d_d3},
    "f42_acpe_111_corr_1d_to_5d_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_111_corr_1d_to_5d_log_ret_252d_d3},
    "f42_acpe_112_corr_1d_to_21d_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_112_corr_1d_to_21d_log_ret_252d_d3},
    "f42_acpe_113_corr_1d_to_63d_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_113_corr_1d_to_63d_log_ret_252d_d3},
    "f42_acpe_114_corr_1d_to_5d_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_114_corr_1d_to_5d_abs_log_ret_252d_d3},
    "f42_acpe_115_corr_1d_to_21d_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_115_corr_1d_to_21d_abs_log_ret_252d_d3},
    "f42_acpe_116_cross_lag_persistence_index_252d_d3": {"inputs": ["close"], "func": f42_acpe_116_cross_lag_persistence_index_252d_d3},
    "f42_acpe_117_block_variance_ratio_block5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_117_block_variance_ratio_block5_log_ret_252d_d3},
    "f42_acpe_118_block_variance_ratio_block10_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_118_block_variance_ratio_block10_log_ret_252d_d3},
    "f42_acpe_119_block_variance_ratio_block21_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_119_block_variance_ratio_block21_log_ret_504d_d3},
    "f42_acpe_120_block_skew_var_block5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_120_block_skew_var_block5_log_ret_252d_d3},
    "f42_acpe_121_moving_block_acf_lag1_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_121_moving_block_acf_lag1_log_ret_252d_d3},
    "f42_acpe_122_circular_block_acf_lag1_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_122_circular_block_acf_lag1_log_ret_252d_d3},
    "f42_acpe_123_mutual_info_lag1_binned_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_123_mutual_info_lag1_binned_log_ret_252d_d3},
    "f42_acpe_124_mutual_info_lag5_binned_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_124_mutual_info_lag5_binned_log_ret_252d_d3},
    "f42_acpe_125_transfer_entropy_proxy_252d_d3": {"inputs": ["close"], "func": f42_acpe_125_transfer_entropy_proxy_252d_d3},
    "f42_acpe_126_kl_divergence_to_normal_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_126_kl_divergence_to_normal_log_ret_252d_d3},
    "f42_acpe_127_shannon_entropy_binned_log_ret_252d_acpe_d3": {"inputs": ["close"], "func": f42_acpe_127_shannon_entropy_binned_log_ret_252d_acpe_d3},
    "f42_acpe_128_tsallis_entropy_q2_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_128_tsallis_entropy_q2_log_ret_252d_d3},
    "f42_acpe_129_wavelet_variance_high_freq_252d_d3": {"inputs": ["close"], "func": f42_acpe_129_wavelet_variance_high_freq_252d_d3},
    "f42_acpe_130_wavelet_variance_med_freq_252d_d3": {"inputs": ["close"], "func": f42_acpe_130_wavelet_variance_med_freq_252d_d3},
    "f42_acpe_131_wavelet_variance_low_freq_252d_d3": {"inputs": ["close"], "func": f42_acpe_131_wavelet_variance_low_freq_252d_d3},
    "f42_acpe_132_wavelet_high_to_low_freq_var_ratio_252d_d3": {"inputs": ["close"], "func": f42_acpe_132_wavelet_high_to_low_freq_var_ratio_252d_d3},
    "f42_acpe_133_wavelet_energy_concentration_high_252d_d3": {"inputs": ["close"], "func": f42_acpe_133_wavelet_energy_concentration_high_252d_d3},
    "f42_acpe_134_wavelet_dominant_scale_indicator_252d_d3": {"inputs": ["close"], "func": f42_acpe_134_wavelet_dominant_scale_indicator_252d_d3},
    "f42_acpe_135_close_to_close_acf_lag1_504d_d3": {"inputs": ["close"], "func": f42_acpe_135_close_to_close_acf_lag1_504d_d3},
    "f42_acpe_136_hl_ratio_acf_lag1_252d_d3": {"inputs": ["high", "low"], "func": f42_acpe_136_hl_ratio_acf_lag1_252d_d3},
    "f42_acpe_137_range_acf_lag1_252d_d3": {"inputs": ["high", "low", "close"], "func": f42_acpe_137_range_acf_lag1_252d_d3},
    "f42_acpe_138_volume_acf_lag1_252d_d3": {"inputs": ["volume"], "func": f42_acpe_138_volume_acf_lag1_252d_d3},
    "f42_acpe_139_dollar_volume_acf_lag1_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_139_dollar_volume_acf_lag1_252d_d3},
    "f42_acpe_140_signed_dollar_flow_acf_lag1_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_140_signed_dollar_flow_acf_lag1_252d_d3},
    "f42_acpe_141_half_life_persistence_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_141_half_life_persistence_log_ret_252d_d3},
    "f42_acpe_142_half_life_persistence_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_142_half_life_persistence_abs_log_ret_252d_d3},
    "f42_acpe_143_integrated_abs_acf_log_ret_lags1to10_252d_d3": {"inputs": ["close"], "func": f42_acpe_143_integrated_abs_acf_log_ret_lags1to10_252d_d3},
    "f42_acpe_144_integrated_abs_acf_abs_log_ret_lags1to10_252d_d3": {"inputs": ["close"], "func": f42_acpe_144_integrated_abs_acf_abs_log_ret_lags1to10_252d_d3},
    "f42_acpe_145_persistence_decay_slope_log_log_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_145_persistence_decay_slope_log_log_log_ret_252d_d3},
    "f42_acpe_146_persistence_decay_slope_log_log_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_146_persistence_decay_slope_log_log_abs_log_ret_252d_d3},
    "f42_acpe_147_composite_persistence_zscore_ar1_hurst_vr_252d_d3": {"inputs": ["close"], "func": f42_acpe_147_composite_persistence_zscore_ar1_hurst_vr_252d_d3},
    "f42_acpe_148_anti_persistence_indicator_hurst_lt_half_252d_d3": {"inputs": ["close"], "func": f42_acpe_148_anti_persistence_indicator_hurst_lt_half_252d_d3},
    "f42_acpe_149_random_walk_indicator_hurst_near_half_252d_d3": {"inputs": ["close"], "func": f42_acpe_149_random_walk_indicator_hurst_near_half_252d_d3},
    "f42_acpe_150_trending_indicator_hurst_gt_half_and_ar1_pos_252d_d3": {"inputs": ["close"], "func": f42_acpe_150_trending_indicator_hurst_gt_half_and_ar1_pos_252d_d3},
}
