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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _dil(shares, w):
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _logdil(shares, w):
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _raise(ncfcommon):
    return -ncfcommon


def _buyback(ncfcommon):
    return ncfcommon.clip(lower=0)


def _raisepos(ncfcommon):
    return _raise(ncfcommon).clip(lower=0)


def _slope(s, w):
    return s - s.shift(w)


def _jerk(s, w):
    return s - 2.0 * s.shift(w) + s.shift(2 * w)


def f29sc_f29_share_count_dynamics_dilbas_21d_5d_jerk_v001_signal(sharesbas):
    base = _logdil(sharesbas, 21)
    d = _jerk(base, 5)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_42d_10d_jerk_v002_signal(sharesbas):
    base = _logdil(sharesbas, 42)
    d = _jerk(base, 10)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_63d_21d_jerk_v003_signal(sharesbas):
    base = _logdil(sharesbas, 63)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_84d_21d_jerk_v004_signal(sharesbas):
    base = _logdil(sharesbas, 84)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_126d_21d_jerk_v005_signal(sharesbas):
    base = _logdil(sharesbas, 126)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_168d_42d_jerk_v006_signal(sharesbas):
    base = _logdil(sharesbas, 168)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_189d_42d_jerk_v007_signal(sharesbas):
    base = _logdil(sharesbas, 189)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_210d_42d_jerk_v008_signal(sharesbas):
    base = _logdil(sharesbas, 210)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_252d_63d_jerk_v009_signal(sharesbas):
    base = _logdil(sharesbas, 252)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_315d_63d_jerk_v010_signal(sharesbas):
    base = _logdil(sharesbas, 315)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_378d_63d_jerk_v011_signal(sharesbas):
    base = _logdil(sharesbas, 378)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_441d_63d_jerk_v012_signal(sharesbas):
    base = _logdil(sharesbas, 441)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_504d_126d_jerk_v013_signal(sharesbas):
    base = _logdil(sharesbas, 504)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_630d_126d_jerk_v014_signal(sharesbas):
    base = _logdil(sharesbas, 630)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbas_756d_126d_jerk_v015_signal(sharesbas):
    base = _logdil(sharesbas, 756)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_21d_5d_jerk_v016_signal(shareswa):
    d = _logdil(shareswa, 21)
    base = _z(d, 126)
    d = _jerk(base, 5)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_42d_10d_jerk_v017_signal(shareswa):
    d = _logdil(shareswa, 42)
    base = _z(d, 126)
    d = _jerk(base, 10)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_63d_21d_jerk_v018_signal(shareswa):
    d = _logdil(shareswa, 63)
    base = _z(d, 126)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_84d_21d_jerk_v019_signal(shareswa):
    d = _logdil(shareswa, 84)
    base = _z(d, 168)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_126d_21d_jerk_v020_signal(shareswa):
    d = _logdil(shareswa, 126)
    base = _z(d, 252)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_168d_42d_jerk_v021_signal(shareswa):
    d = _logdil(shareswa, 168)
    base = _z(d, 336)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_189d_42d_jerk_v022_signal(shareswa):
    d = _logdil(shareswa, 189)
    base = _z(d, 378)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_210d_42d_jerk_v023_signal(shareswa):
    d = _logdil(shareswa, 210)
    base = _z(d, 420)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_252d_63d_jerk_v024_signal(shareswa):
    d = _logdil(shareswa, 252)
    base = _z(d, 504)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_315d_63d_jerk_v025_signal(shareswa):
    d = _logdil(shareswa, 315)
    base = _z(d, 504)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_378d_63d_jerk_v026_signal(shareswa):
    d = _logdil(shareswa, 378)
    base = _z(d, 504)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_441d_63d_jerk_v027_signal(shareswa):
    d = _logdil(shareswa, 441)
    base = _z(d, 504)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_504d_126d_jerk_v028_signal(shareswa):
    d = _logdil(shareswa, 504)
    base = _z(d, 504)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_630d_126d_jerk_v029_signal(shareswa):
    d = _logdil(shareswa, 630)
    base = _z(d, 504)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwa_756d_126d_jerk_v030_signal(shareswa):
    d = _logdil(shareswa, 756)
    base = _z(d, 504)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_21d_5d_jerk_v031_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 21)
    db = _logdil(shareswa, 21)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 5)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_42d_10d_jerk_v032_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 42)
    db = _logdil(shareswa, 42)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 10)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_63d_21d_jerk_v033_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 63)
    db = _logdil(shareswa, 63)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_84d_21d_jerk_v034_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 84)
    db = _logdil(shareswa, 84)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_126d_21d_jerk_v035_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 126)
    db = _logdil(shareswa, 126)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_168d_42d_jerk_v036_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 168)
    db = _logdil(shareswa, 168)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_189d_42d_jerk_v037_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 189)
    db = _logdil(shareswa, 189)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_210d_42d_jerk_v038_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 210)
    db = _logdil(shareswa, 210)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_252d_63d_jerk_v039_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 252)
    db = _logdil(shareswa, 252)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_315d_63d_jerk_v040_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 315)
    db = _logdil(shareswa, 315)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_378d_63d_jerk_v041_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 378)
    db = _logdil(shareswa, 378)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_441d_63d_jerk_v042_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 441)
    db = _logdil(shareswa, 441)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_504d_126d_jerk_v043_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 504)
    db = _logdil(shareswa, 504)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_630d_126d_jerk_v044_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 630)
    db = _logdil(shareswa, 630)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildil_756d_126d_jerk_v045_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 756)
    db = _logdil(shareswa, 756)
    base = dd / db.replace(0, np.nan)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_21d_7d_jerk_v046_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(21)
    d = _jerk(base, 7)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_63d_21d_jerk_v047_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(63)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_126d_42d_jerk_v048_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(126)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_189d_63d_jerk_v049_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(189)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_252d_84d_jerk_v050_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(252)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_378d_126d_jerk_v051_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(378)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepchg_504d_168d_jerk_v052_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp - sp.shift(504)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_21d_7d_jerk_v053_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(21, min_periods=max(1, 21//2)).mean()
    d = _jerk(base, 7)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_63d_21d_jerk_v054_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(63, min_periods=max(1, 63//2)).mean()
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_126d_42d_jerk_v055_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(126, min_periods=max(1, 126//2)).mean()
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_189d_63d_jerk_v056_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(189, min_periods=max(1, 189//2)).mean()
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_252d_84d_jerk_v057_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(252, min_periods=max(1, 252//2)).mean()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_378d_126d_jerk_v058_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(378, min_periods=max(1, 378//2)).mean()
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creeplv_504d_168d_jerk_v059_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = sp.rolling(504, min_periods=max(1, 504//2)).mean()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepz_252_63d_jerk_v060_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = _z(sp, 252)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz63__21d_jerk_v061_signal(shareswadil, shareswa):
    dd = _z(_logdil(shareswadil, 63), 126)
    db = _z(_logdil(shareswa, 63), 126)
    base = dd - db
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz126__42d_jerk_v062_signal(shareswadil, shareswa):
    dd = _z(_logdil(shareswadil, 126), 252)
    db = _z(_logdil(shareswa, 126), 252)
    base = dd - db
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz189__63d_jerk_v063_signal(shareswadil, shareswa):
    dd = _z(_logdil(shareswadil, 189), 378)
    db = _z(_logdil(shareswa, 189), 378)
    base = dd - db
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz252__84d_jerk_v064_signal(shareswadil, shareswa):
    dd = _z(_logdil(shareswadil, 252), 504)
    db = _z(_logdil(shareswa, 252), 504)
    base = dd - db
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz504__168d_jerk_v065_signal(shareswadil, shareswa):
    dd = _z(_logdil(shareswadil, 504), 504)
    db = _z(_logdil(shareswa, 504), 504)
    base = dd - db
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepshare_63d_21d_jerk_v066_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 63)
    db = _logdil(shareswa, 63)
    base = (dd - db) / dd.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepshare_126d_42d_jerk_v067_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 126)
    db = _logdil(shareswa, 126)
    base = (dd - db) / dd.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepshare_252d_84d_jerk_v068_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 252)
    db = _logdil(shareswa, 252)
    base = (dd - db) / dd.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_creepshare_504d_168d_jerk_v069_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 504)
    db = _logdil(shareswa, 504)
    base = (dd - db) / dd.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dragz_252_63d_jerk_v070_signal(shareswadil, shareswa):
    dd = _logdil(shareswadil, 126)
    db = _logdil(shareswa, 126)
    base = _z(dd - db, 252)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_63d_21d_jerk_v071_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(63, min_periods=max(1,63//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(63, min_periods=max(1,63//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_126d_42d_jerk_v072_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(126, min_periods=max(1,126//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(126, min_periods=max(1,126//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_189d_63d_jerk_v073_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(189, min_periods=max(1,189//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(189, min_periods=max(1,189//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_252d_84d_jerk_v074_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_378d_126d_jerk_v075_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(378, min_periods=max(1,378//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(378, min_periods=max(1,378//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_netflow_504d_168d_jerk_v076_signal(ncfcommon):
    flow = _raise(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum()
    base = flow / scale.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_issintens_63d_21d_jerk_v077_signal(ncfcommon, sharesbas):
    raise_ = _raisepos(ncfcommon).rolling(63, min_periods=max(1,63//2)).sum()
    base = raise_ / sharesbas.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_issintens_126d_42d_jerk_v078_signal(ncfcommon, sharesbas):
    raise_ = _raisepos(ncfcommon).rolling(126, min_periods=max(1,126//2)).sum()
    base = raise_ / sharesbas.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_issintens_252d_84d_jerk_v079_signal(ncfcommon, sharesbas):
    raise_ = _raisepos(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    base = raise_ / sharesbas.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_issintens_504d_168d_jerk_v080_signal(ncfcommon, sharesbas):
    raise_ = _raisepos(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum()
    base = raise_ / sharesbas.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbintens_63d_21d_jerk_v081_signal(ncfcommon, sharesbas):
    bb = _buyback(ncfcommon).rolling(63, min_periods=max(1,63//2)).sum()
    base = bb / sharesbas.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbintens_126d_42d_jerk_v082_signal(ncfcommon, sharesbas):
    bb = _buyback(ncfcommon).rolling(126, min_periods=max(1,126//2)).sum()
    base = bb / sharesbas.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbintens_252d_84d_jerk_v083_signal(ncfcommon, sharesbas):
    bb = _buyback(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    base = bb / sharesbas.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbintens_504d_168d_jerk_v084_signal(ncfcommon, sharesbas):
    bb = _buyback(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum()
    base = bb / sharesbas.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowema_63d_21d_jerk_v085_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    ema = raise_.ewm(span=63, min_periods=max(1,63//3)).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    base = ema / scale.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowema_126d_42d_jerk_v086_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    ema = raise_.ewm(span=126, min_periods=max(1,126//3)).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    base = ema / scale.replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowema_252d_84d_jerk_v087_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    ema = raise_.ewm(span=252, min_periods=max(1,252//3)).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    base = ema / scale.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowema_504d_168d_jerk_v088_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    ema = raise_.ewm(span=504, min_periods=max(1,504//3)).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    base = ema / scale.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_posture_126d_42d_jerk_v089_signal(ncfcommon):
    bb = _buyback(ncfcommon).ewm(span=126, min_periods=max(1,126//3)).mean()
    iss = _raisepos(ncfcommon).ewm(span=126, min_periods=max(1,126//3)).mean()
    base = (bb - iss) / (bb + iss).replace(0, np.nan)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_posture_252d_84d_jerk_v090_signal(ncfcommon):
    bb = _buyback(ncfcommon).ewm(span=252, min_periods=max(1,252//3)).mean()
    iss = _raisepos(ncfcommon).ewm(span=252, min_periods=max(1,252//3)).mean()
    base = (bb - iss) / (bb + iss).replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_posture_504d_168d_jerk_v091_signal(ncfcommon):
    bb = _buyback(ncfcommon).ewm(span=504, min_periods=max(1,504//3)).mean()
    iss = _raisepos(ncfcommon).ewm(span=504, min_periods=max(1,504//3)).mean()
    base = (bb - iss) / (bb + iss).replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdisp_126d_42d_jerk_v092_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(126, min_periods=max(1,126//2)).std()
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdisp_252d_84d_jerk_v093_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(252, min_periods=max(1,252//2)).std()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdisp_504d_168d_jerk_v094_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(504, min_periods=max(1,504//2)).std()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowmed_126d_42d_jerk_v095_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(126, min_periods=max(1,126//2)).median()
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowmed_252d_84d_jerk_v096_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(252, min_periods=max(1,252//2)).median()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowmed_504d_168d_jerk_v097_signal(ncfcommon):
    raise_ = _raise(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    base = r.rolling(504, min_periods=max(1,504//2)).median()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdrift_252d_63d_jerk_v098_signal(ncfcommon):
    cum = _raise(ncfcommon).cumsum()
    trend = cum.rolling(252, min_periods=max(1,252//2)).mean()
    scale = _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum()
    base = (cum - trend) / scale.replace(0, np.nan)
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdrift_504d_126d_jerk_v099_signal(ncfcommon):
    cum = _raise(ncfcommon).cumsum()
    trend = cum.rolling(504, min_periods=max(1,504//2)).mean()
    scale = _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum()
    base = (cum - trend) / scale.replace(0, np.nan)
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_flowdrift_756d_189d_jerk_v100_signal(ncfcommon):
    cum = _raise(ncfcommon).cumsum()
    trend = cum.rolling(756, min_periods=max(1,756//2)).mean()
    scale = _raise(ncfcommon).abs().rolling(756, min_periods=max(1,756//2)).sum()
    base = (cum - trend) / scale.replace(0, np.nan)
    d = _jerk(base, 189)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildisp_126d_42d_jerk_v101_signal(sharesbas):
    q = _dil(sharesbas, 63)
    base = q.rolling(126, min_periods=max(1,126//2)).std()
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildisp_252d_84d_jerk_v102_signal(sharesbas):
    q = _dil(sharesbas, 63)
    base = q.rolling(252, min_periods=max(1,252//2)).std()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dildisp_504d_168d_jerk_v103_signal(sharesbas):
    q = _dil(sharesbas, 63)
    base = q.rolling(504, min_periods=max(1,504//2)).std()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilskew_252d_84d_jerk_v104_signal(sharesbas):
    m = _dil(sharesbas, 21)
    base = m.rolling(252, min_periods=max(1,252//2)).skew()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilskew_504d_168d_jerk_v105_signal(sharesbas):
    m = _dil(sharesbas, 21)
    base = m.rolling(504, min_periods=max(1,504//2)).skew()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilkurt_252d_84d_jerk_v106_signal(sharesbas):
    m = _dil(sharesbas, 21)
    base = m.rolling(252, min_periods=max(1,252//2)).kurt()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilkurt_504d_168d_jerk_v107_signal(sharesbas):
    m = _dil(sharesbas, 21)
    base = m.rolling(504, min_periods=max(1,504//2)).kurt()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_hhi_252d_84d_jerk_v108_signal(sharesbas):
    g = _dil(sharesbas, 21).clip(lower=0)
    tot = g.rolling(252, min_periods=max(1,252//2)).sum()
    sq = (g*g).rolling(252, min_periods=max(1,252//2)).sum()
    base = sq / (tot*tot).replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_hhi_504d_168d_jerk_v109_signal(sharesbas):
    g = _dil(sharesbas, 21).clip(lower=0)
    tot = g.rolling(504, min_periods=max(1,504//2)).sum()
    sq = (g*g).rolling(504, min_periods=max(1,504//2)).sum()
    base = sq / (tot*tot).replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_diltally_252d_84d_jerk_v110_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float)
    base = up.rolling(252, min_periods=max(1,252//2)).mean()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_diltally_504d_168d_jerk_v111_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float)
    base = up.rolling(504, min_periods=max(1,504//2)).mean()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_rangepos_252d_84d_jerk_v112_signal(sharesbas):
    hi = sharesbas.rolling(252, min_periods=max(1,252//2)).max()
    lo = sharesbas.rolling(252, min_periods=max(1,252//2)).min()
    base = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_rangepos_504d_168d_jerk_v113_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=max(1,504//2)).max()
    lo = sharesbas.rolling(504, min_periods=max(1,504//2)).min()
    base = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_peakprox_252d_84d_jerk_v114_signal(sharesbas):
    hi = sharesbas.rolling(252, min_periods=max(1,252//2)).max()
    base = sharesbas / hi.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_peakprox_504d_168d_jerk_v115_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=max(1,504//2)).max()
    base = sharesbas / hi.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dileff_252d_84d_jerk_v116_signal(sharesbas):
    net = (sharesbas - sharesbas.shift(252)).abs()
    path = sharesbas.diff().abs().rolling(252, min_periods=max(1,252//2)).sum()
    base = net / path.replace(0, np.nan)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dileff_504d_168d_jerk_v117_signal(sharesbas):
    net = (sharesbas - sharesbas.shift(504)).abs()
    path = sharesbas.diff().abs().rolling(504, min_periods=max(1,504//2)).sum()
    base = net / path.replace(0, np.nan)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilz_252d_84d_jerk_v118_signal(sharesbas):
    d = _dil(sharesbas, 252)
    base = _z(d, 252)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilz_504d_168d_jerk_v119_signal(sharesbas):
    d = _dil(sharesbas, 252)
    base = _z(d, 504)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_basvswa_252d_84d_jerk_v120_signal(sharesbas, shareswa):
    sp = sharesbas / shareswa.replace(0, np.nan)
    base = _z(sp, 252)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_basvswa_504d_168d_jerk_v121_signal(sharesbas, shareswa):
    sp = sharesbas / shareswa.replace(0, np.nan)
    base = _z(sp, 504)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_autocorr_252d_84d_jerk_v122_signal(sharesbas):
    g = _dil(sharesbas, 21)
    base = g.rolling(252, min_periods=max(1,252//2)).corr(g.shift(21))
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_autocorr_504d_168d_jerk_v123_signal(sharesbas):
    g = _dil(sharesbas, 21)
    base = g.rolling(504, min_periods=max(1,504//2)).corr(g.shift(21))
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_couple_252d_84d_jerk_v124_signal(sharesbas, shareswadil):
    db = _dil(sharesbas, 21)
    dd = _dil(shareswadil, 21)
    base = db.rolling(252, min_periods=max(1,252//2)).corr(dd)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_couple_504d_168d_jerk_v125_signal(sharesbas, shareswadil):
    db = _dil(sharesbas, 21)
    dd = _dil(shareswadil, 21)
    base = db.rolling(504, min_periods=max(1,504//2)).corr(dd)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbalance_252d_63d_jerk_v126_signal(sharesbas):
    d = sharesbas.diff()
    up = (d > 0).astype(float)
    dn = (d < 0).astype(float)
    base = (up.rolling(252, min_periods=max(1,252//2)).sum() - dn.rolling(252, min_periods=max(1,252//2)).sum()) / 252.0
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbalance_504d_126d_jerk_v127_signal(sharesbas):
    d = sharesbas.diff()
    up = (d > 0).astype(float)
    dn = (d < 0).astype(float)
    base = (up.rolling(504, min_periods=max(1,504//2)).sum() - dn.rolling(504, min_periods=max(1,504//2)).sum()) / 504.0
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilbalance_756d_189d_jerk_v128_signal(sharesbas):
    d = sharesbas.diff()
    up = (d > 0).astype(float)
    dn = (d < 0).astype(float)
    base = (up.rolling(756, min_periods=max(1,756//2)).sum() - dn.rolling(756, min_periods=max(1,756//2)).sum()) / 756.0
    d = _jerk(base, 189)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_worstdil_252d_84d_jerk_v129_signal(sharesbas):
    q = _dil(sharesbas, 63)
    base = q.rolling(252, min_periods=max(1,252//2)).max()
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_worstdil_504d_168d_jerk_v130_signal(sharesbas):
    q = _dil(sharesbas, 63)
    base = q.rolling(504, min_periods=max(1,504//2)).max()
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_severity_126d_42d_jerk_v131_signal(shareswadil, shareswa, sharesbas):
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    pace = _dil(sharesbas, 126).clip(lower=0)
    base = creep * pace * 10.0
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_severity_252d_84d_jerk_v132_signal(shareswadil, shareswa, sharesbas):
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    pace = _dil(sharesbas, 252).clip(lower=0)
    base = creep * pace * 10.0
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_severity_504d_168d_jerk_v133_signal(shareswadil, shareswa, sharesbas):
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    pace = _dil(sharesbas, 504).clip(lower=0)
    base = creep * pace * 10.0
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_raisefund_252d_84d_jerk_v134_signal(sharesbas, ncfcommon):
    issshare = (_raisepos(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum() / _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum().replace(0, np.nan))
    dil = _logdil(sharesbas, 252)
    base = dil * issshare
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_raisefund_504d_168d_jerk_v135_signal(sharesbas, ncfcommon):
    issshare = (_raisepos(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum() / _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum().replace(0, np.nan))
    dil = _logdil(sharesbas, 504)
    base = dil * issshare
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbfund_252d_84d_jerk_v136_signal(shareswadil, shareswa, ncfcommon):
    bbshare = (_buyback(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum() / _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum().replace(0, np.nan))
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = creep * bbshare
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_bbfund_504d_168d_jerk_v137_signal(shareswadil, shareswa, ncfcommon):
    bbshare = (_buyback(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum() / _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum().replace(0, np.nan))
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    base = creep * bbshare
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilperdollar_252d_84d_jerk_v138_signal(sharesbas, ncfcommon):
    dil = _dil(sharesbas, 252)
    raise_ = _raisepos(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum()
    rn = raise_ / scale.replace(0, np.nan)
    base = dil / (rn + 0.05)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilperdollar_504d_168d_jerk_v139_signal(sharesbas, ncfcommon):
    dil = _dil(sharesbas, 504)
    raise_ = _raisepos(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum()
    rn = raise_ / scale.replace(0, np.nan)
    base = dil / (rn + 0.05)
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_compound_252d_84d_jerk_v140_signal(shareswa, shareswadil):
    dwa = _logdil(shareswa, 252)
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    creep_z = _z(creep, 252)
    base = np.sign(dwa) * (dwa.abs() ** 0.5) * creep_z
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_compound_504d_168d_jerk_v141_signal(shareswa, shareswadil):
    dwa = _logdil(shareswa, 504)
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    creep_z = _z(creep, 252)
    base = np.sign(dwa) * (dwa.abs() ** 0.5) * creep_z
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_cashback_126d_42d_jerk_v142_signal(sharesbas, ncfcommon):
    dil = _dil(sharesbas, 126)
    flow = _raise(ncfcommon).rolling(126, min_periods=max(1,126//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(126, min_periods=max(1,126//2)).sum()
    rn = (flow / scale.replace(0, np.nan)).clip(-1.0, 1.0)
    base = dil * np.tanh(2.0 * rn)
    d = _jerk(base, 42)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_cashback_252d_84d_jerk_v143_signal(sharesbas, ncfcommon):
    dil = _dil(sharesbas, 252)
    flow = _raise(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum()
    rn = (flow / scale.replace(0, np.nan)).clip(-1.0, 1.0)
    base = dil * np.tanh(2.0 * rn)
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_silent_252d_84d_jerk_v144_signal(shareswadil, shareswa, sharesbas):
    cc = (shareswadil / shareswa.replace(0, np.nan) - 1.0)
    cc = cc - cc.shift(252)
    fg = _dil(sharesbas, 252)
    base = cc * (1.0 - np.tanh(50.0 * fg.abs()))
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_silent_504d_168d_jerk_v145_signal(shareswadil, shareswa, sharesbas):
    cc = (shareswadil / shareswa.replace(0, np.nan) - 1.0)
    cc = cc - cc.shift(504)
    fg = _dil(sharesbas, 504)
    base = cc * (1.0 - np.tanh(50.0 * fg.abs()))
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_composite_252d_84d_jerk_v146_signal(ncfcommon, shareswadil, shareswa, sharesbas):
    flow = _raise(ncfcommon).rolling(252, min_periods=max(1,252//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(252, min_periods=max(1,252//2)).sum()
    rn = np.tanh(2.0 * flow / scale.replace(0, np.nan))
    creep = _z(shareswadil / shareswa.replace(0, np.nan) - 1.0, 252)
    pace = _z(_dil(sharesbas, 252), 252)
    base = (rn + creep + pace) / 3.0
    d = _jerk(base, 84)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_composite_504d_168d_jerk_v147_signal(ncfcommon, shareswadil, shareswa, sharesbas):
    flow = _raise(ncfcommon).rolling(504, min_periods=max(1,504//2)).sum()
    scale = _raise(ncfcommon).abs().rolling(504, min_periods=max(1,504//2)).sum()
    rn = np.tanh(2.0 * flow / scale.replace(0, np.nan))
    creep = _z(shareswadil / shareswa.replace(0, np.nan) - 1.0, 252)
    pace = _z(_dil(sharesbas, 504), 252)
    base = (rn + creep + pace) / 3.0
    d = _jerk(base, 168)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwedge_252d_63d_jerk_v148_signal(sharesbas):
    dl = _logdil(sharesbas, 252)
    ds = _logdil(sharesbas, 252//2)
    base = dl - ds
    d = _jerk(base, 63)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwedge_504d_126d_jerk_v149_signal(sharesbas):
    dl = _logdil(sharesbas, 504)
    ds = _logdil(sharesbas, 504//2)
    base = dl - ds
    d = _jerk(base, 126)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


def f29sc_f29_share_count_dynamics_dilwedge_756d_189d_jerk_v150_signal(sharesbas):
    dl = _logdil(sharesbas, 756)
    ds = _logdil(sharesbas, 756//2)
    base = dl - ds
    d = _jerk(base, 189)
    result = d.replace([np.inf, -np.inf], np.nan)
    return result


_FEATURES = [
    f29sc_f29_share_count_dynamics_dilbas_21d_5d_jerk_v001_signal,
    f29sc_f29_share_count_dynamics_dilbas_42d_10d_jerk_v002_signal,
    f29sc_f29_share_count_dynamics_dilbas_63d_21d_jerk_v003_signal,
    f29sc_f29_share_count_dynamics_dilbas_84d_21d_jerk_v004_signal,
    f29sc_f29_share_count_dynamics_dilbas_126d_21d_jerk_v005_signal,
    f29sc_f29_share_count_dynamics_dilbas_168d_42d_jerk_v006_signal,
    f29sc_f29_share_count_dynamics_dilbas_189d_42d_jerk_v007_signal,
    f29sc_f29_share_count_dynamics_dilbas_210d_42d_jerk_v008_signal,
    f29sc_f29_share_count_dynamics_dilbas_252d_63d_jerk_v009_signal,
    f29sc_f29_share_count_dynamics_dilbas_315d_63d_jerk_v010_signal,
    f29sc_f29_share_count_dynamics_dilbas_378d_63d_jerk_v011_signal,
    f29sc_f29_share_count_dynamics_dilbas_441d_63d_jerk_v012_signal,
    f29sc_f29_share_count_dynamics_dilbas_504d_126d_jerk_v013_signal,
    f29sc_f29_share_count_dynamics_dilbas_630d_126d_jerk_v014_signal,
    f29sc_f29_share_count_dynamics_dilbas_756d_126d_jerk_v015_signal,
    f29sc_f29_share_count_dynamics_dilwa_21d_5d_jerk_v016_signal,
    f29sc_f29_share_count_dynamics_dilwa_42d_10d_jerk_v017_signal,
    f29sc_f29_share_count_dynamics_dilwa_63d_21d_jerk_v018_signal,
    f29sc_f29_share_count_dynamics_dilwa_84d_21d_jerk_v019_signal,
    f29sc_f29_share_count_dynamics_dilwa_126d_21d_jerk_v020_signal,
    f29sc_f29_share_count_dynamics_dilwa_168d_42d_jerk_v021_signal,
    f29sc_f29_share_count_dynamics_dilwa_189d_42d_jerk_v022_signal,
    f29sc_f29_share_count_dynamics_dilwa_210d_42d_jerk_v023_signal,
    f29sc_f29_share_count_dynamics_dilwa_252d_63d_jerk_v024_signal,
    f29sc_f29_share_count_dynamics_dilwa_315d_63d_jerk_v025_signal,
    f29sc_f29_share_count_dynamics_dilwa_378d_63d_jerk_v026_signal,
    f29sc_f29_share_count_dynamics_dilwa_441d_63d_jerk_v027_signal,
    f29sc_f29_share_count_dynamics_dilwa_504d_126d_jerk_v028_signal,
    f29sc_f29_share_count_dynamics_dilwa_630d_126d_jerk_v029_signal,
    f29sc_f29_share_count_dynamics_dilwa_756d_126d_jerk_v030_signal,
    f29sc_f29_share_count_dynamics_dildil_21d_5d_jerk_v031_signal,
    f29sc_f29_share_count_dynamics_dildil_42d_10d_jerk_v032_signal,
    f29sc_f29_share_count_dynamics_dildil_63d_21d_jerk_v033_signal,
    f29sc_f29_share_count_dynamics_dildil_84d_21d_jerk_v034_signal,
    f29sc_f29_share_count_dynamics_dildil_126d_21d_jerk_v035_signal,
    f29sc_f29_share_count_dynamics_dildil_168d_42d_jerk_v036_signal,
    f29sc_f29_share_count_dynamics_dildil_189d_42d_jerk_v037_signal,
    f29sc_f29_share_count_dynamics_dildil_210d_42d_jerk_v038_signal,
    f29sc_f29_share_count_dynamics_dildil_252d_63d_jerk_v039_signal,
    f29sc_f29_share_count_dynamics_dildil_315d_63d_jerk_v040_signal,
    f29sc_f29_share_count_dynamics_dildil_378d_63d_jerk_v041_signal,
    f29sc_f29_share_count_dynamics_dildil_441d_63d_jerk_v042_signal,
    f29sc_f29_share_count_dynamics_dildil_504d_126d_jerk_v043_signal,
    f29sc_f29_share_count_dynamics_dildil_630d_126d_jerk_v044_signal,
    f29sc_f29_share_count_dynamics_dildil_756d_126d_jerk_v045_signal,
    f29sc_f29_share_count_dynamics_creepchg_21d_7d_jerk_v046_signal,
    f29sc_f29_share_count_dynamics_creepchg_63d_21d_jerk_v047_signal,
    f29sc_f29_share_count_dynamics_creepchg_126d_42d_jerk_v048_signal,
    f29sc_f29_share_count_dynamics_creepchg_189d_63d_jerk_v049_signal,
    f29sc_f29_share_count_dynamics_creepchg_252d_84d_jerk_v050_signal,
    f29sc_f29_share_count_dynamics_creepchg_378d_126d_jerk_v051_signal,
    f29sc_f29_share_count_dynamics_creepchg_504d_168d_jerk_v052_signal,
    f29sc_f29_share_count_dynamics_creeplv_21d_7d_jerk_v053_signal,
    f29sc_f29_share_count_dynamics_creeplv_63d_21d_jerk_v054_signal,
    f29sc_f29_share_count_dynamics_creeplv_126d_42d_jerk_v055_signal,
    f29sc_f29_share_count_dynamics_creeplv_189d_63d_jerk_v056_signal,
    f29sc_f29_share_count_dynamics_creeplv_252d_84d_jerk_v057_signal,
    f29sc_f29_share_count_dynamics_creeplv_378d_126d_jerk_v058_signal,
    f29sc_f29_share_count_dynamics_creeplv_504d_168d_jerk_v059_signal,
    f29sc_f29_share_count_dynamics_creepz_252_63d_jerk_v060_signal,
    f29sc_f29_share_count_dynamics_dragz63__21d_jerk_v061_signal,
    f29sc_f29_share_count_dynamics_dragz126__42d_jerk_v062_signal,
    f29sc_f29_share_count_dynamics_dragz189__63d_jerk_v063_signal,
    f29sc_f29_share_count_dynamics_dragz252__84d_jerk_v064_signal,
    f29sc_f29_share_count_dynamics_dragz504__168d_jerk_v065_signal,
    f29sc_f29_share_count_dynamics_creepshare_63d_21d_jerk_v066_signal,
    f29sc_f29_share_count_dynamics_creepshare_126d_42d_jerk_v067_signal,
    f29sc_f29_share_count_dynamics_creepshare_252d_84d_jerk_v068_signal,
    f29sc_f29_share_count_dynamics_creepshare_504d_168d_jerk_v069_signal,
    f29sc_f29_share_count_dynamics_dragz_252_63d_jerk_v070_signal,
    f29sc_f29_share_count_dynamics_netflow_63d_21d_jerk_v071_signal,
    f29sc_f29_share_count_dynamics_netflow_126d_42d_jerk_v072_signal,
    f29sc_f29_share_count_dynamics_netflow_189d_63d_jerk_v073_signal,
    f29sc_f29_share_count_dynamics_netflow_252d_84d_jerk_v074_signal,
    f29sc_f29_share_count_dynamics_netflow_378d_126d_jerk_v075_signal,
    f29sc_f29_share_count_dynamics_netflow_504d_168d_jerk_v076_signal,
    f29sc_f29_share_count_dynamics_issintens_63d_21d_jerk_v077_signal,
    f29sc_f29_share_count_dynamics_issintens_126d_42d_jerk_v078_signal,
    f29sc_f29_share_count_dynamics_issintens_252d_84d_jerk_v079_signal,
    f29sc_f29_share_count_dynamics_issintens_504d_168d_jerk_v080_signal,
    f29sc_f29_share_count_dynamics_bbintens_63d_21d_jerk_v081_signal,
    f29sc_f29_share_count_dynamics_bbintens_126d_42d_jerk_v082_signal,
    f29sc_f29_share_count_dynamics_bbintens_252d_84d_jerk_v083_signal,
    f29sc_f29_share_count_dynamics_bbintens_504d_168d_jerk_v084_signal,
    f29sc_f29_share_count_dynamics_flowema_63d_21d_jerk_v085_signal,
    f29sc_f29_share_count_dynamics_flowema_126d_42d_jerk_v086_signal,
    f29sc_f29_share_count_dynamics_flowema_252d_84d_jerk_v087_signal,
    f29sc_f29_share_count_dynamics_flowema_504d_168d_jerk_v088_signal,
    f29sc_f29_share_count_dynamics_posture_126d_42d_jerk_v089_signal,
    f29sc_f29_share_count_dynamics_posture_252d_84d_jerk_v090_signal,
    f29sc_f29_share_count_dynamics_posture_504d_168d_jerk_v091_signal,
    f29sc_f29_share_count_dynamics_flowdisp_126d_42d_jerk_v092_signal,
    f29sc_f29_share_count_dynamics_flowdisp_252d_84d_jerk_v093_signal,
    f29sc_f29_share_count_dynamics_flowdisp_504d_168d_jerk_v094_signal,
    f29sc_f29_share_count_dynamics_flowmed_126d_42d_jerk_v095_signal,
    f29sc_f29_share_count_dynamics_flowmed_252d_84d_jerk_v096_signal,
    f29sc_f29_share_count_dynamics_flowmed_504d_168d_jerk_v097_signal,
    f29sc_f29_share_count_dynamics_flowdrift_252d_63d_jerk_v098_signal,
    f29sc_f29_share_count_dynamics_flowdrift_504d_126d_jerk_v099_signal,
    f29sc_f29_share_count_dynamics_flowdrift_756d_189d_jerk_v100_signal,
    f29sc_f29_share_count_dynamics_dildisp_126d_42d_jerk_v101_signal,
    f29sc_f29_share_count_dynamics_dildisp_252d_84d_jerk_v102_signal,
    f29sc_f29_share_count_dynamics_dildisp_504d_168d_jerk_v103_signal,
    f29sc_f29_share_count_dynamics_dilskew_252d_84d_jerk_v104_signal,
    f29sc_f29_share_count_dynamics_dilskew_504d_168d_jerk_v105_signal,
    f29sc_f29_share_count_dynamics_dilkurt_252d_84d_jerk_v106_signal,
    f29sc_f29_share_count_dynamics_dilkurt_504d_168d_jerk_v107_signal,
    f29sc_f29_share_count_dynamics_hhi_252d_84d_jerk_v108_signal,
    f29sc_f29_share_count_dynamics_hhi_504d_168d_jerk_v109_signal,
    f29sc_f29_share_count_dynamics_diltally_252d_84d_jerk_v110_signal,
    f29sc_f29_share_count_dynamics_diltally_504d_168d_jerk_v111_signal,
    f29sc_f29_share_count_dynamics_rangepos_252d_84d_jerk_v112_signal,
    f29sc_f29_share_count_dynamics_rangepos_504d_168d_jerk_v113_signal,
    f29sc_f29_share_count_dynamics_peakprox_252d_84d_jerk_v114_signal,
    f29sc_f29_share_count_dynamics_peakprox_504d_168d_jerk_v115_signal,
    f29sc_f29_share_count_dynamics_dileff_252d_84d_jerk_v116_signal,
    f29sc_f29_share_count_dynamics_dileff_504d_168d_jerk_v117_signal,
    f29sc_f29_share_count_dynamics_dilz_252d_84d_jerk_v118_signal,
    f29sc_f29_share_count_dynamics_dilz_504d_168d_jerk_v119_signal,
    f29sc_f29_share_count_dynamics_basvswa_252d_84d_jerk_v120_signal,
    f29sc_f29_share_count_dynamics_basvswa_504d_168d_jerk_v121_signal,
    f29sc_f29_share_count_dynamics_autocorr_252d_84d_jerk_v122_signal,
    f29sc_f29_share_count_dynamics_autocorr_504d_168d_jerk_v123_signal,
    f29sc_f29_share_count_dynamics_couple_252d_84d_jerk_v124_signal,
    f29sc_f29_share_count_dynamics_couple_504d_168d_jerk_v125_signal,
    f29sc_f29_share_count_dynamics_dilbalance_252d_63d_jerk_v126_signal,
    f29sc_f29_share_count_dynamics_dilbalance_504d_126d_jerk_v127_signal,
    f29sc_f29_share_count_dynamics_dilbalance_756d_189d_jerk_v128_signal,
    f29sc_f29_share_count_dynamics_worstdil_252d_84d_jerk_v129_signal,
    f29sc_f29_share_count_dynamics_worstdil_504d_168d_jerk_v130_signal,
    f29sc_f29_share_count_dynamics_severity_126d_42d_jerk_v131_signal,
    f29sc_f29_share_count_dynamics_severity_252d_84d_jerk_v132_signal,
    f29sc_f29_share_count_dynamics_severity_504d_168d_jerk_v133_signal,
    f29sc_f29_share_count_dynamics_raisefund_252d_84d_jerk_v134_signal,
    f29sc_f29_share_count_dynamics_raisefund_504d_168d_jerk_v135_signal,
    f29sc_f29_share_count_dynamics_bbfund_252d_84d_jerk_v136_signal,
    f29sc_f29_share_count_dynamics_bbfund_504d_168d_jerk_v137_signal,
    f29sc_f29_share_count_dynamics_dilperdollar_252d_84d_jerk_v138_signal,
    f29sc_f29_share_count_dynamics_dilperdollar_504d_168d_jerk_v139_signal,
    f29sc_f29_share_count_dynamics_compound_252d_84d_jerk_v140_signal,
    f29sc_f29_share_count_dynamics_compound_504d_168d_jerk_v141_signal,
    f29sc_f29_share_count_dynamics_cashback_126d_42d_jerk_v142_signal,
    f29sc_f29_share_count_dynamics_cashback_252d_84d_jerk_v143_signal,
    f29sc_f29_share_count_dynamics_silent_252d_84d_jerk_v144_signal,
    f29sc_f29_share_count_dynamics_silent_504d_168d_jerk_v145_signal,
    f29sc_f29_share_count_dynamics_composite_252d_84d_jerk_v146_signal,
    f29sc_f29_share_count_dynamics_composite_504d_168d_jerk_v147_signal,
    f29sc_f29_share_count_dynamics_dilwedge_252d_63d_jerk_v148_signal,
    f29sc_f29_share_count_dynamics_dilwedge_504d_126d_jerk_v149_signal,
    f29sc_f29_share_count_dynamics_dilwedge_756d_189d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_SHARE_COUNT_DYNAMICS_REGISTRY_301_450 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    _sb = np.random.default_rng(101)
    _drift = np.repeat(_sb.normal(0.02, 0.06, n // 63 + 1), 63)[:n] / 63.0
    _jumps = np.zeros(n)
    _jidx = _sb.choice(np.arange(63, n), size=34, replace=False)
    _jumps[_jidx] = _sb.uniform(0.008, 0.06, size=34)
    sharesbas = pd.Series(1.2e8 * np.exp(np.cumsum(_drift + _jumps)), name="sharesbas")
    shareswa = sharesbas.rolling(63, min_periods=1).mean().rename("shareswa")
    _cr = np.random.default_rng(103)
    _creep = 0.05 + 0.03 * np.sin(np.linspace(0, 7.0, n)) + np.cumsum(_cr.normal(0, 0.0015, n))
    _creep = np.clip(_creep, 0.005, 0.20)
    shareswadil = (shareswa * (1.0 + _creep)).rename("shareswadil")
    _g = np.random.default_rng(104)
    _steps = np.repeat(_g.normal(0.0, 1.0, n // 63 + 1), 63)[:n]
    _mag = _fund(105, base=4e6, drift=0.0, vol=0.25)
    ncfcommon = pd.Series(_steps * _mag.values, name="ncfcommon")

    cols = {"sharesbas": sharesbas, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
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

    print("OK f29_share_count_dynamics_3rd_derivatives_001_150_claude: %d features pass" % n_features)
