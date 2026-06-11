import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
ANN = np.sqrt(252.0)


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (realized-volatility term structure) =====
def _f10_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f10_rvol(closeadj, w):
    r = _f10_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * ANN


def _f10_downside(closeadj, w):
    r = _f10_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_upside(closeadj, w):
    r = _f10_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_term_ratio(closeadj, ws, wl):
    return _f10_rvol(closeadj, ws) / _f10_rvol(closeadj, wl).replace(0, np.nan)


def _f10_voladj_ret(closeadj, w):
    r = _f10_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    v = _f10_rvol(closeadj, w)
    return cum / v.replace(0, np.nan)



# slope of rvol5 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol5r_5d_slope_v001_signal(closeadj):
    u = _f10_rvol(closeadj, 5)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol8 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol8r_5d_slope_v002_signal(closeadj):
    u = _f10_rvol(closeadj, 8)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol10 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol10r_5d_slope_v003_signal(closeadj):
    u = _f10_rvol(closeadj, 10)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol13 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol13r_5d_slope_v004_signal(closeadj):
    u = _f10_rvol(closeadj, 13)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol21r_7d_slope_v005_signal(closeadj):
    u = _f10_rvol(closeadj, 21)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol34 underlier (xform=r) over 11d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol34r_11d_slope_v006_signal(closeadj):
    u = _f10_rvol(closeadj, 34)
    un = u
    b = (un - un.shift(11)) / float(11)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol42r_14d_slope_v007_signal(closeadj):
    u = _f10_rvol(closeadj, 42)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol63r_21d_slope_v008_signal(closeadj):
    u = _f10_rvol(closeadj, 63)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol84 underlier (xform=r) over 28d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol84r_28d_slope_v009_signal(closeadj):
    u = _f10_rvol(closeadj, 84)
    un = u
    b = (un - un.shift(28)) / float(28)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol126r_42d_slope_v010_signal(closeadj):
    u = _f10_rvol(closeadj, 126)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol189 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol189r_63d_slope_v011_signal(closeadj):
    u = _f10_rvol(closeadj, 189)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rvol252 underlier (xform=r) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rvol252r_84d_slope_v012_signal(closeadj):
    u = _f10_rvol(closeadj, 252)
    un = u
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr5v8 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr5v8r_5d_slope_v013_signal(closeadj):
    u = _f10_term_ratio(closeadj, 5, 8)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr8v13 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr8v13r_5d_slope_v014_signal(closeadj):
    u = _f10_term_ratio(closeadj, 8, 13)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr13v21 underlier (xform=r) over 6d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr13v21r_6d_slope_v015_signal(closeadj):
    u = _f10_term_ratio(closeadj, 13, 21)
    un = u
    b = (un - un.shift(6)) / float(6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr21v34 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr21v34r_10d_slope_v016_signal(closeadj):
    u = _f10_term_ratio(closeadj, 21, 34)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr34v55 underlier (xform=r) over 17d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr34v55r_17d_slope_v017_signal(closeadj):
    u = _f10_term_ratio(closeadj, 34, 55)
    un = u
    b = (un - un.shift(17)) / float(17)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr55v89 underlier (xform=r) over 27d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr55v89r_27d_slope_v018_signal(closeadj):
    u = _f10_term_ratio(closeadj, 55, 89)
    un = u
    b = (un - un.shift(27)) / float(27)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr89v126 underlier (xform=r) over 44d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr89v126r_44d_slope_v019_signal(closeadj):
    u = _f10_term_ratio(closeadj, 89, 126)
    un = u
    b = (un - un.shift(44)) / float(44)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr126v189 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr126v189r_63d_slope_v020_signal(closeadj):
    u = _f10_term_ratio(closeadj, 126, 189)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr189v252 underlier (xform=r) over 94d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr189v252r_94d_slope_v021_signal(closeadj):
    u = _f10_term_ratio(closeadj, 189, 252)
    un = u
    b = (un - un.shift(94)) / float(94)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr252v378 underlier (xform=r) over 126d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr252v378r_126d_slope_v022_signal(closeadj):
    u = _f10_term_ratio(closeadj, 252, 378)
    un = u
    b = (un - un.shift(126)) / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tr378v504 underlier (xform=r) over 189d (math 1st derivative)
def f10rv_f10_realized_volatility_term_tr378v504r_189d_slope_v023_signal(closeadj):
    u = _f10_term_ratio(closeadj, 378, 504)
    un = u
    b = (un - un.shift(189)) / float(189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw5v63 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw5v63r_5d_slope_v024_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 5), 252) - _rank(_f10_rvol(closeadj, 63), 252)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw5v126 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw5v126r_5d_slope_v025_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 5), 252) - _rank(_f10_rvol(closeadj, 126), 252)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw5v252 underlier (xform=d) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw5v252d_5d_slope_v026_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 5), 504) - _rank(_f10_rvol(closeadj, 252), 504)
    un = u - u.ewm(span=15, min_periods=5).mean()
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw10v63 underlier (xform=r) over 8d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw10v63r_8d_slope_v027_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 10), 252) - _rank(_f10_rvol(closeadj, 63), 252)
    un = u
    b = (un - un.shift(8)) / float(8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw21v126 underlier (xform=r) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw21v126r_13d_slope_v028_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 21), 252) - _rank(_f10_rvol(closeadj, 126), 252)
    un = u
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw21v252 underlier (xform=r) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw21v252r_13d_slope_v029_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 21), 504) - _rank(_f10_rvol(closeadj, 252), 504)
    un = u
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw42v252 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw42v252r_24d_slope_v030_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 42), 504) - _rank(_f10_rvol(closeadj, 252), 504)
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw63v252 underlier (xform=r) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw63v252r_34d_slope_v031_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 63), 504) - _rank(_f10_rvol(closeadj, 252), 504)
    un = u
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw63v504 underlier (xform=r) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw63v504r_34d_slope_v032_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 63), 504) - _rank(_f10_rvol(closeadj, 504), 504)
    un = u
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trw126v504 underlier (xform=r) over 66d (math 1st derivative)
def f10rv_f10_realized_volatility_term_trw126v504r_66d_slope_v033_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 126), 504) - _rank(_f10_rvol(closeadj, 504), 504)
    un = u
    b = (un - un.shift(66)) / float(66)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls5v21 underlier (xform=r) over 6d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls5v21r_6d_slope_v034_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 5).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    un = u
    b = (un - un.shift(6)) / float(6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls10v42 underlier (xform=r) over 9d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls10v42r_9d_slope_v035_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 10).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 42).replace(0, np.nan))
    un = u
    b = (un - un.shift(9)) / float(9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls21v63 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls21v63r_14d_slope_v036_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 63).replace(0, np.nan))
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls21v126 underlier (xform=d) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls21v126d_14d_slope_v037_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    un = u - u.ewm(span=42, min_periods=14).mean()
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls42v126 underlier (xform=r) over 25d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls42v126r_25d_slope_v038_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 42).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    un = u
    b = (un - un.shift(25)) / float(25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls63v252 underlier (xform=r) over 35d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls63v252r_35d_slope_v039_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    un = u
    b = (un - un.shift(35)) / float(35)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls126v252 underlier (xform=r) over 67d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls126v252r_67d_slope_v040_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 126).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    un = u
    b = (un - un.shift(67)) / float(67)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ls63v189 underlier (xform=r) over 35d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ls63v189r_35d_slope_v041_signal(closeadj):
    u = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 189).replace(0, np.nan))
    un = u
    b = (un - un.shift(35)) / float(35)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf5_21_63 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf5_21_63r_10d_slope_v042_signal(closeadj):
    u = (_f10_rvol(closeadj, 5) + _f10_rvol(closeadj, 63)) / 2.0 - _f10_rvol(closeadj, 21)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf10_42_126 underlier (xform=r) over 17d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf10_42_126r_17d_slope_v043_signal(closeadj):
    u = (_f10_rvol(closeadj, 10) + _f10_rvol(closeadj, 126)) / 2.0 - _f10_rvol(closeadj, 42)
    un = u
    b = (un - un.shift(17)) / float(17)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf21_63_126 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf21_63_126r_24d_slope_v044_signal(closeadj):
    u = (_f10_rvol(closeadj, 21) + _f10_rvol(closeadj, 126)) / 2.0 - _f10_rvol(closeadj, 63)
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf21_63_252 underlier (xform=d) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf21_63_252d_24d_slope_v045_signal(closeadj):
    u = (_f10_rvol(closeadj, 21) + _f10_rvol(closeadj, 252)) / 2.0 - _f10_rvol(closeadj, 63)
    un = u - u.ewm(span=72, min_periods=24).mean()
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf5_63_252 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf5_63_252r_24d_slope_v046_signal(closeadj):
    u = (_f10_rvol(closeadj, 5) + _f10_rvol(closeadj, 252)) / 2.0 - _f10_rvol(closeadj, 63)
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf42_84_189 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf42_84_189r_31d_slope_v047_signal(closeadj):
    u = (_f10_rvol(closeadj, 42) + _f10_rvol(closeadj, 189)) / 2.0 - _f10_rvol(closeadj, 84)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf8_21_55 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf8_21_55r_10d_slope_v048_signal(closeadj):
    u = (_f10_rvol(closeadj, 8) + _f10_rvol(closeadj, 55)) / 2.0 - _f10_rvol(closeadj, 21)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bf63_126_252 underlier (xform=r) over 45d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bf63_126_252r_45d_slope_v049_signal(closeadj):
    u = (_f10_rvol(closeadj, 63) + _f10_rvol(closeadj, 252)) / 2.0 - _f10_rvol(closeadj, 126)
    un = u
    b = (un - un.shift(45)) / float(45)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi10 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi10r_5d_slope_v050_signal(closeadj):
    u = _f10_downside(closeadj, 10)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi21r_7d_slope_v051_signal(closeadj):
    u = _f10_downside(closeadj, 21)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi42r_14d_slope_v052_signal(closeadj):
    u = _f10_downside(closeadj, 42)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi63r_21d_slope_v053_signal(closeadj):
    u = _f10_downside(closeadj, 63)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi126r_42d_slope_v054_signal(closeadj):
    u = _f10_downside(closeadj, 126)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi189 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi189r_63d_slope_v055_signal(closeadj):
    u = _f10_downside(closeadj, 189)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dsemi252 underlier (xform=r) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dsemi252r_84d_slope_v056_signal(closeadj):
    u = _f10_downside(closeadj, 252)
    un = u
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi10 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi10r_5d_slope_v057_signal(closeadj):
    u = _f10_upside(closeadj, 10)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi21r_7d_slope_v058_signal(closeadj):
    u = _f10_upside(closeadj, 21)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi42r_14d_slope_v059_signal(closeadj):
    u = _f10_upside(closeadj, 42)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi63r_21d_slope_v060_signal(closeadj):
    u = _f10_upside(closeadj, 63)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi126r_42d_slope_v061_signal(closeadj):
    u = _f10_upside(closeadj, 126)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of usemi252 underlier (xform=r) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_usemi252r_84d_slope_v062_signal(closeadj):
    u = _f10_upside(closeadj, 252)
    un = u
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym13 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym13r_5d_slope_v063_signal(closeadj):
    d = _f10_downside(closeadj, 13)
    up = _f10_upside(closeadj, 13)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym21r_7d_slope_v064_signal(closeadj):
    d = _f10_downside(closeadj, 21)
    up = _f10_upside(closeadj, 21)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym42r_14d_slope_v065_signal(closeadj):
    d = _f10_downside(closeadj, 42)
    up = _f10_upside(closeadj, 42)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym63r_21d_slope_v066_signal(closeadj):
    d = _f10_downside(closeadj, 63)
    up = _f10_upside(closeadj, 63)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym126r_42d_slope_v067_signal(closeadj):
    d = _f10_downside(closeadj, 126)
    up = _f10_upside(closeadj, 126)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asym252 underlier (xform=r) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_asym252r_84d_slope_v068_signal(closeadj):
    d = _f10_downside(closeadj, 252)
    up = _f10_upside(closeadj, 252)
    u = (d - up) / (d + up).replace(0, np.nan)
    un = u
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of udr21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_udr21r_7d_slope_v069_signal(closeadj):
    u = _f10_downside(closeadj, 21) / _f10_upside(closeadj, 21).replace(0, np.nan)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of udr42 underlier (xform=d) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_udr42d_14d_slope_v070_signal(closeadj):
    u = _f10_downside(closeadj, 42) / _f10_upside(closeadj, 42).replace(0, np.nan)
    un = u - u.ewm(span=42, min_periods=14).mean()
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of udr63 underlier (xform=d) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_udr63d_21d_slope_v071_signal(closeadj):
    u = _f10_downside(closeadj, 63) / _f10_upside(closeadj, 63).replace(0, np.nan)
    un = u - u.ewm(span=63, min_periods=21).mean()
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of udr126 underlier (xform=d) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_udr126d_42d_slope_v072_signal(closeadj):
    u = _f10_downside(closeadj, 126) / _f10_upside(closeadj, 126).replace(0, np.nan)
    un = u - u.ewm(span=126, min_periods=42).mean()
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of udr252 underlier (xform=d) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_udr252d_84d_slope_v073_signal(closeadj):
    u = _f10_downside(closeadj, 252) / _f10_upside(closeadj, 252).replace(0, np.nan)
    un = u - u.ewm(span=252, min_periods=84).mean()
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone10in126 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone10in126r_5d_slope_v074_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 10), 126)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone21in252 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone21in252r_10d_slope_v075_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 21), 252)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone42in252 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone42in252r_21d_slope_v076_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 42), 252)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone63in252 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone63in252r_31d_slope_v077_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 63), 252)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone126in504 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone126in504r_63d_slope_v078_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 126), 504)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cone252in504 underlier (xform=r) over 126d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cone252in504r_126d_slope_v079_signal(closeadj):
    u = _rank(_f10_rvol(closeadj, 252), 504)
    un = u
    b = (un - un.shift(126)) / float(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var10 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var10r_5d_slope_v080_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 10)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var21r_7d_slope_v081_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 21)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var42r_14d_slope_v082_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 42)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var63r_21d_slope_v083_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 63)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var126r_42d_slope_v084_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 126)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of var189 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_var189r_63d_slope_v085_signal(closeadj):
    u = _f10_voladj_ret(closeadj, 189)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vov5in42 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vov5in42r_10d_slope_v086_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    u = _std(v, 42) / _mean(v, 42).replace(0, np.nan)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vov10in63 underlier (xform=r) over 15d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vov10in63r_15d_slope_v087_signal(closeadj):
    v = _f10_rvol(closeadj, 10)
    u = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    un = u
    b = (un - un.shift(15)) / float(15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vov21in63 underlier (xform=r) over 15d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vov21in63r_15d_slope_v088_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    u = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    un = u
    b = (un - un.shift(15)) / float(15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vov21in126 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vov21in126r_31d_slope_v089_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    u = _std(v, 126) / _mean(v, 126).replace(0, np.nan)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ewm04 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ewm04r_10d_slope_v090_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    u = np.sqrt(r2.ewm(alpha=0.04, min_periods=21).mean()) * ANN
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ewm08 underlier (xform=d) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ewm08d_10d_slope_v091_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    u = np.sqrt(r2.ewm(alpha=0.08, min_periods=21).mean()) * ANN
    un = u - u.ewm(span=30, min_periods=10).mean()
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ewm15 underlier (xform=p) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ewm15p_10d_slope_v092_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    u = np.sqrt(r2.ewm(alpha=0.15, min_periods=21).mean()) * ANN
    un = _rank(u, 80)
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of l2l1_21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_l2l1_21r_7d_slope_v093_signal(closeadj):
    r = _f10_logret(closeadj)
    u = r.rolling(21, min_periods=10).std() / r.abs().rolling(21, min_periods=10).mean().replace(0, np.nan)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of l2l1_63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_l2l1_63r_21d_slope_v094_signal(closeadj):
    r = _f10_logret(closeadj)
    u = r.rolling(63, min_periods=31).std() / r.abs().rolling(63, min_periods=31).mean().replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of l2l1_126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_l2l1_126r_42d_slope_v095_signal(closeadj):
    r = _f10_logret(closeadj)
    u = r.rolling(126, min_periods=63).std() / r.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of skew42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_skew42r_14d_slope_v096_signal(closeadj):
    u = _f10_logret(closeadj).rolling(42, min_periods=21).skew()
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of skew126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_skew126r_42d_slope_v097_signal(closeadj):
    u = _f10_logret(closeadj).rolling(126, min_periods=63).skew()
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of kurt63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_kurt63r_21d_slope_v098_signal(closeadj):
    u = _f10_logret(closeadj).rolling(63, min_periods=31).kurt()
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of kurt126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_kurt126r_42d_slope_v099_signal(closeadj):
    u = _f10_logret(closeadj).rolling(126, min_periods=63).kurt()
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cdisp underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_cdispr_21d_slope_v100_signal(closeadj):
    st = pd.concat([_f10_rvol(closeadj, 5), _f10_rvol(closeadj, 21), _f10_rvol(closeadj, 63), _f10_rvol(closeadj, 126), _f10_rvol(closeadj, 252)], axis=1)
    u = st.std(axis=1) / st.mean(axis=1).replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of clevel underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_clevelr_21d_slope_v101_signal(closeadj):
    st = pd.concat([_f10_rvol(closeadj, 5), _f10_rvol(closeadj, 21), _f10_rvol(closeadj, 63), _f10_rvol(closeadj, 126), _f10_rvol(closeadj, 252)], axis=1)
    u = st.mean(axis=1)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of regdist21 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_regdist21r_21d_slope_v102_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q75 = v.rolling(252, min_periods=126).quantile(0.75)
    q25 = v.rolling(252, min_periods=126).quantile(0.25)
    med = v.rolling(252, min_periods=126).median()
    u = (v - med) / (q75 - q25).replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of regdist63 underlier (xform=d) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_regdist63d_21d_slope_v103_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    u = _rank(v, 504)
    un = u - u.ewm(span=63, min_periods=21).mean()
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vratio21 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vratio21r_21d_slope_v104_signal(closeadj):
    r = _f10_logret(closeadj)
    r21 = r.rolling(21, min_periods=21).sum()
    v1 = (r ** 2).rolling(252, min_periods=126).mean()
    v21 = (r21 ** 2).rolling(252, min_periods=126).mean()
    u = v21 / (21.0 * v1).replace(0, np.nan) - 1.0
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of jumpvar63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_jumpvar63r_21d_slope_v105_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    u = r2.rolling(63, min_periods=21).max() / r2.rolling(63, min_periods=21).sum().replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of maxdd63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_maxdd63r_21d_slope_v106_signal(closeadj):
    rp = closeadj.rolling(63, min_periods=21).max()
    u = (closeadj / rp.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).min()
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of semispr126 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_semispr126r_21d_slope_v107_signal(closeadj):
    u = _f10_downside(closeadj, 126) - _f10_upside(closeadj, 126)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of rv5agg63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_rv5agg63r_21d_slope_v108_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    u = r5.rolling(63, min_periods=21).std() * np.sqrt(252.0 / 5.0)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of madvol42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_madvol42r_14d_slope_v109_signal(closeadj):
    u = _f10_logret(closeadj).abs().rolling(42, min_periods=21).mean() * ANN
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inv10v126 underlier (xform=r) over 8d (math 1st derivative)
def f10rv_f10_realized_volatility_term_inv10v126r_8d_slope_v110_signal(closeadj):
    vs = _f10_rvol(closeadj, 10)
    vl = _f10_rvol(closeadj, 126)
    g = (vs - vl) / vl.replace(0, np.nan)
    u = g - g.ewm(span=126, min_periods=31).mean()
    un = u
    b = (un - un.shift(8)) / float(8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inv21v252 underlier (xform=r) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_inv21v252r_13d_slope_v111_signal(closeadj):
    vs = _f10_rvol(closeadj, 21)
    vl = _f10_rvol(closeadj, 252)
    g = (vs - vl) / vl.replace(0, np.nan)
    u = g - g.ewm(span=252, min_periods=63).mean()
    un = u
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inv42v252 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_inv42v252r_24d_slope_v112_signal(closeadj):
    vs = _f10_rvol(closeadj, 42)
    vl = _f10_rvol(closeadj, 252)
    g = (vs - vl) / vl.replace(0, np.nan)
    u = g - g.ewm(span=252, min_periods=63).mean()
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inv63v252 underlier (xform=d) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_inv63v252d_34d_slope_v113_signal(closeadj):
    vs = _f10_rvol(closeadj, 63)
    vl = _f10_rvol(closeadj, 252)
    g = (vs - vl) / vl.replace(0, np.nan)
    u = g - g.ewm(span=252, min_periods=63).mean()
    un = u - u.ewm(span=102, min_periods=34).mean()
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of inv63v504 underlier (xform=r) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_inv63v504r_34d_slope_v114_signal(closeadj):
    vs = _f10_rvol(closeadj, 63)
    vl = _f10_rvol(closeadj, 504)
    g = (vs - vl) / vl.replace(0, np.nan)
    u = g - g.ewm(span=504, min_periods=126).mean()
    un = u
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dterm21v126 underlier (xform=r) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dterm21v126r_13d_slope_v115_signal(closeadj):
    u = _f10_downside(closeadj, 21) / _f10_downside(closeadj, 126).replace(0, np.nan)
    un = u
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dterm21v252 underlier (xform=d) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dterm21v252d_13d_slope_v116_signal(closeadj):
    u = _f10_downside(closeadj, 21) / _f10_downside(closeadj, 252).replace(0, np.nan)
    un = u - u.ewm(span=39, min_periods=13).mean()
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dterm63v252 underlier (xform=r) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dterm63v252r_34d_slope_v117_signal(closeadj):
    u = _f10_downside(closeadj, 63) / _f10_downside(closeadj, 252).replace(0, np.nan)
    un = u
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dterm42v189 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dterm42v189r_24d_slope_v118_signal(closeadj):
    u = _f10_downside(closeadj, 42) / _f10_downside(closeadj, 189).replace(0, np.nan)
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of uterm21v126 underlier (xform=r) over 13d (math 1st derivative)
def f10rv_f10_realized_volatility_term_uterm21v126r_13d_slope_v119_signal(closeadj):
    u = _f10_upside(closeadj, 21) / _f10_upside(closeadj, 126).replace(0, np.nan)
    un = u
    b = (un - un.shift(13)) / float(13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of uterm63v252 underlier (xform=r) over 34d (math 1st derivative)
def f10rv_f10_realized_volatility_term_uterm63v252r_34d_slope_v120_signal(closeadj):
    u = _f10_upside(closeadj, 63) / _f10_upside(closeadj, 252).replace(0, np.nan)
    un = u
    b = (un - un.shift(34)) / float(34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of uterm42v189 underlier (xform=r) over 24d (math 1st derivative)
def f10rv_f10_realized_volatility_term_uterm42v189r_24d_slope_v121_signal(closeadj):
    u = _f10_upside(closeadj, 42) / _f10_upside(closeadj, 189).replace(0, np.nan)
    un = u
    b = (un - un.shift(24)) / float(24)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dcone21in252 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dcone21in252r_10d_slope_v122_signal(closeadj):
    u = _rank(_f10_downside(closeadj, 21), 252)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dcone63in252 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dcone63in252r_31d_slope_v123_signal(closeadj):
    u = _rank(_f10_downside(closeadj, 63), 252)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dcone42in252 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dcone42in252r_21d_slope_v124_signal(closeadj):
    u = _rank(_f10_downside(closeadj, 42), 252)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dcone126in504 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dcone126in504r_63d_slope_v125_signal(closeadj):
    u = _rank(_f10_downside(closeadj, 126), 504)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ucone21in252 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ucone21in252r_10d_slope_v126_signal(closeadj):
    u = _rank(_f10_upside(closeadj, 21), 252)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ucone63in252 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ucone63in252r_31d_slope_v127_signal(closeadj):
    u = _rank(_f10_upside(closeadj, 63), 252)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ucone126in504 underlier (xform=r) over 63d (math 1st derivative)
def f10rv_f10_realized_volatility_term_ucone126in504r_63d_slope_v128_signal(closeadj):
    u = _rank(_f10_upside(closeadj, 126), 504)
    un = u
    b = (un - un.shift(63)) / float(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vovx5in21 underlier (xform=r) over 5d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vovx5in21r_5d_slope_v129_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    u = _std(v, 21) / _mean(v, 21).replace(0, np.nan)
    un = u
    b = (un - un.shift(5)) / float(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vovx10in42 underlier (xform=r) over 10d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vovx10in42r_10d_slope_v130_signal(closeadj):
    v = _f10_rvol(closeadj, 10)
    u = _std(v, 42) / _mean(v, 42).replace(0, np.nan)
    un = u
    b = (un - un.shift(10)) / float(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vovx42in126 underlier (xform=r) over 31d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vovx42in126r_31d_slope_v131_signal(closeadj):
    v = _f10_rvol(closeadj, 42)
    u = _std(v, 126) / _mean(v, 126).replace(0, np.nan)
    un = u
    b = (un - un.shift(31)) / float(31)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vovx63in189 underlier (xform=r) over 47d (math 1st derivative)
def f10rv_f10_realized_volatility_term_vovx63in189r_47d_slope_v132_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    u = _std(v, 189) / _mean(v, 189).replace(0, np.nan)
    un = u
    b = (un - un.shift(47)) / float(47)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of estgap21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_estgap21r_7d_slope_v133_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    ew = np.sqrt(r2.ewm(alpha=0.1, min_periods=21).mean()) * ANN
    sm = _f10_rvol(closeadj, 21)
    u = (ew - sm) / sm.replace(0, np.nan)
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of estgap63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_estgap63r_21d_slope_v134_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    ew = np.sqrt(r2.ewm(alpha=0.06, min_periods=21).mean()) * ANN
    sm = _f10_rvol(closeadj, 63)
    u = (ew - sm) / sm.replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of estgap126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_estgap126r_42d_slope_v135_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    ew = np.sqrt(r2.ewm(alpha=0.04, min_periods=21).mean()) * ANN
    sm = _f10_rvol(closeadj, 126)
    u = (ew - sm) / sm.replace(0, np.nan)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of estgap252 underlier (xform=r) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_estgap252r_84d_slope_v136_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    ew = np.sqrt(r2.ewm(alpha=0.02, min_periods=21).mean()) * ANN
    sm = _f10_rvol(closeadj, 252)
    u = (ew - sm) / sm.replace(0, np.nan)
    un = u
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bipow42 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bipow42r_14d_slope_v137_signal(closeadj):
    r = _f10_logret(closeadj)
    bp = (r.abs() * r.abs().shift(1)).rolling(42, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(42, min_periods=21).sum()
    u = 1.0 - bp / rv.replace(0, np.nan)
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bipow63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bipow63r_21d_slope_v138_signal(closeadj):
    r = _f10_logret(closeadj)
    bp = (r.abs() * r.abs().shift(1)).rolling(63, min_periods=31).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=31).sum()
    u = 1.0 - bp / rv.replace(0, np.nan)
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bipow126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_bipow126r_42d_slope_v139_signal(closeadj):
    r = _f10_logret(closeadj)
    bp = (r.abs() * r.abs().shift(1)).rolling(126, min_periods=63).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(126, min_periods=63).sum()
    u = 1.0 - bp / rv.replace(0, np.nan)
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mad21 underlier (xform=r) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_mad21r_7d_slope_v140_signal(closeadj):
    u = _f10_logret(closeadj).abs().rolling(21, min_periods=10).mean() * ANN
    un = u
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mad63 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_mad63r_21d_slope_v141_signal(closeadj):
    u = _f10_logret(closeadj).abs().rolling(63, min_periods=31).mean() * ANN
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mad126 underlier (xform=r) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_mad126r_42d_slope_v142_signal(closeadj):
    u = _f10_logret(closeadj).abs().rolling(126, min_periods=63).mean() * ANN
    un = u
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of wbf5_42_252 underlier (xform=r) over 14d (math 1st derivative)
def f10rv_f10_realized_volatility_term_wbf5_42_252r_14d_slope_v143_signal(closeadj):
    gm = np.sqrt((_f10_rvol(closeadj, 5) * _f10_rvol(closeadj, 252)).clip(lower=0))
    u = _f10_rvol(closeadj, 42) / gm.replace(0, np.nan) - 1.0
    un = u
    b = (un - un.shift(14)) / float(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of wbf10_63_252 underlier (xform=r) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_wbf10_63_252r_21d_slope_v144_signal(closeadj):
    gm = np.sqrt((_f10_rvol(closeadj, 10) * _f10_rvol(closeadj, 252)).clip(lower=0))
    u = _f10_rvol(closeadj, 63) / gm.replace(0, np.nan) - 1.0
    un = u
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of wbf21_84_252 underlier (xform=r) over 28d (math 1st derivative)
def f10rv_f10_realized_volatility_term_wbf21_84_252r_28d_slope_v145_signal(closeadj):
    gm = np.sqrt((_f10_rvol(closeadj, 21) * _f10_rvol(closeadj, 252)).clip(lower=0))
    u = _f10_rvol(closeadj, 84) / gm.replace(0, np.nan) - 1.0
    un = u
    b = (un - un.shift(28)) / float(28)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of wbf13_55_189 underlier (xform=r) over 18d (math 1st derivative)
def f10rv_f10_realized_volatility_term_wbf13_55_189r_18d_slope_v146_signal(closeadj):
    gm = np.sqrt((_f10_rvol(closeadj, 13) * _f10_rvol(closeadj, 189)).clip(lower=0))
    u = _f10_rvol(closeadj, 55) / gm.replace(0, np.nan) - 1.0
    un = u
    b = (un - un.shift(18)) / float(18)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dshare21 underlier (xform=d) over 7d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dshare21d_7d_slope_v147_signal(closeadj):
    u = _f10_downside(closeadj, 21) / _f10_rvol(closeadj, 21).replace(0, np.nan)
    un = u - u.ewm(span=21, min_periods=7).mean()
    b = (un - un.shift(7)) / float(7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dshare63 underlier (xform=p) over 21d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dshare63p_21d_slope_v148_signal(closeadj):
    u = _f10_downside(closeadj, 63) / _f10_rvol(closeadj, 63).replace(0, np.nan)
    un = _rank(u, 168)
    b = (un - un.shift(21)) / float(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dshare126 underlier (xform=p) over 42d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dshare126p_42d_slope_v149_signal(closeadj):
    u = _f10_downside(closeadj, 126) / _f10_rvol(closeadj, 126).replace(0, np.nan)
    un = _rank(u, 336)
    b = (un - un.shift(42)) / float(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dshare252 underlier (xform=p) over 84d (math 1st derivative)
def f10rv_f10_realized_volatility_term_dshare252p_84d_slope_v150_signal(closeadj):
    u = _f10_downside(closeadj, 252) / _f10_rvol(closeadj, 252).replace(0, np.nan)
    un = _rank(u, 672)
    b = (un - un.shift(84)) / float(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol5r_5d_slope_v001_signal,
    f10rv_f10_realized_volatility_term_rvol8r_5d_slope_v002_signal,
    f10rv_f10_realized_volatility_term_rvol10r_5d_slope_v003_signal,
    f10rv_f10_realized_volatility_term_rvol13r_5d_slope_v004_signal,
    f10rv_f10_realized_volatility_term_rvol21r_7d_slope_v005_signal,
    f10rv_f10_realized_volatility_term_rvol34r_11d_slope_v006_signal,
    f10rv_f10_realized_volatility_term_rvol42r_14d_slope_v007_signal,
    f10rv_f10_realized_volatility_term_rvol63r_21d_slope_v008_signal,
    f10rv_f10_realized_volatility_term_rvol84r_28d_slope_v009_signal,
    f10rv_f10_realized_volatility_term_rvol126r_42d_slope_v010_signal,
    f10rv_f10_realized_volatility_term_rvol189r_63d_slope_v011_signal,
    f10rv_f10_realized_volatility_term_rvol252r_84d_slope_v012_signal,
    f10rv_f10_realized_volatility_term_tr5v8r_5d_slope_v013_signal,
    f10rv_f10_realized_volatility_term_tr8v13r_5d_slope_v014_signal,
    f10rv_f10_realized_volatility_term_tr13v21r_6d_slope_v015_signal,
    f10rv_f10_realized_volatility_term_tr21v34r_10d_slope_v016_signal,
    f10rv_f10_realized_volatility_term_tr34v55r_17d_slope_v017_signal,
    f10rv_f10_realized_volatility_term_tr55v89r_27d_slope_v018_signal,
    f10rv_f10_realized_volatility_term_tr89v126r_44d_slope_v019_signal,
    f10rv_f10_realized_volatility_term_tr126v189r_63d_slope_v020_signal,
    f10rv_f10_realized_volatility_term_tr189v252r_94d_slope_v021_signal,
    f10rv_f10_realized_volatility_term_tr252v378r_126d_slope_v022_signal,
    f10rv_f10_realized_volatility_term_tr378v504r_189d_slope_v023_signal,
    f10rv_f10_realized_volatility_term_trw5v63r_5d_slope_v024_signal,
    f10rv_f10_realized_volatility_term_trw5v126r_5d_slope_v025_signal,
    f10rv_f10_realized_volatility_term_trw5v252d_5d_slope_v026_signal,
    f10rv_f10_realized_volatility_term_trw10v63r_8d_slope_v027_signal,
    f10rv_f10_realized_volatility_term_trw21v126r_13d_slope_v028_signal,
    f10rv_f10_realized_volatility_term_trw21v252r_13d_slope_v029_signal,
    f10rv_f10_realized_volatility_term_trw42v252r_24d_slope_v030_signal,
    f10rv_f10_realized_volatility_term_trw63v252r_34d_slope_v031_signal,
    f10rv_f10_realized_volatility_term_trw63v504r_34d_slope_v032_signal,
    f10rv_f10_realized_volatility_term_trw126v504r_66d_slope_v033_signal,
    f10rv_f10_realized_volatility_term_ls5v21r_6d_slope_v034_signal,
    f10rv_f10_realized_volatility_term_ls10v42r_9d_slope_v035_signal,
    f10rv_f10_realized_volatility_term_ls21v63r_14d_slope_v036_signal,
    f10rv_f10_realized_volatility_term_ls21v126d_14d_slope_v037_signal,
    f10rv_f10_realized_volatility_term_ls42v126r_25d_slope_v038_signal,
    f10rv_f10_realized_volatility_term_ls63v252r_35d_slope_v039_signal,
    f10rv_f10_realized_volatility_term_ls126v252r_67d_slope_v040_signal,
    f10rv_f10_realized_volatility_term_ls63v189r_35d_slope_v041_signal,
    f10rv_f10_realized_volatility_term_bf5_21_63r_10d_slope_v042_signal,
    f10rv_f10_realized_volatility_term_bf10_42_126r_17d_slope_v043_signal,
    f10rv_f10_realized_volatility_term_bf21_63_126r_24d_slope_v044_signal,
    f10rv_f10_realized_volatility_term_bf21_63_252d_24d_slope_v045_signal,
    f10rv_f10_realized_volatility_term_bf5_63_252r_24d_slope_v046_signal,
    f10rv_f10_realized_volatility_term_bf42_84_189r_31d_slope_v047_signal,
    f10rv_f10_realized_volatility_term_bf8_21_55r_10d_slope_v048_signal,
    f10rv_f10_realized_volatility_term_bf63_126_252r_45d_slope_v049_signal,
    f10rv_f10_realized_volatility_term_dsemi10r_5d_slope_v050_signal,
    f10rv_f10_realized_volatility_term_dsemi21r_7d_slope_v051_signal,
    f10rv_f10_realized_volatility_term_dsemi42r_14d_slope_v052_signal,
    f10rv_f10_realized_volatility_term_dsemi63r_21d_slope_v053_signal,
    f10rv_f10_realized_volatility_term_dsemi126r_42d_slope_v054_signal,
    f10rv_f10_realized_volatility_term_dsemi189r_63d_slope_v055_signal,
    f10rv_f10_realized_volatility_term_dsemi252r_84d_slope_v056_signal,
    f10rv_f10_realized_volatility_term_usemi10r_5d_slope_v057_signal,
    f10rv_f10_realized_volatility_term_usemi21r_7d_slope_v058_signal,
    f10rv_f10_realized_volatility_term_usemi42r_14d_slope_v059_signal,
    f10rv_f10_realized_volatility_term_usemi63r_21d_slope_v060_signal,
    f10rv_f10_realized_volatility_term_usemi126r_42d_slope_v061_signal,
    f10rv_f10_realized_volatility_term_usemi252r_84d_slope_v062_signal,
    f10rv_f10_realized_volatility_term_asym13r_5d_slope_v063_signal,
    f10rv_f10_realized_volatility_term_asym21r_7d_slope_v064_signal,
    f10rv_f10_realized_volatility_term_asym42r_14d_slope_v065_signal,
    f10rv_f10_realized_volatility_term_asym63r_21d_slope_v066_signal,
    f10rv_f10_realized_volatility_term_asym126r_42d_slope_v067_signal,
    f10rv_f10_realized_volatility_term_asym252r_84d_slope_v068_signal,
    f10rv_f10_realized_volatility_term_udr21r_7d_slope_v069_signal,
    f10rv_f10_realized_volatility_term_udr42d_14d_slope_v070_signal,
    f10rv_f10_realized_volatility_term_udr63d_21d_slope_v071_signal,
    f10rv_f10_realized_volatility_term_udr126d_42d_slope_v072_signal,
    f10rv_f10_realized_volatility_term_udr252d_84d_slope_v073_signal,
    f10rv_f10_realized_volatility_term_cone10in126r_5d_slope_v074_signal,
    f10rv_f10_realized_volatility_term_cone21in252r_10d_slope_v075_signal,
    f10rv_f10_realized_volatility_term_cone42in252r_21d_slope_v076_signal,
    f10rv_f10_realized_volatility_term_cone63in252r_31d_slope_v077_signal,
    f10rv_f10_realized_volatility_term_cone126in504r_63d_slope_v078_signal,
    f10rv_f10_realized_volatility_term_cone252in504r_126d_slope_v079_signal,
    f10rv_f10_realized_volatility_term_var10r_5d_slope_v080_signal,
    f10rv_f10_realized_volatility_term_var21r_7d_slope_v081_signal,
    f10rv_f10_realized_volatility_term_var42r_14d_slope_v082_signal,
    f10rv_f10_realized_volatility_term_var63r_21d_slope_v083_signal,
    f10rv_f10_realized_volatility_term_var126r_42d_slope_v084_signal,
    f10rv_f10_realized_volatility_term_var189r_63d_slope_v085_signal,
    f10rv_f10_realized_volatility_term_vov5in42r_10d_slope_v086_signal,
    f10rv_f10_realized_volatility_term_vov10in63r_15d_slope_v087_signal,
    f10rv_f10_realized_volatility_term_vov21in63r_15d_slope_v088_signal,
    f10rv_f10_realized_volatility_term_vov21in126r_31d_slope_v089_signal,
    f10rv_f10_realized_volatility_term_ewm04r_10d_slope_v090_signal,
    f10rv_f10_realized_volatility_term_ewm08d_10d_slope_v091_signal,
    f10rv_f10_realized_volatility_term_ewm15p_10d_slope_v092_signal,
    f10rv_f10_realized_volatility_term_l2l1_21r_7d_slope_v093_signal,
    f10rv_f10_realized_volatility_term_l2l1_63r_21d_slope_v094_signal,
    f10rv_f10_realized_volatility_term_l2l1_126r_42d_slope_v095_signal,
    f10rv_f10_realized_volatility_term_skew42r_14d_slope_v096_signal,
    f10rv_f10_realized_volatility_term_skew126r_42d_slope_v097_signal,
    f10rv_f10_realized_volatility_term_kurt63r_21d_slope_v098_signal,
    f10rv_f10_realized_volatility_term_kurt126r_42d_slope_v099_signal,
    f10rv_f10_realized_volatility_term_cdispr_21d_slope_v100_signal,
    f10rv_f10_realized_volatility_term_clevelr_21d_slope_v101_signal,
    f10rv_f10_realized_volatility_term_regdist21r_21d_slope_v102_signal,
    f10rv_f10_realized_volatility_term_regdist63d_21d_slope_v103_signal,
    f10rv_f10_realized_volatility_term_vratio21r_21d_slope_v104_signal,
    f10rv_f10_realized_volatility_term_jumpvar63r_21d_slope_v105_signal,
    f10rv_f10_realized_volatility_term_maxdd63r_21d_slope_v106_signal,
    f10rv_f10_realized_volatility_term_semispr126r_21d_slope_v107_signal,
    f10rv_f10_realized_volatility_term_rv5agg63r_21d_slope_v108_signal,
    f10rv_f10_realized_volatility_term_madvol42r_14d_slope_v109_signal,
    f10rv_f10_realized_volatility_term_inv10v126r_8d_slope_v110_signal,
    f10rv_f10_realized_volatility_term_inv21v252r_13d_slope_v111_signal,
    f10rv_f10_realized_volatility_term_inv42v252r_24d_slope_v112_signal,
    f10rv_f10_realized_volatility_term_inv63v252d_34d_slope_v113_signal,
    f10rv_f10_realized_volatility_term_inv63v504r_34d_slope_v114_signal,
    f10rv_f10_realized_volatility_term_dterm21v126r_13d_slope_v115_signal,
    f10rv_f10_realized_volatility_term_dterm21v252d_13d_slope_v116_signal,
    f10rv_f10_realized_volatility_term_dterm63v252r_34d_slope_v117_signal,
    f10rv_f10_realized_volatility_term_dterm42v189r_24d_slope_v118_signal,
    f10rv_f10_realized_volatility_term_uterm21v126r_13d_slope_v119_signal,
    f10rv_f10_realized_volatility_term_uterm63v252r_34d_slope_v120_signal,
    f10rv_f10_realized_volatility_term_uterm42v189r_24d_slope_v121_signal,
    f10rv_f10_realized_volatility_term_dcone21in252r_10d_slope_v122_signal,
    f10rv_f10_realized_volatility_term_dcone63in252r_31d_slope_v123_signal,
    f10rv_f10_realized_volatility_term_dcone42in252r_21d_slope_v124_signal,
    f10rv_f10_realized_volatility_term_dcone126in504r_63d_slope_v125_signal,
    f10rv_f10_realized_volatility_term_ucone21in252r_10d_slope_v126_signal,
    f10rv_f10_realized_volatility_term_ucone63in252r_31d_slope_v127_signal,
    f10rv_f10_realized_volatility_term_ucone126in504r_63d_slope_v128_signal,
    f10rv_f10_realized_volatility_term_vovx5in21r_5d_slope_v129_signal,
    f10rv_f10_realized_volatility_term_vovx10in42r_10d_slope_v130_signal,
    f10rv_f10_realized_volatility_term_vovx42in126r_31d_slope_v131_signal,
    f10rv_f10_realized_volatility_term_vovx63in189r_47d_slope_v132_signal,
    f10rv_f10_realized_volatility_term_estgap21r_7d_slope_v133_signal,
    f10rv_f10_realized_volatility_term_estgap63r_21d_slope_v134_signal,
    f10rv_f10_realized_volatility_term_estgap126r_42d_slope_v135_signal,
    f10rv_f10_realized_volatility_term_estgap252r_84d_slope_v136_signal,
    f10rv_f10_realized_volatility_term_bipow42r_14d_slope_v137_signal,
    f10rv_f10_realized_volatility_term_bipow63r_21d_slope_v138_signal,
    f10rv_f10_realized_volatility_term_bipow126r_42d_slope_v139_signal,
    f10rv_f10_realized_volatility_term_mad21r_7d_slope_v140_signal,
    f10rv_f10_realized_volatility_term_mad63r_21d_slope_v141_signal,
    f10rv_f10_realized_volatility_term_mad126r_42d_slope_v142_signal,
    f10rv_f10_realized_volatility_term_wbf5_42_252r_14d_slope_v143_signal,
    f10rv_f10_realized_volatility_term_wbf10_63_252r_21d_slope_v144_signal,
    f10rv_f10_realized_volatility_term_wbf21_84_252r_28d_slope_v145_signal,
    f10rv_f10_realized_volatility_term_wbf13_55_189r_18d_slope_v146_signal,
    f10rv_f10_realized_volatility_term_dshare21d_7d_slope_v147_signal,
    f10rv_f10_realized_volatility_term_dshare63p_21d_slope_v148_signal,
    f10rv_f10_realized_volatility_term_dshare126p_42d_slope_v149_signal,
    f10rv_f10_realized_volatility_term_dshare252p_84d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_SLOPE_001_150 = REGISTRY


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

    print("OK f10_realized_volatility_term_2nd_derivatives_001_150_claude: %d features pass" % n_features)
