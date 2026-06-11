# f21_vvwap_convexity — REAL indicator: rolling VWAP deviation & convexity
# Rolling VWAP(n) = sum(typical_price * volume) / sum(volume) over n,
# typical_price = (high + low + close) / 3.
# Facets: price-VWAP deviation, price/VWAP-1, deviation z-score, VWAP bands,
# %position in bands, VWAP convexity (2nd diff / curvature), VWAP slope,
# deviation mean-reversion, deviation*volume interaction, short-vs-long VWAP
# spread, anchored-VWAP distance.
# Rule: windows > 21d use closeadj for price comparisons; closeadj*volume for
# dollar terms; high/low/close used for typical price; raw volume otherwise.
import numpy as np
import pandas as pd

WINDOWS = [5, 10, 21, 63, 126, 252]


def _typ(df):
    return (df['high'] + df['low'] + df['close']) / 3.0


def _price(df, window):
    # price series used for comparison/anchoring; >21d uses closeadj
    return df['closeadj'] if window > 21 else df['close']


def _vwap(df, window, dollar=False):
    """Rolling VWAP over `window`. dollar=True weights typical price by
    closeadj*volume (dollar terms); else by raw volume."""
    tp = _typ(df)
    if dollar:
        w = (df['closeadj'] * df['volume'])
    else:
        w = df['volume']
    num = (tp * w).rolling(window).sum()
    den = w.rolling(window).sum()
    return (num / den).replace([np.inf, -np.inf], np.nan)


def _vw_std(df, window, vwap=None, dollar=False):
    """Volume-weighted std of typical price around its rolling VWAP."""
    tp = _typ(df)
    if vwap is None:
        vwap = _vwap(df, window, dollar=dollar)
    w = (df['closeadj'] * df['volume']) if dollar else df['volume']
    den = w.rolling(window).sum()
    var = (w * (tp - vwap) ** 2).rolling(window).sum() / den
    return np.sqrt(var.clip(lower=0)).replace([np.inf, -np.inf], np.nan)


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _slope(s, window):
    # normalized slope: change over window relative to current level
    return ((s - s.shift(window)) / window).replace([np.inf, -np.inf], np.nan)


def _convexity(s):
    # 2nd difference (discrete curvature) of a series
    return s - 2.0 * s.shift(1) + s.shift(2)


