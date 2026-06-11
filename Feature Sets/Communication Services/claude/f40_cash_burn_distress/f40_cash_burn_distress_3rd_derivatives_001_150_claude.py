import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _logwarp(s):
    return np.sign(s) * np.log1p(s.abs())


# ===== folder domain DRIVER primitives (multi-driver distress composite) =====
# Each derivative below is the math derivative of a MULTI-DRIVER distress base composite
# (combines >=2 of burn / dilution / no-profit / leverage). Single-driver runway /
# cashneq-yoy / burn-rate / coverage-velocity levels belong to f31_cash_burn_runway.
def _f40_burn_pressure(cashneq, ncfo):
    burn = (-ncfo).clip(lower=0.0)
    cushion = cashneq.abs().rolling(126, min_periods=21).mean() + 1.0
    return burn / cushion


def _f40_dilution(sbcomp, sharesbas, equity, w):
    sbc = sbcomp / equity.abs().replace(0, np.nan)
    shr = (sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0).clip(lower=0)
    return sbc.clip(lower=0) + shr


def _f40_noprofit(ncfo, opex):
    return (-ncfo) / opex.replace(0, np.nan)


def _f40_leverage(debt, equity, cashneq):
    return (debt - cashneq) / equity.abs().replace(0, np.nan)


def _f40_zprod(a, b, w):
    return _z(a, w) * _z(b, w)


def _f40_zmin(a, b, w):
    return pd.concat([_z(a, w), _z(b, w)], axis=1).min(axis=1)


def _f40_zmax(a, b, w):
    return pd.concat([_z(a, w), _z(b, w)], axis=1).max(axis=1)


def _f40_zsigninter(a, b, w):
    za, zb = _z(a, w), _z(b, w)
    return np.sign(za) * np.sign(zb) * (za.abs() + zb.abs())


# ============================================================

