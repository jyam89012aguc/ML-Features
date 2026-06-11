"""
11_decline_path_entropy -- Extended Features 001-075
Domain: smooth-vs-jagged / disorder of the decline path -- net-new depth layer
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
All features backward-looking only. Self-contained (numpy/pandas only).
"""
import numpy as np
import pandas as pd

_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9
_N_BINS  = 8


def _safe_div(num, den):
    return num / den.replace(0, np.nan)


def _log_safe(s):
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s):
    return s.pct_change(1)


def _shannon_entropy_raw(x, n_bins=_N_BINS):
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mn, mx = x.min(), x.max()
    if mx - mn < _EPS:
        return 0.0
    counts, _ = np.histogram(x, bins=np.linspace(mn, mx, n_bins + 1))
    total = counts.sum()
    if total == 0:
        return np.nan
    p = counts[counts > 0] / total
    return float(-np.sum(p * np.log(p + _EPS)))


def _multiscale_entropy_s2_raw(x):
    """Multiscale sample entropy, coarse-grain scale=2, m=2."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    nb = n // 2
    cg = np.array([x[i*2:(i+1)*2].mean() for i in range(nb)])
    if len(cg) < 4:
        return np.nan
    r = 0.2 * (cg.std() + _EPS)
    def cm(m):
        c = 0
        for i in range(len(cg) - m):
            for j in range(len(cg) - m):
                if i != j and np.max(np.abs(cg[i:i+m] - cg[j:j+m])) <= r:
                    c += 1
        return c
    A, B = cm(3), cm(2)
    return float(-np.log((A + _EPS) / (B + _EPS))) if B > 0 else np.nan


def _multiscale_entropy_s3_raw(x):
    """Multiscale sample entropy, coarse-grain scale=3, m=2."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 12:
        return np.nan
    nb = n // 3
    cg = np.array([x[i*3:(i+1)*3].mean() for i in range(nb)])
    if len(cg) < 4:
        return np.nan
    r = 0.2 * (cg.std() + _EPS)
    def cm(m):
        c = 0
        for i in range(len(cg) - m):
            for j in range(len(cg) - m):
                if i != j and np.max(np.abs(cg[i:i+m] - cg[j:j+m])) <= r:
                    c += 1
        return c
    A, B = cm(3), cm(2)
    return float(-np.log((A + _EPS) / (B + _EPS))) if B > 0 else np.nan


