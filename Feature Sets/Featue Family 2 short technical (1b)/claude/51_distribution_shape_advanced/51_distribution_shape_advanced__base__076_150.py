"""distribution_shape_advanced base features 076-150 - Pipeline 1b-technical.

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


def _norm_ppf(p):
    """Rational approximation of standard-normal inverse CDF (Beasley-Springer-Moro simplified)."""
    p = float(p)
    if not (0.0 < p < 1.0):
        return np.nan
    if p < 0.5:
        t = np.sqrt(-2.0 * np.log(p))
        x = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (
            1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t ** 3)
        return -x
    else:
        t = np.sqrt(-2.0 * np.log(1.0 - p))
        x = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (
            1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t ** 3)
        return x


def _norm_cdf(x):
    """Standard normal CDF via erf."""
    from math import erf, sqrt
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _rolling_skew(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).skew()


def _rolling_kurt(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).kurt()

def _hartigan_dip(s, n):
    """Hartigan dip statistic via simple Hartigan-Hartigan recursion (greatest-convex-minorant)."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v = np.sort(v)
        nv = v.size
        f = np.arange(1, nv + 1, dtype=float) / nv
        # gcm: greatest convex minorant of empirical CDF
        gcm_y = np.empty(nv); gcm_y[0] = f[0]
        for i in range(1, nv):
            slope = (f[i] - f[0]) / max(i, 1)
            best = f[0] + slope * i
            for j in range(1, i):
                sl = (f[i] - f[j]) / (i - j)
                cand = f[j] + sl * (i - j)
                if cand < best:
                    best = cand
            gcm_y[i] = best
        # lcm: least concave majorant
        lcm_y = np.empty(nv); lcm_y[-1] = f[-1]
        for i in range(nv - 2, -1, -1):
            slope = (f[nv - 1] - f[i]) / max(nv - 1 - i, 1)
            best = f[i] + slope * 0.0
            for j in range(i + 1, nv):
                sl = (f[j] - f[i]) / (j - i)
                cand = f[i]
                if cand > best:
                    best = cand
            lcm_y[i] = best
        return float(np.max(np.abs(gcm_y - lcm_y)))
    # downsample windows to keep cost bounded
    def _g(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sub = v if v.size <= 80 else v[np.linspace(0, v.size - 1, 80).astype(int)]
        return _f(sub)
    return s.rolling(n, min_periods=mp).apply(_g, raw=True)


def _bimodality_coef(s, n):
    """Bimodality coefficient = (skew^2 + 1) / (kurt + 3*(n-1)^2/((n-2)(n-3)))."""
    mp = max(n // 3, 30)
    sk = s.rolling(n, min_periods=mp).skew()
    kt = s.rolling(n, min_periods=mp).kurt()  # excess kurt
    cnt = s.rolling(n, min_periods=mp).count()
    correction = 3.0 * (cnt - 1) ** 2 / ((cnt - 2) * (cnt - 3))
    denom = (kt + 3.0) + correction.where(cnt > 3, np.nan)
    return _safe_div(sk ** 2 + 1.0, denom)


def _kde_mode_count(s, n, bw_factor=0.3):
    """Approximate mode count via histogram smoothing."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = float(v.min()); hi = float(v.max())
        if hi <= lo:
            return 1.0
        nb = max(min(int(np.sqrt(v.size)), 30), 8)
        edges = np.linspace(lo, hi, nb + 1)
        h, _ = np.histogram(v, bins=edges)
        h = h.astype(float)
        # simple triangular smoothing
        k = max(int(bw_factor * nb), 1)
        kernel = np.bartlett(2 * k + 1)
        kernel = kernel / kernel.sum()
        h_s = np.convolve(h, kernel, mode="same")
        modes = 0
        for i in range(1, len(h_s) - 1):
            if h_s[i] > h_s[i - 1] and h_s[i] > h_s[i + 1]:
                modes += 1
        return float(modes) if modes > 0 else 1.0
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hodges_lehmann(s, n):
    """Median of all pairwise averages (downsampled for cost)."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sub = v if v.size <= 60 else v[np.linspace(0, v.size - 1, 60).astype(int)]
        pa = (sub[:, None] + sub[None, :]) / 2.0
        return float(np.median(pa[np.triu_indices_from(pa)]))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _trimean_tukey(s, n):
    """Trimean = (Q1 + 2*Q2 + Q3) / 4."""
    q1 = _rolling_q(s, n, 0.25)
    q2 = _rolling_q(s, n, 0.50)
    q3 = _rolling_q(s, n, 0.75)
    return (q1 + 2.0 * q2 + q3) / 4.0


def _midhinge(s, n):
    """Midhinge = (Q1 + Q3) / 2."""
    q1 = _rolling_q(s, n, 0.25)
    q3 = _rolling_q(s, n, 0.75)
    return (q1 + q3) / 2.0


def _shorth_mean(s, n, frac=0.5):
    """Mean of the shortest interval containing `frac` of the data."""
    mp = max(n // 3, 30)
    def _f(w):
        v = np.sort(w[~np.isnan(w)])
        nv = v.size
        if nv < 30:
            return np.nan
        k = max(int(frac * nv), 5)
        if k >= nv:
            return float(v.mean())
        spans = v[k - 1:] - v[: nv - k + 1]
        i = int(np.argmin(spans))
        return float(v[i:i + k].mean())
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _m_estimator_huber(s, n, c=1.345):
    """Huber M-estimator (iterated, capped at 10 iterations)."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = float(np.median(v))
        for _ in range(10):
            sd = float(np.median(np.abs(v - mu))) * 1.4826
            if sd <= 0:
                return mu
            u = (v - mu) / sd
            w_h = np.where(np.abs(u) <= c, 1.0, c / np.abs(u))
            new_mu = float(np.sum(w_h * v) / np.sum(w_h))
            if abs(new_mu - mu) < 1e-8:
                break
            mu = new_mu
        return mu
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _medcouple(s, n):
    """Brys-Hubert-Struyf medcouple (robust skewness in [-1, 1])."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        if v.size > 80:
            v = v[np.linspace(0, v.size - 1, 80).astype(int)]
        med = float(np.median(v))
        left = v[v <= med]; right = v[v >= med]
        if left.size == 0 or right.size == 0:
            return np.nan
        # h(x_i, y_j) = ((y - med) - (med - x)) / (y - x); skip ties
        rows = []
        for x in left:
            for y in right:
                if y == x:
                    continue
                h_val = ((y - med) - (med - x)) / (y - x)
                rows.append(h_val)
        if not rows:
            return np.nan
        return float(np.median(rows))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hogg_robust_skew(s, n):
    """Hogg skewness = (U(0.05) - L(0.05)) / (U(0.5) - L(0.5)) -- denominator IQR-like."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        v = np.sort(v)
        nv = v.size
        k5 = max(int(0.05 * nv), 1)
        k50 = max(int(0.50 * nv), 2)
        U05 = v[-k5:].mean()
        L05 = v[:k5].mean()
        U50 = v[nv - k50:].mean()
        L50 = v[:k50].mean()
        den = U50 - L50
        if den <= 0:
            return np.nan
        num = (U05 - U50) - (L50 - L05)
        return float(num / den)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _crow_siddiqui_kurt(s, n):
    """(P97.5 - P2.5) / (P75 - P25)."""
    p975 = _rolling_q(s, n, 0.975)
    p025 = _rolling_q(s, n, 0.025)
    p75 = _rolling_q(s, n, 0.75)
    p25 = _rolling_q(s, n, 0.25)
    return _safe_div(p975 - p025, p75 - p25)


def _hogg_kurt(s, n):
    """Hogg kurtosis = (U(0.05) - L(0.05)) / (U(0.5) - L(0.5))."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        v = np.sort(v)
        nv = v.size
        k5 = max(int(0.05 * nv), 1)
        k50 = max(int(0.50 * nv), 2)
        U05 = v[-k5:].mean()
        L05 = v[:k5].mean()
        U50 = v[nv - k50:].mean()
        L50 = v[:k50].mean()
        den = U50 - L50
        if den <= 0:
            return np.nan
        return float((U05 - L05) / den)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _cramer_von_mises_normal(s, n):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = np.sort((v - mu) / sd)
        cdf = np.array([_norm_cdf(zi) for zi in z])
        nv = z.size
        i = np.arange(1, nv + 1, dtype=float)
        cvm = 1.0 / (12.0 * nv) + np.sum((cdf - (2 * i - 1) / (2 * nv)) ** 2)
        return float(cvm)
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _wasserstein_distance_to_normal(s, n):
    """Approximate 1-Wasserstein distance between empirical and fitted-normal CDFs."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        v = np.sort(v)
        nv = v.size
        # match empirical quantiles to normal quantiles
        p = (np.arange(1, nv + 1, dtype=float) - 0.5) / nv
        q_emp = v
        q_norm = mu + sd * np.array([_norm_ppf(pi) for pi in p])
        return float(np.mean(np.abs(q_emp - q_norm)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hellinger_distance_to_normal(s, n):
    """Discrete Hellinger distance between binned empirical pdf and fitted-normal pdf."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        p_emp, _ = np.histogram(v, bins=edges, density=True)
        mids = 0.5 * (edges[:-1] + edges[1:])
        p_norm = (1.0 / (sd * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((mids - mu) / sd) ** 2)
        bw = edges[1] - edges[0]
        return float(np.sqrt(0.5 * np.sum((np.sqrt(np.maximum(p_emp, 0.0)) -
                                            np.sqrt(np.maximum(p_norm, 0.0))) ** 2) * bw))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _renyi_entropy(s, n, q):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        if q == 1.0:
            return float(-(p * np.log(p)).sum())
        return float(np.log((p ** q).sum()) / (1.0 - q))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _fit_laplace_b(s, n):
    """Laplace MLE b = mean(|x - median|)."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        return float(np.mean(np.abs(v - np.median(v))))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _fit_skewnormal_lambda(s, n):
    """Skew-normal shape proxy: skewness implied by sample, mapped to lambda via simple relation."""
    sk = s.rolling(n, min_periods=max(n // 3, 20)).skew()
    # delta = sign(sk) * sqrt(pi / 2) * |sk|^(1/3) / sqrt(1 + |sk|^(2/3)) (Pewsey approx)
    sg = np.sign(sk)
    a = sk.abs() ** (1.0 / 3.0)
    delta = sg * np.sqrt(np.pi / 2.0) * a / np.sqrt(1.0 + a * a)
    lam = delta / np.sqrt(1.0 - delta * delta).replace(0, np.nan)
    return lam


def _fit_t_df_from_kurt(s, n):
    """Implied Student-t df from kurt: df = 4 + 6/excess_kurt (Fisher, capped 3-100)."""
    k = _rolling_kurt(s, n)
    return (4.0 + 6.0 / k.replace(0, np.nan)).clip(lower=3.0, upper=100.0)


def _fit_pareto_alpha_upper(s, n, k_frac=0.10):
    """Hill alpha on top k_frac tail."""
    mp = max(n // 3, 30)
    def _f(w):
        v = w[~np.isnan(w)]
        v = v[v > 0]
        if v.size < 30:
            return np.nan
        v = np.sort(v)
        k = max(int(k_frac * v.size), 5)
        if k >= v.size:
            return np.nan
        thr = v[v.size - k - 1]
        tail = v[v.size - k:]
        if thr <= 0:
            return np.nan
        return float(1.0 / np.mean(np.log(tail / thr)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _log_likelihood_normal(s, n):
    """Per-bar log-likelihood of fitted Normal on window."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(-0.5 * np.log(2.0 * np.pi * sd * sd) - 0.5 * ((v - mu) / sd) ** 2))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _log_likelihood_laplace(s, n):
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        med = np.median(v)
        b = np.mean(np.abs(v - med))
        if b <= 0:
            return np.nan
        return float(np.mean(-np.log(2.0 * b) - np.abs(v - med) / b))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def f51_dsav_076_coskew_tr_with_close_ret_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coskewness between (high-low)/close and log_ret over 252d."""
    r = _log_ret(close)
    tr = _safe_div(_true_range(high, low, close), close)
    mu_r = r.rolling(YDAYS, min_periods=QDAYS).mean()
    mu_t = tr.rolling(YDAYS, min_periods=QDAYS).mean()
    sd_r = r.rolling(YDAYS, min_periods=QDAYS).std()
    sd_t = tr.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((tr - mu_t) * (r - mu_r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd_t * sd_r ** 2))

def f51_dsav_077_cokurt_tr_with_close_ret_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """E[(TR-mu)^2 * (r-mu)^2] / (sd_TR^2 * sd_r^2) over 252d."""
    r = _log_ret(close)
    tr = _safe_div(_true_range(high, low, close), close)
    mu_r = r.rolling(YDAYS, min_periods=QDAYS).mean()
    mu_t = tr.rolling(YDAYS, min_periods=QDAYS).mean()
    sd_r = r.rolling(YDAYS, min_periods=QDAYS).std()
    sd_t = tr.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((tr - mu_t) ** 2 * (r - mu_r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, (sd_t * sd_r) ** 2))

def f51_dsav_078_cross_moment_r_log_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """E[r^2 * log_volume] over 252d - vol-volume co-movement."""
    r = _log_ret(close)
    lv = _safe_log(volume.replace(0, np.nan))
    return ((r ** 2 * lv).rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_079_cross_moment_r_log_volume_change_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """E[r * d(log_volume)] over 252d - return vs volume-shock correlation magnitude."""
    r = _log_ret(close)
    dlv = _safe_log(volume.replace(0, np.nan)).diff()
    return ((r * dlv).rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_080_cross_moment_absr_log_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """E[|r| * log_volume] over 252d."""
    r = _log_ret(close).abs()
    lv = _safe_log(volume.replace(0, np.nan))
    return ((r * lv).rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_081_mean_log_ret_above_mean_252d(close: pd.Series) -> pd.Series:
    """E[r | r > mean(r)] over 252d - upside conditional mean."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = r.where(r > mu, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_082_mean_log_ret_below_mean_252d(close: pd.Series) -> pd.Series:
    """E[r | r < mean(r)] over 252d - downside conditional mean."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = r.where(r < mu, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_083_var_log_ret_above_mean_252d(close: pd.Series) -> pd.Series:
    """Var(r | r > mean) over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = r.where(r > mu, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).var())

def f51_dsav_084_var_log_ret_below_mean_252d(close: pd.Series) -> pd.Series:
    """Var(r | r < mean) over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = r.where(r < mu, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).var())

def f51_dsav_085_ratio_upside_to_downside_var_252d(close: pd.Series) -> pd.Series:
    """Var(r | r > mean) / Var(r | r < mean) over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    vu = r.where(r > mu, np.nan).rolling(YDAYS, min_periods=QDAYS).var()
    vd = r.where(r < mu, np.nan).rolling(YDAYS, min_periods=QDAYS).var()
    return (_safe_div(vu, vd))

def f51_dsav_086_mean_log_ret_after_neg_252d(close: pd.Series) -> pd.Series:
    """E[r_t | r_{t-1} < 0] over 252d - return after a down day."""
    r = _log_ret(close)
    cond = r.where(r.shift(1) < 0, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_087_mean_log_ret_after_pos_252d(close: pd.Series) -> pd.Series:
    """E[r_t | r_{t-1} > 0] over 252d."""
    r = _log_ret(close)
    cond = r.where(r.shift(1) > 0, np.nan)
    return (cond.rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_088_vol_log_ret_after_neg_252d(close: pd.Series) -> pd.Series:
    """Sqrt(E[r_t^2 | r_{t-1} < 0]) over 252d - vol after a down day (leverage effect)."""
    r = _log_ret(close)
    cond_sq = (r ** 2).where(r.shift(1) < 0, np.nan)
    return (cond_sq.rolling(YDAYS, min_periods=QDAYS).mean().pow(0.5))

def f51_dsav_089_vol_log_ret_after_pos_252d(close: pd.Series) -> pd.Series:
    """Sqrt(E[r_t^2 | r_{t-1} > 0]) over 252d."""
    r = _log_ret(close)
    cond_sq = (r ** 2).where(r.shift(1) > 0, np.nan)
    return (cond_sq.rolling(YDAYS, min_periods=QDAYS).mean().pow(0.5))

def f51_dsav_090_ratio_vol_after_neg_to_pos_252d(close: pd.Series) -> pd.Series:
    """Vol(r | prev<0) / Vol(r | prev>0) - direct leverage-effect ratio over 252d."""
    r = _log_ret(close)
    vn = ((r ** 2).where(r.shift(1) < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    vp = ((r ** 2).where(r.shift(1) > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).pow(0.5)
    return (_safe_div(vn, vp))

def f51_dsav_091_realized_skewness_21d_amaya_log_ret(close: pd.Series) -> pd.Series:
    """Realized skewness over 21d: sqrt(n)*sum r^3 / (sum r^2)^1.5 (Amaya et al.)."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(MDAYS, min_periods=10).sum()
    r3 = (r ** 3).rolling(MDAYS, min_periods=10).sum()
    cnt = r.rolling(MDAYS, min_periods=10).count()
    return (_safe_div(cnt.pow(0.5) * r3, r2.pow(1.5)))

def f51_dsav_092_realized_kurtosis_21d_amaya_log_ret(close: pd.Series) -> pd.Series:
    """Realized kurtosis over 21d: n*sum r^4 / (sum r^2)^2."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(MDAYS, min_periods=10).sum()
    r4 = (r ** 4).rolling(MDAYS, min_periods=10).sum()
    cnt = r.rolling(MDAYS, min_periods=10).count()
    return (_safe_div(cnt * r4, r2 ** 2))

def f51_dsav_093_realized_skewness_63d_amaya_log_ret(close: pd.Series) -> pd.Series:
    """Realized skewness over 63d."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(QDAYS, min_periods=20).sum()
    r3 = (r ** 3).rolling(QDAYS, min_periods=20).sum()
    cnt = r.rolling(QDAYS, min_periods=20).count()
    return (_safe_div(cnt.pow(0.5) * r3, r2.pow(1.5)))

def f51_dsav_094_realized_kurtosis_63d_amaya_log_ret(close: pd.Series) -> pd.Series:
    """Realized kurtosis over 63d."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(QDAYS, min_periods=20).sum()
    r4 = (r ** 4).rolling(QDAYS, min_periods=20).sum()
    cnt = r.rolling(QDAYS, min_periods=20).count()
    return (_safe_div(cnt * r4, r2 ** 2))

def f51_dsav_095_signed_jump_variation_63d_log_ret(close: pd.Series) -> pd.Series:
    """Sum of r_t^2 * sign(r_t) over 63d - signed-jump variation (Patton-Sheppard)."""
    r = _log_ret(close)
    sjv = (r ** 2 * np.sign(r)).rolling(QDAYS, min_periods=MDAYS).sum()
    return (sjv)

def f51_dsav_096_signed_jump_variation_252d_log_ret(close: pd.Series) -> pd.Series:
    """Same over 252d."""
    r = _log_ret(close)
    sjv = (r ** 2 * np.sign(r)).rolling(YDAYS, min_periods=QDAYS).sum()
    return (sjv)

def f51_dsav_097_realized_negative_semivariance_63d_log_ret(close: pd.Series) -> pd.Series:
    """Sum of r^2 over r<0 over 63d - downside realized semivar."""
    r = _log_ret(close)
    rsq_neg = (r ** 2).where(r < 0, 0.0)
    return (rsq_neg.rolling(QDAYS, min_periods=MDAYS).sum())

def f51_dsav_098_realized_positive_semivariance_63d_log_ret(close: pd.Series) -> pd.Series:
    """Sum of r^2 over r>0 over 63d."""
    r = _log_ret(close)
    rsq_pos = (r ** 2).where(r > 0, 0.0)
    return (rsq_pos.rolling(QDAYS, min_periods=MDAYS).sum())

def f51_dsav_099_realized_semivariance_diff_neg_minus_pos_252d(close: pd.Series) -> pd.Series:
    """(Neg realized semivar) - (Pos realized semivar) over 252d - signed downside-dominance."""
    r = _log_ret(close)
    neg = (r ** 2).where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    pos = (r ** 2).where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    return (neg - pos)

def f51_dsav_100_realized_skew_jumps_decomp_63d(close: pd.Series) -> pd.Series:
    """Sum r^3 component restricted to |r| > 3*std (jump-component skew) over 63d."""
    r = _log_ret(close)
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    jump = (r ** 3).where(r.abs() > 3.0 * sd, 0.0)
    return (jump.rolling(QDAYS, min_periods=MDAYS).sum())

def f51_dsav_101_rousseeuw_croux_sn_proxy_252d(close: pd.Series) -> pd.Series:
    """Rousseeuw-Croux Sn proxy = median_i median_j |x_i - x_j| over 252d (downsampled)."""
    r = _log_ret(close)
    def _sn(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sub = v if v.size <= 60 else v[np.linspace(0, v.size - 1, 60).astype(int)]
        inner = np.array([np.median(np.abs(sub - x)) for x in sub])
        return float(1.1926 * np.median(inner))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sn, raw=True)
    return (res)

def f51_dsav_102_rousseeuw_croux_qn_proxy_252d(close: pd.Series) -> pd.Series:
    """Rousseeuw-Croux Qn proxy = first quartile of all pairwise distances over 252d."""
    r = _log_ret(close)
    def _qn(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sub = v if v.size <= 60 else v[np.linspace(0, v.size - 1, 60).astype(int)]
        dist = np.abs(sub[:, None] - sub[None, :])
        tri = dist[np.triu_indices_from(dist, k=1)]
        if tri.size == 0:
            return np.nan
        return float(2.219 * np.quantile(tri, 0.25))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_qn, raw=True)
    return (res)

def f51_dsav_103_biweight_midvariance_252d(close: pd.Series) -> pd.Series:
    """Biweight midvariance of 252d log-returns - robust scale estimator."""
    r = _log_ret(close)
    def _bm(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        med = np.median(v); mad = np.median(np.abs(v - med))
        if mad <= 0:
            return np.nan
        u = (v - med) / (9.0 * mad)
        mask = np.abs(u) < 1.0
        if mask.sum() < 3:
            return np.nan
        num = float(np.sum((v[mask] - med) ** 2 * (1 - u[mask] ** 2) ** 4))
        den = float(np.sum((1 - u[mask] ** 2) * (1 - 5 * u[mask] ** 2)))
        if den == 0:
            return np.nan
        return float(v.size * num / (den * den))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bm, raw=True)
    return (res)

def f51_dsav_104_biweight_midcorrelation_with_lag1_252d(close: pd.Series) -> pd.Series:
    """Biweight midcorrelation between r and r_lag1 over 252d - robust serial correlation."""
    r = _log_ret(close)
    lag = r.shift(1)
    def _bmc(w):
        n = w.shape[0]
        if n < 30:
            return np.nan
        a = w[:, 0]; b = w[:, 1]
        valid = ~np.isnan(a) & ~np.isnan(b)
        if valid.sum() < 30:
            return np.nan
        a = a[valid]; b = b[valid]
        med_a = np.median(a); med_b = np.median(b)
        mad_a = np.median(np.abs(a - med_a)); mad_b = np.median(np.abs(b - med_b))
        if mad_a <= 0 or mad_b <= 0:
            return np.nan
        u = (a - med_a) / (9.0 * mad_a); vv = (b - med_b) / (9.0 * mad_b)
        wu = (1 - u ** 2) ** 2 * (np.abs(u) < 1)
        wv = (1 - vv ** 2) ** 2 * (np.abs(vv) < 1)
        num = np.sum((a - med_a) * wu * (b - med_b) * wv)
        den = np.sqrt(np.sum((a - med_a) ** 2 * wu ** 2) * np.sum((b - med_b) ** 2 * wv ** 2))
        if den == 0:
            return np.nan
        return float(num / den)
    df = pd.concat([r.rename('r'), lag.rename('l')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _bmc(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res)

def f51_dsav_105_scale_ratio_qn_to_sd_252d(close: pd.Series) -> pd.Series:
    """Qn / sd over 252d - heavy-tail diagnostic (=1 for normal, <1 indicates outliers)."""
    r = _log_ret(close)
    def _qn(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sub = v if v.size <= 60 else v[np.linspace(0, v.size - 1, 60).astype(int)]
        dist = np.abs(sub[:, None] - sub[None, :])
        tri = dist[np.triu_indices_from(dist, k=1)]
        if tri.size == 0:
            return np.nan
        return float(2.219 * np.quantile(tri, 0.25))
    qn = r.rolling(YDAYS, min_periods=QDAYS).apply(_qn, raw=True)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(qn, sd))

def f51_dsav_106_scale_ratio_mad_to_sd_252d(close: pd.Series) -> pd.Series:
    """1.4826 * MAD / sd over 252d."""
    r = _log_ret(close)
    med = _rolling_q(r, YDAYS, 0.5)
    mad = (r - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(1.4826 * mad, sd))

def f51_dsav_107_scale_ratio_iqr_normal_to_sd_252d(close: pd.Series) -> pd.Series:
    """(IQR / 1.349) / sd over 252d (1.349 = normal IQR/sigma)."""
    r = _log_ret(close)
    iqr = _rolling_q(r, YDAYS, 0.75) - _rolling_q(r, YDAYS, 0.25)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(iqr / 1.349, sd))

def f51_dsav_108_m_estimator_huber_scale_252d(close: pd.Series) -> pd.Series:
    """Huber M-estimator of scale (iterated) over 252d."""
    r = _log_ret(close)
    def _hs(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        med = np.median(v)
        s = 1.4826 * np.median(np.abs(v - med))
        if s <= 0:
            return np.nan
        for _ in range(10):
            u = (v - med) / s
            psi = np.clip(u, -1.345, 1.345)
            s_new = np.sqrt(np.mean(psi ** 2)) * s / 0.778
            if abs(s_new - s) < 1e-8:
                break
            s = s_new
        return float(s)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)
    return (res)

def f51_dsav_109_midhinge_dispersion_p15_p85_252d(close: pd.Series) -> pd.Series:
    """(P85 - P15) - middle-70 spread over 252d."""
    r = _log_ret(close)
    p85 = _rolling_q(r, YDAYS, 0.85)
    p15 = _rolling_q(r, YDAYS, 0.15)
    return (p85 - p15)

def f51_dsav_110_octile_dispersion_e7_minus_e1_252d(close: pd.Series) -> pd.Series:
    """(E7 - E1) octile spread over 252d."""
    r = _log_ret(close)
    e7 = _rolling_q(r, YDAYS, 0.875)
    e1 = _rolling_q(r, YDAYS, 0.125)
    return (e7 - e1)

def f51_dsav_111_kde_left_tail_density_at_p05_252d(close: pd.Series) -> pd.Series:
    """Kernel density at the 5th percentile - empirical-pdf height at the left-tail boundary."""
    r = _log_ret(close)
    def _kt(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        p5 = np.quantile(v, 0.05)
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        z = (v - p5) / bw
        return float(np.mean(np.exp(-0.5 * z * z)) / (bw * np.sqrt(2.0 * np.pi)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_kt, raw=True)
    return (res)

def f51_dsav_112_kde_right_tail_density_at_p95_252d(close: pd.Series) -> pd.Series:
    """Kernel density at the 95th percentile over 252d."""
    r = _log_ret(close)
    def _kt(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        p95 = np.quantile(v, 0.95)
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        z = (v - p95) / bw
        return float(np.mean(np.exp(-0.5 * z * z)) / (bw * np.sqrt(2.0 * np.pi)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_kt, raw=True)
    return (res)

def f51_dsav_113_tail_asymmetry_p05_minus_p95_density_252d(close: pd.Series) -> pd.Series:
    """KDE-density at P5 minus density at P95 over 252d - left vs right tail density gap."""
    r = _log_ret(close)
    def _ta(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        p5 = np.quantile(v, 0.05); p95 = np.quantile(v, 0.95)
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        z5 = (v - p5) / bw; z95 = (v - p95) / bw
        d5 = np.mean(np.exp(-0.5 * z5 * z5)) / (bw * np.sqrt(2.0 * np.pi))
        d95 = np.mean(np.exp(-0.5 * z95 * z95)) / (bw * np.sqrt(2.0 * np.pi))
        return float(d5 - d95)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True)
    return (res)

def f51_dsav_114_p99_minus_p95_log_ret_252d(close: pd.Series) -> pd.Series:
    """P99 - P95 of log-returns - upper-extreme spread."""
    r = _log_ret(close)
    p99 = _rolling_q(r, YDAYS, 0.99); p95 = _rolling_q(r, YDAYS, 0.95)
    return (p99 - p95)

def f51_dsav_115_p05_minus_p01_log_ret_252d(close: pd.Series) -> pd.Series:
    """P5 - P1 of log-returns - lower-extreme spread."""
    r = _log_ret(close)
    p05 = _rolling_q(r, YDAYS, 0.05); p01 = _rolling_q(r, YDAYS, 0.01)
    return (p05 - p01)

def f51_dsav_116_ratio_extreme_spread_left_to_right_252d(close: pd.Series) -> pd.Series:
    """(P05-P01) magnitude / (P99-P95) over 252d - extreme asymmetry."""
    r = _log_ret(close)
    p99 = _rolling_q(r, YDAYS, 0.99); p95 = _rolling_q(r, YDAYS, 0.95)
    p05 = _rolling_q(r, YDAYS, 0.05); p01 = _rolling_q(r, YDAYS, 0.01)
    return (_safe_div((p05 - p01).abs(), p99 - p95))

def f51_dsav_117_kde_mode_value_log_ret_252d(close: pd.Series) -> pd.Series:
    """Value at which KDE is maximized (mode estimate) over 252d."""
    r = _log_ret(close)
    def _km(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        grid = np.linspace(v.min(), v.max(), 41)
        best = grid[0]; best_d = -1.0
        for g in grid:
            z = (v - g) / bw
            d = np.mean(np.exp(-0.5 * z * z)) / (bw * np.sqrt(2.0 * np.pi))
            if d > best_d:
                best_d = d; best = g
        return float(best)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_km, raw=True)
    return (res)

def f51_dsav_118_kde_mode_minus_mean_log_ret_252d(close: pd.Series) -> pd.Series:
    """KDE-mode minus arithmetic mean over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    def _km(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        grid = np.linspace(v.min(), v.max(), 41)
        best = grid[0]; best_d = -1.0
        for g in grid:
            z = (v - g) / bw
            d = np.mean(np.exp(-0.5 * z * z)) / (bw * np.sqrt(2.0 * np.pi))
            if d > best_d:
                best_d = d; best = g
        return float(best)
    mode = r.rolling(YDAYS, min_periods=QDAYS).apply(_km, raw=True)
    return (mode - mu)

def f51_dsav_119_kde_mode_minus_median_log_ret_252d(close: pd.Series) -> pd.Series:
    """KDE-mode minus median over 252d."""
    r = _log_ret(close)
    md = _rolling_q(r, YDAYS, 0.5)
    def _km(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        grid = np.linspace(v.min(), v.max(), 41)
        best = grid[0]; best_d = -1.0
        for g in grid:
            z = (v - g) / bw
            d = np.mean(np.exp(-0.5 * z * z)) / (bw * np.sqrt(2.0 * np.pi))
            if d > best_d:
                best_d = d; best = g
        return float(best)
    mode = r.rolling(YDAYS, min_periods=QDAYS).apply(_km, raw=True)
    return (mode - md)

def f51_dsav_120_tail_decay_rate_left_via_q_diff_252d(close: pd.Series) -> pd.Series:
    """(P10 - P05) - (P05 - P01) over 252d - left tail decay curvature."""
    r = _log_ret(close)
    p01 = _rolling_q(r, YDAYS, 0.01); p05 = _rolling_q(r, YDAYS, 0.05)
    p10 = _rolling_q(r, YDAYS, 0.10)
    return ((p10 - p05) - (p05 - p01))

def f51_dsav_121_log_likelihood_normal_log_ret_252d(close: pd.Series) -> pd.Series:
    """Per-bar log-likelihood under fitted Normal over 252d."""
    r = _log_ret(close)
    return (_log_likelihood_normal(r, YDAYS))

def f51_dsav_122_log_likelihood_laplace_log_ret_252d(close: pd.Series) -> pd.Series:
    """Per-bar log-likelihood under fitted Laplace over 252d."""
    r = _log_ret(close)
    return (_log_likelihood_laplace(r, YDAYS))

def f51_dsav_123_log_likelihood_logistic_log_ret_252d(close: pd.Series) -> pd.Series:
    """Per-bar log-likelihood under fitted Logistic (method-of-moments) over 252d."""
    r = _log_ret(close)
    def _llg(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        s = sd * np.sqrt(3.0) / np.pi
        z = (v - mu) / s
        return float(np.mean(-z - np.log(s) - 2.0 * np.log1p(np.exp(-z))))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_llg, raw=True)
    return (res)

def f51_dsav_124_bic_normal_minus_bic_laplace_log_ret_252d(close: pd.Series) -> pd.Series:
    """BIC(Normal) - BIC(Laplace) over 252d (= -2*(LL_n - LL_l) since param counts equal)."""
    r = _log_ret(close)
    lln = _log_likelihood_normal(r, YDAYS)
    lll = _log_likelihood_laplace(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    return (-2.0 * (lln - lll) * n)

def f51_dsav_125_best_fit_distribution_indicator_252d(close: pd.Series) -> pd.Series:
    """0=Normal, 1=Laplace, 2=Logistic if max LL over 252d."""
    r = _log_ret(close)
    lln = _log_likelihood_normal(r, YDAYS)
    lll = _log_likelihood_laplace(r, YDAYS)
    def _llg(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        s = sd * np.sqrt(3.0) / np.pi
        z = (v - mu) / s
        return float(np.mean(-z - np.log(s) - 2.0 * np.log1p(np.exp(-z))))
    llg = r.rolling(YDAYS, min_periods=QDAYS).apply(_llg, raw=True)
    stacked = pd.concat([lln.rename('n'), lll.rename('l'), llg.rename('g')], axis=1)
    name_to_idx = {'n': 0.0, 'l': 1.0, 'g': 2.0}
    best = stacked.fillna(-np.inf).idxmax(axis=1).map(name_to_idx).where(stacked.notna().any(axis=1), np.nan).astype(float)
    return (best.where(stacked.notna().all(axis=1), np.nan))

def f51_dsav_126_relative_likelihood_t_over_normal_log_ret_252d(close: pd.Series) -> pd.Series:
    """Approximate likelihood ratio of fitted-t (df from kurt) vs Normal over 252d."""
    r = _log_ret(close)
    kt = _rolling_kurt(r, YDAYS)
    llr = (1.0 + kt.clip(lower=0.0)) * (-1.0)
    return (llr)

def f51_dsav_127_aic_normal_minus_aic_t_log_ret_252d(close: pd.Series) -> pd.Series:
    """AIC(Normal) - AIC(Student-t df from kurt) over 252d."""
    r = _log_ret(close)
    lln = _log_likelihood_normal(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    df = _fit_t_df_from_kurt(r, YDAYS)
    # Approximate per-bar LL of fitted t: gaussian + heavy-tail correction
    tail_corr = -0.5 * (1.0 - 1.0 / df)
    ll_t = lln + tail_corr
    return (-2.0 * (lln - ll_t) * n + 2.0)

def f51_dsav_128_residual_iqr_after_laplace_fit_252d(close: pd.Series) -> pd.Series:
    """IQR of (r - median)/b residuals after Laplace fit over 252d."""
    r = _log_ret(close)
    med = _rolling_q(r, YDAYS, 0.5)
    b = _fit_laplace_b(r, YDAYS)
    resid = _safe_div(r - med, b)
    return (_rolling_q(resid, YDAYS, 0.75) - _rolling_q(resid, YDAYS, 0.25))

def f51_dsav_129_residual_skew_after_normal_fit_252d(close: pd.Series) -> pd.Series:
    """Skew of (r - mean)/sd residuals over 252d - should be ~0 if Normal."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(r - mu, sd)
    return (_rolling_skew(z, YDAYS))

def f51_dsav_130_residual_kurt_after_normal_fit_252d(close: pd.Series) -> pd.Series:
    """Excess kurt of standardized residuals over 252d - should be ~0 if Normal."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(r - mu, sd)
    return (_rolling_kurt(z, YDAYS))

def f51_dsav_131_fat_tail_composite_score_252d(close: pd.Series) -> pd.Series:
    """Z-sum of |skew|, |excess_kurt|, Hill-tail (5%) over 252d - omnibus fat-tail intensity."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS).abs(); kt = _rolling_kurt(r, YDAYS).abs()
    p99 = _rolling_q(r, YDAYS, 0.99); p01 = _rolling_q(r, YDAYS, 0.01)
    p75 = _rolling_q(r, YDAYS, 0.75); p25 = _rolling_q(r, YDAYS, 0.25)
    tail = _safe_div(p99 - p01, p75 - p25)
    z1 = _rolling_zscore(sk, YDAYS); z2 = _rolling_zscore(kt, YDAYS); z3 = _rolling_zscore(tail, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0))

def f51_dsav_132_blowoff_distribution_signature_252d(close: pd.Series) -> pd.Series:
    """High positive skew * |excess-kurt| * Hill-upper(5%) composite over 252d - blowoff distribution profile."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    kt = _rolling_kurt(r, YDAYS).abs()
    hill = _fit_pareto_alpha_upper(r, YDAYS, 0.05)
    return (sk * kt * hill)

def f51_dsav_133_distribution_complexity_index_252d(close: pd.Series) -> pd.Series:
    """Bimodality coef * (1 + medcouple^2) over 252d - shape complexity."""
    r = _log_ret(close)
    bc = _bimodality_coef(r, YDAYS)
    mc = _medcouple(r, YDAYS)
    return (bc * (1.0 + mc * mc))

def f51_dsav_134_distribution_stability_index_skew_252d(close: pd.Series) -> pd.Series:
    """Rolling 21d std of skew over 252d - skew-of-skew (stability)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    return (sk.rolling(MDAYS, min_periods=10).std())

def f51_dsav_135_distribution_stability_index_kurt_252d(close: pd.Series) -> pd.Series:
    """Rolling 21d std of kurt over 252d."""
    r = _log_ret(close)
    kt = _rolling_kurt(r, YDAYS)
    return (kt.rolling(MDAYS, min_periods=10).std())

def f51_dsav_136_regime_change_indicator_skew_zchange_252d(close: pd.Series) -> pd.Series:
    """|skew_t - skew_{t-21}| > 1.5*std(skew_21d) over 252d - regime-change in skew."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    ch = (sk - sk.shift(MDAYS)).abs()
    sdc = ch.rolling(MDAYS, min_periods=10).std()
    return ((ch > 1.5 * sdc).astype(float).where(sdc.notna(), np.nan))

def f51_dsav_137_moment_consistency_score_252d(close: pd.Series) -> pd.Series:
    """(skew^2 + 1) vs kurt+3 consistency - distance from Bimodality threshold."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS); kt = _rolling_kurt(r, YDAYS)
    return ((sk * sk + 1.0) - 0.555 * (kt + 3.0))

def f51_dsav_138_normality_violation_intensity_score_252d(close: pd.Series) -> pd.Series:
    """Z-sum of JB, AD, KS test stats over 252d - omnibus non-normality intensity."""
    r = _log_ret(close)
    mp = max(YDAYS // 3, 10)
    sk = r.rolling(YDAYS, min_periods=mp).skew()
    kt = r.rolling(YDAYS, min_periods=mp).kurt()
    cnt = r.rolling(YDAYS, min_periods=mp).count()
    jb = (cnt / 6.0) * (sk ** 2 + 0.25 * (kt ** 2))
    cvm = _cramer_von_mises_normal(r, YDAYS)
    wd = _wasserstein_distance_to_normal(r, YDAYS)
    z1 = _rolling_zscore(jb, YDAYS); z2 = _rolling_zscore(cvm, YDAYS); z3 = _rolling_zscore(wd, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0))

def f51_dsav_139_crash_seer_distribution_composite_252d(close: pd.Series) -> pd.Series:
    """Negative medcouple + Hill-lower + downside-only-3rd-moment composite over 252d - left-tail risk distribution."""
    r = _log_ret(close)
    mc = _medcouple(r, YDAYS)
    p01 = _rolling_q(r, YDAYS, 0.01); p25 = _rolling_q(r, YDAYS, 0.25)
    p75 = _rolling_q(r, YDAYS, 0.75); p99 = _rolling_q(r, YDAYS, 0.99)
    tail = _safe_div(p99 - p01, p75 - p25)
    neg_cubed = (r ** 3).where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (-(mc.fillna(0.0)) + tail.fillna(0.0) + (-neg_cubed.fillna(0.0)))

def f51_dsav_140_euphoria_distribution_composite_252d(close: pd.Series) -> pd.Series:
    """Positive medcouple + upside Hill + positive-only 3rd moment over 252d - blowoff-top distribution profile."""
    r = _log_ret(close)
    mc = _medcouple(r, YDAYS)
    hill = _fit_pareto_alpha_upper(r, YDAYS, 0.05)
    pos_cubed = (r ** 3).where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (mc.fillna(0.0) + hill.fillna(0.0) + pos_cubed.fillna(0.0))

def f51_dsav_141_expected_shortfall_minus_normal_es_at_5pct_252d(close: pd.Series) -> pd.Series:
    """Empirical ES(95) minus normal-implied ES at 5% over 252d - non-normality of tails."""
    r = _log_ret(close)
    def _es(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(-tail.mean()) if tail.size > 0 else np.nan
    emp_es = r.rolling(YDAYS, min_periods=QDAYS).apply(_es, raw=True)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean(); sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = _norm_ppf(0.05)
    phi = np.exp(-0.5 * z * z) / np.sqrt(2.0 * np.pi)
    norm_es = -(mu - sd * phi / 0.05)
    return (emp_es - norm_es)

def f51_dsav_142_hartigan_dip_p_value_proxy_252d(close: pd.Series) -> pd.Series:
    """Asymptotic p-value proxy of Hartigan dip = exp(-2*n*dip^2) - p<.05 suggests multimodal."""
    r = _log_ret(close)
    dip = _hartigan_dip(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    return ((-2.0 * n * dip * dip).apply(np.exp))

def f51_dsav_143_amihud_realized_skew_decile_signal_252d(close: pd.Series) -> pd.Series:
    """Mean realized skewness (21d) over the bottom-decile of recent 252d - Amaya 'short-term predictability'."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(MDAYS, min_periods=10).sum()
    r3 = (r ** 3).rolling(MDAYS, min_periods=10).sum()
    cnt = r.rolling(MDAYS, min_periods=10).count()
    rsk = _safe_div(cnt.pow(0.5) * r3, r2.pow(1.5))
    q10 = rsk.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (rsk.where(rsk <= q10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_144_realized_skew_persistence_ar1_63d(close: pd.Series) -> pd.Series:
    """AR(1) of 21d-realized skewness measured over rolling 63d window."""
    r = _log_ret(close)
    r2 = (r ** 2).rolling(MDAYS, min_periods=10).sum()
    r3 = (r ** 3).rolling(MDAYS, min_periods=10).sum()
    cnt = r.rolling(MDAYS, min_periods=10).count()
    rsk = _safe_div(cnt.pow(0.5) * r3, r2.pow(1.5))
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        a = v[:-1]; b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    res = rsk.rolling(QDAYS, min_periods=MDAYS).apply(_ac, raw=True)
    return (res)

def f51_dsav_145_downside_realized_skew_persistence_252d(close: pd.Series) -> pd.Series:
    """Persistence (rolling 21d-correlation) of negative-realized skew over 252d."""
    r = _log_ret(close)
    neg_r3 = (r ** 3).where(r < 0, 0.0).rolling(MDAYS, min_periods=10).sum()
    lag = neg_r3.shift(1)
    return (neg_r3.rolling(YDAYS, min_periods=QDAYS).corr(lag))

def f51_dsav_146_upside_realized_skew_252d_zscore(close: pd.Series) -> pd.Series:
    """Z-score over 252d of upside-realized skew = sum r^3 (r>0) / sum r^2 (r>0)."""
    r = _log_ret(close)
    pos_r2 = (r ** 2).where(r > 0, 0.0).rolling(MDAYS, min_periods=10).sum()
    pos_r3 = (r ** 3).where(r > 0, 0.0).rolling(MDAYS, min_periods=10).sum()
    ups = _safe_div(pos_r3, pos_r2.pow(1.5))
    return (_rolling_zscore(ups, YDAYS))

def f51_dsav_147_skewness_volatility_252d(close: pd.Series) -> pd.Series:
    """Std of skewness measured over 252d (rolling skew over 21d windows then 252d std)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, MDAYS)
    return (sk.rolling(YDAYS, min_periods=QDAYS).std())

def f51_dsav_148_kurtosis_volatility_252d(close: pd.Series) -> pd.Series:
    """Std of kurtosis measured over 252d."""
    r = _log_ret(close)
    kt = _rolling_kurt(r, MDAYS)
    return (kt.rolling(YDAYS, min_periods=QDAYS).std())

def f51_dsav_149_multimodal_persistence_indicator_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252d where KDE mode count > 1."""
    r = _log_ret(close)
    mc = _kde_mode_count(r, QDAYS)
    ind = (mc > 1.5).astype(float).where(mc.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).mean())

def f51_dsav_150_distribution_shape_omnibus_score_252d(close: pd.Series) -> pd.Series:
    """Aggregate z-scored: medcouple + bimodality + Wasserstein-to-normal + Renyi-2 + fat_tail - distribution-shape composite."""
    r = _log_ret(close)
    mc = _medcouple(r, YDAYS)
    bc = _bimodality_coef(r, YDAYS)
    wd = _wasserstein_distance_to_normal(r, YDAYS)
    re2 = _renyi_entropy(r, YDAYS, 2.0)
    z1 = _rolling_zscore(mc.abs(), YDAYS); z2 = _rolling_zscore(bc, YDAYS)
    z3 = _rolling_zscore(wd, YDAYS); z4 = _rolling_zscore(re2, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0) + z4.fillna(0.0))


# ============================================================
#                         REGISTRY 076_150 (base)
# ============================================================

DISTRIBUTION_SHAPE_ADVANCED_BASE_REGISTRY_076_150 = {
    "f51_dsav_076_coskew_tr_with_close_ret_252d": {"inputs": ["high", "low", "close"], "func": f51_dsav_076_coskew_tr_with_close_ret_252d},
    "f51_dsav_077_cokurt_tr_with_close_ret_252d": {"inputs": ["high", "low", "close"], "func": f51_dsav_077_cokurt_tr_with_close_ret_252d},
    "f51_dsav_078_cross_moment_r_log_volume_252d": {"inputs": ["close", "volume"], "func": f51_dsav_078_cross_moment_r_log_volume_252d},
    "f51_dsav_079_cross_moment_r_log_volume_change_252d": {"inputs": ["close", "volume"], "func": f51_dsav_079_cross_moment_r_log_volume_change_252d},
    "f51_dsav_080_cross_moment_absr_log_volume_252d": {"inputs": ["close", "volume"], "func": f51_dsav_080_cross_moment_absr_log_volume_252d},
    "f51_dsav_081_mean_log_ret_above_mean_252d": {"inputs": ["close"], "func": f51_dsav_081_mean_log_ret_above_mean_252d},
    "f51_dsav_082_mean_log_ret_below_mean_252d": {"inputs": ["close"], "func": f51_dsav_082_mean_log_ret_below_mean_252d},
    "f51_dsav_083_var_log_ret_above_mean_252d": {"inputs": ["close"], "func": f51_dsav_083_var_log_ret_above_mean_252d},
    "f51_dsav_084_var_log_ret_below_mean_252d": {"inputs": ["close"], "func": f51_dsav_084_var_log_ret_below_mean_252d},
    "f51_dsav_085_ratio_upside_to_downside_var_252d": {"inputs": ["close"], "func": f51_dsav_085_ratio_upside_to_downside_var_252d},
    "f51_dsav_086_mean_log_ret_after_neg_252d": {"inputs": ["close"], "func": f51_dsav_086_mean_log_ret_after_neg_252d},
    "f51_dsav_087_mean_log_ret_after_pos_252d": {"inputs": ["close"], "func": f51_dsav_087_mean_log_ret_after_pos_252d},
    "f51_dsav_088_vol_log_ret_after_neg_252d": {"inputs": ["close"], "func": f51_dsav_088_vol_log_ret_after_neg_252d},
    "f51_dsav_089_vol_log_ret_after_pos_252d": {"inputs": ["close"], "func": f51_dsav_089_vol_log_ret_after_pos_252d},
    "f51_dsav_090_ratio_vol_after_neg_to_pos_252d": {"inputs": ["close"], "func": f51_dsav_090_ratio_vol_after_neg_to_pos_252d},
    "f51_dsav_091_realized_skewness_21d_amaya_log_ret": {"inputs": ["close"], "func": f51_dsav_091_realized_skewness_21d_amaya_log_ret},
    "f51_dsav_092_realized_kurtosis_21d_amaya_log_ret": {"inputs": ["close"], "func": f51_dsav_092_realized_kurtosis_21d_amaya_log_ret},
    "f51_dsav_093_realized_skewness_63d_amaya_log_ret": {"inputs": ["close"], "func": f51_dsav_093_realized_skewness_63d_amaya_log_ret},
    "f51_dsav_094_realized_kurtosis_63d_amaya_log_ret": {"inputs": ["close"], "func": f51_dsav_094_realized_kurtosis_63d_amaya_log_ret},
    "f51_dsav_095_signed_jump_variation_63d_log_ret": {"inputs": ["close"], "func": f51_dsav_095_signed_jump_variation_63d_log_ret},
    "f51_dsav_096_signed_jump_variation_252d_log_ret": {"inputs": ["close"], "func": f51_dsav_096_signed_jump_variation_252d_log_ret},
    "f51_dsav_097_realized_negative_semivariance_63d_log_ret": {"inputs": ["close"], "func": f51_dsav_097_realized_negative_semivariance_63d_log_ret},
    "f51_dsav_098_realized_positive_semivariance_63d_log_ret": {"inputs": ["close"], "func": f51_dsav_098_realized_positive_semivariance_63d_log_ret},
    "f51_dsav_099_realized_semivariance_diff_neg_minus_pos_252d": {"inputs": ["close"], "func": f51_dsav_099_realized_semivariance_diff_neg_minus_pos_252d},
    "f51_dsav_100_realized_skew_jumps_decomp_63d": {"inputs": ["close"], "func": f51_dsav_100_realized_skew_jumps_decomp_63d},
    "f51_dsav_101_rousseeuw_croux_sn_proxy_252d": {"inputs": ["close"], "func": f51_dsav_101_rousseeuw_croux_sn_proxy_252d},
    "f51_dsav_102_rousseeuw_croux_qn_proxy_252d": {"inputs": ["close"], "func": f51_dsav_102_rousseeuw_croux_qn_proxy_252d},
    "f51_dsav_103_biweight_midvariance_252d": {"inputs": ["close"], "func": f51_dsav_103_biweight_midvariance_252d},
    "f51_dsav_104_biweight_midcorrelation_with_lag1_252d": {"inputs": ["close"], "func": f51_dsav_104_biweight_midcorrelation_with_lag1_252d},
    "f51_dsav_105_scale_ratio_qn_to_sd_252d": {"inputs": ["close"], "func": f51_dsav_105_scale_ratio_qn_to_sd_252d},
    "f51_dsav_106_scale_ratio_mad_to_sd_252d": {"inputs": ["close"], "func": f51_dsav_106_scale_ratio_mad_to_sd_252d},
    "f51_dsav_107_scale_ratio_iqr_normal_to_sd_252d": {"inputs": ["close"], "func": f51_dsav_107_scale_ratio_iqr_normal_to_sd_252d},
    "f51_dsav_108_m_estimator_huber_scale_252d": {"inputs": ["close"], "func": f51_dsav_108_m_estimator_huber_scale_252d},
    "f51_dsav_109_midhinge_dispersion_p15_p85_252d": {"inputs": ["close"], "func": f51_dsav_109_midhinge_dispersion_p15_p85_252d},
    "f51_dsav_110_octile_dispersion_e7_minus_e1_252d": {"inputs": ["close"], "func": f51_dsav_110_octile_dispersion_e7_minus_e1_252d},
    "f51_dsav_111_kde_left_tail_density_at_p05_252d": {"inputs": ["close"], "func": f51_dsav_111_kde_left_tail_density_at_p05_252d},
    "f51_dsav_112_kde_right_tail_density_at_p95_252d": {"inputs": ["close"], "func": f51_dsav_112_kde_right_tail_density_at_p95_252d},
    "f51_dsav_113_tail_asymmetry_p05_minus_p95_density_252d": {"inputs": ["close"], "func": f51_dsav_113_tail_asymmetry_p05_minus_p95_density_252d},
    "f51_dsav_114_p99_minus_p95_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_114_p99_minus_p95_log_ret_252d},
    "f51_dsav_115_p05_minus_p01_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_115_p05_minus_p01_log_ret_252d},
    "f51_dsav_116_ratio_extreme_spread_left_to_right_252d": {"inputs": ["close"], "func": f51_dsav_116_ratio_extreme_spread_left_to_right_252d},
    "f51_dsav_117_kde_mode_value_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_117_kde_mode_value_log_ret_252d},
    "f51_dsav_118_kde_mode_minus_mean_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_118_kde_mode_minus_mean_log_ret_252d},
    "f51_dsav_119_kde_mode_minus_median_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_119_kde_mode_minus_median_log_ret_252d},
    "f51_dsav_120_tail_decay_rate_left_via_q_diff_252d": {"inputs": ["close"], "func": f51_dsav_120_tail_decay_rate_left_via_q_diff_252d},
    "f51_dsav_121_log_likelihood_normal_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_121_log_likelihood_normal_log_ret_252d},
    "f51_dsav_122_log_likelihood_laplace_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_122_log_likelihood_laplace_log_ret_252d},
    "f51_dsav_123_log_likelihood_logistic_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_123_log_likelihood_logistic_log_ret_252d},
    "f51_dsav_124_bic_normal_minus_bic_laplace_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_124_bic_normal_minus_bic_laplace_log_ret_252d},
    "f51_dsav_125_best_fit_distribution_indicator_252d": {"inputs": ["close"], "func": f51_dsav_125_best_fit_distribution_indicator_252d},
    "f51_dsav_126_relative_likelihood_t_over_normal_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_126_relative_likelihood_t_over_normal_log_ret_252d},
    "f51_dsav_127_aic_normal_minus_aic_t_log_ret_252d": {"inputs": ["close"], "func": f51_dsav_127_aic_normal_minus_aic_t_log_ret_252d},
    "f51_dsav_128_residual_iqr_after_laplace_fit_252d": {"inputs": ["close"], "func": f51_dsav_128_residual_iqr_after_laplace_fit_252d},
    "f51_dsav_129_residual_skew_after_normal_fit_252d": {"inputs": ["close"], "func": f51_dsav_129_residual_skew_after_normal_fit_252d},
    "f51_dsav_130_residual_kurt_after_normal_fit_252d": {"inputs": ["close"], "func": f51_dsav_130_residual_kurt_after_normal_fit_252d},
    "f51_dsav_131_fat_tail_composite_score_252d": {"inputs": ["close"], "func": f51_dsav_131_fat_tail_composite_score_252d},
    "f51_dsav_132_blowoff_distribution_signature_252d": {"inputs": ["close"], "func": f51_dsav_132_blowoff_distribution_signature_252d},
    "f51_dsav_133_distribution_complexity_index_252d": {"inputs": ["close"], "func": f51_dsav_133_distribution_complexity_index_252d},
    "f51_dsav_134_distribution_stability_index_skew_252d": {"inputs": ["close"], "func": f51_dsav_134_distribution_stability_index_skew_252d},
    "f51_dsav_135_distribution_stability_index_kurt_252d": {"inputs": ["close"], "func": f51_dsav_135_distribution_stability_index_kurt_252d},
    "f51_dsav_136_regime_change_indicator_skew_zchange_252d": {"inputs": ["close"], "func": f51_dsav_136_regime_change_indicator_skew_zchange_252d},
    "f51_dsav_137_moment_consistency_score_252d": {"inputs": ["close"], "func": f51_dsav_137_moment_consistency_score_252d},
    "f51_dsav_138_normality_violation_intensity_score_252d": {"inputs": ["close"], "func": f51_dsav_138_normality_violation_intensity_score_252d},
    "f51_dsav_139_crash_seer_distribution_composite_252d": {"inputs": ["close"], "func": f51_dsav_139_crash_seer_distribution_composite_252d},
    "f51_dsav_140_euphoria_distribution_composite_252d": {"inputs": ["close"], "func": f51_dsav_140_euphoria_distribution_composite_252d},
    "f51_dsav_141_expected_shortfall_minus_normal_es_at_5pct_252d": {"inputs": ["close"], "func": f51_dsav_141_expected_shortfall_minus_normal_es_at_5pct_252d},
    "f51_dsav_142_hartigan_dip_p_value_proxy_252d": {"inputs": ["close"], "func": f51_dsav_142_hartigan_dip_p_value_proxy_252d},
    "f51_dsav_143_amihud_realized_skew_decile_signal_252d": {"inputs": ["close"], "func": f51_dsav_143_amihud_realized_skew_decile_signal_252d},
    "f51_dsav_144_realized_skew_persistence_ar1_63d": {"inputs": ["close"], "func": f51_dsav_144_realized_skew_persistence_ar1_63d},
    "f51_dsav_145_downside_realized_skew_persistence_252d": {"inputs": ["close"], "func": f51_dsav_145_downside_realized_skew_persistence_252d},
    "f51_dsav_146_upside_realized_skew_252d_zscore": {"inputs": ["close"], "func": f51_dsav_146_upside_realized_skew_252d_zscore},
    "f51_dsav_147_skewness_volatility_252d": {"inputs": ["close"], "func": f51_dsav_147_skewness_volatility_252d},
    "f51_dsav_148_kurtosis_volatility_252d": {"inputs": ["close"], "func": f51_dsav_148_kurtosis_volatility_252d},
    "f51_dsav_149_multimodal_persistence_indicator_252d": {"inputs": ["close"], "func": f51_dsav_149_multimodal_persistence_indicator_252d},
    "f51_dsav_150_distribution_shape_omnibus_score_252d": {"inputs": ["close"], "func": f51_dsav_150_distribution_shape_omnibus_score_252d},
}
