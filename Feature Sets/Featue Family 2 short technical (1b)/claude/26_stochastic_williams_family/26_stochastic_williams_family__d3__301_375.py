import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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
    tp = (high + low + close) / 3.0
    return tp * volume


def _ulcer_vol_bucket(close, n=63):
    ret = close.pct_change()
    sd = ret.rolling(n, min_periods=max(n // 3, 2)).std()
    med = sd.rolling(YDAYS, min_periods=QDAYS).median()
    return (sd > med).astype(float)


def _hurst_rs(s, n):
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 16:
            return np.nan
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
    def _se(w):
        v = w[~np.isnan(w)]
        if v.size < (m + 2):
            return np.nan
        r = r_frac * v.std()
        if r <= 0:
            return np.nan
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
    return s.rolling(scale, min_periods=max(scale // 2, 1)).mean()


def _higuchi_fd(s, n, kmax=4):
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
    def _lz(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        qs = np.quantile(v, np.linspace(0, 1, n_levels + 1)[1:-1])
        symbols = np.searchsorted(qs, v).astype(int)
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


def f26_stwf_301_vw_stoch_k_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _vw_stoch_k(close, volume, n_vw=14, n_k=14)


def f26_stwf_302_vw_stoch_d_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return _stoch_d(k, 3)


def f26_stwf_303_vw_williams_r_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _vw_williams_r(close, volume, n_vw=14, n=14)


def f26_stwf_304_money_flow_stoch_14(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mf = _money_flow(high, low, close, volume)
    cmf = mf.rolling(MDAYS, min_periods=WDAYS).sum()
    ll = cmf.rolling(14, min_periods=5).min()
    hh = cmf.rolling(14, min_periods=5).max()
    return 100.0 * _safe_div(cmf - ll, hh - ll)


def f26_stwf_305_vw_stoch_above_80_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_306_vw_stoch_div_vs_price_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    k_max = k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((k < k_max) & p_new).astype(float).where(k.notna() & p_new, np.nan)


def f26_stwf_307_vw_stoch_just_exited_above_80(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    return ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_308_vw_williams_r_above_minus20_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    wr = _vw_williams_r(close, volume, n_vw=14, n=14)
    return (wr > -20.0).astype(float).where(wr.notna(), np.nan)


def f26_stwf_309_vw_williams_r_dwell_above_minus20_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    wr = _vw_williams_r(close, volume, n_vw=14, n=14)
    return (wr > -20.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(wr.notna(), np.nan)


def f26_stwf_310_vw_stoch_bars_since_252_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    k = _vw_stoch_k(close, volume, n_vw=14, n_k=14)
    rmax = k.rolling(YDAYS, min_periods=QDAYS).max()
    is_max = (k >= rmax) & rmax.notna()
    return _bars_since_true(is_max).where(k.notna(), np.nan)


def f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)


def f26_stwf_312_stoch_above_adaptive_ob_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_313_stoch_dwell_above_adaptive_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.90, min_periods=QDAYS)
    above = (k > thr).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean().where(thr.notna(), np.nan)


def f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    wr = _williams_r(high, low, close, 14)
    return _quantile_rolling(wr, DDAYS_2Y, 0.90, min_periods=QDAYS)


def f26_stwf_315_williams_r_above_adaptive_ob_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    wr = _williams_r(high, low, close, 14)
    thr = _quantile_rolling(wr, DDAYS_2Y, 0.90, min_periods=QDAYS)
    return (wr > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _quantile_rolling(k, DDAYS_2Y, 0.99, min_periods=QDAYS)


def f26_stwf_317_stoch_above_adaptive_extreme_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    thr = _quantile_rolling(k, DDAYS_2Y, 0.99, min_periods=QDAYS)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    vol_hi = _ulcer_vol_bucket(close, QDAYS)
    q85 = _quantile_rolling(k, DDAYS_2Y, 0.85, min_periods=QDAYS)
    q95 = _quantile_rolling(k, DDAYS_2Y, 0.95, min_periods=QDAYS)
    return q85.where(vol_hi == 0.0, q95).where(vol_hi.notna(), np.nan)


def f26_stwf_319_vol_regime_adaptive_stoch_above_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    vol_hi = _ulcer_vol_bucket(close, QDAYS)
    q85 = _quantile_rolling(k, DDAYS_2Y, 0.85, min_periods=QDAYS)
    q95 = _quantile_rolling(k, DDAYS_2Y, 0.95, min_periods=QDAYS)
    thr = q85.where(vol_hi == 0.0, q95)
    return (k > thr).astype(float).where(thr.notna(), np.nan)


def f26_stwf_320_stoch_threshold_breach_count_normalized_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    above = (k > 80.0).astype(float)
    cnt = above.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(cnt, 6.3)  # expected ~10% of 63 = 6.3


def f26_stwf_321_larry_williams_smash_day_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cond = (low < low.shift(1)) & (close > high.shift(1))
    return cond.astype(float).where(close.notna() & close.shift(1).notna(), np.nan)


def f26_stwf_322_demark_td_pressure_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    return 100.0 * _safe_div(num, den)


def f26_stwf_323_demark_td_pressure_above_82_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    p = 100.0 * _safe_div(num, den)
    return (p > 82.0).astype(float).where(p.notna(), np.nan)


def f26_stwf_324_demark_td_pressure_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    num = (close - low).rolling(5, min_periods=2).sum()
    den = (high - low).rolling(5, min_periods=2).sum()
    p = 100.0 * _safe_div(num, den)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    p_max = p.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p < p_max) & p_new).astype(float).where(p.notna() & p_new, np.nan)


def f26_stwf_325_elder_triple_screen_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    fi = (close - close.shift(1)) * volume
    return _ema(fi, 2)


def f26_stwf_327_elder_force_index_13(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = (close - close.shift(1)) * volume
    return _ema(fi, 13)


def f26_stwf_328_elder_force_index_div_vs_price_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi13 = _ema((close - close.shift(1)) * volume, 13)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    fi_max = fi13.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((fi13 < fi_max) & p_new).astype(float).where(fi13.notna() & p_new, np.nan)


def f26_stwf_329_worden_4_stoch_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    k5 = _stoch_k(high, low, close, 5)
    k14 = _stoch_k(high, low, close, 14)
    k21 = _stoch_k(high, low, close, 21)
    k50 = _stoch_k(high, low, close, 50)
    return ((k5 > 80.0) & (k14 > 80.0) & (k21 > 80.0) & (k50 > 80.0)).astype(float).where(k50.notna(), np.nan)


def f26_stwf_331_stoch_3_3_full_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k_raw = _stoch_k(high, low, close, 14, smooth_k=1)
    k = k_raw.rolling(3, min_periods=2).mean()
    d = k.rolling(3, min_periods=2).mean()
    return k - d


def f26_stwf_332_stoch_8_3_5_pattern(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k_raw = _stoch_k(high, low, close, 8, smooth_k=1)
    k = k_raw.rolling(3, min_periods=2).mean()
    d = k.rolling(5, min_periods=2).mean()
    return k - d


def f26_stwf_333_dorsey_relative_strength_proxy_self(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return 100.0 * _safe_div(close, sma)


def f26_stwf_334_dorsey_rs_above_120_state(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    rs = 100.0 * _safe_div(close, sma)
    return (rs > 120.0).astype(float).where(rs.notna(), np.nan)


def f26_stwf_335_dorsey_rs_dwell_above_120_63(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    rs = 100.0 * _safe_div(close, sma)
    return (rs > 120.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(rs.notna(), np.nan)


def f26_stwf_336_stoch_chronic_ob_no_new_high_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    ob_days = (k > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
    cond = (ob_days > 40.0) & (close < p_max)
    return cond.astype(float).where(ob_days.notna(), np.nan)


def f26_stwf_337_stoch_failing_to_new_high_with_price_extending(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    def _med_ob(w):
        v = w[~np.isnan(w)]
        ob = v[v > 80.0]
        if ob.size < 3:
            return np.nan
        return float(np.median(ob))
    med_ob = k.rolling(YDAYS, min_periods=QDAYS).apply(_med_ob, raw=True)
    return ((k < med_ob) & p_new).astype(float).where(med_ob.notna() & p_new, np.nan)


def f26_stwf_338_stoch_topping_range_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    in_range = ((k >= 70.0) & (k <= 90.0)).astype(float)
    in_range_frac = in_range.rolling(QDAYS, min_periods=MDAYS).mean()
    breakthrough = (k > 95.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return ((in_range_frac > 0.5) & (breakthrough == 0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_339_stoch_repeated_ob_failures_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    enter = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    reach_90 = (k > 90.0).astype(float).rolling(MDAYS, min_periods=1).max()
    enters_shifted = enter.shift(MDAYS)
    max_next = k.rolling(MDAYS, min_periods=1).max()
    failed_at_t = (enters_shifted > 0) & (max_next <= 90.0)
    return failed_at_t.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_340_stoch_failure_after_blow_off_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    blow_off = (k > 95.0).astype(float).rolling(MDAYS, min_periods=1).max()
    return ((blow_off > 0) & (k < 50.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_341_stoch_distribution_zone_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    in_zone = ((k >= 60.0) & (k <= 80.0)).astype(float)
    dwell = in_zone.rolling(QDAYS, min_periods=MDAYS).mean()
    k21_max = k.rolling(MDAYS, min_periods=WDAYS).max()
    slope = _rolling_slope(k21_max, QDAYS, min_periods=MDAYS)
    return ((dwell > 0.4) & (slope < 0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_342_stoch_apathy_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    dwell_low = (k < 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    vol = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    vol_q33 = vol.rolling(YDAYS, min_periods=QDAYS).quantile(0.33)
    return ((dwell_low > 0.6) & (vol < vol_q33)).astype(float).where(vol_q33.notna(), np.nan)


def f26_stwf_343_stoch_decay_after_peak_velocity_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    k_peak = k.rolling(MDAYS, min_periods=WDAYS).max()
    bars = _bars_since_true(k >= k_peak)
    return _safe_div(k - k_peak, bars.where(bars > 0, np.nan))


def f26_stwf_344_stoch_lower_high_count_in_ob_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    is_peak = (k.shift(1) > k.shift(2)) & (k.shift(1) > k) & (k.shift(1) > 80.0)
    peak_val = k.shift(1).where(is_peak, np.nan)
    prior_max = peak_val.shift(1).rolling(YDAYS, min_periods=MDAYS).max()
    lower = (peak_val < prior_max).astype(float)
    return lower.rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_345_stoch_consecutive_failed_breakouts_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    enter = ((k.shift(1) <= 80.0) & (k > 80.0))
    enter_then_max = enter.astype(float)
    enters_shifted = enter.shift(10).astype(float)
    max_next = k.rolling(10, min_periods=1).max()
    failed = (enters_shifted > 0) & (max_next <= 90.0)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_346_stoch_at_top_with_williams_failure_alignment(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    return ((k > 80.0) & (wr < -50.0)).astype(float).where(k.notna() & wr.notna(), np.nan)


def f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (close >= p_peak)
    bars_since_peak = _bars_since_true(is_peak)
    k = _stoch_k(high, low, close, 14)
    low_dwell = (k < 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return ((bars_since_peak <= QDAYS) & (bars_since_peak > MDAYS) & (low_dwell > 0.5)).astype(float).where(k.notna(), np.nan)


def f26_stwf_348_multi_oscillator_failure_stack_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    return cnt.where(p_new, np.nan)


def f26_stwf_349_multi_oscillator_topping_consensus_at_252h(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    k = _stoch_k(high, low, close, 14)
    in_zone = ((k >= 60.0) & (k <= 80.0))
    k21_max = k.rolling(MDAYS, min_periods=WDAYS).max()
    slope = _rolling_slope(k21_max, QDAYS, min_periods=MDAYS)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    return (in_zone & (slope < 0) & p_new).astype(float).where(k.notna(), np.nan)


def f26_stwf_352_stoch_capitulation_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    ob_recent = (k.shift(1) > 80.0).astype(float).rolling(5, min_periods=1).max()
    return ((ob_recent > 0) & (k < 20.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    ob_recent = (k.shift(1) > 80.0).astype(float).rolling(5, min_periods=1).max()
    cap = (ob_recent > 0) & (k < 20.0)
    cap_shifted = cap.shift(10).astype(float)
    max_next = k.rolling(10, min_periods=1).max()
    failed = (cap_shifted > 0) & (max_next <= 60.0)
    return failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_354_stoch_stuck_low_regime_persistence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    cnt = (k < 30.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt > 40.0).astype(float).where(cnt.notna(), np.nan)


def f26_stwf_355_stoch_drift_decay_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _rolling_slope(k, YDAYS, min_periods=QDAYS)


def f26_stwf_356_stoch_sample_entropy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _sample_entropy(k, MDAYS, m=2, r_frac=0.2)


def f26_stwf_357_stoch_sample_entropy_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _sample_entropy(k, QDAYS, m=2, r_frac=0.2)


def f26_stwf_358_stoch_approximate_entropy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _approx_entropy(k, MDAYS, m=2, r_frac=0.2)


def f26_stwf_359_stoch_permutation_entropy_21d_order3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _perm_entropy(k, MDAYS, order=3)


def f26_stwf_360_stoch_permutation_entropy_63d_order3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _perm_entropy(k, QDAYS, order=3)


def f26_stwf_361_stoch_multiscale_entropy_scale2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    cg = _multiscale_coarsegrain(k, scale=2)
    return _sample_entropy(cg, QDAYS, m=2, r_frac=0.2)


def f26_stwf_362_stoch_multiscale_entropy_scale5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    cg = _multiscale_coarsegrain(k, scale=5)
    return _sample_entropy(cg, QDAYS, m=2, r_frac=0.2)


def f26_stwf_363_stoch_fractal_dimension_higuchi_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _higuchi_fd(k, QDAYS, kmax=4)


def f26_stwf_364_stoch_fractal_dimension_petrosian_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _petrosian_fd(k, MDAYS)


def f26_stwf_365_stoch_hurst_exponent_rs_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _hurst_rs(k, QDAYS)


def f26_stwf_366_stoch_hurst_exponent_dfa_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _dfa_hurst(k, YDAYS)


def f26_stwf_367_stoch_recurrence_rate_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _recurrence_rate(k, MDAYS, eps_frac=0.1)


def f26_stwf_368_stoch_recurrence_determinism_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _recurrence_determinism(k, MDAYS, eps_frac=0.1, lmin=2)


def f26_stwf_369_stoch_lempel_ziv_complexity_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _lempel_ziv(k, QDAYS, n_levels=4)


def f26_stwf_370_stoch_kolmogorov_complexity_proxy_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    def _kc(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        qs = np.quantile(v, [0.25, 0.5, 0.75])
        sym = np.searchsorted(qs, v).astype(int)
        rle_len = 1
        for i in range(1, sym.size):
            if sym[i] != sym[i - 1]:
                rle_len += 1
        return float(rle_len) / float(sym.size)
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_kc, raw=True)


def f26_stwf_371_stoch_persistence_index_rs_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    return _hurst_rs(k, MDAYS)


def f26_stwf_372_stoch_information_dimension_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    k = _stoch_k(high, low, close, 14)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        rng = v.max() - v.min()
        if rng <= 0:
            return np.nan
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


def f26_stwf_301_vw_stoch_k_14_d3(close, volume):
    return f26_stwf_301_vw_stoch_k_14(close, volume).diff().diff().diff()


def f26_stwf_302_vw_stoch_d_14_d3(close, volume):
    return f26_stwf_302_vw_stoch_d_14(close, volume).diff().diff().diff()


def f26_stwf_303_vw_williams_r_14_d3(close, volume):
    return f26_stwf_303_vw_williams_r_14(close, volume).diff().diff().diff()


def f26_stwf_304_money_flow_stoch_14_d3(high, low, close, volume):
    return f26_stwf_304_money_flow_stoch_14(high, low, close, volume).diff().diff().diff()


def f26_stwf_305_vw_stoch_above_80_state_d3(close, volume):
    return f26_stwf_305_vw_stoch_above_80_state(close, volume).diff().diff().diff()


def f26_stwf_306_vw_stoch_div_vs_price_63_d3(close, volume):
    return f26_stwf_306_vw_stoch_div_vs_price_63(close, volume).diff().diff().diff()


def f26_stwf_307_vw_stoch_just_exited_above_80_d3(close, volume):
    return f26_stwf_307_vw_stoch_just_exited_above_80(close, volume).diff().diff().diff()


def f26_stwf_308_vw_williams_r_above_minus20_state_d3(close, volume):
    return f26_stwf_308_vw_williams_r_above_minus20_state(close, volume).diff().diff().diff()


def f26_stwf_309_vw_williams_r_dwell_above_minus20_63_d3(close, volume):
    return f26_stwf_309_vw_williams_r_dwell_above_minus20_63(close, volume).diff().diff().diff()


def f26_stwf_310_vw_stoch_bars_since_252_max_d3(close, volume):
    return f26_stwf_310_vw_stoch_bars_since_252_max(close, volume).diff().diff().diff()


def f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90_d3(high, low, close):
    return f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90(high, low, close).diff().diff().diff()


def f26_stwf_312_stoch_above_adaptive_ob_state_d3(high, low, close):
    return f26_stwf_312_stoch_above_adaptive_ob_state(high, low, close).diff().diff().diff()


def f26_stwf_313_stoch_dwell_above_adaptive_ob_63_d3(high, low, close):
    return f26_stwf_313_stoch_dwell_above_adaptive_ob_63(high, low, close).diff().diff().diff()


def f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d_d3(high, low, close):
    return f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d(high, low, close).diff().diff().diff()


def f26_stwf_315_williams_r_above_adaptive_ob_state_d3(high, low, close):
    return f26_stwf_315_williams_r_above_adaptive_ob_state(high, low, close).diff().diff().diff()


def f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504_d3(high, low, close):
    return f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504(high, low, close).diff().diff().diff()


def f26_stwf_317_stoch_above_adaptive_extreme_state_d3(high, low, close):
    return f26_stwf_317_stoch_above_adaptive_extreme_state(high, low, close).diff().diff().diff()


def f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold_d3(high, low, close):
    return f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold(high, low, close).diff().diff().diff()


def f26_stwf_319_vol_regime_adaptive_stoch_above_state_d3(high, low, close):
    return f26_stwf_319_vol_regime_adaptive_stoch_above_state(high, low, close).diff().diff().diff()


def f26_stwf_320_stoch_threshold_breach_count_normalized_504_d3(high, low, close):
    return f26_stwf_320_stoch_threshold_breach_count_normalized_504(high, low, close).diff().diff().diff()


def f26_stwf_321_larry_williams_smash_day_pattern_d3(high, low, close):
    return f26_stwf_321_larry_williams_smash_day_pattern(high, low, close).diff().diff().diff()


def f26_stwf_322_demark_td_pressure_5_d3(high, low, close):
    return f26_stwf_322_demark_td_pressure_5(high, low, close).diff().diff().diff()


def f26_stwf_323_demark_td_pressure_above_82_state_d3(high, low, close):
    return f26_stwf_323_demark_td_pressure_above_82_state(high, low, close).diff().diff().diff()


def f26_stwf_324_demark_td_pressure_div_vs_price_63_d3(high, low, close):
    return f26_stwf_324_demark_td_pressure_div_vs_price_63(high, low, close).diff().diff().diff()


def f26_stwf_325_elder_triple_screen_consensus_d3(high, low, close):
    return f26_stwf_325_elder_triple_screen_consensus(high, low, close).diff().diff().diff()


def f26_stwf_326_elder_force_index_2_d3(close, volume):
    return f26_stwf_326_elder_force_index_2(close, volume).diff().diff().diff()


def f26_stwf_327_elder_force_index_13_d3(close, volume):
    return f26_stwf_327_elder_force_index_13(close, volume).diff().diff().diff()


def f26_stwf_328_elder_force_index_div_vs_price_63_d3(close, volume):
    return f26_stwf_328_elder_force_index_div_vs_price_63(close, volume).diff().diff().diff()


def f26_stwf_329_worden_4_stoch_consensus_d3(high, low, close):
    return f26_stwf_329_worden_4_stoch_consensus(high, low, close).diff().diff().diff()


def f26_stwf_330_worden_4_stoch_all_above_80_state_d3(high, low, close):
    return f26_stwf_330_worden_4_stoch_all_above_80_state(high, low, close).diff().diff().diff()


def f26_stwf_331_stoch_3_3_full_pattern_d3(high, low, close):
    return f26_stwf_331_stoch_3_3_full_pattern(high, low, close).diff().diff().diff()


def f26_stwf_332_stoch_8_3_5_pattern_d3(high, low, close):
    return f26_stwf_332_stoch_8_3_5_pattern(high, low, close).diff().diff().diff()


def f26_stwf_333_dorsey_relative_strength_proxy_self_d3(close):
    return f26_stwf_333_dorsey_relative_strength_proxy_self(close).diff().diff().diff()


def f26_stwf_334_dorsey_rs_above_120_state_d3(close):
    return f26_stwf_334_dorsey_rs_above_120_state(close).diff().diff().diff()


def f26_stwf_335_dorsey_rs_dwell_above_120_63_d3(close):
    return f26_stwf_335_dorsey_rs_dwell_above_120_63(close).diff().diff().diff()


def f26_stwf_336_stoch_chronic_ob_no_new_high_63_d3(high, low, close):
    return f26_stwf_336_stoch_chronic_ob_no_new_high_63(high, low, close).diff().diff().diff()


def f26_stwf_337_stoch_failing_to_new_high_with_price_extending_d3(high, low, close):
    return f26_stwf_337_stoch_failing_to_new_high_with_price_extending(high, low, close).diff().diff().diff()


def f26_stwf_338_stoch_topping_range_indicator_63_d3(high, low, close):
    return f26_stwf_338_stoch_topping_range_indicator_63(high, low, close).diff().diff().diff()


def f26_stwf_339_stoch_repeated_ob_failures_count_252_d3(high, low, close):
    return f26_stwf_339_stoch_repeated_ob_failures_count_252(high, low, close).diff().diff().diff()


def f26_stwf_340_stoch_failure_after_blow_off_indicator_d3(high, low, close):
    return f26_stwf_340_stoch_failure_after_blow_off_indicator(high, low, close).diff().diff().diff()


def f26_stwf_341_stoch_distribution_zone_indicator_63_d3(high, low, close):
    return f26_stwf_341_stoch_distribution_zone_indicator_63(high, low, close).diff().diff().diff()


def f26_stwf_342_stoch_apathy_indicator_63_d3(high, low, close):
    return f26_stwf_342_stoch_apathy_indicator_63(high, low, close).diff().diff().diff()


def f26_stwf_343_stoch_decay_after_peak_velocity_21_d3(high, low, close):
    return f26_stwf_343_stoch_decay_after_peak_velocity_21(high, low, close).diff().diff().diff()


def f26_stwf_344_stoch_lower_high_count_in_ob_252_d3(high, low, close):
    return f26_stwf_344_stoch_lower_high_count_in_ob_252(high, low, close).diff().diff().diff()


def f26_stwf_345_stoch_consecutive_failed_breakouts_count_63_d3(high, low, close):
    return f26_stwf_345_stoch_consecutive_failed_breakouts_count_63(high, low, close).diff().diff().diff()


def f26_stwf_346_stoch_at_top_with_williams_failure_alignment_d3(high, low, close):
    return f26_stwf_346_stoch_at_top_with_williams_failure_alignment(high, low, close).diff().diff().diff()


def f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63_d3(high, low, close):
    return f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63(high, low, close).diff().diff().diff()


def f26_stwf_348_multi_oscillator_failure_stack_count_d3(high, low, close):
    return f26_stwf_348_multi_oscillator_failure_stack_count(high, low, close).diff().diff().diff()


def f26_stwf_349_multi_oscillator_topping_consensus_at_252h_d3(high, low, close):
    return f26_stwf_349_multi_oscillator_topping_consensus_at_252h(high, low, close).diff().diff().diff()


def f26_stwf_350_oscillator_failure_persistence_252_d3(high, low, close):
    return f26_stwf_350_oscillator_failure_persistence_252(high, low, close).diff().diff().diff()


def f26_stwf_351_stoch_distribution_topping_signal_combined_d3(high, low, close):
    return f26_stwf_351_stoch_distribution_topping_signal_combined(high, low, close).diff().diff().diff()


def f26_stwf_352_stoch_capitulation_proxy_d3(high, low, close):
    return f26_stwf_352_stoch_capitulation_proxy(high, low, close).diff().diff().diff()


def f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63_d3(high, low, close):
    return f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63(high, low, close).diff().diff().diff()


def f26_stwf_354_stoch_stuck_low_regime_persistence_d3(high, low, close):
    return f26_stwf_354_stoch_stuck_low_regime_persistence(high, low, close).diff().diff().diff()


def f26_stwf_355_stoch_drift_decay_score_252_d3(high, low, close):
    return f26_stwf_355_stoch_drift_decay_score_252(high, low, close).diff().diff().diff()


def f26_stwf_356_stoch_sample_entropy_21d_d3(high, low, close):
    return f26_stwf_356_stoch_sample_entropy_21d(high, low, close).diff().diff().diff()


def f26_stwf_357_stoch_sample_entropy_63d_d3(high, low, close):
    return f26_stwf_357_stoch_sample_entropy_63d(high, low, close).diff().diff().diff()


def f26_stwf_358_stoch_approximate_entropy_21d_d3(high, low, close):
    return f26_stwf_358_stoch_approximate_entropy_21d(high, low, close).diff().diff().diff()


def f26_stwf_359_stoch_permutation_entropy_21d_order3_d3(high, low, close):
    return f26_stwf_359_stoch_permutation_entropy_21d_order3(high, low, close).diff().diff().diff()


def f26_stwf_360_stoch_permutation_entropy_63d_order3_d3(high, low, close):
    return f26_stwf_360_stoch_permutation_entropy_63d_order3(high, low, close).diff().diff().diff()


def f26_stwf_361_stoch_multiscale_entropy_scale2_d3(high, low, close):
    return f26_stwf_361_stoch_multiscale_entropy_scale2(high, low, close).diff().diff().diff()


def f26_stwf_362_stoch_multiscale_entropy_scale5_d3(high, low, close):
    return f26_stwf_362_stoch_multiscale_entropy_scale5(high, low, close).diff().diff().diff()


def f26_stwf_363_stoch_fractal_dimension_higuchi_63_d3(high, low, close):
    return f26_stwf_363_stoch_fractal_dimension_higuchi_63(high, low, close).diff().diff().diff()


def f26_stwf_364_stoch_fractal_dimension_petrosian_21_d3(high, low, close):
    return f26_stwf_364_stoch_fractal_dimension_petrosian_21(high, low, close).diff().diff().diff()


def f26_stwf_365_stoch_hurst_exponent_rs_63_d3(high, low, close):
    return f26_stwf_365_stoch_hurst_exponent_rs_63(high, low, close).diff().diff().diff()


def f26_stwf_366_stoch_hurst_exponent_dfa_252_d3(high, low, close):
    return f26_stwf_366_stoch_hurst_exponent_dfa_252(high, low, close).diff().diff().diff()


def f26_stwf_367_stoch_recurrence_rate_21_d3(high, low, close):
    return f26_stwf_367_stoch_recurrence_rate_21(high, low, close).diff().diff().diff()


def f26_stwf_368_stoch_recurrence_determinism_21_d3(high, low, close):
    return f26_stwf_368_stoch_recurrence_determinism_21(high, low, close).diff().diff().diff()


def f26_stwf_369_stoch_lempel_ziv_complexity_63_d3(high, low, close):
    return f26_stwf_369_stoch_lempel_ziv_complexity_63(high, low, close).diff().diff().diff()


def f26_stwf_370_stoch_kolmogorov_complexity_proxy_63_d3(high, low, close):
    return f26_stwf_370_stoch_kolmogorov_complexity_proxy_63(high, low, close).diff().diff().diff()


def f26_stwf_371_stoch_persistence_index_rs_21_d3(high, low, close):
    return f26_stwf_371_stoch_persistence_index_rs_21(high, low, close).diff().diff().diff()


def f26_stwf_372_stoch_information_dimension_63_d3(high, low, close):
    return f26_stwf_372_stoch_information_dimension_63(high, low, close).diff().diff().diff()


def f26_stwf_373_stoch_correlation_dimension_proxy_63_d3(high, low, close):
    return f26_stwf_373_stoch_correlation_dimension_proxy_63(high, low, close).diff().diff().diff()


def f26_stwf_374_stoch_lyapunov_proxy_63_d3(high, low, close):
    return f26_stwf_374_stoch_lyapunov_proxy_63(high, low, close).diff().diff().diff()


def f26_stwf_375_stoch_predictability_horizon_63_d3(high, low, close):
    return f26_stwf_375_stoch_predictability_horizon_63(high, low, close).diff().diff().diff()


STOCHASTIC_WILLIAMS_FAMILY_D3_REGISTRY_301_375 = {
    "f26_stwf_301_vw_stoch_k_14_d3": {"inputs": ["close", "volume"], "func": f26_stwf_301_vw_stoch_k_14_d3},
    "f26_stwf_302_vw_stoch_d_14_d3": {"inputs": ["close", "volume"], "func": f26_stwf_302_vw_stoch_d_14_d3},
    "f26_stwf_303_vw_williams_r_14_d3": {"inputs": ["close", "volume"], "func": f26_stwf_303_vw_williams_r_14_d3},
    "f26_stwf_304_money_flow_stoch_14_d3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_304_money_flow_stoch_14_d3},
    "f26_stwf_305_vw_stoch_above_80_state_d3": {"inputs": ["close", "volume"], "func": f26_stwf_305_vw_stoch_above_80_state_d3},
    "f26_stwf_306_vw_stoch_div_vs_price_63_d3": {"inputs": ["close", "volume"], "func": f26_stwf_306_vw_stoch_div_vs_price_63_d3},
    "f26_stwf_307_vw_stoch_just_exited_above_80_d3": {"inputs": ["close", "volume"], "func": f26_stwf_307_vw_stoch_just_exited_above_80_d3},
    "f26_stwf_308_vw_williams_r_above_minus20_state_d3": {"inputs": ["close", "volume"], "func": f26_stwf_308_vw_williams_r_above_minus20_state_d3},
    "f26_stwf_309_vw_williams_r_dwell_above_minus20_63_d3": {"inputs": ["close", "volume"], "func": f26_stwf_309_vw_williams_r_dwell_above_minus20_63_d3},
    "f26_stwf_310_vw_stoch_bars_since_252_max_d3": {"inputs": ["close", "volume"], "func": f26_stwf_310_vw_stoch_bars_since_252_max_d3},
    "f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_311_stoch_adaptive_ob_threshold_from_504d_q90_d3},
    "f26_stwf_312_stoch_above_adaptive_ob_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_312_stoch_above_adaptive_ob_state_d3},
    "f26_stwf_313_stoch_dwell_above_adaptive_ob_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_313_stoch_dwell_above_adaptive_ob_63_d3},
    "f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_314_williams_r_adaptive_ob_threshold_from_504d_d3},
    "f26_stwf_315_williams_r_above_adaptive_ob_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_315_williams_r_above_adaptive_ob_state_d3},
    "f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_316_stoch_adaptive_extreme_threshold_q99_504_d3},
    "f26_stwf_317_stoch_above_adaptive_extreme_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_317_stoch_above_adaptive_extreme_state_d3},
    "f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_318_vol_regime_adaptive_stoch_ob_threshold_d3},
    "f26_stwf_319_vol_regime_adaptive_stoch_above_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_319_vol_regime_adaptive_stoch_above_state_d3},
    "f26_stwf_320_stoch_threshold_breach_count_normalized_504_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_320_stoch_threshold_breach_count_normalized_504_d3},
    "f26_stwf_321_larry_williams_smash_day_pattern_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_321_larry_williams_smash_day_pattern_d3},
    "f26_stwf_322_demark_td_pressure_5_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_322_demark_td_pressure_5_d3},
    "f26_stwf_323_demark_td_pressure_above_82_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_323_demark_td_pressure_above_82_state_d3},
    "f26_stwf_324_demark_td_pressure_div_vs_price_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_324_demark_td_pressure_div_vs_price_63_d3},
    "f26_stwf_325_elder_triple_screen_consensus_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_325_elder_triple_screen_consensus_d3},
    "f26_stwf_326_elder_force_index_2_d3": {"inputs": ["close", "volume"], "func": f26_stwf_326_elder_force_index_2_d3},
    "f26_stwf_327_elder_force_index_13_d3": {"inputs": ["close", "volume"], "func": f26_stwf_327_elder_force_index_13_d3},
    "f26_stwf_328_elder_force_index_div_vs_price_63_d3": {"inputs": ["close", "volume"], "func": f26_stwf_328_elder_force_index_div_vs_price_63_d3},
    "f26_stwf_329_worden_4_stoch_consensus_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_329_worden_4_stoch_consensus_d3},
    "f26_stwf_330_worden_4_stoch_all_above_80_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_330_worden_4_stoch_all_above_80_state_d3},
    "f26_stwf_331_stoch_3_3_full_pattern_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_331_stoch_3_3_full_pattern_d3},
    "f26_stwf_332_stoch_8_3_5_pattern_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_332_stoch_8_3_5_pattern_d3},
    "f26_stwf_333_dorsey_relative_strength_proxy_self_d3": {"inputs": ["close"], "func": f26_stwf_333_dorsey_relative_strength_proxy_self_d3},
    "f26_stwf_334_dorsey_rs_above_120_state_d3": {"inputs": ["close"], "func": f26_stwf_334_dorsey_rs_above_120_state_d3},
    "f26_stwf_335_dorsey_rs_dwell_above_120_63_d3": {"inputs": ["close"], "func": f26_stwf_335_dorsey_rs_dwell_above_120_63_d3},
    "f26_stwf_336_stoch_chronic_ob_no_new_high_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_336_stoch_chronic_ob_no_new_high_63_d3},
    "f26_stwf_337_stoch_failing_to_new_high_with_price_extending_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_337_stoch_failing_to_new_high_with_price_extending_d3},
    "f26_stwf_338_stoch_topping_range_indicator_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_338_stoch_topping_range_indicator_63_d3},
    "f26_stwf_339_stoch_repeated_ob_failures_count_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_339_stoch_repeated_ob_failures_count_252_d3},
    "f26_stwf_340_stoch_failure_after_blow_off_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_340_stoch_failure_after_blow_off_indicator_d3},
    "f26_stwf_341_stoch_distribution_zone_indicator_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_341_stoch_distribution_zone_indicator_63_d3},
    "f26_stwf_342_stoch_apathy_indicator_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_342_stoch_apathy_indicator_63_d3},
    "f26_stwf_343_stoch_decay_after_peak_velocity_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_343_stoch_decay_after_peak_velocity_21_d3},
    "f26_stwf_344_stoch_lower_high_count_in_ob_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_344_stoch_lower_high_count_in_ob_252_d3},
    "f26_stwf_345_stoch_consecutive_failed_breakouts_count_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_345_stoch_consecutive_failed_breakouts_count_63_d3},
    "f26_stwf_346_stoch_at_top_with_williams_failure_alignment_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_346_stoch_at_top_with_williams_failure_alignment_d3},
    "f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_347_stoch_stuck_in_lower_half_post_peak_63_d3},
    "f26_stwf_348_multi_oscillator_failure_stack_count_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_348_multi_oscillator_failure_stack_count_d3},
    "f26_stwf_349_multi_oscillator_topping_consensus_at_252h_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_349_multi_oscillator_topping_consensus_at_252h_d3},
    "f26_stwf_350_oscillator_failure_persistence_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_350_oscillator_failure_persistence_252_d3},
    "f26_stwf_351_stoch_distribution_topping_signal_combined_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_351_stoch_distribution_topping_signal_combined_d3},
    "f26_stwf_352_stoch_capitulation_proxy_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_352_stoch_capitulation_proxy_d3},
    "f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_353_stoch_post_capitulation_failed_recovery_count_63_d3},
    "f26_stwf_354_stoch_stuck_low_regime_persistence_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_354_stoch_stuck_low_regime_persistence_d3},
    "f26_stwf_355_stoch_drift_decay_score_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_355_stoch_drift_decay_score_252_d3},
    "f26_stwf_356_stoch_sample_entropy_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_356_stoch_sample_entropy_21d_d3},
    "f26_stwf_357_stoch_sample_entropy_63d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_357_stoch_sample_entropy_63d_d3},
    "f26_stwf_358_stoch_approximate_entropy_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_358_stoch_approximate_entropy_21d_d3},
    "f26_stwf_359_stoch_permutation_entropy_21d_order3_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_359_stoch_permutation_entropy_21d_order3_d3},
    "f26_stwf_360_stoch_permutation_entropy_63d_order3_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_360_stoch_permutation_entropy_63d_order3_d3},
    "f26_stwf_361_stoch_multiscale_entropy_scale2_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_361_stoch_multiscale_entropy_scale2_d3},
    "f26_stwf_362_stoch_multiscale_entropy_scale5_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_362_stoch_multiscale_entropy_scale5_d3},
    "f26_stwf_363_stoch_fractal_dimension_higuchi_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_363_stoch_fractal_dimension_higuchi_63_d3},
    "f26_stwf_364_stoch_fractal_dimension_petrosian_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_364_stoch_fractal_dimension_petrosian_21_d3},
    "f26_stwf_365_stoch_hurst_exponent_rs_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_365_stoch_hurst_exponent_rs_63_d3},
    "f26_stwf_366_stoch_hurst_exponent_dfa_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_366_stoch_hurst_exponent_dfa_252_d3},
    "f26_stwf_367_stoch_recurrence_rate_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_367_stoch_recurrence_rate_21_d3},
    "f26_stwf_368_stoch_recurrence_determinism_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_368_stoch_recurrence_determinism_21_d3},
    "f26_stwf_369_stoch_lempel_ziv_complexity_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_369_stoch_lempel_ziv_complexity_63_d3},
    "f26_stwf_370_stoch_kolmogorov_complexity_proxy_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_370_stoch_kolmogorov_complexity_proxy_63_d3},
    "f26_stwf_371_stoch_persistence_index_rs_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_371_stoch_persistence_index_rs_21_d3},
    "f26_stwf_372_stoch_information_dimension_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_372_stoch_information_dimension_63_d3},
    "f26_stwf_373_stoch_correlation_dimension_proxy_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_373_stoch_correlation_dimension_proxy_63_d3},
    "f26_stwf_374_stoch_lyapunov_proxy_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_374_stoch_lyapunov_proxy_63_d3},
    "f26_stwf_375_stoch_predictability_horizon_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_375_stoch_predictability_horizon_63_d3},
}
