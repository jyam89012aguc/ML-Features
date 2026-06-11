# f19_atr_normalized_accel — REAL indicator: ATR-normalized price acceleration (part 2)
# Continuation: more distinct facets of ATR-normalized velocity/acceleration/jerk.
# ATR(n) = rolling mean of True Range (raw OHLC). Price series uses closeadj when window>21.
import numpy as np
import pandas as pd

WINDOWS = [5, 10, 21, 63, 126]


def _price(df, window):
    return df['closeadj'] if window > 21 else df['close']


def _true_range(df):
    high = df['high']
    low = df['low']
    prev_close = df['close'].shift(1)
    tr = pd.concat([
        (high - low),
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return tr


def _atr(df, n):
    return _true_range(df).rolling(n).mean()


def _z(s, n):
    m = s.rolling(n).mean()
    sd = s.rolling(n).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    return (a / b).replace([np.inf, -np.inf], np.nan)


def get_f19_atr_normalized_accel_base_076_150(df):
    features = {}
    out = []

    atr_cache = {n: _atr(df, n) for n in WINDOWS}

    # ---- Facet P: cumulative acceleration over window (sum of 2nd diffs) / ATR ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel_sum = p.diff(1).diff(1).rolling(n).sum()
        out.append(_safe_div(accel_sum, atr))

    # ---- Facet Q: ATR-normalized n-bar acceleration (forward/back diff of momentum) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        # (p[t]-p[t-n]) - (p[t-n]-p[t-2n]) = p - 2*p.shift(n) + p.shift(2n)
        accel_n = p - 2 * p.shift(n) + p.shift(2 * n)
        out.append(_safe_div(accel_n, atr))

    # ---- Facet R: velocity slope (change in ATR-normalized velocity) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = _safe_div(p.diff(1), atr)
        out.append(vel.diff(n))  # how velocity itself is trending

    # ---- Facet S: ATR-normalized high-low range expansion vs ATR ----
    for n in WINDOWS:
        atr = atr_cache[n]
        rng = (df['high'] - df['low'])
        out.append(_safe_div(rng - atr, atr))  # range deviation from ATR

    # ---- Facet T: signed acceleration magnitude rank (rolling percentile) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel = _safe_div(p.diff(1).diff(1), atr)
        out.append(accel.rolling(n).rank(pct=True) - 0.5)  # centered percentile rank

    # ---- Facet U: acceleration-to-velocity ratio (curvature of trajectory) ----
    for n in WINDOWS:
        p = _price(df, n)
        accel = p.diff(1).diff(1)
        vel = p.diff(1)
        out.append(_safe_div(accel, vel.abs()))  # accel / |vel|, ATR cancels

    # ---- Facet V: jerk smoothed over window / ATR ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        jerk = p.diff(1).diff(1).diff(1).rolling(n).mean()
        out.append(_safe_div(jerk, atr))

    # ---- Facet W: ATR-normalized distance from rolling max (drawdown in ATR units) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        rmax = p.rolling(n).max()
        out.append(_safe_div(p - rmax, atr))

    # ---- Facet X: ATR-normalized distance from rolling min (run-up in ATR units) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        rmin = p.rolling(n).min()
        out.append(_safe_div(p - rmin, atr))

    # ---- Facet Y: short-vs-long velocity spread (in ATR units) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel_short = _safe_div(p.diff(1), atr)
        long_n = min(n * 3, 126)
        p_long = _price(df, long_n)
        vel_long = _safe_div(p_long.diff(1).rolling(n).mean(), atr)
        out.append(vel_short - vel_long)

    # ---- Facet Z: acceleration sign streak ratio (fraction of up-accel in window) ----
    for n in WINDOWS:
        p = _price(df, n)
        accel = p.diff(1).diff(1)
        up = (accel > 0).astype(float)
        out.append(up.rolling(n).mean() - 0.5)  # centered fraction positive accel

    # ---- Facet AA: ATR slope z-score (volatility trend regime) ----
    for n in WINDOWS:
        atr = atr_cache[n]
        slope = atr.diff(n)
        out.append(_z(slope, n))

    # ---- Facet BB: velocity*ATR-trend interaction ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = _safe_div(p.diff(1), atr)
        atr_trend = _safe_div(atr.diff(n), atr)
        out.append(vel * atr_trend)

    # ---- Facet CC: ATR-normalized gap z-score ----
    for n in WINDOWS:
        atr = atr_cache[n]
        gap = _safe_div(df['open'] - df['close'].shift(1), atr)
        out.append(_z(gap, n))

    # ---- Facet DD: cumulative ATR-normalized momentum (sum of velocity/ATR) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = _safe_div(p.diff(1), atr)
        out.append(vel.rolling(n).sum())  # path length in ATR units, signed

    # assemble exactly 75 columns 076..150
    for k, i in enumerate(range(76, 151)):
        features[f'f19_atr_normalized_accel_{i:03d}'] = out[k]
    return pd.DataFrame(features)
