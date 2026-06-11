# Real indicator: rolling skewness of returns and its DRIFT.
# Core = rolling skewness of closeadj log-returns over a window; "drift" = slope/Delta
# of skewness over time. 150 distinct variants across windows (21/63/126/252) and facets.
# This file produces f12_skewness_drift_076..150 (continuation of the facet set).
import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------- helpers
def _logret(s):
    return np.log(s / s.shift(1))

def _skew(s, w):
    return s.rolling(w).skew()

def _skew_masked(s, w):
    return s.rolling(w, min_periods=max(8, w // 3)).skew()

def _slope(s, k):
    idx = np.arange(k, dtype=float)
    xm = idx.mean()
    den = ((idx - xm) ** 2).sum()
    def _f(arr):
        y = arr
        ym = y.mean()
        return ((idx - xm) * (y - ym)).sum() / den
    return s.rolling(k).apply(_f, raw=True)

def _z(s, w):
    m = s.rolling(w).mean()
    sd = s.rolling(w).std()
    return ((s - m) / sd).replace([np.inf, -np.inf], np.nan)

def _pctrank(s, w):
    return s.rolling(w).apply(lambda a: (a[-1] >= a).mean(), raw=True)

def _rollcorr(a, b, w):
    return a.rolling(w).corr(b)

def _coskew(a, b, w):
    # standardized co-skewness:  E[ za^2 * zb ] using rolling moments
    ma = a.rolling(w).mean(); sa = a.rolling(w).std()
    mb = b.rolling(w).mean(); sb = b.rolling(w).std()
    za = (a - ma) / sa
    zb = (b - mb) / sb
    return ((za ** 2) * zb).rolling(w).mean().replace([np.inf, -np.inf], np.nan)

def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f12_skewness_drift_base_076_150(df):
    features = {}

    closeadj = df['closeadj']
    open_ = df['open']
    close = df['close']
    volume = df['volume']

    ret = _logret(closeadj)
    absret = ret.abs()

    overnight = _safe(np.log(open_ / close.shift(1)))
    intraday = _safe(np.log(close / open_))

    windows = [21, 63, 126, 252]
    skew_lvl = {w: _skew(ret, w) for w in windows}

    feats = []

    # ---- Facet M: skewness DRIFT (slope) over longer k, plus acceleration of skew (4 win x 2) (8)
    for w in windows:
        feats.append(_safe(_slope(skew_lvl[w], 42)))           # slow drift
        sl = _slope(skew_lvl[w], 21)
        feats.append(_safe(sl - sl.shift(21)))                 # drift acceleration

    # ---- Facet N: skew Delta normalised by skew dispersion (drift z) (4 win x 2 zwin) (8)
    for w in windows:
        d = skew_lvl[w] - skew_lvl[w].shift(21)
        feats.append(_safe(_z(d, 63)))
        feats.append(_safe(_z(d, 126)))

    # ---- Facet O: short-vs-long skew spread z-scored & ranked (6)
    sp1 = skew_lvl[21] - skew_lvl[126]
    sp2 = skew_lvl[63] - skew_lvl[252]
    feats.append(_safe(_z(sp1, 126)))
    feats.append(_safe(_z(sp2, 126)))
    feats.append(_safe(_pctrank(sp1, 252)))
    feats.append(_safe(_pctrank(sp2, 252)))
    feats.append(_safe(sp1))
    feats.append(_safe(sp2))

    # ---- Facet P: downside-minus-upside skew asymmetry (4 windows) (4)
    neg = ret.where(ret < 0)
    pos = ret.where(ret > 0)
    for w in windows:
        feats.append(_safe(_skew_masked(neg, w) - _skew_masked(pos, w)))

    # ---- Facet Q: skew regime distance vs 0 with sign-persistence (4 win x 2) (8)
    for w in windows:
        sk = skew_lvl[w]
        feats.append(_safe(np.sign(sk).rolling(21).mean()))    # sign persistence of skew
        feats.append(_safe(sk - sk.rolling(63).mean()))        # distance from own regime mean

    # ---- Facet R: skew of overnight vs intraday spread (4)
    feats.append(_safe(_skew(overnight, 63) - _skew(intraday, 63)))
    feats.append(_safe(_skew(overnight, 126) - _skew(intraday, 126)))
    feats.append(_safe(_skew(overnight, 252)))
    feats.append(_safe(_skew(intraday, 252)))

    # ---- Facet S: coskewness of returns with volume (4 win x 2 forms) (8)
    vchg = _safe(volume.pct_change())
    for w in windows:
        feats.append(_safe(_coskew(ret, volume, w)))           # E[zret^2 * zvol]
        feats.append(_safe(_coskew(ret, vchg, w)))             # vs volume change

    # ---- Facet T: coskewness drift & corr of skew with volume level (4)
    for w in (63, 126):
        cs = _coskew(ret, volume, w)
        feats.append(_safe(cs - cs.shift(21)))                 # coskew drift
        feats.append(_safe(_rollcorr(skew_lvl[w], volume, w))) # skew-vs-volume corr

    # Running total so far: 8+8+6+4+8+4+8+4 = 50. Need 75 -> 25 more.

    # ---- Facet U: skew z-score additional windows (4 win x 2) (8)
    for w in windows:
        feats.append(_safe(_z(skew_lvl[w], 252)))
        feats.append(_safe(_z(skew_lvl[w], 42)))

    # ---- Facet V: skew percentile rank additional lookback (4 win) (4)
    for w in windows:
        feats.append(_safe(_pctrank(skew_lvl[w], 63)))

    # ---- Facet W: signed-skew * magnitude variants (4 win) (4)
    for w in windows:
        sk = skew_lvl[w]
        feats.append(_safe(np.sign(sk) * (sk ** 2)))

    # ---- Facet X: skew of |returns| drift and squared-return skew z (4 win) (4)
    for w in windows:
        feats.append(_safe(_skew(absret, w) - _skew(absret, w).shift(21)))

    # ---- Facet Y: skew Delta over multiple horizons for the remaining slots (5)
    feats.append(_safe(skew_lvl[21] - skew_lvl[21].shift(10)))
    feats.append(_safe(skew_lvl[63] - skew_lvl[63].shift(10)))
    feats.append(_safe(skew_lvl[126] - skew_lvl[126].shift(10)))
    feats.append(_safe(skew_lvl[252] - skew_lvl[252].shift(10)))
    feats.append(_safe(_slope(skew_lvl[252], 63)))

    assert len(feats) == 75, f"file2 facet count {len(feats)}"

    for j, s in enumerate(feats):
        i = 76 + j
        features[f'f12_skewness_drift_{i:03d}'] = s

    return pd.DataFrame(features, index=df.index)
