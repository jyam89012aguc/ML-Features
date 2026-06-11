# Yang-Zhang volatility estimator family (base 076..150)
# Real indicator math (NOT an SMA placeholder):
#   YZ^2 = sig_overnight^2 + k*sig_open_close^2 + (1-k)*sig_RS^2
#   overnight  = ln(open / prev_close)
#   open_close = ln(close / open)
#   Rogers-Satchell sig_RS^2 = mean[ ln(high/close)*ln(high/open) + ln(low/close)*ln(low/open) ]
#   k = 0.34 / (1.34 + (n+1)/(n-1))
# Facets (this file): more z-scores/cone percentiles on components, term-structure
#   for each estimator, vol-of-vol, slope/delta, regime/threshold distance, and
#   estimator-divergence interactions.
import numpy as np
import pandas as pd

_ANN = np.sqrt(252.0)


def _logs(df):
    o = df['open'].astype(float)
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    c = df['close'].astype(float)
    pc = c.shift(1)
    out = {}
    out['ov'] = np.log(o / pc)
    out['oc'] = np.log(c / o)
    out['cc'] = np.log(c / c.shift(1))
    out['hc'] = np.log(h / c)
    out['ho'] = np.log(h / o)
    out['lc'] = np.log(l / c)
    out['lo'] = np.log(l / o)
    out['hl'] = np.log(h / l)
    out['co'] = np.log(c / o)
    for key in out:
        out[key] = out[key].replace([np.inf, -np.inf], np.nan)
    return out


def _k(n):
    if n <= 1:
        return 0.34
    return 0.34 / (1.34 + (n + 1.0) / (n - 1.0))


def _rs(lg, n):
    term = lg['hc'] * lg['ho'] + lg['lc'] * lg['lo']
    return term.rolling(n).mean()


def _yz_var(lg, n):
    ov_mean = lg['ov'].rolling(n).mean()
    oc_mean = lg['oc'].rolling(n).mean()
    sig_ov = ((lg['ov'] - ov_mean) ** 2).rolling(n).sum() / (n - 1)
    sig_oc = ((lg['oc'] - oc_mean) ** 2).rolling(n).sum() / (n - 1)
    sig_rs = _rs(lg, n)
    k = _k(n)
    return sig_ov + k * sig_oc + (1.0 - k) * sig_rs


def _yz_vol(lg, n):
    v = _yz_var(lg, n)
    return np.sqrt(v.clip(lower=0)) * _ANN


def _ov_vol(lg, n):
    return lg['ov'].rolling(n).std() * _ANN


def _oc_vol(lg, n):
    return lg['oc'].rolling(n).std() * _ANN


def _cc_vol(lg, n):
    return lg['cc'].rolling(n).std() * _ANN


def _rs_vol(lg, n):
    return np.sqrt(_rs(lg, n).clip(lower=0)) * _ANN


def _parkinson_vol(lg, n):
    v = (lg['hl'] ** 2).rolling(n).mean() / (4.0 * np.log(2.0))
    return np.sqrt(v.clip(lower=0)) * _ANN


def _gk_vol(lg, n):
    v = (0.5 * lg['hl'] ** 2 - (2.0 * np.log(2.0) - 1.0) * lg['co'] ** 2).rolling(n).mean()
    return np.sqrt(v.clip(lower=0)) * _ANN


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return (s - s.shift(w)).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _ratio(a, b):
    return (a / b).replace([np.inf, -np.inf], np.nan)


def _volofvol(s, w):
    return s.rolling(w).std()


def _cone_pct(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] >= x).mean() if np.isfinite(x[-1]) else np.nan, raw=True)


def _regime_dist(s, w):
    # distance of current vol from its rolling median, in rolling-std units
    med = s.rolling(w).median()
    sd = s.rolling(w).std()
    return ((s - med) / sd).replace([np.inf, -np.inf], np.nan)


def get_f01_yang_zhang_volatility_base_076_150(df):
    lg = _logs(df)
    f = {}
    W = [5, 10, 21, 63, 126, 252]

    yz = {w: _yz_vol(lg, w) for w in W}
    ov = {w: _ov_vol(lg, w) for w in W}
    oc = {w: _oc_vol(lg, w) for w in W}
    cc = {w: _cc_vol(lg, w) for w in W}
    rs = {w: _rs_vol(lg, w) for w in W}
    pk = {w: _parkinson_vol(lg, w) for w in W}
    gk = {w: _gk_vol(lg, w) for w in W}

    feats = []

    # --- 1) Close-to-close vol level (contrast baseline) (6) ---
    for w in W:
        feats.append(cc[w])

    # --- 2) YZ vs close-to-close ratio (variance-ratio style) (6) ---
    for w in W:
        feats.append(_ratio(yz[w], cc[w]))

    # --- 3) Overnight z-score (6) ---
    for w in W:
        feats.append(_z(ov[w], max(w, 63)))

    # --- 4) Open-close z-score (6) ---
    for w in W:
        feats.append(_z(oc[w], max(w, 63)))

    # --- 5) Rogers-Satchell z-score (6) ---
    for w in W:
        feats.append(_z(rs[w], max(w, 63)))

    # --- 6) Parkinson cone percentile (6) ---
    for w in W:
        feats.append(_cone_pct(pk[w], 252))

    # --- 7) Garman-Klass slope/delta (6) ---
    for w in W:
        feats.append(_slope(gk[w], max(2, w // 2)))

    # --- 8) Rogers-Satchell vol-of-vol (6) ---
    for w in W:
        feats.append(_volofvol(rs[w], w))

    # --- 9) YZ regime distance vs rolling median (6) ---
    for w in W:
        feats.append(_regime_dist(yz[w], max(w, 63)))

    # --- 10) Overnight vol-of-vol (6) ---
    for w in W:
        feats.append(_volofvol(ov[w], w))

    # 60 so far.
    # --- term-structure ratios for components (5) ---
    feats.append(_ratio(ov[5], ov[63]))
    feats.append(_ratio(oc[5], oc[63]))
    feats.append(_ratio(rs[5], rs[63]))
    feats.append(_ratio(pk[10], pk[126]))
    feats.append(_ratio(gk[21], gk[252]))

    # 65. estimator-divergence interactions (5)
    feats.append(_slope(_ratio(yz[21], cc[21]), 21))   # variance-ratio momentum
    feats.append(_ratio(pk[63], rs[63]))               # Parkinson vs RS (drift sensitivity)
    feats.append(_ratio(gk[63], cc[63]))               # GK vs CC
    feats.append(ov[21] - oc[21])                       # gap-vs-intraday vol spread
    feats.append(_ratio(yz[10], yz[252]))              # full term-structure slope

    # 70. component momentum / cone (5)
    feats.append(_roc(rs[21], 21))
    feats.append(_roc(ov[21], 21))
    feats.append(_cone_pct(rs[63], 252))
    feats.append(_cone_pct(oc[63], 252))
    feats.append(_z(gk[126], 252))

    # 75 -> these are global indices 076..150
    assert len(feats) == 75, len(feats)
    for j, s in enumerate(feats):
        i = 76 + j
        f[f'f01_yang_zhang_volatility_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
