# Real indicator: Hurst exponent via rescaled-range (R/S) analysis on log-returns.
# Over a window, R/S(n) ~ n^H; H is estimated from the slope of log(R/S) vs log(n)
# across sub-window sizes. H>0.5 => trending/persistent, H<0.5 => mean-reverting.
# Facets: H level, H-0.5 regime distance, R/S statistic, DFA-style fluctuation exponent,
# variance-ratio persistence, return autocorrelation, regime sign/streak, H slope/Delta.
# Windows {63,126,252,504} (all > 21d) => use 'closeadj'.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _logret(s):
    return np.log(s.replace(0.0, np.nan)).diff()


def _z(s, win):
    m = s.rolling(win).mean()
    sd = s.rolling(win).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, k):
    return (s - s.shift(k))


def _rs_single(x):
    # rescaled range of a 1-D array of returns (single scale)
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
    # rolling single-scale R/S statistic over `win`
    return rets.rolling(win).apply(_rs_single, raw=True)


def _hurst_single(x):
    # single-scale R/S proxy Hurst: H = log(R/S)/log(n)
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
    # multi-scale R/S Hurst: regress log(R/S) on log(n) across sub-window sizes
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = x.size
    if n < 32:
        return np.nan
    # choose a few scales between 8 and n
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
    logn = np.asarray(logn)
    logrs = np.asarray(logrs)
    slope = np.polyfit(logn, logrs, 1)[0]
    return slope


def _dfa(x):
    # detrended fluctuation analysis exponent on cumulative deviation of returns
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
    # variance ratio: var(k-day rets) / (k * var(1-day rets)). >1 persistent, <1 mean-revert.
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


def _streak(sign_series):
    # signed consecutive run length of a +/-1 series
    vals = sign_series.values
    out = np.full(vals.shape, np.nan)
    run = 0.0
    prev = 0.0
    for i, v in enumerate(vals):
        if np.isnan(v):
            run = 0.0
            prev = 0.0
            out[i] = np.nan
            continue
        if v == prev and v != 0:
            run += v
        else:
            run = v
        prev = v
        out[i] = run
    return pd.Series(out, index=sign_series.index)


def get_f02_hurst_exponent_regimes_base_001_075(df):
    px = df['closeadj']
    rets = _logret(px)
    features = {}
    windows = [63, 126, 252, 504]

    def put(i, s):
        features[f'f02_hurst_exponent_regimes_{i:03d}'] = s

    i = 1
    # --- Block A: multi-scale Hurst level + regime distance per window (1..16) ---
    for w in windows:
        H = _hurst_series(rets, w, multi=True)
        put(i, H); i += 1                       # H level
        put(i, H - 0.5); i += 1                 # regime distance H-0.5
        put(i, (H - 0.5).clip(lower=0)); i += 1 # persistent excess
        put(i, (0.5 - H).clip(lower=0)); i += 1 # mean-reversion excess

    # --- Block B: single-scale R/S-proxy Hurst per window (17..24) ---
    for w in windows:
        Hs = _hurst_series(rets, w, multi=False)
        put(i, Hs); i += 1
        put(i, Hs - 0.5); i += 1

    # --- Block C: raw R/S statistic + its log per window (25..32) ---
    for w in windows:
        rs = _rs_stat(rets, w)
        put(i, rs); i += 1
        put(i, np.log(rs.replace([np.inf, -np.inf], np.nan).clip(lower=1e-9))); i += 1

    # --- Block D: DFA fluctuation exponent + distance per window (33..40) ---
    for w in windows:
        d = _dfa_series(rets, w)
        put(i, d); i += 1
        put(i, d - 0.5); i += 1

    # --- Block E: variance ratio (k=2,5,10) per window (41..52) ---
    for w in windows:
        for k in (2, 5, 10):
            put(i, _var_ratio(rets, w, k) - 1.0); i += 1

    # --- Block F: return autocorrelation (lag=1,2,5) per window (53..64) ---
    for w in windows:
        for lag in (1, 2, 5):
            put(i, _autocorr(rets, w, lag)); i += 1

    # --- Block G: regime sign & streak from multi-scale Hurst (65..72) ---
    for w in windows:
        H = _hurst_series(rets, w, multi=True)
        sign = np.sign(H - 0.5)
        put(i, sign); i += 1
        put(i, _streak(sign)); i += 1

    # --- Block H: Hurst z-score / slope to fill to 75 (73..75) ---
    H252 = _hurst_series(rets, 252, multi=True)
    put(i, _z(H252, 252)); i += 1                       # 73 H z-score
    put(i, _roc(H252, 21)); i += 1                      # 74 H 21d slope/Delta
    put(i, _roc(H252, 63)); i += 1                      # 75 H 63d slope/Delta

    return pd.DataFrame(features)
