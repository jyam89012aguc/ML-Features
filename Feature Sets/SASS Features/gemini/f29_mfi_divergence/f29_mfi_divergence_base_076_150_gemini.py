# f29_mfi_divergence base features 076-150
# Real indicator: Money Flow Index (MFI) and price-MFI divergence (volume-weighted RSI).
#   TP=(high+low+close)/3 ; raw money flow=TP*volume ; pos/neg split by TP rising/falling
#   money ratio=sum(pos,n)/sum(neg,n) ; MFI=100-100/(1+money ratio)
# This file covers the remaining facets: MFI-vs-RSI spread, MFI sign streak, money-flow
#   percentile/regime, MFI x dollar-volume, short-vs-long spreads, divergence variants.
# Window rule: rolling window > 21d uses 'closeadj' for price; volume stays raw.
import numpy as np
import pandas as pd


def _safe_div(a, b):
    return (a / b).replace([np.inf, -np.inf], np.nan)


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return _safe_div(s - m, sd)


def _roc(s, w):
    return _safe_div(s - s.shift(w), s.shift(w).abs())


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] > x[:-1]).sum() / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )


def _typical_price(df, price_col):
    return (df['high'] + df['low'] + df[price_col]) / 3.0


def _mfi(df, n, price_col):
    tp = _typical_price(df, price_col)
    rmf = tp * df['volume']
    up = tp > tp.shift(1)
    dn = tp < tp.shift(1)
    pos = rmf.where(up, 0.0)
    neg = rmf.where(dn, 0.0)
    pos_sum = pos.rolling(n).sum()
    neg_sum = neg.rolling(n).sum()
    mr = _safe_div(pos_sum, neg_sum)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return mfi, mr, pos_sum, neg_sum


def _rsi(s, n):
    d = s.diff()
    gain = d.clip(lower=0.0)
    loss = (-d).clip(lower=0.0)
    ag = gain.rolling(n).mean()
    al = loss.rolling(n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)


def _streak(sign_series):
    s = sign_series.fillna(0.0)
    out = np.zeros(len(s))
    prev = 0.0
    run = 0
    vals = s.values
    for i in range(len(vals)):
        v = vals[i]
        if v == 0:
            run = 0
        elif v == prev:
            run += 1
        else:
            run = 1
        out[i] = run * (1 if v > 0 else (-1 if v < 0 else 0))
        prev = v
    res = pd.Series(out, index=sign_series.index)
    return res.where(sign_series.notna(), np.nan)


def get_f29_mfi_divergence_base_076_150(df):
    features = {}

    def pc(n):
        return 'close' if n <= 21 else 'closeadj'

    windows = [14, 21, 63, 126]
    mfi = {}
    mr = {}
    possum = {}
    negsum = {}
    for n in windows:
        mfi[n], mr[n], possum[n], negsum[n] = _mfi(df, n, pc(n))

    # RSI on the matching close column for the spread facet
    rsi = {}
    for n in windows:
        rsi[n] = _rsi(df[pc(n)], n)

    dollar = df['closeadj'] * df['volume']

    feats = []

    # ---- Facet A: MFI-vs-RSI spread (MFI minus price RSI) ----
    for n in windows:
        feats.append(mfi[n] - rsi[n])                 # 4
    for n in windows:
        feats.append(_z(mfi[n] - rsi[n], 63))         # 4 z-scored spread

    # ---- Facet B: MFI sign streak (consecutive bars MFI>50) ----
    for n in windows:
        sgn = np.sign(mfi[n] - 50.0)
        feats.append(_streak(sgn))                    # 4
    for n in windows:
        sgn = np.sign(mfi[n] - mfi[n].shift(1))       # rising/falling streak
        feats.append(_streak(sgn))                    # 4

    # ---- Facet C: positive/negative money-flow share ----
    for n in windows:
        feats.append(_safe_div(possum[n], possum[n] + negsum[n]))   # 4 buy pressure share
    for n in windows:
        feats.append(_safe_div(possum[n] - negsum[n],
                               possum[n] + negsum[n]))              # 4 net flow oscillator

    # ---- Facet D: MFI overbought / oversold regime flags & distances ----
    for n in windows:
        feats.append((mfi[n] > 80.0).astype(float))   # 4 OB flag
    for n in windows:
        feats.append((mfi[n] < 20.0).astype(float))   # 4 OS flag
    for n in windows:
        # signed extremity distance beyond the bands
        ob = (mfi[n] - 80.0).clip(lower=0.0)
        os = (20.0 - mfi[n]).clip(lower=0.0)
        feats.append(ob - os)                         # 4 extremity

    # ---- Facet E: MFI smoothed level & deviation from its own EMA ----
    for n in windows:
        ema = mfi[n].ewm(span=10, adjust=False).mean()
        feats.append(mfi[n] - ema)                    # 4
    for n in windows:
        ema = mfi[n].ewm(span=21, adjust=False).mean()
        feats.append(ema)                             # 4 smoothed level

    # running total: 4*12 = 48
    # ---- Facet F: MFI x dollar-volume interactions ----
    dv_z21 = _z(dollar, 21)
    dv_z63 = _z(dollar, 63)
    for n in windows:
        feats.append((mfi[n] - 50.0) * dv_z21)        # 4
    for n in windows:
        feats.append((mfi[n] - 50.0) * dv_z63)        # 4 -> 56

    # ---- Facet G: MFI percentile rank (long lookback) ----
    for n in windows:
        feats.append(_pctrank(mfi[n], 126))           # 4 -> 60

    # ---- Facet H: short-vs-long MFI ratio & spreads ----
    feats.append(_safe_div(mfi[14], mfi[63]))
    feats.append(_safe_div(mfi[14], mfi[126]))
    feats.append(_safe_div(mfi[21], mfi[126]))
    feats.append(_safe_div(mfi[63], mfi[126]))        # 4 -> 64

    # ---- Facet I: divergence variants (price extreme vs MFI level) ----
    for n in windows:
        # price made a new 'n'-bar high but MFI below 50 -> bearish divergence score
        price = df[pc(n)]
        new_high = (price >= price.rolling(n).max()).astype(float)
        feats.append(new_high * (50.0 - mfi[n]) / 50.0)   # 4 -> 68
    for n in windows:
        price = df[pc(n)]
        new_low = (price <= price.rolling(n).min()).astype(float)
        feats.append(new_low * (mfi[n] - 50.0) / 50.0)    # 4 -> 72

    # ---- Facet J: MFI acceleration, longer ROC & money-ratio facets ----
    feats.append(_slope(mfi[14], 21) - _slope(mfi[14], 5))   # acceleration 14
    feats.append(_slope(mfi[63], 21) - _slope(mfi[63], 5))   # acceleration 63
    feats.append(_roc(mfi[63], 21))                          # roc 63
    feats.append(_roc(mfi[126], 21))                         # roc 126
    feats.append(_z(mr[14].clip(upper=1e6), 63))             # money-ratio z 14
    feats.append(_z(mr[63].clip(upper=1e6), 126))            # money-ratio z 63
    feats.append(_pctrank(mr[21].clip(upper=1e6), 63))       # money-ratio pctrank -> 75

    # Assemble exactly 75
    for k in range(76, 151):
        features[f'f29_mfi_divergence_{k:03d}'] = feats[k - 76]

    return pd.DataFrame(features)
