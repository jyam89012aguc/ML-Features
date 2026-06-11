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


# 21d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slope_21d_2d_v001_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slope_63d_2d_v002_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slope_126d_2d_v003_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slope_252d_2d_v004_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_slope_504d_2d_v005_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slope_21d_2d_v006_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slope_63d_2d_v007_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slope_126d_2d_v008_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slope_252d_2d_v009_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_slope_504d_2d_v010_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slope_21d_2d_v011_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slope_63d_2d_v012_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slope_126d_2d_v013_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slope_252d_2d_v014_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_slope_504d_2d_v015_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slope_21d_2d_v016_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slope_63d_2d_v017_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slope_126d_2d_v018_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slope_252d_2d_v019_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_slope_504d_2d_v020_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slope_21d_2d_v021_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slope_63d_2d_v022_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slope_126d_2d_v023_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slope_252d_2d_v024_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_slope_504d_2d_v025_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slope_21d_2d_v026_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slope_63d_2d_v027_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slope_126d_2d_v028_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slope_252d_2d_v029_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_slope_504d_2d_v030_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slope_21d_2d_v031_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slope_63d_2d_v032_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slope_126d_2d_v033_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slope_252d_2d_v034_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_slope_504d_2d_v035_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sm21_sl21_2d_v036_signal(assets, liabilities, closeadj):
    base = _mean(_f030_solv(assets, liabilities), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sm63_sl21_2d_v037_signal(assets, liabilities, closeadj):
    base = _mean(_f030_solv(assets, liabilities), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sm63_sl63_2d_v038_signal(assets, liabilities, closeadj):
    base = _mean(_f030_solv(assets, liabilities), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sm252_sl63_2d_v039_signal(assets, liabilities, closeadj):
    base = _mean(_f030_solv(assets, liabilities), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sm252_sl126_2d_v040_signal(assets, liabilities, closeadj):
    base = _mean(_f030_solv(assets, liabilities), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sm21_sl21_2d_v041_signal(liabilities, assets, closeadj):
    base = _mean(liabilities / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sm63_sl21_2d_v042_signal(liabilities, assets, closeadj):
    base = _mean(liabilities / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sm63_sl63_2d_v043_signal(liabilities, assets, closeadj):
    base = _mean(liabilities / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sm252_sl63_2d_v044_signal(liabilities, assets, closeadj):
    base = _mean(liabilities / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sm252_sl126_2d_v045_signal(liabilities, assets, closeadj):
    base = _mean(liabilities / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sm21_sl21_2d_v046_signal(assets, liabilities, closeadj):
    base = _mean(assets / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sm63_sl21_2d_v047_signal(assets, liabilities, closeadj):
    base = _mean(assets / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sm63_sl63_2d_v048_signal(assets, liabilities, closeadj):
    base = _mean(assets / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sm252_sl63_2d_v049_signal(assets, liabilities, closeadj):
    base = _mean(assets / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sm252_sl126_2d_v050_signal(assets, liabilities, closeadj):
    base = _mean(assets / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sm21_sl21_2d_v051_signal(equity, assets, closeadj):
    base = _mean(equity / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sm63_sl21_2d_v052_signal(equity, assets, closeadj):
    base = _mean(equity / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sm63_sl63_2d_v053_signal(equity, assets, closeadj):
    base = _mean(equity / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sm252_sl63_2d_v054_signal(equity, assets, closeadj):
    base = _mean(equity / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sm252_sl126_2d_v055_signal(equity, assets, closeadj):
    base = _mean(equity / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sm21_sl21_2d_v056_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sm63_sl21_2d_v057_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sm63_sl63_2d_v058_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sm252_sl63_2d_v059_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sm252_sl126_2d_v060_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sm21_sl21_2d_v061_signal(assets, liabilities, sharesbas, closeadj):
    base = _mean(_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sm63_sl21_2d_v062_signal(assets, liabilities, sharesbas, closeadj):
    base = _mean(_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sm63_sl63_2d_v063_signal(assets, liabilities, sharesbas, closeadj):
    base = _mean(_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sm252_sl63_2d_v064_signal(assets, liabilities, sharesbas, closeadj):
    base = _mean(_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sm252_sl126_2d_v065_signal(assets, liabilities, sharesbas, closeadj):
    base = _mean(_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sm21_sl21_2d_v066_signal(liabilities, equity, closeadj):
    base = _mean(liabilities - equity, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sm63_sl21_2d_v067_signal(liabilities, equity, closeadj):
    base = _mean(liabilities - equity, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sm63_sl63_2d_v068_signal(liabilities, equity, closeadj):
    base = _mean(liabilities - equity, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sm252_sl63_2d_v069_signal(liabilities, equity, closeadj):
    base = _mean(liabilities - equity, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sm252_sl126_2d_v070_signal(liabilities, equity, closeadj):
    base = _mean(liabilities - equity, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_pctslope_21d_2d_v071_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_pctslope_63d_2d_v072_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_pctslope_252d_2d_v073_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_pctslope_21d_2d_v074_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_pctslope_63d_2d_v075_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_pctslope_252d_2d_v076_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_pctslope_21d_2d_v077_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_pctslope_63d_2d_v078_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_pctslope_252d_2d_v079_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_pctslope_21d_2d_v080_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_pctslope_63d_2d_v081_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_pctslope_252d_2d_v082_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_pctslope_21d_2d_v083_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_pctslope_63d_2d_v084_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_pctslope_252d_2d_v085_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_pctslope_21d_2d_v086_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_pctslope_63d_2d_v087_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_pctslope_252d_2d_v088_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_pctslope_21d_2d_v089_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_pctslope_63d_2d_v090_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_pctslope_252d_2d_v091_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sgnslope_21d_2d_v092_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sgnslope_63d_2d_v093_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_sgnslope_252d_2d_v094_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sgnslope_21d_2d_v095_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sgnslope_63d_2d_v096_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_sgnslope_252d_2d_v097_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sgnslope_21d_2d_v098_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sgnslope_63d_2d_v099_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_sgnslope_252d_2d_v100_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sgnslope_21d_2d_v101_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sgnslope_63d_2d_v102_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_sgnslope_252d_2d_v103_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sgnslope_21d_2d_v104_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sgnslope_63d_2d_v105_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_sgnslope_252d_2d_v106_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sgnslope_21d_2d_v107_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sgnslope_63d_2d_v108_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_sgnslope_252d_2d_v109_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sgnslope_21d_2d_v110_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sgnslope_63d_2d_v111_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_sgnslope_252d_2d_v112_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_logmagslope_21d_2d_v113_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_logmagslope_63d_2d_v114_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_logmagslope_252d_2d_v115_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_logmagslope_21d_2d_v116_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_logmagslope_63d_2d_v117_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_logmagslope_252d_2d_v118_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_logmagslope_21d_2d_v119_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_logmagslope_63d_2d_v120_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_logmagslope_252d_2d_v121_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_logmagslope_21d_2d_v122_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_logmagslope_63d_2d_v123_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_logmagslope_252d_2d_v124_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_logmagslope_21d_2d_v125_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_logmagslope_63d_2d_v126_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_logmagslope_252d_2d_v127_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_logmagslope_21d_2d_v128_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_logmagslope_63d_2d_v129_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_logmagslope_252d_2d_v130_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_logmagslope_21d_2d_v131_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_logmagslope_63d_2d_v132_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_logmagslope_252d_2d_v133_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|solv_gap|
def f030alg_f030_asset_liability_gap_solv_gap_logslope_63d_2d_v134_signal(assets, liabilities, closeadj):
    base = np.log((_f030_solv(assets, liabilities)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|solv_gap|
def f030alg_f030_asset_liability_gap_solv_gap_logslope_252d_2d_v135_signal(assets, liabilities, closeadj):
    base = np.log((_f030_solv(assets, liabilities)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liab_to_asset|
def f030alg_f030_asset_liability_gap_liab_to_asset_logslope_63d_2d_v136_signal(liabilities, assets, closeadj):
    base = np.log((liabilities / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liab_to_asset|
def f030alg_f030_asset_liability_gap_liab_to_asset_logslope_252d_2d_v137_signal(liabilities, assets, closeadj):
    base = np.log((liabilities / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|solv_ratio|
def f030alg_f030_asset_liability_gap_solv_ratio_logslope_63d_2d_v138_signal(assets, liabilities, closeadj):
    base = np.log((assets / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|solv_ratio|
def f030alg_f030_asset_liability_gap_solv_ratio_logslope_252d_2d_v139_signal(assets, liabilities, closeadj):
    base = np.log((assets / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|equity_to_asset|
def f030alg_f030_asset_liability_gap_equity_to_asset_logslope_63d_2d_v140_signal(equity, assets, closeadj):
    base = np.log((equity / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|equity_to_asset|
def f030alg_f030_asset_liability_gap_equity_to_asset_logslope_252d_2d_v141_signal(equity, assets, closeadj):
    base = np.log((equity / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|neg_equity_flag|
def f030alg_f030_asset_liability_gap_neg_equity_flag_logslope_63d_2d_v142_signal(equity, closeadj):
    base = np.log(((equity < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|neg_equity_flag|
def f030alg_f030_asset_liability_gap_neg_equity_flag_logslope_252d_2d_v143_signal(equity, closeadj):
    base = np.log(((equity < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|solv_per_share|
def f030alg_f030_asset_liability_gap_solv_per_share_logslope_63d_2d_v144_signal(assets, liabilities, sharesbas, closeadj):
    base = np.log((_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|solv_per_share|
def f030alg_f030_asset_liability_gap_solv_per_share_logslope_252d_2d_v145_signal(assets, liabilities, sharesbas, closeadj):
    base = np.log((_f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liab_minus_eq|
def f030alg_f030_asset_liability_gap_liab_minus_eq_logslope_63d_2d_v146_signal(liabilities, equity, closeadj):
    base = np.log((liabilities - equity).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liab_minus_eq|
def f030alg_f030_asset_liability_gap_liab_minus_eq_logslope_252d_2d_v147_signal(liabilities, equity, closeadj):
    base = np.log((liabilities - equity).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

