# Real indicator: rolling skewness of returns and its DRIFT.
# Core = rolling skewness of closeadj log-returns over a window; "drift" = slope/Delta
# of skewness over time. 150 distinct variants across windows (21/63/126/252) and facets.
# This file produces f12_skewness_drift_001..075.
import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------- helpers
def _logret(s):
    return np.log(s / s.shift(1))

def _skew(s, w):
    # rolling Fisher skewness (pandas uses bias-corrected sample skewness)
    return s.rolling(w).skew()

def _skew_masked(s, w):
    # rolling skew over a masked series (NaNs from .where); require >=1/3 of the
    # window to be present so a one-sided distribution still yields values.
    return s.rolling(w, min_periods=max(8, w // 3)).skew()

def _slope(s, k):
    # OLS slope of s over the last k bars (drift), per-bar units
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

def _safe(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f12_skewness_drift_base_001_075(df):
    features = {}

    closeadj = df['closeadj']
    open_ = df['open']
    close = df['close']
    volume = df['volume']

    ret = _logret(closeadj)
    absret = ret.abs()
    sqret = ret ** 2

    # overnight (gap) and intraday returns from open/close
    overnight = _safe(np.log(open_ / close.shift(1)))
    intraday = _safe(np.log(close / open_))

    windows = [21, 63, 126, 252]

    # pre-compute the skewness level per window (re-used by many facets)
    skew_lvl = {w: _skew(ret, w) for w in windows}

    feats = []  # list of Series in order

    # ---- Facet A: skewness LEVEL across windows (4)
    for w in windows:
        feats.append(_safe(skew_lvl[w]))

    # ---- Facet B: skewness DRIFT = OLS slope of skewness over k bars (4 windows x 2 k) (8)
    for w in windows:
        for k in (10, 21):
            feats.append(_safe(_slope(skew_lvl[w], k)))

    # ---- Facet C: skewness Delta (change over k bars) (4 windows x 2 k) (8)
    for w in windows:
        for k in (5, 21):
            feats.append(_safe(skew_lvl[w] - skew_lvl[w].shift(k)))

    # ---- Facet D: signed skew = sign * magnitude (already signed) -> emphasize via sign*sqrt|.| (4)
    for w in windows:
        sk = skew_lvl[w]
        feats.append(_safe(np.sign(sk) * np.sqrt(sk.abs())))

    # ---- Facet E: skew z-score (skew normalised vs its own history) (4 windows x 2 z-win) (8)
    for w in windows:
        for zw in (63, 126):
            feats.append(_safe(_z(skew_lvl[w], zw)))

    # ---- Facet F: skew of |returns| and squared returns (4 windows x 2) (8)
    for w in windows:
        feats.append(_safe(_skew(absret, w)))
        feats.append(_safe(_skew(sqret, w)))

    # ---- Facet G: downside-vs-upside skew (skew computed from neg vs pos returns) (4 windows x 2) (8)
    neg = ret.where(ret < 0)
    pos = ret.where(ret > 0)
    for w in windows:
        feats.append(_safe(_skew_masked(neg, w)))
        feats.append(_safe(_skew_masked(pos, w)))

    # ---- Facet H: skew percentile rank over a lookback (4 windows x 2 ranks) (8)
    for w in windows:
        for rw in (126, 252):
            feats.append(_safe(_pctrank(skew_lvl[w], rw)))

    # ---- Facet I: skew regime distance vs 0 (abs distance and squared distance) (4 windows x 2) (8)
    for w in windows:
        sk = skew_lvl[w]
        feats.append(_safe(sk.abs()))
        feats.append(_safe(sk ** 2))

    # ---- Facet J: short-vs-long skew spread & ratio (pairs) (spread x3 + ratio x4 = 7)
    feats.append(_safe(skew_lvl[21] - skew_lvl[63]))
    feats.append(_safe(skew_lvl[63] - skew_lvl[126]))
    feats.append(_safe(skew_lvl[126] - skew_lvl[252]))
    feats.append(_safe(skew_lvl[21] / skew_lvl[63]))
    feats.append(_safe(skew_lvl[21] / skew_lvl[126]))
    feats.append(_safe(skew_lvl[63] / skew_lvl[126]))
    feats.append(_safe(skew_lvl[63] / skew_lvl[252]))

    # That is 4+8+8+4+8+8+8+8+8+7 = 71. Need 75 -> add 4 more distinct facets.

    # ---- Facet K: skew of overnight vs intraday returns (overnight skew) (2 windows) (2)
    feats.append(_safe(_skew(overnight, 63)))
    feats.append(_safe(_skew(overnight, 126)))

    # ---- Facet L: intraday skew (2 windows) (2)
    feats.append(_safe(_skew(intraday, 63)))
    feats.append(_safe(_skew(intraday, 126)))

    assert len(feats) == 75, f"file1 facet count {len(feats)}"

    for i, s in enumerate(feats, start=1):
        features[f'f12_skewness_drift_{i:03d}'] = s

    return pd.DataFrame(features, index=df.index)
