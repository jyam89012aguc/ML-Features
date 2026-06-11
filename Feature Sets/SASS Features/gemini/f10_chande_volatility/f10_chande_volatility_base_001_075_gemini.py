# f10_chande_volatility — REAL indicator: Chande Momentum Oscillator (CMO)
# + Chande's volatility (VIDYA-style stdev ratio / variable-index dynamic MA).
#
# CMO(n) = 100 * (sumUp - sumDown) / (sumUp + sumDown), over n bars, where
#   Up   = max(close - close.shift(1), 0)
#   Down = max(close.shift(1) - close, 0)
# Chande volatility ratio  VI = STD_short / STD_long  (VIDYA volatility index).
# VIDYA adaptive MA uses k = |CMO|/100 (or VI) as the variable smoothing factor:
#   VIDYA_t = k_t * close_t + (1 - k_t) * VIDYA_{t-1}.
#
# Facets built across windows 9/14/21/63/126:
#   CMO level, |CMO| momentum strength, CMO z-score, CMO slope/delta,
#   VI volatility ratio, VIDYA, price-VIDYA, CMO overbought/oversold threshold
#   distance, CMO sign streak.
# Rule: rolling windows > 21d use 'closeadj'; <=21d may use raw 'close'.
import numpy as np
import pandas as pd

WINDOWS = [9, 14, 21, 63, 126]


def _px(df, window):
    """Price column: >21d windows use closeadj, else raw close."""
    return df['closeadj'] if window > 21 else df['close']


def _cmo(price, n):
    """Chande Momentum Oscillator over n bars, range [-100, 100]."""
    delta = price.diff()
    up = delta.clip(lower=0.0)
    down = (-delta).clip(lower=0.0)
    su = up.rolling(n).sum()
    sd = down.rolling(n).sum()
    denom = su + sd
    cmo = 100.0 * (su - sd) / denom
    return cmo.replace([np.inf, -np.inf], np.nan)


def _z(s, n):
    m = s.rolling(n).mean()
    sd = s.rolling(n).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _vi(price, short, long):
    """Chande volatility index: ratio of short to long stdev of price changes."""
    chg = price.diff()
    sd_s = chg.rolling(short).std()
    sd_l = chg.rolling(long).std()
    return (sd_s / sd_l).replace([np.inf, -np.inf], np.nan)


def _vidya(price, n, k=None):
    """VIDYA adaptive MA. Variable smoothing factor k (defaults to |CMO|/100)."""
    if k is None:
        k = _cmo(price, n).abs() / 100.0
    f = 2.0 / (n + 1.0)
    k = (k * f).clip(0.0, 1.0)
    p = price.to_numpy(dtype=float)
    kk = k.to_numpy(dtype=float)
    out = np.full(p.shape, np.nan)
    prev = np.nan
    for t in range(len(p)):
        kt = kk[t]
        pt = p[t]
        if np.isnan(kt) or np.isnan(pt):
            continue
        if np.isnan(prev):
            prev = pt
        prev = kt * pt + (1.0 - kt) * prev
        out[t] = prev
    return pd.Series(out, index=price.index)


def _sign_streak(s):
    """Signed run length of consecutive same-sign values."""
    sign = np.sign(s.fillna(0.0).to_numpy())
    out = np.zeros(len(sign))
    run = 0.0
    prev = 0.0
    for t in range(len(sign)):
        v = sign[t]
        if v == 0:
            run = 0.0
        elif v == prev:
            run += v
        else:
            run = v
        out[t] = run
        prev = v
    res = pd.Series(out, index=s.index)
    res[s.isna()] = np.nan
    return res


def get_f10_chande_volatility_base_001_075(df):
    features = {}
    f = {}

    # ---- Facet A: CMO level (5 windows) ----
    for w in WINDOWS:
        f.setdefault('cmo_level', []).append(_cmo(_px(df, w), w))
    # ---- Facet B: |CMO| momentum strength ----
    for w in WINDOWS:
        f.setdefault('cmo_abs', []).append(_cmo(_px(df, w), w).abs())
    # ---- Facet C: CMO z-score (z over 21) ----
    for w in WINDOWS:
        f.setdefault('cmo_z', []).append(_z(_cmo(_px(df, w), w), 21))
    # ---- Facet D: CMO slope / delta (1-bar change) ----
    for w in WINDOWS:
        f.setdefault('cmo_delta', []).append(_cmo(_px(df, w), w).diff())
    # ---- Facet E: CMO 5-bar slope ----
    for w in WINDOWS:
        f.setdefault('cmo_slope5', []).append(_cmo(_px(df, w), w).diff(5) / 5.0)
    # ---- Facet F: VI volatility ratio short=w long=2w ----
    for w in WINDOWS:
        f.setdefault('vi_ratio', []).append(_vi(_px(df, 2 * w), w, 2 * w))
    # ---- Facet G: VIDYA (CMO-driven) ----
    for w in WINDOWS:
        f.setdefault('vidya', []).append(_vidya(_px(df, w), w))
    # ---- Facet H: price - VIDYA (deviation) ----
    for w in WINDOWS:
        px = _px(df, w)
        f.setdefault('px_vidya', []).append(px - _vidya(px, w))
    # ---- Facet I: CMO overbought distance (CMO - 50) ----
    for w in WINDOWS:
        f.setdefault('cmo_ob', []).append(_cmo(_px(df, w), w) - 50.0)
    # ---- Facet J: CMO oversold distance (CMO + 50) ----
    for w in WINDOWS:
        f.setdefault('cmo_os', []).append(_cmo(_px(df, w), w) + 50.0)
    # ---- Facet K: CMO sign streak ----
    for w in WINDOWS:
        f.setdefault('cmo_streak', []).append(_sign_streak(_cmo(_px(df, w), w)))
    # ---- Facet L: VI z-score ----
    for w in WINDOWS:
        f.setdefault('vi_z', []).append(_z(_vi(_px(df, 2 * w), w, 2 * w), 21))
    # ---- Facet M: |CMO|/100 smoothing factor (VIDYA k) ----
    for w in WINDOWS:
        f.setdefault('cmo_k', []).append(_cmo(_px(df, w), w).abs() / 100.0)
    # ---- Facet N: price-VIDYA as pct of price ----
    for w in WINDOWS:
        px = _px(df, w)
        dev = (px - _vidya(px, w)) / px
        f.setdefault('px_vidya_pct', []).append(dev.replace([np.inf, -np.inf], np.nan))
    # ---- Facet O: CMO percentile rank over 63 ----
    for w in WINDOWS:
        cmo = _cmo(_px(df, w), w)
        rank = cmo.rolling(63).apply(
            lambda x: (x[-1] > x).mean(), raw=True)
        f.setdefault('cmo_rank', []).append(rank)

    # Assemble in fixed facet order -> 15 facets x 5 windows = 75
    order = ['cmo_level', 'cmo_abs', 'cmo_z', 'cmo_delta', 'cmo_slope5',
             'vi_ratio', 'vidya', 'px_vidya', 'cmo_ob', 'cmo_os',
             'cmo_streak', 'vi_z', 'cmo_k', 'px_vidya_pct', 'cmo_rank']
    series_list = []
    for facet in order:
        series_list.extend(f[facet])

    for i in range(1, 76):
        features[f'f10_chande_volatility_{i:03d}'] = series_list[i - 1]
    return pd.DataFrame(features)
