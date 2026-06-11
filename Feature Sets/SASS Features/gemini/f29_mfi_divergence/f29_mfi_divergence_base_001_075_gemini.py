# f29_mfi_divergence base features 001-075
# Real indicator: Money Flow Index (MFI) and price-MFI divergence.
#   Typical price TP = (high+low+close)/3
#   raw money flow = TP * volume ; split positive/negative by TP rising/falling
#   money ratio = sum(pos_flow, n) / sum(neg_flow, n)
#   MFI = 100 - 100/(1 + money_ratio)   (a volume-weighted RSI)
# Facets: MFI level, OB/OS (80/20) threshold distance, MFI z-score, MFI slope/delta,
#   price-vs-MFI divergence, MFI-vs-RSI spread, MFI sign streak, money-flow-ratio raw,
#   MFI percentile rank, short-vs-long MFI spread, MFI x dollar-volume.
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
    # per-bar change over w bars
    return (s - s.shift(w)) / float(w)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] > x[:-1]).sum() / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )


def _typical_price(df, price_col):
    # TP uses high/low and the chosen close column (close or closeadj)
    return (df['high'] + df['low'] + df[price_col]) / 3.0


def _mfi(df, n, price_col):
    """Money Flow Index over n bars using given close column."""
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
    return mfi, mr


def _rsi(s, n):
    d = s.diff()
    gain = d.clip(lower=0.0)
    loss = (-d).clip(lower=0.0)
    ag = gain.rolling(n).mean()
    al = loss.rolling(n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)


def _streak(sign_series):
    # length of current run of identical sign (signed)
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


def get_f29_mfi_divergence_base_001_075(df):
    features = {}

    # price column choice depends on whether the dominant window > 21d
    def pc(n):
        return 'close' if n <= 21 else 'closeadj'

    windows = [14, 21, 63, 126]
    # precompute MFI / money-ratio per window
    mfi = {}
    mr = {}
    for n in windows:
        mfi[n], mr[n] = _mfi(df, n, pc(n))

    dollar = df['closeadj'] * df['volume']

    feats = []  # list of pandas Series in order

    # ---- Facet block 1: MFI level (4) ----
    for n in windows:
        feats.append(mfi[n])

    # ---- Facet block 2: OB/OS threshold distance (80/20) ----
    # distance below 80 (overbought proximity), distance above 20 (oversold proximity),
    # centered (MFI-50), and combined band position
    for n in windows:
        feats.append(80.0 - mfi[n])          # room to overbought
    for n in windows:
        feats.append(mfi[n] - 20.0)          # room from oversold
    for n in windows:
        feats.append(mfi[n] - 50.0)          # centered level
    for n in windows:
        feats.append((mfi[n] - 20.0) / 60.0) # normalized band position [0..1]

    # ---- Facet block 3: MFI z-score (over multiple lookbacks) ----
    for n in windows:
        feats.append(_z(mfi[n], 21))
    for n in windows:
        feats.append(_z(mfi[n], 63))
    for n in windows:
        feats.append(_z(mfi[n], 126))

    # ---- Facet block 4: MFI slope / delta ----
    for n in windows:
        feats.append(mfi[n] - mfi[n].shift(1))    # 1-bar delta
    for n in windows:
        feats.append(_slope(mfi[n], 5))           # 5-bar slope
    for n in windows:
        feats.append(_slope(mfi[n], 10))          # 10-bar slope
    for n in windows:
        feats.append(_roc(mfi[n], 5))             # 5-bar roc

    # ---- Facet block 5: price-vs-MFI divergence ----
    # price makes a new high over w while MFI does not (and vice versa)
    for n in windows:
        w = n
        price = df[pc(n)]
        price_max = price.rolling(w).max()
        mfi_max = mfi[n].rolling(w).max()
        price_new_high = (price >= price_max).astype(float)
        mfi_new_high = (mfi[n] >= mfi_max).astype(float)
        # bearish divergence: price new high, MFI not
        feats.append(price_new_high - mfi_new_high)
    for n in windows:
        w = n
        price = df[pc(n)]
        price_min = price.rolling(w).min()
        mfi_min = mfi[n].rolling(w).min()
        price_new_low = (price <= price_min).astype(float)
        mfi_new_low = (mfi[n] <= mfi_min).astype(float)
        # bullish divergence: price new low, MFI not
        feats.append(mfi_new_low - price_new_low)
    for n in windows:
        # continuous divergence: normalized price change minus normalized MFI change
        w = n
        price = df['closeadj']  # >21d price divergence uses closeadj per brief
        pchg = _roc(price, w)
        mchg = (mfi[n] - mfi[n].shift(w)) / 100.0
        feats.append(pchg - mchg)

    # truncate / we will fill to 75 with remaining facets below
    # ---- Facet block 6: MFI percentile rank ----
    for n in windows:
        feats.append(_pctrank(mfi[n], 63))     # 4

    # ---- Facet block 7: money-flow-ratio raw + short-vs-long MFI spread ----
    for n in windows:
        feats.append(mr[n].clip(upper=1e6))    # raw money ratio (4)
    # short-vs-long MFI spread (pairs)
    feats.append(mfi[14] - mfi[63])
    feats.append(mfi[14] - mfi[126])
    feats.append(mfi[21] - mfi[126])           # 3
    feats.append(mfi[21] - mfi[63])
    feats.append(mfi[63] - mfi[126])           # 2 more

    # ---- Facet block 8: MFI x dollar-volume z-score interaction ----
    dv_z = _z(dollar, 21)
    feats.append((mfi[14] - 50.0) * dv_z)
    feats.append((mfi[63] - 50.0) * dv_z)      # 2 more -> total 75

    # Assemble exactly 75
    for i in range(1, 76):
        features[f'f29_mfi_divergence_{i:03d}'] = feats[i - 1]

    return pd.DataFrame(features)
