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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _f39_mom(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


def _f39_prox_high(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / hi.replace(0, np.nan)


def _f39_rngpos(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    lo = closeadj.rolling(w, min_periods=max(1, w // 2)).min()
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f39_volsurge(volume, wshort, wlong):
    a = volume.rolling(wshort, min_periods=max(1, wshort // 2)).mean()
    b = volume.rolling(wlong, min_periods=max(1, wlong // 2)).mean()
    return a / b.replace(0, np.nan)


def _f39_dollar_vol(closeadj, volume):
    return closeadj * volume


def _f39_share_growth(sharesbas, w):
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _f39_share_accel(sharesbas, w):
    g = np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))
    return g - g.shift(w)


def _f39_issuance(ncfcommon):
    return -ncfcommon


def f39dx_f39_dilution_trap_detector_trapcore_63d_jerk_v001_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorenorm_63d_jerk_v002_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorerank_63d_jerk_v003_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcore_126d_jerk_v004_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorenorm_126d_jerk_v005_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorerank_126d_jerk_v006_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcore_252d_jerk_v007_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorenorm_252d_jerk_v008_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorerank_252d_jerk_v009_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcore_504d_jerk_v010_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorenorm_504d_jerk_v011_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapcorerank_504d_jerk_v012_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapz_63d_jerk_v013_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapznorm_63d_jerk_v014_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapzrank_63d_jerk_v015_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapz_126d_jerk_v016_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapznorm_126d_jerk_v017_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapzrank_126d_jerk_v018_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapz_252d_jerk_v019_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_mom(closeadj, 252), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapznorm_252d_jerk_v020_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_mom(closeadj, 252), 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapzrank_252d_jerk_v021_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_mom(closeadj, 252), 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapz_504d_jerk_v022_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_mom(closeadj, 504), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapznorm_504d_jerk_v023_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_mom(closeadj, 504), 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_trapzrank_504d_jerk_v024_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_mom(closeadj, 504), 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestr_63d_jerk_v025_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_mom(closeadj, 63).clip(lower=0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrnorm_63d_jerk_v026_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_mom(closeadj, 63).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrrank_63d_jerk_v027_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_mom(closeadj, 63).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestr_126d_jerk_v028_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_mom(closeadj, 126).clip(lower=0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrnorm_126d_jerk_v029_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_mom(closeadj, 126).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrrank_126d_jerk_v030_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_mom(closeadj, 126).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestr_252d_jerk_v031_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_mom(closeadj, 252).clip(lower=0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrnorm_252d_jerk_v032_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_mom(closeadj, 252).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrrank_252d_jerk_v033_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_mom(closeadj, 252).clip(lower=0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestr_504d_jerk_v034_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_mom(closeadj, 504).clip(lower=0)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrnorm_504d_jerk_v035_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_mom(closeadj, 504).clip(lower=0)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_issuestrrank_504d_jerk_v036_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_mom(closeadj, 504).clip(lower=0)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldil_63d_jerk_v037_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilnorm_63d_jerk_v038_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilrank_63d_jerk_v039_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldil_126d_jerk_v040_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilnorm_126d_jerk_v041_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilrank_126d_jerk_v042_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldil_252d_jerk_v043_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilnorm_252d_jerk_v044_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilrank_252d_jerk_v045_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldil_504d_jerk_v046_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilnorm_504d_jerk_v047_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_voldilrank_504d_jerk_v048_signal(sharesbas, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _f39_volsurge(volume, 21, 126)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrap_63d_jerk_v049_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) - _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrapnorm_63d_jerk_v050_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) - _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtraprank_63d_jerk_v051_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) - _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrap_126d_jerk_v052_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) - _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrapnorm_126d_jerk_v053_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) - _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtraprank_126d_jerk_v054_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) - _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrap_252d_jerk_v055_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) - _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrapnorm_252d_jerk_v056_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) - _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtraprank_252d_jerk_v057_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) - _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrap_504d_jerk_v058_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) - _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtrapnorm_504d_jerk_v059_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) - _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_addtraprank_504d_jerk_v060_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) - _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrng_63d_jerk_v061_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (_f39_rngpos(closeadj, 63) - 0.5)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngnorm_63d_jerk_v062_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (_f39_rngpos(closeadj, 63) - 0.5)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngrank_63d_jerk_v063_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (_f39_rngpos(closeadj, 63) - 0.5)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrng_126d_jerk_v064_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (_f39_rngpos(closeadj, 126) - 0.5)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngnorm_126d_jerk_v065_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (_f39_rngpos(closeadj, 126) - 0.5)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngrank_126d_jerk_v066_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (_f39_rngpos(closeadj, 126) - 0.5)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrng_252d_jerk_v067_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (_f39_rngpos(closeadj, 252) - 0.5)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngnorm_252d_jerk_v068_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (_f39_rngpos(closeadj, 252) - 0.5)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngrank_252d_jerk_v069_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (_f39_rngpos(closeadj, 252) - 0.5)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrng_504d_jerk_v070_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (_f39_rngpos(closeadj, 504) - 0.5)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngnorm_504d_jerk_v071_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (_f39_rngpos(closeadj, 504) - 0.5)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dilrngrank_504d_jerk_v072_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (_f39_rngpos(closeadj, 504) - 0.5)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshigh_63d_jerk_v073_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighnorm_63d_jerk_v074_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighrank_63d_jerk_v075_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 63) * _f39_prox_high(closeadj, 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshigh_126d_jerk_v076_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighnorm_126d_jerk_v077_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighrank_126d_jerk_v078_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 126) * _f39_prox_high(closeadj, 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshigh_252d_jerk_v079_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighnorm_252d_jerk_v080_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighrank_252d_jerk_v081_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 252) * _f39_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshigh_504d_jerk_v082_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighnorm_504d_jerk_v083_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_isshighrank_504d_jerk_v084_signal(ncfcommon, closeadj):
    base = _z(_f39_issuance(ncfcommon), 504) * _f39_prox_high(closeadj, 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdil_63d_jerk_v085_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_dollar_vol(closeadj, volume).diff(15), 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilnorm_63d_jerk_v086_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_dollar_vol(closeadj, volume).diff(15), 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilrank_63d_jerk_v087_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_dollar_vol(closeadj, volume).diff(15), 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdil_126d_jerk_v088_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_dollar_vol(closeadj, volume).diff(31), 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilnorm_126d_jerk_v089_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_dollar_vol(closeadj, volume).diff(31), 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilrank_126d_jerk_v090_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_dollar_vol(closeadj, volume).diff(31), 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdil_252d_jerk_v091_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_dollar_vol(closeadj, volume).diff(63), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilnorm_252d_jerk_v092_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_dollar_vol(closeadj, volume).diff(63), 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilrank_252d_jerk_v093_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_dollar_vol(closeadj, volume).diff(63), 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdil_504d_jerk_v094_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_dollar_vol(closeadj, volume).diff(126), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilnorm_504d_jerk_v095_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_dollar_vol(closeadj, volume).diff(126), 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dvdilrank_504d_jerk_v096_signal(sharesbas, closeadj, volume):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * _z(_f39_dollar_vol(closeadj, volume).diff(126), 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrap_63d_jerk_v097_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 31), 63) * _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrapnorm_63d_jerk_v098_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 31), 63) * _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltraprank_63d_jerk_v099_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 31), 63) * _z(_f39_mom(closeadj, 15), 63)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrap_126d_jerk_v100_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 63), 126) * _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrapnorm_126d_jerk_v101_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 63), 126) * _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltraprank_126d_jerk_v102_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 63), 126) * _z(_f39_mom(closeadj, 31), 126)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrap_252d_jerk_v103_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 126), 252) * _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrapnorm_252d_jerk_v104_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 126), 252) * _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltraprank_252d_jerk_v105_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 126), 252) * _z(_f39_mom(closeadj, 63), 252)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrap_504d_jerk_v106_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 252), 504) * _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltrapnorm_504d_jerk_v107_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 252), 504) * _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_acceltraprank_504d_jerk_v108_signal(sharesbas, closeadj):
    base = _z(_f39_share_accel(sharesbas, 252), 504) * _z(_f39_mom(closeadj, 126), 504)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressure_63d_jerk_v109_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurenorm_63d_jerk_v110_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurerank_63d_jerk_v111_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 63), 63) * (closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressure_126d_jerk_v112_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (closeadj / _mean(closeadj, 126).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurenorm_126d_jerk_v113_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (closeadj / _mean(closeadj, 126).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurerank_126d_jerk_v114_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 126), 126) * (closeadj / _mean(closeadj, 126).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressure_252d_jerk_v115_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurenorm_252d_jerk_v116_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurerank_252d_jerk_v117_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 252), 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressure_504d_jerk_v118_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (closeadj / _mean(closeadj, 504).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurenorm_504d_jerk_v119_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (closeadj / _mean(closeadj, 504).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_pressurerank_504d_jerk_v120_signal(sharesbas, closeadj):
    base = _z(_f39_share_growth(sharesbas, 504), 504) * (closeadj / _mean(closeadj, 504).replace(0, np.nan) - 1.0)
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperation_63d_jerk_v121_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * (1.0 - _f39_prox_high(closeadj, 63))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationnorm_63d_jerk_v122_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * (1.0 - _f39_prox_high(closeadj, 63))
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationrank_63d_jerk_v123_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * (1.0 - _f39_prox_high(closeadj, 63))
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperation_126d_jerk_v124_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * (1.0 - _f39_prox_high(closeadj, 126))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationnorm_126d_jerk_v125_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * (1.0 - _f39_prox_high(closeadj, 126))
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationrank_126d_jerk_v126_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * (1.0 - _f39_prox_high(closeadj, 126))
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperation_252d_jerk_v127_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * (1.0 - _f39_prox_high(closeadj, 252))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationnorm_252d_jerk_v128_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * (1.0 - _f39_prox_high(closeadj, 252))
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationrank_252d_jerk_v129_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * (1.0 - _f39_prox_high(closeadj, 252))
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperation_504d_jerk_v130_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * (1.0 - _f39_prox_high(closeadj, 504))
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationnorm_504d_jerk_v131_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * (1.0 - _f39_prox_high(closeadj, 504))
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_desperationrank_504d_jerk_v132_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * (1.0 - _f39_prox_high(closeadj, 504))
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildrag_63d_jerk_v133_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * _f39_mom(closeadj, 63).abs() ** 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragnorm_63d_jerk_v134_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * _f39_mom(closeadj, 63).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragrank_63d_jerk_v135_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 63) * np.sign(_f39_mom(closeadj, 63)) * _f39_mom(closeadj, 63).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildrag_126d_jerk_v136_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * _f39_mom(closeadj, 126).abs() ** 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragnorm_126d_jerk_v137_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * _f39_mom(closeadj, 126).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragrank_126d_jerk_v138_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 126) * np.sign(_f39_mom(closeadj, 126)) * _f39_mom(closeadj, 126).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildrag_252d_jerk_v139_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * _f39_mom(closeadj, 252).abs() ** 0.5
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragnorm_252d_jerk_v140_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * _f39_mom(closeadj, 252).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragrank_252d_jerk_v141_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 252) * np.sign(_f39_mom(closeadj, 252)) * _f39_mom(closeadj, 252).abs() ** 0.5
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildrag_504d_jerk_v142_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * _f39_mom(closeadj, 504).abs() ** 0.5
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragnorm_504d_jerk_v143_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * _f39_mom(closeadj, 504).abs() ** 0.5
    d1 = base - base.shift(63)
    raw2 = d1 - d1.shift(126)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_dildragrank_504d_jerk_v144_signal(sharesbas, closeadj):
    base = _f39_share_growth(sharesbas, 504) * np.sign(_f39_mom(closeadj, 504)) * _f39_mom(closeadj, 504).abs() ** 0.5
    d1 = base - base.shift(63)
    raw2 = (d1 - d1.shift(63)).ewm(span=63, min_periods=31).mean()
    d2 = _rank(raw2, 252)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanh_63d_jerk_v145_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanhnorm_63d_jerk_v146_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63))
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanhrank_63d_jerk_v147_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 63), 63) * _z(_f39_mom(closeadj, 63), 63))
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanh_126d_jerk_v148_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126))
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanhnorm_126d_jerk_v149_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126))
    d1 = base - base.shift(21)
    raw2 = d1 - d1.shift(42)
    d2 = np.sign(raw2) * (raw2.abs() ** 0.5)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

