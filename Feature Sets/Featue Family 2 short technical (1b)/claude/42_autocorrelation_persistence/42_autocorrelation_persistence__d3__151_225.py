"""autocorrelation_persistence d3 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Lo modified R/S / KPSS / Whittle d / multifractal DFA / Hurst-of-Hurst /
RQA laminarity-trapping-diagonal / ApEn / ordinal-pattern Markov entropy /
0-1 chaos / time-reversal asymmetry / Bartels rank / DCCA / cross-ACF /
Sevcik FD / composite regime classifiers.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _lo_modified_rs(w, q=None):
    """Lo's modified R/S statistic — HAC-adjusted denominator.
    q = lag truncation; default sqrt(n)."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if q is None:
        q = int(np.floor(np.sqrt(n)))
    m = v.mean()
    y = np.cumsum(v - m)
    R = float(y.max() - y.min())
    s2 = float(np.var(v, ddof=0))
    if s2 == 0:
        return np.nan
    for k in range(1, q + 1):
        w_k = 1.0 - k / (q + 1.0)
        cov_k = float(np.sum((v[k:] - m) * (v[:-k] - m)) / n)
        s2 += 2.0 * w_k * cov_k
    if s2 <= 0:
        return np.nan
    return float(R / (np.sqrt(s2) * np.sqrt(n)))


def _kpss_level(w):
    """KPSS test for level stationarity — uses Bartlett-windowed long-run variance.
    Returns the test statistic eta_mu."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    y = v - v.mean()
    s = np.cumsum(y)
    s2 = float(np.var(v, ddof=0))
    q = int(np.floor(12.0 * (n / 100.0) ** 0.25))
    for k in range(1, max(1, q) + 1):
        w_k = 1.0 - k / (q + 1.0)
        cov_k = float(np.sum(y[k:] * y[:-k]) / n)
        s2 += 2.0 * w_k * cov_k
    if s2 <= 0:
        return np.nan
    return float(np.sum(s ** 2) / (n ** 2 * s2))


def _adf_stat_proxy(w):
    """ADF unit-root test statistic proxy: regress dy on lag-1 y; report t-stat of coefficient."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    y = v[:-1]
    dy = np.diff(v)
    n = y.size
    if n < 5:
        return np.nan
    ym = y.mean()
    y0 = y - ym
    den = float((y0 ** 2).sum())
    if den == 0:
        return np.nan
    beta = float((y0 * (dy - dy.mean())).sum() / den)
    yhat = beta * y0
    resid = (dy - dy.mean()) - yhat
    sigma2 = float((resid ** 2).sum()) / max(n - 1, 1)
    if sigma2 <= 0:
        return np.nan
    se_beta = np.sqrt(sigma2 / den)
    return float(beta / se_beta) if se_beta > 0 else np.nan


def _gph_d(w, alpha_exp=0.5):
    """Geweke-Porter-Hudak long-memory d estimator. m = n^alpha_exp."""
    valid = ~np.isnan(w)
    if valid.sum() < 60:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    v = v - v.mean()
    n = v.size
    m = int(np.floor(n ** alpha_exp))
    if m < 5:
        return np.nan
    freqs = 2.0 * np.pi * np.arange(1, m + 1) / float(n)
    fft = np.fft.fft(v)
    psd = (np.abs(fft) ** 2) / (2.0 * np.pi * n)
    psd_m = psd[1:m + 1]
    if (psd_m <= 0).any():
        return np.nan
    x = np.log(2.0 * np.sin(freqs / 2.0))
    y = np.log(psd_m)
    xm = x.mean(); ym = y.mean()
    den = float(((x - xm) ** 2).sum())
    if den == 0:
        return np.nan
    return float(-((x - xm) * (y - ym)).sum() / den)


def _whittle_d_proxy(w):
    """Whittle long-memory d estimator (local-Whittle, simplified)."""
    valid = ~np.isnan(w)
    if valid.sum() < 60:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    v = v - v.mean()
    n = v.size
    m = int(np.floor(n ** 0.6))
    if m < 5:
        return np.nan
    freqs = 2.0 * np.pi * np.arange(1, m + 1) / float(n)
    fft = np.fft.fft(v)
    psd = (np.abs(fft) ** 2) / (2.0 * np.pi * n)
    psd_m = psd[1:m + 1]
    if (psd_m <= 0).any():
        return np.nan
    # local-Whittle: d = 0.5 - 0.5 * slope(log psd vs log freq)
    x = np.log(freqs)
    y = np.log(psd_m)
    xm = x.mean(); ym = y.mean()
    den = float(((x - xm) ** 2).sum())
    if den == 0:
        return np.nan
    slope = float(((x - xm) * (y - ym)).sum() / den)
    return float(-slope / 2.0)


def _multifractal_dfa_q(w, q=2.0):
    """Simplified multifractal DFA exponent at order q.
    Returns h(q) — slope of log F_q(s) vs log s across scales."""
    valid = ~np.isnan(w)
    if valid.sum() < 60:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    v = v - v.mean()
    y = np.cumsum(v)
    n = y.size
    scales = [s for s in (4, 8, 16, 32, 64) if 2 * s < n]
    if len(scales) < 3:
        return np.nan
    fq = []
    for s in scales:
        ns = n // s
        f2 = []
        for i in range(ns):
            seg = y[i * s:(i + 1) * s]
            x = np.arange(s)
            p = np.polyfit(x, seg, 1)
            resid = seg - np.polyval(p, x)
            f2.append(float((resid ** 2).mean()))
        if not f2:
            continue
        f2_arr = np.array(f2)
        if q == 0:
            fq.append(np.exp(0.5 * np.mean(np.log(f2_arr + 1e-12))))
        else:
            fq.append((np.mean(f2_arr ** (q / 2.0))) ** (1.0 / q))
    if len(fq) < 3:
        return np.nan
    log_s = np.log(scales[:len(fq)])
    log_fq = np.log(np.array(fq) + 1e-12)
    xm = log_s.mean(); ym = log_fq.mean()
    den = float(((log_s - xm) ** 2).sum())
    if den == 0:
        return np.nan
    return float(((log_s - xm) * (log_fq - ym)).sum() / den)


