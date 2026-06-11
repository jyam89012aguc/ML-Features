# Real indicator: Fisher Transform  (features 076..150)
# Over window n: x = 2*((price - min_n)/(max_n - min_n) - 0.5) clipped to (-0.999, 0.999)
# Fisher = 0.5*ln((1+x)/(1-x)), typically EMA-smoothed; signal = Fisher.shift(1).
# 150 DISTINCT variants across windows (5/10/21/63/126) and facets.
# Windows > 21d use 'closeadj'; (high+low)/2 allowed for the price-position input.
import numpy as np
import pandas as pd

EPS = 1e-12


def _price(df, window, kind='closeadj'):
    if window > 21:
        return df['closeadj']
    if kind == 'close':
        return df['close']
    return df['closeadj']


def _hl2(df):
    return (df['high'] + df['low']) / 2.0


def _fisher_raw(price, window):
    lo = price.rolling(window).min()
    hi = price.rolling(window).max()
    rng = (hi - lo).replace(0.0, np.nan)
    x = 2.0 * ((price - lo) / rng - 0.5)
    x = x.clip(-0.999, 0.999)
    fish = 0.5 * np.log((1.0 + x) / (1.0 - x))
    return fish.replace([np.inf, -np.inf], np.nan)


def _fisher(price, window, span=1):
    fish = _fisher_raw(price, window)
    if span and span > 1:
        fish = fish.ewm(span=span, adjust=False).mean()
    return fish


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std().replace(0.0, np.nan)
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return (s - s.shift(w))


def _streak(cond):
    c = cond.astype('float')
    grp = (c == 0).cumsum()
    return c.groupby(grp).cumsum()


def _sign_cross_streak(s):
    sgn = np.sign(s)
    changed = (sgn != sgn.shift(1)) & sgn.notna() & sgn.shift(1).notna()
    grp = changed.cumsum()
    streak = pd.Series(1.0, index=s.index).groupby(grp).cumsum()
    return streak.where(s.notna())


WINDOWS = [5, 10, 21, 63, 126]


def _build(df, start, end):
    feats = {}
    for w in WINDOWS:
        f = _fisher(_price(df, w), w)
        fe = _fisher(_price(df, w), w, span=5)
        fe9 = _fisher(_price(df, w), w, span=9)
        fhl = _fisher(_hl2(df), w)
        sig = f.shift(1)
        sige = fe.shift(1)

        facet = []
        facet.append(f)
        facet.append(f - sige)
        facet.append(f.diff())
        facet.append(_slope(f, w))
        facet.append(_z(f, w))
        facet.append(_z(f, 252))
        facet.append(f - fhl)
        facet.append(fe)
        facet.append(fe9)
        facet.append(fe - sige)
        facet.append((f - 1.5).clip(lower=0.0))
        facet.append((-1.5 - f).clip(lower=0.0))
        facet.append((f.abs() - 1.0))
        facet.append(_sign_cross_streak(f))
        facet.append(_streak(f > 0))
        facet.append(_streak(f < 0))
        facet.append(_streak(f > sig))
        facet.append(fhl)
        facet.append(fhl.diff())
        facet.append(_z(fhl, w))
        facet.append(f.diff().diff())
        facet.append(f - fe)
        facet.append(f.rolling(w).mean())
        facet.append(f.rolling(w).std())
        facet.append(f.rolling(w).rank(pct=True))
        facet.append(f.rolling(w).max() - f.rolling(w).min())
        f5 = _fisher(_price(df, 5), 5)
        facet.append(f5 - f)
        facet.append((fe - sige).diff())
        facet.append(f * np.sign(f.diff()))
        facet.append(fe / f.rolling(w).std().replace(0.0, np.nan))

        for ff in facet:
            feats[len(feats)] = ff.replace([np.inf, -np.inf], np.nan)

    out = {}
    for i in range(start, end + 1):
        out[f'f05_fisher_transform_{i:03d}'] = feats[i - 1]
    return pd.DataFrame(out)


def get_f05_fisher_transform_base_076_150(df):
    return _build(df, 76, 150)
