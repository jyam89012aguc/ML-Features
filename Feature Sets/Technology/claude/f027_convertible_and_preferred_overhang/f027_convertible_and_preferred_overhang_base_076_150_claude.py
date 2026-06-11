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


# 63d z-score of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_z_63d_base_v076_signal(prefdivis, closeadj):
    base = prefdivis
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_z_126d_base_v077_signal(prefdivis, closeadj):
    base = prefdivis
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_z_252d_base_v078_signal(prefdivis, closeadj):
    base = prefdivis
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_z_504d_base_v079_signal(prefdivis, closeadj):
    base = prefdivis
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_z_63d_base_v080_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_z_126d_base_v081_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_z_252d_base_v082_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_z_504d_base_v083_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_z_63d_base_v084_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_z_126d_base_v085_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_z_252d_base_v086_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_z_504d_base_v087_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_z_63d_base_v088_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_z_126d_base_v089_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_z_252d_base_v090_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_z_504d_base_v091_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_z_63d_base_v092_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_z_126d_base_v093_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_z_252d_base_v094_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_z_504d_base_v095_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_z_63d_base_v096_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_z_126d_base_v097_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_z_252d_base_v098_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_z_504d_base_v099_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_z_63d_base_v100_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_z_126d_base_v101_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_z_252d_base_v102_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_z_504d_base_v103_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_distmax_252d_base_v104_signal(prefdivis, closeadj):
    base = prefdivis
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_distmax_504d_base_v105_signal(prefdivis, closeadj):
    base = prefdivis
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_distmax_252d_base_v106_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_distmax_504d_base_v107_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_distmax_252d_base_v108_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_distmax_504d_base_v109_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_distmax_252d_base_v110_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_distmax_504d_base_v111_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_distmax_252d_base_v112_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_distmax_504d_base_v113_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_distmax_252d_base_v114_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_distmax_504d_base_v115_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_distmax_252d_base_v116_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_distmax_504d_base_v117_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_distmed_126d_base_v118_signal(prefdivis, closeadj):
    base = prefdivis
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_distmed_252d_base_v119_signal(prefdivis, closeadj):
    base = prefdivis
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_distmed_504d_base_v120_signal(prefdivis, closeadj):
    base = prefdivis
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_distmed_126d_base_v121_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_distmed_252d_base_v122_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_distmed_504d_base_v123_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_distmed_126d_base_v124_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_distmed_252d_base_v125_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_distmed_504d_base_v126_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_distmed_126d_base_v127_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_distmed_252d_base_v128_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_distmed_504d_base_v129_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_distmed_126d_base_v130_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_distmed_252d_base_v131_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_distmed_504d_base_v132_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_distmed_126d_base_v133_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_distmed_252d_base_v134_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_distmed_504d_base_v135_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_distmed_126d_base_v136_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_distmed_252d_base_v137_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pref_share_ncfdiv
def f027cpo_f027_convertible_and_preferred_overhang_pref_share_ncfdiv_distmed_504d_base_v138_signal(prefdivis, ncfdiv, closeadj):
    base = prefdivis / ncfdiv.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_chg_63d_base_v139_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in prefdiv_lvl
def f027cpo_f027_convertible_and_preferred_overhang_prefdiv_lvl_chg_252d_base_v140_signal(prefdivis, closeadj):
    base = prefdivis
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_chg_63d_base_v141_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pref_burden_eq
def f027cpo_f027_convertible_and_preferred_overhang_pref_burden_eq_chg_252d_base_v142_signal(prefdivis, equity, closeadj):
    base = _f027_pref_burden(prefdivis, equity)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_chg_63d_base_v143_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pref_to_ni
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_ni_chg_252d_base_v144_signal(prefdivis, netinc, closeadj):
    base = prefdivis / netinc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_chg_63d_base_v145_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in debt_plus_pref_to_eq
def f027cpo_f027_convertible_and_preferred_overhang_debt_plus_pref_to_eq_chg_252d_base_v146_signal(debt, prefdivis, equity, closeadj):
    base = (debt.fillna(0) + prefdivis.fillna(0)*10) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_chg_63d_base_v147_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pref_to_mcap
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_mcap_chg_252d_base_v148_signal(prefdivis, marketcap, closeadj):
    base = prefdivis / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_chg_63d_base_v149_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pref_to_assets
def f027cpo_f027_convertible_and_preferred_overhang_pref_to_assets_chg_252d_base_v150_signal(prefdivis, assets, closeadj):
    base = prefdivis / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

