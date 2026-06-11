# Real indicator: Elder's Force Index (FI) and volume "explosions" (part 2)
#   FI = (close - prior_close) * volume ; smoothed FI = EMA(n, FI)
#   "Explosions" = extreme FI events (|FI z-score| beyond threshold)
# This file extends the facet set with: EMA(2/13) classic pair, FI acceleration,
#   FI dispersion/volatility, explosion regime distance, cumulative-FI z, FI vs
#   range, ratio of up- vs down-force, persistence, drawdown of cumulative FI,
#   normalized FI Delta, force-per-dollar-vol z, long-window divergence, etc.
# Rule: price change uses 'closeadj' on windows > 21d, 'close' on windows <= 21d;
#   raw 'volume' for force; closeadj*volume for normalization.
import numpy as np
import pandas as pd

WINDOWS = [2, 13, 21, 63, 126]
Z_THRESH = 2.0


def _price_col(df, window):
    return df['closeadj'] if window > 21 else df['close']


def _force_index(df, window):
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


def get_f28_force_index_explosions_base_076_150(df):
    features = {}
    fi_raw = {w: _force_index(df, w) for w in WINDOWS}
    fi_ema = {w: _ema(fi_raw[w], w) for w in WINDOWS}
    dvol = _dollar_vol(df)
    px_def = df['closeadj']
    rng = (df['high'] - df['low']).abs()

    cols = []
    W = WINDOWS

    # Normalized FI per window (used by several facets)
    fi_norm = {}
    for w in W:
        scale = dvol.rolling(w).mean().replace(0.0, np.nan)
        fi_norm[w] = (fi_raw[w] / scale).replace([np.inf, -np.inf], np.nan)

    # --- Facet P: classic EMA(2) & EMA(13) FI, normalized + their ratio (5) ---
    sc2 = _ema(dvol, 2).replace(0.0, np.nan)
    sc13 = _ema(dvol, 13).replace(0.0, np.nan)
    fi_e2 = _ema(fi_raw[2], 2)
    fi_e13 = _ema(fi_raw[13], 13)
    cols.append(('fi_ema2', (fi_e2 / sc2).replace([np.inf, -np.inf], np.nan)))
    cols.append(('fi_ema13', (fi_e13 / sc13).replace([np.inf, -np.inf], np.nan)))
    cols.append(('fi_ema2_13_ratio', (fi_e2 / fi_e13.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)))
    cols.append(('fi_ema2_13_diff', ((fi_e2 - fi_e13) / sc13).replace([np.inf, -np.inf], np.nan)))
    cols.append(('fi_ema2_13_zdiff', _z(fi_e2, 21) - _z(fi_e13, 21)))

    # --- Facet Q: FI acceleration (2nd diff of EMA-FI) over window (5) ---
    for w in W:
        cols.append(('fi_accel', _slope(_slope(fi_ema[w], w), w)))

    # --- Facet R: FI dispersion / volatility (rolling std of normalized FI) (5) ---
    for w in W:
        cols.append(('fi_disp', fi_norm[w].rolling(max(w, 5)).std()))

    # --- Facet S: explosion regime distance = |z| - thresh (signed, EMA) (5) ---
    for w in W:
        z = _z(fi_ema[w], max(w, 21))
        cols.append(('fi_regdist', _ema(z.abs() - Z_THRESH, max(w, 5))))

    # --- Facet T: cumulative FI z-score (z of running cumsum window) (5) ---
    for w in W:
        cum = fi_norm[w].rolling(w).sum()
        cols.append(('fi_cumz', _z(cum, max(w, 5))))

    # --- Facet U: FI vs range interaction (FI per unit range, normalized) (5) ---
    for w in W:
        denom = (rng * df['volume']).rolling(w).mean().replace(0.0, np.nan)
        fr = (fi_raw[w] / denom).replace([np.inf, -np.inf], np.nan)
        cols.append(('fi_vs_range', _ema(fr, w)))

    # --- Facet V: up-force vs down-force ratio over window (5) ---
    for w in W:
        up = fi_raw[w].clip(lower=0.0).rolling(max(w, 5)).sum()
        dn = (-fi_raw[w].clip(upper=0.0)).rolling(max(w, 5)).sum()
        cols.append(('fi_updn', ((up - dn) / (up + dn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)))

    # --- Facet W: FI persistence (fraction of same-sign days in window) (5) ---
    for w in W:
        sgn = np.sign(fi_raw[w])
        cols.append(('fi_persist', sgn.rolling(max(w, 5)).mean()))

    # --- Facet X: drawdown of cumulative FI (cum below its running max) (5) ---
    for w in W:
        cum = fi_norm[w].cumsum()
        peak = cum.rolling(max(w, 5), min_periods=1).max()
        cols.append(('fi_cumdd', (cum - peak)))

    # --- Facet Y: normalized FI Delta / ROC of EMA-FI (5) ---
    for w in W:
        cols.append(('fi_roc', _roc(fi_ema[w], w)))

    # --- Facet Z: force-per-dollar-volume z-score (5) ---
    for w in W:
        fpd = (fi_raw[w] / dvol.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
        cols.append(('fi_fpd_z', _z(fpd, max(w, 5))))

    # --- Facet AA: long-window FI-vs-price divergence sign (5) ---
    for w in W:
        proc_sign = np.sign(_roc(px_def, w))
        fi_sign = np.sign(_ema(fi_raw[w], w))
        cols.append(('fi_divsign', (fi_sign - proc_sign)))

    # --- Facet BB: short-vs-long FI spread z (5 pairs) ---
    pairs = [(2, 13), (2, 21), (13, 63), (21, 126), (63, 126)]
    for (s, l) in pairs:
        sc = _ema(dvol, l).replace(0.0, np.nan)
        spread = ((fi_ema[s] - fi_ema[l]) / sc).replace([np.inf, -np.inf], np.nan)
        cols.append(('fi_spread_z', _z(spread, max(l, 5))))

    # --- Facet CC: explosion magnitude EMA-smoothed (5) ---
    for w in W:
        z = _z(fi_ema[w], max(w, 21))
        mag = (z.abs() - Z_THRESH).clip(lower=0.0)
        cols.append(('fi_expl_ema', _ema(mag.where(z.notna()), max(w, 5))))

    # --- Facet DD: FI normalized level EMA-smoothed slope (momentum of force) (5) ---
    for w in W:
        cols.append(('fi_norm_mom', _slope(_ema(fi_norm[w], w), w)))

    # Emit exactly 75 columns 076..150
    assert len(cols) == 75, len(cols)
    for k, (_, series) in enumerate(cols):
        i = 76 + k
        features[f'f28_force_index_explosions_{i:03d}'] = series
    return pd.DataFrame(features, index=df.index)
