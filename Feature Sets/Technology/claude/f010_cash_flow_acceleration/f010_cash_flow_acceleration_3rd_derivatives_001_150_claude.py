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
def _f010_ocf_change(ncfo, n):
    return ncfo.diff(periods=n)


def _f010_fcf_change(fcf, n):
    return fcf.diff(periods=n)


def _f010_cf_signflip(s):
    return (np.sign(s) != np.sign(s.shift(1))).astype(float)


# 21d acceleration of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accel_21d_3d_v001_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accel_63d_3d_v002_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accel_126d_3d_v003_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accel_252d_3d_v004_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accel_21d_3d_v005_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accel_63d_3d_v006_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accel_126d_3d_v007_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accel_252d_3d_v008_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accel_21d_3d_v009_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accel_63d_3d_v010_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accel_126d_3d_v011_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accel_252d_3d_v012_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accel_21d_3d_v013_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accel_63d_3d_v014_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accel_126d_3d_v015_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accel_252d_3d_v016_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accel_21d_3d_v017_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accel_63d_3d_v018_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accel_126d_3d_v019_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accel_252d_3d_v020_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accel_21d_3d_v021_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accel_63d_3d_v022_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accel_126d_3d_v023_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accel_252d_3d_v024_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accel_21d_3d_v025_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accel_63d_3d_v026_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accel_126d_3d_v027_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accel_252d_3d_v028_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accel_21d_3d_v029_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accel_63d_3d_v030_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accel_126d_3d_v031_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accel_252d_3d_v032_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slopez_21d_z126_3d_v033_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slopez_63d_z252_3d_v034_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slopez_126d_z252_3d_v035_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slopez_252d_z504_3d_v036_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slopez_21d_z126_3d_v037_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slopez_63d_z252_3d_v038_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slopez_126d_z252_3d_v039_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slopez_252d_z504_3d_v040_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slopez_21d_z126_3d_v041_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slopez_63d_z252_3d_v042_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slopez_126d_z252_3d_v043_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slopez_252d_z504_3d_v044_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slopez_21d_z126_3d_v045_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slopez_63d_z252_3d_v046_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slopez_126d_z252_3d_v047_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slopez_252d_z504_3d_v048_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slopez_21d_z126_3d_v049_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slopez_63d_z252_3d_v050_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slopez_126d_z252_3d_v051_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slopez_252d_z504_3d_v052_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slopez_21d_z126_3d_v053_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slopez_63d_z252_3d_v054_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slopez_126d_z252_3d_v055_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slopez_252d_z504_3d_v056_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slopez_21d_z126_3d_v057_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slopez_63d_z252_3d_v058_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slopez_126d_z252_3d_v059_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slopez_252d_z504_3d_v060_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slopez_21d_z126_3d_v061_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slopez_63d_z252_3d_v062_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slopez_126d_z252_3d_v063_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slopez_252d_z504_3d_v064_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_jerk_21d_3d_v065_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_jerk_63d_3d_v066_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_jerk_126d_3d_v067_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_jerk_21d_3d_v068_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_jerk_63d_3d_v069_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_jerk_126d_3d_v070_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_jerk_21d_3d_v071_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_jerk_63d_3d_v072_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_jerk_126d_3d_v073_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_jerk_21d_3d_v074_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_jerk_63d_3d_v075_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_jerk_126d_3d_v076_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_jerk_21d_3d_v077_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_jerk_63d_3d_v078_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_jerk_126d_3d_v079_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_jerk_21d_3d_v080_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_jerk_63d_3d_v081_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_jerk_126d_3d_v082_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_jerk_21d_3d_v083_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_jerk_63d_3d_v084_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_jerk_126d_3d_v085_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_jerk_21d_3d_v086_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_jerk_63d_3d_v087_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_jerk_126d_3d_v088_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_qchg smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_smoothaccel_63d_sm252_3d_v089_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_qchg smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_smoothaccel_252d_sm504_3d_v090_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_ychg smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_smoothaccel_63d_sm252_3d_v091_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_ychg smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_smoothaccel_252d_sm504_3d_v092_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_qchg smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_smoothaccel_63d_sm252_3d_v093_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_qchg smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_smoothaccel_252d_sm504_3d_v094_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_ychg smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_smoothaccel_63d_sm252_3d_v095_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_ychg smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_smoothaccel_252d_sm504_3d_v096_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_pastlevel smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_smoothaccel_63d_sm252_3d_v097_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_pastlevel smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_smoothaccel_252d_sm504_3d_v098_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_to_pastlevel smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_smoothaccel_63d_sm252_3d_v099_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_to_pastlevel smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_smoothaccel_252d_sm504_3d_v100_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_sign smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_ocf_sign_smoothaccel_63d_sm252_3d_v101_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_sign smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_ocf_sign_smoothaccel_252d_sm504_3d_v102_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_sign smoothed over 252d
def f010cfa_f010_cash_flow_acceleration_fcf_sign_smoothaccel_63d_sm252_3d_v103_signal(fcf, closeadj):
    base = np.sign(fcf)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_sign smoothed over 504d
