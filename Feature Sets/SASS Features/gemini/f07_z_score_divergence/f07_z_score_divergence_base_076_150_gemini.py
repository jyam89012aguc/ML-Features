# f07_z_score_divergence — REAL indicator: price z-score & z-score divergence (076-150)
# Core:  z(x, n) = (x - SMA_n(x)) / STD_n(x)
# Facets continued: price-z vs volume-z divergence, price-z vs momentum-z divergence,
#         Bollinger %B position, z-of-z (acceleration), cross-window z dispersion,
#         z mean-reversion gap interactions, and more short/long divergence pairs.
# Rule: rolling windows > 21d use 'closeadj'; volume-z uses raw 'volume'.
import numpy as np
import pandas as pd


def _col_for(df, n):
    return df['closeadj'] if n > 21 else df['close']


def _z(x, n):
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    return ((x - m) / s).replace([np.inf, -np.inf], np.nan)


def _zser(x, n):
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    return ((x - m) / s).replace([np.inf, -np.inf], np.nan)


def _pctb(x, n, k=2.0):
    m = x.rolling(n).mean()
    s = x.rolling(n).std()
    upper = m + k * s
    lower = m - k * s
    return ((x - lower) / (upper - lower)).replace([np.inf, -np.inf], np.nan)


def get_f07_z_score_divergence_base_076_150(df):
    features = {}
    close = df['close']
    closeadj = df['closeadj']
    volume = df['volume']

    out = {}

    # --- Facet H: price-z vs volume-z divergence (076-090) ---
    # volume-z uses RAW volume; price-z uses col_for rule.
    h_wins = [5, 10, 21, 42, 63, 126, 252, 8, 13, 34, 84, 189, 7, 14, 30]
    for w in h_wins:
        pz = _z(_col_for(df, w), w)
        vz = _zser(volume, w)
        out[len(out) + 1] = (pz - vz)

    # --- Facet I: price-z vs momentum-z divergence (091-102) ---
    # momentum = n-period ROC of closeadj, then z-scored.
    i_specs = [(5, 5), (10, 10), (21, 21), (42, 21), (63, 63), (126, 63),
               (252, 126), (10, 21), (21, 63), (63, 126), (8, 13), (34, 21)]
    for (w, mom) in i_specs:
        pz = _z(_col_for(df, w), w)
        roc = closeadj.pct_change(mom).replace([np.inf, -np.inf], np.nan)
        mz = _zser(roc, w)
        out[len(out) + 1] = (pz - mz)

    # --- Facet J: Bollinger %B-style position (103-117) ---
    j_specs = [(20, 2.0), (20, 1.0), (50, 2.0), (10, 2.0), (21, 2.5),
               (63, 2.0), (126, 2.0), (252, 2.0), (5, 1.5), (42, 2.0),
               (84, 2.0), (189, 2.0), (30, 1.5), (14, 2.0), (100, 2.0)]
    for (w, k) in j_specs:
        out[len(out) + 1] = _pctb(_col_for(df, w), w, k)

    # --- Facet K: z-of-z (z acceleration / second-order) (118-126) ---
    k_specs = [(21, 5), (63, 10), (126, 21), (21, 10), (63, 21),
               (252, 21), (10, 5), (42, 10), (189, 21)]
    for (w, w2) in k_specs:
        z = _z(_col_for(df, w), w)
        out[len(out) + 1] = _zser(z, w2)

    # --- Facet L: cross-window z dispersion (std of multi-window z) (127-135) ---
    l_groups = [
        [5, 21, 63], [10, 42, 126], [21, 63, 252], [5, 10, 21],
        [42, 126, 252], [8, 34, 84], [13, 63, 189], [7, 30, 90],
        [21, 126, 252],
    ]
    for g in l_groups:
        zs = pd.concat([_z(_col_for(df, w), w) for w in g], axis=1)
        out[len(out) + 1] = zs.std(axis=1, ddof=0).replace([np.inf, -np.inf], np.nan)

    # --- Facet M: more short-minus-long z divergence pairs (136-145) ---
    m_pairs = [(5, 21), (10, 42), (21, 63), (42, 126), (63, 252),
               (5, 252), (10, 126), (21, 252), (5, 126), (34, 189)]
    for (s, l) in m_pairs:
        out[len(out) + 1] = _z(_col_for(df, s), s) - _z(_col_for(df, l), l)

    # --- Facet N: z mean-reversion gap scaled by |z| (extremity-weighted) (146-150) ---
    n_wins = [21, 63, 126, 252, 42]
    for w in n_wins:
        z = _z(_col_for(df, w), w)
        out[len(out) + 1] = (-z * z.abs())

    for i in range(76, 151):
        features[f'f07_z_score_divergence_{i:03d}'] = out[i - 75]
    return pd.DataFrame(features, index=df.index)