def _build(df, idx_start, idx_end):
    """Generate distinct VWAP-deviation/convexity variants. Facets are cycled
    across the 6 windows so each emitted column is a unique (facet, window)
    expression. Returns an ordered list of pandas Series."""
    price_raw = df['close']
    price_adj = df['closeadj']
    vol = df['volume']
    tp = _typ(df)

    feats = []  # list of Series in emission order

    # Pre-compute per-window cores
    cores = {}
    for n in WINDOWS:
        vwap = _vwap(df, n)
        vwap_d = _vwap(df, n, dollar=True)
        price = _price(df, n)
        dev = price - vwap                      # price - VWAP deviation
        ratio = (price / vwap - 1.0).replace([np.inf, -np.inf], np.nan)
        vstd = _vw_std(df, n, vwap=vwap)
        cores[n] = dict(vwap=vwap, vwap_d=vwap_d, price=price, dev=dev,
                        ratio=ratio, vstd=vstd)

    # Facet builders: each takes a window n and returns a Series.
    def f_dev(n):                 # raw price-VWAP deviation
        return cores[n]['dev']

    def f_ratio(n):               # (price/VWAP - 1)
        return cores[n]['ratio']

    def f_dev_z(n):               # deviation z-score
        return _z(cores[n]['dev'], n)

    def f_ratio_z(n):             # ratio z-score
        return _z(cores[n]['ratio'], n)

    def f_band_upper(n, k=2.0):   # distance to upper VWAP band
        c = cores[n]
        upper = c['vwap'] + k * c['vstd']
        return (upper - c['price']).replace([np.inf, -np.inf], np.nan)

    def f_band_lower(n, k=2.0):   # distance to lower VWAP band
        c = cores[n]
        lower = c['vwap'] - k * c['vstd']
        return (c['price'] - lower).replace([np.inf, -np.inf], np.nan)

    def f_band_pos(n, k=2.0):     # %position within ±k bands [0..1]
        c = cores[n]
        lower = c['vwap'] - k * c['vstd']
        width = (2.0 * k * c['vstd'])
        return ((c['price'] - lower) / width).replace([np.inf, -np.inf], np.nan)

    def f_convex(n):              # VWAP convexity: curvature of price about VWAP
        return _convexity(cores[n]['dev'])

    def f_vwap_convex(n):         # convexity of the VWAP line itself
        return _convexity(cores[n]['vwap'])

    def f_slope(n):               # VWAP slope (normalized)
        return _slope(cores[n]['vwap'], max(2, n // 4))

    def f_dev_slope(n):           # slope of the deviation
        return _slope(cores[n]['dev'], max(2, n // 4))

    def f_reversion(n):           # deviation mean-reversion: -dev_z * recent dDev
        c = cores[n]
        return (-_z(c['dev'], n) * c['dev'].diff()).replace([np.inf, -np.inf], np.nan)

    def f_dev_vol(n):             # deviation * volume interaction (z of volume)
        c = cores[n]
        volz = _z(vol, n)
        return (c['ratio'] * volz).replace([np.inf, -np.inf], np.nan)

    facets = [f_dev, f_ratio, f_dev_z, f_ratio_z, f_band_upper, f_band_lower,
              f_band_pos, f_convex, f_vwap_convex, f_slope, f_dev_slope,
              f_reversion, f_dev_vol]

    # Cross-window facets (need a pair of windows)
    short_long_pairs = [(5, 21), (10, 63), (21, 126), (63, 252), (5, 252),
                        (10, 126)]

    def f_sl_spread(pair):        # short-vs-long VWAP spread (normalized)
        a, b = pair
        va, vb = cores[a]['vwap'], cores[b]['vwap']
        return ((va - vb) / vb).replace([np.inf, -np.inf], np.nan)

    def f_sl_dev_spread(pair):    # short-vs-long deviation spread
        a, b = pair
        return (cores[a]['ratio'] - cores[b]['ratio'])

    # Anchored VWAP: cumulative VWAP anchored at rolling window start ==
    # rolling VWAP; "anchored distance" = standardized deviation in vw-std units
    def f_anchored(n):
        c = cores[n]
        return (c['dev'] / c['vstd']).replace([np.inf, -np.inf], np.nan)

    def f_dollar_ratio(n):        # price vs dollar-weighted VWAP
        c = cores[n]
        return (c['price'] / c['vwap_d'] - 1.0).replace([np.inf, -np.inf], np.nan)

    # Emit in a deterministic, diverse order: iterate facets, then windows.
    all_series = []
    for fac in facets:
        for n in WINDOWS:
            all_series.append(fac(n))
    # cross-window spreads
    for pair in short_long_pairs:
        all_series.append(f_sl_spread(pair))
    for pair in short_long_pairs:
        all_series.append(f_sl_dev_spread(pair))
    # anchored distance + dollar ratio across windows
    for n in WINDOWS:
        all_series.append(f_anchored(n))
    for n in WINDOWS:
        all_series.append(f_dollar_ratio(n))
    # band variants with k=1 and k=3 to add diversity / fill out to 150
    for k in (1.0, 3.0):
        for n in WINDOWS:
            all_series.append(f_band_pos(n, k=k))
    # deviation z-score with a fixed cross-window normalization horizon (63d),
    # distinct from the per-window z-score facet above
    for n in WINDOWS:
        all_series.append(_z(cores[n]['ratio'], 63 if n != 63 else 126))

    # --- additional distinct facets to reach 150 total ---
    # normalized band-distance (in vw-std units) upper & lower
    for n in WINDOWS:
        c = cores[n]
        all_series.append(((c['vwap'] + 2.0 * c['vstd'] - c['price']) / c['vstd'])
                          .replace([np.inf, -np.inf], np.nan))
    for n in WINDOWS:
        c = cores[n]
        all_series.append(((c['price'] - (c['vwap'] - 2.0 * c['vstd'])) / c['vstd'])
                          .replace([np.inf, -np.inf], np.nan))
    # z-score of VWAP convexity (curvature regime)
    for n in WINDOWS:
        all_series.append(_z(_convexity(cores[n]['vwap']), n))
    # z-score of VWAP slope (trend strength of VWAP)
    for n in WINDOWS:
        all_series.append(_z(_slope(cores[n]['vwap'], max(2, n // 4)), n))
    # deviation*dollar-volume interaction (dollar terms)
    dvol = (df['closeadj'] * df['volume'])
    for n in WINDOWS:
        all_series.append((cores[n]['ratio'] * _z(dvol, n))
                          .replace([np.inf, -np.inf], np.nan))

    return all_series[idx_start:idx_end]



def get_f21_vvwap_convexity_base_076_150(df):
    series = _build(df, 75, 150)
    features = {}
    for offset, s in enumerate(series):
        k = 76 + offset
        features[f'f21_vvwap_convexity_{k:03d}'] = s
    return pd.DataFrame(features)
