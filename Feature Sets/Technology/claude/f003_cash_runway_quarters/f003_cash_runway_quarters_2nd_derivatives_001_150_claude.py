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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f003_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f003_runway(cashneq, investmentsc, ncfo):
    burn = (-ncfo).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


def _f003_fcf_runway(cashneq, investmentsc, fcf):
    burn = (-fcf).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


# 21d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slope_21d_2d_v001_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slope_63d_2d_v002_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slope_126d_2d_v003_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slope_252d_2d_v004_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slope_504d_2d_v005_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of runway
def f003cr_f003_cash_runway_quarters_runway_slope_21d_2d_v006_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of runway
def f003cr_f003_cash_runway_quarters_runway_slope_63d_2d_v007_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of runway
def f003cr_f003_cash_runway_quarters_runway_slope_126d_2d_v008_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of runway
def f003cr_f003_cash_runway_quarters_runway_slope_252d_2d_v009_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of runway
def f003cr_f003_cash_runway_quarters_runway_slope_504d_2d_v010_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slope_21d_2d_v011_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slope_63d_2d_v012_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slope_126d_2d_v013_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slope_252d_2d_v014_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slope_504d_2d_v015_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slope_21d_2d_v016_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slope_63d_2d_v017_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slope_126d_2d_v018_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slope_252d_2d_v019_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slope_504d_2d_v020_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slope_21d_2d_v021_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slope_63d_2d_v022_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slope_126d_2d_v023_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slope_252d_2d_v024_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slope_504d_2d_v025_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slope_21d_2d_v026_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slope_63d_2d_v027_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slope_126d_2d_v028_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slope_252d_2d_v029_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slope_504d_2d_v030_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slope_21d_2d_v031_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slope_63d_2d_v032_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slope_126d_2d_v033_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slope_252d_2d_v034_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slope_504d_2d_v035_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sm21_sl21_2d_v036_signal(ncfo, closeadj):
    base = _mean(_f003_burn(ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sm63_sl21_2d_v037_signal(ncfo, closeadj):
    base = _mean(_f003_burn(ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sm63_sl63_2d_v038_signal(ncfo, closeadj):
    base = _mean(_f003_burn(ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sm252_sl63_2d_v039_signal(ncfo, closeadj):
    base = _mean(_f003_burn(ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sm252_sl126_2d_v040_signal(ncfo, closeadj):
    base = _mean(_f003_burn(ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sm21_sl21_2d_v041_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f003_runway(cashneq, investmentsc, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sm63_sl21_2d_v042_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f003_runway(cashneq, investmentsc, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sm63_sl63_2d_v043_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f003_runway(cashneq, investmentsc, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sm252_sl63_2d_v044_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f003_runway(cashneq, investmentsc, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sm252_sl126_2d_v045_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f003_runway(cashneq, investmentsc, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sm21_sl21_2d_v046_signal(cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f003_fcf_runway(cashneq, investmentsc, fcf), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sm63_sl21_2d_v047_signal(cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f003_fcf_runway(cashneq, investmentsc, fcf), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sm63_sl63_2d_v048_signal(cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f003_fcf_runway(cashneq, investmentsc, fcf), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sm252_sl63_2d_v049_signal(cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f003_fcf_runway(cashneq, investmentsc, fcf), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sm252_sl126_2d_v050_signal(cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f003_fcf_runway(cashneq, investmentsc, fcf), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sm21_sl21_2d_v051_signal(ncfo, assets, closeadj):
    base = _mean(_f003_burn(ncfo) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sm63_sl21_2d_v052_signal(ncfo, assets, closeadj):
    base = _mean(_f003_burn(ncfo) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sm63_sl63_2d_v053_signal(ncfo, assets, closeadj):
    base = _mean(_f003_burn(ncfo) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sm252_sl63_2d_v054_signal(ncfo, assets, closeadj):
    base = _mean(_f003_burn(ncfo) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sm252_sl126_2d_v055_signal(ncfo, assets, closeadj):
    base = _mean(_f003_burn(ncfo) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sm21_sl21_2d_v056_signal(ncfo, marketcap, closeadj):
    base = _mean(_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sm63_sl21_2d_v057_signal(ncfo, marketcap, closeadj):
    base = _mean(_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sm63_sl63_2d_v058_signal(ncfo, marketcap, closeadj):
    base = _mean(_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sm252_sl63_2d_v059_signal(ncfo, marketcap, closeadj):
    base = _mean(_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sm252_sl126_2d_v060_signal(ncfo, marketcap, closeadj):
    base = _mean(_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sm21_sl21_2d_v061_signal(ncfo, cashneq, closeadj):
    base = _mean(_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sm63_sl21_2d_v062_signal(ncfo, cashneq, closeadj):
    base = _mean(_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sm63_sl63_2d_v063_signal(ncfo, cashneq, closeadj):
    base = _mean(_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sm252_sl63_2d_v064_signal(ncfo, cashneq, closeadj):
    base = _mean(_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sm252_sl126_2d_v065_signal(ncfo, cashneq, closeadj):
    base = _mean(_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sm21_sl21_2d_v066_signal(fcf, marketcap, closeadj):
    base = _mean((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sm63_sl21_2d_v067_signal(fcf, marketcap, closeadj):
    base = _mean((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sm63_sl63_2d_v068_signal(fcf, marketcap, closeadj):
    base = _mean((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sm252_sl63_2d_v069_signal(fcf, marketcap, closeadj):
    base = _mean((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sm252_sl126_2d_v070_signal(fcf, marketcap, closeadj):
    base = _mean((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_pctslope_21d_2d_v071_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_pctslope_63d_2d_v072_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_pctslope_252d_2d_v073_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of runway
def f003cr_f003_cash_runway_quarters_runway_pctslope_21d_2d_v074_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of runway
def f003cr_f003_cash_runway_quarters_runway_pctslope_63d_2d_v075_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of runway
def f003cr_f003_cash_runway_quarters_runway_pctslope_252d_2d_v076_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_pctslope_21d_2d_v077_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_pctslope_63d_2d_v078_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_pctslope_252d_2d_v079_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_pctslope_21d_2d_v080_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_pctslope_63d_2d_v081_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_pctslope_252d_2d_v082_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_pctslope_21d_2d_v083_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_pctslope_63d_2d_v084_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_pctslope_252d_2d_v085_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_pctslope_21d_2d_v086_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_pctslope_63d_2d_v087_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_pctslope_252d_2d_v088_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_pctslope_21d_2d_v089_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_pctslope_63d_2d_v090_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_pctslope_252d_2d_v091_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sgnslope_21d_2d_v092_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sgnslope_63d_2d_v093_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_sgnslope_252d_2d_v094_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sgnslope_21d_2d_v095_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sgnslope_63d_2d_v096_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of runway
def f003cr_f003_cash_runway_quarters_runway_sgnslope_252d_2d_v097_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sgnslope_21d_2d_v098_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sgnslope_63d_2d_v099_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_sgnslope_252d_2d_v100_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sgnslope_21d_2d_v101_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sgnslope_63d_2d_v102_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_sgnslope_252d_2d_v103_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sgnslope_21d_2d_v104_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sgnslope_63d_2d_v105_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_sgnslope_252d_2d_v106_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sgnslope_21d_2d_v107_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sgnslope_63d_2d_v108_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_sgnslope_252d_2d_v109_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sgnslope_21d_2d_v110_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sgnslope_63d_2d_v111_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_sgnslope_252d_2d_v112_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_logmagslope_21d_2d_v113_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_logmagslope_63d_2d_v114_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_logmagslope_252d_2d_v115_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of runway
def f003cr_f003_cash_runway_quarters_runway_logmagslope_21d_2d_v116_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of runway
def f003cr_f003_cash_runway_quarters_runway_logmagslope_63d_2d_v117_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of runway
def f003cr_f003_cash_runway_quarters_runway_logmagslope_252d_2d_v118_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_logmagslope_21d_2d_v119_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_logmagslope_63d_2d_v120_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_logmagslope_252d_2d_v121_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_logmagslope_21d_2d_v122_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_logmagslope_63d_2d_v123_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_logmagslope_252d_2d_v124_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_logmagslope_21d_2d_v125_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_logmagslope_63d_2d_v126_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_logmagslope_252d_2d_v127_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_logmagslope_21d_2d_v128_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_logmagslope_63d_2d_v129_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_logmagslope_252d_2d_v130_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_logmagslope_21d_2d_v131_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_logmagslope_63d_2d_v132_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_logmagslope_252d_2d_v133_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|burn_lvl|
def f003cr_f003_cash_runway_quarters_burn_lvl_logslope_63d_2d_v134_signal(ncfo, closeadj):
    base = np.log((_f003_burn(ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|burn_lvl|
def f003cr_f003_cash_runway_quarters_burn_lvl_logslope_252d_2d_v135_signal(ncfo, closeadj):
    base = np.log((_f003_burn(ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|runway|
def f003cr_f003_cash_runway_quarters_runway_logslope_63d_2d_v136_signal(cashneq, investmentsc, ncfo, closeadj):
    base = np.log((_f003_runway(cashneq, investmentsc, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|runway|
def f003cr_f003_cash_runway_quarters_runway_logslope_252d_2d_v137_signal(cashneq, investmentsc, ncfo, closeadj):
    base = np.log((_f003_runway(cashneq, investmentsc, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|fcf_runway|
def f003cr_f003_cash_runway_quarters_fcf_runway_logslope_63d_2d_v138_signal(cashneq, investmentsc, fcf, closeadj):
    base = np.log((_f003_fcf_runway(cashneq, investmentsc, fcf)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|fcf_runway|
def f003cr_f003_cash_runway_quarters_fcf_runway_logslope_252d_2d_v139_signal(cashneq, investmentsc, fcf, closeadj):
    base = np.log((_f003_fcf_runway(cashneq, investmentsc, fcf)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|burn_to_asset|
def f003cr_f003_cash_runway_quarters_burn_to_asset_logslope_63d_2d_v140_signal(ncfo, assets, closeadj):
    base = np.log((_f003_burn(ncfo) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|burn_to_asset|
def f003cr_f003_cash_runway_quarters_burn_to_asset_logslope_252d_2d_v141_signal(ncfo, assets, closeadj):
    base = np.log((_f003_burn(ncfo) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|burn_to_mcap|
def f003cr_f003_cash_runway_quarters_burn_to_mcap_logslope_63d_2d_v142_signal(ncfo, marketcap, closeadj):
    base = np.log((_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|burn_to_mcap|
def f003cr_f003_cash_runway_quarters_burn_to_mcap_logslope_252d_2d_v143_signal(ncfo, marketcap, closeadj):
    base = np.log((_f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|burn_to_cash|
def f003cr_f003_cash_runway_quarters_burn_to_cash_logslope_63d_2d_v144_signal(ncfo, cashneq, closeadj):
    base = np.log((_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|burn_to_cash|
def f003cr_f003_cash_runway_quarters_burn_to_cash_logslope_252d_2d_v145_signal(ncfo, cashneq, closeadj):
    base = np.log((_f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|fcf_burn_to_mcap|
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_logslope_63d_2d_v146_signal(fcf, marketcap, closeadj):
    base = np.log(((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|fcf_burn_to_mcap|
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_logslope_252d_2d_v147_signal(fcf, marketcap, closeadj):
    base = np.log(((-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

