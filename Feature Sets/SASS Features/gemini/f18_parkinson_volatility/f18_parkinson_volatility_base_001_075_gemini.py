# Parkinson high-low volatility estimator family (base 001..075)
# Real indicator math (NOT an SMA placeholder):
#   Parkinson sig^2(n) = 1/(4*ln2) * mean( ln(high/low)^2 )  over n days
#   Parkinson vol = sqrt(sig^2) annualized by * sqrt(252)
#   Range uses RAW high/low. Close-to-close uses closeadj. Garman-Klass uses ln(C/O).
# Facets (this file): Parkinson vol level, Parkinson vs close-to-close ratio (efficiency),
#   Parkinson vs Garman-Klass, Parkinson z-score, slope/delta, vol-of-vol, cone percentile,
#   term-structure ratios, single-day ln(H/L)^2, Parkinson x dollar-volume.
import numpy as np
import pandas as pd

_ANN = np.sqrt(252.0)
_4LN2 = 4.0 * np.log(2.0)
_GKC = 2.0 * np.log(2.0) - 1.0


# ---------- log-range building blocks ----------
def _logs(df):
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    o = df['open'].astype(float)
    c = df['close'].astype(float)
    ca = df['closeadj'].astype(float)
    out = {}
    out['hl'] = np.log(h / l)               # Parkinson range (raw high/low)
    out['co'] = np.log(c / o)               # close-to-open (Garman-Klass term, raw)
    out['cc'] = np.log(ca / ca.shift(1))    # close-to-close (closeadj)
    out['dv'] = (ca * df['volume'].astype(float))   # dollar volume
    for key in ('hl', 'co', 'cc'):
        out[key] = out[key].replace([np.inf, -np.inf], np.nan)
    return out


# ---------- estimator cores ----------
def _park_var(lg, n):
    # Parkinson variance: 1/(4 ln2) * mean(ln(H/L)^2)
    return (lg['hl'] ** 2).rolling(n).mean() / _4LN2


def _park_vol(lg, n):
    return np.sqrt(_park_var(lg, n).clip(lower=0)) * _ANN


def _cc_vol(lg, n):
    # close-to-close (sample) volatility, annualized
    return lg['cc'].rolling(n).std() * _ANN


def _gk_vol(lg, n):
    # Garman-Klass: 0.5*ln(H/L)^2 - (2 ln2 -1)*ln(C/O)^2
    v = (0.5 * lg['hl'] ** 2 - _GKC * lg['co'] ** 2).rolling(n).mean()
    return np.sqrt(v.clip(lower=0)) * _ANN


# ---------- generic facet transforms ----------
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
    # rolling percentile rank of current value within trailing window (vol cone)
    return s.rolling(w).apply(
        lambda x: (x[-1] >= x).mean() if np.isfinite(x[-1]) else np.nan, raw=True)


def get_f18_parkinson_volatility_base_001_075(df):
    lg = _logs(df)
    f = {}
    W = [5, 10, 21, 63, 126, 252]

    pk = {w: _park_vol(lg, w) for w in W}
    cc = {w: _cc_vol(lg, w) for w in W}
    gk = {w: _gk_vol(lg, w) for w in W}

    feats = []

    # --- 1) Parkinson vol level (annualized) across 6 windows (6) ---
    for w in W:
        feats.append(pk[w])

    # --- 2) Parkinson vs close-to-close ratio = efficiency (6) ---
    for w in W:
        feats.append(_ratio(pk[w], cc[w]))

    # --- 3) Parkinson vs Garman-Klass ratio (6) ---
    for w in W:
        feats.append(_ratio(pk[w], gk[w]))

    # --- 4) Parkinson z-score (6) ---
    for w in W:
        feats.append(_z(pk[w], max(w, 63)))

    # --- 5) Parkinson slope / delta over window (6) ---
    for w in W:
        feats.append(_slope(pk[w], max(2, w // 2)))

    # --- 6) Parkinson vol-of-vol (6) ---
    for w in W:
        feats.append(_volofvol(pk[w], w))

    # --- 7) Parkinson vol-cone percentile (6) ---
    for w in W:
        feats.append(_cone_pct(pk[w], 252))

    # --- 8) Parkinson ROC / momentum (6) ---
    for w in W:
        feats.append(_roc(pk[w], max(2, w // 2)))

    # --- 9) Garman-Klass vol level (contrast estimator) (6) ---
    for w in W:
        feats.append(gk[w])

    # --- 10) Close-to-close vol level (contrast baseline) (6) ---
    for w in W:
        feats.append(cc[w])

    # 60 so far.
    # --- short-vs-long Parkinson term-structure ratios (5) ---
    feats.append(_ratio(pk[5], pk[21]))
    feats.append(_ratio(pk[5], pk[63]))
    feats.append(_ratio(pk[10], pk[63]))
    feats.append(_ratio(pk[21], pk[126]))
    feats.append(_ratio(pk[63], pk[252]))

    # 65. single-day ln(H/L)^2 and its smoothings / facets (5)
    hl2 = (lg['hl'] ** 2)
    feats.append(hl2)                              # single-day ln(H/L)^2
    feats.append(hl2.rolling(5).mean())            # short range energy
    feats.append(_z(hl2, 63))                      # single-day range z-score
    feats.append(_slope(hl2.rolling(5).mean(), 5)) # short-range momentum
    feats.append(hl2 / hl2.rolling(21).mean())     # range spike vs norm

    # 70. Parkinson x dollar-volume interactions (5)
    dv21 = lg['dv'].rolling(21).mean()
    dv63 = lg['dv'].rolling(63).mean()
    feats.append((pk[21] * dv21).replace([np.inf, -np.inf], np.nan))
    feats.append((pk[63] * dv63).replace([np.inf, -np.inf], np.nan))
    feats.append(_z((pk[21] * dv21).replace([np.inf, -np.inf], np.nan), 126))
    feats.append(_ratio(pk[5] * lg['dv'], dv21))   # range-weighted dollar flow vs norm
    feats.append((pk[126] * dv63).replace([np.inf, -np.inf], np.nan))

    # 75 -> exactly 75
    assert len(feats) == 75, len(feats)
    for i, s in enumerate(feats, start=1):
        f[f'f18_parkinson_volatility_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
