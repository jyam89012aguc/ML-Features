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
def _f030_solv(assets, liabilities):
    return assets - liabilities


# 21d mean of solv_gap scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_gap_mean_21d_base_v001_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of solv_gap scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_gap_mean_63d_base_v002_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of solv_gap scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_gap_mean_126d_base_v003_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of solv_gap scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_gap_mean_252d_base_v004_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of solv_gap scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_gap_mean_504d_base_v005_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liab_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_to_asset_mean_21d_base_v006_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liab_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_to_asset_mean_63d_base_v007_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liab_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_to_asset_mean_126d_base_v008_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liab_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_to_asset_mean_252d_base_v009_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liab_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_to_asset_mean_504d_base_v010_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of solv_ratio scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_ratio_mean_21d_base_v011_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of solv_ratio scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_ratio_mean_63d_base_v012_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of solv_ratio scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_ratio_mean_126d_base_v013_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of solv_ratio scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_ratio_mean_252d_base_v014_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of solv_ratio scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_ratio_mean_504d_base_v015_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of equity_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_equity_to_asset_mean_21d_base_v016_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of equity_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_equity_to_asset_mean_63d_base_v017_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of equity_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_equity_to_asset_mean_126d_base_v018_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of equity_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_equity_to_asset_mean_252d_base_v019_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of equity_to_asset scaled by closeadj
def f030alg_f030_asset_liability_gap_equity_to_asset_mean_504d_base_v020_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of neg_equity_flag scaled by closeadj
def f030alg_f030_asset_liability_gap_neg_equity_flag_mean_21d_base_v021_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of neg_equity_flag scaled by closeadj
def f030alg_f030_asset_liability_gap_neg_equity_flag_mean_63d_base_v022_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of neg_equity_flag scaled by closeadj
def f030alg_f030_asset_liability_gap_neg_equity_flag_mean_126d_base_v023_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of neg_equity_flag scaled by closeadj
def f030alg_f030_asset_liability_gap_neg_equity_flag_mean_252d_base_v024_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of neg_equity_flag scaled by closeadj
def f030alg_f030_asset_liability_gap_neg_equity_flag_mean_504d_base_v025_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of solv_per_share scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_per_share_mean_21d_base_v026_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of solv_per_share scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_per_share_mean_63d_base_v027_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of solv_per_share scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_per_share_mean_126d_base_v028_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of solv_per_share scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_per_share_mean_252d_base_v029_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of solv_per_share scaled by closeadj
def f030alg_f030_asset_liability_gap_solv_per_share_mean_504d_base_v030_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liab_minus_eq scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_minus_eq_mean_21d_base_v031_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liab_minus_eq scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_minus_eq_mean_63d_base_v032_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liab_minus_eq scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_minus_eq_mean_126d_base_v033_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liab_minus_eq scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_minus_eq_mean_252d_base_v034_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liab_minus_eq scaled by closeadj
def f030alg_f030_asset_liability_gap_liab_minus_eq_mean_504d_base_v035_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_median_63d_base_v036_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_median_252d_base_v037_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_median_504d_base_v038_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_median_63d_base_v039_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_median_252d_base_v040_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_median_504d_base_v041_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_median_63d_base_v042_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_median_252d_base_v043_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_median_504d_base_v044_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_median_63d_base_v045_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_median_252d_base_v046_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_median_504d_base_v047_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_median_63d_base_v048_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_median_252d_base_v049_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_median_504d_base_v050_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_median_63d_base_v051_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_median_252d_base_v052_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_median_504d_base_v053_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_median_63d_base_v054_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_median_252d_base_v055_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_median_504d_base_v056_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_rmax_252d_base_v057_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_rmax_504d_base_v058_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_rmax_252d_base_v059_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_rmax_504d_base_v060_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_rmax_252d_base_v061_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_rmax_504d_base_v062_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_rmax_252d_base_v063_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_rmax_504d_base_v064_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_rmax_252d_base_v065_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_rmax_504d_base_v066_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_rmax_252d_base_v067_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_rmax_504d_base_v068_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_rmax_252d_base_v069_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_rmax_504d_base_v070_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_rmin_252d_base_v071_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_rmin_504d_base_v072_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_rmin_252d_base_v073_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_rmin_504d_base_v074_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_rmin_252d_base_v075_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

