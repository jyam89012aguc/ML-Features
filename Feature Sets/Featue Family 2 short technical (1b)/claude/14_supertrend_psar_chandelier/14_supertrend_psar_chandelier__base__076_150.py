"""supertrend_psar_chandelier base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the trailing-stop / SuperTrend / PSAR /
Chandelier theme: PSAR AF dynamics, Chandelier distance, breach/recovery,
walking-the-stop, multi-system agreement, implied stop-loss, breakout-to-stop
reversals, composite topping-quality.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# Family-specific helpers (identical to __base__001_075.py).

def _supertrend(high, low, close, n=10, mult=3.0):
    """SuperTrend trailing line. Returns (st, dirn) Series — dirn=1 long, -1 short."""
    atr = _atr(high, low, close, n=n)
    hl2 = (high + low) / 2.0
    upper = hl2 + mult * atr
    lower = hl2 - mult * atr
    c = close.values; u = upper.values; l = lower.values
    nb = len(c)
    st = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
    started = False
    for i in range(nb):
        if np.isnan(u[i]) or np.isnan(l[i]) or np.isnan(c[i]):
            if i > 0:
                st[i] = st[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            st[i] = l[i]; dirn[i] = 1; started = True; continue
        prev_st = st[i - 1]; prev_dir = dirn[i - 1]
        if np.isnan(prev_st):
            st[i] = l[i]; dirn[i] = 1; continue
        if prev_dir == 1:
            stop = max(prev_st, l[i])
            if c[i] < stop:
                dirn[i] = -1; st[i] = u[i]
            else:
                dirn[i] = 1; st[i] = stop
        else:
            stop = min(prev_st, u[i])
            if c[i] > stop:
                dirn[i] = 1; st[i] = l[i]
            else:
                dirn[i] = -1; st[i] = stop
    return pd.Series(st, index=close.index), pd.Series(dirn, index=close.index, dtype="int8")


def _psar(high, low, af0=0.02, afmax=0.2):
    """Parabolic SAR (Wilder). Returns (sar, dirn) Series — dirn=1 long, -1 short."""
    h = high.values; l = low.values
    nb = len(h)
    sar = np.full(nb, np.nan)
    dirn = np.zeros(nb, dtype=np.int8)
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
        prev_sar = sar[i - 1]; prev_dir = dirn[i - 1]
        new_sar = prev_sar + af * (ep - prev_sar)
        if prev_dir == 1:
            lo_prev1 = l[i - 1] if not np.isnan(l[i - 1]) else new_sar
            lo_prev2 = l[i - 2] if i >= 2 and not np.isnan(l[i - 2]) else lo_prev1
            new_sar = min(new_sar, lo_prev1, lo_prev2)
            if l[i] < new_sar:
                dirn[i] = -1; sar[i] = ep; ep = l[i]; af = af0
            else:
                dirn[i] = 1; sar[i] = new_sar
                if h[i] > ep:
                    ep = h[i]; af = min(af + af0, afmax)
        else:
            hi_prev1 = h[i - 1] if not np.isnan(h[i - 1]) else new_sar
            hi_prev2 = h[i - 2] if i >= 2 and not np.isnan(h[i - 2]) else hi_prev1
            new_sar = max(new_sar, hi_prev1, hi_prev2)
            if h[i] > new_sar:
                dirn[i] = 1; sar[i] = ep; ep = h[i]; af = af0
            else:
                dirn[i] = -1; sar[i] = new_sar
                if l[i] < ep:
                    ep = l[i]; af = min(af + af0, afmax)
    return pd.Series(sar, index=high.index), pd.Series(dirn, index=high.index, dtype="int8")


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
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i; out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        run = run + 1 if arr[i] else 0
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
    """Hull MA = WMA(2*WMA(close, n/2) - WMA(close, n), sqrt(n))."""
    half = max(int(n // 2), 2)
    rt = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(close, half) - _wma(close, n), rt)


def _kama(close, n=10, fast=2, slow=30):
    """Kaufman's Adaptive Moving Average."""
    chg = (close - close.shift(n)).abs()
    vol = close.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(chg, vol)
    fast_sc = 2.0 / (fast + 1); slow_sc = 2.0 / (slow + 1)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    arr = close.values; sca = sc.values
    nb = len(arr)
    out = np.full(nb, np.nan)
    started = False
    for i in range(nb):
        if np.isnan(arr[i]):
            continue
        if not started:
            out[i] = arr[i]; started = True; continue
        prev = out[i - 1]
        if np.isnan(prev) or np.isnan(sca[i]):
            out[i] = arr[i]
        else:
            out[i] = prev + sca[i] * (arr[i] - prev)
    return pd.Series(out, index=close.index)


def _atr_trail_stop(high, low, close, n=21, mult=3.0):
    """ATR trailing stop (Wilder, close-anchored). Returns (stop, dirn)."""
    atr = _atr(high, low, close, n=n)
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


