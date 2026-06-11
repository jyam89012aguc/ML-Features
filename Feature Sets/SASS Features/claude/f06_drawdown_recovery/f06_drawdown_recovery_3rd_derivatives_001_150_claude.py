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


def _drawdown(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _logdd(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / peak.replace(0, np.nan))


def _maxdd(close, w):
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        return float(dd.min())
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _recovery(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _underwater(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close < peak * 0.99999).astype(float)


def _uwfrac(close, w, dw):
    # exponentially-smoothed underwater indicator (continuous time-below-water proxy)
    uw = _underwater(close, w)
    return uw.ewm(span=dw, min_periods=max(1, dw // 3)).mean()


def _pain(close, w):
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return dd.rolling(w, min_periods=max(1, w // 2)).mean()


def _ulcer(close, w):
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return np.sqrt((dd * dd).rolling(w, min_periods=max(1, w // 2)).mean())


def _downvol(close, w):
    r = close.pct_change()
    dn = r.clip(upper=0.0)
    return np.sqrt((dn * dn).rolling(w, min_periods=max(1, w // 2)).mean())


def _recovshare(close, w):
    peak = _rmax(close, w)
    trough = _rmin(close, w)
    return (close - trough) / (peak - trough).replace(0, np.nan)


def _calmar(close, w):
    ret = close / close.shift(w) - 1.0
    mdd = _maxdd(close, w).abs()
    return ret / mdd.replace(0, np.nan)


def _painratio(close, w):
    ret = close / close.shift(w) - 1.0
    p = _pain(close, w).abs()
    return ret / p.replace(0, np.nan)


def _gainpain(close, w):
    r = close.pct_change()
    pos = r.clip(lower=0.0).rolling(w, min_periods=max(1, w // 2)).sum()
    neg = (-r.clip(upper=0.0)).rolling(w, min_periods=max(1, w // 2)).sum()
    return pos / neg.replace(0, np.nan)


def _vbalance(close, w):
    rec = _recovery(close, w)
    dd = _drawdown(close, w).abs()
    return (rec - dd) / (rec + dd).replace(0, np.nan)


def _ddvolratio(close, w):
    dd = _drawdown(close, w)
    vol = close.pct_change().rolling(63, min_periods=21).std()
    return dd / vol.replace(0, np.nan)


def _ulcervol(close, w):
    u = _ulcer(close, w)
    vol = close.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    return u / vol.replace(0, np.nan)


def _dvshare(close, w):
    r = close.pct_change()
    dn = r.clip(upper=0.0)
    dvar = (dn * dn).rolling(w, min_periods=max(1, w // 2)).mean()
    tvar = (r * r).rolling(w, min_periods=max(1, w // 2)).mean()
    return dvar / tvar.replace(0, np.nan)


def _ddfromworst(close, w):
    cur = _drawdown(close, w)
    worst = _maxdd(close, w)
    return cur / worst.replace(0, np.nan)


def _painz(close, w):
    return _z(_pain(close, w), w)


def _maxddz(close, w):
    return _z(_maxdd(close, w), w)


def _ewpain(close, w, span):
    dd = _drawdown(close, w)
    return dd.ewm(span=span, min_periods=max(1, span // 3)).mean()


def _ddarea(close, w, dw):
    dd = _drawdown(close, w)
    return dd.rolling(dw, min_periods=max(1, dw // 2)).sum()


def _amplitude(close, w):
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    return (hi - lo) / close.replace(0, np.nan)


def _runup(close, w):
    # log run-up above the trailing trough, net of the log drawdown from the peak
    # (net round-trip position within the window; distinct from plain recovery)
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    up = np.log(close.replace(0, np.nan) / trough.replace(0, np.nan))
    dn = np.log(peak.replace(0, np.nan) / close.replace(0, np.nan))
    return up - dn


def _sortino(close, w):
    ret = close / close.shift(w) - 1.0
    dn = _downvol(close, w)
    return ret / dn.replace(0, np.nan)


def _updownvol(close, w):
    r = close.pct_change()
    dn = np.sqrt((r.clip(upper=0.0) ** 2).rolling(w, min_periods=max(1, w // 2)).mean())
    up = np.sqrt((r.clip(lower=0.0) ** 2).rolling(w, min_periods=max(1, w // 2)).mean())
    return dn / up.replace(0, np.nan)


def _stress(close, w):
    # standardized chronic-stress blend
    p = _z(_pain(close, w), w)
    u = _z(_ulcer(close, w), w)
    return (p - u) / 2.0


def _ddrange(close, w, sw):
    dd = _drawdown(close, w)
    return dd.rolling(sw, min_periods=max(1, sw // 2)).max() - dd.rolling(sw, min_periods=max(1, sw // 2)).min()


def _deepening(close, w, sw):
    # signed deepening pressure: EMA of (dd change), continuous
    dd = _drawdown(close, w)
    return dd.diff().ewm(span=sw, min_periods=max(1, sw // 3)).mean()


def _healeff(close, w):
    peak = _rmax(close, w)
    trough = _rmin(close, w)
    healed = (close - trough) / (peak - trough).replace(0, np.nan)
    pain = _pain(close, w).abs()
    return healed / (pain + 0.05)


def _recovol(close, w):
    rec = _recovery(close, w)
    vol = close.pct_change().rolling(63, min_periods=21).std()
    return rec / vol.replace(0, np.nan)


def _ddskew(close, w):
    dd = _drawdown(close, w)
    return dd.rolling(w, min_periods=max(1, w // 2)).skew()


def _newhi(close, w, dw):
    peak = _rmax(close, w)
    fresh = (close >= peak * 0.99999).astype(float)
    return fresh.rolling(dw, min_periods=max(1, dw // 2)).mean()


def _ddmean_disp(close):
    d1 = _drawdown(close, 63)
    d2 = _drawdown(close, 126)
    d3 = _drawdown(close, 252)
    return pd.concat([d1, d2, d3], axis=1).std(axis=1)


def _avgepdd(close, w):
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        troughs = []
        cur = 0.0
        inep = False
        for x in dd:
            if x < -1e-9:
                inep = True
                if x < cur:
                    cur = x
            else:
                if inep:
                    troughs.append(cur)
                    cur = 0.0
                    inep = False
        if inep:
            troughs.append(cur)
        if len(troughs) == 0:
            return 0.0
        return float(np.mean(troughs))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _es(close, w, q):
    r = close.pct_change()

    def _f(a):
        thr = np.quantile(a, q)
        tail = a[a <= thr]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    return r.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _ddacf(close, w, sw):
    dd = _drawdown(close, w)

    def _f(a):
        x = a[:-1]
        y = a[1:]
        if np.std(x) < 1e-12 or np.std(y) < 1e-12:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return dd.rolling(sw, min_periods=max(1, sw // 2)).apply(_f, raw=True)


def _ddtrend(close, w, sw):
    dd = _drawdown(close, w)

    def _f(a):
        x = np.arange(len(a), dtype=float)
        x = x - x.mean()
        d = (x * x).sum()
        if d == 0:
            return np.nan
        return float((x * (a - a.mean())).sum() / d)
    return dd.rolling(sw, min_periods=max(1, sw // 2)).apply(_f, raw=True)


def _legbal(close, w):
    r = close.pct_change()
    up = (r > 0).astype(float)

    def _f(a):
        runs_up = []
        runs_dn = []
        cur = 0
        sign = 0
        for v in a:
            s = 1 if v > 0.5 else -1
            if s == sign:
                cur += 1
            else:
                if sign == 1:
                    runs_up.append(cur)
                elif sign == -1:
                    runs_dn.append(cur)
                sign = s
                cur = 1
        if sign == 1:
            runs_up.append(cur)
        elif sign == -1:
            runs_dn.append(cur)
        mu = np.mean(runs_up) if runs_up else 0.0
        md = np.mean(runs_dn) if runs_dn else 0.0
        if (mu + md) == 0:
            return np.nan
        return float((mu - md) / (mu + md))
    return up.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _lossconc(close, w):
    r = close.pct_change()
    worst5 = r.rolling(5, min_periods=3).sum().rolling(w, min_periods=max(1, w // 2)).min()
    totloss = r.clip(upper=0.0).rolling(w, min_periods=max(1, w // 2)).sum()
    return worst5 / totloss.replace(0, np.nan)


def _painterm(close):
    ps = _pain(close, 126)
    pl = _pain(close, 504)
    return ps / pl.replace(0, np.nan)


def _cdar(close, w, q):
    dd = _drawdown(close, w)

    def _f(a):
        thr = np.quantile(a, q)
        tail = a[a <= thr]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    return dd.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _cdarrat(close, w):
    dd = _drawdown(close, w)

    def _f(a):
        t = np.quantile(a, 0.05)
        b = np.quantile(a, 0.25)
        tail = a[a <= t]
        body = a[a <= b]
        if tail.size == 0 or body.size == 0:
            return np.nan
        bm = body.mean()
        if bm == 0:
            return np.nan
        return float(tail.mean() / bm)
    return dd.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _tailrat(close, w):
    r = close.pct_change()

    def _f(a):
        thr = np.quantile(a, 0.05)
        tail = a[a <= thr]
        neg = a[a < 0]
        if tail.size == 0 or neg.size == 0:
            return np.nan
        med = np.median(neg)
        if med == 0:
            return np.nan
        return float(tail.mean() / med)
    return r.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)

def f06dr_f06_drawdown_recovery_curdd_63d_jerk_v001_signal(closeadj):
    base = _drawdown(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_63d_jerk_v002_signal(closeadj):
    base = _drawdown(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_126d_jerk_v003_signal(closeadj):
    base = _drawdown(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_126d_jerk_v004_signal(closeadj):
    base = _drawdown(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_252d_jerk_v005_signal(closeadj):
    base = _drawdown(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_252d_jerk_v006_signal(closeadj):
    base = _drawdown(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_504d_jerk_v007_signal(closeadj):
    base = _drawdown(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_504d_jerk_v008_signal(closeadj):
    base = _drawdown(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_63d_jerk_v009_signal(closeadj):
    base = _maxdd(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_63d_jerk_v010_signal(closeadj):
    base = _maxdd(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_126d_jerk_v011_signal(closeadj):
    base = _maxdd(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_126d_jerk_v012_signal(closeadj):
    base = _maxdd(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_252d_jerk_v013_signal(closeadj):
    base = _maxdd(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_252d_jerk_v014_signal(closeadj):
    base = _maxdd(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_504d_jerk_v015_signal(closeadj):
    base = _maxdd(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_504d_jerk_v016_signal(closeadj):
    base = _maxdd(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_63d_jerk_v017_signal(closeadj):
    base = _recovery(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_63d_jerk_v018_signal(closeadj):
    base = _recovery(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_126d_jerk_v019_signal(closeadj):
    base = _recovery(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_126d_jerk_v020_signal(closeadj):
    base = _recovery(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_252d_jerk_v021_signal(closeadj):
    base = _recovery(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_252d_jerk_v022_signal(closeadj):
    base = _recovery(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_504d_jerk_v023_signal(closeadj):
    base = _recovery(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_504d_jerk_v024_signal(closeadj):
    base = _recovery(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_126d_jerk_v025_signal(closeadj):
    base = _uwfrac(closeadj, 126, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_126d_jerk_v026_signal(closeadj):
    base = _uwfrac(closeadj, 126, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_504d_jerk_v027_signal(closeadj):
    base = _uwfrac(closeadj, 504, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_504d_jerk_v028_signal(closeadj):
    base = _uwfrac(closeadj, 504, 252)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup504_504d_jerk_v029_signal(closeadj):
    base = _runup(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup504_504d_jerk_v030_signal(closeadj):
    base = _runup(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdar_252d_jerk_v031_signal(closeadj):
    base = _cdar(closeadj, 252, 0.10)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdar_252d_jerk_v032_signal(closeadj):
    base = _cdar(closeadj, 252, 0.10)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_63d_jerk_v033_signal(closeadj):
    base = _pain(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_63d_jerk_v034_signal(closeadj):
    base = _pain(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_126d_jerk_v035_signal(closeadj):
    base = _pain(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_126d_jerk_v036_signal(closeadj):
    base = _pain(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_252d_jerk_v037_signal(closeadj):
    base = _pain(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_252d_jerk_v038_signal(closeadj):
    base = _pain(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_504d_jerk_v039_signal(closeadj):
    base = _pain(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_504d_jerk_v040_signal(closeadj):
    base = _pain(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_63d_jerk_v041_signal(closeadj):
    base = _recovshare(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_63d_jerk_v042_signal(closeadj):
    base = _recovshare(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_126d_jerk_v043_signal(closeadj):
    base = _recovshare(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_126d_jerk_v044_signal(closeadj):
    base = _recovshare(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_252d_jerk_v045_signal(closeadj):
    base = _recovshare(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_252d_jerk_v046_signal(closeadj):
    base = _recovshare(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_504d_jerk_v047_signal(closeadj):
    base = _recovshare(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovshr_504d_jerk_v048_signal(closeadj):
    base = _recovshare(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_126d_jerk_v049_signal(closeadj):
    base = _calmar(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_126d_jerk_v050_signal(closeadj):
    base = _calmar(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_252d_jerk_v051_signal(closeadj):
    base = _calmar(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_252d_jerk_v052_signal(closeadj):
    base = _calmar(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_504d_jerk_v053_signal(closeadj):
    base = _calmar(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_504d_jerk_v054_signal(closeadj):
    base = _calmar(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painrat_126d_jerk_v055_signal(closeadj):
    base = _painratio(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painrat_126d_jerk_v056_signal(closeadj):
    base = _painratio(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painrat_252d_jerk_v057_signal(closeadj):
    base = _painratio(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painrat_252d_jerk_v058_signal(closeadj):
    base = _painratio(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_63d_jerk_v059_signal(closeadj):
    base = _gainpain(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_63d_jerk_v060_signal(closeadj):
    base = _gainpain(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_126d_jerk_v061_signal(closeadj):
    base = _gainpain(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_126d_jerk_v062_signal(closeadj):
    base = _gainpain(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_252d_jerk_v063_signal(closeadj):
    base = _gainpain(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_gainpain_252d_jerk_v064_signal(closeadj):
    base = _gainpain(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dvshare_126d_jerk_v065_signal(closeadj):
    base = _dvshare(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dvshare_126d_jerk_v066_signal(closeadj):
    base = _dvshare(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dvshare_252d_jerk_v067_signal(closeadj):
    base = _dvshare(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dvshare_252d_jerk_v068_signal(closeadj):
    base = _dvshare(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_avgepdd_252d_jerk_v069_signal(closeadj):
    base = _avgepdd(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_avgepdd_252d_jerk_v070_signal(closeadj):
    base = _avgepdd(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_avgepdd_504d_jerk_v071_signal(closeadj):
    base = _avgepdd(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_avgepdd_504d_jerk_v072_signal(closeadj):
    base = _avgepdd(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfworst_126d_jerk_v073_signal(closeadj):
    base = _ddfromworst(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfworst_126d_jerk_v074_signal(closeadj):
    base = _ddfromworst(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfworst_252d_jerk_v075_signal(closeadj):
    base = _ddfromworst(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfworst_252d_jerk_v076_signal(closeadj):
    base = _ddfromworst(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painz_252d_jerk_v077_signal(closeadj):
    base = _painz(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painz_252d_jerk_v078_signal(closeadj):
    base = _painz(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxddz_252d_jerk_v079_signal(closeadj):
    base = _maxddz(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxddz_252d_jerk_v080_signal(closeadj):
    base = _maxddz(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ewpain_252d_jerk_v081_signal(closeadj):
    base = _ewpain(closeadj, 252, 42)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ewpain_252d_jerk_v082_signal(closeadj):
    base = _ewpain(closeadj, 252, 42)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ewpain_504d_jerk_v083_signal(closeadj):
    base = _ewpain(closeadj, 504, 84)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ewpain_504d_jerk_v084_signal(closeadj):
    base = _ewpain(closeadj, 504, 84)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddarea_252d_jerk_v085_signal(closeadj):
    base = _ddarea(closeadj, 252, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddarea_252d_jerk_v086_signal(closeadj):
    base = _ddarea(closeadj, 252, 126)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddarea_504d_jerk_v087_signal(closeadj):
    base = _ddarea(closeadj, 504, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddarea_504d_jerk_v088_signal(closeadj):
    base = _ddarea(closeadj, 504, 252)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_126d_jerk_v089_signal(closeadj):
    base = _amplitude(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_126d_jerk_v090_signal(closeadj):
    base = _amplitude(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_252d_jerk_v091_signal(closeadj):
    base = _amplitude(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_252d_jerk_v092_signal(closeadj):
    base = _amplitude(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_504d_jerk_v093_signal(closeadj):
    base = _amplitude(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_amp_504d_jerk_v094_signal(closeadj):
    base = _amplitude(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_63d_jerk_v095_signal(closeadj):
    base = _runup(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_63d_jerk_v096_signal(closeadj):
    base = _runup(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_126d_jerk_v097_signal(closeadj):
    base = _runup(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_126d_jerk_v098_signal(closeadj):
    base = _runup(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_252d_jerk_v099_signal(closeadj):
    base = _runup(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_runup_252d_jerk_v100_signal(closeadj):
    base = _runup(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_63d_jerk_v101_signal(closeadj):
    base = _downvol(closeadj, 63)
    slope = base.diff(5) / float(5)
    d = slope.diff(5) / float(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_63d_jerk_v102_signal(closeadj):
    base = _downvol(closeadj, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_126d_jerk_v103_signal(closeadj):
    base = _downvol(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_126d_jerk_v104_signal(closeadj):
    base = _downvol(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_252d_jerk_v105_signal(closeadj):
    base = _downvol(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_252d_jerk_v106_signal(closeadj):
    base = _downvol(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ulcervol_126d_jerk_v107_signal(closeadj):
    base = _ulcervol(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ulcervol_126d_jerk_v108_signal(closeadj):
    base = _ulcervol(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ulcervol_252d_jerk_v109_signal(closeadj):
    base = _ulcervol(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ulcervol_252d_jerk_v110_signal(closeadj):
    base = _ulcervol(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_es95_252d_jerk_v111_signal(closeadj):
    base = _es(closeadj, 252, 0.05)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_es95_252d_jerk_v112_signal(closeadj):
    base = _es(closeadj, 252, 0.05)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_es95_504d_jerk_v113_signal(closeadj):
    base = _es(closeadj, 504, 0.05)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_es95_504d_jerk_v114_signal(closeadj):
    base = _es(closeadj, 504, 0.05)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddacf_126d_jerk_v115_signal(closeadj):
    base = _ddacf(closeadj, 126, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddacf_126d_jerk_v116_signal(closeadj):
    base = _ddacf(closeadj, 126, 63)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddacf_252d_jerk_v117_signal(closeadj):
    base = _ddacf(closeadj, 252, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddacf_252d_jerk_v118_signal(closeadj):
    base = _ddacf(closeadj, 252, 63)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddtrend_252d_jerk_v119_signal(closeadj):
    base = _ddtrend(closeadj, 252, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddtrend_252d_jerk_v120_signal(closeadj):
    base = _ddtrend(closeadj, 252, 63)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddtrend_126d_jerk_v121_signal(closeadj):
    base = _ddtrend(closeadj, 126, 42)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddtrend_126d_jerk_v122_signal(closeadj):
    base = _ddtrend(closeadj, 126, 42)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_legbal_126d_jerk_v123_signal(closeadj):
    base = _legbal(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_legbal_126d_jerk_v124_signal(closeadj):
    base = _legbal(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_legbal_252d_jerk_v125_signal(closeadj):
    base = _legbal(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_legbal_252d_jerk_v126_signal(closeadj):
    base = _legbal(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painterm_252d_jerk_v127_signal(closeadj):
    base = _painterm(closeadj)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_painterm_252d_jerk_v128_signal(closeadj):
    base = _painterm(closeadj)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddrange_252d_jerk_v129_signal(closeadj):
    base = _ddrange(closeadj, 252, 63)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddrange_252d_jerk_v130_signal(closeadj):
    base = _ddrange(closeadj, 252, 63)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddrange_504d_jerk_v131_signal(closeadj):
    base = _ddrange(closeadj, 504, 126)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddrange_504d_jerk_v132_signal(closeadj):
    base = _ddrange(closeadj, 504, 126)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdar_504d_jerk_v133_signal(closeadj):
    base = _cdar(closeadj, 504, 0.10)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdar_504d_jerk_v134_signal(closeadj):
    base = _cdar(closeadj, 504, 0.10)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdarrat_252d_jerk_v135_signal(closeadj):
    base = _cdarrat(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdarrat_252d_jerk_v136_signal(closeadj):
    base = _cdarrat(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_healeff_252d_jerk_v137_signal(closeadj):
    base = _healeff(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_healeff_252d_jerk_v138_signal(closeadj):
    base = _healeff(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_healeff_126d_jerk_v139_signal(closeadj):
    base = _healeff(closeadj, 126)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_healeff_126d_jerk_v140_signal(closeadj):
    base = _healeff(closeadj, 126)
    slope = base.diff(42) / float(42)
    d = slope.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddskew_252d_jerk_v141_signal(closeadj):
    base = _ddskew(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddskew_252d_jerk_v142_signal(closeadj):
    base = _ddskew(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dddisp_252d_jerk_v143_signal(closeadj):
    base = _ddmean_disp(closeadj)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_dddisp_252d_jerk_v144_signal(closeadj):
    base = _ddmean_disp(closeadj)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_504d_jerk_v145_signal(closeadj):
    base = _downvol(closeadj, 504)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_504d_jerk_v146_signal(closeadj):
    base = _downvol(closeadj, 504)
    slope = base.diff(126) / float(126)
    d = slope.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_lossconc_252d_jerk_v147_signal(closeadj):
    base = _lossconc(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_lossconc_252d_jerk_v148_signal(closeadj):
    base = _lossconc(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_tailrat_252d_jerk_v149_signal(closeadj):
    base = _tailrat(closeadj, 252)
    slope = base.diff(21) / float(21)
    d = slope.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_tailrat_252d_jerk_v150_signal(closeadj):
    base = _tailrat(closeadj, 252)
    slope = base.diff(63) / float(63)
    d = slope.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f06dr_f06_drawdown_recovery_curdd_63d_jerk_v001_signal,
    f06dr_f06_drawdown_recovery_curdd_63d_jerk_v002_signal,
    f06dr_f06_drawdown_recovery_curdd_126d_jerk_v003_signal,
    f06dr_f06_drawdown_recovery_curdd_126d_jerk_v004_signal,
    f06dr_f06_drawdown_recovery_curdd_252d_jerk_v005_signal,
    f06dr_f06_drawdown_recovery_curdd_252d_jerk_v006_signal,
    f06dr_f06_drawdown_recovery_curdd_504d_jerk_v007_signal,
    f06dr_f06_drawdown_recovery_curdd_504d_jerk_v008_signal,
    f06dr_f06_drawdown_recovery_maxdd_63d_jerk_v009_signal,
    f06dr_f06_drawdown_recovery_maxdd_63d_jerk_v010_signal,
    f06dr_f06_drawdown_recovery_maxdd_126d_jerk_v011_signal,
    f06dr_f06_drawdown_recovery_maxdd_126d_jerk_v012_signal,
    f06dr_f06_drawdown_recovery_maxdd_252d_jerk_v013_signal,
    f06dr_f06_drawdown_recovery_maxdd_252d_jerk_v014_signal,
    f06dr_f06_drawdown_recovery_maxdd_504d_jerk_v015_signal,
    f06dr_f06_drawdown_recovery_maxdd_504d_jerk_v016_signal,
    f06dr_f06_drawdown_recovery_recov_63d_jerk_v017_signal,
    f06dr_f06_drawdown_recovery_recov_63d_jerk_v018_signal,
    f06dr_f06_drawdown_recovery_recov_126d_jerk_v019_signal,
    f06dr_f06_drawdown_recovery_recov_126d_jerk_v020_signal,
    f06dr_f06_drawdown_recovery_recov_252d_jerk_v021_signal,
    f06dr_f06_drawdown_recovery_recov_252d_jerk_v022_signal,
    f06dr_f06_drawdown_recovery_recov_504d_jerk_v023_signal,
    f06dr_f06_drawdown_recovery_recov_504d_jerk_v024_signal,
    f06dr_f06_drawdown_recovery_uwfrac_126d_jerk_v025_signal,
    f06dr_f06_drawdown_recovery_uwfrac_126d_jerk_v026_signal,
    f06dr_f06_drawdown_recovery_uwfrac_504d_jerk_v027_signal,
    f06dr_f06_drawdown_recovery_uwfrac_504d_jerk_v028_signal,
    f06dr_f06_drawdown_recovery_runup504_504d_jerk_v029_signal,
    f06dr_f06_drawdown_recovery_runup504_504d_jerk_v030_signal,
    f06dr_f06_drawdown_recovery_cdar_252d_jerk_v031_signal,
    f06dr_f06_drawdown_recovery_cdar_252d_jerk_v032_signal,
    f06dr_f06_drawdown_recovery_pain_63d_jerk_v033_signal,
    f06dr_f06_drawdown_recovery_pain_63d_jerk_v034_signal,
    f06dr_f06_drawdown_recovery_pain_126d_jerk_v035_signal,
    f06dr_f06_drawdown_recovery_pain_126d_jerk_v036_signal,
    f06dr_f06_drawdown_recovery_pain_252d_jerk_v037_signal,
    f06dr_f06_drawdown_recovery_pain_252d_jerk_v038_signal,
    f06dr_f06_drawdown_recovery_pain_504d_jerk_v039_signal,
    f06dr_f06_drawdown_recovery_pain_504d_jerk_v040_signal,
    f06dr_f06_drawdown_recovery_recovshr_63d_jerk_v041_signal,
    f06dr_f06_drawdown_recovery_recovshr_63d_jerk_v042_signal,
    f06dr_f06_drawdown_recovery_recovshr_126d_jerk_v043_signal,
    f06dr_f06_drawdown_recovery_recovshr_126d_jerk_v044_signal,
    f06dr_f06_drawdown_recovery_recovshr_252d_jerk_v045_signal,
    f06dr_f06_drawdown_recovery_recovshr_252d_jerk_v046_signal,
    f06dr_f06_drawdown_recovery_recovshr_504d_jerk_v047_signal,
    f06dr_f06_drawdown_recovery_recovshr_504d_jerk_v048_signal,
    f06dr_f06_drawdown_recovery_calmar_126d_jerk_v049_signal,
    f06dr_f06_drawdown_recovery_calmar_126d_jerk_v050_signal,
    f06dr_f06_drawdown_recovery_calmar_252d_jerk_v051_signal,
    f06dr_f06_drawdown_recovery_calmar_252d_jerk_v052_signal,
    f06dr_f06_drawdown_recovery_calmar_504d_jerk_v053_signal,
    f06dr_f06_drawdown_recovery_calmar_504d_jerk_v054_signal,
    f06dr_f06_drawdown_recovery_painrat_126d_jerk_v055_signal,
    f06dr_f06_drawdown_recovery_painrat_126d_jerk_v056_signal,
    f06dr_f06_drawdown_recovery_painrat_252d_jerk_v057_signal,
    f06dr_f06_drawdown_recovery_painrat_252d_jerk_v058_signal,
    f06dr_f06_drawdown_recovery_gainpain_63d_jerk_v059_signal,
    f06dr_f06_drawdown_recovery_gainpain_63d_jerk_v060_signal,
    f06dr_f06_drawdown_recovery_gainpain_126d_jerk_v061_signal,
    f06dr_f06_drawdown_recovery_gainpain_126d_jerk_v062_signal,
    f06dr_f06_drawdown_recovery_gainpain_252d_jerk_v063_signal,
    f06dr_f06_drawdown_recovery_gainpain_252d_jerk_v064_signal,
    f06dr_f06_drawdown_recovery_dvshare_126d_jerk_v065_signal,
    f06dr_f06_drawdown_recovery_dvshare_126d_jerk_v066_signal,
    f06dr_f06_drawdown_recovery_dvshare_252d_jerk_v067_signal,
    f06dr_f06_drawdown_recovery_dvshare_252d_jerk_v068_signal,
    f06dr_f06_drawdown_recovery_avgepdd_252d_jerk_v069_signal,
    f06dr_f06_drawdown_recovery_avgepdd_252d_jerk_v070_signal,
    f06dr_f06_drawdown_recovery_avgepdd_504d_jerk_v071_signal,
    f06dr_f06_drawdown_recovery_avgepdd_504d_jerk_v072_signal,
    f06dr_f06_drawdown_recovery_ddfworst_126d_jerk_v073_signal,
    f06dr_f06_drawdown_recovery_ddfworst_126d_jerk_v074_signal,
    f06dr_f06_drawdown_recovery_ddfworst_252d_jerk_v075_signal,
    f06dr_f06_drawdown_recovery_ddfworst_252d_jerk_v076_signal,
    f06dr_f06_drawdown_recovery_painz_252d_jerk_v077_signal,
    f06dr_f06_drawdown_recovery_painz_252d_jerk_v078_signal,
    f06dr_f06_drawdown_recovery_maxddz_252d_jerk_v079_signal,
    f06dr_f06_drawdown_recovery_maxddz_252d_jerk_v080_signal,
    f06dr_f06_drawdown_recovery_ewpain_252d_jerk_v081_signal,
    f06dr_f06_drawdown_recovery_ewpain_252d_jerk_v082_signal,
    f06dr_f06_drawdown_recovery_ewpain_504d_jerk_v083_signal,
    f06dr_f06_drawdown_recovery_ewpain_504d_jerk_v084_signal,
    f06dr_f06_drawdown_recovery_ddarea_252d_jerk_v085_signal,
    f06dr_f06_drawdown_recovery_ddarea_252d_jerk_v086_signal,
    f06dr_f06_drawdown_recovery_ddarea_504d_jerk_v087_signal,
    f06dr_f06_drawdown_recovery_ddarea_504d_jerk_v088_signal,
    f06dr_f06_drawdown_recovery_amp_126d_jerk_v089_signal,
    f06dr_f06_drawdown_recovery_amp_126d_jerk_v090_signal,
    f06dr_f06_drawdown_recovery_amp_252d_jerk_v091_signal,
    f06dr_f06_drawdown_recovery_amp_252d_jerk_v092_signal,
    f06dr_f06_drawdown_recovery_amp_504d_jerk_v093_signal,
    f06dr_f06_drawdown_recovery_amp_504d_jerk_v094_signal,
    f06dr_f06_drawdown_recovery_runup_63d_jerk_v095_signal,
    f06dr_f06_drawdown_recovery_runup_63d_jerk_v096_signal,
    f06dr_f06_drawdown_recovery_runup_126d_jerk_v097_signal,
    f06dr_f06_drawdown_recovery_runup_126d_jerk_v098_signal,
    f06dr_f06_drawdown_recovery_runup_252d_jerk_v099_signal,
    f06dr_f06_drawdown_recovery_runup_252d_jerk_v100_signal,
    f06dr_f06_drawdown_recovery_downvol_63d_jerk_v101_signal,
    f06dr_f06_drawdown_recovery_downvol_63d_jerk_v102_signal,
    f06dr_f06_drawdown_recovery_downvol_126d_jerk_v103_signal,
    f06dr_f06_drawdown_recovery_downvol_126d_jerk_v104_signal,
    f06dr_f06_drawdown_recovery_downvol_252d_jerk_v105_signal,
    f06dr_f06_drawdown_recovery_downvol_252d_jerk_v106_signal,
    f06dr_f06_drawdown_recovery_ulcervol_126d_jerk_v107_signal,
    f06dr_f06_drawdown_recovery_ulcervol_126d_jerk_v108_signal,
    f06dr_f06_drawdown_recovery_ulcervol_252d_jerk_v109_signal,
    f06dr_f06_drawdown_recovery_ulcervol_252d_jerk_v110_signal,
    f06dr_f06_drawdown_recovery_es95_252d_jerk_v111_signal,
    f06dr_f06_drawdown_recovery_es95_252d_jerk_v112_signal,
    f06dr_f06_drawdown_recovery_es95_504d_jerk_v113_signal,
    f06dr_f06_drawdown_recovery_es95_504d_jerk_v114_signal,
    f06dr_f06_drawdown_recovery_ddacf_126d_jerk_v115_signal,
    f06dr_f06_drawdown_recovery_ddacf_126d_jerk_v116_signal,
    f06dr_f06_drawdown_recovery_ddacf_252d_jerk_v117_signal,
    f06dr_f06_drawdown_recovery_ddacf_252d_jerk_v118_signal,
    f06dr_f06_drawdown_recovery_ddtrend_252d_jerk_v119_signal,
    f06dr_f06_drawdown_recovery_ddtrend_252d_jerk_v120_signal,
    f06dr_f06_drawdown_recovery_ddtrend_126d_jerk_v121_signal,
    f06dr_f06_drawdown_recovery_ddtrend_126d_jerk_v122_signal,
    f06dr_f06_drawdown_recovery_legbal_126d_jerk_v123_signal,
    f06dr_f06_drawdown_recovery_legbal_126d_jerk_v124_signal,
    f06dr_f06_drawdown_recovery_legbal_252d_jerk_v125_signal,
    f06dr_f06_drawdown_recovery_legbal_252d_jerk_v126_signal,
    f06dr_f06_drawdown_recovery_painterm_252d_jerk_v127_signal,
    f06dr_f06_drawdown_recovery_painterm_252d_jerk_v128_signal,
    f06dr_f06_drawdown_recovery_ddrange_252d_jerk_v129_signal,
    f06dr_f06_drawdown_recovery_ddrange_252d_jerk_v130_signal,
    f06dr_f06_drawdown_recovery_ddrange_504d_jerk_v131_signal,
    f06dr_f06_drawdown_recovery_ddrange_504d_jerk_v132_signal,
    f06dr_f06_drawdown_recovery_cdar_504d_jerk_v133_signal,
    f06dr_f06_drawdown_recovery_cdar_504d_jerk_v134_signal,
    f06dr_f06_drawdown_recovery_cdarrat_252d_jerk_v135_signal,
    f06dr_f06_drawdown_recovery_cdarrat_252d_jerk_v136_signal,
    f06dr_f06_drawdown_recovery_healeff_252d_jerk_v137_signal,
    f06dr_f06_drawdown_recovery_healeff_252d_jerk_v138_signal,
    f06dr_f06_drawdown_recovery_healeff_126d_jerk_v139_signal,
    f06dr_f06_drawdown_recovery_healeff_126d_jerk_v140_signal,
    f06dr_f06_drawdown_recovery_ddskew_252d_jerk_v141_signal,
    f06dr_f06_drawdown_recovery_ddskew_252d_jerk_v142_signal,
    f06dr_f06_drawdown_recovery_dddisp_252d_jerk_v143_signal,
    f06dr_f06_drawdown_recovery_dddisp_252d_jerk_v144_signal,
    f06dr_f06_drawdown_recovery_downvol_504d_jerk_v145_signal,
    f06dr_f06_drawdown_recovery_downvol_504d_jerk_v146_signal,
    f06dr_f06_drawdown_recovery_lossconc_252d_jerk_v147_signal,
    f06dr_f06_drawdown_recovery_lossconc_252d_jerk_v148_signal,
    f06dr_f06_drawdown_recovery_tailrat_252d_jerk_v149_signal,
    f06dr_f06_drawdown_recovery_tailrat_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_DRAWDOWN_RECOVERY_REGISTRY_001_150 = REGISTRY


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

    print("OK f06_drawdown_recovery_3rd_derivatives_001_150_claude: %d features pass" % n_features)
