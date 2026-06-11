"""stochastic_williams_family base features 301-375 — Pipeline 1b-technical.

75 distinct "volume-weighted + adaptive + practitioner" hypotheses. Themes:
Volume-weighted oscillators (301-310),
Adaptive / self-calibrating thresholds (311-320),
Practitioner patterns: Larry Williams, DeMark, Elder, Worden, Dorsey (321-335),
Stuck-stock-specific failure signatures (336-355),
ML-orthogonal complexity / entropy / fractal metrics (356-375).

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-file imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


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


def _pct_rank(s, window, min_periods=None):
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


def _quantile_rolling(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _vwap_n(close, volume, n):
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    vv = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, vv)


def _vw_stoch_k(close, volume, n_vw, n_k, smooth_k=1):
    """Stoch K computed on VWP (volume-weighted price) input."""
    vwp = _vwap_n(close, volume, n_vw)
    ll = vwp.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = vwp.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    k = 100.0 * _safe_div(vwp - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k


def _vw_williams_r(close, volume, n_vw, n):
    vwp = _vwap_n(close, volume, n_vw)
    ll = vwp.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = vwp.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - vwp, hh - ll)


def _money_flow(high, low, close, volume):
    """Typical-price money flow series."""
    tp = (high + low + close) / 3.0
    return tp * volume


def _ulcer_vol_bucket(close, n=63):
    """Returns rolling-std-based vol regime (0=low,1=high) using own median split."""
    ret = close.pct_change()
    sd = ret.rolling(n, min_periods=max(n // 3, 2)).std()
    med = sd.rolling(YDAYS, min_periods=QDAYS).median()
    return (sd > med).astype(float)


def _hurst_rs(s, n):
    """R/S Hurst exponent over rolling window n. Returns slope of log(R/S) vs log(sub-window)."""
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 16:
            return np.nan
        # split into 2 sub-windows of half-length
        nn = v.size
        rs_list = []
        for k in (4, 8, 16):
            if nn < k * 2:
                continue
            chunks = nn // k
            rs_vals = []
            for i in range(chunks):
                seg = v[i * k:(i + 1) * k]
                if seg.size < 2:
                    continue
                m = seg.mean()
                z = seg - m
                cum = np.cumsum(z)
                R = cum.max() - cum.min()
                S = seg.std()
                if S > 0:
                    rs_vals.append(R / S)
            if rs_vals:
                rs_list.append((np.log(float(k)), np.log(np.mean(rs_vals))))
        if len(rs_list) < 2:
            return np.nan
        xs = np.array([p[0] for p in rs_list])
        ys = np.array([p[1] for p in rs_list])
        xm = xs.mean(); ym = ys.mean()
        num = ((xs - xm) * (ys - ym)).sum()
        den = ((xs - xm) ** 2).sum()
        return num / den if den > 0 else np.nan
    return s.rolling(n, min_periods=max(n // 2, 8)).apply(_h, raw=True)


def _dfa_hurst(s, n):
    """Detrended Fluctuation Analysis Hurst over rolling window n."""
    def _d(w):
        v = w[~np.isnan(w)]
        if v.size < 16:
            return np.nan
        y = np.cumsum(v - v.mean())
        scales = [4, 8, 16]
        log_pts = []
        for sc in scales:
            if v.size < sc * 2:
                continue
            nseg = v.size // sc
            F = []
            for i in range(nseg):
                seg = y[i * sc:(i + 1) * sc]
                x = np.arange(sc)
                xm = x.mean(); ym = seg.mean()
                num = ((x - xm) * (seg - ym)).sum()
                den = ((x - xm) ** 2).sum()
                slope = num / den if den > 0 else 0.0
                intercept = ym - slope * xm
                trend = slope * x + intercept
                F.append(((seg - trend) ** 2).mean())
            if F:
                log_pts.append((np.log(float(sc)), 0.5 * np.log(np.mean(F))))
        if len(log_pts) < 2:
            return np.nan
        xs = np.array([p[0] for p in log_pts])
        ys = np.array([p[1] for p in log_pts])
        xm = xs.mean(); ym = ys.mean()
        num = ((xs - xm) * (ys - ym)).sum()
        den = ((xs - xm) ** 2).sum()
        return num / den if den > 0 else np.nan
    return s.rolling(n, min_periods=max(n // 2, 8)).apply(_d, raw=True)


def _sample_entropy(s, n, m=2, r_frac=0.2):
    """Sample entropy SampEn(m, r=r_frac*std) on rolling window n."""
    def _se(w):
        v = w[~np.isnan(w)]
        if v.size < (m + 2):
            return np.nan
        r = r_frac * v.std()
        if r <= 0:
            return np.nan
        # count matches at length m and m+1
        def _phi(mm):
            patterns = np.array([v[i:i + mm] for i in range(v.size - mm + 1)])
            if patterns.shape[0] < 2:
                return 0.0
            cnt = 0
            for i in range(patterns.shape[0]):
                diffs = np.max(np.abs(patterns - patterns[i]), axis=1)
                cnt += int((diffs <= r).sum()) - 1  # exclude self-match
            return float(cnt)
        A = _phi(m + 1)
        B = _phi(m)
        if B <= 0 or A <= 0:
            return np.nan
        return -np.log(A / B)
    return s.rolling(n, min_periods=max(n // 2, m + 2)).apply(_se, raw=True)


def _approx_entropy(s, n, m=2, r_frac=0.2):
    """Approximate entropy ApEn(m, r)."""
    def _ae(w):
        v = w[~np.isnan(w)]
        if v.size < (m + 2):
            return np.nan
        r = r_frac * v.std()
        if r <= 0:
            return np.nan
        def _phi(mm):
            N = v.size - mm + 1
            if N <= 0:
                return 0.0
            patterns = np.array([v[i:i + mm] for i in range(N)])
            C = np.zeros(N)
            for i in range(N):
                diffs = np.max(np.abs(patterns - patterns[i]), axis=1)
                C[i] = float((diffs <= r).sum()) / float(N)
            C = C[C > 0]
            if C.size == 0:
                return 0.0
            return float(np.mean(np.log(C)))
        return _phi(m) - _phi(m + 1)
    return s.rolling(n, min_periods=max(n // 2, m + 2)).apply(_ae, raw=True)


def _perm_entropy(s, n, order=3):
    """Permutation entropy of order `order` on rolling window n."""
    from math import factorial
    norm = np.log(float(factorial(order)))
    def _pe(w):
        v = w[~np.isnan(w)]
        if v.size < order + 1:
            return np.nan
        patterns = {}
        for i in range(v.size - order + 1):
            seg = v[i:i + order]
            key = tuple(np.argsort(seg))
            patterns[key] = patterns.get(key, 0) + 1
        total = sum(patterns.values())
        if total == 0:
            return np.nan
        p = np.array([c / total for c in patterns.values()])
        ent = -float((p * np.log(p)).sum())
        return ent / norm if norm > 0 else np.nan
    return s.rolling(n, min_periods=max(n // 2, order + 2)).apply(_pe, raw=True)


def _multiscale_coarsegrain(s, scale):
    """Coarse-grained series at given scale by non-overlapping block-mean (PIT: uses past values via rolling)."""
    return s.rolling(scale, min_periods=max(scale // 2, 1)).mean()


def _higuchi_fd(s, n, kmax=4):
    """Higuchi fractal dimension over rolling window n."""
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < kmax * 4:
            return np.nan
        L = []
        for k in range(1, kmax + 1):
            Lk = 0.0
            cnt = 0
            for mm in range(k):
                idxs = np.arange(mm, v.size, k)
                if idxs.size < 2:
                    continue
                seg = v[idxs]
                diffs = np.abs(np.diff(seg)).sum()
                norm = float(v.size - 1) / (float(idxs.size - 1) * float(k))
                Lk += diffs * norm / float(k)
                cnt += 1
            if cnt > 0:
                L.append((np.log(1.0 / k), np.log(Lk / cnt)))
        if len(L) < 2:
            return np.nan
        xs = np.array([p[0] for p in L])
        ys = np.array([p[1] for p in L])
        xm = xs.mean(); ym = ys.mean()
        num = ((xs - xm) * (ys - ym)).sum()
        den = ((xs - xm) ** 2).sum()
        return num / den if den > 0 else np.nan
    return s.rolling(n, min_periods=max(n // 2, kmax * 4)).apply(_h, raw=True)


def _petrosian_fd(s, n):
    """Petrosian fractal dimension over rolling window n."""
    def _p(w):
        v = w[~np.isnan(w)]
        if v.size < 4:
            return np.nan
        d = np.diff(v)
        sgn = np.sign(d)
        nzc = int((sgn[:-1] * sgn[1:] < 0).sum())
        N = float(v.size)
        if nzc == 0:
            return np.nan
        return np.log10(N) / (np.log10(N) + np.log10(N / (N + 0.4 * nzc)))
    return s.rolling(n, min_periods=max(n // 2, 4)).apply(_p, raw=True)


def _lempel_ziv(s, n, n_levels=4):
    """Lempel-Ziv complexity on discretized series, rolling window n."""
    def _lz(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        # discretize via quantiles into n_levels bins
        qs = np.quantile(v, np.linspace(0, 1, n_levels + 1)[1:-1])
        symbols = np.searchsorted(qs, v).astype(int)
        # convert to string of chars
        s_str = "".join([chr(48 + sv) for sv in symbols])
        i = 0; c = 1; k = 1; l = 1
        n_s = len(s_str)
        while True:
            if (i + k > n_s) or (l + k > n_s):
                break
            if s_str[i + k - 1] == s_str[l + k - 1]:
                k += 1
                if l + k - 1 >= n_s:
                    c += 1
                    break
            else:
                if k > 1:
                    i = l
                    k = 1
                else:
                    l += 1
                    if l >= n_s:
                        break
                    c += 1
                    k = 1
        return float(c) / (n_s / np.log2(n_s)) if n_s > 1 else np.nan
    return s.rolling(n, min_periods=max(n // 2, 8)).apply(_lz, raw=True)


def _recurrence_rate(s, n, eps_frac=0.1):
    """Recurrence quantification: rate = fraction of recurrent points (|x_i-x_j|<eps)."""
    def _rr(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        eps = eps_frac * (v.max() - v.min())
        if eps <= 0:
            return np.nan
        cnt = 0; total = 0
        for i in range(v.size):
            d = np.abs(v - v[i])
            cnt += int((d <= eps).sum()) - 1
            total += v.size - 1
        return float(cnt) / float(total) if total > 0 else np.nan
    return s.rolling(n, min_periods=max(n // 2, 5)).apply(_rr, raw=True)


def _recurrence_determinism(s, n, eps_frac=0.1, lmin=2):
    """Recurrence determinism: fraction of recurrent points forming diagonal lines of length >= lmin."""
    def _det(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        eps = eps_frac * (v.max() - v.min())
        if eps <= 0:
            return np.nan
        N = v.size
        R = np.zeros((N, N), dtype=bool)
        for i in range(N):
            R[i] = np.abs(v - v[i]) <= eps
        # walk each off-diagonal
        total_rec = int(R.sum()) - N  # exclude main diag self-matches
        if total_rec <= 0:
            return np.nan
        det_count = 0
        for off in range(1, N):
            diag = np.diagonal(R, offset=off)
            run = 0
            for x in diag:
                if x:
                    run += 1
                else:
                    if run >= lmin:
                        det_count += run
                    run = 0
            if run >= lmin:
                det_count += run
            # also lower triangle
            diag2 = np.diagonal(R, offset=-off)
            run = 0
            for x in diag2:
                if x:
                    run += 1
                else:
                    if run >= lmin:
                        det_count += run
                    run = 0
            if run >= lmin:
                det_count += run
        return float(det_count) / float(total_rec)
    return s.rolling(n, min_periods=max(n // 2, 5)).apply(_det, raw=True)


def _autocorr_lag(s, n, lag):
    """Rolling autocorrelation at given lag."""
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < lag + 4:
            return np.nan
        a = v[:-lag]
        b = v[lag:]
        am = a.mean(); bm = b.mean()
        num = ((a - am) * (b - bm)).sum()
        den_a = np.sqrt(((a - am) ** 2).sum())
        den_b = np.sqrt(((b - bm) ** 2).sum())
        if den_a == 0 or den_b == 0:
            return np.nan
        return num / (den_a * den_b)
    return s.rolling(n, min_periods=max(n // 2, lag + 4)).apply(_ac, raw=True)


# ============================================================
# Volume-weighted oscillators (301-310)
# ============================================================


def f26_stwf_301_vw_stoch_k_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stoch %K(14) computed on VWP(14) — volume-weighted price replaces close. Captures price location adjusted for volume."""
    return _vw_stoch_k(close, volume, n_vw=14, n_k=14)


