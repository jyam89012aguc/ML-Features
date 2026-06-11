# Real indicator: Kaufman Efficiency Ratio (ER) and KAMA (Kaufman Adaptive MA)
# ER(n) = |close - close.shift(n)| / sum(|close.diff()|) over n   (net change / total path)
# KAMA  = adaptive MA; smoothing constant SC = (ER*(fast-slow)+slow)^2,
#         fast = 2/(2+1), slow = 2/(30+1).
# 150 distinct variants over windows {10,21,63,126,252} and facets:
#   ER level, 1-ER (noise), KAMA, price-KAMA, price/KAMA-1, KAMA slope,
#   ER z-score, ER slope/delta, ER regime (trend vs chop) distance,
#   ER on closeadj vs ER on (high+low)/2.
# Rule: windows > 21d use 'closeadj'.
import numpy as np
import pandas as pd

_FAST = 2.0 / (2.0 + 1.0)    # fast smoothing constant
_SLOW = 2.0 / (30.0 + 1.0)   # slow smoothing constant


def _src(df, window):
    # windows > 21 trading days use closeadj
    return df['closeadj'] if window > 21 else df['close']


def _er(price, n):
    # Kaufman Efficiency Ratio: |net change| / total path over n
    change = (price - price.shift(n)).abs()
    volatility = price.diff().abs().rolling(n).sum()
    er = change / volatility
    return er.replace([np.inf, -np.inf], np.nan)


def _kama(price, n):
    # Kaufman Adaptive Moving Average driven by ER(n)
    er = _er(price, n).fillna(0.0)
    sc = (er * (_FAST - _SLOW) + _SLOW) ** 2
    p = price.to_numpy(dtype=float)
    s = sc.to_numpy(dtype=float)
    out = np.full(p.shape, np.nan)
    # seed: first valid index after warm-up (need n+1 points for ER path)
    start = n
    if start < len(p) and not np.isnan(p[start]):
        out[start] = p[start]
        prev = p[start]
        for j in range(start + 1, len(p)):
            if np.isnan(p[j]):
                out[j] = prev
                continue
            prev = prev + s[j] * (p[j] - prev)
            out[j] = prev
    return pd.Series(out, index=price.index)


def _z(s, lb):
    return ((s - s.rolling(lb).mean()) / s.rolling(lb).std()).replace([np.inf, -np.inf], np.nan)


def _slope(s, lb):
    # simple per-bar slope over lb bars
    return (s - s.shift(lb)) / float(lb)


def _hl2(df):
    return (df['high'] + df['low']) / 2.0


