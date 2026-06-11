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


# 63d z-score of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_z_63d_base_v076_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_z_126d_base_v077_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_z_252d_base_v078_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_z_504d_base_v079_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_z_63d_base_v080_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_z_126d_base_v081_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_z_252d_base_v082_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_z_504d_base_v083_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_z_63d_base_v084_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_z_126d_base_v085_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_z_252d_base_v086_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_z_504d_base_v087_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_z_63d_base_v088_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_z_126d_base_v089_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_z_252d_base_v090_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_z_504d_base_v091_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_z_63d_base_v092_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_z_126d_base_v093_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_z_252d_base_v094_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_z_504d_base_v095_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_z_63d_base_v096_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_z_126d_base_v097_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_z_252d_base_v098_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_z_504d_base_v099_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_z_63d_base_v100_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_z_126d_base_v101_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_z_252d_base_v102_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_z_504d_base_v103_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_distmax_252d_base_v104_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_distmax_504d_base_v105_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_distmax_252d_base_v106_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_distmax_504d_base_v107_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_distmax_252d_base_v108_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_distmax_504d_base_v109_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_distmax_252d_base_v110_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_distmax_504d_base_v111_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_distmax_252d_base_v112_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_distmax_504d_base_v113_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_distmax_252d_base_v114_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_distmax_504d_base_v115_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_distmax_252d_base_v116_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_distmax_504d_base_v117_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_distmed_126d_base_v118_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_distmed_252d_base_v119_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_distmed_504d_base_v120_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_distmed_126d_base_v121_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_distmed_252d_base_v122_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_distmed_504d_base_v123_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_distmed_126d_base_v124_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_distmed_252d_base_v125_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_distmed_504d_base_v126_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_distmed_126d_base_v127_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_distmed_252d_base_v128_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_distmed_504d_base_v129_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_distmed_126d_base_v130_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_distmed_252d_base_v131_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_distmed_504d_base_v132_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_distmed_126d_base_v133_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_distmed_252d_base_v134_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_distmed_504d_base_v135_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_distmed_126d_base_v136_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_distmed_252d_base_v137_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liab_minus_eq
def f030alg_f030_asset_liability_gap_liab_minus_eq_distmed_504d_base_v138_signal(liabilities, equity, closeadj):
    base = liabilities - equity
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_chg_63d_base_v139_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in solv_gap
def f030alg_f030_asset_liability_gap_solv_gap_chg_252d_base_v140_signal(assets, liabilities, closeadj):
    base = _f030_solv(assets, liabilities)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_chg_63d_base_v141_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liab_to_asset
def f030alg_f030_asset_liability_gap_liab_to_asset_chg_252d_base_v142_signal(liabilities, assets, closeadj):
    base = liabilities / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_chg_63d_base_v143_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in solv_ratio
def f030alg_f030_asset_liability_gap_solv_ratio_chg_252d_base_v144_signal(assets, liabilities, closeadj):
    base = assets / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_chg_63d_base_v145_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in equity_to_asset
def f030alg_f030_asset_liability_gap_equity_to_asset_chg_252d_base_v146_signal(equity, assets, closeadj):
    base = equity / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_chg_63d_base_v147_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in neg_equity_flag
def f030alg_f030_asset_liability_gap_neg_equity_flag_chg_252d_base_v148_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_chg_63d_base_v149_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in solv_per_share
def f030alg_f030_asset_liability_gap_solv_per_share_chg_252d_base_v150_signal(assets, liabilities, sharesbas, closeadj):
    base = _f030_solv(assets, liabilities) / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

