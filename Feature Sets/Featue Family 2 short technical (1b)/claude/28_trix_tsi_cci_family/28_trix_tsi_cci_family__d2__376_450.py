"""28_trix_tsi_cci_family d2 features 376-450 — order-2 difference of corresponding base features.

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

def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)

def _basket_classical(high, low, close):
    return [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20), _cmo(close, 14), _dpo(close, MDAYS), _kst(close)]

def _adl(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    return mfv.cumsum()

def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    ad = _adl(high, low, close, volume)
    return _ema(ad, fast) - _ema(ad, slow)

def _force_index(close, volume, n=13):
    return _ema(close.diff() * volume, n)

def _klinger(high, low, close, volume, fast=34, slow=55):
    tp = (high + low + close) / 3.0
    tp_prev = tp.shift(1)
    direction = pd.Series(np.where(tp > tp_prev, 1.0, np.where(tp < tp_prev, -1.0, 0.0)), index=close.index)
    dm = high - low
    cm = dm.rolling(fast, min_periods=max(fast // 3, 2)).sum()
    ratio = _safe_div(dm, cm) * 2.0 - 1.0
    vf = volume * direction * ratio.where(cm > 0, 0.0) * 100.0
    return _ema(vf, fast) - _ema(vf, slow)

def _extended_basket(high, low, close, volume):
    """6 classical + 3 volume-flavor = 9 indicators."""
    return _basket_classical(high, low, close) + [_chaikin_osc(high, low, close, volume, 3, 10), _force_index(close, volume, 13), _klinger(high, low, close, volume, 34, 55)]

def _binned_mutual_info_inner(w):
    """w: flat array of 2*n samples — first n are x, last n are y. Bin both into 4 bins
    via quantiles, compute MI in nats."""
    if np.isnan(w).any():
        return np.nan
    n = len(w) // 2
    if n < 6:
        return np.nan
    x = w[:n]
    y = w[n:]
    if np.ptp(x) == 0 or np.ptp(y) == 0:
        return 0.0
    bx = np.quantile(x, [0.25, 0.5, 0.75])
    by = np.quantile(y, [0.25, 0.5, 0.75])
    ix = np.digitize(x, bx)
    iy = np.digitize(y, by)
    p_xy = np.zeros((4, 4), dtype=float)
    for a, b in zip(ix, iy):
        p_xy[a, b] += 1
    p_xy /= n
    p_x = p_xy.sum(axis=1)
    p_y = p_xy.sum(axis=0)
    mi = 0.0
    for a in range(4):
        for b in range(4):
            if p_xy[a, b] > 0 and p_x[a] > 0 and (p_y[b] > 0):
                mi += p_xy[a, b] * np.log(p_xy[a, b] / (p_x[a] * p_y[b]))
    return float(mi)

def _rolling_mutual_info(x, y, n=63):
    df = pd.concat([x.rename('_x'), y.rename('_y')], axis=1)
    out = np.full(len(df), np.nan)
    arr_x = df['_x'].to_numpy()
    arr_y = df['_y'].to_numpy()
    nv = len(df)
    for i in range(n - 1, nv):
        wx = arr_x[i - n + 1:i + 1]
        wy = arr_y[i - n + 1:i + 1]
        if np.isnan(wx).any() or np.isnan(wy).any():
            continue
        out[i] = _binned_mutual_info_inner(np.concatenate([wx, wy]))
    return pd.Series(out, index=df.index)

def _sample_entropy_inner(w, m=2, r_mult=0.2):
    """SampEn(m, r) on window w. r = r_mult * std(w)."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < m + 2:
        return np.nan
    r = r_mult * np.std(w)
    if r == 0:
        return np.nan

    def _count_matches(mm):
        cnt = 0
        for i in range(n - mm):
            for j in range(i + 1, n - mm + 1):
                if np.max(np.abs(w[i:i + mm] - w[j:j + mm])) < r:
                    cnt += 1
        return cnt
    B = _count_matches(m)
    A = _count_matches(m + 1)
    if B == 0 or A == 0:
        return np.nan
    return float(-np.log(A / B))

def _rolling_sample_entropy(s, n=21):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(lambda w: _sample_entropy_inner(w, 2, 0.2), raw=True)

