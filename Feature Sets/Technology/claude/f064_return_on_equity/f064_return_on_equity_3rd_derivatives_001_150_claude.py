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
def _f064_roe(netinc, equity):
    return netinc / equity.replace(0, np.nan).abs()


# 21d acceleration of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accel_21d_3d_v001_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accel_63d_3d_v002_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accel_126d_3d_v003_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accel_252d_3d_v004_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accel_21d_3d_v005_signal(roe, closeadj):
    base = roe
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accel_63d_3d_v006_signal(roe, closeadj):
    base = roe
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accel_126d_3d_v007_signal(roe, closeadj):
    base = roe
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accel_252d_3d_v008_signal(roe, closeadj):
    base = roe
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accel_21d_3d_v009_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accel_63d_3d_v010_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accel_126d_3d_v011_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accel_252d_3d_v012_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accel_21d_3d_v013_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accel_63d_3d_v014_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accel_126d_3d_v015_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accel_252d_3d_v016_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accel_21d_3d_v017_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accel_63d_3d_v018_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accel_126d_3d_v019_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accel_252d_3d_v020_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accel_21d_3d_v021_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accel_63d_3d_v022_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accel_126d_3d_v023_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accel_252d_3d_v024_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accel_21d_3d_v025_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accel_63d_3d_v026_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accel_126d_3d_v027_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accel_252d_3d_v028_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slopez_21d_z126_3d_v029_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slopez_63d_z252_3d_v030_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slopez_126d_z252_3d_v031_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slopez_252d_z504_3d_v032_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slopez_21d_z126_3d_v033_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slopez_63d_z252_3d_v034_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slopez_126d_z252_3d_v035_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slopez_252d_z504_3d_v036_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slopez_21d_z126_3d_v037_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slopez_63d_z252_3d_v038_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slopez_126d_z252_3d_v039_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slopez_252d_z504_3d_v040_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slopez_21d_z126_3d_v041_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slopez_63d_z252_3d_v042_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slopez_126d_z252_3d_v043_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slopez_252d_z504_3d_v044_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slopez_21d_z126_3d_v045_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slopez_63d_z252_3d_v046_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slopez_126d_z252_3d_v047_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slopez_252d_z504_3d_v048_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slopez_21d_z126_3d_v049_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slopez_63d_z252_3d_v050_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slopez_126d_z252_3d_v051_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slopez_252d_z504_3d_v052_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slopez_21d_z126_3d_v053_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slopez_63d_z252_3d_v054_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slopez_126d_z252_3d_v055_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slopez_252d_z504_3d_v056_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roe_calc
def f064roe_f064_return_on_equity_roe_calc_jerk_21d_3d_v057_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roe_calc
def f064roe_f064_return_on_equity_roe_calc_jerk_63d_3d_v058_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roe_calc
def f064roe_f064_return_on_equity_roe_calc_jerk_126d_3d_v059_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_jerk_21d_3d_v060_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_jerk_63d_3d_v061_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_jerk_126d_3d_v062_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_jerk_21d_3d_v063_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_jerk_63d_3d_v064_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_jerk_126d_3d_v065_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_jerk_21d_3d_v066_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_jerk_63d_3d_v067_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_jerk_126d_3d_v068_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_jerk_21d_3d_v069_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_jerk_63d_3d_v070_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_jerk_126d_3d_v071_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_jerk_21d_3d_v072_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_jerk_63d_3d_v073_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_jerk_126d_3d_v074_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_jerk_21d_3d_v075_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_jerk_63d_3d_v076_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_jerk_126d_3d_v077_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roe_calc smoothed over 252d
def f064roe_f064_return_on_equity_roe_calc_smoothaccel_63d_sm252_3d_v078_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roe_calc smoothed over 504d
def f064roe_f064_return_on_equity_roe_calc_smoothaccel_252d_sm504_3d_v079_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roe_lvl smoothed over 252d
def f064roe_f064_return_on_equity_roe_lvl_smoothaccel_63d_sm252_3d_v080_signal(roe, closeadj):
    base = roe
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roe_lvl smoothed over 504d
def f064roe_f064_return_on_equity_roe_lvl_smoothaccel_252d_sm504_3d_v081_signal(roe, closeadj):
    base = roe
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roe_yoy_chg smoothed over 252d
def f064roe_f064_return_on_equity_roe_yoy_chg_smoothaccel_63d_sm252_3d_v082_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roe_yoy_chg smoothed over 504d
def f064roe_f064_return_on_equity_roe_yoy_chg_smoothaccel_252d_sm504_3d_v083_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of neg_eq_roe_flag smoothed over 252d
def f064roe_f064_return_on_equity_neg_eq_roe_flag_smoothaccel_63d_sm252_3d_v084_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of neg_eq_roe_flag smoothed over 504d
def f064roe_f064_return_on_equity_neg_eq_roe_flag_smoothaccel_252d_sm504_3d_v085_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebit_roe smoothed over 252d
def f064roe_f064_return_on_equity_ebit_roe_smoothaccel_63d_sm252_3d_v086_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebit_roe smoothed over 504d
def f064roe_f064_return_on_equity_ebit_roe_smoothaccel_252d_sm504_3d_v087_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roe_vol_252 smoothed over 252d
def f064roe_f064_return_on_equity_roe_vol_252_smoothaccel_63d_sm252_3d_v088_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roe_vol_252 smoothed over 504d
def f064roe_f064_return_on_equity_roe_vol_252_smoothaccel_252d_sm504_3d_v089_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_equity smoothed over 252d
def f064roe_f064_return_on_equity_ocf_to_equity_smoothaccel_63d_sm252_3d_v090_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_equity smoothed over 504d
def f064roe_f064_return_on_equity_ocf_to_equity_smoothaccel_252d_sm504_3d_v091_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accelz_21d_z252_3d_v092_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roe_calc
def f064roe_f064_return_on_equity_roe_calc_accelz_63d_z504_3d_v093_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accelz_21d_z252_3d_v094_signal(roe, closeadj):
    base = roe
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_accelz_63d_z504_3d_v095_signal(roe, closeadj):
    base = roe
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accelz_21d_z252_3d_v096_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_accelz_63d_z504_3d_v097_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accelz_21d_z252_3d_v098_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_accelz_63d_z504_3d_v099_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accelz_21d_z252_3d_v100_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_accelz_63d_z504_3d_v101_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accelz_21d_z252_3d_v102_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_accelz_63d_z504_3d_v103_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accelz_21d_z252_3d_v104_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_accelz_63d_z504_3d_v105_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roe_calc (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_calc_signflip_63d_3d_v106_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roe_calc (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_calc_signflip_252d_3d_v107_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roe_lvl (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_lvl_signflip_63d_3d_v108_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roe_lvl (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_lvl_signflip_252d_3d_v109_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roe_yoy_chg (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_yoy_chg_signflip_63d_3d_v110_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roe_yoy_chg (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_yoy_chg_signflip_252d_3d_v111_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in neg_eq_roe_flag (raw count, no price scaling)
def f064roe_f064_return_on_equity_neg_eq_roe_flag_signflip_63d_3d_v112_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in neg_eq_roe_flag (raw count, no price scaling)
def f064roe_f064_return_on_equity_neg_eq_roe_flag_signflip_252d_3d_v113_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebit_roe (raw count, no price scaling)
def f064roe_f064_return_on_equity_ebit_roe_signflip_63d_3d_v114_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebit_roe (raw count, no price scaling)
def f064roe_f064_return_on_equity_ebit_roe_signflip_252d_3d_v115_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roe_vol_252 (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_vol_252_signflip_63d_3d_v116_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roe_vol_252 (raw count, no price scaling)
def f064roe_f064_return_on_equity_roe_vol_252_signflip_252d_3d_v117_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_equity (raw count, no price scaling)
def f064roe_f064_return_on_equity_ocf_to_equity_signflip_63d_3d_v118_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_equity (raw count, no price scaling)
def f064roe_f064_return_on_equity_ocf_to_equity_signflip_252d_3d_v119_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_calc normalized by 252d range
def f064roe_f064_return_on_equity_roe_calc_rngaccel_63d_r252_3d_v120_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_calc normalized by 504d range
def f064roe_f064_return_on_equity_roe_calc_rngaccel_252d_r504_3d_v121_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_lvl normalized by 252d range
def f064roe_f064_return_on_equity_roe_lvl_rngaccel_63d_r252_3d_v122_signal(roe, closeadj):
    base = roe
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_lvl normalized by 504d range
def f064roe_f064_return_on_equity_roe_lvl_rngaccel_252d_r504_3d_v123_signal(roe, closeadj):
    base = roe
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_yoy_chg normalized by 252d range
def f064roe_f064_return_on_equity_roe_yoy_chg_rngaccel_63d_r252_3d_v124_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_yoy_chg normalized by 504d range
def f064roe_f064_return_on_equity_roe_yoy_chg_rngaccel_252d_r504_3d_v125_signal(roe, closeadj):
    base = roe.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of neg_eq_roe_flag normalized by 252d range
def f064roe_f064_return_on_equity_neg_eq_roe_flag_rngaccel_63d_r252_3d_v126_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of neg_eq_roe_flag normalized by 504d range
def f064roe_f064_return_on_equity_neg_eq_roe_flag_rngaccel_252d_r504_3d_v127_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_roe normalized by 252d range
def f064roe_f064_return_on_equity_ebit_roe_rngaccel_63d_r252_3d_v128_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_roe normalized by 504d range
def f064roe_f064_return_on_equity_ebit_roe_rngaccel_252d_r504_3d_v129_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roe_vol_252 normalized by 252d range
def f064roe_f064_return_on_equity_roe_vol_252_rngaccel_63d_r252_3d_v130_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roe_vol_252 normalized by 504d range
def f064roe_f064_return_on_equity_roe_vol_252_rngaccel_252d_r504_3d_v131_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_equity normalized by 252d range
def f064roe_f064_return_on_equity_ocf_to_equity_rngaccel_63d_r252_3d_v132_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_equity normalized by 504d range
def f064roe_f064_return_on_equity_ocf_to_equity_rngaccel_252d_r504_3d_v133_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_cumslope_21d_3d_v134_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_cumslope_63d_3d_v135_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_cumslope_252d_3d_v136_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_cumslope_21d_3d_v137_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_cumslope_63d_3d_v138_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_cumslope_252d_3d_v139_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_cumslope_21d_3d_v140_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_cumslope_63d_3d_v141_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_cumslope_252d_3d_v142_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_cumslope_21d_3d_v143_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_cumslope_63d_3d_v144_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_cumslope_252d_3d_v145_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_cumslope_21d_3d_v146_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_cumslope_63d_3d_v147_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_cumslope_252d_3d_v148_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_cumslope_21d_3d_v149_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_cumslope_63d_3d_v150_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

