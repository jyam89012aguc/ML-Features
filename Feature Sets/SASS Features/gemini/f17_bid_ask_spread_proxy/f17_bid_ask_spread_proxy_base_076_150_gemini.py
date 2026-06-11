# Bid-ask spread proxies from OHLC (base 076..150)
# Real indicator math (NOT an SMA placeholder). Same estimator cores as 001..075:
#   Corwin-Schultz high-low spread, Roll serial-covariance spread,
#   Abdi-Ranaldo close-high-low spread, hi-lo/close range proxy.
# This file emphasises the complementary facets: percentile ranks, dispersion /
#   vol-of-spread, regime/threshold distance, dollar-volume interactions on Roll &
#   Abdi-Ranaldo, short-vs-long ratios, z-scores and ROCs across the remaining windows.
import numpy as np
import pandas as pd

_SQ2 = np.sqrt(2.0)
_DEN = 3.0 - 2.0 * _SQ2


def _logs(df):
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    c = df['close'].astype(float)
    out = {}
    out['lc'] = np.log(c)
    hl = np.log(h / l)
    out['hl2'] = (hl * hl)
    h2 = h.rolling(2).max()
    l2 = l.rolling(2).min()
    g = np.log(h2 / l2)
    out['gamma'] = (g * g)
    out['dvol'] = (df['closeadj'].astype(float) * df['volume'].astype(float))
    out['dp'] = np.log(c) - np.log(c.shift(1))
    out['eta'] = 0.5 * (np.log(h) + np.log(l))
    for k in out:
        out[k] = out[k].replace([np.inf, -np.inf], np.nan)
    return out


def _corwin_schultz(lg, n):
    # Canonical CS: per-day spread, clip negatives to zero, then average over window.
    beta = lg['hl2'] + lg['hl2'].shift(1)
    gamma = lg['gamma']
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / _DEN - np.sqrt(gamma / _DEN)
    alpha = alpha.replace([np.inf, -np.inf], np.nan)
    s_day = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    s_day = s_day.clip(lower=0.0)
    return s_day.rolling(n).mean()


def _roll(lg, n):
    dp = lg['dp']
    cov = dp.rolling(n).cov(dp.shift(1))
    s = 2.0 * np.sqrt((-cov).clip(lower=0.0))
    return s.replace([np.inf, -np.inf], np.nan)


def _abdi_ranaldo(lg, n):
    c = lg['lc']
    eta = lg['eta']
    term = (c - eta) * (c - eta.shift(-1))
    m = term.rolling(n).mean()
    s = 2.0 * np.sqrt(m.clip(lower=0.0))
    return s.replace([np.inf, -np.inf], np.nan)


def _hilo_close(df, n):
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    c = df['close'].astype(float)
    proxy = ((h - l) / c).replace([np.inf, -np.inf], np.nan)
    return proxy.rolling(n).mean()


# ---------- generic facet transforms ----------
def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return (s - s.shift(w)).replace([np.inf, -np.inf], np.nan)


def _roc(s, w):
    return (s / s.shift(w) - 1.0).replace([np.inf, -np.inf], np.nan)


def _ratio(a, b):
    return (a / b).replace([np.inf, -np.inf], np.nan)


def _pctrank(s, w):
    return s.rolling(w).apply(
        lambda x: (x[-1] >= x).mean() if np.isfinite(x[-1]) else np.nan, raw=True)


def _dispersion(s, w):
    return s.rolling(w).std()


def _regime_dist(s, w):
    med = s.rolling(w).median()
    sd = s.rolling(w).std()
    return ((s - med) / sd).replace([np.inf, -np.inf], np.nan)


