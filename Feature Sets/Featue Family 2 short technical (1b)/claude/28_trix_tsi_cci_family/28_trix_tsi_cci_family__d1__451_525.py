"""28_trix_tsi_cci_family d1 features 451-525 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _rolling_slope_inner(w):
    valid = ~np.isnan(w)
    if valid.sum() < 2:
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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(_rolling_slope_inner, raw=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _trix(close, n=15):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()

def _tsi(close, n1=25, n2=13):
    m = close.diff()
    e1 = _ema(m, n1)
    e2 = _ema(e1, n2)
    a1 = _ema(m.abs(), n1)
    a2 = _ema(a1, n2)
    return 100.0 * _safe_div(e2, a2)

def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)

def _dpo(close, n=20):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)

def _kst(close):
    roc10 = close.pct_change(10)
    roc15 = close.pct_change(15)
    roc20 = close.pct_change(20)
    roc30 = close.pct_change(30)
    r1 = roc10.rolling(10, min_periods=5).mean()
    r2 = roc15.rolling(10, min_periods=5).mean()
    r3 = roc20.rolling(10, min_periods=5).mean()
    r4 = roc30.rolling(15, min_periods=8).mean()
    return r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4

def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    su = up.rolling(n, min_periods=max(n // 3, 2)).sum()
    sd = dn.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(su - sd, su + sd)

def _rsi_series(s, n=14):
    d = s.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_k(s, n=14):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return 100.0 * _safe_div(s - lo, hi - lo)

def _macd_line(s, fast=12, slow=26):
    return _ema(s, fast) - _ema(s, slow)

def _williams_r(s, n=14):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hi - s, hi - lo)

def _fisher_transform(s, n=10):
    """Fisher transform of a series normalized to [-1, 1] over n-bar window."""
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    x = 2.0 * _safe_div(s - lo, hi - lo) - 1.0
    x = x.clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + x) / (1.0 - x))

def _inverse_fisher_transform_norm(s):
    """Inverse Fisher transform on series normalized via tanh-friendly scaling (s/std)."""
    sd = s.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    x = s / sd
    x = x.clip(-10, 10)
    return (np.exp(2.0 * x) - 1.0) / (np.exp(2.0 * x) + 1.0)

def _drawdown_pct(close, n=YDAYS):
    """Drawdown from rolling n-day high, expressed in (negative) pct (0 at peak, -0.5 = down 50%)."""
    rmax = close.rolling(n, min_periods=max(n // 4, MDAYS)).max()
    return _safe_div(close - rmax, rmax)

def _first_event_value(sig, event_mask, lookback=YDAYS):
    """At each bar, returns sig at the first True in event_mask within past lookback bars
    (NaN if no such event)."""
    ev = event_mask.astype(bool)
    arr = ev.to_numpy()
    out = np.full(len(sig), np.nan)
    sig_arr = sig.to_numpy()
    n = len(sig)
    for i in range(n):
        lo = max(0, i - lookback + 1)
        sub = arr[lo:i + 1]
        if sub.any():
            first = lo + int(np.argmax(sub))
            out[i] = sig_arr[first]
    return pd.Series(out, index=sig.index)

def _quantile_normal_transform(s, n=YDAYS):
    """Map series to its rolling rank, then approximate inverse normal via probit-like
    approximation: z = sqrt(2) * erfinv(2r-1). Use rational approximation of erfinv."""
    rk = s.rolling(n, min_periods=max(n // 3, MDAYS)).rank(pct=True)
    rk = rk.clip(0.001, 0.999)
    u = 2.0 * rk - 1.0
    a = 0.147
    ln = np.log(1.0 - u * u)
    term = 2.0 / (np.pi * a) + ln / 2.0
    z = np.sign(u) * np.sqrt(np.sqrt(term * term - ln / a) - term)
    return np.sqrt(2.0) * z

def _robust_z_mad(s, n=DDAYS_2Y):
    med = s.rolling(n, min_periods=max(n // 3, QDAYS)).median()
    mad = (s - med).abs().rolling(n, min_periods=max(n // 3, QDAYS)).median()
    return _safe_div(s - med, 1.4826 * mad)

def _modified_z_iqr(s, n=YDAYS):
    med = s.rolling(n, min_periods=max(n // 3, MDAYS)).median()
    q75 = s.rolling(n, min_periods=max(n // 3, MDAYS)).quantile(0.75)
    q25 = s.rolling(n, min_periods=max(n // 3, MDAYS)).quantile(0.25)
    iqr = q75 - q25
    return _safe_div(s - med, 0.7413 * iqr)

def _winsorized_zscore(s, n=YDAYS, pct=0.05):
    q_lo = s.rolling(n, min_periods=max(n // 3, MDAYS)).quantile(pct)
    q_hi = s.rolling(n, min_periods=max(n // 3, MDAYS)).quantile(1.0 - pct)
    w = s.where(s >= q_lo, q_lo).where(s <= q_hi, q_hi)
    return _rolling_zscore(w, n)

def _rolling_residual(y, x, n=QDAYS):
    """OLS residual y - (a + b x) where (a, b) computed on rolling n-window."""
    cov = x.rolling(n, min_periods=max(n // 3, 2)).cov(y)
    var = x.rolling(n, min_periods=max(n // 3, 2)).var()
    b = _safe_div(cov, var)
    a = y.rolling(n, min_periods=max(n // 3, 2)).mean() - b * x.rolling(n, min_periods=max(n // 3, 2)).mean()
    pred = a + b * x
    return y - pred

def _rolling_beta(y, x, n=QDAYS):
    cov = x.rolling(n, min_periods=max(n // 3, 2)).cov(y)
    var = x.rolling(n, min_periods=max(n // 3, 2)).var()
    return _safe_div(cov, var)

def _basket_classical(high, low, close):
    return [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20), _cmo(close, 14), _dpo(close, MDAYS), _kst(close)]

def _basket_zscores(high, low, close, n=DDAYS_2Y):
    out = []
    for sig in _basket_classical(high, low, close):
        out.append(_rolling_zscore(sig, n, min_periods=YDAYS))
    return out

def _dtw_distance_to_template_inner(w, template):
    """Simple O(n*m) DTW between window w (len n) and template (len m). Returns distance."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    m = len(template)
    INF = 1e+18
    D = np.full((n + 1, m + 1), INF)
    D[0, 0] = 0.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(w[i - 1] - template[j - 1])
            D[i, j] = cost + min(D[i - 1, j], D[i, j - 1], D[i - 1, j - 1])
    return float(D[n, m]) / (n + m)