def _permutation_entropy_inner(w, order=3):
    """Permutation entropy of order m. Returns normalized in [0,1]."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < order + 1:
        return np.nan
    from math import factorial
    perms = {}
    cnt = 0
    for i in range(n - order + 1):
        sub = w[i:i + order]
        rank = tuple(np.argsort(sub).tolist())
        perms[rank] = perms.get(rank, 0) + 1
        cnt += 1
    if cnt == 0:
        return np.nan
    pe = 0.0
    for v in perms.values():
        p = v / cnt
        if p > 0:
            pe -= p * np.log(p)
    return float(pe / np.log(factorial(order)))

def _rolling_permutation_entropy(s, n=21, order=3):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(lambda w: _permutation_entropy_inner(w, order), raw=True)

def _higuchi_fd_inner(w, k_max=5):
    """Higuchi fractal dimension."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 12:
        return np.nan
    lks = []
    log_ks = []
    for k in range(1, k_max + 1):
        L_k = 0.0
        m_count = 0
        for m in range(k):
            idx = np.arange(m, n, k)
            if len(idx) < 2:
                continue
            L_m = np.sum(np.abs(np.diff(w[idx])))
            norm = (n - 1.0) / ((n - m - 1) // k * k)
            L_k += L_m * norm / k
            m_count += 1
        if m_count == 0:
            continue
        L_k /= m_count
        if L_k > 0:
            lks.append(np.log(L_k))
            log_ks.append(np.log(1.0 / k))
    if len(lks) < 3:
        return np.nan
    slope = np.polyfit(log_ks, lks, 1)[0]
    return float(slope)

def _rolling_higuchi_fd(s, n=63):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(lambda w: _higuchi_fd_inner(w, 5), raw=True)

def _hurst_rs_inner(w):
    """R/S Hurst exponent on window."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 12:
        return np.nan
    lags = [2, 4, 8, 16] if n >= 16 else [2, 4, 8] if n >= 8 else [2, 4]
    rs = []
    log_n = []
    for lag in lags:
        if lag >= n:
            continue
        chunks = n // lag
        if chunks == 0:
            continue
        rs_vals = []
        for c in range(chunks):
            ch = w[c * lag:(c + 1) * lag]
            mean = ch.mean()
            dev = ch - mean
            cdev = np.cumsum(dev)
            R = cdev.max() - cdev.min()
            S = ch.std()
            if S > 0:
                rs_vals.append(R / S)
        if len(rs_vals) > 0:
            rs.append(np.log(np.mean(rs_vals)))
            log_n.append(np.log(lag))
    if len(rs) < 2:
        return np.nan
    slope = np.polyfit(log_n, rs, 1)[0]
    return float(slope)

def _rolling_hurst_rs(s, n=63):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(_hurst_rs_inner, raw=True)

def _dfa_inner(w):
    """Detrended Fluctuation Analysis exponent."""
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 16:
        return np.nan
    y = np.cumsum(w - w.mean())
    scales = [4, 8, 16, 32] if n >= 32 else [4, 8, 16] if n >= 16 else [4, 8]
    f = []
    log_s = []
    for s in scales:
        if s >= n:
            continue
        chunks = n // s
        if chunks < 2:
            continue
        rms = []
        for c in range(chunks):
            seg = y[c * s:(c + 1) * s]
            x = np.arange(s, dtype=float)
            p = np.polyfit(x, seg, 1)
            trend = np.polyval(p, x)
            rms.append(np.sqrt(np.mean((seg - trend) ** 2)))
        if len(rms) > 0:
            f.append(np.log(np.mean(rms)))
            log_s.append(np.log(s))
    if len(f) < 2:
        return np.nan
    return float(np.polyfit(log_s, f, 1)[0])

def _rolling_dfa(s, n=252):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(_dfa_inner, raw=True)

def _lz_complexity_inner(w):
    """Lempel-Ziv complexity on binarized window."""
    if np.isnan(w).any():
        return np.nan
    if len(w) < 6:
        return np.nan
    med = np.median(w)
    bits = ''.join(('1' if v > med else '0' for v in w))
    i, c = (0, 1)
    n = len(bits)
    k = 1
    while True:
        if i + k > n:
            break
        sub = bits[i:i + k]
        if sub in bits[:i]:
            k += 1
            if i + k > n:
                c += 1
                break
        else:
            c += 1
            i += k
            k = 1
            if i >= n:
                break
    return float(c) / (n / np.log2(n + 1))

def _rolling_lz(s, n=63):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(_lz_complexity_inner, raw=True)

def _recurrence_rate_inner(w, eps_mult=0.2):
    """Recurrence rate at threshold eps = eps_mult * std(w)."""
    if np.isnan(w).any() or len(w) < 6:
        return np.nan
    eps = eps_mult * np.std(w)
    if eps == 0:
        return np.nan
    n = len(w)
    diffs = np.abs(w[:, None] - w[None, :])
    return float((diffs < eps).sum() - n) / (n * (n - 1))

def _rolling_recurrence(s, n=21):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(lambda w: _recurrence_rate_inner(w, 0.2), raw=True)

def _multiscale_entropy_inner(w, scale=2):
    """Multi-scale sample entropy: coarse-grain then SampEn."""
    if np.isnan(w).any() or len(w) < scale * 6:
        return np.nan
    n = len(w)
    n_cg = n // scale
    cg = np.array([w[i * scale:(i + 1) * scale].mean() for i in range(n_cg)])
    return _sample_entropy_inner(cg, 2, 0.2)

def _rolling_multiscale_entropy(s, n=63, scale=2):
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(lambda w: _multiscale_entropy_inner(w, scale), raw=True)

def _xfer_entropy_proxy_inner(w):
    """Simplified transfer entropy proxy: |corr(x_t, y_{t-1})| - |corr(y_t, x_{t-1})|.
    Receives window: first half x, second half y."""
    if np.isnan(w).any():
        return np.nan
    n = len(w) // 2
    if n < 6:
        return np.nan
    x = w[:n]
    y = w[n:]
    if np.std(x) == 0 or np.std(y) == 0:
        return np.nan
    xl_yt = np.corrcoef(x[:-1], y[1:])[0, 1] if len(x) > 2 else 0.0
    yl_xt = np.corrcoef(y[:-1], x[1:])[0, 1] if len(y) > 2 else 0.0
    return float(abs(xl_yt) - abs(yl_xt))

def _rolling_xfer_entropy(x, y, n=63):
    df = pd.concat([x.rename('_x'), y.rename('_y')], axis=1)
    out = np.full(len(df), np.nan)
    arr_x = df['_x'].to_numpy()
    arr_y = df['_y'].to_numpy()
    nv = len(df)
    for i in range(n - 1, nv):
        wx = arr_x[i - n + 1:i + 1]
        wy = arr_y[i - n + 1:i + 1]
        if np.isnan(wx).any() or np.isnan(wy).any():
            continue
        out[i] = _xfer_entropy_proxy_inner(np.concatenate([wx, wy]))
    return pd.Series(out, index=df.index)

def _h_chronic_weakness_score_252(high, low, close):
    out = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        out = out + (sig < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    return out.where(close.notna(), np.nan)

def _h_lower_high_breadth_count_63(high, low, close):
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        mx = sig.rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (mx < mx.shift(QDAYS)).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)

def _h_recovery_failure_count_63(high, low, close):
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        prior_max = sig.shift(QDAYS).rolling(QDAYS, min_periods=MDAYS).max()
        recovered = (sig >= prior_max).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
        cnt = cnt + (recovered < 0.5).astype(float)
    return cnt.where(close.notna(), np.nan)

def _h_post_breakdown_failure_count_63(high, low, close):
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        q10 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
        q25 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
        broke = (sig < q10).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
        recov = (sig >= q25).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
        cnt = cnt + ((broke > 0) & (recov < 0.5)).astype(float)
    return cnt.where(close.notna(), np.nan)

def _h_basket_avg_zscore_252(high, low, close):
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1)

def _h_terminal_breakdown_v3(high, low, close):
    lhc = _h_lower_high_breadth_count_63(high, low, close)
    chro = _h_chronic_weakness_score_252(high, low, close)
    avg = _h_basket_avg_zscore_252(high, low, close)
    return ((lhc >= 4) & (chro >= 3) & (avg < -0.5)).astype(float).where(avg.notna(), np.nan)

def _h_post_peak_decay_velocity_63(high, low, close):
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + ((pmax - sig) / float(QDAYS)).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_capitulation_after_persistence(high, low, close):
    avg = _h_basket_avg_zscore_252(high, low, close)
    persist = (avg > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return ((persist > 0.5) & (avg < -1.0)).astype(float).where(avg.notna(), np.nan)

def _h_topping_configuration_v2(high, low, close):
    avg = _h_basket_avg_zscore_252(high, low, close)
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        q = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
        ev = ((sig.shift(1) > q.shift(1)) & (sig <= q)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=1).max() > 0).astype(float).fillna(0)
    return ((cnt >= 3) & (avg > 0.5)).astype(float).where(avg.notna(), np.nan)

def _h_distribution_intensity_v3(high, low, close, volume):
    chro = _h_chronic_weakness_score_252(high, low, close).fillna(0)
    lhc = _h_lower_high_breadth_count_63(high, low, close).fillna(0)
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    cmf = _safe_div(mfv.rolling(20, min_periods=7).sum(), volume.rolling(20, min_periods=7).sum())
    return (chro + lhc + (cmf < 0).astype(float) * 2.0).where(close.notna(), np.nan)

def _h_stuck_score_v3(high, low, close):
    chro = _h_chronic_weakness_score_252(high, low, close).fillna(0)
    recov = _h_recovery_failure_count_63(high, low, close).fillna(0)
    pbf = _h_post_breakdown_failure_count_63(high, low, close).fillna(0)
    avg = _h_basket_avg_zscore_252(high, low, close)
    return (chro + recov + pbf + (avg < -1.0).astype(float) * 3.0).where(close.notna(), np.nan)

def _h_extended_basket_avg_zscore_252(high, low, close, volume):
    zs = []
    for sig in _extended_basket(high, low, close, volume):
        zs.append(_rolling_zscore(sig, YDAYS, min_periods=QDAYS))
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).mean(axis=1)

def _h_extended_basket_extreme_count_252(high, low, close, volume):
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket(high, low, close, volume):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z.abs() > 2.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)

def _h_extended_basket_decay_velocity(high, low, close, volume):
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _extended_basket(high, low, close, volume):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + _safe_div(pmax - sig, pmax.abs()).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_extended_basket_persistent_weakness_252(high, low, close, volume):
    out = pd.Series(0.0, index=close.index)
    for sig in _extended_basket(high, low, close, volume):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        out = out + (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    return out.where(close.notna(), np.nan)

def _h_extended_basket_topping_intensity_v3(high, low, close, volume):
    ex = _h_extended_basket_extreme_count_252(high, low, close, volume).fillna(0)
    az = _h_extended_basket_avg_zscore_252(high, low, close, volume).abs().fillna(0)
    dv = _h_extended_basket_decay_velocity(high, low, close, volume).fillna(0)
    return (ex + az + dv * 5.0).where(close.notna(), np.nan)

def _h_extended_basket_blowoff_collapse(high, low, close, volume):
    az = _h_extended_basket_avg_zscore_252(high, low, close, volume)
    had_blow = (az.shift(1) > 2.0).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    return ((had_blow > 0) & (az < -0.5)).astype(float).where(az.notna(), np.nan)

def f28_ttcf_376_trix_at_sma50_cross_above_value_d2(close: pd.Series) -> pd.Series:
    """TRIX value at the bar of bullish SMA50 cross (close crossing above SMA50). NaN elsewhere."""
    sma50 = close.rolling(50, min_periods=20).mean()
    cross = (close.shift(1) <= sma50.shift(1)) & (close > sma50)
    t = _trix(close, 15)
    return t.where(cross, np.nan).diff().diff()

def f28_ttcf_377_tsi_at_sma200_cross_above_value_d2(close: pd.Series) -> pd.Series:
    """TSI value at the bar close crossed above SMA200 (bull regime onset)."""
    sma200 = close.rolling(200, min_periods=80).mean()
    cross = (close.shift(1) <= sma200.shift(1)) & (close > sma200)
    t = _tsi(close, 25, 13)
    return t.where(cross, np.nan).diff().diff()

def f28_ttcf_378_cci_at_252h_value_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI value when high equals its 252d rolling max — CCI at annual high."""
    c = _cci(high, low, close, 20)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return c.where(at_max, np.nan).diff().diff()

def f28_ttcf_379_cmo_at_252h_value_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """CMO value when high equals its 252d rolling max — CMO at annual high."""
    c = _cmo(close, 14)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return c.where(at_max, np.nan).diff().diff()

def f28_ttcf_380_kst_at_first_252h_in_504_value_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """KST value at first new 252d-high within past 504d (regime-defining peak)."""
    k = _kst(close)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_any_252h = at_max.shift(1).astype(float).fillna(0).rolling(DDAYS_2Y, min_periods=YDAYS).max()
    first_252h = at_max & (prior_any_252h < 0.5)
    return k.where(first_252h, np.nan).diff().diff()

def f28_ttcf_381_dpo_at_first_close_below_sma50_post_peak_value_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """DPO value at first close-below-SMA50 bar following a 63d-high — initial breakdown."""
    sma50 = close.rolling(50, min_periods=20).mean()
    below = close < sma50
    new_below = below & ~below.shift(1, fill_value=False)
    h63 = high == high.rolling(QDAYS, min_periods=MDAYS).max()
    recent_peak = h63.rolling(QDAYS, min_periods=1).max().astype(bool)
    d = _dpo(close, MDAYS)
    return d.where(new_below & recent_peak, np.nan).diff().diff()

def f28_ttcf_382_oscillator_basket_at_252h_avg_zscore_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average z-score of basket indicators ONLY on 252d-high bars; NaN elsewhere."""
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1).where(at_max, np.nan).diff().diff()

def f28_ttcf_383_oscillator_basket_at_volume_climax_value_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Basket-avg-z when volume > 252d 95th percentile (climax volume bars). NaN elsewhere."""
    vq = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    climax = volume > vq
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1).where(climax, np.nan).diff().diff()