def _chande_kroll_stop(high, low, close, p=10, q=20, x=1.0):
    """Chande-Kroll stop. Returns (long_stop, short_stop)."""
    atr = _atr(high, low, close, n=p)
    mp = max(p // 3, 2); mq = max(q // 3, 2)
    h_stop = (high.rolling(p, min_periods=mp).max() - x * atr).rolling(q, min_periods=mq).max()
    l_stop = (low.rolling(p, min_periods=mp).min() + x * atr).rolling(q, min_periods=mq).min()
    return h_stop, l_stop


def _hilo_activator(high, low, n=3):
    """HiLo Activator (Krausz). Returns (stop, dirn)."""
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


def _percent_trail_stop(close, pct):
    """Percent trailing stop (fixed pct below running max close). Returns (stop, dirn)."""
    arr = close.values
    nb = len(arr)
    stop = np.full(nb, np.nan); dirn = np.zeros(nb, dtype=np.int8)
    peak = np.nan; started = False
    for i in range(nb):
        if np.isnan(arr[i]):
            if i > 0:
                stop[i] = stop[i - 1]; dirn[i] = dirn[i - 1]
            continue
        if not started:
            peak = arr[i]; stop[i] = peak * (1 - pct); dirn[i] = 1; started = True; continue
        pd_ = dirn[i - 1]
        if pd_ == 1:
            peak = max(peak, arr[i])
            ns = peak * (1 - pct)
            if arr[i] < ns:
                dirn[i] = -1; peak = arr[i]; stop[i] = peak * (1 + pct)
            else:
                dirn[i] = 1; stop[i] = ns
        else:
            peak = min(peak, arr[i])
            ns = peak * (1 + pct)
            if arr[i] > ns:
                dirn[i] = 1; peak = arr[i]; stop[i] = peak * (1 - pct)
            else:
                dirn[i] = -1; stop[i] = ns
    return pd.Series(stop, index=close.index), pd.Series(dirn, index=close.index, dtype="int8")


# ============================================================
# Bucket G — PSAR acceleration-factor dynamics (076-080)
# ============================================================

def f14_stps_076_psar_step_size_norm_atr(high, low, close):
    """Most recent PSAR step (|sar - sar.prev|) normalized by ATR(21) — implied AF magnitude."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    step = sar.diff().abs()
    return _safe_div(step, _atr(high, low, close, n=MDAYS))


def f14_stps_077_frac_bars_psar_step_at_max_21d(high, low, close):
    """Fraction of bars in 21d where PSAR step ≥ 95th pct of step distribution in 252d — AF-at-max indicator."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    step = sar.diff().abs()
    p95 = step.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    near_max = (step >= p95).astype(float)
    return near_max.rolling(MDAYS, min_periods=WDAYS).mean()


def f14_stps_078_ratio_fast_slow_psar_distance(high, low, close):
    """(close − PSAR_fast(0.04,0.4)) / (close − PSAR_slow(0.01,0.2)) — fast vs slow stop ratio."""
    sf, _ = _psar(high, low, af0=0.04, afmax=0.4)
    ss, _ = _psar(high, low, af0=0.01, afmax=0.2)
    return _safe_div(close - sf, close - ss)


def f14_stps_079_psar_step_change_21d(high, low, close):
    """Change in PSAR step-size: current step − step 21 bars ago, normalized by close."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    step = sar.diff().abs()
    return _safe_div(step - step.shift(MDAYS), close)


def f14_stps_080_log_dist_close_to_30wk_sma(close):
    """Log distance close to 30-week (150d) SMA — Weinstein stage filter (close<SMA = stage 3/4 onset)."""
    return _safe_log(close) - _safe_log(close.rolling(150, min_periods=50).mean())


# ============================================================
# Bucket H — Chandelier-exit distance / extension (081-090)
# ============================================================

def f14_stps_081_log_dist_close_to_chandelier_long_22_3(high, low, close):
    """Log distance close above Chandelier-long(22, 3)."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _safe_log(close) - _safe_log(cl)


def f14_stps_082_atr_dist_close_to_chandelier_long_22_3(high, low, close):
    """(close − Chandelier-long(22,3)) / ATR(22) — ATR-normalized extension above stop."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _safe_div(close - cl, _atr(high, low, close, n=22))


def f14_stps_083_atr_dist_close_to_chandelier_long_50_3(high, low, close):
    """(close − Chandelier-long(50,3)) / ATR(50) — slow-window stop extension."""
    cl = _chandelier_long(high, low, close, n=50, mult=3.0)
    return _safe_div(close - cl, _atr(high, low, close, n=50))


def f14_stps_084_dist_close_to_chandelier_short_22_3(high, low, close):
    """Log distance close above Chandelier-short(22, 3) — distance to short-stop (negative when below)."""
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    return _safe_log(cs) - _safe_log(close)


def f14_stps_085_ratio_long_to_short_chandelier_room(high, low, close):
    """(close − Chandelier-long) / (Chandelier-short − close) — long-stop vs short-stop room asymmetry."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    cs = _chandelier_short(high, low, close, n=22, mult=3.0)
    return _safe_div(close - cl, cs - close)


def f14_stps_086_pct_dist_close_to_chandelier_long_22_3(high, low, close):
    """Percent distance close above Chandelier-long(22, 3)."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _safe_div(close - cl, cl)


def f14_stps_087_sigma_dist_close_to_chandelier_long_22_3_63d(high, low, close):
    """(close − Chandelier-long)/close normalized by 63d return std — sigma-scaled extension."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    ret_std = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div((close - cl) / close, ret_std)


def f14_stps_088_zscore_close_minus_chandelier_long_252d(high, low, close):
    """Z-score of (close − Chandelier-long(22,3))/close in trailing 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _rolling_zscore(_safe_div(close - cl, close), YDAYS)


def f14_stps_089_pctile_rank_close_minus_chandelier_long_252d(high, low, close):
    """Empirical percentile rank of (close − Chandelier-long(22,3))/close in 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    raw = _safe_div(close - cl, close)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f14_stps_090_max_excursion_above_chandelier_long_21d(high, low, close):
    """Max log distance close above Chandelier-long(22,3) over trailing 21d — peak extension."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    d = _safe_log(close) - _safe_log(cl)
    return d.rolling(MDAYS, min_periods=WDAYS).max()


# ============================================================
# Bucket I — Chandelier breach / breach-recovery (091-100)
# ============================================================

def f14_stps_091_chandelier_long_breach_count_63d(high, low, close):
    """Count of intraday breaches (low < Chandelier-long(22,3)) in trailing 63d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = (low < cl).astype(float).where(cl.notna(), np.nan)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_092_chandelier_long_breach_count_252d(high, low, close):
    """Count of intraday breaches (low < Chandelier-long(22,3)) in trailing 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = (low < cl).astype(float).where(cl.notna(), np.nan)
    return breach.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_093_bars_since_chandelier_long_breach(high, low, close):
    """Bars since most recent Chandelier-long(22,3) intraday breach."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _bars_since_true(((low < cl) & cl.notna()).astype(bool))


def f14_stps_094_indicator_recovered_within_5_after_chandelier_breach(high, low, close):
    """Indicator: most recent Chandelier-long breach was followed by close > Chandelier within 5 bars."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = ((low < cl) & cl.notna()).astype(bool)
    bsb = _bars_since_true(breach)
    # if bsb <= 5 and close > cl now, mark 1; otherwise 0 (or NaN if no breach yet)
    cond = (bsb <= 5) & (close > cl)
    return cond.astype(float).where(bsb.notna(), np.nan)


def f14_stps_095_chandelier_breach_then_recover_count_252d(high, low, close):
    """Whipsaw count: bars where low < Chandelier-long AND close > Chandelier-long (same bar), in 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    whip = ((low < cl) & (close > cl)).astype(float).where(cl.notna(), np.nan)
    return whip.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_096_max_consecutive_bars_close_below_chandelier_long_252d(high, low, close):
    """Longest run of consecutive bars with close < Chandelier-long(22,3) in 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    below = (close < cl).astype(float)
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
    return below.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True)


def f14_stps_097_frac_bars_close_below_chandelier_long_63d(high, low, close):
    """Fraction of bars in trailing 63d where close < Chandelier-long(22,3)."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    below = (close < cl).astype(float).where(cl.notna(), np.nan)
    return below.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_098_post_breach_max_drawdown_21d(high, low, close):
    """Max log drawdown of close in 21d after most recent Chandelier-long breach (vs close at breach)."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = ((low < cl) & cl.notna()).astype(bool)
    bsb = _bars_since_true(breach)
    arr = close.values
    bs = bsb.values
    n = len(arr)
    out = np.full(n, np.nan)
    cur_min = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_min = np.nan
            if 0 <= anchor < n and not np.isnan(arr[i]) and not np.isnan(arr[anchor]) and arr[i] > 0 and arr[anchor] > 0:
                r = np.log(arr[i]) - np.log(arr[anchor])
                cur_min = r if np.isnan(cur_min) else min(cur_min, r)
            if bs[i] <= 21:
                out[i] = cur_min
    return pd.Series(out, index=close.index)


def f14_stps_099_false_breach_count_63d(high, low, close):
    """Bars where (low < Chandelier-long AND close > Chandelier-long) — false-breach count in 63d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    fb = ((low < cl) & (close > cl)).astype(float).where(cl.notna(), np.nan)
    return fb.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_100_full_breach_3plus_bars_count_252d(high, low, close):
    """Count of close-below-Chandelier-long runs of ≥3 consecutive bars in 252d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    below = (close < cl).astype(int)
    # Mark the start of each run of consecutive below-bars by where below=1 & below.shift(1)=0
    starts = ((below == 1) & (below.shift(1).fillna(0) == 0)).astype(int)
    # Length of each run measured at the start bar (forward via cumulative trick is not PIT-safe).
    # Instead: at each bar, look back: if current bar starts a run AND next-3-bar look-AHEAD is unavailable,
    # we count at the END of the run, when close >= cl after ≥3 below-bars.
    # PIT-safe alternative: detect end-of-run bars where streak just ended with length ≥ 3.
    streak = _streak_true(below.astype(bool))
    end_bar = ((below.shift(1).fillna(0) == 1) & (below == 0))
    ended_streak = streak.shift(1).fillna(0)
    event = (end_bar & (ended_streak >= 3)).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket J — Trailing-stop "walking" / hugging (101-110)
# ============================================================

def f14_stps_101_frac_close_within_half_atr_of_st_10_3_21d(high, low, close):
    """Fraction of bars in 21d where |close − ST(10,3)| < 0.5 × ATR(21) — stop-hugging."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    hug = ((close - st).abs() < 0.5 * atr).astype(float)
    return hug.rolling(MDAYS, min_periods=WDAYS).mean()


def f14_stps_102_frac_close_within_1atr_of_st_10_3_63d(high, low, close):
    """Fraction of bars in 63d where |close − ST(10,3)| < 1 × ATR(21)."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    hug = ((close - st).abs() < atr).astype(float)
    return hug.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_103_slope_close_to_st_10_3_dist_21d(high, low, close):
    """Slope of (close − ST(10,3))/close over trailing 21d — distance velocity."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _rolling_slope(_safe_div(close - st, close), MDAYS)


def f14_stps_104_slope_close_to_chandelier_long_dist_21d(high, low, close):
    """Slope of (close − Chandelier-long(22,3))/close over trailing 21d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _rolling_slope(_safe_div(close - cl, close), MDAYS)


def f14_stps_105_std_close_to_st_10_3_dist_21d(high, low, close):
    """Std of (close − ST(10,3))/close over trailing 21d — distance volatility."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _safe_div(close - st, close).rolling(MDAYS, min_periods=WDAYS).std()


def f14_stps_106_ratio_mean_dist_21d_to_63d_st_10_3(high, low, close):
    """Mean (close − ST(10,3))/close over 21d / mean over 63d — compression metric."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    r = _safe_div(close - st, close)
    m21 = r.rolling(MDAYS, min_periods=WDAYS).mean()
    m63 = r.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(m21, m63)


def f14_stps_107_proximity_touch_count_st_10_3_252d(high, low, close):
    """Count of bars in 252d where |close − ST(10,3)|/close < 0.005 — proximity-touch count."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    touch = (_safe_div((close - st).abs(), close) < 0.005).astype(float)
    return touch.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_108_frac_close_within_half_atr_of_psar_63d(high, low, close):
    """Fraction of bars in 63d where |close − PSAR(0.02,0.2)| < 0.5 × ATR(21)."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    atr = _atr(high, low, close, n=MDAYS)
    hug = ((close - sar).abs() < 0.5 * atr).astype(float)
    return hug.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_109_log_dist_close_to_chande_kroll_long_stop(high, low, close):
    """Log distance close above Chande-Kroll long stop (p=10, q=20, x=1) — combined-stop trail metric."""
    h_stop, _ = _chande_kroll_stop(high, low, close, p=10, q=20, x=1.0)
    return _safe_log(close) - _safe_log(h_stop)


def f14_stps_110_kama_efficiency_ratio_21d_trajectory_21d(close):
    """Δ KAMA Efficiency Ratio over last 21d (ER_now − ER_21d_ago) — efficiency loss = topping."""
    chg = (close - close.shift(MDAYS)).abs()
    vol = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    er = _safe_div(chg, vol)
    return er - er.shift(MDAYS)


# ============================================================
# Bucket K — Cross-indicator agreement / divergence (111-120)
# ============================================================

def f14_stps_111_count_systems_close_above_stop(high, low, close):
    """Count of (ST(10,3), PSAR(0.02,0.2), Chandelier-long(22,3)) where close > stop."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    a = (close > st).astype(float)
    b = (close > sar).astype(float)
    c = (close > cl).astype(float)
    return a.fillna(0) + b.fillna(0) + c.fillna(0)


def f14_stps_112_cross_system_flip_count_21d(high, low, close):
    """Sum of ST(10,3) + PSAR(0.02,0.2) + Chandelier-direction-proxy flips in 21d."""
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    dch = (close > cl).astype(int).replace(0, -1)
    f1 = (dst.diff().abs() > 0).astype(float)
    f2 = (dps.diff().abs() > 0).astype(float)
    f3 = (dch.diff().abs() > 0).astype(float)
    return (f1 + f2 + f3).rolling(MDAYS, min_periods=WDAYS).sum()


def f14_stps_113_bars_since_all_three_systems_long(high, low, close):
    """Bars since all of (ST(10,3), PSAR(0.02,0.2), Chandelier-long) agreed long."""
    st, dst = _supertrend(high, low, close, n=10, mult=3.0)
    sar, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    aligned = ((dst == 1) & (dps == 1) & (close > cl)).astype(bool)
    return _bars_since_true(aligned)


def f14_stps_114_frac_bars_all_three_aligned_long_63d(high, low, close):
    """Fraction of bars in 63d where all three systems aligned long."""
    st, dst = _supertrend(high, low, close, n=10, mult=3.0)
    sar, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    aligned = ((dst == 1) & (dps == 1) & (close > cl)).astype(float)
    return aligned.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_115_frac_bars_exactly_two_long_63d(high, low, close):
    """Fraction of bars in 63d where exactly two of the three systems are long (disagreement)."""
    st, dst = _supertrend(high, low, close, n=10, mult=3.0)
    sar, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    cnt = (dst == 1).astype(int) + (dps == 1).astype(int) + (close > cl).astype(int)
    two = (cnt == 2).astype(float)
    return two.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_116_fast_slow_supertrend_disagreements_63d(high, low, close):
    """Count of bars in 63d where ST(7,2) and ST(50,3) directions disagree."""
    _, df = _supertrend(high, low, close, n=7, mult=2.0)
    _, ds = _supertrend(high, low, close, n=50, mult=3.0)
    dis = (df != ds).astype(float)
    return dis.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_117_psar_vs_st_10_3_disagreements_252d(high, low, close):
    """Count of bars in 252d where PSAR(0.02,0.2) and ST(10,3) directions disagree."""
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    dis = (dst != dps).astype(float)
    return dis.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_118_chandelier_vs_st_10_3_disagreements_63d(high, low, close):
    """Count of bars in 63d where Chandelier-long position (close above/below) disagrees with ST(10,3) direction."""
    st, dst = _supertrend(high, low, close, n=10, mult=3.0)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    sign_ch = (close > cl).astype(int).replace(0, -1)
    dis = (dst != sign_ch).astype(float)
    return dis.rolling(QDAYS, min_periods=MDAYS).sum()


def f14_stps_119_mean_pairwise_corr_stop_distances_63d(high, low, close):
    """Mean pairwise correlation across (close-ST10_3, close-PSAR, close-Chandelier22_3) in 63d window."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    a = (close - st)
    b = (close - sar)
    c = (close - cl)
    cab = a.rolling(QDAYS, min_periods=MDAYS).corr(b)
    cac = a.rolling(QDAYS, min_periods=MDAYS).corr(c)
    cbc = b.rolling(QDAYS, min_periods=MDAYS).corr(c)
    return (cab + cac + cbc) / 3.0


def f14_stps_120_composite_flip_event_count_252d(high, low, close):
    """Total unique flip-dates across ST(10,3), PSAR(0.02,0.2), Chandelier-cross in trailing 252d."""
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    dch = (close > cl).astype(int).replace(0, -1)
    any_flip = ((dst.diff().abs() > 0) | (dps.diff().abs() > 0) | (dch.diff().abs() > 0)).astype(float)
    return any_flip.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket L — Stop-loss-trip implied loss (121-125)
# ============================================================

def f14_stps_121_log_loss_if_st_10_3_tripped(high, low, close):
    """Log loss from current close if ST(10,3) is tripped — log(stop/close)."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _safe_log(st) - _safe_log(close)


def f14_stps_122_atr_loss_if_st_10_3_tripped(high, low, close):
    """(ST(10,3) − close) / ATR(21) — ATR-normalized implied loss (negative when long extended)."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _safe_div(st - close, _atr(high, low, close, n=MDAYS))


def f14_stps_123_atr_loss_if_psar_tripped(high, low, close):
    """(PSAR(0.02,0.2) − close) / ATR(21) — ATR-normalized implied loss to PSAR."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return _safe_div(sar - close, _atr(high, low, close, n=MDAYS))


def f14_stps_124_min_stop_slack_st_10_3_since_up_flip_atr_norm(high, low, close):
    """Min (close − ST(10,3))/ATR(21) since most recent ST(10,3) up-flip — closest the price has come to stop in current uptrend (low = no pullback = blowoff)."""
    st, d = _supertrend(high, low, close, n=10, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    up = ((d == 1) & (d.shift(1) == -1)).astype(bool)
    bsu = _bars_since_true(up)
    slack = _safe_div(close - st, atr)
    bs = bsu.values; s_arr = slack.values
    n = len(s_arr)
    out = np.full(n, np.nan)
    cur_min = np.nan; last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]):
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_min = np.nan
            if not np.isnan(s_arr[i]):
                cur_min = s_arr[i] if np.isnan(cur_min) else min(cur_min, s_arr[i])
            out[i] = cur_min
    return pd.Series(out, index=close.index)


