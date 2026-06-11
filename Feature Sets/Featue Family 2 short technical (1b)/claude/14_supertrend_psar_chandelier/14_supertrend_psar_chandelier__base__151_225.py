"""supertrend_psar_chandelier base features 151-225 — Pipeline 1b-technical.

Extension batch (75 features) adding new trailing-stop hypotheses to family 14:
- Alt-basis SuperTrend (HLC3, OHLC4, Heikin-Ashi)
- Weighted-ATR and alt-AF PSAR variants
- Whipsaw / reflip / cluster signatures
- Multi-trail consensus (ST, PSAR, Chandelier, ATR-trail, HMA-trail)
- Post-flip recovery / drawdown / volume confirmation
- Alt trailing-stops: ZLEMA, McGinley, T3 Tillson, HiLo Activator, Chande-Kroll,
  Donchian, Kase DevStop, Volatility Stop (Stoller-Atkinson)

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers.
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


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


# --- iterative trailing-stop machines ---

def _supertrend(high, low, close, n=10, mult=3.0, basis='hl2'):
    """SuperTrend with selectable basis. basis in {'hl2','hlc3'}."""
    atr = _atr(high, low, close, n=n)
    if basis == 'hlc3':
        mid = (high + low + close) / 3.0
    else:
        mid = (high + low) / 2.0
    upper = mid + mult * atr
    lower = mid - mult * atr
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
    """Non-recursive HA proxy."""
    ha_close = (open_ + high + low + close) / 4.0
    ha_open = (open_.shift(1) + close.shift(1)) / 2.0
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return ha_open, ha_high, ha_low, ha_close


def _supertrend_ha(open_, high, low, close, n=10, mult=3.0):
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open_, high, low, close)
    return _supertrend(ha_h, ha_l, ha_c, n=n, mult=mult, basis='hl2')


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
    nb = len(c)
    stop = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
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
    """Kase DevStop (skew-adjusted)."""
    tr = _true_range(high, low, close)
    mp = max(n // 3, 2)
    mu = tr.rolling(n, min_periods=mp).mean()
    sd = tr.rolling(n, min_periods=mp).std()
    sk = tr.rolling(n, min_periods=mp).skew().fillna(0)
    adj = mu + sk.clip(-3, 3) * sd
    hc = close.rolling(n, min_periods=mp).max()
    return hc - mult * adj, adj


def _vol_stop_stoller(close, atr, mult=2.0):
    return _atr_trail(close, atr, mult=mult)


def _zlema(close, n):
    lag = max(n // 2, 1)
    src = close + (close - close.shift(lag))
    return src.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()


def _mcginley(close, n=14):
    arr = close.values; nb = len(arr)
    out = np.full(nb, np.nan)
    started = False
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
        ratio = arr[i] / prev
        denom = n * (ratio ** 4)
        if denom == 0:
            out[i] = arr[i]
        else:
            out[i] = prev + (arr[i] - prev) / denom
    return pd.Series(out, index=close.index)


def _t3_tillson(close, n=8, vol=0.7):
    e1 = close.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e2 = e1.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e3 = e2.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e4 = e3.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e5 = e4.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    e6 = e5.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()
    b = vol
    c1 = -b * b * b
    c2 = 3 * b * b + 3 * b * b * b
    c3 = -6 * b * b - 3 * b - 3 * b * b * b
    c4 = 1 + 3 * b + b * b * b + 3 * b * b
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _hilo_activator(high, low, n=3):
    mp = max(n // 3, 2)
    mh = high.rolling(n, min_periods=mp).mean()
    ml = low.rolling(n, min_periods=mp).mean()
    c = ((high + low) / 2.0).values
    mhv = mh.values; mlv = ml.values
    nb = len(c)
    stop = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
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
        L = len(x)
        w = np.arange(1, L + 1, dtype=float)
        return float(np.dot(x, w) / w.sum())
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hma(close, n):
    half = max(int(n // 2), 2)
    rt = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(close, half) - _wma(close, n), rt)


# ============================================================
# Bucket A — Alt-basis SuperTrend (151-155)
# ============================================================

def f14_stps_151_supertrend_hlc3_basis_10_3_log_dist(high, low, close):
    """Log distance close above SuperTrend(10,3) on HLC3 basis."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0, basis='hlc3')
    return _safe_log(close) - _safe_log(st)


def f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist(open, high, low, close):
    """Log distance close above SuperTrend(10,3) on OHLC4 basis."""
    st, _ = _supertrend_ohlc4(open, high, low, close, n=10, mult=3.0)
    return _safe_log(close) - _safe_log(st)