def f010cfa_f010_cash_flow_acceleration_fcf_sign_smoothaccel_252d_sm504_3d_v104_signal(fcf, closeadj):
    base = np.sign(fcf)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accelz_21d_z252_3d_v105_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_accelz_63d_z504_3d_v106_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accelz_21d_z252_3d_v107_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_accelz_63d_z504_3d_v108_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accelz_21d_z252_3d_v109_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_accelz_63d_z504_3d_v110_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accelz_21d_z252_3d_v111_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_accelz_63d_z504_3d_v112_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accelz_21d_z252_3d_v113_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_accelz_63d_z504_3d_v114_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accelz_21d_z252_3d_v115_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_accelz_63d_z504_3d_v116_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accelz_21d_z252_3d_v117_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_accelz_63d_z504_3d_v118_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accelz_21d_z252_3d_v119_signal(fcf, closeadj):
    base = np.sign(fcf)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_accelz_63d_z504_3d_v120_signal(fcf, closeadj):
    base = np.sign(fcf)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_qchg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_signflip_63d_3d_v121_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_qchg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_signflip_252d_3d_v122_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_ychg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_signflip_63d_3d_v123_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_ychg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_signflip_252d_3d_v124_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_qchg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_signflip_63d_3d_v125_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_qchg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_signflip_252d_3d_v126_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_ychg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_signflip_63d_3d_v127_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_ychg (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_signflip_252d_3d_v128_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_pastlevel (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_signflip_63d_3d_v129_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_pastlevel (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_signflip_252d_3d_v130_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_to_pastlevel (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_signflip_63d_3d_v131_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_to_pastlevel (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_signflip_252d_3d_v132_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_sign (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_sign_signflip_63d_3d_v133_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_sign (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_ocf_sign_signflip_252d_3d_v134_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_sign (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_sign_signflip_63d_3d_v135_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_sign (raw count, no price scaling)
def f010cfa_f010_cash_flow_acceleration_fcf_sign_signflip_252d_3d_v136_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_qchg normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_rngaccel_63d_r252_3d_v137_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_qchg normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_rngaccel_252d_r504_3d_v138_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_ychg normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_rngaccel_63d_r252_3d_v139_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_ychg normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_rngaccel_252d_r504_3d_v140_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_qchg normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_rngaccel_63d_r252_3d_v141_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_qchg normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_rngaccel_252d_r504_3d_v142_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_ychg normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_rngaccel_63d_r252_3d_v143_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_ychg normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_rngaccel_252d_r504_3d_v144_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_pastlevel normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_rngaccel_63d_r252_3d_v145_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_pastlevel normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_rngaccel_252d_r504_3d_v146_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_to_pastlevel normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_rngaccel_63d_r252_3d_v147_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_to_pastlevel normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_rngaccel_252d_r504_3d_v148_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_sign normalized by 252d range
def f010cfa_f010_cash_flow_acceleration_ocf_sign_rngaccel_63d_r252_3d_v149_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_sign normalized by 504d range
def f010cfa_f010_cash_flow_acceleration_ocf_sign_rngaccel_252d_r504_3d_v150_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