def f14_stps_125_worst_implied_stop_trip_loss_zscore_252d(high, low, close):
    """Worst (most-negative) of (ST, PSAR, Chandelier) ATR-losses, z-scored in 252d."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    atr21 = _atr(high, low, close, n=MDAYS)
    a = _safe_div(st - close, atr21)
    b = _safe_div(sar - close, atr21)
    c = _safe_div(cl - close, atr21)
    # Use unique column names to avoid the idxmax/string-name gotcha (HANDOFF §8).
    pieces = pd.concat([a.rename("a"), b.rename("b"), c.rename("c")], axis=1)
    worst = pieces.min(axis=1)
    return _rolling_zscore(worst, YDAYS)


# ============================================================
# Bucket M — Stop-distance velocity / slope (126-135)
# ============================================================

def f14_stps_126_smoothed_d1_st_10_3_dist_5d(high, low, close):
    """First-difference of (close − ST(10,3))/close smoothed by 5d rolling mean."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    r = _safe_div(close - st, close)
    return r.diff().rolling(WDAYS, min_periods=2).mean()


def f14_stps_127_slope_st_10_3_dist_63d(high, low, close):
    """Slope of (close − ST(10,3))/close over trailing 63d."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    return _rolling_slope(_safe_div(close - st, close), QDAYS)


def f14_stps_128_slope_chandelier_long_dist_63d(high, low, close):
    """Slope of (close − Chandelier-long(22,3))/close over trailing 63d."""
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    return _rolling_slope(_safe_div(close - cl, close), QDAYS)


def f14_stps_129_ratio_st_10_3_dist_to_63d_median_squeeze(high, low, close):
    """Current (close − ST(10,3))/close divided by trailing-63d-median — squeeze ratio (compression < 1)."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    r = _safe_div(close - st, close)
    return _safe_div(r, r.rolling(QDAYS, min_periods=MDAYS).median())


