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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _f11re_logsq(num, den):
    r = np.log(num.replace(0, np.nan) / den.replace(0, np.nan))
    return r * r


def _f11re_parkinson(high, low, w):
    hl = _f11re_logsq(high, low)
    var = hl.rolling(w, min_periods=max(1, w // 2)).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var)


def _f11re_garman_klass(open_, high, low, close, w):
    term = 0.5 * _f11re_logsq(high, low) - (2.0 * np.log(2.0) - 1.0) * _f11re_logsq(close, open_)
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_rogers_satchell(open_, high, low, close, w):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    term = hc * ho + lc * lo
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_overnight_var(open_, close, w):
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return on.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_open_close_var(open_, close, w):
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return oc.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_yang_zhang(open_, high, low, close, w):
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    von = on.rolling(w, min_periods=max(1, w // 2)).var()
    voc = oc.rolling(w, min_periods=max(1, w // 2)).var()
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(w, min_periods=max(1, w // 2)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    var = von + k * voc + (1.0 - k) * rs
    return np.sqrt(var.clip(lower=0))


def _f11re_overnight_premium(open_, high, low, close, w):
    y = _f11re_yang_zhang(open_, high, low, close, w) ** 2
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(w, min_periods=max(1, w // 2)).mean()
    return (y - rs.clip(lower=0)).clip(lower=0)


def _f11re_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11re_atr(high, low, close, w):
    tr = _f11re_true_range(high, low, close)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f11re_hl_range(high, low, close):
    return (high - low) / close.replace(0, np.nan)


def f11re_f11_range_vol_estimators_park_5d_slope_v001_signal(high, low):
    b = _f11re_parkinson(high, low, 5)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_park_21d_slope_v002_signal(high, low):
    b = _f11re_parkinson(high, low, 21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_park_63d_slope_v003_signal(high, low, closeadj):
    p = _f11re_parkinson(high, low, 63) * np.sqrt(252.0)
    b = p / (closeadj.replace(0, np.nan) ** 0.0)  # annualized sigma is already price-normalized via log
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_park_126d_slope_v004_signal(high, low):
    b = _f11re_parkinson(high, low, 126) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_park_252d_slope_v005_signal(high, low):
    b = _f11re_parkinson(high, low, 252) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkterm_21v126_slope_v006_signal(high, low):
    s = _f11re_parkinson(high, low, 21)
    l = _f11re_parkinson(high, low, 126)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkz_63d_slope_v007_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = _z(p, 252)
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkrank_21d_slope_v008_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = _rank(p, 252)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkmom_21d_slope_v009_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p - p.shift(21)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_5d_slope_v010_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 5)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_21d_slope_v011_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_63d_slope_v012_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 63) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_126d_slope_v013_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 126) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_252d_slope_v014_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 252) * np.sqrt(252.0)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkterm_21v63_slope_v015_signal(open, high, low, close):
    s = _f11re_garman_klass(open, high, low, close, 21)
    l = _f11re_garman_klass(open, high, low, close, 63)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkz_63d_slope_v016_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = _z(g, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkrank_21d_slope_v017_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    b = _rank(g, 252)
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkparkspr_21d_slope_v018_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    p = _f11re_parkinson(high, low, 21)
    b = (g - p) / p.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rs_5d_slope_v019_signal(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    hileg = (hc * ho).rolling(5, min_periods=3).mean()
    loleg = (lc * lo).rolling(5, min_periods=3).mean()
    b = (hileg - loleg) / (hileg + loleg).replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rs_21d_slope_v020_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    b = r - r.shift(5)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rs_63d_slope_v021_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = r / p.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rs_126d_slope_v022_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 126) * np.sqrt(252.0)
    med = r.rolling(252, min_periods=126).median()
    b = r / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(31)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rs_252d_slope_v023_signal(open, high, low, close):
    b = _f11re_rogers_satchell(open, high, low, close, 252) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsterm_21v126_slope_v024_signal(open, high, low, close):
    s = _f11re_rogers_satchell(open, high, low, close, 21)
    l = _f11re_rogers_satchell(open, high, low, close, 126)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(42)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsz_63d_slope_v025_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    frac = r / p.replace(0, np.nan)
    b = _rank(frac, 252)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsrank_21d_slope_v026_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    b = r - r.shift(21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsparkspr_21d_slope_v027_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    p = _f11re_parkinson(high, low, 21)
    b = (p - r) / p.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yz_21d_slope_v028_signal(open, high, low, close):
    prem = _f11re_overnight_premium(open, high, low, close, 21)
    b = np.sqrt(prem)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yz_63d_slope_v029_signal(open, high, low, close):
    prem = _f11re_overnight_premium(open, high, low, close, 63)
    tot = _f11re_yang_zhang(open, high, low, close, 63) ** 2
    b = prem / tot.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yz_126d_slope_v030_signal(open, high, low, close):
    prem = np.sqrt(_f11re_overnight_premium(open, high, low, close, 126)) * np.sqrt(252.0)
    med = prem.rolling(252, min_periods=126).median()
    b = prem / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yz_252d_slope_v031_signal(open, high, low, close):
    b = np.sqrt(_f11re_overnight_premium(open, high, low, close, 252)) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yzterm_21v126_slope_v032_signal(open, high, low, close):
    s = np.sqrt(_f11re_overnight_premium(open, high, low, close, 21))
    l = np.sqrt(_f11re_overnight_premium(open, high, low, close, 126))
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(63)
    _sd = base.rolling(189, min_periods=63).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yzz_63d_slope_v033_signal(open, high, low, close):
    prem = np.sqrt(_f11re_overnight_premium(open, high, low, close, 63))
    b = _z(prem, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onvol_21d_slope_v034_signal(open, close):
    b = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_ocvol_21d_slope_v035_signal(open, close):
    b = np.sqrt(_f11re_open_close_var(open, close, 21).clip(lower=0))
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onshare_63d_slope_v036_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    b = von / (von + voc).replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onocratio_63d_slope_v037_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    ratio = np.sqrt(von.clip(lower=0)) / np.sqrt(voc.clip(lower=0)).replace(0, np.nan)
    b = _rank(ratio, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_5d_slope_v038_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 5)
    b = atr / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_14d_slope_v039_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 14)
    b = atr / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_21d_slope_v040_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 21)
    b = atr / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_63d_slope_v041_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 63)
    b = atr / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_126d_slope_v042_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 126)
    b = atr / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(63)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrp_252d_slope_v043_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 252)
    b = atr / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrterm_21v126_slope_v044_signal(high, low, close):
    s = _f11re_atr(high, low, close, 21)
    l = _f11re_atr(high, low, close, 126)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrpz_21d_slope_v045_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _z(atrp, 252)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrprank_21d_slope_v046_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _rank(atrp, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrpmom_21d_slope_v047_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp - atrp.shift(21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrwilder_14d_slope_v048_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    wild = tr.ewm(alpha=1.0 / 14.0, min_periods=7).mean()
    b = wild / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trp_1d_slope_v049_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = tr / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trz_63d_slope_v050_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = _z(tr, 63)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trz_126d_slope_v051_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 21)
    vov = atr.rolling(63, min_periods=21).std()
    lvl = atr.rolling(126, min_periods=63).mean()
    b = vov / lvl.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trz_252d_slope_v052_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = _z(tr, 252)
    base = b
    _d = base - base.shift(31)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trspike_21d_slope_v053_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    mx = tr.rolling(21, min_periods=10).max()
    atr = tr.rolling(63, min_periods=21).mean()
    b = mx / atr.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trshockcnt_63d_slope_v054_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 126)
    shock = (z > 2.0).astype(float)
    cnt = shock.rolling(63, min_periods=21).sum()
    b = cnt + 0.5 * z.clip(lower=0).rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrng_1d_slope_v055_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    gap = (tr - (high - low)) / close.replace(0, np.nan)
    b = gap.rolling(5, min_periods=3).mean()
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrng_5d_slope_v056_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    m = hl.rolling(5, min_periods=3).mean()
    b = m / m.shift(5).replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrng_21d_slope_v057_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    b = hl.rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrng_63d_slope_v058_signal(high, low, closeadj):
    hl = (high - low) / closeadj.replace(0, np.nan)
    b = hl.rolling(63, min_periods=21).mean()
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrng_252d_slope_v059_signal(open, high, low):
    up = (high - open).clip(lower=0)
    dn = (open - low).clip(lower=0)
    upm = up.rolling(252, min_periods=126).mean()
    dnm = dn.rolling(252, min_periods=126).mean()
    b = (upm - dnm) / (upm + dnm).replace(0, np.nan)
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrngz_21d_slope_v060_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    hl = (high - low)
    share = hl.rolling(21, min_periods=10).sum() / tr.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.5
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrngterm_21v126_slope_v061_signal(high, low, close, closeadj):
    s = (_f11re_hl_range(high, low, close)).rolling(21, min_periods=10).mean()
    l = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrngdisp_63d_slope_v062_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    sd = hl.rolling(63, min_periods=21).std()
    mn = hl.rolling(63, min_periods=21).mean()
    b = sd / mn.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_clrngpos_21d_slope_v063_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    b = pos.rolling(21, min_periods=10).mean() - 0.5
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkeff_21d_slope_v064_signal(high, low, close):
    park = _f11re_parkinson(high, low, 21)
    hl = _f11re_hl_range(high, low, close).rolling(21, min_periods=10).mean()
    b = park / hl.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkrsspr_63d_slope_v065_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    b = (g - r) / g.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yzparkspr_63d_slope_v066_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = (y - p) / y.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkvov_63d_slope_v067_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p.rolling(63, min_periods=21).std() / p.rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parksqueeze_slope_v068_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    lo = p.rolling(252, min_periods=126).min()
    b = p / lo.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkexpand_slope_v069_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    hi = p.rolling(252, min_periods=126).max()
    b = p / hi.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrregime_63d_slope_v070_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 14) / close.replace(0, np.nan)
    med = atrp.rolling(252, min_periods=126).median()
    above = (atrp > med).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkexcess_126d_slope_v071_signal(high, low, closeadj):
    p = _f11re_parkinson(high, low, 126) * np.sqrt(252.0)
    floor = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).quantile(0.1) * np.sqrt(252.0)
    b = p - floor
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkregimez_252d_slope_v072_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 126)
    b = _rank(g, 504)
    base = b
    _d = base - base.shift(63)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trcontract_slope_v073_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    contract = (tr < atr).astype(float)
    grp = (contract == 0).cumsum()
    streak = contract.groupby(grp).cumsum()
    # weight streak by how compressed the range is vs ATR (continuous tightness)
    tightness = (1.0 - tr / atr.replace(0, np.nan)).clip(lower=0)
    b = streak / 21.0 + tightness.rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onsharemom_slope_v074_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    share = von / (von + voc).replace(0, np.nan)
    b = share - share.shift(21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_blendz_63d_slope_v075_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 63)
    sg = _f11re_garman_klass(open, high, low, close, 63)
    sr = _f11re_rogers_satchell(open, high, low, close, 63)
    stacked = pd.concat([sp, sg, sr], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkcone_5d_slope_v076_signal(high, low):
    p = _f11re_parkinson(high, low, 5)
    b = _rank(p, 252)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkcone_63d_slope_v077_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = _rank(p, 504)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkcone_5d_slope_v078_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 5)
    b = _rank(g, 252)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrcone_63d_slope_v079_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = _rank(atrp, 504)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_upsemirng_21d_slope_v080_signal(open, high, low, close):
    upday = (close > open).astype(float)
    hl = _f11re_logsq(high, low) * upday
    var = hl.rolling(21, min_periods=10).sum() / (upday.rolling(21, min_periods=10).sum().replace(0, np.nan) * 4.0 * np.log(2.0))
    b = np.sqrt(var)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_dnsemirng_21d_slope_v081_signal(open, high, low, close):
    dnday = (close < open).astype(float)
    hl = _f11re_logsq(high, low) * dnday
    var = hl.rolling(21, min_periods=10).sum() / (dnday.rolling(21, min_periods=10).sum().replace(0, np.nan) * 4.0 * np.log(2.0))
    b = np.sqrt(var)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_semirngskew_63d_slope_v082_signal(open, high, low, close):
    upday = (close > open).astype(float)
    dnday = (close < open).astype(float)
    hl = _f11re_logsq(high, low)
    uv = (hl * upday).rolling(63, min_periods=21).sum() / upday.rolling(63, min_periods=21).sum().replace(0, np.nan)
    dv = (hl * dnday).rolling(63, min_periods=21).sum() / dnday.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (dv - uv) / (dv + uv).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_uwickshare_21d_slope_v083_signal(open, high, low, close):
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    rng = (high - low)
    share = upper.rolling(21, min_periods=10).sum() / rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.25
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_lwickshare_21d_slope_v084_signal(open, high, low, close):
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    rng = (high - low)
    share = lower.rolling(21, min_periods=10).sum() / rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.25
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_bodyrng_21d_slope_v085_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    b = (body / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkmom_63d_slope_v086_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = p - p.shift(21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkmom_63d_slope_v087_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = g - g.shift(21)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrmom_63d_slope_v088_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = atrp - atrp.shift(21)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkaccel_21d_slope_v089_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    chg = p - p.shift(21)
    b = chg - chg.shift(21)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkregdist_slope_v090_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    med = p.rolling(252, min_periods=126).median()
    b = p / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkregdist_slope_v091_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrsqueeze_slope_v092_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    lo = atrp.rolling(252, min_periods=126).min()
    hi = atrp.rolling(252, min_periods=126).max()
    b = (atrp - lo) / (hi - lo).replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkcompress_slope_v093_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    base = p.rolling(63, min_periods=21).mean()
    comp = (p < base).astype(float)
    grp = (comp == 0).cumsum()
    streak = comp.groupby(grp).cumsum()
    tight = (1.0 - p / base.replace(0, np.nan)).clip(lower=0)
    b = streak / 21.0 + tight.rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkexpcnt_slope_v094_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    base = p.rolling(63, min_periods=21).mean()
    blow = (p > 1.5 * base).astype(float)
    cnt = blow.rolling(63, min_periods=21).sum()
    mag = (p / base.replace(0, np.nan) - 1.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = cnt + 5.0 * mag
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkvov_126d_slope_v095_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p.rolling(126, min_periods=63).std() / p.rolling(126, min_periods=63).mean().replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkvov_63d_slope_v096_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    b = g.rolling(63, min_periods=21).std() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrvov_63d_slope_v097_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp.rolling(63, min_periods=21).std() / atrp.rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkparkspr_63d_slope_v098_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = (g - p) / p.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yzgkspr_63d_slope_v099_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 63)
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = (y - g) / y.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsgkspr_63d_slope_v100_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = (r - g) / g.replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrparkspr_63d_slope_v101_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    hlp = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = (atrp - hlp) / hlp.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parktermslope_slope_v102_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p126 = _f11re_parkinson(high, low, 126)
    p252 = _f11re_parkinson(high, low, 252)
    b = (p21 - p126) / p252.replace(0, np.nan)
    base = b
    _d = base - base.shift(63)
    _sd = base.rolling(189, min_periods=63).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parktermcurv_slope_v103_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p63 = _f11re_parkinson(high, low, 63)
    p126 = _f11re_parkinson(high, low, 126)
    b = (p21 - 2.0 * p63 + p126) / p63.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrtermslope_slope_v104_signal(high, low, close):
    a5 = _f11re_atr(high, low, close, 5)
    a21 = _f11re_atr(high, low, close, 21)
    a63 = _f11re_atr(high, low, close, 63)
    b = (a5 - a21) / a63.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkterm_63v252_slope_v105_signal(open, high, low, close):
    s = _f11re_garman_klass(open, high, low, close, 63)
    l = _f11re_garman_klass(open, high, low, close, 252)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_clrngpostrend_slope_v106_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    m = pos.rolling(21, min_periods=10).mean()
    b = m - m.shift(21)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_clrngupper_slope_v107_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(63, min_periods=21).mean() - 0.5
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_clrngdisp_slope_v108_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    b = pos.rolling(63, min_periods=21).std()
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onsharelong_slope_v109_signal(open, close):
    von = _f11re_overnight_var(open, close, 126)
    voc = _f11re_open_close_var(open, close, 126)
    b = von / (von + voc).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onvolz_slope_v110_signal(open, close):
    on = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    b = _z(on, 252)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_onvolrank_slope_v111_signal(open, close):
    on = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    b = _rank(on, 252)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_ocvolz_slope_v112_signal(open, close):
    oc = np.sqrt(_f11re_open_close_var(open, close, 21).clip(lower=0))
    b = _z(oc, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_amplitude_252d_slope_v113_signal(high, low, closeadj):
    hi = _rmax(high, 252)
    lo = _rmin(low, 252)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_amplitude_504d_slope_v114_signal(high, low, closeadj):
    hi = _rmax(high, 504)
    lo = _rmin(low, 504)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(42)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rangeeff_252d_slope_v115_signal(high, low, closeadj):
    hi = _rmax(high, 252)
    lo = _rmin(low, 252)
    path = (high - low).rolling(252, min_periods=126).sum()
    b = (hi - lo) / path.replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rangeeff_63d_slope_v116_signal(high, low, close):
    hi = _rmax(high, 63)
    lo = _rmin(low, 63)
    path = (high - low).rolling(63, min_periods=21).sum()
    b = (hi - lo) / path.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trexpdays_slope_v117_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    exp = (tr > atr).astype(float)
    cnt = exp.rolling(63, min_periods=21).mean()
    mag = (tr / atr.replace(0, np.nan) - 1.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = cnt + mag
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_contractrun_slope_v118_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    comp = (tr < atr).astype(float)
    grp = (comp == 0).cumsum()
    streak = comp.groupby(grp).cumsum()
    b = streak.rolling(63, min_periods=21).max() / 21.0 + streak / 63.0
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_shockrecency_slope_v119_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 126)
    shock = (z > 2.5)
    idx = pd.Series(np.arange(len(tr)), index=tr.index)
    last = idx.where(shock).ffill()
    dsince = (idx - last)
    b = -np.log1p(dsince.clip(lower=0)) + 0.1 * z.clip(lower=0)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_estagree_21d_slope_v120_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 21)
    sg = _f11re_garman_klass(open, high, low, close, 21)
    sr = _f11re_rogers_satchell(open, high, low, close, 21)
    stk = pd.concat([sp, sg, sr], axis=1)
    disp = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    b = -disp
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_estdisagz_slope_v121_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 63)
    sg = _f11re_garman_klass(open, high, low, close, 63)
    sr = _f11re_rogers_satchell(open, high, low, close, 63)
    stk = pd.concat([sp, sg, sr], axis=1)
    disp = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    b = _z(disp, 252)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_estspread_21d_slope_v122_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 21)
    sg = _f11re_garman_klass(open, high, low, close, 21)
    sr = _f11re_rogers_satchell(open, high, low, close, 21)
    sy = _f11re_yang_zhang(open, high, low, close, 21)
    stk = pd.concat([sp, sg, sr, sy], axis=1)
    b = (stk.max(axis=1) - stk.min(axis=1)) / stk.mean(axis=1).replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_retperpark_63d_slope_v123_signal(high, low, closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    p = _f11re_parkinson(high, low, 63)
    b = ret / (p * np.sqrt(63.0)).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_moveinatr_21d_slope_v124_signal(high, low, close, closeadj):
    move = (closeadj - closeadj.shift(21)).abs()
    atr = _f11re_atr(high, low, close, 21)
    b = move / (atr * np.sqrt(21.0)).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_vardrag_21d_slope_v125_signal(high, low):
    lr2 = _f11re_logsq(high, low)
    mx = lr2.rolling(21, min_periods=10).max()
    tot = lr2.rolling(21, min_periods=10).sum()
    b = mx / tot.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrsmoothspr_slope_v126_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    wild = tr.ewm(alpha=1.0 / 21.0, min_periods=11).mean()
    simple = tr.rolling(21, min_periods=10).mean()
    b = (wild - simple) / simple.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_medatr_21d_slope_v127_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    med = tr.rolling(21, min_periods=10).median()
    b = med / close.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrskew_63d_slope_v128_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    mn = tr.rolling(63, min_periods=21).mean()
    med = tr.rolling(63, min_periods=21).median()
    b = (mn - med) / mn.replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_park_504d_slope_v129_signal(high, low):
    b = _f11re_parkinson(high, low, 504) * np.sqrt(252.0)
    base = b
    _d = base - base.shift(42)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkterm_126v504_slope_v130_signal(high, low):
    s = _f11re_parkinson(high, low, 126)
    l = _f11re_parkinson(high, low, 504)
    b = s / l.replace(0, np.nan)
    base = b
    _d = base - base.shift(2)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atr_504d_slope_v131_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 504)
    b = atr / closeadj.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gk_504d_slope_v132_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 504) * np.sqrt(252.0)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(63)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkbreakout_slope_v133_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    lo = p.rolling(63, min_periods=21).min()
    expand = p / lo.replace(0, np.nan) - 1.0
    prior_tight = (lo / p.rolling(252, min_periods=126).median().replace(0, np.nan))
    b = expand * (1.0 - prior_tight).clip(lower=0)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrbreakout_slope_v134_signal(high, low, close):
    a5 = _f11re_atr(high, low, close, 5)
    a63 = _f11re_atr(high, low, close, 63)
    b = (a5 / a63.replace(0, np.nan) - 1.0)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkbandwidth_slope_v135_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    hi = p.rolling(63, min_periods=21).max()
    lo = p.rolling(63, min_periods=21).min()
    mn = p.rolling(63, min_periods=21).mean()
    b = (hi - lo) / mn.replace(0, np.nan)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_dirrng_21d_slope_v136_signal(open, high, low, close):
    sign = np.sign(close - open)
    rng = (high - low) / close.replace(0, np.nan)
    b = (sign * rng).rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gaptorange_slope_v137_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    rng = (high - low)
    b = (gap / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gapfollow_slope_v138_signal(open, close):
    gap = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    intraday = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    prod = gap * intraday
    b = prod.rolling(63, min_periods=21).mean() / (gap.abs().rolling(63, min_periods=21).mean()
                                                   * intraday.abs().rolling(63, min_periods=21).mean()).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rngskew_63d_slope_v139_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    b = hl.rolling(63, min_periods=21).skew()
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rngkurt_126d_slope_v140_signal(high, low, close):
    trp = _f11re_true_range(high, low, close) / close.replace(0, np.nan)
    b = trp.rolling(126, min_periods=63).kurt()
    base = b
    _d = base - base.shift(5)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rngtailratio_slope_v141_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    q90 = hl.rolling(126, min_periods=63).quantile(0.9)
    q50 = hl.rolling(126, min_periods=63).quantile(0.5)
    b = q90 / q50.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_blendcone_slope_v142_signal(open, high, low, close):
    cp = _rank(_f11re_parkinson(high, low, 21), 252)
    cg = _rank(_f11re_garman_klass(open, high, low, close, 21), 252)
    ca = _rank(_f11re_atr(high, low, close, 21) / close.replace(0, np.nan), 252)
    b = pd.concat([cp, cg, ca], axis=1).mean(axis=1)
    base = b
    _d = base - base.shift(10)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_atrcyclepos_slope_v143_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    lo = atrp.rolling(504, min_periods=252).min()
    hi = atrp.rolling(504, min_periods=252).max()
    b = (atrp - lo) / (hi - lo).replace(0, np.nan)
    base = b
    _d = base - base.shift(10)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parktrendpersist_slope_v144_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    chg = np.sign(p - p.shift(5))
    b = chg.rolling(63, min_periods=21).mean()
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_parkfastdelta_slope_v145_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p5 = _f11re_parkinson(high, low, 5)
    b = (p5 - p21) / p21.replace(0, np.nan)
    base = b
    _d = base - base.shift(21)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_gkz_126d_slope_v146_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 126)
    b = _z(g, 504)
    base = b
    _d = base - base.shift(21)
    _sd = base.rolling(63, min_periods=21).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_rsrank_126d_slope_v147_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 126)
    b = _rank(r, 504)
    base = b
    _d = base - base.shift(63)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_trzmom_slope_v148_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 63)
    sm = z.rolling(21, min_periods=10).mean()
    b = sm - sm.shift(21)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_hlrngreg_126d_slope_v149_signal(high, low, closeadj):
    hl = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    base = hl.rolling(252, min_periods=126).mean()
    b = hl / base.replace(0, np.nan) - 1.0
    base = b
    _d = base - base.shift(42)
    _sd = base.rolling(126, min_periods=42).std()
    result = _d / _sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f11re_f11_range_vol_estimators_yzcone_slope_v150_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 21)
    b = _rank(y, 252)
    base = b
    _d = base - base.shift(5)
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f11re_f11_range_vol_estimators_park_5d_slope_v001_signal,
    f11re_f11_range_vol_estimators_park_21d_slope_v002_signal,
    f11re_f11_range_vol_estimators_park_63d_slope_v003_signal,
    f11re_f11_range_vol_estimators_park_126d_slope_v004_signal,
    f11re_f11_range_vol_estimators_park_252d_slope_v005_signal,
    f11re_f11_range_vol_estimators_parkterm_21v126_slope_v006_signal,
    f11re_f11_range_vol_estimators_parkz_63d_slope_v007_signal,
    f11re_f11_range_vol_estimators_parkrank_21d_slope_v008_signal,
    f11re_f11_range_vol_estimators_parkmom_21d_slope_v009_signal,
    f11re_f11_range_vol_estimators_gk_5d_slope_v010_signal,
    f11re_f11_range_vol_estimators_gk_21d_slope_v011_signal,
    f11re_f11_range_vol_estimators_gk_63d_slope_v012_signal,
    f11re_f11_range_vol_estimators_gk_126d_slope_v013_signal,
    f11re_f11_range_vol_estimators_gk_252d_slope_v014_signal,
    f11re_f11_range_vol_estimators_gkterm_21v63_slope_v015_signal,
    f11re_f11_range_vol_estimators_gkz_63d_slope_v016_signal,
    f11re_f11_range_vol_estimators_gkrank_21d_slope_v017_signal,
    f11re_f11_range_vol_estimators_gkparkspr_21d_slope_v018_signal,
    f11re_f11_range_vol_estimators_rs_5d_slope_v019_signal,
    f11re_f11_range_vol_estimators_rs_21d_slope_v020_signal,
    f11re_f11_range_vol_estimators_rs_63d_slope_v021_signal,
    f11re_f11_range_vol_estimators_rs_126d_slope_v022_signal,
    f11re_f11_range_vol_estimators_rs_252d_slope_v023_signal,
    f11re_f11_range_vol_estimators_rsterm_21v126_slope_v024_signal,
    f11re_f11_range_vol_estimators_rsz_63d_slope_v025_signal,
    f11re_f11_range_vol_estimators_rsrank_21d_slope_v026_signal,
    f11re_f11_range_vol_estimators_rsparkspr_21d_slope_v027_signal,
    f11re_f11_range_vol_estimators_yz_21d_slope_v028_signal,
    f11re_f11_range_vol_estimators_yz_63d_slope_v029_signal,
    f11re_f11_range_vol_estimators_yz_126d_slope_v030_signal,
    f11re_f11_range_vol_estimators_yz_252d_slope_v031_signal,
    f11re_f11_range_vol_estimators_yzterm_21v126_slope_v032_signal,
    f11re_f11_range_vol_estimators_yzz_63d_slope_v033_signal,
    f11re_f11_range_vol_estimators_onvol_21d_slope_v034_signal,
    f11re_f11_range_vol_estimators_ocvol_21d_slope_v035_signal,
    f11re_f11_range_vol_estimators_onshare_63d_slope_v036_signal,
    f11re_f11_range_vol_estimators_onocratio_63d_slope_v037_signal,
    f11re_f11_range_vol_estimators_atrp_5d_slope_v038_signal,
    f11re_f11_range_vol_estimators_atrp_14d_slope_v039_signal,
    f11re_f11_range_vol_estimators_atrp_21d_slope_v040_signal,
    f11re_f11_range_vol_estimators_atrp_63d_slope_v041_signal,
    f11re_f11_range_vol_estimators_atrp_126d_slope_v042_signal,
    f11re_f11_range_vol_estimators_atrp_252d_slope_v043_signal,
    f11re_f11_range_vol_estimators_atrterm_21v126_slope_v044_signal,
    f11re_f11_range_vol_estimators_atrpz_21d_slope_v045_signal,
    f11re_f11_range_vol_estimators_atrprank_21d_slope_v046_signal,
    f11re_f11_range_vol_estimators_atrpmom_21d_slope_v047_signal,
    f11re_f11_range_vol_estimators_atrwilder_14d_slope_v048_signal,
    f11re_f11_range_vol_estimators_trp_1d_slope_v049_signal,
    f11re_f11_range_vol_estimators_trz_63d_slope_v050_signal,
    f11re_f11_range_vol_estimators_trz_126d_slope_v051_signal,
    f11re_f11_range_vol_estimators_trz_252d_slope_v052_signal,
    f11re_f11_range_vol_estimators_trspike_21d_slope_v053_signal,
    f11re_f11_range_vol_estimators_trshockcnt_63d_slope_v054_signal,
    f11re_f11_range_vol_estimators_hlrng_1d_slope_v055_signal,
    f11re_f11_range_vol_estimators_hlrng_5d_slope_v056_signal,
    f11re_f11_range_vol_estimators_hlrng_21d_slope_v057_signal,
    f11re_f11_range_vol_estimators_hlrng_63d_slope_v058_signal,
    f11re_f11_range_vol_estimators_hlrng_252d_slope_v059_signal,
    f11re_f11_range_vol_estimators_hlrngz_21d_slope_v060_signal,
    f11re_f11_range_vol_estimators_hlrngterm_21v126_slope_v061_signal,
    f11re_f11_range_vol_estimators_hlrngdisp_63d_slope_v062_signal,
    f11re_f11_range_vol_estimators_clrngpos_21d_slope_v063_signal,
    f11re_f11_range_vol_estimators_parkeff_21d_slope_v064_signal,
    f11re_f11_range_vol_estimators_gkrsspr_63d_slope_v065_signal,
    f11re_f11_range_vol_estimators_yzparkspr_63d_slope_v066_signal,
    f11re_f11_range_vol_estimators_parkvov_63d_slope_v067_signal,
    f11re_f11_range_vol_estimators_parksqueeze_slope_v068_signal,
    f11re_f11_range_vol_estimators_parkexpand_slope_v069_signal,
    f11re_f11_range_vol_estimators_atrregime_63d_slope_v070_signal,
    f11re_f11_range_vol_estimators_parkexcess_126d_slope_v071_signal,
    f11re_f11_range_vol_estimators_gkregimez_252d_slope_v072_signal,
    f11re_f11_range_vol_estimators_trcontract_slope_v073_signal,
    f11re_f11_range_vol_estimators_onsharemom_slope_v074_signal,
    f11re_f11_range_vol_estimators_blendz_63d_slope_v075_signal,
    f11re_f11_range_vol_estimators_parkcone_5d_slope_v076_signal,
    f11re_f11_range_vol_estimators_parkcone_63d_slope_v077_signal,
    f11re_f11_range_vol_estimators_gkcone_5d_slope_v078_signal,
    f11re_f11_range_vol_estimators_atrcone_63d_slope_v079_signal,
    f11re_f11_range_vol_estimators_upsemirng_21d_slope_v080_signal,
    f11re_f11_range_vol_estimators_dnsemirng_21d_slope_v081_signal,
    f11re_f11_range_vol_estimators_semirngskew_63d_slope_v082_signal,
    f11re_f11_range_vol_estimators_uwickshare_21d_slope_v083_signal,
    f11re_f11_range_vol_estimators_lwickshare_21d_slope_v084_signal,
    f11re_f11_range_vol_estimators_bodyrng_21d_slope_v085_signal,
    f11re_f11_range_vol_estimators_parkmom_63d_slope_v086_signal,
    f11re_f11_range_vol_estimators_gkmom_63d_slope_v087_signal,
    f11re_f11_range_vol_estimators_atrmom_63d_slope_v088_signal,
    f11re_f11_range_vol_estimators_parkaccel_21d_slope_v089_signal,
    f11re_f11_range_vol_estimators_parkregdist_slope_v090_signal,
    f11re_f11_range_vol_estimators_gkregdist_slope_v091_signal,
    f11re_f11_range_vol_estimators_atrsqueeze_slope_v092_signal,
    f11re_f11_range_vol_estimators_parkcompress_slope_v093_signal,
    f11re_f11_range_vol_estimators_parkexpcnt_slope_v094_signal,
    f11re_f11_range_vol_estimators_parkvov_126d_slope_v095_signal,
    f11re_f11_range_vol_estimators_gkvov_63d_slope_v096_signal,
    f11re_f11_range_vol_estimators_atrvov_63d_slope_v097_signal,
    f11re_f11_range_vol_estimators_gkparkspr_63d_slope_v098_signal,
    f11re_f11_range_vol_estimators_yzgkspr_63d_slope_v099_signal,
    f11re_f11_range_vol_estimators_rsgkspr_63d_slope_v100_signal,
    f11re_f11_range_vol_estimators_atrparkspr_63d_slope_v101_signal,
    f11re_f11_range_vol_estimators_parktermslope_slope_v102_signal,
    f11re_f11_range_vol_estimators_parktermcurv_slope_v103_signal,
    f11re_f11_range_vol_estimators_atrtermslope_slope_v104_signal,
    f11re_f11_range_vol_estimators_gkterm_63v252_slope_v105_signal,
    f11re_f11_range_vol_estimators_clrngpostrend_slope_v106_signal,
    f11re_f11_range_vol_estimators_clrngupper_slope_v107_signal,
    f11re_f11_range_vol_estimators_clrngdisp_slope_v108_signal,
    f11re_f11_range_vol_estimators_onsharelong_slope_v109_signal,
    f11re_f11_range_vol_estimators_onvolz_slope_v110_signal,
    f11re_f11_range_vol_estimators_onvolrank_slope_v111_signal,
    f11re_f11_range_vol_estimators_ocvolz_slope_v112_signal,
    f11re_f11_range_vol_estimators_amplitude_252d_slope_v113_signal,
    f11re_f11_range_vol_estimators_amplitude_504d_slope_v114_signal,
    f11re_f11_range_vol_estimators_rangeeff_252d_slope_v115_signal,
    f11re_f11_range_vol_estimators_rangeeff_63d_slope_v116_signal,
    f11re_f11_range_vol_estimators_trexpdays_slope_v117_signal,
    f11re_f11_range_vol_estimators_contractrun_slope_v118_signal,
    f11re_f11_range_vol_estimators_shockrecency_slope_v119_signal,
    f11re_f11_range_vol_estimators_estagree_21d_slope_v120_signal,
    f11re_f11_range_vol_estimators_estdisagz_slope_v121_signal,
    f11re_f11_range_vol_estimators_estspread_21d_slope_v122_signal,
    f11re_f11_range_vol_estimators_retperpark_63d_slope_v123_signal,
    f11re_f11_range_vol_estimators_moveinatr_21d_slope_v124_signal,
    f11re_f11_range_vol_estimators_vardrag_21d_slope_v125_signal,
    f11re_f11_range_vol_estimators_atrsmoothspr_slope_v126_signal,
    f11re_f11_range_vol_estimators_medatr_21d_slope_v127_signal,
    f11re_f11_range_vol_estimators_atrskew_63d_slope_v128_signal,
    f11re_f11_range_vol_estimators_park_504d_slope_v129_signal,
    f11re_f11_range_vol_estimators_parkterm_126v504_slope_v130_signal,
    f11re_f11_range_vol_estimators_atr_504d_slope_v131_signal,
    f11re_f11_range_vol_estimators_gk_504d_slope_v132_signal,
    f11re_f11_range_vol_estimators_parkbreakout_slope_v133_signal,
    f11re_f11_range_vol_estimators_atrbreakout_slope_v134_signal,
    f11re_f11_range_vol_estimators_parkbandwidth_slope_v135_signal,
    f11re_f11_range_vol_estimators_dirrng_21d_slope_v136_signal,
    f11re_f11_range_vol_estimators_gaptorange_slope_v137_signal,
    f11re_f11_range_vol_estimators_gapfollow_slope_v138_signal,
    f11re_f11_range_vol_estimators_rngskew_63d_slope_v139_signal,
    f11re_f11_range_vol_estimators_rngkurt_126d_slope_v140_signal,
    f11re_f11_range_vol_estimators_rngtailratio_slope_v141_signal,
    f11re_f11_range_vol_estimators_blendcone_slope_v142_signal,
    f11re_f11_range_vol_estimators_atrcyclepos_slope_v143_signal,
    f11re_f11_range_vol_estimators_parktrendpersist_slope_v144_signal,
    f11re_f11_range_vol_estimators_parkfastdelta_slope_v145_signal,
    f11re_f11_range_vol_estimators_gkz_126d_slope_v146_signal,
    f11re_f11_range_vol_estimators_rsrank_126d_slope_v147_signal,
    f11re_f11_range_vol_estimators_trzmom_slope_v148_signal,
    f11re_f11_range_vol_estimators_hlrngreg_126d_slope_v149_signal,
    f11re_f11_range_vol_estimators_yzcone_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_001_150 = REGISTRY


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

    print("OK f11_range_vol_estimators_2nd_derivatives_001_150_claude: %d features pass" % n_features)
