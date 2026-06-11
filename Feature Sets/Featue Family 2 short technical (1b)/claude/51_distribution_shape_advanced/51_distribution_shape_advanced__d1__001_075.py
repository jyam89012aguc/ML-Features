"""distribution_shape_advanced d1 features 001-075 - Pipeline 1b-technical.

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


def f51_dsav_001_bimodality_coef_pearson_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Pearson bimodality coefficient (skew^2+1)/(kurt+3+correction) over 63d - >0.555 suggests bimodal."""
    r = _log_ret(close)
    return (_bimodality_coef(r, QDAYS)).diff()

def f51_dsav_002_bimodality_coef_pearson_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pearson bimodality coefficient over 252d."""
    r = _log_ret(close)
    return (_bimodality_coef(r, YDAYS)).diff()

def f51_dsav_003_hartigan_dip_stat_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Hartigan dip statistic on 252d log-returns - low values = unimodal, high = multimodal."""
    r = _log_ret(close)
    return (_hartigan_dip(r, YDAYS)).diff()

def f51_dsav_004_hartigan_dip_stat_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Hartigan dip statistic over 504d."""
    r = _log_ret(close)
    return (_hartigan_dip(r, DDAYS_2Y)).diff()

def f51_dsav_005_kde_mode_count_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Number of local maxima in a smoothed histogram of 252d log-returns."""
    r = _log_ret(close)
    return (_kde_mode_count(r, YDAYS)).diff()

def f51_dsav_006_kde_mode_count_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Number of local maxima in 504d log-return histogram."""
    r = _log_ret(close)
    return (_kde_mode_count(r, DDAYS_2Y)).diff()

def f51_dsav_007_multimodality_binary_indicator_252d_d1(close: pd.Series) -> pd.Series:
    """Indicator: KDE mode count > 1 over 252d log-returns."""
    r = _log_ret(close)
    mc = _kde_mode_count(r, YDAYS)
    return ((mc > 1.5).astype(float).where(mc.notna(), np.nan)).diff()

def f51_dsav_008_bimodality_excess_above_threshold_252d_d1(close: pd.Series) -> pd.Series:
    """Excess of bimodality coefficient above the 0.555 unimodal threshold over 252d."""
    r = _log_ret(close)
    bc = _bimodality_coef(r, YDAYS)
    return (bc - 0.555).diff()

def f51_dsav_009_dagostino_K2_omnibus_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """D'Agostino-Pearson K^2 = Z_skew^2 + Z_kurt^2 omnibus normality test over 252d."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS); kt = _rolling_kurt(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    z_sk = sk / (6.0 / n).pow(0.5)
    z_kt = kt / (24.0 / n).pow(0.5)
    return (z_sk ** 2 + z_kt ** 2).diff()

def f51_dsav_010_dagostino_skewness_z_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """D'Agostino skewness z-stat over 252d = skew / sqrt(6/n)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    return (sk / (6.0 / n).pow(0.5)).diff()

def f51_dsav_011_hodges_lehmann_mean_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Hodges-Lehmann robust mean = median of pairwise averages of 252d log-returns."""
    r = _log_ret(close)
    return (_hodges_lehmann(r, YDAYS)).diff()

def f51_dsav_012_hodges_lehmann_mean_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Hodges-Lehmann mean over 63d."""
    r = _log_ret(close)
    return (_hodges_lehmann(r, QDAYS)).diff()

def f51_dsav_013_trimean_tukey_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Tukey trimean (Q1+2*Q2+Q3)/4 of 252d log-returns."""
    r = _log_ret(close)
    return (_trimean_tukey(r, YDAYS)).diff()

def f51_dsav_014_midhinge_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Midhinge (Q1+Q3)/2 of 252d log-returns."""
    r = _log_ret(close)
    return (_midhinge(r, YDAYS)).diff()

def f51_dsav_015_shorth_mean_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of shortest 50% interval (shorth) of 252d log-returns."""
    r = _log_ret(close)
    return (_shorth_mean(r, YDAYS, 0.5)).diff()

def f51_dsav_016_m_estimator_huber_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Huber M-estimator (c=1.345) of 252d log-returns."""
    r = _log_ret(close)
    return (_m_estimator_huber(r, YDAYS, 1.345)).diff()

def f51_dsav_017_mean_minus_hodges_lehmann_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean minus Hodges-Lehmann mean over 252d - asymmetry diagnostic."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    hl = _hodges_lehmann(r, YDAYS)
    return (mu - hl).diff()

def f51_dsav_018_mean_minus_trimean_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean minus Tukey trimean over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    tm = _trimean_tukey(r, YDAYS)
    return (mu - tm).diff()

def f51_dsav_019_midhinge_minus_median_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Midhinge minus median over 252d - quartile-asymmetry diagnostic."""
    r = _log_ret(close)
    mh = _midhinge(r, YDAYS)
    md = _rolling_q(r, YDAYS, 0.5)
    return (mh - md).diff()

