# Real indicator: Klinger Volume Oscillator (KVO) - facets 076..150
# See base_001_075 for the KVO core derivation.
import numpy as np
import pandas as pd


def _ema(s, span):
    return s.ewm(span=span, adjust=False).mean()


def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s - s.shift(w)) / s.shift(w).replace(0.0, np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(lambda x: (x[-1] > x).mean(), raw=True)


def _vf(df):
    high = df['high']
    low = df['low']
    close = df['close']
    vol = df['volume']
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).replace(0.0, np.nan).ffill().fillna(0.0)
    dm = high - low
    trend_arr = trend.to_numpy()
    dm_arr = dm.to_numpy()
    cm_arr = np.full(len(dm_arr), np.nan)
    prev_cm = 0.0
    prev_trend = np.nan
    for k in range(len(dm_arr)):
        d = dm_arr[k]
        t = trend_arr[k]
        if np.isnan(d):
            cm_arr[k] = prev_cm
            continue
        if k == 0 or np.isnan(prev_trend) or t == prev_trend:
            prev_cm = prev_cm + d
        else:
            prev_cm = dm_arr[k] + (cm_arr[k - 1] if not np.isnan(cm_arr[k - 1]) else d)
        cm_arr[k] = prev_cm
        prev_trend = t
    cm = pd.Series(cm_arr, index=df.index)
    ratio = (dm / cm.replace(0.0, np.nan)) - 1.0
    vf = vol * (2.0 * ratio).abs() * trend * 100.0
    return vf.replace([np.inf, -np.inf], np.nan)


def _kvo(vf, fast, slow):
    return _ema(vf, fast) - _ema(vf, slow)


_PAIRS = [
    (5, 8), (8, 13), (13, 21), (21, 34), (34, 55), (55, 89),
    (10, 20), (12, 26), (20, 40), (30, 60), (40, 80), (50, 100),
]


def get_f23_klinger_oscillator_base_076_150(df):
    features = {}
    vf = _vf(df)
    close = df['close']
    closeadj = df['closeadj']

    kvo = {p: _kvo(vf, p[0], p[1]) for p in _PAIRS}
    sig = {p: _ema(kvo[p], 13) for p in _PAIRS}

    i = 76

    def add(s):
        nonlocal i
        features[f'f23_klinger_oscillator_{i:03d}'] = s
        i += 1

    # --- Facet 9: short-vs-long KVO spread (fast pair minus slow pair) (12) ---
    spread_combos = [
        (_PAIRS[0], _PAIRS[4]), (_PAIRS[1], _PAIRS[4]), (_PAIRS[2], _PAIRS[5]),
        (_PAIRS[0], _PAIRS[5]), (_PAIRS[1], _PAIRS[5]), (_PAIRS[3], _PAIRS[5]),
        (_PAIRS[6], _PAIRS[11]), (_PAIRS[7], _PAIRS[11]), (_PAIRS[8], _PAIRS[11]),
        (_PAIRS[6], _PAIRS[10]), (_PAIRS[7], _PAIRS[10]), (_PAIRS[8], _PAIRS[9]),
    ]
    for a, b in spread_combos:
        add(kvo[a] - kvo[b])

    # --- Facet 10: VF cumulative (rolling sum of volume force) (12) ---
    cwins = [5, 10, 21, 42, 63, 126, 8, 13, 34, 55, 89, 252]
    for w in cwins:
        add(vf.rolling(w).sum())

    # --- Facet 11: KVO percentile rank (12) ---
    pwins = [21, 63, 126, 21, 63, 126, 21, 63, 126, 63, 126, 252]
    for p, w in zip(_PAIRS, pwins):
        add(_pctrank(kvo[p], w))

    # --- Facet 12: histogram z-score (12) ---
    hzwins = [21, 21, 42, 42, 63, 63, 21, 42, 63, 63, 126, 126]
    for p, w in zip(_PAIRS, hzwins):
        add(_z(kvo[p] - sig[p], w))

    # --- Facet 13: signal-line level (smoothed KVO) (12) ---
    for p in _PAIRS:
        add(sig[p])

    # --- Facet 14: KVO-vs-price divergence on closeadj, >21d windows (10) ---
    div_pairs = _PAIRS[:10]
    for p, w in zip(div_pairs, [42, 42, 63, 63, 126, 126, 63, 126, 42, 63]):
        add(_roc(kvo[p], w) - _roc(closeadj, w))

    # --- Facet 15: KVO histogram slope / momentum of histogram (4) ---
    for p, w in zip(_PAIRS[8:12], [3, 5, 5, 10]):
        add((kvo[p] - sig[p]).diff(w))

    # --- Facet 16: overbought/oversold distance vs price-confirmed band (1) ---
    # KVO normalized by rolling std and sign-aligned with short-term return
    p = _PAIRS[4]
    band = kvo[p].rolling(63).std()
    add(((kvo[p] / band) * np.sign(close.pct_change(5))).replace([np.inf, -np.inf], np.nan))

    return pd.DataFrame(features)