def _spectral_entropy_raw(x):
    """Entropy of normalised FFT power spectrum."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    ps = np.abs(np.fft.rfft(x - x.mean())) ** 2
    t = ps.sum()
    if t < _EPS:
        return 0.0
    p = ps / t
    p = p[p > 0]
    return float(-np.sum(p * np.log(p + _EPS)))


def _lempel_ziv_raw(x):
    """Normalised LZ76 complexity of binarised series (>0 -> 1)."""
    import math
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    seq = (x > 0).astype(int).tolist()
    i, k, lv, c, km = 0, 1, 1, 1, 1
    while True:
        if i + k > n or lv + k > n:
            break
        if seq[i + k - 1] == seq[lv + k - 1]:
            k += 1
            if lv + k > n:
                c += 1
                break
        else:
            if k > km:
                km = k
            i += 1
            if i == lv:
                c += 1
                lv += km
                i = 0
                k = 1
                km = 1
            else:
                k = 1
    return float(c / max(1.0, n / max(1.0, math.log2(n + _EPS))))


def _hurst_dfa_raw(x):
    """DFA-based Hurst exponent: detrended fluctuation at 2 scale levels."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    prof = np.cumsum(x - x.mean())
    fv = []
    for s in [max(4, n // 4), max(8, n // 2)]:
        ns = n // s
        if ns < 1:
            continue
        fl = 0.0
        for si in range(ns):
            seg = prof[si*s:(si+1)*s]
            t = np.arange(len(seg), dtype=float)
            if len(t) < 2:
                continue
            tm = t.mean()
            sm = seg.mean()
            den = ((t - tm) ** 2).sum()
            sl = ((t - tm) * (seg - sm)).sum() / den if den >= _EPS else 0.0
            fl += np.mean((seg - (sl * t + (sm - sl * tm))) ** 2)
        fv.append((np.log(s + _EPS), np.log(np.sqrt(fl / ns) + _EPS)))
    if len(fv) < 2:
        return np.nan
    dx = fv[1][0] - fv[0][0]
    return float((fv[1][1] - fv[0][1]) / dx) if abs(dx) >= _EPS else np.nan


def _hurst_thirds_raw(x):
    """R/S Hurst using 3 equal sub-segments."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 12:
        return np.nan
    sl = n // 3
    rs = []
    for k in range(3):
        seg = x[k*sl:(k+1)*sl]
        dev = np.cumsum(seg - seg.mean())
        s = seg.std()
        if s >= _EPS:
            rs.append((dev.max() - dev.min()) / s)
    if not rs:
        return np.nan
    rm = np.mean(rs)
    return float(np.log(rm) / np.log(sl + _EPS)) if rm > 0 else np.nan


def _sample_entropy_m3_raw(x):
    """Sample entropy m=3, r_frac=0.2."""
    x = x[~np.isnan(x)]
    n = len(x)
    m = 3
    if n < m + 2:
        return np.nan
    r = 0.2 * (np.std(x) + _EPS)
    def cm(m_):
        c = 0
        for i in range(n - m_):
            for j in range(n - m_):
                if i != j and np.max(np.abs(x[i:i+m_] - x[j:j+m_])) <= r:
                    c += 1
        return c
    A, B = cm(m + 1), cm(m)
    return float(-np.log((A + _EPS) / (B + _EPS))) if B > 0 else np.nan


def _approx_entropy_m3_raw(x):
    """Approximate entropy m=3, r_frac=0.2."""
    x = x[~np.isnan(x)]
    n = len(x)
    m = 3
    if n < m + 2:
        return np.nan
    r = 0.2 * (np.std(x) + _EPS)
    def phi(m_):
        c = tot = 0
        for i in range(n - m_ + 1):
            for j in range(n - m_ + 1):
                if np.max(np.abs(x[i:i+m_] - x[j:j+m_])) <= r:
                    c += 1
            tot += 1
        return np.log(c / tot + _EPS) if tot > 0 else np.nan
    p1, p2 = phi(m), phi(m + 1)
    if p1 is None or p2 is None or np.isnan(p1) or np.isnan(p2):
        return np.nan
    return float(p1 - p2)


def _sample_entropy_r15_raw(x):
    """Sample entropy m=2, r_frac=0.15 (tighter tolerance)."""
    x = x[~np.isnan(x)]
    n = len(x)
    m = 2
    if n < m + 2:
        return np.nan
    r = 0.15 * (np.std(x) + _EPS)
    def cm(m_):
        c = 0
        for i in range(n - m_):
            for j in range(n - m_):
                if i != j and np.max(np.abs(x[i:i+m_] - x[j:j+m_])) <= r:
                    c += 1
        return c
    A, B = cm(m + 1), cm(m)
    return float(-np.log((A + _EPS) / (B + _EPS))) if B > 0 else np.nan


def _perm_entropy_o5_raw(x):
    """Normalised permutation entropy order 5."""
    from math import factorial
    x = x[~np.isnan(x)]
    order = 5
    n = len(x)
    if n < order + 1:
        return np.nan
    cnt = {}
    for i in range(n - order):
        p = tuple(np.argsort(x[i:i+order]))
        cnt[p] = cnt.get(p, 0) + 1
    tot = sum(cnt.values())
    if tot == 0:
        return np.nan
    pr = np.array(list(cnt.values())) / tot
    me = np.log(factorial(order))
    return float(-np.sum(pr * np.log(pr + _EPS)) / me) if me >= _EPS else 0.0


def _recurrence_rate_raw(x):
    """Recurrence rate: fraction of off-diagonal pairs within eps=10% std."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    eps = 0.1 * (x.std() + _EPS)
    c = 0
    for i in range(n):
        for j in range(n):
            if i != j and abs(x[i] - x[j]) <= eps:
                c += 1
    return float(c / (n * (n - 1)))


def _determinism_rqa_raw(x):
    """RQA determinism: fraction of recurrent points in diagonal lines >= 2."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 6:
        return np.nan
    eps = 0.1 * (x.std() + _EPS)
    R = (np.abs(x[:, None] - x[None, :]) <= eps)
    tr = int(R.sum()) - n
    if tr <= 0:
        return 0.0
    dr = 0
    ml = 2
    for d in range(-n + 1, n):
        diag = np.diag(R, d)
        if len(diag) < ml:
            continue
        cur = 0
        inl = False
        for v in diag:
            if v:
                cur += 1
                if cur >= ml:
                    if not inl:
                        dr += cur
                        inl = True
                    else:
                        dr += 1
            else:
                cur = 0
                inl = False
    return float(dr / max(1, tr))


def _run_len_entropy_raw(x):
    """Shannon entropy of up/down run-length distribution."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    sg = np.sign(x)
    rc = {}
    cur = 1
    for i in range(1, len(sg)):
        if sg[i] == sg[i - 1]:
            cur += 1
        else:
            rc[cur] = rc.get(cur, 0) + 1
            cur = 1
    rc[cur] = rc.get(cur, 0) + 1
    tot = sum(rc.values())
    if tot == 0:
        return np.nan
    p = np.array(list(rc.values())) / tot
    return float(-np.sum(p * np.log(p + _EPS)))


def _cond_entropy_raw(x):
    """Conditional entropy H(X_t | X_{t-1})."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 6:
        return np.nan
    mn, mx = x.min(), x.max()
    if mx - mn < _EPS:
        return 0.0
    idx = np.clip(np.digitize(x, np.linspace(mn, mx, _N_BINS + 1)) - 1, 0, _N_BINS - 1)
    jt = {}
    for i in range(n - 1):
        k = (idx[i], idx[i + 1])
        jt[k] = jt.get(k, 0) + 1
    tot = sum(jt.values())
    if tot == 0:
        return np.nan
    mg = {}
    for (a, b), c in jt.items():
        mg[a] = mg.get(a, 0) + c
    h = 0.0
    for (a, b), c in jt.items():
        pj = c / tot
        pm = mg[a] / tot
        if pj > 0 and pm > 0:
            h -= pj * np.log(pj / pm + _EPS)
    return float(h)


def _tp_strict_raw(x):
    """Strict turning-point density (requires strict inequality)."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    tp = 0
    for i in range(1, len(x) - 1):
        if (x[i] > x[i-1] + _EPS and x[i] > x[i+1] + _EPS) or            (x[i] < x[i-1] - _EPS and x[i] < x[i+1] - _EPS):
            tp += 1
    return float(tp / (len(x) - 2))


def _zcross_absret_raw(x):
    """Zero-crossing rate of (|return| - median|return|)."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    c = np.abs(x) - np.median(np.abs(x))
    return float(np.sum((c[:-1] * c[1:]) < 0) / (len(c) - 1))


def _up_cross_raw(x):
    """Up-crossing rate (negative to non-negative)."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    return float(np.sum((x[:-1] < 0) & (x[1:] >= 0)) / (len(x) - 1))


def _dn_cross_raw(x):
    """Down-crossing rate (non-negative to negative)."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    return float(np.sum((x[:-1] >= 0) & (x[1:] < 0)) / (len(x) - 1))


def _sign_trans_ent_raw(x):
    """Entropy of 4 sign-transition types."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    s = (x > 0).astype(int)
    tr = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for i in range(len(s) - 1):
        tr[(s[i], s[i + 1])] += 1
    tot = sum(tr.values())
    if tot == 0:
        return np.nan
    p = np.array(list(tr.values())) / tot
    p = p[p > 0]
    return float(-np.sum(p * np.log(p + _EPS)))


def _run_count_density_raw(x):
    """Distinct sign-runs per unit length."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2:
        return np.nan
    sg = np.sign(x)
    return float((1 + np.sum(sg[1:] != sg[:-1])) / n)


def _down_run_max_raw(x):
    """Maximum length of consecutive negative runs."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mx = cur = 0
    for v in x:
        if v < 0:
            cur += 1
            mx = max(mx, cur)
        else:
            cur = 0
    return float(mx)


def _up_run_max_raw(x):
    """Maximum length of consecutive positive runs."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mx = cur = 0
    for v in x:
        if v > 0:
            cur += 1
            mx = max(mx, cur)
        else:
            cur = 0
    return float(mx)


def _down_run_std_raw(x):
    """Std of lengths of consecutive negative runs."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    rs = []
    cur = 0
    ind = False
    for v in x:
        if v < 0:
            cur += 1
            ind = True
        elif ind:
            rs.append(cur)
            cur = 0
            ind = False
    if ind:
        rs.append(cur)
    return float(np.std(rs)) if len(rs) >= 2 else 0.0


def _path_roughness_raw(x):
    """Mean |2nd diff| / mean |1st diff|."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    d1 = np.abs(np.diff(x))
    d2 = np.abs(np.diff(x, n=2))
    m = d1.mean()
    return float(d2.mean() / m) if m >= _EPS else np.nan


def _petrosian_fd_raw(x):
    """Petrosian fractal dimension via sign changes of first difference."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    d = np.diff(x)
    nsc = float(np.sum(d[:-1] * d[1:] < 0))
    den = np.log10(n) + np.log10(n / (n + 0.4 * nsc + _EPS))
    return float(np.log10(n) / den) if abs(den) >= _EPS else np.nan


def _hjorth_mob_raw(x):
    """Hjorth mobility: sqrt(var(diff(x)) / var(x))."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    vx = np.var(x)
    return float(np.sqrt(np.var(np.diff(x)) / vx)) if vx >= _EPS else np.nan


def _hjorth_cx_raw(x):
    """Hjorth complexity: mobility(diff(x)) / mobility(x)."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    def mob(v):
        vv = np.var(v)
        return np.sqrt(np.var(np.diff(v)) / vv) if vv >= _EPS else np.nan
    mx, mdx = mob(x), mob(np.diff(x))
    if mx is None or np.isnan(mx) or mx < _EPS:
        return np.nan
    if mdx is None or np.isnan(mdx):
        return np.nan
    return float(mdx / mx)


def _waveform_len_raw(x):
    """Normalised waveform length: sum|diff| / (range * (n-1))."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2:
        return np.nan
    rng = x.max() - x.min()
    return float(np.sum(np.abs(np.diff(x))) / (rng * (n - 1))) if rng >= _EPS else 0.0


def _entropy_12bin_raw(x):
    """Shannon entropy with 12-bin discretisation."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mn, mx = x.min(), x.max()
    if mx - mn < _EPS:
        return 0.0
    counts, _ = np.histogram(x, bins=np.linspace(mn, mx, 13))
    tot = counts.sum()
    if tot == 0:
        return np.nan
    p = counts[counts > 0] / tot
    return float(-np.sum(p * np.log(p + _EPS)))


def _entropy_sq_raw(x):
    """Shannon entropy of squared values."""
    x = x[~np.isnan(x)]
    return _shannon_entropy_raw(x ** 2) if len(x) >= 2 else np.nan


def _entropy_diff_raw(x):
    """Shannon entropy of first-differences."""
    x = x[~np.isnan(x)]
    return _shannon_entropy_raw(np.diff(x)) if len(x) >= 3 else np.nan


def _entropy_logdiff_raw(x):
    """Shannon entropy of log first-differences."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    return _shannon_entropy_raw(np.diff(np.log(np.maximum(x, _EPS))))


def _zscore_last_raw(x):
    """Z-score of last value within window."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    s = x.std()
    return float((x[-1] - x.mean()) / s) if s >= _EPS else 0.0


def _pctrank_last_raw(x):
    """Percentile rank of last value within window (0-1)."""
    x = x[~np.isnan(x)]
    return float(np.sum(x[:-1] < x[-1]) / (len(x) - 1)) if len(x) >= 2 else np.nan


def _ac3_raw(x):
    """Lag-3 autocorrelation."""
    x = x[~np.isnan(x)]
    if len(x) < 5:
        return np.nan
    c = pd.Series(x).autocorr(lag=3)
    return float(c) if not np.isnan(c) else np.nan


def _ac10_raw(x):
    """Lag-10 autocorrelation."""
    x = x[~np.isnan(x)]
    if len(x) < 12:
        return np.nan
    c = pd.Series(x).autocorr(lag=10)
    return float(c) if not np.isnan(c) else np.nan


def _ac21_raw(x):
    """Lag-21 autocorrelation."""
    x = x[~np.isnan(x)]
    if len(x) < 23:
        return np.nan
    c = pd.Series(x).autocorr(lag=21)
    return float(c) if not np.isnan(c) else np.nan


# ---- Group A (001-010): Multiscale & spectral entropy ----

def dpe_ext_001_multiscale_ent_ret_s2_21d(close):
    """Multiscale entropy scale=2 of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _multiscale_entropy_s2_raw, raw=True)

def dpe_ext_002_multiscale_ent_ret_s2_63d(close):
    """Multiscale entropy scale=2 of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(16, _TD_QTR//2)).apply(
        _multiscale_entropy_s2_raw, raw=True)

def dpe_ext_003_multiscale_ent_ret_s3_21d(close):
    """Multiscale entropy scale=3 of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(12, _TD_MON//2)).apply(
        _multiscale_entropy_s3_raw, raw=True)

def dpe_ext_004_multiscale_ent_close_s2_21d(close):
    """Multiscale entropy scale=2 of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _multiscale_entropy_s2_raw, raw=True)

def dpe_ext_005_multiscale_ent_volume_s2_21d(volume):
    """Multiscale entropy scale=2 of volume, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _multiscale_entropy_s2_raw, raw=True)

def dpe_ext_006_spectral_entropy_ret_21d(close):
    """Spectral entropy of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _spectral_entropy_raw, raw=True)

