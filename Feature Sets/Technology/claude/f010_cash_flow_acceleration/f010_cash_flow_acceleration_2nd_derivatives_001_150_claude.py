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


# 21d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slope_21d_2d_v001_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slope_63d_2d_v002_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slope_126d_2d_v003_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slope_252d_2d_v004_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_slope_504d_2d_v005_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slope_21d_2d_v006_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slope_63d_2d_v007_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slope_126d_2d_v008_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slope_252d_2d_v009_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_slope_504d_2d_v010_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slope_21d_2d_v011_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slope_63d_2d_v012_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slope_126d_2d_v013_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slope_252d_2d_v014_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_slope_504d_2d_v015_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slope_21d_2d_v016_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slope_63d_2d_v017_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slope_126d_2d_v018_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slope_252d_2d_v019_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_slope_504d_2d_v020_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slope_21d_2d_v021_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slope_63d_2d_v022_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slope_126d_2d_v023_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slope_252d_2d_v024_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_slope_504d_2d_v025_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slope_21d_2d_v026_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slope_63d_2d_v027_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slope_126d_2d_v028_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slope_252d_2d_v029_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_slope_504d_2d_v030_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slope_21d_2d_v031_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slope_63d_2d_v032_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slope_126d_2d_v033_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slope_252d_2d_v034_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_slope_504d_2d_v035_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slope_21d_2d_v036_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slope_63d_2d_v037_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slope_126d_2d_v038_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slope_252d_2d_v039_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_slope_504d_2d_v040_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sm21_sl21_2d_v041_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sm63_sl21_2d_v042_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sm63_sl63_2d_v043_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sm252_sl63_2d_v044_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sm252_sl126_2d_v045_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sm21_sl21_2d_v046_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sm63_sl21_2d_v047_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sm63_sl63_2d_v048_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sm252_sl63_2d_v049_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sm252_sl126_2d_v050_signal(ncfo, closeadj):
    base = _mean(_f010_ocf_change(ncfo, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sm21_sl21_2d_v051_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sm63_sl21_2d_v052_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sm63_sl63_2d_v053_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sm252_sl63_2d_v054_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sm252_sl126_2d_v055_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sm21_sl21_2d_v056_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sm63_sl21_2d_v057_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sm63_sl63_2d_v058_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sm252_sl63_2d_v059_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sm252_sl126_2d_v060_signal(fcf, closeadj):
    base = _mean(_f010_fcf_change(fcf, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sm21_sl21_2d_v061_signal(ncfo, closeadj):
    base = _mean(ncfo / ncfo.shift(252).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sm63_sl21_2d_v062_signal(ncfo, closeadj):
    base = _mean(ncfo / ncfo.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sm63_sl63_2d_v063_signal(ncfo, closeadj):
    base = _mean(ncfo / ncfo.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sm252_sl63_2d_v064_signal(ncfo, closeadj):
    base = _mean(ncfo / ncfo.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sm252_sl126_2d_v065_signal(ncfo, closeadj):
    base = _mean(ncfo / ncfo.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sm21_sl21_2d_v066_signal(fcf, closeadj):
    base = _mean(fcf / fcf.shift(252).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sm63_sl21_2d_v067_signal(fcf, closeadj):
    base = _mean(fcf / fcf.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sm63_sl63_2d_v068_signal(fcf, closeadj):
    base = _mean(fcf / fcf.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sm252_sl63_2d_v069_signal(fcf, closeadj):
    base = _mean(fcf / fcf.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sm252_sl126_2d_v070_signal(fcf, closeadj):
    base = _mean(fcf / fcf.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sm21_sl21_2d_v071_signal(ncfo, closeadj):
    base = _mean(np.sign(ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sm63_sl21_2d_v072_signal(ncfo, closeadj):
    base = _mean(np.sign(ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sm63_sl63_2d_v073_signal(ncfo, closeadj):
    base = _mean(np.sign(ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sm252_sl63_2d_v074_signal(ncfo, closeadj):
    base = _mean(np.sign(ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sm252_sl126_2d_v075_signal(ncfo, closeadj):
    base = _mean(np.sign(ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sm21_sl21_2d_v076_signal(fcf, closeadj):
    base = _mean(np.sign(fcf), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sm63_sl21_2d_v077_signal(fcf, closeadj):
    base = _mean(np.sign(fcf), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sm63_sl63_2d_v078_signal(fcf, closeadj):
    base = _mean(np.sign(fcf), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sm252_sl63_2d_v079_signal(fcf, closeadj):
    base = _mean(np.sign(fcf), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sm252_sl126_2d_v080_signal(fcf, closeadj):
    base = _mean(np.sign(fcf), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_pctslope_21d_2d_v081_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_pctslope_63d_2d_v082_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_pctslope_252d_2d_v083_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_pctslope_21d_2d_v084_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_pctslope_63d_2d_v085_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_pctslope_252d_2d_v086_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_pctslope_21d_2d_v087_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_pctslope_63d_2d_v088_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_pctslope_252d_2d_v089_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_pctslope_21d_2d_v090_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_pctslope_63d_2d_v091_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_pctslope_252d_2d_v092_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_pctslope_21d_2d_v093_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_pctslope_63d_2d_v094_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_pctslope_252d_2d_v095_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_pctslope_21d_2d_v096_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_pctslope_63d_2d_v097_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_pctslope_252d_2d_v098_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_pctslope_21d_2d_v099_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_pctslope_63d_2d_v100_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_pctslope_252d_2d_v101_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_pctslope_21d_2d_v102_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_pctslope_63d_2d_v103_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_pctslope_252d_2d_v104_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sgnslope_21d_2d_v105_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sgnslope_63d_2d_v106_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_sgnslope_252d_2d_v107_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sgnslope_21d_2d_v108_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sgnslope_63d_2d_v109_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_sgnslope_252d_2d_v110_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sgnslope_21d_2d_v111_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sgnslope_63d_2d_v112_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_sgnslope_252d_2d_v113_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sgnslope_21d_2d_v114_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sgnslope_63d_2d_v115_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_sgnslope_252d_2d_v116_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sgnslope_21d_2d_v117_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sgnslope_63d_2d_v118_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_sgnslope_252d_2d_v119_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sgnslope_21d_2d_v120_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sgnslope_63d_2d_v121_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_sgnslope_252d_2d_v122_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sgnslope_21d_2d_v123_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sgnslope_63d_2d_v124_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_sgnslope_252d_2d_v125_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sgnslope_21d_2d_v126_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sgnslope_63d_2d_v127_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_sgnslope_252d_2d_v128_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_logmagslope_21d_2d_v129_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_logmagslope_63d_2d_v130_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_logmagslope_252d_2d_v131_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_logmagslope_21d_2d_v132_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_logmagslope_63d_2d_v133_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_logmagslope_252d_2d_v134_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_logmagslope_21d_2d_v135_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_logmagslope_63d_2d_v136_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_logmagslope_252d_2d_v137_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_logmagslope_21d_2d_v138_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_logmagslope_63d_2d_v139_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_logmagslope_252d_2d_v140_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_logmagslope_21d_2d_v141_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_logmagslope_63d_2d_v142_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_logmagslope_252d_2d_v143_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_logmagslope_21d_2d_v144_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_logmagslope_63d_2d_v145_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_logmagslope_252d_2d_v146_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_logmagslope_21d_2d_v147_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_logmagslope_63d_2d_v148_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_logmagslope_252d_2d_v149_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_logmagslope_21d_2d_v150_signal(fcf, closeadj):
    base = np.sign(fcf)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

