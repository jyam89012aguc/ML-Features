"""tail_risk_var_es d1 features 001-075 - Pipeline 1b-technical.

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


def f43_trve_001_hist_var_95_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Historical 95% VaR of log-returns over 63d - positive loss magnitude."""
    r = _log_ret(close)
    return (_hist_var(r, QDAYS, 0.95)).diff()

def f43_trve_002_hist_var_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 95% VaR over 252d."""
    r = _log_ret(close)
    return (_hist_var(r, YDAYS, 0.95)).diff()

def f43_trve_003_hist_var_99_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Historical 99% VaR over 63d."""
    r = _log_ret(close)
    return (_hist_var(r, QDAYS, 0.99)).diff()

def f43_trve_004_hist_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 99% VaR over 252d."""
    r = _log_ret(close)
    return (_hist_var(r, YDAYS, 0.99)).diff()

def f43_trve_005_hist_var_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 99.5% VaR over 252d."""
    r = _log_ret(close)
    return (_hist_var(r, YDAYS, 0.995)).diff()

def f43_trve_006_hist_upside_var_95_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Upper-tail 'VaR' (97.5th percentile of returns) over 63d."""
    r = _log_ret(close)
    return (_rolling_q(r, QDAYS, 0.95)).diff()

def f43_trve_007_hist_upside_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Upper-tail VaR (99th percentile) over 252d."""
    r = _log_ret(close)
    return (_rolling_q(r, YDAYS, 0.99)).diff()

def f43_trve_008_hist_var_95_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Historical 95% VaR over 504d."""
    r = _log_ret(close)
    return (_hist_var(r, DDAYS_2Y, 0.95)).diff()

def f43_trve_009_hist_var_99_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    """Historical 99% VaR over 504d."""
    r = _log_ret(close)
    return (_hist_var(r, DDAYS_2Y, 0.99)).diff()

def f43_trve_010_hist_es_95_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Historical 95% ES (CVaR) of log-returns over 63d."""
    r = _log_ret(close)
    return (_hist_es(r, QDAYS, 0.95)).diff()

def f43_trve_011_hist_es_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 95% ES over 252d."""
    r = _log_ret(close)
    return (_hist_es(r, YDAYS, 0.95)).diff()

def f43_trve_012_hist_es_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 99% ES over 252d."""
    r = _log_ret(close)
    return (_hist_es(r, YDAYS, 0.99)).diff()

def f43_trve_013_hist_es_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Historical 99.5% ES over 252d."""
    r = _log_ret(close)
    return (_hist_es(r, YDAYS, 0.995)).diff()

def f43_trve_014_hist_upside_es_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of upper-tail returns above 95th percentile over 252d."""
    r = _log_ret(close)
    return (_hist_upside_es(r, YDAYS, 0.95)).diff()

def f43_trve_015_hist_upside_es_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of upper-tail returns above 99th percentile over 252d."""
    r = _log_ret(close)
    return (_hist_upside_es(r, YDAYS, 0.99)).diff()

def f43_trve_016_param_norm_var_95_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 95% VaR over 63d."""
    r = _log_ret(close)
    return (_param_norm_var(r, QDAYS, 0.95)).diff()

def f43_trve_017_param_norm_var_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 95% VaR over 252d."""
    r = _log_ret(close)
    return (_param_norm_var(r, YDAYS, 0.95)).diff()

def f43_trve_018_param_norm_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 99% VaR over 252d."""
    r = _log_ret(close)
    return (_param_norm_var(r, YDAYS, 0.99)).diff()

def f43_trve_019_param_norm_es_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 95% ES over 252d."""
    r = _log_ret(close)
    return (_param_norm_es(r, YDAYS, 0.95)).diff()

def f43_trve_020_param_norm_es_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 99% ES over 252d."""
    r = _log_ret(close)
    return (_param_norm_es(r, YDAYS, 0.99)).diff()

def f43_trve_021_param_norm_es_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric normal 99.5% ES over 252d."""
    r = _log_ret(close)
    return (_param_norm_es(r, YDAYS, 0.995)).diff()

def f43_trve_022_cornish_fisher_var_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 95% VaR over 252d (skew/kurt-adjusted normal VaR)."""
    r = _log_ret(close)
    return (_cornish_fisher_var(r, YDAYS, 0.95)).diff()

