# Real indicator: Choppiness Index (CHOP) -- features 076..150
# CHOP(n) = 100 * log10( sum(TR, n) / (max(high,n) - min(low,n)) ) / log10(n)
# High (~100) = choppy/sideways, low (~0) = trending.
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)

def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return _clean((s - m) / sd)

def _true_range(high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr

def _tr_hl(high, low):
    return (high - low)

def _tr_close(close):
    return close.diff().abs()

def _chop(tr, high, low, n):
    atr_sum = tr.rolling(n).sum()
    rng = high.rolling(n).max() - low.rolling(n).min()
    ratio = _clean(atr_sum / rng)
    chop = 100.0 * np.log10(ratio) / np.log10(n)
    return _clean(chop)

def _roc(s, w):
    return _clean(s / s.shift(w) - 1.0)

# ---------------------------------------------------------------------------
# Feature builder
# ---------------------------------------------------------------------------
def get_f09_choppiness_index_base_076_150(df):
    features = {}

    high = df['high']
    low = df['low']
    close = df['close']
    closeadj = df['closeadj']

    tr_std = _true_range(high, low, close)
    tr_hl = _tr_hl(high, low)
    tr_cl = _tr_close(close)

    windows = [14, 21, 63, 126, 252]

    chop = {w: _chop(tr_std, high, low, w) for w in windows}
    chop_hl = {w: _chop(tr_hl, high, low, w) for w in windows}
    chop_cl = {w: _chop(tr_cl, high, low, w) for w in windows}
    rng = {w: _clean(high.rolling(w).max() - low.rolling(w).min()) for w in windows}
    ratio_raw = {w: _clean(tr_std.rolling(w).sum() / rng[w]) for w in windows}

    f = []

    # ---- Facet 16: trend-vs-chop distance from 50 midline (5)
    for w in windows:
        f.append(_clean(chop[w] - 50.0))

    # ---- Facet 17: CHOP slope/delta over 10d (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[w].shift(10)))

    # ---- Facet 18: CHOP slope/delta over 63d (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[w].shift(63)))

    # ---- Facet 19: CHOP z-score over 252d lookback (5)
    for w in windows:
        f.append(_z(chop[w], 252))

    # ---- Facet 20: high-low-TR CHOP z-score over 63d (5)
    for w in windows:
        f.append(_z(chop_hl[w], 63))

    # ---- Facet 21: close-to-close-TR CHOP slope over 21d (5)
    for w in windows:
        f.append(_clean(chop_cl[w] - chop_cl[w].shift(21)))

    # ---- Facet 22: spread between classic-TR CHOP and high-low-TR CHOP (5)
    for w in windows:
        f.append(_clean(chop[w] - chop_hl[w]))

    # ---- Facet 23: spread between classic-TR CHOP and close-to-close-TR CHOP (5)
    for w in windows:
        f.append(_clean(chop[w] - chop_cl[w]))

    # ---- Facet 24: raw ATR-sum/range ratio z-score over 126d (5)
    for w in windows:
        f.append(_z(ratio_raw[w], 126))

    # ---- Facet 25: CHOP regime streak BELOW 50 midline (trending persistence) (5)
    for w in windows:
        trend = (chop[w] < 50.0).astype(float)
        grp = (trend != trend.shift(1)).cumsum()
        streak = trend.groupby(grp).cumsum()
        f.append(_clean(streak))

    # ---- Facet 26: short-vs-long CHOP spread (w vs 14d short anchor) (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[14].rolling(w).mean()))

    # ---- Facet 27: CHOP ratio to its own 63d mean (5)
    for w in windows:
        f.append(_clean(chop[w] / chop[w].rolling(63).mean()))

    # ---- Facet 28: CHOP percentile rank over 252d (5)
    for w in windows:
        f.append(chop[w].rolling(252).rank(pct=True))

    # ---- Facet 29: absolute distance to nearest Fib threshold (61.8 / 38.2) (5)
    for w in windows:
        d = pd.concat([(chop[w] - 61.8).abs(), (chop[w] - 38.2).abs()], axis=1).min(axis=1)
        f.append(_clean(d))

    # ---- Facet 30: CHOP acceleration (2nd difference of 5d slope) (5)
    for w in windows:
        slope = chop[w] - chop[w].shift(5)
        f.append(_clean(slope - slope.shift(5)))

    # Assemble: 15 facets * 5 windows = 75 features -> 076..150
    assert len(f) == 75, f"expected 75, got {len(f)}"
    for k, s in enumerate(f, start=76):
        features[f'f09_choppiness_index_{k:03d}'] = s

    return pd.DataFrame(features)
