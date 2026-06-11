"""14_supertrend_psar_chandelier d1 features 001-075 — order-1 difference of corresponding base features.

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

def _supertrend(high, low, close, n=10, mult=3.0):
    """SuperTrend trailing line. Returns (st, dirn) Series — dirn=1 long, -1 short."""
    atr = _atr(high, low, close, n=n)
    hl2 = (high + low) / 2.0
    upper = hl2 + mult * atr
    lower = hl2 - mult * atr
    c = close.values
    u = upper.values
    l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]
                dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]
            dirn[i] = 1
            started = True
            continue
        prev_st = st[i - 1]
        prev_dir = dirn[i - 1]
        if np.isnan(prev_st):
            st[i] = l[i]
            dirn[i] = 1
            continue
        if prev_dir == 1:
            stop = max(prev_st, l[i])
            if c[i] < stop:
                dirn[i] = -1
                st[i] = u[i]
            else:
                dirn[i] = 1
                st[i] = stop
        else:
            stop = min(prev_st, u[i])
            if c[i] > stop:
                dirn[i] = 1
                st[i] = l[i]
            else:
                dirn[i] = -1
                st[i] = stop
    return (pd.Series(st, index=close.index), pd.Series(dirn, index=close.index, dtype='int8'))

def _psar(high, low, af0=0.02, afmax=0.2):
    """Parabolic SAR (Wilder). Returns (sar, dirn) Series — dirn=1 long, -1 short."""
    h = high.values
    l = low.values
    nb = len(h)
    sar = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    if nb == 0:
        return (pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype='int8'))
    start = 0
    while start < nb and (np.isnan(h[start]) or np.isnan(l[start])):
        start += 1
    if start >= nb - 1:
        return (pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype='int8'))
    sar[start] = l[start]
    dirn[start] = 1
    ep = h[start]
    af = af0
    for i in range(start + 1, nb):
        if np.isnan(h[i]) or np.isnan(l[i]):
            sar[i] = sar[i - 1]
            dirn[i] = dirn[i - 1]
            continue
        prev_sar = sar[i - 1]
        prev_dir = dirn[i - 1]
        new_sar = prev_sar + af * (ep - prev_sar)
        if prev_dir == 1:
            lo_prev1 = l[i - 1] if not np.isnan(l[i - 1]) else new_sar
            lo_prev2 = l[i - 2] if i >= 2 and (not np.isnan(l[i - 2])) else lo_prev1
            new_sar = min(new_sar, lo_prev1, lo_prev2)
            if l[i] < new_sar:
                dirn[i] = -1
                sar[i] = ep
                ep = l[i]
                af = af0
            else:
                dirn[i] = 1
                sar[i] = new_sar
                if h[i] > ep:
                    ep = h[i]
                    af = min(af + af0, afmax)
        else:
            hi_prev1 = h[i - 1] if not np.isnan(h[i - 1]) else new_sar
            hi_prev2 = h[i - 2] if i >= 2 and (not np.isnan(h[i - 2])) else hi_prev1
            new_sar = max(new_sar, hi_prev1, hi_prev2)
            if h[i] > new_sar:
                dirn[i] = 1
                sar[i] = ep
                ep = h[i]
                af = af0
            else:
                dirn[i] = -1
                sar[i] = new_sar
                if l[i] < ep:
                    ep = l[i]
                    af = min(af + af0, afmax)
    return (pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype='int8'))

def _chandelier_long(high, low, close, n=22, mult=3.0):
    """Chandelier long stop = highest_high(n) - mult * ATR(n)."""
    atr = _atr(high, low, close, n=n)
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return hh - mult * atr

def _chandelier_short(high, low, close, n=22, mult=3.0):
    """Chandelier short stop = lowest_low(n) + mult * ATR(n)."""
    atr = _atr(high, low, close, n=n)
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return ll + mult * atr

def _bars_since_true(mask: pd.Series) -> pd.Series:
    """Bars since the most recent True in mask (NaN until first True)."""
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

def _streak_true(mask: pd.Series) -> pd.Series:
    """Current run length of consecutive True values ending at each bar."""
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        if arr[i]:
            run += 1
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=mask.index)

def _wma(s, n):
    """Weighted moving average (linear weights). Uses partial-window weights when window not yet full."""
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
    """Hull Moving Average = WMA(2*WMA(close, n/2) - WMA(close, n), sqrt(n))."""
    half = max(int(n // 2), 2)
    rt = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(close, half) - _wma(close, n), rt)

def _kama(close, n=10, fast=2, slow=30):
    """Kaufman's Adaptive Moving Average."""
    chg = (close - close.shift(n)).abs()
    vol = close.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(chg, vol)
    fast_sc = 2.0 / (fast + 1)
    slow_sc = 2.0 / (slow + 1)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    arr = close.values
    sca = sc.values
    nb = len(arr)
    out = np.full(nb, np.nan)
    started = False
    for i in range(nb):
        if np.isnan(arr[i]):
            continue
        if not started:
            out[i] = arr[i]
            started = True
            continue
        prev = out[i - 1]
        if np.isnan(prev) or np.isnan(sca[i]):
            out[i] = arr[i]
        else:
            out[i] = prev + sca[i] * (arr[i] - prev)
    return pd.Series(out, index=close.index)

def _atr_trail_stop(high, low, close, n=21, mult=3.0):
    """ATR trailing stop (Wilder, close-anchored). Returns (stop, dirn)."""
    atr = _atr(high, low, close, n=n)
    c = close.values
    a = atr.values
    nb = len(c)
    stop = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(c[i]) or np.isnan(a[i]):
            if i > 0:
                stop[i] = stop[i - 1]
                dirn[i] = dirn[i - 1]
            continue
        cu = c[i] - mult * a[i]
        cd = c[i] + mult * a[i]
        if not started:
            stop[i] = cu
            dirn[i] = 1
            started = True
            continue
        ps = stop[i - 1]
        pd_ = dirn[i - 1]
        if np.isnan(ps):
            stop[i] = cu
            dirn[i] = 1
            continue
        if pd_ == 1:
            ns = max(ps, cu)
            if c[i] < ns:
                dirn[i] = -1
                stop[i] = cd
            else:
                dirn[i] = 1
                stop[i] = ns
        else:
            ns = min(ps, cd)
            if c[i] > ns:
                dirn[i] = 1
                stop[i] = cu
            else:
                dirn[i] = -1
                stop[i] = ns
    return (pd.Series(stop, index=close.index), pd.Series(dirn, index=close.index, dtype='int8'))

