# Real indicator: Choppiness Index (CHOP)
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
    """Classic true range using prior close."""
    pc = close.shift(1)
    tr = pd.concat([(high - low),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr

def _tr_hl(high, low):
    """High-Low only true range (no gaps)."""
    return (high - low)

def _tr_close(close):
    """Close-to-close absolute range (gap-only TR variant)."""
    return close.diff().abs()

def _chop(tr, high, low, n):
    """Core Choppiness Index over window n given a TR series."""
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
def get_f09_choppiness_index_base_001_075(df):
    features = {}

    high = df['high']
    low = df['low']
    close = df['close']
    closeadj = df['closeadj']

    # TR definitions
    tr_std = _true_range(high, low, close)          # classic TR (raw OHLC)
    tr_hl = _tr_hl(high, low)                        # high-low TR
    tr_cl = _tr_close(close)                         # close-to-close TR

    windows = [14, 21, 63, 126, 252]
    # For windows > 21 the range extremes use closeadj-consistent series.
    # high/low rolling extremes are acceptable for the range term per spec;
    # we keep high/low for the range max/min in all cases.

    # Pre-compute the primary CHOP (classic TR) for every window.
    chop = {w: _chop(tr_std, high, low, w) for w in windows}
    # CHOP using high-low TR
    chop_hl = {w: _chop(tr_hl, high, low, w) for w in windows}
    # CHOP using close-to-close TR
    chop_cl = {w: _chop(tr_cl, high, low, w) for w in windows}
    # Raw ATR-sum / range ratio (no log normalization)
    rng = {w: _clean(high.rolling(w).max() - low.rolling(w).min()) for w in windows}
    ratio_raw = {w: _clean(tr_std.rolling(w).sum() / rng[w]) for w in windows}

    f = []  # list of (name_suffix-less) series in deterministic order

    # ---- Facet 1: CHOP level (classic TR) for each window (5)
    for w in windows:
        f.append(chop[w])

    # ---- Facet 2: CHOP z-score over a 63d lookback, each window (5)
    for w in windows:
        f.append(_z(chop[w], 63))

    # ---- Facet 3: CHOP z-score over a 126d lookback, each window (5)
    for w in windows:
        f.append(_z(chop[w], 126))

    # ---- Facet 4: CHOP slope / delta over 5d, each window (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[w].shift(5)))

    # ---- Facet 5: CHOP slope / delta over 21d, each window (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[w].shift(21)))

    # ---- Facet 6: trend-vs-chop threshold distance from Fib 61.8 (5)
    for w in windows:
        f.append(_clean(chop[w] - 61.8))

    # ---- Facet 7: trend-vs-chop threshold distance from Fib 38.2 (5)
    for w in windows:
        f.append(_clean(chop[w] - 38.2))

    # ---- Facet 8: CHOP using high-low TR, level (5)
    for w in windows:
        f.append(chop_hl[w])

    # ---- Facet 9: CHOP using close-to-close TR, level (5)
    for w in windows:
        f.append(chop_cl[w])

    # ---- Facet 10: raw ATR-sum/range ratio (5)
    for w in windows:
        f.append(ratio_raw[w])

    # ---- Facet 11: CHOP regime streak above 61.8 (choppy persistence) (5)
    for w in windows:
        choppy = (chop[w] > 50.0).astype(float)
        # consecutive-count via grouping of run boundaries
        grp = (choppy != choppy.shift(1)).cumsum()
        streak = choppy.groupby(grp).cumsum()
        f.append(_clean(streak))

    # ---- Facet 12: short-vs-long CHOP spread (CHOP vs its 126d mean) (5)
    for w in windows:
        f.append(_clean(chop[w] - chop[w].rolling(126).mean()))

    # ---- Facet 13: CHOP rate-of-change over 10d (5)
    for w in windows:
        f.append(_roc(chop[w], 10))

    # ---- Facet 14: CHOP percentile rank over 126d (5)
    for w in windows:
        f.append(chop[w].rolling(126).rank(pct=True))

    # ---- Facet 15: CHOP dispersion (rolling std of CHOP, 21d) (5)
    for w in windows:
        f.append(_clean(chop[w].rolling(21).std()))

    # Assemble: 15 facets * 5 windows = 75 features -> 001..075
    assert len(f) == 75, f"expected 75, got {len(f)}"
    for k, s in enumerate(f, start=1):
        features[f'f09_choppiness_index_{k:03d}'] = s

    return pd.DataFrame(features)