def _0_1_chaos_test(w, c=None):
    """Gottwald-Melbourne 0-1 test for chaos. Returns K in [0,1]; 1 = chaotic, 0 = regular."""
    valid = ~np.isnan(w)
    if valid.sum() < 60:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if c is None:
        c = np.pi / 5.0
    t = np.arange(1, n + 1, dtype=float)
    p = np.cumsum(v * np.cos(c * t))
    q = np.cumsum(v * np.sin(c * t))
    # mean-square displacement
    n_cut = min(n // 10, 100)
    if n_cut < 5:
        return np.nan
    M = np.empty(n_cut)
    for nn in range(1, n_cut + 1):
        diff_p = p[nn:] - p[:-nn]
        diff_q = q[nn:] - q[:-nn]
        M[nn - 1] = np.mean(diff_p ** 2 + diff_q ** 2)
    # K = correlation of log M with log n
    log_n = np.log(np.arange(1, n_cut + 1))
    log_M = np.log(M + 1e-12)
    xm = log_n.mean(); ym = log_M.mean()
    num = float(((log_n - xm) * (log_M - ym)).sum())
    d1 = float(((log_n - xm) ** 2).sum()); d2 = float(((log_M - ym) ** 2).sum())
    if d1 == 0 or d2 == 0:
        return np.nan
    return float(num / np.sqrt(d1 * d2))


def _ordinal_pattern_transition_entropy(w, d=3):
    """Entropy of the transition matrix between consecutive ordinal patterns of dim d."""
    valid = ~np.isnan(w)
    if valid.sum() < d * 4:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if n - d < 5:
        return np.nan
    pats = []
    for i in range(n - d + 1):
        seg = v[i:i + d]
        order = tuple(np.argsort(seg))
        pats.append(order)
    # Build transition matrix
    cat = dict((p, i) for i, p in enumerate(set(pats)))
    seqs = np.array([cat[p] for p in pats])
    M = np.zeros((len(cat), len(cat)))
    for t in range(len(seqs) - 1):
        M[seqs[t], seqs[t + 1]] += 1
    row_sums = M.sum(axis=1, keepdims=True)
    P = M / np.where(row_sums == 0, 1, row_sums)
    # Joint stationary distribution: row of M / total
    pi = M.sum(axis=1) / max(M.sum(), 1)
    ent = 0.0
    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            if P[i, j] > 0:
                ent -= pi[i] * P[i, j] * np.log(P[i, j])
    return float(ent)


def _bartels_rank_test(w):
    """Bartels rank von-Neumann test for randomness."""
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    r = np.argsort(np.argsort(v)) + 1
    rm = r.mean()
    num = float(np.sum(np.diff(r) ** 2))
    den = float(np.sum((r - rm) ** 2))
    if den == 0:
        return np.nan
    return float(num / den)


def _sevcik_fd(w):
    """Sevcik's fractal dimension."""
    valid = ~np.isnan(w)
    if valid.sum() < 10:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    rng = v.max() - v.min()
    if rng == 0:
        return 1.0
    y_norm = (v - v.min()) / rng
    x_norm = np.arange(n, dtype=float) / (n - 1)
    L = float(np.sum(np.sqrt(np.diff(y_norm) ** 2 + np.diff(x_norm) ** 2)))
    if L <= 0:
        return np.nan
    return float(1.0 + np.log(L) / np.log(2 * (n - 1)))


def _dcca_corr(x, y, w_size=21):
    """Detrended cross-correlation analysis (DCCA) coefficient at scale w_size.
    Implemented as a single-window callable expecting equal-length arrays."""
    if len(x) != len(y) or len(x) < 30:
        return np.nan
    mask = ~np.isnan(x) & ~np.isnan(y)
    if mask.sum() < 30:
        return np.nan
    x = x[mask]; y = y[mask]
    n = len(x)
    yx = np.cumsum(x - x.mean())
    yy = np.cumsum(y - y.mean())
    ns = n // w_size
    if ns < 3:
        return np.nan
    f_xy = 0.0; f_xx = 0.0; f_yy = 0.0
    for i in range(ns):
        seg_x = yx[i * w_size:(i + 1) * w_size]
        seg_y = yy[i * w_size:(i + 1) * w_size]
        t = np.arange(w_size)
        px = np.polyfit(t, seg_x, 1); py = np.polyfit(t, seg_y, 1)
        rx = seg_x - np.polyval(px, t); ry = seg_y - np.polyval(py, t)
        f_xy += float(np.sum(rx * ry))
        f_xx += float(np.sum(rx ** 2))
        f_yy += float(np.sum(ry ** 2))
    if f_xx <= 0 or f_yy <= 0:
        return np.nan
    return float(f_xy / np.sqrt(f_xx * f_yy))


def _apen(w, m=2, r_frac=0.2):
    """Approximate Entropy (Pincus)."""
    valid = ~np.isnan(w)
    if valid.sum() < 30:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if n < m + 2:
        return np.nan
    r = r_frac * float(np.std(v, ddof=0))
    if r <= 0:
        return np.nan
    def _phi(mm):
        x = np.array([v[i:i + mm] for i in range(n - mm + 1)])
        C = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
            d = np.max(np.abs(x - x[i]), axis=1)
            C[i] = np.sum(d <= r) / float(x.shape[0])
        C = np.where(C > 0, C, 1e-12)
        return float(np.mean(np.log(C)))
    return float(_phi(m) - _phi(m + 1))


def f42_acpe_151_lo_modified_rs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_lo_modified_rs, raw=True)
    return out.diff().diff().diff()


def f42_acpe_152_lo_modified_rs_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(504, min_periods=168).apply(_lo_modified_rs, raw=True)
    return out.diff().diff().diff()


def f42_acpe_153_lo_modified_rs_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    out = r.rolling(252, min_periods=84).apply(_lo_modified_rs, raw=True)
    return out.diff().diff().diff()


def f42_acpe_154_gph_d_alpha_07_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _gph_d(w, alpha_exp=0.7), raw=True)
    return out.diff().diff().diff()


