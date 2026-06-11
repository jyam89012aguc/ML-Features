# Real indicator: Klinger Volume Oscillator (KVO)
# Trend = sign(diff(typical price)); dm = high-low; cm = cumulative measurement
# VF = volume * |2*(dm/cm - 1)| * trend * 100
# KVO = EMA(fast, VF) - EMA(slow, VF); signal = EMA(13, KVO)
# Facets: KVO level, histogram, z-score, slope, VF level, sign-streak,
#         price divergence, OB/OS distance, short-vs-long spread, VF cumsum, percentile rank.
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
    """Volume force series (the core Klinger building block)."""
    high = df['high']
    low = df['low']
    close = df['close']
    vol = df['volume']
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).replace(0.0, np.nan).ffill().fillna(0.0)
    dm = high - low
    # cumulative measurement: resets implicitly via running accumulation of dm by trend persistence
    # standard KVO uses a running cm that carries forward; approximate with expanding-trend cumsum
    cm = dm.copy()
    # build cm as cumulative dm while trend unchanged, else reset to prior cm + dm
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
            prev_cm = (prev_cm if not np.isnan(prev_cm) else 0.0) + d
            # trend flip: cm restarts from previous-bar cm + current dm
            prev_cm = dm_arr[k] + (cm_arr[k - 1] if not np.isnan(cm_arr[k - 1]) else d)
        cm_arr[k] = prev_cm
        prev_trend = t
    cm = pd.Series(cm_arr, index=df.index)
    ratio = (dm / cm.replace(0.0, np.nan)) - 1.0
    vf = vol * (2.0 * ratio).abs() * trend * 100.0
    return vf.replace([np.inf, -np.inf], np.nan)


def _kvo(vf, fast, slow):
    return _ema(vf, fast) - _ema(vf, slow)


# EMA fast/slow window pairs spanning short to long regimes (the classic 34/55 plus scaled variants)
_PAIRS = [
    (5, 8), (8, 13), (13, 21), (21, 34), (34, 55), (55, 89),
    (10, 20), (12, 26), (20, 40), (30, 60), (40, 80), (50, 100),
]


def get_f23_klinger_oscillator_base_001_075(df):
    features = {}
    vf = _vf(df)
    # price series: closeadj for >21d divergence windows, close otherwise
    close = df['close']
    closeadj = df['closeadj']

    # precompute KVO + signal for each pair
    kvo = {p: _kvo(vf, p[0], p[1]) for p in _PAIRS}
    sig = {p: _ema(kvo[p], 13) for p in _PAIRS}

    i = 1

    def add(s):
        nonlocal i
        features[f'f23_klinger_oscillator_{i:03d}'] = s
        i += 1

    # --- Facet 1: KVO level for each pair (12) ---
    for p in _PAIRS:
        add(kvo[p])

    # --- Facet 2: histogram KVO - signal for each pair (12) ---
    for p in _PAIRS:
        add(kvo[p] - sig[p])

    # --- Facet 3: KVO z-score over varied windows (12) ---
    zwins = [10, 21, 63, 10, 21, 63, 10, 21, 63, 21, 63, 126]
    for p, w in zip(_PAIRS, zwins):
        add(_z(kvo[p], w))

    # --- Facet 4: KVO slope / delta (12) ---
    dwins = [1, 1, 2, 2, 3, 5, 1, 2, 3, 5, 5, 10]
    for p, w in zip(_PAIRS, dwins):
        add(kvo[p].diff(w))

    # --- Facet 5: volume-force level smoothed (varied EMA) (12) ---
    vwins = [5, 8, 13, 21, 34, 55, 10, 12, 20, 30, 40, 50]
    for w in vwins:
        add(_ema(vf, w))

    # --- Facet 6: KVO sign / zero-cross streak (a few pairs) (3) ---
    def _streak(s):
        sgn = np.sign(s)
        grp = (sgn != sgn.shift()).cumsum()
        return sgn * sgn.groupby(grp).cumcount().add(1)
    for p in [_PAIRS[3], _PAIRS[4], _PAIRS[5]]:
        add(_streak(kvo[p]))

    # remaining slots up to 75
    # --- Facet 7: KVO-vs-price divergence (>21d -> closeadj) (6) ---
    for p, w in zip(_PAIRS[:6], [21, 21, 42, 42, 63, 63]):
        price = closeadj if w > 21 else close
        add(_roc(kvo[p], w) - _roc(price, w))

    # --- Facet 8: overbought/oversold distance (KVO vs rolling band) (6) ---
    for p, w in zip(_PAIRS[6:12], [21, 21, 42, 42, 63, 63]):
        band = kvo[p].rolling(w).std()
        add((kvo[p] / band).replace([np.inf, -np.inf], np.nan))

    return pd.DataFrame(features)
