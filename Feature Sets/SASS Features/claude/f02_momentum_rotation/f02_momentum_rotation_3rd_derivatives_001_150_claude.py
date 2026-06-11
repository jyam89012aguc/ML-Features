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


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(close, w):
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _logmom(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _vol(close, w):
    return close.pct_change().rolling(w, min_periods=max(1, w // 2)).std()


def _annmom(close, w):
    return _logmom(close, w) * (252.0 / w)


def _slope(s, rw):
    # 1st math derivative: rate of change of the base series over rw days
    return s - s.shift(rw)


def _jerk(s, rw):
    # 2nd math derivative: change of the change (discrete second difference) over rw days
    return (s - s.shift(rw)) - (s.shift(rw) - s.shift(2 * rw))


def _wrap_raw(s, w):
    # de-trended raw: subtract a long mean so it is not a pure level (still keeps shape)
    return s - s.rolling(max(21, w), min_periods=max(2, w // 2)).mean()


def _wrap_z(s, w):
    return _z(s, max(21, w))


def _wrap_rank(s, w):
    return _rank(s, max(21, w))


def _wrap_tanh(s, w):
    sd = s.rolling(max(21, w), min_periods=max(2, w // 2)).std().replace(0, np.nan)
    return np.tanh(s / sd)


def _wrap_emadisp(s, w):
    return s - s.ewm(span=max(10, w), min_periods=max(2, w // 2)).mean()


def _wrap_smooth(s, w):
    return _rank(s.ewm(span=max(5, w // 3 + 2), min_periods=2).mean(), max(21, w))


def f02mr_f02_momentum_rotation_roc_5d_jerk_v001_signal(closeadj):
    base = _roc(closeadj, 5)
    wbase = _wrap_z(base, 47)
    result = _jerk(wbase, 12)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_21d_jerk_v002_signal(closeadj):
    base = _roc(closeadj, 21)
    wbase = _wrap_rank(base, 64)
    result = _jerk(wbase, 19)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_63d_jerk_v003_signal(closeadj):
    base = _roc(closeadj, 63)
    wbase = _wrap_tanh(base, 81)
    result = _jerk(wbase, 26)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_126d_jerk_v004_signal(closeadj):
    base = _roc(closeadj, 126)
    wbase = _wrap_emadisp(base, 98)
    result = _jerk(wbase, 33)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_252d_jerk_v005_signal(closeadj):
    base = _roc(closeadj, 252)
    wbase = _wrap_smooth(base, 115)
    result = _jerk(wbase, 40)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logmom_21d_jerk_v006_signal(closeadj):
    base = _logmom(closeadj, 21)
    wbase = _wrap_raw(base, 132)
    result = _jerk(wbase, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logmom_63d_jerk_v007_signal(closeadj):
    base = _logmom(closeadj, 63)
    wbase = _wrap_z(base, 149)
    result = _jerk(wbase, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logmom_126d_jerk_v008_signal(closeadj):
    base = _logmom(closeadj, 126)
    wbase = _wrap_rank(base, 166)
    result = _jerk(wbase, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logmom_252d_jerk_v009_signal(closeadj):
    base = _logmom(closeadj, 252)
    wbase = _wrap_tanh(base, 183)
    result = _jerk(wbase, 28)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_annmom_21d_jerk_v010_signal(closeadj):
    base = _annmom(closeadj, 21)
    wbase = _wrap_emadisp(base, 200)
    result = _jerk(wbase, 35)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_annmom_63d_jerk_v011_signal(closeadj):
    base = _annmom(closeadj, 63)
    wbase = _wrap_smooth(base, 217)
    result = _jerk(wbase, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_annmom_126d_jerk_v012_signal(closeadj):
    base = _annmom(closeadj, 126)
    wbase = _wrap_raw(base, 234)
    result = _jerk(wbase, 9)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_annmom_252d_jerk_v013_signal(closeadj):
    base = _annmom(closeadj, 252)
    wbase = _wrap_z(base, 251)
    result = _jerk(wbase, 16)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emaprc_10d_jerk_v014_signal(closeadj):
    base = closeadj.ewm(span=10, min_periods=max(2, 10 // 2)).mean() / closeadj.ewm(span=10 * 3, min_periods=10).mean() - 1.0
    wbase = _wrap_rank(base, 268)
    result = _jerk(wbase, 23)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emaprc_21d_jerk_v015_signal(closeadj):
    base = closeadj.ewm(span=21, min_periods=max(2, 21 // 2)).mean() / closeadj.ewm(span=21 * 3, min_periods=21).mean() - 1.0
    wbase = _wrap_tanh(base, 45)
    result = _jerk(wbase, 30)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emaprc_63d_jerk_v016_signal(closeadj):
    base = closeadj.ewm(span=63, min_periods=max(2, 63 // 2)).mean() / closeadj.ewm(span=63 * 3, min_periods=63).mean() - 1.0
    wbase = _wrap_emadisp(base, 62)
    result = _jerk(wbase, 37)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_21d_jerk_v017_signal(closeadj):
    base = _roc(closeadj, 21) / (_vol(closeadj, 21) * np.sqrt(21)).replace(0, np.nan)
    wbase = _wrap_smooth(base, 79)
    result = _jerk(wbase, 44)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_63d_jerk_v018_signal(closeadj):
    base = _roc(closeadj, 63) / (_vol(closeadj, 63) * np.sqrt(63)).replace(0, np.nan)
    wbase = _wrap_raw(base, 96)
    result = _jerk(wbase, 11)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_126d_jerk_v019_signal(closeadj):
    base = _roc(closeadj, 126) / (_vol(closeadj, 126) * np.sqrt(126)).replace(0, np.nan)
    wbase = _wrap_z(base, 113)
    result = _jerk(wbase, 18)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_252d_jerk_v020_signal(closeadj):
    base = _roc(closeadj, 252) / (_vol(closeadj, 252) * np.sqrt(252)).replace(0, np.nan)
    wbase = _wrap_rank(base, 130)
    result = _jerk(wbase, 25)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sharpe_21d_jerk_v021_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 21) / _std(r, 21).replace(0, np.nan)
    wbase = _wrap_tanh(base, 147)
    result = _jerk(wbase, 32)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sharpe_63d_jerk_v022_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63) / _std(r, 63).replace(0, np.nan)
    wbase = _wrap_emadisp(base, 164)
    result = _jerk(wbase, 39)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sharpe_126d_jerk_v023_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 126) / _std(r, 126).replace(0, np.nan)
    wbase = _wrap_smooth(base, 181)
    result = _jerk(wbase, 6)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitrate_21d_jerk_v024_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean() - 0.5
    base = hr + 2.0 * _roc(closeadj, 21)
    wbase = _wrap_raw(base, 198)
    result = _jerk(wbase, 13)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitrate_63d_jerk_v025_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean() - 0.5
    base = hr + 2.0 * _roc(closeadj, 63)
    wbase = _wrap_z(base, 215)
    result = _jerk(wbase, 20)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitrate_126d_jerk_v026_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean() - 0.5
    base = hr + 2.0 * _roc(closeadj, 126)
    wbase = _wrap_rank(base, 232)
    result = _jerk(wbase, 27)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocrank_21d_jerk_v027_signal(closeadj):
    base = _rank(_roc(closeadj, 21), 21 * 4)
    wbase = _wrap_tanh(base, 249)
    result = _jerk(wbase, 34)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocrank_63d_jerk_v028_signal(closeadj):
    base = _rank(_roc(closeadj, 63), 63 * 4)
    wbase = _wrap_emadisp(base, 266)
    result = _jerk(wbase, 41)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocrank_126d_jerk_v029_signal(closeadj):
    base = _rank(_roc(closeadj, 126), 126 * 4)
    wbase = _wrap_smooth(base, 43)
    result = _jerk(wbase, 8)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_pricez_21d_jerk_v030_signal(closeadj):
    base = _z(closeadj, 21)
    wbase = _wrap_raw(base, 60)
    result = _jerk(wbase, 15)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_pricez_63d_jerk_v031_signal(closeadj):
    base = _z(closeadj, 63)
    wbase = _wrap_z(base, 77)
    result = _jerk(wbase, 22)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_pricez_126d_jerk_v032_signal(closeadj):
    base = _z(closeadj, 126)
    wbase = _wrap_rank(base, 94)
    result = _jerk(wbase, 29)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsi_14d_jerk_v033_signal(closeadj):
    d = closeadj.diff()
    g = d.where(d > 0, 0.0).rolling(14, min_periods=max(5, 14 // 2)).mean()
    l = (-d.where(d < 0, 0.0)).rolling(14, min_periods=max(5, 14 // 2)).mean()
    base = (1.0 - 1.0 / (1.0 + g / l.replace(0, np.nan))) - 0.5
    wbase = _wrap_tanh(base, 111)
    result = _jerk(wbase, 36)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsi_21d_jerk_v034_signal(closeadj):
    d = closeadj.diff()
    g = d.where(d > 0, 0.0).rolling(21, min_periods=max(5, 21 // 2)).mean()
    l = (-d.where(d < 0, 0.0)).rolling(21, min_periods=max(5, 21 // 2)).mean()
    base = (1.0 - 1.0 / (1.0 + g / l.replace(0, np.nan))) - 0.5
    wbase = _wrap_emadisp(base, 128)
    result = _jerk(wbase, 43)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsi_63d_jerk_v035_signal(closeadj):
    d = closeadj.diff()
    g = d.where(d > 0, 0.0).rolling(63, min_periods=max(5, 63 // 2)).mean()
    l = (-d.where(d < 0, 0.0)).rolling(63, min_periods=max(5, 63 // 2)).mean()
    base = (1.0 - 1.0 / (1.0 + g / l.replace(0, np.nan))) - 0.5
    wbase = _wrap_smooth(base, 145)
    result = _jerk(wbase, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmamom_10d_jerk_v036_signal(closeadj):
    base = closeadj.pct_change().ewm(span=10, min_periods=max(2, 10 // 2)).mean() * 10
    wbase = _wrap_raw(base, 162)
    result = _jerk(wbase, 17)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmamom_21d_jerk_v037_signal(closeadj):
    base = closeadj.pct_change().ewm(span=21, min_periods=max(2, 21 // 2)).mean() * 21
    wbase = _wrap_z(base, 179)
    result = _jerk(wbase, 24)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmamom_63d_jerk_v038_signal(closeadj):
    base = closeadj.pct_change().ewm(span=63, min_periods=max(2, 63 // 2)).mean() * 63
    wbase = _wrap_rank(base, 196)
    result = _jerk(wbase, 31)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_patheff_21d_jerk_v039_signal(closeadj):
    net = (closeadj - closeadj.shift(21))
    gross = closeadj.diff().abs().rolling(21, min_periods=max(1, 21 // 2)).sum()
    base = net / gross.replace(0, np.nan)
    wbase = _wrap_tanh(base, 213)
    result = _jerk(wbase, 38)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_patheff_63d_jerk_v040_signal(closeadj):
    net = (closeadj - closeadj.shift(63))
    gross = closeadj.diff().abs().rolling(63, min_periods=max(1, 63 // 2)).sum()
    base = net / gross.replace(0, np.nan)
    wbase = _wrap_emadisp(base, 230)
    result = _jerk(wbase, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_patheff_126d_jerk_v041_signal(closeadj):
    net = (closeadj - closeadj.shift(126))
    gross = closeadj.diff().abs().rolling(126, min_periods=max(1, 126 // 2)).sum()
    base = net / gross.replace(0, np.nan)
    wbase = _wrap_smooth(base, 247)
    result = _jerk(wbase, 12)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_gainloss_21d_jerk_v042_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, 0.0).rolling(21, min_periods=max(1, 21 // 2)).mean()
    dn = (-r.where(r < 0, 0.0)).rolling(21, min_periods=max(1, 21 // 2)).mean()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    wbase = _wrap_raw(base, 264)
    result = _jerk(wbase, 19)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_gainloss_63d_jerk_v043_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, 0.0).rolling(63, min_periods=max(1, 63 // 2)).mean()
    dn = (-r.where(r < 0, 0.0)).rolling(63, min_periods=max(1, 63 // 2)).mean()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    wbase = _wrap_z(base, 41)
    result = _jerk(wbase, 26)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_gainloss_126d_jerk_v044_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, 0.0).rolling(126, min_periods=max(1, 126 // 2)).mean()
    dn = (-r.where(r < 0, 0.0)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    wbase = _wrap_rank(base, 58)
    result = _jerk(wbase, 33)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dnfreq_21d_jerk_v045_signal(closeadj):
    dn = (closeadj.pct_change() < 0).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean() - 0.5
    base = dn - 2.0 * _roc(closeadj, 21)
    wbase = _wrap_tanh(base, 75)
    result = _jerk(wbase, 40)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dnfreq_63d_jerk_v046_signal(closeadj):
    dn = (closeadj.pct_change() < 0).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean() - 0.5
    base = dn - 2.0 * _roc(closeadj, 63)
    wbase = _wrap_emadisp(base, 92)
    result = _jerk(wbase, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dnfreq_126d_jerk_v047_signal(closeadj):
    dn = (closeadj.pct_change() < 0).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean() - 0.5
    base = dn - 2.0 * _roc(closeadj, 126)
    wbase = _wrap_smooth(base, 109)
    result = _jerk(wbase, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_volratio_21d_jerk_v048_signal(closeadj):
    base = _vol(closeadj, 21) / _vol(closeadj, 21 * 3).replace(0, np.nan)
    wbase = _wrap_raw(base, 126)
    result = _jerk(wbase, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_volratio_42d_jerk_v049_signal(closeadj):
    base = _vol(closeadj, 42) / _vol(closeadj, 42 * 3).replace(0, np.nan)
    wbase = _wrap_z(base, 143)
    result = _jerk(wbase, 28)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_volratio_63d_jerk_v050_signal(closeadj):
    base = _vol(closeadj, 63) / _vol(closeadj, 63 * 3).replace(0, np.nan)
    wbase = _wrap_rank(base, 160)
    result = _jerk(wbase, 35)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logslopeq_63d_jerk_v051_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _sl(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        dn = (xd ** 2).sum()
        if dn == 0:
            return np.nan
        sl = np.dot(xd, a - a.mean()) / dn
        resid = a - (a.mean() + sl * xd)
        rs = resid.std()
        if rs == 0:
            return np.nan
        return float(sl / rs)
    base = lp.rolling(63, min_periods=max(2, 63 // 2)).apply(_sl, raw=True)
    wbase = _wrap_tanh(base, 177)
    result = _jerk(wbase, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logslopeq_126d_jerk_v052_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _sl(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        dn = (xd ** 2).sum()
        if dn == 0:
            return np.nan
        sl = np.dot(xd, a - a.mean()) / dn
        resid = a - (a.mean() + sl * xd)
        rs = resid.std()
        if rs == 0:
            return np.nan
        return float(sl / rs)
    base = lp.rolling(126, min_periods=max(2, 126 // 2)).apply(_sl, raw=True)
    wbase = _wrap_emadisp(base, 194)
    result = _jerk(wbase, 9)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logslopeq_252d_jerk_v053_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _sl(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        dn = (xd ** 2).sum()
        if dn == 0:
            return np.nan
        sl = np.dot(xd, a - a.mean()) / dn
        resid = a - (a.mean() + sl * xd)
        rs = resid.std()
        if rs == 0:
            return np.nan
        return float(sl / rs)
    base = lp.rolling(252, min_periods=max(2, 252 // 2)).apply(_sl, raw=True)
    wbase = _wrap_smooth(base, 211)
    result = _jerk(wbase, 16)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momdisp_126d_jerk_v054_signal(closeadj):
    a = _annmom(closeadj, 21)
    b1 = _annmom(closeadj, 63)
    c = _annmom(closeadj, 126)
    base = pd.concat([a, b1, c], axis=1).std(axis=1)
    wbase = _wrap_raw(base, 228)
    result = _jerk(wbase, 23)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momdisp_252d_jerk_v055_signal(closeadj):
    a = _annmom(closeadj, 21)
    b1 = _annmom(closeadj, 63)
    c = _annmom(closeadj, 252)
    base = pd.concat([a, b1, c], axis=1).std(axis=1)
    wbase = _wrap_z(base, 245)
    result = _jerk(wbase, 30)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_mtspr_63d_jerk_v056_signal(closeadj):
    base = _annmom(closeadj, 21) - _annmom(closeadj, 63)
    wbase = _wrap_rank(base, 262)
    result = _jerk(wbase, 37)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_mtspr_126d_jerk_v057_signal(closeadj):
    base = _annmom(closeadj, 21) - _annmom(closeadj, 126)
    wbase = _wrap_tanh(base, 39)
    result = _jerk(wbase, 44)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_mtspr_252d_jerk_v058_signal(closeadj):
    base = _annmom(closeadj, 21) - _annmom(closeadj, 252)
    wbase = _wrap_emadisp(base, 56)
    result = _jerk(wbase, 11)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dvwmom_21d_jerk_v059_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    num = (r * dv).rolling(21, min_periods=max(1, 21 // 2)).sum()
    den = dv.rolling(21, min_periods=max(1, 21 // 2)).sum()
    base = num / den.replace(0, np.nan) * 21
    wbase = _wrap_smooth(base, 73)
    result = _jerk(wbase, 18)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dvwmom_63d_jerk_v060_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    num = (r * dv).rolling(63, min_periods=max(1, 63 // 2)).sum()
    den = dv.rolling(63, min_periods=max(1, 63 // 2)).sum()
    base = num / den.replace(0, np.nan) * 63
    wbase = _wrap_raw(base, 90)
    result = _jerk(wbase, 25)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dvwmom_126d_jerk_v061_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    num = (r * dv).rolling(126, min_periods=max(1, 126 // 2)).sum()
    den = dv.rolling(126, min_periods=max(1, 126 // 2)).sum()
    base = num / den.replace(0, np.nan) * 126
    wbase = _wrap_z(base, 107)
    result = _jerk(wbase, 32)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_relvol_63d_jerk_v062_signal(closeadj, volume):
    relvol = volume / volume.rolling(63, min_periods=max(1, 63 // 2)).mean().replace(0, np.nan)
    base = np.sign(_roc(closeadj, 63)) * np.tanh(_z(relvol, 63 * 2))
    wbase = _wrap_rank(base, 124)
    result = _jerk(wbase, 39)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_relvol_126d_jerk_v063_signal(closeadj, volume):
    relvol = volume / volume.rolling(126, min_periods=max(1, 126 // 2)).mean().replace(0, np.nan)
    base = np.sign(_roc(closeadj, 126)) * np.tanh(_z(relvol, 126 * 2))
    wbase = _wrap_tanh(base, 141)
    result = _jerk(wbase, 6)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_aroon_21d_jerk_v064_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    up = 1.0 - closeadj.rolling(21, min_periods=max(1, 21 // 2)).apply(_dsh, raw=True)
    dn = 1.0 - closeadj.rolling(21, min_periods=max(1, 21 // 2)).apply(_dsl, raw=True)
    base = up - dn
    wbase = _wrap_emadisp(base, 158)
    result = _jerk(wbase, 13)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_aroon_63d_jerk_v065_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    up = 1.0 - closeadj.rolling(63, min_periods=max(1, 63 // 2)).apply(_dsh, raw=True)
    dn = 1.0 - closeadj.rolling(63, min_periods=max(1, 63 // 2)).apply(_dsl, raw=True)
    base = up - dn
    wbase = _wrap_smooth(base, 175)
    result = _jerk(wbase, 20)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_aroon_126d_jerk_v066_signal(closeadj):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    up = 1.0 - closeadj.rolling(126, min_periods=max(1, 126 // 2)).apply(_dsh, raw=True)
    dn = 1.0 - closeadj.rolling(126, min_periods=max(1, 126 // 2)).apply(_dsl, raw=True)
    base = up - dn
    wbase = _wrap_raw(base, 192)
    result = _jerk(wbase, 27)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_netupdays_21d_jerk_v067_signal(closeadj):
    r = closeadj.pct_change()
    nu = np.sign(r).rolling(21, min_periods=max(1, 21 // 2)).sum() / float(21)
    typ = r.abs().rolling(21, min_periods=max(1, 21 // 2)).mean()
    base = nu * typ * np.sqrt(float(21))
    wbase = _wrap_z(base, 209)
    result = _jerk(wbase, 34)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_netupdays_63d_jerk_v068_signal(closeadj):
    r = closeadj.pct_change()
    nu = np.sign(r).rolling(63, min_periods=max(1, 63 // 2)).sum() / float(63)
    typ = r.abs().rolling(63, min_periods=max(1, 63 // 2)).mean()
    base = nu * typ * np.sqrt(float(63))
    wbase = _wrap_rank(base, 226)
    result = _jerk(wbase, 41)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_netupdays_126d_jerk_v069_signal(closeadj):
    r = closeadj.pct_change()
    nu = np.sign(r).rolling(126, min_periods=max(1, 126 // 2)).sum() / float(126)
    typ = r.abs().rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = nu * typ * np.sqrt(float(126))
    wbase = _wrap_tanh(base, 243)
    result = _jerk(wbase, 8)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tanhmom_5d_jerk_v070_signal(closeadj):
    base = np.tanh(6.0 * _roc(closeadj, 5))
    wbase = _wrap_emadisp(base, 260)
    result = _jerk(wbase, 15)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tanhmom_21d_jerk_v071_signal(closeadj):
    base = np.tanh(6.0 * _roc(closeadj, 21))
    wbase = _wrap_smooth(base, 37)
    result = _jerk(wbase, 22)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tanhmom_63d_jerk_v072_signal(closeadj):
    base = np.tanh(6.0 * _roc(closeadj, 63))
    wbase = _wrap_raw(base, 54)
    result = _jerk(wbase, 29)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tanhmom_126d_jerk_v073_signal(closeadj):
    base = np.tanh(6.0 * _roc(closeadj, 126))
    wbase = _wrap_z(base, 71)
    result = _jerk(wbase, 36)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sortino_21d_jerk_v074_signal(closeadj):
    r = closeadj.pct_change()
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=max(1, 21 // 2)).std()
    base = _roc(closeadj, 21) / (dn * np.sqrt(21)).replace(0, np.nan)
    wbase = _wrap_rank(base, 88)
    result = _jerk(wbase, 43)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sortino_63d_jerk_v075_signal(closeadj):
    r = closeadj.pct_change()
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=max(1, 63 // 2)).std()
    base = _roc(closeadj, 63) / (dn * np.sqrt(63)).replace(0, np.nan)
    wbase = _wrap_tanh(base, 105)
    result = _jerk(wbase, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_sortino_126d_jerk_v076_signal(closeadj):
    r = closeadj.pct_change()
    dn = r.where(r < 0, 0.0).rolling(126, min_periods=max(1, 126 // 2)).std()
    base = _roc(closeadj, 126) / (dn * np.sqrt(126)).replace(0, np.nan)
    wbase = _wrap_emadisp(base, 122)
    result = _jerk(wbase, 17)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_retskew_63d_jerk_v077_signal(closeadj):
    base = closeadj.pct_change().rolling(63, min_periods=max(1, 63 // 2)).skew()
    wbase = _wrap_smooth(base, 139)
    result = _jerk(wbase, 24)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_retskew_126d_jerk_v078_signal(closeadj):
    base = closeadj.pct_change().rolling(126, min_periods=max(1, 126 // 2)).skew()
    wbase = _wrap_raw(base, 156)
    result = _jerk(wbase, 31)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_macd_12d_jerk_v079_signal(closeadj):
    base = (closeadj.ewm(span=12, min_periods=max(2, 12 // 2)).mean() - closeadj.ewm(span=12 * 2, min_periods=12).mean()) / closeadj.replace(0, np.nan)
    wbase = _wrap_z(base, 173)
    result = _jerk(wbase, 38)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_macd_21d_jerk_v080_signal(closeadj):
    base = (closeadj.ewm(span=21, min_periods=max(2, 21 // 2)).mean() - closeadj.ewm(span=21 * 2, min_periods=21).mean()) / closeadj.replace(0, np.nan)
    wbase = _wrap_rank(base, 190)
    result = _jerk(wbase, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_macd_63d_jerk_v081_signal(closeadj):
    base = (closeadj.ewm(span=63, min_periods=max(2, 63 // 2)).mean() - closeadj.ewm(span=63 * 2, min_periods=63).mean()) / closeadj.replace(0, np.nan)
    wbase = _wrap_tanh(base, 207)
    result = _jerk(wbase, 12)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_excessmom_63d_jerk_v082_signal(closeadj):
    roc = _roc(closeadj, 63)
    base = roc - roc.rolling(63 * 2, min_periods=63).mean()
    wbase = _wrap_emadisp(base, 224)
    result = _jerk(wbase, 19)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_excessmom_126d_jerk_v083_signal(closeadj):
    roc = _roc(closeadj, 126)
    base = roc - roc.rolling(126 * 2, min_periods=126).mean()
    wbase = _wrap_smooth(base, 241)
    result = _jerk(wbase, 26)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_excessmom_252d_jerk_v084_signal(closeadj):
    roc = _roc(closeadj, 252)
    base = roc - roc.rolling(252 * 2, min_periods=252).mean()
    wbase = _wrap_raw(base, 258)
    result = _jerk(wbase, 33)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_coherence_63d_jerk_v085_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _coh(a):
        if a.std() == 0:
            return np.nan
        return float(np.corrcoef(np.arange(len(a), dtype=float), a)[0, 1])
    base = lp.rolling(63, min_periods=max(2, 63 // 2)).apply(_coh, raw=True)
    wbase = _wrap_z(base, 35)
    result = _jerk(wbase, 40)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_coherence_126d_jerk_v086_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _coh(a):
        if a.std() == 0:
            return np.nan
        return float(np.corrcoef(np.arange(len(a), dtype=float), a)[0, 1])
    base = lp.rolling(126, min_periods=max(2, 126 // 2)).apply(_coh, raw=True)
    wbase = _wrap_rank(base, 52)
    result = _jerk(wbase, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_wgtmom_63d_jerk_v087_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=max(1, 63 // 2)).apply(lambda a: float(np.average(a, weights=np.arange(1, len(a) + 1))), raw=True) * 63
    wbase = _wrap_tanh(base, 69)
    result = _jerk(wbase, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_wgtmom_126d_jerk_v088_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=max(1, 126 // 2)).apply(lambda a: float(np.average(a, weights=np.arange(1, len(a) + 1))), raw=True) * 126
    wbase = _wrap_emadisp(base, 86)
    result = _jerk(wbase, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ulcermom_63d_jerk_v089_signal(closeadj):
    roc = _roc(closeadj, 63)
    peak = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    ulcer = np.sqrt((dd ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean())
    base = roc / ulcer.replace(0, np.nan)
    wbase = _wrap_smooth(base, 103)
    result = _jerk(wbase, 28)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ulcermom_126d_jerk_v090_signal(closeadj):
    roc = _roc(closeadj, 126)
    peak = closeadj.rolling(126, min_periods=max(1, 126 // 2)).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    ulcer = np.sqrt((dd ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean())
    base = roc / ulcer.replace(0, np.nan)
    wbase = _wrap_raw(base, 120)
    result = _jerk(wbase, 35)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dirstrength_21d_jerk_v091_signal(closeadj):
    upmove = closeadj.diff().clip(lower=0)
    dnmove = (-closeadj.diff()).clip(lower=0)
    us = upmove.rolling(21, min_periods=max(1, 21 // 2)).sum()
    ds = dnmove.rolling(21, min_periods=max(1, 21 // 2)).sum()
    base = (us - ds) / (us + ds).replace(0, np.nan)
    wbase = _wrap_z(base, 137)
    result = _jerk(wbase, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dirstrength_63d_jerk_v092_signal(closeadj):
    upmove = closeadj.diff().clip(lower=0)
    dnmove = (-closeadj.diff()).clip(lower=0)
    us = upmove.rolling(63, min_periods=max(1, 63 // 2)).sum()
    ds = dnmove.rolling(63, min_periods=max(1, 63 // 2)).sum()
    base = (us - ds) / (us + ds).replace(0, np.nan)
    wbase = _wrap_rank(base, 154)
    result = _jerk(wbase, 9)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_dirstrength_126d_jerk_v093_signal(closeadj):
    upmove = closeadj.diff().clip(lower=0)
    dnmove = (-closeadj.diff()).clip(lower=0)
    us = upmove.rolling(126, min_periods=max(1, 126 // 2)).sum()
    ds = dnmove.rolling(126, min_periods=max(1, 126 // 2)).sum()
    base = (us - ds) / (us + ds).replace(0, np.nan)
    wbase = _wrap_tanh(base, 171)
    result = _jerk(wbase, 16)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momofmom_63d_jerk_v094_signal(closeadj):
    roc = _roc(closeadj, 63)
    base = roc - roc.shift(63 // 3)
    wbase = _wrap_emadisp(base, 188)
    result = _jerk(wbase, 23)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momofmom_126d_jerk_v095_signal(closeadj):
    roc = _roc(closeadj, 126)
    base = roc - roc.shift(126 // 3)
    wbase = _wrap_smooth(base, 205)
    result = _jerk(wbase, 30)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_momofmom_252d_jerk_v096_signal(closeadj):
    roc = _roc(closeadj, 252)
    base = roc - roc.shift(252 // 3)
    wbase = _wrap_raw(base, 222)
    result = _jerk(wbase, 37)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_zscoremom_21d_jerk_v097_signal(closeadj):
    base = _z(_roc(closeadj, 21), 21 * 2)
    wbase = _wrap_z(base, 239)
    result = _jerk(wbase, 44)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_zscoremom_63d_jerk_v098_signal(closeadj):
    base = _z(_roc(closeadj, 63), 63 * 2)
    wbase = _wrap_rank(base, 256)
    result = _jerk(wbase, 11)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_zscoremom_126d_jerk_v099_signal(closeadj):
    base = _z(_roc(closeadj, 126), 126 * 2)
    wbase = _wrap_tanh(base, 33)
    result = _jerk(wbase, 18)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_consist_63d_jerk_v100_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean() - 0.5
    roc = _roc(closeadj, 63)
    base = (2.0 * hr) * roc.abs() * np.sign(roc)
    wbase = _wrap_emadisp(base, 50)
    result = _jerk(wbase, 25)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_consist_126d_jerk_v101_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean() - 0.5
    roc = _roc(closeadj, 126)
    base = (2.0 * hr) * roc.abs() * np.sign(roc)
    wbase = _wrap_smooth(base, 67)
    result = _jerk(wbase, 32)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmacross_10d_jerk_v102_signal(closeadj):
    fast = closeadj.ewm(span=10, min_periods=max(2, 10 // 2)).mean()
    slow = closeadj.ewm(span=10 * 4, min_periods=10).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    wbase = _wrap_raw(base, 84)
    result = _jerk(wbase, 39)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmacross_21d_jerk_v103_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    slow = closeadj.ewm(span=21 * 4, min_periods=21).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    wbase = _wrap_z(base, 101)
    result = _jerk(wbase, 6)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmacross_63d_jerk_v104_signal(closeadj):
    fast = closeadj.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    slow = closeadj.ewm(span=63 * 4, min_periods=63).mean()
    base = fast / slow.replace(0, np.nan) - 1.0
    wbase = _wrap_rank(base, 118)
    result = _jerk(wbase, 13)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocaccel_63d_jerk_v105_signal(closeadj):
    roc = _roc(closeadj, 63)
    base = roc - roc.shift(63)
    wbase = _wrap_tanh(base, 135)
    result = _jerk(wbase, 20)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocaccel_126d_jerk_v106_signal(closeadj):
    roc = _roc(closeadj, 126)
    base = roc - roc.shift(126)
    wbase = _wrap_emadisp(base, 152)
    result = _jerk(wbase, 27)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_seqmom_63d_jerk_v107_signal(closeadj):
    recent = _roc(closeadj, 63)
    prior = closeadj.shift(63) / closeadj.shift(63 * 2).replace(0, np.nan) - 1.0
    base = recent - prior
    wbase = _wrap_smooth(base, 169)
    result = _jerk(wbase, 34)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_seqmom_126d_jerk_v108_signal(closeadj):
    recent = _roc(closeadj, 126)
    prior = closeadj.shift(126) / closeadj.shift(126 * 2).replace(0, np.nan) - 1.0
    base = recent - prior
    wbase = _wrap_raw(base, 186)
    result = _jerk(wbase, 41)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_trendresid_63d_jerk_v109_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _rsd(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        dn = (xd ** 2).sum()
        if dn == 0:
            return np.nan
        sl = np.dot(xd, a - a.mean()) / dn
        return float(a[-1] - (a.mean() + sl * xd[-1]))
    base = lp.rolling(63, min_periods=max(2, 63 // 2)).apply(_rsd, raw=True)
    wbase = _wrap_z(base, 203)
    result = _jerk(wbase, 8)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_trendresid_126d_jerk_v110_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    def _rsd(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        dn = (xd ** 2).sum()
        if dn == 0:
            return np.nan
        sl = np.dot(xd, a - a.mean()) / dn
        return float(a[-1] - (a.mean() + sl * xd[-1]))
    base = lp.rolling(126, min_periods=max(2, 126 // 2)).apply(_rsd, raw=True)
    wbase = _wrap_rank(base, 220)
    result = _jerk(wbase, 15)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_diffuse_126d_jerk_v111_signal(closeadj):
    base = sum(np.tanh(4.0 * _annmom(closeadj, w)) for w in [5, 21, 63, 126]) / 4.0
    wbase = _wrap_tanh(base, 237)
    result = _jerk(wbase, 22)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_diffuse_252d_jerk_v112_signal(closeadj):
    base = sum(np.tanh(4.0 * _annmom(closeadj, w)) for w in [5, 21, 63, 252]) / 4.0
    wbase = _wrap_emadisp(base, 254)
    result = _jerk(wbase, 29)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_upstreak_63d_jerk_v113_signal(closeadj):
    up = (closeadj.pct_change() > 0).astype(float)
    def _mr(a):
        best = 0
        cur = 0
        for v in a:
            if v > 0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    base = up.rolling(63, min_periods=max(1, 63 // 2)).apply(_mr, raw=True) / float(63) * (1.0 + np.tanh(5.0 * _roc(closeadj, 63)))
    wbase = _wrap_smooth(base, 31)
    result = _jerk(wbase, 36)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_upstreak_126d_jerk_v114_signal(closeadj):
    up = (closeadj.pct_change() > 0).astype(float)
    def _mr(a):
        best = 0
        cur = 0
        for v in a:
            if v > 0:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    base = up.rolling(126, min_periods=max(1, 126 // 2)).apply(_mr, raw=True) / float(126) * (1.0 + np.tanh(5.0 * _roc(closeadj, 126)))
    wbase = _wrap_raw(base, 48)
    result = _jerk(wbase, 43)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_voltgtmom_63d_jerk_v115_signal(closeadj):
    va = _vol(closeadj, 63) * np.sqrt(252)
    base = _roc(closeadj, 63) * (0.2 / va.replace(0, np.nan))
    wbase = _wrap_z(base, 65)
    result = _jerk(wbase, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_voltgtmom_126d_jerk_v116_signal(closeadj):
    va = _vol(closeadj, 126) * np.sqrt(252)
    base = _roc(closeadj, 126) * (0.2 / va.replace(0, np.nan))
    wbase = _wrap_rank(base, 82)
    result = _jerk(wbase, 17)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_voltgtmom_252d_jerk_v117_signal(closeadj):
    va = _vol(closeadj, 252) * np.sqrt(252)
    base = _roc(closeadj, 252) * (0.2 / va.replace(0, np.nan))
    wbase = _wrap_tanh(base, 99)
    result = _jerk(wbase, 24)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsdrift_21d_jerk_v118_signal(closeadj):
    r = closeadj.pct_change()
    base = (r.ewm(span=21, min_periods=max(2, 21 // 2)).mean() - r.ewm(span=21 * 4, min_periods=21).mean()) * 100.0
    wbase = _wrap_emadisp(base, 116)
    result = _jerk(wbase, 31)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rsdrift_63d_jerk_v119_signal(closeadj):
    r = closeadj.pct_change()
    base = (r.ewm(span=63, min_periods=max(2, 63 // 2)).mean() - r.ewm(span=63 * 4, min_periods=63).mean()) * 100.0
    wbase = _wrap_smooth(base, 133)
    result = _jerk(wbase, 38)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_impulse_63d_jerk_v120_signal(closeadj):
    r = closeadj.pct_change()
    sd = r.rolling(63, min_periods=max(1, 63 // 2)).std()
    bu = r.where(r > 1.5 * sd, 0.0)
    bd = (-r).where(r < -1.5 * sd, 0.0)
    base = (bu - bd).rolling(63, min_periods=max(1, 63 // 2)).sum()
    wbase = _wrap_raw(base, 150)
    result = _jerk(wbase, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_impulse_126d_jerk_v121_signal(closeadj):
    r = closeadj.pct_change()
    sd = r.rolling(126, min_periods=max(1, 126 // 2)).std()
    bu = r.where(r > 1.5 * sd, 0.0)
    bd = (-r).where(r < -1.5 * sd, 0.0)
    base = (bu - bd).rolling(126, min_periods=max(1, 126 // 2)).sum()
    wbase = _wrap_z(base, 167)
    result = _jerk(wbase, 12)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_regexcess_63d_jerk_v122_signal(closeadj):
    roc = _roc(closeadj, 63)
    base = roc - roc.ewm(span=63 * 4, min_periods=63).mean()
    wbase = _wrap_rank(base, 184)
    result = _jerk(wbase, 19)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_regexcess_126d_jerk_v123_signal(closeadj):
    roc = _roc(closeadj, 126)
    base = roc - roc.ewm(span=126 * 4, min_periods=126).mean()
    wbase = _wrap_tanh(base, 201)
    result = _jerk(wbase, 26)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_turnmom_63d_jerk_v124_signal(closeadj):
    roc = _roc(closeadj, 63)
    turn = closeadj.pct_change().abs().rolling(63, min_periods=max(1, 63 // 2)).sum()
    base = roc / turn.replace(0, np.nan)
    wbase = _wrap_emadisp(base, 218)
    result = _jerk(wbase, 33)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_turnmom_126d_jerk_v125_signal(closeadj):
    roc = _roc(closeadj, 126)
    turn = closeadj.pct_change().abs().rolling(126, min_periods=max(1, 126 // 2)).sum()
    base = roc / turn.replace(0, np.nan)
    wbase = _wrap_smooth(base, 235)
    result = _jerk(wbase, 40)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_pricezspr_21d_jerk_v126_signal(closeadj):
    base = _z(closeadj, 21) - _z(closeadj, 21 * 4)
    wbase = _wrap_raw(base, 252)
    result = _jerk(wbase, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_pricezspr_63d_jerk_v127_signal(closeadj):
    base = _z(closeadj, 63) - _z(closeadj, 63 * 4)
    wbase = _wrap_z(base, 269)
    result = _jerk(wbase, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tsi_13d_jerk_v128_signal(closeadj):
    d = closeadj.diff()
    pc = d.ewm(span=13 * 2, min_periods=13).mean().ewm(span=13, min_periods=max(2, 13 // 2)).mean()
    apc = d.abs().ewm(span=13 * 2, min_periods=13).mean().ewm(span=13, min_periods=max(2, 13 // 2)).mean()
    base = pc / apc.replace(0, np.nan)
    wbase = _wrap_rank(base, 46)
    result = _jerk(wbase, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_tsi_21d_jerk_v129_signal(closeadj):
    d = closeadj.diff()
    pc = d.ewm(span=21 * 2, min_periods=21).mean().ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    apc = d.abs().ewm(span=21 * 2, min_periods=21).mean().ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    base = pc / apc.replace(0, np.nan)
    wbase = _wrap_tanh(base, 63)
    result = _jerk(wbase, 28)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_shockz_42d_jerk_v130_signal(closeadj):
    base = _z(_roc(closeadj, 5), 42)
    wbase = _wrap_emadisp(base, 80)
    result = _jerk(wbase, 35)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_shockz_63d_jerk_v131_signal(closeadj):
    base = _z(_roc(closeadj, 5), 63)
    wbase = _wrap_smooth(base, 97)
    result = _jerk(wbase, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_shockz_126d_jerk_v132_signal(closeadj):
    base = _z(_roc(closeadj, 5), 126)
    wbase = _wrap_raw(base, 114)
    result = _jerk(wbase, 9)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rankvel_63d_jerk_v133_signal(closeadj):
    rk = _rank(_roc(closeadj, 63), 63 * 4)
    base = rk - rk.shift(63 // 3)
    wbase = _wrap_z(base, 131)
    result = _jerk(wbase, 16)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rankvel_126d_jerk_v134_signal(closeadj):
    rk = _rank(_roc(closeadj, 126), 126 * 4)
    base = rk - rk.shift(126 // 3)
    wbase = _wrap_rank(base, 148)
    result = _jerk(wbase, 23)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_anncurv_126d_jerk_v135_signal(closeadj):
    short = _annmom(closeadj, 21)
    mid = _annmom(closeadj, 63)
    long = _annmom(closeadj, 126)
    base = short + long - 2.0 * mid
    wbase = _wrap_tanh(base, 165)
    result = _jerk(wbase, 30)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_anncurv_252d_jerk_v136_signal(closeadj):
    short = _annmom(closeadj, 21)
    mid = _annmom(closeadj, 63)
    long = _annmom(closeadj, 252)
    base = short + long - 2.0 * mid
    wbase = _wrap_emadisp(base, 182)
    result = _jerk(wbase, 37)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_netflow_63d_jerk_v137_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    up = dv.where(r > 0, 0.0).rolling(63, min_periods=max(1, 63 // 2)).sum()
    dn = dv.where(r < 0, 0.0).rolling(63, min_periods=max(1, 63 // 2)).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    wbase = _wrap_smooth(base, 199)
    result = _jerk(wbase, 44)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_netflow_126d_jerk_v138_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    up = dv.where(r > 0, 0.0).rolling(126, min_periods=max(1, 126 // 2)).sum()
    dn = dv.where(r < 0, 0.0).rolling(126, min_periods=max(1, 126 // 2)).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    wbase = _wrap_raw(base, 216)
    result = _jerk(wbase, 11)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_kst_21d_jerk_v139_signal(closeadj):
    r1 = _roc(closeadj, 21).rolling(21, min_periods=max(1, 21 // 2)).mean()
    r2 = _roc(closeadj, 21 * 2).rolling(21, min_periods=max(1, 21 // 2)).mean()
    base = 1.0 * r1 + 2.0 * r2
    wbase = _wrap_z(base, 233)
    result = _jerk(wbase, 18)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_kst_63d_jerk_v140_signal(closeadj):
    r1 = _roc(closeadj, 63).rolling(63, min_periods=max(1, 63 // 2)).mean()
    r2 = _roc(closeadj, 63 * 2).rolling(63, min_periods=max(1, 63 // 2)).mean()
    base = 1.0 * r1 + 2.0 * r2
    wbase = _wrap_rank(base, 250)
    result = _jerk(wbase, 25)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emacross2_21d_jerk_v141_signal(closeadj):
    fast = closeadj.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    slow = closeadj.ewm(span=21 * 2, min_periods=21).mean()
    cross = fast / slow.replace(0, np.nan) - 1.0
    base = cross - cross.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    wbase = _wrap_tanh(base, 267)
    result = _jerk(wbase, 32)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_emacross2_63d_jerk_v142_signal(closeadj):
    fast = closeadj.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    slow = closeadj.ewm(span=63 * 2, min_periods=63).mean()
    cross = fast / slow.replace(0, np.nan) - 1.0
    base = cross - cross.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    wbase = _wrap_emadisp(base, 44)
    result = _jerk(wbase, 39)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitz_21d_jerk_v143_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    base = _z(hr, 21 * 4)
    wbase = _wrap_smooth(base, 61)
    result = _jerk(wbase, 6)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitz_63d_jerk_v144_signal(closeadj):
    hr = (closeadj.pct_change() > 0).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    base = _z(hr, 63 * 4)
    wbase = _wrap_raw(base, 78)
    result = _jerk(wbase, 13)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logcurv_42d_jerk_v145_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp - 2.0 * lp.shift(42) + lp.shift(42 * 2)
    wbase = _wrap_z(base, 95)
    result = _jerk(wbase, 20)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logcurv_63d_jerk_v146_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp - 2.0 * lp.shift(63) + lp.shift(63 * 2)
    wbase = _wrap_rank(base, 112)
    result = _jerk(wbase, 27)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_micro_21d_jerk_v147_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=max(2, 21 // 2)).skew()
    wbase = _wrap_tanh(base, 129)
    result = _jerk(wbase, 34)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_micro_42d_jerk_v148_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(42, min_periods=max(2, 42 // 2)).skew()
    wbase = _wrap_emadisp(base, 146)
    result = _jerk(wbase, 41)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_yoypers_126d_jerk_v149_signal(closeadj):
    rocn = _roc(closeadj, 126)
    base = np.sign(rocn) * np.sign(rocn.shift(126)) * (rocn.abs() ** 0.5)
    wbase = _wrap_smooth(base, 163)
    result = _jerk(wbase, 8)
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_yoypers_252d_jerk_v150_signal(closeadj):
    rocn = _roc(closeadj, 252)
    base = np.sign(rocn) * np.sign(rocn.shift(252)) * (rocn.abs() ** 0.5)
    wbase = _wrap_raw(base, 180)
    result = _jerk(wbase, 15)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02mr_f02_momentum_rotation_roc_5d_jerk_v001_signal,
    f02mr_f02_momentum_rotation_roc_21d_jerk_v002_signal,
    f02mr_f02_momentum_rotation_roc_63d_jerk_v003_signal,
    f02mr_f02_momentum_rotation_roc_126d_jerk_v004_signal,
    f02mr_f02_momentum_rotation_roc_252d_jerk_v005_signal,
    f02mr_f02_momentum_rotation_logmom_21d_jerk_v006_signal,
    f02mr_f02_momentum_rotation_logmom_63d_jerk_v007_signal,
    f02mr_f02_momentum_rotation_logmom_126d_jerk_v008_signal,
    f02mr_f02_momentum_rotation_logmom_252d_jerk_v009_signal,
    f02mr_f02_momentum_rotation_annmom_21d_jerk_v010_signal,
    f02mr_f02_momentum_rotation_annmom_63d_jerk_v011_signal,
    f02mr_f02_momentum_rotation_annmom_126d_jerk_v012_signal,
    f02mr_f02_momentum_rotation_annmom_252d_jerk_v013_signal,
    f02mr_f02_momentum_rotation_emaprc_10d_jerk_v014_signal,
    f02mr_f02_momentum_rotation_emaprc_21d_jerk_v015_signal,
    f02mr_f02_momentum_rotation_emaprc_63d_jerk_v016_signal,
    f02mr_f02_momentum_rotation_radjmom_21d_jerk_v017_signal,
    f02mr_f02_momentum_rotation_radjmom_63d_jerk_v018_signal,
    f02mr_f02_momentum_rotation_radjmom_126d_jerk_v019_signal,
    f02mr_f02_momentum_rotation_radjmom_252d_jerk_v020_signal,
    f02mr_f02_momentum_rotation_sharpe_21d_jerk_v021_signal,
    f02mr_f02_momentum_rotation_sharpe_63d_jerk_v022_signal,
    f02mr_f02_momentum_rotation_sharpe_126d_jerk_v023_signal,
    f02mr_f02_momentum_rotation_hitrate_21d_jerk_v024_signal,
    f02mr_f02_momentum_rotation_hitrate_63d_jerk_v025_signal,
    f02mr_f02_momentum_rotation_hitrate_126d_jerk_v026_signal,
    f02mr_f02_momentum_rotation_rocrank_21d_jerk_v027_signal,
    f02mr_f02_momentum_rotation_rocrank_63d_jerk_v028_signal,
    f02mr_f02_momentum_rotation_rocrank_126d_jerk_v029_signal,
    f02mr_f02_momentum_rotation_pricez_21d_jerk_v030_signal,
    f02mr_f02_momentum_rotation_pricez_63d_jerk_v031_signal,
    f02mr_f02_momentum_rotation_pricez_126d_jerk_v032_signal,
    f02mr_f02_momentum_rotation_rsi_14d_jerk_v033_signal,
    f02mr_f02_momentum_rotation_rsi_21d_jerk_v034_signal,
    f02mr_f02_momentum_rotation_rsi_63d_jerk_v035_signal,
    f02mr_f02_momentum_rotation_ewmamom_10d_jerk_v036_signal,
    f02mr_f02_momentum_rotation_ewmamom_21d_jerk_v037_signal,
    f02mr_f02_momentum_rotation_ewmamom_63d_jerk_v038_signal,
    f02mr_f02_momentum_rotation_patheff_21d_jerk_v039_signal,
    f02mr_f02_momentum_rotation_patheff_63d_jerk_v040_signal,
    f02mr_f02_momentum_rotation_patheff_126d_jerk_v041_signal,
    f02mr_f02_momentum_rotation_gainloss_21d_jerk_v042_signal,
    f02mr_f02_momentum_rotation_gainloss_63d_jerk_v043_signal,
    f02mr_f02_momentum_rotation_gainloss_126d_jerk_v044_signal,
    f02mr_f02_momentum_rotation_dnfreq_21d_jerk_v045_signal,
    f02mr_f02_momentum_rotation_dnfreq_63d_jerk_v046_signal,
    f02mr_f02_momentum_rotation_dnfreq_126d_jerk_v047_signal,
    f02mr_f02_momentum_rotation_volratio_21d_jerk_v048_signal,
    f02mr_f02_momentum_rotation_volratio_42d_jerk_v049_signal,
    f02mr_f02_momentum_rotation_volratio_63d_jerk_v050_signal,
    f02mr_f02_momentum_rotation_logslopeq_63d_jerk_v051_signal,
    f02mr_f02_momentum_rotation_logslopeq_126d_jerk_v052_signal,
    f02mr_f02_momentum_rotation_logslopeq_252d_jerk_v053_signal,
    f02mr_f02_momentum_rotation_momdisp_126d_jerk_v054_signal,
    f02mr_f02_momentum_rotation_momdisp_252d_jerk_v055_signal,
    f02mr_f02_momentum_rotation_mtspr_63d_jerk_v056_signal,
    f02mr_f02_momentum_rotation_mtspr_126d_jerk_v057_signal,
    f02mr_f02_momentum_rotation_mtspr_252d_jerk_v058_signal,
    f02mr_f02_momentum_rotation_dvwmom_21d_jerk_v059_signal,
    f02mr_f02_momentum_rotation_dvwmom_63d_jerk_v060_signal,
    f02mr_f02_momentum_rotation_dvwmom_126d_jerk_v061_signal,
    f02mr_f02_momentum_rotation_relvol_63d_jerk_v062_signal,
    f02mr_f02_momentum_rotation_relvol_126d_jerk_v063_signal,
    f02mr_f02_momentum_rotation_aroon_21d_jerk_v064_signal,
    f02mr_f02_momentum_rotation_aroon_63d_jerk_v065_signal,
    f02mr_f02_momentum_rotation_aroon_126d_jerk_v066_signal,
    f02mr_f02_momentum_rotation_netupdays_21d_jerk_v067_signal,
    f02mr_f02_momentum_rotation_netupdays_63d_jerk_v068_signal,
    f02mr_f02_momentum_rotation_netupdays_126d_jerk_v069_signal,
    f02mr_f02_momentum_rotation_tanhmom_5d_jerk_v070_signal,
    f02mr_f02_momentum_rotation_tanhmom_21d_jerk_v071_signal,
    f02mr_f02_momentum_rotation_tanhmom_63d_jerk_v072_signal,
    f02mr_f02_momentum_rotation_tanhmom_126d_jerk_v073_signal,
    f02mr_f02_momentum_rotation_sortino_21d_jerk_v074_signal,
    f02mr_f02_momentum_rotation_sortino_63d_jerk_v075_signal,
    f02mr_f02_momentum_rotation_sortino_126d_jerk_v076_signal,
    f02mr_f02_momentum_rotation_retskew_63d_jerk_v077_signal,
    f02mr_f02_momentum_rotation_retskew_126d_jerk_v078_signal,
    f02mr_f02_momentum_rotation_macd_12d_jerk_v079_signal,
    f02mr_f02_momentum_rotation_macd_21d_jerk_v080_signal,
    f02mr_f02_momentum_rotation_macd_63d_jerk_v081_signal,
    f02mr_f02_momentum_rotation_excessmom_63d_jerk_v082_signal,
    f02mr_f02_momentum_rotation_excessmom_126d_jerk_v083_signal,
    f02mr_f02_momentum_rotation_excessmom_252d_jerk_v084_signal,
    f02mr_f02_momentum_rotation_coherence_63d_jerk_v085_signal,
    f02mr_f02_momentum_rotation_coherence_126d_jerk_v086_signal,
    f02mr_f02_momentum_rotation_wgtmom_63d_jerk_v087_signal,
    f02mr_f02_momentum_rotation_wgtmom_126d_jerk_v088_signal,
    f02mr_f02_momentum_rotation_ulcermom_63d_jerk_v089_signal,
    f02mr_f02_momentum_rotation_ulcermom_126d_jerk_v090_signal,
    f02mr_f02_momentum_rotation_dirstrength_21d_jerk_v091_signal,
    f02mr_f02_momentum_rotation_dirstrength_63d_jerk_v092_signal,
    f02mr_f02_momentum_rotation_dirstrength_126d_jerk_v093_signal,
    f02mr_f02_momentum_rotation_momofmom_63d_jerk_v094_signal,
    f02mr_f02_momentum_rotation_momofmom_126d_jerk_v095_signal,
    f02mr_f02_momentum_rotation_momofmom_252d_jerk_v096_signal,
    f02mr_f02_momentum_rotation_zscoremom_21d_jerk_v097_signal,
    f02mr_f02_momentum_rotation_zscoremom_63d_jerk_v098_signal,
    f02mr_f02_momentum_rotation_zscoremom_126d_jerk_v099_signal,
    f02mr_f02_momentum_rotation_consist_63d_jerk_v100_signal,
    f02mr_f02_momentum_rotation_consist_126d_jerk_v101_signal,
    f02mr_f02_momentum_rotation_ewmacross_10d_jerk_v102_signal,
    f02mr_f02_momentum_rotation_ewmacross_21d_jerk_v103_signal,
    f02mr_f02_momentum_rotation_ewmacross_63d_jerk_v104_signal,
    f02mr_f02_momentum_rotation_rocaccel_63d_jerk_v105_signal,
    f02mr_f02_momentum_rotation_rocaccel_126d_jerk_v106_signal,
    f02mr_f02_momentum_rotation_seqmom_63d_jerk_v107_signal,
    f02mr_f02_momentum_rotation_seqmom_126d_jerk_v108_signal,
    f02mr_f02_momentum_rotation_trendresid_63d_jerk_v109_signal,
    f02mr_f02_momentum_rotation_trendresid_126d_jerk_v110_signal,
    f02mr_f02_momentum_rotation_diffuse_126d_jerk_v111_signal,
    f02mr_f02_momentum_rotation_diffuse_252d_jerk_v112_signal,
    f02mr_f02_momentum_rotation_upstreak_63d_jerk_v113_signal,
    f02mr_f02_momentum_rotation_upstreak_126d_jerk_v114_signal,
    f02mr_f02_momentum_rotation_voltgtmom_63d_jerk_v115_signal,
    f02mr_f02_momentum_rotation_voltgtmom_126d_jerk_v116_signal,
    f02mr_f02_momentum_rotation_voltgtmom_252d_jerk_v117_signal,
    f02mr_f02_momentum_rotation_rsdrift_21d_jerk_v118_signal,
    f02mr_f02_momentum_rotation_rsdrift_63d_jerk_v119_signal,
    f02mr_f02_momentum_rotation_impulse_63d_jerk_v120_signal,
    f02mr_f02_momentum_rotation_impulse_126d_jerk_v121_signal,
    f02mr_f02_momentum_rotation_regexcess_63d_jerk_v122_signal,
    f02mr_f02_momentum_rotation_regexcess_126d_jerk_v123_signal,
    f02mr_f02_momentum_rotation_turnmom_63d_jerk_v124_signal,
    f02mr_f02_momentum_rotation_turnmom_126d_jerk_v125_signal,
    f02mr_f02_momentum_rotation_pricezspr_21d_jerk_v126_signal,
    f02mr_f02_momentum_rotation_pricezspr_63d_jerk_v127_signal,
    f02mr_f02_momentum_rotation_tsi_13d_jerk_v128_signal,
    f02mr_f02_momentum_rotation_tsi_21d_jerk_v129_signal,
    f02mr_f02_momentum_rotation_shockz_42d_jerk_v130_signal,
    f02mr_f02_momentum_rotation_shockz_63d_jerk_v131_signal,
    f02mr_f02_momentum_rotation_shockz_126d_jerk_v132_signal,
    f02mr_f02_momentum_rotation_rankvel_63d_jerk_v133_signal,
    f02mr_f02_momentum_rotation_rankvel_126d_jerk_v134_signal,
    f02mr_f02_momentum_rotation_anncurv_126d_jerk_v135_signal,
    f02mr_f02_momentum_rotation_anncurv_252d_jerk_v136_signal,
    f02mr_f02_momentum_rotation_netflow_63d_jerk_v137_signal,
    f02mr_f02_momentum_rotation_netflow_126d_jerk_v138_signal,
    f02mr_f02_momentum_rotation_kst_21d_jerk_v139_signal,
    f02mr_f02_momentum_rotation_kst_63d_jerk_v140_signal,
    f02mr_f02_momentum_rotation_emacross2_21d_jerk_v141_signal,
    f02mr_f02_momentum_rotation_emacross2_63d_jerk_v142_signal,
    f02mr_f02_momentum_rotation_hitz_21d_jerk_v143_signal,
    f02mr_f02_momentum_rotation_hitz_63d_jerk_v144_signal,
    f02mr_f02_momentum_rotation_logcurv_42d_jerk_v145_signal,
    f02mr_f02_momentum_rotation_logcurv_63d_jerk_v146_signal,
    f02mr_f02_momentum_rotation_micro_21d_jerk_v147_signal,
    f02mr_f02_momentum_rotation_micro_42d_jerk_v148_signal,
    f02mr_f02_momentum_rotation_yoypers_126d_jerk_v149_signal,
    f02mr_f02_momentum_rotation_yoypers_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_001_150 = REGISTRY


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

    print("OK f02_momentum_rotation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