def dpe_ext_007_spectral_entropy_ret_63d(close):
    """Spectral entropy of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(10, _TD_QTR//2)).apply(
        _spectral_entropy_raw, raw=True)

def dpe_ext_008_spectral_entropy_close_21d(close):
    """Spectral entropy of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _spectral_entropy_raw, raw=True)

def dpe_ext_009_spectral_entropy_hl_range_21d(high, low):
    """Spectral entropy of H-L range, 21-day window."""
    return (high - low).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _spectral_entropy_raw, raw=True)

def dpe_ext_010_spectral_entropy_volume_21d(volume):
    """Spectral entropy of volume, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _spectral_entropy_raw, raw=True)


# ---- Group B (011-018): Lempel-Ziv complexity ----

def dpe_ext_011_lz_complexity_ret_21d(close):
    """Lempel-Ziv complexity of binarised returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_012_lz_complexity_ret_63d(close):
    """Lempel-Ziv complexity of binarised returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(10, _TD_QTR//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_013_lz_complexity_ret_126d(close):
    """Lempel-Ziv complexity of binarised returns, 126-day window."""
    return _daily_ret(close).rolling(_TD_HALF, min_periods=max(20, _TD_HALF//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_014_lz_complexity_logret_21d(close):
    """Lempel-Ziv complexity of binarised log-returns, 21-day window."""
    return _log_safe(close).diff(1).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_015_lz_complexity_oc_ret_21d(open, close):
    """Lempel-Ziv complexity of binarised open-to-close returns, 21-day."""
    oc = _safe_div(close - open, open)
    return oc.rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_016_lz_complexity_hl_diff_21d(high, low):
    """Lempel-Ziv complexity of binarised H-L range diff, 21-day window."""
    return (high - low).diff(1).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_017_lz_complexity_vol_diff_21d(volume):
    """Lempel-Ziv complexity of binarised volume first-diff, 21-day window."""
    return volume.diff(1).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _lempel_ziv_raw, raw=True)

def dpe_ext_018_lz_complexity_ret_10d(close):
    """Lempel-Ziv complexity of binarised returns, 10-day window."""
    return _daily_ret(close).rolling(10, min_periods=5).apply(
        _lempel_ziv_raw, raw=True)


# ---- Group C (019-025): DFA Hurst & 3-segment Hurst ----

def dpe_ext_019_dfa_hurst_ret_63d(close):
    """DFA-based Hurst exponent of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(16, _TD_QTR//2)).apply(
        _hurst_dfa_raw, raw=True)

