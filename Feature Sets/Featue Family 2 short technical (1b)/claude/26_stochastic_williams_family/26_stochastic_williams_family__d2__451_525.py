"""26_stochastic_williams_family d2 features 451-525 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()

def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)

def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k

def _stoch_d(k, n_d):
    return k.rolling(n_d, min_periods=max(n_d // 2, 1)).mean()

def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)

def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_rsi_k(close, n_rsi=14, n_k=14, smooth_k=3):
    r = _rsi(close, n_rsi)
    ll = r.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = r.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    return raw_k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()

def _rsi_on_series(s, n=14):
    """RSI applied to an arbitrary series (not just close)."""
    delta = s.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_on_series(s, n, smooth_k=1):
    """Stochastic K applied to an arbitrary series."""
    ll = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = s.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(s - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k

def _macd_on_series(s, fast=12, slow=26, signal=9):
    """MACD line + signal applied to arbitrary series."""
    ema_f = _ema(s, fast)
    ema_s = _ema(s, slow)
    macd = ema_f - ema_s
    sig = _ema(macd, signal)
    return (macd, sig)

def _trix_on_series(s, n=15):
    """TRIX applied to arbitrary series — 1-bar % change of triple-EMA."""
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return _safe_div(e3.diff(), e3.shift(1)) * 100.0

def _tsi_on_series(s, r=25, ssp=13):
    """True Strength Index on arbitrary series."""
    m = s.diff()
    e1 = _ema(m, r)
    e2 = _ema(e1, ssp)
    a1 = _ema(m.abs(), r)
    a2 = _ema(a1, ssp)
    return 100.0 * _safe_div(e2, a2)

def _cci_on_series(s, n=20):
    """CCI applied to arbitrary series."""
    m = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    md = (s - m).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(s - m, 0.015 * md)

def _cmo_on_series(s, n=14):
    """Chande Momentum Oscillator on arbitrary series."""
    d = s.diff()
    up = d.clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    dn = (-d).clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(up - dn, up + dn)

def _williams_r_on_series(s, n):
    """Williams %R on arbitrary series (treats series as both high/low/close)."""
    ll = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - s, hh - ll)

def _running_dd_pct(price, window=DDAYS_5Y):
    """Drawdown percent from running max within `window`."""
    rmax = price.rolling(window, min_periods=QDAYS).max()
    return (1.0 - _safe_div(price, rmax)) * 100.0

def _cond_mean(value, mask, window):
    """Rolling mean of `value` over bars where `mask` is True within `window`."""
    v = value.where(mask, np.nan)
    return v.rolling(window, min_periods=max(window // 4, 2)).mean()

def _cond_std(value, mask, window):
    v = value.where(mask, np.nan)
    return v.rolling(window, min_periods=max(window // 4, 2)).std()

def _quantile_rolling(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)

def _rolling_corr(a, b, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return a.rolling(n, min_periods=min_periods).corr(b)

def _rolling_beta(a, b, n, min_periods=None):
    """Beta = Cov(a,b)/Var(b)."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    cov = a.rolling(n, min_periods=min_periods).cov(b)
    var = b.rolling(n, min_periods=min_periods).var()
    return _safe_div(cov, var)