def f14_stps_130_ratio_st_10_3_dist_to_252d_median(high, low, close):
    """Current (close − ST(10,3))/close divided by trailing-252d-median."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    r = _safe_div(close - st, close)
    return _safe_div(r, r.rolling(YDAYS, min_periods=QDAYS).median())


def f14_stps_131_smoothed_d2_st_10_3_dist_5d(high, low, close):
    """Second-difference of (close − ST(10,3))/close smoothed by 5d rolling mean — acceleration."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    r = _safe_div(close - st, close)
    return r.diff().diff().rolling(WDAYS, min_periods=2).mean()


def f14_stps_132_slope_psar_dist_21d(high, low, close):
    """Slope of (close − PSAR(0.02,0.2))/close over trailing 21d."""
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return _rolling_slope(_safe_div(close - sar, close), MDAYS)


def f14_stps_133_percent_trail_stop_10pct_in_short_state(close):
    """Indicator: 10%-percent-trailing-stop is currently in 'short' (post-flip) state — fixed-pct stop tripped."""
    _, d = _percent_trail_stop(close, 0.10)
    return (d == -1).astype(float)


def f14_stps_134_composite_blowoff_stop_indicator_3systems_p95_252d(high, low, close):
    """Indicator: ALL of (ST(10,3), PSAR(0.02,0.2), Chandelier(22,3)) distances are simultaneously at ≥95th-pct of trailing-252d distribution — maximum cross-system extension = blowoff."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    d_st = _safe_div(close - st, close)
    d_ps = _safe_div(close - sar, close)
    d_cl = _safe_div(close - cl, close)
    p95_st = d_st.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    p95_ps = d_ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    p95_cl = d_cl.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return ((d_st >= p95_st) & (d_ps >= p95_ps) & (d_cl >= p95_cl)).astype(float).where(
        p95_st.notna() & p95_ps.notna() & p95_cl.notna(), np.nan
    )


def f14_stps_135_atr_dist_close_to_hilo_activator_3(high, low, close):
    """(close − HiLo-Activator(3) stop) / ATR(21) — Krausz HiLo trailing-stop extension."""
    st, _ = _hilo_activator(high, low, n=3)
    return _safe_div(close - st, _atr(high, low, close, n=MDAYS))


# ============================================================
# Bucket N — Breakout-into-stop reversal at peaks (136-142)
# ============================================================

def f14_stps_136_indicator_252d_high_and_st_10_3_down_flip_within_5(high, low, close):
    """Indicator: bar within 5 days of a 252d high AND a ST(10,3) down-flip within 5 days."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(int)
    near_peak = at_peak.rolling(5, min_periods=1).sum().fillna(0) > 0
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((dst == -1) & (dst.shift(1) == 1)).astype(int)
    near_down = down.rolling(5, min_periods=1).sum().fillna(0) > 0
    return (near_peak & near_down).astype(float)


