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


def _pxvma(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return close / ma.replace(0, np.nan) - 1.0


def _maslope(close, w, k):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(ma.replace(0, np.nan) / ma.shift(k).replace(0, np.nan)) / float(k)


def _maspread(close, ws, wl):
    s = close.rolling(ws, min_periods=max(1, ws // 2)).mean()
    l = close.rolling(wl, min_periods=max(1, wl // 2)).mean()
    return s / l.replace(0, np.nan) - 1.0


def _stack3(close):
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    g1 = (m21 - m63) / m63.replace(0, np.nan)
    g2 = (m63 - m126) / m126.replace(0, np.nan)
    g3 = (m126 - m252) / m252.replace(0, np.nan)
    sc = (m21 > m63).astype(float) + (m63 > m126).astype(float) + (m126 > m252).astype(float) - 1.5
    return sc + 5.0 * (g1 + g2 + g3)


def _abovefrac(close, w, lw):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(lw, min_periods=max(1, lw // 2)).mean()


def _efficiency(close, w):
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _signeff(close, w):
    net = close - close.shift(w)
    path = close.diff().abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _distz(close, w, zw):
    return _z(_pxvma(close, w), zw)


def _macd(close):
    e1 = close.ewm(span=12, min_periods=6).mean()
    e2 = close.ewm(span=26, min_periods=13).mean()
    return (e1 - e2) / close.replace(0, np.nan)


def _emavssma(close, w):
    ema = close.ewm(span=w, min_periods=max(1, w // 2)).mean()
    sma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (ema - sma) / sma.replace(0, np.nan)


def _dirpersist(close, w, lw):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sign(ma.diff()).rolling(lw, min_periods=max(1, lw // 2)).mean()


def f01ts_f01_trend_structure_pxvma21d_21d_slope_v001_signal(closeadj):
    base = _pxvma(closeadj, 21)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma21d_42d_slope_v002_signal(closeadj):
    base = _pxvma(closeadj, 21)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma42d_21d_slope_v003_signal(closeadj):
    base = _pxvma(closeadj, 42)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma42d_42d_slope_v004_signal(closeadj):
    base = _pxvma(closeadj, 42)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma63d_21d_slope_v005_signal(closeadj):
    base = _pxvma(closeadj, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma63d_63d_slope_v006_signal(closeadj):
    base = _pxvma(closeadj, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma126d_63d_slope_v007_signal(closeadj):
    base = _pxvma(closeadj, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma126d_126d_slope_v008_signal(closeadj):
    base = _pxvma(closeadj, 126)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma252d_63d_slope_v009_signal(closeadj):
    base = _pxvma(closeadj, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma252d_126d_slope_v010_signal(closeadj):
    base = _pxvma(closeadj, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvma504d_126d_slope_v011_signal(closeadj):
    base = _pxvma(closeadj, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope21d_21d_slope_v012_signal(closeadj):
    base = _maslope(closeadj, 21, 21)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope21d_42d_slope_v013_signal(closeadj):
    base = _maslope(closeadj, 21, 21)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope42d_42d_slope_v014_signal(closeadj):
    base = _maslope(closeadj, 42, 21)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope42d_95d_slope_v015_signal(closeadj):
    base = _maslope(closeadj, 42, 21)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope63d_21d_slope_v016_signal(closeadj):
    base = _maslope(closeadj, 63, 21)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope63d_95d_slope_v017_signal(closeadj):
    base = _maslope(closeadj, 63, 21)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope126d_63d_slope_v018_signal(closeadj):
    base = _maslope(closeadj, 126, 21)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope126d_126d_slope_v019_signal(closeadj):
    base = _maslope(closeadj, 126, 21)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope252d_63d_slope_v020_signal(closeadj):
    base = _maslope(closeadj, 252, 21)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope252d_126d_slope_v021_signal(closeadj):
    base = _maslope(closeadj, 252, 21)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_maslope504d_126d_slope_v022_signal(closeadj):
    base = _maslope(closeadj, 504, 21)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr5v21_21d_slope_v023_signal(closeadj):
    base = _maspread(closeadj, 5, 21)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr5v21_42d_slope_v024_signal(closeadj):
    base = _maspread(closeadj, 5, 21)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr21v63_21d_slope_v025_signal(closeadj):
    base = _maspread(closeadj, 21, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr21v126_21d_slope_v026_signal(closeadj):
    base = _maspread(closeadj, 21, 126)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr21v126_63d_slope_v027_signal(closeadj):
    base = _maspread(closeadj, 21, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr42v126_42d_slope_v028_signal(closeadj):
    base = _maspread(closeadj, 42, 126)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr42v126_63d_slope_v029_signal(closeadj):
    base = _maspread(closeadj, 42, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr63v189_63d_slope_v030_signal(closeadj):
    base = _maspread(closeadj, 63, 189)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr63v189_126d_slope_v031_signal(closeadj):
    base = _maspread(closeadj, 63, 189)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr63v252_95d_slope_v032_signal(closeadj):
    base = _maspread(closeadj, 63, 252)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr126v252_126d_slope_v033_signal(closeadj):
    base = _maspread(closeadj, 126, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_spr126v504_126d_slope_v034_signal(closeadj):
    base = _maspread(closeadj, 126, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz5d_21d_slope_v035_signal(closeadj):
    base = _distz(closeadj, 5, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz32d_21d_slope_v036_signal(closeadj):
    base = _distz(closeadj, 32, 126)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz32d_63d_slope_v037_signal(closeadj):
    base = _distz(closeadj, 32, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz95d_63d_slope_v038_signal(closeadj):
    base = _distz(closeadj, 95, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz95d_126d_slope_v039_signal(closeadj):
    base = _distz(closeadj, 95, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz160d_63d_slope_v040_signal(closeadj):
    base = _distz(closeadj, 160, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz160d_126d_slope_v041_signal(closeadj):
    base = _distz(closeadj, 160, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distz315d_126d_slope_v042_signal(closeadj):
    base = _distz(closeadj, 315, 504)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_stack_21d_slope_v043_signal(closeadj):
    base = _stack3(closeadj)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_stack_42d_slope_v044_signal(closeadj):
    base = _stack3(closeadj)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_stack_63d_slope_v045_signal(closeadj):
    base = _stack3(closeadj)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_stack_126d_slope_v046_signal(closeadj):
    base = _stack3(closeadj)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac21d_21d_slope_v047_signal(closeadj):
    base = _abovefrac(closeadj, 21, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac21d_42d_slope_v048_signal(closeadj):
    base = _abovefrac(closeadj, 21, 63)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac63d_21d_slope_v049_signal(closeadj):
    base = _abovefrac(closeadj, 63, 126)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac63d_63d_slope_v050_signal(closeadj):
    base = _abovefrac(closeadj, 63, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac126d_63d_slope_v051_signal(closeadj):
    base = _abovefrac(closeadj, 126, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac126d_126d_slope_v052_signal(closeadj):
    base = _abovefrac(closeadj, 126, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac252d_63d_slope_v053_signal(closeadj):
    base = _abovefrac(closeadj, 252, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac252d_126d_slope_v054_signal(closeadj):
    base = _abovefrac(closeadj, 252, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefrac504d_126d_slope_v055_signal(closeadj):
    base = _abovefrac(closeadj, 504, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff21d_21d_slope_v056_signal(closeadj):
    base = _efficiency(closeadj, 21)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff21d_42d_slope_v057_signal(closeadj):
    base = _efficiency(closeadj, 21)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff63d_21d_slope_v058_signal(closeadj):
    base = _efficiency(closeadj, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff63d_63d_slope_v059_signal(closeadj):
    base = _efficiency(closeadj, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff126d_63d_slope_v060_signal(closeadj):
    base = _efficiency(closeadj, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff126d_126d_slope_v061_signal(closeadj):
    base = _efficiency(closeadj, 126)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff252d_63d_slope_v062_signal(closeadj):
    base = _efficiency(closeadj, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_eff252d_126d_slope_v063_signal(closeadj):
    base = _efficiency(closeadj, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff63d_21d_slope_v064_signal(closeadj):
    base = _signeff(closeadj, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff63d_63d_slope_v065_signal(closeadj):
    base = _signeff(closeadj, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff126d_63d_slope_v066_signal(closeadj):
    base = _signeff(closeadj, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff126d_126d_slope_v067_signal(closeadj):
    base = _signeff(closeadj, 126)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff252d_63d_slope_v068_signal(closeadj):
    base = _signeff(closeadj, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_signeff252d_126d_slope_v069_signal(closeadj):
    base = _signeff(closeadj, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_macd_21d_slope_v070_signal(closeadj):
    base = _macd(closeadj)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_macd_42d_slope_v071_signal(closeadj):
    base = _macd(closeadj)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_macd_63d_slope_v072_signal(closeadj):
    base = _macd(closeadj)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emavssma63d_21d_slope_v073_signal(closeadj):
    base = _emavssma(closeadj, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emavssma63d_63d_slope_v074_signal(closeadj):
    base = _emavssma(closeadj, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emavssma126d_63d_slope_v075_signal(closeadj):
    base = _emavssma(closeadj, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emavssma126d_126d_slope_v076_signal(closeadj):
    base = _emavssma(closeadj, 126)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emavssma252d_126d_slope_v077_signal(closeadj):
    base = _emavssma(closeadj, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_dirp63d_21d_slope_v078_signal(closeadj):
    base = _dirpersist(closeadj, 63, 63)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_dirp63d_63d_slope_v079_signal(closeadj):
    base = _dirpersist(closeadj, 63, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_dirp126d_63d_slope_v080_signal(closeadj):
    base = _dirpersist(closeadj, 126, 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_dirp126d_126d_slope_v081_signal(closeadj):
    base = _dirpersist(closeadj, 126, 126)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_dirp252d_126d_slope_v082_signal(closeadj):
    base = _dirpersist(closeadj, 252, 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube32d_21d_slope_v083_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 32)) * (_pxvma(closeadj, 32) ** 2) * 50.0)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube32d_63d_slope_v084_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 32)) * (_pxvma(closeadj, 32) ** 2) * 50.0)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube95d_63d_slope_v085_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 95)) * (_pxvma(closeadj, 95) ** 2) * 50.0)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube95d_126d_slope_v086_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 95)) * (_pxvma(closeadj, 95) ** 2) * 50.0)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube160d_63d_slope_v087_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 160)) * (_pxvma(closeadj, 160) ** 2) * 50.0)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmacube160d_126d_slope_v088_signal(closeadj):
    base = (np.sign(_pxvma(closeadj, 160)) * (_pxvma(closeadj, 160) ** 2) * 50.0)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprtanh10v50_21d_slope_v089_signal(closeadj):
    base = np.tanh(25.0 * _maspread(closeadj, 10, 50))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprtanh10v50_42d_slope_v090_signal(closeadj):
    base = np.tanh(25.0 * _maspread(closeadj, 10, 50))
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprtanh50v200_63d_slope_v091_signal(closeadj):
    base = np.tanh(25.0 * _maspread(closeadj, 50, 200))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprtanh50v200_126d_slope_v092_signal(closeadj):
    base = np.tanh(25.0 * _maspread(closeadj, 50, 200))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprtanh32v160_63d_slope_v093_signal(closeadj):
    base = np.tanh(25.0 * _maspread(closeadj, 32, 160))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emaslope50d_42d_slope_v094_signal(closeadj):
    base = np.log(_ema(closeadj, 50).replace(0, np.nan) / _ema(closeadj, 50).shift(21).replace(0, np.nan))
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emaslope50d_95d_slope_v095_signal(closeadj):
    base = np.log(_ema(closeadj, 50).replace(0, np.nan) / _ema(closeadj, 50).shift(21).replace(0, np.nan))
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emaslope100d_95d_slope_v096_signal(closeadj):
    base = np.log(_ema(closeadj, 100).replace(0, np.nan) / _ema(closeadj, 100).shift(21).replace(0, np.nan))
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emaslope100d_126d_slope_v097_signal(closeadj):
    base = np.log(_ema(closeadj, 100).replace(0, np.nan) / _ema(closeadj, 100).shift(21).replace(0, np.nan))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emaslope200d_126d_slope_v098_signal(closeadj):
    base = np.log(_ema(closeadj, 200).replace(0, np.nan) / _ema(closeadj, 200).shift(21).replace(0, np.nan))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmarank32d_21d_slope_v099_signal(closeadj):
    base = (_pxvma(closeadj, 32).rolling(252, min_periods=63).rank(pct=True) - 0.5)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmarank32d_63d_slope_v100_signal(closeadj):
    base = (_pxvma(closeadj, 32).rolling(252, min_periods=63).rank(pct=True) - 0.5)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmarank95d_63d_slope_v101_signal(closeadj):
    base = (_pxvma(closeadj, 95).rolling(504, min_periods=126).rank(pct=True) - 0.5)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmarank95d_126d_slope_v102_signal(closeadj):
    base = (_pxvma(closeadj, 95).rolling(504, min_periods=126).rank(pct=True) - 0.5)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_pxvmarank160d_126d_slope_v103_signal(closeadj):
    base = (_pxvma(closeadj, 160).rolling(1260, min_periods=315).rank(pct=True) - 0.5)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopeanom32d_21d_slope_v104_signal(closeadj):
    base = (_maslope(closeadj, 32, 21) - _maslope(closeadj, 32, 21).rolling(252, min_periods=126).mean())
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopeanom32d_95d_slope_v105_signal(closeadj):
    base = (_maslope(closeadj, 32, 21) - _maslope(closeadj, 32, 21).rolling(252, min_periods=126).mean())
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopeanom95d_42d_slope_v106_signal(closeadj):
    base = (_maslope(closeadj, 95, 21) - _maslope(closeadj, 95, 21).rolling(252, min_periods=126).mean())
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopeanom95d_126d_slope_v107_signal(closeadj):
    base = (_maslope(closeadj, 95, 21) - _maslope(closeadj, 95, 21).rolling(252, min_periods=126).mean())
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopeanom160d_126d_slope_v108_signal(closeadj):
    base = (_maslope(closeadj, 160, 21) - _maslope(closeadj, 160, 21).rolling(252, min_periods=126).mean())
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distrev15d_21d_slope_v109_signal(closeadj):
    base = (_pxvma(closeadj, 15) - _pxvma(closeadj, 15).rolling(42, min_periods=21).mean())
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distrev35d_42d_slope_v110_signal(closeadj):
    base = (_pxvma(closeadj, 35) - _pxvma(closeadj, 35).rolling(95, min_periods=47).mean())
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distrev35d_95d_slope_v111_signal(closeadj):
    base = (_pxvma(closeadj, 35) - _pxvma(closeadj, 35).rolling(95, min_periods=47).mean())
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distrev75d_95d_slope_v112_signal(closeadj):
    base = (_pxvma(closeadj, 75) - _pxvma(closeadj, 75).rolling(189, min_periods=94).mean())
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_distrev75d_126d_slope_v113_signal(closeadj):
    base = (_pxvma(closeadj, 75) - _pxvma(closeadj, 75).rolling(189, min_periods=94).mean())
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel10d_21d_slope_v114_signal(closeadj):
    base = ((closeadj / closeadj.shift(10).replace(0, np.nan) - 1.0) - (closeadj.shift(10) / closeadj.shift(20).replace(0, np.nan) - 1.0))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel10d_42d_slope_v115_signal(closeadj):
    base = ((closeadj / closeadj.shift(10).replace(0, np.nan) - 1.0) - (closeadj.shift(10) / closeadj.shift(20).replace(0, np.nan) - 1.0))
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel32d_21d_slope_v116_signal(closeadj):
    base = ((closeadj / closeadj.shift(32).replace(0, np.nan) - 1.0) - (closeadj.shift(32) / closeadj.shift(64).replace(0, np.nan) - 1.0))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel32d_63d_slope_v117_signal(closeadj):
    base = ((closeadj / closeadj.shift(32).replace(0, np.nan) - 1.0) - (closeadj.shift(32) / closeadj.shift(64).replace(0, np.nan) - 1.0))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel95d_63d_slope_v118_signal(closeadj):
    base = ((closeadj / closeadj.shift(95).replace(0, np.nan) - 1.0) - (closeadj.shift(95) / closeadj.shift(190).replace(0, np.nan) - 1.0))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_accel95d_126d_slope_v119_signal(closeadj):
    base = ((closeadj / closeadj.shift(95).replace(0, np.nan) - 1.0) - (closeadj.shift(95) / closeadj.shift(190).replace(0, np.nan) - 1.0))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprz21v63_42d_slope_v120_signal(closeadj):
    base = _z(_maspread(closeadj, 21, 63), 252)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprz21v63_63d_slope_v121_signal(closeadj):
    base = _z(_maspread(closeadj, 21, 63), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprz63v252_95d_slope_v122_signal(closeadj):
    base = _z(_maspread(closeadj, 63, 252), 252)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprz63v252_126d_slope_v123_signal(closeadj):
    base = _z(_maspread(closeadj, 63, 252), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_sprz126v504_126d_slope_v124_signal(closeadj):
    base = _z(_maspread(closeadj, 126, 504), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopesm75d_21d_slope_v125_signal(closeadj):
    base = (np.sign(_maslope(closeadj, 75, 21)) * (_maslope(closeadj, 75, 21).abs() ** 0.5))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopesm75d_63d_slope_v126_signal(closeadj):
    base = (np.sign(_maslope(closeadj, 75, 21)) * (_maslope(closeadj, 75, 21).abs() ** 0.5))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopesm150d_63d_slope_v127_signal(closeadj):
    base = (np.sign(_maslope(closeadj, 150, 21)) * (_maslope(closeadj, 150, 21).abs() ** 0.5))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopesm150d_126d_slope_v128_signal(closeadj):
    base = (np.sign(_maslope(closeadj, 150, 21)) * (_maslope(closeadj, 150, 21).abs() ** 0.5))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slopesm300d_126d_slope_v129_signal(closeadj):
    base = (np.sign(_maslope(closeadj, 300, 21)) * (_maslope(closeadj, 300, 21).abs() ** 0.5))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma30d_21d_slope_v130_signal(closeadj):
    base = _emavssma(closeadj, 30)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma30d_42d_slope_v131_signal(closeadj):
    base = _emavssma(closeadj, 30)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma75d_21d_slope_v132_signal(closeadj):
    base = _emavssma(closeadj, 75)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma75d_63d_slope_v133_signal(closeadj):
    base = _emavssma(closeadj, 75)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma150d_63d_slope_v134_signal(closeadj):
    base = _emavssma(closeadj, 150)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_emasma150d_126d_slope_v135_signal(closeadj):
    base = _emavssma(closeadj, 150)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefr32d_21d_slope_v136_signal(closeadj):
    base = _abovefrac(closeadj, 32, 95)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefr32d_63d_slope_v137_signal(closeadj):
    base = _abovefrac(closeadj, 32, 95)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefr95d_42d_slope_v138_signal(closeadj):
    base = _abovefrac(closeadj, 95, 189)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefr95d_95d_slope_v139_signal(closeadj):
    base = _abovefrac(closeadj, 95, 189)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_abovefr160d_95d_slope_v140_signal(closeadj):
    base = _abovefrac(closeadj, 160, 315)
    d = base.diff(95) / float(95)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slead21v42_42d_slope_v141_signal(closeadj):
    base = (_maslope(closeadj, 21, 21) - _maslope(closeadj, 42, 21))
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slead21v42_75d_slope_v142_signal(closeadj):
    base = (_maslope(closeadj, 21, 21) - _maslope(closeadj, 42, 21))
    d = base.diff(75) / float(75)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slead42v75_126d_slope_v143_signal(closeadj):
    base = (_maslope(closeadj, 42, 21) - _maslope(closeadj, 75, 21))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slead63v95_63d_slope_v144_signal(closeadj):
    base = (_maslope(closeadj, 63, 21) - _maslope(closeadj, 95, 21))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_slead63v95_126d_slope_v145_signal(closeadj):
    base = (_maslope(closeadj, 63, 21) - _maslope(closeadj, 95, 21))
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_effi42d_21d_slope_v146_signal(closeadj):
    base = _efficiency(closeadj, 42)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_effi42d_42d_slope_v147_signal(closeadj):
    base = _efficiency(closeadj, 42)
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_effi95d_63d_slope_v148_signal(closeadj):
    base = _efficiency(closeadj, 95)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_effi95d_126d_slope_v149_signal(closeadj):
    base = _efficiency(closeadj, 95)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f01ts_f01_trend_structure_effi189d_126d_slope_v150_signal(closeadj):
    base = _efficiency(closeadj, 189)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_pxvma21d_21d_slope_v001_signal,
    f01ts_f01_trend_structure_pxvma21d_42d_slope_v002_signal,
    f01ts_f01_trend_structure_pxvma42d_21d_slope_v003_signal,
    f01ts_f01_trend_structure_pxvma42d_42d_slope_v004_signal,
    f01ts_f01_trend_structure_pxvma63d_21d_slope_v005_signal,
    f01ts_f01_trend_structure_pxvma63d_63d_slope_v006_signal,
    f01ts_f01_trend_structure_pxvma126d_63d_slope_v007_signal,
    f01ts_f01_trend_structure_pxvma126d_126d_slope_v008_signal,
    f01ts_f01_trend_structure_pxvma252d_63d_slope_v009_signal,
    f01ts_f01_trend_structure_pxvma252d_126d_slope_v010_signal,
    f01ts_f01_trend_structure_pxvma504d_126d_slope_v011_signal,
    f01ts_f01_trend_structure_maslope21d_21d_slope_v012_signal,
    f01ts_f01_trend_structure_maslope21d_42d_slope_v013_signal,
    f01ts_f01_trend_structure_maslope42d_42d_slope_v014_signal,
    f01ts_f01_trend_structure_maslope42d_95d_slope_v015_signal,
    f01ts_f01_trend_structure_maslope63d_21d_slope_v016_signal,
    f01ts_f01_trend_structure_maslope63d_95d_slope_v017_signal,
    f01ts_f01_trend_structure_maslope126d_63d_slope_v018_signal,
    f01ts_f01_trend_structure_maslope126d_126d_slope_v019_signal,
    f01ts_f01_trend_structure_maslope252d_63d_slope_v020_signal,
    f01ts_f01_trend_structure_maslope252d_126d_slope_v021_signal,
    f01ts_f01_trend_structure_maslope504d_126d_slope_v022_signal,
    f01ts_f01_trend_structure_spr5v21_21d_slope_v023_signal,
    f01ts_f01_trend_structure_spr5v21_42d_slope_v024_signal,
    f01ts_f01_trend_structure_spr21v63_21d_slope_v025_signal,
    f01ts_f01_trend_structure_spr21v126_21d_slope_v026_signal,
    f01ts_f01_trend_structure_spr21v126_63d_slope_v027_signal,
    f01ts_f01_trend_structure_spr42v126_42d_slope_v028_signal,
    f01ts_f01_trend_structure_spr42v126_63d_slope_v029_signal,
    f01ts_f01_trend_structure_spr63v189_63d_slope_v030_signal,
    f01ts_f01_trend_structure_spr63v189_126d_slope_v031_signal,
    f01ts_f01_trend_structure_spr63v252_95d_slope_v032_signal,
    f01ts_f01_trend_structure_spr126v252_126d_slope_v033_signal,
    f01ts_f01_trend_structure_spr126v504_126d_slope_v034_signal,
    f01ts_f01_trend_structure_distz5d_21d_slope_v035_signal,
    f01ts_f01_trend_structure_distz32d_21d_slope_v036_signal,
    f01ts_f01_trend_structure_distz32d_63d_slope_v037_signal,
    f01ts_f01_trend_structure_distz95d_63d_slope_v038_signal,
    f01ts_f01_trend_structure_distz95d_126d_slope_v039_signal,
    f01ts_f01_trend_structure_distz160d_63d_slope_v040_signal,
    f01ts_f01_trend_structure_distz160d_126d_slope_v041_signal,
    f01ts_f01_trend_structure_distz315d_126d_slope_v042_signal,
    f01ts_f01_trend_structure_stack_21d_slope_v043_signal,
    f01ts_f01_trend_structure_stack_42d_slope_v044_signal,
    f01ts_f01_trend_structure_stack_63d_slope_v045_signal,
    f01ts_f01_trend_structure_stack_126d_slope_v046_signal,
    f01ts_f01_trend_structure_abovefrac21d_21d_slope_v047_signal,
    f01ts_f01_trend_structure_abovefrac21d_42d_slope_v048_signal,
    f01ts_f01_trend_structure_abovefrac63d_21d_slope_v049_signal,
    f01ts_f01_trend_structure_abovefrac63d_63d_slope_v050_signal,
    f01ts_f01_trend_structure_abovefrac126d_63d_slope_v051_signal,
    f01ts_f01_trend_structure_abovefrac126d_126d_slope_v052_signal,
    f01ts_f01_trend_structure_abovefrac252d_63d_slope_v053_signal,
    f01ts_f01_trend_structure_abovefrac252d_126d_slope_v054_signal,
    f01ts_f01_trend_structure_abovefrac504d_126d_slope_v055_signal,
    f01ts_f01_trend_structure_eff21d_21d_slope_v056_signal,
    f01ts_f01_trend_structure_eff21d_42d_slope_v057_signal,
    f01ts_f01_trend_structure_eff63d_21d_slope_v058_signal,
    f01ts_f01_trend_structure_eff63d_63d_slope_v059_signal,
    f01ts_f01_trend_structure_eff126d_63d_slope_v060_signal,
    f01ts_f01_trend_structure_eff126d_126d_slope_v061_signal,
    f01ts_f01_trend_structure_eff252d_63d_slope_v062_signal,
    f01ts_f01_trend_structure_eff252d_126d_slope_v063_signal,
    f01ts_f01_trend_structure_signeff63d_21d_slope_v064_signal,
    f01ts_f01_trend_structure_signeff63d_63d_slope_v065_signal,
    f01ts_f01_trend_structure_signeff126d_63d_slope_v066_signal,
    f01ts_f01_trend_structure_signeff126d_126d_slope_v067_signal,
    f01ts_f01_trend_structure_signeff252d_63d_slope_v068_signal,
    f01ts_f01_trend_structure_signeff252d_126d_slope_v069_signal,
    f01ts_f01_trend_structure_macd_21d_slope_v070_signal,
    f01ts_f01_trend_structure_macd_42d_slope_v071_signal,
    f01ts_f01_trend_structure_macd_63d_slope_v072_signal,
    f01ts_f01_trend_structure_emavssma63d_21d_slope_v073_signal,
    f01ts_f01_trend_structure_emavssma63d_63d_slope_v074_signal,
    f01ts_f01_trend_structure_emavssma126d_63d_slope_v075_signal,
    f01ts_f01_trend_structure_emavssma126d_126d_slope_v076_signal,
    f01ts_f01_trend_structure_emavssma252d_126d_slope_v077_signal,
    f01ts_f01_trend_structure_dirp63d_21d_slope_v078_signal,
    f01ts_f01_trend_structure_dirp63d_63d_slope_v079_signal,
    f01ts_f01_trend_structure_dirp126d_63d_slope_v080_signal,
    f01ts_f01_trend_structure_dirp126d_126d_slope_v081_signal,
    f01ts_f01_trend_structure_dirp252d_126d_slope_v082_signal,
    f01ts_f01_trend_structure_pxvmacube32d_21d_slope_v083_signal,
    f01ts_f01_trend_structure_pxvmacube32d_63d_slope_v084_signal,
    f01ts_f01_trend_structure_pxvmacube95d_63d_slope_v085_signal,
    f01ts_f01_trend_structure_pxvmacube95d_126d_slope_v086_signal,
    f01ts_f01_trend_structure_pxvmacube160d_63d_slope_v087_signal,
    f01ts_f01_trend_structure_pxvmacube160d_126d_slope_v088_signal,
    f01ts_f01_trend_structure_sprtanh10v50_21d_slope_v089_signal,
    f01ts_f01_trend_structure_sprtanh10v50_42d_slope_v090_signal,
    f01ts_f01_trend_structure_sprtanh50v200_63d_slope_v091_signal,
    f01ts_f01_trend_structure_sprtanh50v200_126d_slope_v092_signal,
    f01ts_f01_trend_structure_sprtanh32v160_63d_slope_v093_signal,
    f01ts_f01_trend_structure_emaslope50d_42d_slope_v094_signal,
    f01ts_f01_trend_structure_emaslope50d_95d_slope_v095_signal,
    f01ts_f01_trend_structure_emaslope100d_95d_slope_v096_signal,
    f01ts_f01_trend_structure_emaslope100d_126d_slope_v097_signal,
    f01ts_f01_trend_structure_emaslope200d_126d_slope_v098_signal,
    f01ts_f01_trend_structure_pxvmarank32d_21d_slope_v099_signal,
    f01ts_f01_trend_structure_pxvmarank32d_63d_slope_v100_signal,
    f01ts_f01_trend_structure_pxvmarank95d_63d_slope_v101_signal,
    f01ts_f01_trend_structure_pxvmarank95d_126d_slope_v102_signal,
    f01ts_f01_trend_structure_pxvmarank160d_126d_slope_v103_signal,
    f01ts_f01_trend_structure_slopeanom32d_21d_slope_v104_signal,
    f01ts_f01_trend_structure_slopeanom32d_95d_slope_v105_signal,
    f01ts_f01_trend_structure_slopeanom95d_42d_slope_v106_signal,
    f01ts_f01_trend_structure_slopeanom95d_126d_slope_v107_signal,
    f01ts_f01_trend_structure_slopeanom160d_126d_slope_v108_signal,
    f01ts_f01_trend_structure_distrev15d_21d_slope_v109_signal,
    f01ts_f01_trend_structure_distrev35d_42d_slope_v110_signal,
    f01ts_f01_trend_structure_distrev35d_95d_slope_v111_signal,
    f01ts_f01_trend_structure_distrev75d_95d_slope_v112_signal,
    f01ts_f01_trend_structure_distrev75d_126d_slope_v113_signal,
    f01ts_f01_trend_structure_accel10d_21d_slope_v114_signal,
    f01ts_f01_trend_structure_accel10d_42d_slope_v115_signal,
    f01ts_f01_trend_structure_accel32d_21d_slope_v116_signal,
    f01ts_f01_trend_structure_accel32d_63d_slope_v117_signal,
    f01ts_f01_trend_structure_accel95d_63d_slope_v118_signal,
    f01ts_f01_trend_structure_accel95d_126d_slope_v119_signal,
    f01ts_f01_trend_structure_sprz21v63_42d_slope_v120_signal,
    f01ts_f01_trend_structure_sprz21v63_63d_slope_v121_signal,
    f01ts_f01_trend_structure_sprz63v252_95d_slope_v122_signal,
    f01ts_f01_trend_structure_sprz63v252_126d_slope_v123_signal,
    f01ts_f01_trend_structure_sprz126v504_126d_slope_v124_signal,
    f01ts_f01_trend_structure_slopesm75d_21d_slope_v125_signal,
    f01ts_f01_trend_structure_slopesm75d_63d_slope_v126_signal,
    f01ts_f01_trend_structure_slopesm150d_63d_slope_v127_signal,
    f01ts_f01_trend_structure_slopesm150d_126d_slope_v128_signal,
    f01ts_f01_trend_structure_slopesm300d_126d_slope_v129_signal,
    f01ts_f01_trend_structure_emasma30d_21d_slope_v130_signal,
    f01ts_f01_trend_structure_emasma30d_42d_slope_v131_signal,
    f01ts_f01_trend_structure_emasma75d_21d_slope_v132_signal,
    f01ts_f01_trend_structure_emasma75d_63d_slope_v133_signal,
    f01ts_f01_trend_structure_emasma150d_63d_slope_v134_signal,
    f01ts_f01_trend_structure_emasma150d_126d_slope_v135_signal,
    f01ts_f01_trend_structure_abovefr32d_21d_slope_v136_signal,
    f01ts_f01_trend_structure_abovefr32d_63d_slope_v137_signal,
    f01ts_f01_trend_structure_abovefr95d_42d_slope_v138_signal,
    f01ts_f01_trend_structure_abovefr95d_95d_slope_v139_signal,
    f01ts_f01_trend_structure_abovefr160d_95d_slope_v140_signal,
    f01ts_f01_trend_structure_slead21v42_42d_slope_v141_signal,
    f01ts_f01_trend_structure_slead21v42_75d_slope_v142_signal,
    f01ts_f01_trend_structure_slead42v75_126d_slope_v143_signal,
    f01ts_f01_trend_structure_slead63v95_63d_slope_v144_signal,
    f01ts_f01_trend_structure_slead63v95_126d_slope_v145_signal,
    f01ts_f01_trend_structure_effi42d_21d_slope_v146_signal,
    f01ts_f01_trend_structure_effi42d_42d_slope_v147_signal,
    f01ts_f01_trend_structure_effi95d_63d_slope_v148_signal,
    f01ts_f01_trend_structure_effi95d_126d_slope_v149_signal,
    f01ts_f01_trend_structure_effi189d_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f01_trend_structure_2nd_derivatives_001_150_claude: %d features pass" % n_features)