def dpe_ext_020_dfa_hurst_close_63d(close):
    """DFA-based Hurst exponent of close prices, 63-day window."""
    return close.rolling(_TD_QTR, min_periods=max(16, _TD_QTR//2)).apply(
        _hurst_dfa_raw, raw=True)

def dpe_ext_021_dfa_hurst_ret_126d(close):
    """DFA-based Hurst exponent of returns, 126-day window."""
    return _daily_ret(close).rolling(_TD_HALF, min_periods=max(20, _TD_HALF//2)).apply(
        _hurst_dfa_raw, raw=True)

def dpe_ext_022_hurst_rs_thirds_close_63d(close):
    """R/S Hurst (3-segment) of close prices, 63-day window."""
    return close.rolling(_TD_QTR, min_periods=max(12, _TD_QTR//2)).apply(
        _hurst_thirds_raw, raw=True)

def dpe_ext_023_hurst_rs_thirds_ret_63d(close):
    """R/S Hurst (3-segment) of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(12, _TD_QTR//2)).apply(
        _hurst_thirds_raw, raw=True)

def dpe_ext_024_hurst_rs_thirds_logprice_63d(close):
    """R/S Hurst (3-segment) of log-close, 63-day window."""
    return _log_safe(close).rolling(_TD_QTR, min_periods=max(12, _TD_QTR//2)).apply(
        _hurst_thirds_raw, raw=True)

def dpe_ext_025_dfa_hurst_volume_63d(volume):
    """DFA-based Hurst exponent of volume, 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(16, _TD_QTR//2)).apply(
        _hurst_dfa_raw, raw=True)


# ---- Group D (026-032): Sample/approx entropy at new orders/tolerances ----

def dpe_ext_026_sample_entropy_m3_ret_21d(close):
    """Sample entropy m=3 of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _sample_entropy_m3_raw, raw=True)

def dpe_ext_027_approx_entropy_m3_ret_21d(close):
    """Approximate entropy m=3 of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _approx_entropy_m3_raw, raw=True)

def dpe_ext_028_sample_entropy_r15_ret_21d(close):
    """Sample entropy m=2 r=0.15 of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _sample_entropy_r15_raw, raw=True)

def dpe_ext_029_sample_entropy_m3_close_21d(close):
    """Sample entropy m=3 of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(8, _TD_MON//2)).apply(
        _sample_entropy_m3_raw, raw=True)

def dpe_ext_030_sample_entropy_r15_volume_21d(volume):
    """Sample entropy m=2 r=0.15 of volume, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _sample_entropy_r15_raw, raw=True)

def dpe_ext_031_perm_entropy_order5_ret_63d(close):
    """Permutation entropy order 5 of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(8, _TD_QTR//2)).apply(
        _perm_entropy_o5_raw, raw=True)

def dpe_ext_032_perm_entropy_order5_close_63d(close):
    """Permutation entropy order 5 of close prices, 63-day window."""
    return close.rolling(_TD_QTR, min_periods=max(8, _TD_QTR//2)).apply(
        _perm_entropy_o5_raw, raw=True)


# ---- Group E (033-039): Recurrence quantification ----

def dpe_ext_033_recurrence_rate_ret_21d(close):
    """Recurrence rate (eps=10% std) of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _recurrence_rate_raw, raw=True)

def dpe_ext_034_recurrence_rate_close_21d(close):
    """Recurrence rate of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _recurrence_rate_raw, raw=True)

def dpe_ext_035_determinism_rqa_ret_21d(close):
    """RQA determinism of returns (min_line=2), 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _determinism_rqa_raw, raw=True)

def dpe_ext_036_recurrence_rate_logret_21d(close):
    """Recurrence rate of log-returns, 21-day window."""
    return _log_safe(close).diff(1).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _recurrence_rate_raw, raw=True)

def dpe_ext_037_determinism_rqa_close_21d(close):
    """RQA determinism of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _determinism_rqa_raw, raw=True)

def dpe_ext_038_recurrence_rate_hl_range_21d(high, low):
    """Recurrence rate of H-L range, 21-day window."""
    return (high - low).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _recurrence_rate_raw, raw=True)