def f43_trve_023_cornish_fisher_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 99% VaR over 252d."""
    r = _log_ret(close)
    return (_cornish_fisher_var(r, YDAYS, 0.99)).diff()

def f43_trve_024_cornish_fisher_var_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 99.5% VaR over 252d."""
    r = _log_ret(close)
    return (_cornish_fisher_var(r, YDAYS, 0.995)).diff()

def f43_trve_025_cornish_fisher_es_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 95% ES approximation over 252d."""
    r = _log_ret(close)
    return (_cornish_fisher_es(r, YDAYS, 0.95)).diff()

def f43_trve_026_cornish_fisher_es_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 99% ES over 252d."""
    r = _log_ret(close)
    return (_cornish_fisher_es(r, YDAYS, 0.99)).diff()

def f43_trve_027_cornish_fisher_es_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher 99.5% ES over 252d."""
    r = _log_ret(close)
    return (_cornish_fisher_es(r, YDAYS, 0.995)).diff()

def f43_trve_028_modified_var_skew_adj_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR 95% minus normal VaR 95% over 252d - skew/kurt contribution."""
    r = _log_ret(close)
    cf = _cornish_fisher_var(r, YDAYS, 0.95)
    norm = _param_norm_var(r, YDAYS, 0.95)
    return (cf - norm).diff()

def f43_trve_029_modified_var_kurt_adj_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR 99% minus normal VaR 99% over 252d."""
    r = _log_ret(close)
    cf = _cornish_fisher_var(r, YDAYS, 0.99)
    norm = _param_norm_var(r, YDAYS, 0.99)
    return (cf - norm).diff()

def f43_trve_030_modified_var_skew_kurt_total_adj_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR 99.5% minus normal VaR 99.5% over 252d."""
    r = _log_ret(close)
    cf = _cornish_fisher_var(r, YDAYS, 0.995)
    norm = _param_norm_var(r, YDAYS, 0.995)
    return (cf - norm).diff()

def f43_trve_031_param_minus_hist_var_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric VaR 95% minus historical VaR 95% over 252d - model misfit."""
    r = _log_ret(close)
    p = _param_norm_var(r, YDAYS, 0.95)
    h = _hist_var(r, YDAYS, 0.95)
    return (p - h).diff()

def f43_trve_032_param_minus_hist_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric minus historical VaR 99% over 252d."""
    r = _log_ret(close)
    p = _param_norm_var(r, YDAYS, 0.99)
    h = _hist_var(r, YDAYS, 0.99)
    return (p - h).diff()

def f43_trve_033_param_minus_hist_es_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Parametric minus historical ES 95% over 252d."""
    r = _log_ret(close)
    p = _param_norm_es(r, YDAYS, 0.95)
    h = _hist_es(r, YDAYS, 0.95)
    return (p - h).diff()

def f43_trve_034_param_t5_var_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t(df=5) parametric 95% VaR over 252d."""
    r = _log_ret(close)
    return (_param_t_var(r, YDAYS, 0.95, 5)).diff()

def f43_trve_035_param_t5_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t(df=5) parametric 99% VaR over 252d."""
    r = _log_ret(close)
    return (_param_t_var(r, YDAYS, 0.99, 5)).diff()

def f43_trve_036_param_t5_var_995_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t(df=5) parametric 99.5% VaR over 252d."""
    r = _log_ret(close)
    return (_param_t_var(r, YDAYS, 0.995, 5)).diff()

def f43_trve_037_param_t10_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t(df=10) 99% VaR over 252d - lighter tail than df=5."""
    r = _log_ret(close)
    return (_param_t_var(r, YDAYS, 0.99, 10)).diff()

def f43_trve_038_param_t_fitted_df_from_kurt_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Implied Student-t df from sample excess kurtosis over 252d (df=4+6/k)."""
    r = _log_ret(close)
    return (_kurt_implied_df(r, YDAYS)).diff()