def _rolling_residual(a, b, n):
    """Residual of a from a = alpha + beta*b regression in rolling window."""
    beta = _rolling_beta(a, b, n)
    a_m = a.rolling(n, min_periods=max(n // 3, 2)).mean()
    b_m = b.rolling(n, min_periods=max(n // 3, 2)).mean()
    alpha = a_m - beta * b_m
    return a - (alpha + beta * b)

def _smi_compact(high, low, close, n=14):
    mid = (high.rolling(n, min_periods=max(n // 3, 2)).max() + low.rolling(n, min_periods=max(n // 3, 2)).min()) / 2.0
    diff = close - mid
    hl = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(_ema(_ema(diff, 3), 3), 0.5 * _ema(_ema(hl, 3), 3))

def _ultimate_osc(high, low, close):
    bp = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    a7 = bp.rolling(7, min_periods=3).sum() / tr.rolling(7, min_periods=3).sum().replace(0, np.nan)
    a14 = bp.rolling(14, min_periods=5).sum() / tr.rolling(14, min_periods=5).sum().replace(0, np.nan)
    a28 = bp.rolling(28, min_periods=10).sum() / tr.rolling(28, min_periods=10).sum().replace(0, np.nan)
    return 100.0 * (4 * a7 + 2 * a14 + a28) / 7.0

def _all_oscillators(high, low, close):
    """Return dict of canonical oscillators used across composites."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    uo = _ultimate_osc(high, low, close)
    smi = _smi_compact(high, low, close, 14)
    return {'k': k, 'wr': wr, 'sk': sk, 'uo': uo, 'smi': smi}

def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)

def _normal_inv_cdf(p):
    """Approximate inverse normal CDF — Acklam-style rational approximation, vectorized."""
    p = np.clip(p, 1e-06, 1.0 - 1e-06)
    a = [-39.69683028665376, 220.9460984245205, -275.9285104469687, 138.357751867269, -30.66479806614716, 2.506628277459239]
    b = [-54.47609879822406, 161.5858368580409, -155.6989798598866, 66.80131188771972, -13.28068155288572]
    c = [-0.007784894002430293, -0.3223964580411365, -2.400758277161838, -2.549732539343734, 4.374664141464968, 2.938163982698783]
    d = [0.007784695709041462, 0.3224671290700398, 2.445134137142996, 3.754408661907416]
    plow = 0.02425
    phigh = 1.0 - plow
    out = np.zeros_like(p)
    lower = p < plow
    q = np.sqrt(-2.0 * np.log(np.where(lower, p, plow)))
    out_l = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0)
    upper = p > phigh
    q2 = np.sqrt(-2.0 * np.log(np.where(upper, 1.0 - p, plow)))
    out_u = -(((((c[0] * q2 + c[1]) * q2 + c[2]) * q2 + c[3]) * q2 + c[4]) * q2 + c[5]) / ((((d[0] * q2 + d[1]) * q2 + d[2]) * q2 + d[3]) * q2 + 1.0)
    mid = ~lower & ~upper
    q3 = np.where(mid, p - 0.5, 0.0)
    r3 = q3 * q3
    out_m = (((((a[0] * r3 + a[1]) * r3 + a[2]) * r3 + a[3]) * r3 + a[4]) * r3 + a[5]) * q3 / (((((b[0] * r3 + b[1]) * r3 + b[2]) * r3 + b[3]) * r3 + b[4]) * r3 + 1.0)
    return np.where(lower, out_l, np.where(upper, out_u, out_m))

def _quantile_normal_transform(s, window, min_periods=None):
    """Rolling rank-pct, then inverse-normal CDF — produces ~ N(0,1)-shaped values."""
    pr = _rolling_rank_pct(s, window, min_periods=min_periods)
    arr = pr.to_numpy()
    out = np.full(arr.shape, np.nan)
    m = ~np.isnan(arr)
    if m.any():
        out[m] = _normal_inv_cdf(arr[m])
    return pd.Series(out, index=s.index)

def _mad_rolling(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    return (s - med).abs().rolling(window, min_periods=min_periods).median()

def _iqr_rolling(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    q75 = s.rolling(window, min_periods=min_periods).quantile(0.75)
    q25 = s.rolling(window, min_periods=min_periods).quantile(0.25)
    return q75 - q25

def _winsorize_zscore(s, window, p_low=0.05, p_high=0.95, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    lo = s.rolling(window, min_periods=min_periods).quantile(p_low)
    hi = s.rolling(window, min_periods=min_periods).quantile(p_high)
    w = s.clip(lower=lo, upper=hi)
    m = w.rolling(window, min_periods=min_periods).mean()
    sd = w.rolling(window, min_periods=min_periods).std()
    return (w - m) / sd.replace(0, np.nan)

def _path_length(s, window):
    """Sum of |diff(s)| over window."""
    return s.diff().abs().rolling(window, min_periods=max(window // 3, 2)).sum()

def _shannon_sign_entropy(s, window):
    """Shannon entropy (base 2) of sign(diff(s)) classification — bits."""
    d = np.sign(s.diff().fillna(0))

    def _ent(w):
        if np.isnan(w).all():
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        out = 0.0
        for c in (-1.0, 0.0, 1.0):
            p = float((v == c).sum()) / float(v.size)
            if p > 0:
                out -= p * np.log2(p)
        return out
    return d.rolling(window, min_periods=max(window // 3, 2)).apply(_ent, raw=True)

def _dtw_distance_to_template(s_window, template):
    """Banded DTW (band=5) distance between window and template (numpy arrays)."""
    n = len(s_window)
    m = len(template)
    if n == 0 or m == 0:
        return np.nan
    if np.isnan(s_window).any():
        return np.nan
    band = max(5, abs(n - m))
    INF = 1e+18
    D = np.full((n + 1, m + 1), INF)
    D[0, 0] = 0.0
    for i in range(1, n + 1):
        jlo = max(1, i - band)
        jhi = min(m, i + band)
        for j in range(jlo, jhi + 1):
            cost = abs(s_window[i - 1] - template[j - 1])
            D[i, j] = cost + min(D[i - 1, j], D[i, j - 1], D[i - 1, j - 1])
    return float(D[n, m])

def _rolling_dtw_to_template(s, window, template):
    arr = s.to_numpy()
    out = np.full(arr.shape, np.nan)
    tpl = np.asarray(template, dtype=float)
    for i in range(window - 1, len(arr)):
        w = arr[i - window + 1:i + 1]
        if np.isnan(w).any():
            continue
        out[i] = _dtw_distance_to_template(w, tpl)
    return pd.Series(out, index=s.index)

def _coskew(x, y, n):
    """Co-skew(x,y) = E[(x-mx)*(y-my)^2] / (sx*sy^2)."""
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    num = ((x - mx) * (y - my) ** 2).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(num, sx * sy ** 2)

def _cokurt(x, y, n):
    """Co-kurt(x,y) = E[(x-mx)*(y-my)^3] / (sx*sy^3)."""
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    num = ((x - mx) * (y - my) ** 3).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(num, sx * sy ** 3)

def f26_stwf_451_rsi_of_stoch_k_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI(14) applied to Stoch %K(14) series — momentum of the momentum oscillator."""
    k = _stoch_k(high, low, close, 14)
    return _rsi_on_series(k, 14).diff().diff()

def f26_stwf_452_rsi_of_stoch_d_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI(14) applied to Stoch %D(14)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    return _rsi_on_series(d, 14).diff().diff()

def f26_stwf_453_stoch_of_rsi_of_stoch_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch(14) of RSI(14) of Stoch %K(14) — third-order oscillator."""
    k = _stoch_k(high, low, close, 14)
    r = _rsi_on_series(k, 14)
    return _stoch_on_series(r, 14).diff().diff()

def f26_stwf_454_macd_of_stoch_k_12_26_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD(12,26) line applied to Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    macd, _ = _macd_on_series(k, 12, 26, 9)
    return macd.diff().diff()

def f26_stwf_455_macd_of_stoch_k_signal_cross_down_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: MACD-of-K crossed BELOW its signal in the past bar."""
    k = _stoch_k(high, low, close, 14)
    macd, sig = _macd_on_series(k, 12, 26, 9)
    prev = macd.shift(1) >= sig.shift(1)
    now = macd < sig
    return (prev & now).astype(float).where(close.notna(), np.nan).diff().diff()

def f26_stwf_456_macd_of_williams_r_12_26_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD(12,26) applied to Williams %R(14)."""
    wr = _williams_r(high, low, close, 14)
    macd, _ = _macd_on_series(wr, 12, 26, 9)
    return macd.diff().diff()

def f26_stwf_457_trix_of_stoch_k_15_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TRIX(15) applied to Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    return _trix_on_series(k, 15).diff().diff()

def f26_stwf_458_trix_of_williams_r_15_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TRIX(15) applied to Williams %R(14)."""
    wr = _williams_r(high, low, close, 14)
    return _trix_on_series(wr, 15).diff().diff()

def f26_stwf_459_tsi_of_stoch_k_25_13_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TSI(25,13) applied to Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    return _tsi_on_series(k, 25, 13).diff().diff()

def f26_stwf_460_ema_of_stoch_minus_sma_of_stoch_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EMA(14) of %K minus SMA(14) of %K — leading-vs-lagging smoothing divergence."""
    k = _stoch_k(high, low, close, 14)
    return (_ema(k, 14) - k.rolling(14, min_periods=5).mean()).diff().diff()

def f26_stwf_461_cci_of_stoch_k_20_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) applied to Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    return _cci_on_series(k, 20).diff().diff()

def f26_stwf_462_cmo_of_stoch_k_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator(14) of Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    return _cmo_on_series(k, 14).diff().diff()

def f26_stwf_463_stoch_of_williams_r_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) applied to Williams %R(14) series."""
    wr = _williams_r(high, low, close, 14)
    return _stoch_on_series(wr, 14).diff().diff()

def f26_stwf_464_stoch_of_macd_signal_proxy_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) of MACD-line(12,26) of close — captures MACD extremes via stoch normalization."""
    macd, _ = _macd_on_series(close, 12, 26, 9)
    return _stoch_on_series(macd, 14).diff().diff()

def f26_stwf_465_williams_r_of_stoch_k_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R(14) applied to Stoch %K(14)."""
    k = _stoch_k(high, low, close, 14)
    return _williams_r_on_series(k, 14).diff().diff()

def f26_stwf_466_stoch_k_when_dd_5_to_10pct_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of %K conditional on drawdown from 1260d max being in 5-10%."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = (dd >= 5.0) & (dd < 10.0)
    return _cond_mean(k, mask, QDAYS).diff().diff()

def f26_stwf_467_stoch_k_when_dd_10_to_20pct_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of %K when drawdown 10-20%."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = (dd >= 10.0) & (dd < 20.0)
    return _cond_mean(k, mask, QDAYS).diff().diff()

def f26_stwf_468_stoch_k_when_dd_above_20pct_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of %K when drawdown >= 20%."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = dd >= 20.0
    return _cond_mean(k, mask, QDAYS).diff().diff()

def f26_stwf_469_williams_r_when_dd_5_to_10pct_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of Williams %R when drawdown 5-10%."""
    wr = _williams_r(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = (dd >= 5.0) & (dd < 10.0)
    return _cond_mean(wr, mask, QDAYS).diff().diff()

def f26_stwf_470_williams_r_when_dd_above_20pct_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of Williams %R when drawdown >= 20%."""
    wr = _williams_r(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = dd >= 20.0
    return _cond_mean(wr, mask, QDAYS).diff().diff()

def f26_stwf_471_stoch_change_at_first_dd_above_10pct_post_peak_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K change at first bar where dd-from-1260d-max first crosses above 10% post-peak — forward-filled."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    crossed = (dd >= 10.0) & (dd.shift(1) < 10.0)
    val = k.diff().where(crossed, np.nan).ffill()
    return val.diff().diff()

def f26_stwf_472_stoch_change_at_first_dd_above_20pct_post_peak_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K change at first bar where dd crosses above 20% — forward-filled."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    crossed = (dd >= 20.0) & (dd.shift(1) < 20.0)
    return k.diff().where(crossed, np.nan).ffill().diff().diff()

def f26_stwf_473_stoch_at_first_dd_above_30pct_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K value at first bar dd crosses 30% — forward-filled."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    crossed = (dd >= 30.0) & (dd.shift(1) < 30.0)
    return k.where(crossed, np.nan).ffill().diff().diff()

def f26_stwf_474_williams_r_at_first_dd_above_30pct_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R at first bar dd crosses 30% — forward-filled."""
    wr = _williams_r(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    crossed = (dd >= 30.0) & (dd.shift(1) < 30.0)
    return wr.where(crossed, np.nan).ffill().diff().diff()

def f26_stwf_475_stoch_recovery_oscillator_pattern_post_dd_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 mean of %K conditional on dd > 10% (recovery zone behavior)."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = dd > 10.0
    return _cond_mean(k, mask, QDAYS).diff().diff()

def f26_stwf_476_stoch_hysteresis_indicator_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K on up-close bars minus mean %K on down-close bars over 252 — hysteresis."""
    k = _stoch_k(high, low, close, 14)
    up = close.diff() > 0
    dn = close.diff() < 0
    up_mean = _cond_mean(k, up, YDAYS)
    dn_mean = _cond_mean(k, dn, YDAYS)
    return (up_mean - dn_mean).diff().diff()

def f26_stwf_477_stoch_path_dependence_from_peak_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of (K-50) over 252 — path-deviation-from-neutral integral."""
    k = _stoch_k(high, low, close, 14)
    return (k - 50.0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f26_stwf_478_williams_r_asymmetry_up_down_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean Williams %R on up vs down ret bars over 252."""
    wr = _williams_r(high, low, close, 14)
    up = close.diff() > 0
    dn = close.diff() < 0
    return (_cond_mean(wr, up, YDAYS) - _cond_mean(wr, dn, YDAYS)).diff().diff()

def f26_stwf_479_stoch_conditional_std_at_dd_above_20pct_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 std of %K when dd >= 20%."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    mask = dd >= 20.0
    return _cond_std(k, mask, QDAYS).diff().diff()

def f26_stwf_480_stoch_distribution_shift_pre_post_dd_zscore_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (mean K when dd<5%) - (mean K when dd>=10%) over 252 — distribution shift."""
    k = _stoch_k(high, low, close, 14)
    dd = _running_dd_pct(close, DDAYS_5Y)
    pre = _cond_mean(k, dd < 5.0, YDAYS)
    post = _cond_mean(k, dd >= 10.0, YDAYS)
    diff = pre - post
    return _rolling_zscore(diff, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_481_stoch_quantile_normal_transform_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse-normal CDF of rolling rank-pct of %K over 252 — Gaussianized."""
    k = _stoch_k(high, low, close, 14)
    return _quantile_normal_transform(k, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_482_stoch_uniform_quantile_transform_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling rank-pct of %K over 252 — uniform [0,1] transform."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_rank_pct(k, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_483_stoch_robust_zscore_mad_504_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Robust z-score: (K - median) / (1.4826 * MAD) over 504 — outlier-tolerant."""
    k = _stoch_k(high, low, close, 14)
    med = k.rolling(DDAYS_2Y, min_periods=QDAYS).median()
    mad = _mad_rolling(k, DDAYS_2Y, min_periods=QDAYS)
    return _safe_div(k - med, 1.4826 * mad).diff().diff()

def f26_stwf_484_stoch_modified_zscore_iqr_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Modified z: (K - median) / IQR(252)."""
    k = _stoch_k(high, low, close, 14)
    med = k.rolling(YDAYS, min_periods=QDAYS).median()
    iqr = _iqr_rolling(k, YDAYS, min_periods=QDAYS)
    return _safe_div(k - med, iqr).diff().diff()

def f26_stwf_485_multi_window_rolling_rank_avg_5_21_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of rolling rank-pct at 5/21/63 windows — multi-resolution agreement."""
    k = _stoch_k(high, low, close, 14)
    r5 = _rolling_rank_pct(k, WDAYS, min_periods=2)
    r21 = _rolling_rank_pct(k, MDAYS, min_periods=WDAYS)
    r63 = _rolling_rank_pct(k, QDAYS, min_periods=MDAYS)
    return pd.concat([r5.rename('r5'), r21.rename('r21'), r63.rename('r63')], axis=1).mean(axis=1).diff().diff()

def f26_stwf_486_multi_window_rolling_rank_std_5_21_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of rolling rank-pct at 5/21/63 windows — disagreement across horizons."""
    k = _stoch_k(high, low, close, 14)
    r5 = _rolling_rank_pct(k, WDAYS, min_periods=2)
    r21 = _rolling_rank_pct(k, MDAYS, min_periods=WDAYS)
    r63 = _rolling_rank_pct(k, QDAYS, min_periods=MDAYS)
    return pd.concat([r5.rename('r5'), r21.rename('r21'), r63.rename('r63')], axis=1).std(axis=1).diff().diff()

def f26_stwf_487_stoch_winsorized_5pct_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Winsorize K at 5/95% tails then z-score over 252."""
    k = _stoch_k(high, low, close, 14)
    return _winsorize_zscore(k, YDAYS, p_low=0.05, p_high=0.95, min_periods=QDAYS).diff().diff()

def f26_stwf_488_williams_r_quantile_normal_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Quantile-normal transform of Williams %R over 252."""
    wr = _williams_r(high, low, close, 14)
    return _quantile_normal_transform(wr, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_489_stoch_double_normalized_zscore_504_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double normalization: z-score, then quantile-normal of that z, over 504."""
    k = _stoch_k(high, low, close, 14)
    z = _rolling_zscore(k, DDAYS_2Y, min_periods=QDAYS)
    return _quantile_normal_transform(z, DDAYS_2Y, min_periods=QDAYS).diff().diff()

def f26_stwf_490_stoch_rolling_quantile_band_position_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position within [q10,q90] band over 252: (K - q10) / (q90 - q10)."""
    k = _stoch_k(high, low, close, 14)
    q10 = _quantile_rolling(k, YDAYS, 0.1, min_periods=QDAYS)
    q90 = _quantile_rolling(k, YDAYS, 0.9, min_periods=QDAYS)
    return _safe_div(k - q10, q90 - q10).diff().diff()

def f26_stwf_491_stoch_residual_after_removing_williams_r_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 residual of %K from K = alpha + beta*WR regression."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    return _rolling_residual(k, wr, QDAYS).diff().diff()

def f26_stwf_492_stoch_residual_after_removing_srsi_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 residual of %K from K = alpha + beta*SRSI-K regression."""
    k = _stoch_k(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    return _rolling_residual(k, sk, QDAYS).diff().diff()

def f26_stwf_493_williams_r_residual_after_removing_stoch_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 residual of Williams %R from WR = alpha + beta*K regression."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    return _rolling_residual(wr, k, QDAYS).diff().diff()

def f26_stwf_494_multi_oscillator_first_pc_proxy_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-PC proxy: simple average of z-scored basket — captures common factor."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    return df.mean(axis=1).diff().diff()

def f26_stwf_495_multi_oscillator_second_pc_proxy_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second-PC proxy: %K-z minus first-PC proxy — orthogonalized residual."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    pc1 = df.mean(axis=1)
    k_z = _rolling_zscore(o['k'], YDAYS, min_periods=QDAYS)
    return (k_z - pc1).diff().diff()

def f26_stwf_496_oscillator_pair_corr_stoch_williams_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 correlation between %K and Williams %R — pair coherence."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    return _rolling_corr(k, wr, QDAYS).diff().diff()

def f26_stwf_497_oscillator_pair_spread_stoch_williams_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252) of spread (K - (WR+100)) — both [0,100]-scaled."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    spread = k - (wr + 100.0)
    return _rolling_zscore(spread, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_498_oscillator_divergence_regression_residual_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Residual of %K from K = alpha + beta*close regression over 63 — price-orthogonal K."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_residual(k, close, QDAYS).diff().diff()

def f26_stwf_499_cross_oscillator_beta_to_stoch_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg rolling-63 beta of SRSI/WR/UO/SMI to %K — coupling strength to %K."""
    o = _all_oscillators(high, low, close)
    k = o['k']
    betas = []
    for name in ('wr', 'sk', 'uo', 'smi'):
        betas.append(_rolling_beta(o[name], k, QDAYS))
    df = pd.concat([b.rename(i) for i, b in enumerate(betas)], axis=1)
    return df.mean(axis=1).diff().diff()

def f26_stwf_500_cross_oscillator_residual_variance_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg rolling-63 variance of residuals of basket from K-regression — idiosyncratic dispersion."""
    o = _all_oscillators(high, low, close)
    k = o['k']
    res_var = []
    for name in ('wr', 'sk', 'uo', 'smi'):
        r = _rolling_residual(o[name], k, QDAYS)
        res_var.append(r.rolling(QDAYS, min_periods=MDAYS).var())
    df = pd.concat([v.rename(i) for i, v in enumerate(res_var)], axis=1)
    return df.mean(axis=1).diff().diff()

def f26_stwf_501_dtw_distance_stoch_to_simulated_50pct_dd_template_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DTW distance of %K(14) (63d window) to a parameterized template that linearly declines
    from 90 to 20 (proxy for 50% drawdown pattern)."""
    k = _stoch_k(high, low, close, 14)
    tpl = np.linspace(90.0, 20.0, 63)
    return _rolling_dtw_to_template(k, QDAYS, tpl).diff().diff()

def f26_stwf_502_dtw_distance_stoch_to_252h_breakdown_template_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DTW distance of %K(14) to a template: peak at 90, then concave drop to 10 over 63 bars
    (post-252h-high breakdown pattern)."""
    k = _stoch_k(high, low, close, 14)
    x = np.arange(63, dtype=float) / 62.0
    tpl = 90.0 - 80.0 * x ** 0.7
    return _rolling_dtw_to_template(k, QDAYS, tpl).diff().diff()

def f26_stwf_503_oscillator_path_length_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |%K.diff()| over 63 — total oscillator path length."""
    k = _stoch_k(high, low, close, 14)
    return _path_length(k, QDAYS).diff().diff()

def f26_stwf_504_oscillator_path_length_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252) of 63d path length — turbulence regime."""
    k = _stoch_k(high, low, close, 14)
    pl = _path_length(k, QDAYS)
    return _rolling_zscore(pl, YDAYS, min_periods=QDAYS).diff().diff()

def f26_stwf_505_oscillator_path_curvature_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |diff(diff(K))| over 63 — second-difference magnitude (curvature)."""
    k = _stoch_k(high, low, close, 14)
    return k.diff().diff().abs().rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f26_stwf_506_oscillator_path_complexity_score_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Complexity = path_length / |last - first|; higher = more wiggle per net move."""
    k = _stoch_k(high, low, close, 14)
    pl = _path_length(k, QDAYS)
    net = (k - k.shift(QDAYS - 1)).abs()
    return _safe_div(pl, net).diff().diff()

def f26_stwf_507_oscillator_path_entropy_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy (bits) of sign(K.diff()) over 63 — directional unpredictability."""
    k = _stoch_k(high, low, close, 14)
    return _shannon_sign_entropy(k, QDAYS).diff().diff()

def f26_stwf_508_oscillator_persistence_amplitude_weighted_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Amplitude-weighted persistence: sum(sign(dK)*|dK|) / sum(|dK|) over 63."""
    k = _stoch_k(high, low, close, 14)
    d = k.diff()
    num = (np.sign(d) * d.abs()).rolling(QDAYS, min_periods=MDAYS).sum()
    den = d.abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den).diff().diff()

def f26_stwf_509_oscillator_path_amplitude_index_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range(K) over 63 divided by std(K) over 63 — peak-to-peak vs typical."""
    k = _stoch_k(high, low, close, 14)
    rng = k.rolling(QDAYS, min_periods=MDAYS).max() - k.rolling(QDAYS, min_periods=MDAYS).min()
    sd = k.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(rng, sd).diff().diff()

def f26_stwf_510_oscillator_path_decay_index_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decay: ratio of |K - 63d max| to bars-since-63d-max."""
    k = _stoch_k(high, low, close, 14)
    peak = k.rolling(QDAYS, min_periods=MDAYS).max()
    bars = _bars_since_true(k >= peak)
    return _safe_div(peak - k, bars.where(bars > 0, np.nan)).diff().diff()

def f26_stwf_511_coskew_stoch_returns_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-skew(K, returns) over 21 — asymmetric joint behavior."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    return _coskew(k, ret, MDAYS).diff().diff()

def f26_stwf_512_cokurt_stoch_returns_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-kurt(K, returns) over 21 — joint tail co-movement."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    return _cokurt(k, ret, MDAYS).diff().diff()

def f26_stwf_513_stoch_in_extreme_return_tail_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K conditional on |ret| > q90(63) — K in extreme return regime."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    q90 = ret.abs().rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    mask = ret.abs() > q90
    return _cond_mean(k, mask, QDAYS).diff().diff()

def f26_stwf_514_corr_abs_returns_stoch_lag1_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling-63 corr between |ret| and lag-1 %K — leverage-effect-like coupling."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    return _rolling_corr(ret.abs(), k.shift(1), QDAYS).diff().diff()

def f26_stwf_515_coskew_at_252h_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-skew(K, ret) value at most-recent 252d high (forward-filled)."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    cs = _coskew(k, ret, MDAYS)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return cs.where(is_top, np.nan).ffill().diff().diff()

def f26_stwf_516_cokurt_at_252h_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-kurt(K, ret) value at most-recent 252d high."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    ck = _cokurt(k, ret, MDAYS)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ck.where(is_top, np.nan).ffill().diff().diff()

def f26_stwf_517_asymmetric_corr_up_vs_down_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(K, ret | ret>0) - Corr(K, ret | ret<0) over 63."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    up = ret > 0
    dn = ret < 0
    k_up = k.where(up, np.nan)
    r_up = ret.where(up, np.nan)
    k_dn = k.where(dn, np.nan)
    r_dn = ret.where(dn, np.nan)
    cu = _rolling_corr(k_up, r_up, QDAYS, min_periods=WDAYS)
    cd = _rolling_corr(k_dn, r_dn, QDAYS, min_periods=WDAYS)
    return (cu - cd).diff().diff()

def f26_stwf_518_stoch_tail_dependence_proxy_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """P(K > q90(K) and ret < q10(ret)) over 63 — adverse tail dependence."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    k_q90 = _quantile_rolling(k, QDAYS, 0.9, min_periods=MDAYS)
    r_q10 = _quantile_rolling(ret, QDAYS, 0.1, min_periods=MDAYS)
    co = ((k > k_q90) & (ret < r_q10)).astype(float)
    return co.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f26_stwf_519_williams_r_coskew_returns_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-skew(WR, ret) over 21."""
    wr = _williams_r(high, low, close, 14)
    ret = close.pct_change()
    return _coskew(wr, ret, MDAYS).diff().diff()

def f26_stwf_520_cross_oscillator_coskew_returns_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg co-skew(osc, ret) over basket — basket-wide asymmetry signature."""
    o = _all_oscillators(high, low, close)
    ret = close.pct_change()
    cs_list = [_coskew(s, ret, MDAYS) for s in o.values()]
    df = pd.concat([c.rename(i) for i, c in enumerate(cs_list)], axis=1)
    return df.mean(axis=1).diff().diff()

def f26_stwf_521_batch_4_orthogonal_aggregate_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of 252-z of (multi-window rank disagreement) + (path complexity) + (residual variance)
    + (tail dependence) — orthogonal aggregate of batch-4 axes."""
    k = _stoch_k(high, low, close, 14)
    r5 = _rolling_rank_pct(k, WDAYS, min_periods=2)
    r21 = _rolling_rank_pct(k, MDAYS, min_periods=WDAYS)
    r63 = _rolling_rank_pct(k, QDAYS, min_periods=MDAYS)
    a1 = pd.concat([r5.rename('r5'), r21.rename('r21'), r63.rename('r63')], axis=1).std(axis=1)
    pl = _path_length(k, QDAYS)
    net = (k - k.shift(QDAYS - 1)).abs()
    a2 = _safe_div(pl, net)
    wr = _williams_r(high, low, close, 14)
    res = _rolling_residual(k, wr, QDAYS)
    a3 = res.rolling(QDAYS, min_periods=MDAYS).var()
    ret = close.pct_change()
    k_q90 = _quantile_rolling(k, QDAYS, 0.9, min_periods=MDAYS)
    r_q10 = _quantile_rolling(ret, QDAYS, 0.1, min_periods=MDAYS)
    a4 = ((k > k_q90) & (ret < r_q10)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return (nz(a1) + nz(a2) + nz(a3) + nz(a4)).diff().diff()

def f26_stwf_522_oscillator_recall_optimized_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V4 recall: count of (rank disagreement above median) + (path entropy below median)
    + (residual variance above median) + (tail dependence above 0)."""
    k = _stoch_k(high, low, close, 14)
    r5 = _rolling_rank_pct(k, WDAYS, min_periods=2)
    r21 = _rolling_rank_pct(k, MDAYS, min_periods=WDAYS)
    r63 = _rolling_rank_pct(k, QDAYS, min_periods=MDAYS)
    rd = pd.concat([r5.rename('r5'), r21.rename('r21'), r63.rename('r63')], axis=1).std(axis=1)
    rd_med = rd.rolling(YDAYS, min_periods=QDAYS).median()
    pe = _shannon_sign_entropy(k, QDAYS)
    pe_med = pe.rolling(YDAYS, min_periods=QDAYS).median()
    wr = _williams_r(high, low, close, 14)
    rv = _rolling_residual(k, wr, QDAYS).rolling(QDAYS, min_periods=MDAYS).var()
    rv_med = rv.rolling(YDAYS, min_periods=QDAYS).median()
    ret = close.pct_change()
    k_q90 = _quantile_rolling(k, QDAYS, 0.9, min_periods=MDAYS)
    r_q10 = _quantile_rolling(ret, QDAYS, 0.1, min_periods=MDAYS)
    td = ((k > k_q90) & (ret < r_q10)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    score = (rd > rd_med).astype(float).fillna(0) + (pe < pe_med).astype(float).fillna(0) + (rv > rv_med).astype(float).fillna(0) + (td > 0).astype(float).fillna(0)
    return score.diff().diff()

def f26_stwf_523_oscillator_precision_optimized_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V4 precision: AND of (rank disagreement >= q75) AND (residual var >= q75) AND
    (tail dependence > 0.1) AND (close at 252d high)."""
    k = _stoch_k(high, low, close, 14)
    r5 = _rolling_rank_pct(k, WDAYS, min_periods=2)
    r21 = _rolling_rank_pct(k, MDAYS, min_periods=WDAYS)
    r63 = _rolling_rank_pct(k, QDAYS, min_periods=MDAYS)
    rd = pd.concat([r5.rename('r5'), r21.rename('r21'), r63.rename('r63')], axis=1).std(axis=1)
    rd_q75 = rd.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    wr = _williams_r(high, low, close, 14)
    rv = _rolling_residual(k, wr, QDAYS).rolling(QDAYS, min_periods=MDAYS).var()
    rv_q75 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    ret = close.pct_change()
    k_q90 = _quantile_rolling(k, QDAYS, 0.9, min_periods=MDAYS)
    r_q10 = _quantile_rolling(ret, QDAYS, 0.1, min_periods=MDAYS)
    td = ((k > k_q90) & (ret < r_q10)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((rd >= rd_q75) & (rv >= rv_q75) & (td > 0.1) & is_top).astype(float).where(close.notna(), np.nan).diff().diff()

def f26_stwf_524_oscillator_topping_master_v4_score_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V4 master topping: combines path complexity z, quantile-normal extreme, asymmetric corr,
    second-PC proxy magnitude (all z-normed)."""
    k = _stoch_k(high, low, close, 14)
    pl = _path_length(k, QDAYS)
    net = (k - k.shift(QDAYS - 1)).abs()
    cplx = _safe_div(pl, net)
    qn = _quantile_normal_transform(k, YDAYS, min_periods=QDAYS)
    ret = close.pct_change()
    up = ret > 0
    dn = ret < 0
    k_up = k.where(up, np.nan)
    r_up = ret.where(up, np.nan)
    k_dn = k.where(dn, np.nan)
    r_dn = ret.where(dn, np.nan)
    cu = _rolling_corr(k_up, r_up, QDAYS, min_periods=WDAYS)
    cd = _rolling_corr(k_dn, r_dn, QDAYS, min_periods=WDAYS)
    asym = cu - cd
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    pc1 = df.mean(axis=1)
    k_z = _rolling_zscore(o['k'], YDAYS, min_periods=QDAYS)
    pc2 = (k_z - pc1).abs()
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return (nz(cplx) + qn.fillna(0) + nz(asym) + nz(pc2)).diff().diff()

def f26_stwf_525_absolute_terminal_oscillator_v4_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """V4 absolute-terminal: 1 if (quantile-normal K > 2) AND (path complexity > q75)
    AND (volume z > 1) AND (close at 252d high)."""
    k = _stoch_k(high, low, close, 14)
    qn = _quantile_normal_transform(k, YDAYS, min_periods=QDAYS)
    pl = _path_length(k, QDAYS)
    net = (k - k.shift(QDAYS - 1)).abs()
    cplx = _safe_div(pl, net)
    cplx_q75 = cplx.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((qn > 2.0) & (cplx > cplx_q75) & (v_z > 1.0) & is_top).astype(float).where(close.notna(), np.nan).diff().diff()
STOCHASTIC_WILLIAMS_FAMILY_D2_REGISTRY_451_525 = {'f26_stwf_451_rsi_of_stoch_k_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_451_rsi_of_stoch_k_14_d2}, 'f26_stwf_452_rsi_of_stoch_d_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_452_rsi_of_stoch_d_14_d2}, 'f26_stwf_453_stoch_of_rsi_of_stoch_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_453_stoch_of_rsi_of_stoch_14_d2}, 'f26_stwf_454_macd_of_stoch_k_12_26_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_454_macd_of_stoch_k_12_26_d2}, 'f26_stwf_455_macd_of_stoch_k_signal_cross_down_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_455_macd_of_stoch_k_signal_cross_down_d2}, 'f26_stwf_456_macd_of_williams_r_12_26_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_456_macd_of_williams_r_12_26_d2}, 'f26_stwf_457_trix_of_stoch_k_15_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_457_trix_of_stoch_k_15_d2}, 'f26_stwf_458_trix_of_williams_r_15_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_458_trix_of_williams_r_15_d2}, 'f26_stwf_459_tsi_of_stoch_k_25_13_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_459_tsi_of_stoch_k_25_13_d2}, 'f26_stwf_460_ema_of_stoch_minus_sma_of_stoch_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_460_ema_of_stoch_minus_sma_of_stoch_14_d2}, 'f26_stwf_461_cci_of_stoch_k_20_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_461_cci_of_stoch_k_20_d2}, 'f26_stwf_462_cmo_of_stoch_k_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_462_cmo_of_stoch_k_14_d2}, 'f26_stwf_463_stoch_of_williams_r_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_463_stoch_of_williams_r_14_d2}, 'f26_stwf_464_stoch_of_macd_signal_proxy_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_464_stoch_of_macd_signal_proxy_d2}, 'f26_stwf_465_williams_r_of_stoch_k_14_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_465_williams_r_of_stoch_k_14_d2}, 'f26_stwf_466_stoch_k_when_dd_5_to_10pct_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_466_stoch_k_when_dd_5_to_10pct_avg_63_d2}, 'f26_stwf_467_stoch_k_when_dd_10_to_20pct_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_467_stoch_k_when_dd_10_to_20pct_avg_63_d2}, 'f26_stwf_468_stoch_k_when_dd_above_20pct_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_468_stoch_k_when_dd_above_20pct_avg_63_d2}, 'f26_stwf_469_williams_r_when_dd_5_to_10pct_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_469_williams_r_when_dd_5_to_10pct_avg_63_d2}, 'f26_stwf_470_williams_r_when_dd_above_20pct_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_470_williams_r_when_dd_above_20pct_avg_63_d2}, 'f26_stwf_471_stoch_change_at_first_dd_above_10pct_post_peak_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_471_stoch_change_at_first_dd_above_10pct_post_peak_d2}, 'f26_stwf_472_stoch_change_at_first_dd_above_20pct_post_peak_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_472_stoch_change_at_first_dd_above_20pct_post_peak_d2}, 'f26_stwf_473_stoch_at_first_dd_above_30pct_value_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_473_stoch_at_first_dd_above_30pct_value_d2}, 'f26_stwf_474_williams_r_at_first_dd_above_30pct_value_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_474_williams_r_at_first_dd_above_30pct_value_d2}, 'f26_stwf_475_stoch_recovery_oscillator_pattern_post_dd_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_475_stoch_recovery_oscillator_pattern_post_dd_63_d2}, 'f26_stwf_476_stoch_hysteresis_indicator_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_476_stoch_hysteresis_indicator_252_d2}, 'f26_stwf_477_stoch_path_dependence_from_peak_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_477_stoch_path_dependence_from_peak_d2}, 'f26_stwf_478_williams_r_asymmetry_up_down_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_478_williams_r_asymmetry_up_down_d2}, 'f26_stwf_479_stoch_conditional_std_at_dd_above_20pct_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_479_stoch_conditional_std_at_dd_above_20pct_d2}, 'f26_stwf_480_stoch_distribution_shift_pre_post_dd_zscore_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_480_stoch_distribution_shift_pre_post_dd_zscore_d2}, 'f26_stwf_481_stoch_quantile_normal_transform_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_481_stoch_quantile_normal_transform_252_d2}, 'f26_stwf_482_stoch_uniform_quantile_transform_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_482_stoch_uniform_quantile_transform_252_d2}, 'f26_stwf_483_stoch_robust_zscore_mad_504_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_483_stoch_robust_zscore_mad_504_d2}, 'f26_stwf_484_stoch_modified_zscore_iqr_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_484_stoch_modified_zscore_iqr_252_d2}, 'f26_stwf_485_multi_window_rolling_rank_avg_5_21_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_485_multi_window_rolling_rank_avg_5_21_63_d2}, 'f26_stwf_486_multi_window_rolling_rank_std_5_21_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_486_multi_window_rolling_rank_std_5_21_63_d2}, 'f26_stwf_487_stoch_winsorized_5pct_zscore_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_487_stoch_winsorized_5pct_zscore_252_d2}, 'f26_stwf_488_williams_r_quantile_normal_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_488_williams_r_quantile_normal_252_d2}, 'f26_stwf_489_stoch_double_normalized_zscore_504_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_489_stoch_double_normalized_zscore_504_d2}, 'f26_stwf_490_stoch_rolling_quantile_band_position_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_490_stoch_rolling_quantile_band_position_252_d2}, 'f26_stwf_491_stoch_residual_after_removing_williams_r_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_491_stoch_residual_after_removing_williams_r_63_d2}, 'f26_stwf_492_stoch_residual_after_removing_srsi_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_492_stoch_residual_after_removing_srsi_63_d2}, 'f26_stwf_493_williams_r_residual_after_removing_stoch_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_493_williams_r_residual_after_removing_stoch_63_d2}, 'f26_stwf_494_multi_oscillator_first_pc_proxy_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_494_multi_oscillator_first_pc_proxy_d2}, 'f26_stwf_495_multi_oscillator_second_pc_proxy_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_495_multi_oscillator_second_pc_proxy_d2}, 'f26_stwf_496_oscillator_pair_corr_stoch_williams_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_496_oscillator_pair_corr_stoch_williams_63_d2}, 'f26_stwf_497_oscillator_pair_spread_stoch_williams_zscore_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_497_oscillator_pair_spread_stoch_williams_zscore_252_d2}, 'f26_stwf_498_oscillator_divergence_regression_residual_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_498_oscillator_divergence_regression_residual_63_d2}, 'f26_stwf_499_cross_oscillator_beta_to_stoch_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_499_cross_oscillator_beta_to_stoch_63_d2}, 'f26_stwf_500_cross_oscillator_residual_variance_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_500_cross_oscillator_residual_variance_63_d2}, 'f26_stwf_501_dtw_distance_stoch_to_simulated_50pct_dd_template_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_501_dtw_distance_stoch_to_simulated_50pct_dd_template_63_d2}, 'f26_stwf_502_dtw_distance_stoch_to_252h_breakdown_template_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_502_dtw_distance_stoch_to_252h_breakdown_template_63_d2}, 'f26_stwf_503_oscillator_path_length_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_503_oscillator_path_length_63_d2}, 'f26_stwf_504_oscillator_path_length_zscore_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_504_oscillator_path_length_zscore_252_d2}, 'f26_stwf_505_oscillator_path_curvature_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_505_oscillator_path_curvature_63_d2}, 'f26_stwf_506_oscillator_path_complexity_score_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_506_oscillator_path_complexity_score_63_d2}, 'f26_stwf_507_oscillator_path_entropy_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_507_oscillator_path_entropy_63_d2}, 'f26_stwf_508_oscillator_persistence_amplitude_weighted_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_508_oscillator_persistence_amplitude_weighted_63_d2}, 'f26_stwf_509_oscillator_path_amplitude_index_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_509_oscillator_path_amplitude_index_63_d2}, 'f26_stwf_510_oscillator_path_decay_index_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_510_oscillator_path_decay_index_63_d2}, 'f26_stwf_511_coskew_stoch_returns_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_511_coskew_stoch_returns_21_d2}, 'f26_stwf_512_cokurt_stoch_returns_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_512_cokurt_stoch_returns_21_d2}, 'f26_stwf_513_stoch_in_extreme_return_tail_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_513_stoch_in_extreme_return_tail_avg_63_d2}, 'f26_stwf_514_corr_abs_returns_stoch_lag1_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_514_corr_abs_returns_stoch_lag1_63_d2}, 'f26_stwf_515_coskew_at_252h_value_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_515_coskew_at_252h_value_d2}, 'f26_stwf_516_cokurt_at_252h_value_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_516_cokurt_at_252h_value_d2}, 'f26_stwf_517_asymmetric_corr_up_vs_down_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_517_asymmetric_corr_up_vs_down_63_d2}, 'f26_stwf_518_stoch_tail_dependence_proxy_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_518_stoch_tail_dependence_proxy_63_d2}, 'f26_stwf_519_williams_r_coskew_returns_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_519_williams_r_coskew_returns_21_d2}, 'f26_stwf_520_cross_oscillator_coskew_returns_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_520_cross_oscillator_coskew_returns_21_d2}, 'f26_stwf_521_batch_4_orthogonal_aggregate_zscore_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_521_batch_4_orthogonal_aggregate_zscore_252_d2}, 'f26_stwf_522_oscillator_recall_optimized_v4_score_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_522_oscillator_recall_optimized_v4_score_d2}, 'f26_stwf_523_oscillator_precision_optimized_v4_score_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_523_oscillator_precision_optimized_v4_score_d2}, 'f26_stwf_524_oscillator_topping_master_v4_score_d2': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_524_oscillator_topping_master_v4_score_d2}, 'f26_stwf_525_absolute_terminal_oscillator_v4_indicator_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_525_absolute_terminal_oscillator_v4_indicator_d2}}