def dpe_ext_039_recurrence_rate_volume_21d(volume):
    """Recurrence rate of volume, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _recurrence_rate_raw, raw=True)


# ---- Group F (040-047): Run-length & conditional entropy ----

def dpe_ext_040_run_length_entropy_ret_21d(close):
    """Shannon entropy of run-length distribution of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _run_len_entropy_raw, raw=True)

def dpe_ext_041_run_length_entropy_ret_63d(close):
    """Shannon entropy of run-length distribution of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(8, _TD_QTR//2)).apply(
        _run_len_entropy_raw, raw=True)

def dpe_ext_042_run_length_entropy_vol_diff_21d(volume):
    """Shannon entropy of volume-diff run-length distribution, 21-day window."""
    return volume.diff(1).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _run_len_entropy_raw, raw=True)

def dpe_ext_043_conditional_entropy_ret_21d(close):
    """Conditional entropy H(X_t|X_{t-1}) of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _cond_entropy_raw, raw=True)

def dpe_ext_044_conditional_entropy_ret_63d(close):
    """Conditional entropy H(X_t|X_{t-1}) of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(10, _TD_QTR//2)).apply(
        _cond_entropy_raw, raw=True)

def dpe_ext_045_entropy_sign_trans_ret_21d(close):
    """Entropy of 4 sign-transition types of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _sign_trans_ent_raw, raw=True)

def dpe_ext_046_down_run_max_ret_21d(close):
    """Maximum consecutive down-run length of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _down_run_max_raw, raw=True)

def dpe_ext_047_up_run_max_ret_21d(close):
    """Maximum consecutive up-run length of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _up_run_max_raw, raw=True)


# ---- Group G (048-056): Turning-point & zero-crossing variants ----

def dpe_ext_048_tp_density_strict_ret_21d(close):
    """Strict turning-point density of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _tp_strict_raw, raw=True)

def dpe_ext_049_tp_density_strict_close_63d(close):
    """Strict turning-point density of close prices, 63-day window."""
    return close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR//2)).apply(
        _tp_strict_raw, raw=True)

def dpe_ext_050_zero_cross_absret_21d(close):
    """Zero-crossing rate of (|ret|-median|ret|), 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _zcross_absret_raw, raw=True)

def dpe_ext_051_zero_cross_absret_63d(close):
    """Zero-crossing rate of (|ret|-median|ret|), 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(8, _TD_QTR//2)).apply(
        _zcross_absret_raw, raw=True)

def dpe_ext_052_up_crossing_ret_21d(close):
    """Up-crossing rate of returns (neg to non-neg), 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _up_cross_raw, raw=True)

