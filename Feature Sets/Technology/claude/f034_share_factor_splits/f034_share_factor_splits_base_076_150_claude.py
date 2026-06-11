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
def _f034_sf_chg(sharefactor):
    return sharefactor.diff()


# 63d z-score of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_z_63d_base_v076_signal(sharefactor, closeadj):
    base = sharefactor
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_z_126d_base_v077_signal(sharefactor, closeadj):
    base = sharefactor
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_z_252d_base_v078_signal(sharefactor, closeadj):
    base = sharefactor
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_z_504d_base_v079_signal(sharefactor, closeadj):
    base = sharefactor
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_z_63d_base_v080_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_z_126d_base_v081_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_z_252d_base_v082_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_z_504d_base_v083_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_log
def f034sfs_f034_share_factor_splits_sf_log_z_63d_base_v084_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_log
def f034sfs_f034_share_factor_splits_sf_log_z_126d_base_v085_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_log
def f034sfs_f034_share_factor_splits_sf_log_z_252d_base_v086_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_log
def f034sfs_f034_share_factor_splits_sf_log_z_504d_base_v087_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_z_63d_base_v088_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_z_126d_base_v089_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_z_252d_base_v090_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_z_504d_base_v091_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_z_63d_base_v092_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_z_126d_base_v093_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_z_252d_base_v094_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_z_504d_base_v095_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_z_63d_base_v096_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_z_126d_base_v097_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_z_252d_base_v098_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_z_504d_base_v099_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_z_63d_base_v100_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_z_126d_base_v101_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_z_252d_base_v102_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_z_504d_base_v103_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_distmax_252d_base_v104_signal(sharefactor, closeadj):
    base = sharefactor
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_distmax_504d_base_v105_signal(sharefactor, closeadj):
    base = sharefactor
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_distmax_252d_base_v106_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_distmax_504d_base_v107_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_log
def f034sfs_f034_share_factor_splits_sf_log_distmax_252d_base_v108_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_log
def f034sfs_f034_share_factor_splits_sf_log_distmax_504d_base_v109_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_distmax_252d_base_v110_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_distmax_504d_base_v111_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_distmax_252d_base_v112_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_distmax_504d_base_v113_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_distmax_252d_base_v114_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_distmax_504d_base_v115_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_distmax_252d_base_v116_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_distmax_504d_base_v117_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_distmed_126d_base_v118_signal(sharefactor, closeadj):
    base = sharefactor
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_distmed_252d_base_v119_signal(sharefactor, closeadj):
    base = sharefactor
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_distmed_504d_base_v120_signal(sharefactor, closeadj):
    base = sharefactor
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_distmed_126d_base_v121_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_distmed_252d_base_v122_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_distmed_504d_base_v123_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_distmed_126d_base_v124_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_distmed_252d_base_v125_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_distmed_504d_base_v126_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_distmed_126d_base_v127_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_distmed_252d_base_v128_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_distmed_504d_base_v129_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_distmed_126d_base_v130_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_distmed_252d_base_v131_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_distmed_504d_base_v132_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_distmed_126d_base_v133_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_distmed_252d_base_v134_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_distmed_504d_base_v135_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_distmed_126d_base_v136_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_distmed_252d_base_v137_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_distmed_504d_base_v138_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_chg_63d_base_v139_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_chg_252d_base_v140_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_chg_63d_base_v141_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_chg_252d_base_v142_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_log
def f034sfs_f034_share_factor_splits_sf_log_chg_63d_base_v143_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_log
def f034sfs_f034_share_factor_splits_sf_log_chg_252d_base_v144_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_chg_63d_base_v145_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_chg_252d_base_v146_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_chg_63d_base_v147_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_chg_252d_base_v148_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_chg_63d_base_v149_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_chg_252d_base_v150_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

