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
def _f063_roa(netinc, assetsavg):
    return netinc / assetsavg.replace(0, np.nan).abs()


# 21d acceleration of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accel_21d_3d_v001_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accel_63d_3d_v002_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accel_126d_3d_v003_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accel_252d_3d_v004_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accel_21d_3d_v005_signal(roa, closeadj):
    base = roa
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accel_63d_3d_v006_signal(roa, closeadj):
    base = roa
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accel_126d_3d_v007_signal(roa, closeadj):
    base = roa
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accel_252d_3d_v008_signal(roa, closeadj):
    base = roa
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accel_21d_3d_v009_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accel_63d_3d_v010_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accel_126d_3d_v011_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accel_252d_3d_v012_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accel_21d_3d_v013_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accel_63d_3d_v014_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accel_126d_3d_v015_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accel_252d_3d_v016_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accel_21d_3d_v017_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accel_63d_3d_v018_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accel_126d_3d_v019_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accel_252d_3d_v020_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accel_21d_3d_v021_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accel_63d_3d_v022_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accel_126d_3d_v023_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accel_252d_3d_v024_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accel_21d_3d_v025_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accel_63d_3d_v026_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accel_126d_3d_v027_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accel_252d_3d_v028_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slopez_21d_z126_3d_v029_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slopez_63d_z252_3d_v030_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slopez_126d_z252_3d_v031_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slopez_252d_z504_3d_v032_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slopez_21d_z126_3d_v033_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slopez_63d_z252_3d_v034_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slopez_126d_z252_3d_v035_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slopez_252d_z504_3d_v036_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slopez_21d_z126_3d_v037_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slopez_63d_z252_3d_v038_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slopez_126d_z252_3d_v039_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slopez_252d_z504_3d_v040_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slopez_21d_z126_3d_v041_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slopez_63d_z252_3d_v042_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slopez_126d_z252_3d_v043_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slopez_252d_z504_3d_v044_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slopez_21d_z126_3d_v045_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slopez_63d_z252_3d_v046_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slopez_126d_z252_3d_v047_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slopez_252d_z504_3d_v048_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slopez_21d_z126_3d_v049_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slopez_63d_z252_3d_v050_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slopez_126d_z252_3d_v051_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slopez_252d_z504_3d_v052_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slopez_21d_z126_3d_v053_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slopez_63d_z252_3d_v054_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slopez_126d_z252_3d_v055_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slopez_252d_z504_3d_v056_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roa_calc
def f063roa_f063_return_on_assets_roa_calc_jerk_21d_3d_v057_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roa_calc
def f063roa_f063_return_on_assets_roa_calc_jerk_63d_3d_v058_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roa_calc
def f063roa_f063_return_on_assets_roa_calc_jerk_126d_3d_v059_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_jerk_21d_3d_v060_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_jerk_63d_3d_v061_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_jerk_126d_3d_v062_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_jerk_21d_3d_v063_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_jerk_63d_3d_v064_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_jerk_126d_3d_v065_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_jerk_21d_3d_v066_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_jerk_63d_3d_v067_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_jerk_126d_3d_v068_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_jerk_21d_3d_v069_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_jerk_63d_3d_v070_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_jerk_126d_3d_v071_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_jerk_21d_3d_v072_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_jerk_63d_3d_v073_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_jerk_126d_3d_v074_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_jerk_21d_3d_v075_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_jerk_63d_3d_v076_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_jerk_126d_3d_v077_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roa_calc smoothed over 252d
def f063roa_f063_return_on_assets_roa_calc_smoothaccel_63d_sm252_3d_v078_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roa_calc smoothed over 504d
def f063roa_f063_return_on_assets_roa_calc_smoothaccel_252d_sm504_3d_v079_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roa_lvl smoothed over 252d
def f063roa_f063_return_on_assets_roa_lvl_smoothaccel_63d_sm252_3d_v080_signal(roa, closeadj):
    base = roa
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roa_lvl smoothed over 504d
def f063roa_f063_return_on_assets_roa_lvl_smoothaccel_252d_sm504_3d_v081_signal(roa, closeadj):
    base = roa
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roa_yoy_chg smoothed over 252d
def f063roa_f063_return_on_assets_roa_yoy_chg_smoothaccel_63d_sm252_3d_v082_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roa_yoy_chg smoothed over 504d
def f063roa_f063_return_on_assets_roa_yoy_chg_smoothaccel_252d_sm504_3d_v083_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebit_roa smoothed over 252d
def f063roa_f063_return_on_assets_ebit_roa_smoothaccel_63d_sm252_3d_v084_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebit_roa smoothed over 504d
def f063roa_f063_return_on_assets_ebit_roa_smoothaccel_252d_sm504_3d_v085_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_roa smoothed over 252d
def f063roa_f063_return_on_assets_ocf_roa_smoothaccel_63d_sm252_3d_v086_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_roa smoothed over 504d
def f063roa_f063_return_on_assets_ocf_roa_smoothaccel_252d_sm504_3d_v087_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_roa smoothed over 252d
def f063roa_f063_return_on_assets_fcf_roa_smoothaccel_63d_sm252_3d_v088_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_roa smoothed over 504d
def f063roa_f063_return_on_assets_fcf_roa_smoothaccel_252d_sm504_3d_v089_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of roa_vol_252 smoothed over 252d
def f063roa_f063_return_on_assets_roa_vol_252_smoothaccel_63d_sm252_3d_v090_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of roa_vol_252 smoothed over 504d
def f063roa_f063_return_on_assets_roa_vol_252_smoothaccel_252d_sm504_3d_v091_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accelz_21d_z252_3d_v092_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roa_calc
def f063roa_f063_return_on_assets_roa_calc_accelz_63d_z504_3d_v093_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accelz_21d_z252_3d_v094_signal(roa, closeadj):
    base = roa
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_accelz_63d_z504_3d_v095_signal(roa, closeadj):
    base = roa
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accelz_21d_z252_3d_v096_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_accelz_63d_z504_3d_v097_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accelz_21d_z252_3d_v098_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_accelz_63d_z504_3d_v099_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accelz_21d_z252_3d_v100_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_accelz_63d_z504_3d_v101_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accelz_21d_z252_3d_v102_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_accelz_63d_z504_3d_v103_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accelz_21d_z252_3d_v104_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_accelz_63d_z504_3d_v105_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roa_calc (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_calc_signflip_63d_3d_v106_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roa_calc (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_calc_signflip_252d_3d_v107_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roa_lvl (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_lvl_signflip_63d_3d_v108_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roa_lvl (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_lvl_signflip_252d_3d_v109_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roa_yoy_chg (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_yoy_chg_signflip_63d_3d_v110_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roa_yoy_chg (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_yoy_chg_signflip_252d_3d_v111_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebit_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_ebit_roa_signflip_63d_3d_v112_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebit_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_ebit_roa_signflip_252d_3d_v113_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_ocf_roa_signflip_63d_3d_v114_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_ocf_roa_signflip_252d_3d_v115_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_fcf_roa_signflip_63d_3d_v116_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_roa (raw count, no price scaling)
def f063roa_f063_return_on_assets_fcf_roa_signflip_252d_3d_v117_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in roa_vol_252 (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_vol_252_signflip_63d_3d_v118_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in roa_vol_252 (raw count, no price scaling)
def f063roa_f063_return_on_assets_roa_vol_252_signflip_252d_3d_v119_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_calc normalized by 252d range
def f063roa_f063_return_on_assets_roa_calc_rngaccel_63d_r252_3d_v120_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_calc normalized by 504d range
def f063roa_f063_return_on_assets_roa_calc_rngaccel_252d_r504_3d_v121_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_lvl normalized by 252d range
def f063roa_f063_return_on_assets_roa_lvl_rngaccel_63d_r252_3d_v122_signal(roa, closeadj):
    base = roa
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_lvl normalized by 504d range
def f063roa_f063_return_on_assets_roa_lvl_rngaccel_252d_r504_3d_v123_signal(roa, closeadj):
    base = roa
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_yoy_chg normalized by 252d range
def f063roa_f063_return_on_assets_roa_yoy_chg_rngaccel_63d_r252_3d_v124_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_yoy_chg normalized by 504d range
def f063roa_f063_return_on_assets_roa_yoy_chg_rngaccel_252d_r504_3d_v125_signal(roa, closeadj):
    base = roa.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebit_roa normalized by 252d range
def f063roa_f063_return_on_assets_ebit_roa_rngaccel_63d_r252_3d_v126_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebit_roa normalized by 504d range
def f063roa_f063_return_on_assets_ebit_roa_rngaccel_252d_r504_3d_v127_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_roa normalized by 252d range
def f063roa_f063_return_on_assets_ocf_roa_rngaccel_63d_r252_3d_v128_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_roa normalized by 504d range
def f063roa_f063_return_on_assets_ocf_roa_rngaccel_252d_r504_3d_v129_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_roa normalized by 252d range
def f063roa_f063_return_on_assets_fcf_roa_rngaccel_63d_r252_3d_v130_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_roa normalized by 504d range
def f063roa_f063_return_on_assets_fcf_roa_rngaccel_252d_r504_3d_v131_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roa_vol_252 normalized by 252d range
def f063roa_f063_return_on_assets_roa_vol_252_rngaccel_63d_r252_3d_v132_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roa_vol_252 normalized by 504d range
def f063roa_f063_return_on_assets_roa_vol_252_rngaccel_252d_r504_3d_v133_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_cumslope_21d_3d_v134_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_cumslope_63d_3d_v135_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_cumslope_252d_3d_v136_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_cumslope_21d_3d_v137_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_cumslope_63d_3d_v138_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_cumslope_252d_3d_v139_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_cumslope_21d_3d_v140_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_cumslope_63d_3d_v141_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_cumslope_252d_3d_v142_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_cumslope_21d_3d_v143_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_cumslope_63d_3d_v144_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_cumslope_252d_3d_v145_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_cumslope_21d_3d_v146_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_cumslope_63d_3d_v147_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_cumslope_252d_3d_v148_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_cumslope_21d_3d_v149_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_cumslope_63d_3d_v150_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

