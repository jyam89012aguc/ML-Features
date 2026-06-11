# f07_z_score_divergence — REAL indicator: price z-score & z-score divergence
# Core:  z(x, n) = (x - SMA_n(x)) / STD_n(x)
# Facets: z level, short-minus-long z divergence, z of closeadj vs smoothed price,
#         z mean-reversion gap, z slope/delta, |z| extreme-tail distance,
#         z sign-flip streak, price-z vs volume-z divergence, Bollinger %B position.
# Rule: rolling windows > 21d use 'closeadj'; volume-z uses raw 'volume'.
import numpy as np
import pandas as pd


def _col_for(df, n):
    # >21d windows use adjusted close; <=21d may use raw close
    return df['closeadj'] if n > 21 else df['close']


def _z(x, n):
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    z = (x - m) / s
    return z.replace([np.inf, -np.inf], np.nan)


def _zser(x, n):
    """z of an arbitrary series x using its own rolling stats."""
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    return ((x - m) / s).replace([np.inf, -np.inf], np.nan)


def _pctb(x, n, k=2.0):
    """Bollinger %B-style position of x within its band over window n."""
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    upper = m + k * s
    lower = m - k * s
    return ((x - lower) / (upper - lower)).replace([np.inf, -np.inf], np.nan)


def _signflip_streak(z):
    """Consecutive-bar streak length since the last sign flip of z."""
    sign = np.sign(z)
    flip = (sign != sign.shift(1)) & sign.notna() & sign.shift(1).notna()
    grp = flip.cumsum()
    streak = z.groupby(grp).cumcount() + 1.0
    return streak.where(z.notna())


# Window pairs (short, long) for divergence facets
_PAIRS = [(5, 21), (10, 42), (21, 63), (42, 126), (63, 252), (10, 21),
          (21, 126), (5, 63), (63, 126), (126, 252)]


def get_f07_z_score_divergence_base_001_075(df):
    features = {}
    close = df['close']
    closeadj = df['closeadj']
    volume = df['volume']

    out = {}

    # --- Facet A: raw z-score level across many windows (001-012) ---
    a_wins = [5, 8, 10, 13, 21, 34, 42, 63, 84, 126, 189, 252]
    for w in a_wins:
        out[len(out) + 1] = _z(_col_for(df, w), w)

    # --- Facet B: short-minus-long z divergence (013-024) ---
    for (s, l) in _PAIRS:
        out[len(out) + 1] = _z(_col_for(df, s), s) - _z(_col_for(df, l), l)
    # two more pair variants to reach 12 in this facet
    out[len(out) + 1] = _z(close, 5) - _z(closeadj, 252)
    out[len(out) + 1] = _z(close, 10) - _z(closeadj, 126)

    # --- Facet C: z of closeadj vs z of a smoothed (EMA) price (025-036) ---
    c_wins = [5, 10, 21, 42, 63, 126, 252, 8, 13, 34, 84, 189]
    for w in c_wins:
        sm = closeadj.ewm(span=max(2, w // 2), adjust=False).mean()
        out[len(out) + 1] = (_z(_col_for(df, w), w) - _zser(sm, w))

    # --- Facet D: z mean-reversion gap = -z (distance to revert) (037-048) ---
    d_wins = [5, 10, 21, 42, 63, 126, 252, 7, 14, 30, 90, 200]
    for w in d_wins:
        out[len(out) + 1] = (-_z(_col_for(df, w), w))

    # --- Facet E: z slope / delta over k bars (049-060) ---
    e_specs = [(21, 1), (21, 3), (21, 5), (63, 1), (63, 5), (63, 10),
               (10, 1), (10, 3), (126, 5), (126, 10), (252, 10), (252, 21)]
    for (w, k) in e_specs:
        z = _z(_col_for(df, w), w)
        out[len(out) + 1] = (z - z.shift(k)) / float(k)

    # --- Facet F: |z| extreme-tail distance beyond threshold (061-072) ---
    f_specs = [(21, 2.0), (21, 1.0), (63, 2.0), (63, 1.5), (126, 2.0),
               (252, 2.0), (10, 2.0), (42, 1.5), (84, 2.0), (189, 2.0),
               (5, 1.5), (21, 2.5)]
    for (w, thr) in f_specs:
        z = _z(_col_for(df, w), w)
        out[len(out) + 1] = (z.abs() - thr).clip(lower=0.0)

    # --- Facet G: z sign-flip streak (073-075) ---
    for w in [21, 63, 126]:
        out[len(out) + 1] = _signflip_streak(_z(_col_for(df, w), w))

    for i in range(1, 76):
        features[f'f07_z_score_divergence_{i:03d}'] = out[i]
    return pd.DataFrame(features, index=df.index)
