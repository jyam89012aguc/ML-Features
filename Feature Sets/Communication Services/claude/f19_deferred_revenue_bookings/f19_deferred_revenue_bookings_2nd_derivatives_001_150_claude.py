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


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _cover(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _billings(deferredrev, revenue, w):
    return revenue + (deferredrev - deferredrev.shift(w))


def _drevrecv(deferredrev, receivables):
    return deferredrev / receivables.replace(0, np.nan)


def _drevcash(deferredrev, ncfo):
    return deferredrev / ncfo.replace(0, np.nan)


def _d1(base, rw, zw):
    d = (base - base.shift(rw)) / float(rw)
    return d / _std(d, zw).replace(0, np.nan)


def _d2(base, rw, zw):
    d = (base - 2.0 * base.shift(rw) + base.shift(2 * rw)) / float(rw * rw)
    return d / _std(d, zw).replace(0, np.nan)


def f19db_f19_deferred_revenue_bookings_covernorm_21d_slope_v001_signal(deferredrev, revenue, ncfo):
    c = _cover(deferredrev, revenue)
    base = c / _mean(c, 63).replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(ncfo, 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covernorm_42d_slope_v002_signal(deferredrev, revenue, ncfo):
    c = _cover(deferredrev, revenue)
    base = c / _mean(c, 126).replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(ncfo, 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covernorm_63d_slope_v003_signal(deferredrev, revenue, ncfo):
    c = _cover(deferredrev, revenue)
    base = c / _mean(c, 126).replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(ncfo, 126))
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covernorm_84d_slope_v004_signal(deferredrev, revenue, ncfo):
    c = _cover(deferredrev, revenue)
    base = c / _mean(c, 252).replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(ncfo, 252))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covernorm_126d_slope_v005_signal(deferredrev, revenue, ncfo):
    c = _cover(deferredrev, revenue)
    base = c / _mean(c, 504).replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(ncfo, 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverema_21d_slope_v006_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue)
    base = c.ewm(span=63, min_periods=max(5, 63//3)).mean()
    d = _d1(base, 21, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverema_42d_slope_v007_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue)
    base = c.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 42, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverema_63d_slope_v008_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue)
    base = c.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 63, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverema_84d_slope_v009_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue)
    base = c.ewm(span=252, min_periods=max(5, 252//3)).mean()
    d = _d1(base, 84, 252)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverema_126d_slope_v010_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue)
    base = c.ewm(span=504, min_periods=max(5, 504//3)).mean()
    d = _d1(base, 126, 252)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverpos_21d_slope_v011_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    hi = _rmax(c, 63); lo = _rmin(c, 63)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverpos_42d_slope_v012_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    hi = _rmax(c, 126); lo = _rmin(c, 126)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverpos_63d_slope_v013_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    hi = _rmax(c, 126); lo = _rmin(c, 126)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverpos_84d_slope_v014_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    hi = _rmax(c, 252); lo = _rmin(c, 252)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(252) * 5.0)
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverpos_126d_slope_v015_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    hi = _rmax(c, 504); lo = _rmin(c, 504)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(252) * 5.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverz_21d_slope_v016_signal(deferredrev, revenue, ncfo):
    base = _z(_cover(deferredrev, revenue), 63)
    d = _d1(base, 21, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverz_42d_slope_v017_signal(deferredrev, revenue, ncfo):
    base = _z(_cover(deferredrev, revenue), 126)
    d = _d1(base, 42, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverz_63d_slope_v018_signal(deferredrev, revenue, ncfo):
    base = _z(_cover(deferredrev, revenue), 126)
    d = _d1(base, 63, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverz_84d_slope_v019_signal(deferredrev, revenue, ncfo):
    base = _z(_cover(deferredrev, revenue), 252)
    d = _d1(base, 84, 252)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverz_126d_slope_v020_signal(deferredrev, revenue, ncfo):
    base = _z(_cover(deferredrev, revenue), 504)
    d = _d1(base, 126, 252)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverrk_21d_slope_v021_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c.rolling(63, min_periods=max(5, 63//3)).rank(pct=True) - 0.5
    d = _d1(base, 21, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverrk_42d_slope_v022_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c.rolling(126, min_periods=max(5, 126//3)).rank(pct=True) - 0.5
    d = _d1(base, 42, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverrk_63d_slope_v023_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c.rolling(126, min_periods=max(5, 126//3)).rank(pct=True) - 0.5
    d = _d1(base, 63, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverrk_84d_slope_v024_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c.rolling(252, min_periods=max(5, 252//3)).rank(pct=True) - 0.5
    d = _d1(base, 84, 252)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 252))
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverrk_126d_slope_v025_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c.rolling(504, min_periods=max(5, 504//3)).rank(pct=True) - 0.5
    d = _d1(base, 126, 252)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 252))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevg_21d_slope_v026_signal(deferredrev, receivables):
    base = np.log(deferredrev.replace(0,np.nan) / deferredrev.shift(63).replace(0,np.nan))
    d = _d1(base, 21, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevg_42d_slope_v027_signal(deferredrev, receivables):
    base = np.log(deferredrev.replace(0,np.nan) / deferredrev.shift(126).replace(0,np.nan))
    d = _d1(base, 42, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevg_63d_slope_v028_signal(deferredrev, receivables):
    base = np.log(deferredrev.replace(0,np.nan) / deferredrev.shift(126).replace(0,np.nan))
    d = _d1(base, 63, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevg_84d_slope_v029_signal(deferredrev, receivables):
    base = np.log(deferredrev.replace(0,np.nan) / deferredrev.shift(252).replace(0,np.nan))
    d = _d1(base, 84, 252)
    m = np.tanh(receivables.pct_change(252) * 3.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevg_126d_slope_v030_signal(deferredrev, receivables):
    base = np.log(deferredrev.replace(0,np.nan) / deferredrev.shift(504).replace(0,np.nan))
    d = _d1(base, 126, 252)
    m = np.tanh(receivables.pct_change(252) * 3.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvnorm_21d_slope_v031_signal(deferredrev, receivables, revenue):
    r = _drevrecv(deferredrev, receivables)
    base = r / _mean(r, 63).replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvnorm_42d_slope_v032_signal(deferredrev, receivables, revenue):
    r = _drevrecv(deferredrev, receivables)
    base = r / _mean(r, 126).replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvnorm_63d_slope_v033_signal(deferredrev, receivables, revenue):
    r = _drevrecv(deferredrev, receivables)
    base = r / _mean(r, 126).replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvnorm_84d_slope_v034_signal(deferredrev, receivables, revenue):
    r = _drevrecv(deferredrev, receivables)
    base = r / _mean(r, 252).replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(revenue.pct_change(21), 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvnorm_126d_slope_v035_signal(deferredrev, receivables, revenue):
    r = _drevrecv(deferredrev, receivables)
    base = r / _mean(r, 504).replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(revenue.pct_change(21), 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvz_21d_slope_v036_signal(deferredrev, receivables, ncfo):
    base = _z(_drevrecv(deferredrev, receivables), 63)
    d = _d1(base, 21, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvz_42d_slope_v037_signal(deferredrev, receivables, ncfo):
    base = _z(_drevrecv(deferredrev, receivables), 126)
    d = _d1(base, 42, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvz_63d_slope_v038_signal(deferredrev, receivables, ncfo):
    base = _z(_drevrecv(deferredrev, receivables), 126)
    d = _d1(base, 63, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvz_84d_slope_v039_signal(deferredrev, receivables, ncfo):
    base = _z(_drevrecv(deferredrev, receivables), 252)
    d = _d1(base, 84, 252)
    m = np.tanh((ncfo - _mean(ncfo, 252)) / _std(ncfo, 252).replace(0, np.nan))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevrecvz_126d_slope_v040_signal(deferredrev, receivables, ncfo):
    base = _z(_drevrecv(deferredrev, receivables), 504)
    d = _d1(base, 126, 252)
    m = np.tanh((ncfo - _mean(ncfo, 252)) / _std(ncfo, 252).replace(0, np.nan))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevcashema_21d_slope_v041_signal(deferredrev, ncfo, receivables):
    r = np.tanh(_drevcash(deferredrev, ncfo))
    base = r.ewm(span=63, min_periods=max(5, 63//3)).mean()
    d = _d1(base, 21, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevcashema_42d_slope_v042_signal(deferredrev, ncfo, receivables):
    r = np.tanh(_drevcash(deferredrev, ncfo))
    base = r.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 42, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevcashema_63d_slope_v043_signal(deferredrev, ncfo, receivables):
    r = np.tanh(_drevcash(deferredrev, ncfo))
    base = r.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 63, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevcashema_84d_slope_v044_signal(deferredrev, ncfo, receivables):
    r = np.tanh(_drevcash(deferredrev, ncfo))
    base = r.ewm(span=252, min_periods=max(5, 252//3)).mean()
    d = _d1(base, 84, 252)
    m = (receivables.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_drevcashema_126d_slope_v045_signal(deferredrev, ncfo, receivables):
    r = np.tanh(_drevcash(deferredrev, ncfo))
    base = r.ewm(span=504, min_periods=max(5, 504//3)).mean()
    d = _d1(base, 126, 252)
    m = (receivables.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_bookturnnorm_21d_slope_v046_signal(deferredrev, revenue):
    t = revenue / deferredrev.replace(0, np.nan)
    base = t - _mean(t, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_bookturnnorm_42d_slope_v047_signal(deferredrev, revenue):
    t = revenue / deferredrev.replace(0, np.nan)
    base = t - _mean(t, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_bookturnnorm_63d_slope_v048_signal(deferredrev, revenue):
    t = revenue / deferredrev.replace(0, np.nan)
    base = t - _mean(t, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_bookturnnorm_84d_slope_v049_signal(deferredrev, revenue):
    t = revenue / deferredrev.replace(0, np.nan)
    base = t - _mean(t, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(deferredrev.pct_change(63), 252))
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_bookturnnorm_126d_slope_v050_signal(deferredrev, revenue):
    t = revenue / deferredrev.replace(0, np.nan)
    base = t - _mean(t, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(deferredrev.pct_change(63), 252))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncforecv_21d_slope_v051_signal(ncfo, receivables, revenue):
    nr = ncfo / receivables.replace(0, np.nan)
    base = nr - _mean(nr, 63)
    d = _d1(base, 21, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncforecv_42d_slope_v052_signal(ncfo, receivables, revenue):
    nr = ncfo / receivables.replace(0, np.nan)
    base = nr - _mean(nr, 126)
    d = _d1(base, 42, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncforecv_63d_slope_v053_signal(ncfo, receivables, revenue):
    nr = ncfo / receivables.replace(0, np.nan)
    base = nr - _mean(nr, 126)
    d = _d1(base, 63, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncforecv_84d_slope_v054_signal(ncfo, receivables, revenue):
    nr = ncfo / receivables.replace(0, np.nan)
    base = nr - _mean(nr, 252)
    d = _d1(base, 84, 252)
    m = np.tanh((revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0) * 5.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncforecv_126d_slope_v055_signal(ncfo, receivables, revenue):
    nr = ncfo / receivables.replace(0, np.nan)
    base = nr - _mean(nr, 504)
    d = _d1(base, 126, 252)
    m = np.tanh((revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0) * 5.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_booksharepos_21d_slope_v056_signal(deferredrev, receivables, ncfo):
    sh = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    hi = _rmax(sh, 63); lo = _rmin(sh, 63)
    base = (sh - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_booksharepos_42d_slope_v057_signal(deferredrev, receivables, ncfo):
    sh = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    hi = _rmax(sh, 126); lo = _rmin(sh, 126)
    base = (sh - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_booksharepos_63d_slope_v058_signal(deferredrev, receivables, ncfo):
    sh = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    hi = _rmax(sh, 126); lo = _rmin(sh, 126)
    base = (sh - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_booksharepos_84d_slope_v059_signal(deferredrev, receivables, ncfo):
    sh = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    hi = _rmax(sh, 252); lo = _rmin(sh, 252)
    base = (sh - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = (ncfo > 0).astype(float).rolling(252, min_periods=max(5,252//3)).mean() - 0.5
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_booksharepos_126d_slope_v060_signal(deferredrev, receivables, ncfo):
    sh = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    hi = _rmax(sh, 504); lo = _rmin(sh, 504)
    base = (sh - lo) / (hi - lo).replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = (ncfo > 0).astype(float).rolling(252, min_periods=max(5,252//3)).mean() - 0.5
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logdrevext_21d_slope_v061_signal(deferredrev, receivables):
    ld = np.log(deferredrev.replace(0, np.nan))
    base = ld - _mean(ld, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logdrevext_42d_slope_v062_signal(deferredrev, receivables):
    ld = np.log(deferredrev.replace(0, np.nan))
    base = ld - _mean(ld, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logdrevext_63d_slope_v063_signal(deferredrev, receivables):
    ld = np.log(deferredrev.replace(0, np.nan))
    base = ld - _mean(ld, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logdrevext_84d_slope_v064_signal(deferredrev, receivables):
    ld = np.log(deferredrev.replace(0, np.nan))
    base = ld - _mean(ld, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(receivables.pct_change(63), 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logdrevext_126d_slope_v065_signal(deferredrev, receivables):
    ld = np.log(deferredrev.replace(0, np.nan))
    base = ld - _mean(ld, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(receivables.pct_change(63), 252))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billratio_21d_slope_v066_signal(deferredrev, revenue):
    bill = _billings(deferredrev, revenue, 63)
    base = bill / revenue.replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billratio_42d_slope_v067_signal(deferredrev, revenue):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / revenue.replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billratio_63d_slope_v068_signal(deferredrev, revenue):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / revenue.replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billratio_84d_slope_v069_signal(deferredrev, revenue):
    bill = _billings(deferredrev, revenue, 252)
    base = bill / revenue.replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = (deferredrev.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billratio_126d_slope_v070_signal(deferredrev, revenue):
    bill = _billings(deferredrev, revenue, 504)
    base = bill / revenue.replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = (deferredrev.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billrecv_21d_slope_v071_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 63)
    base = bill / receivables.replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = np.tanh((revenue.pct_change(126)) * 4.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billrecv_42d_slope_v072_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / receivables.replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = np.tanh((revenue.pct_change(126)) * 4.0)
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billrecv_63d_slope_v073_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / receivables.replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = np.tanh((revenue.pct_change(126)) * 4.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billrecv_84d_slope_v074_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 252)
    base = bill / receivables.replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = np.tanh((revenue.pct_change(252)) * 4.0)
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billrecv_126d_slope_v075_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 504)
    base = bill / receivables.replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = np.tanh((revenue.pct_change(252)) * 4.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_revcash_21d_slope_v076_signal(revenue, ncfo):
    rc = revenue / ncfo.replace(0, np.nan)
    base = np.tanh(rc - _mean(rc, 63))
    d = _d1(base, 21, 126)
    m = np.tanh(ncfo.pct_change(63).clip(-2, 2))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_revcash_42d_slope_v077_signal(revenue, ncfo):
    rc = revenue / ncfo.replace(0, np.nan)
    base = np.tanh(rc - _mean(rc, 126))
    d = _d1(base, 42, 126)
    m = np.tanh(ncfo.pct_change(63).clip(-2, 2))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_revcash_63d_slope_v078_signal(revenue, ncfo):
    rc = revenue / ncfo.replace(0, np.nan)
    base = np.tanh(rc - _mean(rc, 126))
    d = _d1(base, 63, 126)
    m = np.tanh(ncfo.pct_change(63).clip(-2, 2))
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_revcash_84d_slope_v079_signal(revenue, ncfo):
    rc = revenue / ncfo.replace(0, np.nan)
    base = np.tanh(rc - _mean(rc, 252))
    d = _d1(base, 84, 252)
    m = np.tanh(ncfo.pct_change(63).clip(-2, 2))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_revcash_126d_slope_v080_signal(revenue, ncfo):
    rc = revenue / ncfo.replace(0, np.nan)
    base = np.tanh(rc - _mean(rc, 504))
    d = _d1(base, 126, 252)
    m = np.tanh(ncfo.pct_change(63).clip(-2, 2))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashmgnema_21d_slope_v081_signal(revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    base = cm.ewm(span=63, min_periods=max(5, 63//3)).mean()
    d = _d1(base, 21, 126)
    m = np.tanh(_z(ncfo, 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashmgnema_42d_slope_v082_signal(revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    base = cm.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 42, 126)
    m = np.tanh(_z(ncfo, 126))
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashmgnema_63d_slope_v083_signal(revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    base = cm.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 63, 126)
    m = np.tanh(_z(ncfo, 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashmgnema_84d_slope_v084_signal(revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    base = cm.ewm(span=252, min_periods=max(5, 252//3)).mean()
    d = _d1(base, 84, 252)
    m = np.tanh(_z(ncfo, 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashmgnema_126d_slope_v085_signal(revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    base = cm.ewm(span=504, min_periods=max(5, 504//3)).mean()
    d = _d1(base, 126, 252)
    m = np.tanh(_z(ncfo, 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashconvnorm_21d_slope_v086_signal(deferredrev, ncfo, receivables):
    cv = ncfo / deferredrev.replace(0, np.nan)
    base = cv - _mean(cv, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashconvnorm_42d_slope_v087_signal(deferredrev, ncfo, receivables):
    cv = ncfo / deferredrev.replace(0, np.nan)
    base = cv - _mean(cv, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashconvnorm_63d_slope_v088_signal(deferredrev, ncfo, receivables):
    cv = ncfo / deferredrev.replace(0, np.nan)
    base = cv - _mean(cv, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashconvnorm_84d_slope_v089_signal(deferredrev, ncfo, receivables):
    cv = ncfo / deferredrev.replace(0, np.nan)
    base = cv - _mean(cv, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashconvnorm_126d_slope_v090_signal(deferredrev, ncfo, receivables):
    cv = ncfo / deferredrev.replace(0, np.nan)
    base = cv - _mean(cv, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(np.log(receivables.replace(0,np.nan)), 252))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashbill_21d_slope_v091_signal(deferredrev, revenue, ncfo):
    bill = _billings(deferredrev, revenue, 63)
    base = ncfo / bill.replace(0, np.nan)
    d = _d1(base, 21, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashbill_42d_slope_v092_signal(deferredrev, revenue, ncfo):
    bill = _billings(deferredrev, revenue, 126)
    base = ncfo / bill.replace(0, np.nan)
    d = _d1(base, 42, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashbill_63d_slope_v093_signal(deferredrev, revenue, ncfo):
    bill = _billings(deferredrev, revenue, 126)
    base = ncfo / bill.replace(0, np.nan)
    d = _d1(base, 63, 126)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(126) * 5.0)
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashbill_84d_slope_v094_signal(deferredrev, revenue, ncfo):
    bill = _billings(deferredrev, revenue, 252)
    base = ncfo / bill.replace(0, np.nan)
    d = _d1(base, 84, 252)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(252) * 5.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashbill_126d_slope_v095_signal(deferredrev, revenue, ncfo):
    bill = _billings(deferredrev, revenue, 504)
    base = ncfo / bill.replace(0, np.nan)
    d = _d1(base, 126, 252)
    m = np.tanh(np.log(revenue.replace(0,np.nan)).diff(252) * 5.0)
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_dsoz_21d_slope_v096_signal(revenue, receivables, ncfo):
    d = receivables / revenue.replace(0, np.nan)
    base = _z(d, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_dsoz_42d_slope_v097_signal(revenue, receivables, ncfo):
    d = receivables / revenue.replace(0, np.nan)
    base = _z(d, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_dsoz_63d_slope_v098_signal(revenue, receivables, ncfo):
    d = receivables / revenue.replace(0, np.nan)
    base = _z(d, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 126).replace(0, np.nan))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_dsoz_84d_slope_v099_signal(revenue, receivables, ncfo):
    d = receivables / revenue.replace(0, np.nan)
    base = _z(d, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_dsoz_126d_slope_v100_signal(revenue, receivables, ncfo):
    d = receivables / revenue.replace(0, np.nan)
    base = _z(d, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covermean_21d_slope_v101_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c - _mean(c, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covermean_42d_slope_v102_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c - _mean(c, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covermean_63d_slope_v103_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c - _mean(c, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 126))
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covermean_84d_slope_v104_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c - _mean(c, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 252))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_covermean_126d_slope_v105_signal(deferredrev, revenue):
    c = _cover(deferredrev, revenue)
    base = c - _mean(c, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(np.log(deferredrev.replace(0,np.nan)).diff(21), 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_pipeg_21d_slope_v106_signal(deferredrev, receivables):
    pipe = (deferredrev + receivables)
    base = np.log(pipe.replace(0,np.nan) / pipe.shift(63).replace(0,np.nan))
    d = _d1(base, 21, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_pipeg_42d_slope_v107_signal(deferredrev, receivables):
    pipe = (deferredrev + receivables)
    base = np.log(pipe.replace(0,np.nan) / pipe.shift(126).replace(0,np.nan))
    d = _d1(base, 42, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_pipeg_63d_slope_v108_signal(deferredrev, receivables):
    pipe = (deferredrev + receivables)
    base = np.log(pipe.replace(0,np.nan) / pipe.shift(126).replace(0,np.nan))
    d = _d1(base, 63, 126)
    m = np.tanh(receivables.pct_change(126) * 3.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_pipeg_84d_slope_v109_signal(deferredrev, receivables):
    pipe = (deferredrev + receivables)
    base = np.log(pipe.replace(0,np.nan) / pipe.shift(252).replace(0,np.nan))
    d = _d1(base, 84, 252)
    m = np.tanh(receivables.pct_change(252) * 3.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_pipeg_126d_slope_v110_signal(deferredrev, receivables):
    pipe = (deferredrev + receivables)
    base = np.log(pipe.replace(0,np.nan) / pipe.shift(504).replace(0,np.nan))
    d = _d1(base, 126, 252)
    m = np.tanh(receivables.pct_change(252) * 3.0)
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_visibdisp_21d_slope_v111_signal(deferredrev, revenue):
    v = (deferredrev / revenue.replace(0, np.nan)) * 12.0
    base = v - v.ewm(span=63, min_periods=max(5, 63//3)).mean()
    d = _d1(base, 21, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_visibdisp_42d_slope_v112_signal(deferredrev, revenue):
    v = (deferredrev / revenue.replace(0, np.nan)) * 12.0
    base = v - v.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 42, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_visibdisp_63d_slope_v113_signal(deferredrev, revenue):
    v = (deferredrev / revenue.replace(0, np.nan)) * 12.0
    base = v - v.ewm(span=126, min_periods=max(5, 126//3)).mean()
    d = _d1(base, 63, 126)
    m = np.tanh(_z(revenue.pct_change(21), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_visibdisp_84d_slope_v114_signal(deferredrev, revenue):
    v = (deferredrev / revenue.replace(0, np.nan)) * 12.0
    base = v - v.ewm(span=252, min_periods=max(5, 252//3)).mean()
    d = _d1(base, 84, 252)
    m = np.tanh(_z(revenue.pct_change(21), 252))
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_visibdisp_126d_slope_v115_signal(deferredrev, revenue):
    v = (deferredrev / revenue.replace(0, np.nan)) * 12.0
    base = v - v.ewm(span=504, min_periods=max(5, 504//3)).mean()
    d = _d1(base, 126, 252)
    m = np.tanh(_z(revenue.pct_change(21), 252))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncfog_21d_slope_v116_signal(ncfo):
    la = np.log(ncfo.abs().replace(0, np.nan))
    base = la - _mean(la, 63)
    d = _d1(base, 21, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncfog_42d_slope_v117_signal(ncfo):
    la = np.log(ncfo.abs().replace(0, np.nan))
    base = la - _mean(la, 126)
    d = _d1(base, 42, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncfog_63d_slope_v118_signal(ncfo):
    la = np.log(ncfo.abs().replace(0, np.nan))
    base = la - _mean(la, 126)
    d = _d1(base, 63, 126)
    m = np.tanh((ncfo - _mean(ncfo, 126)) / _std(ncfo, 126).replace(0, np.nan))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncfog_84d_slope_v119_signal(ncfo):
    la = np.log(ncfo.abs().replace(0, np.nan))
    base = la - _mean(la, 252)
    d = _d1(base, 84, 252)
    m = np.tanh((ncfo - _mean(ncfo, 252)) / _std(ncfo, 252).replace(0, np.nan))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_ncfog_126d_slope_v120_signal(ncfo):
    la = np.log(ncfo.abs().replace(0, np.nan))
    base = la - _mean(la, 504)
    d = _d1(base, 126, 252)
    m = np.tanh((ncfo - _mean(ncfo, 252)) / _std(ncfo, 252).replace(0, np.nan))
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logspreadext_21d_slope_v121_signal(deferredrev, revenue, receivables):
    sp = np.log(deferredrev.replace(0,np.nan)) - np.log(revenue.replace(0,np.nan))
    base = sp - _mean(sp, 63)
    d = _d1(base, 21, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logspreadext_42d_slope_v122_signal(deferredrev, revenue, receivables):
    sp = np.log(deferredrev.replace(0,np.nan)) - np.log(revenue.replace(0,np.nan))
    base = sp - _mean(sp, 126)
    d = _d1(base, 42, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logspreadext_63d_slope_v123_signal(deferredrev, revenue, receivables):
    sp = np.log(deferredrev.replace(0,np.nan)) - np.log(revenue.replace(0,np.nan))
    base = sp - _mean(sp, 126)
    d = _d1(base, 63, 126)
    m = (receivables.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logspreadext_84d_slope_v124_signal(deferredrev, revenue, receivables):
    sp = np.log(deferredrev.replace(0,np.nan)) - np.log(revenue.replace(0,np.nan))
    base = sp - _mean(sp, 252)
    d = _d1(base, 84, 252)
    m = (receivables.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_logspreadext_126d_slope_v125_signal(deferredrev, revenue, receivables):
    sp = np.log(deferredrev.replace(0,np.nan)) - np.log(revenue.replace(0,np.nan))
    base = sp - _mean(sp, 504)
    d = _d1(base, 126, 252)
    m = (receivables.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverdso_21d_slope_v126_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue) - receivables / revenue.replace(0, np.nan)
    base = _z(c, 63)
    d = _d1(base, 21, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverdso_42d_slope_v127_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue) - receivables / revenue.replace(0, np.nan)
    base = _z(c, 126)
    d = _d1(base, 42, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverdso_63d_slope_v128_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue) - receivables / revenue.replace(0, np.nan)
    base = _z(c, 126)
    d = _d1(base, 63, 126)
    m = np.tanh(_z(deferredrev.pct_change(63), 126))
    r = d - d.shift(63) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverdso_84d_slope_v129_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue) - receivables / revenue.replace(0, np.nan)
    base = _z(c, 252)
    d = _d1(base, 84, 252)
    m = np.tanh(_z(deferredrev.pct_change(63), 252))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_coverdso_126d_slope_v130_signal(deferredrev, revenue, receivables):
    c = _cover(deferredrev, revenue) - receivables / revenue.replace(0, np.nan)
    base = _z(c, 504)
    d = _d1(base, 126, 252)
    m = np.tanh(_z(deferredrev.pct_change(63), 252))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashsharenorm_21d_slope_v131_signal(deferredrev, receivables, ncfo, revenue):
    cs = ncfo / (deferredrev + receivables).replace(0, np.nan)
    base = cs - _mean(cs, 63)
    d = _d1(base, 21, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashsharenorm_42d_slope_v132_signal(deferredrev, receivables, ncfo, revenue):
    cs = ncfo / (deferredrev + receivables).replace(0, np.nan)
    base = cs - _mean(cs, 126)
    d = _d1(base, 42, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = d - d.shift(42) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashsharenorm_63d_slope_v133_signal(deferredrev, receivables, ncfo, revenue):
    cs = ncfo / (deferredrev + receivables).replace(0, np.nan)
    base = cs - _mean(cs, 126)
    d = _d1(base, 63, 126)
    m = np.tanh((revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0) * 5.0)
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashsharenorm_84d_slope_v134_signal(deferredrev, receivables, ncfo, revenue):
    cs = ncfo / (deferredrev + receivables).replace(0, np.nan)
    base = cs - _mean(cs, 252)
    d = _d1(base, 84, 252)
    m = np.tanh((revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0) * 5.0)
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_cashsharenorm_126d_slope_v135_signal(deferredrev, receivables, ncfo, revenue):
    cs = ncfo / (deferredrev + receivables).replace(0, np.nan)
    base = cs - _mean(cs, 504)
    d = _d1(base, 126, 252)
    m = np.tanh((revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0) * 5.0)
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recogpace_21d_slope_v136_signal(deferredrev, revenue, ncfo):
    rg = np.log(revenue.replace(0,np.nan)/revenue.shift(63).replace(0,np.nan))
    dg = np.log(deferredrev.replace(0,np.nan)/deferredrev.shift(63).replace(0,np.nan))
    base = rg - dg
    d = _d1(base, 21, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = d - d.shift(21) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recogpace_42d_slope_v137_signal(deferredrev, revenue, ncfo):
    rg = np.log(revenue.replace(0,np.nan)/revenue.shift(126).replace(0,np.nan))
    dg = np.log(deferredrev.replace(0,np.nan)/deferredrev.shift(126).replace(0,np.nan))
    base = rg - dg
    d = _d1(base, 42, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recogpace_63d_slope_v138_signal(deferredrev, revenue, ncfo):
    rg = np.log(revenue.replace(0,np.nan)/revenue.shift(126).replace(0,np.nan))
    dg = np.log(deferredrev.replace(0,np.nan)/deferredrev.shift(126).replace(0,np.nan))
    base = rg - dg
    d = _d1(base, 63, 126)
    m = (ncfo > 0).astype(float).rolling(126, min_periods=max(5,126//3)).mean() - 0.5
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recogpace_84d_slope_v139_signal(deferredrev, revenue, ncfo):
    rg = np.log(revenue.replace(0,np.nan)/revenue.shift(252).replace(0,np.nan))
    dg = np.log(deferredrev.replace(0,np.nan)/deferredrev.shift(252).replace(0,np.nan))
    base = rg - dg
    d = _d1(base, 84, 252)
    m = (ncfo > 0).astype(float).rolling(252, min_periods=max(5,252//3)).mean() - 0.5
    r = (d + 0.6*m).rolling(252, min_periods=84).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recogpace_126d_slope_v140_signal(deferredrev, revenue, ncfo):
    rg = np.log(revenue.replace(0,np.nan)/revenue.shift(504).replace(0,np.nan))
    dg = np.log(deferredrev.replace(0,np.nan)/deferredrev.shift(504).replace(0,np.nan))
    base = rg - dg
    d = _d1(base, 126, 252)
    m = (ncfo > 0).astype(float).rolling(252, min_periods=max(5,252//3)).mean() - 0.5
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billgap_21d_slope_v141_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 63)
    base = bill / revenue.replace(0, np.nan) - 1.0
    d = _d1(base, 21, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billgap_42d_slope_v142_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / revenue.replace(0, np.nan) - 1.0
    d = _d1(base, 42, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billgap_63d_slope_v143_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 126)
    base = bill / revenue.replace(0, np.nan) - 1.0
    d = _d1(base, 63, 126)
    m = np.tanh(_z(receivables.pct_change(63), 126))
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billgap_84d_slope_v144_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 252)
    base = bill / revenue.replace(0, np.nan) - 1.0
    d = _d1(base, 84, 252)
    m = np.tanh(_z(receivables.pct_change(63), 252))
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_billgap_126d_slope_v145_signal(deferredrev, revenue, receivables):
    bill = _billings(deferredrev, revenue, 504)
    base = bill / revenue.replace(0, np.nan) - 1.0
    d = _d1(base, 126, 252)
    m = np.tanh(_z(receivables.pct_change(63), 252))
    r = d - d.shift(126) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recvshare_21d_slope_v146_signal(deferredrev, receivables):
    sh = receivables / (deferredrev + receivables).replace(0, np.nan)
    base = _z(sh, 63)
    d = _d1(base, 21, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = d * (0.5 + m)
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recvshare_42d_slope_v147_signal(deferredrev, receivables):
    sh = receivables / (deferredrev + receivables).replace(0, np.nan)
    base = _z(sh, 126)
    d = _d1(base, 42, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = (d + 0.6*m).rolling(126, min_periods=42).rank(pct=True) - 0.5
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recvshare_63d_slope_v148_signal(deferredrev, receivables):
    sh = receivables / (deferredrev + receivables).replace(0, np.nan)
    base = _z(sh, 126)
    d = _d1(base, 63, 126)
    m = (deferredrev.rolling(126, min_periods=max(5,126//3)).rank(pct=True) - 0.5) * 2.0
    r = np.tanh(d) * np.sign(m) + 0.3*m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recvshare_84d_slope_v149_signal(deferredrev, receivables):
    sh = receivables / (deferredrev + receivables).replace(0, np.nan)
    base = _z(sh, 252)
    d = _d1(base, 84, 252)
    m = (deferredrev.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d - d.shift(84) + m
    return r.replace([np.inf, -np.inf], np.nan)

def f19db_f19_deferred_revenue_bookings_recvshare_126d_slope_v150_signal(deferredrev, receivables):
    sh = receivables / (deferredrev + receivables).replace(0, np.nan)
    base = _z(sh, 504)
    d = _d1(base, 126, 252)
    m = (deferredrev.rolling(252, min_periods=max(5,252//3)).rank(pct=True) - 0.5) * 2.0
    r = d * np.exp(m.clip(-1.0, 1.0)) - m
    return r.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f19db_f19_deferred_revenue_bookings_covernorm_21d_slope_v001_signal,
    f19db_f19_deferred_revenue_bookings_covernorm_42d_slope_v002_signal,
    f19db_f19_deferred_revenue_bookings_covernorm_63d_slope_v003_signal,
    f19db_f19_deferred_revenue_bookings_covernorm_84d_slope_v004_signal,
    f19db_f19_deferred_revenue_bookings_covernorm_126d_slope_v005_signal,
    f19db_f19_deferred_revenue_bookings_coverema_21d_slope_v006_signal,
    f19db_f19_deferred_revenue_bookings_coverema_42d_slope_v007_signal,
    f19db_f19_deferred_revenue_bookings_coverema_63d_slope_v008_signal,
    f19db_f19_deferred_revenue_bookings_coverema_84d_slope_v009_signal,
    f19db_f19_deferred_revenue_bookings_coverema_126d_slope_v010_signal,
    f19db_f19_deferred_revenue_bookings_coverpos_21d_slope_v011_signal,
    f19db_f19_deferred_revenue_bookings_coverpos_42d_slope_v012_signal,
    f19db_f19_deferred_revenue_bookings_coverpos_63d_slope_v013_signal,
    f19db_f19_deferred_revenue_bookings_coverpos_84d_slope_v014_signal,
    f19db_f19_deferred_revenue_bookings_coverpos_126d_slope_v015_signal,
    f19db_f19_deferred_revenue_bookings_coverz_21d_slope_v016_signal,
    f19db_f19_deferred_revenue_bookings_coverz_42d_slope_v017_signal,
    f19db_f19_deferred_revenue_bookings_coverz_63d_slope_v018_signal,
    f19db_f19_deferred_revenue_bookings_coverz_84d_slope_v019_signal,
    f19db_f19_deferred_revenue_bookings_coverz_126d_slope_v020_signal,
    f19db_f19_deferred_revenue_bookings_coverrk_21d_slope_v021_signal,
    f19db_f19_deferred_revenue_bookings_coverrk_42d_slope_v022_signal,
    f19db_f19_deferred_revenue_bookings_coverrk_63d_slope_v023_signal,
    f19db_f19_deferred_revenue_bookings_coverrk_84d_slope_v024_signal,
    f19db_f19_deferred_revenue_bookings_coverrk_126d_slope_v025_signal,
    f19db_f19_deferred_revenue_bookings_drevg_21d_slope_v026_signal,
    f19db_f19_deferred_revenue_bookings_drevg_42d_slope_v027_signal,
    f19db_f19_deferred_revenue_bookings_drevg_63d_slope_v028_signal,
    f19db_f19_deferred_revenue_bookings_drevg_84d_slope_v029_signal,
    f19db_f19_deferred_revenue_bookings_drevg_126d_slope_v030_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvnorm_21d_slope_v031_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvnorm_42d_slope_v032_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvnorm_63d_slope_v033_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvnorm_84d_slope_v034_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvnorm_126d_slope_v035_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvz_21d_slope_v036_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvz_42d_slope_v037_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvz_63d_slope_v038_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvz_84d_slope_v039_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvz_126d_slope_v040_signal,
    f19db_f19_deferred_revenue_bookings_drevcashema_21d_slope_v041_signal,
    f19db_f19_deferred_revenue_bookings_drevcashema_42d_slope_v042_signal,
    f19db_f19_deferred_revenue_bookings_drevcashema_63d_slope_v043_signal,
    f19db_f19_deferred_revenue_bookings_drevcashema_84d_slope_v044_signal,
    f19db_f19_deferred_revenue_bookings_drevcashema_126d_slope_v045_signal,
    f19db_f19_deferred_revenue_bookings_bookturnnorm_21d_slope_v046_signal,
    f19db_f19_deferred_revenue_bookings_bookturnnorm_42d_slope_v047_signal,
    f19db_f19_deferred_revenue_bookings_bookturnnorm_63d_slope_v048_signal,
    f19db_f19_deferred_revenue_bookings_bookturnnorm_84d_slope_v049_signal,
    f19db_f19_deferred_revenue_bookings_bookturnnorm_126d_slope_v050_signal,
    f19db_f19_deferred_revenue_bookings_ncforecv_21d_slope_v051_signal,
    f19db_f19_deferred_revenue_bookings_ncforecv_42d_slope_v052_signal,
    f19db_f19_deferred_revenue_bookings_ncforecv_63d_slope_v053_signal,
    f19db_f19_deferred_revenue_bookings_ncforecv_84d_slope_v054_signal,
    f19db_f19_deferred_revenue_bookings_ncforecv_126d_slope_v055_signal,
    f19db_f19_deferred_revenue_bookings_booksharepos_21d_slope_v056_signal,
    f19db_f19_deferred_revenue_bookings_booksharepos_42d_slope_v057_signal,
    f19db_f19_deferred_revenue_bookings_booksharepos_63d_slope_v058_signal,
    f19db_f19_deferred_revenue_bookings_booksharepos_84d_slope_v059_signal,
    f19db_f19_deferred_revenue_bookings_booksharepos_126d_slope_v060_signal,
    f19db_f19_deferred_revenue_bookings_logdrevext_21d_slope_v061_signal,
    f19db_f19_deferred_revenue_bookings_logdrevext_42d_slope_v062_signal,
    f19db_f19_deferred_revenue_bookings_logdrevext_63d_slope_v063_signal,
    f19db_f19_deferred_revenue_bookings_logdrevext_84d_slope_v064_signal,
    f19db_f19_deferred_revenue_bookings_logdrevext_126d_slope_v065_signal,
    f19db_f19_deferred_revenue_bookings_billratio_21d_slope_v066_signal,
    f19db_f19_deferred_revenue_bookings_billratio_42d_slope_v067_signal,
    f19db_f19_deferred_revenue_bookings_billratio_63d_slope_v068_signal,
    f19db_f19_deferred_revenue_bookings_billratio_84d_slope_v069_signal,
    f19db_f19_deferred_revenue_bookings_billratio_126d_slope_v070_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_21d_slope_v071_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_42d_slope_v072_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_63d_slope_v073_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_84d_slope_v074_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_126d_slope_v075_signal,
    f19db_f19_deferred_revenue_bookings_revcash_21d_slope_v076_signal,
    f19db_f19_deferred_revenue_bookings_revcash_42d_slope_v077_signal,
    f19db_f19_deferred_revenue_bookings_revcash_63d_slope_v078_signal,
    f19db_f19_deferred_revenue_bookings_revcash_84d_slope_v079_signal,
    f19db_f19_deferred_revenue_bookings_revcash_126d_slope_v080_signal,
    f19db_f19_deferred_revenue_bookings_cashmgnema_21d_slope_v081_signal,
    f19db_f19_deferred_revenue_bookings_cashmgnema_42d_slope_v082_signal,
    f19db_f19_deferred_revenue_bookings_cashmgnema_63d_slope_v083_signal,
    f19db_f19_deferred_revenue_bookings_cashmgnema_84d_slope_v084_signal,
    f19db_f19_deferred_revenue_bookings_cashmgnema_126d_slope_v085_signal,
    f19db_f19_deferred_revenue_bookings_cashconvnorm_21d_slope_v086_signal,
    f19db_f19_deferred_revenue_bookings_cashconvnorm_42d_slope_v087_signal,
    f19db_f19_deferred_revenue_bookings_cashconvnorm_63d_slope_v088_signal,
    f19db_f19_deferred_revenue_bookings_cashconvnorm_84d_slope_v089_signal,
    f19db_f19_deferred_revenue_bookings_cashconvnorm_126d_slope_v090_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_21d_slope_v091_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_42d_slope_v092_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_63d_slope_v093_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_84d_slope_v094_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_126d_slope_v095_signal,
    f19db_f19_deferred_revenue_bookings_dsoz_21d_slope_v096_signal,
    f19db_f19_deferred_revenue_bookings_dsoz_42d_slope_v097_signal,
    f19db_f19_deferred_revenue_bookings_dsoz_63d_slope_v098_signal,
    f19db_f19_deferred_revenue_bookings_dsoz_84d_slope_v099_signal,
    f19db_f19_deferred_revenue_bookings_dsoz_126d_slope_v100_signal,
    f19db_f19_deferred_revenue_bookings_covermean_21d_slope_v101_signal,
    f19db_f19_deferred_revenue_bookings_covermean_42d_slope_v102_signal,
    f19db_f19_deferred_revenue_bookings_covermean_63d_slope_v103_signal,
    f19db_f19_deferred_revenue_bookings_covermean_84d_slope_v104_signal,
    f19db_f19_deferred_revenue_bookings_covermean_126d_slope_v105_signal,
    f19db_f19_deferred_revenue_bookings_pipeg_21d_slope_v106_signal,
    f19db_f19_deferred_revenue_bookings_pipeg_42d_slope_v107_signal,
    f19db_f19_deferred_revenue_bookings_pipeg_63d_slope_v108_signal,
    f19db_f19_deferred_revenue_bookings_pipeg_84d_slope_v109_signal,
    f19db_f19_deferred_revenue_bookings_pipeg_126d_slope_v110_signal,
    f19db_f19_deferred_revenue_bookings_visibdisp_21d_slope_v111_signal,
    f19db_f19_deferred_revenue_bookings_visibdisp_42d_slope_v112_signal,
    f19db_f19_deferred_revenue_bookings_visibdisp_63d_slope_v113_signal,
    f19db_f19_deferred_revenue_bookings_visibdisp_84d_slope_v114_signal,
    f19db_f19_deferred_revenue_bookings_visibdisp_126d_slope_v115_signal,
    f19db_f19_deferred_revenue_bookings_ncfog_21d_slope_v116_signal,
    f19db_f19_deferred_revenue_bookings_ncfog_42d_slope_v117_signal,
    f19db_f19_deferred_revenue_bookings_ncfog_63d_slope_v118_signal,
    f19db_f19_deferred_revenue_bookings_ncfog_84d_slope_v119_signal,
    f19db_f19_deferred_revenue_bookings_ncfog_126d_slope_v120_signal,
    f19db_f19_deferred_revenue_bookings_logspreadext_21d_slope_v121_signal,
    f19db_f19_deferred_revenue_bookings_logspreadext_42d_slope_v122_signal,
    f19db_f19_deferred_revenue_bookings_logspreadext_63d_slope_v123_signal,
    f19db_f19_deferred_revenue_bookings_logspreadext_84d_slope_v124_signal,
    f19db_f19_deferred_revenue_bookings_logspreadext_126d_slope_v125_signal,
    f19db_f19_deferred_revenue_bookings_coverdso_21d_slope_v126_signal,
    f19db_f19_deferred_revenue_bookings_coverdso_42d_slope_v127_signal,
    f19db_f19_deferred_revenue_bookings_coverdso_63d_slope_v128_signal,
    f19db_f19_deferred_revenue_bookings_coverdso_84d_slope_v129_signal,
    f19db_f19_deferred_revenue_bookings_coverdso_126d_slope_v130_signal,
    f19db_f19_deferred_revenue_bookings_cashsharenorm_21d_slope_v131_signal,
    f19db_f19_deferred_revenue_bookings_cashsharenorm_42d_slope_v132_signal,
    f19db_f19_deferred_revenue_bookings_cashsharenorm_63d_slope_v133_signal,
    f19db_f19_deferred_revenue_bookings_cashsharenorm_84d_slope_v134_signal,
    f19db_f19_deferred_revenue_bookings_cashsharenorm_126d_slope_v135_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_21d_slope_v136_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_42d_slope_v137_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_63d_slope_v138_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_84d_slope_v139_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_126d_slope_v140_signal,
    f19db_f19_deferred_revenue_bookings_billgap_21d_slope_v141_signal,
    f19db_f19_deferred_revenue_bookings_billgap_42d_slope_v142_signal,
    f19db_f19_deferred_revenue_bookings_billgap_63d_slope_v143_signal,
    f19db_f19_deferred_revenue_bookings_billgap_84d_slope_v144_signal,
    f19db_f19_deferred_revenue_bookings_billgap_126d_slope_v145_signal,
    f19db_f19_deferred_revenue_bookings_recvshare_21d_slope_v146_signal,
    f19db_f19_deferred_revenue_bookings_recvshare_42d_slope_v147_signal,
    f19db_f19_deferred_revenue_bookings_recvshare_63d_slope_v148_signal,
    f19db_f19_deferred_revenue_bookings_recvshare_84d_slope_v149_signal,
    f19db_f19_deferred_revenue_bookings_recvshare_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DEFERRED_REVENUE_BOOKINGS_REGISTRY_001_150 = REGISTRY


ALLOW = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
    "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
    "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
    "investments", "inventory", "receivables", "payables", "equity", "retearn",
    "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
    "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
    "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
    "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb",
    "ps", "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders", "putvalue",
    "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}
# this family consumes only these fundamental columns
FUNDAMENTAL = {"deferredrev", "revenue", "receivables", "ncfo"}

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    deferredrev = _fund(101, base=8e7, drift=0.035, vol=0.08).rename("deferredrev")
    revenue = _fund(102, base=2e8, drift=0.030, vol=0.06).rename("revenue")
    receivables = _fund(103, base=5e7, drift=0.028, vol=0.07).rename("receivables")
    ncfo = _fund(104, base=4e7, drift=0.025, vol=0.10, allow_neg=True).rename("ncfo")

    cols = {
        "deferredrev": deferredrev, "revenue": revenue,
        "receivables": receivables, "ncfo": ncfo,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "ALLOWLIST %s: %s" % (name, meta["inputs"])
        assert any(c in FUNDAMENTAL for c in meta["inputs"]), "NO FUND %s" % name
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

    print("OK f19_deferred_revenue_bookings_2nd_derivatives_001_150_claude: %d features pass" % n_features)
