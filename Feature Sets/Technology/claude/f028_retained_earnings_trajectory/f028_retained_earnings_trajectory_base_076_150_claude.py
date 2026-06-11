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
def _f028_retearn_share(retearn, equity):
    return retearn / equity.replace(0, np.nan).abs()


# 63d z-score of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_z_63d_base_v076_signal(retearn, closeadj):
    base = retearn
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_z_126d_base_v077_signal(retearn, closeadj):
    base = retearn
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_z_252d_base_v078_signal(retearn, closeadj):
    base = retearn
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_z_504d_base_v079_signal(retearn, closeadj):
    base = retearn
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_z_63d_base_v080_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_z_126d_base_v081_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_z_252d_base_v082_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_z_504d_base_v083_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_z_63d_base_v084_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_z_126d_base_v085_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_z_252d_base_v086_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_z_504d_base_v087_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_z_63d_base_v088_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_z_126d_base_v089_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_z_252d_base_v090_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_z_504d_base_v091_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_z_63d_base_v092_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_z_126d_base_v093_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_z_252d_base_v094_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_z_504d_base_v095_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_z_63d_base_v096_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_z_126d_base_v097_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_z_252d_base_v098_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_z_504d_base_v099_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_z_63d_base_v100_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_z_126d_base_v101_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_z_252d_base_v102_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_z_504d_base_v103_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_distmax_252d_base_v104_signal(retearn, closeadj):
    base = retearn
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_distmax_504d_base_v105_signal(retearn, closeadj):
    base = retearn
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_distmax_252d_base_v106_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_distmax_504d_base_v107_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_distmax_252d_base_v108_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_distmax_504d_base_v109_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_distmax_252d_base_v110_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_distmax_504d_base_v111_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_distmax_252d_base_v112_signal(retearn, closeadj):
    base = np.sign(retearn)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_distmax_504d_base_v113_signal(retearn, closeadj):
    base = np.sign(retearn)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_distmax_252d_base_v114_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_distmax_504d_base_v115_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_distmax_252d_base_v116_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_distmax_504d_base_v117_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_distmed_126d_base_v118_signal(retearn, closeadj):
    base = retearn
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_distmed_252d_base_v119_signal(retearn, closeadj):
    base = retearn
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_distmed_504d_base_v120_signal(retearn, closeadj):
    base = retearn
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_distmed_126d_base_v121_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_distmed_252d_base_v122_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_distmed_504d_base_v123_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_distmed_126d_base_v124_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_distmed_252d_base_v125_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_distmed_504d_base_v126_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_distmed_126d_base_v127_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_distmed_252d_base_v128_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_distmed_504d_base_v129_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_distmed_126d_base_v130_signal(retearn, closeadj):
    base = np.sign(retearn)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_distmed_252d_base_v131_signal(retearn, closeadj):
    base = np.sign(retearn)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_distmed_504d_base_v132_signal(retearn, closeadj):
    base = np.sign(retearn)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_distmed_126d_base_v133_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_distmed_252d_base_v134_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_distmed_504d_base_v135_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_distmed_126d_base_v136_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_distmed_252d_base_v137_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_distmed_504d_base_v138_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_chg_63d_base_v139_signal(retearn, closeadj):
    base = retearn
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_chg_252d_base_v140_signal(retearn, closeadj):
    base = retearn
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_chg_63d_base_v141_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_chg_252d_base_v142_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_chg_63d_base_v143_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_chg_252d_base_v144_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_chg_63d_base_v145_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_chg_252d_base_v146_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_chg_63d_base_v147_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_chg_252d_base_v148_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_chg_63d_base_v149_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_chg_252d_base_v150_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