def f43_trve_039_param_t20_var_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Student-t(df=20) 99% VaR over 252d - approximately normal-like."""
    r = _log_ret(close)
    return (_param_t_var(r, YDAYS, 0.99, 20)).diff()

def f43_trve_040_pot_threshold_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """POT threshold (95th-percentile loss) of log-returns over 252d."""
    r = _log_ret(close)
    return (_pot_threshold(r, YDAYS, 0.95)).diff()

def f43_trve_041_pot_mean_excess_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess over 95th-percentile loss threshold over 252d - GPD-flavored summary."""
    r = _log_ret(close)
    return (_pot_mean_excess(r, YDAYS, 0.95)).diff()

def f43_trve_042_pot_mean_excess_99_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess over 99th-percentile loss threshold over 252d."""
    r = _log_ret(close)
    return (_pot_mean_excess(r, YDAYS, 0.99)).diff()

def f43_trve_043_pot_gpd_shape_xi_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Method-of-moments GPD shape xi over 252d - tail-thickness parameter."""
    r = _log_ret(close)
    return (_pot_gpd_shape(r, YDAYS, 0.95)).diff()

def f43_trve_044_pot_gpd_scale_beta_95_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Method-of-moments GPD scale beta over 252d."""
    r = _log_ret(close)
    return (_pot_gpd_scale(r, YDAYS, 0.95)).diff()

def f43_trve_045_pot_var_99_GPD_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """POT-implied 99% VaR using GPD: u + (beta/xi)*((n/(n-Nu)*(1-0.99))^(-xi) - 1) - simplified."""
    r = _log_ret(close)
    u = _pot_threshold(r, YDAYS, 0.95)
    xi = _pot_gpd_shape(r, YDAYS, 0.95)
    beta = _pot_gpd_scale(r, YDAYS, 0.95)
    # Simplified: assume Nu/n ~ 0.05 (since threshold is at 95th pct)
    ratio = pd.Series(0.05 / 0.01, index=close.index)
    term = ratio.pow(xi) - 1.0
    var = u + _safe_div(beta, xi) * term
    return (var).diff()

def f43_trve_046_max_log_loss_5d_in_252d_window_d1(close: pd.Series) -> pd.Series:
    """Worst 5-day cumulative log-loss within 252d window."""
    r = _log_ret(close)
    rf = r.rolling(5).sum()
    return (-(rf.rolling(YDAYS, min_periods=QDAYS).min())).diff()

def f43_trve_047_max_log_loss_21d_in_252d_window_d1(close: pd.Series) -> pd.Series:
    """Worst 21-day cumulative log-loss within 252d window."""
    r = _log_ret(close)
    rf = r.rolling(21).sum()
    return (-(rf.rolling(YDAYS, min_periods=QDAYS).min())).diff()

def f43_trve_048_max_log_loss_63d_in_252d_window_d1(close: pd.Series) -> pd.Series:
    """Worst 63-day cumulative log-loss within 252d window."""
    r = _log_ret(close)
    rf = r.rolling(63).sum()
    return (-(rf.rolling(YDAYS, min_periods=QDAYS).min())).diff()

def f43_trve_049_min_daily_log_ret_in_252d_d1(close: pd.Series) -> pd.Series:
    """Single worst daily log-return within 252d."""
    r = _log_ret(close)
    return (-(r.rolling(YDAYS, min_periods=QDAYS).min())).diff()

def f43_trve_050_mean_monthly_min_daily_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of rolling-21d minimum daily log-return over 252d - typical monthly bad day."""
    r = _log_ret(close)
    mn = r.rolling(21, min_periods=10).min()
    return (-(mn.rolling(YDAYS, min_periods=QDAYS).mean())).diff()

def f43_trve_051_expected_block_max_loss_gumbel_proxy_252d_d1(close: pd.Series) -> pd.Series:
    """Gumbel-proxy: mean(monthly worst loss) + std(monthly worst loss) over 252d."""
    r = _log_ret(close)
    mn = r.rolling(21, min_periods=10).min()
    mu = mn.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = mn.rolling(YDAYS, min_periods=QDAYS).std()
    return (-(mu - sd)).diff()

def f43_trve_052_max_drawdown_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Maximum log-drawdown over 252d (negative value)."""
    return (_rolling_max_drawdown(close, YDAYS)).diff()

def f43_trve_053_max_drawdown_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Maximum log-drawdown over 504d."""
    return (_rolling_max_drawdown(close, DDAYS_2Y)).diff()

