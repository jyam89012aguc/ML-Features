import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _ma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _ema(close, span):
    return close.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _pdist(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(close.replace(0, np.nan) / ma.replace(0, np.nan))


def _emadist(close, span):
    ema = close.ewm(span=span, min_periods=max(1, span // 2)).mean()
    return np.log(close.replace(0, np.nan) / ema.replace(0, np.nan))


def _maratio(close, ws, wl):
    ms = close.rolling(ws, min_periods=max(1, ws // 2)).mean()
    ml = close.rolling(wl, min_periods=max(1, wl // 2)).mean()
    return np.log(ms.replace(0, np.nan) / ml.replace(0, np.nan))


def _bandpos(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    return (close - lower) / (upper - lower).replace(0, np.nan)


def _abovefrac(close, w, ow):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(ow, min_periods=max(1, ow // 2)).mean()


def _chanmid(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return np.log(close.replace(0, np.nan) / mid.replace(0, np.nan))


def _stackmag(close):
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    m504 = close.rolling(504, min_periods=252).mean()
    g1 = np.tanh(80.0 * np.log(m21.replace(0, np.nan) / m63.replace(0, np.nan)))
    g2 = np.tanh(80.0 * np.log(m63.replace(0, np.nan) / m126.replace(0, np.nan)))
    g3 = np.tanh(80.0 * np.log(m126.replace(0, np.nan) / m252.replace(0, np.nan)))
    g4 = np.tanh(80.0 * np.log(m252.replace(0, np.nan) / m504.replace(0, np.nan)))
    return g1 + g2 + g3 + g4


def _diref(close, w):
    lr = np.log(close.replace(0, np.nan)).diff()
    net = lr.rolling(w, min_periods=max(1, w // 2)).sum().abs()
    gross = lr.abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return net / gross.replace(0, np.nan)


def _normstretch(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    return (close - ma) / sd.replace(0, np.nan)


def _meddist(close, w):
    med = close.rolling(w, min_periods=max(1, w // 2)).median()
    return np.log(close.replace(0, np.nan) / med.replace(0, np.nan))


def _macd(close, fast, slow):
    return (_ema(close, fast) - _ema(close, slow)) / close.replace(0, np.nan)


def f01ct_f01_cyclical_trend_structure_pdistA_21d_jerk_v001_signal(closeadj):
    base = _pdist(closeadj, 21)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistA_63d_jerk_v002_signal(closeadj):
    base = _pdist(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistA_126d_jerk_v003_signal(closeadj):
    base = _pdist(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistA_252d_jerk_v004_signal(closeadj):
    base = _pdist(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistA_504d_jerk_v005_signal(closeadj):
    base = _pdist(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzA_63d_jerk_v006_signal(closeadj):
    base = _z(_pdist(closeadj, 63), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzA_126d_jerk_v007_signal(closeadj):
    base = _z(_pdist(closeadj, 126), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzA_252d_jerk_v008_signal(closeadj):
    base = _z(_pdist(closeadj, 252), 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistA_21d_jerk_v009_signal(closeadj):
    base = _emadist(closeadj, 21)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistA_63d_jerk_v010_signal(closeadj):
    base = _emadist(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistA_126d_jerk_v011_signal(closeadj):
    base = _emadist(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistA_252d_jerk_v012_signal(closeadj):
    base = _emadist(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioA_63d_jerk_v013_signal(closeadj):
    base = _maratio(closeadj, 21, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioA_126d_jerk_v014_signal(closeadj):
    base = _maratio(closeadj, 63, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioA_252d_jerk_v015_signal(closeadj):
    base = _maratio(closeadj, 126, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioA_504d_jerk_v016_signal(closeadj):
    base = _maratio(closeadj, 252, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiolongA_252d_jerk_v017_signal(closeadj):
    base = _maratio(closeadj, 21, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emaratioA_252d_jerk_v018_signal(closeadj):
    base = np.log(_ema(closeadj, 63).replace(0, np.nan) / _ema(closeadj, 252).replace(0, np.nan))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposA_63d_jerk_v019_signal(closeadj):
    base = (_bandpos(closeadj, 63) - 0.5)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposA_126d_jerk_v020_signal(closeadj):
    base = (_bandpos(closeadj, 126) - 0.5)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposA_252d_jerk_v021_signal(closeadj):
    base = (_bandpos(closeadj, 252) - 0.5)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracA_63d_jerk_v022_signal(closeadj):
    base = _abovefrac(closeadj, 63, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracA_126d_jerk_v023_signal(closeadj):
    base = _abovefrac(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracA_252d_jerk_v024_signal(closeadj):
    base = _abovefrac(closeadj, 252, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracA_504d_jerk_v025_signal(closeadj):
    base = _abovefrac(closeadj, 504, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidA_252d_jerk_v026_signal(closeadj):
    base = _chanmid(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidA_504d_jerk_v027_signal(closeadj):
    base = _chanmid(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_stackmagA_252d_jerk_v028_signal(closeadj):
    base = _stackmag(closeadj)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfA_126d_jerk_v029_signal(closeadj):
    base = _diref(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfA_252d_jerk_v030_signal(closeadj):
    base = _diref(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrA_126d_jerk_v031_signal(closeadj):
    base = _normstretch(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrA_252d_jerk_v032_signal(closeadj):
    base = _normstretch(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistA_252d_jerk_v033_signal(closeadj):
    base = _meddist(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistA_504d_jerk_v034_signal(closeadj):
    base = _meddist(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdA_63d_jerk_v035_signal(closeadj):
    base = _macd(closeadj, 21, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdA_126d_jerk_v036_signal(closeadj):
    base = _macd(closeadj, 63, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdA_252d_jerk_v037_signal(closeadj):
    base = _macd(closeadj, 126, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhA_252d_jerk_v038_signal(closeadj):
    base = np.tanh(4.0 * _pdist(closeadj, 252))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhA_504d_jerk_v039_signal(closeadj):
    base = np.tanh(3.0 * _pdist(closeadj, 504))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistsqA_252d_jerk_v040_signal(closeadj):
    base = (np.sign(_pdist(closeadj, 252)) * (_pdist(closeadj, 252).abs() ** 0.5))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistcubeA_126d_jerk_v041_signal(closeadj):
    base = (_pdist(closeadj, 126) ** 3)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandpospowA_252d_jerk_v042_signal(closeadj):
    base = ((_bandpos(closeadj, 252) - 0.5) ** 3)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiotanhA_252d_jerk_v043_signal(closeadj):
    base = np.tanh(60.0 * _maratio(closeadj, 63, 252))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistexpA_252d_jerk_v044_signal(closeadj):
    base = (np.exp(_pdist(closeadj, 252)) - 1.0)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposA_504d_jerk_v045_signal(closeadj):
    base = (_bandpos(closeadj, 504) - 0.5)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrA_63d_jerk_v046_signal(closeadj):
    base = _normstretch(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistzA_126d_jerk_v047_signal(closeadj):
    base = _z(_emadist(closeadj, 126), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidA_126d_jerk_v048_signal(closeadj):
    base = _chanmid(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistzA_252d_jerk_v049_signal(closeadj):
    base = _z(_meddist(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiozA_252d_jerk_v050_signal(closeadj):
    base = _z(_maratio(closeadj, 63, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistB_21d_jerk_v051_signal(closeadj):
    base = _pdist(closeadj, 21)
    sl = base.diff(10) / float(10)
    j = sl.diff(10) / float(10)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistB_63d_jerk_v052_signal(closeadj):
    base = _pdist(closeadj, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistB_126d_jerk_v053_signal(closeadj):
    base = _pdist(closeadj, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistB_252d_jerk_v054_signal(closeadj):
    base = _pdist(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistB_504d_jerk_v055_signal(closeadj):
    base = _pdist(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzB_63d_jerk_v056_signal(closeadj):
    base = _z(_pdist(closeadj, 63), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzB_126d_jerk_v057_signal(closeadj):
    base = _z(_pdist(closeadj, 126), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzB_252d_jerk_v058_signal(closeadj):
    base = _z(_pdist(closeadj, 252), 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistB_21d_jerk_v059_signal(closeadj):
    base = _emadist(closeadj, 21)
    sl = base.diff(10) / float(10)
    j = sl.diff(10) / float(10)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistB_63d_jerk_v060_signal(closeadj):
    base = _emadist(closeadj, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistB_126d_jerk_v061_signal(closeadj):
    base = _emadist(closeadj, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistB_252d_jerk_v062_signal(closeadj):
    base = _emadist(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioB_63d_jerk_v063_signal(closeadj):
    base = _maratio(closeadj, 21, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioB_126d_jerk_v064_signal(closeadj):
    base = _maratio(closeadj, 63, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioB_252d_jerk_v065_signal(closeadj):
    base = _maratio(closeadj, 126, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioB_504d_jerk_v066_signal(closeadj):
    base = _maratio(closeadj, 252, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiolongB_252d_jerk_v067_signal(closeadj):
    base = _maratio(closeadj, 21, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emaratioB_252d_jerk_v068_signal(closeadj):
    base = np.log(_ema(closeadj, 63).replace(0, np.nan) / _ema(closeadj, 252).replace(0, np.nan))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposB_63d_jerk_v069_signal(closeadj):
    base = (_bandpos(closeadj, 63) - 0.5)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposB_126d_jerk_v070_signal(closeadj):
    base = (_bandpos(closeadj, 126) - 0.5)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposB_252d_jerk_v071_signal(closeadj):
    base = (_bandpos(closeadj, 252) - 0.5)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracB_63d_jerk_v072_signal(closeadj):
    base = _abovefrac(closeadj, 63, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracB_126d_jerk_v073_signal(closeadj):
    base = _abovefrac(closeadj, 126, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracB_252d_jerk_v074_signal(closeadj):
    base = _abovefrac(closeadj, 252, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracB_504d_jerk_v075_signal(closeadj):
    base = _abovefrac(closeadj, 504, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidB_252d_jerk_v076_signal(closeadj):
    base = _chanmid(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidB_504d_jerk_v077_signal(closeadj):
    base = _chanmid(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_stackmagB_252d_jerk_v078_signal(closeadj):
    base = _stackmag(closeadj)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfB_126d_jerk_v079_signal(closeadj):
    base = _diref(closeadj, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfB_252d_jerk_v080_signal(closeadj):
    base = _diref(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrB_126d_jerk_v081_signal(closeadj):
    base = _normstretch(closeadj, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrB_252d_jerk_v082_signal(closeadj):
    base = _normstretch(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistB_252d_jerk_v083_signal(closeadj):
    base = _meddist(closeadj, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistB_504d_jerk_v084_signal(closeadj):
    base = _meddist(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdB_63d_jerk_v085_signal(closeadj):
    base = _macd(closeadj, 21, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdB_126d_jerk_v086_signal(closeadj):
    base = _macd(closeadj, 63, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdB_252d_jerk_v087_signal(closeadj):
    base = _macd(closeadj, 126, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhB_252d_jerk_v088_signal(closeadj):
    base = np.tanh(4.0 * _pdist(closeadj, 252))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhB_504d_jerk_v089_signal(closeadj):
    base = np.tanh(3.0 * _pdist(closeadj, 504))
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistsqB_252d_jerk_v090_signal(closeadj):
    base = (np.sign(_pdist(closeadj, 252)) * (_pdist(closeadj, 252).abs() ** 0.5))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistcubeB_126d_jerk_v091_signal(closeadj):
    base = (_pdist(closeadj, 126) ** 3)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandpospowB_252d_jerk_v092_signal(closeadj):
    base = ((_bandpos(closeadj, 252) - 0.5) ** 3)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiotanhB_252d_jerk_v093_signal(closeadj):
    base = np.tanh(60.0 * _maratio(closeadj, 63, 252))
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistexpB_252d_jerk_v094_signal(closeadj):
    base = (np.exp(_pdist(closeadj, 252)) - 1.0)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposB_504d_jerk_v095_signal(closeadj):
    base = (_bandpos(closeadj, 504) - 0.5)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrB_63d_jerk_v096_signal(closeadj):
    base = _normstretch(closeadj, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistzB_126d_jerk_v097_signal(closeadj):
    base = _z(_emadist(closeadj, 126), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidB_126d_jerk_v098_signal(closeadj):
    base = _chanmid(closeadj, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistzB_252d_jerk_v099_signal(closeadj):
    base = _z(_meddist(closeadj, 252), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiozB_252d_jerk_v100_signal(closeadj):
    base = _z(_maratio(closeadj, 63, 252), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistC_21d_jerk_v101_signal(closeadj):
    base = _pdist(closeadj, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistC_63d_jerk_v102_signal(closeadj):
    base = _pdist(closeadj, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistC_126d_jerk_v103_signal(closeadj):
    base = _pdist(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistC_252d_jerk_v104_signal(closeadj):
    base = _pdist(closeadj, 252)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistC_504d_jerk_v105_signal(closeadj):
    base = _pdist(closeadj, 504)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzC_63d_jerk_v106_signal(closeadj):
    base = _z(_pdist(closeadj, 63), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzC_126d_jerk_v107_signal(closeadj):
    base = _z(_pdist(closeadj, 126), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistzC_252d_jerk_v108_signal(closeadj):
    base = _z(_pdist(closeadj, 252), 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistC_21d_jerk_v109_signal(closeadj):
    base = _emadist(closeadj, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistC_63d_jerk_v110_signal(closeadj):
    base = _emadist(closeadj, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistC_126d_jerk_v111_signal(closeadj):
    base = _emadist(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistC_252d_jerk_v112_signal(closeadj):
    base = _emadist(closeadj, 252)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioC_63d_jerk_v113_signal(closeadj):
    base = _maratio(closeadj, 21, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioC_126d_jerk_v114_signal(closeadj):
    base = _maratio(closeadj, 63, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioC_252d_jerk_v115_signal(closeadj):
    base = _maratio(closeadj, 126, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratioC_504d_jerk_v116_signal(closeadj):
    base = _maratio(closeadj, 252, 504)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiolongC_252d_jerk_v117_signal(closeadj):
    base = _maratio(closeadj, 21, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emaratioC_252d_jerk_v118_signal(closeadj):
    base = np.log(_ema(closeadj, 63).replace(0, np.nan) / _ema(closeadj, 252).replace(0, np.nan))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposC_63d_jerk_v119_signal(closeadj):
    base = (_bandpos(closeadj, 63) - 0.5)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposC_126d_jerk_v120_signal(closeadj):
    base = (_bandpos(closeadj, 126) - 0.5)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposC_252d_jerk_v121_signal(closeadj):
    base = (_bandpos(closeadj, 252) - 0.5)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracC_63d_jerk_v122_signal(closeadj):
    base = _abovefrac(closeadj, 63, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracC_126d_jerk_v123_signal(closeadj):
    base = _abovefrac(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracC_252d_jerk_v124_signal(closeadj):
    base = _abovefrac(closeadj, 252, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_abovefracC_504d_jerk_v125_signal(closeadj):
    base = _abovefrac(closeadj, 504, 504)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidC_252d_jerk_v126_signal(closeadj):
    base = _chanmid(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidC_504d_jerk_v127_signal(closeadj):
    base = _chanmid(closeadj, 504)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_stackmagC_252d_jerk_v128_signal(closeadj):
    base = _stackmag(closeadj)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfC_126d_jerk_v129_signal(closeadj):
    base = _diref(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_direfC_252d_jerk_v130_signal(closeadj):
    base = _diref(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrC_126d_jerk_v131_signal(closeadj):
    base = _normstretch(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrC_252d_jerk_v132_signal(closeadj):
    base = _normstretch(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistC_252d_jerk_v133_signal(closeadj):
    base = _meddist(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistC_504d_jerk_v134_signal(closeadj):
    base = _meddist(closeadj, 504)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdC_63d_jerk_v135_signal(closeadj):
    base = _macd(closeadj, 21, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdC_126d_jerk_v136_signal(closeadj):
    base = _macd(closeadj, 63, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_macdC_252d_jerk_v137_signal(closeadj):
    base = _macd(closeadj, 126, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhC_252d_jerk_v138_signal(closeadj):
    base = np.tanh(4.0 * _pdist(closeadj, 252))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdisttanhC_504d_jerk_v139_signal(closeadj):
    base = np.tanh(3.0 * _pdist(closeadj, 504))
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistsqC_252d_jerk_v140_signal(closeadj):
    base = (np.sign(_pdist(closeadj, 252)) * (_pdist(closeadj, 252).abs() ** 0.5))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistcubeC_126d_jerk_v141_signal(closeadj):
    base = (_pdist(closeadj, 126) ** 3)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandpospowC_252d_jerk_v142_signal(closeadj):
    base = ((_bandpos(closeadj, 252) - 0.5) ** 3)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiotanhC_252d_jerk_v143_signal(closeadj):
    base = np.tanh(60.0 * _maratio(closeadj, 63, 252))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_pdistexpC_252d_jerk_v144_signal(closeadj):
    base = (np.exp(_pdist(closeadj, 252)) - 1.0)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_bandposC_504d_jerk_v145_signal(closeadj):
    base = (_bandpos(closeadj, 504) - 0.5)
    sl = base.diff(252) / float(252)
    j = sl.diff(252) / float(252)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_normstrC_63d_jerk_v146_signal(closeadj):
    base = _normstretch(closeadj, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = np.tanh(8.0 * j)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_emadistzC_126d_jerk_v147_signal(closeadj):
    base = _z(_emadist(closeadj, 126), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = (j.rolling(252, min_periods=63).rank(pct=True) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_chanmidC_126d_jerk_v148_signal(closeadj):
    base = _chanmid(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = _z(j, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_meddistzC_252d_jerk_v149_signal(closeadj):
    base = _z(_meddist(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = ((j.abs()) - j.abs().rolling(126, min_periods=31).mean())
    return result.replace([np.inf, -np.inf], np.nan)

def f01ct_f01_cyclical_trend_structure_maratiozC_252d_jerk_v150_signal(closeadj):
    base = _z(_maratio(closeadj, 63, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = (np.sign(j) * (j.abs() ** 0.5))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ct_f01_cyclical_trend_structure_pdistA_21d_jerk_v001_signal,
    f01ct_f01_cyclical_trend_structure_pdistA_63d_jerk_v002_signal,
    f01ct_f01_cyclical_trend_structure_pdistA_126d_jerk_v003_signal,
    f01ct_f01_cyclical_trend_structure_pdistA_252d_jerk_v004_signal,
    f01ct_f01_cyclical_trend_structure_pdistA_504d_jerk_v005_signal,
    f01ct_f01_cyclical_trend_structure_pdistzA_63d_jerk_v006_signal,
    f01ct_f01_cyclical_trend_structure_pdistzA_126d_jerk_v007_signal,
    f01ct_f01_cyclical_trend_structure_pdistzA_252d_jerk_v008_signal,
    f01ct_f01_cyclical_trend_structure_emadistA_21d_jerk_v009_signal,
    f01ct_f01_cyclical_trend_structure_emadistA_63d_jerk_v010_signal,
    f01ct_f01_cyclical_trend_structure_emadistA_126d_jerk_v011_signal,
    f01ct_f01_cyclical_trend_structure_emadistA_252d_jerk_v012_signal,
    f01ct_f01_cyclical_trend_structure_maratioA_63d_jerk_v013_signal,
    f01ct_f01_cyclical_trend_structure_maratioA_126d_jerk_v014_signal,
    f01ct_f01_cyclical_trend_structure_maratioA_252d_jerk_v015_signal,
    f01ct_f01_cyclical_trend_structure_maratioA_504d_jerk_v016_signal,
    f01ct_f01_cyclical_trend_structure_maratiolongA_252d_jerk_v017_signal,
    f01ct_f01_cyclical_trend_structure_emaratioA_252d_jerk_v018_signal,
    f01ct_f01_cyclical_trend_structure_bandposA_63d_jerk_v019_signal,
    f01ct_f01_cyclical_trend_structure_bandposA_126d_jerk_v020_signal,
    f01ct_f01_cyclical_trend_structure_bandposA_252d_jerk_v021_signal,
    f01ct_f01_cyclical_trend_structure_abovefracA_63d_jerk_v022_signal,
    f01ct_f01_cyclical_trend_structure_abovefracA_126d_jerk_v023_signal,
    f01ct_f01_cyclical_trend_structure_abovefracA_252d_jerk_v024_signal,
    f01ct_f01_cyclical_trend_structure_abovefracA_504d_jerk_v025_signal,
    f01ct_f01_cyclical_trend_structure_chanmidA_252d_jerk_v026_signal,
    f01ct_f01_cyclical_trend_structure_chanmidA_504d_jerk_v027_signal,
    f01ct_f01_cyclical_trend_structure_stackmagA_252d_jerk_v028_signal,
    f01ct_f01_cyclical_trend_structure_direfA_126d_jerk_v029_signal,
    f01ct_f01_cyclical_trend_structure_direfA_252d_jerk_v030_signal,
    f01ct_f01_cyclical_trend_structure_normstrA_126d_jerk_v031_signal,
    f01ct_f01_cyclical_trend_structure_normstrA_252d_jerk_v032_signal,
    f01ct_f01_cyclical_trend_structure_meddistA_252d_jerk_v033_signal,
    f01ct_f01_cyclical_trend_structure_meddistA_504d_jerk_v034_signal,
    f01ct_f01_cyclical_trend_structure_macdA_63d_jerk_v035_signal,
    f01ct_f01_cyclical_trend_structure_macdA_126d_jerk_v036_signal,
    f01ct_f01_cyclical_trend_structure_macdA_252d_jerk_v037_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhA_252d_jerk_v038_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhA_504d_jerk_v039_signal,
    f01ct_f01_cyclical_trend_structure_pdistsqA_252d_jerk_v040_signal,
    f01ct_f01_cyclical_trend_structure_pdistcubeA_126d_jerk_v041_signal,
    f01ct_f01_cyclical_trend_structure_bandpospowA_252d_jerk_v042_signal,
    f01ct_f01_cyclical_trend_structure_maratiotanhA_252d_jerk_v043_signal,
    f01ct_f01_cyclical_trend_structure_pdistexpA_252d_jerk_v044_signal,
    f01ct_f01_cyclical_trend_structure_bandposA_504d_jerk_v045_signal,
    f01ct_f01_cyclical_trend_structure_normstrA_63d_jerk_v046_signal,
    f01ct_f01_cyclical_trend_structure_emadistzA_126d_jerk_v047_signal,
    f01ct_f01_cyclical_trend_structure_chanmidA_126d_jerk_v048_signal,
    f01ct_f01_cyclical_trend_structure_meddistzA_252d_jerk_v049_signal,
    f01ct_f01_cyclical_trend_structure_maratiozA_252d_jerk_v050_signal,
    f01ct_f01_cyclical_trend_structure_pdistB_21d_jerk_v051_signal,
    f01ct_f01_cyclical_trend_structure_pdistB_63d_jerk_v052_signal,
    f01ct_f01_cyclical_trend_structure_pdistB_126d_jerk_v053_signal,
    f01ct_f01_cyclical_trend_structure_pdistB_252d_jerk_v054_signal,
    f01ct_f01_cyclical_trend_structure_pdistB_504d_jerk_v055_signal,
    f01ct_f01_cyclical_trend_structure_pdistzB_63d_jerk_v056_signal,
    f01ct_f01_cyclical_trend_structure_pdistzB_126d_jerk_v057_signal,
    f01ct_f01_cyclical_trend_structure_pdistzB_252d_jerk_v058_signal,
    f01ct_f01_cyclical_trend_structure_emadistB_21d_jerk_v059_signal,
    f01ct_f01_cyclical_trend_structure_emadistB_63d_jerk_v060_signal,
    f01ct_f01_cyclical_trend_structure_emadistB_126d_jerk_v061_signal,
    f01ct_f01_cyclical_trend_structure_emadistB_252d_jerk_v062_signal,
    f01ct_f01_cyclical_trend_structure_maratioB_63d_jerk_v063_signal,
    f01ct_f01_cyclical_trend_structure_maratioB_126d_jerk_v064_signal,
    f01ct_f01_cyclical_trend_structure_maratioB_252d_jerk_v065_signal,
    f01ct_f01_cyclical_trend_structure_maratioB_504d_jerk_v066_signal,
    f01ct_f01_cyclical_trend_structure_maratiolongB_252d_jerk_v067_signal,
    f01ct_f01_cyclical_trend_structure_emaratioB_252d_jerk_v068_signal,
    f01ct_f01_cyclical_trend_structure_bandposB_63d_jerk_v069_signal,
    f01ct_f01_cyclical_trend_structure_bandposB_126d_jerk_v070_signal,
    f01ct_f01_cyclical_trend_structure_bandposB_252d_jerk_v071_signal,
    f01ct_f01_cyclical_trend_structure_abovefracB_63d_jerk_v072_signal,
    f01ct_f01_cyclical_trend_structure_abovefracB_126d_jerk_v073_signal,
    f01ct_f01_cyclical_trend_structure_abovefracB_252d_jerk_v074_signal,
    f01ct_f01_cyclical_trend_structure_abovefracB_504d_jerk_v075_signal,
    f01ct_f01_cyclical_trend_structure_chanmidB_252d_jerk_v076_signal,
    f01ct_f01_cyclical_trend_structure_chanmidB_504d_jerk_v077_signal,
    f01ct_f01_cyclical_trend_structure_stackmagB_252d_jerk_v078_signal,
    f01ct_f01_cyclical_trend_structure_direfB_126d_jerk_v079_signal,
    f01ct_f01_cyclical_trend_structure_direfB_252d_jerk_v080_signal,
    f01ct_f01_cyclical_trend_structure_normstrB_126d_jerk_v081_signal,
    f01ct_f01_cyclical_trend_structure_normstrB_252d_jerk_v082_signal,
    f01ct_f01_cyclical_trend_structure_meddistB_252d_jerk_v083_signal,
    f01ct_f01_cyclical_trend_structure_meddistB_504d_jerk_v084_signal,
    f01ct_f01_cyclical_trend_structure_macdB_63d_jerk_v085_signal,
    f01ct_f01_cyclical_trend_structure_macdB_126d_jerk_v086_signal,
    f01ct_f01_cyclical_trend_structure_macdB_252d_jerk_v087_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhB_252d_jerk_v088_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhB_504d_jerk_v089_signal,
    f01ct_f01_cyclical_trend_structure_pdistsqB_252d_jerk_v090_signal,
    f01ct_f01_cyclical_trend_structure_pdistcubeB_126d_jerk_v091_signal,
    f01ct_f01_cyclical_trend_structure_bandpospowB_252d_jerk_v092_signal,
    f01ct_f01_cyclical_trend_structure_maratiotanhB_252d_jerk_v093_signal,
    f01ct_f01_cyclical_trend_structure_pdistexpB_252d_jerk_v094_signal,
    f01ct_f01_cyclical_trend_structure_bandposB_504d_jerk_v095_signal,
    f01ct_f01_cyclical_trend_structure_normstrB_63d_jerk_v096_signal,
    f01ct_f01_cyclical_trend_structure_emadistzB_126d_jerk_v097_signal,
    f01ct_f01_cyclical_trend_structure_chanmidB_126d_jerk_v098_signal,
    f01ct_f01_cyclical_trend_structure_meddistzB_252d_jerk_v099_signal,
    f01ct_f01_cyclical_trend_structure_maratiozB_252d_jerk_v100_signal,
    f01ct_f01_cyclical_trend_structure_pdistC_21d_jerk_v101_signal,
    f01ct_f01_cyclical_trend_structure_pdistC_63d_jerk_v102_signal,
    f01ct_f01_cyclical_trend_structure_pdistC_126d_jerk_v103_signal,
    f01ct_f01_cyclical_trend_structure_pdistC_252d_jerk_v104_signal,
    f01ct_f01_cyclical_trend_structure_pdistC_504d_jerk_v105_signal,
    f01ct_f01_cyclical_trend_structure_pdistzC_63d_jerk_v106_signal,
    f01ct_f01_cyclical_trend_structure_pdistzC_126d_jerk_v107_signal,
    f01ct_f01_cyclical_trend_structure_pdistzC_252d_jerk_v108_signal,
    f01ct_f01_cyclical_trend_structure_emadistC_21d_jerk_v109_signal,
    f01ct_f01_cyclical_trend_structure_emadistC_63d_jerk_v110_signal,
    f01ct_f01_cyclical_trend_structure_emadistC_126d_jerk_v111_signal,
    f01ct_f01_cyclical_trend_structure_emadistC_252d_jerk_v112_signal,
    f01ct_f01_cyclical_trend_structure_maratioC_63d_jerk_v113_signal,
    f01ct_f01_cyclical_trend_structure_maratioC_126d_jerk_v114_signal,
    f01ct_f01_cyclical_trend_structure_maratioC_252d_jerk_v115_signal,
    f01ct_f01_cyclical_trend_structure_maratioC_504d_jerk_v116_signal,
    f01ct_f01_cyclical_trend_structure_maratiolongC_252d_jerk_v117_signal,
    f01ct_f01_cyclical_trend_structure_emaratioC_252d_jerk_v118_signal,
    f01ct_f01_cyclical_trend_structure_bandposC_63d_jerk_v119_signal,
    f01ct_f01_cyclical_trend_structure_bandposC_126d_jerk_v120_signal,
    f01ct_f01_cyclical_trend_structure_bandposC_252d_jerk_v121_signal,
    f01ct_f01_cyclical_trend_structure_abovefracC_63d_jerk_v122_signal,
    f01ct_f01_cyclical_trend_structure_abovefracC_126d_jerk_v123_signal,
    f01ct_f01_cyclical_trend_structure_abovefracC_252d_jerk_v124_signal,
    f01ct_f01_cyclical_trend_structure_abovefracC_504d_jerk_v125_signal,
    f01ct_f01_cyclical_trend_structure_chanmidC_252d_jerk_v126_signal,
    f01ct_f01_cyclical_trend_structure_chanmidC_504d_jerk_v127_signal,
    f01ct_f01_cyclical_trend_structure_stackmagC_252d_jerk_v128_signal,
    f01ct_f01_cyclical_trend_structure_direfC_126d_jerk_v129_signal,
    f01ct_f01_cyclical_trend_structure_direfC_252d_jerk_v130_signal,
    f01ct_f01_cyclical_trend_structure_normstrC_126d_jerk_v131_signal,
    f01ct_f01_cyclical_trend_structure_normstrC_252d_jerk_v132_signal,
    f01ct_f01_cyclical_trend_structure_meddistC_252d_jerk_v133_signal,
    f01ct_f01_cyclical_trend_structure_meddistC_504d_jerk_v134_signal,
    f01ct_f01_cyclical_trend_structure_macdC_63d_jerk_v135_signal,
    f01ct_f01_cyclical_trend_structure_macdC_126d_jerk_v136_signal,
    f01ct_f01_cyclical_trend_structure_macdC_252d_jerk_v137_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhC_252d_jerk_v138_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanhC_504d_jerk_v139_signal,
    f01ct_f01_cyclical_trend_structure_pdistsqC_252d_jerk_v140_signal,
    f01ct_f01_cyclical_trend_structure_pdistcubeC_126d_jerk_v141_signal,
    f01ct_f01_cyclical_trend_structure_bandpospowC_252d_jerk_v142_signal,
    f01ct_f01_cyclical_trend_structure_maratiotanhC_252d_jerk_v143_signal,
    f01ct_f01_cyclical_trend_structure_pdistexpC_252d_jerk_v144_signal,
    f01ct_f01_cyclical_trend_structure_bandposC_504d_jerk_v145_signal,
    f01ct_f01_cyclical_trend_structure_normstrC_63d_jerk_v146_signal,
    f01ct_f01_cyclical_trend_structure_emadistzC_126d_jerk_v147_signal,
    f01ct_f01_cyclical_trend_structure_chanmidC_126d_jerk_v148_signal,
    f01ct_f01_cyclical_trend_structure_meddistzC_252d_jerk_v149_signal,
    f01ct_f01_cyclical_trend_structure_maratiozC_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_CYCLICAL_TREND_STRUCTURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f01_cyclical_trend_structure_3rd_derivatives_001_150_claude: %d features pass" % n_features)
