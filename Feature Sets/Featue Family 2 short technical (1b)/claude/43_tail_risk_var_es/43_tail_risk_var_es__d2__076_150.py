"""tail_risk_var_es d2 features 076-150 - Pipeline 1b-technical.

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


def _norm_ppf(p):
    """Rational approximation of standard-normal inverse CDF (Beasley-Springer simplified)."""
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


def _norm_pdf(x):
    return float(np.exp(-0.5 * x * x) / np.sqrt(2.0 * np.pi))


def _hist_var(ret_s, n, q):
    """Historical VaR at confidence q (e.g. 0.95) - positive loss magnitude."""
    return -_rolling_q(ret_s, n, 1.0 - q)


def _hist_es(ret_s, n, q):
    """Historical Expected Shortfall at confidence q - mean loss in lower (1-q) tail."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        thr = np.quantile(v, 1.0 - q)
        tail = v[v <= thr]
        return -float(tail.mean()) if tail.size > 0 else np.nan
    return ret_s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hist_upside_es(ret_s, n, q):
    """Mean of returns in the upper (1-q) tail - positive 'gain' magnitude."""
    mp = max(n // 3, 20)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        thr = np.quantile(v, q)
        tail = v[v >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    return ret_s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _param_norm_var(ret_s, n, q):
    """Parametric normal VaR at confidence q - returns positive loss magnitude."""
    mp = max(n // 3, 20)
    mu = ret_s.rolling(n, min_periods=mp).mean()
    sd = ret_s.rolling(n, min_periods=mp).std()
    z = _norm_ppf(1.0 - q)
    return -(mu + sd * z)


def _param_norm_es(ret_s, n, q):
    """Parametric normal Expected Shortfall - positive loss magnitude."""
    mp = max(n // 3, 20)
    mu = ret_s.rolling(n, min_periods=mp).mean()
    sd = ret_s.rolling(n, min_periods=mp).std()
    z = _norm_ppf(1.0 - q)
    pdf = _norm_pdf(z)
    factor = pdf / (1.0 - q)
    return -(mu - sd * factor)


def _cornish_fisher_var(ret_s, n, q):
    """Cornish-Fisher VaR using skew/excess-kurt-adjusted z-score."""
    mp = max(n // 3, 30)
    mu = ret_s.rolling(n, min_periods=mp).mean()
    sd = ret_s.rolling(n, min_periods=mp).std()
    sk = ret_s.rolling(n, min_periods=mp).skew()
    kt = ret_s.rolling(n, min_periods=mp).kurt()
    z = _norm_ppf(1.0 - q)
    z_cf = (z + (z * z - 1.0) * sk / 6.0
              + (z ** 3 - 3.0 * z) * kt / 24.0
              - (2.0 * z ** 3 - 5.0 * z) * sk * sk / 36.0)
    return -(mu + sd * z_cf)


def _cornish_fisher_es(ret_s, n, q):
    """Cornish-Fisher ES proxy: integrate CF density tail via simple approximation:
    ES_CF ~ -mu + sd * phi(z_cf) / (1-q) (skew/kurt enter via z_cf)."""
    mp = max(n // 3, 30)
    mu = ret_s.rolling(n, min_periods=mp).mean()
    sd = ret_s.rolling(n, min_periods=mp).std()
    sk = ret_s.rolling(n, min_periods=mp).skew()
    kt = ret_s.rolling(n, min_periods=mp).kurt()
    z = _norm_ppf(1.0 - q)
    z_cf = (z + (z * z - 1.0) * sk / 6.0
              + (z ** 3 - 3.0 * z) * kt / 24.0
              - (2.0 * z ** 3 - 5.0 * z) * sk * sk / 36.0)
    pdf_z_cf = np.exp(-0.5 * z_cf * z_cf) / np.sqrt(2.0 * np.pi)
    factor = pdf_z_cf / (1.0 - q)
    return -(mu - sd * factor)


# Pre-computed Student-t quantile for canonical degrees of freedom.
# Source: standard tables (one-sided lower tail).
_T_QUANT = {
    5:  {0.95: -2.0150, 0.99: -3.3649, 0.995: -4.0322},
    10: {0.95: -1.8125, 0.99: -2.7638, 0.995: -3.1693},
    20: {0.95: -1.7247, 0.99: -2.5280, 0.995: -2.8453},
}


def _param_t_var(ret_s, n, q, df):
    """Parametric Student-t VaR at confidence q using df from {5,10,20}."""
    mp = max(n // 3, 20)
    mu = ret_s.rolling(n, min_periods=mp).mean()
    sd = ret_s.rolling(n, min_periods=mp).std()
    scale = np.sqrt((df - 2.0) / df) if df > 2 else 1.0
    t_q = _T_QUANT.get(df, _T_QUANT[10]).get(q, _T_QUANT[10][0.95])
    return -(mu + sd * scale * t_q)


def _kurt_implied_df(ret_s, n):
    """Approx df from sample kurt: df = 4 + 6/excess_kurt (Fisher's method)."""
    mp = max(n // 3, 20)
    k = ret_s.rolling(n, min_periods=mp).kurt()
    return (4.0 + 6.0 / k.replace(0, np.nan)).clip(lower=3.0, upper=100.0)


def _pot_threshold(ret_s, n, q=0.95):
    """Peaks-over-threshold reference level (q-quantile of losses)."""
    mp = max(n // 3, 30)
    losses = -ret_s
    return _rolling_q(losses, n, q, min_periods=mp)


def _pot_mean_excess(ret_s, n, q=0.95):
    """Mean excess over POT threshold - simple EVT-flavored summary."""
    mp = max(n // 3, 30)
    def _f(w):
        v = -w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, q)
        ex = v[v > thr] - thr
        return float(ex.mean()) if ex.size > 0 else np.nan
    return ret_s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _pot_gpd_shape(ret_s, n, q=0.95):
    """GPD shape parameter xi via Hill-style moment estimator on POT excesses."""
    mp = max(n // 3, 40)
    def _f(w):
        v = -w[~np.isnan(w)]
        if v.size < 40:
            return np.nan
        thr = np.quantile(v, q)
        ex = v[v > thr] - thr
        if ex.size < 10 or (ex <= 0).any():
            return np.nan
        # Method of moments: xi = 0.5 * (1 - (mean(ex)^2) / var(ex))
        m = ex.mean(); va = ex.var(ddof=1)
        if va <= 0:
            return np.nan
        return float(0.5 * (1.0 - (m * m) / va))
    return ret_s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _pot_gpd_scale(ret_s, n, q=0.95):
    """GPD scale beta via method of moments: beta = 0.5 * mean(ex) * (1 + (mean(ex)^2)/var(ex))."""
    mp = max(n // 3, 40)
    def _f(w):
        v = -w[~np.isnan(w)]
        if v.size < 40:
            return np.nan
        thr = np.quantile(v, q)
        ex = v[v > thr] - thr
        if ex.size < 10 or (ex <= 0).any():
            return np.nan
        m = ex.mean(); va = ex.var(ddof=1)
        if va <= 0:
            return np.nan
        return float(0.5 * m * (1.0 + (m * m) / va))
    return ret_s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _drawdown_series(close):
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    return lc - rmax  # <= 0


def _rolling_max_drawdown(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _md(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((v - cm).min())
    return lc.rolling(n, min_periods=mp).apply(_md, raw=True)


def _rolling_mean_drawdown(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _mn(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = v - cm
        return float(dd.mean())
    return lc.rolling(n, min_periods=mp).apply(_mn, raw=True)


def _ulcer_index(close, n):
    mp = max(n // 3, 10)
    lc = _safe_log(close)
    def _u(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = v - cm
        return float(np.sqrt(np.mean(dd ** 2)))
    return lc.rolling(n, min_periods=mp).apply(_u, raw=True)


def _drawdown_duration_max(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _dd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        cm = np.maximum.accumulate(v)
        in_dd = v < cm
        cur = 0; best = 0
        for x in in_dd:
            if x:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return lc.rolling(n, min_periods=mp).apply(_dd, raw=True)


def _cdar(close, n, q=0.95):
    """Conditional drawdown at risk - mean of worst (1-q) drawdowns over n."""
    mp = max(n // 3, 30)
    lc = _safe_log(close)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = -(v - cm)  # positive magnitudes
        thr = np.quantile(dd, q)
        tail = dd[dd >= thr]
        return float(tail.mean()) if tail.size > 0 else np.nan
    return lc.rolling(n, min_periods=mp).apply(_f, raw=True)


def _hill_index_lower(s, n, k_frac=0.05):
    mp = max(n // 3, 30)
    def _f(w):
        v = -w[~np.isnan(w)]
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


def f43_trve_076_tail_dep_lower_close_volume_05_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Joint probability of close in bottom 5% AND volume in top 5% over 252d - panic-tail dep."""
    r = _log_ret(close)
    v = _safe_log(volume.replace(0, np.nan)).diff()
    def _td(w):
        n = w.shape[0]
        if n < 30:
            return np.nan
        ra = w[:, 0]; va = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(va)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; va = va[valid]
        rq = np.quantile(ra, 0.05); vq = np.quantile(va, 0.95)
        return float(((ra <= rq) & (va >= vq)).mean())
    df = pd.concat([r.rename('r'), v.rename('v')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _td(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f43_trve_077_tail_dep_upper_close_volume_95_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Joint probability of close in top 5% AND volume in top 5% over 252d - euphoria-tail dep."""
    r = _log_ret(close)
    v = _safe_log(volume.replace(0, np.nan)).diff()
    def _td(w):
        n = w.shape[0]
        if n < 30:
            return np.nan
        ra = w[:, 0]; va = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(va)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; va = va[valid]
        rq = np.quantile(ra, 0.95); vq = np.quantile(va, 0.95)
        return float(((ra >= rq) & (va >= vq)).mean())
    df = pd.concat([r.rename('r'), v.rename('v')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _td(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f43_trve_078_tail_dep_lower_close_overnight_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Joint probability of close-return in bottom 5% AND overnight-gap in bottom 5% over 252d."""
    r = _log_ret(close)
    on = _safe_log(open) - _safe_log(close.shift(1))
    def _td(w):
        n = w.shape[0]
        if n < 30:
            return np.nan
        ra = w[:, 0]; oa = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(oa)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; oa = oa[valid]
        rq = np.quantile(ra, 0.05); oq = np.quantile(oa, 0.05)
        return float(((ra <= rq) & (oa <= oq)).mean())
    df = pd.concat([r.rename('r'), on.rename('o')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _td(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f43_trve_079_tail_dep_upper_close_overnight_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Joint probability of close-return AND overnight-gap both in top 5% over 252d."""
    r = _log_ret(close)
    on = _safe_log(open) - _safe_log(close.shift(1))
    def _td(w):
        n = w.shape[0]
        if n < 30:
            return np.nan
        ra = w[:, 0]; oa = w[:, 1]
        valid = ~np.isnan(ra) & ~np.isnan(oa)
        if valid.sum() < 30:
            return np.nan
        ra = ra[valid]; oa = oa[valid]
        rq = np.quantile(ra, 0.95); oq = np.quantile(oa, 0.95)
        return float(((ra >= rq) & (oa >= oq)).mean())
    df = pd.concat([r.rename('r'), on.rename('o')], axis=1)
    arr = df.values
    out = np.full(len(arr), np.nan, dtype=float)
    for i in range(len(arr)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _td(arr[lo:i + 1])
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f43_trve_080_extreme_returns_volume_corr_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation between |log-return| and log-volume over 252d - extreme co-movement."""
    r = _log_ret(close).abs()
    lv = _safe_log(volume.replace(0, np.nan))
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(lv)).diff().diff()

def f43_trve_081_spectral_risk_exp_weighted_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Exponentially-weighted spectral risk on bottom 5% over 252d - weight=exp(-k/n_tail) on sorted losses."""
    r = _log_ret(close)
    def _sp(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        losses = -np.sort(v)
        k = max(int(0.05 * v.size), 3)
        tail = losses[:k]
        wts = np.exp(-np.arange(k) / max(k / 2.0, 1.0))
        wts /= wts.sum()
        return float((tail * wts).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sp, raw=True)
    return (res).diff().diff()

def f43_trve_082_spectral_risk_power_weighted_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Power-weighted spectral risk on bottom 5% over 252d - weight=k^-0.5 on sorted losses."""
    r = _log_ret(close)
    def _sp(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        losses = -np.sort(v)
        k = max(int(0.05 * v.size), 3)
        tail = losses[:k]
        wts = 1.0 / np.sqrt(np.arange(1, k + 1, dtype=float))
        wts /= wts.sum()
        return float((tail * wts).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sp, raw=True)
    return (res).diff().diff()

def f43_trve_083_wang_transform_risk_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Wang-transform-like risk: shifted-normal distortion with parameter 0.5 on losses, top 5% over 252d."""
    r = _log_ret(close)
    def _wg(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        losses = -np.sort(v)
        k = max(int(0.05 * v.size), 3)
        tail = losses[:k]
        wts = np.exp(-((np.arange(k) - 0.5 * (k - 1)) / max(k / 4.0, 1.0)) ** 2)
        wts /= wts.sum()
        return float((tail * wts).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_wg, raw=True)
    return (res).diff().diff()

def f43_trve_084_dual_power_risk_alpha2_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Dual-power distortion with alpha=2 on losses, top 10% over 252d."""
    r = _log_ret(close)
    def _dp(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        losses = -np.sort(v)
        k = max(int(0.10 * v.size), 5)
        tail = losses[:k]
        wts = (k - np.arange(k, dtype=float)) ** 2
        wts /= wts.sum()
        return float((tail * wts).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_dp, raw=True)
    return (res).diff().diff()

def f43_trve_085_proportional_hazard_risk_alpha_half_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Proportional-hazard distortion (alpha=0.5) on losses, top 10% over 252d."""
    r = _log_ret(close)
    def _ph(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        losses = -np.sort(v)
        k = max(int(0.10 * v.size), 5)
        tail = losses[:k]
        ranks = np.arange(1, k + 1, dtype=float)
        wts = np.sqrt(ranks) - np.sqrt(ranks - 1.0)
        wts /= wts.sum()
        return float((tail * wts).sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ph, raw=True)
    return (res).diff().diff()

def f43_trve_086_rank_distortion_risk_uniform_top10_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Uniform-weighted top-10% loss average over 252d - simple TVaR."""
    r = _log_ret(close)
    return (_hist_es(r, YDAYS, 0.90)).diff().diff()

def f43_trve_087_var_breach_count_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars where loss > VaR(95) within the same 252d window."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    breach = (-r > v).astype(float).where(v.notna(), np.nan)
    return (breach.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f43_trve_088_var_breach_count_99_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars where loss > VaR(99) over 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.99)
    breach = (-r > v).astype(float).where(v.notna(), np.nan)
    return (breach.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f43_trve_089_var_breach_rate_coverage_error_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """(observed breach rate - expected 5%) over 252d - coverage error."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    breach = (-r > v).astype(float).where(v.notna(), np.nan)
    rate = breach.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rate - 0.05).diff().diff()

def f43_trve_090_clustering_of_var_breaches_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar breach pairs in last 252d - clustering indicator."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    breach = (-r > v).astype(float).where(v.notna(), np.nan)
    pair = ((breach > 0.5) & (breach.shift(1) > 0.5)).astype(float)
    return (pair.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f43_trve_091_mean_loss_given_breach_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean loss size on bars where VaR(95) was breached, within last 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    loss_on_breach = (-r).where((-r > v) & v.notna(), np.nan)
    return (loss_on_breach.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f43_trve_092_max_loss_given_breach_99_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Maximum loss on bars where VaR(99) was breached, within last 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.99)
    loss_on_breach = (-r).where((-r > v) & v.notna(), np.nan)
    return (loss_on_breach.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()

def f43_trve_093_asymmetric_var_ratio_up_down_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upper-tail 95th-quantile magnitude to lower-tail 95% VaR over 252d."""
    r = _log_ret(close)
    up = _rolling_q(r, YDAYS, 0.95)
    dn = _hist_var(r, YDAYS, 0.95)
    return (_safe_div(up, dn)).diff().diff()

def f43_trve_094_asymmetric_es_ratio_up_down_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upside ES (95) to downside ES (95) over 252d."""
    r = _log_ret(close)
    up = _hist_upside_es(r, YDAYS, 0.95)
    dn = _hist_es(r, YDAYS, 0.95)
    return (_safe_div(up, dn)).diff().diff()

def f43_trve_095_tail_skew_index_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Upper VaR(95) minus lower VaR(95) magnitude over 252d - tail skew."""
    r = _log_ret(close)
    up = _rolling_q(r, YDAYS, 0.95)
    dn = _hist_var(r, YDAYS, 0.95)
    return (up - dn).diff().diff()

def f43_trve_096_tail_kurt_index_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of upper VaR(95) magnitude and lower VaR(95) magnitude over 252d - tail width."""
    r = _log_ret(close)
    up = _rolling_q(r, YDAYS, 0.95)
    dn = _hist_var(r, YDAYS, 0.95)
    return (up + dn).diff().diff()

def f43_trve_097_cf_var_diff_up_down_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 95 VaR(loss) minus Cornish-Fisher 95 'upside VaR' (mu+sd*z_cf) over 252d."""
    r = _log_ret(close)
    lo = _cornish_fisher_var(r, YDAYS, 0.95)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    sk = r.rolling(YDAYS, min_periods=QDAYS).skew(); kt = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    z = _norm_ppf(0.95)
    z_cf = (z + (z * z - 1.0) * sk / 6.0 + (z ** 3 - 3.0 * z) * kt / 24.0 - (2.0 * z ** 3 - 5.0 * z) * sk * sk / 36.0)
    up = (mu + sd * z_cf)
    return (lo - up).diff().diff()

def f43_trve_098_param_t_var_diff_up_down_99_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Student-t(df=5) 99 VaR minus 'upside' equivalent over 252d - parametric tail asymmetry."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    scale = np.sqrt((5.0 - 2.0) / 5.0)
    lo_q = _T_QUANT[5][0.99]
    up_q = -lo_q
    lo = -(mu + sd * scale * lo_q)
    up = (mu + sd * scale * up_q)
    return (lo - up).diff().diff()

def f43_trve_099_hill_tail_estimator_lower_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator on bottom 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_lower(r, YDAYS, 0.05)).diff().diff()

def f43_trve_100_hill_tail_estimator_upper_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Hill tail-index estimator on top 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hill_index_upper(r, YDAYS, 0.05)).diff().diff()

def f43_trve_101_pickands_tail_estimator_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Pickands tail-index estimator on log-returns over 252d."""
    r = _log_ret(close)
    return (_pickands_index(r, YDAYS)).diff().diff()

def f43_trve_102_moment_tail_estimator_dekkers_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Dekkers-Einmahl-deHaan moment-style tail estimator (simplified) on log-returns over 252d."""
    r = _log_ret(close)
    def _dk(w):
        v = -w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = np.sort(v)
        k = max(int(0.05 * v.size), 5)
        if k >= v.size:
            return np.nan
        thr = v[v.size - k - 1]
        tail = v[v.size - k:]
        if thr <= 0 or (tail <= 0).any():
            return np.nan
        logd = np.log(tail / thr)
        m1 = logd.mean(); m2 = (logd ** 2).mean()
        if m2 <= 0:
            return np.nan
        return float(m1 + 1.0 - 0.5 / (1.0 - (m1 * m1) / m2))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_dk, raw=True)
    return (res).diff().diff()

def f43_trve_103_extreme_value_index_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Extreme-value index: ratio top-1%/top-5% mean log-returns over 252d."""
    r = _log_ret(close).abs()
    def _ev(w):
        v = np.sort(w[~np.isnan(w)])
        if v.size < 60:
            return np.nan
        k1 = max(int(0.01 * v.size), 2); k5 = max(int(0.05 * v.size), 5)
        if k1 >= v.size or k5 >= v.size:
            return np.nan
        return float(v[-k1:].mean() / v[-k5:].mean()) if v[-k5:].mean() > 0 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ev, raw=True)
    return (res).diff().diff()

def f43_trve_104_tail_index_diff_lower_upper_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Lower Hill minus upper Hill (5%) over 252d - asymmetry of tail thickness."""
    r = _log_ret(close)
    lo = _hill_index_lower(r, YDAYS, 0.05)
    up = _hill_index_upper(r, YDAYS, 0.05)
    return (lo - up).diff().diff()

def f43_trve_105_worst_drawdown_504d_log_close_d2(close: pd.Series) -> pd.Series:
    """Worst drawdown over 504d (more stress per longer window)."""
    return (_rolling_max_drawdown(close, DDAYS_2Y)).diff().diff()

def f43_trve_106_recovery_rate_post_dd_log_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars in 252d where price is at new high (regime recovery)."""
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    at_high = (lc >= rmax - 1e-9).astype(float)
    return (at_high.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f43_trve_107_time_to_recovery_from_max_dd_log_252d_d2(close: pd.Series) -> pd.Series:
    """Bars since last new-high within 252d window."""
    lc = _safe_log(close)
    rmax = lc.expanding(min_periods=1).max()
    is_high = (lc >= rmax - 1e-9)
    arr = is_high.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f43_trve_108_drawdown_volatility_log_252d_d2(close: pd.Series) -> pd.Series:
    """Std of drawdown depths over 252d - drawdown variability."""
    dd = _drawdown_series(close)
    return (dd.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f43_trve_109_stress_loss_3sigma_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Loss magnitude at -3 sigma normal: 3*sigma over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (3.0 * sd).diff().diff()

def f43_trve_110_stress_loss_5sigma_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Loss magnitude at -5 sigma normal over 252d (rare-tail)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (5.0 * sd).diff().diff()

def f43_trve_111_mean_loss_top_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean loss magnitude in bottom 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hist_es(r, YDAYS, 0.95)).diff().diff()

def f43_trve_112_mean_gain_top_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean gain magnitude in top 5% of log-returns over 252d."""
    r = _log_ret(close)
    return (_hist_upside_es(r, YDAYS, 0.95)).diff().diff()

def f43_trve_113_loss_to_gain_ratio_extreme_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean loss(bot 5%) / mean gain(top 5%) over 252d - asymmetric extreme amplitude."""
    r = _log_ret(close)
    lo = _hist_es(r, YDAYS, 0.95)
    up = _hist_upside_es(r, YDAYS, 0.95)
    return (_safe_div(lo, up)).diff().diff()

def f43_trve_114_expected_tail_loss_share_total_loss_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """ES(95) * 0.05 / mean(|negative returns|) over 252d - tail share of total downside."""
    r = _log_ret(close)
    es = _hist_es(r, YDAYS, 0.95)
    neg = (-r).clip(lower=0.0)
    tot = neg.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(es * 0.05, tot)).diff().diff()

def f43_trve_115_tail_loss_share_top_1pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of bottom-1% returns / sum of all negative returns over 252d."""
    r = _log_ret(close)
    def _ts(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        neg = v[v < 0]
        if neg.size == 0 or neg.sum() == 0:
            return np.nan
        k = max(int(0.01 * v.size), 1)
        bot = np.sort(v)[:k]
        return float(bot.sum() / neg.sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)
    return (res).diff().diff()

def f43_trve_116_tail_gain_share_top_1pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of top-1% returns / sum of all positive returns over 252d."""
    r = _log_ret(close)
    def _ts(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        pos = v[v > 0]
        if pos.size == 0 or pos.sum() == 0:
            return np.nan
        k = max(int(0.01 * v.size), 1)
        top = np.sort(v)[-k:]
        return float(top.sum() / pos.sum())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ts, raw=True)
    return (res).diff().diff()

def f43_trve_117_var_term_struct_slope_63_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of historical VaR(95) at 63d to at 252d - term-structure shape."""
    r = _log_ret(close)
    short = _hist_var(r, QDAYS, 0.95)
    long = _hist_var(r, YDAYS, 0.95)
    return (_safe_div(short, long)).diff().diff()

def f43_trve_118_var_term_struct_slope_21_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of 21d VaR(95) to 252d VaR(95)."""
    r = _log_ret(close)
    short = _hist_var(r, MDAYS, 0.95)
    long = _hist_var(r, YDAYS, 0.95)
    return (_safe_div(short, long)).diff().diff()

def f43_trve_119_es_term_struct_slope_63_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of 63d ES(95) to 252d ES(95)."""
    r = _log_ret(close)
    short = _hist_es(r, QDAYS, 0.95)
    long = _hist_es(r, YDAYS, 0.95)
    return (_safe_div(short, long)).diff().diff()

def f43_trve_120_var_acceleration_term_struct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Discrete acceleration of VaR(95) across 21d/63d/252d windows."""
    r = _log_ret(close)
    v1 = _hist_var(r, MDAYS, 0.95); v2 = _hist_var(r, QDAYS, 0.95); v3 = _hist_var(r, YDAYS, 0.95)
    return ((v3 - 2.0 * v2 + v1)).diff().diff()

def f43_trve_121_var_to_vol_ratio_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """VaR(95) / std(log_ret) over 252d - vol-normalized tail depth."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(v, sd)).diff().diff()

def f43_trve_122_es_to_var_ratio_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """ES(95) / VaR(95) over 252d - tail-conditional severity."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    es = _hist_es(r, YDAYS, 0.95)
    return (_safe_div(es, v)).diff().diff()

def f43_trve_123_amihud_weighted_var_95_log_ret_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity-weighted VaR proxy: VaR(95) * mean(|r|/dollar_volume) over 252d."""
    r = _log_ret(close)
    illiq = _safe_div(r.abs(), close * volume)
    il = illiq.rolling(YDAYS, min_periods=QDAYS).mean()
    v = _hist_var(r, YDAYS, 0.95)
    return (v * (1.0 + il)).diff().diff()

def f43_trve_124_range_to_var_ratio_log_ret_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high-low)/close over 252d divided by VaR(95)."""
    r = _log_ret(close)
    rng = _safe_div(high - low, close).rolling(YDAYS, min_periods=QDAYS).mean()
    v = _hist_var(r, YDAYS, 0.95)
    return (_safe_div(rng, v)).diff().diff()

def f43_trve_125_atr_to_var_ratio_log_ret_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21/close over 252d divided by VaR(95)."""
    atr_nm = _safe_div(_atr(high, low, close, n=MDAYS), close)
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    atr_avg = atr_nm.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(atr_avg, v)).diff().diff()

def f43_trve_126_var_intraday_atr_norm_log_ret_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VaR(95) on log-returns / mean ATR21/close over 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    atr_avg = _safe_div(_atr(high, low, close, n=MDAYS), close).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(v, atr_avg)).diff().diff()

def f43_trve_127_var_jumps_only_252d_d2(close: pd.Series) -> pd.Series:
    """Historical VaR(95) computed on jump component (returns above 3-sigma magnitudes) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    jumps = r.where(r.abs() > 3.0 * sd, np.nan)
    return (_hist_var(jumps, YDAYS, 0.95)).diff().diff()

def f43_trve_128_var_continuous_only_252d_d2(close: pd.Series) -> pd.Series:
    """Historical VaR(95) computed on continuous component (returns within 3-sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cont = r.where(r.abs() <= 3.0 * sd, np.nan)
    return (_hist_var(cont, YDAYS, 0.95)).diff().diff()

def f43_trve_129_ncskew_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Negative coefficient of skewness: -[n(n-1)^1.5 * sum r^3] / [(n-1)(n-2)*(sum r^2)^1.5] over 252d."""
    r = _log_ret(close)
    def _ncskew(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 60:
            return np.nan
        s2 = (v ** 2).sum()
        s3 = (v ** 3).sum()
        if s2 <= 0:
            return np.nan
        num = -n * (n - 1) ** 1.5 * s3
        den = (n - 1) * (n - 2) * (s2 ** 1.5)
        if den == 0:
            return np.nan
        return float(num / den)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ncskew, raw=True)
    return (res).diff().diff()

def f43_trve_130_duvol_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """DUVOL (Down-to-Up volatility): log[(n_u-1)*var_down / (n_d-1)*var_up] over 252d."""
    r = _log_ret(close)
    def _du(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        mu = v.mean()
        down = v[v < mu]; up = v[v >= mu]
        if down.size < 5 or up.size < 5:
            return np.nan
        vd = down.var(ddof=1); vu = up.var(ddof=1)
        if vd <= 0 or vu <= 0:
            return np.nan
        return float(np.log(((up.size - 1) * vd) / ((down.size - 1) * vu)))
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_du, raw=True)
    return (res).diff().diff()

def f43_trve_131_crash_indicator_3sigma_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Count of days with r <= mean - 3 sigma over 252d (firm-specific crash event count)."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    crash = (r <= mu - 3.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (crash.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f43_trve_132_probability_neg_extreme_3sigma_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Empirical probability of return <= -3 sigma normalized over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    crash = (r <= mu - 3.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (crash.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f43_trve_133_left_tail_density_norm_p10_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of negative returns relative to 10th-percentile normalization over 252d."""
    r = _log_ret(close)
    neg = r.where(r < 0, np.nan)
    mu = neg.rolling(YDAYS, min_periods=QDAYS).mean()
    p10 = _rolling_q(r, YDAYS, 0.10)
    return (_safe_div(mu, p10)).diff().diff()

def f43_trve_134_third_central_moment_neg_only_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of r^3 restricted to r < 0 over 252d - signed downside-skew kernel."""
    r = _log_ret(close)
    neg_cubed = (r ** 3).where(r < 0, np.nan)
    return (neg_cubed.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f43_trve_135_pareto_alpha_estimator_lower_5pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Pareto alpha = 1/Hill on bottom 5% over 252d - tail-index estimator."""
    r = _log_ret(close)
    return (_hill_index_lower(r, YDAYS, 0.05)).diff().diff()

def f43_trve_136_pareto_alpha_estimator_lower_10pct_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Pareto alpha on bottom 10% over 252d."""
    r = _log_ret(close)
    return (_hill_index_lower(r, YDAYS, 0.10)).diff().diff()

def f43_trve_137_log_log_tail_slope_lower_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Slope of log(1-empirical CDF) vs log(loss magnitude) on lower 20% over 252d."""
    r = _log_ret(close)
    def _ll(w):
        v = -w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        v = np.sort(v)
        k = max(int(0.20 * v.size), 10)
        tail = v[v.size - k:]
        tail = tail[tail > 0]
        if tail.size < 5:
            return np.nan
        p = np.arange(1, tail.size + 1, dtype=float) / (tail.size + 1)
        x = np.log(tail); y = np.log(1.0 - p)
        if np.var(x) == 0:
            return np.nan
        return float(np.polyfit(x, y, 1)[0])
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_ll, raw=True)
    return (res).diff().diff()

def f43_trve_138_tail_thickness_index_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of 99th to 90th percentile loss over 252d - tail-thickness proxy."""
    r = _log_ret(close)
    v99 = _hist_var(r, YDAYS, 0.99)
    v90 = _hist_var(r, YDAYS, 0.90)
    return (_safe_div(v99, v90)).diff().diff()

def f43_trve_139_heavy_tail_test_chebyshev_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """P(|r|>2sigma) vs Chebyshev bound 0.25 - excess gives heavy-tail indicator over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    over2 = (r.abs() > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    rate = over2.rolling(YDAYS, min_periods=QDAYS).mean()
    return (rate - 0.25).diff().diff()

def f43_trve_140_extreme_event_density_per_year_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Count of |r| > 3 sigma days per 252d window (annualized rare-event density)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    ext = (r.abs() > 3.0 * sd).astype(float).where(sd.notna(), np.nan)
    return (ext.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f43_trve_141_spectral_coherent_var_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Convex-combined VaR(95) and ES(95): 0.5*VaR + 0.5*ES (coherent risk avg) over 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    es = _hist_es(r, YDAYS, 0.95)
    return (0.5 * v + 0.5 * es).diff().diff()

def f43_trve_142_weighted_var_exponential_decay_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Exponentially-decay-weighted VaR proxy: EWMA std at alpha=0.06 * z_95 over 252d."""
    r = _log_ret(close)
    sd = r.ewm(alpha=0.06, adjust=False, min_periods=20).std()
    z = _norm_ppf(0.95)
    return (-(sd * z)).diff().diff()

def f43_trve_143_truncated_var_extreme_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of bottom-1% losses capped at 5*sigma over 252d - dispersion in extreme tail."""
    r = _log_ret(close)
    def _tv(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        cap = -5.0 * sd
        tail = np.clip(np.sort(v)[: max(int(0.01 * v.size), 1)], cap, None)
        return float(-tail.mean())
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_tv, raw=True)
    return (res).diff().diff()

def f43_trve_144_shortfall_dispersion_95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Std of returns in bottom 5% over 252d - dispersion within tail."""
    r = _log_ret(close)
    def _sd(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.05)
        tail = v[v <= thr]
        return float(tail.std(ddof=1)) if tail.size > 2 else np.nan
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_sd, raw=True)
    return (res).diff().diff()

def f43_trve_145_tail_concentration_risk_index_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of bottom-10% losses / variance of full distribution over 252d - tail-vs-body dispersion."""
    r = _log_ret(close)
    def _tc(w):
        v = w[~np.isnan(w)]
        if v.size < 60:
            return np.nan
        thr = np.quantile(v, 0.10)
        tail = v[v <= thr]
        if tail.size < 5:
            return np.nan
        vt = tail.var(ddof=1); vf = v.var(ddof=1)
        if vf <= 0:
            return np.nan
        return float(vt / vf)
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_tc, raw=True)
    return (res).diff().diff()

def f43_trve_146_mean_excess_function_at_var95_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """Mean excess of losses above VaR(95) - same as ES(95) - VaR(95), over 252d."""
    r = _log_ret(close)
    es = _hist_es(r, YDAYS, 0.95)
    v = _hist_var(r, YDAYS, 0.95)
    return (es - v).diff().diff()

def f43_trve_147_composite_tail_risk_zscore_var_es_dd_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score-summed composite of VaR(95), ES(95) and max-drawdown (all losses), over 252d."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95); es = _hist_es(r, YDAYS, 0.95); md = -_rolling_max_drawdown(close, YDAYS)
    z1 = _rolling_zscore(v, YDAYS); z2 = _rolling_zscore(es, YDAYS); z3 = _rolling_zscore(md, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0)).diff().diff()

def f43_trve_148_tail_stability_index_rolling_var_std_252d_d2(close: pd.Series) -> pd.Series:
    """Std (over the last 63 bars) of the 252d-VaR(95) series - stability of tail estimate."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    return (v.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f43_trve_149_var_innovation_log_ret_252d_d2(close: pd.Series) -> pd.Series:
    """1-day change in 252d VaR(95) - new-information impact on tail estimate."""
    r = _log_ret(close)
    v = _hist_var(r, YDAYS, 0.95)
    return (v.diff()).diff().diff()

def f43_trve_150_crash_prone_composite_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Composite indicator: NCSKEW > 0 AND |Hill_lower| > median AND max_dd > median over 252d."""
    r = _log_ret(close)
    def _ncs(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 60:
            return np.nan
        s2 = (v ** 2).sum(); s3 = (v ** 3).sum()
        if s2 <= 0:
            return np.nan
        num = -n * (n - 1) ** 1.5 * s3
        den = (n - 1) * (n - 2) * (s2 ** 1.5)
        if den == 0:
            return np.nan
        return float(num / den)
    ncs = r.rolling(YDAYS, min_periods=QDAYS).apply(_ncs, raw=True)
    hill = _hill_index_lower(r, YDAYS, 0.05)
    mdd = -_rolling_max_drawdown(close, YDAYS)
    h_med = hill.rolling(YDAYS, min_periods=QDAYS).median()
    m_med = mdd.rolling(YDAYS, min_periods=QDAYS).median()
    sig = ((ncs > 0) & (hill > h_med) & (mdd > m_med)).astype(float).where(
        ncs.notna() & hill.notna() & mdd.notna(), np.nan)
    return (sig).diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

TAIL_RISK_VAR_ES_D2_REGISTRY_076_150 = {
    "f43_trve_076_tail_dep_lower_close_volume_05_252d_d2": {"inputs": ["close", "volume"], "func": f43_trve_076_tail_dep_lower_close_volume_05_252d_d2},
    "f43_trve_077_tail_dep_upper_close_volume_95_252d_d2": {"inputs": ["close", "volume"], "func": f43_trve_077_tail_dep_upper_close_volume_95_252d_d2},
    "f43_trve_078_tail_dep_lower_close_overnight_252d_d2": {"inputs": ["open", "close"], "func": f43_trve_078_tail_dep_lower_close_overnight_252d_d2},
    "f43_trve_079_tail_dep_upper_close_overnight_252d_d2": {"inputs": ["open", "close"], "func": f43_trve_079_tail_dep_upper_close_overnight_252d_d2},
    "f43_trve_080_extreme_returns_volume_corr_252d_d2": {"inputs": ["close", "volume"], "func": f43_trve_080_extreme_returns_volume_corr_252d_d2},
    "f43_trve_081_spectral_risk_exp_weighted_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_081_spectral_risk_exp_weighted_5pct_log_ret_252d_d2},
    "f43_trve_082_spectral_risk_power_weighted_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_082_spectral_risk_power_weighted_5pct_log_ret_252d_d2},
    "f43_trve_083_wang_transform_risk_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_083_wang_transform_risk_5pct_log_ret_252d_d2},
    "f43_trve_084_dual_power_risk_alpha2_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_084_dual_power_risk_alpha2_log_ret_252d_d2},
    "f43_trve_085_proportional_hazard_risk_alpha_half_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_085_proportional_hazard_risk_alpha_half_log_ret_252d_d2},
    "f43_trve_086_rank_distortion_risk_uniform_top10_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_086_rank_distortion_risk_uniform_top10_log_ret_252d_d2},
    "f43_trve_087_var_breach_count_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_087_var_breach_count_95_log_ret_252d_d2},
    "f43_trve_088_var_breach_count_99_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_088_var_breach_count_99_log_ret_252d_d2},
    "f43_trve_089_var_breach_rate_coverage_error_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_089_var_breach_rate_coverage_error_95_log_ret_252d_d2},
    "f43_trve_090_clustering_of_var_breaches_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_090_clustering_of_var_breaches_95_log_ret_252d_d2},
    "f43_trve_091_mean_loss_given_breach_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_091_mean_loss_given_breach_95_log_ret_252d_d2},
    "f43_trve_092_max_loss_given_breach_99_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_092_max_loss_given_breach_99_log_ret_252d_d2},
    "f43_trve_093_asymmetric_var_ratio_up_down_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_093_asymmetric_var_ratio_up_down_95_log_ret_252d_d2},
    "f43_trve_094_asymmetric_es_ratio_up_down_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_094_asymmetric_es_ratio_up_down_95_log_ret_252d_d2},
    "f43_trve_095_tail_skew_index_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_095_tail_skew_index_log_ret_252d_d2},
    "f43_trve_096_tail_kurt_index_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_096_tail_kurt_index_log_ret_252d_d2},
    "f43_trve_097_cf_var_diff_up_down_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_097_cf_var_diff_up_down_95_log_ret_252d_d2},
    "f43_trve_098_param_t_var_diff_up_down_99_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_098_param_t_var_diff_up_down_99_log_ret_252d_d2},
    "f43_trve_099_hill_tail_estimator_lower_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_099_hill_tail_estimator_lower_5pct_log_ret_252d_d2},
    "f43_trve_100_hill_tail_estimator_upper_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_100_hill_tail_estimator_upper_5pct_log_ret_252d_d2},
    "f43_trve_101_pickands_tail_estimator_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_101_pickands_tail_estimator_log_ret_252d_d2},
    "f43_trve_102_moment_tail_estimator_dekkers_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_102_moment_tail_estimator_dekkers_log_ret_252d_d2},
    "f43_trve_103_extreme_value_index_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_103_extreme_value_index_log_ret_252d_d2},
    "f43_trve_104_tail_index_diff_lower_upper_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_104_tail_index_diff_lower_upper_log_ret_252d_d2},
    "f43_trve_105_worst_drawdown_504d_log_close_d2": {"inputs": ["close"], "func": f43_trve_105_worst_drawdown_504d_log_close_d2},
    "f43_trve_106_recovery_rate_post_dd_log_252d_d2": {"inputs": ["close"], "func": f43_trve_106_recovery_rate_post_dd_log_252d_d2},
    "f43_trve_107_time_to_recovery_from_max_dd_log_252d_d2": {"inputs": ["close"], "func": f43_trve_107_time_to_recovery_from_max_dd_log_252d_d2},
    "f43_trve_108_drawdown_volatility_log_252d_d2": {"inputs": ["close"], "func": f43_trve_108_drawdown_volatility_log_252d_d2},
    "f43_trve_109_stress_loss_3sigma_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_109_stress_loss_3sigma_log_ret_252d_d2},
    "f43_trve_110_stress_loss_5sigma_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_110_stress_loss_5sigma_log_ret_252d_d2},
    "f43_trve_111_mean_loss_top_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_111_mean_loss_top_5pct_log_ret_252d_d2},
    "f43_trve_112_mean_gain_top_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_112_mean_gain_top_5pct_log_ret_252d_d2},
    "f43_trve_113_loss_to_gain_ratio_extreme_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_113_loss_to_gain_ratio_extreme_5pct_log_ret_252d_d2},
    "f43_trve_114_expected_tail_loss_share_total_loss_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_114_expected_tail_loss_share_total_loss_log_ret_252d_d2},
    "f43_trve_115_tail_loss_share_top_1pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_115_tail_loss_share_top_1pct_log_ret_252d_d2},
    "f43_trve_116_tail_gain_share_top_1pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_116_tail_gain_share_top_1pct_log_ret_252d_d2},
    "f43_trve_117_var_term_struct_slope_63_252d_d2": {"inputs": ["close"], "func": f43_trve_117_var_term_struct_slope_63_252d_d2},
    "f43_trve_118_var_term_struct_slope_21_252d_d2": {"inputs": ["close"], "func": f43_trve_118_var_term_struct_slope_21_252d_d2},
    "f43_trve_119_es_term_struct_slope_63_252d_d2": {"inputs": ["close"], "func": f43_trve_119_es_term_struct_slope_63_252d_d2},
    "f43_trve_120_var_acceleration_term_struct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_120_var_acceleration_term_struct_log_ret_252d_d2},
    "f43_trve_121_var_to_vol_ratio_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_121_var_to_vol_ratio_95_log_ret_252d_d2},
    "f43_trve_122_es_to_var_ratio_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_122_es_to_var_ratio_95_log_ret_252d_d2},
    "f43_trve_123_amihud_weighted_var_95_log_ret_252d_d2": {"inputs": ["close", "volume"], "func": f43_trve_123_amihud_weighted_var_95_log_ret_252d_d2},
    "f43_trve_124_range_to_var_ratio_log_ret_252d_d2": {"inputs": ["high", "low", "close"], "func": f43_trve_124_range_to_var_ratio_log_ret_252d_d2},
    "f43_trve_125_atr_to_var_ratio_log_ret_252d_d2": {"inputs": ["high", "low", "close"], "func": f43_trve_125_atr_to_var_ratio_log_ret_252d_d2},
    "f43_trve_126_var_intraday_atr_norm_log_ret_252d_d2": {"inputs": ["high", "low", "close"], "func": f43_trve_126_var_intraday_atr_norm_log_ret_252d_d2},
    "f43_trve_127_var_jumps_only_252d_d2": {"inputs": ["close"], "func": f43_trve_127_var_jumps_only_252d_d2},
    "f43_trve_128_var_continuous_only_252d_d2": {"inputs": ["close"], "func": f43_trve_128_var_continuous_only_252d_d2},
    "f43_trve_129_ncskew_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_129_ncskew_log_ret_252d_d2},
    "f43_trve_130_duvol_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_130_duvol_log_ret_252d_d2},
    "f43_trve_131_crash_indicator_3sigma_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_131_crash_indicator_3sigma_log_ret_252d_d2},
    "f43_trve_132_probability_neg_extreme_3sigma_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_132_probability_neg_extreme_3sigma_log_ret_252d_d2},
    "f43_trve_133_left_tail_density_norm_p10_252d_d2": {"inputs": ["close"], "func": f43_trve_133_left_tail_density_norm_p10_252d_d2},
    "f43_trve_134_third_central_moment_neg_only_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_134_third_central_moment_neg_only_log_ret_252d_d2},
    "f43_trve_135_pareto_alpha_estimator_lower_5pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_135_pareto_alpha_estimator_lower_5pct_log_ret_252d_d2},
    "f43_trve_136_pareto_alpha_estimator_lower_10pct_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_136_pareto_alpha_estimator_lower_10pct_log_ret_252d_d2},
    "f43_trve_137_log_log_tail_slope_lower_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_137_log_log_tail_slope_lower_log_ret_252d_d2},
    "f43_trve_138_tail_thickness_index_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_138_tail_thickness_index_log_ret_252d_d2},
    "f43_trve_139_heavy_tail_test_chebyshev_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_139_heavy_tail_test_chebyshev_log_ret_252d_d2},
    "f43_trve_140_extreme_event_density_per_year_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_140_extreme_event_density_per_year_log_ret_252d_d2},
    "f43_trve_141_spectral_coherent_var_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_141_spectral_coherent_var_95_log_ret_252d_d2},
    "f43_trve_142_weighted_var_exponential_decay_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_142_weighted_var_exponential_decay_log_ret_252d_d2},
    "f43_trve_143_truncated_var_extreme_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_143_truncated_var_extreme_log_ret_252d_d2},
    "f43_trve_144_shortfall_dispersion_95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_144_shortfall_dispersion_95_log_ret_252d_d2},
    "f43_trve_145_tail_concentration_risk_index_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_145_tail_concentration_risk_index_log_ret_252d_d2},
    "f43_trve_146_mean_excess_function_at_var95_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_146_mean_excess_function_at_var95_log_ret_252d_d2},
    "f43_trve_147_composite_tail_risk_zscore_var_es_dd_252d_d2": {"inputs": ["close"], "func": f43_trve_147_composite_tail_risk_zscore_var_es_dd_252d_d2},
    "f43_trve_148_tail_stability_index_rolling_var_std_252d_d2": {"inputs": ["close"], "func": f43_trve_148_tail_stability_index_rolling_var_std_252d_d2},
    "f43_trve_149_var_innovation_log_ret_252d_d2": {"inputs": ["close"], "func": f43_trve_149_var_innovation_log_ret_252d_d2},
    "f43_trve_150_crash_prone_composite_indicator_252d_d2": {"inputs": ["close"], "func": f43_trve_150_crash_prone_composite_indicator_252d_d2},
}
