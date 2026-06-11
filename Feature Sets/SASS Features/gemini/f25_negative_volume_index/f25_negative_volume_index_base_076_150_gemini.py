# Negative Volume Index (NVI) — real indicator implementation (variants 076..150)
# NVI is a cumulative index seeded at 1000 that moves by the price return ONLY on
# "low-volume" days (volume_t < volume_{t-1}); it carries forward unchanged on
# high-volume days. Returns use 'closeadj' (windows > 21d); volume uses raw 'volume'.
# This file extends the facet set with distinct windows and additional facets:
# dispersion, acceleration, EMA-cross regime persistence, dollar-volume gating,
# rolling drawdown of NVI, and NVI-vs-price beta-style spreads.
import numpy as np
import pandas as pd


def _nvi(closeadj, volume):
    ret = closeadj.pct_change()
    low_vol = volume < volume.shift(1)
    factor = pd.Series(1.0, index=closeadj.index)
    factor[low_vol] = 1.0 + ret[low_vol]
    factor = factor.fillna(1.0)
    nvi = 1000.0 * factor.cumprod()
    nvi[closeadj.isna() | volume.isna()] = np.nan
    return nvi


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return ((s - s.shift(w)) / w).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] > x[:-1]).sum() / max(len(x) - 1, 1), raw=True
    )


def get_f25_negative_volume_index_base_076_150(df):
    closeadj = df['closeadj']
    volume = df['volume']

    nvi = _nvi(closeadj, volume)
    lognvi = np.log(nvi.replace([np.inf, -np.inf], np.nan))
    dnvi = lognvi.diff()  # NVI log return (already only nonzero on low-vol days)

    features = {}

    def put(i, series):
        features[f'f25_negative_volume_index_{i:03d}'] = series

    i = 76

    # Facet M: NVI/EMA classic signal with finer span grid  -> 6
    for w in [13, 34, 55, 100, 150, 255]:
        ema = nvi.ewm(span=w, adjust=False).mean()
        put(i, (nvi / ema - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet N: NVI z-score, longer windows  -> 6
    for w in [30, 90, 150, 200, 300, 378]:
        put(i, _z(nvi, w)); i += 1

    # Facet O: NVI ROC, finer windows  -> 6
    for w in [5, 15, 30, 90, 150, 200]:
        put(i, _roc(nvi, w)); i += 1

    # Facet P: NVI acceleration (Δ of slope) normalized by level  -> 5
    for w in [10, 21, 42, 63, 126]:
        sl = _slope(nvi, w)
        put(i, (sl - sl.shift(w)).div(nvi).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet Q: dispersion of NVI log-returns (volatility of the index)  -> 6
    for w in [21, 42, 63, 126, 189, 252]:
        put(i, dnvi.rolling(w).std()); i += 1

    # Facet R: NVI percentile rank, more windows  -> 5
    for w in [30, 90, 150, 200, 300]:
        put(i, _pctrank(nvi, w)); i += 1

    # Facet S: above/below 255d-EMA regime persistence (fraction above EMA) -> 6
    ema255 = nvi.ewm(span=255, adjust=False).mean()
    above = (nvi > ema255).astype(float)
    above[nvi.isna() | ema255.isna()] = np.nan
    for w in [21, 42, 63, 126, 189, 252]:
        put(i, above.rolling(w).mean()); i += 1

    # Facet T: short-vs-long NVI EMA spread, alt pairs  -> 6
    pairs = [(5, 34), (13, 55), (21, 89), (34, 144), (55, 200), (89, 255)]
    for s_, l_ in pairs:
        es = nvi.ewm(span=s_, adjust=False).mean()
        el = nvi.ewm(span=l_, adjust=False).mean()
        put(i, (es / el - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet U: NVI rolling drawdown (distance below rolling max)  -> 6
    for w in [42, 63, 126, 189, 252, 378]:
        rollmax = nvi.rolling(w).max()
        put(i, (nvi / rollmax - 1.0).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet V: NVI-vs-price spread (NVI return minus price return) finer windows -> 6
    base_lognvi = lognvi - np.log(1000.0)
    for w in [10, 30, 90, 150, 200, 300]:
        price_ret = np.log(closeadj / closeadj.shift(w))
        nvi_ret = base_lognvi - base_lognvi.shift(w)
        put(i, (nvi_ret - price_ret).replace([np.inf, -np.inf], np.nan)); i += 1

    # Facet W: dollar-volume-gated smart-money return accumulation  -> 6
    # low-vol day return weighted by inverse dollar-volume rank (smart-money proxy)
    ret = closeadj.pct_change()
    low_vol = volume < volume.shift(1)
    dollar_vol = closeadj * volume
    dv_z = _z(dollar_vol, 63)
    sm_w = pd.Series(0.0, index=closeadj.index)
    sm_w[low_vol] = ret[low_vol] * (-dv_z[low_vol]).clip(lower=0).fillna(0.0)
    sm_w[closeadj.isna() | volume.isna()] = np.nan
    for w in [21, 42, 63, 126, 189, 252]:
        put(i, sm_w.rolling(w).sum()); i += 1

    # Facet X: NVI log-return z-score (index momentum), long windows  -> 5
    while i <= 150:
        for w in [63, 126, 189, 252, 378]:
            if i > 150:
                break
            put(i, _z(dnvi, w)); i += 1

    out = pd.DataFrame(features)
    return out
