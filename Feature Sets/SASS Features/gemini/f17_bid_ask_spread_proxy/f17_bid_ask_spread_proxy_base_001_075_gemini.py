# Bid-ask spread proxies from OHLC (base 001..075)
# Real indicator math (NOT an SMA placeholder). Spread estimators:
#   Corwin-Schultz (2012): from 1- & 2-day high-low log-ranges
#       beta  = E[ (ln(H_t/L_t))^2 + (ln(H_{t-1}/L_{t-1}))^2 ]
#       gamma = ( ln(H2/L2) )^2      where H2/L2 = 2-day high/low
#       alpha = (sqrt(2*beta)-sqrt(beta))/(3-2*sqrt2) - sqrt(gamma/(3-2*sqrt2))
#       S     = 2*(exp(alpha)-1)/(1+exp(alpha))   (negative -> 0)
#   Roll (1984): S = 2*sqrt(-cov(dp_t, dp_{t-1})) when cov<0 else 0
#   Abdi-Ranaldo (2017) CHL: S = 2*sqrt(max( E[(c-eta)(c-eta_next)], 0 ))
#       with eta = (ln H + ln L)/2 midrange, c = ln close
#   Hi-lo/close proxy: (H-L)/C  range-based liquidity proxy
# Facets: CS level, Roll, Abdi-Ranaldo, hi-lo/close, z-score, slope/delta,
#   illiquidity-regime distance, spread x dollar-volume, short-vs-long, percentile rank.
import numpy as np
import pandas as pd

_SQ2 = np.sqrt(2.0)
_DEN = 3.0 - 2.0 * _SQ2  # 3 - 2*sqrt(2)


# ---------- log building blocks (raw OHLC for the spread math) ----------
def _logs(df):
    h = df['high'].astype(float)
    l = df['low'].astype(float)
    c = df['close'].astype(float)
    out = {}
    out['lh'] = np.log(h)
    out['ll'] = np.log(l)
    out['lc'] = np.log(c)
    # single-day high-low log range squared (beta building block)
    hl = np.log(h / l)
    out['hl2'] = (hl * hl)
    # 2-day high/low (rolling max high / rolling min low over 2 days)
    h2 = h.rolling(2).max()
    l2 = l.rolling(2).min()
    g = np.log(h2 / l2)
    out['gamma'] = (g * g)
    # dollar volume uses closeadj * volume
    out['dvol'] = (df['closeadj'].astype(float) * df['volume'].astype(float))
    # close log-price change (for Roll)
    out['dp'] = np.log(c) - np.log(c.shift(1))
    # Abdi-Ranaldo midrange eta = (lnH + lnL)/2
    out['eta'] = 0.5 * (np.log(h) + np.log(l))
    for k in out:
        out[k] = out[k].replace([np.inf, -np.inf], np.nan)
    return out


# ---------- spread estimator cores ----------
def _corwin_schultz(lg, n):
    # Canonical CS: per-day spread from beta(=hl2_t + hl2_{t-1}) and gamma(=2-day range^2),
    # clip negative daily spread to zero, then average over the n-day window.
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
    # CHL: E[(c_t - eta_t)(c_t - eta_{t+1})]; approximate with eta_{t+1}=eta.shift(-1)
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


def _regime_dist(s, w):
    # distance (in std) of current spread above its trailing median illiquidity regime
    med = s.rolling(w).median()
    sd = s.rolling(w).std()
    return ((s - med) / sd).replace([np.inf, -np.inf], np.nan)


def get_f17_bid_ask_spread_proxy_base_001_075(df):
    lg = _logs(df)
    f = {}
    W = [21, 63, 126, 252]

    cs = {w: _corwin_schultz(lg, w) for w in W}
    rl = {w: _roll(lg, w) for w in W}
    ar = {w: _abdi_ranaldo(lg, w) for w in W}
    hc = {w: _hilo_close(df, w) for w in W}
    dvol = {w: lg['dvol'].rolling(w).mean() for w in W}

    feats = []

    # 1) Corwin-Schultz spread level (4)
    for w in W:
        feats.append(cs[w])
    # 2) Roll spread level (4)
    for w in W:
        feats.append(rl[w])
    # 3) Abdi-Ranaldo spread level (4)
    for w in W:
        feats.append(ar[w])
    # 4) hi-lo/close proxy level (4)
    for w in W:
        feats.append(hc[w])
    # 16

    # 5) CS z-score (4)
    for w in W:
        feats.append(_z(cs[w], max(w, 63)))
    # 6) Roll z-score (4)
    for w in W:
        feats.append(_z(rl[w], max(w, 63)))
    # 7) Abdi-Ranaldo z-score (4)
    for w in W:
        feats.append(_z(ar[w], max(w, 63)))
    # 8) hi-lo/close z-score (4)
    for w in W:
        feats.append(_z(hc[w], max(w, 63)))
    # 32

    # 9) CS slope/delta (4)
    for w in W:
        feats.append(_slope(cs[w], max(2, w // 3)))
    # 10) Roll slope/delta (4)
    for w in W:
        feats.append(_slope(rl[w], max(2, w // 3)))
    # 11) hi-lo/close slope (4)
    for w in W:
        feats.append(_slope(hc[w], max(2, w // 3)))
    # 44

    # 12) CS ROC (4)
    for w in W:
        feats.append(_roc(cs[w], max(2, w // 3)))
    # 13) Abdi-Ranaldo ROC (4)
    for w in W:
        feats.append(_roc(ar[w], max(2, w // 3)))
    # 52

    # 14) illiquidity regime distance (CS) (4)
    for w in W:
        feats.append(_regime_dist(cs[w], 252))
    # 15) illiquidity regime distance (hi-lo/close) (4)
    for w in W:
        feats.append(_regime_dist(hc[w], 252))
    # 60

    # 16) spread x dollar-volume interaction (CS * dvol) (4)
    for w in W:
        feats.append((cs[w] * dvol[w]).replace([np.inf, -np.inf], np.nan))
    # 64

    # 17) short-vs-long CS spread spread (difference) (4)
    feats.append((cs[21] - cs[63]).replace([np.inf, -np.inf], np.nan))
    feats.append((cs[21] - cs[126]).replace([np.inf, -np.inf], np.nan))
    feats.append((cs[63] - cs[252]).replace([np.inf, -np.inf], np.nan))
    feats.append((cs[21] - cs[252]).replace([np.inf, -np.inf], np.nan))
    # 68

    # 18) percentile rank (CS) (4)
    for w in W:
        feats.append(_pctrank(cs[w], 252))
    # 72

    # 19) cross-estimator ratios (Roll vs CS, AR vs CS, hilo vs CS) (3)
    feats.append(_ratio(rl[63], cs[63]))
    feats.append(_ratio(ar[63], cs[63]))
    feats.append(_ratio(hc[63], cs[63]))
    # 75

    assert len(feats) == 75, len(feats)
    for i, s in enumerate(feats, start=1):
        f[f'f17_bid_ask_spread_proxy_{i:03d}'] = s
    return pd.DataFrame(f, index=df.index)