def get_f17_bid_ask_spread_proxy_base_076_150(df):
    lg = _logs(df)
    f = {}
    W = [21, 63, 126, 252]

    cs = {w: _corwin_schultz(lg, w) for w in W}
    rl = {w: _roll(lg, w) for w in W}
    ar = {w: _abdi_ranaldo(lg, w) for w in W}
    hc = {w: _hilo_close(df, w) for w in W}
    dvol = {w: lg['dvol'].rolling(w).mean() for w in W}

    feats = []

    # 1) Roll spread x dollar-volume interaction (4)
    for w in W:
        feats.append((rl[w] * dvol[w]).replace([np.inf, -np.inf], np.nan))
    # 2) Abdi-Ranaldo spread x dollar-volume interaction (4)
    for w in W:
        feats.append((ar[w] * dvol[w]).replace([np.inf, -np.inf], np.nan))
    # 3) hi-lo/close x dollar-volume interaction (4)
    for w in W:
        feats.append((hc[w] * dvol[w]).replace([np.inf, -np.inf], np.nan))
    # 12

    # 4) Abdi-Ranaldo term structure: spread normalized by its own long-window level (4)
    #    (short-vs-long illiquidity ratio; distinct from any z-score facet)
    for w in W:
        feats.append(_ratio(ar[w], ar[252].rolling(63).mean()))
    # 5) Roll regime distance (4)
    for w in W:
        feats.append(_regime_dist(rl[w], 252))
    # 6) Abdi-Ranaldo regime distance (4)
    for w in W:
        feats.append(_regime_dist(ar[w], 252))
    # 24

    # 7) Roll percentile rank (4)
    for w in W:
        feats.append(_pctrank(rl[w], 252))
    # 8) Abdi-Ranaldo percentile rank (4)
    for w in W:
        feats.append(_pctrank(ar[w], 252))
    # 9) hi-lo/close percentile rank (4)
    for w in W:
        feats.append(_pctrank(hc[w], 252))
    # 36

    # 10) CS dispersion / vol-of-spread (4)
    for w in W:
        feats.append(_dispersion(cs[w], w))
    # 11) Roll dispersion (4)
    for w in W:
        feats.append(_dispersion(rl[w], w))
    # 12) hi-lo/close dispersion (4)
    for w in W:
        feats.append(_dispersion(hc[w], w))
    # 48

    # 13) Roll ROC (4)
    for w in W:
        feats.append(_roc(rl[w], max(2, w // 3)))
    # 14) hi-lo/close ROC (4)
    for w in W:
        feats.append(_roc(hc[w], max(2, w // 3)))
    # 15) Abdi-Ranaldo slope/delta (4)
    for w in W:
        feats.append(_slope(ar[w], max(2, w // 3)))
    # 60

    # 16) short-vs-long Roll spread ratio (4)
    feats.append(_ratio(rl[21], rl[63]))
    feats.append(_ratio(rl[21], rl[126]))
    feats.append(_ratio(rl[63], rl[252]))
    feats.append(_ratio(rl[21], rl[252]))
    # 64

    # 17) short-vs-long Abdi-Ranaldo spread spread (difference) (4)
    feats.append((ar[21] - ar[63]).replace([np.inf, -np.inf], np.nan))
    feats.append((ar[21] - ar[126]).replace([np.inf, -np.inf], np.nan))
    feats.append((ar[63] - ar[252]).replace([np.inf, -np.inf], np.nan))
    feats.append((hc[21] - hc[252]).replace([np.inf, -np.inf], np.nan))
    # 68

    # 18) short-vs-long hi-lo/close ratio (4)
    feats.append(_ratio(hc[21], hc[63]))
    feats.append(_ratio(hc[21], hc[126]))
    feats.append(_ratio(hc[63], hc[252]))
    feats.append(_ratio(hc[21], hc[252]))
    # 72

    # 19) cross-estimator agreement: Roll vs Abdi-Ranaldo, hilo vs AR, CS vs hilo (3)
    feats.append(_ratio(rl[126], ar[126]))
    feats.append(_ratio(hc[126], ar[126]))
    feats.append(_ratio(cs[126], hc[126]))
    # 75

    assert len(feats) == 75, len(feats)
    for i, s in enumerate(feats, start=76):
        f[f'f17_bid_ask_spread_proxy_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
