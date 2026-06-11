# Real indicator: Elder's Force Index (FI) and volume "explosions"
#   FI = (close - prior_close) * volume ; smoothed FI = EMA(n, FI)
#   "Explosions" = extreme FI events (|FI z-score| beyond threshold)
# Facets across windows {2,13,21,63,126}: FI level (normalized by dollar-volume
#   scale), EMA-smoothed FI, FI z-score, explosion flag/magnitude, FI sign streak,
#   FI-vs-price divergence, cumulative FI, FI percentile rank, FI slope/Delta,
#   short-vs-long FI spread, force-per-dollar-volume.
# Rule: price change uses 'closeadj' on windows > 21d, 'close' on windows <= 21d;
#   raw 'volume' for force; closeadj*volume for normalization.
import numpy as np
import pandas as pd

WINDOWS = [2, 13, 21, 63, 126]
Z_THRESH = 2.0


def _price_col(df, window):
    return df['closeadj'] if window > 21 else df['close']


def _force_index(df, window):
    """Raw Force Index using the price column appropriate for the window."""
    px = _price_col(df, window)
    return px.diff() * df['volume']


def _dollar_vol(df):
    return (df['closeadj'] * df['volume']).abs()


def _ema(s, span):
    return s.ewm(span=max(span, 2), adjust=False).mean()


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _roc(s, window):
    return (s - s.shift(window)) / s.shift(window).abs().replace(0.0, np.nan)


def _slope(s, window):
    return (s - s.shift(window)) / float(window)


def _pct_rank(s, window):
    return s.rolling(window).apply(
        lambda a: (a[-1] > a[:-1]).mean() if len(a) > 1 else np.nan, raw=True)


def _sign_streak(sign):
    """Length of the current run of identical FI sign (signed by direction)."""
    out = np.zeros(len(sign))
    prev = 0.0
    run = 0
    vals = sign.to_numpy()
    for i in range(len(vals)):
        v = vals[i]
        if np.isnan(v) or v == 0:
            run = 0
        elif v == prev:
            run += 1
        else:
            run = 1
        out[i] = run * (1.0 if v > 0 else (-1.0 if v < 0 else 0.0))
        prev = v
    return pd.Series(out, index=sign.index)


def get_f28_force_index_explosions_base_001_075(df):
    features = {}
    fi_raw = {w: _force_index(df, w) for w in WINDOWS}
    fi_ema = {w: _ema(fi_raw[w], w) for w in WINDOWS}
    dvol = _dollar_vol(df)
    px_def = df['closeadj']

    cols = []
    W = WINDOWS

    # --- Facet A: FI level normalized by dollar-volume scale (rolling) (5) ---
    for w in W:
        scale = dvol.rolling(w).mean().replace(0.0, np.nan)
        cols.append(('fi_norm', (fi_raw[w] / scale).replace([np.inf, -np.inf], np.nan)))

    # --- Facet B: EMA-smoothed FI, normalized by dollar-vol EMA scale (5) ---
    for w in W:
        scale = _ema(dvol, w).replace(0.0, np.nan)
        cols.append(('fi_ema_norm', (fi_ema[w] / scale).replace([np.inf, -np.inf], np.nan)))

    # --- Facet C: FI z-score over each window (5) ---
    for w in W:
        cols.append(('fi_z', _z(fi_raw[w], max(w, 5))))

    # --- Facet D: EMA-FI z-score (5) ---
    for w in W:
        cols.append(('fi_ema_z', _z(fi_ema[w], max(w, 5))))

    # Explosion z-score: extremeness of EMA-FI vs a stable baseline window
    # (>=21 bars so the z is meaningful even for tiny smoothing spans).
    def _expl_z(w):
        return _z(fi_ema[w], max(w, 21))

    # --- Facet E: explosion flag |z|>thresh (5) ---
    for w in W:
        z = _expl_z(w)
        cols.append(('fi_expl_flag', (z.abs() > Z_THRESH).astype(float).where(z.notna())))

    # --- Facet F: explosion magnitude = max(|z|-thresh,0) (5) ---
    for w in W:
        z = _expl_z(w)
        cols.append(('fi_expl_mag', (z.abs() - Z_THRESH).clip(lower=0.0).where(z.notna())))

    # --- Facet G: signed explosion magnitude (5) ---
    for w in W:
        z = _expl_z(w)
        mag = (z.abs() - Z_THRESH).clip(lower=0.0)
        cols.append(('fi_expl_smag', (np.sign(z) * mag).where(z.notna())))

    # --- Facet H: explosion count over window (5) ---
    for w in W:
        z = _expl_z(w)
        flag = (z.abs() > Z_THRESH).astype(float).where(z.notna())
        cols.append(('fi_expl_cnt', flag.rolling(max(w, 21)).sum()))

    # --- Facet I: FI sign streak (5) ---
    for w in W:
        cols.append(('fi_streak', _sign_streak(np.sign(fi_raw[w]))))

    # --- Facet J: cumulative FI over window, normalized (5) ---
    for w in W:
        scale = dvol.rolling(w).sum().replace(0.0, np.nan)
        cols.append(('fi_cum', (fi_raw[w].rolling(w).sum() / scale).replace([np.inf, -np.inf], np.nan)))

    # --- Facet K: FI percentile rank in window (5) ---
    for w in W:
        cols.append(('fi_pctrank', _pct_rank(fi_raw[w], max(w, 5))))

    # --- Facet L: FI slope / Delta over window (5) ---
    for w in W:
        cols.append(('fi_slope', _slope(fi_ema[w], w)))

    # --- Facet M: force-per-dollar-volume (FI / dollar-vol, EMA-smoothed) (5) ---
    for w in W:
        fpd = (fi_raw[w] / dvol.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
        cols.append(('fi_fpd', _ema(fpd, w)))

    # --- Facet N: short-vs-long FI spread (EMA short minus EMA long) (5 pairs) ---
    pairs = [(2, 13), (2, 21), (13, 63), (21, 126), (63, 126)]
    for (s, l) in pairs:
        sc = _ema(dvol, l).replace(0.0, np.nan)
        spread = (fi_ema[s] - fi_ema[l]) / sc
        cols.append(('fi_spread', spread.replace([np.inf, -np.inf], np.nan)))

    # --- Facet O: FI-vs-price divergence (corr of FI sign vs price ROC) (5) ---
    for w in W:
        proc = _roc(px_def, w)
        fi_n = (fi_raw[w] / dvol.rolling(w).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
        cols.append(('fi_div', (fi_n.rolling(max(w, 5)).corr(proc)).replace([np.inf, -np.inf], np.nan)))

    # Emit exactly 75 columns 001..075
    assert len(cols) == 75, len(cols)
    for i, (_, series) in enumerate(cols, start=1):
        features[f'f28_force_index_explosions_{i:03d}'] = series
    return pd.DataFrame(features, index=df.index)