def f51_dsav_020_shorth_mean_minus_median_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Shorth (shortest 50% interval) mean minus median over 252d."""
    r = _log_ret(close)
    sh = _shorth_mean(r, YDAYS, 0.5)
    md = _rolling_q(r, YDAYS, 0.5)
    return (sh - md).diff()

def f51_dsav_021_medcouple_brys_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Brys-Hubert-Struyf medcouple skewness in [-1, 1] over 252d - robust skew."""
    r = _log_ret(close)
    return (_medcouple(r, YDAYS)).diff()

def f51_dsav_022_medcouple_brys_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Medcouple skewness over 504d."""
    r = _log_ret(close)
    return (_medcouple(r, DDAYS_2Y)).diff()

def f51_dsav_023_hogg_robust_skew_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Hogg robust skewness = ((U05-U50) - (L50-L05)) / (U50-L50) over 252d."""
    r = _log_ret(close)
    return (_hogg_robust_skew(r, YDAYS)).diff()

def f51_dsav_024_groeneveld_meeden_skew_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Groeneveld-Meeden skew = (mean-median)/E|x-median| over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    md = _rolling_q(r, YDAYS, 0.5)
    abs_dev = (r - md).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(mu - md, abs_dev)).diff()

def f51_dsav_025_pearson_2nd_skew_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pearson 2nd skewness = 3*(mean-median)/std over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    md = _rolling_q(r, YDAYS, 0.5)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (3.0 * _safe_div(mu - md, sd)).diff()

def f51_dsav_026_octile_skew_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Octile skew = (E7 + E1 - 2*E4) / (E7 - E1) over 252d (E_k = k-th octile)."""
    r = _log_ret(close)
    e1 = _rolling_q(r, YDAYS, 0.125)
    e4 = _rolling_q(r, YDAYS, 0.500)
    e7 = _rolling_q(r, YDAYS, 0.875)
    return (_safe_div(e7 + e1 - 2.0 * e4, e7 - e1)).diff()

def f51_dsav_027_galton_yule_skew_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Galton-Yule skew = (Q3 - 2*Q2 + Q1) / (Q3 - Q1) over 252d - signed Bowley alternative."""
    r = _log_ret(close)
    q1 = _rolling_q(r, YDAYS, 0.25); q2 = _rolling_q(r, YDAYS, 0.5)
    q3 = _rolling_q(r, YDAYS, 0.75)
    return (_safe_div(q3 - 2.0 * q2 + q1, q3 - q1)).diff()

def f51_dsav_028_kelly_skew_p10_p90_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Kelly's measure of skewness using P10/P50/P90 over 252d."""
    r = _log_ret(close)
    p10 = _rolling_q(r, YDAYS, 0.10)
    p50 = _rolling_q(r, YDAYS, 0.5)
    p90 = _rolling_q(r, YDAYS, 0.90)
    return (_safe_div((p90 - p50) - (p50 - p10), p90 - p10)).diff()

def f51_dsav_029_conditional_tail_imbalance_one_sigma_252d_d1(close: pd.Series) -> pd.Series:
    """E[r | r < -sigma] + E[r | r > +sigma] (sum, not diff) over 252d - tail-imbalance."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    lo = r.where(r < -sd, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    hi = r.where(r > sd, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (lo + hi).diff()

def f51_dsav_030_right_minus_left_tail_centroid_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of returns above 95th-pct minus magnitude of returns below 5th-pct over 252d."""
    r = _log_ret(close)
    thrh = _rolling_q(r, YDAYS, 0.95)
    thrl = _rolling_q(r, YDAYS, 0.05)
    hi = r.where(r >= thrh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    lo = r.where(r <= thrl, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (hi - (-lo)).diff()

def f51_dsav_031_crow_siddiqui_kurt_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Crow-Siddiqui robust kurtosis = (P975-P025)/(P75-P25) over 252d."""
    r = _log_ret(close)
    return (_crow_siddiqui_kurt(r, YDAYS)).diff()

def f51_dsav_032_hogg_kurt_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Hogg kurtosis = (U05-L05) / (U50-L50) over 252d."""
    r = _log_ret(close)
    return (_hogg_kurt(r, YDAYS)).diff()

def f51_dsav_033_moors_octile_kurt_extended_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Moors octile kurt using deeper octiles ((E7-E5)+(E3-E1))/(E6-E2) - already in 41; use deeper levels here."""
    r = _log_ret(close)
    p125 = _rolling_q(r, YDAYS, 0.125); p375 = _rolling_q(r, YDAYS, 0.375)
    p625 = _rolling_q(r, YDAYS, 0.625); p875 = _rolling_q(r, YDAYS, 0.875)
    p25 = _rolling_q(r, YDAYS, 0.25); p75 = _rolling_q(r, YDAYS, 0.75)
    return (_safe_div((p875 - p625) + (p375 - p125), p75 - p25)).diff()

def f51_dsav_034_percentile_kurt_p99_p01_to_iqr_252d_d1(close: pd.Series) -> pd.Series:
    """(P99 - P01) / (P75 - P25) over 252d - extreme-tail vs body ratio."""
    r = _log_ret(close)
    p99 = _rolling_q(r, YDAYS, 0.99); p01 = _rolling_q(r, YDAYS, 0.01)
    p75 = _rolling_q(r, YDAYS, 0.75); p25 = _rolling_q(r, YDAYS, 0.25)
    return (_safe_div(p99 - p01, p75 - p25)).diff()

def f51_dsav_035_tail_to_center_kurt_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """Std of returns in |z|>1.5 vs std in |z|<=1.5 over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    z = (r - mu) / sd.replace(0, np.nan)
    tail = r.where(z.abs() > 1.5, np.nan).rolling(YDAYS, min_periods=QDAYS).std()
    core = r.where(z.abs() <= 1.5, np.nan).rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(tail, core)).diff()

def f51_dsav_036_excess_mass_tails_above_1sigma_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of |r| > 1 sigma over 252d minus 0.317 (normal-expected)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    over1 = (r.abs() > sd).astype(float).where(sd.notna(), np.nan)
    rate = over1.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rate - 0.317).diff()