def _build(df, idx_range):
    """Construct the full ordered list of 150 facet specs and return the slice
    of feature Series for the requested 1-based index range (inclusive)."""
    windows = [10, 21, 63, 126, 252]

    # Pre-compute ER / KAMA per window on the window-appropriate source.
    er = {}
    kama = {}
    price = {}
    for w in windows:
        p = _src(df, w)
        price[w] = p
        er[w] = _er(p, w)
        kama[w] = _kama(p, w)
    hl2 = _hl2(df)
    er_hl2 = {w: _er(hl2, w) for w in windows}

    feats = []  # list of (Series,) built in canonical order

    # Facet group A: ER level (5)
    for w in windows:
        feats.append(er[w])
    # Facet group B: 1 - ER  (noise ratio) (5)
    for w in windows:
        feats.append(1.0 - er[w])
    # Facet group C: KAMA level (5)
    for w in windows:
        feats.append(kama[w])
    # Facet group D: price - KAMA (5)
    for w in windows:
        feats.append(price[w] - kama[w])
    # Facet group E: price / KAMA - 1 (5)
    for w in windows:
        feats.append((price[w] / kama[w] - 1.0).replace([np.inf, -np.inf], np.nan))
    # Facet group F: KAMA slope over w//4 bars (5)
    for w in windows:
        feats.append(_slope(kama[w], max(2, w // 4)))
    # Facet group G: ER z-score over 63-bar lookback (5)
    for w in windows:
        feats.append(_z(er[w], 63))
    # Facet group H: ER slope/delta over w//4 bars (5)
    for w in windows:
        feats.append(_slope(er[w], max(2, w // 4)))
    # Facet group I: ER regime distance (ER - 0.5 trend/chop threshold) (5)
    for w in windows:
        feats.append(er[w] - 0.5)
    # Facet group J: ER on closeadj vs ER on (high+low)/2 (difference) (5)
    for w in windows:
        feats.append(er[w] - er_hl2[w])
    # ---- 50 so far. Expand facets with extra parameterizations to 150 ----

    # Facet group K: ER z-score over 21-bar lookback (5)
    for w in windows:
        feats.append(_z(er[w], 21))
    # Facet group L: ER z-score over 126-bar lookback (5)
    for w in windows:
        feats.append(_z(er[w], 126))
    # Facet group M: KAMA slope over w//2 bars (5)
    for w in windows:
        feats.append(_slope(kama[w], max(2, w // 2)))
    # Facet group N: ER slope over w//2 bars (5)
    for w in windows:
        feats.append(_slope(er[w], max(2, w // 2)))
    # Facet group O: ER regime distance from chop band (|ER-0.3|) (5)
    for w in windows:
        feats.append((er[w] - 0.3).abs())
    # Facet group P: ER regime distance from trend band (ER - 0.7) (5)
    for w in windows:
        feats.append(er[w] - 0.7)
    # Facet group Q: (price-KAMA)/KAMA*100 normalized gap pct (5)
    for w in windows:
        feats.append(((price[w] - kama[w]) / kama[w] * 100.0).replace([np.inf, -np.inf], np.nan))
    # Facet group R: ER on hl2 level (5)
    for w in windows:
        feats.append(er_hl2[w])
    # Facet group S: 1 - ER on hl2 (noise on hl2) (5)
    for w in windows:
        feats.append(1.0 - er_hl2[w])
    # Facet group T: ER smoothed (rolling mean w//2) (5)
    for w in windows:
        feats.append(er[w].rolling(max(2, w // 2)).mean())
    # ---- 100 so far ----

    # Facet group U: ER delta (1-bar change) (5)
    for w in windows:
        feats.append(er[w].diff())
    # Facet group V: KAMA z-score over 63 (5)
    for w in windows:
        feats.append(_z(kama[w], 63))
    # Facet group W: price/KAMA-1 z-score over 63 (5)
    for w in windows:
        feats.append(_z((price[w] / kama[w] - 1.0).replace([np.inf, -np.inf], np.nan), 63))
    # Facet group X: ER short-vs-long ratio (ER(w)/ER(long)); for the longest
    # window compare against its own 63-bar rolling mean so it is not constant 1.
    for w in windows:
        ref = er[w].rolling(63).mean() if w == 252 else er[252]
        feats.append((er[w] / ref).replace([np.inf, -np.inf], np.nan))
    # Facet group Y: KAMA slope normalized by price (slope/price) (5)
    for w in windows:
        feats.append((_slope(kama[w], max(2, w // 4)) / price[w]).replace([np.inf, -np.inf], np.nan))
    # Facet group Z: ER dispersion (rolling std of ER over w) (5)
    for w in windows:
        feats.append(er[w].rolling(w).std())
    # Facet group AA: ER acceleration (2nd diff over w//4) (5)
    for w in windows:
        feats.append(_slope(er[w], max(2, w // 4)).diff())
    # Facet group AB: price - KAMA sign-scaled by ER (interaction) (5)
    for w in windows:
        feats.append(((price[w] - kama[w]) * er[w]).replace([np.inf, -np.inf], np.nan))
    # Facet group AC: 1-ER z-score over 63 (noise z) (5)
    for w in windows:
        feats.append(_z(1.0 - er[w], 63))
    # Facet group AD: ER regime distance abs from 0.5 (trend/chop magnitude) (5)
    for w in windows:
        feats.append((er[w] - 0.5).abs())
    # ---- 150 total ----

    lo, hi = idx_range  # 1-based inclusive
    out = {}
    for i in range(lo, hi + 1):
        out[f'f08_kaufman_efficiency_{i:03d}'] = feats[i - 1]
    return pd.DataFrame(out)


def get_f08_kaufman_efficiency_base_001_075(df):
    return _build(df, (1, 75))