def f14_stps_137_indicator_252d_high_and_chandelier_breach_within_21(high, low, close):
    """Indicator: 252d high within trailing 21d AND Chandelier-long breach within trailing 21d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(int)
    near_peak = at_peak.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = ((low < cl) & cl.notna()).astype(int)
    near_breach = breach.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    return (near_peak & near_breach).astype(float)


def f14_stps_138_indicator_252d_high_and_psar_down_flip_within_10(high, low, close):
    """Indicator: 252d high within trailing 10d AND PSAR(0.02,0.2) down-flip within trailing 10d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(int)
    near_peak = at_peak.rolling(10, min_periods=1).sum().fillna(0) > 0
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    down = ((dps == -1) & (dps.shift(1) == 1)).astype(int)
    near_down = down.rolling(10, min_periods=1).sum().fillna(0) > 0
    return (near_peak & near_down).astype(float)


def f14_stps_139_count_peak_st_flip_events_504d(high, low, close):
    """Count of (252d-high AND ST(10,3) down-flip within 5 days) co-occurrences in trailing 504d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(int)
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((dst == -1) & (dst.shift(1) == 1)).astype(int)
    near_down = (down.rolling(5, min_periods=1).sum().fillna(0) > 0).astype(int)
    co = ((at_peak == 1) & (near_down == 1)).astype(float)
    return co.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f14_stps_140_count_peak_chandelier_breach_events_504d(high, low, close):
    """Count of (252d-high AND Chandelier-long breach within 21d) co-occurrences in trailing 504d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(int)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    breach = ((low < cl) & cl.notna()).astype(int)
    near_breach = (breach.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0).astype(int)
    co = ((at_peak == 1) & (near_breach == 1)).astype(float)
    return co.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f14_stps_141_log_return_from_252d_peak_to_recent_st_down_flip(high, low, close):
    """Log close-return from most recent 252d-high bar to most recent ST(10,3) down-flip bar."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(bool)
    bsp = _bars_since_true(at_peak)
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((dst == -1) & (dst.shift(1) == 1)).astype(bool)
    bsd = _bars_since_true(down)
    arr = close.values
    bp = bsp.values; bd = bsd.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(bp[i]) or np.isnan(bd[i]):
            continue
        peak_i = i - int(bp[i])
        down_i = i - int(bd[i])
        if 0 <= peak_i < n and 0 <= down_i < n and arr[peak_i] > 0 and arr[down_i] > 0:
            out[i] = np.log(arr[down_i]) - np.log(arr[peak_i])
    return pd.Series(out, index=close.index)


def f14_stps_142_bars_from_252d_peak_to_recent_st_down_flip(high, low, close):
    """Signed gap (in bars) from most recent 252d-high to most recent ST(10,3) down-flip."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high >= rmax).astype(bool)
    bsp = _bars_since_true(at_peak)
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    down = ((dst == -1) & (dst.shift(1) == 1)).astype(bool)
    bsd = _bars_since_true(down)
    # peak_index - down_index = (i - bsp) - (i - bsd) = bsd - bsp
    return bsd - bsp