def f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d(open, high, low, close):
    """Flips of SuperTrend(10,3) computed on Heikin-Ashi candles over 63d."""
    _, d = _supertrend_ha(open, high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_154_supertrend_HA_close_dist_atr_10_3(open, high, low, close):
    """(ha_close - ST_HA(10,3)) / ATR(21) — HA ST extension."""
    ha_o, ha_h, ha_l, ha_c = _heikin_ashi(open, high, low, close)
    st, _ = _supertrend(ha_h, ha_l, ha_c, n=10, mult=3.0, basis='hl2')
    return _safe_div(ha_c - st, _atr(high, low, close, n=MDAYS))


def f14_stps_155_weighted_atr_supertrend_recent_heavy_dist(high, low, close):
    """SuperTrend(10,3) with linearly-weighted ATR (recent-heavy). Log dist close above stop."""
    watr = _wtr_atr(high, low, close, n=10)
    hl2 = (high + low) / 2.0
    upper = hl2 + 3.0 * watr; lower = hl2 - 3.0 * watr
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
    st_s = pd.Series(st, index=close.index)
    return _safe_log(close) - _safe_log(st_s)


# ============================================================
# Bucket B — Whipsaw / reflip signatures (156-162)
# ============================================================

def f14_stps_156_supertrend_immediate_reflip_count_63d(high, low, close):
    """Count of ST(10,3) flip-then-reflip within 3 bars in trailing 63d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool).values
    n = len(flip)
    refl = np.zeros(n, dtype=float)
    for i in range(1, n):
        if flip[i]:
            for k in range(1, min(4, i + 1)):
                if flip[i - k]:
                    refl[i] = 1.0
                    break
    refl_s = pd.Series(refl, index=close.index)
    return refl_s.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d(high, low, close):
    """Ratio reflips/flips of ST(10,3) over 252d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool).values
    n = len(flip)
    refl = np.zeros(n, dtype=float); fl = np.zeros(n, dtype=float)
    for i in range(n):
        if flip[i]:
            fl[i] = 1.0
            for k in range(1, min(4, i + 1)):
                if flip[i - k]:
                    refl[i] = 1.0
                    break
    refl_s = pd.Series(refl, index=close.index); fl_s = pd.Series(fl, index=close.index)
    rs = refl_s.rolling(YDAYS, min_periods=QDAYS).sum()
    fs = fl_s.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rs, fs)


def f14_stps_158_supertrend_short_state_after_252d_high(high, low, close):
    """Indicator: ST(10,3) is short AND 252d-high was set within last 21 bars."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high >= rmax).astype(float)
    recent_high = new_high.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    short_state = (d == -1)
    return (short_state & recent_high).astype(float).where(d != 0, np.nan)


def f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d(high, low, close):
    """Flip count of SuperTrend(10,4) over 63d — wider multiplier."""
    _, d = _supertrend(high, low, close, n=10, mult=4.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d(high, low, close):
    """Flip count of SuperTrend(10,1.5) over 63d — tighter multiplier."""
    _, d = _supertrend(high, low, close, n=10, mult=1.5)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_161_supertrend_consecutive_short_state_streak_max_252d(high, low, close):
    """Longest consecutive-short-state run of ST(10,3) in trailing 252d."""
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


def f14_stps_162_supertrend_avg_short_state_duration_252d(high, low, close):
    """Average length of completed short-state runs of ST(10,3) in trailing 252d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    sm = (d == -1).astype(int).values
    n = len(sm)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
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


# ============================================================
# Bucket C — PSAR variants (163-169)
# ============================================================

def f14_stps_163_psar_fast_step_0p04_flip_count_63d(high, low):
    """Flip count of fast PSAR (AF step 0.04, max 0.40) over 63d."""
    _, d = _psar(high, low, af0=0.04, afmax=0.40)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_164_psar_slow_step_0p01_flip_count_252d(high, low):
    """Flip count of slow PSAR (AF step 0.01, max 0.10) over 252d."""
    _, d = _psar(high, low, af0=0.01, afmax=0.10)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator(high, low):
    """Indicator: 3+ PSAR reversals within trailing 10d window."""
    _, d = _psar(high, low)
    flip = (d.diff().abs() > 0).astype(float)
    return (flip.rolling(10, min_periods=3).sum() >= 3).astype(float).where(flip.notna(), np.nan)


def f14_stps_166_psar_cluster_count_5plus_in_21d_252d(high, low):
    """Count of 21d windows in trailing 252d with 5+ PSAR reversals."""
    _, d = _psar(high, low)
    flip = (d.diff().abs() > 0).astype(float)
    cl = (flip.rolling(MDAYS, min_periods=WDAYS).sum() >= 5).astype(float)
    return cl.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_167_psar_first_down_flip_after_60d_long_streak(high, low):
    """Indicator: PSAR down-flip AND prior PSAR-long streak >= 60 bars."""
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    long_arr = (d == 1).astype(int).values
    n = len(d)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        if long_arr[i] == 1:
            run += 1
        else:
            if down[i] and run >= 60:
                out[i] = 1.0
            run = 0
    res = pd.Series(out, index=high.index)
    return res.where(d != 0, np.nan)


def f14_stps_168_psar_AF_at_max_then_flip_within_5d(high, low):
    """Indicator: AF reached max within prior 5d AND a PSAR flip occurred within prior 5d."""
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
    af_series = pd.Series(af_arr, index=high.index)
    dirn_s = pd.Series(dirn, index=high.index)
    at_max = (af_series >= 0.199)
    flip = (dirn_s.diff().abs() > 0)
    am5 = at_max.rolling(WDAYS, min_periods=1).max() > 0
    fl5 = flip.rolling(WDAYS, min_periods=1).max() > 0
    return (am5 & fl5).astype(float).where(dirn_s != 0, np.nan)


def f14_stps_169_psar_gap_through_psar_pct(open, high, low, close):
    """Percent gap through PSAR: (psar - open)/close when open < psar (long state)."""
    sar, d = _psar(high, low)
    long_state = (d.shift(1) == 1)
    gap = _safe_div(sar - open, close)
    return gap.where(long_state & (open < sar), 0.0).where(d.notna() & open.notna(), np.nan)