def f26_stwf_302_vw_stoch_d_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VW-Stoch %D(3) — 3-bar mean of VW-K(14)."""
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return _stoch_d(k, 3)


def f26_stwf_303_vw_williams_r_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R(14) on VWP(14) — volume-weighted Williams percentage range."""
    return _vw_williams_r(close, volume, n_vw=14, n=14)


def f26_stwf_304_money_flow_stoch_14(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stoch K(14) on rolling 21d-cumulative money flow (typical_price * volume cumulated)."""
    mf = _money_flow(high, low, close, volume)
    cmf = mf.rolling(MDAYS, min_periods=WDAYS).sum()
    ll = cmf.rolling(14, min_periods=5).min()
    hh = cmf.rolling(14, min_periods=5).max()
    return 100.0 * _safe_div(cmf - ll, hh - ll)


def f26_stwf_305_vw_stoch_above_80_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VW-Stoch K(14) > 80 — volume-weighted OB state (captures distribution-day OB)."""
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_306_vw_stoch_div_vs_price_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish divergence: price 63d new high but VW-Stoch K(14) below its 63d max — volume-aware divergence."""
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    k_max = k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((k < k_max) & p_new).astype(float).where(k.notna() & p_new, np.nan)


def f26_stwf_307_vw_stoch_just_exited_above_80(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VW-Stoch K(14) just exited from >80 (yesterday>80, today<=80) — VW-OB exit signal."""
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_308_vw_williams_r_above_minus20_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VW-Williams %R(14) > -20 — volume-weighted OB state."""
    wr = _vw_williams_r(close, volume, n_vw=14, n=14)
    return (wr > -20.0).astype(float).where(wr.notna(), np.nan)


def f26_stwf_309_vw_williams_r_dwell_above_minus20_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where VW-Williams %R(14) > -20 — VW-OB dwell."""
    wr = _vw_williams_r(close, volume, n_vw=14, n=14)
    return (wr > -20.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(wr.notna(), np.nan)


def f26_stwf_310_vw_stoch_bars_since_252_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since VW-Stoch K(14) made its 252d max — time-since-VW-peak (stale OB indicator)."""
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    rmax = k.rolling(YDAYS, min_periods=QDAYS).max()
    is_max = (k >= rmax) & rmax.notna()
    return _bars_since_true(is_max).where(k.notna(), np.nan)


# ============================================================
# Adaptive / self-calibrating thresholds (311-320)
# ============================================================


def f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Adaptive OB threshold: 90th percentile of Stoch K(14) over trailing 504d (own-history calibration)."""
    k = _stoch_k(high, low, close, 14)
    return _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)


def f26_stwf_312_stoch_above_adaptive_ob_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K(14) > own 504d q90 — self-calibrated OB."""
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_313_stoch_dwell_above_adaptive_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars Stoch K(14) > own 504d q90 — self-calibrated dwell."""
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    above = (k > thr).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean().where(thr.notna(), np.nan)


def f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Adaptive OB threshold for Williams %R(14): 90th percentile over 504d."""
    wr = _williams_r(high, low, close, 14)
    return _quantile_rolling(wr, DDAYS_2Y, 0.90, min_periods=QDAYS)


def f26_stwf_315_williams_r_above_adaptive_ob_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R(14) > own 504d q90 — self-calibrated WR-OB."""
    wr = _williams_r(high, low, close, 14)
    thr = _quantile_rolling(wr, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return (wr > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Adaptive extreme-OB threshold: 99th percentile of Stoch K(14) over 504d."""
    k = _stoch_k(high, low, close, 14)
    return _quantile_rolling(k, DDAYS_2Y, 0.99, min_periods=QDAYS)


def f26_stwf_317_stoch_above_adaptive_extreme_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K(14) > own 504d q99 — extreme self-calibrated state (rare, top-of-cycle indicator)."""
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.99, min_periods=QDAYS)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Threshold conditional on vol regime: low vol -> q85, high vol -> q95 (lower threshold makes more sense in calm regime)."""
    k = _stoch_k(high, low, close, 14)
    vol_hi = _ulcer_vol_bucket(close, QDAYS)
    q85 = _quantile_rolling(k, DDAYS_2Y, 0.85, min_periods=QDAYS)
    q95 = _quantile_rolling(k, DDAYS_2Y, 0.95, min_periods=QDAYS)
    return q85.where(vol_hi == 0.0, q95).where(vol_hi.notna(), np.nan)


def f26_stwf_319_vol_regime_adaptive_stoch_above_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) > vol-regime-adaptive threshold (q85 low-vol / q95 high-vol)."""
    k = _stoch_k(high, low, close, 14)
    vol_hi = _ulcer_vol_bucket(close, QDAYS)
    q85 = _quantile_rolling(k, DDAYS_2Y, 0.85, min_periods=QDAYS)
    q95 = _quantile_rolling(k, DDAYS_2Y, 0.95, min_periods=QDAYS)
    thr = q85.where(vol_hi == 0.0, q95)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_320_stoch_threshold_breach_count_normalized_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized OB breach count: (past-63 above-80 bars) / (expected = 0.1*63) — values >1 indicate elevated OB occupancy."""
    k = _stoch_k(high, low, close, 14)
    above = (k > 80.0).astype(float)
    cnt = above.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(cnt, 6.3)  # expected ~10% of 63 = 6.3


# ============================================================
# Practitioner patterns (321-335)
# ============================================================


def f26_stwf_321_larry_williams_smash_day_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Larry Williams Smash Day: today's low < yesterday's low AND today's close > yesterday's high.
    Failure-prone when fires near a top — bearish exhaustion candle pattern."""
    cond = (low < low.shift(1)) & (close > high.shift(1))
    return cond.astype(float).where(close.notna() & close.shift(1).notna(), np.nan)


def f26_stwf_322_demark_td_pressure_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DeMark TD Pressure(5): 100 * sum(close-low, 5) / sum(high-low, 5)."""
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    return 100.0 * _safe_div(num, den)


def f26_stwf_323_demark_td_pressure_above_82_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TD Pressure(5) > 82 — DeMark OB level."""
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    p = 100.0 * _safe_div(num, den)
    return (p > 82.0).astype(float).where(p.notna(), np.nan)


def f26_stwf_324_demark_td_pressure_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TD Pressure bearish divergence: close at 63d high but Pressure < 63d Pressure max."""
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    p = 100.0 * _safe_div(num, den)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    p_max = p.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p < p_max) & p_new).astype(float).where(p.notna() & p_new, np.nan)


def f26_stwf_325_elder_triple_screen_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Elder triple screen consensus: 1 if daily-K(14) > 80 AND weekly-K(14) > 80 AND monthly-K(14) > 80."""
    k_d = _stoch_k(high, low, close, 14)
    hi_w = high.rolling(5, min_periods=2).max()
    lo_w = low.rolling(5, min_periods=2).min()
    cl_w = close
    k_w = _stoch_k(hi_w, lo_w, cl_w, 14)
    hi_m = high.rolling(MDAYS, min_periods=WDAYS).max()
    lo_m = low.rolling(MDAYS, min_periods=WDAYS).min()
    k_m = _stoch_k(hi_m, lo_m, cl_w, 14)
    return ((k_d > 80.0) & (k_w > 80.0) & (k_m > 80.0)).astype(float).where(k_d.notna(), np.nan)


def f26_stwf_326_elder_force_index_2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder's Force Index = (close - close.shift(1)) * volume, EMA(2) — short-term volume-pressure measure."""
    fi = (close - close.shift(1)) * volume
    return _ema(fi, 2)


def f26_stwf_327_elder_force_index_13(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder's Force Index EMA(13) — intermediate-term volume-pressure measure."""
    fi = (close - close.shift(1)) * volume
    return _ema(fi, 13)


def f26_stwf_328_elder_force_index_div_vs_price_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish divergence: close at 63d new high but Force Index EMA(13) below 63d max — buying pressure waning."""
    fi13 = _ema((close - close.shift(1)) * volume, 13)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    fi_max = fi13.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((fi13 < fi_max) & p_new).astype(float).where(fi13.notna() & p_new, np.nan)


def f26_stwf_329_worden_4_stoch_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Worden 4 stoch consensus: count of K(5), K(14), K(21), K(50) > 80 — multi-period stoch alignment."""
    k5 = _stoch_k(high, low, close, 5)
    k14 = _stoch_k(high, low, close, 14)
    k21 = _stoch_k(high, low, close, 21)
    k50 = _stoch_k(high, low, close, 50)
    cnt = ((k5 > 80.0).astype(float).fillna(0)
           + (k14 > 80.0).astype(float).fillna(0)
           + (k21 > 80.0).astype(float).fillna(0)
           + (k50 > 80.0).astype(float).fillna(0))
    return cnt.where(k50.notna(), np.nan)


def f26_stwf_330_worden_4_stoch_all_above_80_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(5), K(14), K(21), K(50) all > 80 — Worden's stretched-market signal."""
    k5 = _stoch_k(high, low, close, 5)
    k14 = _stoch_k(high, low, close, 14)
    k21 = _stoch_k(high, low, close, 21)
    k50 = _stoch_k(high, low, close, 50)
    return ((k5 > 80.0) & (k14 > 80.0) & (k21 > 80.0) & (k50 > 80.0)).astype(float).where(k50.notna(), np.nan)


def f26_stwf_331_stoch_3_3_full_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classic full stoch 14,3,3: smooth K(14) by 3, then D = 3-bar mean. Returns K-D differential."""
    k_raw = _stoch_k(high, low, close, 14, smooth_k=1)
    k = k_raw.rolling(3, min_periods=2).mean()
    d = k.rolling(3, min_periods=2).mean()
    return k - d


def f26_stwf_332_stoch_8_3_5_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Alternative slow stoch 8,3,5: K(8) smoothed-3, D = 5-bar mean. Returns K-D differential."""
    k_raw = _stoch_k(high, low, close, 8, smooth_k=1)
    k = k_raw.rolling(3, min_periods=2).mean()
    d = k.rolling(5, min_periods=2).mean()
    return k - d


def f26_stwf_333_dorsey_relative_strength_proxy_self(close: pd.Series) -> pd.Series:
    """Dorsey RS proxy (vs own 252d avg): 100 * close / SMA(close, 252) — self-relative-strength."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return 100.0 * _safe_div(close, sma)


def f26_stwf_334_dorsey_rs_above_120_state(close: pd.Series) -> pd.Series:
    """1 if self-RS (100 * close / SMA252) > 120 — significantly above annual mean."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    rs = 100.0 * _safe_div(close, sma)
    return (rs > 120.0).astype(float).where(rs.notna(), np.nan)


def f26_stwf_335_dorsey_rs_dwell_above_120_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars self-RS > 120 — extended-from-annual-mean dwell."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    rs = 100.0 * _safe_div(close, sma)
    return (rs > 120.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(rs.notna(), np.nan)


# ============================================================
# Stuck-stock-specific failure signatures (336-355)
# ============================================================


def f26_stwf_336_stoch_chronic_ob_no_new_high_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K>80 for >40 of last 63 bars AND close NOT at 63d new high — chronic OB without progress."""
    k = _stoch_k(high, low, close, 14)
    ob_days = (k > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
    cond = (ob_days > 40.0) & (close < p_max)
    return cond.astype(float).where(ob_days.notna(), np.nan)


def f26_stwf_337_stoch_failing_to_new_high_with_price_extending(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price at 63d new high but Stoch K below median of historical OB-zone values — internal weakness."""
    k = _stoch_k(high, low, close, 14)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    # OB-zone median: median of K values when K>80 over 252d
    def _med_ob(w):
        v = w[~np.isnan(w)]
        ob = v[v > 80.0]
        if ob.size < 3:
            return np.nan
        return float(np.median(ob))
    med_ob = k.rolling(YDAYS, min_periods=QDAYS).apply(_med_ob, raw=True)
    return ((k < med_ob) & p_new).astype(float).where(med_ob.notna() & p_new, np.nan)


def f26_stwf_338_stoch_topping_range_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K oscillates in 70-90 range repeatedly over 63d without breakthrough above 95 — topping range pattern."""
    k = _stoch_k(high, low, close, 14)
    in_range = ((k >= 70.0) & (k <= 90.0)).astype(float)
    in_range_frac = in_range.rolling(QDAYS, min_periods=MDAYS).mean()
    breakthrough = (k > 95.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return ((in_range_frac > 0.5) & (breakthrough == 0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_339_stoch_repeated_ob_failures_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct OB entries (K crosses above 80) that did NOT reach 90 — failed-attempt count, 252d."""
    k = _stoch_k(high, low, close, 14)
    enter = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    # within each OB period (until K drops back below 80), did K reach 90?
    # Approx: for each enter, check next 21 bars (typical OB duration) for max > 90
    reach_90 = (k > 90.0).astype(float).rolling(MDAYS, min_periods=1).max()
    # NOTE: this is forward-looking. Use a backward proxy instead.
    # backward: at each bar, count enters in past 252 bars where the subsequent 21d max stayed <= 90
    # use shift to look at: enter at t-21, did k[t-20..t] never exceed 90?
    enters_shifted = enter.shift(MDAYS)
    # next-21-from-enter window max captured by rolling backward at the future bar
    max_next = k.rolling(MDAYS, min_periods=1).max()
    failed_at_t = (enters_shifted > 0) & (max_next <= 90.0)
    return failed_at_t.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_340_stoch_failure_after_blow_off_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K reached >95 in past 21 bars AND now K < 50 — extreme OB then sharp decline."""
    k = _stoch_k(high, low, close, 14)
    blow_off = (k > 95.0).astype(float).rolling(MDAYS, min_periods=1).max()
    return ((blow_off > 0) & (k < 50.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_341_stoch_distribution_zone_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distribution zone: K dwells in 60-80 with declining 21d max over 63d — accumulation->distribution transition."""
    k = _stoch_k(high, low, close, 14)
    in_zone = ((k >= 60.0) & (k <= 80.0)).astype(float)
    dwell = in_zone.rolling(QDAYS, min_periods=MDAYS).mean()
    k21_max = k.rolling(MDAYS, min_periods=WDAYS).max()
    slope = _rolling_slope(k21_max, QDAYS, min_periods=MDAYS)
    return ((dwell > 0.4) & (slope < 0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_342_stoch_apathy_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Apathy: K < 50 dwell > 0.6 AND realized vol in lowest tercile — stuck-in-low-energy regime."""
    k = _stoch_k(high, low, close, 14)
    dwell_low = (k < 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    vol_q33 = vol.rolling(YDAYS, min_periods=QDAYS).quantile(0.33)
    return ((dwell_low > 0.6) & (vol < vol_q33)).astype(float).where(vol_q33.notna(), np.nan)


def f26_stwf_343_stoch_decay_after_peak_velocity_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Velocity of K decay after recent 21d K-peak: (K - K_peak_21) / bars_since_peak."""
    k = _stoch_k(high, low, close, 14)
    k_peak = k.rolling(MDAYS, min_periods=WDAYS).max()
    bars = _bars_since_true(k >= k_peak)
    return _safe_div(k - k_peak, bars.where(bars > 0, np.nan))


def f26_stwf_344_stoch_lower_high_count_in_ob_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of OB peaks (K>80) in past 252d that were LOWER than the prior OB peak — distribution top sequence."""
    k = _stoch_k(high, low, close, 14)
    # OB peaks: K crosses above 80 then peaks then crosses below 80; approximate as local maxima above 80
    is_peak = (k.shift(1) > k.shift(2)) & (k.shift(1) > k) & (k.shift(1) > 80.0)
    # lower-than-prior-peak count: at each peak, was its value lower than the max of all peaks in prior 63d?
    # Approx: count where peak value < cumulative-252d-prior peak max
    peak_val = k.shift(1).where(is_peak, np.nan)
    prior_max = peak_val.shift(1).rolling(YDAYS, min_periods=MDAYS).max()
    lower = (peak_val < prior_max).astype(float)
    return lower.rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_345_stoch_consecutive_failed_breakouts_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of consecutive K-breakouts above 80 that failed (didn't reach 90) in past 63d."""
    k = _stoch_k(high, low, close, 14)
    enter = ((k.shift(1) <= 80.0) & (k > 80.0))
    enter_then_max = enter.astype(float)
    # for each enter, check if next 10 bars hit > 90 (backward proxy: enter at t-10, max(k[t-9..t]) <= 90)
    enters_shifted = enter.shift(10).astype(float)
    max_next = k.rolling(10, min_periods=1).max()
    failed = (enters_shifted > 0) & (max_next <= 90.0)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_346_stoch_at_top_with_williams_failure_alignment(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) > 80 AND Williams %R(14) < -50 simultaneously — divergence between stoch and WR (failure alignment)."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    return ((k > 80.0) & (wr < -50.0)).astype(float).where(k.notna() & wr.notna(), np.nan)


def f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 252d close-peak happened in past 63d AND K dwells < 50 for > 0.5 of subsequent bars."""
    p_peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (close >= p_peak)
    bars_since_peak = _bars_since_true(is_peak)
    k = _stoch_k(high, low, close, 14)
    low_dwell = (k < 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return ((bars_since_peak <= QDAYS) & (bars_since_peak > MDAYS) & (low_dwell > 0.5)).astype(float).where(k.notna(), np.nan)


def f26_stwf_348_multi_oscillator_failure_stack_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators {stoch, williams, srsi, UO, SMI} in failure mode (price at 63d high, osc < own 63d max)."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    # UO simplified: weighted avg of bp ratios
    bp = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    a7 = bp.rolling(7, min_periods=3).sum() / tr.rolling(7, min_periods=3).sum().replace(0, np.nan)
    a14 = bp.rolling(14, min_periods=5).sum() / tr.rolling(14, min_periods=5).sum().replace(0, np.nan)
    a28 = bp.rolling(28, min_periods=10).sum() / tr.rolling(28, min_periods=10).sum().replace(0, np.nan)
    uo = 100.0 * (4 * a7 + 2 * a14 + a28) / 7.0
    # SMI simplified
    mid = (high.rolling(14, min_periods=5).max() + low.rolling(14, min_periods=5).min()) / 2.0
    diff = close - mid
    hl = high.rolling(14, min_periods=5).max() - low.rolling(14, min_periods=5).min()
    smi = 100.0 * _safe_div(_ema(_ema(diff, 3), 3), 0.5 * _ema(_ema(hl, 3), 3))
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for osc in (k, wr, sk, uo, smi):
        omax = osc.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        fail = ((osc < omax) & p_new).astype(float).fillna(0)
        cnt = cnt + fail
    return cnt.where(p_new, np.nan)


def f26_stwf_349_multi_oscillator_topping_consensus_at_252h(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d close-high: count of {K, WR, SRSI, momentum} in OB (top quartile of their range)."""
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    mom = (close / close.shift(21) - 1.0)
    mom_pr = _pct_rank(mom, YDAYS, min_periods=QDAYS) * 100.0
    cnt = ((k > 80.0).astype(float).fillna(0)
           + (wr > -20.0).astype(float).fillna(0)
           + (sk > 80.0).astype(float).fillna(0)
           + (mom_pr > 75.0).astype(float).fillna(0))
    return cnt.where(is_top, np.nan)


def f26_stwf_350_oscillator_failure_persistence_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252d where multi-osc failure regime is true (>=3 of 5 oscillators in failure mode)."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    bp = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    a7 = bp.rolling(7, min_periods=3).sum() / tr.rolling(7, min_periods=3).sum().replace(0, np.nan)
    a14 = bp.rolling(14, min_periods=5).sum() / tr.rolling(14, min_periods=5).sum().replace(0, np.nan)
    a28 = bp.rolling(28, min_periods=10).sum() / tr.rolling(28, min_periods=10).sum().replace(0, np.nan)
    uo = 100.0 * (4 * a7 + 2 * a14 + a28) / 7.0
    mid = (high.rolling(14, min_periods=5).max() + low.rolling(14, min_periods=5).min()) / 2.0
    diff = close - mid
    hl = high.rolling(14, min_periods=5).max() - low.rolling(14, min_periods=5).min()
    smi = 100.0 * _safe_div(_ema(_ema(diff, 3), 3), 0.5 * _ema(_ema(hl, 3), 3))
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for osc in (k, wr, sk, uo, smi):
        omax = osc.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        fail = ((osc < omax) & p_new).astype(float).fillna(0)
        cnt = cnt + fail
    regime = (cnt >= 3).astype(float)
    return regime.rolling(YDAYS, min_periods=QDAYS).mean().where(close.notna(), np.nan)


def f26_stwf_351_stoch_distribution_topping_signal_combined(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Combined: K in 60-80 AND 21d K-max declining AND close at 63d new high — distribution topping signal."""
    k = _stoch_k(high, low, close, 14)
    in_zone = ((k >= 60.0) & (k <= 80.0))
    k21_max = k.rolling(MDAYS, min_periods=WDAYS).max()
    slope = _rolling_slope(k21_max, QDAYS, min_periods=MDAYS)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    return (in_zone & (slope < 0) & p_new).astype(float).where(k.notna(), np.nan)


def f26_stwf_352_stoch_capitulation_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K breaks below 20 within 5 bars after being > 80 — sharp capitulation indicator."""
    k = _stoch_k(high, low, close, 14)
    ob_recent = (k.shift(1) > 80.0).astype(float).rolling(5, min_periods=1).max()
    return ((ob_recent > 0) & (k < 20.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of capitulation events (K<20 after recent OB) in past 63d where K failed to return > 60 within 10 bars."""
    k = _stoch_k(high, low, close, 14)
    ob_recent = (k.shift(1) > 80.0).astype(float).rolling(5, min_periods=1).max()
    cap = (ob_recent > 0) & (k < 20.0)
    # was the recovery failed: at t, check cap at t-10 and that k didn't exceed 60 in t-9..t
    cap_shifted = cap.shift(10).astype(float)
    max_next = k.rolling(10, min_periods=1).max()
    failed = (cap_shifted > 0) & (max_next <= 60.0)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_354_stoch_stuck_low_regime_persistence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K < 30 for > 40 of past 63 bars — stuck-low regime (post-breakdown weakness)."""
    k = _stoch_k(high, low, close, 14)
    cnt = (k < 30.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt > 40.0).astype(float).where(cnt.notna(), np.nan)


def f26_stwf_355_stoch_drift_decay_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Negative drift score: linear regression slope of K(14) over 252 bars — measures multi-quarter K decay trend."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_slope(k, YDAYS, min_periods=QDAYS)


# ============================================================
# ML-orthogonal complexity / entropy (356-375)
# ============================================================


def f26_stwf_356_stoch_sample_entropy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sample entropy SampEn(m=2, r=0.2*std) of stoch K(14) over rolling 21d window."""
    k = _stoch_k(high, low, close, 14)
    return _sample_entropy(k, MDAYS, m=2, r_frac=0.2)


def f26_stwf_357_stoch_sample_entropy_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sample entropy SampEn(m=2, r=0.2*std) of stoch K(14) over rolling 63d window."""
    k = _stoch_k(high, low, close, 14)
    return _sample_entropy(k, QDAYS, m=2, r_frac=0.2)


def f26_stwf_358_stoch_approximate_entropy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Approximate entropy ApEn(m=2, r=0.2*std) of stoch K(14) over rolling 21d window."""
    k = _stoch_k(high, low, close, 14)
    return _approx_entropy(k, MDAYS, m=2, r_frac=0.2)


def f26_stwf_359_stoch_permutation_entropy_21d_order3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Permutation entropy (order=3) of stoch K(14) over rolling 21d window."""
    k = _stoch_k(high, low, close, 14)
    return _perm_entropy(k, MDAYS, order=3)


def f26_stwf_360_stoch_permutation_entropy_63d_order3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Permutation entropy (order=3) of stoch K(14) over rolling 63d window."""
    k = _stoch_k(high, low, close, 14)
    return _perm_entropy(k, QDAYS, order=3)


def f26_stwf_361_stoch_multiscale_entropy_scale2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multiscale entropy at scale 2: SampEn on coarse-grained K(14) (2-bar block mean)."""
    k = _stoch_k(high, low, close, 14)
    cg = _multiscale_coarsegrain(k, scale=2)
    return _sample_entropy(cg, QDAYS, m=2, r_frac=0.2)


def f26_stwf_362_stoch_multiscale_entropy_scale5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multiscale entropy at scale 5: SampEn on coarse-grained K(14) (5-bar block mean)."""
    k = _stoch_k(high, low, close, 14)
    cg = _multiscale_coarsegrain(k, scale=5)
    return _sample_entropy(cg, QDAYS, m=2, r_frac=0.2)


def f26_stwf_363_stoch_fractal_dimension_higuchi_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of stoch K(14) over rolling 63d window — D in [1, 2]."""
    k = _stoch_k(high, low, close, 14)
    return _higuchi_fd(k, QDAYS, kmax=4)


def f26_stwf_364_stoch_fractal_dimension_petrosian_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of stoch K(14) over rolling 21d window."""
    k = _stoch_k(high, low, close, 14)
    return _petrosian_fd(k, MDAYS)


def f26_stwf_365_stoch_hurst_exponent_rs_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of stoch K(14) over rolling 63d window — H>0.5 = persistent, H<0.5 = anti-persistent."""
    k = _stoch_k(high, low, close, 14)
    return _hurst_rs(k, QDAYS)


def f26_stwf_366_stoch_hurst_exponent_dfa_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DFA Hurst exponent of stoch K(14) over rolling 252d window."""
    k = _stoch_k(high, low, close, 14)
    return _dfa_hurst(k, YDAYS)


def f26_stwf_367_stoch_recurrence_rate_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recurrence rate (RQA) of stoch K(14) over rolling 21d window with epsilon = 10% of range."""
    k = _stoch_k(high, low, close, 14)
    return _recurrence_rate(k, MDAYS, eps_frac=0.1)


def f26_stwf_368_stoch_recurrence_determinism_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recurrence determinism (RQA) of stoch K(14) over rolling 21d window — fraction in diagonal lines."""
    k = _stoch_k(high, low, close, 14)
    return _recurrence_determinism(k, MDAYS, eps_frac=0.1, lmin=2)


def f26_stwf_369_stoch_lempel_ziv_complexity_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lempel-Ziv complexity (normalized) of discretized stoch K(14) over rolling 63d window."""
    k = _stoch_k(high, low, close, 14)
    return _lempel_ziv(k, QDAYS, n_levels=4)


def f26_stwf_370_stoch_kolmogorov_complexity_proxy_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kolmogorov complexity proxy: compression ratio via run-length encoding of discretized K(14), 63d window."""
    k = _stoch_k(high, low, close, 14)
    def _kc(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        # discretize into 4 bins
        qs = np.quantile(v, [0.25, 0.5, 0.75])
        sym = np.searchsorted(qs, v).astype(int)
        # run-length encode
        rle_len = 1
        for i in range(1, sym.size):
            if sym[i] != sym[i - 1]:
                rle_len += 1
        return float(rle_len) / float(sym.size)
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_kc, raw=True)


def f26_stwf_371_stoch_persistence_index_rs_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-horizon R/S persistence index of stoch K(14) over rolling 21d window."""
    k = _stoch_k(high, low, close, 14)
    return _hurst_rs(k, MDAYS)


def f26_stwf_372_stoch_information_dimension_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Information dimension proxy: D_1 = lim eps->0 of -H(eps)/log(eps), approximated at 2 scales, 63d."""
    k = _stoch_k(high, low, close, 14)
    def _id(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        scales = [0.05, 0.1]
        H = []
        for eps_f in scales:
            rng = v.max() - v.min()
            if rng <= 0:
                return np.nan
            eps = eps_f * rng
            bins = max(2, int(np.ceil(rng / eps)))
            edges = np.linspace(v.min(), v.max() + 1e-9, bins + 1)
            hist, _ = np.histogram(v, bins=edges)
            p = hist[hist > 0] / float(hist.sum())
            ent = -float((p * np.log(p)).sum())
            H.append((np.log(eps_f), ent))
        if len(H) < 2:
            return np.nan
        xs = np.array([p[0] for p in H])
        ys = np.array([p[1] for p in H])
        xm = xs.mean(); ym = ys.mean()
        num = ((xs - xm) * (ys - ym)).sum()
        den = ((xs - xm) ** 2).sum()
        return -(num / den) if den > 0 else np.nan
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_id, raw=True)


def f26_stwf_373_stoch_correlation_dimension_proxy_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Correlation dimension proxy: log(C(eps)) / log(eps) slope at 2 scales of pairwise distances, 63d."""
    k = _stoch_k(high, low, close, 14)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        rng = v.max() - v.min()
        if rng <= 0:
            return np.nan
        # pairwise distances on embed dim 2
        m = 2
        N = v.size - m + 1
        embed = np.array([v[i:i + m] for i in range(N)])
        dists = []
        for i in range(N):
            for j in range(i + 1, N):
                dists.append(np.max(np.abs(embed[i] - embed[j])))
        if len(dists) < 4:
            return np.nan
        dists = np.array(dists)
        pts = []
        for eps_f in (0.05, 0.1):
            eps = eps_f * rng
            C = float((dists < eps).sum()) / float(dists.size)
            if C > 0:
                pts.append((np.log(eps_f), np.log(C)))
        if len(pts) < 2:
            return np.nan
        xs = np.array([p[0] for p in pts])
        ys = np.array([p[1] for p in pts])
        xm = xs.mean(); ym = ys.mean()
        num = ((xs - xm) * (ys - ym)).sum()
        den = ((xs - xm) ** 2).sum()
        return num / den if den > 0 else np.nan
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_cd, raw=True)


def f26_stwf_374_stoch_lyapunov_proxy_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lyapunov-like sensitivity proxy: avg log-distance growth rate between neighbor trajectories over 63d."""
    k = _stoch_k(high, low, close, 14)
    def _ly(w):
        v = w[~np.isnan(w)]
        if v.size < 12:
            return np.nan
        steps = 4
        N = v.size - steps - 1
        if N < 4:
            return np.nan
        rates = []
        for i in range(N):
            # find nearest neighbor (excluding self), then track divergence
            d0 = np.abs(v - v[i])
            d0[i] = np.inf
            if i + steps >= v.size:
                continue
            nn = int(np.argmin(d0[:v.size - steps]))
            if nn == i or nn + steps >= v.size:
                continue
            ini = abs(v[i] - v[nn])
            fin = abs(v[i + steps] - v[nn + steps])
            if ini > 1e-9 and fin > 0:
                rates.append(np.log(fin / ini) / steps)
        if len(rates) < 2:
            return np.nan
        return float(np.mean(rates))
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_ly, raw=True)


def f26_stwf_375_stoch_predictability_horizon_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Predictability horizon: smallest lag at which autocorr(K(14)) drops below 0.5, computed over 63d."""
    k = _stoch_k(high, low, close, 14)
    def _ph(w):
        v = w[~np.isnan(w)]
        if v.size < 12:
            return np.nan
        for lag in range(1, min(15, v.size - 4)):
            a = v[:-lag]; b = v[lag:]
            am = a.mean(); bm = b.mean()
            num = ((a - am) * (b - bm)).sum()
            da = np.sqrt(((a - am) ** 2).sum())
            db = np.sqrt(((b - bm) ** 2).sum())
            if da == 0 or db == 0:
                continue
            ac = num / (da * db)
            if ac < 0.5:
                return float(lag)
        return float(min(15, v.size - 4))
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_ph, raw=True)


# ============================================================
#                         REGISTRY 301-375
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_BASE_REGISTRY_301_375 = {
    "f26_stwf_301_vw_stoch_k_14": {"inputs": ["close", "volume"], "func": f26_stwf_301_vw_stoch_k_14},
    "f26_stwf_302_vw_stoch_d_14": {"inputs": ["close", "volume"], "func": f26_stwf_302_vw_stoch_d_14},
    "f26_stwf_303_vw_williams_r_14": {"inputs": ["close", "volume"], "func": f26_stwf_303_vw_williams_r_14},
    "f26_stwf_304_money_flow_stoch_14": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_304_money_flow_stoch_14},
    "f26_stwf_305_vw_stoch_above_80_state": {"inputs": ["close", "volume"], "func": f26_stwf_305_vw_stoch_above_80_state},
    "f26_stwf_306_vw_stoch_div_vs_price_63": {"inputs": ["close", "volume"], "func": f26_stwf_306_vw_stoch_div_vs_price_63},
    "f26_stwf_307_vw_stoch_just_exited_above_80": {"inputs": ["close", "volume"], "func": f26_stwf_307_vw_stoch_just_exited_above_80},
    "f26_stwf_308_vw_williams_r_above_minus20_state": {"inputs": ["close", "volume"], "func": f26_stwf_308_vw_williams_r_above_minus20_state},
    "f26_stwf_309_vw_williams_r_dwell_above_minus20_63": {"inputs": ["close", "volume"], "func": f26_stwf_309_vw_williams_r_dwell_above_minus20_63},
    "f26_stwf_310_vw_stoch_bars_since_252_max": {"inputs": ["close", "volume"], "func": f26_stwf_310_vw_stoch_bars_since_252_max},
    "f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90": {"inputs": ["high", "low", "close"], "func": f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90},
    "f26_stwf_312_stoch_above_adaptive_ob_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_312_stoch_above_adaptive_ob_state},
    "f26_stwf_313_stoch_dwell_above_adaptive_ob_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_313_stoch_dwell_above_adaptive_ob_63},
    "f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d": {"inputs": ["high", "low", "close"], "func": f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d},
    "f26_stwf_315_williams_r_above_adaptive_ob_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_315_williams_r_above_adaptive_ob_state},
    "f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504": {"inputs": ["high", "low", "close"], "func": f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504},
    "f26_stwf_317_stoch_above_adaptive_extreme_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_317_stoch_above_adaptive_extreme_state},
    "f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold": {"inputs": ["high", "low", "close"], "func": f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold},
    "f26_stwf_319_vol_regime_adaptive_stoch_above_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_319_vol_regime_adaptive_stoch_above_state},
    "f26_stwf_320_stoch_threshold_breach_count_normalized_504": {"inputs": ["high", "low", "close"], "func": f26_stwf_320_stoch_threshold_breach_count_normalized_504},
    "f26_stwf_321_larry_williams_smash_day_pattern": {"inputs": ["high", "low", "close"], "func": f26_stwf_321_larry_williams_smash_day_pattern},
    "f26_stwf_322_demark_td_pressure_5": {"inputs": ["high", "low", "close"], "func": f26_stwf_322_demark_td_pressure_5},
    "f26_stwf_323_demark_td_pressure_above_82_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_323_demark_td_pressure_above_82_state},
    "f26_stwf_324_demark_td_pressure_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_324_demark_td_pressure_div_vs_price_63},
    "f26_stwf_325_elder_triple_screen_consensus": {"inputs": ["high", "low", "close"], "func": f26_stwf_325_elder_triple_screen_consensus},
    "f26_stwf_326_elder_force_index_2": {"inputs": ["close", "volume"], "func": f26_stwf_326_elder_force_index_2},
    "f26_stwf_327_elder_force_index_13": {"inputs": ["close", "volume"], "func": f26_stwf_327_elder_force_index_13},
    "f26_stwf_328_elder_force_index_div_vs_price_63": {"inputs": ["close", "volume"], "func": f26_stwf_328_elder_force_index_div_vs_price_63},
    "f26_stwf_329_worden_4_stoch_consensus": {"inputs": ["high", "low", "close"], "func": f26_stwf_329_worden_4_stoch_consensus},
    "f26_stwf_330_worden_4_stoch_all_above_80_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_330_worden_4_stoch_all_above_80_state},
    "f26_stwf_331_stoch_3_3_full_pattern": {"inputs": ["high", "low", "close"], "func": f26_stwf_331_stoch_3_3_full_pattern},
    "f26_stwf_332_stoch_8_3_5_pattern": {"inputs": ["high", "low", "close"], "func": f26_stwf_332_stoch_8_3_5_pattern},
    "f26_stwf_333_dorsey_relative_strength_proxy_self": {"inputs": ["close"], "func": f26_stwf_333_dorsey_relative_strength_proxy_self},
    "f26_stwf_334_dorsey_rs_above_120_state": {"inputs": ["close"], "func": f26_stwf_334_dorsey_rs_above_120_state},
    "f26_stwf_335_dorsey_rs_dwell_above_120_63": {"inputs": ["close"], "func": f26_stwf_335_dorsey_rs_dwell_above_120_63},
    "f26_stwf_336_stoch_chronic_ob_no_new_high_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_336_stoch_chronic_ob_no_new_high_63},
    "f26_stwf_337_stoch_failing_to_new_high_with_price_extending": {"inputs": ["high", "low", "close"], "func": f26_stwf_337_stoch_failing_to_new_high_with_price_extending},
    "f26_stwf_338_stoch_topping_range_indicator_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_338_stoch_topping_range_indicator_63},
    "f26_stwf_339_stoch_repeated_ob_failures_count_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_339_stoch_repeated_ob_failures_count_252},
    "f26_stwf_340_stoch_failure_after_blow_off_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_340_stoch_failure_after_blow_off_indicator},
    "f26_stwf_341_stoch_distribution_zone_indicator_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_341_stoch_distribution_zone_indicator_63},
    "f26_stwf_342_stoch_apathy_indicator_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_342_stoch_apathy_indicator_63},
    "f26_stwf_343_stoch_decay_after_peak_velocity_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_343_stoch_decay_after_peak_velocity_21},
    "f26_stwf_344_stoch_lower_high_count_in_ob_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_344_stoch_lower_high_count_in_ob_252},
    "f26_stwf_345_stoch_consecutive_failed_breakouts_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_345_stoch_consecutive_failed_breakouts_count_63},
    "f26_stwf_346_stoch_at_top_with_williams_failure_alignment": {"inputs": ["high", "low", "close"], "func": f26_stwf_346_stoch_at_top_with_williams_failure_alignment},
    "f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63},
    "f26_stwf_348_multi_oscillator_failure_stack_count": {"inputs": ["high", "low", "close"], "func": f26_stwf_348_multi_oscillator_failure_stack_count},
    "f26_stwf_349_multi_oscillator_topping_consensus_at_252h": {"inputs": ["high", "low", "close"], "func": f26_stwf_349_multi_oscillator_topping_consensus_at_252h},
    "f26_stwf_350_oscillator_failure_persistence_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_350_oscillator_failure_persistence_252},
    "f26_stwf_351_stoch_distribution_topping_signal_combined": {"inputs": ["high", "low", "close"], "func": f26_stwf_351_stoch_distribution_topping_signal_combined},
    "f26_stwf_352_stoch_capitulation_proxy": {"inputs": ["high", "low", "close"], "func": f26_stwf_352_stoch_capitulation_proxy},
    "f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63},
    "f26_stwf_354_stoch_stuck_low_regime_persistence": {"inputs": ["high", "low", "close"], "func": f26_stwf_354_stoch_stuck_low_regime_persistence},
    "f26_stwf_355_stoch_drift_decay_score_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_355_stoch_drift_decay_score_252},
    "f26_stwf_356_stoch_sample_entropy_21d": {"inputs": ["high", "low", "close"], "func": f26_stwf_356_stoch_sample_entropy_21d},
    "f26_stwf_357_stoch_sample_entropy_63d": {"inputs": ["high", "low", "close"], "func": f26_stwf_357_stoch_sample_entropy_63d},
    "f26_stwf_358_stoch_approximate_entropy_21d": {"inputs": ["high", "low", "close"], "func": f26_stwf_358_stoch_approximate_entropy_21d},
    "f26_stwf_359_stoch_permutation_entropy_21d_order3": {"inputs": ["high", "low", "close"], "func": f26_stwf_359_stoch_permutation_entropy_21d_order3},
    "f26_stwf_360_stoch_permutation_entropy_63d_order3": {"inputs": ["high", "low", "close"], "func": f26_stwf_360_stoch_permutation_entropy_63d_order3},
    "f26_stwf_361_stoch_multiscale_entropy_scale2": {"inputs": ["high", "low", "close"], "func": f26_stwf_361_stoch_multiscale_entropy_scale2},
    "f26_stwf_362_stoch_multiscale_entropy_scale5": {"inputs": ["high", "low", "close"], "func": f26_stwf_362_stoch_multiscale_entropy_scale5},
    "f26_stwf_363_stoch_fractal_dimension_higuchi_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_363_stoch_fractal_dimension_higuchi_63},
    "f26_stwf_364_stoch_fractal_dimension_petrosian_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_364_stoch_fractal_dimension_petrosian_21},
    "f26_stwf_365_stoch_hurst_exponent_rs_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_365_stoch_hurst_exponent_rs_63},
    "f26_stwf_366_stoch_hurst_exponent_dfa_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_366_stoch_hurst_exponent_dfa_252},
    "f26_stwf_367_stoch_recurrence_rate_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_367_stoch_recurrence_rate_21},
    "f26_stwf_368_stoch_recurrence_determinism_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_368_stoch_recurrence_determinism_21},
    "f26_stwf_369_stoch_lempel_ziv_complexity_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_369_stoch_lempel_ziv_complexity_63},
    "f26_stwf_370_stoch_kolmogorov_complexity_proxy_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_370_stoch_kolmogorov_complexity_proxy_63},
    "f26_stwf_371_stoch_persistence_index_rs_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_371_stoch_persistence_index_rs_21},
    "f26_stwf_372_stoch_information_dimension_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_372_stoch_information_dimension_63},
    "f26_stwf_373_stoch_correlation_dimension_proxy_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_373_stoch_correlation_dimension_proxy_63},
    "f26_stwf_374_stoch_lyapunov_proxy_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_374_stoch_lyapunov_proxy_63},
    "f26_stwf_375_stoch_predictability_horizon_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_375_stoch_predictability_horizon_63},
}