def f51_dsav_037_excess_mass_tails_above_2sigma_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of |r| > 2 sigma over 252d minus 0.0455 (normal-expected)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    over2 = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    rate = over2.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rate - 0.0455).diff()

def f51_dsav_038_excess_mass_central_within_half_sigma_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of |r| < 0.5 sigma over 252d minus 0.383 (normal-expected)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    core = (r.abs() < 0.5 * sd).astype(float).where(sd.notna(), np.nan)
    rate = core.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rate - 0.383).diff()

def f51_dsav_039_ratio_iqr_to_p90_minus_p10_252d_d1(close: pd.Series) -> pd.Series:
    """(P75-P25) / (P90-P10) over 252d - body vs body-+-tail spread."""
    r = _log_ret(close)
    p75 = _rolling_q(r, YDAYS, 0.75); p25 = _rolling_q(r, YDAYS, 0.25)
    p90 = _rolling_q(r, YDAYS, 0.90); p10 = _rolling_q(r, YDAYS, 0.10)
    return (_safe_div(p75 - p25, p90 - p10)).diff()

def f51_dsav_040_ratio_p95_minus_p5_to_iqr_252d_d1(close: pd.Series) -> pd.Series:
    """(P95-P5) / (P75-P25) over 252d - tail spread vs body."""
    r = _log_ret(close)
    p95 = _rolling_q(r, YDAYS, 0.95); p5 = _rolling_q(r, YDAYS, 0.05)
    p75 = _rolling_q(r, YDAYS, 0.75); p25 = _rolling_q(r, YDAYS, 0.25)
    return (_safe_div(p95 - p5, p75 - p25)).diff()

def f51_dsav_041_fit_laplace_scale_b_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Laplace MLE scale b = mean(|x - median|) over 252d."""
    r = _log_ret(close)
    return (_fit_laplace_b(r, YDAYS)).diff()

def f51_dsav_042_fit_logistic_scale_s_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Logistic MLE scale s = std * sqrt(3)/pi over 252d (method of moments)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (sd * np.sqrt(3.0) / np.pi).diff()

def f51_dsav_043_fit_t_distribution_df_via_kurt_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t df implied by sample excess kurtosis over 252d (df=4+6/k, clipped 3-100)."""
    r = _log_ret(close)
    return (_fit_t_df_from_kurt(r, YDAYS)).diff()

def f51_dsav_044_fit_skewnormal_lambda_pewsey_252d_d1(close: pd.Series) -> pd.Series:
    """Skew-normal shape lambda via Pewsey moment-based approx over 252d."""
    r = _log_ret(close)
    return (_fit_skewnormal_lambda(r, YDAYS)).diff()

def f51_dsav_045_fit_gumbel_mu_from_losses_252d_d1(close: pd.Series) -> pd.Series:
    """Gumbel location mu from block-minimum daily losses over 252d (Euler-Mascheroni adj)."""
    r = _log_ret(close)
    mn = r.rolling(21, min_periods=10).min()
    mu = mn.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = mn.rolling(YDAYS, min_periods=QDAYS).std()
    return ((-mu) - 0.5772 * sd * np.sqrt(6.0) / np.pi).diff()

def f51_dsav_046_fit_gumbel_beta_from_losses_252d_d1(close: pd.Series) -> pd.Series:
    """Gumbel scale beta from block-minimum losses over 252d (= sd*sqrt(6)/pi)."""
    r = _log_ret(close)
    mn = r.rolling(21, min_periods=10).min()
    sd = mn.rolling(YDAYS, min_periods=QDAYS).std()
    return (sd * np.sqrt(6.0) / np.pi).diff()

def f51_dsav_047_fit_pareto_alpha_upper_5pct_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pareto alpha (Hill) on top 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_fit_pareto_alpha_upper(r, YDAYS, 0.05)).diff()

