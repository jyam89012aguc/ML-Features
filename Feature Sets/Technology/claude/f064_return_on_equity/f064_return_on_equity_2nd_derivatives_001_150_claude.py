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


# 21d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slope_21d_2d_v001_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slope_63d_2d_v002_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slope_126d_2d_v003_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slope_252d_2d_v004_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_slope_504d_2d_v005_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slope_21d_2d_v006_signal(roe, closeadj):
    base = roe
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slope_63d_2d_v007_signal(roe, closeadj):
    base = roe
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slope_126d_2d_v008_signal(roe, closeadj):
    base = roe
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slope_252d_2d_v009_signal(roe, closeadj):
    base = roe
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_slope_504d_2d_v010_signal(roe, closeadj):
    base = roe
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slope_21d_2d_v011_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slope_63d_2d_v012_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slope_126d_2d_v013_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slope_252d_2d_v014_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_slope_504d_2d_v015_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slope_21d_2d_v016_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slope_63d_2d_v017_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slope_126d_2d_v018_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slope_252d_2d_v019_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_slope_504d_2d_v020_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slope_21d_2d_v021_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slope_63d_2d_v022_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slope_126d_2d_v023_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slope_252d_2d_v024_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_slope_504d_2d_v025_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slope_21d_2d_v026_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slope_63d_2d_v027_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slope_126d_2d_v028_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slope_252d_2d_v029_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_slope_504d_2d_v030_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slope_21d_2d_v031_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slope_63d_2d_v032_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slope_126d_2d_v033_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slope_252d_2d_v034_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_slope_504d_2d_v035_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sm21_sl21_2d_v036_signal(netinc, equity, closeadj):
    base = _mean(_f064_roe(netinc, equity), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sm63_sl21_2d_v037_signal(netinc, equity, closeadj):
    base = _mean(_f064_roe(netinc, equity), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sm63_sl63_2d_v038_signal(netinc, equity, closeadj):
    base = _mean(_f064_roe(netinc, equity), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sm252_sl63_2d_v039_signal(netinc, equity, closeadj):
    base = _mean(_f064_roe(netinc, equity), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sm252_sl126_2d_v040_signal(netinc, equity, closeadj):
    base = _mean(_f064_roe(netinc, equity), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sm21_sl21_2d_v041_signal(roe, closeadj):
    base = _mean(roe, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sm63_sl21_2d_v042_signal(roe, closeadj):
    base = _mean(roe, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sm63_sl63_2d_v043_signal(roe, closeadj):
    base = _mean(roe, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sm252_sl63_2d_v044_signal(roe, closeadj):
    base = _mean(roe, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sm252_sl126_2d_v045_signal(roe, closeadj):
    base = _mean(roe, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sm21_sl21_2d_v046_signal(roe, closeadj):
    base = _mean(roe.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sm63_sl21_2d_v047_signal(roe, closeadj):
    base = _mean(roe.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sm63_sl63_2d_v048_signal(roe, closeadj):
    base = _mean(roe.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sm252_sl63_2d_v049_signal(roe, closeadj):
    base = _mean(roe.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sm252_sl126_2d_v050_signal(roe, closeadj):
    base = _mean(roe.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sm21_sl21_2d_v051_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sm63_sl21_2d_v052_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sm63_sl63_2d_v053_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sm252_sl63_2d_v054_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sm252_sl126_2d_v055_signal(equity, closeadj):
    base = _mean((equity < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sm21_sl21_2d_v056_signal(ebit, equity, closeadj):
    base = _mean(ebit / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sm63_sl21_2d_v057_signal(ebit, equity, closeadj):
    base = _mean(ebit / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sm63_sl63_2d_v058_signal(ebit, equity, closeadj):
    base = _mean(ebit / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sm252_sl63_2d_v059_signal(ebit, equity, closeadj):
    base = _mean(ebit / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sm252_sl126_2d_v060_signal(ebit, equity, closeadj):
    base = _mean(ebit / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sm21_sl21_2d_v061_signal(roe, closeadj):
    base = _mean(roe.rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sm63_sl21_2d_v062_signal(roe, closeadj):
    base = _mean(roe.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sm63_sl63_2d_v063_signal(roe, closeadj):
    base = _mean(roe.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sm252_sl63_2d_v064_signal(roe, closeadj):
    base = _mean(roe.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sm252_sl126_2d_v065_signal(roe, closeadj):
    base = _mean(roe.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sm21_sl21_2d_v066_signal(ncfo, equity, closeadj):
    base = _mean(ncfo / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sm63_sl21_2d_v067_signal(ncfo, equity, closeadj):
    base = _mean(ncfo / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sm63_sl63_2d_v068_signal(ncfo, equity, closeadj):
    base = _mean(ncfo / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sm252_sl63_2d_v069_signal(ncfo, equity, closeadj):
    base = _mean(ncfo / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sm252_sl126_2d_v070_signal(ncfo, equity, closeadj):
    base = _mean(ncfo / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_pctslope_21d_2d_v071_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_pctslope_63d_2d_v072_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_pctslope_252d_2d_v073_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_pctslope_21d_2d_v074_signal(roe, closeadj):
    base = roe
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_pctslope_63d_2d_v075_signal(roe, closeadj):
    base = roe
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_pctslope_252d_2d_v076_signal(roe, closeadj):
    base = roe
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_pctslope_21d_2d_v077_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_pctslope_63d_2d_v078_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_pctslope_252d_2d_v079_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_pctslope_21d_2d_v080_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_pctslope_63d_2d_v081_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_pctslope_252d_2d_v082_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_pctslope_21d_2d_v083_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_pctslope_63d_2d_v084_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_pctslope_252d_2d_v085_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_pctslope_21d_2d_v086_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_pctslope_63d_2d_v087_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_pctslope_252d_2d_v088_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_pctslope_21d_2d_v089_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_pctslope_63d_2d_v090_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_pctslope_252d_2d_v091_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sgnslope_21d_2d_v092_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sgnslope_63d_2d_v093_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_sgnslope_252d_2d_v094_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sgnslope_21d_2d_v095_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sgnslope_63d_2d_v096_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_sgnslope_252d_2d_v097_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sgnslope_21d_2d_v098_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sgnslope_63d_2d_v099_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_sgnslope_252d_2d_v100_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sgnslope_21d_2d_v101_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sgnslope_63d_2d_v102_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_sgnslope_252d_2d_v103_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sgnslope_21d_2d_v104_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sgnslope_63d_2d_v105_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_sgnslope_252d_2d_v106_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sgnslope_21d_2d_v107_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sgnslope_63d_2d_v108_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_sgnslope_252d_2d_v109_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sgnslope_21d_2d_v110_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sgnslope_63d_2d_v111_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_sgnslope_252d_2d_v112_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_logmagslope_21d_2d_v113_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_logmagslope_63d_2d_v114_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roe_calc
def f064roe_f064_return_on_equity_roe_calc_logmagslope_252d_2d_v115_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_logmagslope_21d_2d_v116_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_logmagslope_63d_2d_v117_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_logmagslope_252d_2d_v118_signal(roe, closeadj):
    base = roe
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_logmagslope_21d_2d_v119_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_logmagslope_63d_2d_v120_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_logmagslope_252d_2d_v121_signal(roe, closeadj):
    base = roe.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_logmagslope_21d_2d_v122_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_logmagslope_63d_2d_v123_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_logmagslope_252d_2d_v124_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_logmagslope_21d_2d_v125_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_logmagslope_63d_2d_v126_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_logmagslope_252d_2d_v127_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_logmagslope_21d_2d_v128_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_logmagslope_63d_2d_v129_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_logmagslope_252d_2d_v130_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_logmagslope_21d_2d_v131_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_logmagslope_63d_2d_v132_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_logmagslope_252d_2d_v133_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roe_calc|
def f064roe_f064_return_on_equity_roe_calc_logslope_63d_2d_v134_signal(netinc, equity, closeadj):
    base = np.log((_f064_roe(netinc, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roe_calc|
def f064roe_f064_return_on_equity_roe_calc_logslope_252d_2d_v135_signal(netinc, equity, closeadj):
    base = np.log((_f064_roe(netinc, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roe_lvl|
def f064roe_f064_return_on_equity_roe_lvl_logslope_63d_2d_v136_signal(roe, closeadj):
    base = np.log((roe).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roe_lvl|
def f064roe_f064_return_on_equity_roe_lvl_logslope_252d_2d_v137_signal(roe, closeadj):
    base = np.log((roe).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roe_yoy_chg|
def f064roe_f064_return_on_equity_roe_yoy_chg_logslope_63d_2d_v138_signal(roe, closeadj):
    base = np.log((roe.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roe_yoy_chg|
def f064roe_f064_return_on_equity_roe_yoy_chg_logslope_252d_2d_v139_signal(roe, closeadj):
    base = np.log((roe.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|neg_eq_roe_flag|
def f064roe_f064_return_on_equity_neg_eq_roe_flag_logslope_63d_2d_v140_signal(equity, closeadj):
    base = np.log(((equity < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|neg_eq_roe_flag|
def f064roe_f064_return_on_equity_neg_eq_roe_flag_logslope_252d_2d_v141_signal(equity, closeadj):
    base = np.log(((equity < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ebit_roe|
def f064roe_f064_return_on_equity_ebit_roe_logslope_63d_2d_v142_signal(ebit, equity, closeadj):
    base = np.log((ebit / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ebit_roe|
def f064roe_f064_return_on_equity_ebit_roe_logslope_252d_2d_v143_signal(ebit, equity, closeadj):
    base = np.log((ebit / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|roe_vol_252|
def f064roe_f064_return_on_equity_roe_vol_252_logslope_63d_2d_v144_signal(roe, closeadj):
    base = np.log((roe.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|roe_vol_252|
def f064roe_f064_return_on_equity_roe_vol_252_logslope_252d_2d_v145_signal(roe, closeadj):
    base = np.log((roe.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_to_equity|
def f064roe_f064_return_on_equity_ocf_to_equity_logslope_63d_2d_v146_signal(ncfo, equity, closeadj):
    base = np.log((ncfo / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_to_equity|
def f064roe_f064_return_on_equity_ocf_to_equity_logslope_252d_2d_v147_signal(ncfo, equity, closeadj):
    base = np.log((ncfo / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

