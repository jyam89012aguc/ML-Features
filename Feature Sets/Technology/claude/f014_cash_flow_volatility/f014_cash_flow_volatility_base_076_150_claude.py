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


# 63d z-score of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_z_63d_base_v076_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_z_126d_base_v077_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_z_252d_base_v078_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_z_504d_base_v079_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_z_63d_base_v080_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_z_126d_base_v081_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_z_252d_base_v082_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_z_504d_base_v083_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_z_63d_base_v084_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_z_126d_base_v085_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_z_252d_base_v086_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_z_504d_base_v087_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_z_63d_base_v088_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_z_126d_base_v089_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_z_252d_base_v090_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_z_504d_base_v091_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_z_63d_base_v092_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_z_126d_base_v093_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_z_252d_base_v094_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_z_504d_base_v095_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_z_63d_base_v096_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_z_126d_base_v097_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_z_252d_base_v098_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_z_504d_base_v099_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_z_63d_base_v100_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_z_126d_base_v101_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_z_252d_base_v102_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_z_504d_base_v103_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_z_63d_base_v104_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_z_126d_base_v105_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_z_252d_base_v106_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_z_504d_base_v107_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_distmax_252d_base_v108_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_distmax_504d_base_v109_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_distmax_252d_base_v110_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_distmax_504d_base_v111_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_distmax_252d_base_v112_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_distmax_504d_base_v113_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_distmax_252d_base_v114_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_distmax_504d_base_v115_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_distmax_252d_base_v116_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_distmax_504d_base_v117_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_distmax_252d_base_v118_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_distmax_504d_base_v119_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_distmax_252d_base_v120_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_distmax_504d_base_v121_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_distmax_252d_base_v122_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_distmax_504d_base_v123_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_distmed_126d_base_v124_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_distmed_252d_base_v125_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_distmed_504d_base_v126_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_distmed_126d_base_v127_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_distmed_252d_base_v128_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_distmed_504d_base_v129_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_distmed_126d_base_v130_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_distmed_252d_base_v131_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_504d_std
def f014cfv_f014_cash_flow_volatility_ocf_504d_std_distmed_504d_base_v132_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_distmed_126d_base_v133_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_distmed_252d_base_v134_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_504d_std
def f014cfv_f014_cash_flow_volatility_fcf_504d_std_distmed_504d_base_v135_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_distmed_126d_base_v136_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_distmed_252d_base_v137_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfi_252d_std
def f014cfv_f014_cash_flow_volatility_ncfi_252d_std_distmed_504d_base_v138_signal(ncfi, closeadj):
    base = ncfi.rolling(252, min_periods=126).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_distmed_126d_base_v139_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_distmed_252d_base_v140_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncff_252d_std
def f014cfv_f014_cash_flow_volatility_ncff_252d_std_distmed_504d_base_v141_signal(ncff, closeadj):
    base = ncff.rolling(252, min_periods=126).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_distmed_126d_base_v142_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_distmed_252d_base_v143_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_cv_252d
def f014cfv_f014_cash_flow_volatility_ocf_cv_252d_distmed_504d_base_v144_signal(ncfo, closeadj):
    base = _f014_cv(ncfo, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_distmed_126d_base_v145_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_distmed_252d_base_v146_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_cv_252d
def f014cfv_f014_cash_flow_volatility_fcf_cv_252d_distmed_504d_base_v147_signal(fcf, closeadj):
    base = _f014_cv(fcf, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_chg_63d_base_v148_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ocf_252d_std
def f014cfv_f014_cash_flow_volatility_ocf_252d_std_chg_252d_base_v149_signal(ncfo, closeadj):
    base = _f014_ocf_vol(ncfo, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in fcf_252d_std
def f014cfv_f014_cash_flow_volatility_fcf_252d_std_chg_63d_base_v150_signal(fcf, closeadj):
    base = _f014_fcf_vol(fcf, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