# ============================================================
# Bucket D — Chandelier variants & breaches (170-176)
# ============================================================

def f14_stps_170_chandelier_long_atr_dist_zscore_504d(high, low, close):
    """504d z-score of ATR-normalized (close - chandelier_long(22,3))."""
    ch = _chandelier_long(high, low, close, n=22, mult=3.0)
    raw = _safe_div(close - ch, _atr(high, low, close, n=MDAYS))
    return _rolling_zscore(raw, DDAYS_2Y, min_periods=YDAYS)


def f14_stps_171_chandelier_no_mans_land_indicator(high, low, close):
    """Indicator: close between chandelier_long and chandelier_short."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    return ((close > cl) & (close < cs)).astype(float).where(cl.notna() & cs.notna(), np.nan)


def f14_stps_172_chandelier_short_breach_count_63d(high, low, close):
    """Count of bars in trailing 63d where close > chandelier_short(22,3)."""
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    br = (close > cs).astype(float).where(cs.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d(high, low, close):
    """252d count of chandelier_long breaches followed by lower low within 5 bars."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    br = (close < cl) & cl.notna()
    br5 = br.shift(5).fillna(False).astype(bool)
    breach_low = low.shift(5)
    confirmed = br5 & (low < breach_low)
    return confirmed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_174_chandelier_long_param_50_2_atr_dist(high, low, close):
    """(close - chandelier_long(50,2)) / ATR(21) — wider window, tighter mult."""
    cl = _chandelier_long(high, low, close, n=50, mult=2.0)
    return _safe_div(close - cl, _atr(high, low, close, n=MDAYS))


def f14_stps_175_chandelier_long_param_10_4_atr_dist(high, low, close):
    """(close - chandelier_long(10,4)) / ATR(21) — shorter window, fatter mult."""
    cl = _chandelier_long(high, low, close, n=10, mult=4.0)
    return _safe_div(close - cl, _atr(high, low, close, n=MDAYS))


def f14_stps_176_chandelier_distance_compression_21d_vs_252d(high, low, close):
    """Ratio of 21d std to 252d std of (close - chandelier_long(22,3))."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    gap = close - cl
    s21 = gap.rolling(MDAYS, min_periods=WDAYS).std()
    s252 = gap.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s21, s252)


# ============================================================
# Bucket E — Kase DevStop & Volatility Stop (177-183)
# ============================================================

def f14_stps_177_kase_devstop_long_atr_skew_distance(high, low, close):
    """(close - kase_devstop_long(10,3)) / ATR(21) — Kase skew-adjusted long stop dist."""
    ks, _ = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    return _safe_div(close - ks, _atr(high, low, close, n=MDAYS))


def f14_stps_178_kase_devstop_breach_count_63d(high, low, close):
    """Count of bars in trailing 63d where close < kase_devstop_long."""
    ks, _ = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    br = (close < ks).astype(float).where(ks.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_179_kase_devstop_warning_line_dist_atr(high, low, close):
    """(close - kase_warning_line) / ATR(21), warning = kase_long + 1*adj."""
    ks, adj = _kase_devstop_long(high, low, close, n=10, mult=3.0)
    warning = ks + 1.0 * adj
    return _safe_div(close - warning, _atr(high, low, close, n=MDAYS))


def f14_stps_180_volatility_stop_stoller_atkinson_dist_atr(high, low, close):
    """(close - stoller_vol_stop(15,2)) / ATR(21) — STARC-style vol stop distance."""
    atr15 = _atr(high, low, close, n=15)
    vs, _ = _vol_stop_stoller(close, atr15, mult=2.0)
    return _safe_div(close - vs, _atr(high, low, close, n=MDAYS))


def f14_stps_181_volatility_stop_flips_in_63d(high, low, close):
    """Flip count of Stoller volatility stop in trailing 63d."""
    atr15 = _atr(high, low, close, n=15)
    _, d = _vol_stop_stoller(close, atr15, mult=2.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_182_atr_trail_1x_breach_count_63d(high, low, close):
    """Count of breaches of ATR(21)-trail with mult=1 in trailing 63d."""
    atr = _atr(high, low, close, n=MDAYS)
    stop, d = _atr_trail(close, atr, mult=1.0)
    flip = ((d == -1) & (d.shift(1) == 1)).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_183_atr_trail_5x_breach_count_252d(high, low, close):
    """Count of breaches of ATR(21)-trail with mult=5 in trailing 252d."""
    atr = _atr(high, low, close, n=MDAYS)
    stop, d = _atr_trail(close, atr, mult=5.0)
    flip = ((d == -1) & (d.shift(1) == 1)).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — Multi-trail consensus (184-187)
# ============================================================

def _multi_trail_short_mask(open, high, low, close):
    """Boolean (0/1) short-state for {ST10/3, PSAR, Chand-long, ATR-trail3x, HMA20-trail}."""
    _, d_st = _supertrend(high, low, close, n=10, mult=3.0)
    _, d_psar = _psar(high, low)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    d_cl = (close < cl).astype(int).where(cl.notna(), 0).fillna(0).astype(int)
    atr = _atr(high, low, close, n=MDAYS)
    _, d_at = _atr_trail(close, atr, mult=3.0)
    hma = _hma(close, 20)
    d_hma = (close < hma).astype(int).where(hma.notna(), 0).fillna(0).astype(int)
    s_st = (d_st == -1).astype(int)
    s_psar = (d_psar == -1).astype(int)
    s_at = (d_at == -1).astype(int)
    return s_st, s_psar, d_cl, s_at, d_hma


def f14_stps_184_count_trails_in_short_state(open, high, low, close):
    """Count of {ST, PSAR, Chandelier-long, ATR-trail, HMA-trail} in short state."""
    s_st, s_psar, s_cl, s_at, s_hma = _multi_trail_short_mask(open, high, low, close)
    return (s_st + s_psar + s_cl + s_at + s_hma).astype(float)


def f14_stps_185_count_trails_flipped_short_within_5d(open, high, low, close):
    """Count of trails that flipped to short within trailing 5d (cascade)."""
    s_st, s_psar, s_cl, s_at, s_hma = _multi_trail_short_mask(open, high, low, close)
    def _fl(s):
        flip = ((s == 1) & (s.shift(1) == 0)).astype(float)
        return flip.rolling(WDAYS, min_periods=1).max()
    return (_fl(s_st) + _fl(s_psar) + _fl(s_cl) + _fl(s_at) + _fl(s_hma)).astype(float)


def f14_stps_186_count_trails_flipped_short_within_10d(open, high, low, close):
    """Count of trails that flipped to short within trailing 10d."""
    s_st, s_psar, s_cl, s_at, s_hma = _multi_trail_short_mask(open, high, low, close)
    def _fl(s):
        flip = ((s == 1) & (s.shift(1) == 0)).astype(float)
        return flip.rolling(10, min_periods=1).max()
    return (_fl(s_st) + _fl(s_psar) + _fl(s_cl) + _fl(s_at) + _fl(s_hma)).astype(float)


def f14_stps_187_count_trails_flipped_short_within_21d(open, high, low, close):
    """Count of trails that flipped to short within trailing 21d."""
    s_st, s_psar, s_cl, s_at, s_hma = _multi_trail_short_mask(open, high, low, close)
    def _fl(s):
        flip = ((s == 1) & (s.shift(1) == 0)).astype(float)
        return flip.rolling(MDAYS, min_periods=1).max()
    return (_fl(s_st) + _fl(s_psar) + _fl(s_cl) + _fl(s_at) + _fl(s_hma)).astype(float)


# ============================================================
# Bucket G — Bars-since-up-flip per system (188-190)
# ============================================================

def f14_stps_188_bars_since_psar_up_flip(high, low):
    """Bars since most recent PSAR up-flip (short→long)."""
    _, d = _psar(high, low)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    return _bars_since_true(up)


def f14_stps_189_bars_since_chandelier_long_flip_up(high, low, close):
    """Bars since transition from close<chandelier_long to close>=chandelier_long."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    long_state = (close >= cl) & cl.notna()
    up = (long_state & ~long_state.shift(1).fillna(False)).astype(bool)
    return _bars_since_true(up)


