# Real indicator: Hurst exponent via rescaled-range (R/S) analysis on log-returns.
# Part 2 (features 076..150): persistence/regime facets built on the same Hurst core --
# short-vs-long H spread/ratio, percentile rank, dispersion, slope/Delta, variance-ratio
# and autocorrelation persistence, DFA exponent, and interactions with range/volume.
# Windows {63,126,252,504} (all > 21d) => use 'closeadj'.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# helpers (mirror part 1; kept self-contained per spec)
# ---------------------------------------------------------------------------
def _logret(s):
    return np.log(s.replace(0.0, np.nan)).diff()


def _z(s, win):
    m = s.rolling(win).mean()
    sd = s.rolling(win).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, k):
    return (s - s.shift(k))


def _pctrank(s, win):
    return s.rolling(win).apply(
        lambda x: (x[-1] > x[:-1]).mean() if np.isfinite(x[-1]) else np.nan, raw=True)


def _rs_single(x):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    if x.size < 8:
        return np.nan
    m = x.mean()
    y = np.cumsum(x - m)
    R = y.max() - y.min()
    S = x.std(ddof=0)
    if S <= 0:
        return np.nan
    return R / S


def _rs_stat(rets, win):
    return rets.rolling(win).apply(_rs_single, raw=True)


def _hurst_single(x):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = x.size
    if n < 16:
        return np.nan
    rs = _rs_single(x)
    if rs is None or not np.isfinite(rs) or rs <= 0:
        return np.nan
    return np.log(rs) / np.log(n)


def _hurst_multi(x):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = x.size
    if n < 32:
        return np.nan
    scales = []
    s = 8
    while s <= n:
        scales.append(s)
        s = int(s * 1.6)
    scales = sorted(set([sc for sc in scales if sc <= n]))
    if len(scales) < 3:
        return np.nan
    logn, logrs = [], []
    for sc in scales:
        nblocks = n // sc
        if nblocks < 1:
            continue
        rss = []
        for b in range(nblocks):
            seg = x[b * sc:(b + 1) * sc]
            r = _rs_single(seg)
            if r is not None and np.isfinite(r) and r > 0:
                rss.append(r)
        if rss:
            logn.append(np.log(sc))
            logrs.append(np.log(np.mean(rss)))
    if len(logn) < 3:
        return np.nan
    return np.polyfit(np.asarray(logn), np.asarray(logrs), 1)[0]


def _dfa(x):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = x.size
    if n < 32:
        return np.nan
    y = np.cumsum(x - x.mean())
    scales = []
    s = 8
    while s <= n // 2:
        scales.append(s)
        s = int(s * 1.6)
    scales = sorted(set([sc for sc in scales if 4 <= sc <= n // 2]))
    if len(scales) < 3:
        return np.nan
    logn, logf = [], []
    idx = np.arange(n)
    for sc in scales:
        nblocks = n // sc
        if nblocks < 1:
            continue
        fluct = []
        for b in range(nblocks):
            seg = y[b * sc:(b + 1) * sc]
            t = idx[b * sc:(b + 1) * sc]
            coef = np.polyfit(t, seg, 1)
            trend = np.polyval(coef, t)
            fluct.append(np.mean((seg - trend) ** 2))
        if fluct:
            F = np.sqrt(np.mean(fluct))
            if F > 0:
                logn.append(np.log(sc))
                logf.append(np.log(F))
    if len(logn) < 3:
        return np.nan
    return np.polyfit(np.asarray(logn), np.asarray(logf), 1)[0]


def _hurst_series(rets, win, multi=True):
    fn = _hurst_multi if multi else _hurst_single
    return rets.rolling(win).apply(fn, raw=True)


def _dfa_series(rets, win):
    return rets.rolling(win).apply(_dfa, raw=True)


def _var_ratio(rets, win, k):
    v1 = rets.rolling(win).var()
    vk = rets.rolling(k).sum().rolling(win).var()
    return (vk / (k * v1)).replace([np.inf, -np.inf], np.nan)


def _autocorr(rets, win, lag):
    def _ac(x):
        x = np.asarray(x, dtype=float)
        x = x[~np.isnan(x)]
        if x.size < lag + 4:
            return np.nan
        a = x[:-lag]
        b = x[lag:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return np.corrcoef(a, b)[0, 1]
    return rets.rolling(win).apply(_ac, raw=True)


def get_f02_hurst_exponent_regimes_base_076_150(df):
    px = df['closeadj']
    rng = (df['high'] - df['low']) / df['close'].replace(0.0, np.nan)
    dvol = df['closeadj'] * df['volume']
    rets = _logret(px)
    features = {}
    windows = [63, 126, 252, 504]

    def put(i, s):
        features[f'f02_hurst_exponent_regimes_{i:03d}'] = s

    # Precompute the multi-scale Hurst at each window once.
    Hm = {w: _hurst_series(rets, w, multi=True) for w in windows}

    i = 76
    # --- Block I: short-vs-long Hurst spread & ratio (76..81) ---
    pairs = [(63, 126), (63, 252), (126, 252), (126, 504), (252, 504), (63, 504)]
    for a, b in pairs:
        put(i, Hm[a] - Hm[b]); i += 1   # spread (regime term-structure)

    # --- Block J: short/long Hurst ratio (82..87) ---
    for a, b in pairs:
        put(i, (Hm[a] / Hm[b].replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)); i += 1

    # --- Block K: Hurst z-score per window (88..91) ---
    for w in windows:
        put(i, _z(Hm[w], w)); i += 1

    # --- Block L: Hurst percentile rank per window (92..95) ---
    for w in windows:
        put(i, _pctrank(Hm[w], w)); i += 1

    # --- Block M: Hurst slope / Delta (k=21,63) per window (96..103) ---
    for w in windows:
        put(i, _roc(Hm[w], 21)); i += 1
        put(i, _roc(Hm[w], 63)); i += 1

    # --- Block N: Hurst dispersion (rolling std of H) per window (104..107) ---
    for w in windows:
        put(i, Hm[w].rolling(63).std()); i += 1

    # --- Block O: single-scale R/S-proxy Hurst regime distance (108..111) ---
    for w in windows:
        put(i, _hurst_series(rets, w, multi=False) - 0.5); i += 1

    # --- Block P: R/S statistic z-score & roc (112..119) ---
    for w in windows:
        rs = _rs_stat(rets, w)
        put(i, _z(rs, w)); i += 1
        put(i, _roc(rs, 21)); i += 1

    # --- Block Q: DFA exponent regime distance & slope (120..127) ---
    for w in windows:
        d = _dfa_series(rets, w)
        put(i, d - 0.5); i += 1
        put(i, _roc(d, 21)); i += 1

    # --- Block R: variance-ratio persistence (k=2,5,10) per window (128..139) ---
    for w in windows:
        for k in (2, 5, 10):
            put(i, _var_ratio(rets, w, k) - 1.0); i += 1

    # --- Block S: autocorrelation persistence (lag=1,3) per window (140..147) ---
    for w in windows:
        for lag in (1, 3):
            put(i, _autocorr(rets, w, lag)); i += 1

    # --- Block T: Hurst interactions with range & dollar-volume (148..150) ---
    put(i, (Hm[252] - 0.5) * _z(rng, 252)); i += 1          # 148 regime x range stress
    put(i, (Hm[126] - 0.5) * _z(dvol, 126)); i += 1         # 149 regime x volume
    put(i, (Hm[63] - 0.5) * np.sign(rets.rolling(63).mean())); i += 1  # 150 regime x drift sign

    return pd.DataFrame(features)
