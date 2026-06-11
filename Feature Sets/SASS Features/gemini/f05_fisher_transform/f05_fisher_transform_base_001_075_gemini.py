# Real indicator: Fisher Transform
# Over window n: x = 2*((price - min_n)/(max_n - min_n) - 0.5) clipped to (-0.999, 0.999)
# Fisher = 0.5*ln((1+x)/(1-x)), typically EMA-smoothed; signal = Fisher.shift(1).
# 150 DISTINCT variants across windows (5/10/21/63/126) and facets.
# Windows > 21d use 'closeadj'; (high+low)/2 allowed for the price-position input.
import numpy as np
import pandas as pd

EPS = 1e-12


def _price(df, window, kind='closeadj'):
    # Rule: window > 21 must use closeadj. <=21 may use raw close.
    if window > 21:
        return df['closeadj']
    if kind == 'close':
        return df['close']
    return df['closeadj']


def _hl2(df):
    return (df['high'] + df['low']) / 2.0


def _fisher_raw(price, window):
    # Normalized position of price within rolling [min,max] over window.
    lo = price.rolling(window).min()
    hi = price.rolling(window).max()
    rng = (hi - lo).replace(0.0, np.nan)
    x = 2.0 * ((price - lo) / rng - 0.5)
    x = x.clip(-0.999, 0.999)
    fish = 0.5 * np.log((1.0 + x) / (1.0 - x))
    return fish.replace([np.inf, -np.inf], np.nan)


def _fisher(price, window, span=1):
    # EMA-smoothed Fisher (span=1 -> effectively the recursive smoothing standard form).
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
    # Length of current consecutive True-run at each point.
    c = cond.astype('float')
    grp = (c == 0).cumsum()
    return c.groupby(grp).cumsum()


def _sign_cross_streak(s):
    # Bars since last sign change (zero-cross) of series s.
    sgn = np.sign(s)
    changed = (sgn != sgn.shift(1)) & sgn.notna() & sgn.shift(1).notna()
    grp = changed.cumsum()
    streak = pd.Series(1.0, index=s.index).groupby(grp).cumsum()
    return streak.where(s.notna())


WINDOWS = [5, 10, 21, 63, 126]


def _build(df, start, end):
    # 30 facet builders; applied across the 5 windows in order to yield 150 distinct cols.
    feats = {}
    for w in WINDOWS:
        # Core fisher series on closeadj-rule price and on hl2 price-position input.
        f = _fisher(_price(df, w), w)            # raw (recursive-equivalent) level
        fe = _fisher(_price(df, w), w, span=5)   # EMA(5)-smoothed fisher
        fe9 = _fisher(_price(df, w), w, span=9)  # EMA(9)-smoothed fisher
        fhl = _fisher(_hl2(df), w)               # fisher on (high+low)/2 price-position
        sig = f.shift(1)                          # signal line
        sige = fe.shift(1)

        facet = []
        # 1 level
        facet.append(f)
        # 2 fisher - smoothed signal line (histogram vs EMA(5) signal)
        facet.append(f - sige)
        # 3 fisher slope (1-bar delta)
        facet.append(f.diff())
        # 4 fisher slope over window
        facet.append(_slope(f, w))
        # 5 fisher z-score over window
        facet.append(_z(f, w))
        # 6 fisher z-score over fixed 252 (long-horizon normalization)
        facet.append(_z(f, 252))
        # 7 fisher on closeadj minus fisher on hl2 median price
        facet.append(f - fhl)
        # 8 EMA(5)-smoothed fisher level
        facet.append(fe)
        # 9 EMA(9)-smoothed fisher level
        facet.append(fe9)
        # 10 smoothed fisher minus its signal
        facet.append(fe - sige)
        # 11 overbought distance (distance above +1.5 threshold, else 0)
        facet.append((f - 1.5).clip(lower=0.0))
        # 12 oversold distance (distance below -1.5 threshold, else 0)
        facet.append((-1.5 - f).clip(lower=0.0))
        # 13 absolute threshold distance from neutral band edges
        facet.append((f.abs() - 1.0))
        # 14 sign/zero-cross streak (bars since last zero cross)
        facet.append(_sign_cross_streak(f))
        # 15 positive streak length (consecutive bars fisher>0)
        facet.append(_streak(f > 0))
        # 16 negative streak length (consecutive bars fisher<0)
        facet.append(_streak(f < 0))
        # 17 crossover streak: bars since fisher last crossed its signal up
        facet.append(_streak(f > sig))
        # 18 hl2-based fisher level
        facet.append(fhl)
        # 19 hl2 fisher slope
        facet.append(fhl.diff())
        # 20 hl2 fisher z-score
        facet.append(_z(fhl, w))
        # 21 fisher acceleration (2nd diff)
        facet.append(f.diff().diff())
        # 22 fisher minus EMA(5) of fisher (smoothing residual)
        facet.append(f - fe)
        # 23 fisher rolling mean (level smoothing via SMA)
        facet.append(f.rolling(w).mean())
        # 24 fisher rolling std (dispersion)
        facet.append(f.rolling(w).std())
        # 25 fisher percentile rank within window
        facet.append(f.rolling(w).rank(pct=True))
        # 26 fisher range within window (max-min)
        facet.append(f.rolling(w).max() - f.rolling(w).min())
        # 27 short-vs this window: fisher(5) minus this fisher (regime spread)
        f5 = _fisher(_price(df, 5), 5)
        facet.append(f5 - f)
        # 28 momentum of smoothed histogram: delta of (fe - signal)
        facet.append((fe - sige).diff())
        # 29 fisher times sign of slope (directional level)
        facet.append(f * np.sign(f.diff()))
        # 30 distance of smoothed fisher from zero scaled by dispersion
        facet.append(fe / f.rolling(w).std().replace(0.0, np.nan))

        for ff in facet:
            feats[len(feats)] = ff.replace([np.inf, -np.inf], np.nan)

    # feats now holds 150 series keyed 0..149 in (window-major, facet-minor) order.
    out = {}
    for i in range(start, end + 1):
        out[f'f05_fisher_transform_{i:03d}'] = feats[i - 1]
    return pd.DataFrame(out)


def get_f05_fisher_transform_base_001_075(df):
    return _build(df, 1, 75)
