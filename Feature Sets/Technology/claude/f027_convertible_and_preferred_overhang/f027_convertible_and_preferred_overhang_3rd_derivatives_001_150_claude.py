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


# 21d acceleration of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accel_21d_3d_v001_signal(prefdivis, closeadj):
    base = prefdivis
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accel_63d_3d_v002_signal(prefdivis, closeadj):
    base = prefdivis
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accel_126d_3d_v003_signal(prefdivis, closeadj):
    base = prefdivis
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accel_252d_3d_v004_signal(prefdivis, closeadj):
    base = prefdivis
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accel_21d_3d_v005_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accel_63d_3d_v006_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accel_126d_3d_v007_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accel_252d_3d_v008_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accel_21d_3d_v009_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accel_63d_3d_v010_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accel_126d_3d_v011_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accel_252d_3d_v012_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accel_21d_3d_v013_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accel_63d_3d_v014_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accel_126d_3d_v015_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accel_252d_3d_v016_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accel_21d_3d_v017_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accel_63d_3d_v018_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accel_126d_3d_v019_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accel_252d_3d_v020_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accel_21d_3d_v021_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accel_63d_3d_v022_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accel_126d_3d_v023_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accel_252d_3d_v024_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accel_21d_3d_v025_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accel_63d_3d_v026_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accel_126d_3d_v027_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accel_252d_3d_v028_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slopez_21d_z126_3d_v029_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slopez_63d_z252_3d_v030_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slopez_126d_z252_3d_v031_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_slopez_252d_z504_3d_v032_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slopez_21d_z126_3d_v033_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slopez_63d_z252_3d_v034_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slopez_126d_z252_3d_v035_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_slopez_252d_z504_3d_v036_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slopez_21d_z126_3d_v037_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slopez_63d_z252_3d_v038_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slopez_126d_z252_3d_v039_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_slopez_252d_z504_3d_v040_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slopez_21d_z126_3d_v041_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slopez_63d_z252_3d_v042_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slopez_126d_z252_3d_v043_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_slopez_252d_z504_3d_v044_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slopez_21d_z126_3d_v045_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slopez_63d_z252_3d_v046_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slopez_126d_z252_3d_v047_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_slopez_252d_z504_3d_v048_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slopez_21d_z126_3d_v049_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slopez_63d_z252_3d_v050_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slopez_126d_z252_3d_v051_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_slopez_252d_z504_3d_v052_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slopez_21d_z126_3d_v053_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slopez_63d_z252_3d_v054_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slopez_126d_z252_3d_v055_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_slopez_252d_z504_3d_v056_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_jerk_21d_3d_v057_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_jerk_63d_3d_v058_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_jerk_126d_3d_v059_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_jerk_21d_3d_v060_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_jerk_63d_3d_v061_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_jerk_126d_3d_v062_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_jerk_21d_3d_v063_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_jerk_63d_3d_v064_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_jerk_126d_3d_v065_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_jerk_21d_3d_v066_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_jerk_63d_3d_v067_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_jerk_126d_3d_v068_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_jerk_21d_3d_v069_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_jerk_63d_3d_v070_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_jerk_126d_3d_v071_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_jerk_21d_3d_v072_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_jerk_63d_3d_v073_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_jerk_126d_3d_v074_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_jerk_21d_3d_v075_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_jerk_63d_3d_v076_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_jerk_126d_3d_v077_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of prefdiv_lvl smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_smoothaccel_63d_sm252_3d_v078_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of prefdiv_lvl smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_smoothaccel_252d_sm504_3d_v079_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pref_burden_eq smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_smoothaccel_63d_sm252_3d_v080_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pref_burden_eq smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_smoothaccel_252d_sm504_3d_v081_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pref_to_ni smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_smoothaccel_63d_sm252_3d_v082_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pref_to_ni smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_smoothaccel_252d_sm504_3d_v083_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debt_plus_pref_to_eq smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_smoothaccel_63d_sm252_3d_v084_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debt_plus_pref_to_eq smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_smoothaccel_252d_sm504_3d_v085_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pref_to_mcap smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_smoothaccel_63d_sm252_3d_v086_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pref_to_mcap smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_smoothaccel_252d_sm504_3d_v087_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pref_to_assets smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_smoothaccel_63d_sm252_3d_v088_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pref_to_assets smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_smoothaccel_252d_sm504_3d_v089_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pref_share_ncfdiv smoothed over 252d
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_smoothaccel_63d_sm252_3d_v090_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pref_share_ncfdiv smoothed over 504d
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_smoothaccel_252d_sm504_3d_v091_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accelz_21d_z252_3d_v092_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_accelz_63d_z504_3d_v093_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accelz_21d_z252_3d_v094_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_accelz_63d_z504_3d_v095_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accelz_21d_z252_3d_v096_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_accelz_63d_z504_3d_v097_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accelz_21d_z252_3d_v098_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_accelz_63d_z504_3d_v099_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accelz_21d_z252_3d_v100_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_accelz_63d_z504_3d_v101_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accelz_21d_z252_3d_v102_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_accelz_63d_z504_3d_v103_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accelz_21d_z252_3d_v104_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_accelz_63d_z504_3d_v105_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in prefdiv_lvl (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_signflip_63d_3d_v106_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in prefdiv_lvl (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_signflip_252d_3d_v107_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pref_burden_eq (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_signflip_63d_3d_v108_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pref_burden_eq (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_signflip_252d_3d_v109_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pref_to_ni (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_signflip_63d_3d_v110_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pref_to_ni (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_signflip_252d_3d_v111_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debt_plus_pref_to_eq (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_signflip_63d_3d_v112_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debt_plus_pref_to_eq (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_signflip_252d_3d_v113_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pref_to_mcap (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_signflip_63d_3d_v114_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pref_to_mcap (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_signflip_252d_3d_v115_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pref_to_assets (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_signflip_63d_3d_v116_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pref_to_assets (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_signflip_252d_3d_v117_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pref_share_ncfdiv (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_signflip_63d_3d_v118_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pref_share_ncfdiv (raw count, no price scaling)
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_signflip_252d_3d_v119_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of prefdiv_lvl normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rngaccel_63d_r252_3d_v120_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of prefdiv_lvl normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_rngaccel_252d_r504_3d_v121_signal(prefdivis, closeadj):
    base = prefdivis
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_burden_eq normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rngaccel_63d_r252_3d_v122_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_burden_eq normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_rngaccel_252d_r504_3d_v123_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_ni normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_rngaccel_63d_r252_3d_v124_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_ni normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_rngaccel_252d_r504_3d_v125_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debt_plus_pref_to_eq normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_rngaccel_63d_r252_3d_v126_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debt_plus_pref_to_eq normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_rngaccel_252d_r504_3d_v127_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_mcap normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_rngaccel_63d_r252_3d_v128_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_mcap normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_rngaccel_252d_r504_3d_v129_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_to_assets normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_rngaccel_63d_r252_3d_v130_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_to_assets normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_rngaccel_252d_r504_3d_v131_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pref_share_ncfdiv normalized by 252d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_rngaccel_63d_r252_3d_v132_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pref_share_ncfdiv normalized by 504d range
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_rngaccel_252d_r504_3d_v133_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_cumslope_21d_3d_v134_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_cumslope_63d_3d_v135_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_cumslope_252d_3d_v136_signal(prefdivis, closeadj):
    base = prefdivis
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_cumslope_21d_3d_v137_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_cumslope_63d_3d_v138_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_cumslope_252d_3d_v139_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_cumslope_21d_3d_v140_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_cumslope_63d_3d_v141_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_cumslope_252d_3d_v142_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_cumslope_21d_3d_v143_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_cumslope_63d_3d_v144_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_cumslope_252d_3d_v145_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_cumslope_21d_3d_v146_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_cumslope_63d_3d_v147_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_cumslope_252d_3d_v148_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_cumslope_21d_3d_v149_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_cumslope_63d_3d_v150_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

