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
def _f063_roa(netinc, assetsavg):
    return netinc / assetsavg.replace(0, np.nan).abs()


# 21d mean of roa_calc scaled by closeadj
def f063roa_f063_return_on_assets_roa_calc_mean_21d_base_v001_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roa_calc scaled by closeadj
def f063roa_f063_return_on_assets_roa_calc_mean_63d_base_v002_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roa_calc scaled by closeadj
def f063roa_f063_return_on_assets_roa_calc_mean_126d_base_v003_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roa_calc scaled by closeadj
def f063roa_f063_return_on_assets_roa_calc_mean_252d_base_v004_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roa_calc scaled by closeadj
def f063roa_f063_return_on_assets_roa_calc_mean_504d_base_v005_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roa_lvl scaled by closeadj
def f063roa_f063_return_on_assets_roa_lvl_mean_21d_base_v006_signal(roa, closeadj):
    base = roa
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roa_lvl scaled by closeadj
def f063roa_f063_return_on_assets_roa_lvl_mean_63d_base_v007_signal(roa, closeadj):
    base = roa
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roa_lvl scaled by closeadj
def f063roa_f063_return_on_assets_roa_lvl_mean_126d_base_v008_signal(roa, closeadj):
    base = roa
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roa_lvl scaled by closeadj
def f063roa_f063_return_on_assets_roa_lvl_mean_252d_base_v009_signal(roa, closeadj):
    base = roa
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roa_lvl scaled by closeadj
def f063roa_f063_return_on_assets_roa_lvl_mean_504d_base_v010_signal(roa, closeadj):
    base = roa
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roa_yoy_chg scaled by closeadj
def f063roa_f063_return_on_assets_roa_yoy_chg_mean_21d_base_v011_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roa_yoy_chg scaled by closeadj
def f063roa_f063_return_on_assets_roa_yoy_chg_mean_63d_base_v012_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roa_yoy_chg scaled by closeadj
def f063roa_f063_return_on_assets_roa_yoy_chg_mean_126d_base_v013_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roa_yoy_chg scaled by closeadj
def f063roa_f063_return_on_assets_roa_yoy_chg_mean_252d_base_v014_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roa_yoy_chg scaled by closeadj
def f063roa_f063_return_on_assets_roa_yoy_chg_mean_504d_base_v015_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebit_roa scaled by closeadj
def f063roa_f063_return_on_assets_ebit_roa_mean_21d_base_v016_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebit_roa scaled by closeadj
def f063roa_f063_return_on_assets_ebit_roa_mean_63d_base_v017_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebit_roa scaled by closeadj
def f063roa_f063_return_on_assets_ebit_roa_mean_126d_base_v018_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebit_roa scaled by closeadj
def f063roa_f063_return_on_assets_ebit_roa_mean_252d_base_v019_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebit_roa scaled by closeadj
def f063roa_f063_return_on_assets_ebit_roa_mean_504d_base_v020_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_roa scaled by closeadj
def f063roa_f063_return_on_assets_ocf_roa_mean_21d_base_v021_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_roa scaled by closeadj
def f063roa_f063_return_on_assets_ocf_roa_mean_63d_base_v022_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_roa scaled by closeadj
def f063roa_f063_return_on_assets_ocf_roa_mean_126d_base_v023_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_roa scaled by closeadj
def f063roa_f063_return_on_assets_ocf_roa_mean_252d_base_v024_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_roa scaled by closeadj
def f063roa_f063_return_on_assets_ocf_roa_mean_504d_base_v025_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_roa scaled by closeadj
def f063roa_f063_return_on_assets_fcf_roa_mean_21d_base_v026_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_roa scaled by closeadj
def f063roa_f063_return_on_assets_fcf_roa_mean_63d_base_v027_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_roa scaled by closeadj
def f063roa_f063_return_on_assets_fcf_roa_mean_126d_base_v028_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_roa scaled by closeadj
def f063roa_f063_return_on_assets_fcf_roa_mean_252d_base_v029_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_roa scaled by closeadj
def f063roa_f063_return_on_assets_fcf_roa_mean_504d_base_v030_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roa_vol_252 scaled by closeadj
def f063roa_f063_return_on_assets_roa_vol_252_mean_21d_base_v031_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roa_vol_252 scaled by closeadj
def f063roa_f063_return_on_assets_roa_vol_252_mean_63d_base_v032_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roa_vol_252 scaled by closeadj
def f063roa_f063_return_on_assets_roa_vol_252_mean_126d_base_v033_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roa_vol_252 scaled by closeadj
def f063roa_f063_return_on_assets_roa_vol_252_mean_252d_base_v034_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roa_vol_252 scaled by closeadj
def f063roa_f063_return_on_assets_roa_vol_252_mean_504d_base_v035_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_median_63d_base_v036_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_median_252d_base_v037_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_median_504d_base_v038_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_median_63d_base_v039_signal(roa, closeadj):
    base = roa
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_median_252d_base_v040_signal(roa, closeadj):
    base = roa
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_median_504d_base_v041_signal(roa, closeadj):
    base = roa
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_median_63d_base_v042_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_median_252d_base_v043_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_median_504d_base_v044_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_median_63d_base_v045_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_median_252d_base_v046_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_median_504d_base_v047_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_median_63d_base_v048_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_median_252d_base_v049_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_median_504d_base_v050_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_median_63d_base_v051_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_median_252d_base_v052_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_median_504d_base_v053_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_median_63d_base_v054_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_median_252d_base_v055_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_median_504d_base_v056_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roa_calc
def f063roa_f063_return_on_assets_roa_calc_rmax_252d_base_v057_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roa_calc
def f063roa_f063_return_on_assets_roa_calc_rmax_504d_base_v058_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_rmax_252d_base_v059_signal(roa, closeadj):
    base = roa
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_rmax_504d_base_v060_signal(roa, closeadj):
    base = roa
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_rmax_252d_base_v061_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_rmax_504d_base_v062_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_rmax_252d_base_v063_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_rmax_504d_base_v064_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_rmax_252d_base_v065_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_rmax_504d_base_v066_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_rmax_252d_base_v067_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_rmax_504d_base_v068_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_rmax_252d_base_v069_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_rmax_504d_base_v070_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roa_calc
def f063roa_f063_return_on_assets_roa_calc_rmin_252d_base_v071_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of roa_calc
def f063roa_f063_return_on_assets_roa_calc_rmin_504d_base_v072_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_rmin_252d_base_v073_signal(roa, closeadj):
    base = roa
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_rmin_504d_base_v074_signal(roa, closeadj):
    base = roa
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_rmin_252d_base_v075_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

