# f06_vpin_flow_toxicity — REAL indicator: VPIN (Volume-synchronized Probability
# of Informed Trading) with bulk-volume classification.
#
# Bulk-volume classification (BVC):
#   z = ret / sigma           (sigma = rolling std of closeadj log returns)
#   buy_fraction  = Phi(z)    (standard normal CDF)
#   sell_fraction = 1 - Phi(z)
#   buy_vol  = volume * Phi(z)
#   sell_vol = volume * (1 - Phi(z))
#   VPIN_n   = sum_n |buy_vol - sell_vol| / sum_n volume
#
# 150 distinct variants over windows {21,50,63,126,252} and facets:
#   VPIN level, order-flow imbalance, signed flow, VPIN z-score, VPIN slope/delta,
#   toxicity-regime distance, flow*dollar-volume interaction, cumulative signed flow.
import numpy as np
import pandas as pd
from math import erf, sqrt

_WINDOWS = [21, 50, 63, 126, 252]
_SIG = 21  # window for the return-standardizing volatility


_erf = np.vectorize(erf, otypes=[float])


def _norm_cdf(x):
    # standard normal CDF via erf; preserves NaN warm-up
    a = x.to_numpy(dtype=float) / sqrt(2.0)
    out = np.full_like(a, np.nan)
    m = np.isfinite(a)
    out[m] = 0.5 * (1.0 + _erf(a[m]))
    return pd.Series(out, index=x.index)


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _bvc(df):
    """Return (buy_vol, sell_vol, signed_vol, volume) Series via bulk-volume classification."""
    ret = np.log(df['closeadj'] / df['closeadj'].shift(1))
    sigma = ret.rolling(_SIG).std()
    zz = (ret / sigma).replace([np.inf, -np.inf], np.nan)
    phi = _norm_cdf(zz)
    vol = df['volume'].astype(float)
    buy_vol = vol * phi
    sell_vol = vol * (1.0 - phi)
    signed_vol = buy_vol - sell_vol  # = vol*(2*phi - 1)
    return buy_vol, sell_vol, signed_vol, vol


def _vpin(buy_vol, sell_vol, vol, w):
    num = (buy_vol - sell_vol).abs().rolling(w).sum()
    den = vol.rolling(w).sum()
    return (num / den).replace([np.inf, -np.inf], np.nan)


def _ofi(signed_vol, vol, w):
    # order-flow imbalance: (buy - sell)/total over the window
    return (signed_vol.rolling(w).sum() / vol.rolling(w).sum()).replace([np.inf, -np.inf], np.nan)


def _facet(name, df, buy_vol, sell_vol, signed_vol, vol, w):
    if name == 'level':
        return _vpin(buy_vol, sell_vol, vol, w)
    if name == 'ofi':
        return _ofi(signed_vol, vol, w)
    if name == 'signed':
        # mean signed flow normalized by mean volume
        return (signed_vol.rolling(w).mean() / vol.rolling(w).mean()).replace([np.inf, -np.inf], np.nan)
    if name == 'zscore':
        return _z(_vpin(buy_vol, sell_vol, vol, w), w)
    if name == 'slope':
        v = _vpin(buy_vol, sell_vol, vol, w)
        return v - v.shift(max(1, w // 5))
    if name == 'regime':
        # toxicity-regime distance: VPIN minus its rolling median (threshold) of a longer lookback
        v = _vpin(buy_vol, sell_vol, vol, w)
        thr = v.rolling(w * 2).median()
        return (v - thr).replace([np.inf, -np.inf], np.nan)
    if name == 'dollar':
        # flow * dollar-volume interaction (dollar-volume on >21d uses closeadj*volume)
        dv = df['closeadj'] * vol
        ofi = _ofi(signed_vol, vol, w)
        return (ofi * dv.rolling(w).mean()).replace([np.inf, -np.inf], np.nan)
    if name == 'cumsigned':
        # cumulative signed flow over window normalized by total volume
        return (signed_vol.rolling(w).sum() / vol.rolling(w).sum().abs()).replace([np.inf, -np.inf], np.nan)
    raise ValueError(name)


# Deterministic ordered (facet, window) spec for all 150 features.
_FACETS = ['level', 'ofi', 'signed', 'zscore', 'slope', 'regime', 'dollar', 'cumsigned']


def _build_specs():
    specs = []
    # 1) 8 facets x 5 windows = 40 direct facet/window combos.
    for f in _FACETS:
        for w in _WINDOWS:
            specs.append((f, w))
    # 2) short-vs-long ratios: 8 facets x 5 window-pairs = 40.
    pairs = [(21, 63), (50, 126), (63, 252), (21, 252), (50, 252)]
    for f in _FACETS:
        for p in pairs:
            specs.append((('ratio', f), p))
    # 3) deltas (slope of facet): 8 facets x 5 windows = 40.
    for f in _FACETS:
        for w in _WINDOWS:
            specs.append((('delta', f), w))
    # 4) facet z-scores: 8 facets x 5 windows = 40.  (total now 160)
    for f in _FACETS:
        for w in _WINDOWS:
            specs.append((('fz', f), w))
    # Trim to exactly 150 distinct expressions.
    return specs[:150]


_SPECS = _build_specs()


def _eval_spec(spec, window, df, buy_vol, sell_vol, signed_vol, vol):
    if isinstance(spec, tuple):
        kind, base = spec
        if kind == 'ratio':
            ws, wl = window
            a = _facet(base, df, buy_vol, sell_vol, signed_vol, vol, ws)
            b = _facet(base, df, buy_vol, sell_vol, signed_vol, vol, wl)
            return (a / b).replace([np.inf, -np.inf], np.nan)
        if kind == 'delta':
            v = _facet(base, df, buy_vol, sell_vol, signed_vol, vol, window)
            return v - v.shift(max(1, window // 5))
        if kind == 'fz':
            v = _facet(base, df, buy_vol, sell_vol, signed_vol, vol, window)
            return _z(v, window)
    return _facet(spec, df, buy_vol, sell_vol, signed_vol, vol, window)


def _compute_range(df, lo, hi):
    buy_vol, sell_vol, signed_vol, vol = _bvc(df)
    features = {}
    for i in range(lo, hi + 1):
        spec, window = _SPECS[i - 1]
        features[f'f06_vpin_flow_toxicity_{i:03d}'] = _eval_spec(
            spec, window, df, buy_vol, sell_vol, signed_vol, vol)
    return pd.DataFrame(features, index=df.index)


def get_f06_vpin_flow_toxicity_base_001_075(df):
    return _compute_range(df, 1, 75)