def f42_acpe_155_gph_d_alpha_05_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _gph_d(w, alpha_exp=0.5), raw=True)
    return out.diff().diff().diff()


def f42_acpe_156_whittle_d_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_whittle_d_proxy, raw=True)
    return out.diff().diff().diff()


def f42_acpe_157_whittle_d_abs_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    out = r.rolling(252, min_periods=84).apply(_whittle_d_proxy, raw=True)
    return out.diff().diff().diff()


def f42_acpe_158_kpss_level_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_kpss_level, raw=True)
    return out.diff().diff().diff()


def f42_acpe_159_kpss_level_log_close_252d_d3(close: pd.Series) -> pd.Series:
    out = _safe_log(close).rolling(252, min_periods=84).apply(_kpss_level, raw=True)
    return out.diff().diff().diff()


def f42_acpe_160_adf_tstat_log_close_252d_d3(close: pd.Series) -> pd.Series:
    out = _safe_log(close).rolling(252, min_periods=84).apply(_adf_stat_proxy, raw=True)
    return out.diff().diff().diff()


def f42_acpe_161_mfdfa_h_q1_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=1.0), raw=True)
    return out.diff().diff().diff()


def f42_acpe_162_mfdfa_h_q2_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=2.0), raw=True)
    return out.diff().diff().diff()


def f42_acpe_163_mfdfa_h_q4_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=4.0), raw=True)
    return out.diff().diff().diff()


def f42_acpe_164_mfdfa_spectrum_width_q1_to_q4_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    h1 = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=1.0), raw=True)
    h4 = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=4.0), raw=True)
    out = h1 - h4
    return out.diff().diff().diff()


def f42_acpe_165_hurst_of_hurst_63d_over_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    hurst63 = r.rolling(63, min_periods=21).apply(_rs, raw=True)
    out = hurst63.rolling(252, min_periods=84).std()
    return out.diff().diff().diff()