def f51_dsav_048_fit_pareto_alpha_upper_10pct_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Pareto alpha on top 10% of log-returns over 252d."""
    r = _log_ret(close)
    return (_fit_pareto_alpha_upper(r, YDAYS, 0.10)).diff()

def f51_dsav_049_fit_weibull_shape_from_pos_returns_252d_d1(close: pd.Series) -> pd.Series:
    """Weibull shape k via method-of-moments from positive log-returns over 252d (k ~ (mu/sd)^1.086)."""
    r = _log_ret(close).where(_log_ret(close) > 0, np.nan)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(mu, sd).pow(1.086)).diff()

def f51_dsav_050_ratio_laplace_to_normal_scale_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Laplace b * sqrt(2) divided by sd (=1 for normal, >1 for heavy-tail) over 252d."""
    r = _log_ret(close)
    b = _fit_laplace_b(r, YDAYS)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(b * np.sqrt(2.0), sd)).diff()

def f51_dsav_051_cramer_von_mises_to_normal_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cramer-von Mises distance to fitted Normal over 252d."""
    r = _log_ret(close)
    return (_cramer_von_mises_normal(r, YDAYS)).diff()

def f51_dsav_052_cramer_von_mises_to_normal_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """CvM distance over 63d."""
    r = _log_ret(close)
    return (_cramer_von_mises_normal(r, QDAYS)).diff()

def f51_dsav_053_wasserstein_to_normal_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """1-Wasserstein (earth-mover) distance to fitted Normal over 252d."""
    r = _log_ret(close)
    return (_wasserstein_distance_to_normal(r, YDAYS)).diff()

def f51_dsav_054_hellinger_to_normal_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Hellinger distance between binned empirical PDF and fitted Normal over 252d."""
    r = _log_ret(close)
    return (_hellinger_distance_to_normal(r, YDAYS)).diff()

