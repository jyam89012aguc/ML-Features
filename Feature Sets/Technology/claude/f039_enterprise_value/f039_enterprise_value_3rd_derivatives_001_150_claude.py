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
def _f039_ev_to_mcap(ev, marketcap):
    return ev / marketcap.replace(0, np.nan).abs()


# 21d acceleration of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accel_21d_3d_v001_signal(ev, closeadj):
    base = ev
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accel_63d_3d_v002_signal(ev, closeadj):
    base = ev
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accel_126d_3d_v003_signal(ev, closeadj):
    base = ev
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accel_252d_3d_v004_signal(ev, closeadj):
    base = ev
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accel_21d_3d_v005_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accel_63d_3d_v006_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accel_126d_3d_v007_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accel_252d_3d_v008_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accel_21d_3d_v009_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accel_63d_3d_v010_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accel_126d_3d_v011_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accel_252d_3d_v012_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accel_21d_3d_v013_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accel_63d_3d_v014_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accel_126d_3d_v015_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accel_252d_3d_v016_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_ev
def f039env_f039_enterprise_value_log_ev_accel_21d_3d_v017_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_ev
def f039env_f039_enterprise_value_log_ev_accel_63d_3d_v018_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_ev
def f039env_f039_enterprise_value_log_ev_accel_126d_3d_v019_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_ev
def f039env_f039_enterprise_value_log_ev_accel_252d_3d_v020_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accel_21d_3d_v021_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accel_63d_3d_v022_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accel_126d_3d_v023_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accel_252d_3d_v024_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accel_21d_3d_v025_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accel_63d_3d_v026_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accel_126d_3d_v027_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accel_252d_3d_v028_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slopez_21d_z126_3d_v029_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slopez_63d_z252_3d_v030_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slopez_126d_z252_3d_v031_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slopez_252d_z504_3d_v032_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slopez_21d_z126_3d_v033_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slopez_63d_z252_3d_v034_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slopez_126d_z252_3d_v035_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slopez_252d_z504_3d_v036_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slopez_21d_z126_3d_v037_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slopez_63d_z252_3d_v038_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slopez_126d_z252_3d_v039_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slopez_252d_z504_3d_v040_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slopez_21d_z126_3d_v041_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slopez_63d_z252_3d_v042_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slopez_126d_z252_3d_v043_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slopez_252d_z504_3d_v044_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_ev
def f039env_f039_enterprise_value_log_ev_slopez_21d_z126_3d_v045_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_ev
def f039env_f039_enterprise_value_log_ev_slopez_63d_z252_3d_v046_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_ev
def f039env_f039_enterprise_value_log_ev_slopez_126d_z252_3d_v047_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_ev
def f039env_f039_enterprise_value_log_ev_slopez_252d_z504_3d_v048_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slopez_21d_z126_3d_v049_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slopez_63d_z252_3d_v050_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slopez_126d_z252_3d_v051_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slopez_252d_z504_3d_v052_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slopez_21d_z126_3d_v053_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slopez_63d_z252_3d_v054_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slopez_126d_z252_3d_v055_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slopez_252d_z504_3d_v056_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_jerk_21d_3d_v057_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_jerk_63d_3d_v058_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_jerk_126d_3d_v059_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_jerk_21d_3d_v060_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_jerk_63d_3d_v061_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_jerk_126d_3d_v062_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_jerk_21d_3d_v063_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_jerk_63d_3d_v064_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_jerk_126d_3d_v065_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_jerk_21d_3d_v066_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_jerk_63d_3d_v067_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_jerk_126d_3d_v068_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_ev
def f039env_f039_enterprise_value_log_ev_jerk_21d_3d_v069_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_ev
def f039env_f039_enterprise_value_log_ev_jerk_63d_3d_v070_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_ev
def f039env_f039_enterprise_value_log_ev_jerk_126d_3d_v071_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_jerk_21d_3d_v072_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_jerk_63d_3d_v073_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_jerk_126d_3d_v074_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_jerk_21d_3d_v075_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_jerk_63d_3d_v076_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_jerk_126d_3d_v077_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_lvl smoothed over 252d
def f039env_f039_enterprise_value_ev_lvl_smoothaccel_63d_sm252_3d_v078_signal(ev, closeadj):
    base = ev
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_lvl smoothed over 504d
def f039env_f039_enterprise_value_ev_lvl_smoothaccel_252d_sm504_3d_v079_signal(ev, closeadj):
    base = ev
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_to_mcap smoothed over 252d
def f039env_f039_enterprise_value_ev_to_mcap_smoothaccel_63d_sm252_3d_v080_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_to_mcap smoothed over 504d
def f039env_f039_enterprise_value_ev_to_mcap_smoothaccel_252d_sm504_3d_v081_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_minus_mcap smoothed over 252d
def f039env_f039_enterprise_value_ev_minus_mcap_smoothaccel_63d_sm252_3d_v082_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_minus_mcap smoothed over 504d
def f039env_f039_enterprise_value_ev_minus_mcap_smoothaccel_252d_sm504_3d_v083_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_neg_flag smoothed over 252d
def f039env_f039_enterprise_value_ev_neg_flag_smoothaccel_63d_sm252_3d_v084_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_neg_flag smoothed over 504d
def f039env_f039_enterprise_value_ev_neg_flag_smoothaccel_252d_sm504_3d_v085_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_ev smoothed over 252d
def f039env_f039_enterprise_value_log_ev_smoothaccel_63d_sm252_3d_v086_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_ev smoothed over 504d
def f039env_f039_enterprise_value_log_ev_smoothaccel_252d_sm504_3d_v087_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_per_share smoothed over 252d
def f039env_f039_enterprise_value_ev_per_share_smoothaccel_63d_sm252_3d_v088_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_per_share smoothed over 504d
def f039env_f039_enterprise_value_ev_per_share_smoothaccel_252d_sm504_3d_v089_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_to_asset smoothed over 252d
def f039env_f039_enterprise_value_ev_to_asset_smoothaccel_63d_sm252_3d_v090_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_to_asset smoothed over 504d
def f039env_f039_enterprise_value_ev_to_asset_smoothaccel_252d_sm504_3d_v091_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accelz_21d_z252_3d_v092_signal(ev, closeadj):
    base = ev
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_accelz_63d_z504_3d_v093_signal(ev, closeadj):
    base = ev
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accelz_21d_z252_3d_v094_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_accelz_63d_z504_3d_v095_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accelz_21d_z252_3d_v096_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_accelz_63d_z504_3d_v097_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accelz_21d_z252_3d_v098_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_accelz_63d_z504_3d_v099_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_ev
def f039env_f039_enterprise_value_log_ev_accelz_21d_z252_3d_v100_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_ev
def f039env_f039_enterprise_value_log_ev_accelz_63d_z504_3d_v101_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accelz_21d_z252_3d_v102_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_accelz_63d_z504_3d_v103_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accelz_21d_z252_3d_v104_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_accelz_63d_z504_3d_v105_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_lvl (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_lvl_signflip_63d_3d_v106_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_lvl (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_lvl_signflip_252d_3d_v107_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_to_mcap (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_to_mcap_signflip_63d_3d_v108_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_to_mcap (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_to_mcap_signflip_252d_3d_v109_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_minus_mcap (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_minus_mcap_signflip_63d_3d_v110_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_minus_mcap (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_minus_mcap_signflip_252d_3d_v111_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_neg_flag (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_neg_flag_signflip_63d_3d_v112_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_neg_flag (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_neg_flag_signflip_252d_3d_v113_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_ev (raw count, no price scaling)
def f039env_f039_enterprise_value_log_ev_signflip_63d_3d_v114_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_ev (raw count, no price scaling)
def f039env_f039_enterprise_value_log_ev_signflip_252d_3d_v115_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_per_share (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_per_share_signflip_63d_3d_v116_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_per_share (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_per_share_signflip_252d_3d_v117_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_to_asset (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_to_asset_signflip_63d_3d_v118_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_to_asset (raw count, no price scaling)
def f039env_f039_enterprise_value_ev_to_asset_signflip_252d_3d_v119_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_lvl normalized by 252d range
def f039env_f039_enterprise_value_ev_lvl_rngaccel_63d_r252_3d_v120_signal(ev, closeadj):
    base = ev
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_lvl normalized by 504d range
def f039env_f039_enterprise_value_ev_lvl_rngaccel_252d_r504_3d_v121_signal(ev, closeadj):
    base = ev
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_mcap normalized by 252d range
def f039env_f039_enterprise_value_ev_to_mcap_rngaccel_63d_r252_3d_v122_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_mcap normalized by 504d range
def f039env_f039_enterprise_value_ev_to_mcap_rngaccel_252d_r504_3d_v123_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_minus_mcap normalized by 252d range
def f039env_f039_enterprise_value_ev_minus_mcap_rngaccel_63d_r252_3d_v124_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_minus_mcap normalized by 504d range
def f039env_f039_enterprise_value_ev_minus_mcap_rngaccel_252d_r504_3d_v125_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_neg_flag normalized by 252d range
def f039env_f039_enterprise_value_ev_neg_flag_rngaccel_63d_r252_3d_v126_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_neg_flag normalized by 504d range
def f039env_f039_enterprise_value_ev_neg_flag_rngaccel_252d_r504_3d_v127_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_ev normalized by 252d range
def f039env_f039_enterprise_value_log_ev_rngaccel_63d_r252_3d_v128_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_ev normalized by 504d range
def f039env_f039_enterprise_value_log_ev_rngaccel_252d_r504_3d_v129_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_per_share normalized by 252d range
def f039env_f039_enterprise_value_ev_per_share_rngaccel_63d_r252_3d_v130_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_per_share normalized by 504d range
def f039env_f039_enterprise_value_ev_per_share_rngaccel_252d_r504_3d_v131_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_to_asset normalized by 252d range
def f039env_f039_enterprise_value_ev_to_asset_rngaccel_63d_r252_3d_v132_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_to_asset normalized by 504d range
def f039env_f039_enterprise_value_ev_to_asset_rngaccel_252d_r504_3d_v133_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_cumslope_21d_3d_v134_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_cumslope_63d_3d_v135_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_cumslope_252d_3d_v136_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_cumslope_21d_3d_v137_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_cumslope_63d_3d_v138_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_cumslope_252d_3d_v139_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_cumslope_21d_3d_v140_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_cumslope_63d_3d_v141_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_cumslope_252d_3d_v142_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_cumslope_21d_3d_v143_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_cumslope_63d_3d_v144_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_cumslope_252d_3d_v145_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of log_ev
def f039env_f039_enterprise_value_log_ev_cumslope_21d_3d_v146_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of log_ev
def f039env_f039_enterprise_value_log_ev_cumslope_63d_3d_v147_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of log_ev
def f039env_f039_enterprise_value_log_ev_cumslope_252d_3d_v148_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_cumslope_21d_3d_v149_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_cumslope_63d_3d_v150_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