def _chande_kroll_stop(high, low, close, p=10, q=20, x=1.0):
    """Chande-Kroll stop. Returns (long_stop, short_stop)."""
    atr = _atr(high, low, close, n=p)
    mp = max(p // 3, 2)
    mq = max(q // 3, 2)
    h_stop = (high.rolling(p, min_periods=mp).max() - x * atr).rolling(q, min_periods=mq).max()
    l_stop = (low.rolling(p, min_periods=mp).min() + x * atr).rolling(q, min_periods=mq).min()
    return (h_stop, l_stop)

def _hilo_activator(high, low, n=3):
    """HiLo Activator (Krausz): SMA-of-high/SMA-of-low trailing stop. Returns (stop, dirn)."""
    mp = max(n // 3, 2)
    mh = high.rolling(n, min_periods=mp).mean()
    ml = low.rolling(n, min_periods=mp).mean()
    c = ((high + low) / 2.0).values
    mhv = mh.values
    mlv = ml.values
    nb = len(c)
    stop = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    for i in range(nb):
        if np.isnan(c[i]) or np.isnan(mhv[i]) or np.isnan(mlv[i]):
            if i > 0:
                stop[i] = stop[i - 1]
                dirn[i] = dirn[i - 1]
            continue
        if i == 0 or dirn[i - 1] == 0:
            stop[i] = mlv[i]
            dirn[i] = 1
            continue
        if dirn[i - 1] == 1:
            if c[i] < mlv[i]:
                dirn[i] = -1
                stop[i] = mhv[i]
            else:
                dirn[i] = 1
                stop[i] = mlv[i]
        elif c[i] > mhv[i]:
            dirn[i] = 1
            stop[i] = mlv[i]
        else:
            dirn[i] = -1
            stop[i] = mhv[i]
    return (pd.Series(stop, index=high.index), pd.Series(dirn, index=high.index, dtype='int8'))

def _percent_trail_stop(close, pct):
    """Percent trailing stop (fixed pct below running max close). Returns (stop, dirn)."""
    arr = close.values
    nb = len(arr)
    stop = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    peak = np.nan
    started = False
    for i in range(nb):
        if np.isnan(arr[i]):
            if i > 0:
                stop[i] = stop[i - 1]
                dirn[i] = dirn[i - 1]
            continue
        if not started:
            peak = arr[i]
            stop[i] = peak * (1 - pct)
            dirn[i] = 1
            started = True
            continue
        pd_ = dirn[i - 1]
        if pd_ == 1:
            peak = max(peak, arr[i])
            ns = peak * (1 - pct)
            if arr[i] < ns:
                dirn[i] = -1
                peak = arr[i]
                stop[i] = peak * (1 + pct)
            else:
                dirn[i] = 1
                stop[i] = ns
        else:
            peak = min(peak, arr[i])
            ns = peak * (1 + pct)
            if arr[i] > ns:
                dirn[i] = 1
                peak = arr[i]
                stop[i] = peak * (1 - pct)
            else:
                dirn[i] = -1
                stop[i] = ns
    return (pd.Series(stop, index=close.index), pd.Series(dirn, index=close.index, dtype='int8'))

def f14_stps_001_log_dist_close_to_supertrend_10_3_d1(high, low, close):
    """Log distance close above SuperTrend(10, 3) — short-term trailing-stop extension."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return (_safe_log(close) - _safe_log(st)).diff()

def f14_stps_002_log_dist_close_to_supertrend_7_2_d1(high, low, close):
    """Log distance close above SuperTrend(7, 2) — fast trailing-stop extension."""
    st, _ = _supertrend(high, low, close, n=7, mult=2.0)
    return (_safe_log(close) - _safe_log(st)).diff()

def f14_stps_003_log_dist_close_to_supertrend_21_4_d1(high, low, close):
    """Log distance close above SuperTrend(21, 4) — medium-term trailing-stop extension."""
    st, _ = _supertrend(high, low, close, n=21, mult=4.0)
    return (_safe_log(close) - _safe_log(st)).diff()

def f14_stps_004_log_dist_close_to_supertrend_50_3_d1(high, low, close):
    """Log distance close above SuperTrend(50, 3) — long-term trailing-stop extension."""
    st, _ = _supertrend(high, low, close, n=50, mult=3.0)
    return (_safe_log(close) - _safe_log(st)).diff()

def f14_stps_005_atr_dist_close_to_supertrend_10_3_d1(high, low, close):
    """(close − SuperTrend(10,3)) / ATR(21) — ATR-normalized fast-stop extension."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _safe_div(close - st, _atr(high, low, close, n=MDAYS)).diff()

def f14_stps_006_atr_dist_close_to_supertrend_50_3_d1(high, low, close):
    """(close − SuperTrend(50,3)) / ATR(63) — ATR-normalized slow-stop extension."""
    st, _ = _supertrend(high, low, close, n=50, mult=3.0)
    return _safe_div(close - st, _atr(high, low, close, n=QDAYS)).diff()

def f14_stps_007_sigma_dist_close_to_supertrend_21_3_d1(high, low, close):
    """(close − SuperTrend(21,3)) z-scored by 63d return std of close."""
    st, _ = _supertrend(high, low, close, n=21, mult=3.0)
    ret_std = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div((close - st) / close, ret_std).diff()

def f14_stps_008_pct_dist_close_to_supertrend_10_3_d1(high, low, close):
    """Percent distance close above SuperTrend(10, 3)."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _safe_div(close - st, st).diff()

def f14_stps_009_pct_dist_close_to_supertrend_50_4_d1(high, low, close):
    """Percent distance close above SuperTrend(50, 4) — wide-band long-term stop."""
    st, _ = _supertrend(high, low, close, n=50, mult=4.0)
    return _safe_div(close - st, st).diff()

def f14_stps_010_ratio_fast_slow_supertrend_extension_d1(high, low, close):
    """Ratio of (close − ST(10,3)) to (close − ST(50,3)) — fast-vs-slow stop extension."""
    fast, _ = _supertrend(high, low, close, n=10, mult=3.0)
    slow, _ = _supertrend(high, low, close, n=50, mult=3.0)
    return _safe_div(close - fast, close - slow).diff()

def f14_stps_011_max_dist_above_supertrend_10_3_in_21d_d1(high, low, close):
    """Max log distance close above SuperTrend(10,3) over trailing 21d — peak extension."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    d = _safe_log(close) - _safe_log(st)
    return d.rolling(MDAYS, min_periods=WDAYS).max().diff()

def f14_stps_012_cum_atr_room_above_st_10_3_63d_d1(high, low, close):
    """Cumulative ATR-normalized room above SuperTrend(10,3) over trailing 63d."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    r = _safe_div(close - st, atr).clip(lower=0)
    return r.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f14_stps_013_zscore_st_10_3_dist_in_252d_d1(high, low, close):
    """Z-score of (close − SuperTrend(10,3))/close in 252d window."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    raw = _safe_div(close - st, close)
    return _rolling_zscore(raw, YDAYS).diff()

def f14_stps_014_zscore_st_50_3_dist_in_504d_d1(high, low, close):
    """Z-score of (close − SuperTrend(50,3))/close in 504d window — multi-year scale."""
    st, _ = _supertrend(high, low, close, n=50, mult=3.0)
    raw = _safe_div(close - st, close)
    return _rolling_zscore(raw, DDAYS_2Y).diff()

def f14_stps_015_pctile_rank_st_10_3_dist_in_252d_d1(high, low, close):
    """Empirical percentile rank of (close − ST(10,3))/close in 252d distribution."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    raw = _safe_div(close - st, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f14_stps_016_flips_st_10_3_in_21d_d1(high, low, close):
    """Count of SuperTrend(10,3) direction flips in trailing 21d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f14_stps_017_flips_st_10_3_in_63d_d1(high, low, close):
    """Count of SuperTrend(10,3) direction flips in trailing 63d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f14_stps_018_flips_st_50_3_in_252d_d1(high, low, close):
    """Count of SuperTrend(50,3) direction flips in trailing 252d — slow-system regime turnover."""
    _, d = _supertrend(high, low, close, n=50, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f14_stps_019_bars_since_st_10_3_down_flip_d1(high, low, close):
    """Bars since most recent SuperTrend(10,3) down-flip (long→short)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    return _bars_since_true(down).diff()

def f14_stps_020_bars_since_st_10_3_up_flip_d1(high, low, close):
    """Bars since most recent SuperTrend(10,3) up-flip (short→long)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    return _bars_since_true(up).diff()

def f14_stps_021_bars_since_st_50_3_any_flip_d1(high, low, close):
    """Bars since any SuperTrend(50,3) flip."""
    _, d = _supertrend(high, low, close, n=50, mult=3.0)
    any_flip = (d.diff().abs() > 0).astype(bool)
    return _bars_since_true(any_flip).diff()

def f14_stps_022_st_10_3_flip_asymmetry_252d_d1(high, low, close):
    """(down-flips − up-flips) / (down-flips + up-flips) of ST(10,3) in 252d — flip-direction asymmetry."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((d == -1) & (d.shift(1) == 1)).astype(float)
    up = ((d == 1) & (d.shift(1) == -1)).astype(float)
    nd = down.rolling(YDAYS, min_periods=QDAYS).sum()
    nu = up.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(nd - nu, nd + nu).diff()

def f14_stps_023_kama_efficiency_ratio_21d_d1(close):
    """Kaufman Efficiency Ratio over 21d: |Δclose_21d| / Σ|Δclose|_21d — trend efficiency [0,1]."""
    chg = (close - close.shift(MDAYS)).abs()
    vol = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(chg, vol).diff()

def f14_stps_024_std_bars_between_st_10_3_flips_252d_d1(high, low, close):
    """Std of inter-flip spacings of ST(10,3) in trailing 252d — irregularity proxy."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool)

    def _std_gaps(w):
        idx = np.flatnonzero(w)
        if idx.size < 3:
            return np.nan
        gaps = np.diff(idx)
        return float(gaps.std()) if gaps.size else np.nan
    return flip.rolling(YDAYS, min_periods=QDAYS).apply(_std_gaps, raw=True).diff()

def f14_stps_025_longest_long_state_streak_st_10_3_252d_d1(high, low, close):
    """Longest consecutive-long-state run of ST(10,3) in trailing 252d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_mask = (d == 1).astype(float)

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
    return long_mask.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True).diff()

def f14_stps_026_current_long_state_duration_st_10_3_d1(high, low, close):
    """Current ST(10,3) long-state duration (bars since latest up-flip if currently long, else 0)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_mask = d == 1
    return _streak_true(long_mask).diff()

def f14_stps_027_flips_st_7_2_in_21d_d1(high, low, close):
    """Count of fast SuperTrend(7,2) flips in 21d — fast-system flip frequency."""
    _, d = _supertrend(high, low, close, n=7, mult=2.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f14_stps_028_log_dist_close_to_hma_50_d1(close):
    """Log distance close above Hull Moving Average(50) — fast-trail trend reference."""
    return (_safe_log(close) - _safe_log(_hma(close, 50))).diff()

def f14_stps_029_kama_efficiency_ratio_21d_zscore_252d_d1(close):
    """Z-score of 21d KAMA Efficiency Ratio in trailing 252d — trend-efficiency anomaly vs history."""
    chg = (close - close.shift(MDAYS)).abs()
    vol = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    er = _safe_div(chg, vol)
    return _rolling_zscore(er, YDAYS).diff()

def f14_stps_030_bars_since_st_10_3_stop_catch_up_event_d1(high, low, close):
    """Bars since most recent ST(10,3) "catch-up" (|close − ST| < 0.5×ATR(21)) — undisturbed extension = no catch-up = blowoff."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    catch = ((close - st).abs() < 0.5 * atr) & atr.notna() & st.notna()
    return _bars_since_true(catch.astype(bool)).diff()

def f14_stps_031_signed_bars_since_last_st_10_3_up_flip_d1(high, low, close):
    """Bars-since-last-ST(10,3)-up-flip multiplied by current direction (signed maturity)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    return (bsu * d.astype(float)).diff()

def f14_stps_032_log_return_since_last_st_10_3_up_flip_d1(high, low, close):
    """Log return of close since most recent ST(10,3) up-flip (NaN if no prior up-flip)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    arr = close.values
    n = len(arr)
    out = np.full(n, np.nan)
    bs = bsu.values
    for i in range(n):
        if np.isnan(bs[i]):
            continue
        j = i - int(bs[i])
        if 0 <= j < n and (not np.isnan(arr[j])) and (arr[j] > 0) and (not np.isnan(arr[i])) and (arr[i] > 0):
            out[i] = np.log(arr[i]) - np.log(arr[j])
    return pd.Series(out, index=close.index).diff()

def f14_stps_033_log_return_since_last_st_10_3_down_flip_d1(high, low, close):
    """Log return of close since most recent ST(10,3) down-flip."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    dn = ((d == -1) & (d.shift(1) == 1)).astype(bool)
    bsd = _bars_since_true(dn)
    arr = close.values
    n = len(arr)
    out = np.full(n, np.nan)
    bs = bsd.values
    for i in range(n):
        if np.isnan(bs[i]):
            continue
        j = i - int(bs[i])
        if 0 <= j < n and (not np.isnan(arr[j])) and (arr[j] > 0) and (not np.isnan(arr[i])) and (arr[i] > 0):
            out[i] = np.log(arr[i]) - np.log(arr[j])
    return pd.Series(out, index=close.index).diff()

def f14_stps_034_atr_run_since_last_st_10_3_up_flip_d1(high, low, close):
    """(close − close_at_up_flip) / ATR(21) — ATR-normalized run-up since latest ST(10,3) up-flip."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    arr = close.values
    n = len(arr)
    out = np.full(n, np.nan)
    bs = bsu.values
    for i in range(n):
        if np.isnan(bs[i]):
            continue
        j = i - int(bs[i])
        if 0 <= j < n and (not np.isnan(arr[j])) and (not np.isnan(arr[i])):
            out[i] = arr[i] - arr[j]
    raw = pd.Series(out, index=close.index)
    return _safe_div(raw, _atr(high, low, close, n=MDAYS)).diff()

def f14_stps_035_max_drawdown_vs_st_10_3_since_up_flip_d1(high, low, close):
    """Max drawdown of low vs ST(10,3) line since most recent up-flip — closest stop-approach in current long."""
    st, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    gap = _safe_div(low - st, low)
    bs = bsu.values
    g = gap.values
    n = len(g)
    out = np.full(n, np.nan)
    cur_min = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_min = np.nan
            if not np.isnan(g[i]):
                cur_min = g[i] if np.isnan(cur_min) else min(cur_min, g[i])
            out[i] = cur_min
    return pd.Series(out, index=close.index).diff()

def f14_stps_036_max_excursion_above_st_50_3_since_up_flip_d1(high, low, close):
    """Max excursion of high above ST(50,3) since most recent ST(50,3) up-flip — long-extended magnitude."""
    st, d = _supertrend(high, low, close, n=50, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    gap = _safe_div(high - st, st)
    bs = bsu.values
    g = gap.values
    n = len(g)
    out = np.full(n, np.nan)
    cur_max = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_max = np.nan
            if not np.isnan(g[i]):
                cur_max = g[i] if np.isnan(cur_max) else max(cur_max, g[i])
            out[i] = cur_max
    return pd.Series(out, index=close.index).diff()

def f14_stps_037_parabolic_exponent_fit_close_63d_d1(close):
    """Parabolic exponent k from log-linear fit log(close) ~ k·log(t) over 63d — k>1 parabolic; k>>1 blowoff."""

    def _fit_k(w):
        if not np.isfinite(w).all() or len(w) < 30 or (w <= 0).any():
            return np.nan
        y = np.log(w)
        x = np.log(np.arange(1, len(w) + 1, dtype=float))
        xm = x.mean()
        ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_fit_k, raw=True).diff()

def f14_stps_038_timewt_mean_dist_close_to_st_10_3_since_up_flip_d1(high, low, close):
    """Time-weighted mean log distance close-to-ST(10,3) since most recent up-flip."""
    st, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    dist = _safe_log(close) - _safe_log(st)
    bs = bsu.values
    v = dist.values
    n = len(v)
    out = np.full(n, np.nan)
    cur_sum = 0.0
    cur_n = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0.0
                cur_n = 0
            if not np.isnan(v[i]):
                cur_sum += v[i]
                cur_n += 1
            out[i] = cur_sum / cur_n if cur_n > 0 else np.nan
    return pd.Series(out, index=close.index).diff()

def f14_stps_039_drawdown_to_stop_ratio_st_10_3_d1(high, low, close):
    """Current (close − ST(10,3)) divided by max (close − ST(10,3)) in current long-state."""
    st, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    gap = close - st
    bs = bsu.values
    g = gap.values
    n = len(g)
    out = np.full(n, np.nan)
    cur_max = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_max = np.nan
            if not np.isnan(g[i]):
                cur_max = g[i] if np.isnan(cur_max) else max(cur_max, g[i])
            if cur_max is not None and (not np.isnan(cur_max)) and (cur_max != 0):
                out[i] = g[i] / cur_max
    return pd.Series(out, index=close.index).diff()

def f14_stps_040_run_ratio_current_vs_prior_long_state_st_10_3_d1(high, low, close):
    """Ratio of current long-state's max-run to the most recently completed long-state's max-run."""
    st, d = _supertrend(high, low, close, n=10, mult=3.0)
    arr_close = close.values
    arr_d = d.values
    n = len(arr_d)
    out = np.full(n, np.nan)
    state_start = -1
    state_max = np.nan
    last_completed_max = np.nan
    last_dir = 0
    for i in range(n):
        if arr_d[i] == 1 and last_dir != 1:
            state_start = i
            state_max = arr_close[i]
        elif arr_d[i] == 1:
            if not np.isnan(state_max) and (not np.isnan(arr_close[i])):
                state_max = max(state_max, arr_close[i])
        elif arr_d[i] != 1 and last_dir == 1:
            last_completed_max = state_max - arr_close[state_start] if state_start >= 0 else np.nan
            state_start = -1
            state_max = np.nan
        if arr_d[i] == 1 and state_start >= 0 and (not np.isnan(state_max)):
            cur_run = state_max - arr_close[state_start]
            if not np.isnan(last_completed_max) and last_completed_max != 0:
                out[i] = cur_run / last_completed_max
        last_dir = arr_d[i]
    return pd.Series(out, index=close.index).diff()

def f14_stps_041_new_21d_highs_since_st_10_3_up_flip_d1(high, low, close):
    """Count of new 21d-high prints since most recent ST(10,3) up-flip."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_new = (high >= rmax).astype(float)
    bs = bsu.values
    h = is_new.values
    n = len(h)
    out = np.full(n, np.nan)
    cur_sum = 0.0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0.0
            if not np.isnan(h[i]):
                cur_sum += h[i]
            out[i] = cur_sum
    return pd.Series(out, index=close.index).diff()

def f14_stps_042_green_bar_fraction_since_st_10_3_up_flip_d1(open, high, low, close):
    """Fraction of green (close > open) bars since most recent ST(10,3) up-flip."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    green = (close > open).astype(float)
    bs = bsu.values
    g = green.values
    n = len(g)
    out = np.full(n, np.nan)
    cur_sum = 0.0
    cur_n = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0.0
                cur_n = 0
            cur_sum += g[i]
            cur_n += 1
            out[i] = cur_sum / cur_n if cur_n > 0 else np.nan
    return pd.Series(out, index=close.index).diff()

def f14_stps_043_cum_volume_since_st_10_3_up_flip_norm_63d_avg_d1(high, low, close, volume):
    """Cumulative volume since latest ST(10,3) up-flip, normalized to 63d average volume."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    vavg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    v = volume.values
    bs = bsu.values
    va = vavg.values
    n = len(v)
    out = np.full(n, np.nan)
    cur_sum = 0.0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0.0
            if not np.isnan(v[i]):
                cur_sum += v[i]
            if not np.isnan(va[i]) and va[i] > 0:
                out[i] = cur_sum / va[i]
    return pd.Series(out, index=close.index).diff()

def f14_stps_044_log_dist_close_to_kama_10_2_30_d1(close):
    """Log distance close above Kaufman Adaptive MA (KAMA 10/2/30) — adaptive-trail reference."""
    return (_safe_log(close) - _safe_log(_kama(close, 10, 2, 30))).diff()

def f14_stps_045_indicator_long_state_above_p95_st_10_3_d1(high, low, close):
    """Indicator: current ST(10,3) long-state duration exceeds 95th-percentile of historical long-state durations."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_run = _streak_true(d == 1)
    p95 = long_run.expanding(min_periods=YDAYS).quantile(0.95)
    return ((long_run > p95) & p95.notna()).astype(float).diff()

def f14_stps_046_ratio_current_long_state_to_median_252d_d1(high, low, close):
    """Current ST(10,3) long-state duration / median historical long-state duration in 252d-of-streaks window."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_run = _streak_true(d == 1)
    med = long_run.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(long_run, med).diff()

def f14_stps_047_pctile_rank_current_long_state_st_10_3_d1(high, low, close):
    """Empirical percentile rank of current ST(10,3) long-state duration in trailing-252d distribution."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_run = _streak_true(d == 1)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return long_run.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f14_stps_048_hazard_inverse_median_flip_spacing_st_10_3_d1(high, low, close):
    """Implied next-flip hazard: 1 / median bars-between-flips in trailing 252d."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(bool)

    def _med_gap(w):
        idx = np.flatnonzero(w)
        if idx.size < 3:
            return np.nan
        return float(np.median(np.diff(idx)))
    med = flip.rolling(YDAYS, min_periods=QDAYS).apply(_med_gap, raw=True)
    return _safe_div(1.0, med).diff()

def f14_stps_049_ratio_current_long_state_to_longest_ever_st_10_3_d1(high, low, close):
    """Current ST(10,3) long-state duration / expanding longest-ever long-state duration."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_run = _streak_true(d == 1)
    longest_ever = long_run.expanding(min_periods=1).max()
    return _safe_div(long_run, longest_ever).diff()

def f14_stps_050_hma_20_slope_21d_norm_close_d1(close):
    """Slope of Hull-MA(20) over 21d, normalized by close — HMA reverses early at tops (low lag)."""
    return _safe_div(_rolling_slope(_hma(close, 20), MDAYS), close).diff()

def f14_stps_051_indicator_long_state_st_10_3_over_126_bars_d1(high, low, close):
    """Indicator: current ST(10,3) long-state has lasted > 126 bars (stale long)."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_run = _streak_true(d == 1)
    return (long_run > 126).astype(float).diff()

def f14_stps_052_count_systems_long_over_63bars_d1(high, low, close):
    """Count of ST systems (7/2, 10/3, 21/4, 50/3) currently in long-state >63 bars."""
    _, d1 = _supertrend(high, low, close, n=7, mult=2.0)
    _, d2 = _supertrend(high, low, close, n=10, mult=3.0)
    _, d3 = _supertrend(high, low, close, n=21, mult=4.0)
    _, d4 = _supertrend(high, low, close, n=50, mult=3.0)
    r1 = (_streak_true(d1 == 1) > QDAYS).astype(float)
    r2 = (_streak_true(d2 == 1) > QDAYS).astype(float)
    r3 = (_streak_true(d3 == 1) > QDAYS).astype(float)
    r4 = (_streak_true(d4 == 1) > QDAYS).astype(float)
    return (r1 + r2 + r3 + r4).diff()

def f14_stps_053_signed_staleness_st_10_3_d1(high, low, close):
    """Direction × current-state-duration of ST(10,3) — signed regime maturity."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    long_dur = _streak_true(d == 1)
    short_dur = _streak_true(d == -1)
    return (long_dur - short_dur).diff()

def f14_stps_054_bars_since_st_10_3_aligned_new_252d_high_d1(high, low, close):
    """Bars since last bar where ST(10,3) was long AND high == trailing-252d-max — 'aligned new high'."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    mask = ((d == 1) & (high >= rmax)).astype(bool)
    return _bars_since_true(mask).diff()

def f14_stps_055_annualized_flip_rate_st_10_3_252d_d1(high, low, close):
    """Annualized flip rate: ST(10,3) flip-count in trailing 252d × (252/252) — flips per year."""
    _, d = _supertrend(high, low, close, n=10, mult=3.0)
    flip = (d.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f14_stps_056_log_dist_close_to_psar_default_d1(high, low, close):
    """Log distance close above PSAR(0.02, 0.2)."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return (_safe_log(close) - _safe_log(sar)).diff()

def f14_stps_057_atr_dist_close_to_psar_default_d1(high, low, close):
    """(close − PSAR(0.02,0.2)) / ATR(21) — ATR-normalized PSAR extension."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return _safe_div(close - sar, _atr(high, low, close, n=MDAYS)).diff()

def f14_stps_058_sigma_dist_close_to_psar_default_63d_d1(high, low, close):
    """(close − PSAR)/close normalized by 63d return std — sigma-scaled extension."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    ret_std = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div((close - sar) / close, ret_std).diff()

def f14_stps_059_pct_dist_close_to_psar_fast_d1(high, low, close):
    """Percent distance close above PSAR(0.04, 0.2) — faster-AF variant (different concept)."""
    sar, _ = _psar(high, low, af0=0.04, afmax=0.2)
    return _safe_div(close - sar, sar).diff()

def f14_stps_060_pct_dist_close_to_psar_slow_d1(high, low, close):
    """Percent distance close above PSAR(0.01, 0.2) — slower-AF variant."""
    sar, _ = _psar(high, low, af0=0.01, afmax=0.2)
    return _safe_div(close - sar, sar).diff()

def f14_stps_061_close_position_in_psar_band_21d_d1(high, low, close):
    """Position of close within [min_PSAR_21d, max_PSAR_21d]."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    lo = sar.rolling(MDAYS, min_periods=WDAYS).min()
    hi = sar.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(close - lo, hi - lo).diff()

def f14_stps_062_close_position_in_psar_band_252d_d1(high, low, close):
    """Position of close within [min_PSAR_252d, max_PSAR_252d] — long-horizon channel position."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    lo = sar.rolling(YDAYS, min_periods=QDAYS).min()
    hi = sar.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(close - lo, hi - lo).diff()

def f14_stps_063_zscore_close_minus_psar_in_252d_d1(high, low, close):
    """Z-score of (close − PSAR)/close in trailing 252d window."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return _rolling_zscore(_safe_div(close - sar, close), YDAYS).diff()

def f14_stps_064_pctile_rank_close_minus_psar_in_252d_d1(high, low, close):
    """Empirical percentile rank of (close − PSAR)/close in 252d distribution."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    raw = _safe_div(close - sar, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f14_stps_065_indicator_close_within_half_atr_of_psar_d1(high, low, close):
    """Indicator: close within 0.5×ATR(21) of PSAR — stop-trip imminent."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    atr = _atr(high, low, close, n=MDAYS)
    return ((close - sar).abs() < 0.5 * atr).astype(float).where(atr.notna() & sar.notna(), np.nan).diff()

def f14_stps_066_psar_flips_in_21d_d1(high, low, close):
    """Count of PSAR(0.02,0.2) flips in trailing 21d."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    flip = (dp.diff().abs() > 0).astype(float)
    return flip.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f14_stps_067_psar_flips_in_63d_d1(high, low, close):
    """Count of PSAR(0.02,0.2) flips in trailing 63d."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    flip = (dp.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f14_stps_068_psar_flips_in_252d_d1(high, low, close):
    """Count of PSAR(0.02,0.2) flips in trailing 252d."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    flip = (dp.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f14_stps_069_bars_since_psar_down_flip_d1(high, low, close):
    """Bars since most recent PSAR(0.02,0.2) down-flip."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    dn = ((dp == -1) & (dp.shift(1) == 1)).astype(bool)
    return _bars_since_true(dn).diff()

def f14_stps_070_atr_dist_close_to_atr_trail_stop_21_3_d1(high, low, close):
    """(close − Wilder ATR-trail-stop(21,3)) / ATR(21) — close-anchored ATR-trail extension (distinct from Chandelier high-anchored)."""
    st, _ = _atr_trail_stop(high, low, close, n=21, mult=3.0)
    return _safe_div(close - st, _atr(high, low, close, n=MDAYS)).diff()

def f14_stps_071_std_bars_between_psar_flips_252d_d1(high, low, close):
    """Std of PSAR(0.02,0.2) inter-flip spacings in trailing 252d — irregularity."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    flip = (dp.diff().abs() > 0).astype(bool)

    def _std_gaps(w):
        idx = np.flatnonzero(w)
        if idx.size < 3:
            return np.nan
        gaps = np.diff(idx)
        return float(gaps.std()) if gaps.size else np.nan
    return flip.rolling(YDAYS, min_periods=QDAYS).apply(_std_gaps, raw=True).diff()

def f14_stps_072_ratio_long_to_short_state_duration_psar_252d_d1(high, low, close):
    """Total long-state bars / total short-state bars of PSAR(0.02,0.2) in 252d."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    long_b = (dp == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    short_b = (dp == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(long_b, short_b).diff()

def f14_stps_073_longest_psar_long_streak_252d_d1(high, low, close):
    """Longest PSAR(0.02,0.2) consecutive-long streak in trailing 252d."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    long_mask = (dp == 1).astype(float)

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
    return long_mask.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True).diff()

def f14_stps_074_current_psar_state_duration_d1(high, low, close):
    """Current PSAR(0.02,0.2) state duration (positive when long, negative when short)."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    long_dur = _streak_true(dp == 1)
    short_dur = _streak_true(dp == -1)
    return (long_dur - short_dur).diff()

def f14_stps_075_psar_flips_at_extreme_range_position_d1(high, low, close):
    """PSAR flip-count(21d) × close-position-in-252d-range — regime change at range extremes."""
    _, dp = _psar(high, low, af0=0.02, afmax=0.2)
    flip = (dp.diff().abs() > 0).astype(float)
    fcount = flip.rolling(MDAYS, min_periods=WDAYS).sum()
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return (fcount * pos).diff()
SUPERTREND_PSAR_CHANDELIER_D1_REGISTRY_001_075 = {'f14_stps_001_log_dist_close_to_supertrend_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_001_log_dist_close_to_supertrend_10_3_d1}, 'f14_stps_002_log_dist_close_to_supertrend_7_2_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_002_log_dist_close_to_supertrend_7_2_d1}, 'f14_stps_003_log_dist_close_to_supertrend_21_4_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_003_log_dist_close_to_supertrend_21_4_d1}, 'f14_stps_004_log_dist_close_to_supertrend_50_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_004_log_dist_close_to_supertrend_50_3_d1}, 'f14_stps_005_atr_dist_close_to_supertrend_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_005_atr_dist_close_to_supertrend_10_3_d1}, 'f14_stps_006_atr_dist_close_to_supertrend_50_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_006_atr_dist_close_to_supertrend_50_3_d1}, 'f14_stps_007_sigma_dist_close_to_supertrend_21_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_007_sigma_dist_close_to_supertrend_21_3_d1}, 'f14_stps_008_pct_dist_close_to_supertrend_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_008_pct_dist_close_to_supertrend_10_3_d1}, 'f14_stps_009_pct_dist_close_to_supertrend_50_4_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_009_pct_dist_close_to_supertrend_50_4_d1}, 'f14_stps_010_ratio_fast_slow_supertrend_extension_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_010_ratio_fast_slow_supertrend_extension_d1}, 'f14_stps_011_max_dist_above_supertrend_10_3_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_011_max_dist_above_supertrend_10_3_in_21d_d1}, 'f14_stps_012_cum_atr_room_above_st_10_3_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_012_cum_atr_room_above_st_10_3_63d_d1}, 'f14_stps_013_zscore_st_10_3_dist_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_013_zscore_st_10_3_dist_in_252d_d1}, 'f14_stps_014_zscore_st_50_3_dist_in_504d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_014_zscore_st_50_3_dist_in_504d_d1}, 'f14_stps_015_pctile_rank_st_10_3_dist_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_015_pctile_rank_st_10_3_dist_in_252d_d1}, 'f14_stps_016_flips_st_10_3_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_016_flips_st_10_3_in_21d_d1}, 'f14_stps_017_flips_st_10_3_in_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_017_flips_st_10_3_in_63d_d1}, 'f14_stps_018_flips_st_50_3_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_018_flips_st_50_3_in_252d_d1}, 'f14_stps_019_bars_since_st_10_3_down_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_019_bars_since_st_10_3_down_flip_d1}, 'f14_stps_020_bars_since_st_10_3_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_020_bars_since_st_10_3_up_flip_d1}, 'f14_stps_021_bars_since_st_50_3_any_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_021_bars_since_st_50_3_any_flip_d1}, 'f14_stps_022_st_10_3_flip_asymmetry_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_022_st_10_3_flip_asymmetry_252d_d1}, 'f14_stps_023_kama_efficiency_ratio_21d_d1': {'inputs': ['close'], 'func': f14_stps_023_kama_efficiency_ratio_21d_d1}, 'f14_stps_024_std_bars_between_st_10_3_flips_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_024_std_bars_between_st_10_3_flips_252d_d1}, 'f14_stps_025_longest_long_state_streak_st_10_3_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_025_longest_long_state_streak_st_10_3_252d_d1}, 'f14_stps_026_current_long_state_duration_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_026_current_long_state_duration_st_10_3_d1}, 'f14_stps_027_flips_st_7_2_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_027_flips_st_7_2_in_21d_d1}, 'f14_stps_028_log_dist_close_to_hma_50_d1': {'inputs': ['close'], 'func': f14_stps_028_log_dist_close_to_hma_50_d1}, 'f14_stps_029_kama_efficiency_ratio_21d_zscore_252d_d1': {'inputs': ['close'], 'func': f14_stps_029_kama_efficiency_ratio_21d_zscore_252d_d1}, 'f14_stps_030_bars_since_st_10_3_stop_catch_up_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_030_bars_since_st_10_3_stop_catch_up_event_d1}, 'f14_stps_031_signed_bars_since_last_st_10_3_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_031_signed_bars_since_last_st_10_3_up_flip_d1}, 'f14_stps_032_log_return_since_last_st_10_3_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_032_log_return_since_last_st_10_3_up_flip_d1}, 'f14_stps_033_log_return_since_last_st_10_3_down_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_033_log_return_since_last_st_10_3_down_flip_d1}, 'f14_stps_034_atr_run_since_last_st_10_3_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_034_atr_run_since_last_st_10_3_up_flip_d1}, 'f14_stps_035_max_drawdown_vs_st_10_3_since_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_035_max_drawdown_vs_st_10_3_since_up_flip_d1}, 'f14_stps_036_max_excursion_above_st_50_3_since_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_036_max_excursion_above_st_50_3_since_up_flip_d1}, 'f14_stps_037_parabolic_exponent_fit_close_63d_d1': {'inputs': ['close'], 'func': f14_stps_037_parabolic_exponent_fit_close_63d_d1}, 'f14_stps_038_timewt_mean_dist_close_to_st_10_3_since_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_038_timewt_mean_dist_close_to_st_10_3_since_up_flip_d1}, 'f14_stps_039_drawdown_to_stop_ratio_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_039_drawdown_to_stop_ratio_st_10_3_d1}, 'f14_stps_040_run_ratio_current_vs_prior_long_state_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_040_run_ratio_current_vs_prior_long_state_st_10_3_d1}, 'f14_stps_041_new_21d_highs_since_st_10_3_up_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_041_new_21d_highs_since_st_10_3_up_flip_d1}, 'f14_stps_042_green_bar_fraction_since_st_10_3_up_flip_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f14_stps_042_green_bar_fraction_since_st_10_3_up_flip_d1}, 'f14_stps_043_cum_volume_since_st_10_3_up_flip_norm_63d_avg_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f14_stps_043_cum_volume_since_st_10_3_up_flip_norm_63d_avg_d1}, 'f14_stps_044_log_dist_close_to_kama_10_2_30_d1': {'inputs': ['close'], 'func': f14_stps_044_log_dist_close_to_kama_10_2_30_d1}, 'f14_stps_045_indicator_long_state_above_p95_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_045_indicator_long_state_above_p95_st_10_3_d1}, 'f14_stps_046_ratio_current_long_state_to_median_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_046_ratio_current_long_state_to_median_252d_d1}, 'f14_stps_047_pctile_rank_current_long_state_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_047_pctile_rank_current_long_state_st_10_3_d1}, 'f14_stps_048_hazard_inverse_median_flip_spacing_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_048_hazard_inverse_median_flip_spacing_st_10_3_d1}, 'f14_stps_049_ratio_current_long_state_to_longest_ever_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_049_ratio_current_long_state_to_longest_ever_st_10_3_d1}, 'f14_stps_050_hma_20_slope_21d_norm_close_d1': {'inputs': ['close'], 'func': f14_stps_050_hma_20_slope_21d_norm_close_d1}, 'f14_stps_051_indicator_long_state_st_10_3_over_126_bars_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_051_indicator_long_state_st_10_3_over_126_bars_d1}, 'f14_stps_052_count_systems_long_over_63bars_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_052_count_systems_long_over_63bars_d1}, 'f14_stps_053_signed_staleness_st_10_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_053_signed_staleness_st_10_3_d1}, 'f14_stps_054_bars_since_st_10_3_aligned_new_252d_high_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_054_bars_since_st_10_3_aligned_new_252d_high_d1}, 'f14_stps_055_annualized_flip_rate_st_10_3_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_055_annualized_flip_rate_st_10_3_252d_d1}, 'f14_stps_056_log_dist_close_to_psar_default_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_056_log_dist_close_to_psar_default_d1}, 'f14_stps_057_atr_dist_close_to_psar_default_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_057_atr_dist_close_to_psar_default_d1}, 'f14_stps_058_sigma_dist_close_to_psar_default_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_058_sigma_dist_close_to_psar_default_63d_d1}, 'f14_stps_059_pct_dist_close_to_psar_fast_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_059_pct_dist_close_to_psar_fast_d1}, 'f14_stps_060_pct_dist_close_to_psar_slow_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_060_pct_dist_close_to_psar_slow_d1}, 'f14_stps_061_close_position_in_psar_band_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_061_close_position_in_psar_band_21d_d1}, 'f14_stps_062_close_position_in_psar_band_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_062_close_position_in_psar_band_252d_d1}, 'f14_stps_063_zscore_close_minus_psar_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_063_zscore_close_minus_psar_in_252d_d1}, 'f14_stps_064_pctile_rank_close_minus_psar_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_064_pctile_rank_close_minus_psar_in_252d_d1}, 'f14_stps_065_indicator_close_within_half_atr_of_psar_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_065_indicator_close_within_half_atr_of_psar_d1}, 'f14_stps_066_psar_flips_in_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_066_psar_flips_in_21d_d1}, 'f14_stps_067_psar_flips_in_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_067_psar_flips_in_63d_d1}, 'f14_stps_068_psar_flips_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_068_psar_flips_in_252d_d1}, 'f14_stps_069_bars_since_psar_down_flip_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_069_bars_since_psar_down_flip_d1}, 'f14_stps_070_atr_dist_close_to_atr_trail_stop_21_3_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_070_atr_dist_close_to_atr_trail_stop_21_3_d1}, 'f14_stps_071_std_bars_between_psar_flips_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_071_std_bars_between_psar_flips_252d_d1}, 'f14_stps_072_ratio_long_to_short_state_duration_psar_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_072_ratio_long_to_short_state_duration_psar_252d_d1}, 'f14_stps_073_longest_psar_long_streak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_073_longest_psar_long_streak_252d_d1}, 'f14_stps_074_current_psar_state_duration_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_074_current_psar_state_duration_d1}, 'f14_stps_075_psar_flips_at_extreme_range_position_d1': {'inputs': ['high', 'low', 'close'], 'func': f14_stps_075_psar_flips_at_extreme_range_position_d1}}