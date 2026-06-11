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
def _f014_ocf_vol(ncfo, w):
    return ncfo.rolling(w, min_periods=max(1, w//2)).std()


def _f014_fcf_vol(fcf, w):
    return fcf.rolling(w, min_periods=max(1, w//2)).std()


def _f014_cv(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std() / s.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan).abs()


# 21d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_slope_21d_2d_v001_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_slope_63d_2d_v002_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_slope_126d_2d_v003_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_slope_252d_2d_v004_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_slope_504d_2d_v005_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_slope_21d_2d_v006_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_slope_63d_2d_v007_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_slope_126d_2d_v008_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_slope_252d_2d_v009_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_slope_504d_2d_v010_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_slope_21d_2d_v011_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_slope_63d_2d_v012_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_slope_126d_2d_v013_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_slope_252d_2d_v014_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_slope_504d_2d_v015_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_slope_21d_2d_v016_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_slope_63d_2d_v017_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_slope_126d_2d_v018_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_slope_252d_2d_v019_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_slope_504d_2d_v020_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_slope_21d_2d_v021_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_slope_63d_2d_v022_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_slope_126d_2d_v023_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_slope_252d_2d_v024_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_slope_504d_2d_v025_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_slope_21d_2d_v026_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_slope_63d_2d_v027_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_slope_126d_2d_v028_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_slope_252d_2d_v029_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_slope_504d_2d_v030_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_slope_21d_2d_v031_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_slope_63d_2d_v032_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_slope_126d_2d_v033_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_slope_252d_2d_v034_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_slope_504d_2d_v035_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_slope_21d_2d_v036_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_slope_63d_2d_v037_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_slope_126d_2d_v038_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_slope_252d_2d_v039_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_slope_504d_2d_v040_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sm21_sl21_2d_v041_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sm63_sl21_2d_v042_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sm63_sl63_2d_v043_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sm252_sl63_2d_v044_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sm252_sl126_2d_v045_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sm21_sl21_2d_v046_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sm63_sl21_2d_v047_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sm63_sl63_2d_v048_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sm252_sl63_2d_v049_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sm252_sl126_2d_v050_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sm21_sl21_2d_v051_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sm63_sl21_2d_v052_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sm63_sl63_2d_v053_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sm252_sl63_2d_v054_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sm252_sl126_2d_v055_signal(ncfo, closeadj):
    base = _mean(_f014_ocf_vol(ncfo, 504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sm21_sl21_2d_v056_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sm63_sl21_2d_v057_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sm63_sl63_2d_v058_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sm252_sl63_2d_v059_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sm252_sl126_2d_v060_signal(fcf, closeadj):
    base = _mean(_f014_fcf_vol(fcf, 504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sm21_sl21_2d_v061_signal(ncfi, closeadj):
    base = _mean(ncfi.rolling(252, min_periods=126).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sm63_sl21_2d_v062_signal(ncfi, closeadj):
    base = _mean(ncfi.rolling(252, min_periods=126).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sm63_sl63_2d_v063_signal(ncfi, closeadj):
    base = _mean(ncfi.rolling(252, min_periods=126).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sm252_sl63_2d_v064_signal(ncfi, closeadj):
    base = _mean(ncfi.rolling(252, min_periods=126).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sm252_sl126_2d_v065_signal(ncfi, closeadj):
    base = _mean(ncfi.rolling(252, min_periods=126).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sm21_sl21_2d_v066_signal(ncff, closeadj):
    base = _mean(ncff.rolling(252, min_periods=126).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sm63_sl21_2d_v067_signal(ncff, closeadj):
    base = _mean(ncff.rolling(252, min_periods=126).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sm63_sl63_2d_v068_signal(ncff, closeadj):
    base = _mean(ncff.rolling(252, min_periods=126).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sm252_sl63_2d_v069_signal(ncff, closeadj):
    base = _mean(ncff.rolling(252, min_periods=126).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sm252_sl126_2d_v070_signal(ncff, closeadj):
    base = _mean(ncff.rolling(252, min_periods=126).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sm21_sl21_2d_v071_signal(ncfo, closeadj):
    base = _mean(_f014_cv(ncfo, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sm63_sl21_2d_v072_signal(ncfo, closeadj):
    base = _mean(_f014_cv(ncfo, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sm63_sl63_2d_v073_signal(ncfo, closeadj):
    base = _mean(_f014_cv(ncfo, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sm252_sl63_2d_v074_signal(ncfo, closeadj):
    base = _mean(_f014_cv(ncfo, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sm252_sl126_2d_v075_signal(ncfo, closeadj):
    base = _mean(_f014_cv(ncfo, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sm21_sl21_2d_v076_signal(fcf, closeadj):
    base = _mean(_f014_cv(fcf, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sm63_sl21_2d_v077_signal(fcf, closeadj):
    base = _mean(_f014_cv(fcf, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sm63_sl63_2d_v078_signal(fcf, closeadj):
    base = _mean(_f014_cv(fcf, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sm252_sl63_2d_v079_signal(fcf, closeadj):
    base = _mean(_f014_cv(fcf, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sm252_sl126_2d_v080_signal(fcf, closeadj):
    base = _mean(_f014_cv(fcf, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_pctslope_21d_2d_v081_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_pctslope_63d_2d_v082_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_pctslope_252d_2d_v083_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_pctslope_21d_2d_v084_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_pctslope_63d_2d_v085_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_pctslope_252d_2d_v086_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_pctslope_21d_2d_v087_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_pctslope_63d_2d_v088_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_pctslope_252d_2d_v089_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_pctslope_21d_2d_v090_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_pctslope_63d_2d_v091_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_pctslope_252d_2d_v092_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_pctslope_21d_2d_v093_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_pctslope_63d_2d_v094_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_pctslope_252d_2d_v095_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_pctslope_21d_2d_v096_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_pctslope_63d_2d_v097_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_pctslope_252d_2d_v098_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_pctslope_21d_2d_v099_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_pctslope_63d_2d_v100_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_pctslope_252d_2d_v101_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_pctslope_21d_2d_v102_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_pctslope_63d_2d_v103_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_pctslope_252d_2d_v104_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sgnslope_21d_2d_v105_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sgnslope_63d_2d_v106_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_sgnslope_252d_2d_v107_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sgnslope_21d_2d_v108_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sgnslope_63d_2d_v109_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_sgnslope_252d_2d_v110_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sgnslope_21d_2d_v111_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sgnslope_63d_2d_v112_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_sgnslope_252d_2d_v113_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sgnslope_21d_2d_v114_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sgnslope_63d_2d_v115_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_sgnslope_252d_2d_v116_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sgnslope_21d_2d_v117_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sgnslope_63d_2d_v118_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_sgnslope_252d_2d_v119_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sgnslope_21d_2d_v120_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sgnslope_63d_2d_v121_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_sgnslope_252d_2d_v122_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sgnslope_21d_2d_v123_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sgnslope_63d_2d_v124_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_sgnslope_252d_2d_v125_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sgnslope_21d_2d_v126_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sgnslope_63d_2d_v127_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_sgnslope_252d_2d_v128_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_logmagslope_21d_2d_v129_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_logmagslope_63d_2d_v130_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_logmagslope_252d_2d_v131_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_logmagslope_21d_2d_v132_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_logmagslope_63d_2d_v133_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_logmagslope_252d_2d_v134_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_logmagslope_21d_2d_v135_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_logmagslope_63d_2d_v136_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_logmagslope_252d_2d_v137_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_logmagslope_21d_2d_v138_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_logmagslope_63d_2d_v139_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_logmagslope_252d_2d_v140_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_logmagslope_21d_2d_v141_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_logmagslope_63d_2d_v142_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_logmagslope_252d_2d_v143_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_logmagslope_21d_2d_v144_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_logmagslope_63d_2d_v145_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_logmagslope_252d_2d_v146_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_logmagslope_21d_2d_v147_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_logmagslope_63d_2d_v148_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_logmagslope_252d_2d_v149_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_logmagslope_21d_2d_v150_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

