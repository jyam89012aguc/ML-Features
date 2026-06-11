# f04_information_entropy — REAL indicator: information entropy of the return distribution.
# File 2 (076..150): volatility entropy (entropy of |returns| and squared returns),
# normalized vol entropy, vol-entropy slope/z-score, low-vs-high entropy regime distance,
# entropy dispersion, cross-window entropy ratios/spreads, more permutation & MI-proxy facets.
# Windows > 21d use 'closeadj'.
import numpy as np
import pandas as pd
from itertools import permutations

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _ret(df, window):
    col = 'close' if window <= 21 else 'closeadj'
    p = df[col].astype(float)
    return np.log(p / p.shift(1))


def _z(s, w=63):
    out = (s - s.rolling(w).mean()) / s.rolling(w).std()
    return out.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _shannon_from_counts(vals, k):
    vals = vals[np.isfinite(vals)]
    if vals.size < 2:
        return np.nan
    vmin, vmax = vals.min(), vals.max()
    if vmax <= vmin:
        return 0.0
    hist, _ = np.histogram(vals, bins=k, range=(vmin, vmax))
    tot = hist.sum()
    if tot <= 0:
        return np.nan
    p = hist[hist > 0] / tot
    return float(-np.sum(p * np.log(p)))


def _rolling_shannon(vals_series, window, k):
    return vals_series.rolling(window).apply(lambda x: _shannon_from_counts(np.asarray(x), k), raw=True)


def _perm_entropy_window(x, m):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = x.size
    if n < m + 1:
        return np.nan
    patt_idx = {p: i for i, p in enumerate(permutations(range(m)))}
    counts = np.zeros(len(patt_idx))
    for i in range(n - m + 1):
        order = tuple(np.argsort(x[i:i + m], kind='mergesort'))
        counts[patt_idx[order]] += 1
    tot = counts.sum()
    if tot <= 0:
        return np.nan
    p = counts[counts > 0] / tot
    return float(-np.sum(p * np.log(p)))


def _rolling_perm_entropy(ret, window, m):
    return ret.rolling(window).apply(lambda x: _perm_entropy_window(x, m), raw=True)


def _mi_autocorr_proxy_window(x, k):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if x.size < 4:
        return np.nan
    a = x[1:]
    b = x[:-1]

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
# file 2: features 076..150
# ---------------------------------------------------------------------------

def get_f04_information_entropy_base_076_150(df):
    features = {}

    def add(i, series):
        features[f'f04_information_entropy_{i:03d}'] = series

    windows = [21, 63, 126, 252]
    bins = [5, 8, 10, 16]

    i = 76

    # --- 076-091: vol entropy = Shannon entropy of |returns| (windows x bins) ---
    absent_cache = {}
    for w in windows:
        aret = _ret(df, w).abs()
        for k in bins:
            s = _rolling_shannon(aret, w, k)
            absent_cache[(w, k)] = s
            add(i, s)
            i += 1

    # --- 092-107: entropy of squared returns (windows x bins) ---
    sqent_cache = {}
    for w in windows:
        sret = _ret(df, w) ** 2
        for k in bins:
            s = _rolling_shannon(sret, w, k)
            sqent_cache[(w, k)] = s
            add(i, s)
            i += 1

    # --- 108-115: normalized vol entropy (|ret|) / log k ---
    for w in windows:
        for k in [8, 16]:
            s = absent_cache[(w, k)]
            add(i, (s / np.log(k)).replace([np.inf, -np.inf], np.nan))
            i += 1

    # --- 116-123: vol-entropy slope and short delta ---
    for w in windows:
        s = absent_cache[(w, 10)]
        add(i, _slope(s, w)); i += 1
        add(i, s - s.shift(5)); i += 1

    # --- 124-129: vol-entropy z-score (|ret| and squared) ---
    for w in [63, 126, 252]:
        add(i, _z(absent_cache[(w, 10)], max(63, w))); i += 1
    for w in [63, 126, 252]:
        add(i, _z(sqent_cache[(w, 10)], max(63, w))); i += 1

    # --- 130-137: low-vs-high entropy regime distance ---
    # distance of current entropy from its rolling regime band (median +/- range).
    for w in [63, 126, 252, 252]:
        # use return-entropy via |ret| proxy at k=10
        s = absent_cache[(w, 10)] if w != 252 else absent_cache[(252, 10)]
        med = s.rolling(max(63, w)).median()
        lo = s.rolling(max(63, w)).quantile(0.10)
        hi = s.rolling(max(63, w)).quantile(0.90)
        # signed distance to nearest regime edge, scaled by band width
        band = (hi - lo).replace(0, np.nan)
        add(i, ((s - med) / band).replace([np.inf, -np.inf], np.nan)); i += 1
        # distance from low-entropy floor (how far above ordered regime)
        add(i, ((s - lo) / band).replace([np.inf, -np.inf], np.nan)); i += 1

    # --- 138-141: entropy dispersion (rolling std of entropy series) ---
    for w in [63, 126, 252]:
        add(i, absent_cache[(w, 10)].rolling(max(63, w)).std()); i += 1
    add(i, sqent_cache[(252, 10)].rolling(63).std()); i += 1

    # --- 142-145: cross-window entropy spread / ratio (short vs long) ---
    s_short = absent_cache[(63, 10)]
    s_long = absent_cache[(252, 10)]
    add(i, s_short - s_long); i += 1
    add(i, (s_short / s_long).replace([np.inf, -np.inf], np.nan)); i += 1
    sq_short = sqent_cache[(63, 10)]
    sq_long = sqent_cache[(252, 10)]
    add(i, sq_short - sq_long); i += 1
    add(i, (sq_short / sq_long).replace([np.inf, -np.inf], np.nan)); i += 1

    # --- 146-148: permutation entropy of |returns| (vol ordinal regularity) ---
    for w in [63, 126, 252]:
        aret = _ret(df, w).abs()
        add(i, _rolling_perm_entropy(aret, w, 3)); i += 1

    # --- 149-150: MI-style proxy on |returns| (vol clustering / persistence) ---
    for w in [126, 252]:
        aret = _ret(df, w).abs()
        add(i, _rolling_mi_proxy(aret, w, 6)); i += 1

    out = pd.DataFrame(features)
    return out
