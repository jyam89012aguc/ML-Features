"""supertrend_psar_chandelier d2 features 151-225 — Pipeline 1b-technical.

Second-derivative (.diff().diff()) of base 151-225 hypotheses. Self-contained:
helpers and base-feature bodies are re-included; each d2 function returns
base.diff().diff().

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, no .shift(N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


# ---------------------------- helpers ----------------------------

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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _bars_since_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr); out = np.full(n, np.nan); last = -1
    for i in range(n):
        if arr[i]:
            last = i; out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _supertrend(high, low, close, n=10, mult=3.0, basis='hl2'):
    atr = _atr(high, low, close, n=n)
    mid = (high + low + close) / 3.0 if basis == 'hlc3' else (high + low) / 2.0
    upper = mid + mult * atr; lower = mid - mult * atr
    c = close.values; u = upper.values; l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]; dirn[i] = 1; started = True; continue
        ps = st[i - 1]; pd_ = dirn[i - 1]
        if np.isnan(ps):
            st[i] = l[i]; dirn[i] = 1; continue
        if pd_ == 1:
            stop = max(ps, l[i])
            if c[i] < stop:
                dirn[i] = -1; st[i] = u[i]
            else:
                dirn[i] = 1; st[i] = stop
        else:
            stop = min(ps, u[i])
            if c[i] > stop:
                dirn[i] = 1; st[i] = l[i]
            else:
                dirn[i] = -1; st[i] = stop
    return pd.Series(st, index=close.index), pd.Series(dirn, index=close.index, dtype="int8")


def _supertrend_ohlc4(open_, high, low, close, n=10, mult=3.0):
    atr = _atr(high, low, close, n=n)
    mid = (open_ + high + low + close) / 4.0
    upper = mid + mult * atr; lower = mid - mult * atr
    c = close.values; u = upper.values; l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]; dirn[i] = 1; started = True; continue
        ps = st[i - 1]; pd_ = dirn[i - 1]
        if np.isnan(ps):
            st[i] = l[i]; dirn[i] = 1; continue
        if pd_ == 1:
            stop = max(ps, l[i])
            if c[i] < stop:
                dirn[i] = -1; st[i] = u[i]
            else:
                dirn[i] = 1; st[i] = stop
        else:
            stop = min(ps, u[i])
            if c[i] > stop:
                dirn[i] = 1; st[i] = l[i]
            else:
                dirn[i] = -1; st[i] = stop
    return pd.Series(st, index=close.index), pd.Series(dirn, index=close.index, dtype="int8")


def _heikin_ashi(open_, high, low, close):
    ha_close = (open_ + high + low + close) / 4.0
    ha_open = (open_.shift(1) + close.shift(1)) / 2.0
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return ha_open, ha_high, ha_low, ha_close


def _wtr_atr(high, low, close, n=21):
    tr = _true_range(high, low, close)
    def _wm(x):
        v = x[~np.isnan(x)]
        if v.size == 0:
            return np.nan
        w = np.arange(1, v.size + 1, dtype=float)
        return float(np.dot(v, w) / w.sum())
    return tr.rolling(n, min_periods=max(n // 3, 2)).apply(_wm, raw=True)


def _ewma_atr(high, low, close, n=21, lam=0.94):
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1 - lam, min_periods=max(n // 3, 2), adjust=False).mean()


def _psar(high, low, af0=0.02, afmax=0.2):
    h = high.values; l = low.values
    nb = len(h)
    sar = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    if nb == 0:
        return pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype="int8")
    start = 0
    while start < nb and (np.isnan(h[start]) or np.isnan(l[start])):
        start += 1
    if start >= nb - 1:
        return pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype="int8")
    sar[start] = l[start]; dirn[start] = 1
    ep = h[start]; af = af0
    for i in range(start + 1, nb):
        if np.isnan(h[i]) or np.isnan(l[i]):
            sar[i] = sar[i - 1]; dirn[i] = dirn[i - 1]; continue
        ps = sar[i - 1]; pd_ = dirn[i - 1]
        ns = ps + af * (ep - ps)
        if pd_ == 1:
            lp1 = l[i - 1] if not np.isnan(l[i - 1]) else ns
            lp2 = l[i - 2] if i >= 2 and not np.isnan(l[i - 2]) else lp1
            ns = min(ns, lp1, lp2)
            if l[i] < ns:
                dirn[i] = -1; sar[i] = ep; ep = l[i]; af = af0
            else:
                dirn[i] = 1; sar[i] = ns
                if h[i] > ep:
                    ep = h[i]; af = min(af + af0, afmax)
        else:
            hp1 = h[i - 1] if not np.isnan(h[i - 1]) else ns
            hp2 = h[i - 2] if i >= 2 and not np.isnan(h[i - 2]) else hp1
            ns = max(ns, hp1, hp2)
            if h[i] > ns:
                dirn[i] = 1; sar[i] = ep; ep = h[i]; af = af0
            else:
                dirn[i] = -1; sar[i] = ns
                if l[i] < ep:
                    ep = l[i]; af = min(af + af0, afmax)
    return pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype="int8")


def _chandelier_long(high, low, close, n=22, mult=3.0):
    atr = _atr(high, low, close, n=n)
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return hh - mult * atr


def _chandelier_short(high, low, close, n=22, mult=3.0):
    atr = _atr(high, low, close, n=n)
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return ll + mult * atr


def _atr_trail(close, atr, mult=3.0):
    c = close.values; a = atr.values
    nb = len(c); stop = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(c[i]) or np.isnan(a[i]):
            if i > 0:
                stop[i] = stop[i - 1]; dirn[i] = dirn[i - 1]
            continue
        cu = c[i] - mult * a[i]; cd = c[i] + mult * a[i]
        if not started:
            stop[i] = cu; dirn[i] = 1; started = True; continue
        ps = stop[i - 1]; pd_ = dirn[i - 1]
        if np.isnan(ps):
            stop[i] = cu; dirn[i] = 1; continue
        if pd_ == 1:
            ns = max(ps, cu)
            if c[i] < ns:
                dirn[i] = -1; stop[i] = cd
            else:
                dirn[i] = 1; stop[i] = ns
        else:
            ns = min(ps, cd)
            if c[i] > ns:
                dirn[i] = 1; stop[i] = cu
            else:
                dirn[i] = -1; stop[i] = ns
    return pd.Series(stop, index=close.index), pd.Series(dirn, index=close.index, dtype="int8")


def _kase_devstop_long(high, low, close, n=10, mult=3.0):
    tr = _true_range(high, low, close)
    mp = max(n // 3, 2)
    mu = tr.rolling(n, min_periods=mp).mean()
    sd = tr.rolling(n, min_periods=mp).std()
    sk = tr.rolling(n, min_periods=mp).skew().fillna(0)
    adj = mu + sk.clip(-3, 3) * sd
    hc = close.rolling(n, min_periods=mp).max()
    return hc - mult * adj, adj


def _zlema(close, n):
    lag = max(n // 2, 1)
    src = close + (close - close.shift(lag))
    return src.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()


def _mcginley(close, n=14):
    arr = close.values; nb = len(arr)
    out = np.full(nb, np.nan); started = False
    for i in range(nb):
        if np.isnan(arr[i]):
            if i > 0:
                out[i] = out[i - 1]
            continue
        if not started:
            out[i] = arr[i]; started = True; continue
        prev = out[i - 1]
        if np.isnan(prev) or prev == 0:
            out[i] = arr[i]; continue
        ratio = arr[i] / prev; denom = n * (ratio ** 4)
        out[i] = arr[i] if denom == 0 else prev + (arr[i] - prev) / denom
    return pd.Series(out, index=close.index)


def _t3_tillson(close, n=8, vol=0.7):
    e1 = close.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e2 = e1.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e3 = e2.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e4 = e3.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e5 = e4.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e6 = e5.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    b = vol
    c1 = -b * b * b; c2 = 3 * b * b + 3 * b * b * b
    c3 = -6 * b * b - 3 * b - 3 * b * b * b; c4 = 1 + 3 * b + b * b * b + 3 * b * b
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _hilo_activator(high, low, n=3):
    mp = max(n // 3, 2)
    mh = high.rolling(n, min_periods=mp).mean()
    ml = low.rolling(n, min_periods=mp).mean()
    c = ((high + low) / 2.0).values
    mhv = mh.values; mlv = ml.values
    nb = len(c); stop = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    for i in range(nb):
        if np.isnan(c[i]) or np.isnan(mhv[i]) or np.isnan(mlv[i]):
            if i > 0:
                stop[i] = stop[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if i == 0 or dirn[i - 1] == 0:
            stop[i] = mlv[i]; dirn[i] = 1; continue
        if dirn[i - 1] == 1:
            if c[i] < mlv[i]:
                dirn[i] = -1; stop[i] = mhv[i]
            else:
                dirn[i] = 1; stop[i] = mlv[i]
        else:
            if c[i] > mhv[i]:
                dirn[i] = 1; stop[i] = mlv[i]
            else:
                dirn[i] = -1; stop[i] = mhv[i]
    return pd.Series(stop, index=high.index), pd.Series(dirn, index=high.index, dtype="int8")


def _chande_kroll(high, low, close, p=10, q=20, mult=3.0):
    atr = _atr(high, low, close, n=p)
    mp = max(p // 3, 2); mq = max(q // 3, 2)
    h_stop = (high.rolling(p, min_periods=mp).max() - mult * atr).rolling(q, min_periods=mq).max()
    l_stop = (low.rolling(p, min_periods=mp).min() + mult * atr).rolling(q, min_periods=mq).min()
    return h_stop, l_stop


def _wma(s, n):
    if n < 1:
        return pd.Series(np.nan, index=s.index)
    def _f(x):
        if np.isnan(x).any():
            return np.nan
        L = len(x); w = np.arange(1, L + 1, dtype=float)
        return float(np.dot(x, w) / w.sum())
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hma(close, n):
    half = max(int(n // 2), 2); rt = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(close, half) - _wma(close, n), rt)


# ---------------------------- base bodies (internal) ----------------------------

def _b151(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0, basis='hlc3')
    return _safe_log(close) - _safe_log(st)


def _b152(open, high, low, close):
    st, _ = _supertrend_ohlc4(open, high, low, close, n=10, mult=3.0)
    return _safe_log(close) - _safe_log(st)


def _b153(open, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open, high, low, close)
    _, d = _supertrend(ha_h, ha_l, ha_c, n=10, mult=3.0, basis='hl2')
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def _b154(open, high, low, close):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open, high, low, close)
    st, _ = _supertrend(ha_h, ha_l, ha_c, n=10, mult=3.0, basis='hl2')
    return _safe_div(ha_c - st, _atr(high, low, close, n=MDAYS))


def _b155(high, low, close):
    watr = _wtr_atr(high, low, close, n=10)
    hl2 = (high + low) / 2.0
    upper = hl2 + 3.0 * watr; lower = hl2 - 3.0 * watr
    c = close.values; u = upper.values; l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8); started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]; dirn[i] = 1; started = True; continue
        ps = st[i - 1]; pd_ = dirn[i - 1]
        if np.isnan(ps):
            st[i] = l[i]; dirn[i] = 1; continue
        if pd_ == 1:
            stop = max(ps, l[i])
            if c[i] < stop:
                dirn[i] = -1; st[i] = u[i]
            else:
                dirn[i] = 1; st[i] = stop
        else:
            stop = min(ps, u[i])
            if c[i] > stop:
                dirn[i] = 1; st[i] = l[i]
            else:
                dirn[i] = -1; st[i] = stop
    st_s = pd.Series(st, index=close.index)
    return _safe_log(close) - _safe_log(st_s)


def _b156(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool).values
    n = len(flip); refl = np.zeros(n, dtype=float)
    for i in range(1, n):
        if flip[i]:
            for k in range(1, min(4, i + 1)):
                if flip[i - k]:
                    refl[i] = 1.0; break
    return pd.Series(refl, index=close.index).rolling(QDAYS, min_periods=MDAYS).sum()


def _b157(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool).values
    n = len(flip); refl = np.zeros(n, dtype=float); fl = np.zeros(n, dtype=float)
    for i in range(n):
        if flip[i]:
            fl[i] = 1.0
            for k in range(1, min(4, i + 1)):
                if flip[i - k]:
                    refl[i] = 1.0; break
    rs = pd.Series(refl, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()
    fs = pd.Series(fl, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rs, fs)


def _b158(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high >= rmax).astype(float)
    recent = new_high.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return ((d == -1) & recent).astype(float).where(d != 0, np.nan)


def _b159(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=4.0)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b160(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=1.5)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b161(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    short_mask = (d == -1).astype(float)
    def _longest(w):
        run = best = 0
        for v in w:
            if v > 0:
                run += 1
                if run > best:
                    best = run
            else:
                run = 0
        return float(best)
    return short_mask.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True)


def _b162(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    sm = (d == -1).astype(int).values
    n = len(sm); out = np.full(n, np.nan, dtype=float); win = YDAYS
    for i in range(n):
        lo = max(0, i - win + 1)
        w = sm[lo:i + 1]
        runs = []; run = 0; prev = 0
        for v in w:
            if v == 1:
                run += 1
            else:
                if prev == 1 and run > 0:
                    runs.append(run)
                run = 0
            prev = v
        if runs:
            out[i] = float(np.mean(runs))
    return pd.Series(out, index=close.index)


def _b163(high, low):
    _, d = _psar(high, low, af0=0.04, afmax=0.40)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b164(high, low):
    _, d = _psar(high, low, af0=0.01, afmax=0.10)
    return (d.diff().abs() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def _b165(high, low):
    _, d = _psar(high, low)
    flip = (d.diff().abs() > 0).astype(float)
    return (flip.rolling(10, min_periods=3).sum() >= 3).astype(float).where(flip.notna(), np.nan)


def _b166(high, low):
    _, d = _psar(high, low)
    flip = (d.diff().abs() > 0).astype(float)
    cl = (flip.rolling(MDAYS, min_periods=WDAYS).sum() >= 5).astype(float)
    return cl.rolling(YDAYS, min_periods=QDAYS).sum()


def _b167(high, low):
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    long_arr = (d == 1).astype(int).values
    n = len(d); out = np.zeros(n, dtype=float); run = 0
    for i in range(n):
        if long_arr[i] == 1:
            run += 1
        else:
            if down[i] and run >= 60:
                out[i] = 1.0
            run = 0
    return pd.Series(out, index=high.index).where(d != 0, np.nan)


def _b168(high, low):
    h = high.values; l = low.values
    nb = len(h)
    sar = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8); af_arr = np.full(nb, np.nan)
    if nb < 2:
        return pd.Series(np.nan, index=high.index)
    start = 0
    while start < nb and (np.isnan(h[start]) or np.isnan(l[start])):
        start += 1
    if start >= nb - 1:
        return pd.Series(np.nan, index=high.index)
    sar[start] = l[start]; dirn[start] = 1
    ep = h[start]; af = 0.02; af_arr[start] = af
    for i in range(start + 1, nb):
        if np.isnan(h[i]) or np.isnan(l[i]):
            sar[i] = sar[i - 1]; dirn[i] = dirn[i - 1]; af_arr[i] = af_arr[i - 1]; continue
        ps = sar[i - 1]; pd_ = dirn[i - 1]
        ns = ps + af * (ep - ps)
        if pd_ == 1:
            lp1 = l[i - 1] if not np.isnan(l[i - 1]) else ns
            lp2 = l[i - 2] if i >= 2 and not np.isnan(l[i - 2]) else lp1
            ns = min(ns, lp1, lp2)
            if l[i] < ns:
                dirn[i] = -1; sar[i] = ep; ep = l[i]; af = 0.02
            else:
                dirn[i] = 1; sar[i] = ns
                if h[i] > ep:
                    ep = h[i]; af = min(af + 0.02, 0.2)
        else:
            hp1 = h[i - 1] if not np.isnan(h[i - 1]) else ns
            hp2 = h[i - 2] if i >= 2 and not np.isnan(h[i - 2]) else hp1
            ns = max(ns, hp1, hp2)
            if h[i] > ns:
                dirn[i] = 1; sar[i] = ep; ep = h[i]; af = 0.02
            else:
                dirn[i] = -1; sar[i] = ns
                if l[i] < ep:
                    ep = l[i]; af = min(af + 0.02, 0.2)
        af_arr[i] = af
    af_s = pd.Series(af_arr, index=high.index)
    dirn_s = pd.Series(dirn, index=high.index)
    at_max = (af_s >= 0.199)
    flip = (dirn_s.diff().abs() > 0)
    am5 = at_max.rolling(WDAYS, min_periods=1).max() > 0
    fl5 = flip.rolling(WDAYS, min_periods=1).max() > 0
    return (am5 & fl5).astype(float).where(dirn_s != 0, np.nan)


def _b169(open, high, low, close):
    sar, d = _psar(high, low)
    long_state = (d.shift(1) == 1)
    gap = _safe_div(sar - open, close)
    return gap.where(long_state & (open < sar), 0.0).where(d.notna() & open.notna(), np.nan)


def _b170(high, low, close):
    ch = _chandelier_long(high, low, close, n=22, mult=3.0)
    raw = _safe_div(close - ch, _atr(high, low, close, n=MDAYS))
    return _rolling_zscore(raw, DDAYS_2Y, min_periods=YDAYS)


def _b171(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    return ((close > cl) & (close < cs)).astype(float).where(cl.notna() & cs.notna(), np.nan)


def _b172(high, low, close):
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    return (close > cs).astype(float).where(cs.notna(), np.nan).rolling(QDAYS, min_periods=MDAYS).sum()


def _b173(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    br = (close < cl) & cl.notna()
    br5 = br.shift(5).fillna(False).astype(bool)
    confirmed = br5 & (low < low.shift(5))
    return confirmed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def _b174(high, low, close):
    cl = _chandelier_long(high, low, close, n=50, mult=2.0)
    return _safe_div(close - cl, _atr(high, low, close, n=MDAYS))


def _b175(high, low, close):
    cl = _chandelier_long(high, low, close, n=10, mult=4.0)
    return _safe_div(close - cl, _atr(high, low, close, n=MDAYS))


def _b176(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    gap = close - cl
    return _safe_div(gap.rolling(MDAYS, min_periods=WDAYS).std(), gap.rolling(YDAYS, min_periods=QDAYS).std())


def _b177(high, low, close):
    ks, _ = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    return _safe_div(close - ks, _atr(high, low, close, n=MDAYS))


def _b178(high, low, close):
    ks, _ = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    return (close < ks).astype(float).where(ks.notna(), np.nan).rolling(QDAYS, min_periods=MDAYS).sum()


def _b179(high, low, close):
    ks, adj = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    warning = ks + 1.0 * adj
    return _safe_div(close - warning, _atr(high, low, close, n=MDAYS))


def _b180(high, low, close):
    atr15 = _atr(high, low, close, n=15)
    vs, _ = _atr_trail(close, atr15, mult=2.0)
    return _safe_div(close - vs, _atr(high, low, close, n=MDAYS))


def _b181(high, low, close):
    atr15 = _atr(high, low, close, n=15)
    _, d = _atr_trail(close, atr15, mult=2.0)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b182(high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    _, d = _atr_trail(close, atr, mult=1.0)
    return ((d == -1) & (d.shift(1) == 1)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b183(high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    _, d = _atr_trail(close, atr, mult=5.0)
    return ((d == -1) & (d.shift(1) == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def _multi_trail_short_mask(open, high, low, close):
    _, d_st = _supertrend(high, low, close, n=10, mult=3.0)
    _, d_psar = _psar(high, low)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    d_cl = (close < cl).astype(int).where(cl.notna(), 0).fillna(0).astype(int)
    atr = _atr(high, low, close, n=MDAYS)
    _, d_at = _atr_trail(close, atr, mult=3.0)
    hma = _hma(close, 20)
    d_hma = (close < hma).astype(int).where(hma.notna(), 0).fillna(0).astype(int)
    return (d_st == -1).astype(int), (d_psar == -1).astype(int), d_cl, (d_at == -1).astype(int), d_hma


def _b184(open, high, low, close):
    s = _multi_trail_short_mask(open, high, low, close)
    return (s[0] + s[1] + s[2] + s[3] + s[4]).astype(float)


def _b185(open, high, low, close):
    s = _multi_trail_short_mask(open, high, low, close)
    def _fl(x):
        flip = ((x == 1) & (x.shift(1) == 0)).astype(float)
        return flip.rolling(WDAYS, min_periods=1).max()
    return (_fl(s[0]) + _fl(s[1]) + _fl(s[2]) + _fl(s[3]) + _fl(s[4])).astype(float)


def _b186(open, high, low, close):
    s = _multi_trail_short_mask(open, high, low, close)
    def _fl(x):
        flip = ((x == 1) & (x.shift(1) == 0)).astype(float)
        return flip.rolling(10, min_periods=1).max()
    return (_fl(s[0]) + _fl(s[1]) + _fl(s[2]) + _fl(s[3]) + _fl(s[4])).astype(float)


def _b187(open, high, low, close):
    s = _multi_trail_short_mask(open, high, low, close)
    def _fl(x):
        flip = ((x == 1) & (x.shift(1) == 0)).astype(float)
        return flip.rolling(MDAYS, min_periods=1).max()
    return (_fl(s[0]) + _fl(s[1]) + _fl(s[2]) + _fl(s[3]) + _fl(s[4])).astype(float)


def _b188(high, low):
    _, d = _psar(high, low)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    return _bars_since_true(up)


def _b189(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    long_state = (close >= cl) & cl.notna()
    up = (long_state & ~long_state.shift(1).fillna(False)).astype(bool)
    return _bars_since_true(up)


def _b190(high, low, close):
    atr = _atr(high, low, close, n=MDAYS)
    _, d = _atr_trail(close, atr, mult=3.0)
    return _bars_since_true((d.diff().abs() > 0).astype(bool))


def _post_flip_extreme(close, flip_mask, window, mode='min'):
    arr = close.values; flip = flip_mask.values.astype(bool)
    n = len(arr); out = np.full(n, np.nan)
    last_flip_idx = -1; last_flip_close = np.nan
    for i in range(n):
        if flip[i]:
            last_flip_idx = i; last_flip_close = arr[i]
        if last_flip_idx >= 0 and (i - last_flip_idx) <= window:
            lo = last_flip_idx; hi = i + 1
            if hi > lo:
                seg = arr[lo:hi]
                v = np.nanmin(seg) if mode == 'min' else np.nanmax(seg)
                if not np.isnan(v) and not np.isnan(last_flip_close) and last_flip_close > 0:
                    out[i] = (v - last_flip_close) / last_flip_close
    return pd.Series(out, index=close.index)


def _b191(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='max')


def _b192(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='min')


def _b193(high, low, close):
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='min')


def _b194(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    br = ((close < cl) & ~(close.shift(1) < cl.shift(1))).fillna(False).astype(bool)
    return _post_flip_extreme(close, br, MDAYS, mode='min')


def _b195(high, low, close, volume):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    v = volume.values; n = len(v); out = np.full(n, np.nan)
    prior_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean().shift(1).values
    last_flip = -1
    for i in range(n):
        if down[i]:
            last_flip = i
        if last_flip >= 0 and (i - last_flip) < WDAYS:
            seg = v[last_flip:i + 1]; seg = seg[~np.isnan(seg)]
            if seg.size > 0 and not np.isnan(prior_mean[last_flip]) and prior_mean[last_flip] > 0:
                out[i] = float(seg.mean()) / float(prior_mean[last_flip])
    return pd.Series(out, index=close.index)


def _b196(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    return (d.diff().abs() > 0).astype(float).rolling(42, min_periods=10).sum()


def _b197(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    fl21 = flip.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return fl21.where(pos >= 0.9, np.nan)


def _b198(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    fl21 = flip.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return fl21.where(pos >= 0.95, np.nan)


def _b199(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    gap = close - st
    return _safe_div(gap.rolling(MDAYS, min_periods=WDAYS).std(), gap.rolling(YDAYS, min_periods=QDAYS).std())


def _b200(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    gap = (close - st).rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(gap, YDAYS)


def _b201(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    g = _safe_div(close - st, close)
    return g.rolling(QDAYS, min_periods=MDAYS).std()


def _b202(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    long_arr = (d == 1).astype(int).values
    n = len(d); out = np.zeros(n, dtype=float); run = 0
    for i in range(n):
        if long_arr[i] == 1:
            run += 1
        else:
            if down[i] and run >= YDAYS:
                out[i] = 1.0
            run = 0
    return pd.Series(out, index=close.index).where(d != 0, np.nan)


def _b203(high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    c = close.values; n = len(c); out = np.full(n, np.nan)
    last = -1; cval = np.nan
    for i in range(n):
        if down[i]:
            last = i; cval = c[i]
        if last >= 0 and (i - last) <= WDAYS and not np.isnan(cval) and cval > 0 and not np.isnan(c[i]) and c[i] > 0:
            out[i] = np.log(c[i]) - np.log(cval)
    return pd.Series(out, index=close.index)


def _b204(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sl = _rolling_slope(_safe_div(st, close), MDAYS)
    return np.degrees(np.arctan(sl))


def _b205(high, low, close):
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    norm = _safe_div(st, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


def _b206(high, low, close):
    sar, _ = _psar(high, low)
    norm = _safe_div(sar, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


def _b207(high, low, close):
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    norm = _safe_div(cl, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


def _b208(high, low, close):
    _, df = _supertrend(high, low, close, n=7, mult=2.0)
    _, ds = _supertrend(high, low, close, n=50, mult=3.0)
    return ((df == -1) & (ds == 1)).astype(float).where((df != 0) & (ds != 0), np.nan)


def _b209(high, low, close):
    _, df = _supertrend(high, low, close, n=7, mult=2.0)
    _, ds = _supertrend(high, low, close, n=50, mult=3.0)
    return ((df == 1) & (ds == -1)).astype(float).where((df != 0) & (ds != 0), np.nan)


def _b210(open, high, low, close):
    _, ha_h, ha_l, _ = _heikin_ashi(open, high, low, close)
    _, d = _psar(ha_h, ha_l)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b211(open, high, low, close):
    _, ha_h, ha_l, ha_c = _heikin_ashi(open, high, low, close)
    sar, _ = _psar(ha_h, ha_l)
    return _safe_div(ha_c - sar, _atr(high, low, close, n=MDAYS))


def _b212(high, low, close):
    eatr = _ewma_atr(high, low, close, n=10, lam=0.94)
    hl2 = (high + low) / 2.0
    upper = hl2 + 3.0 * eatr; lower = hl2 - 3.0 * eatr
    c = close.values; u = upper.values; l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8); started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]; dirn[i] = 1; started = True; continue
        ps = st[i - 1]; pd_ = dirn[i - 1]
        if np.isnan(ps):
            st[i] = l[i]; dirn[i] = 1; continue
        if pd_ == 1:
            stop = max(ps, l[i])
            if c[i] < stop:
                dirn[i] = -1; st[i] = u[i]
            else:
                dirn[i] = 1; st[i] = stop
        else:
            stop = min(ps, u[i])
            if c[i] > stop:
                dirn[i] = 1; st[i] = l[i]
            else:
                dirn[i] = -1; st[i] = stop
    st_s = pd.Series(st, index=close.index)
    return _safe_log(close) - _safe_log(st_s)


def _b213(high, low, close):
    return _safe_div(close - _zlema(close, 20), _atr(high, low, close, n=MDAYS))


def _b214(high, low, close):
    return _safe_div(close - _mcginley(close, n=14), _atr(high, low, close, n=MDAYS))


def _b215(high, low, close):
    return _safe_div(close - _t3_tillson(close, n=8, vol=0.7), _atr(high, low, close, n=MDAYS))


def _b216(high, low):
    _, d = _hilo_activator(high, low, n=5)
    return (d.diff().abs() > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b217(high, low, close):
    stop, _ = _hilo_activator(high, low, n=3)
    return _safe_div(close - stop, _atr(high, low, close, n=MDAYS))


def _b218(high, low, close):
    h_stop, _ = _chande_kroll(high, low, close, p=10, q=20, mult=3.0)
    br = (close < h_stop) & h_stop.notna()
    return (br & ~br.shift(1).fillna(False)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b219(high, low, close):
    h_stop, _ = _chande_kroll(high, low, close, p=10, q=20, mult=3.0)
    br = (close < h_stop) & h_stop.notna()
    br_arr = br.values; n = len(br_arr); rec = np.zeros(n, dtype=float)
    for i in range(n):
        if br_arr[i]:
            end = min(n, i + 1 + WDAYS)
            for j in range(i + 1, end):
                if not br_arr[j]:
                    rec[i] = 1.0; break
    return pd.Series(rec, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()


def _b220(high, low, close):
    ll = low.rolling(20, min_periods=5).min()
    br = (close < ll) & ll.notna()
    return (br & ~br.shift(1).fillna(False)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _b221(high, low, close):
    ll = low.rolling(10, min_periods=3).min()
    br = (close < ll).astype(float).where(ll.notna(), np.nan)
    return br.rolling(YDAYS, min_periods=QDAYS).sum()


def _b222(open, high, low, close):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1))
    gap_down = (open < close.shift(1))
    return (down & gap_down).astype(float).where(d != 0, np.nan)


def _b223(high, low, close, volume):
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1))
    return _rolling_zscore(volume, YDAYS).where(down, np.nan)


def _b224(high, low, close):
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, 10, mode='max')


def _b225(open, high, low, close):
    cnt = _b184(open, high, low, close)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((cnt >= 3) & (pos >= 0.95)).astype(float).where(cnt.notna() & pos.notna(), np.nan)


# ---------------------------- d2 wrappers (second derivative) ----------------------------

def f14_stps_151_supertrend_hlc3_basis_10_3_log_dist_d2(high, low, close):
    return _b151(high, low, close).diff().diff()

def f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist_d2(open, high, low, close):
    return _b152(open, high, low, close).diff().diff()

def f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d_d2(open, high, low, close):
    return _b153(open, high, low, close).diff().diff()

def f14_stps_154_supertrend_HA_close_dist_atr_10_3_d2(open, high, low, close):
    return _b154(open, high, low, close).diff().diff()

def f14_stps_155_weighted_atr_supertrend_recent_heavy_dist_d2(high, low, close):
    return _b155(high, low, close).diff().diff()

def f14_stps_156_supertrend_immediate_reflip_count_63d_d2(high, low, close):
    return _b156(high, low, close).diff().diff()

def f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d_d2(high, low, close):
    return _b157(high, low, close).diff().diff()

def f14_stps_158_supertrend_short_state_after_252d_high_d2(high, low, close):
    return _b158(high, low, close).diff().diff()

def f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d_d2(high, low, close):
    return _b159(high, low, close).diff().diff()

def f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d_d2(high, low, close):
    return _b160(high, low, close).diff().diff()

def f14_stps_161_supertrend_consecutive_short_state_streak_max_252d_d2(high, low, close):
    return _b161(high, low, close).diff().diff()

def f14_stps_162_supertrend_avg_short_state_duration_252d_d2(high, low, close):
    return _b162(high, low, close).diff().diff()

def f14_stps_163_psar_fast_step_0p04_flip_count_63d_d2(high, low):
    return _b163(high, low).diff().diff()

def f14_stps_164_psar_slow_step_0p01_flip_count_252d_d2(high, low):
    return _b164(high, low).diff().diff()

def f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator_d2(high, low):
    return _b165(high, low).diff().diff()

def f14_stps_166_psar_cluster_count_5plus_in_21d_252d_d2(high, low):
    return _b166(high, low).diff().diff()

def f14_stps_167_psar_first_down_flip_after_60d_long_streak_d2(high, low):
    return _b167(high, low).diff().diff()

def f14_stps_168_psar_AF_at_max_then_flip_within_5d_d2(high, low):
    return _b168(high, low).diff().diff()

def f14_stps_169_psar_gap_through_psar_pct_d2(open, high, low, close):
    return _b169(open, high, low, close).diff().diff()

def f14_stps_170_chandelier_long_atr_dist_zscore_504d_d2(high, low, close):
    return _b170(high, low, close).diff().diff()

def f14_stps_171_chandelier_no_mans_land_indicator_d2(high, low, close):
    return _b171(high, low, close).diff().diff()

def f14_stps_172_chandelier_short_breach_count_63d_d2(high, low, close):
    return _b172(high, low, close).diff().diff()

def f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d_d2(high, low, close):
    return _b173(high, low, close).diff().diff()

def f14_stps_174_chandelier_long_param_50_2_atr_dist_d2(high, low, close):
    return _b174(high, low, close).diff().diff()

def f14_stps_175_chandelier_long_param_10_4_atr_dist_d2(high, low, close):
    return _b175(high, low, close).diff().diff()

def f14_stps_176_chandelier_distance_compression_21d_vs_252d_d2(high, low, close):
    return _b176(high, low, close).diff().diff()

def f14_stps_177_kase_devstop_long_atr_skew_distance_d2(high, low, close):
    return _b177(high, low, close).diff().diff()

def f14_stps_178_kase_devstop_breach_count_63d_d2(high, low, close):
    return _b178(high, low, close).diff().diff()

def f14_stps_179_kase_devstop_warning_line_dist_atr_d2(high, low, close):
    return _b179(high, low, close).diff().diff()

def f14_stps_180_volatility_stop_stoller_atkinson_dist_atr_d2(high, low, close):
    return _b180(high, low, close).diff().diff()

def f14_stps_181_volatility_stop_flips_in_63d_d2(high, low, close):
    return _b181(high, low, close).diff().diff()

def f14_stps_182_atr_trail_1x_breach_count_63d_d2(high, low, close):
    return _b182(high, low, close).diff().diff()

def f14_stps_183_atr_trail_5x_breach_count_252d_d2(high, low, close):
    return _b183(high, low, close).diff().diff()

def f14_stps_184_count_trails_in_short_state_d2(open, high, low, close):
    return _b184(open, high, low, close).diff().diff()

def f14_stps_185_count_trails_flipped_short_within_5d_d2(open, high, low, close):
    return _b185(open, high, low, close).diff().diff()

def f14_stps_186_count_trails_flipped_short_within_10d_d2(open, high, low, close):
    return _b186(open, high, low, close).diff().diff()

def f14_stps_187_count_trails_flipped_short_within_21d_d2(open, high, low, close):
    return _b187(open, high, low, close).diff().diff()

def f14_stps_188_bars_since_psar_up_flip_d2(high, low):
    return _b188(high, low).diff().diff()

def f14_stps_189_bars_since_chandelier_long_flip_up_d2(high, low, close):
    return _b189(high, low, close).diff().diff()

def f14_stps_190_bars_since_atr_trail_3x_flip_d2(high, low, close):
    return _b190(high, low, close).diff().diff()

def f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d_d2(high, low, close):
    return _b191(high, low, close).diff().diff()

def f14_stps_192_max_drawdown_from_st_down_flip_bar_21d_d2(high, low, close):
    return _b192(high, low, close).diff().diff()

def f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d_d2(high, low, close):
    return _b193(high, low, close).diff().diff()

def f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d_d2(high, low, close):
    return _b194(high, low, close).diff().diff()

def f14_stps_195_post_flip_volume_surge_ratio_5d_d2(high, low, close, volume):
    return _b195(high, low, close, volume).diff().diff()

def f14_stps_196_whipsaw_freq_st_10_3_in_42d_d2(high, low, close):
    return _b196(high, low, close).diff().diff()

def f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high_d2(high, low, close):
    return _b197(high, low, close).diff().diff()

def f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high_d2(high, low, close):
    return _b198(high, low, close).diff().diff()

def f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio_d2(high, low, close):
    return _b199(high, low, close).diff().diff()

def f14_stps_200_st_stop_distance_expansion_zscore_21d_d2(high, low, close):
    return _b200(high, low, close).diff().diff()

def f14_stps_201_trail_to_price_gap_rolling_std_63d_d2(high, low, close):
    return _b201(high, low, close).diff().diff()

def f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator_d2(high, low, close):
    return _b202(high, low, close).diff().diff()

def f14_stps_203_first_st_down_flip_magnitude_log_drop_5d_d2(high, low, close):
    return _b203(high, low, close).diff().diff()

def f14_stps_204_st_10_3_trail_slope_degrees_21d_d2(high, low, close):
    return _b204(high, low, close).diff().diff()

def f14_stps_205_st_trail_slope_deceleration_21d_vs_63d_d2(high, low, close):
    return _b205(high, low, close).diff().diff()

def f14_stps_206_psar_curve_deceleration_21d_d2(high, low, close):
    return _b206(high, low, close).diff().diff()

def f14_stps_207_chandelier_long_slope_decay_21d_vs_63d_d2(high, low, close):
    return _b207(high, low, close).diff().diff()

def f14_stps_208_multi_period_st_fast_short_slow_long_indicator_d2(high, low, close):
    return _b208(high, low, close).diff().diff()

def f14_stps_209_multi_period_st_fast_long_slow_short_indicator_d2(high, low, close):
    return _b209(high, low, close).diff().diff()

def f14_stps_210_HA_psar_flip_count_63d_d2(open, high, low, close):
    return _b210(open, high, low, close).diff().diff()

def f14_stps_211_HA_psar_atr_dist_d2(open, high, low, close):
    return _b211(open, high, low, close).diff().diff()

def f14_stps_212_time_decay_weighted_atr_st_dist_d2(high, low, close):
    return _b212(high, low, close).diff().diff()

def f14_stps_213_zlema_trail_dist_atr_d2(high, low, close):
    return _b213(high, low, close).diff().diff()

def f14_stps_214_mcginley_dynamic_trail_dist_atr_d2(high, low, close):
    return _b214(high, low, close).diff().diff()

def f14_stps_215_t3_tillson_trail_dist_atr_d2(high, low, close):
    return _b215(high, low, close).diff().diff()

def f14_stps_216_hilo_activator_5_flip_count_63d_d2(high, low):
    return _b216(high, low).diff().diff()

def f14_stps_217_hilo_activator_atr_dist_period_3_d2(high, low, close):
    return _b217(high, low, close).diff().diff()

def f14_stps_218_chande_kroll_stop_flip_count_63d_d2(high, low, close):
    return _b218(high, low, close).diff().diff()

def f14_stps_219_chande_kroll_breach_then_recover_count_252d_d2(high, low, close):
    return _b219(high, low, close).diff().diff()

def f14_stps_220_donchian_trail_20_long_flip_count_63d_d2(high, low, close):
    return _b220(high, low, close).diff().diff()

def f14_stps_221_donchian_trail_10_exit_breach_count_252d_d2(high, low, close):
    return _b221(high, low, close).diff().diff()

def f14_stps_222_st_10_3_flip_with_gap_down_indicator_d2(open, high, low, close):
    return _b222(open, high, low, close).diff().diff()

def f14_stps_223_volume_at_st_down_flip_zscore_252d_d2(high, low, close, volume):
    return _b223(high, low, close, volume).diff().diff()

def f14_stps_224_post_psar_flip_max_recovery_pct_10d_d2(high, low, close):
    return _b224(high, low, close).diff().diff()

def f14_stps_225_count_trails_breached_at_peak_top5pct_indicator_d2(open, high, low, close):
    return _b225(open, high, low, close).diff().diff()


SUPERTREND_PSAR_CHANDELIER_D2_REGISTRY_151_225 = {
    "f14_stps_151_supertrend_hlc3_basis_10_3_log_dist_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_151_supertrend_hlc3_basis_10_3_log_dist_d2},
    "f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist_d2},
    "f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d_d2},
    "f14_stps_154_supertrend_HA_close_dist_atr_10_3_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_154_supertrend_HA_close_dist_atr_10_3_d2},
    "f14_stps_155_weighted_atr_supertrend_recent_heavy_dist_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_155_weighted_atr_supertrend_recent_heavy_dist_d2},
    "f14_stps_156_supertrend_immediate_reflip_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_156_supertrend_immediate_reflip_count_63d_d2},
    "f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d_d2},
    "f14_stps_158_supertrend_short_state_after_252d_high_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_158_supertrend_short_state_after_252d_high_d2},
    "f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d_d2},
    "f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d_d2},
    "f14_stps_161_supertrend_consecutive_short_state_streak_max_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_161_supertrend_consecutive_short_state_streak_max_252d_d2},
    "f14_stps_162_supertrend_avg_short_state_duration_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_162_supertrend_avg_short_state_duration_252d_d2},
    "f14_stps_163_psar_fast_step_0p04_flip_count_63d_d2": {"inputs": ["high", "low"], "func": f14_stps_163_psar_fast_step_0p04_flip_count_63d_d2},
    "f14_stps_164_psar_slow_step_0p01_flip_count_252d_d2": {"inputs": ["high", "low"], "func": f14_stps_164_psar_slow_step_0p01_flip_count_252d_d2},
    "f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator_d2": {"inputs": ["high", "low"], "func": f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator_d2},
    "f14_stps_166_psar_cluster_count_5plus_in_21d_252d_d2": {"inputs": ["high", "low"], "func": f14_stps_166_psar_cluster_count_5plus_in_21d_252d_d2},
    "f14_stps_167_psar_first_down_flip_after_60d_long_streak_d2": {"inputs": ["high", "low"], "func": f14_stps_167_psar_first_down_flip_after_60d_long_streak_d2},
    "f14_stps_168_psar_AF_at_max_then_flip_within_5d_d2": {"inputs": ["high", "low"], "func": f14_stps_168_psar_AF_at_max_then_flip_within_5d_d2},
    "f14_stps_169_psar_gap_through_psar_pct_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_169_psar_gap_through_psar_pct_d2},
    "f14_stps_170_chandelier_long_atr_dist_zscore_504d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_170_chandelier_long_atr_dist_zscore_504d_d2},
    "f14_stps_171_chandelier_no_mans_land_indicator_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_171_chandelier_no_mans_land_indicator_d2},
    "f14_stps_172_chandelier_short_breach_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_172_chandelier_short_breach_count_63d_d2},
    "f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d_d2},
    "f14_stps_174_chandelier_long_param_50_2_atr_dist_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_174_chandelier_long_param_50_2_atr_dist_d2},
    "f14_stps_175_chandelier_long_param_10_4_atr_dist_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_175_chandelier_long_param_10_4_atr_dist_d2},
    "f14_stps_176_chandelier_distance_compression_21d_vs_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_176_chandelier_distance_compression_21d_vs_252d_d2},
    "f14_stps_177_kase_devstop_long_atr_skew_distance_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_177_kase_devstop_long_atr_skew_distance_d2},
    "f14_stps_178_kase_devstop_breach_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_178_kase_devstop_breach_count_63d_d2},
    "f14_stps_179_kase_devstop_warning_line_dist_atr_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_179_kase_devstop_warning_line_dist_atr_d2},
    "f14_stps_180_volatility_stop_stoller_atkinson_dist_atr_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_180_volatility_stop_stoller_atkinson_dist_atr_d2},
    "f14_stps_181_volatility_stop_flips_in_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_181_volatility_stop_flips_in_63d_d2},
    "f14_stps_182_atr_trail_1x_breach_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_182_atr_trail_1x_breach_count_63d_d2},
    "f14_stps_183_atr_trail_5x_breach_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_183_atr_trail_5x_breach_count_252d_d2},
    "f14_stps_184_count_trails_in_short_state_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_184_count_trails_in_short_state_d2},
    "f14_stps_185_count_trails_flipped_short_within_5d_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_185_count_trails_flipped_short_within_5d_d2},
    "f14_stps_186_count_trails_flipped_short_within_10d_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_186_count_trails_flipped_short_within_10d_d2},
    "f14_stps_187_count_trails_flipped_short_within_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_187_count_trails_flipped_short_within_21d_d2},
    "f14_stps_188_bars_since_psar_up_flip_d2": {"inputs": ["high", "low"], "func": f14_stps_188_bars_since_psar_up_flip_d2},
    "f14_stps_189_bars_since_chandelier_long_flip_up_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_189_bars_since_chandelier_long_flip_up_d2},
    "f14_stps_190_bars_since_atr_trail_3x_flip_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_190_bars_since_atr_trail_3x_flip_d2},
    "f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d_d2},
    "f14_stps_192_max_drawdown_from_st_down_flip_bar_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_192_max_drawdown_from_st_down_flip_bar_21d_d2},
    "f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d_d2},
    "f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d_d2},
    "f14_stps_195_post_flip_volume_surge_ratio_5d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f14_stps_195_post_flip_volume_surge_ratio_5d_d2},
    "f14_stps_196_whipsaw_freq_st_10_3_in_42d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_196_whipsaw_freq_st_10_3_in_42d_d2},
    "f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high_d2},
    "f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high_d2},
    "f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio_d2},
    "f14_stps_200_st_stop_distance_expansion_zscore_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_200_st_stop_distance_expansion_zscore_21d_d2},
    "f14_stps_201_trail_to_price_gap_rolling_std_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_201_trail_to_price_gap_rolling_std_63d_d2},
    "f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator_d2},
    "f14_stps_203_first_st_down_flip_magnitude_log_drop_5d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_203_first_st_down_flip_magnitude_log_drop_5d_d2},
    "f14_stps_204_st_10_3_trail_slope_degrees_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_204_st_10_3_trail_slope_degrees_21d_d2},
    "f14_stps_205_st_trail_slope_deceleration_21d_vs_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_205_st_trail_slope_deceleration_21d_vs_63d_d2},
    "f14_stps_206_psar_curve_deceleration_21d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_206_psar_curve_deceleration_21d_d2},
    "f14_stps_207_chandelier_long_slope_decay_21d_vs_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_207_chandelier_long_slope_decay_21d_vs_63d_d2},
    "f14_stps_208_multi_period_st_fast_short_slow_long_indicator_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_208_multi_period_st_fast_short_slow_long_indicator_d2},
    "f14_stps_209_multi_period_st_fast_long_slow_short_indicator_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_209_multi_period_st_fast_long_slow_short_indicator_d2},
    "f14_stps_210_HA_psar_flip_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_210_HA_psar_flip_count_63d_d2},
    "f14_stps_211_HA_psar_atr_dist_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_211_HA_psar_atr_dist_d2},
    "f14_stps_212_time_decay_weighted_atr_st_dist_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_212_time_decay_weighted_atr_st_dist_d2},
    "f14_stps_213_zlema_trail_dist_atr_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_213_zlema_trail_dist_atr_d2},
    "f14_stps_214_mcginley_dynamic_trail_dist_atr_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_214_mcginley_dynamic_trail_dist_atr_d2},
    "f14_stps_215_t3_tillson_trail_dist_atr_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_215_t3_tillson_trail_dist_atr_d2},
    "f14_stps_216_hilo_activator_5_flip_count_63d_d2": {"inputs": ["high", "low"], "func": f14_stps_216_hilo_activator_5_flip_count_63d_d2},
    "f14_stps_217_hilo_activator_atr_dist_period_3_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_217_hilo_activator_atr_dist_period_3_d2},
    "f14_stps_218_chande_kroll_stop_flip_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_218_chande_kroll_stop_flip_count_63d_d2},
    "f14_stps_219_chande_kroll_breach_then_recover_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_219_chande_kroll_breach_then_recover_count_252d_d2},
    "f14_stps_220_donchian_trail_20_long_flip_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_220_donchian_trail_20_long_flip_count_63d_d2},
    "f14_stps_221_donchian_trail_10_exit_breach_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_221_donchian_trail_10_exit_breach_count_252d_d2},
    "f14_stps_222_st_10_3_flip_with_gap_down_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_222_st_10_3_flip_with_gap_down_indicator_d2},
    "f14_stps_223_volume_at_st_down_flip_zscore_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f14_stps_223_volume_at_st_down_flip_zscore_252d_d2},
    "f14_stps_224_post_psar_flip_max_recovery_pct_10d_d2": {"inputs": ["high", "low", "close"], "func": f14_stps_224_post_psar_flip_max_recovery_pct_10d_d2},
    "f14_stps_225_count_trails_breached_at_peak_top5pct_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_225_count_trails_breached_at_peak_top5pct_indicator_d2},
}
