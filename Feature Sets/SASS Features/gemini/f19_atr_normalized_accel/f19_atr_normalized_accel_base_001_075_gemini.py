# f19_atr_normalized_accel — REAL indicator: ATR-normalized price acceleration
# ATR(n) = rolling mean of True Range (TR from raw high/low/close).
# Acceleration = 2nd difference of price; velocity = ROC/1st diff; jerk = 3rd diff.
# Everything measured in ATR units (price moves normalized by ATR).
# Windows > 21d use 'closeadj' for the price series; TR/ATR always from raw OHLC.
import numpy as np
import pandas as pd

WINDOWS = [5, 10, 21, 63, 126]


def _price(df, window):
    # >21d windows use closeadj; <=21d may use raw close
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


def _roc(s, n):
    return s.pct_change(n).replace([np.inf, -np.inf], np.nan)


def get_f19_atr_normalized_accel_base_001_075(df):
    features = {}
    out = []

    atr_cache = {n: _atr(df, n) for n in WINDOWS}

    # ---- Facet A: price velocity (1st diff) in ATR units ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = p.diff(1)
        out.append(_safe_div(vel, atr))  # 1-bar velocity / ATR(n)

    # ---- Facet B: price velocity as ROC(n) in ATR units (scaled by price) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        roc_move = p - p.shift(n)
        out.append(_safe_div(roc_move, atr))  # n-bar move / ATR(n)

    # ---- Facet C: price acceleration (2nd diff) in ATR units ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel = p.diff(1).diff(1)
        out.append(_safe_div(accel, atr))  # 2nd diff / ATR(n)

    # ---- Facet D: smoothed acceleration over window / ATR ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel = p.diff(1).diff(1).rolling(n).mean()
        out.append(_safe_div(accel, atr))  # mean(2nd diff,n) / ATR(n)

    # ---- Facet E: momentum-change / ATR (Δ of n-bar momentum) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        mom = p - p.shift(n)
        mom_change = mom.diff(1)
        out.append(_safe_div(mom_change, atr))  # change in momentum / ATR(n)

    # ---- Facet F: ATR-normalized distance from moving average ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        ma = p.rolling(n).mean()
        out.append(_safe_div(p - ma, atr))  # (price - MA(n)) / ATR(n)

    # ---- Facet G: ATR z-score (ATR vs its own history) ----
    for n in WINDOWS:
        atr = atr_cache[n]
        out.append(_z(atr, n))  # z-score of ATR(n)

    # ---- Facet H: acceleration sign streak ----
    for n in WINDOWS:
        p = _price(df, n)
        accel = p.diff(1).diff(1)
        sign = np.sign(accel)
        # streak length of consistent acceleration sign
        grp = (sign != sign.shift(1)).cumsum()
        streak = sign.groupby(grp).cumcount() + 1
        out.append((streak * sign).reindex(p.index))  # signed accel streak

    # ---- Facet I: jerk (3rd diff) / ATR ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        jerk = p.diff(1).diff(1).diff(1)
        out.append(_safe_div(jerk, atr))  # 3rd diff / ATR(n)

    # ---- Facet J: ATR slope (trend in volatility) normalized by ATR ----
    for n in WINDOWS:
        atr = atr_cache[n]
        slope = atr.diff(n)
        out.append(_safe_div(slope, atr))  # ATR slope / ATR(n)

    # ---- Facet K: velocity-vs-acceleration interaction (both in ATR units) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = _safe_div(p.diff(1), atr)
        accel = _safe_div(p.diff(1).diff(1), atr)
        out.append(vel * accel)  # velocity * acceleration

    # ---- Facet L: ATR-normalized overnight gap ----
    for n in WINDOWS:
        atr = atr_cache[n]
        gap = df['open'] - df['close'].shift(1)
        out.append(_safe_div(gap, atr))  # gap / ATR(n)

    # ---- Facet M: short-vs-long acceleration spread ----
    # acceleration in ATR units measured over n vs over a longer horizon
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel_short = _safe_div(p.diff(1).diff(1), atr)
        long_n = min(n * 3, 126)
        p_long = _price(df, long_n)
        accel_long = _safe_div(p_long.diff(1).diff(1).rolling(n).mean(), atr)
        out.append(accel_short - accel_long)  # short - long accel spread

    # ---- Facet N: acceleration z-score (regime) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        accel = _safe_div(p.diff(1).diff(1), atr)
        out.append(_z(accel, n))  # z-score of ATR-normalized acceleration

    # ---- Facet O: velocity z-score (regime) ----
    for n in WINDOWS:
        p = _price(df, n)
        atr = atr_cache[n]
        vel = _safe_div(p.diff(1), atr)
        out.append(_z(vel, n))  # z-score of ATR-normalized velocity

    # assemble exactly 75 columns 001..075
    for i in range(1, 76):
        features[f'f19_atr_normalized_accel_{i:03d}'] = out[i - 1]
    return pd.DataFrame(features)