def f40cd_f40_cash_burn_distress_zpbl_42d_jerk_v001_signal(cashneq, ncfo, debt, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_leverage(debt, equity, cashneq)
    base = _z(a, 63) * _z(b, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zpbd_42d_jerk_v002_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_dilution(sbcomp, sharesbas, equity, 126)
    base = _z(a, 126) * _z(b, 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zpbn_42d_jerk_v003_signal(cashneq, ncfo, opex):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_noprofit(ncfo, opex)
    base = _z(a, 63) * _z(b, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zpdl_42d_jerk_v004_signal(sbcomp, sharesbas, equity, debt, cashneq):
    a = _f40_dilution(sbcomp, sharesbas, equity, 126)
    b = _f40_leverage(debt, equity, cashneq)
    base = _z(a, 126) * _z(b, 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zpnl_42d_jerk_v005_signal(ncfo, opex, debt, equity, cashneq):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_leverage(debt, equity, cashneq)
    base = _z(a, 63) * _z(b, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zpnd_42d_jerk_v006_signal(ncfo, opex, sbcomp, sharesbas, equity):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_dilution(sbcomp, sharesbas, equity, 126)
    base = _z(a, 126) * _z(b, 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmnbl_42d_jerk_v007_signal(cashneq, ncfo, debt, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmnbd_42d_jerk_v008_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_dilution(sbcomp, sharesbas, equity, 63)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmnbn_42d_jerk_v009_signal(cashneq, ncfo, opex):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_noprofit(ncfo, opex)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmndl_42d_jerk_v010_signal(sbcomp, sharesbas, equity, debt, cashneq):
    a = _f40_dilution(sbcomp, sharesbas, equity, 63)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmnnl_42d_jerk_v011_signal(ncfo, opex, debt, equity, cashneq):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmnnd_42d_jerk_v012_signal(ncfo, opex, sbcomp, sharesbas, equity):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_dilution(sbcomp, sharesbas, equity, 63)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxbl_42d_jerk_v013_signal(cashneq, ncfo, debt, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxbd_42d_jerk_v014_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_dilution(sbcomp, sharesbas, equity, 126)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxbn_42d_jerk_v015_signal(cashneq, ncfo, opex):
    a = _f40_burn_pressure(cashneq, ncfo)
    b = _f40_noprofit(ncfo, opex)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxdl_42d_jerk_v016_signal(sbcomp, sharesbas, equity, debt, cashneq):
    a = _f40_dilution(sbcomp, sharesbas, equity, 126)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxnl_42d_jerk_v017_signal(ncfo, opex, debt, equity, cashneq):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_leverage(debt, equity, cashneq)
    base = pd.concat([_z(a, 63), _z(b, 63)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zmxnd_42d_jerk_v018_signal(ncfo, opex, sbcomp, sharesbas, equity):
    a = _f40_noprofit(ncfo, opex)
    b = _f40_dilution(sbcomp, sharesbas, equity, 126)
    base = pd.concat([_z(a, 126), _z(b, 126)], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgbl_42d_jerk_v019_signal(cashneq, ncfo, debt, equity):
    a = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    b = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgbd_42d_jerk_v020_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    a = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    b = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgbn_42d_jerk_v021_signal(cashneq, ncfo, opex):
    a = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    b = _z(_f40_noprofit(ncfo, opex), 126)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgdl_42d_jerk_v022_signal(sbcomp, sharesbas, equity, debt, cashneq):
    a = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    b = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgnl_42d_jerk_v023_signal(ncfo, opex, debt, equity, cashneq):
    a = _z(_f40_noprofit(ncfo, opex), 126)
    b = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_zsgnd_42d_jerk_v024_signal(ncfo, opex, sbcomp, sharesbas, equity):
    a = _z(_f40_noprofit(ncfo, opex), 63)
    b = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sign(a) * np.sign(b) * (a.abs() + b.abs())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprbl_42d_jerk_v025_signal(cashneq, ncfo, debt, equity):
    base = _z(_f40_burn_pressure(cashneq, ncfo), 63) - _z(_f40_leverage(debt, equity, cashneq), 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprbd_42d_jerk_v026_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    base = _z(_f40_burn_pressure(cashneq, ncfo), 126) - _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprbn_42d_jerk_v027_signal(cashneq, ncfo, opex):
    base = _z(_f40_burn_pressure(cashneq, ncfo), 63) - _z(_f40_noprofit(ncfo, opex), 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprdl_42d_jerk_v028_signal(sbcomp, sharesbas, equity, debt, cashneq):
    base = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) - _z(_f40_leverage(debt, equity, cashneq), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprnl_42d_jerk_v029_signal(ncfo, opex, debt, equity, cashneq):
    base = _z(_f40_noprofit(ncfo, opex), 63) - _z(_f40_leverage(debt, equity, cashneq), 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sprnd_42d_jerk_v030_signal(ncfo, opex, sbcomp, sharesbas, equity):
    base = _z(_f40_noprofit(ncfo, opex), 126) - _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpbl_42d_jerk_v031_signal(cashneq, ncfo, debt, equity):
    base = _rank(_z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpbd_42d_jerk_v032_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    base = _rank(_z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpbn_42d_jerk_v033_signal(cashneq, ncfo, opex):
    base = _rank(_z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_noprofit(ncfo, opex), 126), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpdl_42d_jerk_v034_signal(sbcomp, sharesbas, equity, debt, cashneq):
    base = _rank(_z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpnl_42d_jerk_v035_signal(ncfo, opex, debt, equity, cashneq):
    base = _rank(_z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_rkpnd_42d_jerk_v036_signal(ncfo, opex, sbcomp, sharesbas, equity):
    base = _rank(_z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63), 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpbl_42d_jerk_v037_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp.ewm(span=63, min_periods=31).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpbd_42d_jerk_v038_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp.ewm(span=126, min_periods=63).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpbn_42d_jerk_v039_signal(cashneq, ncfo, opex):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_noprofit(ncfo, opex), 63)
    base = comp.ewm(span=63, min_periods=31).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpdl_42d_jerk_v040_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp.ewm(span=126, min_periods=63).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpnl_42d_jerk_v041_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp.ewm(span=63, min_periods=31).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewpnd_42d_jerk_v042_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp.ewm(span=126, min_periods=63).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmbl_42d_jerk_v043_signal(cashneq, ncfo, debt, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126).clip(lower=0.05)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmbd_42d_jerk_v044_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 63).clip(lower=0.05)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmbn_42d_jerk_v045_signal(cashneq, ncfo, opex):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126).clip(lower=0.05)
    zb = _z(_f40_noprofit(ncfo, opex), 126).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmdl_42d_jerk_v046_signal(sbcomp, sharesbas, equity, debt, cashneq):
    za = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63).clip(lower=0.05)
    zb = _z(_f40_leverage(debt, equity, cashneq), 63).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmnl_42d_jerk_v047_signal(ncfo, opex, debt, equity, cashneq):
    za = _z(_f40_noprofit(ncfo, opex), 126).clip(lower=0.05)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_hrmnd_42d_jerk_v048_signal(ncfo, opex, sbcomp, sharesbas, equity):
    za = _z(_f40_noprofit(ncfo, opex), 63).clip(lower=0.05)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63).clip(lower=0.05)
    base = np.tanh(2.0 / (1.0 / za + 1.0 / zb))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpbl_42d_jerk_v049_signal(cashneq, ncfo, debt, equity):
    base = np.tanh(_z(_f40_burn_pressure(cashneq, ncfo), 63)) * np.tanh(_z(_f40_leverage(debt, equity, cashneq), 63))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpbd_42d_jerk_v050_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    base = np.tanh(_z(_f40_burn_pressure(cashneq, ncfo), 126)) * np.tanh(_z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpbn_42d_jerk_v051_signal(cashneq, ncfo, opex):
    base = np.tanh(_z(_f40_burn_pressure(cashneq, ncfo), 63)) * np.tanh(_z(_f40_noprofit(ncfo, opex), 63))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpdl_42d_jerk_v052_signal(sbcomp, sharesbas, equity, debt, cashneq):
    base = np.tanh(_z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)) * np.tanh(_z(_f40_leverage(debt, equity, cashneq), 126))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpnl_42d_jerk_v053_signal(ncfo, opex, debt, equity, cashneq):
    base = np.tanh(_z(_f40_noprofit(ncfo, opex), 63)) * np.tanh(_z(_f40_leverage(debt, equity, cashneq), 63))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tnpnd_42d_jerk_v054_signal(ncfo, opex, sbcomp, sharesbas, equity):
    base = np.tanh(_z(_f40_noprofit(ncfo, opex), 126)) * np.tanh(_z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucbl_42d_jerk_v055_signal(cashneq, ncfo, debt, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucbd_42d_jerk_v056_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucbn_42d_jerk_v057_signal(cashneq, ncfo, opex):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zb = _z(_f40_noprofit(ncfo, opex), 126)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucdl_42d_jerk_v058_signal(sbcomp, sharesbas, equity, debt, cashneq):
    za = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zb = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucnl_42d_jerk_v059_signal(ncfo, opex, debt, equity, cashneq):
    za = _z(_f40_noprofit(ncfo, opex), 126)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eucnd_42d_jerk_v060_signal(ncfo, opex, sbcomp, sharesbas, equity):
    za = _z(_f40_noprofit(ncfo, opex), 63)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sqrt(za ** 2 + zb ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtbl_42d_jerk_v061_signal(cashneq, ncfo, debt, equity):
    s = 0.5 * _z(_f40_burn_pressure(cashneq, ncfo), 63) + 0.5 * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtbd_42d_jerk_v062_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    s = 0.5 * _z(_f40_burn_pressure(cashneq, ncfo), 126) + 0.5 * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtbn_42d_jerk_v063_signal(cashneq, ncfo, opex):
    s = 0.5 * _z(_f40_burn_pressure(cashneq, ncfo), 63) + 0.5 * _z(_f40_noprofit(ncfo, opex), 63)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtdl_42d_jerk_v064_signal(sbcomp, sharesbas, equity, debt, cashneq):
    s = 0.5 * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) + 0.5 * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtnl_42d_jerk_v065_signal(ncfo, opex, debt, equity, cashneq):
    s = 0.5 * _z(_f40_noprofit(ncfo, opex), 63) + 0.5 * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_lgtnd_42d_jerk_v066_signal(ncfo, opex, sbcomp, sharesbas, equity):
    s = 0.5 * _z(_f40_noprofit(ncfo, opex), 126) + 0.5 * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cndbl_42d_jerk_v067_signal(cashneq, ncfo, debt, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cndbd_42d_jerk_v068_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cndbn_42d_jerk_v069_signal(cashneq, ncfo, opex):
    za = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zb = _z(_f40_noprofit(ncfo, opex), 126)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cnddl_42d_jerk_v070_signal(sbcomp, sharesbas, equity, debt, cashneq):
    za = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zb = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cndnl_42d_jerk_v071_signal(ncfo, opex, debt, equity, cashneq):
    za = _z(_f40_noprofit(ncfo, opex), 126)
    zb = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cndnd_42d_jerk_v072_signal(ncfo, opex, sbcomp, sharesbas, equity):
    za = _z(_f40_noprofit(ncfo, opex), 63)
    zb = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = za * (zb > 0).astype(float)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triwa_42d_jerk_v073_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = 0.6 * zb + 0.2 * zd + 0.2 * zl
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triwb_42d_jerk_v074_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = 0.2 * zb + 0.6 * zd + 0.2 * zl
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triwc_42d_jerk_v075_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = 0.2 * zb + 0.2 * zd + 0.6 * zl
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trimin_42d_jerk_v076_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = pd.concat([zb, zd, zl], axis=1).min(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trimax_42d_jerk_v077_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = pd.concat([zb, zd, zl], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trimean_42d_jerk_v078_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = (zb + zd + zl) / 3.0
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trieuc_42d_jerk_v079_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sqrt(zb ** 2 + zd ** 2 + zl ** 2)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tridisp_42d_jerk_v080_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = pd.concat([zb, zd, zl], axis=1).std(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trigeo_42d_jerk_v081_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    base = ((zb.clip(lower=0) + 0.1) * (zd.clip(lower=0) + 0.1) * (zl.clip(lower=0) + 0.1)) ** (1.0 / 3.0)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_trilgt_42d_jerk_v082_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    s = zb + zd + zl
    base = 1.0 / (1.0 + np.exp(-s)) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triwpair_42d_jerk_v083_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    st = pd.concat([zb, zd, zl], axis=1)
    base = (st.sum(axis=1) - st.min(axis=1)) / 2.0
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triprod_42d_jerk_v084_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = pd.concat([zb * zd, zb * zl, zd * zl], axis=1).max(axis=1)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_tridir_42d_jerk_v085_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 63)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    zl = _z(_f40_leverage(debt, equity, cashneq), 63)
    mag = np.sqrt(zb ** 2 + zd ** 2 + zl ** 2).replace(0, np.nan)
    base = (zb + zd + zl) / mag
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_triskew_42d_jerk_v086_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    zl = _z(_f40_leverage(debt, equity, cashneq), 126)
    s = zb + zd + zl
    m = _mean(s, 126)
    sd = _std(s, 126).replace(0, np.nan)
    base = ((s - m) / sd) ** 3
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_netrun_42d_jerk_v087_signal(cashneq, debt, ncfo):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    base = np.tanh((netcash / burn) / 6.0)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_solvm_42d_jerk_v088_signal(cashneq, equity, debt, ncfo):
    a = cashneq.clip(lower=0) + equity.clip(lower=0)
    b = debt.clip(lower=0) + (-ncfo).clip(lower=0.0)
    base = _logwarp((a + 1.0) / (b + 1.0))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eqburn_42d_jerk_v089_signal(equity, ncfo, cashneq):
    burn = (-ncfo).clip(lower=0.0)
    base = np.tanh(burn / (equity.abs() + 1.0)) * np.tanh(_f40_burn_pressure(cashneq, ncfo))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_bufdil_42d_jerk_v090_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    base = np.tanh((netcash / burn) / 4.0) - dil
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_obldist_42d_jerk_v091_signal(cashneq, ncfo, debt, opex):
    obl = debt.clip(lower=0) + (-ncfo).clip(lower=0.0)
    base = np.tanh((cashneq / (obl + opex.abs() * 0.1 + 1.0)) / 3.0)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_eqvsburn_42d_jerk_v092_signal(equity, ncfo, cashneq):
    cum = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).mean()
    cush = equity.clip(lower=0) + cashneq.clip(lower=0)
    base = np.tanh(_mean(cush, 126) / (cum + 1.0))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_monthsxdil_42d_jerk_v093_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    monthly = (-ncfo).clip(lower=0.0) / 12.0 + 1.0
    months = (netcash / monthly).clip(-60, 120)
    base = _z(-months, 252) * _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cashcover_42d_jerk_v094_signal(cashneq, debt, sbcomp, ncfo):
    need = debt.clip(lower=0) + sbcomp.clip(lower=0) + (-ncfo).clip(lower=0.0)
    base = np.tanh((cashneq / (need + 1.0)) / 2.0)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_resil_42d_jerk_v095_signal(cashneq, debt, ncfo, equity):
    buf = (cashneq - debt) / (equity.abs() + 1.0)
    base = _z(buf, 252) - 0.5 * (_z(_f40_burn_pressure(cashneq, ncfo), 252) + _z(_f40_leverage(debt, equity, cashneq), 252))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_burnamp_42d_jerk_v096_signal(cashneq, ncfo, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    cush = equity.abs().rolling(252, min_periods=126).mean() + 1.0
    base = np.tanh(bp * (cashneq.abs().rolling(252, min_periods=126).mean() + 1.0) / cush)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_negeqb_42d_jerk_v097_signal(equity, cashneq, ncfo):
    neg = (-_z(equity, 252)).clip(lower=0)
    base = np.tanh(_f40_burn_pressure(cashneq, ncfo)) * neg
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_burneq_42d_jerk_v098_signal(cashneq, ncfo, equity):
    eqdec = -(equity - equity.shift(63))
    base = _z(_f40_burn_pressure(cashneq, ncfo), 252) * _z(eqdec, 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_chronic_42d_jerk_v099_signal(ncfo, debt, equity, cashneq):
    bf = _mean((ncfo < 0).astype(float), 252)
    base = bf * np.tanh(_z(_f40_leverage(debt, equity, cashneq), 252))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cumdrag_42d_jerk_v100_signal(sharesbas, ncfo, cashneq):
    shr = (sharesbas / sharesbas.shift(252).replace(0, np.nan) - 1.0).clip(lower=0)
    base = shr * np.tanh(_mean(_f40_burn_pressure(cashneq, ncfo), 126))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_gbll_42d_jerk_v101_signal(cashneq, ncfo, debt, equity):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    lev = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = bp * (0.5 + 0.5 * np.tanh(lev))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_gdb_42d_jerk_v102_signal(ncfo, sbcomp, sharesbas, equity, cashneq):
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 126) * 5.0)
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    base = dil * bp
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dualmed_42d_jerk_v103_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    base = np.tanh(bp) * np.tanh(lev.clip(lower=0)) + 0.1 * _z(bp, 126)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_detbr_42d_jerk_v104_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 126)
    dil = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    lev = _z(_f40_leverage(debt, equity, cashneq), 126)
    base = (bp - bp.shift(63)) + (dil - dil.shift(63)) + (lev - lev.shift(63))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mdbl_42d_jerk_v105_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sign(comp) * np.log1p(comp.abs()) * (comp.abs().rolling(63, min_periods=21).rank(pct=True))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mdbd_42d_jerk_v106_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = np.sign(comp) * np.log1p(comp.abs()) * (comp.abs().rolling(63, min_periods=21).rank(pct=True))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mddl_42d_jerk_v107_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sign(comp) * np.log1p(comp.abs()) * (comp.abs().rolling(63, min_periods=21).rank(pct=True))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mdnl_42d_jerk_v108_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sign(comp) * np.log1p(comp.abs()) * (comp.abs().rolling(63, min_periods=21).rank(pct=True))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mdnd_42d_jerk_v109_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sign(comp) * np.log1p(comp.abs()) * (comp.abs().rolling(63, min_periods=21).rank(pct=True))
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewbl_42d_jerk_v110_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp - comp.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewbd_42d_jerk_v111_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = comp - comp.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewdl_42d_jerk_v112_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp - comp.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewnl_42d_jerk_v113_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp - comp.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_ewnd_42d_jerk_v114_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp - comp.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_vlbl_42d_jerk_v115_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = _std(comp, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_vlbd_42d_jerk_v116_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = _std(comp, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_vldl_42d_jerk_v117_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = _std(comp, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_vlnl_42d_jerk_v118_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = _std(comp, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_vlnd_42d_jerk_v119_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = _std(comp, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dvbl_42d_jerk_v120_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp - comp.shift(42)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dvbd_42d_jerk_v121_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = comp - comp.shift(42)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dvdl_42d_jerk_v122_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp - comp.shift(42)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dvnl_42d_jerk_v123_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp - comp.shift(42)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_dvnd_42d_jerk_v124_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp - comp.shift(42)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_abbl_42d_jerk_v125_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp.abs() - comp.abs().rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_abbd_42d_jerk_v126_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp.abs() - comp.abs().rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_abdl_42d_jerk_v127_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp.abs() - comp.abs().rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_abnl_42d_jerk_v128_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp.abs() - comp.abs().rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_abnd_42d_jerk_v129_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = comp.abs() - comp.abs().rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sgbl_42d_jerk_v130_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sign(comp).rolling(63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sgbd_42d_jerk_v131_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = np.sign(comp).rolling(63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sgdl_42d_jerk_v132_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = np.sign(comp).rolling(63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sgnl_42d_jerk_v133_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = np.sign(comp).rolling(63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_sgnd_42d_jerk_v134_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = np.sign(comp).rolling(63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_czbl_42d_jerk_v135_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = _rank(comp, 252) - _rank(comp.shift(63), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_czbd_42d_jerk_v136_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = _rank(comp, 252) - _rank(comp.shift(63), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_czdl_42d_jerk_v137_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = _rank(comp, 252) - _rank(comp.shift(63), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cznl_42d_jerk_v138_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = _rank(comp, 252) - _rank(comp.shift(63), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_cznd_42d_jerk_v139_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = _rank(comp, 252) - _rank(comp.shift(63), 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_smbl_42d_jerk_v140_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp.rolling(42, min_periods=14).mean() - comp.rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_smbd_42d_jerk_v141_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = comp.rolling(42, min_periods=14).mean() - comp.rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_smdl_42d_jerk_v142_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp.rolling(42, min_periods=14).mean() - comp.rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_smnl_42d_jerk_v143_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = comp.rolling(42, min_periods=14).mean() - comp.rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_smnd_42d_jerk_v144_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = comp.rolling(42, min_periods=14).mean() - comp.rolling(126, min_periods=42).mean()
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_posbl_42d_jerk_v145_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = (comp > 0).astype(float).rolling(126, min_periods=42).mean() - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_posbd_42d_jerk_v146_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_dilution(sbcomp, sharesbas, equity, 126), 126)
    base = (comp > 0).astype(float).rolling(126, min_periods=42).mean() - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_posdl_42d_jerk_v147_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63) * _z(_f40_leverage(debt, equity, cashneq), 63)
    base = (comp > 0).astype(float).rolling(126, min_periods=42).mean() - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_posnl_42d_jerk_v148_signal(ncfo, opex, debt, equity, cashneq):
    comp = _z(_f40_noprofit(ncfo, opex), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = (comp > 0).astype(float).rolling(126, min_periods=42).mean() - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_posnd_42d_jerk_v149_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _z(_f40_noprofit(ncfo, opex), 63) * _z(_f40_dilution(sbcomp, sharesbas, equity, 63), 63)
    base = (comp > 0).astype(float).rolling(126, min_periods=42).mean() - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f40cd_f40_cash_burn_distress_mxbl_42d_jerk_v150_signal(cashneq, ncfo, debt, equity):
    comp = _z(_f40_burn_pressure(cashneq, ncfo), 126) * _z(_f40_leverage(debt, equity, cashneq), 126)
    base = comp.rolling(126, min_periods=42).max() - comp
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / float(42 * 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cd_f40_cash_burn_distress_zpbl_42d_jerk_v001_signal,
    f40cd_f40_cash_burn_distress_zpbd_42d_jerk_v002_signal,
    f40cd_f40_cash_burn_distress_zpbn_42d_jerk_v003_signal,
    f40cd_f40_cash_burn_distress_zpdl_42d_jerk_v004_signal,
    f40cd_f40_cash_burn_distress_zpnl_42d_jerk_v005_signal,
    f40cd_f40_cash_burn_distress_zpnd_42d_jerk_v006_signal,
    f40cd_f40_cash_burn_distress_zmnbl_42d_jerk_v007_signal,
    f40cd_f40_cash_burn_distress_zmnbd_42d_jerk_v008_signal,
    f40cd_f40_cash_burn_distress_zmnbn_42d_jerk_v009_signal,
    f40cd_f40_cash_burn_distress_zmndl_42d_jerk_v010_signal,
    f40cd_f40_cash_burn_distress_zmnnl_42d_jerk_v011_signal,
    f40cd_f40_cash_burn_distress_zmnnd_42d_jerk_v012_signal,
    f40cd_f40_cash_burn_distress_zmxbl_42d_jerk_v013_signal,
    f40cd_f40_cash_burn_distress_zmxbd_42d_jerk_v014_signal,
    f40cd_f40_cash_burn_distress_zmxbn_42d_jerk_v015_signal,
    f40cd_f40_cash_burn_distress_zmxdl_42d_jerk_v016_signal,
    f40cd_f40_cash_burn_distress_zmxnl_42d_jerk_v017_signal,
    f40cd_f40_cash_burn_distress_zmxnd_42d_jerk_v018_signal,
    f40cd_f40_cash_burn_distress_zsgbl_42d_jerk_v019_signal,
    f40cd_f40_cash_burn_distress_zsgbd_42d_jerk_v020_signal,
    f40cd_f40_cash_burn_distress_zsgbn_42d_jerk_v021_signal,
    f40cd_f40_cash_burn_distress_zsgdl_42d_jerk_v022_signal,
    f40cd_f40_cash_burn_distress_zsgnl_42d_jerk_v023_signal,
    f40cd_f40_cash_burn_distress_zsgnd_42d_jerk_v024_signal,
    f40cd_f40_cash_burn_distress_sprbl_42d_jerk_v025_signal,
    f40cd_f40_cash_burn_distress_sprbd_42d_jerk_v026_signal,
    f40cd_f40_cash_burn_distress_sprbn_42d_jerk_v027_signal,
    f40cd_f40_cash_burn_distress_sprdl_42d_jerk_v028_signal,
    f40cd_f40_cash_burn_distress_sprnl_42d_jerk_v029_signal,
    f40cd_f40_cash_burn_distress_sprnd_42d_jerk_v030_signal,
    f40cd_f40_cash_burn_distress_rkpbl_42d_jerk_v031_signal,
    f40cd_f40_cash_burn_distress_rkpbd_42d_jerk_v032_signal,
    f40cd_f40_cash_burn_distress_rkpbn_42d_jerk_v033_signal,
    f40cd_f40_cash_burn_distress_rkpdl_42d_jerk_v034_signal,
    f40cd_f40_cash_burn_distress_rkpnl_42d_jerk_v035_signal,
    f40cd_f40_cash_burn_distress_rkpnd_42d_jerk_v036_signal,
    f40cd_f40_cash_burn_distress_ewpbl_42d_jerk_v037_signal,
    f40cd_f40_cash_burn_distress_ewpbd_42d_jerk_v038_signal,
    f40cd_f40_cash_burn_distress_ewpbn_42d_jerk_v039_signal,
    f40cd_f40_cash_burn_distress_ewpdl_42d_jerk_v040_signal,
    f40cd_f40_cash_burn_distress_ewpnl_42d_jerk_v041_signal,
    f40cd_f40_cash_burn_distress_ewpnd_42d_jerk_v042_signal,
    f40cd_f40_cash_burn_distress_hrmbl_42d_jerk_v043_signal,
    f40cd_f40_cash_burn_distress_hrmbd_42d_jerk_v044_signal,
    f40cd_f40_cash_burn_distress_hrmbn_42d_jerk_v045_signal,
    f40cd_f40_cash_burn_distress_hrmdl_42d_jerk_v046_signal,
    f40cd_f40_cash_burn_distress_hrmnl_42d_jerk_v047_signal,
    f40cd_f40_cash_burn_distress_hrmnd_42d_jerk_v048_signal,
    f40cd_f40_cash_burn_distress_tnpbl_42d_jerk_v049_signal,
    f40cd_f40_cash_burn_distress_tnpbd_42d_jerk_v050_signal,
    f40cd_f40_cash_burn_distress_tnpbn_42d_jerk_v051_signal,
    f40cd_f40_cash_burn_distress_tnpdl_42d_jerk_v052_signal,
    f40cd_f40_cash_burn_distress_tnpnl_42d_jerk_v053_signal,
    f40cd_f40_cash_burn_distress_tnpnd_42d_jerk_v054_signal,
    f40cd_f40_cash_burn_distress_eucbl_42d_jerk_v055_signal,
    f40cd_f40_cash_burn_distress_eucbd_42d_jerk_v056_signal,
    f40cd_f40_cash_burn_distress_eucbn_42d_jerk_v057_signal,
    f40cd_f40_cash_burn_distress_eucdl_42d_jerk_v058_signal,
    f40cd_f40_cash_burn_distress_eucnl_42d_jerk_v059_signal,
    f40cd_f40_cash_burn_distress_eucnd_42d_jerk_v060_signal,
    f40cd_f40_cash_burn_distress_lgtbl_42d_jerk_v061_signal,
    f40cd_f40_cash_burn_distress_lgtbd_42d_jerk_v062_signal,
    f40cd_f40_cash_burn_distress_lgtbn_42d_jerk_v063_signal,
    f40cd_f40_cash_burn_distress_lgtdl_42d_jerk_v064_signal,
    f40cd_f40_cash_burn_distress_lgtnl_42d_jerk_v065_signal,
    f40cd_f40_cash_burn_distress_lgtnd_42d_jerk_v066_signal,
    f40cd_f40_cash_burn_distress_cndbl_42d_jerk_v067_signal,
    f40cd_f40_cash_burn_distress_cndbd_42d_jerk_v068_signal,
    f40cd_f40_cash_burn_distress_cndbn_42d_jerk_v069_signal,
    f40cd_f40_cash_burn_distress_cnddl_42d_jerk_v070_signal,
    f40cd_f40_cash_burn_distress_cndnl_42d_jerk_v071_signal,
    f40cd_f40_cash_burn_distress_cndnd_42d_jerk_v072_signal,
    f40cd_f40_cash_burn_distress_triwa_42d_jerk_v073_signal,
    f40cd_f40_cash_burn_distress_triwb_42d_jerk_v074_signal,
    f40cd_f40_cash_burn_distress_triwc_42d_jerk_v075_signal,
    f40cd_f40_cash_burn_distress_trimin_42d_jerk_v076_signal,
    f40cd_f40_cash_burn_distress_trimax_42d_jerk_v077_signal,
    f40cd_f40_cash_burn_distress_trimean_42d_jerk_v078_signal,
    f40cd_f40_cash_burn_distress_trieuc_42d_jerk_v079_signal,
    f40cd_f40_cash_burn_distress_tridisp_42d_jerk_v080_signal,
    f40cd_f40_cash_burn_distress_trigeo_42d_jerk_v081_signal,
    f40cd_f40_cash_burn_distress_trilgt_42d_jerk_v082_signal,
    f40cd_f40_cash_burn_distress_triwpair_42d_jerk_v083_signal,
    f40cd_f40_cash_burn_distress_triprod_42d_jerk_v084_signal,
    f40cd_f40_cash_burn_distress_tridir_42d_jerk_v085_signal,
    f40cd_f40_cash_burn_distress_triskew_42d_jerk_v086_signal,
    f40cd_f40_cash_burn_distress_netrun_42d_jerk_v087_signal,
    f40cd_f40_cash_burn_distress_solvm_42d_jerk_v088_signal,
    f40cd_f40_cash_burn_distress_eqburn_42d_jerk_v089_signal,
    f40cd_f40_cash_burn_distress_bufdil_42d_jerk_v090_signal,
    f40cd_f40_cash_burn_distress_obldist_42d_jerk_v091_signal,
    f40cd_f40_cash_burn_distress_eqvsburn_42d_jerk_v092_signal,
    f40cd_f40_cash_burn_distress_monthsxdil_42d_jerk_v093_signal,
    f40cd_f40_cash_burn_distress_cashcover_42d_jerk_v094_signal,
    f40cd_f40_cash_burn_distress_resil_42d_jerk_v095_signal,
    f40cd_f40_cash_burn_distress_burnamp_42d_jerk_v096_signal,
    f40cd_f40_cash_burn_distress_negeqb_42d_jerk_v097_signal,
    f40cd_f40_cash_burn_distress_burneq_42d_jerk_v098_signal,
    f40cd_f40_cash_burn_distress_chronic_42d_jerk_v099_signal,
    f40cd_f40_cash_burn_distress_cumdrag_42d_jerk_v100_signal,
    f40cd_f40_cash_burn_distress_gbll_42d_jerk_v101_signal,
    f40cd_f40_cash_burn_distress_gdb_42d_jerk_v102_signal,
    f40cd_f40_cash_burn_distress_dualmed_42d_jerk_v103_signal,
    f40cd_f40_cash_burn_distress_detbr_42d_jerk_v104_signal,
    f40cd_f40_cash_burn_distress_mdbl_42d_jerk_v105_signal,
    f40cd_f40_cash_burn_distress_mdbd_42d_jerk_v106_signal,
    f40cd_f40_cash_burn_distress_mddl_42d_jerk_v107_signal,
    f40cd_f40_cash_burn_distress_mdnl_42d_jerk_v108_signal,
    f40cd_f40_cash_burn_distress_mdnd_42d_jerk_v109_signal,
    f40cd_f40_cash_burn_distress_ewbl_42d_jerk_v110_signal,
    f40cd_f40_cash_burn_distress_ewbd_42d_jerk_v111_signal,
    f40cd_f40_cash_burn_distress_ewdl_42d_jerk_v112_signal,
    f40cd_f40_cash_burn_distress_ewnl_42d_jerk_v113_signal,
    f40cd_f40_cash_burn_distress_ewnd_42d_jerk_v114_signal,
    f40cd_f40_cash_burn_distress_vlbl_42d_jerk_v115_signal,
    f40cd_f40_cash_burn_distress_vlbd_42d_jerk_v116_signal,
    f40cd_f40_cash_burn_distress_vldl_42d_jerk_v117_signal,
    f40cd_f40_cash_burn_distress_vlnl_42d_jerk_v118_signal,
    f40cd_f40_cash_burn_distress_vlnd_42d_jerk_v119_signal,
    f40cd_f40_cash_burn_distress_dvbl_42d_jerk_v120_signal,
    f40cd_f40_cash_burn_distress_dvbd_42d_jerk_v121_signal,
    f40cd_f40_cash_burn_distress_dvdl_42d_jerk_v122_signal,
    f40cd_f40_cash_burn_distress_dvnl_42d_jerk_v123_signal,
    f40cd_f40_cash_burn_distress_dvnd_42d_jerk_v124_signal,
    f40cd_f40_cash_burn_distress_abbl_42d_jerk_v125_signal,
    f40cd_f40_cash_burn_distress_abbd_42d_jerk_v126_signal,
    f40cd_f40_cash_burn_distress_abdl_42d_jerk_v127_signal,
    f40cd_f40_cash_burn_distress_abnl_42d_jerk_v128_signal,
    f40cd_f40_cash_burn_distress_abnd_42d_jerk_v129_signal,
    f40cd_f40_cash_burn_distress_sgbl_42d_jerk_v130_signal,
    f40cd_f40_cash_burn_distress_sgbd_42d_jerk_v131_signal,
    f40cd_f40_cash_burn_distress_sgdl_42d_jerk_v132_signal,
    f40cd_f40_cash_burn_distress_sgnl_42d_jerk_v133_signal,
    f40cd_f40_cash_burn_distress_sgnd_42d_jerk_v134_signal,
    f40cd_f40_cash_burn_distress_czbl_42d_jerk_v135_signal,
    f40cd_f40_cash_burn_distress_czbd_42d_jerk_v136_signal,
    f40cd_f40_cash_burn_distress_czdl_42d_jerk_v137_signal,
    f40cd_f40_cash_burn_distress_cznl_42d_jerk_v138_signal,
    f40cd_f40_cash_burn_distress_cznd_42d_jerk_v139_signal,
    f40cd_f40_cash_burn_distress_smbl_42d_jerk_v140_signal,
    f40cd_f40_cash_burn_distress_smbd_42d_jerk_v141_signal,
    f40cd_f40_cash_burn_distress_smdl_42d_jerk_v142_signal,
    f40cd_f40_cash_burn_distress_smnl_42d_jerk_v143_signal,
    f40cd_f40_cash_burn_distress_smnd_42d_jerk_v144_signal,
    f40cd_f40_cash_burn_distress_posbl_42d_jerk_v145_signal,
    f40cd_f40_cash_burn_distress_posbd_42d_jerk_v146_signal,
    f40cd_f40_cash_burn_distress_posdl_42d_jerk_v147_signal,
    f40cd_f40_cash_burn_distress_posnl_42d_jerk_v148_signal,
    f40cd_f40_cash_burn_distress_posnd_42d_jerk_v149_signal,
    f40cd_f40_cash_burn_distress_mxbl_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CASH_BURN_DISTRESS_REGISTRY_JERK_001_150 = REGISTRY


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis", "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, amp=0.0):
        g = np.random.default_rng(seed)
        nq = n // 63 + 1
        steps = np.repeat(g.normal(drift, vol, nq), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if amp:
            cyc = np.repeat(g.normal(0.0, 1.0, nq), 63)[:n]
            s = s + amp * base * cyc
        e = g.normal(0.0, 0.06, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = 0.9 * ar[t - 1] + e[t]
        s = s * (1.0 + ar)
        return pd.Series(s, name=None)

    cashneq = _fund(1, base=1.5e8, drift=-0.01, vol=0.08, amp=0.6).rename("cashneq")
    ncfo = _fund(2, base=1.0e8, drift=0.01, vol=0.10, amp=1.3).rename("ncfo")
    sbcomp = _fund(3, base=2e7, drift=0.03, vol=0.06, amp=0.5).rename("sbcomp")
    sharesbas = _fund(4, base=1e8, drift=0.02, vol=0.02).rename("sharesbas")
    debt = _fund(5, base=1.3e8, drift=0.03, vol=0.08, amp=0.7).rename("debt")
    equity = _fund(6, base=2.0e8, drift=0.01, vol=0.06, amp=1.2).rename("equity")
    opex = _fund(7, base=2.5e8, drift=0.02, vol=0.05, amp=0.3).rename("opex")

    cols = {"cashneq": cashneq, "ncfo": ncfo, "sbcomp": sbcomp, "sharesbas": sharesbas,
            "debt": debt, "equity": equity, "opex": opex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f40_cash_burn_distress_3rd_derivatives_001_150_claude: %d features pass" % n_features)
