# f04_information_entropy — REAL indicator: information entropy of the return distribution.
# Facets: Shannon entropy (binned), normalized entropy (/log k), permutation entropy
# (ordinal patterns length m), sample/approximate-entropy-style regularity, entropy of
# |returns| and squared returns (vol entropy), entropy slope/delta, entropy z-score,
# low-vs-high-entropy regime distance, rolling MI-style autocorrelation proxy.
# Windows > 21d use 'closeadj'.
import math
import numpy as np
import pandas as pd
from itertools import permutations

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _ret(df, window):
    """Daily log returns. Windows > 21d use closeadj, else raw close."""
    col = 'close' if window <= 21 else 'closeadj'
    p = df[col].astype(float)
    return np.log(p / p.shift(1))


def _z(s, w=63):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    out = (s - m) / sd
    return out.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    """Per-bar slope of s over window w via simple (last-first)/w difference quotient."""
    return (s - s.shift(w)) / float(w)


def _shannon_from_counts(vals, k):
    """Shannon entropy (nats) of an array binned into k equal-width bins."""
    vals = vals[np.isfinite(vals)]
    if vals.size < 2:
        return np.nan
    vmin = vals.min()
    vmax = vals.max()
    if vmax <= vmin:
        return 0.0
    hist, _ = np.histogram(vals, bins=k, range=(vmin, vmax))
    tot = hist.sum()
    if tot <= 0:
        return np.nan
    p = hist[hist > 0] / tot
    return float(-np.sum(p * np.log(p)))


def _rolling_shannon(ret, window, k):
    """Rolling Shannon entropy (nats) of returns binned into k bins."""
    return ret.rolling(window).apply(lambda x: _shannon_from_counts(np.asarray(x), k), raw=True)


def _perm_entropy_window(x, m):
    """Permutation entropy (nats) of a 1D window for ordinal pattern length m."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    if n < m + 1:
        return np.nan
    # build the m! pattern dictionary
    patt_idx = {p: i for i, p in enumerate(permutations(range(m)))}
    counts = np.zeros(len(patt_idx))
    for i in range(n - m + 1):
        window = x[i:i + m]
        order = tuple(np.argsort(window, kind='mergesort'))
        counts[patt_idx[order]] += 1
    tot = counts.sum()
    if tot <= 0:
        return np.nan
    p = counts[counts > 0] / tot
    return float(-np.sum(p * np.log(p)))


def _rolling_perm_entropy(ret, window, m):
    return ret.rolling(window).apply(lambda x: _perm_entropy_window(x, m), raw=True)


def _sampen_window(x, m, r_mult):
    """Sample-entropy-style regularity of a 1D window (m=embedding, r=r_mult*std)."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    if n < m + 2:
        return np.nan
    sd = x.std()
    if sd == 0:
        return 0.0
    r = r_mult * sd

    def _phi(mm):
        templates = np.array([x[i:i + mm] for i in range(n - mm + 1)])
        cnt = 0
        nt = templates.shape[0]
        for i in range(nt):
            d = np.max(np.abs(templates - templates[i]), axis=1)
            cnt += np.sum(d <= r) - 1  # exclude self-match
        return cnt

    B = _phi(m)
    A = _phi(m + 1)
    if B <= 0 or A <= 0:
        return np.nan
    return float(-np.log(A / B))


def _rolling_sampen(ret, window, m, r_mult):
    return ret.rolling(window).apply(lambda x: _sampen_window(x, m, r_mult), raw=True)


def _mi_autocorr_proxy_window(x, k):
    """MI-style proxy: joint entropy of (x_t, x_{t-1}) binned into k bins along each axis;
    proxy MI = H(x) + H(x_lag) - H(x, x_lag). Higher => stronger dependence."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if x.size < 4:
        return np.nan
    a = x[1:]
    b = x[:-1]
    if a.size < 2:
        return np.nan

    def _ent1(v):
        vmin, vmax = v.min(), v.max()
        if vmax <= vmin:
            return 0.0
        h, _ = np.histogram(v, bins=k, range=(vmin, vmax))
        t = h.sum()
        pp = h[h > 0] / t
        return -np.sum(pp * np.log(pp))

    amin, amax = a.min(), a.max()
    bmin, bmax = b.min(), b.max()
    if amax <= amin or bmax <= bmin:
        return 0.0
    hj, _, _ = np.histogram2d(a, b, bins=k, range=[[amin, amax], [bmin, bmax]])
    tj = hj.sum()
    if tj <= 0:
        return np.nan
    pj = hj[hj > 0] / tj
    Hj = -np.sum(pj * np.log(pj))
    return float(_ent1(a) + _ent1(b) - Hj)


def _rolling_mi_proxy(ret, window, k):
    return ret.rolling(window).apply(lambda x: _mi_autocorr_proxy_window(x, k), raw=True)


# ---------------------------------------------------------------------------
# file 1: features 001..075
# ---------------------------------------------------------------------------

def get_f04_information_entropy_base_001_075(df):
    features = {}

    def add(i, series):
        features[f'f04_information_entropy_{i:03d}'] = series

    windows = [21, 63, 126, 252]
    bins = [5, 8, 10, 16]

    # --- 001-016: Shannon entropy level of returns (windows x bins) ---
    i = 1
    shannon_cache = {}
    for w in windows:
        ret = _ret(df, w)
        for k in bins:
            s = _rolling_shannon(ret, w, k)
            shannon_cache[(w, k)] = s
            add(i, s)
            i += 1

    # --- 017-032: normalized Shannon entropy (/ log k) ---
    for w in windows:
        for k in bins:
            s = shannon_cache[(w, k)]
            add(i, (s / np.log(k)).replace([np.inf, -np.inf], np.nan))
            i += 1

    # --- 033-040: entropy slope (per-bar delta over its own window) ---
    for w in windows:
        for k in [8, 16]:
            s = shannon_cache[(w, k)]
            add(i, _slope(s, w))
            i += 1

    # --- 041-048: entropy short Delta (5-bar change) ---
    for w in windows:
        for k in [8, 16]:
            s = shannon_cache[(w, k)]
            add(i, s - s.shift(5))
            i += 1

    # --- 049-056: entropy z-score (regime standardization) ---
    for w in windows:
        for k in [8, 16]:
            s = shannon_cache[(w, k)]
            add(i, _z(s, max(63, w)))
            i += 1

    # --- 057-066: permutation entropy (ordinal patterns) windows x orders m ---
    for w in [63, 126, 252]:
        ret = _ret(df, w)
        for m in [3, 4]:
            add(i, _rolling_perm_entropy(ret, w, m))
            i += 1
    # two extra perm-entropy variants normalized by log(m!)
    for w, m in [(63, 5), (126, 5), (252, 4), (21, 3)]:
        ret = _ret(df, w)
        pe = _rolling_perm_entropy(ret, w, m)
        norm = np.log(math.factorial(m))
        add(i, (pe / norm).replace([np.inf, -np.inf], np.nan))
        i += 1

    # --- 067-072: sample/approximate-entropy-style regularity ---
    for w in [63, 126, 252]:
        ret = _ret(df, w)
        for r_mult in [0.2, 0.35]:
            add(i, _rolling_sampen(ret, w, 2, r_mult))
            i += 1

    # --- 073-075: MI-style rolling autocorrelation proxy ---
    for w in [63, 126, 252]:
        ret = _ret(df, w)
        add(i, _rolling_mi_proxy(ret, w, 6))
        i += 1

    out = pd.DataFrame(features)
    return out
