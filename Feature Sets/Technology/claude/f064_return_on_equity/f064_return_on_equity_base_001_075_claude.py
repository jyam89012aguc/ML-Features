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
def _f064_roe(netinc, equity):
    return netinc / equity.replace(0, np.nan).abs()


# 21d mean of roe_calc scaled by closeadj
def f064roe_f064_return_on_equity_roe_calc_mean_21d_base_v001_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roe_calc scaled by closeadj
def f064roe_f064_return_on_equity_roe_calc_mean_63d_base_v002_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roe_calc scaled by closeadj
def f064roe_f064_return_on_equity_roe_calc_mean_126d_base_v003_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roe_calc scaled by closeadj
def f064roe_f064_return_on_equity_roe_calc_mean_252d_base_v004_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roe_calc scaled by closeadj
def f064roe_f064_return_on_equity_roe_calc_mean_504d_base_v005_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roe_lvl scaled by closeadj
def f064roe_f064_return_on_equity_roe_lvl_mean_21d_base_v006_signal(roe, closeadj):
    base = roe
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roe_lvl scaled by closeadj
def f064roe_f064_return_on_equity_roe_lvl_mean_63d_base_v007_signal(roe, closeadj):
    base = roe
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roe_lvl scaled by closeadj
def f064roe_f064_return_on_equity_roe_lvl_mean_126d_base_v008_signal(roe, closeadj):
    base = roe
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roe_lvl scaled by closeadj
def f064roe_f064_return_on_equity_roe_lvl_mean_252d_base_v009_signal(roe, closeadj):
    base = roe
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roe_lvl scaled by closeadj
def f064roe_f064_return_on_equity_roe_lvl_mean_504d_base_v010_signal(roe, closeadj):
    base = roe
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roe_yoy_chg scaled by closeadj
def f064roe_f064_return_on_equity_roe_yoy_chg_mean_21d_base_v011_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roe_yoy_chg scaled by closeadj
def f064roe_f064_return_on_equity_roe_yoy_chg_mean_63d_base_v012_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roe_yoy_chg scaled by closeadj
def f064roe_f064_return_on_equity_roe_yoy_chg_mean_126d_base_v013_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roe_yoy_chg scaled by closeadj
def f064roe_f064_return_on_equity_roe_yoy_chg_mean_252d_base_v014_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roe_yoy_chg scaled by closeadj
def f064roe_f064_return_on_equity_roe_yoy_chg_mean_504d_base_v015_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of neg_eq_roe_flag scaled by closeadj
def f064roe_f064_return_on_equity_neg_eq_roe_flag_mean_21d_base_v016_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of neg_eq_roe_flag scaled by closeadj
def f064roe_f064_return_on_equity_neg_eq_roe_flag_mean_63d_base_v017_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of neg_eq_roe_flag scaled by closeadj
def f064roe_f064_return_on_equity_neg_eq_roe_flag_mean_126d_base_v018_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of neg_eq_roe_flag scaled by closeadj
def f064roe_f064_return_on_equity_neg_eq_roe_flag_mean_252d_base_v019_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of neg_eq_roe_flag scaled by closeadj
def f064roe_f064_return_on_equity_neg_eq_roe_flag_mean_504d_base_v020_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebit_roe scaled by closeadj
def f064roe_f064_return_on_equity_ebit_roe_mean_21d_base_v021_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebit_roe scaled by closeadj
def f064roe_f064_return_on_equity_ebit_roe_mean_63d_base_v022_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebit_roe scaled by closeadj
def f064roe_f064_return_on_equity_ebit_roe_mean_126d_base_v023_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebit_roe scaled by closeadj
def f064roe_f064_return_on_equity_ebit_roe_mean_252d_base_v024_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebit_roe scaled by closeadj
def f064roe_f064_return_on_equity_ebit_roe_mean_504d_base_v025_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roe_vol_252 scaled by closeadj
def f064roe_f064_return_on_equity_roe_vol_252_mean_21d_base_v026_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roe_vol_252 scaled by closeadj
def f064roe_f064_return_on_equity_roe_vol_252_mean_63d_base_v027_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roe_vol_252 scaled by closeadj
def f064roe_f064_return_on_equity_roe_vol_252_mean_126d_base_v028_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roe_vol_252 scaled by closeadj
def f064roe_f064_return_on_equity_roe_vol_252_mean_252d_base_v029_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roe_vol_252 scaled by closeadj
def f064roe_f064_return_on_equity_roe_vol_252_mean_504d_base_v030_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_equity scaled by closeadj
def f064roe_f064_return_on_equity_ocf_to_equity_mean_21d_base_v031_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_equity scaled by closeadj
def f064roe_f064_return_on_equity_ocf_to_equity_mean_63d_base_v032_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_equity scaled by closeadj
def f064roe_f064_return_on_equity_ocf_to_equity_mean_126d_base_v033_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_equity scaled by closeadj
def f064roe_f064_return_on_equity_ocf_to_equity_mean_252d_base_v034_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_equity scaled by closeadj
def f064roe_f064_return_on_equity_ocf_to_equity_mean_504d_base_v035_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_median_63d_base_v036_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_median_252d_base_v037_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_median_504d_base_v038_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_median_63d_base_v039_signal(roe, closeadj):
    base = roe
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_median_252d_base_v040_signal(roe, closeadj):
    base = roe
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_median_504d_base_v041_signal(roe, closeadj):
    base = roe
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_median_63d_base_v042_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_median_252d_base_v043_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_median_504d_base_v044_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_median_63d_base_v045_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_median_252d_base_v046_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_median_504d_base_v047_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_median_63d_base_v048_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_median_252d_base_v049_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_median_504d_base_v050_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_median_63d_base_v051_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_median_252d_base_v052_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_median_504d_base_v053_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_median_63d_base_v054_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_median_252d_base_v055_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_median_504d_base_v056_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roe_calc
def f064roe_f064_return_on_equity_roe_calc_rmax_252d_base_v057_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roe_calc
def f064roe_f064_return_on_equity_roe_calc_rmax_504d_base_v058_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_rmax_252d_base_v059_signal(roe, closeadj):
    base = roe
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_rmax_504d_base_v060_signal(roe, closeadj):
    base = roe
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_rmax_252d_base_v061_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_rmax_504d_base_v062_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_rmax_252d_base_v063_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_rmax_504d_base_v064_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_rmax_252d_base_v065_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_rmax_504d_base_v066_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_rmax_252d_base_v067_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_rmax_504d_base_v068_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_rmax_252d_base_v069_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_rmax_504d_base_v070_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roe_calc
def f064roe_f064_return_on_equity_roe_calc_rmin_252d_base_v071_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of roe_calc
def f064roe_f064_return_on_equity_roe_calc_rmin_504d_base_v072_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_rmin_252d_base_v073_signal(roe, closeadj):
    base = roe
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_rmin_504d_base_v074_signal(roe, closeadj):
    base = roe
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_rmin_252d_base_v075_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