def f51_dsav_055_bhattacharyya_to_normal_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Bhattacharyya distance to fitted Normal over 252d (= -log of overlap)."""
    r = _log_ret(close)
    def _bh(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        mu = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        bw = edges[1] - edges[0]
        p_emp, _ = np.histogram(v, bins=edges, density=True)
        mids = 0.5 * (edges[:-1] + edges[1:])
        p_norm = (1.0 / (sd * np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * ((mids - mu) / sd) ** 2)
        bc = float(np.sum(np.sqrt(np.maximum(p_emp, 0.0) * np.maximum(p_norm, 0.0))) * bw)
        if bc <= 0 or bc > 1.0:
            return np.nan
        return float(-np.log(bc))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_bh, raw=True)
    return (res).diff()

def f51_dsav_056_kl_divergence_to_laplace_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """KL(empirical || fitted Laplace) over 252d."""
    r = _log_ret(close)
    def _kl(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        med = float(np.median(v)); b = float(np.mean(np.abs(v - med)))
        if b <= 0:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        bw = edges[1] - edges[0]
        p_emp, _ = np.histogram(v, bins=edges, density=True)
        mids = 0.5 * (edges[:-1] + edges[1:])
        p_lap = (1.0 / (2.0 * b)) * np.exp(-np.abs(mids - med) / b)
        mask = (p_emp > 0) & (p_lap > 0)
        return float(np.sum(p_emp[mask] * np.log(p_emp[mask] / p_lap[mask])) * bw)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_kl, raw=True)
    return (res).diff()

def f51_dsav_057_ks_distance_to_laplace_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Kolmogorov-Smirnov distance to fitted Laplace over 252d."""
    r = _log_ret(close)
    def _ks(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        med = float(np.median(v)); b = float(np.mean(np.abs(v - med)))
        if b <= 0:
            return np.nan
        v = np.sort(v)
        cdf = np.where(v < med, 0.5 * np.exp((v - med) / b), 1.0 - 0.5 * np.exp(-(v - med) / b))
        ec = np.arange(1, v.size + 1, dtype=float) / v.size
        return float(np.max(np.abs(cdf - ec)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ks, raw=True)
    return (res).diff()

def f51_dsav_058_normal_minus_laplace_loglik_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Log-likelihood gap: LL(Normal) - LL(Laplace) over 252d (negative = Laplace preferred)."""
    r = _log_ret(close)
    lln = _log_likelihood_normal(r, YDAYS)
    lll = _log_likelihood_laplace(r, YDAYS)
    return (lln - lll).diff()

def f51_dsav_059_aic_normal_minus_aic_laplace_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """AIC(Normal) - AIC(Laplace) = -2*(LL_n - LL_l) over 252d."""
    r = _log_ret(close)
    lln = _log_likelihood_normal(r, YDAYS)
    lll = _log_likelihood_laplace(r, YDAYS)
    n = r.rolling(YDAYS, min_periods=QDAYS).count()
    return (-2.0 * (lln - lll) * n).diff()

def f51_dsav_060_residual_normality_after_loc_scale_fit_252d_d1(close: pd.Series) -> pd.Series:
    """Residual normality (Cramer-von Mises) after subtracting fitted Laplace location-scale over 252d."""
    r = _log_ret(close)
    med = _rolling_q(r, YDAYS, 0.5)
    b = _fit_laplace_b(r, YDAYS)
    resid = _safe_div(r - med, b)
    return (_cramer_von_mises_normal(resid, YDAYS)).diff()

def f51_dsav_061_renyi_entropy_q2_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Renyi-2 entropy of binned 252d log-returns - collision-entropy variant."""
    r = _log_ret(close)
    return (_renyi_entropy(r, YDAYS, 2.0)).diff()

def f51_dsav_062_renyi_entropy_q3_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Renyi-3 entropy over 252d - higher-order generalization."""
    r = _log_ret(close)
    return (_renyi_entropy(r, YDAYS, 3.0)).diff()

def f51_dsav_063_renyi_entropy_qhalf_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Renyi-1/2 entropy over 252d - Hartley-like (more sensitive to rare events)."""
    r = _log_ret(close)
    return (_renyi_entropy(r, YDAYS, 0.5)).diff()

def f51_dsav_064_tsallis_entropy_q3_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Tsallis-3 entropy of binned 252d log-returns (= (1 - sum p^3)/2)."""
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
        return float((1.0 - (p ** 3).sum()) / 2.0)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)
    return (res).diff()

def f51_dsav_065_entropy_relative_to_uniform_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Empirical Shannon entropy / log(bins) over 252d - 1.0 = uniform."""
    r = _log_ret(close)
    def _re(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        edges = np.linspace(v.min(), v.max(), 21)
        if edges[-1] <= edges[0]:
            return 1.0
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        H = -(p * np.log(p)).sum()
        return float(H / np.log(len(p))) if len(p) > 1 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_re, raw=True)
    return (res).diff()

def f51_dsav_066_conditional_entropy_log_ret_given_sign_252d_d1(close: pd.Series) -> pd.Series:
    """Entropy of binned log-returns given prior-bar sign over 252d."""
    r = _log_ret(close)
    def _ce(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        sg = np.sign(v[:-1])
        fut = v[1:]
        edges = np.linspace(fut.min(), fut.max(), 21)
        if edges[-1] <= edges[0]:
            return 0.0
        H = 0.0
        for s_val in (-1, 1):
            sub = fut[sg == s_val]
            if sub.size < 5:
                continue
            h, _ = np.histogram(sub, bins=edges)
            p = h.astype(float) / h.sum()
            p = p[p > 0]
            ent = -(p * np.log(p)).sum()
            H += (sub.size / fut.size) * ent
        return float(H)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ce, raw=True)
    return (res).diff()

def f51_dsav_067_joint_entropy_r_and_absr_252d_d1(close: pd.Series) -> pd.Series:
    """Joint Shannon entropy of (binned r, binned |r|) over 252d."""
    r = _log_ret(close)
    x = _log_ret(close).abs()
    def _je(w):
        n = w.shape[0]
        if n < 50:
            return np.nan
        ra = w[:, 0]; xa = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(xa)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; xa = xa[valid]
        H, _, _ = np.histogram2d(ra, xa, bins=10)
        p = H / H.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    df = pd.concat([r.rename('r'), x.rename('x')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _je(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f51_dsav_068_mutual_info_r_with_absr_252d_d1(close: pd.Series) -> pd.Series:
    """Mutual information between r and |r| over 252d (vol-asymmetry coupling)."""
    r = _log_ret(close)
    x = _log_ret(close).abs()
    def _mi(w):
        n = w.shape[0]
        if n < 50:
            return np.nan
        ra = w[:, 0]; xa = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(xa)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; xa = xa[valid]
        H, _, _ = np.histogram2d(ra, xa, bins=10)
        P = H / H.sum()
        Pr = P.sum(axis=1); Px = P.sum(axis=0)
        mi = 0.0
        for i in range(10):
            for j in range(10):
                if P[i, j] > 0 and Pr[i] > 0 and Px[j] > 0:
                    mi += P[i, j] * np.log(P[i, j] / (Pr[i] * Px[j]))
        return float(mi)
    df = pd.concat([r.rename('r'), x.rename('x')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _mi(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f51_dsav_069_kde_differential_entropy_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """KDE-based differential entropy of 252d log-returns (Silverman bandwidth proxy)."""
    r = _log_ret(close)
    def _de(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        bw = 1.06 * sd * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        edges = np.linspace(v.min() - bw, v.max() + bw, 41)
        mids = 0.5 * (edges[:-1] + edges[1:])
        pdf = np.zeros_like(mids)
        for vi in v:
            pdf += np.exp(-0.5 * ((mids - vi) / bw) ** 2)
        pdf /= (v.size * bw * np.sqrt(2.0 * np.pi))
        p = pdf[pdf > 0]
        return float(-np.sum(p * np.log(p)) * (edges[1] - edges[0]))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_de, raw=True)
    return (res).diff()

def f51_dsav_070_negentropy_kde_minus_gaussian_252d_d1(close: pd.Series) -> pd.Series:
    """KDE-based differential entropy minus Gaussian entropy 0.5*log(2*pi*e*var) over 252d - non-Gaussianity."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    def _de(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        s2 = v.var()
        if s2 <= 0:
            return np.nan
        sigma = np.sqrt(s2)
        bw = 1.06 * sigma * v.size ** (-1.0 / 5.0)
        if bw <= 0:
            return np.nan
        edges = np.linspace(v.min() - bw, v.max() + bw, 41)
        mids = 0.5 * (edges[:-1] + edges[1:])
        pdf = np.zeros_like(mids)
        for vi in v:
            pdf += np.exp(-0.5 * ((mids - vi) / bw) ** 2)
        pdf /= (v.size * bw * np.sqrt(2.0 * np.pi))
        p = pdf[pdf > 0]
        return float(-np.sum(p * np.log(p)) * (edges[1] - edges[0]))
    de = r.rolling(YDAYS, min_periods=QDAYS).apply(_de, raw=True)
    gent = 0.5 * np.log(2.0 * np.pi * np.e * (sd ** 2).replace(0, np.nan))
    return (gent - de).diff()

def f51_dsav_071_coskew_r_with_lag1_rsq_252d_d1(close: pd.Series) -> pd.Series:
    """E[(r_t - mu) * (r_{t-1} - mu)^2] / sd^3 over 252d - coskewness with prior squared return."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((r - mu) * (r.shift(1) - mu) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd ** 3)).diff()

def f51_dsav_072_coskew_r_with_lag1_absr_252d_d1(close: pd.Series) -> pd.Series:
    """E[(r_t - mu) * |r_{t-1} - mu|^2] / sd^3 over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((r - mu) * (r.shift(1) - mu).abs() ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd ** 3)).diff()

def f51_dsav_073_cokurt_r_with_lag1_r_252d_d1(close: pd.Series) -> pd.Series:
    """E[(r_t - mu)^2 * (r_{t-1} - mu)^2] / sd^4 over 252d - kurt-like joint dependence."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((r - mu) ** 2 * (r.shift(1) - mu) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd ** 4)).diff()

def f51_dsav_074_cokurt_r_with_lag2_r_252d_d1(close: pd.Series) -> pd.Series:
    """Same with lag 2."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((r - mu) ** 2 * (r.shift(2) - mu) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd ** 4)).diff()

def f51_dsav_075_coskew_overnight_intraday_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Coskewness between overnight and intraday returns over 252d."""
    on = _safe_log(open) - _safe_log(close.shift(1))
    intr = _safe_log(close) - _safe_log(open)
    mu_on = on.rolling(YDAYS, min_periods=QDAYS).mean()
    mu_in = intr.rolling(YDAYS, min_periods=QDAYS).mean()
    sd_on = on.rolling(YDAYS, min_periods=QDAYS).std()
    sd_in = intr.rolling(YDAYS, min_periods=QDAYS).std()
    cm = ((on - mu_on) * (intr - mu_in) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(cm, sd_on * sd_in ** 2)).diff()


# ============================================================
#                         REGISTRY 001_075 (d1)
# ============================================================

DISTRIBUTION_SHAPE_ADVANCED_D1_REGISTRY_001_075 = {
    "f51_dsav_001_bimodality_coef_pearson_log_ret_63d_d1": {"inputs": ["close"], "func": f51_dsav_001_bimodality_coef_pearson_log_ret_63d_d1},
    "f51_dsav_002_bimodality_coef_pearson_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_002_bimodality_coef_pearson_log_ret_252d_d1},
    "f51_dsav_003_hartigan_dip_stat_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_003_hartigan_dip_stat_log_ret_252d_d1},
    "f51_dsav_004_hartigan_dip_stat_log_ret_504d_d1": {"inputs": ["close"], "func": f51_dsav_004_hartigan_dip_stat_log_ret_504d_d1},
    "f51_dsav_005_kde_mode_count_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_005_kde_mode_count_log_ret_252d_d1},
    "f51_dsav_006_kde_mode_count_log_ret_504d_d1": {"inputs": ["close"], "func": f51_dsav_006_kde_mode_count_log_ret_504d_d1},
    "f51_dsav_007_multimodality_binary_indicator_252d_d1": {"inputs": ["close"], "func": f51_dsav_007_multimodality_binary_indicator_252d_d1},
    "f51_dsav_008_bimodality_excess_above_threshold_252d_d1": {"inputs": ["close"], "func": f51_dsav_008_bimodality_excess_above_threshold_252d_d1},
    "f51_dsav_009_dagostino_K2_omnibus_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_009_dagostino_K2_omnibus_log_ret_252d_d1},
    "f51_dsav_010_dagostino_skewness_z_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_010_dagostino_skewness_z_log_ret_252d_d1},
    "f51_dsav_011_hodges_lehmann_mean_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_011_hodges_lehmann_mean_log_ret_252d_d1},
    "f51_dsav_012_hodges_lehmann_mean_log_ret_63d_d1": {"inputs": ["close"], "func": f51_dsav_012_hodges_lehmann_mean_log_ret_63d_d1},
    "f51_dsav_013_trimean_tukey_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_013_trimean_tukey_log_ret_252d_d1},
    "f51_dsav_014_midhinge_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_014_midhinge_log_ret_252d_d1},
    "f51_dsav_015_shorth_mean_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_015_shorth_mean_log_ret_252d_d1},
    "f51_dsav_016_m_estimator_huber_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_016_m_estimator_huber_log_ret_252d_d1},
    "f51_dsav_017_mean_minus_hodges_lehmann_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_017_mean_minus_hodges_lehmann_log_ret_252d_d1},
    "f51_dsav_018_mean_minus_trimean_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_018_mean_minus_trimean_log_ret_252d_d1},
    "f51_dsav_019_midhinge_minus_median_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_019_midhinge_minus_median_log_ret_252d_d1},
    "f51_dsav_020_shorth_mean_minus_median_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_020_shorth_mean_minus_median_log_ret_252d_d1},
    "f51_dsav_021_medcouple_brys_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_021_medcouple_brys_log_ret_252d_d1},
    "f51_dsav_022_medcouple_brys_log_ret_504d_d1": {"inputs": ["close"], "func": f51_dsav_022_medcouple_brys_log_ret_504d_d1},
    "f51_dsav_023_hogg_robust_skew_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_023_hogg_robust_skew_log_ret_252d_d1},
    "f51_dsav_024_groeneveld_meeden_skew_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_024_groeneveld_meeden_skew_log_ret_252d_d1},
    "f51_dsav_025_pearson_2nd_skew_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_025_pearson_2nd_skew_log_ret_252d_d1},
    "f51_dsav_026_octile_skew_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_026_octile_skew_log_ret_252d_d1},
    "f51_dsav_027_galton_yule_skew_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_027_galton_yule_skew_log_ret_252d_d1},
    "f51_dsav_028_kelly_skew_p10_p90_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_028_kelly_skew_p10_p90_log_ret_252d_d1},
    "f51_dsav_029_conditional_tail_imbalance_one_sigma_252d_d1": {"inputs": ["close"], "func": f51_dsav_029_conditional_tail_imbalance_one_sigma_252d_d1},
    "f51_dsav_030_right_minus_left_tail_centroid_252d_d1": {"inputs": ["close"], "func": f51_dsav_030_right_minus_left_tail_centroid_252d_d1},
    "f51_dsav_031_crow_siddiqui_kurt_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_031_crow_siddiqui_kurt_log_ret_252d_d1},
    "f51_dsav_032_hogg_kurt_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_032_hogg_kurt_log_ret_252d_d1},
    "f51_dsav_033_moors_octile_kurt_extended_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_033_moors_octile_kurt_extended_log_ret_252d_d1},
    "f51_dsav_034_percentile_kurt_p99_p01_to_iqr_252d_d1": {"inputs": ["close"], "func": f51_dsav_034_percentile_kurt_p99_p01_to_iqr_252d_d1},
    "f51_dsav_035_tail_to_center_kurt_ratio_252d_d1": {"inputs": ["close"], "func": f51_dsav_035_tail_to_center_kurt_ratio_252d_d1},
    "f51_dsav_036_excess_mass_tails_above_1sigma_252d_d1": {"inputs": ["close"], "func": f51_dsav_036_excess_mass_tails_above_1sigma_252d_d1},
    "f51_dsav_037_excess_mass_tails_above_2sigma_252d_d1": {"inputs": ["close"], "func": f51_dsav_037_excess_mass_tails_above_2sigma_252d_d1},
    "f51_dsav_038_excess_mass_central_within_half_sigma_252d_d1": {"inputs": ["close"], "func": f51_dsav_038_excess_mass_central_within_half_sigma_252d_d1},
    "f51_dsav_039_ratio_iqr_to_p90_minus_p10_252d_d1": {"inputs": ["close"], "func": f51_dsav_039_ratio_iqr_to_p90_minus_p10_252d_d1},
    "f51_dsav_040_ratio_p95_minus_p5_to_iqr_252d_d1": {"inputs": ["close"], "func": f51_dsav_040_ratio_p95_minus_p5_to_iqr_252d_d1},
    "f51_dsav_041_fit_laplace_scale_b_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_041_fit_laplace_scale_b_log_ret_252d_d1},
    "f51_dsav_042_fit_logistic_scale_s_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_042_fit_logistic_scale_s_log_ret_252d_d1},
    "f51_dsav_043_fit_t_distribution_df_via_kurt_252d_d1": {"inputs": ["close"], "func": f51_dsav_043_fit_t_distribution_df_via_kurt_252d_d1},
    "f51_dsav_044_fit_skewnormal_lambda_pewsey_252d_d1": {"inputs": ["close"], "func": f51_dsav_044_fit_skewnormal_lambda_pewsey_252d_d1},
    "f51_dsav_045_fit_gumbel_mu_from_losses_252d_d1": {"inputs": ["close"], "func": f51_dsav_045_fit_gumbel_mu_from_losses_252d_d1},
    "f51_dsav_046_fit_gumbel_beta_from_losses_252d_d1": {"inputs": ["close"], "func": f51_dsav_046_fit_gumbel_beta_from_losses_252d_d1},
    "f51_dsav_047_fit_pareto_alpha_upper_5pct_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_047_fit_pareto_alpha_upper_5pct_log_ret_252d_d1},
    "f51_dsav_048_fit_pareto_alpha_upper_10pct_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_048_fit_pareto_alpha_upper_10pct_log_ret_252d_d1},
    "f51_dsav_049_fit_weibull_shape_from_pos_returns_252d_d1": {"inputs": ["close"], "func": f51_dsav_049_fit_weibull_shape_from_pos_returns_252d_d1},
    "f51_dsav_050_ratio_laplace_to_normal_scale_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_050_ratio_laplace_to_normal_scale_log_ret_252d_d1},
    "f51_dsav_051_cramer_von_mises_to_normal_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_051_cramer_von_mises_to_normal_log_ret_252d_d1},
    "f51_dsav_052_cramer_von_mises_to_normal_log_ret_63d_d1": {"inputs": ["close"], "func": f51_dsav_052_cramer_von_mises_to_normal_log_ret_63d_d1},
    "f51_dsav_053_wasserstein_to_normal_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_053_wasserstein_to_normal_log_ret_252d_d1},
    "f51_dsav_054_hellinger_to_normal_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_054_hellinger_to_normal_log_ret_252d_d1},
    "f51_dsav_055_bhattacharyya_to_normal_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_055_bhattacharyya_to_normal_log_ret_252d_d1},
    "f51_dsav_056_kl_divergence_to_laplace_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_056_kl_divergence_to_laplace_log_ret_252d_d1},
    "f51_dsav_057_ks_distance_to_laplace_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_057_ks_distance_to_laplace_log_ret_252d_d1},
    "f51_dsav_058_normal_minus_laplace_loglik_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_058_normal_minus_laplace_loglik_log_ret_252d_d1},
    "f51_dsav_059_aic_normal_minus_aic_laplace_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_059_aic_normal_minus_aic_laplace_log_ret_252d_d1},
    "f51_dsav_060_residual_normality_after_loc_scale_fit_252d_d1": {"inputs": ["close"], "func": f51_dsav_060_residual_normality_after_loc_scale_fit_252d_d1},
    "f51_dsav_061_renyi_entropy_q2_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_061_renyi_entropy_q2_log_ret_252d_d1},
    "f51_dsav_062_renyi_entropy_q3_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_062_renyi_entropy_q3_log_ret_252d_d1},
    "f51_dsav_063_renyi_entropy_qhalf_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_063_renyi_entropy_qhalf_log_ret_252d_d1},
    "f51_dsav_064_tsallis_entropy_q3_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_064_tsallis_entropy_q3_log_ret_252d_d1},
    "f51_dsav_065_entropy_relative_to_uniform_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_065_entropy_relative_to_uniform_log_ret_252d_d1},
    "f51_dsav_066_conditional_entropy_log_ret_given_sign_252d_d1": {"inputs": ["close"], "func": f51_dsav_066_conditional_entropy_log_ret_given_sign_252d_d1},
    "f51_dsav_067_joint_entropy_r_and_absr_252d_d1": {"inputs": ["close"], "func": f51_dsav_067_joint_entropy_r_and_absr_252d_d1},
    "f51_dsav_068_mutual_info_r_with_absr_252d_d1": {"inputs": ["close"], "func": f51_dsav_068_mutual_info_r_with_absr_252d_d1},
    "f51_dsav_069_kde_differential_entropy_log_ret_252d_d1": {"inputs": ["close"], "func": f51_dsav_069_kde_differential_entropy_log_ret_252d_d1},
    "f51_dsav_070_negentropy_kde_minus_gaussian_252d_d1": {"inputs": ["close"], "func": f51_dsav_070_negentropy_kde_minus_gaussian_252d_d1},
    "f51_dsav_071_coskew_r_with_lag1_rsq_252d_d1": {"inputs": ["close"], "func": f51_dsav_071_coskew_r_with_lag1_rsq_252d_d1},
    "f51_dsav_072_coskew_r_with_lag1_absr_252d_d1": {"inputs": ["close"], "func": f51_dsav_072_coskew_r_with_lag1_absr_252d_d1},
    "f51_dsav_073_cokurt_r_with_lag1_r_252d_d1": {"inputs": ["close"], "func": f51_dsav_073_cokurt_r_with_lag1_r_252d_d1},
    "f51_dsav_074_cokurt_r_with_lag2_r_252d_d1": {"inputs": ["close"], "func": f51_dsav_074_cokurt_r_with_lag2_r_252d_d1},
    "f51_dsav_075_coskew_overnight_intraday_252d_d1": {"inputs": ["open", "close"], "func": f51_dsav_075_coskew_overnight_intraday_252d_d1},
}
