# Yang-Zhang volatility estimator family (base 001..075)
# Real indicator math (NOT an SMA placeholder):
#   YZ^2 = sig_overnight^2 + k*sig_open_close^2 + (1-k)*sig_RS^2
#   overnight  = ln(open / prev_close)
#   open_close = ln(close / open)
#   Rogers-Satchell sig_RS^2 = mean[ ln(high/close)*ln(high/open) + ln(low/close)*ln(low/open) ]
#   k = 0.34 / (1.34 + (n+1)/(n-1))
# Facets: YZ vol, components (overnight, open-close, Rogers-Satchell, Parkinson,
#   Garman-Klass), term-structure ratios, z-scores, slope/delta, vol-of-vol, cone percentile.
import numpy as np
import pandas as pd

_ANN = np.sqrt(252.0)


# ---------- log-return building blocks (raw OHLC for intraday range terms) ----------
def _logs(df):
    o = df['open'].astype(float)
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    c = df['close'].astype(float)
    pc = c.shift(1)
    out = {}
    out['ov'] = np.log(o / pc)              # overnight gap
    out['oc'] = np.log(c / o)               # open-to-close
    out['cc'] = np.log(c / c.shift(1))      # close-to-close
    out['hc'] = np.log(h / c)
    out['ho'] = np.log(h / o)
    out['lc'] = np.log(l / c)
    out['lo'] = np.log(l / o)
    out['hl'] = np.log(h / l)               # Parkinson range
    out['co'] = np.log(c / o)
    for key in out:
        out[key] = out[key].replace([np.inf, -np.inf], np.nan)
    return out


def _k(n):
    if n <= 1:
        return 0.34
    return 0.34 / (1.34 + (n + 1.0) / (n - 1.0))


def _rs(lg, n):
    # Rogers-Satchell variance (per-day term then rolling mean)
    term = lg['hc'] * lg['ho'] + lg['lc'] * lg['lo']
    return term.rolling(n).mean()


def _yz_var(lg, n):
    # Yang-Zhang variance components
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


def _rs_vol(lg, n):
    return np.sqrt(_rs(lg, n).clip(lower=0)) * _ANN


def _parkinson_vol(lg, n):
    # Parkinson: 1/(4 ln2) * mean(ln(H/L)^2)
    v = (lg['hl'] ** 2).rolling(n).mean() / (4.0 * np.log(2.0))
    return np.sqrt(v.clip(lower=0)) * _ANN


def _gk_vol(lg, n):
    # Garman-Klass: 0.5*ln(H/L)^2 - (2 ln2 -1)*ln(C/O)^2
    v = (0.5 * lg['hl'] ** 2 - (2.0 * np.log(2.0) - 1.0) * lg['co'] ** 2).rolling(n).mean()
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


def get_f01_yang_zhang_volatility_base_001_075(df):
    lg = _logs(df)
    f = {}
    W = [5, 10, 21, 63, 126, 252]

    # Precompute core vol series per window
    yz = {w: _yz_vol(lg, w) for w in W}
    ov = {w: _ov_vol(lg, w) for w in W}
    oc = {w: _oc_vol(lg, w) for w in W}
    rs = {w: _rs_vol(lg, w) for w in W}
    pk = {w: _parkinson_vol(lg, w) for w in W}
    gk = {w: _gk_vol(lg, w) for w in W}

    feats = []

    # --- 1) YZ vol level across 6 windows (6) ---
    for w in W:
        feats.append(yz[w])

    # --- 2) Overnight vol level (6) ---
    for w in W:
        feats.append(ov[w])

    # --- 3) Open-close vol level (6) ---
    for w in W:
        feats.append(oc[w])

    # --- 4) Rogers-Satchell vol level (6) ---
    for w in W:
        feats.append(rs[w])

    # --- 5) Parkinson vol level (6) ---
    for w in W:
        feats.append(pk[w])

    # --- 6) Garman-Klass vol level (6) ---
    for w in W:
        feats.append(gk[w])

    # --- 7) YZ z-score (6) ---
    for w in W:
        feats.append(_z(yz[w], max(w, 63)))

    # --- 8) YZ slope / delta over window (6) ---
    for w in W:
        feats.append(_slope(yz[w], max(2, w // 2)))

    # --- 9) YZ vol-of-vol (6) ---
    for w in W:
        feats.append(_volofvol(yz[w], w))

    # --- 10) YZ cone percentile (6) ---
    for w in W:
        feats.append(_cone_pct(yz[w], 252))

    # 60 so far. Term-structure ratios (short vs long) of YZ vol (5)
    feats.append(_ratio(yz[5], yz[21]))
    feats.append(_ratio(yz[5], yz[63]))
    feats.append(_ratio(yz[10], yz[63]))
    feats.append(_ratio(yz[21], yz[126]))
    feats.append(_ratio(yz[63], yz[252]))

    # 65. Component-mix ratios (contrast estimators) (5)
    feats.append(_ratio(ov[21], oc[21]))     # overnight vs intraday share
    feats.append(_ratio(rs[21], yz[21]))     # RS contribution
    feats.append(_ratio(pk[21], yz[21]))     # Parkinson vs YZ
    feats.append(_ratio(gk[21], pk[21]))     # GK vs Parkinson
    feats.append(_ratio(oc[63], yz[63]))     # open-close share long

    # 70. YZ ROC (vol momentum) (5)
    feats.append(_roc(yz[5], 5))
    feats.append(_roc(yz[21], 5))
    feats.append(_roc(yz[21], 21))
    feats.append(_roc(yz[63], 21))
    feats.append(_roc(yz[126], 21))

    # 75. exactly 75
    assert len(feats) == 75, len(feats)
    for i, s in enumerate(feats, start=1):
        f[f'f01_yang_zhang_volatility_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
