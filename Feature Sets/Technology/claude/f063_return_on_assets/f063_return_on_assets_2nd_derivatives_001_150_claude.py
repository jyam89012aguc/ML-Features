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


# 21d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slope_21d_2d_v001_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slope_63d_2d_v002_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slope_126d_2d_v003_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slope_252d_2d_v004_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_slope_504d_2d_v005_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slope_21d_2d_v006_signal(roa, closeadj):
    base = roa
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slope_63d_2d_v007_signal(roa, closeadj):
    base = roa
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slope_126d_2d_v008_signal(roa, closeadj):
    base = roa
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slope_252d_2d_v009_signal(roa, closeadj):
    base = roa
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_slope_504d_2d_v010_signal(roa, closeadj):
    base = roa
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slope_21d_2d_v011_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slope_63d_2d_v012_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slope_126d_2d_v013_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slope_252d_2d_v014_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_slope_504d_2d_v015_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slope_21d_2d_v016_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slope_63d_2d_v017_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slope_126d_2d_v018_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slope_252d_2d_v019_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_slope_504d_2d_v020_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slope_21d_2d_v021_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slope_63d_2d_v022_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slope_126d_2d_v023_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slope_252d_2d_v024_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_slope_504d_2d_v025_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slope_21d_2d_v026_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slope_63d_2d_v027_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slope_126d_2d_v028_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slope_252d_2d_v029_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_slope_504d_2d_v030_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slope_21d_2d_v031_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slope_63d_2d_v032_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slope_126d_2d_v033_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slope_252d_2d_v034_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_slope_504d_2d_v035_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sm21_sl21_2d_v036_signal(netinc, assetsavg, closeadj):
    base = _mean(_f063_roa(netinc, assetsavg), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sm63_sl21_2d_v037_signal(netinc, assetsavg, closeadj):
    base = _mean(_f063_roa(netinc, assetsavg), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sm63_sl63_2d_v038_signal(netinc, assetsavg, closeadj):
    base = _mean(_f063_roa(netinc, assetsavg), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sm252_sl63_2d_v039_signal(netinc, assetsavg, closeadj):
    base = _mean(_f063_roa(netinc, assetsavg), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sm252_sl126_2d_v040_signal(netinc, assetsavg, closeadj):
    base = _mean(_f063_roa(netinc, assetsavg), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sm21_sl21_2d_v041_signal(roa, closeadj):
    base = _mean(roa, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sm63_sl21_2d_v042_signal(roa, closeadj):
    base = _mean(roa, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sm63_sl63_2d_v043_signal(roa, closeadj):
    base = _mean(roa, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sm252_sl63_2d_v044_signal(roa, closeadj):
    base = _mean(roa, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sm252_sl126_2d_v045_signal(roa, closeadj):
    base = _mean(roa, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sm21_sl21_2d_v046_signal(roa, closeadj):
    base = _mean(roa.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sm63_sl21_2d_v047_signal(roa, closeadj):
    base = _mean(roa.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sm63_sl63_2d_v048_signal(roa, closeadj):
    base = _mean(roa.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sm252_sl63_2d_v049_signal(roa, closeadj):
    base = _mean(roa.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sm252_sl126_2d_v050_signal(roa, closeadj):
    base = _mean(roa.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sm21_sl21_2d_v051_signal(ebit, assetsavg, closeadj):
    base = _mean(ebit / assetsavg.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sm63_sl21_2d_v052_signal(ebit, assetsavg, closeadj):
    base = _mean(ebit / assetsavg.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sm63_sl63_2d_v053_signal(ebit, assetsavg, closeadj):
    base = _mean(ebit / assetsavg.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sm252_sl63_2d_v054_signal(ebit, assetsavg, closeadj):
    base = _mean(ebit / assetsavg.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sm252_sl126_2d_v055_signal(ebit, assetsavg, closeadj):
    base = _mean(ebit / assetsavg.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sm21_sl21_2d_v056_signal(ncfo, assets, closeadj):
    base = _mean(ncfo / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sm63_sl21_2d_v057_signal(ncfo, assets, closeadj):
    base = _mean(ncfo / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sm63_sl63_2d_v058_signal(ncfo, assets, closeadj):
    base = _mean(ncfo / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sm252_sl63_2d_v059_signal(ncfo, assets, closeadj):
    base = _mean(ncfo / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sm252_sl126_2d_v060_signal(ncfo, assets, closeadj):
    base = _mean(ncfo / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sm21_sl21_2d_v061_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sm63_sl21_2d_v062_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sm63_sl63_2d_v063_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sm252_sl63_2d_v064_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sm252_sl126_2d_v065_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sm21_sl21_2d_v066_signal(roa, closeadj):
    base = _mean(roa.rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sm63_sl21_2d_v067_signal(roa, closeadj):
    base = _mean(roa.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sm63_sl63_2d_v068_signal(roa, closeadj):
    base = _mean(roa.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sm252_sl63_2d_v069_signal(roa, closeadj):
    base = _mean(roa.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sm252_sl126_2d_v070_signal(roa, closeadj):
    base = _mean(roa.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_pctslope_21d_2d_v071_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_pctslope_63d_2d_v072_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_pctslope_252d_2d_v073_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_pctslope_21d_2d_v074_signal(roa, closeadj):
    base = roa
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_pctslope_63d_2d_v075_signal(roa, closeadj):
    base = roa
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_pctslope_252d_2d_v076_signal(roa, closeadj):
    base = roa
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_pctslope_21d_2d_v077_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_pctslope_63d_2d_v078_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_pctslope_252d_2d_v079_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_pctslope_21d_2d_v080_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_pctslope_63d_2d_v081_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_pctslope_252d_2d_v082_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_pctslope_21d_2d_v083_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_pctslope_63d_2d_v084_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_pctslope_252d_2d_v085_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_pctslope_21d_2d_v086_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_pctslope_63d_2d_v087_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_pctslope_252d_2d_v088_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_pctslope_21d_2d_v089_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_pctslope_63d_2d_v090_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_pctslope_252d_2d_v091_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sgnslope_21d_2d_v092_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sgnslope_63d_2d_v093_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_sgnslope_252d_2d_v094_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sgnslope_21d_2d_v095_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sgnslope_63d_2d_v096_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_sgnslope_252d_2d_v097_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sgnslope_21d_2d_v098_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sgnslope_63d_2d_v099_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_sgnslope_252d_2d_v100_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sgnslope_21d_2d_v101_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sgnslope_63d_2d_v102_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_sgnslope_252d_2d_v103_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sgnslope_21d_2d_v104_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sgnslope_63d_2d_v105_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_sgnslope_252d_2d_v106_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sgnslope_21d_2d_v107_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sgnslope_63d_2d_v108_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_sgnslope_252d_2d_v109_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sgnslope_21d_2d_v110_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sgnslope_63d_2d_v111_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_sgnslope_252d_2d_v112_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_logmagslope_21d_2d_v113_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_logmagslope_63d_2d_v114_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roa_calc
def f063roa_f063_return_on_assets_roa_calc_logmagslope_252d_2d_v115_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_logmagslope_21d_2d_v116_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_logmagslope_63d_2d_v117_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_logmagslope_252d_2d_v118_signal(roa, closeadj):
    base = roa
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_logmagslope_21d_2d_v119_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_logmagslope_63d_2d_v120_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_logmagslope_252d_2d_v121_signal(roa, closeadj):
    base = roa.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_logmagslope_21d_2d_v122_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_logmagslope_63d_2d_v123_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_logmagslope_252d_2d_v124_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_logmagslope_21d_2d_v125_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_logmagslope_63d_2d_v126_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_logmagslope_252d_2d_v127_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_logmagslope_21d_2d_v128_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_logmagslope_63d_2d_v129_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_logmagslope_252d_2d_v130_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_logmagslope_21d_2d_v131_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_logmagslope_63d_2d_v132_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_logmagslope_252d_2d_v133_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roa_calc|
def f063roa_f063_return_on_assets_roa_calc_logslope_63d_2d_v134_signal(netinc, assetsavg, closeadj):
    base = np.log((_f063_roa(netinc, assetsavg)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roa_calc|
def f063roa_f063_return_on_assets_roa_calc_logslope_252d_2d_v135_signal(netinc, assetsavg, closeadj):
    base = np.log((_f063_roa(netinc, assetsavg)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roa_lvl|
def f063roa_f063_return_on_assets_roa_lvl_logslope_63d_2d_v136_signal(roa, closeadj):
    base = np.log((roa).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roa_lvl|
def f063roa_f063_return_on_assets_roa_lvl_logslope_252d_2d_v137_signal(roa, closeadj):
    base = np.log((roa).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roa_yoy_chg|
def f063roa_f063_return_on_assets_roa_yoy_chg_logslope_63d_2d_v138_signal(roa, closeadj):
    base = np.log((roa.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roa_yoy_chg|
def f063roa_f063_return_on_assets_roa_yoy_chg_logslope_252d_2d_v139_signal(roa, closeadj):
    base = np.log((roa.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ebit_roa|
def f063roa_f063_return_on_assets_ebit_roa_logslope_63d_2d_v140_signal(ebit, assetsavg, closeadj):
    base = np.log((ebit / assetsavg.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ebit_roa|
def f063roa_f063_return_on_assets_ebit_roa_logslope_252d_2d_v141_signal(ebit, assetsavg, closeadj):
    base = np.log((ebit / assetsavg.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_roa|
def f063roa_f063_return_on_assets_ocf_roa_logslope_63d_2d_v142_signal(ncfo, assets, closeadj):
    base = np.log((ncfo / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_roa|
def f063roa_f063_return_on_assets_ocf_roa_logslope_252d_2d_v143_signal(ncfo, assets, closeadj):
    base = np.log((ncfo / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|fcf_roa|
def f063roa_f063_return_on_assets_fcf_roa_logslope_63d_2d_v144_signal(fcf, assets, closeadj):
    base = np.log((fcf / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|fcf_roa|
def f063roa_f063_return_on_assets_fcf_roa_logslope_252d_2d_v145_signal(fcf, assets, closeadj):
    base = np.log((fcf / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roa_vol_252|
def f063roa_f063_return_on_assets_roa_vol_252_logslope_63d_2d_v146_signal(roa, closeadj):
    base = np.log((roa.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roa_vol_252|
def f063roa_f063_return_on_assets_roa_vol_252_logslope_252d_2d_v147_signal(roa, closeadj):
    base = np.log((roa.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