def dpe_ext_053_down_crossing_ret_21d(close):
    """Down-crossing rate of returns (non-neg to neg), 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _dn_cross_raw, raw=True)

def dpe_ext_054_run_count_density_ret_21d(close):
    """Run-count density (runs/n) of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _run_count_density_raw, raw=True)

def dpe_ext_055_run_count_density_ret_63d(close):
    """Run-count density of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(6, _TD_QTR//2)).apply(
        _run_count_density_raw, raw=True)

def dpe_ext_056_down_run_std_ret_21d(close):
    """Std of consecutive down-run lengths, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _down_run_std_raw, raw=True)


# ---- Group H (057-063): Path roughness, Petrosian, Hjorth, waveform ----

def dpe_ext_057_path_roughness_ret_21d(close):
    """Path roughness (|2nd diff|/|1st diff|) of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _path_roughness_raw, raw=True)

def dpe_ext_058_path_roughness_close_21d(close):
    """Path roughness of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _path_roughness_raw, raw=True)

def dpe_ext_059_petrosian_fd_ret_21d(close):
    """Petrosian fractal dimension of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _petrosian_fd_raw, raw=True)

def dpe_ext_060_petrosian_fd_close_21d(close):
    """Petrosian fractal dimension of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _petrosian_fd_raw, raw=True)

def dpe_ext_061_hjorth_mobility_ret_21d(close):
    """Hjorth mobility of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _hjorth_mob_raw, raw=True)

def dpe_ext_062_hjorth_complexity_ret_21d(close):
    """Hjorth complexity of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(5, _TD_MON//2)).apply(
        _hjorth_cx_raw, raw=True)

def dpe_ext_063_waveform_length_ret_21d(close):
    """Normalised waveform length of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _waveform_len_raw, raw=True)


# ---- Group I (064-069): Entropy of volume changes & squared returns ----

def dpe_ext_064_entropy_vol_diff_21d(volume):
    """Shannon entropy of volume first-differences, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _entropy_diff_raw, raw=True)

def dpe_ext_065_entropy_vol_logdiff_21d(volume):
    """Shannon entropy of log-volume first-differences, 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _entropy_logdiff_raw, raw=True)

def dpe_ext_066_entropy_vol_diff_63d(volume):
    """Shannon entropy of volume first-differences, 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(6, _TD_QTR//2)).apply(
        _entropy_diff_raw, raw=True)

def dpe_ext_067_entropy_squared_ret_21d(close):
    """Shannon entropy of squared returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _entropy_sq_raw, raw=True)

def dpe_ext_068_entropy_squared_ret_63d(close):
    """Shannon entropy of squared returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(6, _TD_QTR//2)).apply(
        _entropy_sq_raw, raw=True)

def dpe_ext_069_entropy_ret_12bin_21d(close):
    """Shannon entropy of returns (12-bin), 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _entropy_12bin_raw, raw=True)


# ---- Group J (070-075): Z-score, pctrank, new-lag autocorrelation ----

def dpe_ext_070_zscore_ret_21d(close):
    """Z-score of current return within 21-day distribution."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _zscore_last_raw, raw=True)

def dpe_ext_071_pctrank_ret_21d(close):
    """Percentile rank of current return within 21-day window (0-1)."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _pctrank_last_raw, raw=True)

def dpe_ext_072_autocorr_lag3_ret_21d(close):
    """Lag-3 autocorrelation of returns, 21-day window."""
    return _daily_ret(close).rolling(_TD_MON, min_periods=max(6, _TD_MON//2)).apply(
        _ac3_raw, raw=True)

def dpe_ext_073_autocorr_lag10_ret_63d(close):
    """Lag-10 autocorrelation of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(14, _TD_QTR//2)).apply(
        _ac10_raw, raw=True)

def dpe_ext_074_autocorr_lag21_ret_63d(close):
    """Lag-21 (monthly) autocorrelation of returns, 63-day window."""
    return _daily_ret(close).rolling(_TD_QTR, min_periods=max(25, _TD_QTR//2)).apply(
        _ac21_raw, raw=True)

def dpe_ext_075_hjorth_mobility_close_21d(close):
    """Hjorth mobility of close prices, 21-day window."""
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON//2)).apply(
        _hjorth_mob_raw, raw=True)


# ---- Registry ----

