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
def _f030_solv(assets, liabilities):
    return assets - liabilities


# 21d acceleration of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accel_21d_3d_v001_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accel_63d_3d_v002_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accel_126d_3d_v003_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accel_252d_3d_v004_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accel_21d_3d_v005_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accel_63d_3d_v006_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accel_126d_3d_v007_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accel_252d_3d_v008_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accel_21d_3d_v009_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accel_63d_3d_v010_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accel_126d_3d_v011_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accel_252d_3d_v012_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accel_21d_3d_v013_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accel_63d_3d_v014_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accel_126d_3d_v015_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accel_252d_3d_v016_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accel_21d_3d_v017_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accel_63d_3d_v018_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accel_126d_3d_v019_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accel_252d_3d_v020_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accel_21d_3d_v021_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accel_63d_3d_v022_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accel_126d_3d_v023_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accel_252d_3d_v024_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accel_21d_3d_v025_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accel_63d_3d_v026_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accel_126d_3d_v027_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accel_252d_3d_v028_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slopez_21d_z126_3d_v029_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slopez_63d_z252_3d_v030_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slopez_126d_z252_3d_v031_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slopez_252d_z504_3d_v032_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slopez_21d_z126_3d_v033_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slopez_63d_z252_3d_v034_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slopez_126d_z252_3d_v035_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slopez_252d_z504_3d_v036_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slopez_21d_z126_3d_v037_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slopez_63d_z252_3d_v038_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slopez_126d_z252_3d_v039_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slopez_252d_z504_3d_v040_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slopez_21d_z126_3d_v041_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slopez_63d_z252_3d_v042_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slopez_126d_z252_3d_v043_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slopez_252d_z504_3d_v044_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slopez_21d_z126_3d_v045_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slopez_63d_z252_3d_v046_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slopez_126d_z252_3d_v047_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slopez_252d_z504_3d_v048_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slopez_21d_z126_3d_v049_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slopez_63d_z252_3d_v050_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slopez_126d_z252_3d_v051_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slopez_252d_z504_3d_v052_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slopez_21d_z126_3d_v053_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slopez_63d_z252_3d_v054_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slopez_126d_z252_3d_v055_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slopez_252d_z504_3d_v056_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_jerk_21d_3d_v057_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_jerk_63d_3d_v058_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_jerk_126d_3d_v059_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_jerk_21d_3d_v060_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_jerk_63d_3d_v061_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_jerk_126d_3d_v062_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_jerk_21d_3d_v063_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_jerk_63d_3d_v064_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_jerk_126d_3d_v065_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_jerk_21d_3d_v066_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_jerk_63d_3d_v067_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_jerk_126d_3d_v068_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_jerk_21d_3d_v069_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_jerk_63d_3d_v070_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_jerk_126d_3d_v071_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_jerk_21d_3d_v072_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_jerk_63d_3d_v073_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_jerk_126d_3d_v074_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_jerk_21d_3d_v075_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_jerk_63d_3d_v076_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_jerk_126d_3d_v077_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of solv_gap smoothed over 252d
def f030alg_f030_asset_liability_gap_solv_gap_smoothaccel_63d_sm252_3d_v078_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of solv_gap smoothed over 504d
def f030alg_f030_asset_liability_gap_solv_gap_smoothaccel_252d_sm504_3d_v079_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liab_to_asset smoothed over 252d
def f030alg_f030_asset_liability_gap_liab_to_asset_smoothaccel_63d_sm252_3d_v080_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liab_to_asset smoothed over 504d
def f030alg_f030_asset_liability_gap_liab_to_asset_smoothaccel_252d_sm504_3d_v081_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of solv_ratio smoothed over 252d
def f030alg_f030_asset_liability_gap_solv_ratio_smoothaccel_63d_sm252_3d_v082_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of solv_ratio smoothed over 504d
def f030alg_f030_asset_liability_gap_solv_ratio_smoothaccel_252d_sm504_3d_v083_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of equity_to_asset smoothed over 252d
def f030alg_f030_asset_liability_gap_equity_to_asset_smoothaccel_63d_sm252_3d_v084_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of equity_to_asset smoothed over 504d
def f030alg_f030_asset_liability_gap_equity_to_asset_smoothaccel_252d_sm504_3d_v085_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of neg_equity_flag smoothed over 252d
def f030alg_f030_asset_liability_gap_neg_equity_flag_smoothaccel_63d_sm252_3d_v086_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of neg_equity_flag smoothed over 504d
def f030alg_f030_asset_liability_gap_neg_equity_flag_smoothaccel_252d_sm504_3d_v087_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of solv_per_share smoothed over 252d
def f030alg_f030_asset_liability_gap_solv_per_share_smoothaccel_63d_sm252_3d_v088_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of solv_per_share smoothed over 504d
def f030alg_f030_asset_liability_gap_solv_per_share_smoothaccel_252d_sm504_3d_v089_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liab_minus_eq smoothed over 252d
def f030alg_f030_asset_liability_gap_liab_minus_eq_smoothaccel_63d_sm252_3d_v090_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liab_minus_eq smoothed over 504d
def f030alg_f030_asset_liability_gap_liab_minus_eq_smoothaccel_252d_sm504_3d_v091_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accelz_21d_z252_3d_v092_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_accelz_63d_z504_3d_v093_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accelz_21d_z252_3d_v094_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_accelz_63d_z504_3d_v095_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accelz_21d_z252_3d_v096_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_accelz_63d_z504_3d_v097_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accelz_21d_z252_3d_v098_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_accelz_63d_z504_3d_v099_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accelz_21d_z252_3d_v100_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_accelz_63d_z504_3d_v101_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accelz_21d_z252_3d_v102_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_accelz_63d_z504_3d_v103_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accelz_21d_z252_3d_v104_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_accelz_63d_z504_3d_v105_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in solv_gap (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_gap_signflip_63d_3d_v106_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in solv_gap (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_gap_signflip_252d_3d_v107_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liab_to_asset (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_liab_to_asset_signflip_63d_3d_v108_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liab_to_asset (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_liab_to_asset_signflip_252d_3d_v109_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in solv_ratio (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_ratio_signflip_63d_3d_v110_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in solv_ratio (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_ratio_signflip_252d_3d_v111_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in equity_to_asset (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_equity_to_asset_signflip_63d_3d_v112_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in equity_to_asset (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_equity_to_asset_signflip_252d_3d_v113_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in neg_equity_flag (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_neg_equity_flag_signflip_63d_3d_v114_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in neg_equity_flag (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_neg_equity_flag_signflip_252d_3d_v115_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in solv_per_share (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_per_share_signflip_63d_3d_v116_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in solv_per_share (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_solv_per_share_signflip_252d_3d_v117_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liab_minus_eq (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_liab_minus_eq_signflip_63d_3d_v118_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liab_minus_eq (raw count, no price scaling)
def f030alg_f030_asset_liability_gap_liab_minus_eq_signflip_252d_3d_v119_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_gap normalized by 252d range
def f030alg_f030_asset_liability_gap_solv_gap_rngaccel_63d_r252_3d_v120_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_gap normalized by 504d range
def f030alg_f030_asset_liability_gap_solv_gap_rngaccel_252d_r504_3d_v121_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liab_to_asset normalized by 252d range
def f030alg_f030_asset_liability_gap_liab_to_asset_rngaccel_63d_r252_3d_v122_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liab_to_asset normalized by 504d range
def f030alg_f030_asset_liability_gap_liab_to_asset_rngaccel_252d_r504_3d_v123_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_ratio normalized by 252d range
def f030alg_f030_asset_liability_gap_solv_ratio_rngaccel_63d_r252_3d_v124_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_ratio normalized by 504d range
def f030alg_f030_asset_liability_gap_solv_ratio_rngaccel_252d_r504_3d_v125_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of equity_to_asset normalized by 252d range
def f030alg_f030_asset_liability_gap_equity_to_asset_rngaccel_63d_r252_3d_v126_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of equity_to_asset normalized by 504d range
def f030alg_f030_asset_liability_gap_equity_to_asset_rngaccel_252d_r504_3d_v127_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of neg_equity_flag normalized by 252d range
def f030alg_f030_asset_liability_gap_neg_equity_flag_rngaccel_63d_r252_3d_v128_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of neg_equity_flag normalized by 504d range
def f030alg_f030_asset_liability_gap_neg_equity_flag_rngaccel_252d_r504_3d_v129_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of solv_per_share normalized by 252d range
def f030alg_f030_asset_liability_gap_solv_per_share_rngaccel_63d_r252_3d_v130_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of solv_per_share normalized by 504d range
def f030alg_f030_asset_liability_gap_solv_per_share_rngaccel_252d_r504_3d_v131_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liab_minus_eq normalized by 252d range
def f030alg_f030_asset_liability_gap_liab_minus_eq_rngaccel_63d_r252_3d_v132_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liab_minus_eq normalized by 504d range
def f030alg_f030_asset_liability_gap_liab_minus_eq_rngaccel_252d_r504_3d_v133_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_cumslope_21d_3d_v134_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_cumslope_63d_3d_v135_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_cumslope_252d_3d_v136_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_cumslope_21d_3d_v137_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_cumslope_63d_3d_v138_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_cumslope_252d_3d_v139_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_cumslope_21d_3d_v140_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_cumslope_63d_3d_v141_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_cumslope_252d_3d_v142_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_cumslope_21d_3d_v143_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_cumslope_63d_3d_v144_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_cumslope_252d_3d_v145_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_cumslope_21d_3d_v146_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_cumslope_63d_3d_v147_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_cumslope_252d_3d_v148_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_cumslope_21d_3d_v149_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_cumslope_63d_3d_v150_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

