# Real indicator: Chaikin Money Flow (CMF) & Chaikin Oscillator
# MFM = ((close-low)-(high-close))/(high-low);  MFV = MFM*volume
# CMF(n) = sum(MFV,n)/sum(volume,n)
# ADL = cumsum(MFV);  Chaikin Osc = EMA(3,ADL)-EMA(10,ADL)
import numpy as np
import pandas as pd

WINDOWS = [10, 20, 21, 63, 126]


def _mfm(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    return ((close - low) - (high - close)) / rng


def _mfv(high, low, close, volume):
    return _mfm(high, low, close) * volume


def _cmf(mfv, volume, n):
    return mfv.rolling(n).sum() / volume.rolling(n).sum().replace(0.0, np.nan)


def _adl(mfv):
    return mfv.cumsum()


def _ema(s, span):
    return s.ewm(span=span, adjust=False).mean()


def _chaikin_osc(adl):
    return _ema(adl, 3) - _ema(adl, 10)


def _z(s, n):
    return (s - s.rolling(n).mean()) / s.rolling(n).std().replace(0.0, np.nan)


def _slope(s, n):
    return (s - s.shift(n)) / float(n)


def _roc(s, n):
    return (s / s.shift(n).replace(0.0, np.nan)) - 1.0


def _sign_streak(s):
    sign = np.sign(s.fillna(0.0))
    grp = (sign != sign.shift(1)).cumsum()
    streak = sign.groupby(grp).cumcount() + 1
    return (streak * sign).where(s.notna())


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def get_f22_chaikin_money_flow_base_001_075(df):
    high = df['high']
    low = df['low']
    close = df['close']
    closeadj = df['closeadj']
    volume = df['volume']

    mfv = _mfv(high, low, close, volume)
    adl = _adl(mfv)
    osc = _chaikin_osc(adl)
    dollar_vol = closeadj * volume

    features = {}
    idx = 1

    def put(s):
        nonlocal idx
        features[f'f22_chaikin_money_flow_{idx:03d}'] = _clean(s)
        idx += 1

    # Facet 1: CMF level (5 windows)
    cmf = {n: _cmf(mfv, volume, n) for n in WINDOWS}
    for n in WINDOWS:
        put(cmf[n])

    # Facet 2: Chaikin oscillator level + normalized by rolling vol (5 windows)
    for n in WINDOWS:
        put(osc / volume.rolling(n).mean().replace(0.0, np.nan))

    # Facet 3: ADL slope (5 windows)
    for n in WINDOWS:
        put(_slope(adl, n))

    # Facet 4: CMF z-score (5 windows)
    for n in WINDOWS:
        put(_z(cmf[n], n))

    # Facet 5: CMF slope / delta (5 windows)
    for n in WINDOWS:
        put(_slope(cmf[n], max(2, n // 3)))

    # Facet 6: CMF sign streak (5 windows)
    for n in WINDOWS:
        put(_sign_streak(cmf[n]))

    # Facet 7: ADL-vs-price divergence (>21d uses closeadj) (5 windows)
    for n in WINDOWS:
        price = closeadj if n > 21 else close
        put(_roc(adl, n) - _roc(price, n))

    # Facet 8: CMF overbought/oversold threshold distance (5 windows)
    for n in WINDOWS:
        c = cmf[n]
        put(np.maximum(c - 0.05, 0.0) + np.minimum(c + 0.05, 0.0))

    # Facet 9: CMF x dollar-volume (5 windows)
    for n in WINDOWS:
        put(cmf[n] * dollar_vol.rolling(n).mean())

    # Facet 10: short-vs-long CMF spread (5 windows, vs longest 126;
    # the 126-vs-126 slot instead measures 126 vs its own EMA to stay informative)
    for n in WINDOWS:
        if n == 126:
            put(cmf[126] - _ema(cmf[126], 63))
        else:
            put(cmf[n] - cmf[126])

    # Facet 11: ADL ROC (5 windows)
    for n in WINDOWS:
        put(_roc(adl, n))

    # Facet 12: Chaikin osc z-score (5 windows)
    for n in WINDOWS:
        put(_z(osc, n))

    # Facet 13: CMF percentile rank (5 windows)
    for n in WINDOWS:
        put(cmf[n].rolling(n).rank(pct=True))

    # Facet 14: CMF dispersion / rolling std (5 windows)
    for n in WINDOWS:
        put(cmf[n].rolling(n).std())

    # Facet 15: osc slope (5 windows)
    for n in WINDOWS:
        put(_slope(osc, max(2, n // 3)))

    return pd.DataFrame(features)
