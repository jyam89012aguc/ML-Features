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
def _f010_ocf_change(ncfo, n):
    return ncfo.diff(periods=n)


def _f010_fcf_change(fcf, n):
    return fcf.diff(periods=n)


def _f010_cf_signflip(s):
    return (np.sign(s) != np.sign(s.shift(1))).astype(float)


# 21d mean of ocf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_mean_21d_base_v001_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_mean_63d_base_v002_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_mean_126d_base_v003_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_mean_252d_base_v004_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_mean_504d_base_v005_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_mean_21d_base_v006_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_mean_63d_base_v007_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_mean_126d_base_v008_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_mean_252d_base_v009_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_mean_504d_base_v010_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_mean_21d_base_v011_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_mean_63d_base_v012_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_mean_126d_base_v013_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_mean_252d_base_v014_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_qchg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_mean_504d_base_v015_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_mean_21d_base_v016_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_mean_63d_base_v017_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_mean_126d_base_v018_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_mean_252d_base_v019_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_ychg scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_mean_504d_base_v020_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_mean_21d_base_v021_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_mean_63d_base_v022_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_mean_126d_base_v023_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_mean_252d_base_v024_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_mean_504d_base_v025_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_mean_21d_base_v026_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_mean_63d_base_v027_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_mean_126d_base_v028_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_mean_252d_base_v029_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_to_pastlevel scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_mean_504d_base_v030_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_sign_mean_21d_base_v031_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_sign_mean_63d_base_v032_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_sign_mean_126d_base_v033_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_sign_mean_252d_base_v034_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_ocf_sign_mean_504d_base_v035_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_sign_mean_21d_base_v036_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_sign_mean_63d_base_v037_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_sign_mean_126d_base_v038_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_sign_mean_252d_base_v039_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_sign scaled by closeadj
def f010cfa_f010_cash_flow_acceleration_fcf_sign_mean_504d_base_v040_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_median_63d_base_v041_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_median_252d_base_v042_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_median_504d_base_v043_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_median_63d_base_v044_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_median_252d_base_v045_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_median_504d_base_v046_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_median_63d_base_v047_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_median_252d_base_v048_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_median_504d_base_v049_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_median_63d_base_v050_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_median_252d_base_v051_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_median_504d_base_v052_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_median_63d_base_v053_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_median_252d_base_v054_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_median_504d_base_v055_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_median_63d_base_v056_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_median_252d_base_v057_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_median_504d_base_v058_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_median_63d_base_v059_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_median_252d_base_v060_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_sign
def f010cfa_f010_cash_flow_acceleration_ocf_sign_median_504d_base_v061_signal(ncfo, closeadj):
    base = np.sign(ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_median_63d_base_v062_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_median_252d_base_v063_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_sign
def f010cfa_f010_cash_flow_acceleration_fcf_sign_median_504d_base_v064_signal(fcf, closeadj):
    base = np.sign(fcf)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_rmax_252d_base_v065_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_qchg
def f010cfa_f010_cash_flow_acceleration_ocf_qchg_rmax_504d_base_v066_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_rmax_252d_base_v067_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_ychg
def f010cfa_f010_cash_flow_acceleration_ocf_ychg_rmax_504d_base_v068_signal(ncfo, closeadj):
    base = _f010_ocf_change(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_rmax_252d_base_v069_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_qchg
def f010cfa_f010_cash_flow_acceleration_fcf_qchg_rmax_504d_base_v070_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_rmax_252d_base_v071_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_ychg
def f010cfa_f010_cash_flow_acceleration_fcf_ychg_rmax_504d_base_v072_signal(fcf, closeadj):
    base = _f010_fcf_change(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_rmax_252d_base_v073_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_ocf_to_pastlevel_rmax_504d_base_v074_signal(ncfo, closeadj):
    base = ncfo / ncfo.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_to_pastlevel
def f010cfa_f010_cash_flow_acceleration_fcf_to_pastlevel_rmax_252d_base_v075_signal(fcf, closeadj):
    base = fcf / fcf.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

