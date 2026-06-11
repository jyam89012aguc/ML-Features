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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f027_pref_burden(prefdivis, equity):
    return prefdivis / equity.replace(0, np.nan).abs()


# 21d mean of prefdiv_lvl scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_mean_21d_base_v001_signal(prefdivis, closeadj):
    base = prefdivis
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of prefdiv_lvl scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_mean_63d_base_v002_signal(prefdivis, closeadj):
    base = prefdivis
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of prefdiv_lvl scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_mean_126d_base_v003_signal(prefdivis, closeadj):
    base = prefdivis
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of prefdiv_lvl scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_mean_252d_base_v004_signal(prefdivis, closeadj):
    base = prefdivis
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of prefdiv_lvl scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_mean_504d_base_v005_signal(prefdivis, closeadj):
    base = prefdivis
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pref_burden_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_mean_21d_base_v006_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pref_burden_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_mean_63d_base_v007_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pref_burden_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_mean_126d_base_v008_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pref_burden_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_mean_252d_base_v009_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pref_burden_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_mean_504d_base_v010_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pref_to_ni scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_mean_21d_base_v011_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pref_to_ni scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_mean_63d_base_v012_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pref_to_ni scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_mean_126d_base_v013_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pref_to_ni scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_mean_252d_base_v014_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pref_to_ni scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_mean_504d_base_v015_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_plus_pref_to_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_mean_21d_base_v016_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_plus_pref_to_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_mean_63d_base_v017_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_plus_pref_to_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_mean_126d_base_v018_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_plus_pref_to_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_mean_252d_base_v019_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_plus_pref_to_eq scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_mean_504d_base_v020_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pref_to_mcap scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_mean_21d_base_v021_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pref_to_mcap scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_mean_63d_base_v022_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pref_to_mcap scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_mean_126d_base_v023_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pref_to_mcap scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_mean_252d_base_v024_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pref_to_mcap scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_mean_504d_base_v025_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pref_to_assets scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_mean_21d_base_v026_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pref_to_assets scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_mean_63d_base_v027_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pref_to_assets scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_mean_126d_base_v028_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pref_to_assets scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_mean_252d_base_v029_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pref_to_assets scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_mean_504d_base_v030_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pref_share_ncfdiv scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_mean_21d_base_v031_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pref_share_ncfdiv scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_mean_63d_base_v032_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pref_share_ncfdiv scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_mean_126d_base_v033_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pref_share_ncfdiv scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_mean_252d_base_v034_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pref_share_ncfdiv scaled by closeadj
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_mean_504d_base_v035_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_median_63d_base_v036_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_median_252d_base_v037_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_median_504d_base_v038_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_median_63d_base_v039_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_median_252d_base_v040_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_median_504d_base_v041_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_median_63d_base_v042_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_median_252d_base_v043_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_median_504d_base_v044_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_median_63d_base_v045_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_median_252d_base_v046_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_median_504d_base_v047_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_median_63d_base_v048_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_median_252d_base_v049_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_median_504d_base_v050_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_median_63d_base_v051_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_median_252d_base_v052_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_median_504d_base_v053_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_median_63d_base_v054_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_median_252d_base_v055_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_median_504d_base_v056_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rmax_252d_base_v057_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rmax_504d_base_v058_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rmax_252d_base_v059_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rmax_504d_base_v060_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_rmax_252d_base_v061_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_rmax_504d_base_v062_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_rmax_252d_base_v063_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_rmax_504d_base_v064_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_rmax_252d_base_v065_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_rmax_504d_base_v066_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_rmax_252d_base_v067_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_rmax_504d_base_v068_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_rmax_252d_base_v069_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_rmax_504d_base_v070_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rmin_252d_base_v071_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rmin_504d_base_v072_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rmin_252d_base_v073_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rmin_504d_base_v074_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_rmin_252d_base_v075_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

