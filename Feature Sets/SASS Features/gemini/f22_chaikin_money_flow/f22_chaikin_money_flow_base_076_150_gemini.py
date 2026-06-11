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


def get_f22_chaikin_money_flow_base_076_150(df):
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
    idx = 76

    def put(s):
        nonlocal idx
        features[f'f22_chaikin_money_flow_{idx:03d}'] = _clean(s)
        idx += 1

    cmf = {n: _cmf(mfv, volume, n) for n in WINDOWS}

    # Facet 1: smoothed CMF (EMA) level (5 windows)
    for n in WINDOWS:
        put(_ema(cmf[n], max(2, n // 2)))

    # Facet 2: ADL z-score (5 windows)
    for n in WINDOWS:
        put(_z(adl, n))

    # Facet 3: CMF delta over 1 step vs window mean (acceleration) (5 windows)
    for n in WINDOWS:
        put(cmf[n] - cmf[n].rolling(n).mean())

    # Facet 4: osc / dollar-volume scaled (5 windows)
    for n in WINDOWS:
        put(osc / dollar_vol.rolling(n).mean().replace(0.0, np.nan))

    # Facet 5: CMF overbought distance (positive threshold 0.10) (5 windows)
    for n in WINDOWS:
        put(cmf[n] - 0.10)

    # Facet 6: CMF oversold distance (negative threshold -0.10) (5 windows)
    for n in WINDOWS:
        put(cmf[n] + 0.10)

    # Facet 7: ADL-vs-price divergence using slope difference (>21d closeadj) (5 windows)
    for n in WINDOWS:
        price = closeadj if n > 21 else close
        put(_slope(_z(adl, n), n) - _slope(_z(price, n), n))

    # Facet 8: short-vs-long CMF spread (vs shortest 10) (5 windows;
    # the 10-vs-10 slot instead measures 10 vs its own EMA to stay informative)
    for n in WINDOWS:
        if n == 10:
            put(cmf[10] - _ema(cmf[10], 5))
        else:
            put(cmf[n] - cmf[10])

    # Facet 9: ADL ROC of ROC (acceleration) (5 windows)
    for n in WINDOWS:
        put(_roc(adl, n) - _roc(adl, n).shift(max(2, n // 3)))

    # Facet 10: CMF x raw volume mean (money-flow magnitude) (5 windows)
    for n in WINDOWS:
        put(cmf[n] * volume.rolling(n).mean())

    # Facet 11: osc sign streak (5 windows)
    for n in WINDOWS:
        put(_sign_streak(osc).rolling(n).mean())

    # Facet 12: CMF range-normalized (CMF over rolling abs max) (5 windows)
    for n in WINDOWS:
        denom = cmf[n].abs().rolling(n).max().replace(0.0, np.nan)
        put(cmf[n] / denom)

    # Facet 13: MFM rolling mean (money-flow multiplier bias) (5 windows)
    mfm = _mfm(high, low, close)
    for n in WINDOWS:
        put(mfm.rolling(n).mean())

    # Facet 14: CMF ROC (5 windows)
    for n in WINDOWS:
        put(_roc(cmf[n], max(2, n // 3)))

    # Facet 15: ADL detrended (ADL minus its rolling mean) divergence vs price (5 windows)
    for n in WINDOWS:
        price = closeadj if n > 21 else close
        adl_dt = adl - adl.rolling(n).mean()
        price_dt = price - price.rolling(n).mean()
        put(np.sign(adl_dt) - np.sign(price_dt))

    return pd.DataFrame(features)