DECLINE_PATH_ENTROPY_EXTENDED_REGISTRY_001_075 = {
    "dpe_ext_001_multiscale_ent_ret_s2_21d":     {"inputs": ["close"],       "func": dpe_ext_001_multiscale_ent_ret_s2_21d},
    "dpe_ext_002_multiscale_ent_ret_s2_63d":     {"inputs": ["close"],       "func": dpe_ext_002_multiscale_ent_ret_s2_63d},
    "dpe_ext_003_multiscale_ent_ret_s3_21d":     {"inputs": ["close"],       "func": dpe_ext_003_multiscale_ent_ret_s3_21d},
    "dpe_ext_004_multiscale_ent_close_s2_21d":   {"inputs": ["close"],       "func": dpe_ext_004_multiscale_ent_close_s2_21d},
    "dpe_ext_005_multiscale_ent_volume_s2_21d":  {"inputs": ["volume"],      "func": dpe_ext_005_multiscale_ent_volume_s2_21d},
    "dpe_ext_006_spectral_entropy_ret_21d":      {"inputs": ["close"],       "func": dpe_ext_006_spectral_entropy_ret_21d},
    "dpe_ext_007_spectral_entropy_ret_63d":      {"inputs": ["close"],       "func": dpe_ext_007_spectral_entropy_ret_63d},
    "dpe_ext_008_spectral_entropy_close_21d":    {"inputs": ["close"],       "func": dpe_ext_008_spectral_entropy_close_21d},
    "dpe_ext_009_spectral_entropy_hl_range_21d": {"inputs": ["high","low"],  "func": dpe_ext_009_spectral_entropy_hl_range_21d},
    "dpe_ext_010_spectral_entropy_volume_21d":   {"inputs": ["volume"],      "func": dpe_ext_010_spectral_entropy_volume_21d},
    "dpe_ext_011_lz_complexity_ret_21d":         {"inputs": ["close"],       "func": dpe_ext_011_lz_complexity_ret_21d},
    "dpe_ext_012_lz_complexity_ret_63d":         {"inputs": ["close"],       "func": dpe_ext_012_lz_complexity_ret_63d},
    "dpe_ext_013_lz_complexity_ret_126d":        {"inputs": ["close"],       "func": dpe_ext_013_lz_complexity_ret_126d},
    "dpe_ext_014_lz_complexity_logret_21d":      {"inputs": ["close"],       "func": dpe_ext_014_lz_complexity_logret_21d},
    "dpe_ext_015_lz_complexity_oc_ret_21d":      {"inputs": ["open","close"],"func": dpe_ext_015_lz_complexity_oc_ret_21d},
    "dpe_ext_016_lz_complexity_hl_diff_21d":     {"inputs": ["high","low"],  "func": dpe_ext_016_lz_complexity_hl_diff_21d},
    "dpe_ext_017_lz_complexity_vol_diff_21d":    {"inputs": ["volume"],      "func": dpe_ext_017_lz_complexity_vol_diff_21d},
    "dpe_ext_018_lz_complexity_ret_10d":         {"inputs": ["close"],       "func": dpe_ext_018_lz_complexity_ret_10d},
    "dpe_ext_019_dfa_hurst_ret_63d":             {"inputs": ["close"],       "func": dpe_ext_019_dfa_hurst_ret_63d},
    "dpe_ext_020_dfa_hurst_close_63d":           {"inputs": ["close"],       "func": dpe_ext_020_dfa_hurst_close_63d},
    "dpe_ext_021_dfa_hurst_ret_126d":            {"inputs": ["close"],       "func": dpe_ext_021_dfa_hurst_ret_126d},
    "dpe_ext_022_hurst_rs_thirds_close_63d":     {"inputs": ["close"],       "func": dpe_ext_022_hurst_rs_thirds_close_63d},
    "dpe_ext_023_hurst_rs_thirds_ret_63d":       {"inputs": ["close"],       "func": dpe_ext_023_hurst_rs_thirds_ret_63d},
    "dpe_ext_024_hurst_rs_thirds_logprice_63d":  {"inputs": ["close"],       "func": dpe_ext_024_hurst_rs_thirds_logprice_63d},
    "dpe_ext_025_dfa_hurst_volume_63d":          {"inputs": ["volume"],      "func": dpe_ext_025_dfa_hurst_volume_63d},
    "dpe_ext_026_sample_entropy_m3_ret_21d":     {"inputs": ["close"],       "func": dpe_ext_026_sample_entropy_m3_ret_21d},
    "dpe_ext_027_approx_entropy_m3_ret_21d":     {"inputs": ["close"],       "func": dpe_ext_027_approx_entropy_m3_ret_21d},
    "dpe_ext_028_sample_entropy_r15_ret_21d":    {"inputs": ["close"],       "func": dpe_ext_028_sample_entropy_r15_ret_21d},
    "dpe_ext_029_sample_entropy_m3_close_21d":   {"inputs": ["close"],       "func": dpe_ext_029_sample_entropy_m3_close_21d},
    "dpe_ext_030_sample_entropy_r15_volume_21d": {"inputs": ["volume"],      "func": dpe_ext_030_sample_entropy_r15_volume_21d},
    "dpe_ext_031_perm_entropy_order5_ret_63d":   {"inputs": ["close"],       "func": dpe_ext_031_perm_entropy_order5_ret_63d},
    "dpe_ext_032_perm_entropy_order5_close_63d": {"inputs": ["close"],       "func": dpe_ext_032_perm_entropy_order5_close_63d},
    "dpe_ext_033_recurrence_rate_ret_21d":       {"inputs": ["close"],       "func": dpe_ext_033_recurrence_rate_ret_21d},
    "dpe_ext_034_recurrence_rate_close_21d":     {"inputs": ["close"],       "func": dpe_ext_034_recurrence_rate_close_21d},
    "dpe_ext_035_determinism_rqa_ret_21d":       {"inputs": ["close"],       "func": dpe_ext_035_determinism_rqa_ret_21d},
    "dpe_ext_036_recurrence_rate_logret_21d":    {"inputs": ["close"],       "func": dpe_ext_036_recurrence_rate_logret_21d},
    "dpe_ext_037_determinism_rqa_close_21d":     {"inputs": ["close"],       "func": dpe_ext_037_determinism_rqa_close_21d},
    "dpe_ext_038_recurrence_rate_hl_range_21d":  {"inputs": ["high","low"],  "func": dpe_ext_038_recurrence_rate_hl_range_21d},
    "dpe_ext_039_recurrence_rate_volume_21d":    {"inputs": ["volume"],      "func": dpe_ext_039_recurrence_rate_volume_21d},
    "dpe_ext_040_run_length_entropy_ret_21d":    {"inputs": ["close"],       "func": dpe_ext_040_run_length_entropy_ret_21d},
    "dpe_ext_041_run_length_entropy_ret_63d":    {"inputs": ["close"],       "func": dpe_ext_041_run_length_entropy_ret_63d},
    "dpe_ext_042_run_length_entropy_vol_diff_21d":{"inputs": ["volume"],     "func": dpe_ext_042_run_length_entropy_vol_diff_21d},
    "dpe_ext_043_conditional_entropy_ret_21d":   {"inputs": ["close"],       "func": dpe_ext_043_conditional_entropy_ret_21d},
    "dpe_ext_044_conditional_entropy_ret_63d":   {"inputs": ["close"],       "func": dpe_ext_044_conditional_entropy_ret_63d},
    "dpe_ext_045_entropy_sign_trans_ret_21d":    {"inputs": ["close"],       "func": dpe_ext_045_entropy_sign_trans_ret_21d},
    "dpe_ext_046_down_run_max_ret_21d":          {"inputs": ["close"],       "func": dpe_ext_046_down_run_max_ret_21d},
    "dpe_ext_047_up_run_max_ret_21d":            {"inputs": ["close"],       "func": dpe_ext_047_up_run_max_ret_21d},
    "dpe_ext_048_tp_density_strict_ret_21d":     {"inputs": ["close"],       "func": dpe_ext_048_tp_density_strict_ret_21d},
    "dpe_ext_049_tp_density_strict_close_63d":   {"inputs": ["close"],       "func": dpe_ext_049_tp_density_strict_close_63d},
    "dpe_ext_050_zero_cross_absret_21d":         {"inputs": ["close"],       "func": dpe_ext_050_zero_cross_absret_21d},
    "dpe_ext_051_zero_cross_absret_63d":         {"inputs": ["close"],       "func": dpe_ext_051_zero_cross_absret_63d},
    "dpe_ext_052_up_crossing_ret_21d":           {"inputs": ["close"],       "func": dpe_ext_052_up_crossing_ret_21d},
    "dpe_ext_053_down_crossing_ret_21d":         {"inputs": ["close"],       "func": dpe_ext_053_down_crossing_ret_21d},
    "dpe_ext_054_run_count_density_ret_21d":     {"inputs": ["close"],       "func": dpe_ext_054_run_count_density_ret_21d},
    "dpe_ext_055_run_count_density_ret_63d":     {"inputs": ["close"],       "func": dpe_ext_055_run_count_density_ret_63d},
    "dpe_ext_056_down_run_std_ret_21d":          {"inputs": ["close"],       "func": dpe_ext_056_down_run_std_ret_21d},
    "dpe_ext_057_path_roughness_ret_21d":        {"inputs": ["close"],       "func": dpe_ext_057_path_roughness_ret_21d},
    "dpe_ext_058_path_roughness_close_21d":      {"inputs": ["close"],       "func": dpe_ext_058_path_roughness_close_21d},
    "dpe_ext_059_petrosian_fd_ret_21d":          {"inputs": ["close"],       "func": dpe_ext_059_petrosian_fd_ret_21d},
    "dpe_ext_060_petrosian_fd_close_21d":        {"inputs": ["close"],       "func": dpe_ext_060_petrosian_fd_close_21d},
    "dpe_ext_061_hjorth_mobility_ret_21d":       {"inputs": ["close"],       "func": dpe_ext_061_hjorth_mobility_ret_21d},
    "dpe_ext_062_hjorth_complexity_ret_21d":     {"inputs": ["close"],       "func": dpe_ext_062_hjorth_complexity_ret_21d},
    "dpe_ext_063_waveform_length_ret_21d":       {"inputs": ["close"],       "func": dpe_ext_063_waveform_length_ret_21d},
    "dpe_ext_064_entropy_vol_diff_21d":          {"inputs": ["volume"],      "func": dpe_ext_064_entropy_vol_diff_21d},
    "dpe_ext_065_entropy_vol_logdiff_21d":       {"inputs": ["volume"],      "func": dpe_ext_065_entropy_vol_logdiff_21d},
    "dpe_ext_066_entropy_vol_diff_63d":          {"inputs": ["volume"],      "func": dpe_ext_066_entropy_vol_diff_63d},
    "dpe_ext_067_entropy_squared_ret_21d":       {"inputs": ["close"],       "func": dpe_ext_067_entropy_squared_ret_21d},
    "dpe_ext_068_entropy_squared_ret_63d":       {"inputs": ["close"],       "func": dpe_ext_068_entropy_squared_ret_63d},
    "dpe_ext_069_entropy_ret_12bin_21d":         {"inputs": ["close"],       "func": dpe_ext_069_entropy_ret_12bin_21d},
    "dpe_ext_070_zscore_ret_21d":                {"inputs": ["close"],       "func": dpe_ext_070_zscore_ret_21d},
    "dpe_ext_071_pctrank_ret_21d":               {"inputs": ["close"],       "func": dpe_ext_071_pctrank_ret_21d},
    "dpe_ext_072_autocorr_lag3_ret_21d":         {"inputs": ["close"],       "func": dpe_ext_072_autocorr_lag3_ret_21d},
    "dpe_ext_073_autocorr_lag10_ret_63d":        {"inputs": ["close"],       "func": dpe_ext_073_autocorr_lag10_ret_63d},
    "dpe_ext_074_autocorr_lag21_ret_63d":        {"inputs": ["close"],       "func": dpe_ext_074_autocorr_lag21_ret_63d},
    "dpe_ext_075_hjorth_mobility_close_21d":     {"inputs": ["close"],       "func": dpe_ext_075_hjorth_mobility_close_21d},
}
