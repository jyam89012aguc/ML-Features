import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mp(w):
    return max(2, w // 3)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _Rmed(s, w):
    return s.rolling(w, min_periods=_mp(w)).median()


def _Rstd(s, w):
    return s.rolling(w, min_periods=_mp(w)).std()


def _Rmean(s, w):
    return s.rolling(w, min_periods=_mp(w)).mean()


def _Rmax(s, w):
    return s.rolling(w, min_periods=_mp(w)).max()


def _Rmin(s, w):
    return s.rolling(w, min_periods=_mp(w)).min()


def _Rsum(s, w):
    return s.rolling(w, min_periods=_mp(w)).sum()


def _Rvar(s, w):
    return s.rolling(w, min_periods=_mp(w)).var()


def _Rskew(s, w):
    return s.rolling(w, min_periods=_mp(w)).skew()


def _Rkurt(s, w):
    return s.rolling(w, min_periods=_mp(w)).kurt()


def _Rq(s, w, q):
    return s.rolling(w, min_periods=_mp(w)).quantile(q)


def _dv(closeadj, volume):
    return closeadj * volume


def _logdv(closeadj, volume):
    return np.log((closeadj * volume).replace(0, np.nan))


def _tier(closeadj, volume, w):
    return _Rmean(np.log((closeadj * volume).replace(0, np.nan)), w)


def f17dv_f17_dollar_volume_dynamics_logdvlvl_63d_jerk_v001_signal(closeadj, volume):
    base = _tier(closeadj, volume, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_logdvlvl_126d_jerk_v002_signal(closeadj, volume):
    base = _tier(closeadj, volume, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_logdvlvl_252d_jerk_v003_signal(closeadj, volume):
    base = _tier(closeadj, volume, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_logdvz_63d_jerk_v004_signal(closeadj, volume):
    base = _z(_logdv(closeadj, volume), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_logdvz_126d_jerk_v005_signal(closeadj, volume):
    base = _z(_logdv(closeadj, volume), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_logdvz_252d_jerk_v006_signal(closeadj, volume):
    base = _z(_logdv(closeadj, volume), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvautocorr_63d_jerk_v007_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); lag = ldv.shift(1)
    cov = _Rmean(ldv * lag, 63) - _Rmean(ldv, 63) * _Rmean(lag, 63)
    base = cov / np.sqrt(_Rvar(ldv, 63) * _Rvar(lag, 63)).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvautocorr_126d_jerk_v008_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); lag = ldv.shift(1)
    cov = _Rmean(ldv * lag, 126) - _Rmean(ldv, 126) * _Rmean(lag, 126)
    base = cov / np.sqrt(_Rvar(ldv, 126) * _Rvar(lag, 126)).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvautocorr_252d_jerk_v009_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); lag = ldv.shift(1)
    cov = _Rmean(ldv * lag, 252) - _Rmean(ldv, 252) * _Rmean(lag, 252)
    base = cov / np.sqrt(_Rvar(ldv, 252) * _Rvar(lag, 252)).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_regdist_63d_jerk_v010_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rmean(ldv, 21) - _Rmed(ldv, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_regdist_126d_jerk_v011_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rmean(ldv, 21) - _Rmed(ldv, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_regdist_252d_jerk_v012_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rmean(ldv, 21) - _Rmed(ldv, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvdd_63d_jerk_v013_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = sm / _Rmax(sm, 63).replace(0, np.nan) - 1.0
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvdd_126d_jerk_v014_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = sm / _Rmax(sm, 126).replace(0, np.nan) - 1.0
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvdd_252d_jerk_v015_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = sm / _Rmax(sm, 252).replace(0, np.nan) - 1.0
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrecov_63d_jerk_v016_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = np.log(sm.replace(0, np.nan) / _Rmin(sm, 63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrecov_126d_jerk_v017_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = np.log(sm.replace(0, np.nan) / _Rmin(sm, 126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrecov_252d_jerk_v018_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    base = np.log(sm.replace(0, np.nan) / _Rmin(sm, 252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierpos_63d_jerk_v019_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21); hi = _Rmax(lvl, 63); lo = _Rmin(lvl, 63)
    base = (lvl - lo) / (hi - lo).replace(0, np.nan) - 0.5
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierpos_126d_jerk_v020_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21); hi = _Rmax(lvl, 126); lo = _Rmin(lvl, 126)
    base = (lvl - lo) / (hi - lo).replace(0, np.nan) - 0.5
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierpos_252d_jerk_v021_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21); hi = _Rmax(lvl, 252); lo = _Rmin(lvl, 252)
    base = (lvl - lo) / (hi - lo).replace(0, np.nan) - 0.5
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierfloor_63d_jerk_v022_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = lvl - _Rmin(lvl, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierfloor_126d_jerk_v023_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = lvl - _Rmin(lvl, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierfloor_252d_jerk_v024_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = lvl - _Rmin(lvl, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_spikemag_63d_jerk_v025_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmean(np.log(dv.replace(0, np.nan) / _Rmed(dv, 63).replace(0, np.nan)), 10)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_spikemag_126d_jerk_v026_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmean(np.log(dv.replace(0, np.nan) / _Rmed(dv, 126).replace(0, np.nan)), 10)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_spikemag_252d_jerk_v027_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmean(np.log(dv.replace(0, np.nan) / _Rmed(dv, 252).replace(0, np.nan)), 10)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvconc_63d_jerk_v028_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmax(dv, 63) / _Rsum(dv, 63).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvconc_126d_jerk_v029_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmax(dv, 126) / _Rsum(dv, 126).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvconc_252d_jerk_v030_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    base = _Rmax(dv, 252) / _Rsum(dv, 252).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhhi_63d_jerk_v031_signal(closeadj, volume):
    dv = _dv(closeadj, volume); tot = _Rsum(dv, 63)
    base = _Rsum(dv * dv, 63) / (tot * tot).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhhi_126d_jerk_v032_signal(closeadj, volume):
    dv = _dv(closeadj, volume); tot = _Rsum(dv, 126)
    base = _Rsum(dv * dv, 126) / (tot * tot).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhhi_252d_jerk_v033_signal(closeadj, volume):
    dv = _dv(closeadj, volume); tot = _Rsum(dv, 252)
    base = _Rsum(dv * dv, 252) / (tot * tot).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqcd_63d_jerk_v034_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 63, 0.75); q25 = _Rq(dv, 63, 0.25)
    base = (q75 - q25) / (q75 + q25).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqcd_126d_jerk_v035_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 126, 0.75); q25 = _Rq(dv, 126, 0.25)
    base = (q75 - q25) / (q75 + q25).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqcd_252d_jerk_v036_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 252, 0.75); q25 = _Rq(dv, 252, 0.25)
    base = (q75 - q25) / (q75 + q25).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvturb_63d_jerk_v037_signal(closeadj, volume):
    base = _Rstd(_logdv(closeadj, volume).diff(), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvturb_126d_jerk_v038_signal(closeadj, volume):
    base = _Rstd(_logdv(closeadj, volume).diff(), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvturb_252d_jerk_v039_signal(closeadj, volume):
    base = _Rstd(_logdv(closeadj, volume).diff(), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvimbal_63d_jerk_v040_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    up = _Rsum(dv.where(ret > 0, 0.0), 63); dn = _Rsum(dv.where(ret < 0, 0.0), 63)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvimbal_126d_jerk_v041_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    up = _Rsum(dv.where(ret > 0, 0.0), 126); dn = _Rsum(dv.where(ret < 0, 0.0), 126)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvimbal_252d_jerk_v042_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    up = _Rsum(dv.where(ret > 0, 0.0), 252); dn = _Rsum(dv.where(ret < 0, 0.0), 252)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_signedflow_63d_jerk_v043_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    base = _Rsum(ret * dv, 63) / _Rsum(dv, 63).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_signedflow_126d_jerk_v044_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    base = _Rsum(ret * dv, 126) / _Rsum(dv, 126).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_signedflow_252d_jerk_v045_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    base = _Rsum(ret * dv, 252) / _Rsum(dv, 252).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthlvl_63d_jerk_v046_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = np.log(_Rmean(depth, 63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthlvl_126d_jerk_v047_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = np.log(_Rmean(depth, 126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthlvl_252d_jerk_v048_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = np.log(_Rmean(depth, 252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rangedv_63d_jerk_v049_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = np.log(_Rmean(rdv, 63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rangedv_126d_jerk_v050_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = np.log(_Rmean(rdv, 126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rangedv_252d_jerk_v051_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = np.log(_Rmean(rdv, 252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tailspread_63d_jerk_v052_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rq(ldv, 63, 0.90) - _Rq(ldv, 63, 0.50)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tailspread_126d_jerk_v053_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rq(ldv, 126, 0.90) - _Rq(ldv, 126, 0.50)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tailspread_252d_jerk_v054_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rq(ldv, 252, 0.90) - _Rq(ldv, 252, 0.50)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpriceshare_63d_jerk_v055_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _Rstd(np.log(depth.replace(0, np.nan)), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpriceshare_126d_jerk_v056_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _Rstd(np.log(depth.replace(0, np.nan)), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpriceshare_252d_jerk_v057_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _Rstd(np.log(depth.replace(0, np.nan)), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvspan_63d_jerk_v058_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    base = np.log(_Rmax(sm, 63).replace(0, np.nan) / _Rmin(sm, 63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvspan_126d_jerk_v059_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    base = np.log(_Rmax(sm, 126).replace(0, np.nan) / _Rmin(sm, 126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvspan_252d_jerk_v060_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    base = np.log(_Rmax(sm, 252).replace(0, np.nan) / _Rmin(sm, 252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_emadisp_63d_jerk_v061_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = ldv.ewm(span=max(5, 63 // 6), min_periods=5).mean() - ldv.ewm(span=63, min_periods=_mp(63)).mean()
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_emadisp_126d_jerk_v062_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = ldv.ewm(span=max(5, 126 // 6), min_periods=5).mean() - ldv.ewm(span=126, min_periods=_mp(126)).mean()
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_emadisp_252d_jerk_v063_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = ldv.ewm(span=max(5, 252 // 6), min_periods=5).mean() - ldv.ewm(span=252, min_periods=_mp(252)).mean()
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveff_63d_jerk_v064_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(63)).abs() / _Rsum(ldv.diff().abs(), 63).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveff_126d_jerk_v065_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(126)).abs() / _Rsum(ldv.diff().abs(), 126).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveff_252d_jerk_v066_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(252)).abs() / _Rsum(ldv.diff().abs(), 252).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_updisp_63d_jerk_v067_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg > 0, np.nan), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_updisp_126d_jerk_v068_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg > 0, np.nan), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_updisp_252d_jerk_v069_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg > 0, np.nan), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_surprisemag_63d_jerk_v070_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ratio = dv / _Rmed(dv, 63).replace(0, np.nan)
    base = _Rsum((ratio - 1.0).clip(lower=0), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_surprisemag_126d_jerk_v071_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ratio = dv / _Rmed(dv, 63).replace(0, np.nan)
    base = _Rsum((ratio - 1.0).clip(lower=0), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_surprisemag_252d_jerk_v072_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ratio = dv / _Rmed(dv, 63).replace(0, np.nan)
    base = _Rsum((ratio - 1.0).clip(lower=0), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvskew_63d_jerk_v073_signal(closeadj, volume):
    base = _Rskew(_logdv(closeadj, volume).diff(), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvskew_126d_jerk_v074_signal(closeadj, volume):
    base = _Rskew(_logdv(closeadj, volume).diff(), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvskew_252d_jerk_v075_signal(closeadj, volume):
    base = _Rskew(_logdv(closeadj, volume).diff(), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtilt_63d_jerk_v076_signal(closeadj, volume):
    dv = _dv(closeadj, volume); h = max(5, 63 // 2)
    recent = _Rsum(dv, h); older = _Rsum(dv.shift(h), h)
    base = (recent - older) / (recent + older).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtilt_126d_jerk_v077_signal(closeadj, volume):
    dv = _dv(closeadj, volume); h = max(5, 126 // 2)
    recent = _Rsum(dv, h); older = _Rsum(dv.shift(h), h)
    base = (recent - older) / (recent + older).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtilt_252d_jerk_v078_signal(closeadj, volume):
    dv = _dv(closeadj, volume); h = max(5, 252 // 2)
    recent = _Rsum(dv, h); older = _Rsum(dv.shift(h), h)
    base = (recent - older) / (recent + older).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtoggle_63d_jerk_v079_signal(closeadj, volume):
    dv = _dv(closeadj, volume); above = (dv > _Rmed(dv, 21)).astype(float)
    base = _Rmean((above != above.shift(1)).astype(float), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtoggle_126d_jerk_v080_signal(closeadj, volume):
    dv = _dv(closeadj, volume); above = (dv > _Rmed(dv, 21)).astype(float)
    base = _Rmean((above != above.shift(1)).astype(float), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtoggle_252d_jerk_v081_signal(closeadj, volume):
    dv = _dv(closeadj, volume); above = (dv > _Rmed(dv, 21)).astype(float)
    base = _Rmean((above != above.shift(1)).astype(float), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvcomove_63d_jerk_v082_signal(closeadj, volume):
    aret = closeadj.pct_change().abs(); dldv = _logdv(closeadj, volume).diff()
    cov = _Rmean(aret * dldv, 63) - _Rmean(aret, 63) * _Rmean(dldv, 63)
    base = cov / np.sqrt(_Rvar(aret, 63) * _Rvar(dldv, 63)).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvcomove_126d_jerk_v083_signal(closeadj, volume):
    aret = closeadj.pct_change().abs(); dldv = _logdv(closeadj, volume).diff()
    cov = _Rmean(aret * dldv, 126) - _Rmean(aret, 126) * _Rmean(dldv, 126)
    base = cov / np.sqrt(_Rvar(aret, 126) * _Rvar(dldv, 126)).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvcomove_252d_jerk_v084_signal(closeadj, volume):
    aret = closeadj.pct_change().abs(); dldv = _logdv(closeadj, volume).diff()
    cov = _Rmean(aret * dldv, 252) - _Rmean(aret, 252) * _Rmean(dldv, 252)
    base = cov / np.sqrt(_Rvar(aret, 252) * _Rvar(dldv, 252)).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierwidth_63d_jerk_v085_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = _Rmax(lvl, 63) - _Rmin(lvl, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierwidth_126d_jerk_v086_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = _Rmax(lvl, 126) - _Rmin(lvl, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierwidth_252d_jerk_v087_signal(closeadj, volume):
    lvl = _tier(closeadj, volume, 21)
    base = _Rmax(lvl, 252) - _Rmin(lvl, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvkurt_63d_jerk_v088_signal(closeadj, volume):
    base = _Rkurt(_logdv(closeadj, volume).diff(), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvkurt_126d_jerk_v089_signal(closeadj, volume):
    base = _Rkurt(_logdv(closeadj, volume).diff(), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvkurt_252d_jerk_v090_signal(closeadj, volume):
    base = _Rkurt(_logdv(closeadj, volume).diff(), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dsdvpeak_63d_jerk_v091_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = sm.rolling(63, min_periods=_mp(63)).apply(_f, raw=True)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dsdvpeak_126d_jerk_v092_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = sm.rolling(126, min_periods=_mp(126)).apply(_f, raw=True)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dsdvpeak_252d_jerk_v093_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5)
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = sm.rolling(252, min_periods=_mp(252)).apply(_f, raw=True)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthz_63d_jerk_v094_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _z(_Rmean(np.log(depth.replace(0, np.nan)), 5), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthz_126d_jerk_v095_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _z(_Rmean(np.log(depth.replace(0, np.nan)), 5), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_depthz_252d_jerk_v096_signal(closeadj, volume, high, low):
    depth = _dv(closeadj, volume) / (high - low).replace(0, np.nan)
    base = _z(_Rmean(np.log(depth.replace(0, np.nan)), 5), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvperpct_63d_jerk_v097_signal(closeadj, volume, high, low):
    dpp = np.log((_dv(closeadj, volume) / ((high - low) / closeadj.replace(0, np.nan)).replace(0, np.nan)).replace(0, np.nan))
    base = _Rmean(dpp, 21) - _Rmed(dpp, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvperpct_126d_jerk_v098_signal(closeadj, volume, high, low):
    dpp = np.log((_dv(closeadj, volume) / ((high - low) / closeadj.replace(0, np.nan)).replace(0, np.nan)).replace(0, np.nan))
    base = _Rmean(dpp, 21) - _Rmed(dpp, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvperpct_252d_jerk_v099_signal(closeadj, volume, high, low):
    dpp = np.log((_dv(closeadj, volume) / ((high - low) / closeadj.replace(0, np.nan)).replace(0, np.nan)).replace(0, np.nan))
    base = _Rmean(dpp, 21) - _Rmed(dpp, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_flowtilt_63d_jerk_v100_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    wavg = _Rsum(ret * dv, 63) / _Rsum(dv, 63).replace(0, np.nan)
    base = wavg - _Rmean(ret, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_flowtilt_126d_jerk_v101_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    wavg = _Rsum(ret * dv, 126) / _Rsum(dv, 126).replace(0, np.nan)
    base = wavg - _Rmean(ret, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_flowtilt_252d_jerk_v102_signal(closeadj, volume):
    dv = _dv(closeadj, volume); ret = closeadj.pct_change()
    wavg = _Rsum(ret * dv, 252) / _Rsum(dv, 252).replace(0, np.nan)
    base = wavg - _Rmean(ret, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtrendsl_63d_jerk_v103_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(63)) / float(63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtrendsl_126d_jerk_v104_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(126)) / float(126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtrendsl_252d_jerk_v105_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5)
    base = (ldv - ldv.shift(252)) / float(252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvretvol_63d_jerk_v106_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5); hi = _Rmax(sm, 63); lo = _Rmin(sm, 63)
    base = (sm - lo) / (hi - lo).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvretvol_126d_jerk_v107_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5); hi = _Rmax(sm, 126); lo = _Rmin(sm, 126)
    base = (sm - lo) / (hi - lo).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvretvol_252d_jerk_v108_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 5); hi = _Rmax(sm, 252); lo = _Rmin(sm, 252)
    base = (sm - lo) / (hi - lo).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierinstab_63d_jerk_v109_signal(closeadj, volume):
    base = _Rstd(_tier(closeadj, volume, 21), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierinstab_126d_jerk_v110_signal(closeadj, volume):
    base = _Rstd(_tier(closeadj, volume, 21), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_tierinstab_252d_jerk_v111_signal(closeadj, volume):
    base = _Rstd(_tier(closeadj, volume, 21), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvvr_63d_jerk_v112_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rvar(ldv.diff(5), 63) / (5.0 * _Rvar(ldv.diff(), 63)).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvvr_126d_jerk_v113_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rvar(ldv.diff(5), 126) / (5.0 * _Rvar(ldv.diff(), 126)).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvvr_252d_jerk_v114_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume)
    base = _Rvar(ldv.diff(5), 252) / (5.0 * _Rvar(ldv.diff(), 252)).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvmad_63d_jerk_v115_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); med = _Rmed(ldv, 63)
    base = _Rmean((ldv - med).abs(), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvmad_126d_jerk_v116_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); med = _Rmed(ldv, 126)
    base = _Rmean((ldv - med).abs(), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvmad_252d_jerk_v117_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); med = _Rmed(ldv, 252)
    base = _Rmean((ldv - med).abs(), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveffsh_63d_jerk_v118_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5); k = max(10, 63 // 4)
    base = (ldv - ldv.shift(k)).abs() / ldv.diff().abs().rolling(k, min_periods=5).sum().replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveffsh_126d_jerk_v119_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5); k = max(10, 126 // 4)
    base = (ldv - ldv.shift(k)).abs() / ldv.diff().abs().rolling(k, min_periods=5).sum().replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dveffsh_252d_jerk_v120_signal(closeadj, volume):
    ldv = _Rmean(_logdv(closeadj, volume), 5); k = max(10, 252 // 4)
    base = (ldv - ldv.shift(k)).abs() / ldv.diff().abs().rolling(k, min_periods=5).sum().replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_elevfrac_63d_jerk_v121_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 252, 0.75)
    base = _Rmean((dv / q75.replace(0, np.nan) - 1.0).clip(lower=0), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_elevfrac_126d_jerk_v122_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 252, 0.75)
    base = _Rmean((dv / q75.replace(0, np.nan) - 1.0).clip(lower=0), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_elevfrac_252d_jerk_v123_signal(closeadj, volume):
    dv = _dv(closeadj, volume); q75 = _Rq(dv, 252, 0.75)
    base = _Rmean((dv / q75.replace(0, np.nan) - 1.0).clip(lower=0), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dndisp_63d_jerk_v124_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg < 0, np.nan), 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dndisp_126d_jerk_v125_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg < 0, np.nan), 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dndisp_252d_jerk_v126_signal(closeadj, volume):
    chg = _logdv(closeadj, volume).diff()
    base = _Rstd(chg.where(chg < 0, np.nan), 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtotgrow_63d_jerk_v127_signal(closeadj, volume):
    tot = _Rsum(_dv(closeadj, volume), 63)
    base = np.log(tot.replace(0, np.nan) / tot.shift(63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtotgrow_126d_jerk_v128_signal(closeadj, volume):
    tot = _Rsum(_dv(closeadj, volume), 126)
    base = np.log(tot.replace(0, np.nan) / tot.shift(126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvtotgrow_252d_jerk_v129_signal(closeadj, volume):
    tot = _Rsum(_dv(closeadj, volume), 252)
    base = np.log(tot.replace(0, np.nan) / tot.shift(252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_top3share_63d_jerk_v130_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    def _f(a):
        s = np.sort(a)[-3:].sum(); tot = a.sum()
        return s / tot if tot > 0 else np.nan
    base = dv.rolling(63, min_periods=_mp(63)).apply(_f, raw=True)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_top3share_126d_jerk_v131_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    def _f(a):
        s = np.sort(a)[-3:].sum(); tot = a.sum()
        return s / tot if tot > 0 else np.nan
    base = dv.rolling(126, min_periods=_mp(126)).apply(_f, raw=True)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_top3share_252d_jerk_v132_signal(closeadj, volume):
    dv = _dv(closeadj, volume)
    def _f(a):
        s = np.sort(a)[-3:].sum(); tot = a.sum()
        return s / tot if tot > 0 else np.nan
    base = dv.rolling(252, min_periods=_mp(252)).apply(_f, raw=True)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_monthvspeak_63d_jerk_v133_signal(closeadj, volume):
    m21 = _Rsum(_dv(closeadj, volume), 21)
    base = np.log(m21.replace(0, np.nan) / _Rmax(m21, 63).replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_monthvspeak_126d_jerk_v134_signal(closeadj, volume):
    m21 = _Rsum(_dv(closeadj, volume), 21)
    base = np.log(m21.replace(0, np.nan) / _Rmax(m21, 126).replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_monthvspeak_252d_jerk_v135_signal(closeadj, volume):
    m21 = _Rsum(_dv(closeadj, volume), 21)
    base = np.log(m21.replace(0, np.nan) / _Rmax(m21, 252).replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrangecorr_63d_jerk_v136_signal(closeadj, volume, high, low):
    ldv = _logdv(closeadj, volume); lrng = np.log((high - low).replace(0, np.nan))
    cov = _Rmean(ldv * lrng, 63) - _Rmean(ldv, 63) * _Rmean(lrng, 63)
    base = cov / np.sqrt(_Rvar(ldv, 63) * _Rvar(lrng, 63)).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrangecorr_126d_jerk_v137_signal(closeadj, volume, high, low):
    ldv = _logdv(closeadj, volume); lrng = np.log((high - low).replace(0, np.nan))
    cov = _Rmean(ldv * lrng, 126) - _Rmean(ldv, 126) * _Rmean(lrng, 126)
    base = cov / np.sqrt(_Rvar(ldv, 126) * _Rvar(lrng, 126)).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvrangecorr_252d_jerk_v138_signal(closeadj, volume, high, low):
    ldv = _logdv(closeadj, volume); lrng = np.log((high - low).replace(0, np.nan))
    cov = _Rmean(ldv * lrng, 252) - _Rmean(ldv, 252) * _Rmean(lrng, 252)
    base = cov / np.sqrt(_Rvar(ldv, 252) * _Rvar(lrng, 252)).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhilo_63d_jerk_v139_signal(closeadj, volume):
    dv = _dv(closeadj, volume); med = _Rmed(dv, 63)
    hi = _Rmean(dv.where(dv > med, np.nan), 63); lo = _Rmean(dv.where(dv <= med, np.nan), 63)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhilo_126d_jerk_v140_signal(closeadj, volume):
    dv = _dv(closeadj, volume); med = _Rmed(dv, 126)
    hi = _Rmean(dv.where(dv > med, np.nan), 126); lo = _Rmean(dv.where(dv <= med, np.nan), 126)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvhilo_252d_jerk_v141_signal(closeadj, volume):
    dv = _dv(closeadj, volume); med = _Rmed(dv, 252)
    hi = _Rmean(dv.where(dv > med, np.nan), 252); lo = _Rmean(dv.where(dv <= med, np.nan), 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpain_63d_jerk_v142_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    dd = sm / _Rmax(sm, 63).replace(0, np.nan) - 1.0
    base = _Rmean(dd, 63)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpain_126d_jerk_v143_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    dd = sm / _Rmax(sm, 126).replace(0, np.nan) - 1.0
    base = _Rmean(dd, 126)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvpain_252d_jerk_v144_signal(closeadj, volume):
    sm = _Rmean(_dv(closeadj, volume), 10)
    dd = sm / _Rmax(sm, 252).replace(0, np.nan) - 1.0
    base = _Rmean(dd, 252)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rwconc_63d_jerk_v145_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = _Rmax(rdv, 63) / _Rsum(rdv, 63).replace(0, np.nan)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rwconc_126d_jerk_v146_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = _Rmax(rdv, 126) / _Rsum(rdv, 126).replace(0, np.nan)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_rwconc_252d_jerk_v147_signal(closeadj, volume, high, low):
    rdv = (closeadj * volume) * ((high - low) / low.replace(0, np.nan))
    base = _Rmax(rdv, 252) / _Rsum(rdv, 252).replace(0, np.nan)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqusk_63d_jerk_v148_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); q90 = _Rq(ldv, 63, 0.90); q50 = _Rq(ldv, 63, 0.50); q10 = _Rq(ldv, 63, 0.10)
    base = (q90 - q50) - (q50 - q10)
    pb = base
    d1 = pb - pb.shift(10)
    result = d1 - d1.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqusk_126d_jerk_v149_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); q90 = _Rq(ldv, 126, 0.90); q50 = _Rq(ldv, 126, 0.50); q10 = _Rq(ldv, 126, 0.10)
    base = (q90 - q50) - (q50 - q10)
    pb = base.rolling(126, min_periods=42).rank(pct=True) - 0.5
    d1 = pb - pb.shift(21)
    result = d1 - d1.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f17dv_f17_dollar_volume_dynamics_dvqusk_252d_jerk_v150_signal(closeadj, volume):
    ldv = _logdv(closeadj, volume); q90 = _Rq(ldv, 252, 0.90); q50 = _Rq(ldv, 252, 0.50); q10 = _Rq(ldv, 252, 0.10)
    base = (q90 - q50) - (q50 - q10)
    g = base - base.ewm(span=63, min_periods=21).mean()
    pb = np.sign(g) * (g.abs() ** 0.5)
    d1 = pb - pb.shift(42)
    result = d1 - d1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17dv_f17_dollar_volume_dynamics_logdvlvl_63d_jerk_v001_signal,
    f17dv_f17_dollar_volume_dynamics_logdvlvl_126d_jerk_v002_signal,
    f17dv_f17_dollar_volume_dynamics_logdvlvl_252d_jerk_v003_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_63d_jerk_v004_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_126d_jerk_v005_signal,
    f17dv_f17_dollar_volume_dynamics_logdvz_252d_jerk_v006_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr_63d_jerk_v007_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr_126d_jerk_v008_signal,
    f17dv_f17_dollar_volume_dynamics_dvautocorr_252d_jerk_v009_signal,
    f17dv_f17_dollar_volume_dynamics_regdist_63d_jerk_v010_signal,
    f17dv_f17_dollar_volume_dynamics_regdist_126d_jerk_v011_signal,
    f17dv_f17_dollar_volume_dynamics_regdist_252d_jerk_v012_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_63d_jerk_v013_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_126d_jerk_v014_signal,
    f17dv_f17_dollar_volume_dynamics_dvdd_252d_jerk_v015_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecov_63d_jerk_v016_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecov_126d_jerk_v017_signal,
    f17dv_f17_dollar_volume_dynamics_dvrecov_252d_jerk_v018_signal,
    f17dv_f17_dollar_volume_dynamics_tierpos_63d_jerk_v019_signal,
    f17dv_f17_dollar_volume_dynamics_tierpos_126d_jerk_v020_signal,
    f17dv_f17_dollar_volume_dynamics_tierpos_252d_jerk_v021_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor_63d_jerk_v022_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor_126d_jerk_v023_signal,
    f17dv_f17_dollar_volume_dynamics_tierfloor_252d_jerk_v024_signal,
    f17dv_f17_dollar_volume_dynamics_spikemag_63d_jerk_v025_signal,
    f17dv_f17_dollar_volume_dynamics_spikemag_126d_jerk_v026_signal,
    f17dv_f17_dollar_volume_dynamics_spikemag_252d_jerk_v027_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_63d_jerk_v028_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_126d_jerk_v029_signal,
    f17dv_f17_dollar_volume_dynamics_dvconc_252d_jerk_v030_signal,
    f17dv_f17_dollar_volume_dynamics_dvhhi_63d_jerk_v031_signal,
    f17dv_f17_dollar_volume_dynamics_dvhhi_126d_jerk_v032_signal,
    f17dv_f17_dollar_volume_dynamics_dvhhi_252d_jerk_v033_signal,
    f17dv_f17_dollar_volume_dynamics_dvqcd_63d_jerk_v034_signal,
    f17dv_f17_dollar_volume_dynamics_dvqcd_126d_jerk_v035_signal,
    f17dv_f17_dollar_volume_dynamics_dvqcd_252d_jerk_v036_signal,
    f17dv_f17_dollar_volume_dynamics_dvturb_63d_jerk_v037_signal,
    f17dv_f17_dollar_volume_dynamics_dvturb_126d_jerk_v038_signal,
    f17dv_f17_dollar_volume_dynamics_dvturb_252d_jerk_v039_signal,
    f17dv_f17_dollar_volume_dynamics_dvimbal_63d_jerk_v040_signal,
    f17dv_f17_dollar_volume_dynamics_dvimbal_126d_jerk_v041_signal,
    f17dv_f17_dollar_volume_dynamics_dvimbal_252d_jerk_v042_signal,
    f17dv_f17_dollar_volume_dynamics_signedflow_63d_jerk_v043_signal,
    f17dv_f17_dollar_volume_dynamics_signedflow_126d_jerk_v044_signal,
    f17dv_f17_dollar_volume_dynamics_signedflow_252d_jerk_v045_signal,
    f17dv_f17_dollar_volume_dynamics_depthlvl_63d_jerk_v046_signal,
    f17dv_f17_dollar_volume_dynamics_depthlvl_126d_jerk_v047_signal,
    f17dv_f17_dollar_volume_dynamics_depthlvl_252d_jerk_v048_signal,
    f17dv_f17_dollar_volume_dynamics_rangedv_63d_jerk_v049_signal,
    f17dv_f17_dollar_volume_dynamics_rangedv_126d_jerk_v050_signal,
    f17dv_f17_dollar_volume_dynamics_rangedv_252d_jerk_v051_signal,
    f17dv_f17_dollar_volume_dynamics_tailspread_63d_jerk_v052_signal,
    f17dv_f17_dollar_volume_dynamics_tailspread_126d_jerk_v053_signal,
    f17dv_f17_dollar_volume_dynamics_tailspread_252d_jerk_v054_signal,
    f17dv_f17_dollar_volume_dynamics_dvpriceshare_63d_jerk_v055_signal,
    f17dv_f17_dollar_volume_dynamics_dvpriceshare_126d_jerk_v056_signal,
    f17dv_f17_dollar_volume_dynamics_dvpriceshare_252d_jerk_v057_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_63d_jerk_v058_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_126d_jerk_v059_signal,
    f17dv_f17_dollar_volume_dynamics_dvspan_252d_jerk_v060_signal,
    f17dv_f17_dollar_volume_dynamics_emadisp_63d_jerk_v061_signal,
    f17dv_f17_dollar_volume_dynamics_emadisp_126d_jerk_v062_signal,
    f17dv_f17_dollar_volume_dynamics_emadisp_252d_jerk_v063_signal,
    f17dv_f17_dollar_volume_dynamics_dveff_63d_jerk_v064_signal,
    f17dv_f17_dollar_volume_dynamics_dveff_126d_jerk_v065_signal,
    f17dv_f17_dollar_volume_dynamics_dveff_252d_jerk_v066_signal,
    f17dv_f17_dollar_volume_dynamics_updisp_63d_jerk_v067_signal,
    f17dv_f17_dollar_volume_dynamics_updisp_126d_jerk_v068_signal,
    f17dv_f17_dollar_volume_dynamics_updisp_252d_jerk_v069_signal,
    f17dv_f17_dollar_volume_dynamics_surprisemag_63d_jerk_v070_signal,
    f17dv_f17_dollar_volume_dynamics_surprisemag_126d_jerk_v071_signal,
    f17dv_f17_dollar_volume_dynamics_surprisemag_252d_jerk_v072_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew_63d_jerk_v073_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew_126d_jerk_v074_signal,
    f17dv_f17_dollar_volume_dynamics_dvskew_252d_jerk_v075_signal,
    f17dv_f17_dollar_volume_dynamics_dvtilt_63d_jerk_v076_signal,
    f17dv_f17_dollar_volume_dynamics_dvtilt_126d_jerk_v077_signal,
    f17dv_f17_dollar_volume_dynamics_dvtilt_252d_jerk_v078_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoggle_63d_jerk_v079_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoggle_126d_jerk_v080_signal,
    f17dv_f17_dollar_volume_dynamics_dvtoggle_252d_jerk_v081_signal,
    f17dv_f17_dollar_volume_dynamics_dvcomove_63d_jerk_v082_signal,
    f17dv_f17_dollar_volume_dynamics_dvcomove_126d_jerk_v083_signal,
    f17dv_f17_dollar_volume_dynamics_dvcomove_252d_jerk_v084_signal,
    f17dv_f17_dollar_volume_dynamics_tierwidth_63d_jerk_v085_signal,
    f17dv_f17_dollar_volume_dynamics_tierwidth_126d_jerk_v086_signal,
    f17dv_f17_dollar_volume_dynamics_tierwidth_252d_jerk_v087_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt_63d_jerk_v088_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt_126d_jerk_v089_signal,
    f17dv_f17_dollar_volume_dynamics_dvkurt_252d_jerk_v090_signal,
    f17dv_f17_dollar_volume_dynamics_dsdvpeak_63d_jerk_v091_signal,
    f17dv_f17_dollar_volume_dynamics_dsdvpeak_126d_jerk_v092_signal,
    f17dv_f17_dollar_volume_dynamics_dsdvpeak_252d_jerk_v093_signal,
    f17dv_f17_dollar_volume_dynamics_depthz_63d_jerk_v094_signal,
    f17dv_f17_dollar_volume_dynamics_depthz_126d_jerk_v095_signal,
    f17dv_f17_dollar_volume_dynamics_depthz_252d_jerk_v096_signal,
    f17dv_f17_dollar_volume_dynamics_dvperpct_63d_jerk_v097_signal,
    f17dv_f17_dollar_volume_dynamics_dvperpct_126d_jerk_v098_signal,
    f17dv_f17_dollar_volume_dynamics_dvperpct_252d_jerk_v099_signal,
    f17dv_f17_dollar_volume_dynamics_flowtilt_63d_jerk_v100_signal,
    f17dv_f17_dollar_volume_dynamics_flowtilt_126d_jerk_v101_signal,
    f17dv_f17_dollar_volume_dynamics_flowtilt_252d_jerk_v102_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendsl_63d_jerk_v103_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendsl_126d_jerk_v104_signal,
    f17dv_f17_dollar_volume_dynamics_dvtrendsl_252d_jerk_v105_signal,
    f17dv_f17_dollar_volume_dynamics_dvretvol_63d_jerk_v106_signal,
    f17dv_f17_dollar_volume_dynamics_dvretvol_126d_jerk_v107_signal,
    f17dv_f17_dollar_volume_dynamics_dvretvol_252d_jerk_v108_signal,
    f17dv_f17_dollar_volume_dynamics_tierinstab_63d_jerk_v109_signal,
    f17dv_f17_dollar_volume_dynamics_tierinstab_126d_jerk_v110_signal,
    f17dv_f17_dollar_volume_dynamics_tierinstab_252d_jerk_v111_signal,
    f17dv_f17_dollar_volume_dynamics_dvvr_63d_jerk_v112_signal,
    f17dv_f17_dollar_volume_dynamics_dvvr_126d_jerk_v113_signal,
    f17dv_f17_dollar_volume_dynamics_dvvr_252d_jerk_v114_signal,
    f17dv_f17_dollar_volume_dynamics_dvmad_63d_jerk_v115_signal,
    f17dv_f17_dollar_volume_dynamics_dvmad_126d_jerk_v116_signal,
    f17dv_f17_dollar_volume_dynamics_dvmad_252d_jerk_v117_signal,
    f17dv_f17_dollar_volume_dynamics_dveffsh_63d_jerk_v118_signal,
    f17dv_f17_dollar_volume_dynamics_dveffsh_126d_jerk_v119_signal,
    f17dv_f17_dollar_volume_dynamics_dveffsh_252d_jerk_v120_signal,
    f17dv_f17_dollar_volume_dynamics_elevfrac_63d_jerk_v121_signal,
    f17dv_f17_dollar_volume_dynamics_elevfrac_126d_jerk_v122_signal,
    f17dv_f17_dollar_volume_dynamics_elevfrac_252d_jerk_v123_signal,
    f17dv_f17_dollar_volume_dynamics_dndisp_63d_jerk_v124_signal,
    f17dv_f17_dollar_volume_dynamics_dndisp_126d_jerk_v125_signal,
    f17dv_f17_dollar_volume_dynamics_dndisp_252d_jerk_v126_signal,
    f17dv_f17_dollar_volume_dynamics_dvtotgrow_63d_jerk_v127_signal,
    f17dv_f17_dollar_volume_dynamics_dvtotgrow_126d_jerk_v128_signal,
    f17dv_f17_dollar_volume_dynamics_dvtotgrow_252d_jerk_v129_signal,
    f17dv_f17_dollar_volume_dynamics_top3share_63d_jerk_v130_signal,
    f17dv_f17_dollar_volume_dynamics_top3share_126d_jerk_v131_signal,
    f17dv_f17_dollar_volume_dynamics_top3share_252d_jerk_v132_signal,
    f17dv_f17_dollar_volume_dynamics_monthvspeak_63d_jerk_v133_signal,
    f17dv_f17_dollar_volume_dynamics_monthvspeak_126d_jerk_v134_signal,
    f17dv_f17_dollar_volume_dynamics_monthvspeak_252d_jerk_v135_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangecorr_63d_jerk_v136_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangecorr_126d_jerk_v137_signal,
    f17dv_f17_dollar_volume_dynamics_dvrangecorr_252d_jerk_v138_signal,
    f17dv_f17_dollar_volume_dynamics_dvhilo_63d_jerk_v139_signal,
    f17dv_f17_dollar_volume_dynamics_dvhilo_126d_jerk_v140_signal,
    f17dv_f17_dollar_volume_dynamics_dvhilo_252d_jerk_v141_signal,
    f17dv_f17_dollar_volume_dynamics_dvpain_63d_jerk_v142_signal,
    f17dv_f17_dollar_volume_dynamics_dvpain_126d_jerk_v143_signal,
    f17dv_f17_dollar_volume_dynamics_dvpain_252d_jerk_v144_signal,
    f17dv_f17_dollar_volume_dynamics_rwconc_63d_jerk_v145_signal,
    f17dv_f17_dollar_volume_dynamics_rwconc_126d_jerk_v146_signal,
    f17dv_f17_dollar_volume_dynamics_rwconc_252d_jerk_v147_signal,
    f17dv_f17_dollar_volume_dynamics_dvqusk_63d_jerk_v148_signal,
    f17dv_f17_dollar_volume_dynamics_dvqusk_126d_jerk_v149_signal,
    f17dv_f17_dollar_volume_dynamics_dvqusk_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_DOLLAR_VOLUME_DYNAMICS_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    ALLOW = {"open", "high", "low", "close", "closeadj", "volume",
             "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
             "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
             "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
             "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
             "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
             "investments", "inventory", "receivables", "payables", "equity", "retearn",
             "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
             "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
             "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
             "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
             "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
             "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
             "cllvalue", "wntholders", "wntvalue", "dbtvalue"}


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
    print("OK f17_dollar_volume_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