# ============================================================
# Bucket O — Composite trailing-stop topping-quality (143-150)
# ============================================================

def f14_stps_143_product_st_psar_log_extensions(high, low, close):
    """Product of (log(close)−log(ST(10,3))) and (log(close)−log(PSAR(0.02,0.2))) — combined extension."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    return (_safe_log(close) - _safe_log(st)) * (_safe_log(close) - _safe_log(sar))


def f14_stps_144_ratio_fast_slow_st_distance(high, low, close):
    """(close − ST(7,2)) / (close − ST(50,3)) — stop-system divergence ratio."""
    fast, _ = _supertrend(high, low, close, n=7, mult=2.0)
    slow, _ = _supertrend(high, low, close, n=50, mult=3.0)
    return _safe_div(close - fast, close - slow)


def f14_stps_145_weinstein_stage_classifier_30wk(close):
    """Stan Weinstein stage 1/2/3/4 based on close vs 30wk(150d) SMA and SMA slope (21d). Stage 2=2 (uptrend), Stage 3=3 (top), Stage 4=4 (decline)."""
    sma = close.rolling(150, min_periods=50).mean()
    slope = _rolling_slope(sma, MDAYS)
    above = close > sma
    slope_up = slope > 0
    stage = pd.Series(np.nan, index=close.index)
    stage = stage.where(~(above & slope_up), 2.0)     # stage 2: above, rising
    stage = stage.where(~(above & ~slope_up), 3.0)    # stage 3: above, flat/declining
    stage = stage.where(~(~above & slope_up), 1.0)    # stage 1: below, rising (accumulation)
    stage = stage.where(~(~above & ~slope_up), 4.0)   # stage 4: below, declining
    return stage.where(sma.notna() & slope.notna(), np.nan)


def f14_stps_146_distinct_state_configs_63d(high, low, close):
    """Count of distinct (ST, PSAR, Chandelier-above) configurations observed in trailing 63d."""
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    a = (dst == 1).astype(int).fillna(0)
    b = (dps == 1).astype(int).fillna(0)
    c = (close > cl).astype(int).fillna(0)
    code = (a * 4 + b * 2 + c).astype(float)
    return code.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float(len(np.unique(w[~np.isnan(w)]))), raw=True)


def f14_stps_147_weighted_topping_quality_score(high, low, close):
    """Σ z(extension_i) × (1 / dist_to_stop_i) summed across (ST, PSAR, Chandelier) — heuristic topping score."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    e_st = _rolling_zscore(_safe_div(close - st, close), YDAYS)
    e_ps = _rolling_zscore(_safe_div(close - sar, close), YDAYS)
    e_cl = _rolling_zscore(_safe_div(close - cl, close), YDAYS)
    inv_st = _safe_div(close, (close - st).abs())
    inv_ps = _safe_div(close, (close - sar).abs())
    inv_cl = _safe_div(close, (close - cl).abs())
    return e_st * inv_st + e_ps * inv_ps + e_cl * inv_cl