_TPL_50PCT_DD = np.linspace(1.5, -2.5, 10)
_TPL_BREAKDOWN_252 = np.concatenate([np.linspace(1.5, 1.2, 5), np.linspace(1.0, -1.5, 10)])

def _rolling_dtw_to_template(s, n, template):
    arr = s.to_numpy()
    out = np.full(len(s), np.nan)
    for i in range(n - 1, len(s)):
        w = arr[i - n + 1:i + 1]
        if len(template) > 0 and n >= len(template):
            stride = max(1, n // len(template))
            ws = w[::stride][:len(template)]
            if len(ws) == len(template):
                out[i] = _dtw_distance_to_template_inner(ws, template)
    return pd.Series(out, index=s.index)

def _path_length(s, n):
    return s.diff().abs().rolling(n, min_periods=max(n // 3, MDAYS)).sum()

def _path_curvature(s, n):
    return s.diff().diff().abs().rolling(n, min_periods=max(n // 3, MDAYS)).sum()

def _path_complexity(s, n):
    """Path length / |start - end|, larger = more winding."""
    pl = _path_length(s, n)
    span = (s - s.shift(n - 1)).abs()
    return _safe_div(pl, span)

def _path_entropy_inner(w):
    """Histogram entropy over n bins (4) of binarized first differences."""
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    d = np.diff(w)
    if np.std(d) == 0:
        return 0.0
    q = np.quantile(d, [0.25, 0.5, 0.75])
    ix = np.digitize(d, q)
    counts = np.bincount(ix, minlength=4).astype(float)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())

def _rolling_path_entropy(s, n):
    return s.rolling(n, min_periods=max(n // 2, 4)).apply(_path_entropy_inner, raw=True)

def _amplitude_weighted_persistence(s, n):
    """Sum of |s| * sign(s)-persistence over n: high when amplitude is preserved with sign."""
    sgn = np.sign(s)
    streak = (sgn == sgn.shift(1)).astype(float)
    return (s.abs() * streak).rolling(n, min_periods=max(n // 3, MDAYS)).mean()

def _amplitude_index(s, n):
    """Range of s over n / std over n — amplitude in std units."""
    hi = s.rolling(n, min_periods=max(n // 3, MDAYS)).max()
    lo = s.rolling(n, min_periods=max(n // 3, MDAYS)).min()
    sd = s.rolling(n, min_periods=max(n // 3, MDAYS)).std()
    return _safe_div(hi - lo, sd)

def _path_decay_index(s, n):
    """Compare amplitude in recent half vs older half: high = recent decay."""
    half = n // 2
    rec = s.rolling(half, min_periods=max(half // 3, 2)).max() - s.rolling(half, min_periods=max(half // 3, 2)).min()
    older_max = s.shift(half).rolling(half, min_periods=max(half // 3, 2)).max()
    older_min = s.shift(half).rolling(half, min_periods=max(half // 3, 2)).min()
    older = older_max - older_min
    return _safe_div(older - rec, older)

def _rolling_coskew(x, y, n):
    """E[(x-mx)^2 * (y-my)] / (std_x^2 * std_y)"""
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    cs = ((x - mx) ** 2 * (y - my)).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(cs, sx * sx * sy)

def _rolling_cokurt(x, y, n):
    """E[(x-mx)^2 * (y-my)^2] / (std_x^2 * std_y^2)"""
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    ck = ((x - mx) ** 2 * (y - my) ** 2).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(ck, sx * sx * sy * sy)

def _asymmetric_corr(x, y, n, up=True):
    """Correlation of x and y computed only on bars where y has up (down) return.
    Implemented by masking with NaN and dropping pairs implicitly via cov/var on rolling."""
    if up:
        mask = y > 0
    else:
        mask = y < 0
    xm = x.where(mask)
    ym = y.where(mask)
    return xm.rolling(n, min_periods=max(n // 4, 4)).corr(ym)

def _h_basket_orthogonal_aggregate_zscore_252(high, low, close):
    """Orthogonalize each basket signal against the basket mean, then average resulting z-scores.
    Captures unique variance per indicator."""
    sigs = _basket_classical(high, low, close)
    avg_raw = pd.concat([s.rename(i) for i, s in enumerate(sigs)], axis=1).mean(axis=1)
    out_zs = []
    for s in sigs:
        resid = _rolling_residual(s, avg_raw, QDAYS)
        out_zs.append(_rolling_zscore(resid, YDAYS, min_periods=QDAYS))
    return pd.concat([z.rename(i) for i, z in enumerate(out_zs)], axis=1).mean(axis=1)

def _h_basket_first_pc_proxy(high, low, close):
    """First-PC proxy = mean of z-scored basket signals (captures common variance)."""
    zs = _basket_zscores(high, low, close, DDAYS_2Y)
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).mean(axis=1)

def _h_basket_second_pc_proxy(high, low, close):
    """Second-PC proxy = mean of residuals after removing first-PC proxy from each indicator."""
    sigs = _basket_classical(high, low, close)
    pc1 = _h_basket_first_pc_proxy(high, low, close)
    resids = []
    for s in sigs:
        resids.append(_rolling_residual(_rolling_zscore(s, DDAYS_2Y, min_periods=YDAYS), pc1, QDAYS))
    return pd.concat([r.rename(i) for i, r in enumerate(resids)], axis=1).mean(axis=1)

def _h_basket_dispersion(high, low, close):
    zs = _basket_zscores(high, low, close, DDAYS_2Y)
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).std(axis=1)

def _h_basket_avg_coskew_returns(high, low, close, n=MDAYS):
    sigs = _basket_classical(high, low, close)
    ret = close.pct_change()
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for s in sigs:
        out = out + _rolling_coskew(s, ret, n).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_basket_avg_cokurt_returns(high, low, close, n=MDAYS):
    sigs = _basket_classical(high, low, close)
    ret = close.pct_change()
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for s in sigs:
        out = out + _rolling_cokurt(s, ret, n).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_basket_dtw_to_breakdown_template(high, low, close):
    sigs = _basket_classical(high, low, close)
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for s in sigs:
        out = out + _rolling_dtw_to_template(s, QDAYS, _TPL_BREAKDOWN_252).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_basket_path_complexity_score(high, low, close):
    sigs = _basket_classical(high, low, close)
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for s in sigs:
        out = out + _path_complexity(s, QDAYS).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def f28_ttcf_451_rsi_of_cci_14_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI(14) applied to CCI series — momentum-of-CCI (extension of CCI signal velocity)."""
    return _rsi_series(_cci(high, low, close, 20), 14).diff()

def f28_ttcf_452_rsi_of_trix_14_d1(close: pd.Series) -> pd.Series:
    """RSI(14) applied to TRIX series — momentum-of-TRIX."""
    return _rsi_series(_trix(close, 15), 14).diff()

def f28_ttcf_453_stoch_of_cci_14_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic-K(14) applied to CCI — normalized CCI position in its 14-bar range."""
    return _stoch_k(_cci(high, low, close, 20), 14).diff()

def f28_ttcf_454_stoch_of_trix_14_d1(close: pd.Series) -> pd.Series:
    """Stochastic-K(14) applied to TRIX — normalized TRIX position in its 14-bar range."""
    return _stoch_k(_trix(close, 15), 14).diff()

def f28_ttcf_455_macd_of_cci_12_26_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD(12, 26) applied to CCI series — multi-scale CCI momentum spread."""
    return _macd_line(_cci(high, low, close, 20), 12, 26).diff()

def f28_ttcf_456_macd_of_cmo_12_26_d1(close: pd.Series) -> pd.Series:
    """MACD(12, 26) applied to CMO — multi-scale CMO momentum spread."""
    return _macd_line(_cmo(close, 14), 12, 26).diff()

def f28_ttcf_457_trix_of_cci_15_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TRIX(15) applied to CCI series — triple-smoothed momentum-of-CCI (cycle filter on CCI)."""
    c = _cci(high, low, close, 20)
    e1 = _ema(c, 15)
    e2 = _ema(e1, 15)
    e3 = _ema(e2, 15)
    return (100.0 * e3.pct_change()).diff()

def f28_ttcf_458_cci_of_trix_20_d1(close: pd.Series) -> pd.Series:
    """CCI(20) applied to TRIX as 'price' — TRIX deviation from its mean normalized by TRIX MAD."""
    t = _trix(close, 15)
    sma = t.rolling(20, min_periods=7).mean()
    mad = (t - sma).abs().rolling(20, min_periods=7).mean()
    return _safe_div(t - sma, 0.015 * mad).diff()

def f28_ttcf_459_cmo_of_cci_14_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CMO(14) applied to CCI series — momentum-balance of CCI swings."""
    c = _cci(high, low, close, 20)
    d = c.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    su = up.rolling(14, min_periods=5).sum()
    sd = dn.rolling(14, min_periods=5).sum()
    return (100.0 * _safe_div(su - sd, su + sd)).diff()

def f28_ttcf_460_williams_r_of_cci_14_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R(14) applied to CCI — CCI position within its 14-bar high/low range (negated)."""
    return _williams_r(_cci(high, low, close, 20), 14).diff()

def f28_ttcf_461_tsi_of_cci_25_13_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TSI(25, 13) applied to CCI — double-smoothed signed momentum-of-CCI."""
    c = _cci(high, low, close, 20)
    m = c.diff()
    e1 = _ema(m, 25)
    e2 = _ema(e1, 13)
    a1 = _ema(m.abs(), 25)
    a2 = _ema(a1, 13)
    return (100.0 * _safe_div(e2, a2)).diff()

def f28_ttcf_462_fisher_transform_of_cci_10_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fisher transform of CCI over 10-bar normalization window — emphasizes turning points."""
    return _fisher_transform(_cci(high, low, close, 20), 10).diff()

def f28_ttcf_463_inverse_fisher_transform_of_cci_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse Fisher transform of CCI/std — maps CCI into [-1, 1] with sigmoid shape."""
    return _inverse_fisher_transform_norm(_cci(high, low, close, 20)).diff()

def f28_ttcf_464_ema_of_trix_minus_sma_of_trix_15_d1(close: pd.Series) -> pd.Series:
    """EMA15(TRIX) - SMA15(TRIX) — fast vs slow filter spread of TRIX (curvature proxy)."""
    t = _trix(close, 15)
    return (_ema(t, 15) - _sma(t, 15)).diff()

def f28_ttcf_465_ema_of_cci_minus_sma_of_cci_20_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EMA20(CCI) - SMA20(CCI) — fast vs slow filter spread of CCI (curvature proxy)."""
    c = _cci(high, low, close, 20)
    return (_ema(c, 20) - _sma(c, 20)).diff()

def f28_ttcf_466_cci_when_dd_5_to_10pct_avg_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean of CCI restricted to bars where 5% < drawdown <= 10% (mild-correction regime)."""
    dd = _drawdown_pct(close, YDAYS)
    mask = (dd <= -0.05) & (dd > -0.1)
    c = _cci(high, low, close, 20).where(mask)
    return c.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_467_cci_when_dd_10_to_20pct_avg_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean of CCI restricted to bars where 10% < drawdown <= 20%."""
    dd = _drawdown_pct(close, YDAYS)
    mask = (dd <= -0.1) & (dd > -0.2)
    c = _cci(high, low, close, 20).where(mask)
    return c.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_468_cci_when_dd_above_20pct_avg_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean of CCI restricted to bars where drawdown > 20%."""
    dd = _drawdown_pct(close, YDAYS)
    mask = dd <= -0.2
    c = _cci(high, low, close, 20).where(mask)
    return c.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_469_trix_when_dd_above_20pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """63d mean of TRIX restricted to bars where 252d drawdown > 20%."""
    dd = _drawdown_pct(close, YDAYS)
    mask = dd <= -0.2
    t = _trix(close, 15).where(mask)
    return t.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_470_cmo_when_dd_above_20pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """63d mean of CMO restricted to bars where 252d drawdown > 20%."""
    dd = _drawdown_pct(close, YDAYS)
    mask = dd <= -0.2
    c = _cmo(close, 14).where(mask)
    return c.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_471_cci_change_at_first_dd_above_10pct_post_peak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI - CCI[peak] at the first bar in 252d window where dd > 10%. NaN until event present."""
    c = _cci(high, low, close, 20)
    dd = _drawdown_pct(close, YDAYS)
    event = dd <= -0.1
    cci_at_event = _first_event_value(c, event, YDAYS)
    rmax_close = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = close >= rmax_close
    cci_at_peak = _first_event_value(c, at_peak, YDAYS)
    return (cci_at_event - cci_at_peak).diff()

def f28_ttcf_472_cci_change_at_first_dd_above_20pct_post_peak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI - CCI[peak] at the first bar in 252d window where dd > 20%."""
    c = _cci(high, low, close, 20)
    dd = _drawdown_pct(close, YDAYS)
    event = dd <= -0.2
    cci_at_event = _first_event_value(c, event, YDAYS)
    rmax_close = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = close >= rmax_close
    cci_at_peak = _first_event_value(c, at_peak, YDAYS)
    return (cci_at_event - cci_at_peak).diff()

def f28_ttcf_473_cci_at_first_dd_above_30pct_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI value at the first bar within past 504d where 252d drawdown > 30% — capitulation imprint."""
    c = _cci(high, low, close, 20)
    dd = _drawdown_pct(close, YDAYS)
    event = dd <= -0.3
    return _first_event_value(c, event, DDAYS_2Y).diff()

def f28_ttcf_474_trix_at_first_dd_above_30pct_value_d1(close: pd.Series) -> pd.Series:
    """TRIX value at the first bar within past 504d where 252d drawdown > 30%."""
    t = _trix(close, 15)
    dd = _drawdown_pct(close, YDAYS)
    event = dd <= -0.3
    return _first_event_value(t, event, DDAYS_2Y).diff()

def f28_ttcf_475_cci_recovery_pattern_post_dd_avg_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean of CCI restricted to bars within 21 days AFTER a 10% drawdown trigger — recovery pattern."""
    c = _cci(high, low, close, 20)
    dd = _drawdown_pct(close, YDAYS)
    trigger = (dd <= -0.1) & (dd.shift(1) > -0.1)
    flag = trigger.astype(float).rolling(MDAYS, min_periods=1).max().shift(1).fillna(0)
    mask = flag > 0
    return c.where(mask).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_476_cci_hysteresis_indicator_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hysteresis = (CCI now - CCI 252 ago) / |range CCI 252|. Path-dependence proxy."""
    c = _cci(high, low, close, 20)
    rng = c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(c - c.shift(YDAYS), rng).diff()

def f28_ttcf_477_cci_path_dependence_from_peak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative CCI since the most recent 252d high — path-dependent CCI exposure since peak."""
    c = _cci(high, low, close, 20)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = close >= rmax
    grp = at_peak.astype(int).cumsum()
    return c.groupby(grp).cumsum().where(c.notna(), np.nan).diff()

def f28_ttcf_478_cci_asymmetry_up_down_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean CCI on up-return days minus mean CCI on down-return days over 63d — directional bias."""
    c = _cci(high, low, close, 20)
    ret = close.pct_change()
    cu = c.where(ret > 0).rolling(QDAYS, min_periods=MDAYS).mean()
    cd = c.where(ret < 0).rolling(QDAYS, min_periods=MDAYS).mean()
    return (cu - cd).diff()

def f28_ttcf_479_cci_conditional_std_at_dd_above_20pct_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d std of CCI restricted to drawdown > 20% — conditional volatility regime."""
    c = _cci(high, low, close, 20)
    dd = _drawdown_pct(close, YDAYS)
    mask = dd <= -0.2
    return c.where(mask).rolling(QDAYS, min_periods=MDAYS).std().diff()

def f28_ttcf_480_cci_distribution_shift_pre_post_dd_zscore_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (mean CCI in past 21 bars - mean CCI in 22..63 bars-ago) over 252d.
    Captures regime-shift in CCI distribution around drawdown."""
    c = _cci(high, low, close, 20)
    rec = c.rolling(MDAYS, min_periods=7).mean()
    older = c.shift(MDAYS).rolling(QDAYS - MDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(rec - older, YDAYS, min_periods=QDAYS).diff()

def f28_ttcf_481_cci_quantile_normal_transform_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probit-like quantile normal transform of CCI over 252d — Gaussianized CCI."""
    return _quantile_normal_transform(_cci(high, low, close, 20), YDAYS).diff()

def f28_ttcf_482_trix_quantile_normal_transform_252_d1(close: pd.Series) -> pd.Series:
    """Quantile-normal transform of TRIX over 252d."""
    return _quantile_normal_transform(_trix(close, 15), YDAYS).diff()

def f28_ttcf_483_cmo_quantile_normal_transform_252_d1(close: pd.Series) -> pd.Series:
    """Quantile-normal transform of CMO over 252d."""
    return _quantile_normal_transform(_cmo(close, 14), YDAYS).diff()

def f28_ttcf_484_cci_robust_zscore_mad_504_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Robust z-score of CCI = (CCI - median) / (1.4826*MAD) over 504d — outlier-resistant CCI."""
    return _robust_z_mad(_cci(high, low, close, 20), DDAYS_2Y).diff()

def f28_ttcf_485_trix_modified_zscore_iqr_252_d1(close: pd.Series) -> pd.Series:
    """Modified z-score using IQR: (TRIX - median) / (0.7413*IQR) over 252d."""
    return _modified_z_iqr(_trix(close, 15), YDAYS).diff()

def f28_ttcf_486_multi_window_cci_rank_avg_5_21_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average pct-rank of CCI across windows 5d, 21d, 63d — multi-resolution CCI position."""
    c = _cci(high, low, close, 20)
    r5 = c.rolling(WDAYS, min_periods=2).rank(pct=True)
    r21 = c.rolling(MDAYS, min_periods=7).rank(pct=True)
    r63 = c.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    return pd.concat([r5.rename('a'), r21.rename('b'), r63.rename('c')], axis=1).mean(axis=1).diff()

def f28_ttcf_487_multi_window_trix_rank_std_5_21_63_d1(close: pd.Series) -> pd.Series:
    """Std of pct-rank of TRIX across windows 5d, 21d, 63d — multi-resolution disagreement."""
    t = _trix(close, 15)
    r5 = t.rolling(WDAYS, min_periods=2).rank(pct=True)
    r21 = t.rolling(MDAYS, min_periods=7).rank(pct=True)
    r63 = t.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    return pd.concat([r5.rename('a'), r21.rename('b'), r63.rename('c')], axis=1).std(axis=1).diff()

def f28_ttcf_488_cci_winsorized_5pct_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Winsorized (5%-trimmed) z-score of CCI over 252d — clips tails before standardizing."""
    return _winsorized_zscore(_cci(high, low, close, 20), YDAYS, 0.05).diff()

def f28_ttcf_489_basket_zscore_avg_504_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean z-score (504d) across basket {trix, tsi, cci, cmo, dpo, kst} — long-context basket position."""
    zs = _basket_zscores(high, low, close, DDAYS_2Y)
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).mean(axis=1).diff()

def f28_ttcf_490_basket_zscore_dispersion_504_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std (dispersion) of 504d z-scores across basket — long-context disagreement."""
    return _h_basket_dispersion(high, low, close).diff()

def f28_ttcf_491_cci_residual_after_removing_trix_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Residual of CCI after OLS-removing TRIX over 63d — unique CCI information."""
    return _rolling_residual(_cci(high, low, close, 20), _trix(close, 15), QDAYS).diff()

def f28_ttcf_492_trix_residual_after_removing_tsi_63_d1(close: pd.Series) -> pd.Series:
    """Residual of TRIX after OLS-removing TSI over 63d — unique TRIX information."""
    return _rolling_residual(_trix(close, 15), _tsi(close, 25, 13), QDAYS).diff()

def f28_ttcf_493_cmo_residual_after_removing_cci_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Residual of CMO after OLS-removing CCI over 63d — unique CMO information."""
    return _rolling_residual(_cmo(close, 14), _cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_494_basket_first_pc_proxy_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First-PC proxy = mean of 504d z-scored basket signals (common component)."""
    return _h_basket_first_pc_proxy(high, low, close).diff()

def f28_ttcf_495_basket_second_pc_proxy_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second-PC proxy = mean of residuals after removing first-PC proxy from each basket signal."""
    return _h_basket_second_pc_proxy(high, low, close).diff()

def f28_ttcf_496_cci_trix_pair_corr_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d Pearson correlation between CCI and TRIX — basket-pair coherence."""
    return _cci(high, low, close, 20).rolling(QDAYS, min_periods=MDAYS).corr(_trix(close, 15)).diff()

def f28_ttcf_497_cci_trix_pair_spread_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d z-score of (z(CCI) - z(TRIX)) over 504d — pair-spread anomaly."""
    zc = _rolling_zscore(_cci(high, low, close, 20), DDAYS_2Y, min_periods=YDAYS)
    zt = _rolling_zscore(_trix(close, 15), DDAYS_2Y, min_periods=YDAYS)
    return _rolling_zscore(zc - zt, YDAYS, min_periods=QDAYS).diff()

def f28_ttcf_498_cross_basket_divergence_regression_residual_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Residual of close-return regressed on basket-mean (z) over 63d — return not explained by basket."""
    ret = close.pct_change()
    bm = _h_basket_first_pc_proxy(high, low, close)
    return _rolling_residual(ret, bm, QDAYS).diff()

def f28_ttcf_499_cross_basket_beta_to_cci_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Beta of basket-first-PC on CCI over 63d — sensitivity of common factor to CCI."""
    return _rolling_beta(_h_basket_first_pc_proxy(high, low, close), _cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_500_cross_basket_residual_variance_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance over 63d of the second-PC proxy — unique-component variance (idiosyncratic basket spread)."""
    return _h_basket_second_pc_proxy(high, low, close).rolling(QDAYS, min_periods=MDAYS).var().diff()

def f28_ttcf_501_dtw_distance_cci_to_50pct_dd_template_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DTW distance from CCI over 63d window to a synthetic 50%-drawdown template."""
    return _rolling_dtw_to_template(_cci(high, low, close, 20), QDAYS, _TPL_50PCT_DD).diff()

def f28_ttcf_502_dtw_distance_trix_to_252h_breakdown_template_63_d1(close: pd.Series) -> pd.Series:
    """DTW distance from TRIX over 63d to a peak-then-breakdown template."""
    return _rolling_dtw_to_template(_trix(close, 15), QDAYS, _TPL_BREAKDOWN_252).diff()

def f28_ttcf_503_cci_path_length_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |diff(CCI)| over 63d — path length (total CCI motion)."""
    return _path_length(_cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_504_cci_path_length_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d z-score of CCI 63d path length — distribution-context path-anomaly."""
    return _rolling_zscore(_path_length(_cci(high, low, close, 20), QDAYS), YDAYS, min_periods=QDAYS).diff()

def f28_ttcf_505_trix_path_curvature_63_d1(close: pd.Series) -> pd.Series:
    """Sum of |second-difference| of TRIX over 63d — TRIX path curvature."""
    return _path_curvature(_trix(close, 15), QDAYS).diff()

def f28_ttcf_506_cci_path_complexity_score_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI path length / |CCI[t] - CCI[t-62]| — winding-vs-direct ratio."""
    return _path_complexity(_cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_507_cmo_path_entropy_63_d1(close: pd.Series) -> pd.Series:
    """Path entropy of CMO over 63d — entropy of binned CMO first differences."""
    return _rolling_path_entropy(_cmo(close, 14), QDAYS).diff()

def f28_ttcf_508_cci_persistence_amplitude_weighted_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Amplitude-weighted sign-persistence: mean(|CCI| * sign-streak-mask) over 63d."""
    return _amplitude_weighted_persistence(_cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_509_trix_path_amplitude_index_63_d1(close: pd.Series) -> pd.Series:
    """Range(TRIX, 63d) / std(TRIX, 63d) — TRIX amplitude in std units."""
    return _amplitude_index(_trix(close, 15), QDAYS).diff()

def f28_ttcf_510_cci_path_decay_index_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(older-half range - recent-half range)/older-half range over 63d — high = recent amplitude decay."""
    return _path_decay_index(_cci(high, low, close, 20), QDAYS).diff()

def f28_ttcf_511_coskew_cci_returns_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-skewness E[(CCI-mu)^2 (ret-mu)] / (std_cci^2 * std_ret) over 21d."""
    return _rolling_coskew(_cci(high, low, close, 20), close.pct_change(), MDAYS).diff()

def f28_ttcf_512_cokurt_cci_returns_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Co-kurtosis E[(CCI-mu)^2 (ret-mu)^2] / (std_cci^2 * std_ret^2) over 21d."""
    return _rolling_cokurt(_cci(high, low, close, 20), close.pct_change(), MDAYS).diff()

def f28_ttcf_513_cci_in_extreme_return_tail_avg_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean of CCI restricted to bars where |return| > 252d 95th percentile of |return| — tail-event CCI."""
    ret = close.pct_change()
    q95 = ret.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    mask = ret.abs() > q95
    c = _cci(high, low, close, 20).where(mask)
    return c.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_514_corr_abs_returns_cci_lag1_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d correlation between |returns| and CCI lagged 1 bar — leverage-effect proxy."""
    c = _cci(high, low, close, 20).shift(1)
    ar = close.pct_change().abs()
    return ar.rolling(QDAYS, min_periods=MDAYS).corr(c).diff()

def f28_ttcf_515_trix_coskew_returns_21_d1(close: pd.Series) -> pd.Series:
    """Co-skewness of TRIX with returns over 21d."""
    return _rolling_coskew(_trix(close, 15), close.pct_change(), MDAYS).diff()

def f28_ttcf_516_cmo_cokurt_returns_21_d1(close: pd.Series) -> pd.Series:
    """Co-kurtosis of CMO with returns over 21d."""
    return _rolling_cokurt(_cmo(close, 14), close.pct_change(), MDAYS).diff()

def f28_ttcf_517_asymmetric_corr_up_vs_down_cci_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(CCI, ret | ret>0) - Corr(CCI, ret | ret<0) over 63d — directional-sensitivity asymmetry."""
    c = _cci(high, low, close, 20)
    r = close.pct_change()
    return (_asymmetric_corr(c, r, QDAYS, up=True) - _asymmetric_corr(c, r, QDAYS, up=False)).diff()

def f28_ttcf_518_cci_tail_dependence_proxy_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frac of past 63d where both CCI > 252d-q90 AND return > 252d-q90(ret) — joint right-tail."""
    c = _cci(high, low, close, 20)
    r = close.pct_change()
    cq = c.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    rq = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    joint = ((c > cq) & (r > rq)).astype(float)
    return joint.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f28_ttcf_519_basket_avg_coskew_returns_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean across basket of co-skewness with returns over 21d."""
    return _h_basket_avg_coskew_returns(high, low, close, MDAYS).diff()

def f28_ttcf_520_basket_avg_cokurt_returns_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean across basket of co-kurtosis with returns over 21d."""
    return _h_basket_avg_cokurt_returns(high, low, close, MDAYS).diff()

def f28_ttcf_521_batch_4_basket_orthogonal_aggregate_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Orthogonal-aggregate v4: residual-z aggregate after removing basket-mean common variance."""
    return _h_basket_orthogonal_aggregate_zscore_252(high, low, close).diff()

def f28_ttcf_522_basket_recall_optimized_v4_score_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recall-oriented v4: basket-dispersion + |first-PC| + DTW-to-breakdown — broad signal."""
    disp = _h_basket_dispersion(high, low, close).fillna(0)
    pc1 = _h_basket_first_pc_proxy(high, low, close).abs().fillna(0)
    dtw = _h_basket_dtw_to_breakdown_template(high, low, close).fillna(0)
    return (disp + pc1 + dtw).where(close.notna(), np.nan).diff()

def f28_ttcf_523_basket_precision_optimized_v4_score_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Precision-oriented v4: high only when both first-PC < -1 AND second-PC < -0.5 AND dispersion > median."""
    pc1 = _h_basket_first_pc_proxy(high, low, close)
    pc2 = _h_basket_second_pc_proxy(high, low, close)
    disp = _h_basket_dispersion(high, low, close)
    disp_med = disp.rolling(YDAYS, min_periods=QDAYS).median()
    cond = (pc1 < -1.0) & (pc2 < -0.5) & (disp > disp_med)
    raw = pc1.abs() + pc2.abs() + disp
    return raw.where(cond, 0.0).where(close.notna(), np.nan).diff()

def f28_ttcf_524_basket_topping_master_v4_score_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Topping-master v4 = (first-PC > 1) * (path-complexity) * (dispersion). Stronger when complexity rises with extension."""
    pc1 = _h_basket_first_pc_proxy(high, low, close).fillna(0)
    pc = _h_basket_path_complexity_score(high, low, close).fillna(0)
    disp = _h_basket_dispersion(high, low, close).fillna(0)
    cond = (pc1 > 1.0).astype(float)
    return (cond * pc * disp).where(close.notna(), np.nan).diff()

def f28_ttcf_525_absolute_terminal_basket_v4_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (first-PC was > 2 in past 63d) AND (now first-PC < -0.5) AND (second-PC < -0.5) — absolute terminal v4."""
    pc1 = _h_basket_first_pc_proxy(high, low, close)
    pc2 = _h_basket_second_pc_proxy(high, low, close)
    had_blow = (pc1.shift(1) > 2.0).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    cond = (had_blow > 0) & (pc1 < -0.5) & (pc2 < -0.5)
    return cond.astype(float).where(pc1.notna(), np.nan).diff()
TRIX_TSI_CCI_FAMILY_D1_REGISTRY_451_525 = {'f28_ttcf_451_rsi_of_cci_14_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_451_rsi_of_cci_14_d1}, 'f28_ttcf_452_rsi_of_trix_14_d1': {'inputs': ['close'], 'func': f28_ttcf_452_rsi_of_trix_14_d1}, 'f28_ttcf_453_stoch_of_cci_14_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_453_stoch_of_cci_14_d1}, 'f28_ttcf_454_stoch_of_trix_14_d1': {'inputs': ['close'], 'func': f28_ttcf_454_stoch_of_trix_14_d1}, 'f28_ttcf_455_macd_of_cci_12_26_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_455_macd_of_cci_12_26_d1}, 'f28_ttcf_456_macd_of_cmo_12_26_d1': {'inputs': ['close'], 'func': f28_ttcf_456_macd_of_cmo_12_26_d1}, 'f28_ttcf_457_trix_of_cci_15_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_457_trix_of_cci_15_d1}, 'f28_ttcf_458_cci_of_trix_20_d1': {'inputs': ['close'], 'func': f28_ttcf_458_cci_of_trix_20_d1}, 'f28_ttcf_459_cmo_of_cci_14_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_459_cmo_of_cci_14_d1}, 'f28_ttcf_460_williams_r_of_cci_14_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_460_williams_r_of_cci_14_d1}, 'f28_ttcf_461_tsi_of_cci_25_13_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_461_tsi_of_cci_25_13_d1}, 'f28_ttcf_462_fisher_transform_of_cci_10_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_462_fisher_transform_of_cci_10_d1}, 'f28_ttcf_463_inverse_fisher_transform_of_cci_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_463_inverse_fisher_transform_of_cci_normalized_d1}, 'f28_ttcf_464_ema_of_trix_minus_sma_of_trix_15_d1': {'inputs': ['close'], 'func': f28_ttcf_464_ema_of_trix_minus_sma_of_trix_15_d1}, 'f28_ttcf_465_ema_of_cci_minus_sma_of_cci_20_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_465_ema_of_cci_minus_sma_of_cci_20_d1}, 'f28_ttcf_466_cci_when_dd_5_to_10pct_avg_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_466_cci_when_dd_5_to_10pct_avg_63_d1}, 'f28_ttcf_467_cci_when_dd_10_to_20pct_avg_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_467_cci_when_dd_10_to_20pct_avg_63_d1}, 'f28_ttcf_468_cci_when_dd_above_20pct_avg_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_468_cci_when_dd_above_20pct_avg_63_d1}, 'f28_ttcf_469_trix_when_dd_above_20pct_avg_63_d1': {'inputs': ['close'], 'func': f28_ttcf_469_trix_when_dd_above_20pct_avg_63_d1}, 'f28_ttcf_470_cmo_when_dd_above_20pct_avg_63_d1': {'inputs': ['close'], 'func': f28_ttcf_470_cmo_when_dd_above_20pct_avg_63_d1}, 'f28_ttcf_471_cci_change_at_first_dd_above_10pct_post_peak_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_471_cci_change_at_first_dd_above_10pct_post_peak_d1}, 'f28_ttcf_472_cci_change_at_first_dd_above_20pct_post_peak_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_472_cci_change_at_first_dd_above_20pct_post_peak_d1}, 'f28_ttcf_473_cci_at_first_dd_above_30pct_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_473_cci_at_first_dd_above_30pct_value_d1}, 'f28_ttcf_474_trix_at_first_dd_above_30pct_value_d1': {'inputs': ['close'], 'func': f28_ttcf_474_trix_at_first_dd_above_30pct_value_d1}, 'f28_ttcf_475_cci_recovery_pattern_post_dd_avg_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_475_cci_recovery_pattern_post_dd_avg_63_d1}, 'f28_ttcf_476_cci_hysteresis_indicator_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_476_cci_hysteresis_indicator_252_d1}, 'f28_ttcf_477_cci_path_dependence_from_peak_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_477_cci_path_dependence_from_peak_d1}, 'f28_ttcf_478_cci_asymmetry_up_down_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_478_cci_asymmetry_up_down_d1}, 'f28_ttcf_479_cci_conditional_std_at_dd_above_20pct_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_479_cci_conditional_std_at_dd_above_20pct_d1}, 'f28_ttcf_480_cci_distribution_shift_pre_post_dd_zscore_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_480_cci_distribution_shift_pre_post_dd_zscore_d1}, 'f28_ttcf_481_cci_quantile_normal_transform_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_481_cci_quantile_normal_transform_252_d1}, 'f28_ttcf_482_trix_quantile_normal_transform_252_d1': {'inputs': ['close'], 'func': f28_ttcf_482_trix_quantile_normal_transform_252_d1}, 'f28_ttcf_483_cmo_quantile_normal_transform_252_d1': {'inputs': ['close'], 'func': f28_ttcf_483_cmo_quantile_normal_transform_252_d1}, 'f28_ttcf_484_cci_robust_zscore_mad_504_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_484_cci_robust_zscore_mad_504_d1}, 'f28_ttcf_485_trix_modified_zscore_iqr_252_d1': {'inputs': ['close'], 'func': f28_ttcf_485_trix_modified_zscore_iqr_252_d1}, 'f28_ttcf_486_multi_window_cci_rank_avg_5_21_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_486_multi_window_cci_rank_avg_5_21_63_d1}, 'f28_ttcf_487_multi_window_trix_rank_std_5_21_63_d1': {'inputs': ['close'], 'func': f28_ttcf_487_multi_window_trix_rank_std_5_21_63_d1}, 'f28_ttcf_488_cci_winsorized_5pct_zscore_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_488_cci_winsorized_5pct_zscore_252_d1}, 'f28_ttcf_489_basket_zscore_avg_504_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_489_basket_zscore_avg_504_d1}, 'f28_ttcf_490_basket_zscore_dispersion_504_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_490_basket_zscore_dispersion_504_d1}, 'f28_ttcf_491_cci_residual_after_removing_trix_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_491_cci_residual_after_removing_trix_63_d1}, 'f28_ttcf_492_trix_residual_after_removing_tsi_63_d1': {'inputs': ['close'], 'func': f28_ttcf_492_trix_residual_after_removing_tsi_63_d1}, 'f28_ttcf_493_cmo_residual_after_removing_cci_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_493_cmo_residual_after_removing_cci_63_d1}, 'f28_ttcf_494_basket_first_pc_proxy_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_494_basket_first_pc_proxy_d1}, 'f28_ttcf_495_basket_second_pc_proxy_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_495_basket_second_pc_proxy_d1}, 'f28_ttcf_496_cci_trix_pair_corr_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_496_cci_trix_pair_corr_63_d1}, 'f28_ttcf_497_cci_trix_pair_spread_zscore_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_497_cci_trix_pair_spread_zscore_252_d1}, 'f28_ttcf_498_cross_basket_divergence_regression_residual_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_498_cross_basket_divergence_regression_residual_63_d1}, 'f28_ttcf_499_cross_basket_beta_to_cci_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_499_cross_basket_beta_to_cci_63_d1}, 'f28_ttcf_500_cross_basket_residual_variance_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_500_cross_basket_residual_variance_63_d1}, 'f28_ttcf_501_dtw_distance_cci_to_50pct_dd_template_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_501_dtw_distance_cci_to_50pct_dd_template_63_d1}, 'f28_ttcf_502_dtw_distance_trix_to_252h_breakdown_template_63_d1': {'inputs': ['close'], 'func': f28_ttcf_502_dtw_distance_trix_to_252h_breakdown_template_63_d1}, 'f28_ttcf_503_cci_path_length_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_503_cci_path_length_63_d1}, 'f28_ttcf_504_cci_path_length_zscore_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_504_cci_path_length_zscore_252_d1}, 'f28_ttcf_505_trix_path_curvature_63_d1': {'inputs': ['close'], 'func': f28_ttcf_505_trix_path_curvature_63_d1}, 'f28_ttcf_506_cci_path_complexity_score_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_506_cci_path_complexity_score_63_d1}, 'f28_ttcf_507_cmo_path_entropy_63_d1': {'inputs': ['close'], 'func': f28_ttcf_507_cmo_path_entropy_63_d1}, 'f28_ttcf_508_cci_persistence_amplitude_weighted_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_508_cci_persistence_amplitude_weighted_63_d1}, 'f28_ttcf_509_trix_path_amplitude_index_63_d1': {'inputs': ['close'], 'func': f28_ttcf_509_trix_path_amplitude_index_63_d1}, 'f28_ttcf_510_cci_path_decay_index_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_510_cci_path_decay_index_63_d1}, 'f28_ttcf_511_coskew_cci_returns_21_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_511_coskew_cci_returns_21_d1}, 'f28_ttcf_512_cokurt_cci_returns_21_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_512_cokurt_cci_returns_21_d1}, 'f28_ttcf_513_cci_in_extreme_return_tail_avg_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_513_cci_in_extreme_return_tail_avg_63_d1}, 'f28_ttcf_514_corr_abs_returns_cci_lag1_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_514_corr_abs_returns_cci_lag1_63_d1}, 'f28_ttcf_515_trix_coskew_returns_21_d1': {'inputs': ['close'], 'func': f28_ttcf_515_trix_coskew_returns_21_d1}, 'f28_ttcf_516_cmo_cokurt_returns_21_d1': {'inputs': ['close'], 'func': f28_ttcf_516_cmo_cokurt_returns_21_d1}, 'f28_ttcf_517_asymmetric_corr_up_vs_down_cci_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_517_asymmetric_corr_up_vs_down_cci_63_d1}, 'f28_ttcf_518_cci_tail_dependence_proxy_63_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_518_cci_tail_dependence_proxy_63_d1}, 'f28_ttcf_519_basket_avg_coskew_returns_21_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_519_basket_avg_coskew_returns_21_d1}, 'f28_ttcf_520_basket_avg_cokurt_returns_21_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_520_basket_avg_cokurt_returns_21_d1}, 'f28_ttcf_521_batch_4_basket_orthogonal_aggregate_zscore_252_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_521_batch_4_basket_orthogonal_aggregate_zscore_252_d1}, 'f28_ttcf_522_basket_recall_optimized_v4_score_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_522_basket_recall_optimized_v4_score_d1}, 'f28_ttcf_523_basket_precision_optimized_v4_score_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_523_basket_precision_optimized_v4_score_d1}, 'f28_ttcf_524_basket_topping_master_v4_score_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_524_basket_topping_master_v4_score_d1}, 'f28_ttcf_525_absolute_terminal_basket_v4_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_525_absolute_terminal_basket_v4_indicator_d1}}