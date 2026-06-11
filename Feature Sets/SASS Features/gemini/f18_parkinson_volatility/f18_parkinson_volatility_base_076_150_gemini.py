# Parkinson high-low volatility estimator family (base 076..150)
# Real indicator math (NOT an SMA placeholder):
#   Parkinson sig^2(n) = 1/(4*ln2) * mean( ln(high/low)^2 )  over n days
#   Parkinson vol = sqrt(sig^2) annualized by * sqrt(252)
#   Range uses RAW high/low. Close-to-close uses closeadj. Garman-Klass uses ln(C/O).
# Facets (this file): more z-scores/cone percentiles, regime distance, vol-of-vol,
#   efficiency-ratio dynamics, GK-divergence, term-structure across estimators,
#   single-day range interactions, Parkinson x dollar-volume.
import numpy as np
import pandas as pd

_ANN = np.sqrt(252.0)
_4LN2 = 4.0 * np.log(2.0)
_GKC = 2.0 * np.log(2.0) - 1.0


def _logs(df):
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    o = df['open'].astype(float)
    c = df['close'].astype(float)
    ca = df['closeadj'].astype(float)
    out = {}
    out['hl'] = np.log(h / l)
    out['co'] = np.log(c / o)
    out['cc'] = np.log(ca / ca.shift(1))
    out['dv'] = (ca * df['volume'].astype(float))
    for key in ('hl', 'co', 'cc'):
        out[key] = out[key].replace([np.inf, -np.inf], np.nan)
    return out


def _park_var(lg, n):
    return (lg['hl'] ** 2).rolling(n).mean() / _4LN2


def _park_vol(lg, n):
    return np.sqrt(_park_var(lg, n).clip(lower=0)) * _ANN


def _cc_vol(lg, n):
    return lg['cc'].rolling(n).std() * _ANN


def _gk_vol(lg, n):
    v = (0.5 * lg['hl'] ** 2 - _GKC * lg['co'] ** 2).rolling(n).mean()
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


def get_f18_parkinson_volatility_base_076_150(df):
    lg = _logs(df)
    f = {}
    W = [5, 10, 21, 63, 126, 252]

    pk = {w: _park_vol(lg, w) for w in W}
    cc = {w: _cc_vol(lg, w) for w in W}
    gk = {w: _gk_vol(lg, w) for w in W}
    eff = {w: _ratio(pk[w], cc[w]) for w in W}   # Parkinson efficiency ratio

    feats = []

    # --- 1) Parkinson regime distance vs rolling median (6) ---
    for w in W:
        feats.append(_regime_dist(pk[w], max(w, 63)))

    # --- 2) Parkinson efficiency-ratio z-score (6) ---
    for w in W:
        feats.append(_z(eff[w], max(w, 63)))

    # --- 3) Parkinson efficiency-ratio slope/delta (6) ---
    for w in W:
        feats.append(_slope(eff[w], max(2, w // 2)))

    # --- 4) Parkinson vs GK z-score (estimator divergence) (6) ---
    for w in W:
        feats.append(_z(_ratio(pk[w], gk[w]), max(w, 63)))

    # --- 5) Parkinson cone percentile on long lookback (6) ---
    for w in W:
        feats.append(_cone_pct(pk[w], 126))

    # --- 6) Parkinson variance (sig^2) level, annualized (6) ---
    for w in W:
        feats.append((_park_var(lg, w) * 252.0))

    # --- 7) Parkinson vol-of-vol on long window (6) ---
    for w in W:
        feats.append(_volofvol(pk[w], max(w, 21)))

    # --- 8) Garman-Klass z-score (6) ---
    for w in W:
        feats.append(_z(gk[w], max(w, 63)))

    # --- 9) Close-to-close z-score (contrast) (6) ---
    for w in W:
        feats.append(_z(cc[w], max(w, 63)))

    # --- 10) Parkinson efficiency-ratio cone percentile (6) ---
    for w in W:
        feats.append(_cone_pct(eff[w], 252))

    # 60 so far.
    # --- short-vs-long term-structure ratios across estimators (5) ---
    feats.append(_ratio(pk[10], pk[252]))
    feats.append(_ratio(gk[5], gk[63]))
    feats.append(_ratio(cc[5], cc[63]))
    feats.append(_ratio(eff[5], eff[63]))
    feats.append(_ratio(pk[21], pk[252]))

    # 65. estimator-divergence / regime interactions (5)
    feats.append(pk[21] - gk[21])                  # Parkinson-GK vol spread (drift signal)
    feats.append(_ratio(gk[63], cc[63]))           # GK vs CC
    feats.append(_slope(eff[21], 21))              # efficiency momentum
    feats.append(_regime_dist(eff[63], 252))       # efficiency regime distance
    feats.append(_ratio(pk[5] * pk[21], pk[63] ** 2))  # convexity of term-structure

    # 70. single-day range + Parkinson x dollar-volume (5)
    hl2 = (lg['hl'] ** 2)
    dv63 = lg['dv'].rolling(63).mean()
    dv126 = lg['dv'].rolling(126).mean()
    feats.append(_roc(hl2.rolling(10).mean(), 10))       # 10d range energy momentum
    feats.append(_cone_pct(hl2.rolling(21).mean(), 252)) # smoothed range cone
    feats.append((pk[252] * dv126).replace([np.inf, -np.inf], np.nan))
    feats.append(_z((pk[63] * dv63).replace([np.inf, -np.inf], np.nan), 252))
    feats.append(_ratio(pk[126] * dv63, dv126))          # range-weighted flow vs norm

    # 75 -> these are global indices 076..150
    assert len(feats) == 75, len(feats)
    for j, s in enumerate(feats):
        i = 76 + j
        f[f'f18_parkinson_volatility_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