def f14_stps_148_cum_time_all_three_extended_above_stop_252d(high, low, close):
    """Cumulative bars in 252d where close > ST AND close > PSAR AND close > Chandelier-long by ≥ 1×ATR."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    atr = _atr(high, low, close, n=MDAYS)
    cond = ((close - st > atr) & (close - sar > atr) & (close - cl > atr)).astype(float)
    return cond.rolling(YDAYS, min_periods=QDAYS).sum()


def f14_stps_149_vol_normalized_cross_system_stop_dispersion_63d(high, low, close):
    """Std (across ST, PSAR, Chandelier) of stop levels normalized by ATR(21), averaged over 63d."""
    st, _ = _supertrend(high, low, close, n=10, mult=3.0)
    sar, _ = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    pieces = pd.concat([st.rename("a"), sar.rename("b"), cl.rename("c")], axis=1)
    stop_std = pieces.std(axis=1)
    norm = _safe_div(stop_std, _atr(high, low, close, n=MDAYS))
    return norm.rolling(QDAYS, min_periods=MDAYS).mean()


def f14_stps_150_change_in_cross_system_agreement_21d(high, low, close):
    """Current count-of-systems-long minus that count 21d ago — agreement-shift velocity."""
    _, dst = _supertrend(high, low, close, n=10, mult=3.0)
    _, dps = _psar(high, low, af0=0.02, afmax=0.2)
    cl = _chandelier_long(high, low, close, n=22, mult=3.0)
    cnt = ((dst == 1).astype(int) + (dps == 1).astype(int) + (close > cl).astype(int)).astype(float)
    return cnt - cnt.shift(MDAYS)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

SUPERTREND_PSAR_CHANDELIER_BASE_REGISTRY_076_150 = {
    "f14_stps_076_psar_step_size_norm_atr": {"inputs": ["high", "low", "close"], "func": f14_stps_076_psar_step_size_norm_atr},
    "f14_stps_077_frac_bars_psar_step_at_max_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_077_frac_bars_psar_step_at_max_21d},
    "f14_stps_078_ratio_fast_slow_psar_distance": {"inputs": ["high", "low", "close"], "func": f14_stps_078_ratio_fast_slow_psar_distance},
    "f14_stps_079_psar_step_change_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_079_psar_step_change_21d},
    "f14_stps_080_log_dist_close_to_30wk_sma": {"inputs": ["close"], "func": f14_stps_080_log_dist_close_to_30wk_sma},
    "f14_stps_081_log_dist_close_to_chandelier_long_22_3": {"inputs": ["high", "low", "close"], "func": f14_stps_081_log_dist_close_to_chandelier_long_22_3},
    "f14_stps_082_atr_dist_close_to_chandelier_long_22_3": {"inputs": ["high", "low", "close"], "func": f14_stps_082_atr_dist_close_to_chandelier_long_22_3},
    "f14_stps_083_atr_dist_close_to_chandelier_long_50_3": {"inputs": ["high", "low", "close"], "func": f14_stps_083_atr_dist_close_to_chandelier_long_50_3},
    "f14_stps_084_dist_close_to_chandelier_short_22_3": {"inputs": ["high", "low", "close"], "func": f14_stps_084_dist_close_to_chandelier_short_22_3},
    "f14_stps_085_ratio_long_to_short_chandelier_room": {"inputs": ["high", "low", "close"], "func": f14_stps_085_ratio_long_to_short_chandelier_room},
    "f14_stps_086_pct_dist_close_to_chandelier_long_22_3": {"inputs": ["high", "low", "close"], "func": f14_stps_086_pct_dist_close_to_chandelier_long_22_3},
    "f14_stps_087_sigma_dist_close_to_chandelier_long_22_3_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_087_sigma_dist_close_to_chandelier_long_22_3_63d},
    "f14_stps_088_zscore_close_minus_chandelier_long_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_088_zscore_close_minus_chandelier_long_252d},
    "f14_stps_089_pctile_rank_close_minus_chandelier_long_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_089_pctile_rank_close_minus_chandelier_long_252d},
    "f14_stps_090_max_excursion_above_chandelier_long_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_090_max_excursion_above_chandelier_long_21d},
    "f14_stps_091_chandelier_long_breach_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_091_chandelier_long_breach_count_63d},
    "f14_stps_092_chandelier_long_breach_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_092_chandelier_long_breach_count_252d},
    "f14_stps_093_bars_since_chandelier_long_breach": {"inputs": ["high", "low", "close"], "func": f14_stps_093_bars_since_chandelier_long_breach},
    "f14_stps_094_indicator_recovered_within_5_after_chandelier_breach": {"inputs": ["high", "low", "close"], "func": f14_stps_094_indicator_recovered_within_5_after_chandelier_breach},
    "f14_stps_095_chandelier_breach_then_recover_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_095_chandelier_breach_then_recover_count_252d},
    "f14_stps_096_max_consecutive_bars_close_below_chandelier_long_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_096_max_consecutive_bars_close_below_chandelier_long_252d},
    "f14_stps_097_frac_bars_close_below_chandelier_long_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_097_frac_bars_close_below_chandelier_long_63d},
    "f14_stps_098_post_breach_max_drawdown_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_098_post_breach_max_drawdown_21d},
    "f14_stps_099_false_breach_count_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_099_false_breach_count_63d},
    "f14_stps_100_full_breach_3plus_bars_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_100_full_breach_3plus_bars_count_252d},
    "f14_stps_101_frac_close_within_half_atr_of_st_10_3_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_101_frac_close_within_half_atr_of_st_10_3_21d},
    "f14_stps_102_frac_close_within_1atr_of_st_10_3_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_102_frac_close_within_1atr_of_st_10_3_63d},
    "f14_stps_103_slope_close_to_st_10_3_dist_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_103_slope_close_to_st_10_3_dist_21d},
    "f14_stps_104_slope_close_to_chandelier_long_dist_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_104_slope_close_to_chandelier_long_dist_21d},
    "f14_stps_105_std_close_to_st_10_3_dist_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_105_std_close_to_st_10_3_dist_21d},
    "f14_stps_106_ratio_mean_dist_21d_to_63d_st_10_3": {"inputs": ["high", "low", "close"], "func": f14_stps_106_ratio_mean_dist_21d_to_63d_st_10_3},
    "f14_stps_107_proximity_touch_count_st_10_3_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_107_proximity_touch_count_st_10_3_252d},
    "f14_stps_108_frac_close_within_half_atr_of_psar_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_108_frac_close_within_half_atr_of_psar_63d},
    "f14_stps_109_log_dist_close_to_chande_kroll_long_stop": {"inputs": ["high", "low", "close"], "func": f14_stps_109_log_dist_close_to_chande_kroll_long_stop},
    "f14_stps_110_kama_efficiency_ratio_21d_trajectory_21d": {"inputs": ["close"], "func": f14_stps_110_kama_efficiency_ratio_21d_trajectory_21d},
    "f14_stps_111_count_systems_close_above_stop": {"inputs": ["high", "low", "close"], "func": f14_stps_111_count_systems_close_above_stop},
    "f14_stps_112_cross_system_flip_count_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_112_cross_system_flip_count_21d},
    "f14_stps_113_bars_since_all_three_systems_long": {"inputs": ["high", "low", "close"], "func": f14_stps_113_bars_since_all_three_systems_long},
    "f14_stps_114_frac_bars_all_three_aligned_long_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_114_frac_bars_all_three_aligned_long_63d},
    "f14_stps_115_frac_bars_exactly_two_long_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_115_frac_bars_exactly_two_long_63d},
    "f14_stps_116_fast_slow_supertrend_disagreements_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_116_fast_slow_supertrend_disagreements_63d},
    "f14_stps_117_psar_vs_st_10_3_disagreements_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_117_psar_vs_st_10_3_disagreements_252d},
    "f14_stps_118_chandelier_vs_st_10_3_disagreements_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_118_chandelier_vs_st_10_3_disagreements_63d},
    "f14_stps_119_mean_pairwise_corr_stop_distances_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_119_mean_pairwise_corr_stop_distances_63d},
    "f14_stps_120_composite_flip_event_count_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_120_composite_flip_event_count_252d},
    "f14_stps_121_log_loss_if_st_10_3_tripped": {"inputs": ["high", "low", "close"], "func": f14_stps_121_log_loss_if_st_10_3_tripped},
    "f14_stps_122_atr_loss_if_st_10_3_tripped": {"inputs": ["high", "low", "close"], "func": f14_stps_122_atr_loss_if_st_10_3_tripped},
    "f14_stps_123_atr_loss_if_psar_tripped": {"inputs": ["high", "low", "close"], "func": f14_stps_123_atr_loss_if_psar_tripped},
    "f14_stps_124_min_stop_slack_st_10_3_since_up_flip_atr_norm": {"inputs": ["high", "low", "close"], "func": f14_stps_124_min_stop_slack_st_10_3_since_up_flip_atr_norm},
    "f14_stps_125_worst_implied_stop_trip_loss_zscore_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_125_worst_implied_stop_trip_loss_zscore_252d},
    "f14_stps_126_smoothed_d1_st_10_3_dist_5d": {"inputs": ["high", "low", "close"], "func": f14_stps_126_smoothed_d1_st_10_3_dist_5d},
    "f14_stps_127_slope_st_10_3_dist_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_127_slope_st_10_3_dist_63d},
    "f14_stps_128_slope_chandelier_long_dist_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_128_slope_chandelier_long_dist_63d},
    "f14_stps_129_ratio_st_10_3_dist_to_63d_median_squeeze": {"inputs": ["high", "low", "close"], "func": f14_stps_129_ratio_st_10_3_dist_to_63d_median_squeeze},
    "f14_stps_130_ratio_st_10_3_dist_to_252d_median": {"inputs": ["high", "low", "close"], "func": f14_stps_130_ratio_st_10_3_dist_to_252d_median},
    "f14_stps_131_smoothed_d2_st_10_3_dist_5d": {"inputs": ["high", "low", "close"], "func": f14_stps_131_smoothed_d2_st_10_3_dist_5d},
    "f14_stps_132_slope_psar_dist_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_132_slope_psar_dist_21d},
    "f14_stps_133_percent_trail_stop_10pct_in_short_state": {"inputs": ["close"], "func": f14_stps_133_percent_trail_stop_10pct_in_short_state},
    "f14_stps_134_composite_blowoff_stop_indicator_3systems_p95_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_134_composite_blowoff_stop_indicator_3systems_p95_252d},
    "f14_stps_135_atr_dist_close_to_hilo_activator_3": {"inputs": ["high", "low", "close"], "func": f14_stps_135_atr_dist_close_to_hilo_activator_3},
    "f14_stps_136_indicator_252d_high_and_st_10_3_down_flip_within_5": {"inputs": ["high", "low", "close"], "func": f14_stps_136_indicator_252d_high_and_st_10_3_down_flip_within_5},
    "f14_stps_137_indicator_252d_high_and_chandelier_breach_within_21": {"inputs": ["high", "low", "close"], "func": f14_stps_137_indicator_252d_high_and_chandelier_breach_within_21},
    "f14_stps_138_indicator_252d_high_and_psar_down_flip_within_10": {"inputs": ["high", "low", "close"], "func": f14_stps_138_indicator_252d_high_and_psar_down_flip_within_10},
    "f14_stps_139_count_peak_st_flip_events_504d": {"inputs": ["high", "low", "close"], "func": f14_stps_139_count_peak_st_flip_events_504d},
    "f14_stps_140_count_peak_chandelier_breach_events_504d": {"inputs": ["high", "low", "close"], "func": f14_stps_140_count_peak_chandelier_breach_events_504d},
    "f14_stps_141_log_return_from_252d_peak_to_recent_st_down_flip": {"inputs": ["high", "low", "close"], "func": f14_stps_141_log_return_from_252d_peak_to_recent_st_down_flip},
    "f14_stps_142_bars_from_252d_peak_to_recent_st_down_flip": {"inputs": ["high", "low", "close"], "func": f14_stps_142_bars_from_252d_peak_to_recent_st_down_flip},
    "f14_stps_143_product_st_psar_log_extensions": {"inputs": ["high", "low", "close"], "func": f14_stps_143_product_st_psar_log_extensions},
    "f14_stps_144_ratio_fast_slow_st_distance": {"inputs": ["high", "low", "close"], "func": f14_stps_144_ratio_fast_slow_st_distance},
    "f14_stps_145_weinstein_stage_classifier_30wk": {"inputs": ["close"], "func": f14_stps_145_weinstein_stage_classifier_30wk},
    "f14_stps_146_distinct_state_configs_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_146_distinct_state_configs_63d},
    "f14_stps_147_weighted_topping_quality_score": {"inputs": ["high", "low", "close"], "func": f14_stps_147_weighted_topping_quality_score},
    "f14_stps_148_cum_time_all_three_extended_above_stop_252d": {"inputs": ["high", "low", "close"], "func": f14_stps_148_cum_time_all_three_extended_above_stop_252d},
    "f14_stps_149_vol_normalized_cross_system_stop_dispersion_63d": {"inputs": ["high", "low", "close"], "func": f14_stps_149_vol_normalized_cross_system_stop_dispersion_63d},
    "f14_stps_150_change_in_cross_system_agreement_21d": {"inputs": ["high", "low", "close"], "func": f14_stps_150_change_in_cross_system_agreement_21d},
}
