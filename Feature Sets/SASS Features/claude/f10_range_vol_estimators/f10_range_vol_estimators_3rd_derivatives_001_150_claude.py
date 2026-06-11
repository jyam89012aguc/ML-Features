import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _pk_term(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    return (hl * hl) / (4.0 * np.log(2.0))


def _gk_term(open_, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return 0.5 * hl * hl - (2.0 * np.log(2.0) - 1.0) * co * co


def _rs_term(open_, high, low, close):
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    return ho * hc + lo * lc


def _on_term(open_, close):
    o = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return o * o


def _tr(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _pk_vol(high, low, w):
    return np.sqrt(_pk_term(high, low).rolling(w, min_periods=max(1, w // 2)).mean())


def _gk_vol(open_, high, low, close, w):
    t = _gk_term(open_, high, low, close).clip(lower=0)
    return np.sqrt(t.rolling(w, min_periods=max(1, w // 2)).mean())


def _rs_vol(open_, high, low, close, w):
    t = _rs_term(open_, high, low, close).clip(lower=0)
    return np.sqrt(t.rolling(w, min_periods=max(1, w // 2)).mean())


def _atr(high, low, close, w):
    return _tr(high, low, close).rolling(w, min_periods=max(1, w // 2)).mean()


def _yz_vol(open_, high, low, close, w):
    on = _on_term(open_, close).rolling(w, min_periods=max(5, w // 3)).mean()
    rs = _rs_term(open_, high, low, close).clip(lower=0).rolling(w, min_periods=max(5, w // 3)).mean()
    co = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=max(5, w // 3)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    return np.sqrt((on + k * oc + (1.0 - k) * rs).clip(lower=0))


def _rsdrift(open_, high, low, close, w):
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    up = (ho * hc).rolling(w, min_periods=max(5, w // 2)).mean()
    dn = (lo * lc).rolling(w, min_periods=max(5, w // 2)).mean()
    return (up - dn) / (up + dn).replace(0, np.nan)


def _rsupdown(open_, high, low, close, w):
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    u = np.sqrt((ho * hc).clip(lower=0).rolling(w, min_periods=max(5, w // 2)).mean())
    d = np.sqrt((lo * lc).clip(lower=0).rolling(w, min_periods=max(5, w // 2)).mean())
    return np.log((u + 1e-9) / (d + 1e-9))


def _gksemi(open_, high, low, close, w):
    t = _gk_term(open_, high, low, close).clip(lower=0)
    up = close >= open_
    vu = np.sqrt(t.where(up).rolling(w, min_periods=max(5, w // 2)).mean())
    vd = np.sqrt(t.where(~up).rolling(w, min_periods=max(5, w // 2)).mean())
    return (vd - vu) / (vd + vu).replace(0, np.nan)


def _estdisp(open_, high, low, close, w):
    pk = _pk_vol(high, low, w) / close.replace(0, np.nan)
    gk = _gk_vol(open_, high, low, close, w) / close.replace(0, np.nan)
    rs = _rs_vol(open_, high, low, close, w) / close.replace(0, np.nan)
    return pd.concat([pk, gk, rs], axis=1).std(axis=1)


def _conepos(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _stab(t, w):
    m = t.rolling(w, min_periods=max(1, w // 2)).mean()
    s = t.rolling(w, min_periods=max(1, w // 2)).std()
    return m / s.replace(0, np.nan)

def f10rv_f10_range_vol_estimators_pkvola_21d_jerk_v001_signal(high, low, close):  # jerk curv5d
    b0 = _pk_vol(high, low, 21) / close.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolb_21d_jerk_v002_signal(high, low, close):  # jerk daccel7d
    b0 = _pk_vol(high, low, 21) / close.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolc_21d_jerk_v003_signal(high, low, close):  # jerk zcurv10d
    b0 = _pk_vol(high, low, 21) / close.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvola_63d_jerk_v004_signal(high, low, closeadj):  # jerk curv21d
    b0 = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolb_63d_jerk_v005_signal(high, low, closeadj):  # jerk daccel31d
    b0 = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolc_63d_jerk_v006_signal(high, low, closeadj):  # jerk zcurv42d
    b0 = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvola_126d_jerk_v007_signal(high, low, closeadj):  # jerk curv21d
    b0 = _pk_vol(high, low, 126) / closeadj.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolb_126d_jerk_v008_signal(high, low, closeadj):  # jerk daccel31d
    b0 = _pk_vol(high, low, 126) / closeadj.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolc_126d_jerk_v009_signal(high, low, closeadj):  # jerk zcurv42d
    b0 = _pk_vol(high, low, 126) / closeadj.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvola_252d_jerk_v010_signal(high, low, closeadj):  # jerk curv63d
    b0 = _pk_vol(high, low, 252) / closeadj.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(63) + b0.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolb_252d_jerk_v011_signal(high, low, closeadj):  # jerk daccel94d
    b0 = _pk_vol(high, low, 252) / closeadj.replace(0, np.nan)
    sl = b0 - b0.shift(94)
    b = sl - sl.ewm(span=94, min_periods=max(3, 94 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkvolc_252d_jerk_v012_signal(high, low, closeadj):  # jerk zcurv126d
    b0 = _pk_vol(high, low, 252) / closeadj.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(126) + b0.shift(252)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkratioa_21v63_jerk_v013_signal(high, low):  # jerk curv5d
    b0 = _pk_vol(high, low, 21) / _pk_vol(high, low, 63).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkratiob_21v63_jerk_v014_signal(high, low):  # jerk daccel7d
    b0 = _pk_vol(high, low, 21) / _pk_vol(high, low, 63).replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkratioc_21v63_jerk_v015_signal(high, low):  # jerk zcurv10d
    b0 = _pk_vol(high, low, 21) / _pk_vol(high, low, 63).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkza_63d_jerk_v016_signal(high, low):  # jerk curv21d
    b0 = _z(_pk_vol(high, low, 63), 252)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkzb_63d_jerk_v017_signal(high, low):  # jerk daccel31d
    b0 = _z(_pk_vol(high, low, 63), 252)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkzc_63d_jerk_v018_signal(high, low):  # jerk zcurv42d
    b0 = _z(_pk_vol(high, low, 63), 252)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkcurva_63d_jerk_v019_signal(high, low):  # jerk curv21d
    s = _pk_vol(high, low, 21)
    m = _pk_vol(high, low, 63)
    l = _pk_vol(high, low, 252)
    b0 = (s - 2.0 * m + l) / m.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkcurvb_63d_jerk_v020_signal(high, low):  # jerk daccel31d
    s = _pk_vol(high, low, 21)
    m = _pk_vol(high, low, 63)
    l = _pk_vol(high, low, 252)
    b0 = (s - 2.0 * m + l) / m.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkcurvc_63d_jerk_v021_signal(high, low):  # jerk zcurv42d
    s = _pk_vol(high, low, 21)
    m = _pk_vol(high, low, 63)
    l = _pk_vol(high, low, 252)
    b0 = (s - 2.0 * m + l) / m.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkstaba_63d_jerk_v022_signal(high, low):  # jerk curv21d
    b0 = _stab(_pk_term(high, low), 63)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkstabb_63d_jerk_v023_signal(high, low):  # jerk daccel31d
    b0 = _stab(_pk_term(high, low), 63)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkstabc_63d_jerk_v024_signal(high, low):  # jerk zcurv42d
    b0 = _stab(_pk_term(high, low), 63)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkjumpa_21d_jerk_v025_signal(high, low):  # jerk curv5d
    t = _pk_term(high, low)
    mx = t.rolling(21, min_periods=10).max()
    mn = t.rolling(21, min_periods=10).mean()
    b0 = mx / mn.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkjumpb_21d_jerk_v026_signal(high, low):  # jerk daccel7d
    t = _pk_term(high, low)
    mx = t.rolling(21, min_periods=10).max()
    mn = t.rolling(21, min_periods=10).mean()
    b0 = mx / mn.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkjumpc_21d_jerk_v027_signal(high, low):  # jerk zcurv10d
    t = _pk_term(high, low)
    mx = t.rolling(21, min_periods=10).max()
    mn = t.rolling(21, min_periods=10).mean()
    b0 = mx / mn.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkewmsmaa_63d_jerk_v028_signal(high, low):  # jerk curv21d
    t = _pk_term(high, low)
    ew = np.sqrt(t.ewm(span=21, min_periods=10).mean())
    sm = np.sqrt(t.rolling(63, min_periods=21).mean())
    b0 = ew / sm.replace(0, np.nan) - 1.0
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkewmsmab_63d_jerk_v029_signal(high, low):  # jerk daccel31d
    t = _pk_term(high, low)
    ew = np.sqrt(t.ewm(span=21, min_periods=10).mean())
    sm = np.sqrt(t.rolling(63, min_periods=21).mean())
    b0 = ew / sm.replace(0, np.nan) - 1.0
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkewmsmac_63d_jerk_v030_signal(high, low):  # jerk zcurv42d
    t = _pk_term(high, low)
    ew = np.sqrt(t.ewm(span=21, min_periods=10).mean())
    sm = np.sqrt(t.rolling(63, min_periods=21).mean())
    b0 = ew / sm.replace(0, np.nan) - 1.0
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkbodysharea_21d_jerk_v031_signal(open, high, low, close):  # jerk curv5d
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    h = (0.5 * hl * hl).rolling(21, min_periods=10).mean()
    c = ((2.0 * np.log(2.0) - 1.0) * co * co).rolling(21, min_periods=10).mean()
    b0 = c / (h + c).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkbodyshareb_21d_jerk_v032_signal(open, high, low, close):  # jerk daccel7d
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    h = (0.5 * hl * hl).rolling(21, min_periods=10).mean()
    c = ((2.0 * np.log(2.0) - 1.0) * co * co).rolling(21, min_periods=10).mean()
    b0 = c / (h + c).replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkbodysharec_21d_jerk_v033_signal(open, high, low, close):  # jerk zcurv10d
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    h = (0.5 * hl * hl).rolling(21, min_periods=10).mean()
    c = ((2.0 * np.log(2.0) - 1.0) * co * co).rolling(21, min_periods=10).mean()
    b0 = c / (h + c).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkrobza_63d_jerk_v034_signal(open, high, low, close):  # jerk curv21d
    gk = _gk_vol(open, high, low, close, 63)
    med = gk.rolling(252, min_periods=126).median()
    iqr = gk.rolling(252, min_periods=126).quantile(0.75) - gk.rolling(252, min_periods=126).quantile(0.25)
    b0 = (gk - med) / iqr.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkrobzb_63d_jerk_v035_signal(open, high, low, close):  # jerk daccel31d
    gk = _gk_vol(open, high, low, close, 63)
    med = gk.rolling(252, min_periods=126).median()
    iqr = gk.rolling(252, min_periods=126).quantile(0.75) - gk.rolling(252, min_periods=126).quantile(0.25)
    b0 = (gk - med) / iqr.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkrobzc_63d_jerk_v036_signal(open, high, low, close):  # jerk zcurv42d
    gk = _gk_vol(open, high, low, close, 63)
    med = gk.rolling(252, min_periods=126).median()
    iqr = gk.rolling(252, min_periods=126).quantile(0.75) - gk.rolling(252, min_periods=126).quantile(0.25)
    b0 = (gk - med) / iqr.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkmrza_126d_jerk_v037_signal(open, high, low, close):  # jerk curv21d
    s = _gk_vol(open, high, low, close, 21)
    l = _gk_vol(open, high, low, close, 126)
    gap = s - l
    b0 = gap / gap.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkmrzb_126d_jerk_v038_signal(open, high, low, close):  # jerk daccel31d
    s = _gk_vol(open, high, low, close, 21)
    l = _gk_vol(open, high, low, close, 126)
    gap = s - l
    b0 = gap / gap.rolling(126, min_periods=63).std().replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkmrzc_126d_jerk_v039_signal(open, high, low, close):  # jerk zcurv42d
    s = _gk_vol(open, high, low, close, 21)
    l = _gk_vol(open, high, low, close, 126)
    gap = s - l
    b0 = gap / gap.rolling(126, min_periods=63).std().replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hltrsharea_21d_jerk_v040_signal(high, low, close):  # jerk curv5d
    hl = (high - low)
    tr = _tr(high, low, close)
    b0 = (hl / tr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hltrshareb_21d_jerk_v041_signal(high, low, close):  # jerk daccel7d
    hl = (high - low)
    tr = _tr(high, low, close)
    b0 = (hl / tr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hltrsharec_21d_jerk_v042_signal(high, low, close):  # jerk zcurv10d
    hl = (high - low)
    tr = _tr(high, low, close)
    b0 = (hl / tr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkewmdiva_63d_jerk_v043_signal(open, high, low, close):  # jerk curv21d
    t = _gk_term(open, high, low, close).clip(lower=0)
    f = np.sqrt(t.ewm(span=5, min_periods=3).mean())
    s = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    b0 = np.log((f + 1e-12) / (s + 1e-12))
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkewmdivb_63d_jerk_v044_signal(open, high, low, close):  # jerk daccel31d
    t = _gk_term(open, high, low, close).clip(lower=0)
    f = np.sqrt(t.ewm(span=5, min_periods=3).mean())
    s = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    b0 = np.log((f + 1e-12) / (s + 1e-12))
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkewmdivc_63d_jerk_v045_signal(open, high, low, close):  # jerk zcurv42d
    t = _gk_term(open, high, low, close).clip(lower=0)
    f = np.sqrt(t.ewm(span=5, min_periods=3).mean())
    s = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    b0 = np.log((f + 1e-12) / (s + 1e-12))
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkpkspreada_63d_jerk_v046_signal(open, high, low, close):  # jerk curv21d
    gk = _gk_vol(open, high, low, close, 63)
    pk = _pk_vol(high, low, 63)
    b0 = (gk - pk) / (gk + pk).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkpkspreadb_63d_jerk_v047_signal(open, high, low, close):  # jerk daccel31d
    gk = _gk_vol(open, high, low, close, 63)
    pk = _pk_vol(high, low, 63)
    b0 = (gk - pk) / (gk + pk).replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkpkspreadc_63d_jerk_v048_signal(open, high, low, close):  # jerk zcurv42d
    gk = _gk_vol(open, high, low, close, 63)
    pk = _pk_vol(high, low, 63)
    b0 = (gk - pk) / (gk + pk).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkkurta_63d_jerk_v049_signal(open, high, low, close):  # jerk curv21d
    t = _gk_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).kurt()
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkkurtb_63d_jerk_v050_signal(open, high, low, close):  # jerk daccel31d
    t = _gk_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).kurt()
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkkurtc_63d_jerk_v051_signal(open, high, low, close):  # jerk zcurv42d
    t = _gk_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).kurt()
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkstaba_63d_jerk_v052_signal(open, high, low, close):  # jerk curv21d
    b0 = _stab(_gk_term(open, high, low, close).clip(lower=0), 63)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkstabb_63d_jerk_v053_signal(open, high, low, close):  # jerk daccel31d
    b0 = _stab(_gk_term(open, high, low, close).clip(lower=0), 63)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_gkstabc_63d_jerk_v054_signal(open, high, low, close):  # jerk zcurv42d
    b0 = _stab(_gk_term(open, high, low, close).clip(lower=0), 63)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rspulsea_21d_jerk_v055_signal(open, high, low, close):  # jerk curv5d
    rs = _rs_vol(open, high, low, close, 21) / close.replace(0, np.nan)
    b0 = rs / rs.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rspulseb_21d_jerk_v056_signal(open, high, low, close):  # jerk daccel7d
    rs = _rs_vol(open, high, low, close, 21) / close.replace(0, np.nan)
    b0 = rs / rs.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rspulsec_21d_jerk_v057_signal(open, high, low, close):  # jerk zcurv10d
    rs = _rs_vol(open, high, low, close, 21) / close.replace(0, np.nan)
    b0 = rs / rs.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsskewa_63d_jerk_v058_signal(open, high, low, close):  # jerk curv21d
    t = _rs_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).skew()
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsskewb_63d_jerk_v059_signal(open, high, low, close):  # jerk daccel31d
    t = _rs_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).skew()
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsskewc_63d_jerk_v060_signal(open, high, low, close):  # jerk zcurv42d
    t = _rs_term(open, high, low, close).clip(lower=0)
    b0 = t.rolling(63, min_periods=21).skew()
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsdrifta_21d_jerk_v061_signal(open, high, low, close):  # jerk curv5d
    b0 = _rsdrift(open, high, low, close, 21)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsdriftb_21d_jerk_v062_signal(open, high, low, close):  # jerk daccel7d
    b0 = _rsdrift(open, high, low, close, 21)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsdriftc_21d_jerk_v063_signal(open, high, low, close):  # jerk zcurv10d
    b0 = _rsdrift(open, high, low, close, 21)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsupdowna_63d_jerk_v064_signal(open, high, low, close):  # jerk curv21d
    b0 = _rsupdown(open, high, low, close, 63)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsupdownb_63d_jerk_v065_signal(open, high, low, close):  # jerk daccel31d
    b0 = _rsupdown(open, high, low, close, 63)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_rsupdownc_63d_jerk_v066_signal(open, high, low, close):  # jerk zcurv42d
    b0 = _rsupdown(open, high, low, close, 63)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzrsspreada_63d_jerk_v067_signal(open, high, low, close):  # jerk curv21d
    yz = _yz_vol(open, high, low, close, 63)
    rs = _rs_vol(open, high, low, close, 63)
    b0 = (yz - rs) / (yz + rs).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzrsspreadb_63d_jerk_v068_signal(open, high, low, close):  # jerk daccel31d
    yz = _yz_vol(open, high, low, close, 63)
    rs = _rs_vol(open, high, low, close, 63)
    b0 = (yz - rs) / (yz + rs).replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzrsspreadc_63d_jerk_v069_signal(open, high, low, close):  # jerk zcurv42d
    yz = _yz_vol(open, high, low, close, 63)
    rs = _rs_vol(open, high, low, close, 63)
    b0 = (yz - rs) / (yz + rs).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzcompressa_21d_jerk_v070_signal(open, high, low, close):  # jerk curv5d
    yz = _yz_vol(open, high, low, close, 21)
    q25 = yz.rolling(126, min_periods=63).quantile(0.25)
    b0 = (q25 - yz) / q25.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzcompressb_21d_jerk_v071_signal(open, high, low, close):  # jerk daccel7d
    yz = _yz_vol(open, high, low, close, 21)
    q25 = yz.rolling(126, min_periods=63).quantile(0.25)
    b0 = (q25 - yz) / q25.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzcompressc_21d_jerk_v072_signal(open, high, low, close):  # jerk zcurv10d
    yz = _yz_vol(open, high, low, close, 21)
    q25 = yz.rolling(126, min_periods=63).quantile(0.25)
    b0 = (q25 - yz) / q25.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovkurta_63d_jerk_v073_signal(open, close):  # jerk curv21d
    o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b0 = o.rolling(63, min_periods=21).kurt()
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovkurtb_63d_jerk_v074_signal(open, close):  # jerk daccel31d
    o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b0 = o.rolling(63, min_periods=21).kurt()
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovkurtc_63d_jerk_v075_signal(open, close):  # jerk zcurv42d
    o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b0 = o.rolling(63, min_periods=21).kurt()
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgapsharea_21d_jerk_v076_signal(open, high, low, close):  # jerk curv5d
    on = _on_term(open, close).rolling(21, min_periods=10).mean()
    rs = _rs_term(open, high, low, close).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = on / (on + rs).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgapshareb_21d_jerk_v077_signal(open, high, low, close):  # jerk daccel7d
    on = _on_term(open, close).rolling(21, min_periods=10).mean()
    rs = _rs_term(open, high, low, close).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = on / (on + rs).replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgapsharec_21d_jerk_v078_signal(open, high, low, close):  # jerk zcurv10d
    on = _on_term(open, close).rolling(21, min_periods=10).mean()
    rs = _rs_term(open, high, low, close).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = on / (on + rs).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovvola_63d_jerk_v079_signal(open, close):  # jerk curv21d
    b0 = np.sqrt(_on_term(open, close).rolling(63, min_periods=21).mean())
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovvolb_63d_jerk_v080_signal(open, close):  # jerk daccel31d
    b0 = np.sqrt(_on_term(open, close).rolling(63, min_periods=21).mean())
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_ovvolc_63d_jerk_v081_signal(open, close):  # jerk zcurv42d
    b0 = np.sqrt(_on_term(open, close).rolling(63, min_periods=21).mean())
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzpkratioa_21d_jerk_v082_signal(open, high, low, close):  # jerk curv5d
    yz = _yz_vol(open, high, low, close, 21)
    pk = _pk_vol(high, low, 21)
    b0 = yz / pk.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzpkratiob_21d_jerk_v083_signal(open, high, low, close):  # jerk daccel7d
    yz = _yz_vol(open, high, low, close, 21)
    pk = _pk_vol(high, low, 21)
    b0 = yz / pk.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzpkratioc_21d_jerk_v084_signal(open, high, low, close):  # jerk zcurv10d
    yz = _yz_vol(open, high, low, close, 21)
    pk = _pk_vol(high, low, 21)
    b0 = yz / pk.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpa_14d_jerk_v085_signal(high, low, close):  # jerk curv5d
    b0 = _atr(high, low, close, 14) / close.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpb_14d_jerk_v086_signal(high, low, close):  # jerk daccel7d
    b0 = _atr(high, low, close, 14) / close.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpc_14d_jerk_v087_signal(high, low, close):  # jerk zcurv10d
    b0 = _atr(high, low, close, 14) / close.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpa_21d_jerk_v088_signal(high, low, close):  # jerk curv5d
    b0 = _atr(high, low, close, 21) / close.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpb_21d_jerk_v089_signal(high, low, close):  # jerk daccel7d
    b0 = _atr(high, low, close, 21) / close.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpc_21d_jerk_v090_signal(high, low, close):  # jerk zcurv10d
    b0 = _atr(high, low, close, 21) / close.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpa_63d_jerk_v091_signal(high, low, close, closeadj):  # jerk curv21d
    b0 = _atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpb_63d_jerk_v092_signal(high, low, close, closeadj):  # jerk daccel31d
    b0 = _atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpc_63d_jerk_v093_signal(high, low, close, closeadj):  # jerk zcurv42d
    b0 = _atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrunitdispa_21d_jerk_v094_signal(high, low, close):  # jerk curv5d
    atr = _atr(high, low, close, 21)
    u = (close - close.shift(1)) / atr.replace(0, np.nan)
    b0 = u.rolling(21, min_periods=10).std()
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrunitdispb_21d_jerk_v095_signal(high, low, close):  # jerk daccel7d
    atr = _atr(high, low, close, 21)
    u = (close - close.shift(1)) / atr.replace(0, np.nan)
    b0 = u.rolling(21, min_periods=10).std()
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrunitdispc_21d_jerk_v096_signal(high, low, close):  # jerk zcurv10d
    atr = _atr(high, low, close, 21)
    u = (close - close.shift(1)) / atr.replace(0, np.nan)
    b0 = u.rolling(21, min_periods=10).std()
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trza_21d_jerk_v097_signal(high, low, close):  # jerk curv5d
    b0 = _z(_tr(high, low, close), 21)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trzb_21d_jerk_v098_signal(high, low, close):  # jerk daccel7d
    b0 = _z(_tr(high, low, close), 21)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trzc_21d_jerk_v099_signal(high, low, close):  # jerk zcurv10d
    b0 = _z(_tr(high, low, close), 21)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpka_63d_jerk_v100_signal(high, low, close):  # jerk curv21d
    a = _atr(high, low, close, 63) / close.replace(0, np.nan)
    p = _pk_vol(high, low, 63) / close.replace(0, np.nan)
    b0 = a / p.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpkb_63d_jerk_v101_signal(high, low, close):  # jerk daccel31d
    a = _atr(high, low, close, 63) / close.replace(0, np.nan)
    p = _pk_vol(high, low, 63) / close.replace(0, np.nan)
    b0 = a / p.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrpkc_63d_jerk_v102_signal(high, low, close):  # jerk zcurv42d
    a = _atr(high, low, close, 63) / close.replace(0, np.nan)
    p = _pk_vol(high, low, 63) / close.replace(0, np.nan)
    b0 = a / p.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trstaba_63d_jerk_v103_signal(high, low, close):  # jerk curv21d
    b0 = _stab(_tr(high, low, close), 63)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trstabb_63d_jerk_v104_signal(high, low, close):  # jerk daccel31d
    b0 = _stab(_tr(high, low, close), 63)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trstabc_63d_jerk_v105_signal(high, low, close):  # jerk zcurv42d
    b0 = _stab(_tr(high, low, close), 63)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlra_21d_jerk_v106_signal(high, low, close):  # jerk curv5d
    b0 = ((high - low) / close.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlrb_21d_jerk_v107_signal(high, low, close):  # jerk daccel7d
    b0 = ((high - low) / close.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlrc_21d_jerk_v108_signal(high, low, close):  # jerk zcurv10d
    b0 = ((high - low) / close.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlra_63d_jerk_v109_signal(high, low, closeadj):  # jerk curv21d
    b0 = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlrb_63d_jerk_v110_signal(high, low, closeadj):  # jerk daccel31d
    b0 = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_hlrc_63d_jerk_v111_signal(high, low, closeadj):  # jerk zcurv42d
    b0 = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_clposa_21d_jerk_v112_signal(high, low, close):  # jerk curv5d
    pos = (close - low) / (high - low).replace(0, np.nan)
    b0 = pos.rolling(21, min_periods=10).mean() - 0.5
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_clposb_21d_jerk_v113_signal(high, low, close):  # jerk daccel7d
    pos = (close - low) / (high - low).replace(0, np.nan)
    b0 = pos.rolling(21, min_periods=10).mean() - 0.5
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_clposc_21d_jerk_v114_signal(high, low, close):  # jerk zcurv10d
    pos = (close - low) / (high - low).replace(0, np.nan)
    b0 = pos.rolling(21, min_periods=10).mean() - 0.5
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_volofpkvola_126d_jerk_v115_signal(high, low):  # jerk curv21d
    pk = _pk_vol(high, low, 21)
    m = pk.rolling(126, min_periods=63).mean()
    b0 = pk.rolling(126, min_periods=63).std() / m.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_volofpkvolb_126d_jerk_v116_signal(high, low):  # jerk daccel31d
    pk = _pk_vol(high, low, 21)
    m = pk.rolling(126, min_periods=63).mean()
    b0 = pk.rolling(126, min_periods=63).std() / m.replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_volofpkvolc_126d_jerk_v117_signal(high, low):  # jerk zcurv42d
    pk = _pk_vol(high, low, 21)
    m = pk.rolling(126, min_periods=63).mean()
    b0 = pk.rolling(126, min_periods=63).std() / m.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_wickdoma_21d_jerk_v118_signal(open, high, low, close):  # jerk curv5d
    rng = (high - low)
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    b0 = (wick / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_wickdomb_21d_jerk_v119_signal(open, high, low, close):  # jerk daccel7d
    rng = (high - low)
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    b0 = (wick / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_wickdomc_21d_jerk_v120_signal(open, high, low, close):  # jerk zcurv10d
    rng = (high - low)
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    b0 = (wick / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_estdispa_63d_jerk_v121_signal(open, high, low, close):  # jerk curv21d
    b0 = _estdisp(open, high, low, close, 63)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_estdispb_63d_jerk_v122_signal(open, high, low, close):  # jerk daccel31d
    b0 = _estdisp(open, high, low, close, 63)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_estdispc_63d_jerk_v123_signal(open, high, low, close):  # jerk zcurv42d
    b0 = _estdisp(open, high, low, close, 63)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_intrakurta_63d_jerk_v124_signal(open, close):  # jerk curv21d
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b0 = c.rolling(63, min_periods=21).kurt()
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_intrakurtb_63d_jerk_v125_signal(open, close):  # jerk daccel31d
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b0 = c.rolling(63, min_periods=21).kurt()
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_intrakurtc_63d_jerk_v126_signal(open, close):  # jerk zcurv42d
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b0 = c.rolling(63, min_periods=21).kurt()
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkchopa_63d_jerk_v127_signal(high, low, closeadj):  # jerk curv21d
    pk = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    net = (closeadj / closeadj.shift(63) - 1.0).abs()
    b0 = pk / (net.replace(0, np.nan) + 1e-6)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkchopb_63d_jerk_v128_signal(high, low, closeadj):  # jerk daccel31d
    pk = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    net = (closeadj / closeadj.shift(63) - 1.0).abs()
    b0 = pk / (net.replace(0, np.nan) + 1e-6)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_pkchopc_63d_jerk_v129_signal(high, low, closeadj):  # jerk zcurv42d
    pk = _pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    net = (closeadj / closeadj.shift(63) - 1.0).abs()
    b0 = pk / (net.replace(0, np.nan) + 1e-6)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trconca_21d_jerk_v130_signal(high, low, close):  # jerk curv5d
    tr = _tr(high, low, close)
    s = tr.rolling(21, min_periods=10).sum()
    mx = tr.rolling(21, min_periods=10).max()
    b0 = mx / s.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trconcb_21d_jerk_v131_signal(high, low, close):  # jerk daccel7d
    tr = _tr(high, low, close)
    s = tr.rolling(21, min_periods=10).sum()
    mx = tr.rolling(21, min_periods=10).max()
    b0 = mx / s.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trconcc_21d_jerk_v132_signal(high, low, close):  # jerk zcurv10d
    tr = _tr(high, low, close)
    s = tr.rolling(21, min_periods=10).sum()
    mx = tr.rolling(21, min_periods=10).max()
    b0 = mx / s.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trgapsharea_63d_jerk_v133_signal(high, low, close):  # jerk curv21d
    tr = _tr(high, low, close)
    hl = (high - low)
    gap = (tr - hl).clip(lower=0)
    b0 = gap.rolling(63, min_periods=21).sum() / tr.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trgapshareb_63d_jerk_v134_signal(high, low, close):  # jerk daccel31d
    tr = _tr(high, low, close)
    hl = (high - low)
    gap = (tr - hl).clip(lower=0)
    b0 = gap.rolling(63, min_periods=21).sum() / tr.rolling(63, min_periods=21).sum().replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trgapsharec_63d_jerk_v135_signal(high, low, close):  # jerk zcurv42d
    tr = _tr(high, low, close)
    hl = (high - low)
    gap = (tr - hl).clip(lower=0)
    b0 = gap.rolling(63, min_periods=21).sum() / tr.rolling(63, min_periods=21).sum().replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgkspreada_63d_jerk_v136_signal(open, high, low, close):  # jerk curv21d
    yz = _yz_vol(open, high, low, close, 63)
    gk = _gk_vol(open, high, low, close, 63)
    b0 = (yz - gk) / (yz + gk).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(21) + b0.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgkspreadb_63d_jerk_v137_signal(open, high, low, close):  # jerk daccel31d
    yz = _yz_vol(open, high, low, close, 63)
    gk = _gk_vol(open, high, low, close, 63)
    b0 = (yz - gk) / (yz + gk).replace(0, np.nan)
    sl = b0 - b0.shift(31)
    b = sl - sl.ewm(span=31, min_periods=max(3, 31 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_yzgkspreadc_63d_jerk_v138_signal(open, high, low, close):  # jerk zcurv42d
    yz = _yz_vol(open, high, low, close, 63)
    gk = _gk_vol(open, high, low, close, 63)
    b0 = (yz - gk) / (yz + gk).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(42) + b0.shift(84)
    b = _z(a, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrmoma_21d_jerk_v139_signal(high, low, close):  # jerk curv5d
    atrp = _atr(high, low, close, 21) / close.replace(0, np.nan)
    ret = (close / close.shift(21) - 1.0)
    b0 = ret / atrp.replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrmomb_21d_jerk_v140_signal(high, low, close):  # jerk daccel7d
    atrp = _atr(high, low, close, 21) / close.replace(0, np.nan)
    ret = (close / close.shift(21) - 1.0)
    b0 = ret / atrp.replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_atrmomc_21d_jerk_v141_signal(high, low, close):  # jerk zcurv10d
    atrp = _atr(high, low, close, 21) / close.replace(0, np.nan)
    ret = (close / close.shift(21) - 1.0)
    b0 = ret / atrp.replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_dirrangea_21d_jerk_v142_signal(open, high, low, close):  # jerk curv5d
    rng = (high - low) / close.replace(0, np.nan)
    sign = np.sign(close - open)
    b0 = (sign * rng).rolling(21, min_periods=10).mean()
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_dirrangeb_21d_jerk_v143_signal(open, high, low, close):  # jerk daccel7d
    rng = (high - low) / close.replace(0, np.nan)
    sign = np.sign(close - open)
    b0 = (sign * rng).rolling(21, min_periods=10).mean()
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_dirrangec_21d_jerk_v144_signal(open, high, low, close):  # jerk zcurv10d
    rng = (high - low) / close.replace(0, np.nan)
    sign = np.sign(close - open)
    b0 = (sign * rng).rolling(21, min_periods=10).mean()
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trdira_21d_jerk_v145_signal(high, low, close):  # jerk curv5d
    tr = _tr(high, low, close)
    up = close > close.shift(1)
    su = tr.where(up).rolling(21, min_periods=8).sum()
    sd = tr.where(~up).rolling(21, min_periods=8).sum()
    b0 = (su - sd) / (su + sd).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trdirb_21d_jerk_v146_signal(high, low, close):  # jerk daccel7d
    tr = _tr(high, low, close)
    up = close > close.shift(1)
    su = tr.where(up).rolling(21, min_periods=8).sum()
    sd = tr.where(~up).rolling(21, min_periods=8).sum()
    b0 = (su - sd) / (su + sd).replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_trdirc_21d_jerk_v147_signal(high, low, close):  # jerk zcurv10d
    tr = _tr(high, low, close)
    up = close > close.shift(1)
    su = tr.where(up).rolling(21, min_periods=8).sum()
    sd = tr.where(~up).rolling(21, min_periods=8).sum()
    b0 = (su - sd) / (su + sd).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_shadowskewa_21d_jerk_v148_signal(open, high, low):  # jerk curv5d
    su = (high - open).clip(lower=0).rolling(21, min_periods=10).mean()
    sl = (open - low).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = (su - sl) / (su + sl).replace(0, np.nan)
    b = b0 - 2.0 * b0.shift(5) + b0.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_shadowskewb_21d_jerk_v149_signal(open, high, low):  # jerk daccel7d
    su = (high - open).clip(lower=0).rolling(21, min_periods=10).mean()
    sl = (open - low).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = (su - sl) / (su + sl).replace(0, np.nan)
    sl = b0 - b0.shift(7)
    b = sl - sl.ewm(span=7, min_periods=max(3, 7 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f10rv_f10_range_vol_estimators_shadowskewc_21d_jerk_v150_signal(open, high, low):  # jerk zcurv10d
    su = (high - open).clip(lower=0).rolling(21, min_periods=10).mean()
    sl = (open - low).clip(lower=0).rolling(21, min_periods=10).mean()
    b0 = (su - sl) / (su + sl).replace(0, np.nan)
    a = b0 - 2.0 * b0.shift(10) + b0.shift(20)
    b = _z(a, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f10rv_f10_range_vol_estimators_pkvola_21d_jerk_v001_signal,
    f10rv_f10_range_vol_estimators_pkvolb_21d_jerk_v002_signal,
    f10rv_f10_range_vol_estimators_pkvolc_21d_jerk_v003_signal,
    f10rv_f10_range_vol_estimators_pkvola_63d_jerk_v004_signal,
    f10rv_f10_range_vol_estimators_pkvolb_63d_jerk_v005_signal,
    f10rv_f10_range_vol_estimators_pkvolc_63d_jerk_v006_signal,
    f10rv_f10_range_vol_estimators_pkvola_126d_jerk_v007_signal,
    f10rv_f10_range_vol_estimators_pkvolb_126d_jerk_v008_signal,
    f10rv_f10_range_vol_estimators_pkvolc_126d_jerk_v009_signal,
    f10rv_f10_range_vol_estimators_pkvola_252d_jerk_v010_signal,
    f10rv_f10_range_vol_estimators_pkvolb_252d_jerk_v011_signal,
    f10rv_f10_range_vol_estimators_pkvolc_252d_jerk_v012_signal,
    f10rv_f10_range_vol_estimators_pkratioa_21v63_jerk_v013_signal,
    f10rv_f10_range_vol_estimators_pkratiob_21v63_jerk_v014_signal,
    f10rv_f10_range_vol_estimators_pkratioc_21v63_jerk_v015_signal,
    f10rv_f10_range_vol_estimators_pkza_63d_jerk_v016_signal,
    f10rv_f10_range_vol_estimators_pkzb_63d_jerk_v017_signal,
    f10rv_f10_range_vol_estimators_pkzc_63d_jerk_v018_signal,
    f10rv_f10_range_vol_estimators_pkcurva_63d_jerk_v019_signal,
    f10rv_f10_range_vol_estimators_pkcurvb_63d_jerk_v020_signal,
    f10rv_f10_range_vol_estimators_pkcurvc_63d_jerk_v021_signal,
    f10rv_f10_range_vol_estimators_pkstaba_63d_jerk_v022_signal,
    f10rv_f10_range_vol_estimators_pkstabb_63d_jerk_v023_signal,
    f10rv_f10_range_vol_estimators_pkstabc_63d_jerk_v024_signal,
    f10rv_f10_range_vol_estimators_pkjumpa_21d_jerk_v025_signal,
    f10rv_f10_range_vol_estimators_pkjumpb_21d_jerk_v026_signal,
    f10rv_f10_range_vol_estimators_pkjumpc_21d_jerk_v027_signal,
    f10rv_f10_range_vol_estimators_pkewmsmaa_63d_jerk_v028_signal,
    f10rv_f10_range_vol_estimators_pkewmsmab_63d_jerk_v029_signal,
    f10rv_f10_range_vol_estimators_pkewmsmac_63d_jerk_v030_signal,
    f10rv_f10_range_vol_estimators_gkbodysharea_21d_jerk_v031_signal,
    f10rv_f10_range_vol_estimators_gkbodyshareb_21d_jerk_v032_signal,
    f10rv_f10_range_vol_estimators_gkbodysharec_21d_jerk_v033_signal,
    f10rv_f10_range_vol_estimators_gkrobza_63d_jerk_v034_signal,
    f10rv_f10_range_vol_estimators_gkrobzb_63d_jerk_v035_signal,
    f10rv_f10_range_vol_estimators_gkrobzc_63d_jerk_v036_signal,
    f10rv_f10_range_vol_estimators_gkmrza_126d_jerk_v037_signal,
    f10rv_f10_range_vol_estimators_gkmrzb_126d_jerk_v038_signal,
    f10rv_f10_range_vol_estimators_gkmrzc_126d_jerk_v039_signal,
    f10rv_f10_range_vol_estimators_hltrsharea_21d_jerk_v040_signal,
    f10rv_f10_range_vol_estimators_hltrshareb_21d_jerk_v041_signal,
    f10rv_f10_range_vol_estimators_hltrsharec_21d_jerk_v042_signal,
    f10rv_f10_range_vol_estimators_gkewmdiva_63d_jerk_v043_signal,
    f10rv_f10_range_vol_estimators_gkewmdivb_63d_jerk_v044_signal,
    f10rv_f10_range_vol_estimators_gkewmdivc_63d_jerk_v045_signal,
    f10rv_f10_range_vol_estimators_gkpkspreada_63d_jerk_v046_signal,
    f10rv_f10_range_vol_estimators_gkpkspreadb_63d_jerk_v047_signal,
    f10rv_f10_range_vol_estimators_gkpkspreadc_63d_jerk_v048_signal,
    f10rv_f10_range_vol_estimators_gkkurta_63d_jerk_v049_signal,
    f10rv_f10_range_vol_estimators_gkkurtb_63d_jerk_v050_signal,
    f10rv_f10_range_vol_estimators_gkkurtc_63d_jerk_v051_signal,
    f10rv_f10_range_vol_estimators_gkstaba_63d_jerk_v052_signal,
    f10rv_f10_range_vol_estimators_gkstabb_63d_jerk_v053_signal,
    f10rv_f10_range_vol_estimators_gkstabc_63d_jerk_v054_signal,
    f10rv_f10_range_vol_estimators_rspulsea_21d_jerk_v055_signal,
    f10rv_f10_range_vol_estimators_rspulseb_21d_jerk_v056_signal,
    f10rv_f10_range_vol_estimators_rspulsec_21d_jerk_v057_signal,
    f10rv_f10_range_vol_estimators_rsskewa_63d_jerk_v058_signal,
    f10rv_f10_range_vol_estimators_rsskewb_63d_jerk_v059_signal,
    f10rv_f10_range_vol_estimators_rsskewc_63d_jerk_v060_signal,
    f10rv_f10_range_vol_estimators_rsdrifta_21d_jerk_v061_signal,
    f10rv_f10_range_vol_estimators_rsdriftb_21d_jerk_v062_signal,
    f10rv_f10_range_vol_estimators_rsdriftc_21d_jerk_v063_signal,
    f10rv_f10_range_vol_estimators_rsupdowna_63d_jerk_v064_signal,
    f10rv_f10_range_vol_estimators_rsupdownb_63d_jerk_v065_signal,
    f10rv_f10_range_vol_estimators_rsupdownc_63d_jerk_v066_signal,
    f10rv_f10_range_vol_estimators_yzrsspreada_63d_jerk_v067_signal,
    f10rv_f10_range_vol_estimators_yzrsspreadb_63d_jerk_v068_signal,
    f10rv_f10_range_vol_estimators_yzrsspreadc_63d_jerk_v069_signal,
    f10rv_f10_range_vol_estimators_yzcompressa_21d_jerk_v070_signal,
    f10rv_f10_range_vol_estimators_yzcompressb_21d_jerk_v071_signal,
    f10rv_f10_range_vol_estimators_yzcompressc_21d_jerk_v072_signal,
    f10rv_f10_range_vol_estimators_ovkurta_63d_jerk_v073_signal,
    f10rv_f10_range_vol_estimators_ovkurtb_63d_jerk_v074_signal,
    f10rv_f10_range_vol_estimators_ovkurtc_63d_jerk_v075_signal,
    f10rv_f10_range_vol_estimators_yzgapsharea_21d_jerk_v076_signal,
    f10rv_f10_range_vol_estimators_yzgapshareb_21d_jerk_v077_signal,
    f10rv_f10_range_vol_estimators_yzgapsharec_21d_jerk_v078_signal,
    f10rv_f10_range_vol_estimators_ovvola_63d_jerk_v079_signal,
    f10rv_f10_range_vol_estimators_ovvolb_63d_jerk_v080_signal,
    f10rv_f10_range_vol_estimators_ovvolc_63d_jerk_v081_signal,
    f10rv_f10_range_vol_estimators_yzpkratioa_21d_jerk_v082_signal,
    f10rv_f10_range_vol_estimators_yzpkratiob_21d_jerk_v083_signal,
    f10rv_f10_range_vol_estimators_yzpkratioc_21d_jerk_v084_signal,
    f10rv_f10_range_vol_estimators_atrpa_14d_jerk_v085_signal,
    f10rv_f10_range_vol_estimators_atrpb_14d_jerk_v086_signal,
    f10rv_f10_range_vol_estimators_atrpc_14d_jerk_v087_signal,
    f10rv_f10_range_vol_estimators_atrpa_21d_jerk_v088_signal,
    f10rv_f10_range_vol_estimators_atrpb_21d_jerk_v089_signal,
    f10rv_f10_range_vol_estimators_atrpc_21d_jerk_v090_signal,
    f10rv_f10_range_vol_estimators_atrpa_63d_jerk_v091_signal,
    f10rv_f10_range_vol_estimators_atrpb_63d_jerk_v092_signal,
    f10rv_f10_range_vol_estimators_atrpc_63d_jerk_v093_signal,
    f10rv_f10_range_vol_estimators_atrunitdispa_21d_jerk_v094_signal,
    f10rv_f10_range_vol_estimators_atrunitdispb_21d_jerk_v095_signal,
    f10rv_f10_range_vol_estimators_atrunitdispc_21d_jerk_v096_signal,
    f10rv_f10_range_vol_estimators_trza_21d_jerk_v097_signal,
    f10rv_f10_range_vol_estimators_trzb_21d_jerk_v098_signal,
    f10rv_f10_range_vol_estimators_trzc_21d_jerk_v099_signal,
    f10rv_f10_range_vol_estimators_atrpka_63d_jerk_v100_signal,
    f10rv_f10_range_vol_estimators_atrpkb_63d_jerk_v101_signal,
    f10rv_f10_range_vol_estimators_atrpkc_63d_jerk_v102_signal,
    f10rv_f10_range_vol_estimators_trstaba_63d_jerk_v103_signal,
    f10rv_f10_range_vol_estimators_trstabb_63d_jerk_v104_signal,
    f10rv_f10_range_vol_estimators_trstabc_63d_jerk_v105_signal,
    f10rv_f10_range_vol_estimators_hlra_21d_jerk_v106_signal,
    f10rv_f10_range_vol_estimators_hlrb_21d_jerk_v107_signal,
    f10rv_f10_range_vol_estimators_hlrc_21d_jerk_v108_signal,
    f10rv_f10_range_vol_estimators_hlra_63d_jerk_v109_signal,
    f10rv_f10_range_vol_estimators_hlrb_63d_jerk_v110_signal,
    f10rv_f10_range_vol_estimators_hlrc_63d_jerk_v111_signal,
    f10rv_f10_range_vol_estimators_clposa_21d_jerk_v112_signal,
    f10rv_f10_range_vol_estimators_clposb_21d_jerk_v113_signal,
    f10rv_f10_range_vol_estimators_clposc_21d_jerk_v114_signal,
    f10rv_f10_range_vol_estimators_volofpkvola_126d_jerk_v115_signal,
    f10rv_f10_range_vol_estimators_volofpkvolb_126d_jerk_v116_signal,
    f10rv_f10_range_vol_estimators_volofpkvolc_126d_jerk_v117_signal,
    f10rv_f10_range_vol_estimators_wickdoma_21d_jerk_v118_signal,
    f10rv_f10_range_vol_estimators_wickdomb_21d_jerk_v119_signal,
    f10rv_f10_range_vol_estimators_wickdomc_21d_jerk_v120_signal,
    f10rv_f10_range_vol_estimators_estdispa_63d_jerk_v121_signal,
    f10rv_f10_range_vol_estimators_estdispb_63d_jerk_v122_signal,
    f10rv_f10_range_vol_estimators_estdispc_63d_jerk_v123_signal,
    f10rv_f10_range_vol_estimators_intrakurta_63d_jerk_v124_signal,
    f10rv_f10_range_vol_estimators_intrakurtb_63d_jerk_v125_signal,
    f10rv_f10_range_vol_estimators_intrakurtc_63d_jerk_v126_signal,
    f10rv_f10_range_vol_estimators_pkchopa_63d_jerk_v127_signal,
    f10rv_f10_range_vol_estimators_pkchopb_63d_jerk_v128_signal,
    f10rv_f10_range_vol_estimators_pkchopc_63d_jerk_v129_signal,
    f10rv_f10_range_vol_estimators_trconca_21d_jerk_v130_signal,
    f10rv_f10_range_vol_estimators_trconcb_21d_jerk_v131_signal,
    f10rv_f10_range_vol_estimators_trconcc_21d_jerk_v132_signal,
    f10rv_f10_range_vol_estimators_trgapsharea_63d_jerk_v133_signal,
    f10rv_f10_range_vol_estimators_trgapshareb_63d_jerk_v134_signal,
    f10rv_f10_range_vol_estimators_trgapsharec_63d_jerk_v135_signal,
    f10rv_f10_range_vol_estimators_yzgkspreada_63d_jerk_v136_signal,
    f10rv_f10_range_vol_estimators_yzgkspreadb_63d_jerk_v137_signal,
    f10rv_f10_range_vol_estimators_yzgkspreadc_63d_jerk_v138_signal,
    f10rv_f10_range_vol_estimators_atrmoma_21d_jerk_v139_signal,
    f10rv_f10_range_vol_estimators_atrmomb_21d_jerk_v140_signal,
    f10rv_f10_range_vol_estimators_atrmomc_21d_jerk_v141_signal,
    f10rv_f10_range_vol_estimators_dirrangea_21d_jerk_v142_signal,
    f10rv_f10_range_vol_estimators_dirrangeb_21d_jerk_v143_signal,
    f10rv_f10_range_vol_estimators_dirrangec_21d_jerk_v144_signal,
    f10rv_f10_range_vol_estimators_trdira_21d_jerk_v145_signal,
    f10rv_f10_range_vol_estimators_trdirb_21d_jerk_v146_signal,
    f10rv_f10_range_vol_estimators_trdirc_21d_jerk_v147_signal,
    f10rv_f10_range_vol_estimators_shadowskewa_21d_jerk_v148_signal,
    f10rv_f10_range_vol_estimators_shadowskewb_21d_jerk_v149_signal,
    f10rv_f10_range_vol_estimators_shadowskewc_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RANGE_VOL_ESTIMATORS_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f10_range_vol_estimators_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
