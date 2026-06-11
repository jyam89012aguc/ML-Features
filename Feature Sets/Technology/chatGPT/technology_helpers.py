import numpy as np
import pandas as pd


def _to_num(s):
    if isinstance(s, pd.Series):
        return pd.to_numeric(s, errors="coerce").astype(float)
    return pd.Series(s, dtype=float)


def _clean(s):
    if not isinstance(s, pd.Series):
        s = pd.Series(s)
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(num, den):
    num = _to_num(num)
    den = _to_num(den) if isinstance(den, pd.Series) else den
    if isinstance(den, pd.Series):
        den = den.replace(0, np.nan)
    elif den == 0:
        den = np.nan
    return _clean(num / den)


def _log(s):
    s = _to_num(s)
    return np.log(s.where(s > 0, np.nan))


def _mean(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).mean()


def _std(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).std()


def _sum(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).sum()


def _min(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).min()


def _max(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).max()


def _z(s, n):
    s = _to_num(s)
    return _safe_div(s - _mean(s, n), _std(s, n))


def _pct_change(s, n):
    return _to_num(s).pct_change(n).replace([np.inf, -np.inf], np.nan)


def _diff(s, n):
    return _to_num(s).diff(n)


def _rank(s, n):
    return _to_num(s).rolling(n, min_periods=max(2, n // 3)).rank(pct=True)


def _skew(s, n):
    return _to_num(s).rolling(n, min_periods=max(3, n // 3)).skew()


def _kurt(s, n):
    return _to_num(s).rolling(n, min_periods=max(4, n // 3)).kurt()


def _autocorr(s, n, lag=1):
    s = _to_num(s)
    return s.rolling(n, min_periods=max(4, n // 3)).corr(s.shift(lag))


def _corr(a, b, n):
    return _to_num(a).rolling(n, min_periods=max(4, n // 3)).corr(_to_num(b))


def _slope(s, n):
    s = _to_num(s)
    def f(w):
        valid = np.isfinite(w)
        if valid.sum() < max(2, n // 3):
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        xv = x - x.mean()
        den = float((xv * xv).sum())
        if den == 0:
            return np.nan
        return float((xv * (y - y.mean())).sum() / den)
    return s.rolling(n, min_periods=max(2, n // 3)).apply(f, raw=True)


def _ewm(s, span):
    return _to_num(s).ewm(span=span, adjust=False, min_periods=max(2, span // 3)).mean()


def _event_flag(s):
    if isinstance(s, pd.Series):
        if pd.api.types.is_numeric_dtype(s):
            return pd.to_numeric(s, errors="coerce").fillna(0).ne(0).astype(float)
        txt = s.astype("string")
        return txt.notna().astype(float)
    return pd.Series(s).notna().astype(float)


def _event_count(s, n):
    return _event_flag(s).rolling(n, min_periods=1).sum()


def _event_rate(s, n):
    return _event_flag(s).rolling(n, min_periods=1).mean()


def _clip_z(s, n, lo=-5.0, hi=5.0):
    return _z(s, n).clip(lo, hi)