def f43_trve_054_mean_drawdown_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Mean log-drawdown over 252d."""
    return (_rolling_mean_drawdown(close, YDAYS)).diff()

def f43_trve_055_drawdown_duration_max_252d_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive bars in drawdown over 252d."""
    return (_drawdown_duration_max(close, YDAYS)).diff()

def f43_trve_056_drawdown_duration_max_504d_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive bars in drawdown over 504d."""
    return (_drawdown_duration_max(close, DDAYS_2Y)).diff()

def f43_trve_057_ulcer_index_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Ulcer index = RMS of drawdown depths over 252d."""
    return (_ulcer_index(close, YDAYS)).diff()

def f43_trve_058_cdar_95_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Conditional Drawdown at Risk at 95% over 252d."""
    return (_cdar(close, YDAYS, 0.95)).diff()

def f43_trve_059_cdar_99_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """CDaR at 99% over 252d."""
    return (_cdar(close, YDAYS, 0.99)).diff()

def f43_trve_060_cdar_95_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """CDaR at 95% over 504d."""
    return (_cdar(close, DDAYS_2Y, 0.95)).diff()

def f43_trve_061_avg_top_5_drawdowns_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Mean of top-5 (worst) drawdown magnitudes over 252d."""
    lc = _safe_log(close)
    def _t5(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        dd = -(v - cm)
        top = np.sort(dd)[-5:]
        return float(top.mean())
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_t5, raw=True)
    return (res).diff()

def f43_trve_062_ulcer_index_log_close_504d_d1(close: pd.Series) -> pd.Series:
    """Ulcer index over 504d - long-horizon RMS drawdown."""
    return (_ulcer_index(close, DDAYS_2Y)).diff()

def f43_trve_063_pain_index_log_close_252d_d1(close: pd.Series) -> pd.Series:
    """Mean drawdown magnitude (Pain Index) over 252d."""
    lc = _safe_log(close)
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    res = lc.rolling(YDAYS, min_periods=QDAYS).apply(_pi, raw=True)
    return (res).diff()