def f42_acpe_166_rqa_laminarity_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _lam(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        vert_lens = []
        for j in range(n):
            col = R[:, j]
            cur = 0
            for k in range(n):
                if col[k] > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        vert_lens.append(cur)
                    cur = 0
            if cur >= 2:
                vert_lens.append(cur)
        if not vert_lens:
            return 0.0
        total_recur = float(R.sum())
        if total_recur == 0:
            return 0.0
        return float(sum(vert_lens) / total_recur)
    out = r.rolling(252, min_periods=84).apply(_lam, raw=True)
    return out.diff().diff().diff()


def f42_acpe_167_rqa_trapping_time_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _tt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        vert_lens = []
        for j in range(n):
            col = R[:, j]
            cur = 0
            for k in range(n):
                if col[k] > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        vert_lens.append(cur)
                    cur = 0
            if cur >= 2:
                vert_lens.append(cur)
        if not vert_lens:
            return np.nan
        return float(np.mean(vert_lens))
    out = r.rolling(252, min_periods=84).apply(_tt, raw=True)
    return out.diff().diff().diff()


def f42_acpe_168_rqa_avg_diag_length_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ad(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        diag_lens = []
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        diag_lens.append(cur)
                    cur = 0
            if cur >= 2:
                diag_lens.append(cur)
        if not diag_lens:
            return np.nan
        return float(np.mean(diag_lens))
    out = r.rolling(252, min_periods=84).apply(_ad, raw=True)
    return out.diff().diff().diff()


def f42_acpe_169_rqa_max_diag_length_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _md(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        best = 0
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                    if cur > best:
                        best = cur
                else:
                    cur = 0
        return float(best)
    out = r.rolling(252, min_periods=84).apply(_md, raw=True)
    return out.diff().diff().diff()


def f42_acpe_170_rqa_divergence_inv_max_diag_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _md(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        best = 0
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                    if cur > best:
                        best = cur
                else:
                    cur = 0
        return float(1.0 / max(best, 1))
    out = r.rolling(252, min_periods=84).apply(_md, raw=True)
    return out.diff().diff().diff()


def f42_acpe_171_rqa_entropy_diag_lengths_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _de(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        diag_lens = []
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        diag_lens.append(cur)
                    cur = 0
            if cur >= 2:
                diag_lens.append(cur)
        if len(diag_lens) < 2:
            return np.nan
        arr = np.array(diag_lens)
        counts = np.bincount(arr)
        p = counts / counts.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = r.rolling(252, min_periods=84).apply(_de, raw=True)
    return out.diff().diff().diff()


def f42_acpe_172_apen_m2_r02_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _apen(w, m=2, r_frac=0.2), raw=True)
    return out.diff().diff().diff()


def f42_acpe_173_apen_m3_r02_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _apen(w, m=3, r_frac=0.2), raw=True)
    return out.diff().diff().diff()


def f42_acpe_174_cond_entropy_log_ret_given_lag1_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ce(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        sd = np.std(v, ddof=0)
        if sd <= 0:
            return np.nan
        edges = np.linspace(np.min(v) - 1e-9, np.max(v) + 1e-9, 7)
        bins = np.digitize(v, edges) - 1
        pairs = list(zip(bins[:-1], bins[1:]))
        from collections import Counter
        cP = Counter(pairs)
        cX = Counter(bins[:-1])
        ent = 0.0
        total = sum(cP.values())
        for (a, b), c in cP.items():
            pxy = c / total
            px = cX[a] / (n - 1)
            if pxy > 0 and px > 0:
                ent -= pxy * np.log(pxy / px)
        return float(ent)
    out = r.rolling(252, min_periods=84).apply(_ce, raw=True)
    return out.diff().diff().diff()


def f42_acpe_175_block_2bar_joint_entropy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _be(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        edges = np.linspace(np.min(v) - 1e-9, np.max(v) + 1e-9, 5)
        bins = np.digitize(v, edges) - 1
        pairs = list(zip(bins[:-1], bins[1:]))
        from collections import Counter
        cP = Counter(pairs)
        total = sum(cP.values())
        if total == 0:
            return np.nan
        return float(-sum((c / total) * np.log(c / total) for c in cP.values()))
    out = r.rolling(252, min_periods=84).apply(_be, raw=True)
    return out.diff().diff().diff()


def f42_acpe_176_recurrence_period_density_entropy_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rpde(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        periods = []
        for i in range(n):
            for j in range(i + 1, n):
                if R[i, j] > 0.5:
                    periods.append(j - i)
        if not periods:
            return np.nan
        arr = np.array(periods)
        counts = np.bincount(arr)
        p = counts / counts.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = r.rolling(252, min_periods=84).apply(_rpde, raw=True)
    return out.diff().diff().diff()


def f42_acpe_177_trapping_time_zscore_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _tt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        vert_lens = []
        for j in range(n):
            col = R[:, j]
            cur = 0
            for k in range(n):
                if col[k] > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        vert_lens.append(cur)
                    cur = 0
            if cur >= 2:
                vert_lens.append(cur)
        if not vert_lens:
            return np.nan
        return float(np.mean(vert_lens))
    tt = r.rolling(252, min_periods=84).apply(_tt, raw=True)
    out = _rolling_zscore(tt, 504, min_periods=168)
    return out.diff().diff().diff()


def f42_acpe_178_rqa_det_strength_max_diag_over_avg_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ratio(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        diag_lens = []
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        diag_lens.append(cur)
                    cur = 0
            if cur >= 2:
                diag_lens.append(cur)
        if len(diag_lens) < 2:
            return np.nan
        return float(max(diag_lens) / np.mean(diag_lens))
    out = r.rolling(252, min_periods=84).apply(_ratio, raw=True)
    return out.diff().diff().diff()


def f42_acpe_179_max_diag_minus_avg_diag_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _diff(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n > 80:
            step = max(1, n // 80)
            v = v[::step]; n = v.size
        if n < 10:
            return np.nan
        th = 0.2 * np.std(v, ddof=0)
        if th <= 0:
            return np.nan
        R = (np.abs(v[:, None] - v[None, :]) < th).astype(float)
        np.fill_diagonal(R, 0)
        diag_lens = []
        for k in range(1, n):
            diag = np.diag(R, k=k)
            cur = 0
            for vv in diag:
                if vv > 0.5:
                    cur += 1
                else:
                    if cur >= 2:
                        diag_lens.append(cur)
                    cur = 0
            if cur >= 2:
                diag_lens.append(cur)
        if len(diag_lens) < 2:
            return np.nan
        return float(max(diag_lens) - np.mean(diag_lens))
    out = r.rolling(252, min_periods=84).apply(_diff, raw=True)
    return out.diff().diff().diff()


def f42_acpe_180_cross_recurrence_close_vs_high_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    def _crc(w_pair):
        # called per-bar with a single column; we adapt: pass close and high separately via combined index
        return np.nan
    # Use rolling-corr as approximation for cross-recurrence trend
    out = lc.rolling(252, min_periods=84).corr(lh)
    return out.diff().diff().diff()


def f42_acpe_181_ordinal_pat_trans_entropy_d3_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _ordinal_pattern_transition_entropy(w, d=3), raw=True)
    return out.diff().diff().diff()


def f42_acpe_182_ordinal_pat_trans_entropy_d4_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _ordinal_pattern_transition_entropy(w, d=4), raw=True)
    return out.diff().diff().diff()


def f42_acpe_183_sign_markov_2x2_entropy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        sg = np.sign(v).astype(int)
        sg = np.where(sg == 0, 1, sg)
        pairs = list(zip(sg[:-1], sg[1:]))
        from collections import Counter
        cP = Counter(pairs)
        total = sum(cP.values())
        if total == 0:
            return np.nan
        return float(-sum((c / total) * np.log(c / total) for c in cP.values()))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_184_magnitude_3bin_markov_entropy_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        q33 = np.percentile(v, 33.3); q66 = np.percentile(v, 66.7)
        bins = np.where(v < q33, 0, np.where(v < q66, 1, 2))
        pairs = list(zip(bins[:-1], bins[1:]))
        from collections import Counter
        cP = Counter(pairs)
        total = sum(cP.values())
        if total == 0:
            return np.nan
        return float(-sum((c / total) * np.log(c / total) for c in cP.values()))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_185_time_reversal_asym_logret_lag1_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        return float(np.mean(v[1:] * v[:-1] ** 2) - np.mean(v[:-1] * v[1:] ** 2))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_186_time_reversal_asym_logret_lag1_504d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        return float(np.mean(v[1:] * v[:-1] ** 2) - np.mean(v[:-1] * v[1:] ** 2))
    out = r.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_187_bartels_rank_stat_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_bartels_rank_test, raw=True)
    return out.diff().diff().diff()


def f42_acpe_188_chaos_test_K_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_0_1_chaos_test, raw=True)
    return out.diff().diff().diff()


def f42_acpe_189_chaos_test_K_log_ret_504d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(504, min_periods=168).apply(_0_1_chaos_test, raw=True)
    return out.diff().diff().diff()


def f42_acpe_190_spectral_slope_logfreq_logpower_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        v = v - v.mean()
        n = v.size
        fft = np.fft.fft(v)
        psd = (np.abs(fft[1:n//2]) ** 2) / n
        freqs = np.arange(1, n//2)
        if psd.size < 5 or (psd <= 0).any():
            return np.nan
        x = np.log(freqs.astype(float)); y = np.log(psd)
        xm = x.mean(); ym = y.mean()
        den = float(((x - xm) ** 2).sum())
        if den == 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_191_pinkness_slope_near_minus1_indicator_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        v = v - v.mean()
        n = v.size
        fft = np.fft.fft(v)
        psd = (np.abs(fft[1:n//2]) ** 2) / n
        freqs = np.arange(1, n//2)
        if psd.size < 5 or (psd <= 0).any():
            return np.nan
        x = np.log(freqs.astype(float)); y = np.log(psd)
        xm = x.mean(); ym = y.mean()
        den = float(((x - xm) ** 2).sum())
        if den == 0:
            return np.nan
        slope = float(((x - xm) * (y - ym)).sum() / den)
        return float(abs(slope - (-1.0)) < 0.3)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_192_chaos_high_low_apen_composite_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    chaos_k = r.rolling(252, min_periods=84).apply(_0_1_chaos_test, raw=True)
    apen = r.rolling(252, min_periods=84).apply(lambda w: _apen(w, m=2, r_frac=0.2), raw=True)
    med_ap = apen.rolling(252, min_periods=84).median()
    out = ((chaos_k > 0.5) & (apen < med_ap)).astype(float).where(chaos_k.notna() & apen.notna() & med_ap.notna(), np.nan)
    return out.diff().diff().diff()


def f42_acpe_193_sevcik_fd_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_sevcik_fd, raw=True)
    return out.diff().diff().diff()


def f42_acpe_194_sevcik_fd_log_close_504d_d3(close: pd.Series) -> pd.Series:
    out = _safe_log(close).rolling(504, min_periods=168).apply(_sevcik_fd, raw=True)
    return out.diff().diff().diff()


def f42_acpe_195_active_info_storage_proxy_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        edges = np.linspace(np.min(v) - 1e-9, np.max(v) + 1e-9, 5)
        bins = np.digitize(v, edges) - 1
        pairs = list(zip(bins[:-1], bins[1:]))
        from collections import Counter
        cP = Counter(pairs)
        cX = Counter(bins[:-1])
        cY = Counter(bins[1:])
        total = sum(cP.values()); tot_x = sum(cX.values()); tot_y = sum(cY.values())
        ais = 0.0
        for (a, b), c in cP.items():
            pxy = c / total
            px = cX[a] / tot_x; py = cY[b] / tot_y
            if pxy > 0 and px > 0 and py > 0:
                ais += pxy * np.log(pxy / (px * py))
        return float(ais)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_196_dcca_close_vs_volume_scale21_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    lc = _safe_log(close); lv = _safe_log(volume.replace(0, np.nan))
    def _f(idx_arr, lc=lc, lv=lv):
        # rolling.apply doesn't easily pass two series; use a workaround via index
        return np.nan
    # Approximate DCCA via rolling-correlation of residuals from 21d linear-detrend
    lc_dt = lc - lc.rolling(21, min_periods=7).mean()
    lv_dt = lv - lv.rolling(21, min_periods=7).mean()
    out = lc_dt.rolling(252, min_periods=84).corr(lv_dt)
    return out.diff().diff().diff()


def f42_acpe_197_dcca_close_vs_range_scale21_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lr = _safe_log((high - low).replace(0, np.nan))
    lc_dt = lc - lc.rolling(21, min_periods=7).mean()
    lr_dt = lr - lr.rolling(21, min_periods=7).mean()
    out = lc_dt.rolling(252, min_periods=84).corr(lr_dt)
    return out.diff().diff().diff()


def f42_acpe_198_cross_acf_ret_volume_lag1_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    out = r.shift(1).rolling(252, min_periods=84).corr(v)
    return out.diff().diff().diff()


def f42_acpe_199_cross_acf_ret_volume_lag5_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    out = r.shift(5).rolling(252, min_periods=84).corr(v)
    return out.diff().diff().diff()


def f42_acpe_200_cross_acf_abs_ret_volume_lag1_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    v = _safe_log(volume.replace(0, np.nan))
    out = r.shift(1).rolling(252, min_periods=84).corr(v)
    return out.diff().diff().diff()


def f42_acpe_201_cross_acf_abs_ret_range_lag1_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    rng = _safe_log((high - low).replace(0, np.nan))
    out = r.shift(1).rolling(252, min_periods=84).corr(rng)
    return out.diff().diff().diff()


def f42_acpe_202_granger_proxy_volume_to_return_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    # r_t ~ v_{t-1} regression slope as Granger-like measure
    out = r.rolling(252, min_periods=84).cov(v.shift(1)) / v.shift(1).rolling(252, min_periods=84).var().replace(0, np.nan)
    return out.diff().diff().diff()


def f42_acpe_203_granger_proxy_return_to_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    out = v.rolling(252, min_periods=84).cov(r.shift(1)) / r.shift(1).rolling(252, min_periods=84).var().replace(0, np.nan)
    return out.diff().diff().diff()


def f42_acpe_204_acf_overnight_ret_lag1_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    og = _safe_log(open) - _safe_log(close.shift(1))
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    out = og.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_205_acf_intraday_ret_lag1_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    out = ir.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_206_overnight_intraday_cross_corr_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    og = _safe_log(open) - _safe_log(close.shift(1))
    ir = _safe_log(close) - _safe_log(open)
    out = og.rolling(252, min_periods=84).corr(ir)
    return out.diff().diff().diff()


def f42_acpe_207_ar1_anomaly_63d_vs_neighborhood_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ar1(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    ar = r.rolling(63, min_periods=21).apply(_ar1, raw=True).abs()
    nbh = ar.rolling(252, min_periods=84).mean()
    out = ar - nbh
    return out.diff().diff().diff()


def f42_acpe_208_cross_cumulant_ret_vol_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    r_dev = r - r.rolling(252, min_periods=84).mean()
    v_dev = v - v.rolling(252, min_periods=84).mean()
    out = (r_dev * v_dev * v_dev).rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f42_acpe_209_mutual_info_ret_volume_bin3_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    def _mi(w_r, w_v):
        mask = ~np.isnan(w_r) & ~np.isnan(w_v)
        if mask.sum() < 30:
            return np.nan
        r_ = w_r[mask]; v_ = w_v[mask]
        # 3-bin both
        qx = [np.percentile(r_, p) for p in (33.3, 66.7)]
        qy = [np.percentile(v_, p) for p in (33.3, 66.7)]
        rx = np.digitize(r_, qx)
        vy = np.digitize(v_, qy)
        from collections import Counter
        cJ = Counter(zip(rx, vy))
        cX = Counter(rx); cY = Counter(vy)
        n = r_.size
        mi = 0.0
        for (a, b), c in cJ.items():
            pxy = c / n; px = cX[a] / n; py = cY[b] / n
            if pxy > 0 and px > 0 and py > 0:
                mi += pxy * np.log(pxy / (px * py))
        return float(mi)
    # Compute via rolling 252d using paired-index manual loop
    arr_r = r.values; arr_v = v.values
    n_total = len(close)
    out_arr = np.full(n_total, np.nan)
    for i in range(84, n_total):
        start = max(0, i - 251)
        wr = arr_r[start:i+1]; wv = arr_v[start:i+1]
        out_arr[i] = _mi(wr, wv)
    out = pd.Series(out_arr, index=close.index)
    return out.diff().diff().diff()


def f42_acpe_210_vol_ret_causality_dir_proxy_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    # Direction: |corr(r, v.shift(1))| - |corr(v, r.shift(1))|
    c1 = r.rolling(252, min_periods=84).corr(v.shift(1)).abs()
    c2 = v.rolling(252, min_periods=84).corr(r.shift(1)).abs()
    out = c1 - c2
    return out.diff().diff().diff()


def f42_acpe_211_mfdfa_spectrum_width_at_qs_neg_pos_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    hq_neg = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=-2.0), raw=True)
    hq_pos = r.rolling(252, min_periods=84).apply(lambda w: _multifractal_dfa_q(w, q=2.0), raw=True)
    out = hq_neg - hq_pos
    return out.diff().diff().diff()


def f42_acpe_212_scale_dep_hurst_diff_63_vs_252_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    h63 = r.rolling(63, min_periods=21).apply(_rs, raw=True)
    h252 = r.rolling(252, min_periods=84).apply(_rs, raw=True)
    out = h63 - h252
    return out.diff().diff().diff()


def f42_acpe_213_sevcik_fd_close_504d_d3(close: pd.Series) -> pd.Series:
    out = close.rolling(504, min_periods=168).apply(_sevcik_fd, raw=True)
    return out.diff().diff().diff()


def f42_acpe_214_acf_integral_lags_1to5_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 7:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float(sum(abs((vc[k:] * vc[:-k]).sum() / den) for k in range(1, 6)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_215_acf_integral_lags_11to21_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 22:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float(sum(abs((vc[k:] * vc[:-k]).sum() / den) for k in range(11, 22)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_216_acf_integral_lags_22to63_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 84:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 64:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float(sum(abs((vc[k:] * vc[:-k]).sum() / den) for k in range(22, 64)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_217_acf_power_law_decay_slope_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        if v.size < 22:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        lags = list(range(1, 21))
        acs = [abs((vc[k:] * vc[:-k]).sum() / den) for k in lags]
        acs = np.array(acs)
        if (acs <= 0).any():
            return np.nan
        x = np.log(np.array(lags, dtype=float)); y = np.log(acs)
        xm = x.mean(); ym = y.mean()
        den2 = float(((x - xm) ** 2).sum())
        if den2 == 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den2)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_218_comp_long_memory_indicator_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    h = r.rolling(252, min_periods=84).apply(_rs, raw=True)
    d = r.rolling(252, min_periods=84).apply(_whittle_d_proxy, raw=True)
    lrs = r.rolling(252, min_periods=84).apply(_lo_modified_rs, raw=True)
    out = (h - 0.5).abs() + d.abs() + (lrs - 1.0).abs()
    return out.diff().diff().diff()


def f42_acpe_219_trend_vs_mean_revert_score_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ar1(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        return float((vc[1:] * vc[:-1]).sum() / den)
    ar = r.rolling(252, min_periods=84).apply(_ar1, raw=True)
    ret63 = _safe_log(close).diff(63)
    out = ar * np.sign(ret63)
    return out.diff().diff().diff()


def f42_acpe_220_turning_point_density_per_21d_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    is_tp = ((r > 0) & (r.shift(1) < 0)) | ((r < 0) & (r.shift(1) > 0))
    is_tp = is_tp.astype(float).where(r.notna() & r.shift(1).notna(), np.nan)
    out = is_tp.rolling(252, min_periods=84).sum() * 21.0 / 252.0
    return out.diff().diff().diff()


def f42_acpe_221_vr_pvalue_proxy_log_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        n = v.size
        if n < 10:
            return np.nan
        v_ = v - v.mean()
        var1 = float((v_ ** 2).mean())
        sums = np.add.reduceat(v_, np.arange(0, n - n % 5, 5))
        if sums.size < 2:
            return np.nan
        var5 = float((sums ** 2).mean() / 5.0)
        if var1 == 0:
            return np.nan
        vr = var5 / var1
        z = (vr - 1.0) * np.sqrt(n) / np.sqrt(2.0)
        # 2-sided p-value approx
        return float(2.0 * (1.0 - 0.5 * (1.0 + np.tanh(z / np.sqrt(2.0)))))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff().diff()


def f42_acpe_222_regime_classifier_random_walk_indicator_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    h = r.rolling(252, min_periods=84).apply(_rs, raw=True)
    out = ((h > 0.45) & (h < 0.55)).astype(float).where(h.notna(), np.nan)
    return out.diff().diff().diff()


def f42_acpe_223_hurst_acceleration_63d_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    h = r.rolling(252, min_periods=84).apply(_rs, raw=True)
    out = h - h.shift(63)
    return out.diff().diff().diff()


def f42_acpe_224_mfdfa_width_stability_std_63d_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    width = r.rolling(63, min_periods=21).apply(lambda w: _multifractal_dfa_q(w, q=1.0) - _multifractal_dfa_q(w, q=4.0), raw=True)
    out = width.rolling(252, min_periods=84).std()
    return out.diff().diff().diff()


def f42_acpe_225_comp_chaos_random_trend_classifier_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _rs(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        y = np.cumsum(v - v.mean())
        R = float(y.max() - y.min())
        S = float(np.std(v, ddof=0))
        if S == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(v)))
    h = r.rolling(252, min_periods=84).apply(_rs, raw=True)
    ck = r.rolling(252, min_periods=84).apply(_0_1_chaos_test, raw=True)
    # classification: 0 = random (|H-0.5|<0.05 and chaos<0.3); 1 = chaotic (chaos>0.5); 2 = trending (H>0.55)
    out = pd.Series(np.where(ck > 0.5, 1.0, np.where(h > 0.55, 2.0, 0.0)), index=r.index).where(h.notna() & ck.notna(), np.nan)
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 151_225 (d3)
# ============================================================

AUTOCORRELATION_PERSISTENCE_D3_REGISTRY_151_225 = {
    "f42_acpe_151_lo_modified_rs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_151_lo_modified_rs_log_ret_252d_d3},
    "f42_acpe_152_lo_modified_rs_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_152_lo_modified_rs_log_ret_504d_d3},
    "f42_acpe_153_lo_modified_rs_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_153_lo_modified_rs_abs_log_ret_252d_d3},
    "f42_acpe_154_gph_d_alpha_07_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_154_gph_d_alpha_07_log_ret_252d_d3},
    "f42_acpe_155_gph_d_alpha_05_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_155_gph_d_alpha_05_log_ret_252d_d3},
    "f42_acpe_156_whittle_d_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_156_whittle_d_log_ret_252d_d3},
    "f42_acpe_157_whittle_d_abs_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_157_whittle_d_abs_log_ret_252d_d3},
    "f42_acpe_158_kpss_level_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_158_kpss_level_log_ret_252d_d3},
    "f42_acpe_159_kpss_level_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_159_kpss_level_log_close_252d_d3},
    "f42_acpe_160_adf_tstat_log_close_252d_d3": {"inputs": ["close"], "func": f42_acpe_160_adf_tstat_log_close_252d_d3},
    "f42_acpe_161_mfdfa_h_q1_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_161_mfdfa_h_q1_log_ret_252d_d3},
    "f42_acpe_162_mfdfa_h_q2_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_162_mfdfa_h_q2_log_ret_252d_d3},
    "f42_acpe_163_mfdfa_h_q4_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_163_mfdfa_h_q4_log_ret_252d_d3},
    "f42_acpe_164_mfdfa_spectrum_width_q1_to_q4_252d_d3": {"inputs": ["close"], "func": f42_acpe_164_mfdfa_spectrum_width_q1_to_q4_252d_d3},
    "f42_acpe_165_hurst_of_hurst_63d_over_252d_d3": {"inputs": ["close"], "func": f42_acpe_165_hurst_of_hurst_63d_over_252d_d3},
    "f42_acpe_166_rqa_laminarity_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_166_rqa_laminarity_log_ret_252d_d3},
    "f42_acpe_167_rqa_trapping_time_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_167_rqa_trapping_time_log_ret_252d_d3},
    "f42_acpe_168_rqa_avg_diag_length_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_168_rqa_avg_diag_length_log_ret_252d_d3},
    "f42_acpe_169_rqa_max_diag_length_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_169_rqa_max_diag_length_log_ret_252d_d3},
    "f42_acpe_170_rqa_divergence_inv_max_diag_252d_d3": {"inputs": ["close"], "func": f42_acpe_170_rqa_divergence_inv_max_diag_252d_d3},
    "f42_acpe_171_rqa_entropy_diag_lengths_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_171_rqa_entropy_diag_lengths_log_ret_252d_d3},
    "f42_acpe_172_apen_m2_r02_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_172_apen_m2_r02_log_ret_252d_d3},
    "f42_acpe_173_apen_m3_r02_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_173_apen_m3_r02_log_ret_252d_d3},
    "f42_acpe_174_cond_entropy_log_ret_given_lag1_252d_d3": {"inputs": ["close"], "func": f42_acpe_174_cond_entropy_log_ret_given_lag1_252d_d3},
    "f42_acpe_175_block_2bar_joint_entropy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_175_block_2bar_joint_entropy_log_ret_252d_d3},
    "f42_acpe_176_recurrence_period_density_entropy_252d_d3": {"inputs": ["close"], "func": f42_acpe_176_recurrence_period_density_entropy_252d_d3},
    "f42_acpe_177_trapping_time_zscore_252d_d3": {"inputs": ["close"], "func": f42_acpe_177_trapping_time_zscore_252d_d3},
    "f42_acpe_178_rqa_det_strength_max_diag_over_avg_252d_d3": {"inputs": ["close"], "func": f42_acpe_178_rqa_det_strength_max_diag_over_avg_252d_d3},
    "f42_acpe_179_max_diag_minus_avg_diag_252d_d3": {"inputs": ["close"], "func": f42_acpe_179_max_diag_minus_avg_diag_252d_d3},
    "f42_acpe_180_cross_recurrence_close_vs_high_252d_d3": {"inputs": ["high", "close"], "func": f42_acpe_180_cross_recurrence_close_vs_high_252d_d3},
    "f42_acpe_181_ordinal_pat_trans_entropy_d3_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_181_ordinal_pat_trans_entropy_d3_log_ret_252d_d3},
    "f42_acpe_182_ordinal_pat_trans_entropy_d4_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_182_ordinal_pat_trans_entropy_d4_log_ret_252d_d3},
    "f42_acpe_183_sign_markov_2x2_entropy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_183_sign_markov_2x2_entropy_log_ret_252d_d3},
    "f42_acpe_184_magnitude_3bin_markov_entropy_252d_d3": {"inputs": ["close"], "func": f42_acpe_184_magnitude_3bin_markov_entropy_252d_d3},
    "f42_acpe_185_time_reversal_asym_logret_lag1_252d_d3": {"inputs": ["close"], "func": f42_acpe_185_time_reversal_asym_logret_lag1_252d_d3},
    "f42_acpe_186_time_reversal_asym_logret_lag1_504d_d3": {"inputs": ["close"], "func": f42_acpe_186_time_reversal_asym_logret_lag1_504d_d3},
    "f42_acpe_187_bartels_rank_stat_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_187_bartels_rank_stat_log_ret_252d_d3},
    "f42_acpe_188_chaos_test_K_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_188_chaos_test_K_log_ret_252d_d3},
    "f42_acpe_189_chaos_test_K_log_ret_504d_d3": {"inputs": ["close"], "func": f42_acpe_189_chaos_test_K_log_ret_504d_d3},
    "f42_acpe_190_spectral_slope_logfreq_logpower_252d_d3": {"inputs": ["close"], "func": f42_acpe_190_spectral_slope_logfreq_logpower_252d_d3},
    "f42_acpe_191_pinkness_slope_near_minus1_indicator_252d_d3": {"inputs": ["close"], "func": f42_acpe_191_pinkness_slope_near_minus1_indicator_252d_d3},
    "f42_acpe_192_chaos_high_low_apen_composite_252d_d3": {"inputs": ["close"], "func": f42_acpe_192_chaos_high_low_apen_composite_252d_d3},
    "f42_acpe_193_sevcik_fd_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_193_sevcik_fd_log_ret_252d_d3},
    "f42_acpe_194_sevcik_fd_log_close_504d_d3": {"inputs": ["close"], "func": f42_acpe_194_sevcik_fd_log_close_504d_d3},
    "f42_acpe_195_active_info_storage_proxy_252d_d3": {"inputs": ["close"], "func": f42_acpe_195_active_info_storage_proxy_252d_d3},
    "f42_acpe_196_dcca_close_vs_volume_scale21_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_196_dcca_close_vs_volume_scale21_252d_d3},
    "f42_acpe_197_dcca_close_vs_range_scale21_252d_d3": {"inputs": ["high", "low", "close"], "func": f42_acpe_197_dcca_close_vs_range_scale21_252d_d3},
    "f42_acpe_198_cross_acf_ret_volume_lag1_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_198_cross_acf_ret_volume_lag1_252d_d3},
    "f42_acpe_199_cross_acf_ret_volume_lag5_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_199_cross_acf_ret_volume_lag5_252d_d3},
    "f42_acpe_200_cross_acf_abs_ret_volume_lag1_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_200_cross_acf_abs_ret_volume_lag1_252d_d3},
    "f42_acpe_201_cross_acf_abs_ret_range_lag1_252d_d3": {"inputs": ["high", "low", "close"], "func": f42_acpe_201_cross_acf_abs_ret_range_lag1_252d_d3},
    "f42_acpe_202_granger_proxy_volume_to_return_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_202_granger_proxy_volume_to_return_252d_d3},
    "f42_acpe_203_granger_proxy_return_to_volume_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_203_granger_proxy_return_to_volume_252d_d3},
    "f42_acpe_204_acf_overnight_ret_lag1_252d_d3": {"inputs": ["open", "close"], "func": f42_acpe_204_acf_overnight_ret_lag1_252d_d3},
    "f42_acpe_205_acf_intraday_ret_lag1_252d_d3": {"inputs": ["open", "close"], "func": f42_acpe_205_acf_intraday_ret_lag1_252d_d3},
    "f42_acpe_206_overnight_intraday_cross_corr_252d_d3": {"inputs": ["open", "close"], "func": f42_acpe_206_overnight_intraday_cross_corr_252d_d3},
    "f42_acpe_207_ar1_anomaly_63d_vs_neighborhood_252d_d3": {"inputs": ["close"], "func": f42_acpe_207_ar1_anomaly_63d_vs_neighborhood_252d_d3},
    "f42_acpe_208_cross_cumulant_ret_vol_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_208_cross_cumulant_ret_vol_252d_d3},
    "f42_acpe_209_mutual_info_ret_volume_bin3_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_209_mutual_info_ret_volume_bin3_252d_d3},
    "f42_acpe_210_vol_ret_causality_dir_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f42_acpe_210_vol_ret_causality_dir_proxy_252d_d3},
    "f42_acpe_211_mfdfa_spectrum_width_at_qs_neg_pos_252d_d3": {"inputs": ["close"], "func": f42_acpe_211_mfdfa_spectrum_width_at_qs_neg_pos_252d_d3},
    "f42_acpe_212_scale_dep_hurst_diff_63_vs_252_252d_d3": {"inputs": ["close"], "func": f42_acpe_212_scale_dep_hurst_diff_63_vs_252_252d_d3},
    "f42_acpe_213_sevcik_fd_close_504d_d3": {"inputs": ["close"], "func": f42_acpe_213_sevcik_fd_close_504d_d3},
    "f42_acpe_214_acf_integral_lags_1to5_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_214_acf_integral_lags_1to5_log_ret_252d_d3},
    "f42_acpe_215_acf_integral_lags_11to21_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_215_acf_integral_lags_11to21_log_ret_252d_d3},
    "f42_acpe_216_acf_integral_lags_22to63_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_216_acf_integral_lags_22to63_log_ret_252d_d3},
    "f42_acpe_217_acf_power_law_decay_slope_252d_d3": {"inputs": ["close"], "func": f42_acpe_217_acf_power_law_decay_slope_252d_d3},
    "f42_acpe_218_comp_long_memory_indicator_252d_d3": {"inputs": ["close"], "func": f42_acpe_218_comp_long_memory_indicator_252d_d3},
    "f42_acpe_219_trend_vs_mean_revert_score_252d_d3": {"inputs": ["close"], "func": f42_acpe_219_trend_vs_mean_revert_score_252d_d3},
    "f42_acpe_220_turning_point_density_per_21d_252d_d3": {"inputs": ["close"], "func": f42_acpe_220_turning_point_density_per_21d_252d_d3},
    "f42_acpe_221_vr_pvalue_proxy_log_ret_252d_d3": {"inputs": ["close"], "func": f42_acpe_221_vr_pvalue_proxy_log_ret_252d_d3},
    "f42_acpe_222_regime_classifier_random_walk_indicator_252d_d3": {"inputs": ["close"], "func": f42_acpe_222_regime_classifier_random_walk_indicator_252d_d3},
    "f42_acpe_223_hurst_acceleration_63d_252d_d3": {"inputs": ["close"], "func": f42_acpe_223_hurst_acceleration_63d_252d_d3},
    "f42_acpe_224_mfdfa_width_stability_std_63d_in_252d_d3": {"inputs": ["close"], "func": f42_acpe_224_mfdfa_width_stability_std_63d_in_252d_d3},
    "f42_acpe_225_comp_chaos_random_trend_classifier_252d_d3": {"inputs": ["close"], "func": f42_acpe_225_comp_chaos_random_trend_classifier_252d_d3},
}