def f14_stps_190_bars_since_atr_trail_3x_flip(high, low, close):
    """Bars since most recent ATR-trail(mult=3) any flip."""
    atr = _atr(high, low, close, n=MDAYS)
    _, d = _atr_trail(close, atr, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool)
    return _bars_since_true(flip)


# ============================================================
# Bucket H — Post-flip recovery / drawdown / volume (191-195)
# ============================================================

def _post_flip_extreme(close, flip_mask, window, mode='min'):
    """For each bar within `window` bars of most-recent flip, compute pct extreme of close
    relative to flip-bar close. PIT-safe: only uses bars up to and including current i."""
    arr = close.values; flip = flip_mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last_flip_idx = -1
    last_flip_close = np.nan
    for i in range(n):
        if flip[i]:
            last_flip_idx = i
            last_flip_close = arr[i]
        if last_flip_idx >= 0 and (i - last_flip_idx) <= window:
            lo = last_flip_idx; hi = i + 1
            if hi > lo:
                seg = arr[lo:hi]
                v = np.nanmin(seg) if mode == 'min' else np.nanmax(seg)
                if not np.isnan(v) and not np.isnan(last_flip_close) and last_flip_close > 0:
                    out[i] = (v - last_flip_close) / last_flip_close
    return pd.Series(out, index=close.index)


def f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d(high, low, close):
    """After ST(10,3) down-flip: max recovery (max return) of close within 21d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='max')


def f14_stps_192_max_drawdown_from_st_down_flip_bar_21d(high, low, close):
    """After ST(10,3) down-flip: min return of close within 21d (post-flip acceleration)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='min')


def f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d(high, low, close):
    """After PSAR down-flip: min return of close within 21d."""
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, MDAYS, mode='min')


def f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d(high, low, close):
    """After chandelier_long breach: min return of close within 21d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    br = ((close < cl) & ~(close.shift(1) < cl.shift(1))).fillna(False).astype(bool)
    return _post_flip_extreme(close, br, MDAYS, mode='min')


def f14_stps_195_post_flip_volume_surge_ratio_5d(high, low, close, volume):
    """Mean volume since most recent ST(10,3) down-flip (within 5d) / prior 63d mean."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    v = volume.values
    n = len(v)
    out = np.full(n, np.nan)
    prior_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean().shift(1).values
    last_flip = -1
    for i in range(n):
        if down[i]:
            last_flip = i
        if last_flip >= 0 and (i - last_flip) < WDAYS:
            seg = v[last_flip:i + 1]
            seg = seg[~np.isnan(seg)]
            if seg.size > 0 and not np.isnan(prior_mean[last_flip]) and prior_mean[last_flip] > 0:
                out[i] = float(seg.mean()) / float(prior_mean[last_flip])
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket I — Whipsaw conditional on peak proximity (196-198)
# ============================================================

