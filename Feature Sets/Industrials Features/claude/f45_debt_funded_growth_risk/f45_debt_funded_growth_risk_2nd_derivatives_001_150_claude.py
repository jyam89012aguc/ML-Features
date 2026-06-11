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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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

# slope feature 1: da_gap_5d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xc_5d_slope_v001_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 2: da_gap_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xclog_10d_slope_v002_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 3: da_gap_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xcm21_21d_slope_v003_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 4: da_gap_10d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xc_42d_slope_v004_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 5: da_gap_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xclog_63d_slope_v005_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 6: da_gap_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xcm21_126d_slope_v006_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 7: da_gap_21d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xc_5d_slope_v007_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 8: da_gap_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xclog_10d_slope_v008_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 9: da_gap_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xcm21_21d_slope_v009_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 10: da_gap_42d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xc_42d_slope_v010_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 11: da_gap_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xclog_63d_slope_v011_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 12: da_gap_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xcm21_126d_slope_v012_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 13: da_gap_63d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xc_5d_slope_v013_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 14: da_gap_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xclog_10d_slope_v014_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 15: da_gap_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xcm21_21d_slope_v015_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 16: da_gap_126d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xc_42d_slope_v016_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 17: da_gap_126d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xclog_63d_slope_v017_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 18: da_gap_126d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xcm21_126d_slope_v018_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 19: da_gap_189d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xc_5d_slope_v019_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 20: da_gap_189d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xclog_10d_slope_v020_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 21: da_gap_189d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xcm21_21d_slope_v021_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 22: da_gap_252d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xc_42d_slope_v022_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 23: da_gap_252d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xclog_63d_slope_v023_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 24: da_gap_252d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xcm21_126d_slope_v024_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 25: da_gap_378d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xc_5d_slope_v025_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 26: da_gap_378d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xclog_10d_slope_v026_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 27: da_gap_378d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xcm21_21d_slope_v027_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 28: da_gap_504d_xc
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xc_42d_slope_v028_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 29: da_gap_504d_xclog
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xclog_63d_slope_v029_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 30: da_gap_504d_xcm21
def f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xcm21_126d_slope_v030_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 31: dfg_5d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xc_5d_slope_v031_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 32: dfg_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xclog_10d_slope_v032_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 33: dfg_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_5d_xcm21_21d_slope_v033_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 5)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 34: dfg_10d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xc_42d_slope_v034_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 35: dfg_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xclog_63d_slope_v035_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 36: dfg_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_10d_xcm21_126d_slope_v036_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 10)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 37: dfg_21d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xc_5d_slope_v037_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 38: dfg_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xclog_10d_slope_v038_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 39: dfg_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_21d_xcm21_21d_slope_v039_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 40: dfg_42d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xc_42d_slope_v040_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 41: dfg_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xclog_63d_slope_v041_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 42: dfg_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_42d_xcm21_126d_slope_v042_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 43: dfg_63d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xc_5d_slope_v043_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 44: dfg_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xclog_10d_slope_v044_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 45: dfg_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_63d_xcm21_21d_slope_v045_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 46: dfg_126d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xc_42d_slope_v046_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 47: dfg_126d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xclog_63d_slope_v047_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 48: dfg_126d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_126d_xcm21_126d_slope_v048_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 49: dfg_189d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xc_5d_slope_v049_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 50: dfg_189d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xclog_10d_slope_v050_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 51: dfg_189d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_189d_xcm21_21d_slope_v051_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 189)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 52: dfg_252d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xc_42d_slope_v052_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 53: dfg_252d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xclog_63d_slope_v053_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 54: dfg_252d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_252d_xcm21_126d_slope_v054_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 55: dfg_378d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xc_5d_slope_v055_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 56: dfg_378d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xclog_10d_slope_v056_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 57: dfg_378d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_378d_xcm21_21d_slope_v057_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 378)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 58: dfg_504d_xc
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xc_42d_slope_v058_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 59: dfg_504d_xclog
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xclog_63d_slope_v059_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 60: dfg_504d_xcm21
def f45dfg_f45_debt_funded_growth_risk_dfg_504d_xcm21_126d_slope_v060_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 504)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 61: acqint_5d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xc_5d_slope_v061_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 62: acqint_5d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xclog_10d_slope_v062_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 63: acqint_5d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_5d_xcm21_21d_slope_v063_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 64: acqint_10d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xc_42d_slope_v064_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 65: acqint_10d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xclog_63d_slope_v065_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 66: acqint_10d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_10d_xcm21_126d_slope_v066_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 67: acqint_21d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xc_5d_slope_v067_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 68: acqint_21d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xclog_10d_slope_v068_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 69: acqint_21d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_21d_xcm21_21d_slope_v069_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 70: acqint_42d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xc_42d_slope_v070_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 71: acqint_42d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xclog_63d_slope_v071_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 72: acqint_42d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_42d_xcm21_126d_slope_v072_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 73: acqint_63d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xc_5d_slope_v073_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 74: acqint_63d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xclog_10d_slope_v074_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 75: acqint_63d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_63d_xcm21_21d_slope_v075_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 76: acqint_126d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_126d_xc_42d_slope_v076_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 77: acqint_126d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_126d_xclog_63d_slope_v077_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 78: acqint_126d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_126d_xcm21_126d_slope_v078_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 79: acqint_189d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_189d_xc_5d_slope_v079_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 80: acqint_189d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_189d_xclog_10d_slope_v080_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 81: acqint_189d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_189d_xcm21_21d_slope_v081_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 82: acqint_252d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_252d_xc_42d_slope_v082_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 83: acqint_252d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_252d_xclog_63d_slope_v083_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 84: acqint_252d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_252d_xcm21_126d_slope_v084_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 85: acqint_378d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_378d_xc_5d_slope_v085_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 86: acqint_378d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_378d_xclog_10d_slope_v086_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 87: acqint_378d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_378d_xcm21_21d_slope_v087_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 88: acqint_504d_xc
def f45dfg_f45_debt_funded_growth_risk_acqint_504d_xc_42d_slope_v088_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 89: acqint_504d_xclog
def f45dfg_f45_debt_funded_growth_risk_acqint_504d_xclog_63d_slope_v089_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 90: acqint_504d_xcm21
def f45dfg_f45_debt_funded_growth_risk_acqint_504d_xcm21_126d_slope_v090_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 91: gapxacq_21d
def f45dfg_f45_debt_funded_growth_risk_gapxacq_21d_5d_slope_v091_signal(debt, assets, intangibles, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 21)
    b = _f45_acquisition_intensity(intangibles, debt, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 92: dfgxacq_21d
def f45dfg_f45_debt_funded_growth_risk_dfgxacq_21d_10d_slope_v092_signal(debt, revenue, intangibles, closeadj):
    a = _f45_debt_funded_growth(debt, revenue, 21)
    b = _f45_acquisition_intensity(intangibles, debt, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 93: gap_z_21d
def f45dfg_f45_debt_funded_growth_risk_gap_z_21d_21d_slope_v093_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 94: dfg_z_21d
def f45dfg_f45_debt_funded_growth_risk_dfg_z_21d_42d_slope_v094_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 95: acq_z_21d
def f45dfg_f45_debt_funded_growth_risk_acq_z_21d_63d_slope_v095_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 96: gap_ema_21d
def f45dfg_f45_debt_funded_growth_risk_gap_ema_21d_126d_slope_v096_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 97: dfg_ema_21d
def f45dfg_f45_debt_funded_growth_risk_dfg_ema_21d_5d_slope_v097_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 98: acq_ema_21d
def f45dfg_f45_debt_funded_growth_risk_acq_ema_21d_10d_slope_v098_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 99: gap_sq_21d
def f45dfg_f45_debt_funded_growth_risk_gap_sq_21d_21d_slope_v099_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 100: acq_sq_21d
def f45dfg_f45_debt_funded_growth_risk_acq_sq_21d_42d_slope_v100_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 21)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 101: gapxdfg_21d
def f45dfg_f45_debt_funded_growth_risk_gapxdfg_21d_63d_slope_v101_signal(debt, assets, revenue, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 21)
    b = _f45_debt_funded_growth(debt, revenue, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 102: gapxacq_42d
def f45dfg_f45_debt_funded_growth_risk_gapxacq_42d_126d_slope_v102_signal(debt, assets, intangibles, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 42)
    b = _f45_acquisition_intensity(intangibles, debt, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 103: dfgxacq_42d
def f45dfg_f45_debt_funded_growth_risk_dfgxacq_42d_5d_slope_v103_signal(debt, revenue, intangibles, closeadj):
    a = _f45_debt_funded_growth(debt, revenue, 42)
    b = _f45_acquisition_intensity(intangibles, debt, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 104: gap_z_42d
def f45dfg_f45_debt_funded_growth_risk_gap_z_42d_10d_slope_v104_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 105: dfg_z_42d
def f45dfg_f45_debt_funded_growth_risk_dfg_z_42d_21d_slope_v105_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 106: acq_z_42d
def f45dfg_f45_debt_funded_growth_risk_acq_z_42d_42d_slope_v106_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 107: gap_ema_42d
def f45dfg_f45_debt_funded_growth_risk_gap_ema_42d_63d_slope_v107_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 108: dfg_ema_42d
def f45dfg_f45_debt_funded_growth_risk_dfg_ema_42d_126d_slope_v108_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 109: acq_ema_42d
def f45dfg_f45_debt_funded_growth_risk_acq_ema_42d_5d_slope_v109_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 110: gap_sq_42d
def f45dfg_f45_debt_funded_growth_risk_gap_sq_42d_10d_slope_v110_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 111: acq_sq_42d
def f45dfg_f45_debt_funded_growth_risk_acq_sq_42d_21d_slope_v111_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 112: gapxdfg_42d
def f45dfg_f45_debt_funded_growth_risk_gapxdfg_42d_42d_slope_v112_signal(debt, assets, revenue, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 42)
    b = _f45_debt_funded_growth(debt, revenue, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 113: gapxacq_63d
def f45dfg_f45_debt_funded_growth_risk_gapxacq_63d_63d_slope_v113_signal(debt, assets, intangibles, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 63)
    b = _f45_acquisition_intensity(intangibles, debt, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 114: dfgxacq_63d
def f45dfg_f45_debt_funded_growth_risk_dfgxacq_63d_126d_slope_v114_signal(debt, revenue, intangibles, closeadj):
    a = _f45_debt_funded_growth(debt, revenue, 63)
    b = _f45_acquisition_intensity(intangibles, debt, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 115: gap_z_63d
def f45dfg_f45_debt_funded_growth_risk_gap_z_63d_5d_slope_v115_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 116: dfg_z_63d
def f45dfg_f45_debt_funded_growth_risk_dfg_z_63d_10d_slope_v116_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 117: acq_z_63d
def f45dfg_f45_debt_funded_growth_risk_acq_z_63d_21d_slope_v117_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 118: gap_ema_63d
def f45dfg_f45_debt_funded_growth_risk_gap_ema_63d_42d_slope_v118_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 119: dfg_ema_63d
def f45dfg_f45_debt_funded_growth_risk_dfg_ema_63d_63d_slope_v119_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 120: acq_ema_63d
def f45dfg_f45_debt_funded_growth_risk_acq_ema_63d_126d_slope_v120_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 121: gap_sq_63d
def f45dfg_f45_debt_funded_growth_risk_gap_sq_63d_5d_slope_v121_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 122: acq_sq_63d
def f45dfg_f45_debt_funded_growth_risk_acq_sq_63d_10d_slope_v122_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 123: gapxdfg_63d
def f45dfg_f45_debt_funded_growth_risk_gapxdfg_63d_21d_slope_v123_signal(debt, assets, revenue, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 63)
    b = _f45_debt_funded_growth(debt, revenue, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 124: gapxacq_126d
def f45dfg_f45_debt_funded_growth_risk_gapxacq_126d_42d_slope_v124_signal(debt, assets, intangibles, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 126)
    b = _f45_acquisition_intensity(intangibles, debt, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 125: dfgxacq_126d
def f45dfg_f45_debt_funded_growth_risk_dfgxacq_126d_63d_slope_v125_signal(debt, revenue, intangibles, closeadj):
    a = _f45_debt_funded_growth(debt, revenue, 126)
    b = _f45_acquisition_intensity(intangibles, debt, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 126: gap_z_126d
def f45dfg_f45_debt_funded_growth_risk_gap_z_126d_126d_slope_v126_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 127: dfg_z_126d
def f45dfg_f45_debt_funded_growth_risk_dfg_z_126d_5d_slope_v127_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 128: acq_z_126d
def f45dfg_f45_debt_funded_growth_risk_acq_z_126d_10d_slope_v128_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 129: gap_ema_126d
def f45dfg_f45_debt_funded_growth_risk_gap_ema_126d_21d_slope_v129_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 130: dfg_ema_126d
def f45dfg_f45_debt_funded_growth_risk_dfg_ema_126d_42d_slope_v130_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 131: acq_ema_126d
def f45dfg_f45_debt_funded_growth_risk_acq_ema_126d_63d_slope_v131_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 132: gap_sq_126d
def f45dfg_f45_debt_funded_growth_risk_gap_sq_126d_126d_slope_v132_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 133: acq_sq_126d
def f45dfg_f45_debt_funded_growth_risk_acq_sq_126d_5d_slope_v133_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 134: gapxdfg_126d
def f45dfg_f45_debt_funded_growth_risk_gapxdfg_126d_10d_slope_v134_signal(debt, assets, revenue, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 126)
    b = _f45_debt_funded_growth(debt, revenue, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 135: gapxacq_252d
def f45dfg_f45_debt_funded_growth_risk_gapxacq_252d_21d_slope_v135_signal(debt, assets, intangibles, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 252)
    b = _f45_acquisition_intensity(intangibles, debt, 252)
    base = (a * b)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 136: dfgxacq_252d
def f45dfg_f45_debt_funded_growth_risk_dfgxacq_252d_42d_slope_v136_signal(debt, revenue, intangibles, closeadj):
    a = _f45_debt_funded_growth(debt, revenue, 252)
    b = _f45_acquisition_intensity(intangibles, debt, 252)
    base = (a * b)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 137: gap_z_252d
def f45dfg_f45_debt_funded_growth_risk_gap_z_252d_63d_slope_v137_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 138: dfg_z_252d
def f45dfg_f45_debt_funded_growth_risk_dfg_z_252d_126d_slope_v138_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 139: acq_z_252d
def f45dfg_f45_debt_funded_growth_risk_acq_z_252d_5d_slope_v139_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 140: gap_ema_252d
def f45dfg_f45_debt_funded_growth_risk_gap_ema_252d_10d_slope_v140_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 141: dfg_ema_252d
def f45dfg_f45_debt_funded_growth_risk_dfg_ema_252d_21d_slope_v141_signal(debt, revenue, closeadj):
    base = _f45_debt_funded_growth(debt, revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 142: acq_ema_252d
def f45dfg_f45_debt_funded_growth_risk_acq_ema_252d_42d_slope_v142_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 143: gap_sq_252d
def f45dfg_f45_debt_funded_growth_risk_gap_sq_252d_63d_slope_v143_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 144: acq_sq_252d
def f45dfg_f45_debt_funded_growth_risk_acq_sq_252d_126d_slope_v144_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 145: gapxdfg_252d
def f45dfg_f45_debt_funded_growth_risk_gapxdfg_252d_5d_slope_v145_signal(debt, assets, revenue, closeadj):
    a = _f45_debt_asset_gap(debt, assets, 252)
    b = _f45_debt_funded_growth(debt, revenue, 252)
    base = (a * b)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 146: gap_long_10d
def f45dfg_f45_debt_funded_growth_risk_gap_long_10d_10d_slope_v146_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 10)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 147: acq_long_10d
def f45dfg_f45_debt_funded_growth_risk_acq_long_10d_21d_slope_v147_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 10)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 148: gap_long_42d
def f45dfg_f45_debt_funded_growth_risk_gap_long_42d_42d_slope_v148_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 149: acq_long_42d
def f45dfg_f45_debt_funded_growth_risk_acq_long_42d_63d_slope_v149_signal(intangibles, debt, closeadj):
    base = _f45_acquisition_intensity(intangibles, debt, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 150: gap_long_189d
def f45dfg_f45_debt_funded_growth_risk_gap_long_189d_126d_slope_v150_signal(debt, assets, closeadj):
    base = _f45_debt_asset_gap(debt, assets, 189)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xc_5d_slope_v001_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xclog_10d_slope_v002_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_5d_xcm21_21d_slope_v003_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xc_42d_slope_v004_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xclog_63d_slope_v005_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_10d_xcm21_126d_slope_v006_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xc_5d_slope_v007_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xclog_10d_slope_v008_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_21d_xcm21_21d_slope_v009_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xc_42d_slope_v010_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xclog_63d_slope_v011_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_42d_xcm21_126d_slope_v012_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xc_5d_slope_v013_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xclog_10d_slope_v014_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_63d_xcm21_21d_slope_v015_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xc_42d_slope_v016_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xclog_63d_slope_v017_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_126d_xcm21_126d_slope_v018_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xc_5d_slope_v019_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xclog_10d_slope_v020_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_189d_xcm21_21d_slope_v021_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xc_42d_slope_v022_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xclog_63d_slope_v023_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_252d_xcm21_126d_slope_v024_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xc_5d_slope_v025_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xclog_10d_slope_v026_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_378d_xcm21_21d_slope_v027_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xc_42d_slope_v028_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xclog_63d_slope_v029_signal,
    f45dfg_f45_debt_funded_growth_risk_da_gap_504d_xcm21_126d_slope_v030_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xc_5d_slope_v031_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xclog_10d_slope_v032_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_5d_xcm21_21d_slope_v033_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xc_42d_slope_v034_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xclog_63d_slope_v035_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_10d_xcm21_126d_slope_v036_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xc_5d_slope_v037_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xclog_10d_slope_v038_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_21d_xcm21_21d_slope_v039_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xc_42d_slope_v040_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xclog_63d_slope_v041_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_42d_xcm21_126d_slope_v042_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xc_5d_slope_v043_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xclog_10d_slope_v044_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_63d_xcm21_21d_slope_v045_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xc_42d_slope_v046_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xclog_63d_slope_v047_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_126d_xcm21_126d_slope_v048_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xc_5d_slope_v049_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xclog_10d_slope_v050_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_189d_xcm21_21d_slope_v051_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xc_42d_slope_v052_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xclog_63d_slope_v053_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_252d_xcm21_126d_slope_v054_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xc_5d_slope_v055_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xclog_10d_slope_v056_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_378d_xcm21_21d_slope_v057_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xc_42d_slope_v058_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xclog_63d_slope_v059_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_504d_xcm21_126d_slope_v060_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xc_5d_slope_v061_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xclog_10d_slope_v062_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_5d_xcm21_21d_slope_v063_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xc_42d_slope_v064_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xclog_63d_slope_v065_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_10d_xcm21_126d_slope_v066_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xc_5d_slope_v067_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xclog_10d_slope_v068_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_21d_xcm21_21d_slope_v069_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xc_42d_slope_v070_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xclog_63d_slope_v071_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_42d_xcm21_126d_slope_v072_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xc_5d_slope_v073_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xclog_10d_slope_v074_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_63d_xcm21_21d_slope_v075_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_126d_xc_42d_slope_v076_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_126d_xclog_63d_slope_v077_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_126d_xcm21_126d_slope_v078_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_189d_xc_5d_slope_v079_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_189d_xclog_10d_slope_v080_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_189d_xcm21_21d_slope_v081_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_252d_xc_42d_slope_v082_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_252d_xclog_63d_slope_v083_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_252d_xcm21_126d_slope_v084_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_378d_xc_5d_slope_v085_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_378d_xclog_10d_slope_v086_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_378d_xcm21_21d_slope_v087_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_504d_xc_42d_slope_v088_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_504d_xclog_63d_slope_v089_signal,
    f45dfg_f45_debt_funded_growth_risk_acqint_504d_xcm21_126d_slope_v090_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxacq_21d_5d_slope_v091_signal,
    f45dfg_f45_debt_funded_growth_risk_dfgxacq_21d_10d_slope_v092_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_z_21d_21d_slope_v093_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_z_21d_42d_slope_v094_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_z_21d_63d_slope_v095_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_ema_21d_126d_slope_v096_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_ema_21d_5d_slope_v097_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_ema_21d_10d_slope_v098_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_sq_21d_21d_slope_v099_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_sq_21d_42d_slope_v100_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxdfg_21d_63d_slope_v101_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxacq_42d_126d_slope_v102_signal,
    f45dfg_f45_debt_funded_growth_risk_dfgxacq_42d_5d_slope_v103_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_z_42d_10d_slope_v104_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_z_42d_21d_slope_v105_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_z_42d_42d_slope_v106_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_ema_42d_63d_slope_v107_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_ema_42d_126d_slope_v108_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_ema_42d_5d_slope_v109_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_sq_42d_10d_slope_v110_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_sq_42d_21d_slope_v111_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxdfg_42d_42d_slope_v112_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxacq_63d_63d_slope_v113_signal,
    f45dfg_f45_debt_funded_growth_risk_dfgxacq_63d_126d_slope_v114_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_z_63d_5d_slope_v115_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_z_63d_10d_slope_v116_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_z_63d_21d_slope_v117_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_ema_63d_42d_slope_v118_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_ema_63d_63d_slope_v119_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_ema_63d_126d_slope_v120_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_sq_63d_5d_slope_v121_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_sq_63d_10d_slope_v122_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxdfg_63d_21d_slope_v123_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxacq_126d_42d_slope_v124_signal,
    f45dfg_f45_debt_funded_growth_risk_dfgxacq_126d_63d_slope_v125_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_z_126d_126d_slope_v126_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_z_126d_5d_slope_v127_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_z_126d_10d_slope_v128_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_ema_126d_21d_slope_v129_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_ema_126d_42d_slope_v130_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_ema_126d_63d_slope_v131_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_sq_126d_126d_slope_v132_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_sq_126d_5d_slope_v133_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxdfg_126d_10d_slope_v134_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxacq_252d_21d_slope_v135_signal,
    f45dfg_f45_debt_funded_growth_risk_dfgxacq_252d_42d_slope_v136_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_z_252d_63d_slope_v137_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_z_252d_126d_slope_v138_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_z_252d_5d_slope_v139_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_ema_252d_10d_slope_v140_signal,
    f45dfg_f45_debt_funded_growth_risk_dfg_ema_252d_21d_slope_v141_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_ema_252d_42d_slope_v142_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_sq_252d_63d_slope_v143_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_sq_252d_126d_slope_v144_signal,
    f45dfg_f45_debt_funded_growth_risk_gapxdfg_252d_5d_slope_v145_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_long_10d_10d_slope_v146_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_long_10d_21d_slope_v147_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_long_42d_42d_slope_v148_signal,
    f45dfg_f45_debt_funded_growth_risk_acq_long_42d_63d_slope_v149_signal,
    f45dfg_f45_debt_funded_growth_risk_gap_long_189d_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_DEBT_FUNDED_GROWTH_RISK_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f45_debt_funded_growth_risk_2nd_derivatives_001_150_claude: {n_features} features pass")