def f43_trve_064_lpm_order2_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Lower partial moment (order 2) of log-returns vs zero threshold over 252d."""
    r = _log_ret(close)
    neg = (-r).clip(lower=0.0)
    return ((neg ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f43_trve_065_lpm_order1_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Lower partial moment (order 1) of log-returns over 252d."""
    r = _log_ret(close)
    neg = (-r).clip(lower=0.0)
    return (neg.rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f43_trve_066_lpm_order3_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Lower partial moment (order 3) of log-returns over 252d."""
    r = _log_ret(close)
    neg = (-r).clip(lower=0.0)
    return ((neg ** 3).rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f43_trve_067_upm_order2_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Upper partial moment (order 2) of log-returns over 252d."""
    r = _log_ret(close)
    pos = r.clip(lower=0.0)
    return ((pos ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f43_trve_068_lpm_to_upm_ratio_order2_252d_d1(close: pd.Series) -> pd.Series:
    """Ratio LPM2/UPM2 over 252d - downside vs upside variance ratio."""
    r = _log_ret(close)
    neg = (-r).clip(lower=0.0); pos = r.clip(lower=0.0)
    lpm = (neg ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    upm = (pos ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(lpm, upm)).diff()

def f43_trve_069_omega_ratio_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Omega ratio at threshold 0: UPM1/LPM1 over 252d."""
    r = _log_ret(close)
    neg = (-r).clip(lower=0.0); pos = r.clip(lower=0.0)
    upm1 = pos.rolling(YDAYS, min_periods=QDAYS).mean()
    lpm1 = neg.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(upm1, lpm1)).diff()

def f43_trve_070_sortino_ratio_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    """Sortino: mean(log_ret) / downside-semidev over 252d."""
    r = _log_ret(close)
    mu = r.rolling(YDAYS, min_periods=QDAYS).mean()
    neg = (-r).clip(lower=0.0)
    dd = np.sqrt((neg ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return (_safe_div(mu, dd)).diff()

def f43_trve_071_calmar_ratio_log_252d_d1(close: pd.Series) -> pd.Series:
    """Calmar: annualized return / |max-drawdown| over 252d."""
    r = _log_ret(close)
    ann = r.rolling(YDAYS, min_periods=QDAYS).mean() * YDAYS
    mdd = -_rolling_max_drawdown(close, YDAYS)
    return (_safe_div(ann, mdd)).diff()

def f43_trve_072_sterling_ratio_log_252d_d1(close: pd.Series) -> pd.Series:
    """Sterling: annualized return / (avg of top-N drawdowns + 10%) over 252d (here use top-3 + 0.1)."""
    r = _log_ret(close)
    ann = r.rolling(YDAYS, min_periods=QDAYS).mean() * YDAYS
    lc = _safe_log(close)
    def _avg3(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v); dd = -(v - cm)
        return float(np.sort(dd)[-3:].mean())
    avg = lc.rolling(YDAYS, min_periods=QDAYS).apply(_avg3, raw=True) + 0.10
    return (_safe_div(ann, avg)).diff()

def f43_trve_073_burke_ratio_log_252d_d1(close: pd.Series) -> pd.Series:
    """Burke: annualized return / sqrt(sum of squared top-N drawdowns) over 252d."""
    r = _log_ret(close)
    ann = r.rolling(YDAYS, min_periods=QDAYS).mean() * YDAYS
    lc = _safe_log(close)
    def _br(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v); dd = -(v - cm)
        top = np.sort(dd)[-5:]
        return float(np.sqrt((top ** 2).sum()))
    den = lc.rolling(YDAYS, min_periods=QDAYS).apply(_br, raw=True)
    return (_safe_div(ann, den)).diff()

def f43_trve_074_martin_ratio_log_252d_d1(close: pd.Series) -> pd.Series:
    """Martin (Ulcer-adjusted Sharpe): annualized return / Ulcer over 252d."""
    r = _log_ret(close)
    ann = r.rolling(YDAYS, min_periods=QDAYS).mean() * YDAYS
    ulc = _ulcer_index(close, YDAYS)
    return (_safe_div(ann, ulc)).diff()

def f43_trve_075_pain_ratio_log_252d_d1(close: pd.Series) -> pd.Series:
    """Pain ratio: annualized return / pain index (mean drawdown) over 252d."""
    r = _log_ret(close)
    ann = r.rolling(YDAYS, min_periods=QDAYS).mean() * YDAYS
    lc = _safe_log(close)
    def _pi(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        cm = np.maximum.accumulate(v)
        return float((-(v - cm)).mean())
    pain = lc.rolling(YDAYS, min_periods=QDAYS).apply(_pi, raw=True)
    return (_safe_div(ann, pain)).diff()


# ============================================================
#                         REGISTRY 001_075 (d1)
# ============================================================

TAIL_RISK_VAR_ES_D1_REGISTRY_001_075 = {
    "f43_trve_001_hist_var_95_log_ret_63d_d1": {"inputs": ["close"], "func": f43_trve_001_hist_var_95_log_ret_63d_d1},
    "f43_trve_002_hist_var_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_002_hist_var_95_log_ret_252d_d1},
    "f43_trve_003_hist_var_99_log_ret_63d_d1": {"inputs": ["close"], "func": f43_trve_003_hist_var_99_log_ret_63d_d1},
    "f43_trve_004_hist_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_004_hist_var_99_log_ret_252d_d1},
    "f43_trve_005_hist_var_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_005_hist_var_995_log_ret_252d_d1},
    "f43_trve_006_hist_upside_var_95_log_ret_63d_d1": {"inputs": ["close"], "func": f43_trve_006_hist_upside_var_95_log_ret_63d_d1},
    "f43_trve_007_hist_upside_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_007_hist_upside_var_99_log_ret_252d_d1},
    "f43_trve_008_hist_var_95_log_ret_504d_d1": {"inputs": ["close"], "func": f43_trve_008_hist_var_95_log_ret_504d_d1},
    "f43_trve_009_hist_var_99_log_ret_504d_d1": {"inputs": ["close"], "func": f43_trve_009_hist_var_99_log_ret_504d_d1},
    "f43_trve_010_hist_es_95_log_ret_63d_d1": {"inputs": ["close"], "func": f43_trve_010_hist_es_95_log_ret_63d_d1},
    "f43_trve_011_hist_es_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_011_hist_es_95_log_ret_252d_d1},
    "f43_trve_012_hist_es_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_012_hist_es_99_log_ret_252d_d1},
    "f43_trve_013_hist_es_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_013_hist_es_995_log_ret_252d_d1},
    "f43_trve_014_hist_upside_es_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_014_hist_upside_es_95_log_ret_252d_d1},
    "f43_trve_015_hist_upside_es_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_015_hist_upside_es_99_log_ret_252d_d1},
    "f43_trve_016_param_norm_var_95_log_ret_63d_d1": {"inputs": ["close"], "func": f43_trve_016_param_norm_var_95_log_ret_63d_d1},
    "f43_trve_017_param_norm_var_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_017_param_norm_var_95_log_ret_252d_d1},
    "f43_trve_018_param_norm_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_018_param_norm_var_99_log_ret_252d_d1},
    "f43_trve_019_param_norm_es_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_019_param_norm_es_95_log_ret_252d_d1},
    "f43_trve_020_param_norm_es_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_020_param_norm_es_99_log_ret_252d_d1},
    "f43_trve_021_param_norm_es_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_021_param_norm_es_995_log_ret_252d_d1},
    "f43_trve_022_cornish_fisher_var_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_022_cornish_fisher_var_95_log_ret_252d_d1},
    "f43_trve_023_cornish_fisher_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_023_cornish_fisher_var_99_log_ret_252d_d1},
    "f43_trve_024_cornish_fisher_var_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_024_cornish_fisher_var_995_log_ret_252d_d1},
    "f43_trve_025_cornish_fisher_es_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_025_cornish_fisher_es_95_log_ret_252d_d1},
    "f43_trve_026_cornish_fisher_es_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_026_cornish_fisher_es_99_log_ret_252d_d1},
    "f43_trve_027_cornish_fisher_es_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_027_cornish_fisher_es_995_log_ret_252d_d1},
    "f43_trve_028_modified_var_skew_adj_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_028_modified_var_skew_adj_95_log_ret_252d_d1},
    "f43_trve_029_modified_var_kurt_adj_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_029_modified_var_kurt_adj_99_log_ret_252d_d1},
    "f43_trve_030_modified_var_skew_kurt_total_adj_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_030_modified_var_skew_kurt_total_adj_995_log_ret_252d_d1},
    "f43_trve_031_param_minus_hist_var_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_031_param_minus_hist_var_95_log_ret_252d_d1},
    "f43_trve_032_param_minus_hist_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_032_param_minus_hist_var_99_log_ret_252d_d1},
    "f43_trve_033_param_minus_hist_es_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_033_param_minus_hist_es_95_log_ret_252d_d1},
    "f43_trve_034_param_t5_var_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_034_param_t5_var_95_log_ret_252d_d1},
    "f43_trve_035_param_t5_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_035_param_t5_var_99_log_ret_252d_d1},
    "f43_trve_036_param_t5_var_995_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_036_param_t5_var_995_log_ret_252d_d1},
    "f43_trve_037_param_t10_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_037_param_t10_var_99_log_ret_252d_d1},
    "f43_trve_038_param_t_fitted_df_from_kurt_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_038_param_t_fitted_df_from_kurt_log_ret_252d_d1},
    "f43_trve_039_param_t20_var_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_039_param_t20_var_99_log_ret_252d_d1},
    "f43_trve_040_pot_threshold_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_040_pot_threshold_95_log_ret_252d_d1},
    "f43_trve_041_pot_mean_excess_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_041_pot_mean_excess_95_log_ret_252d_d1},
    "f43_trve_042_pot_mean_excess_99_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_042_pot_mean_excess_99_log_ret_252d_d1},
    "f43_trve_043_pot_gpd_shape_xi_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_043_pot_gpd_shape_xi_95_log_ret_252d_d1},
    "f43_trve_044_pot_gpd_scale_beta_95_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_044_pot_gpd_scale_beta_95_log_ret_252d_d1},
    "f43_trve_045_pot_var_99_GPD_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_045_pot_var_99_GPD_log_ret_252d_d1},
    "f43_trve_046_max_log_loss_5d_in_252d_window_d1": {"inputs": ["close"], "func": f43_trve_046_max_log_loss_5d_in_252d_window_d1},
    "f43_trve_047_max_log_loss_21d_in_252d_window_d1": {"inputs": ["close"], "func": f43_trve_047_max_log_loss_21d_in_252d_window_d1},
    "f43_trve_048_max_log_loss_63d_in_252d_window_d1": {"inputs": ["close"], "func": f43_trve_048_max_log_loss_63d_in_252d_window_d1},
    "f43_trve_049_min_daily_log_ret_in_252d_d1": {"inputs": ["close"], "func": f43_trve_049_min_daily_log_ret_in_252d_d1},
    "f43_trve_050_mean_monthly_min_daily_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_050_mean_monthly_min_daily_log_ret_252d_d1},
    "f43_trve_051_expected_block_max_loss_gumbel_proxy_252d_d1": {"inputs": ["close"], "func": f43_trve_051_expected_block_max_loss_gumbel_proxy_252d_d1},
    "f43_trve_052_max_drawdown_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_052_max_drawdown_log_close_252d_d1},
    "f43_trve_053_max_drawdown_log_close_504d_d1": {"inputs": ["close"], "func": f43_trve_053_max_drawdown_log_close_504d_d1},
    "f43_trve_054_mean_drawdown_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_054_mean_drawdown_log_close_252d_d1},
    "f43_trve_055_drawdown_duration_max_252d_d1": {"inputs": ["close"], "func": f43_trve_055_drawdown_duration_max_252d_d1},
    "f43_trve_056_drawdown_duration_max_504d_d1": {"inputs": ["close"], "func": f43_trve_056_drawdown_duration_max_504d_d1},
    "f43_trve_057_ulcer_index_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_057_ulcer_index_log_close_252d_d1},
    "f43_trve_058_cdar_95_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_058_cdar_95_log_close_252d_d1},
    "f43_trve_059_cdar_99_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_059_cdar_99_log_close_252d_d1},
    "f43_trve_060_cdar_95_log_close_504d_d1": {"inputs": ["close"], "func": f43_trve_060_cdar_95_log_close_504d_d1},
    "f43_trve_061_avg_top_5_drawdowns_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_061_avg_top_5_drawdowns_log_close_252d_d1},
    "f43_trve_062_ulcer_index_log_close_504d_d1": {"inputs": ["close"], "func": f43_trve_062_ulcer_index_log_close_504d_d1},
    "f43_trve_063_pain_index_log_close_252d_d1": {"inputs": ["close"], "func": f43_trve_063_pain_index_log_close_252d_d1},
    "f43_trve_064_lpm_order2_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_064_lpm_order2_log_ret_252d_d1},
    "f43_trve_065_lpm_order1_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_065_lpm_order1_log_ret_252d_d1},
    "f43_trve_066_lpm_order3_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_066_lpm_order3_log_ret_252d_d1},
    "f43_trve_067_upm_order2_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_067_upm_order2_log_ret_252d_d1},
    "f43_trve_068_lpm_to_upm_ratio_order2_252d_d1": {"inputs": ["close"], "func": f43_trve_068_lpm_to_upm_ratio_order2_252d_d1},
    "f43_trve_069_omega_ratio_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_069_omega_ratio_log_ret_252d_d1},
    "f43_trve_070_sortino_ratio_log_ret_252d_d1": {"inputs": ["close"], "func": f43_trve_070_sortino_ratio_log_ret_252d_d1},
    "f43_trve_071_calmar_ratio_log_252d_d1": {"inputs": ["close"], "func": f43_trve_071_calmar_ratio_log_252d_d1},
    "f43_trve_072_sterling_ratio_log_252d_d1": {"inputs": ["close"], "func": f43_trve_072_sterling_ratio_log_252d_d1},
    "f43_trve_073_burke_ratio_log_252d_d1": {"inputs": ["close"], "func": f43_trve_073_burke_ratio_log_252d_d1},
    "f43_trve_074_martin_ratio_log_252d_d1": {"inputs": ["close"], "func": f43_trve_074_martin_ratio_log_252d_d1},
    "f43_trve_075_pain_ratio_log_252d_d1": {"inputs": ["close"], "func": f43_trve_075_pain_ratio_log_252d_d1},
}