def f28_ttcf_384_oscillator_basket_during_atr_expansion_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 0 AND ATR21/ATR63 > 1.2 (expansion regime)."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    expand = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS)) > 1.2
    return ((avg > 0) & expand).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_385_oscillator_basket_during_atr_contraction_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 0 AND ATR21/ATR63 < 0.8 (contraction regime — quiet topping)."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    contract = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS)) < 0.8
    return ((avg > 0) & contract).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_386_oscillator_basket_in_high_vol_regime_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 1 AND ATR-rank (252d) > 0.8 — extension during high-vol regime."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    atr_rank = _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((avg > 1.0) & (atr_rank > 0.8)).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_387_oscillator_basket_in_low_vol_regime_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 1 AND ATR-rank (252d) < 0.2 — extension during quiet regime (smart-money distribution)."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    atr_rank = _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((avg > 1.0) & (atr_rank < 0.2)).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_388_oscillator_basket_in_uptrend_regime_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 0 AND 63d slope of close > 0 — bullish-during-uptrend."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    sl = _rolling_slope(close, QDAYS)
    return ((avg > 0) & (sl > 0)).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_389_oscillator_basket_in_downtrend_regime_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 0 AND 63d slope of close < 0 — bull-osc-during-downtrend (mean-reversion bounce). Distress sig."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    sl = _rolling_slope(close, QDAYS)
    return ((avg > 0) & (sl < 0)).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_390_oscillator_basket_at_distribution_day_event_value_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Basket-avg-z on distribution-day events: close down >0.2% AND volume > prior day. NaN elsewhere."""
    ret = close.pct_change()
    vd = volume.diff()
    distrib = (ret < -0.002) & (vd > 0)
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1).where(distrib, np.nan).diff().diff()

def f28_ttcf_391_trix_chronic_weakness_count_252_d2(close: pd.Series) -> pd.Series:
    """Count of past 252 bars with TRIX < its 504d 25th-percentile (chronic-weak quartile)."""
    t = _trix(close, 15)
    q25 = t.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.25)
    return (t < q25).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(q25.notna(), np.nan).diff().diff()

def f28_ttcf_392_tsi_chronic_below_zero_persistence_252_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with TSI < 0 — chronic-weakness (TSI flavor)."""
    t = _tsi(close, 25, 13)
    return (t < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(t.notna(), np.nan).diff().diff()

def f28_ttcf_393_cci_chronic_below_zero_persistence_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CCI < 0 — chronic-weakness (CCI flavor)."""
    c = _cci(high, low, close, 20)
    return (c < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna(), np.nan).diff().diff()

def f28_ttcf_394_cmo_failed_to_q90_recovery_count_252_d2(close: pd.Series) -> pd.Series:
    """Count of past 252 bars where CMO failed to reach its 504d q90 within prior 63 days."""
    c = _cmo(close, 14)
    q90 = c.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    reached = (c >= q90).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    failed = (reached < 0.5).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum().where(q90.notna(), np.nan).diff().diff()

def f28_ttcf_395_kst_chronic_negative_252_persistence_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with KST < 0 — annual long-momentum chronic-weak."""
    k = _kst(close)
    return (k < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna(), np.nan).diff().diff()

def f28_ttcf_396_dpo_chronic_below_zero_252_persistence_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with DPO < 0 — chronic-cycle-bearish."""
    d = _dpo(close, MDAYS)
    return (d < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(d.notna(), np.nan).diff().diff()

def f28_ttcf_397_oscillator_basket_chronic_weakness_score_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum across basket of (frac past 252 with sig < 0). Higher = more chronic weakness."""
    return _h_chronic_weakness_score_252(high, low, close).diff().diff()

def f28_ttcf_398_oscillator_basket_lower_high_breadth_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators whose 63d rolling max < same max 63 bars ago — breadth of lower-highs."""
    return _h_lower_high_breadth_count_63(high, low, close).diff().diff()

def f28_ttcf_399_oscillator_basket_recovery_failure_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators that DID NOT recover to their prior 63d max within past 63d."""
    return _h_recovery_failure_count_63(high, low, close).diff().diff()

def f28_ttcf_400_oscillator_basket_distribution_zone_indicator_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (basket-avg-z negative slope over 63d) AND (CMF over 63d period avg < 0). Distribution zone."""
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    avg = zs.mean(axis=1)
    sl = _rolling_slope(avg, QDAYS)
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    cmf = _safe_div(mfv.rolling(QDAYS, min_periods=MDAYS).sum(), volume.rolling(QDAYS, min_periods=MDAYS).sum())
    return ((sl < 0) & (cmf < 0)).astype(float).where(avg.notna() & cmf.notna(), np.nan).diff().diff()

def f28_ttcf_401_oscillator_basket_topping_configuration_v2_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket has: (>=3 indicators just exited their 252d q90 in last 21d) AND avg-z still > 0.5."""
    return _h_topping_configuration_v2(high, low, close).diff().diff()

def f28_ttcf_402_oscillator_basket_post_peak_decay_velocity_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean across basket of (63d-max - current) / 63 = decay velocity post-peak."""
    return _h_post_peak_decay_velocity_63(high, low, close).diff().diff()

def f28_ttcf_403_oscillator_basket_blowoff_then_decay_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z was >2 in past 63 days AND is now < 0 — blowoff then collapse."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    had_blowoff = (avg.shift(1) > 2.0).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    return ((had_blowoff > 0) & (avg < 0)).astype(float).where(avg.notna(), np.nan).diff().diff()

def f28_ttcf_404_oscillator_basket_capitulation_after_persistence_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z had > 0.5 persistence (frac > 0.5 over 252d) AND now < -1.0 — capitulation post-persistence."""
    return _h_capitulation_after_persistence(high, low, close).diff().diff()

def f28_ttcf_405_oscillator_basket_failed_breakout_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators that broke above 252d q90 then fell back below within 21d — failed breakouts."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        q = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
        above = sig > q
        prev_above = above.shift(1, fill_value=False).astype(bool)
        ev = above & ~prev_above
        ev_lag = ev.shift(MDAYS).fillna(False).astype(bool)
        recently_failed = (ev_lag & (sig < q)).astype(float)
        cnt = cnt + recently_failed.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return cnt.where(close.notna(), np.nan).diff().diff()

def f28_ttcf_406_oscillator_basket_terminal_breakdown_v3_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (lower-high-count >= 4) AND (chronic-weakness >= 3) AND (basket-avg-z < -0.5). Terminal v3."""
    return _h_terminal_breakdown_v3(high, low, close).diff().diff()

def f28_ttcf_407_oscillator_basket_post_breakdown_failure_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators that crossed below their 252d q10 AND have not recovered above q25 in 63d."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        q10 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
        q25 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
        broke = (sig < q10).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
        recov = (sig >= q25).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
        cnt = cnt + ((broke > 0) & (recov < 0.5)).astype(float)
    return cnt.where(close.notna(), np.nan).diff().diff()

def f28_ttcf_408_oscillator_basket_persistent_decline_score_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum across basket of (count of past 252 bars with 21d slope < 0). High score = persistent declines."""
    out = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        sl = _rolling_slope(sig, MDAYS)
        out = out + (sl < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return out.where(close.notna(), np.nan).diff().diff()

def f28_ttcf_409_oscillator_basket_distribution_intensity_v3_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-intensity v3 = chronic-weakness + lower-high-count + (CMF-below-zero) * 2."""
    return _h_distribution_intensity_v3(high, low, close, volume).diff().diff()

def f28_ttcf_410_oscillator_basket_stuck_score_v3_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck-score v3 = chronic-weakness + recovery-failure + post-breakdown-failure + (avg-z<-1) * 3."""
    return _h_stuck_score_v3(high, low, close).diff().diff()

def f28_ttcf_411_mutual_information_trix_tsi_63_d2(close: pd.Series) -> pd.Series:
    """63d binned mutual information between TRIX and TSI (information overlap)."""
    return _rolling_mutual_info(_trix(close, 15), _tsi(close, 25, 13), QDAYS).diff().diff()

def f28_ttcf_412_mutual_information_cci_cmo_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d binned MI between CCI and CMO."""
    return _rolling_mutual_info(_cci(high, low, close, 20), _cmo(close, 14), QDAYS).diff().diff()

def f28_ttcf_413_mutual_information_dpo_kst_63_d2(close: pd.Series) -> pd.Series:
    """63d binned MI between DPO and KST."""
    return _rolling_mutual_info(_dpo(close, MDAYS), _kst(close), QDAYS).diff().diff()

def f28_ttcf_414_transfer_entropy_short_to_long_proxy_63_d2(close: pd.Series) -> pd.Series:
    """Info-flow proxy: TRIX(5) leads TRIX(50)? |corr(short[:-1], long[1:])| - reverse."""
    return _rolling_xfer_entropy(_trix(close, 5), _trix(close, 50), QDAYS).diff().diff()

def f28_ttcf_415_transfer_entropy_long_to_short_proxy_63_d2(close: pd.Series) -> pd.Series:
    """Info-flow proxy: TRIX(50) leads TRIX(5)?"""
    return _rolling_xfer_entropy(_trix(close, 50), _trix(close, 5), QDAYS).diff().diff()

def f28_ttcf_416_cross_oscillator_information_flow_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of TRIX-vs-TSI mutual info."""
    mi = _rolling_mutual_info(_trix(close, 15), _tsi(close, 25, 13), QDAYS)
    return _rolling_zscore(mi, YDAYS, min_periods=QDAYS).diff().diff()

def f28_ttcf_417_cross_oscillator_redundancy_indicator_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if mean of (TRIX-TSI MI + CCI-CMO MI + DPO-KST MI) > 0.5 — high redundancy (basket says same thing)."""
    mi1 = _rolling_mutual_info(_trix(close, 15), _tsi(close, 25, 13), QDAYS).fillna(0)
    mi2 = _rolling_mutual_info(_cci(high, low, close, 20), _cmo(close, 14), QDAYS).fillna(0)
    mi3 = _rolling_mutual_info(_dpo(close, MDAYS), _kst(close), QDAYS).fillna(0)
    avg = (mi1 + mi2 + mi3) / 3.0
    return (avg > 0.5).astype(float).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_418_cross_oscillator_synergy_indicator_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Synergy proxy: total MI minus pairwise MI mean (joint info beyond pairwise). Approx via (1 - mean(pairwise))."""
    mi1 = _rolling_mutual_info(_trix(close, 15), _tsi(close, 25, 13), QDAYS).fillna(0)
    mi2 = _rolling_mutual_info(_cci(high, low, close, 20), _cmo(close, 14), QDAYS).fillna(0)
    mi3 = _rolling_mutual_info(_dpo(close, MDAYS), _kst(close), QDAYS).fillna(0)
    return (1.0 - (mi1 + mi2 + mi3) / 3.0).diff().diff()

def f28_ttcf_419_cross_oscillator_disagreement_index_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Disagreement = std across basket sign-states (TRIX>0, TSI>0, ...). High = indicators disagree."""
    states = []
    for sig in _basket_classical(high, low, close):
        states.append((sig > 0).astype(float))
    df = pd.concat([s.rename(i) for i, s in enumerate(states)], axis=1)
    return df.std(axis=1).diff().diff()

def f28_ttcf_420_cross_oscillator_consensus_index_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consensus = |mean across basket sign-states - 0.5| * 2 (1 = full consensus, 0 = no consensus)."""
    states = []
    for sig in _basket_classical(high, low, close):
        states.append((sig > 0).astype(float))
    df = pd.concat([s.rename(i) for i, s in enumerate(states)], axis=1)
    return ((df.mean(axis=1) - 0.5).abs() * 2.0).diff().diff()

def f28_ttcf_421_trix_sample_entropy_21_d2(close: pd.Series) -> pd.Series:
    """SampEn(m=2, r=0.2*std) of TRIX over 21-bar window — TRIX irregularity."""
    return _rolling_sample_entropy(_trix(close, 15), MDAYS).diff().diff()

def f28_ttcf_422_tsi_sample_entropy_21_d2(close: pd.Series) -> pd.Series:
    """SampEn of TSI over 21-bar window."""
    return _rolling_sample_entropy(_tsi(close, 25, 13), MDAYS).diff().diff()

def f28_ttcf_423_cci_sample_entropy_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SampEn of CCI(20) over 21-bar window."""
    return _rolling_sample_entropy(_cci(high, low, close, 20), MDAYS).diff().diff()

def f28_ttcf_424_cmo_permutation_entropy_21_order3_d2(close: pd.Series) -> pd.Series:
    """Permutation entropy(order=3) of CMO over 21d — pattern-complexity of CMO."""
    return _rolling_permutation_entropy(_cmo(close, 14), MDAYS, 3).diff().diff()

def f28_ttcf_425_kst_permutation_entropy_63_order3_d2(close: pd.Series) -> pd.Series:
    """Permutation entropy(order=3) of KST over 63d."""
    return _rolling_permutation_entropy(_kst(close), QDAYS, 3).diff().diff()

def f28_ttcf_426_dpo_multiscale_entropy_scale2_d2(close: pd.Series) -> pd.Series:
    """Multi-scale sample entropy (scale 2) of DPO over 63d."""
    return _rolling_multiscale_entropy(_dpo(close, MDAYS), QDAYS, 2).diff().diff()

def f28_ttcf_427_basket_avg_sample_entropy_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean SampEn across basket indicators (63d window) — basket-avg irregularity."""
    sums = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        sums = sums + _rolling_sample_entropy(sig, QDAYS).fillna(0)
        nb += 1
    return (sums / float(nb)).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_428_basket_avg_permutation_entropy_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean permutation entropy (order=3) across basket (63d window)."""
    sums = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        sums = sums + _rolling_permutation_entropy(sig, QDAYS, 3).fillna(0)
        nb += 1
    return (sums / float(nb)).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_429_trix_fractal_dimension_higuchi_63_d2(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of TRIX over 63d."""
    return _rolling_higuchi_fd(_trix(close, 15), QDAYS).diff().diff()

def f28_ttcf_430_tsi_hurst_rs_63_d2(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of TSI over 63d."""
    return _rolling_hurst_rs(_tsi(close, 25, 13), QDAYS).diff().diff()

def f28_ttcf_431_cci_hurst_dfa_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DFA Hurst exponent of CCI(20) over 252d."""
    return _rolling_dfa(_cci(high, low, close, 20), YDAYS).diff().diff()

def f28_ttcf_432_cmo_lempel_ziv_complexity_63_d2(close: pd.Series) -> pd.Series:
    """Lempel-Ziv complexity of binarized CMO over 63d."""
    return _rolling_lz(_cmo(close, 14), QDAYS).diff().diff()

def f28_ttcf_433_oscillator_recurrence_rate_avg_21_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean recurrence rate across basket (21d, eps=0.2*std)."""
    sums = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        sums = sums + _rolling_recurrence(sig, MDAYS).fillna(0)
        nb += 1
    return (sums / float(nb)).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_434_oscillator_predictability_horizon_avg_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Predictability proxy: 1 - (avg basket sample entropy / log(63)). High = more predictable."""
    sums = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        sums = sums + _rolling_sample_entropy(sig, QDAYS).fillna(0)
        nb += 1
    avg_se = sums / float(nb)
    return (1.0 - avg_se / float(np.log(QDAYS))).diff().diff()

def f28_ttcf_435_oscillator_complexity_aggregate_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d z-score of basket-avg sample entropy — distribution-context complexity."""
    sums = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        sums = sums + _rolling_sample_entropy(sig, QDAYS).fillna(0)
        nb += 1
    return _rolling_zscore(sums / float(nb), YDAYS, min_periods=QDAYS).diff().diff()

def f28_ttcf_436_extended_basket_with_chaikin_klinger_force_count_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of extended basket (9 indicators: 6 classical + Chaikin + Klinger + Force) with z>1 over 252d."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket(high, low, close, volume):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 1.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan).diff().diff()

def f28_ttcf_437_extended_basket_with_volume_flavor_avg_zscore_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average 252d z-score across the extended (9-indicator) basket."""
    return _h_extended_basket_avg_zscore_252(high, low, close, volume).diff().diff()

def f28_ttcf_438_extended_basket_universe_extreme_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of extended-basket indicators with |z|>2 over 252d — extended-extreme breadth."""
    return _h_extended_basket_extreme_count_252(high, low, close, volume).diff().diff()

def f28_ttcf_439_extended_basket_universe_correlation_breakdown_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z-score of mean pairwise 63d corr across 9-indicator extended basket."""
    cols = _extended_basket(high, low, close, volume)
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pairs.append(cols[i].rolling(QDAYS, min_periods=MDAYS).corr(cols[j]))
    mean_corr = pd.concat([p.rename(k) for k, p in enumerate(pairs)], axis=1).mean(axis=1)
    return _rolling_zscore(mean_corr, YDAYS, min_periods=QDAYS).diff().diff()

def f28_ttcf_440_extended_basket_decay_velocity_post_peak_aggregate_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average across 9-indicator extended basket of (63d max - current) / |63d max| — decay-velocity aggregate."""
    return _h_extended_basket_decay_velocity(high, low, close, volume).diff().diff()

def f28_ttcf_441_extended_basket_topping_intensity_v3_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """v3 topping intensity = extreme_count + (mean abs z) + (peak-decay aggregate * 5)."""
    return _h_extended_basket_topping_intensity_v3(high, low, close, volume).diff().diff()

def f28_ttcf_442_extended_basket_persistent_weakness_score_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum across 9-indicator extended basket of (frac of past 252 bars with z < -0.5)."""
    return _h_extended_basket_persistent_weakness_252(high, low, close, volume).diff().diff()

def f28_ttcf_443_extended_basket_blowoff_collapse_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if extended-basket avg-z exceeded 2.0 in past 63d AND is now < -0.5 — extended blowoff-collapse."""
    return _h_extended_basket_blowoff_collapse(high, low, close, volume).diff().diff()

def f28_ttcf_444_extended_basket_recall_optimized_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recall-oriented score: extreme_count + persistent_weakness + peak_decay (no precision multipliers)."""
    ex = _h_extended_basket_extreme_count_252(high, low, close, volume).fillna(0)
    pw = _h_extended_basket_persistent_weakness_252(high, low, close, volume).fillna(0)
    dv = _h_extended_basket_decay_velocity(high, low, close, volume).fillna(0)
    return (ex + pw + dv).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_445_extended_basket_precision_optimized_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Precision-oriented: blowoff-collapse (5x) + topping-config + chronic-weakness only when ALL >0."""
    bc = _h_extended_basket_blowoff_collapse(high, low, close, volume).fillna(0) * 5.0
    tc = _h_topping_configuration_v2(high, low, close).fillna(0)
    chro = _h_chronic_weakness_score_252(high, low, close).fillna(0)
    all_pos = (bc > 0) & (tc > 0) & (chro > 0)
    return (bc + tc + chro).where(all_pos, 0.0).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_446_oscillator_stuck_probability_proxy_v3_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stuck-prob proxy v3: normalize (stuck_score_v3 + persistent_weakness) by max across basket. In [0,1]."""
    ss = _h_stuck_score_v3(high, low, close).fillna(0)
    pw = _h_extended_basket_persistent_weakness_252(high, low, close, volume).fillna(0)
    raw = ss + pw
    rmax = raw.rolling(YDAYS, min_periods=QDAYS).max().replace(0, np.nan)
    return (raw / rmax).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_447_oscillator_terminal_pattern_master_v3_score_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal master v3 = terminal_breakdown_v3 * 10 + topping_v2 * 5 + blowoff_collapse * 5 + distribution_v3."""
    tb = _h_terminal_breakdown_v3(high, low, close).fillna(0) * 10.0
    tp = _h_topping_configuration_v2(high, low, close).fillna(0) * 5.0
    bc = _h_extended_basket_blowoff_collapse(high, low, close, volume).fillna(0) * 5.0
    di = _h_distribution_intensity_v3(high, low, close, volume).fillna(0)
    return (tb + tp + bc + di).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_448_oscillator_distribution_topping_aggregate_v3_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution+topping aggregate = distribution_v3_score + topping_intensity_v3 + lower_high_count."""
    di = _h_distribution_intensity_v3(high, low, close, volume).fillna(0)
    ti = _h_extended_basket_topping_intensity_v3(high, low, close, volume).fillna(0)
    lh = _h_lower_high_breadth_count_63(high, low, close).fillna(0)
    return (di + ti + lh).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_449_oscillator_blowoff_decay_master_v3_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Blowoff-decay master = post_peak_decay * 10 + blowoff_collapse * 5 + capitulation."""
    pd_ = _h_post_peak_decay_velocity_63(high, low, close).fillna(0) * 10.0
    bc = _h_extended_basket_blowoff_collapse(high, low, close, volume).fillna(0) * 5.0
    cap = _h_capitulation_after_persistence(high, low, close).fillna(0)
    return (pd_ + bc + cap).where(close.notna(), np.nan).diff().diff()

def f28_ttcf_450_absolute_terminal_oscillator_extended_v3_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if terminal_breakdown_v3 = 1 AND blowoff_collapse = 1 AND stuck_score >= 5 — absolute terminal."""
    tb = _h_terminal_breakdown_v3(high, low, close).fillna(0)
    bc = _h_extended_basket_blowoff_collapse(high, low, close, volume).fillna(0)
    ss = _h_stuck_score_v3(high, low, close).fillna(0)
    return ((tb > 0) & (bc > 0) & (ss >= 5.0)).astype(float).where(close.notna(), np.nan).diff().diff()
TRIX_TSI_CCI_FAMILY_D2_REGISTRY_376_450 = {'f28_ttcf_376_trix_at_sma50_cross_above_value_d2': {'inputs': ['close'], 'func': f28_ttcf_376_trix_at_sma50_cross_above_value_d2}, 'f28_ttcf_377_tsi_at_sma200_cross_above_value_d2': {'inputs': ['close'], 'func': f28_ttcf_377_tsi_at_sma200_cross_above_value_d2}, 'f28_ttcf_378_cci_at_252h_value_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_378_cci_at_252h_value_d2}, 'f28_ttcf_379_cmo_at_252h_value_d2': {'inputs': ['high', 'close'], 'func': f28_ttcf_379_cmo_at_252h_value_d2}, 'f28_ttcf_380_kst_at_first_252h_in_504_value_d2': {'inputs': ['high', 'close'], 'func': f28_ttcf_380_kst_at_first_252h_in_504_value_d2}, 'f28_ttcf_381_dpo_at_first_close_below_sma50_post_peak_value_d2': {'inputs': ['high', 'close'], 'func': f28_ttcf_381_dpo_at_first_close_below_sma50_post_peak_value_d2}, 'f28_ttcf_382_oscillator_basket_at_252h_avg_zscore_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_382_oscillator_basket_at_252h_avg_zscore_d2}, 'f28_ttcf_383_oscillator_basket_at_volume_climax_value_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_383_oscillator_basket_at_volume_climax_value_d2}, 'f28_ttcf_384_oscillator_basket_during_atr_expansion_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_384_oscillator_basket_during_atr_expansion_state_d2}, 'f28_ttcf_385_oscillator_basket_during_atr_contraction_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_385_oscillator_basket_during_atr_contraction_state_d2}, 'f28_ttcf_386_oscillator_basket_in_high_vol_regime_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_386_oscillator_basket_in_high_vol_regime_state_d2}, 'f28_ttcf_387_oscillator_basket_in_low_vol_regime_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_387_oscillator_basket_in_low_vol_regime_state_d2}, 'f28_ttcf_388_oscillator_basket_in_uptrend_regime_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_388_oscillator_basket_in_uptrend_regime_state_d2}, 'f28_ttcf_389_oscillator_basket_in_downtrend_regime_state_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_389_oscillator_basket_in_downtrend_regime_state_d2}, 'f28_ttcf_390_oscillator_basket_at_distribution_day_event_value_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_390_oscillator_basket_at_distribution_day_event_value_d2}, 'f28_ttcf_391_trix_chronic_weakness_count_252_d2': {'inputs': ['close'], 'func': f28_ttcf_391_trix_chronic_weakness_count_252_d2}, 'f28_ttcf_392_tsi_chronic_below_zero_persistence_252_d2': {'inputs': ['close'], 'func': f28_ttcf_392_tsi_chronic_below_zero_persistence_252_d2}, 'f28_ttcf_393_cci_chronic_below_zero_persistence_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_393_cci_chronic_below_zero_persistence_252_d2}, 'f28_ttcf_394_cmo_failed_to_q90_recovery_count_252_d2': {'inputs': ['close'], 'func': f28_ttcf_394_cmo_failed_to_q90_recovery_count_252_d2}, 'f28_ttcf_395_kst_chronic_negative_252_persistence_d2': {'inputs': ['close'], 'func': f28_ttcf_395_kst_chronic_negative_252_persistence_d2}, 'f28_ttcf_396_dpo_chronic_below_zero_252_persistence_d2': {'inputs': ['close'], 'func': f28_ttcf_396_dpo_chronic_below_zero_252_persistence_d2}, 'f28_ttcf_397_oscillator_basket_chronic_weakness_score_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_397_oscillator_basket_chronic_weakness_score_252_d2}, 'f28_ttcf_398_oscillator_basket_lower_high_breadth_count_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_398_oscillator_basket_lower_high_breadth_count_63_d2}, 'f28_ttcf_399_oscillator_basket_recovery_failure_count_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_399_oscillator_basket_recovery_failure_count_63_d2}, 'f28_ttcf_400_oscillator_basket_distribution_zone_indicator_63_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_400_oscillator_basket_distribution_zone_indicator_63_d2}, 'f28_ttcf_401_oscillator_basket_topping_configuration_v2_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_401_oscillator_basket_topping_configuration_v2_d2}, 'f28_ttcf_402_oscillator_basket_post_peak_decay_velocity_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_402_oscillator_basket_post_peak_decay_velocity_63_d2}, 'f28_ttcf_403_oscillator_basket_blowoff_then_decay_indicator_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_403_oscillator_basket_blowoff_then_decay_indicator_d2}, 'f28_ttcf_404_oscillator_basket_capitulation_after_persistence_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_404_oscillator_basket_capitulation_after_persistence_d2}, 'f28_ttcf_405_oscillator_basket_failed_breakout_count_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_405_oscillator_basket_failed_breakout_count_252_d2}, 'f28_ttcf_406_oscillator_basket_terminal_breakdown_v3_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_406_oscillator_basket_terminal_breakdown_v3_d2}, 'f28_ttcf_407_oscillator_basket_post_breakdown_failure_count_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_407_oscillator_basket_post_breakdown_failure_count_63_d2}, 'f28_ttcf_408_oscillator_basket_persistent_decline_score_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_408_oscillator_basket_persistent_decline_score_252_d2}, 'f28_ttcf_409_oscillator_basket_distribution_intensity_v3_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_409_oscillator_basket_distribution_intensity_v3_score_d2}, 'f28_ttcf_410_oscillator_basket_stuck_score_v3_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_410_oscillator_basket_stuck_score_v3_d2}, 'f28_ttcf_411_mutual_information_trix_tsi_63_d2': {'inputs': ['close'], 'func': f28_ttcf_411_mutual_information_trix_tsi_63_d2}, 'f28_ttcf_412_mutual_information_cci_cmo_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_412_mutual_information_cci_cmo_63_d2}, 'f28_ttcf_413_mutual_information_dpo_kst_63_d2': {'inputs': ['close'], 'func': f28_ttcf_413_mutual_information_dpo_kst_63_d2}, 'f28_ttcf_414_transfer_entropy_short_to_long_proxy_63_d2': {'inputs': ['close'], 'func': f28_ttcf_414_transfer_entropy_short_to_long_proxy_63_d2}, 'f28_ttcf_415_transfer_entropy_long_to_short_proxy_63_d2': {'inputs': ['close'], 'func': f28_ttcf_415_transfer_entropy_long_to_short_proxy_63_d2}, 'f28_ttcf_416_cross_oscillator_information_flow_zscore_252_d2': {'inputs': ['close'], 'func': f28_ttcf_416_cross_oscillator_information_flow_zscore_252_d2}, 'f28_ttcf_417_cross_oscillator_redundancy_indicator_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_417_cross_oscillator_redundancy_indicator_63_d2}, 'f28_ttcf_418_cross_oscillator_synergy_indicator_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_418_cross_oscillator_synergy_indicator_63_d2}, 'f28_ttcf_419_cross_oscillator_disagreement_index_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_419_cross_oscillator_disagreement_index_63_d2}, 'f28_ttcf_420_cross_oscillator_consensus_index_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_420_cross_oscillator_consensus_index_63_d2}, 'f28_ttcf_421_trix_sample_entropy_21_d2': {'inputs': ['close'], 'func': f28_ttcf_421_trix_sample_entropy_21_d2}, 'f28_ttcf_422_tsi_sample_entropy_21_d2': {'inputs': ['close'], 'func': f28_ttcf_422_tsi_sample_entropy_21_d2}, 'f28_ttcf_423_cci_sample_entropy_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_423_cci_sample_entropy_21_d2}, 'f28_ttcf_424_cmo_permutation_entropy_21_order3_d2': {'inputs': ['close'], 'func': f28_ttcf_424_cmo_permutation_entropy_21_order3_d2}, 'f28_ttcf_425_kst_permutation_entropy_63_order3_d2': {'inputs': ['close'], 'func': f28_ttcf_425_kst_permutation_entropy_63_order3_d2}, 'f28_ttcf_426_dpo_multiscale_entropy_scale2_d2': {'inputs': ['close'], 'func': f28_ttcf_426_dpo_multiscale_entropy_scale2_d2}, 'f28_ttcf_427_basket_avg_sample_entropy_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_427_basket_avg_sample_entropy_63_d2}, 'f28_ttcf_428_basket_avg_permutation_entropy_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_428_basket_avg_permutation_entropy_63_d2}, 'f28_ttcf_429_trix_fractal_dimension_higuchi_63_d2': {'inputs': ['close'], 'func': f28_ttcf_429_trix_fractal_dimension_higuchi_63_d2}, 'f28_ttcf_430_tsi_hurst_rs_63_d2': {'inputs': ['close'], 'func': f28_ttcf_430_tsi_hurst_rs_63_d2}, 'f28_ttcf_431_cci_hurst_dfa_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_431_cci_hurst_dfa_252_d2}, 'f28_ttcf_432_cmo_lempel_ziv_complexity_63_d2': {'inputs': ['close'], 'func': f28_ttcf_432_cmo_lempel_ziv_complexity_63_d2}, 'f28_ttcf_433_oscillator_recurrence_rate_avg_21_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_433_oscillator_recurrence_rate_avg_21_d2}, 'f28_ttcf_434_oscillator_predictability_horizon_avg_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_434_oscillator_predictability_horizon_avg_63_d2}, 'f28_ttcf_435_oscillator_complexity_aggregate_zscore_252_d2': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_435_oscillator_complexity_aggregate_zscore_252_d2}, 'f28_ttcf_436_extended_basket_with_chaikin_klinger_force_count_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_436_extended_basket_with_chaikin_klinger_force_count_d2}, 'f28_ttcf_437_extended_basket_with_volume_flavor_avg_zscore_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_437_extended_basket_with_volume_flavor_avg_zscore_d2}, 'f28_ttcf_438_extended_basket_universe_extreme_count_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_438_extended_basket_universe_extreme_count_252_d2}, 'f28_ttcf_439_extended_basket_universe_correlation_breakdown_zscore_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_439_extended_basket_universe_correlation_breakdown_zscore_252_d2}, 'f28_ttcf_440_extended_basket_decay_velocity_post_peak_aggregate_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_440_extended_basket_decay_velocity_post_peak_aggregate_d2}, 'f28_ttcf_441_extended_basket_topping_intensity_v3_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_441_extended_basket_topping_intensity_v3_score_d2}, 'f28_ttcf_442_extended_basket_persistent_weakness_score_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_442_extended_basket_persistent_weakness_score_252_d2}, 'f28_ttcf_443_extended_basket_blowoff_collapse_indicator_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_443_extended_basket_blowoff_collapse_indicator_d2}, 'f28_ttcf_444_extended_basket_recall_optimized_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_444_extended_basket_recall_optimized_score_d2}, 'f28_ttcf_445_extended_basket_precision_optimized_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_445_extended_basket_precision_optimized_score_d2}, 'f28_ttcf_446_oscillator_stuck_probability_proxy_v3_252_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_446_oscillator_stuck_probability_proxy_v3_252_d2}, 'f28_ttcf_447_oscillator_terminal_pattern_master_v3_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_447_oscillator_terminal_pattern_master_v3_score_d2}, 'f28_ttcf_448_oscillator_distribution_topping_aggregate_v3_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_448_oscillator_distribution_topping_aggregate_v3_d2}, 'f28_ttcf_449_oscillator_blowoff_decay_master_v3_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_449_oscillator_blowoff_decay_master_v3_d2}, 'f28_ttcf_450_absolute_terminal_oscillator_extended_v3_indicator_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_450_absolute_terminal_oscillator_extended_v3_indicator_d2}}