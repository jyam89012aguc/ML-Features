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
def _f014_ocf_vol(ncfo, w):
    return ncfo.rolling(w, min_periods=max(1, w//2)).std()


def _f014_fcf_vol(fcf, w):
    return fcf.rolling(w, min_periods=max(1, w//2)).std()


def _f014_cv(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std() / s.rolling(w, min_periods=max(1, w//2)).mean().replace(0, np.nan).abs()


# 21d mean of ocf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_mean_21d_base_v001_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_mean_63d_base_v002_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_mean_126d_base_v003_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_mean_252d_base_v004_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_mean_504d_base_v005_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_mean_21d_base_v006_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_mean_63d_base_v007_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_mean_126d_base_v008_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_mean_252d_base_v009_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_mean_504d_base_v010_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_mean_21d_base_v011_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_mean_63d_base_v012_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_mean_126d_base_v013_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_mean_252d_base_v014_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_mean_504d_base_v015_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_mean_21d_base_v016_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_mean_63d_base_v017_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_mean_126d_base_v018_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_mean_252d_base_v019_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_504d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_mean_504d_base_v020_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncfi_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_mean_21d_base_v021_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfi_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_mean_63d_base_v022_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfi_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_mean_126d_base_v023_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfi_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_mean_252d_base_v024_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfi_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_mean_504d_base_v025_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncff_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_mean_21d_base_v026_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncff_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_mean_63d_base_v027_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncff_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_mean_126d_base_v028_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncff_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_mean_252d_base_v029_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncff_252d_std scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_mean_504d_base_v030_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_mean_21d_base_v031_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_mean_63d_base_v032_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_mean_126d_base_v033_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_mean_252d_base_v034_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_mean_504d_base_v035_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_mean_21d_base_v036_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_mean_63d_base_v037_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_mean_126d_base_v038_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_mean_252d_base_v039_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_cv_252d scaled by closeadj
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_mean_504d_base_v040_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_median_63d_base_v041_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_median_252d_base_v042_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_median_504d_base_v043_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_median_63d_base_v044_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_median_252d_base_v045_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_median_504d_base_v046_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_median_63d_base_v047_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_median_252d_base_v048_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_median_504d_base_v049_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_median_63d_base_v050_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_median_252d_base_v051_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_median_504d_base_v052_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_median_63d_base_v053_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_median_252d_base_v054_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_median_504d_base_v055_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_median_63d_base_v056_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_median_252d_base_v057_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_median_504d_base_v058_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_median_63d_base_v059_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_median_252d_base_v060_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_median_504d_base_v061_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_median_63d_base_v062_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_median_252d_base_v063_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_median_504d_base_v064_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_rmax_252d_base_v065_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_rmax_504d_base_v066_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_rmax_252d_base_v067_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_rmax_504d_base_v068_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_rmax_252d_base_v069_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_rmax_504d_base_v070_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_rmax_252d_base_v071_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_rmax_504d_base_v072_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_rmax_252d_base_v073_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_rmax_504d_base_v074_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_rmax_252d_base_v075_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

