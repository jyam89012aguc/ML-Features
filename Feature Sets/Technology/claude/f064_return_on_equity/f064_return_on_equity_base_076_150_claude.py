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


# 63d z-score of roe_calc
def f064roe_f064_return_on_equity_roe_calc_z_63d_base_v076_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roe_calc
def f064roe_f064_return_on_equity_roe_calc_z_126d_base_v077_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roe_calc
def f064roe_f064_return_on_equity_roe_calc_z_252d_base_v078_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roe_calc
def f064roe_f064_return_on_equity_roe_calc_z_504d_base_v079_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_z_63d_base_v080_signal(roe, closeadj):
    base = roe
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_z_126d_base_v081_signal(roe, closeadj):
    base = roe
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_z_252d_base_v082_signal(roe, closeadj):
    base = roe
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_z_504d_base_v083_signal(roe, closeadj):
    base = roe
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_z_63d_base_v084_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_z_126d_base_v085_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_z_252d_base_v086_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_z_504d_base_v087_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_z_63d_base_v088_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_z_126d_base_v089_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_z_252d_base_v090_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_z_504d_base_v091_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_z_63d_base_v092_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_z_126d_base_v093_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_z_252d_base_v094_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_z_504d_base_v095_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_z_63d_base_v096_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_z_126d_base_v097_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_z_252d_base_v098_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_z_504d_base_v099_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_z_63d_base_v100_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_z_126d_base_v101_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_z_252d_base_v102_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_z_504d_base_v103_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roe_calc
def f064roe_f064_return_on_equity_roe_calc_distmax_252d_base_v104_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roe_calc
def f064roe_f064_return_on_equity_roe_calc_distmax_504d_base_v105_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_distmax_252d_base_v106_signal(roe, closeadj):
    base = roe
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_distmax_504d_base_v107_signal(roe, closeadj):
    base = roe
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_distmax_252d_base_v108_signal(roe, closeadj):
    base = roe.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_distmax_504d_base_v109_signal(roe, closeadj):
    base = roe.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_distmax_252d_base_v110_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_distmax_504d_base_v111_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_distmax_252d_base_v112_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_distmax_504d_base_v113_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_distmax_252d_base_v114_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_distmax_504d_base_v115_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_distmax_252d_base_v116_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_distmax_504d_base_v117_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_distmed_126d_base_v118_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_distmed_252d_base_v119_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roe_calc
def f064roe_f064_return_on_equity_roe_calc_distmed_504d_base_v120_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_distmed_126d_base_v121_signal(roe, closeadj):
    base = roe
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_distmed_252d_base_v122_signal(roe, closeadj):
    base = roe
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_distmed_504d_base_v123_signal(roe, closeadj):
    base = roe
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_distmed_126d_base_v124_signal(roe, closeadj):
    base = roe.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_distmed_252d_base_v125_signal(roe, closeadj):
    base = roe.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_distmed_504d_base_v126_signal(roe, closeadj):
    base = roe.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_distmed_126d_base_v127_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_distmed_252d_base_v128_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_distmed_504d_base_v129_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_distmed_126d_base_v130_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_distmed_252d_base_v131_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_distmed_504d_base_v132_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_distmed_126d_base_v133_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_distmed_252d_base_v134_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_distmed_504d_base_v135_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_distmed_126d_base_v136_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_distmed_252d_base_v137_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_equity
def f064roe_f064_return_on_equity_ocf_to_equity_distmed_504d_base_v138_signal(ncfo, equity, closeadj):
    base = ncfo / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roe_calc
def f064roe_f064_return_on_equity_roe_calc_chg_63d_base_v139_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roe_calc
def f064roe_f064_return_on_equity_roe_calc_chg_252d_base_v140_signal(netinc, equity, closeadj):
    base = _f064_roe(netinc, equity)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_chg_63d_base_v141_signal(roe, closeadj):
    base = roe
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roe_lvl
def f064roe_f064_return_on_equity_roe_lvl_chg_252d_base_v142_signal(roe, closeadj):
    base = roe
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_chg_63d_base_v143_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roe_yoy_chg
def f064roe_f064_return_on_equity_roe_yoy_chg_chg_252d_base_v144_signal(roe, closeadj):
    base = roe.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_chg_63d_base_v145_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in neg_eq_roe_flag
def f064roe_f064_return_on_equity_neg_eq_roe_flag_chg_252d_base_v146_signal(equity, closeadj):
    base = (equity < 0).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_chg_63d_base_v147_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ebit_roe
def f064roe_f064_return_on_equity_ebit_roe_chg_252d_base_v148_signal(ebit, equity, closeadj):
    base = ebit / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_chg_63d_base_v149_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roe_vol_252
def f064roe_f064_return_on_equity_roe_vol_252_chg_252d_base_v150_signal(roe, closeadj):
    base = roe.rolling(252, min_periods=63).std()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

