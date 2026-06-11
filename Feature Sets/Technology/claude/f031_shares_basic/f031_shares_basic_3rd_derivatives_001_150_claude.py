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
def _f031_share_yoy(sharesbas):
    return sharesbas.pct_change(periods=252)


# 21d acceleration of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accel_21d_3d_v001_signal(sharesbas, closeadj):
    base = sharesbas
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accel_63d_3d_v002_signal(sharesbas, closeadj):
    base = sharesbas
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accel_126d_3d_v003_signal(sharesbas, closeadj):
    base = sharesbas
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accel_252d_3d_v004_signal(sharesbas, closeadj):
    base = sharesbas
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accel_21d_3d_v005_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accel_63d_3d_v006_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accel_126d_3d_v007_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accel_252d_3d_v008_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accel_21d_3d_v009_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accel_63d_3d_v010_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accel_126d_3d_v011_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accel_252d_3d_v012_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accel_21d_3d_v013_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accel_63d_3d_v014_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accel_126d_3d_v015_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accel_252d_3d_v016_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accel_21d_3d_v017_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accel_63d_3d_v018_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accel_126d_3d_v019_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accel_252d_3d_v020_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accel_21d_3d_v021_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accel_63d_3d_v022_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accel_126d_3d_v023_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accel_252d_3d_v024_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accel_21d_3d_v025_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accel_63d_3d_v026_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accel_126d_3d_v027_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accel_252d_3d_v028_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slopez_21d_z126_3d_v029_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slopez_63d_z252_3d_v030_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slopez_126d_z252_3d_v031_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slopez_252d_z504_3d_v032_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slopez_21d_z126_3d_v033_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slopez_63d_z252_3d_v034_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slopez_126d_z252_3d_v035_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slopez_252d_z504_3d_v036_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slopez_21d_z126_3d_v037_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slopez_63d_z252_3d_v038_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slopez_126d_z252_3d_v039_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slopez_252d_z504_3d_v040_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slopez_21d_z126_3d_v041_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slopez_63d_z252_3d_v042_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slopez_126d_z252_3d_v043_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slopez_252d_z504_3d_v044_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slopez_21d_z126_3d_v045_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slopez_63d_z252_3d_v046_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slopez_126d_z252_3d_v047_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slopez_252d_z504_3d_v048_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slopez_21d_z126_3d_v049_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slopez_63d_z252_3d_v050_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slopez_126d_z252_3d_v051_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slopez_252d_z504_3d_v052_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slopez_21d_z126_3d_v053_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slopez_63d_z252_3d_v054_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slopez_126d_z252_3d_v055_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slopez_252d_z504_3d_v056_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_jerk_21d_3d_v057_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_jerk_63d_3d_v058_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_jerk_126d_3d_v059_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_jerk_21d_3d_v060_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_jerk_63d_3d_v061_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_jerk_126d_3d_v062_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_jerk_21d_3d_v063_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_jerk_63d_3d_v064_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_jerk_126d_3d_v065_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_jerk_21d_3d_v066_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_jerk_63d_3d_v067_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_jerk_126d_3d_v068_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_jerk_21d_3d_v069_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_jerk_63d_3d_v070_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_jerk_126d_3d_v071_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_jerk_21d_3d_v072_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_jerk_63d_3d_v073_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_jerk_126d_3d_v074_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_jerk_21d_3d_v075_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_jerk_63d_3d_v076_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_jerk_126d_3d_v077_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_lvl smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_lvl_smoothaccel_63d_sm252_3d_v078_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_lvl smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_lvl_smoothaccel_252d_sm504_3d_v079_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_log smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_log_smoothaccel_63d_sm252_3d_v080_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_log smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_log_smoothaccel_252d_sm504_3d_v081_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_qoq smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_qoq_smoothaccel_63d_sm252_3d_v082_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_qoq smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_qoq_smoothaccel_252d_sm504_3d_v083_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_yoy smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_yoy_smoothaccel_63d_sm252_3d_v084_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_yoy smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_yoy_smoothaccel_252d_sm504_3d_v085_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_3y smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_3y_smoothaccel_63d_sm252_3d_v086_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_3y smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_3y_smoothaccel_252d_sm504_3d_v087_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_5y smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_5y_smoothaccel_63d_sm252_3d_v088_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_5y smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_5y_smoothaccel_252d_sm504_3d_v089_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sharesbas_to_mcap smoothed over 252d
def f031shb_f031_shares_basic_sharesbas_to_mcap_smoothaccel_63d_sm252_3d_v090_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sharesbas_to_mcap smoothed over 504d
def f031shb_f031_shares_basic_sharesbas_to_mcap_smoothaccel_252d_sm504_3d_v091_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accelz_21d_z252_3d_v092_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_accelz_63d_z504_3d_v093_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accelz_21d_z252_3d_v094_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_accelz_63d_z504_3d_v095_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accelz_21d_z252_3d_v096_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_accelz_63d_z504_3d_v097_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accelz_21d_z252_3d_v098_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_accelz_63d_z504_3d_v099_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accelz_21d_z252_3d_v100_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_accelz_63d_z504_3d_v101_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accelz_21d_z252_3d_v102_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_accelz_63d_z504_3d_v103_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accelz_21d_z252_3d_v104_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_accelz_63d_z504_3d_v105_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_lvl (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_lvl_signflip_63d_3d_v106_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_lvl (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_lvl_signflip_252d_3d_v107_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_log (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_log_signflip_63d_3d_v108_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_log (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_log_signflip_252d_3d_v109_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_qoq (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_qoq_signflip_63d_3d_v110_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_qoq (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_qoq_signflip_252d_3d_v111_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_yoy (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_yoy_signflip_63d_3d_v112_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_yoy (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_yoy_signflip_252d_3d_v113_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_3y (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_3y_signflip_63d_3d_v114_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_3y (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_3y_signflip_252d_3d_v115_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_5y (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_5y_signflip_63d_3d_v116_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_5y (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_5y_signflip_252d_3d_v117_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sharesbas_to_mcap (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_to_mcap_signflip_63d_3d_v118_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sharesbas_to_mcap (raw count, no price scaling)
def f031shb_f031_shares_basic_sharesbas_to_mcap_signflip_252d_3d_v119_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_lvl normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_lvl_rngaccel_63d_r252_3d_v120_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_lvl normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_lvl_rngaccel_252d_r504_3d_v121_signal(sharesbas, closeadj):
    base = sharesbas
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_log normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_log_rngaccel_63d_r252_3d_v122_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_log normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_log_rngaccel_252d_r504_3d_v123_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_qoq normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_qoq_rngaccel_63d_r252_3d_v124_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_qoq normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_qoq_rngaccel_252d_r504_3d_v125_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_yoy normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_yoy_rngaccel_63d_r252_3d_v126_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_yoy normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_yoy_rngaccel_252d_r504_3d_v127_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_3y normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_3y_rngaccel_63d_r252_3d_v128_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_3y normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_3y_rngaccel_252d_r504_3d_v129_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_5y normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_5y_rngaccel_63d_r252_3d_v130_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_5y normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_5y_rngaccel_252d_r504_3d_v131_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sharesbas_to_mcap normalized by 252d range
def f031shb_f031_shares_basic_sharesbas_to_mcap_rngaccel_63d_r252_3d_v132_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sharesbas_to_mcap normalized by 504d range
def f031shb_f031_shares_basic_sharesbas_to_mcap_rngaccel_252d_r504_3d_v133_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_cumslope_21d_3d_v134_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_cumslope_63d_3d_v135_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_cumslope_252d_3d_v136_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_cumslope_21d_3d_v137_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_cumslope_63d_3d_v138_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_cumslope_252d_3d_v139_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_cumslope_21d_3d_v140_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_cumslope_63d_3d_v141_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_cumslope_252d_3d_v142_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_cumslope_21d_3d_v143_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_cumslope_63d_3d_v144_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_cumslope_252d_3d_v145_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_cumslope_21d_3d_v146_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_cumslope_63d_3d_v147_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_cumslope_252d_3d_v148_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_cumslope_21d_3d_v149_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_cumslope_63d_3d_v150_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