def f14_stps_196_whipsaw_freq_st_10_3_in_42d(high, low, close):
    """Count of ST(10,3) flips in trailing 42d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(42, min_periods=10).sum()


def f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high(high, low, close):
    """ST(10,3) flip count in trailing 21d, conditional on close in top 10% of 252d range."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    fl21 = flip.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return fl21.where(pos >= 0.9, np.nan)


def f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high(high, low, close):
    """ST(10,3) flip count in trailing 21d, conditional on close in top 5% of 252d range."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    fl21 = flip.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return fl21.where(pos >= 0.95, np.nan)


# ============================================================
# Bucket J — Stop-distance compression / expansion / slope (199-207)
# ============================================================

def f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio(high, low, close):
    """Ratio of 21d std to 252d std of (close - ST(10,3))."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    gap = close - st
    s21 = gap.rolling(MDAYS, min_periods=WDAYS).std()
    s252 = gap.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s21, s252)


def f14_stps_200_st_stop_distance_expansion_zscore_21d(high, low, close):
    """Z-score over 252d of 21d mean of (close - ST(10,3))."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    gap = (close - st).rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(gap, YDAYS)


def f14_stps_201_trail_to_price_gap_rolling_std_63d(high, low, close):
    """63d rolling std of (close - ST(10,3))/close."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    g = _safe_div(close - st, close)
    return g.rolling(QDAYS, min_periods=MDAYS).std()


def f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator(high, low, close):
    """Indicator: ST(10,3) down-flip after >= 252 consecutive long-state bars."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    long_arr = (d == 1).astype(int).values
    n = len(d)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        if long_arr[i] == 1:
            run += 1
        else:
            if down[i] and run >= YDAYS:
                out[i] = 1.0
            run = 0
    return pd.Series(out, index=close.index).where(d != 0, np.nan)


def f14_stps_203_first_st_down_flip_magnitude_log_drop_5d(high, low, close):
    """Log drop of close over 5d following most recent ST(10,3) down-flip."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool).values
    c = close.values
    n = len(c)
    out = np.full(n, np.nan)
    last = -1; cval = np.nan
    for i in range(n):
        if down[i]:
            last = i; cval = c[i]
        if last >= 0 and (i - last) <= WDAYS and not np.isnan(cval) and cval > 0 and not np.isnan(c[i]) and c[i] > 0:
            out[i] = np.log(c[i]) - np.log(cval)
    return pd.Series(out, index=close.index)


def f14_stps_204_st_10_3_trail_slope_degrees_21d(high, low, close):
    """21d slope (degrees) of ST(10,3)/close."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    norm = _safe_div(st, close)
    sl = _rolling_slope(norm, MDAYS)
    return np.degrees(np.arctan(sl))


def f14_stps_205_st_trail_slope_deceleration_21d_vs_63d(high, low, close):
    """21d slope minus 63d slope of ST(10,3)/close."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    norm = _safe_div(st, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


