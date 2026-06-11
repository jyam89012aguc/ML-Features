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
def _f027_pref_burden(prefdivis, equity):
    return prefdivis / equity.replace(0, np.nan).abs()


# 21d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slope_21d_2d_v001_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slope_63d_2d_v002_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slope_126d_2d_v003_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slope_252d_2d_v004_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slope_504d_2d_v005_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slope_21d_2d_v006_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slope_63d_2d_v007_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slope_126d_2d_v008_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slope_252d_2d_v009_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slope_504d_2d_v010_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slope_21d_2d_v011_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slope_63d_2d_v012_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slope_126d_2d_v013_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slope_252d_2d_v014_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slope_504d_2d_v015_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slope_21d_2d_v016_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slope_63d_2d_v017_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slope_126d_2d_v018_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slope_252d_2d_v019_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slope_504d_2d_v020_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slope_21d_2d_v021_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slope_63d_2d_v022_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slope_126d_2d_v023_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slope_252d_2d_v024_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slope_504d_2d_v025_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slope_21d_2d_v026_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slope_63d_2d_v027_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slope_126d_2d_v028_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slope_252d_2d_v029_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slope_504d_2d_v030_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slope_21d_2d_v031_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slope_63d_2d_v032_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slope_126d_2d_v033_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slope_252d_2d_v034_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slope_504d_2d_v035_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sm21_sl21_2d_v036_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sm63_sl21_2d_v037_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sm63_sl63_2d_v038_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sm252_sl63_2d_v039_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sm252_sl126_2d_v040_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sm21_sl21_2d_v041_signal(prefdivis, equity, closeadj):
    base = _mean(_f027_pref_burden(prefdivis, equity), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sm63_sl21_2d_v042_signal(prefdivis, equity, closeadj):
    base = _mean(_f027_pref_burden(prefdivis, equity), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sm63_sl63_2d_v043_signal(prefdivis, equity, closeadj):
    base = _mean(_f027_pref_burden(prefdivis, equity), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sm252_sl63_2d_v044_signal(prefdivis, equity, closeadj):
    base = _mean(_f027_pref_burden(prefdivis, equity), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sm252_sl126_2d_v045_signal(prefdivis, equity, closeadj):
    base = _mean(_f027_pref_burden(prefdivis, equity), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sm21_sl21_2d_v046_signal(prefdivis, netinc, closeadj):
    base = _mean(prefdivis / netinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sm63_sl21_2d_v047_signal(prefdivis, netinc, closeadj):
    base = _mean(prefdivis / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sm63_sl63_2d_v048_signal(prefdivis, netinc, closeadj):
    base = _mean(prefdivis / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sm252_sl63_2d_v049_signal(prefdivis, netinc, closeadj):
    base = _mean(prefdivis / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sm252_sl126_2d_v050_signal(prefdivis, netinc, closeadj):
    base = _mean(prefdivis / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sm21_sl21_2d_v051_signal(debt, prefdivis, equity, closeadj):
    base = _mean((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sm63_sl21_2d_v052_signal(debt, prefdivis, equity, closeadj):
    base = _mean((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sm63_sl63_2d_v053_signal(debt, prefdivis, equity, closeadj):
    base = _mean((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sm252_sl63_2d_v054_signal(debt, prefdivis, equity, closeadj):
    base = _mean((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sm252_sl126_2d_v055_signal(debt, prefdivis, equity, closeadj):
    base = _mean((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sm21_sl21_2d_v056_signal(prefdivis, marketcap, closeadj):
    base = _mean(prefdivis / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sm63_sl21_2d_v057_signal(prefdivis, marketcap, closeadj):
    base = _mean(prefdivis / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sm63_sl63_2d_v058_signal(prefdivis, marketcap, closeadj):
    base = _mean(prefdivis / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sm252_sl63_2d_v059_signal(prefdivis, marketcap, closeadj):
    base = _mean(prefdivis / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sm252_sl126_2d_v060_signal(prefdivis, marketcap, closeadj):
    base = _mean(prefdivis / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sm21_sl21_2d_v061_signal(prefdivis, assets, closeadj):
    base = _mean(prefdivis / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sm63_sl21_2d_v062_signal(prefdivis, assets, closeadj):
    base = _mean(prefdivis / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sm63_sl63_2d_v063_signal(prefdivis, assets, closeadj):
    base = _mean(prefdivis / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sm252_sl63_2d_v064_signal(prefdivis, assets, closeadj):
    base = _mean(prefdivis / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sm252_sl126_2d_v065_signal(prefdivis, assets, closeadj):
    base = _mean(prefdivis / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sm21_sl21_2d_v066_signal(prefdivis, ncfdiv, closeadj):
    base = _mean(prefdivis / ncfdiv.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sm63_sl21_2d_v067_signal(prefdivis, ncfdiv, closeadj):
    base = _mean(prefdivis / ncfdiv.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sm63_sl63_2d_v068_signal(prefdivis, ncfdiv, closeadj):
    base = _mean(prefdivis / ncfdiv.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sm252_sl63_2d_v069_signal(prefdivis, ncfdiv, closeadj):
    base = _mean(prefdivis / ncfdiv.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sm252_sl126_2d_v070_signal(prefdivis, ncfdiv, closeadj):
    base = _mean(prefdivis / ncfdiv.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_pctslope_21d_2d_v071_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_pctslope_63d_2d_v072_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_pctslope_252d_2d_v073_signal(prefdivis, closeadj):
    base = prefdivis
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_pctslope_21d_2d_v074_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_pctslope_63d_2d_v075_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_pctslope_252d_2d_v076_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_pctslope_21d_2d_v077_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_pctslope_63d_2d_v078_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_pctslope_252d_2d_v079_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_pctslope_21d_2d_v080_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_pctslope_63d_2d_v081_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_pctslope_252d_2d_v082_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_pctslope_21d_2d_v083_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_pctslope_63d_2d_v084_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_pctslope_252d_2d_v085_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_pctslope_21d_2d_v086_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_pctslope_63d_2d_v087_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_pctslope_252d_2d_v088_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_pctslope_21d_2d_v089_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_pctslope_63d_2d_v090_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_pctslope_252d_2d_v091_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sgnslope_21d_2d_v092_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sgnslope_63d_2d_v093_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_sgnslope_252d_2d_v094_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sgnslope_21d_2d_v095_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sgnslope_63d_2d_v096_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_sgnslope_252d_2d_v097_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sgnslope_21d_2d_v098_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sgnslope_63d_2d_v099_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_sgnslope_252d_2d_v100_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sgnslope_21d_2d_v101_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sgnslope_63d_2d_v102_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_sgnslope_252d_2d_v103_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sgnslope_21d_2d_v104_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sgnslope_63d_2d_v105_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_sgnslope_252d_2d_v106_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sgnslope_21d_2d_v107_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sgnslope_63d_2d_v108_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_sgnslope_252d_2d_v109_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sgnslope_21d_2d_v110_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sgnslope_63d_2d_v111_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_sgnslope_252d_2d_v112_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_logmagslope_21d_2d_v113_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_logmagslope_63d_2d_v114_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_logmagslope_252d_2d_v115_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_logmagslope_21d_2d_v116_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_logmagslope_63d_2d_v117_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_logmagslope_252d_2d_v118_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_logmagslope_21d_2d_v119_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_logmagslope_63d_2d_v120_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_logmagslope_252d_2d_v121_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_logmagslope_21d_2d_v122_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_logmagslope_63d_2d_v123_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_logmagslope_252d_2d_v124_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_logmagslope_21d_2d_v125_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_logmagslope_63d_2d_v126_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_logmagslope_252d_2d_v127_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_logmagslope_21d_2d_v128_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_logmagslope_63d_2d_v129_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_logmagslope_252d_2d_v130_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_logmagslope_21d_2d_v131_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_logmagslope_63d_2d_v132_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_logmagslope_252d_2d_v133_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|prefdiv_lvl|
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_logslope_63d_2d_v134_signal(prefdivis, closeadj):
    base = np.log((prefdivis).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|prefdiv_lvl|
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_logslope_252d_2d_v135_signal(prefdivis, closeadj):
    base = np.log((prefdivis).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pref_burden_eq|
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_logslope_63d_2d_v136_signal(prefdivis, equity, closeadj):
    base = np.log((_f027_pref_burden(prefdivis, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pref_burden_eq|
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_logslope_252d_2d_v137_signal(prefdivis, equity, closeadj):
    base = np.log((_f027_pref_burden(prefdivis, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pref_to_ni|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_logslope_63d_2d_v138_signal(prefdivis, netinc, closeadj):
    base = np.log((prefdivis / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pref_to_ni|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_logslope_252d_2d_v139_signal(prefdivis, netinc, closeadj):
    base = np.log((prefdivis / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debt_plus_pref_to_eq|
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_logslope_63d_2d_v140_signal(debt, prefdivis, equity, closeadj):
    base = np.log(((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debt_plus_pref_to_eq|
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_logslope_252d_2d_v141_signal(debt, prefdivis, equity, closeadj):
    base = np.log(((debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pref_to_mcap|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_logslope_63d_2d_v142_signal(prefdivis, marketcap, closeadj):
    base = np.log((prefdivis / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pref_to_mcap|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_logslope_252d_2d_v143_signal(prefdivis, marketcap, closeadj):
    base = np.log((prefdivis / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pref_to_assets|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_logslope_63d_2d_v144_signal(prefdivis, assets, closeadj):
    base = np.log((prefdivis / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pref_to_assets|
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_logslope_252d_2d_v145_signal(prefdivis, assets, closeadj):
    base = np.log((prefdivis / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pref_share_ncfdiv|
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_logslope_63d_2d_v146_signal(prefdivis, ncfdiv, closeadj):
    base = np.log((prefdivis / ncfdiv.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pref_share_ncfdiv|
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_logslope_252d_2d_v147_signal(prefdivis, ncfdiv, closeadj):
    base = np.log((prefdivis / ncfdiv.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

