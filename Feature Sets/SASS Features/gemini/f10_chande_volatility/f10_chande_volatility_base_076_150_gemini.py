# f10_chande_volatility — REAL indicator: Chande Momentum Oscillator (CMO)
# + Chande's volatility (VIDYA-style stdev ratio / variable-index dynamic MA).
# File 2 of 2: features 076..150 (75 columns), further DISTINCT facets.
#
# CMO(n) = 100 * (sumUp - sumDown) / (sumUp + sumDown).
# VI = STD_short / STD_long  (VIDYA volatility index).
# VIDYA_t = k_t*close_t + (1-k_t)*VIDYA_{t-1},  k driven by |CMO|/100 or VI.
# Rule: rolling windows > 21d use 'closeadj'; <=21d may use raw 'close'.
import numpy as np
import pandas as pd

WINDOWS = [9, 14, 21, 63, 126]


def _px(df, window):
    return df['closeadj'] if window > 21 else df['close']


def _cmo(price, n):
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
    chg = price.diff()
    sd_s = chg.rolling(short).std()
    sd_l = chg.rolling(long).std()
    return (sd_s / sd_l).replace([np.inf, -np.inf], np.nan)


def _vidya(price, n, k=None):
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


def _vidya_vi(price, short, long):
    """VIDYA whose smoothing factor is driven by the volatility ratio VI."""
    k = _vi(price, short, long).clip(0.0, 1.0)
    return _vidya(price, short, k=k)


def _sign_streak(s):
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


def get_f10_chande_volatility_base_076_150(df):
    features = {}
    f = {}

    # ---- Facet A: CMO short-vs-long spread (CMO(w) - CMO(2w)) ----
    for w in WINDOWS:
        f.setdefault('cmo_spread', []).append(
            _cmo(_px(df, w), w) - _cmo(_px(df, 2 * w), 2 * w))
    # ---- Facet B: CMO acceleration (2nd diff) ----
    for w in WINDOWS:
        f.setdefault('cmo_accel', []).append(_cmo(_px(df, w), w).diff().diff())
    # ---- Facet C: |CMO| z-score (momentum-strength regime) ----
    for w in WINDOWS:
        f.setdefault('cmo_abs_z', []).append(_z(_cmo(_px(df, w), w).abs(), 21))
    # ---- Facet D: VI-driven VIDYA ----
    for w in WINDOWS:
        f.setdefault('vidya_vi', []).append(_vidya_vi(_px(df, 2 * w), w, 2 * w))
    # ---- Facet E: price - VI-VIDYA ----
    for w in WINDOWS:
        px = _px(df, 2 * w)
        f.setdefault('px_vidya_vi', []).append(px - _vidya_vi(px, w, 2 * w))
    # ---- Facet F: CMO overbought regime flag distance, |CMO|-70 ----
    for w in WINDOWS:
        f.setdefault('cmo_ext', []).append(_cmo(_px(df, w), w).abs() - 70.0)
    # ---- Facet G: VI slope/delta ----
    for w in WINDOWS:
        f.setdefault('vi_delta', []).append(_vi(_px(df, 2 * w), w, 2 * w).diff())
    # ---- Facet H: CMO * VI interaction (momentum scaled by vol regime) ----
    for w in WINDOWS:
        cmo = _cmo(_px(df, w), w)
        vi = _vi(_px(df, 2 * w), w, 2 * w)
        f.setdefault('cmo_x_vi', []).append(cmo * vi)
    # ---- Facet I: VIDYA slope (trend of adaptive MA) ----
    for w in WINDOWS:
        f.setdefault('vidya_slope', []).append(_vidya(_px(df, w), w).diff(5) / 5.0)
    # ---- Facet J: CMO rolling mean (smoothed momentum) ----
    for w in WINDOWS:
        f.setdefault('cmo_smooth', []).append(_cmo(_px(df, w), w).rolling(5).mean())
    # ---- Facet K: CMO sign-streak magnitude (abs run length) ----
    for w in WINDOWS:
        f.setdefault('cmo_streak_abs', []).append(_sign_streak(_cmo(_px(df, w), w)).abs())
    # ---- Facet L: VI percentile rank over 63 ----
    for w in WINDOWS:
        vi = _vi(_px(df, 2 * w), w, 2 * w)
        f.setdefault('vi_rank', []).append(
            vi.rolling(63).apply(lambda x: (x[-1] > x).mean(), raw=True))
    # ---- Facet M: CMO threshold cross distance to zero-line (raw level / range) ----
    for w in WINDOWS:
        cmo = _cmo(_px(df, w), w)
        f.setdefault('cmo_norm', []).append(cmo / 100.0)
    # ---- Facet N: VIDYA-to-price gap z-score ----
    for w in WINDOWS:
        px = _px(df, w)
        gap = px - _vidya(px, w)
        f.setdefault('gap_z', []).append(_z(gap, 21))
    # ---- Facet O: |CMO| change (momentum-strength velocity) ----
    for w in WINDOWS:
        f.setdefault('cmo_abs_delta', []).append(_cmo(_px(df, w), w).abs().diff())

    order = ['cmo_spread', 'cmo_accel', 'cmo_abs_z', 'vidya_vi', 'px_vidya_vi',
             'cmo_ext', 'vi_delta', 'cmo_x_vi', 'vidya_slope', 'cmo_smooth',
             'cmo_streak_abs', 'vi_rank', 'cmo_norm', 'gap_z', 'cmo_abs_delta']
    series_list = []
    for facet in order:
        series_list.extend(f[facet])

    for j, i in enumerate(range(76, 151)):
        features[f'f10_chande_volatility_{i:03d}'] = series_list[j]
    return pd.DataFrame(features)
