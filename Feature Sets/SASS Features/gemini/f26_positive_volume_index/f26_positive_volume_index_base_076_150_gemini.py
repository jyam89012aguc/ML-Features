# Positive Volume Index (PVI) — real indicator implementation (features 076-150)
# PVI accumulates price ROC only on high-volume days (volume_t > volume_{t-1});
# carries forward unchanged otherwise. Start at 1000.
# Returns use 'closeadj' (>21d math); volume comparison uses raw 'volume'.
# This file uses a complementary set of windows/facets to file 001-075 so all
# 150 features are distinct expressions.
import numpy as np
import pandas as pd

_BASE = 1000.0


def _ret(df):
    return df['closeadj'].pct_change()


def _pvi(df):
    """Positive Volume Index: accumulate return only on high-volume days."""
    ret = _ret(df).fillna(0.0).to_numpy()
    vol = df['volume'].to_numpy()
    up = np.empty(len(vol), dtype=bool)
    up[0] = False
    up[1:] = vol[1:] > vol[:-1]
    factor = np.where(up, 1.0 + ret, 1.0)
    pvi = _BASE * np.cumprod(factor)
    return pd.Series(pvi, index=df.index)


def _nvi(df):
    """Negative Volume Index companion (for divergence facet only)."""
    ret = _ret(df).fillna(0.0).to_numpy()
    vol = df['volume'].to_numpy()
    dn = np.empty(len(vol), dtype=bool)
    dn[0] = False
    dn[1:] = vol[1:] < vol[:-1]
    factor = np.where(dn, 1.0 + ret, 1.0)
    nvi = _BASE * np.cumprod(factor)
    return pd.Series(nvi, index=df.index)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=span).mean()


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return ((s - s.shift(w)) / (w * s.shift(w))).replace([np.inf, -np.inf], np.nan)


def _pctile(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] > x[:-1]).mean() if len(x) > 1 else np.nan, raw=True)


def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f26_positive_volume_index_base_076_150(df):
    features = {}
    pvi = _pvi(df)
    nvi = _nvi(df)
    ret = _ret(df)
    vol = df['volume']
    price = df['closeadj']

    log_pvi = np.log(pvi.replace(0, np.nan))
    log_nvi = np.log(nvi.replace(0, np.nan))

    # Complementary window set (shifted from file 1) to keep features distinct
    windows = [7, 14, 30, 50, 90, 180, 200]

    def put(i, series):
        features[f'f26_positive_volume_index_{i:03d}'] = _safe(series)

    i = 76

    # --- Facet 1: PVI level normalized by rolling median, 7 windows ---
    for w in windows:
        put(i, pvi / pvi.rolling(w).median() - 1.0)
        i += 1

    # --- Facet 2: PVI vs its EMA signal (log distance), 7 windows ---
    for w in windows:
        put(i, log_pvi - np.log(_ema(pvi, w)))
        i += 1

    # --- Facet 3: PVI ROC, 7 windows ---
    for w in windows:
        put(i, _roc(pvi, w))
        i += 1

    # --- Facet 4: PVI slope (normalized trend), 7 windows ---
    for w in windows:
        put(i, _slope(pvi, w))
        i += 1

    # --- Facet 5: PVI z-score, 7 windows ---
    for w in windows:
        put(i, _z(pvi, w))
        i += 1

    # --- Facet 6: PVI-vs-price spread (PVI ROC minus price ROC), 7 windows ---
    for w in windows:
        put(i, _roc(pvi, w) - _roc(price, w))
        i += 1

    # --- Facet 7: high-volume-day return accumulation (mean), 7 windows ---
    upvol = (vol > vol.shift(1))
    hv_ret = ret.where(upvol, 0.0)
    for w in windows:
        put(i, hv_ret.rolling(w).mean())
        i += 1

    # --- Facet 8: PVI above/below 255d-EMA regime (sign-distance), 7 windows ---
    ema255 = _ema(pvi, 255)
    for w in windows:
        put(i, (_ema(pvi, w) - ema255) / ema255)
        i += 1

    # --- Facet 9: PVI percentile rank, 7 windows ---
    for w in windows:
        put(i, _pctile(pvi, w))
        i += 1

    # --- Facet 10: short-vs-long PVI spread (EMA pairs) ---
    pairs = [(7, 30), (14, 50), (30, 90), (30, 180), (50, 180), (90, 200), (14, 200)]
    for a, b in pairs:
        put(i, _ema(pvi, a) / _ema(pvi, b) - 1.0)
        i += 1

    # --- Facet 11: crowd-flow proxy (mean crowd-day return), 3 windows ---
    crowd = (ret * upvol.astype(float))
    for w in [30, 90, 180]:
        cnt = upvol.rolling(w).sum()
        put(i, (crowd.rolling(w).sum() / cnt))
        i += 1

    # --- Facet 12: PVI - NVI-style divergence (log spread z-score), 2 windows ---
    div = log_pvi - log_nvi
    for w in [90, 180]:
        put(i, _z(div, w))
        i += 1

    return pd.DataFrame(features)
