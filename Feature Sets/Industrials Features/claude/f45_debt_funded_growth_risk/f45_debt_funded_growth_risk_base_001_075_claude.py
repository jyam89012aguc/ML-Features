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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f45_debt_asset_gap(debt, assets, w):
    dg = debt.pct_change(periods=w)
    ag = assets.pct_change(periods=w)
    return dg - ag


def _f45_debt_funded_growth(debt, revenue, w):
    dg = debt.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return dg / rg.replace(0, np.nan)


def _f45_acquisition_intensity(intangibles, debt, w):
    ig = intangibles.pct_change(periods=w)
    dg = debt.pct_change(periods=w)
    return ig + dg

# feature 1: da_gap_5d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xc_base_v001_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 2: da_gap_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xclog_base_v002_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 3: da_gap_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xcm21_base_v003_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 4: da_gap_10d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xc_base_v004_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 5: da_gap_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xclog_base_v005_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 6: da_gap_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xcm21_base_v006_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 7: da_gap_21d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xc_base_v007_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 8: da_gap_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xclog_base_v008_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 9: da_gap_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xcm21_base_v009_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 10: da_gap_42d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xc_base_v010_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 11: da_gap_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xclog_base_v011_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 12: da_gap_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xcm21_base_v012_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 13: da_gap_63d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xc_base_v013_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 14: da_gap_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xclog_base_v014_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 15: da_gap_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xcm21_base_v015_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 16: da_gap_126d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xc_base_v016_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 17: da_gap_126d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xclog_base_v017_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 18: da_gap_126d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xcm21_base_v018_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 19: da_gap_189d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xc_base_v019_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 20: da_gap_189d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xclog_base_v020_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 21: da_gap_189d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xcm21_base_v021_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 22: da_gap_252d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xc_base_v022_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 23: da_gap_252d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xclog_base_v023_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 24: da_gap_252d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xcm21_base_v024_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 25: da_gap_378d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xc_base_v025_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 26: da_gap_378d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xclog_base_v026_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 27: da_gap_378d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xcm21_base_v027_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 28: da_gap_504d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xc_base_v028_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 29: da_gap_504d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xclog_base_v029_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 30: da_gap_504d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xcm21_base_v030_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 31: dfg_5d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xc_base_v031_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 32: dfg_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xclog_base_v032_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 33: dfg_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xcm21_base_v033_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 34: dfg_10d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xc_base_v034_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 35: dfg_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xclog_base_v035_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 36: dfg_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xcm21_base_v036_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 37: dfg_21d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xc_base_v037_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 38: dfg_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xclog_base_v038_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 39: dfg_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xcm21_base_v039_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 40: dfg_42d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xc_base_v040_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 41: dfg_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xclog_base_v041_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 42: dfg_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xcm21_base_v042_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 43: dfg_63d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xc_base_v043_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 44: dfg_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xclog_base_v044_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 45: dfg_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xcm21_base_v045_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 46: dfg_126d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xc_base_v046_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 47: dfg_126d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xclog_base_v047_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 48: dfg_126d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xcm21_base_v048_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 49: dfg_189d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xc_base_v049_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 50: dfg_189d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xclog_base_v050_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 51: dfg_189d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xcm21_base_v051_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 52: dfg_252d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xc_base_v052_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 53: dfg_252d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xclog_base_v053_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 54: dfg_252d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xcm21_base_v054_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 55: dfg_378d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xc_base_v055_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 56: dfg_378d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xclog_base_v056_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 57: dfg_378d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xcm21_base_v057_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 58: dfg_504d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xc_base_v058_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = sm * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 59: dfg_504d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xclog_base_v059_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = sm * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 60: dfg_504d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xcm21_base_v060_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = sm * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 61: acqint_5d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xc_base_v061_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 62: acqint_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xclog_base_v062_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 63: acqint_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xcm21_base_v063_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 64: acqint_10d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xc_base_v064_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 65: acqint_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xclog_base_v065_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 66: acqint_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xcm21_base_v066_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 67: acqint_21d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xc_base_v067_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 68: acqint_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xclog_base_v068_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 69: acqint_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xcm21_base_v069_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 70: acqint_42d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xc_base_v070_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 71: acqint_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xclog_base_v071_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 72: acqint_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xcm21_base_v072_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 73: acqint_63d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xc_base_v073_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 74: acqint_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xclog_base_v074_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 75: acqint_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xcm21_base_v075_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xc_base_v001_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xclog_base_v002_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xcm21_base_v003_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xc_base_v004_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xclog_base_v005_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xcm21_base_v006_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xc_base_v007_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xclog_base_v008_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xcm21_base_v009_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xc_base_v010_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xclog_base_v011_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xcm21_base_v012_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xc_base_v013_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xclog_base_v014_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xcm21_base_v015_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xc_base_v016_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xclog_base_v017_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xcm21_base_v018_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xc_base_v019_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xclog_base_v020_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xcm21_base_v021_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xc_base_v022_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xclog_base_v023_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xcm21_base_v024_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xc_base_v025_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xclog_base_v026_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xcm21_base_v027_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xc_base_v028_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xclog_base_v029_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xcm21_base_v030_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xc_base_v031_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xclog_base_v032_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xcm21_base_v033_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xc_base_v034_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xclog_base_v035_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xcm21_base_v036_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xc_base_v037_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xclog_base_v038_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xcm21_base_v039_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xc_base_v040_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xclog_base_v041_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xcm21_base_v042_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xc_base_v043_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xclog_base_v044_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xcm21_base_v045_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xc_base_v046_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xclog_base_v047_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xcm21_base_v048_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xc_base_v049_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xclog_base_v050_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xcm21_base_v051_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xc_base_v052_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xclog_base_v053_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xcm21_base_v054_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xc_base_v055_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xclog_base_v056_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xcm21_base_v057_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xc_base_v058_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xclog_base_v059_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xcm21_base_v060_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xc_base_v061_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xclog_base_v062_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xcm21_base_v063_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xc_base_v064_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xclog_base_v065_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xcm21_base_v066_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xc_base_v067_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xclog_base_v068_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xcm21_base_v069_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xc_base_v070_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xclog_base_v071_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xcm21_base_v072_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xc_base_v073_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xclog_base_v074_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xcm21_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_DEBT_FUNDED_GROWTH_RISK_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f45_debt_asset_gap', '_f45_debt_funded_growth', '_f45_acquisition_intensity')
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
    print(f"OK f45_debt_funded_growth_risk_base_001_075_claude: {n_features} features pass")
