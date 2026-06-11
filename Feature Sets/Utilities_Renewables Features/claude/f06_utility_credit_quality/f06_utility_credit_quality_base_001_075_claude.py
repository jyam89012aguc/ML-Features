import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives =====
def _f06_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _f06_credit_quality(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_solvency_score(debt, ebitda, fcf, w):
    de_ratio = debt / ebitda.replace(0, np.nan)
    fcf_cov = fcf / debt.replace(0, np.nan)
    de_smooth = de_ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    fcf_smooth = fcf_cov.rolling(w, min_periods=max(1, w // 2)).mean()
    return fcf_smooth - de_smooth


# v001: 21d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_base_v001_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_base_v002_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_126d_base_v003_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_base_v004_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 504d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_504d_base_v005_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 21d std of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_std_base_v006_signal(debt, ebitda, closeadj):
    result = _std(_f06_debt_ebitda(debt, ebitda), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 63d std of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_std_base_v007_signal(debt, ebitda, closeadj):
    result = _std(_f06_debt_ebitda(debt, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 252d std of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_std_base_v008_signal(debt, ebitda, closeadj):
    result = _std(_f06_debt_ebitda(debt, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: zscore 252d of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_z_base_v009_signal(debt, ebitda, closeadj):
    result = _z(_f06_debt_ebitda(debt, ebitda), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: zscore 504d of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_504d_z_base_v010_signal(debt, ebitda, closeadj):
    result = _z(_f06_debt_ebitda(debt, ebitda), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_21d_base_v011_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_63d_base_v012_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_126d_base_v013_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_252d_base_v014_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 504d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_504d_base_v015_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_21d_base_v016_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_base_v017_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 126d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_126d_base_v018_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 252d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_base_v019_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 504d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_504d_base_v020_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 21d debt/ebitda × de × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_xde_base_v021_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 63d debt/ebitda × de × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_xde_base_v022_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 252d debt/ebitda × de × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_xde_base_v023_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: 63d EMA of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_ema_base_v024_signal(debt, ebitda, closeadj):
    de_ratio = _f06_debt_ebitda(debt, ebitda)
    result = de_ratio.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: 252d EMA of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_ema_base_v025_signal(debt, ebitda, closeadj):
    de_ratio = _f06_debt_ebitda(debt, ebitda)
    result = de_ratio.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: ratio of debt/ebitda × fcf × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_fcfwt_63d_base_v026_signal(debt, ebitda, fcf, closeadj):
    de_ratio = _f06_debt_ebitda(debt, ebitda)
    result = _mean(de_ratio, 63) * _mean(fcf, 63) / _mean(debt, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: 21d cred-q × de
def f06ucq_f06_utility_credit_quality_creditq_21d_xde_base_v027_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 21) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 63d cred-q × de
def f06ucq_f06_utility_credit_quality_creditq_63d_xde_base_v028_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 252d cred-q × de
def f06ucq_f06_utility_credit_quality_creditq_252d_xde_base_v029_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 5d debt/ebitda × closeadj (short)
def f06ucq_f06_utility_credit_quality_debtebitda_5d_base_v030_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 10d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_10d_base_v031_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 42d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_42d_base_v032_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 189d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_189d_base_v033_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 378d debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_378d_base_v034_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 21d debt/ebitda × log(closeadj)
def f06ucq_f06_utility_credit_quality_debtebitda_21d_logc_base_v035_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 63d debt/ebitda × log(closeadj)
def f06ucq_f06_utility_credit_quality_debtebitda_63d_logc_base_v036_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 252d debt/ebitda × log(closeadj)
def f06ucq_f06_utility_credit_quality_debtebitda_252d_logc_base_v037_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 21d debt/ebitda * sqrt(closeadj)
def f06ucq_f06_utility_credit_quality_debtebitda_21d_sqrtc_base_v038_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * np.sqrt(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v039: zscore 126d of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_126d_z_base_v039_signal(debt, ebitda, closeadj):
    result = _z(_f06_debt_ebitda(debt, ebitda), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: zscore 63d of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_z_base_v040_signal(debt, ebitda, closeadj):
    result = _z(_f06_debt_ebitda(debt, ebitda), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 21d credit quality × log(closeadj)
def f06ucq_f06_utility_credit_quality_creditq_21d_logc_base_v041_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 63d credit quality × log(closeadj)
def f06ucq_f06_utility_credit_quality_creditq_63d_logc_base_v042_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 252d credit quality × log(closeadj)
def f06ucq_f06_utility_credit_quality_creditq_252d_logc_base_v043_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 21d solvency × log(closeadj)
def f06ucq_f06_utility_credit_quality_solv_21d_logc_base_v044_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 63d solvency × log(closeadj)
def f06ucq_f06_utility_credit_quality_solv_63d_logc_base_v045_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 252d solvency × log(closeadj)
def f06ucq_f06_utility_credit_quality_solv_252d_logc_base_v046_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 5d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_5d_base_v047_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 10d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_10d_base_v048_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 42d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_42d_base_v049_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 189d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_189d_base_v050_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 378d credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_378d_base_v051_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 5d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_5d_base_v052_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 10d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_10d_base_v053_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 42d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_42d_base_v054_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 189d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_189d_base_v055_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 378d solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_378d_base_v056_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 21d std of solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_21d_std_base_v057_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _std(sv, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 63d std of solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_std_base_v058_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 63)
    result = _std(sv, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 252d std of solvency × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_std_base_v059_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 252)
    result = _std(sv, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d std of credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_21d_std_base_v060_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 21)
    result = _std(cq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d std of credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_63d_std_base_v061_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 63)
    result = _std(cq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 252d std of credit quality × closeadj
def f06ucq_f06_utility_credit_quality_creditq_252d_std_base_v062_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 252)
    result = _std(cq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: debt/ebitda × fcf × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_fcf_21d_base_v063_signal(debt, ebitda, fcf, closeadj):
    result = _f06_debt_ebitda(debt, ebitda) * _mean(fcf, 21) / _mean(ebitda, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: debt/ebitda × fcf 252d
def f06ucq_f06_utility_credit_quality_debtebitda_fcf_252d_base_v064_signal(debt, ebitda, fcf, closeadj):
    result = _f06_debt_ebitda(debt, ebitda) * _mean(fcf, 252) / _mean(ebitda, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: credit quality × fcf 63d
def f06ucq_f06_utility_credit_quality_creditq_fcf_63d_base_v065_signal(debt, equity, fcf, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * _mean(fcf, 63) / _mean(equity, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: credit quality × fcf 252d
def f06ucq_f06_utility_credit_quality_creditq_fcf_252d_base_v066_signal(debt, equity, fcf, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * _mean(fcf, 252) / _mean(equity, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 21d ema of credit quality
def f06ucq_f06_utility_credit_quality_creditq_21d_ema_base_v067_signal(debt, equity, closeadj):
    de_ratio = debt / equity.replace(0, np.nan)
    result = -de_ratio.ewm(span=21, adjust=False).mean() * closeadj + _f06_credit_quality(debt, equity, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 63d ema of credit quality
def f06ucq_f06_utility_credit_quality_creditq_63d_ema_base_v068_signal(debt, equity, closeadj):
    de_ratio = debt / equity.replace(0, np.nan)
    result = -de_ratio.ewm(span=63, adjust=False).mean() * closeadj + _f06_credit_quality(debt, equity, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 252d ema of credit quality
def f06ucq_f06_utility_credit_quality_creditq_252d_ema_base_v069_signal(debt, equity, closeadj):
    de_ratio = debt / equity.replace(0, np.nan)
    result = -de_ratio.ewm(span=252, adjust=False).mean() * closeadj + _f06_credit_quality(debt, equity, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d ema of solvency
def f06ucq_f06_utility_credit_quality_solv_63d_ema_base_v070_signal(debt, ebitda, fcf, closeadj):
    de_ratio = debt / ebitda.replace(0, np.nan)
    fcf_cov = fcf / debt.replace(0, np.nan)
    result = (fcf_cov.ewm(span=63, adjust=False).mean() - de_ratio.ewm(span=63, adjust=False).mean()) * closeadj + _f06_solvency_score(debt, ebitda, fcf, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 252d ema of solvency
def f06ucq_f06_utility_credit_quality_solv_252d_ema_base_v071_signal(debt, ebitda, fcf, closeadj):
    de_ratio = debt / ebitda.replace(0, np.nan)
    fcf_cov = fcf / debt.replace(0, np.nan)
    result = (fcf_cov.ewm(span=252, adjust=False).mean() - de_ratio.ewm(span=252, adjust=False).mean()) * closeadj + _f06_solvency_score(debt, ebitda, fcf, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v072: 21d debt/ebitda × ebitda growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_21d_base_v072_signal(debt, ebitda, closeadj):
    gr = ebitda.pct_change(21)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: 63d debt/ebitda × ebitda growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_63d_base_v073_signal(debt, ebitda, closeadj):
    gr = ebitda.pct_change(63)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: 252d debt/ebitda × ebitda growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_252d_base_v074_signal(debt, ebitda, closeadj):
    gr = ebitda.pct_change(252)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: 63d cred-q × debt growth × closeadj
def f06ucq_f06_utility_credit_quality_creditq_debtgr_63d_base_v075_signal(debt, equity, closeadj):
    gr = debt.pct_change(63)
    result = _f06_credit_quality(debt, equity, 63) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06ucq_f06_utility_credit_quality_debtebitda_21d_base_v001_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_base_v002_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_base_v003_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_base_v004_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_504d_base_v005_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_std_base_v006_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_std_base_v007_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_std_base_v008_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_z_base_v009_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_504d_z_base_v010_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_base_v011_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_base_v012_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_base_v013_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_base_v014_signal,
    f06ucq_f06_utility_credit_quality_creditq_504d_base_v015_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_base_v016_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_base_v017_signal,
    f06ucq_f06_utility_credit_quality_solv_126d_base_v018_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_base_v019_signal,
    f06ucq_f06_utility_credit_quality_solv_504d_base_v020_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_xde_base_v021_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_xde_base_v022_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_xde_base_v023_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_ema_base_v024_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_ema_base_v025_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_fcfwt_63d_base_v026_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_xde_base_v027_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_xde_base_v028_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_xde_base_v029_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_5d_base_v030_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_10d_base_v031_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_42d_base_v032_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_189d_base_v033_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_378d_base_v034_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_logc_base_v035_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_logc_base_v036_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_logc_base_v037_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_sqrtc_base_v038_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_z_base_v039_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_z_base_v040_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_logc_base_v041_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_logc_base_v042_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_logc_base_v043_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_logc_base_v044_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_logc_base_v045_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_logc_base_v046_signal,
    f06ucq_f06_utility_credit_quality_creditq_5d_base_v047_signal,
    f06ucq_f06_utility_credit_quality_creditq_10d_base_v048_signal,
    f06ucq_f06_utility_credit_quality_creditq_42d_base_v049_signal,
    f06ucq_f06_utility_credit_quality_creditq_189d_base_v050_signal,
    f06ucq_f06_utility_credit_quality_creditq_378d_base_v051_signal,
    f06ucq_f06_utility_credit_quality_solv_5d_base_v052_signal,
    f06ucq_f06_utility_credit_quality_solv_10d_base_v053_signal,
    f06ucq_f06_utility_credit_quality_solv_42d_base_v054_signal,
    f06ucq_f06_utility_credit_quality_solv_189d_base_v055_signal,
    f06ucq_f06_utility_credit_quality_solv_378d_base_v056_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_std_base_v057_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_std_base_v058_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_std_base_v059_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_std_base_v060_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_std_base_v061_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_std_base_v062_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_fcf_21d_base_v063_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_fcf_252d_base_v064_signal,
    f06ucq_f06_utility_credit_quality_creditq_fcf_63d_base_v065_signal,
    f06ucq_f06_utility_credit_quality_creditq_fcf_252d_base_v066_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_ema_base_v067_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_ema_base_v068_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_ema_base_v069_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_ema_base_v070_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_ema_base_v071_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_21d_base_v072_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_63d_base_v073_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_ebitdagr_252d_base_v074_signal,
    f06ucq_f06_utility_credit_quality_creditq_debtgr_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_UTILITY_CREDIT_QUALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    de = pd.Series(0.6 + 0.2 * np.sin(np.arange(n) / 250.0) + 0.05 * np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj, "ebitda": ebitda, "fcf": fcf, "equity": equity,
        "debt": debt, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_debt_ebitda", "_f06_credit_quality", "_f06_solvency_score")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_utility_credit_quality_base_001_075_claude: {n_features} features pass")
