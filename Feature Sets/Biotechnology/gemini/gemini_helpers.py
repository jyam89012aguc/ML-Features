import numpy as np


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _z(s, w):
    mean = _mean(s, w)
    std = _std(s, w)
    return (s - mean) / std.replace(0, np.nan)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / w


def _log(s):
    return np.log(s.abs().replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w).rank(pct=True)


def _skew(s, w):
    return s.rolling(w).skew()


def _kurt(s, w):
    return s.rolling(w).kurt()


def _autocorr(s, w, l=1):
    return s.rolling(w).apply(lambda x: x.autocorr(lag=l) if len(x) > l else np.nan)
