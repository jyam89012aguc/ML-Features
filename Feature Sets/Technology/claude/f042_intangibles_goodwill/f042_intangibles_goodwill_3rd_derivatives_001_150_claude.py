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
def _f042_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 21d acceleration of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accel_21d_3d_v001_signal(intangibles, closeadj):
    base = intangibles
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accel_63d_3d_v002_signal(intangibles, closeadj):
    base = intangibles
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accel_126d_3d_v003_signal(intangibles, closeadj):
    base = intangibles
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accel_252d_3d_v004_signal(intangibles, closeadj):
    base = intangibles
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accel_21d_3d_v005_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accel_63d_3d_v006_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accel_126d_3d_v007_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accel_252d_3d_v008_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accel_21d_3d_v009_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accel_63d_3d_v010_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accel_126d_3d_v011_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accel_252d_3d_v012_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accel_21d_3d_v013_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accel_63d_3d_v014_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accel_126d_3d_v015_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accel_252d_3d_v016_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accel_21d_3d_v017_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accel_63d_3d_v018_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accel_126d_3d_v019_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accel_252d_3d_v020_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accel_21d_3d_v021_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accel_63d_3d_v022_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accel_126d_3d_v023_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accel_252d_3d_v024_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accel_21d_3d_v025_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accel_63d_3d_v026_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accel_126d_3d_v027_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accel_252d_3d_v028_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slopez_21d_z126_3d_v029_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slopez_63d_z252_3d_v030_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slopez_126d_z252_3d_v031_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slopez_252d_z504_3d_v032_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slopez_21d_z126_3d_v033_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slopez_63d_z252_3d_v034_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slopez_126d_z252_3d_v035_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slopez_252d_z504_3d_v036_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slopez_21d_z126_3d_v037_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slopez_63d_z252_3d_v038_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slopez_126d_z252_3d_v039_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slopez_252d_z504_3d_v040_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slopez_21d_z126_3d_v041_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slopez_63d_z252_3d_v042_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slopez_126d_z252_3d_v043_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slopez_252d_z504_3d_v044_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slopez_21d_z126_3d_v045_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slopez_63d_z252_3d_v046_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slopez_126d_z252_3d_v047_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slopez_252d_z504_3d_v048_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slopez_21d_z126_3d_v049_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slopez_63d_z252_3d_v050_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slopez_126d_z252_3d_v051_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slopez_252d_z504_3d_v052_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slopez_21d_z126_3d_v053_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slopez_63d_z252_3d_v054_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slopez_126d_z252_3d_v055_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slopez_252d_z504_3d_v056_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_jerk_21d_3d_v057_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_jerk_63d_3d_v058_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_jerk_126d_3d_v059_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_jerk_21d_3d_v060_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_jerk_63d_3d_v061_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_jerk_126d_3d_v062_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_jerk_21d_3d_v063_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_jerk_63d_3d_v064_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_jerk_126d_3d_v065_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_jerk_21d_3d_v066_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_jerk_63d_3d_v067_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_jerk_126d_3d_v068_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_jerk_21d_3d_v069_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_jerk_63d_3d_v070_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_jerk_126d_3d_v071_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_jerk_21d_3d_v072_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_jerk_63d_3d_v073_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_jerk_126d_3d_v074_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_jerk_21d_3d_v075_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_jerk_63d_3d_v076_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_jerk_126d_3d_v077_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_lvl smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_lvl_smoothaccel_63d_sm252_3d_v078_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_lvl smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_lvl_smoothaccel_252d_sm504_3d_v079_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_to_asset smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_to_asset_smoothaccel_63d_sm252_3d_v080_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_to_asset smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_to_asset_smoothaccel_252d_sm504_3d_v081_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_to_equity smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_to_equity_smoothaccel_63d_sm252_3d_v082_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_to_equity smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_to_equity_smoothaccel_252d_sm504_3d_v083_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of amort_to_intang smoothed over 252d
def f042itg_f042_intangibles_goodwill_amort_to_intang_smoothaccel_63d_sm252_3d_v084_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of amort_to_intang smoothed over 504d
def f042itg_f042_intangibles_goodwill_amort_to_intang_smoothaccel_252d_sm504_3d_v085_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_per_share smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_per_share_smoothaccel_63d_sm252_3d_v086_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_per_share smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_per_share_smoothaccel_252d_sm504_3d_v087_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_yoy smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_yoy_smoothaccel_63d_sm252_3d_v088_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_yoy smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_yoy_smoothaccel_252d_sm504_3d_v089_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_to_mcap smoothed over 252d
def f042itg_f042_intangibles_goodwill_intang_to_mcap_smoothaccel_63d_sm252_3d_v090_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_to_mcap smoothed over 504d
def f042itg_f042_intangibles_goodwill_intang_to_mcap_smoothaccel_252d_sm504_3d_v091_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accelz_21d_z252_3d_v092_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_accelz_63d_z504_3d_v093_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accelz_21d_z252_3d_v094_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_accelz_63d_z504_3d_v095_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accelz_21d_z252_3d_v096_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_accelz_63d_z504_3d_v097_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accelz_21d_z252_3d_v098_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_accelz_63d_z504_3d_v099_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accelz_21d_z252_3d_v100_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_accelz_63d_z504_3d_v101_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accelz_21d_z252_3d_v102_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_accelz_63d_z504_3d_v103_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accelz_21d_z252_3d_v104_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_accelz_63d_z504_3d_v105_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_lvl (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_lvl_signflip_63d_3d_v106_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_lvl (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_lvl_signflip_252d_3d_v107_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_to_asset (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_asset_signflip_63d_3d_v108_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_to_asset (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_asset_signflip_252d_3d_v109_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_to_equity (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_equity_signflip_63d_3d_v110_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_to_equity (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_equity_signflip_252d_3d_v111_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in amort_to_intang (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_amort_to_intang_signflip_63d_3d_v112_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in amort_to_intang (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_amort_to_intang_signflip_252d_3d_v113_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_per_share (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_per_share_signflip_63d_3d_v114_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_per_share (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_per_share_signflip_252d_3d_v115_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_yoy (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_yoy_signflip_63d_3d_v116_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_yoy (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_yoy_signflip_252d_3d_v117_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_to_mcap (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_mcap_signflip_63d_3d_v118_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_to_mcap (raw count, no price scaling)
def f042itg_f042_intangibles_goodwill_intang_to_mcap_signflip_252d_3d_v119_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_lvl normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_lvl_rngaccel_63d_r252_3d_v120_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_lvl normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_lvl_rngaccel_252d_r504_3d_v121_signal(intangibles, closeadj):
    base = intangibles
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_asset normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_to_asset_rngaccel_63d_r252_3d_v122_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_asset normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_to_asset_rngaccel_252d_r504_3d_v123_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_equity normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_to_equity_rngaccel_63d_r252_3d_v124_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_equity normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_to_equity_rngaccel_252d_r504_3d_v125_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_to_intang normalized by 252d range
def f042itg_f042_intangibles_goodwill_amort_to_intang_rngaccel_63d_r252_3d_v126_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_to_intang normalized by 504d range
def f042itg_f042_intangibles_goodwill_amort_to_intang_rngaccel_252d_r504_3d_v127_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_per_share normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_per_share_rngaccel_63d_r252_3d_v128_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_per_share normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_per_share_rngaccel_252d_r504_3d_v129_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_yoy normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_yoy_rngaccel_63d_r252_3d_v130_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_yoy normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_yoy_rngaccel_252d_r504_3d_v131_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_to_mcap normalized by 252d range
def f042itg_f042_intangibles_goodwill_intang_to_mcap_rngaccel_63d_r252_3d_v132_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_to_mcap normalized by 504d range
def f042itg_f042_intangibles_goodwill_intang_to_mcap_rngaccel_252d_r504_3d_v133_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_cumslope_21d_3d_v134_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_cumslope_63d_3d_v135_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_cumslope_252d_3d_v136_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_cumslope_21d_3d_v137_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_cumslope_63d_3d_v138_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_cumslope_252d_3d_v139_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_cumslope_21d_3d_v140_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_cumslope_63d_3d_v141_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_cumslope_252d_3d_v142_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_cumslope_21d_3d_v143_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_cumslope_63d_3d_v144_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_cumslope_252d_3d_v145_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_cumslope_21d_3d_v146_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_cumslope_63d_3d_v147_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_cumslope_252d_3d_v148_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_cumslope_21d_3d_v149_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_cumslope_63d_3d_v150_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