def f14_stps_206_psar_curve_deceleration_21d(high, low, close):
    """21d slope minus 63d slope of PSAR/close."""
    sar, _ = _psar(high, low)
    norm = _safe_div(sar, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


def f14_stps_207_chandelier_long_slope_decay_21d_vs_63d(high, low, close):
    """21d slope minus 63d slope of chandelier_long/close."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    norm = _safe_div(cl, close)
    return _rolling_slope(norm, MDAYS) - _rolling_slope(norm, QDAYS)


# ============================================================
# Bucket K — Multi-period divergence & HA-PSAR & decay-weighted ATR (208-212)
# ============================================================

def f14_stps_208_multi_period_st_fast_short_slow_long_indicator(high, low, close):
    """Indicator: fast ST(7,2) short AND slow ST(50,3) long."""
    _, df = _supertrend(high, low, close, n=7, mult=2.0)
    _, ds = _supertrend(high, low, close, n=50, mult=3.0)
    return ((df == -1) & (ds == 1)).astype(float).where((df != 0) & (ds != 0), np.nan)


def f14_stps_209_multi_period_st_fast_long_slow_short_indicator(high, low, close):
    """Indicator: fast ST(7,2) long AND slow ST(50,3) short."""
    _, df = _supertrend(high, low, close, n=7, mult=2.0)
    _, ds = _supertrend(high, low, close, n=50, mult=3.0)
    return ((df == 1) & (ds == -1)).astype(float).where((df != 0) & (ds != 0), np.nan)


def f14_stps_210_HA_psar_flip_count_63d(open, high, low, close):
    """PSAR flip count over 63d on Heikin-Ashi OHLC."""
    _, ha_h, ha_l, _ = _heikin_ashi(open, high, low, close)
    _, d = _psar(ha_h, ha_l)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_211_HA_psar_atr_dist(open, high, low, close):
    """(ha_close - PSAR_HA) / ATR(21)."""
    _, ha_h, ha_l, ha_c = _heikin_ashi(open, high, low, close)
    sar, _ = _psar(ha_h, ha_l)
    return _safe_div(ha_c - sar, _atr(high, low, close, n=MDAYS))


def f14_stps_212_time_decay_weighted_atr_st_dist(high, low, close):
    """Log dist close above ST(10,3) using EWMA ATR (RiskMetrics lambda=0.94)."""
    eatr = _ewma_atr(high, low, close, n=10, lam=0.94)
    hl2 = (high + low) / 2.0
    upper = hl2 + 3.0 * eatr; lower = hl2 - 3.0 * eatr
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
    st_s = pd.Series(st, index=close.index)
    return _safe_log(close) - _safe_log(st_s)


# ============================================================
# Bucket L — Alt smoothed trailing-stops (213-217)
# ============================================================

def f14_stps_213_zlema_trail_dist_atr(high, low, close):
    """(close - ZLEMA(close,20)) / ATR(21) — zero-lag EMA trail dist."""
    z = _zlema(close, 20)
    return _safe_div(close - z, _atr(high, low, close, n=MDAYS))


def f14_stps_214_mcginley_dynamic_trail_dist_atr(high, low, close):
    """(close - McGinley(close,14)) / ATR(21)."""
    m = _mcginley(close, n=14)
    return _safe_div(close - m, _atr(high, low, close, n=MDAYS))


def f14_stps_215_t3_tillson_trail_dist_atr(high, low, close):
    """(close - T3_Tillson(close,8,0.7)) / ATR(21)."""
    t3 = _t3_tillson(close, n=8, vol=0.7)
    return _safe_div(close - t3, _atr(high, low, close, n=MDAYS))


def f14_stps_216_hilo_activator_5_flip_count_63d(high, low):
    """Flip count of Krausz HiLo Activator(5) over 63d."""
    _, d = _hilo_activator(high, low, n=5)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_217_hilo_activator_atr_dist_period_3(high, low, close):
    """(close - HiLo Activator(3) stop) / ATR(21)."""
    stop, _ = _hilo_activator(high, low, n=3)
    return _safe_div(close - stop, _atr(high, low, close, n=MDAYS))


# ============================================================
# Bucket M — Chande-Kroll & Donchian (218-221)
# ============================================================

def f14_stps_218_chande_kroll_stop_flip_count_63d(high, low, close):
    """Count over 63d of bars where close crossed below chande_kroll long stop."""
    h_stop, _ = _chande_kroll(high, low, close, p=10, q=20, mult=3.0)
    br = (close < h_stop) & h_stop.notna()
    flip = (br & ~br.shift(1).fillna(False)).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_219_chande_kroll_breach_then_recover_count_252d(high, low, close):
    """252d count of chande_kroll breach-then-recover events within 5d."""
    h_stop, _ = _chande_kroll(high, low, close, p=10, q=20, mult=3.0)
    br = (close < h_stop) & h_stop.notna()
    br_arr = br.values
    n = len(br_arr)
    rec = np.zeros(n, dtype=float)
    for i in range(n):
        if br_arr[i]:
            end = min(n, i + 1 + WDAYS)
            for j in range(i + 1, end):
                if not br_arr[j]:
                    rec[i] = 1.0
                    break
    rec_s = pd.Series(rec, index=close.index)
    return rec_s.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_220_donchian_trail_20_long_flip_count_63d(high, low, close):
    """Count over 63d of Donchian(20) long-exit events (close crosses below ll(20))."""
    ll = low.rolling(20, min_periods=5).min()
    br = (close < ll) & ll.notna()
    flip = (br & ~br.shift(1).fillna(False)).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_221_donchian_trail_10_exit_breach_count_252d(high, low, close):
    """Count over 252d of bars where close < lowest_low(10) (Donchian-10 exit)."""
    ll = low.rolling(10, min_periods=3).min()
    br = (close < ll).astype(float).where(ll.notna(), np.nan)
    return br.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket N — Composite top/distribution (222-225)
# ============================================================

def f14_stps_222_st_10_3_flip_with_gap_down_indicator(open, high, low, close):
    """Indicator: ST(10,3) down-flip AND today's open < yesterday's close."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1))
    gap_down = (open < close.shift(1))
    return (down & gap_down).astype(float).where(d != 0, np.nan)


def f14_stps_223_volume_at_st_down_flip_zscore_252d(high, low, close, volume):
    """Z-score over 252d of volume, evaluated only at ST(10,3) down-flip bars."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1))
    z = _rolling_zscore(volume, YDAYS)
    return z.where(down, np.nan)


def f14_stps_224_post_psar_flip_max_recovery_pct_10d(high, low, close):
    """After PSAR down-flip: max recovery (max return) within 10d."""
    _, d = _psar(high, low)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _post_flip_extreme(close, down, 10, mode='max')


def f14_stps_225_count_trails_breached_at_peak_top5pct_indicator(open, high, low, close):
    """Indicator: 3+ trails in short state AND close in top 5% of 252d range."""
    cnt = f14_stps_184_count_trails_in_short_state(open, high, low, close)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((cnt >= 3) & (pos >= 0.95)).astype(float).where(cnt.notna() & pos.notna(), np.nan)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

SUPERTREND_PSAR_CHANDELIER_BASE_REGISTRY_151_225 = {
    "f14_stps_151_supertrend_hlc3_basis_10_3_log_dist": {"inputs": ["high", "low", "close"], "func": f14_stps_151_supertrend_hlc3_basis_10_3_log_dist},
    "f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_152_supertrend_ohlc4_basis_10_3_log_dist},
    "f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_153_supertrend_heikin_ashi_10_3_flip_count_63d},
    "f14_stps_154_supertrend_HA_close_dist_atr_10_3": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_154_supertrend_HA_close_dist_atr_10_3},
    "f14_stps_155_weighted_atr_supertrend_recent_heavy_dist": {"inputs": ["high", "low", "close"], "func": f14_stps_155_weighted_atr_supertrend_recent_heavy_dist},
    "f14_stps_156_supertrend_immediate_reflip_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_156_supertrend_immediate_reflip_count_63d},
    "f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_157_supertrend_reflip_ratio_to_total_flips_252d},
    "f14_stps_158_supertrend_short_state_after_252d_high": {"inputs": ["high", "low", "close"], "func": f14_stps_158_supertrend_short_state_after_252d_high},
    "f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_159_supertrend_atr_multiplier_4_flip_count_63d},
    "f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_160_supertrend_atr_multiplier_1p5_flip_count_63d},
    "f14_stps_161_supertrend_consecutive_short_state_streak_max_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_161_supertrend_consecutive_short_state_streak_max_252d},
    "f14_stps_162_supertrend_avg_short_state_duration_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_162_supertrend_avg_short_state_duration_252d},
    "f14_stps_163_psar_fast_step_0p04_flip_count_63d": {"inputs": ["high", "low"], "func": f14_stps_163_psar_fast_step_0p04_flip_count_63d},
    "f14_stps_164_psar_slow_step_0p01_flip_count_252d": {"inputs": ["high", "low"], "func": f14_stps_164_psar_slow_step_0p01_flip_count_252d},
    "f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator": {"inputs": ["high", "low"], "func": f14_stps_165_psar_cluster_3plus_reversals_in_10d_indicator},
    "f14_stps_166_psar_cluster_count_5plus_in_21d_252d": {"inputs": ["high", "low"], "func": f14_stps_166_psar_cluster_count_5plus_in_21d_252d},
    "f14_stps_167_psar_first_down_flip_after_60d_long_streak": {"inputs": ["high", "low"], "func": f14_stps_167_psar_first_down_flip_after_60d_long_streak},
    "f14_stps_168_psar_AF_at_max_then_flip_within_5d": {"inputs": ["high", "low"], "func": f14_stps_168_psar_AF_at_max_then_flip_within_5d},
    "f14_stps_169_psar_gap_through_psar_pct": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_169_psar_gap_through_psar_pct},
    "f14_stps_170_chandelier_long_atr_dist_zscore_504d": {"inputs": ["high", "low", "close"], "func": f14_stps_170_chandelier_long_atr_dist_zscore_504d},
    "f14_stps_171_chandelier_no_mans_land_indicator": {"inputs": ["high", "low", "close"], "func": f14_stps_171_chandelier_no_mans_land_indicator},
    "f14_stps_172_chandelier_short_breach_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_172_chandelier_short_breach_count_63d},
    "f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_173_chandelier_long_breach_then_lower_low_5d_count_252d},
    "f14_stps_174_chandelier_long_param_50_2_atr_dist": {"inputs": ["high", "low", "close"], "func": f14_stps_174_chandelier_long_param_50_2_atr_dist},
    "f14_stps_175_chandelier_long_param_10_4_atr_dist": {"inputs": ["high", "low", "close"], "func": f14_stps_175_chandelier_long_param_10_4_atr_dist},
    "f14_stps_176_chandelier_distance_compression_21d_vs_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_176_chandelier_distance_compression_21d_vs_252d},
    "f14_stps_177_kase_devstop_long_atr_skew_distance": {"inputs": ["high", "low", "close"], "func": f14_stps_177_kase_devstop_long_atr_skew_distance},
    "f14_stps_178_kase_devstop_breach_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_178_kase_devstop_breach_count_63d},
    "f14_stps_179_kase_devstop_warning_line_dist_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_179_kase_devstop_warning_line_dist_atr},
    "f14_stps_180_volatility_stop_stoller_atkinson_dist_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_180_volatility_stop_stoller_atkinson_dist_atr},
    "f14_stps_181_volatility_stop_flips_in_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_181_volatility_stop_flips_in_63d},
    "f14_stps_182_atr_trail_1x_breach_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_182_atr_trail_1x_breach_count_63d},
    "f14_stps_183_atr_trail_5x_breach_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_183_atr_trail_5x_breach_count_252d},
    "f14_stps_184_count_trails_in_short_state": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_184_count_trails_in_short_state},
    "f14_stps_185_count_trails_flipped_short_within_5d": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_185_count_trails_flipped_short_within_5d},
    "f14_stps_186_count_trails_flipped_short_within_10d": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_186_count_trails_flipped_short_within_10d},
    "f14_stps_187_count_trails_flipped_short_within_21d": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_187_count_trails_flipped_short_within_21d},
    "f14_stps_188_bars_since_psar_up_flip": {"inputs": ["high", "low"], "func": f14_stps_188_bars_since_psar_up_flip},
    "f14_stps_189_bars_since_chandelier_long_flip_up": {"inputs": ["high", "low", "close"], "func": f14_stps_189_bars_since_chandelier_long_flip_up},
    "f14_stps_190_bars_since_atr_trail_3x_flip": {"inputs": ["high", "low", "close"], "func": f14_stps_190_bars_since_atr_trail_3x_flip},
    "f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_191_max_recovery_back_toward_st_10_3_after_down_flip_21d},
    "f14_stps_192_max_drawdown_from_st_down_flip_bar_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_192_max_drawdown_from_st_down_flip_bar_21d},
    "f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_193_max_drawdown_from_psar_down_flip_bar_21d},
    "f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_194_max_drawdown_from_chandelier_breach_bar_21d},
    "f14_stps_195_post_flip_volume_surge_ratio_5d": {"inputs": ["high", "low", "close", "volume"], "func": f14_stps_195_post_flip_volume_surge_ratio_5d},
    "f14_stps_196_whipsaw_freq_st_10_3_in_42d": {"inputs": ["high", "low", "close"], "func": f14_stps_196_whipsaw_freq_st_10_3_in_42d},
    "f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high": {"inputs": ["high", "low", "close"], "func": f14_stps_197_whipsaw_freq_at_peak_top10pct_252d_high},
    "f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high": {"inputs": ["high", "low", "close"], "func": f14_stps_198_whipsaw_freq_at_peak_top5pct_252d_high},
    "f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio": {"inputs": ["high", "low", "close"], "func": f14_stps_199_st_stop_distance_compression_21d_vs_252d_ratio},
    "f14_stps_200_st_stop_distance_expansion_zscore_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_200_st_stop_distance_expansion_zscore_21d},
    "f14_stps_201_trail_to_price_gap_rolling_std_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_201_trail_to_price_gap_rolling_std_63d},
    "f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator": {"inputs": ["high", "low", "close"], "func": f14_stps_202_first_st_down_flip_after_252d_uptrend_indicator},
    "f14_stps_203_first_st_down_flip_magnitude_log_drop_5d": {"inputs": ["high", "low", "close"], "func": f14_stps_203_first_st_down_flip_magnitude_log_drop_5d},
    "f14_stps_204_st_10_3_trail_slope_degrees_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_204_st_10_3_trail_slope_degrees_21d},
    "f14_stps_205_st_trail_slope_deceleration_21d_vs_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_205_st_trail_slope_deceleration_21d_vs_63d},
    "f14_stps_206_psar_curve_deceleration_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_206_psar_curve_deceleration_21d},
    "f14_stps_207_chandelier_long_slope_decay_21d_vs_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_207_chandelier_long_slope_decay_21d_vs_63d},
    "f14_stps_208_multi_period_st_fast_short_slow_long_indicator": {"inputs": ["high", "low", "close"], "func": f14_stps_208_multi_period_st_fast_short_slow_long_indicator},
    "f14_stps_209_multi_period_st_fast_long_slow_short_indicator": {"inputs": ["high", "low", "close"], "func": f14_stps_209_multi_period_st_fast_long_slow_short_indicator},
    "f14_stps_210_HA_psar_flip_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_210_HA_psar_flip_count_63d},
    "f14_stps_211_HA_psar_atr_dist": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_211_HA_psar_atr_dist},
    "f14_stps_212_time_decay_weighted_atr_st_dist": {"inputs": ["high", "low", "close"], "func": f14_stps_212_time_decay_weighted_atr_st_dist},
    "f14_stps_213_zlema_trail_dist_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_213_zlema_trail_dist_atr},
    "f14_stps_214_mcginley_dynamic_trail_dist_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_214_mcginley_dynamic_trail_dist_atr},
    "f14_stps_215_t3_tillson_trail_dist_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_215_t3_tillson_trail_dist_atr},
    "f14_stps_216_hilo_activator_5_flip_count_63d": {"inputs": ["high", "low"], "func": f14_stps_216_hilo_activator_5_flip_count_63d},
    "f14_stps_217_hilo_activator_atr_dist_period_3": {"inputs": ["high", "low", "close"], "func": f14_stps_217_hilo_activator_atr_dist_period_3},
    "f14_stps_218_chande_kroll_stop_flip_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_218_chande_kroll_stop_flip_count_63d},
    "f14_stps_219_chande_kroll_breach_then_recover_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_219_chande_kroll_breach_then_recover_count_252d},
    "f14_stps_220_donchian_trail_20_long_flip_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_220_donchian_trail_20_long_flip_count_63d},
    "f14_stps_221_donchian_trail_10_exit_breach_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_221_donchian_trail_10_exit_breach_count_252d},
    "f14_stps_222_st_10_3_flip_with_gap_down_indicator": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_222_st_10_3_flip_with_gap_down_indicator},
    "f14_stps_223_volume_at_st_down_flip_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f14_stps_223_volume_at_st_down_flip_zscore_252d},
    "f14_stps_224_post_psar_flip_max_recovery_pct_10d": {"inputs": ["high", "low", "close"], "func": f14_stps_224_post_psar_flip_max_recovery_pct_10d},
    "f14_stps_225_count_trails_breached_at_peak_top5pct_indicator": {"inputs": ["open", "high", "low", "close"], "func": f14_stps_225_count_trails_breached_at_peak_top5pct_indicator},
}