def f39dx_f39_dilution_trap_detector_traptanhrank_126d_jerk_v150_signal(sharesbas, closeadj):
    base = np.tanh(_z(_f39_share_growth(sharesbas, 126), 126) * _z(_f39_mom(closeadj, 126), 126))
    d1 = base - base.shift(21)
    raw2 = (d1 - d1.shift(21)).ewm(span=21, min_periods=10).mean()
    d2 = _rank(raw2, 126)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39dx_f39_dilution_trap_detector_trapcore_63d_jerk_v001_signal,
    f39dx_f39_dilution_trap_detector_trapcorenorm_63d_jerk_v002_signal,
    f39dx_f39_dilution_trap_detector_trapcorerank_63d_jerk_v003_signal,
    f39dx_f39_dilution_trap_detector_trapcore_126d_jerk_v004_signal,
    f39dx_f39_dilution_trap_detector_trapcorenorm_126d_jerk_v005_signal,
    f39dx_f39_dilution_trap_detector_trapcorerank_126d_jerk_v006_signal,
    f39dx_f39_dilution_trap_detector_trapcore_252d_jerk_v007_signal,
    f39dx_f39_dilution_trap_detector_trapcorenorm_252d_jerk_v008_signal,
    f39dx_f39_dilution_trap_detector_trapcorerank_252d_jerk_v009_signal,
    f39dx_f39_dilution_trap_detector_trapcore_504d_jerk_v010_signal,
    f39dx_f39_dilution_trap_detector_trapcorenorm_504d_jerk_v011_signal,
    f39dx_f39_dilution_trap_detector_trapcorerank_504d_jerk_v012_signal,
    f39dx_f39_dilution_trap_detector_trapz_63d_jerk_v013_signal,
    f39dx_f39_dilution_trap_detector_trapznorm_63d_jerk_v014_signal,
    f39dx_f39_dilution_trap_detector_trapzrank_63d_jerk_v015_signal,
    f39dx_f39_dilution_trap_detector_trapz_126d_jerk_v016_signal,
    f39dx_f39_dilution_trap_detector_trapznorm_126d_jerk_v017_signal,
    f39dx_f39_dilution_trap_detector_trapzrank_126d_jerk_v018_signal,
    f39dx_f39_dilution_trap_detector_trapz_252d_jerk_v019_signal,
    f39dx_f39_dilution_trap_detector_trapznorm_252d_jerk_v020_signal,
    f39dx_f39_dilution_trap_detector_trapzrank_252d_jerk_v021_signal,
    f39dx_f39_dilution_trap_detector_trapz_504d_jerk_v022_signal,
    f39dx_f39_dilution_trap_detector_trapznorm_504d_jerk_v023_signal,
    f39dx_f39_dilution_trap_detector_trapzrank_504d_jerk_v024_signal,
    f39dx_f39_dilution_trap_detector_issuestr_63d_jerk_v025_signal,
    f39dx_f39_dilution_trap_detector_issuestrnorm_63d_jerk_v026_signal,
    f39dx_f39_dilution_trap_detector_issuestrrank_63d_jerk_v027_signal,
    f39dx_f39_dilution_trap_detector_issuestr_126d_jerk_v028_signal,
    f39dx_f39_dilution_trap_detector_issuestrnorm_126d_jerk_v029_signal,
    f39dx_f39_dilution_trap_detector_issuestrrank_126d_jerk_v030_signal,
    f39dx_f39_dilution_trap_detector_issuestr_252d_jerk_v031_signal,
    f39dx_f39_dilution_trap_detector_issuestrnorm_252d_jerk_v032_signal,
    f39dx_f39_dilution_trap_detector_issuestrrank_252d_jerk_v033_signal,
    f39dx_f39_dilution_trap_detector_issuestr_504d_jerk_v034_signal,
    f39dx_f39_dilution_trap_detector_issuestrnorm_504d_jerk_v035_signal,
    f39dx_f39_dilution_trap_detector_issuestrrank_504d_jerk_v036_signal,
    f39dx_f39_dilution_trap_detector_voldil_63d_jerk_v037_signal,
    f39dx_f39_dilution_trap_detector_voldilnorm_63d_jerk_v038_signal,
    f39dx_f39_dilution_trap_detector_voldilrank_63d_jerk_v039_signal,
    f39dx_f39_dilution_trap_detector_voldil_126d_jerk_v040_signal,
    f39dx_f39_dilution_trap_detector_voldilnorm_126d_jerk_v041_signal,
    f39dx_f39_dilution_trap_detector_voldilrank_126d_jerk_v042_signal,
    f39dx_f39_dilution_trap_detector_voldil_252d_jerk_v043_signal,
    f39dx_f39_dilution_trap_detector_voldilnorm_252d_jerk_v044_signal,
    f39dx_f39_dilution_trap_detector_voldilrank_252d_jerk_v045_signal,
    f39dx_f39_dilution_trap_detector_voldil_504d_jerk_v046_signal,
    f39dx_f39_dilution_trap_detector_voldilnorm_504d_jerk_v047_signal,
    f39dx_f39_dilution_trap_detector_voldilrank_504d_jerk_v048_signal,
    f39dx_f39_dilution_trap_detector_addtrap_63d_jerk_v049_signal,
    f39dx_f39_dilution_trap_detector_addtrapnorm_63d_jerk_v050_signal,
    f39dx_f39_dilution_trap_detector_addtraprank_63d_jerk_v051_signal,
    f39dx_f39_dilution_trap_detector_addtrap_126d_jerk_v052_signal,
    f39dx_f39_dilution_trap_detector_addtrapnorm_126d_jerk_v053_signal,
    f39dx_f39_dilution_trap_detector_addtraprank_126d_jerk_v054_signal,
    f39dx_f39_dilution_trap_detector_addtrap_252d_jerk_v055_signal,
    f39dx_f39_dilution_trap_detector_addtrapnorm_252d_jerk_v056_signal,
    f39dx_f39_dilution_trap_detector_addtraprank_252d_jerk_v057_signal,
    f39dx_f39_dilution_trap_detector_addtrap_504d_jerk_v058_signal,
    f39dx_f39_dilution_trap_detector_addtrapnorm_504d_jerk_v059_signal,
    f39dx_f39_dilution_trap_detector_addtraprank_504d_jerk_v060_signal,
    f39dx_f39_dilution_trap_detector_dilrng_63d_jerk_v061_signal,
    f39dx_f39_dilution_trap_detector_dilrngnorm_63d_jerk_v062_signal,
    f39dx_f39_dilution_trap_detector_dilrngrank_63d_jerk_v063_signal,
    f39dx_f39_dilution_trap_detector_dilrng_126d_jerk_v064_signal,
    f39dx_f39_dilution_trap_detector_dilrngnorm_126d_jerk_v065_signal,
    f39dx_f39_dilution_trap_detector_dilrngrank_126d_jerk_v066_signal,
    f39dx_f39_dilution_trap_detector_dilrng_252d_jerk_v067_signal,
    f39dx_f39_dilution_trap_detector_dilrngnorm_252d_jerk_v068_signal,
    f39dx_f39_dilution_trap_detector_dilrngrank_252d_jerk_v069_signal,
    f39dx_f39_dilution_trap_detector_dilrng_504d_jerk_v070_signal,
    f39dx_f39_dilution_trap_detector_dilrngnorm_504d_jerk_v071_signal,
    f39dx_f39_dilution_trap_detector_dilrngrank_504d_jerk_v072_signal,
    f39dx_f39_dilution_trap_detector_isshigh_63d_jerk_v073_signal,
    f39dx_f39_dilution_trap_detector_isshighnorm_63d_jerk_v074_signal,
    f39dx_f39_dilution_trap_detector_isshighrank_63d_jerk_v075_signal,
    f39dx_f39_dilution_trap_detector_isshigh_126d_jerk_v076_signal,
    f39dx_f39_dilution_trap_detector_isshighnorm_126d_jerk_v077_signal,
    f39dx_f39_dilution_trap_detector_isshighrank_126d_jerk_v078_signal,
    f39dx_f39_dilution_trap_detector_isshigh_252d_jerk_v079_signal,
    f39dx_f39_dilution_trap_detector_isshighnorm_252d_jerk_v080_signal,
    f39dx_f39_dilution_trap_detector_isshighrank_252d_jerk_v081_signal,
    f39dx_f39_dilution_trap_detector_isshigh_504d_jerk_v082_signal,
    f39dx_f39_dilution_trap_detector_isshighnorm_504d_jerk_v083_signal,
    f39dx_f39_dilution_trap_detector_isshighrank_504d_jerk_v084_signal,
    f39dx_f39_dilution_trap_detector_dvdil_63d_jerk_v085_signal,
    f39dx_f39_dilution_trap_detector_dvdilnorm_63d_jerk_v086_signal,
    f39dx_f39_dilution_trap_detector_dvdilrank_63d_jerk_v087_signal,
    f39dx_f39_dilution_trap_detector_dvdil_126d_jerk_v088_signal,
    f39dx_f39_dilution_trap_detector_dvdilnorm_126d_jerk_v089_signal,
    f39dx_f39_dilution_trap_detector_dvdilrank_126d_jerk_v090_signal,
    f39dx_f39_dilution_trap_detector_dvdil_252d_jerk_v091_signal,
    f39dx_f39_dilution_trap_detector_dvdilnorm_252d_jerk_v092_signal,
    f39dx_f39_dilution_trap_detector_dvdilrank_252d_jerk_v093_signal,
    f39dx_f39_dilution_trap_detector_dvdil_504d_jerk_v094_signal,
    f39dx_f39_dilution_trap_detector_dvdilnorm_504d_jerk_v095_signal,
    f39dx_f39_dilution_trap_detector_dvdilrank_504d_jerk_v096_signal,
    f39dx_f39_dilution_trap_detector_acceltrap_63d_jerk_v097_signal,
    f39dx_f39_dilution_trap_detector_acceltrapnorm_63d_jerk_v098_signal,
    f39dx_f39_dilution_trap_detector_acceltraprank_63d_jerk_v099_signal,
    f39dx_f39_dilution_trap_detector_acceltrap_126d_jerk_v100_signal,
    f39dx_f39_dilution_trap_detector_acceltrapnorm_126d_jerk_v101_signal,
    f39dx_f39_dilution_trap_detector_acceltraprank_126d_jerk_v102_signal,
    f39dx_f39_dilution_trap_detector_acceltrap_252d_jerk_v103_signal,
    f39dx_f39_dilution_trap_detector_acceltrapnorm_252d_jerk_v104_signal,
    f39dx_f39_dilution_trap_detector_acceltraprank_252d_jerk_v105_signal,
    f39dx_f39_dilution_trap_detector_acceltrap_504d_jerk_v106_signal,
    f39dx_f39_dilution_trap_detector_acceltrapnorm_504d_jerk_v107_signal,
    f39dx_f39_dilution_trap_detector_acceltraprank_504d_jerk_v108_signal,
    f39dx_f39_dilution_trap_detector_pressure_63d_jerk_v109_signal,
    f39dx_f39_dilution_trap_detector_pressurenorm_63d_jerk_v110_signal,
    f39dx_f39_dilution_trap_detector_pressurerank_63d_jerk_v111_signal,
    f39dx_f39_dilution_trap_detector_pressure_126d_jerk_v112_signal,
    f39dx_f39_dilution_trap_detector_pressurenorm_126d_jerk_v113_signal,
    f39dx_f39_dilution_trap_detector_pressurerank_126d_jerk_v114_signal,
    f39dx_f39_dilution_trap_detector_pressure_252d_jerk_v115_signal,
    f39dx_f39_dilution_trap_detector_pressurenorm_252d_jerk_v116_signal,
    f39dx_f39_dilution_trap_detector_pressurerank_252d_jerk_v117_signal,
    f39dx_f39_dilution_trap_detector_pressure_504d_jerk_v118_signal,
    f39dx_f39_dilution_trap_detector_pressurenorm_504d_jerk_v119_signal,
    f39dx_f39_dilution_trap_detector_pressurerank_504d_jerk_v120_signal,
    f39dx_f39_dilution_trap_detector_desperation_63d_jerk_v121_signal,
    f39dx_f39_dilution_trap_detector_desperationnorm_63d_jerk_v122_signal,
    f39dx_f39_dilution_trap_detector_desperationrank_63d_jerk_v123_signal,
    f39dx_f39_dilution_trap_detector_desperation_126d_jerk_v124_signal,
    f39dx_f39_dilution_trap_detector_desperationnorm_126d_jerk_v125_signal,
    f39dx_f39_dilution_trap_detector_desperationrank_126d_jerk_v126_signal,
    f39dx_f39_dilution_trap_detector_desperation_252d_jerk_v127_signal,
    f39dx_f39_dilution_trap_detector_desperationnorm_252d_jerk_v128_signal,
    f39dx_f39_dilution_trap_detector_desperationrank_252d_jerk_v129_signal,
    f39dx_f39_dilution_trap_detector_desperation_504d_jerk_v130_signal,
    f39dx_f39_dilution_trap_detector_desperationnorm_504d_jerk_v131_signal,
    f39dx_f39_dilution_trap_detector_desperationrank_504d_jerk_v132_signal,
    f39dx_f39_dilution_trap_detector_dildrag_63d_jerk_v133_signal,
    f39dx_f39_dilution_trap_detector_dildragnorm_63d_jerk_v134_signal,
    f39dx_f39_dilution_trap_detector_dildragrank_63d_jerk_v135_signal,
    f39dx_f39_dilution_trap_detector_dildrag_126d_jerk_v136_signal,
    f39dx_f39_dilution_trap_detector_dildragnorm_126d_jerk_v137_signal,
    f39dx_f39_dilution_trap_detector_dildragrank_126d_jerk_v138_signal,
    f39dx_f39_dilution_trap_detector_dildrag_252d_jerk_v139_signal,
    f39dx_f39_dilution_trap_detector_dildragnorm_252d_jerk_v140_signal,
    f39dx_f39_dilution_trap_detector_dildragrank_252d_jerk_v141_signal,
    f39dx_f39_dilution_trap_detector_dildrag_504d_jerk_v142_signal,
    f39dx_f39_dilution_trap_detector_dildragnorm_504d_jerk_v143_signal,
    f39dx_f39_dilution_trap_detector_dildragrank_504d_jerk_v144_signal,
    f39dx_f39_dilution_trap_detector_traptanh_63d_jerk_v145_signal,
    f39dx_f39_dilution_trap_detector_traptanhnorm_63d_jerk_v146_signal,
    f39dx_f39_dilution_trap_detector_traptanhrank_63d_jerk_v147_signal,
    f39dx_f39_dilution_trap_detector_traptanh_126d_jerk_v148_signal,
    f39dx_f39_dilution_trap_detector_traptanhnorm_126d_jerk_v149_signal,
    f39dx_f39_dilution_trap_detector_traptanhrank_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_DILUTION_TRAP_DETECTOR_REGISTRY_001_150 = REGISTRY


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

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    sharesbas = _fund(101, base=5e7, drift=0.06, vol=0.10).rename("sharesbas")
    ncfcommon = _fund(77, base=2e7, drift=0.0, vol=2.5, allow_neg=True).rename("ncfcommon")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume,
            "sharesbas": sharesbas, "ncfcommon": ncfcommon}

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

    print("OK f39_dilution_trap_detector_3rd_derivatives_001_150_claude: %d features pass" % n_features)
