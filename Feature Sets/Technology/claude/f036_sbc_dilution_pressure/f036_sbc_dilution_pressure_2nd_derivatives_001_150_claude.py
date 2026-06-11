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
def _f036_sbc_pps(sbcomp, sharesbas):
    return sbcomp / sharesbas.replace(0, np.nan).abs()


# 21d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slope_21d_2d_v001_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slope_63d_2d_v002_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slope_126d_2d_v003_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slope_252d_2d_v004_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slope_504d_2d_v005_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slope_21d_2d_v006_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slope_63d_2d_v007_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slope_126d_2d_v008_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slope_252d_2d_v009_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slope_504d_2d_v010_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slope_21d_2d_v011_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slope_63d_2d_v012_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slope_126d_2d_v013_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slope_252d_2d_v014_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slope_504d_2d_v015_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slope_21d_2d_v016_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slope_63d_2d_v017_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slope_126d_2d_v018_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slope_252d_2d_v019_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slope_504d_2d_v020_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slope_21d_2d_v021_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slope_63d_2d_v022_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slope_126d_2d_v023_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slope_252d_2d_v024_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slope_504d_2d_v025_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slope_21d_2d_v026_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slope_63d_2d_v027_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slope_126d_2d_v028_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slope_252d_2d_v029_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slope_504d_2d_v030_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slope_21d_2d_v031_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slope_63d_2d_v032_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slope_126d_2d_v033_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slope_252d_2d_v034_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slope_504d_2d_v035_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sm21_sl21_2d_v036_signal(sbcomp, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sm63_sl21_2d_v037_signal(sbcomp, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sm63_sl63_2d_v038_signal(sbcomp, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sm252_sl63_2d_v039_signal(sbcomp, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sm252_sl126_2d_v040_signal(sbcomp, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sm21_sl21_2d_v041_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_f036_sbc_pps(sbcomp, sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sm63_sl21_2d_v042_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_f036_sbc_pps(sbcomp, sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sm63_sl63_2d_v043_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_f036_sbc_pps(sbcomp, sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sm252_sl63_2d_v044_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_f036_sbc_pps(sbcomp, sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sm252_sl126_2d_v045_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_f036_sbc_pps(sbcomp, sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sm21_sl21_2d_v046_signal(sbcomp, ncfcommon, closeadj):
    base = _mean(sbcomp / ncfcommon.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sm63_sl21_2d_v047_signal(sbcomp, ncfcommon, closeadj):
    base = _mean(sbcomp / ncfcommon.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sm63_sl63_2d_v048_signal(sbcomp, ncfcommon, closeadj):
    base = _mean(sbcomp / ncfcommon.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sm252_sl63_2d_v049_signal(sbcomp, ncfcommon, closeadj):
    base = _mean(sbcomp / ncfcommon.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sm252_sl126_2d_v050_signal(sbcomp, ncfcommon, closeadj):
    base = _mean(sbcomp / ncfcommon.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sm21_sl21_2d_v051_signal(sbcomp, shareswadil, closeadj):
    base = _mean(sbcomp / shareswadil.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sm63_sl21_2d_v052_signal(sbcomp, shareswadil, closeadj):
    base = _mean(sbcomp / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sm63_sl63_2d_v053_signal(sbcomp, shareswadil, closeadj):
    base = _mean(sbcomp / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sm252_sl63_2d_v054_signal(sbcomp, shareswadil, closeadj):
    base = _mean(sbcomp / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sm252_sl126_2d_v055_signal(sbcomp, shareswadil, closeadj):
    base = _mean(sbcomp / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sm21_sl21_2d_v056_signal(sbcomp, closeadj):
    base = _mean(sbcomp.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sm63_sl21_2d_v057_signal(sbcomp, closeadj):
    base = _mean(sbcomp.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sm63_sl63_2d_v058_signal(sbcomp, closeadj):
    base = _mean(sbcomp.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sm252_sl63_2d_v059_signal(sbcomp, closeadj):
    base = _mean(sbcomp.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sm252_sl126_2d_v060_signal(sbcomp, closeadj):
    base = _mean(sbcomp.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sm21_sl21_2d_v061_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sm63_sl21_2d_v062_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sm63_sl63_2d_v063_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sm252_sl63_2d_v064_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sm252_sl126_2d_v065_signal(sbcomp, equity, closeadj):
    base = _mean(sbcomp / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sm21_sl21_2d_v066_signal(sbcomp, revenue, closeadj):
    base = _mean(sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sm63_sl21_2d_v067_signal(sbcomp, revenue, closeadj):
    base = _mean(sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sm63_sl63_2d_v068_signal(sbcomp, revenue, closeadj):
    base = _mean(sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sm252_sl63_2d_v069_signal(sbcomp, revenue, closeadj):
    base = _mean(sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sm252_sl126_2d_v070_signal(sbcomp, revenue, closeadj):
    base = _mean(sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_pctslope_21d_2d_v071_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_pctslope_63d_2d_v072_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_pctslope_252d_2d_v073_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_pctslope_21d_2d_v074_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_pctslope_63d_2d_v075_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_pctslope_252d_2d_v076_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_pctslope_21d_2d_v077_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_pctslope_63d_2d_v078_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_pctslope_252d_2d_v079_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_pctslope_21d_2d_v080_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_pctslope_63d_2d_v081_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_pctslope_252d_2d_v082_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_pctslope_21d_2d_v083_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_pctslope_63d_2d_v084_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_pctslope_252d_2d_v085_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_pctslope_21d_2d_v086_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_pctslope_63d_2d_v087_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_pctslope_252d_2d_v088_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_pctslope_21d_2d_v089_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_pctslope_63d_2d_v090_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_pctslope_252d_2d_v091_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sgnslope_21d_2d_v092_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sgnslope_63d_2d_v093_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_sgnslope_252d_2d_v094_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sgnslope_21d_2d_v095_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sgnslope_63d_2d_v096_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_sgnslope_252d_2d_v097_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sgnslope_21d_2d_v098_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sgnslope_63d_2d_v099_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_sgnslope_252d_2d_v100_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sgnslope_21d_2d_v101_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sgnslope_63d_2d_v102_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_sgnslope_252d_2d_v103_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sgnslope_21d_2d_v104_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sgnslope_63d_2d_v105_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_sgnslope_252d_2d_v106_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sgnslope_21d_2d_v107_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sgnslope_63d_2d_v108_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_sgnslope_252d_2d_v109_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sgnslope_21d_2d_v110_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sgnslope_63d_2d_v111_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_sgnslope_252d_2d_v112_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_logmagslope_21d_2d_v113_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_logmagslope_63d_2d_v114_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_logmagslope_252d_2d_v115_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_logmagslope_21d_2d_v116_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_logmagslope_63d_2d_v117_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_logmagslope_252d_2d_v118_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_logmagslope_21d_2d_v119_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_logmagslope_63d_2d_v120_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_logmagslope_252d_2d_v121_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_logmagslope_21d_2d_v122_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_logmagslope_63d_2d_v123_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_logmagslope_252d_2d_v124_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_logmagslope_21d_2d_v125_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_logmagslope_63d_2d_v126_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_logmagslope_252d_2d_v127_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_logmagslope_21d_2d_v128_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_logmagslope_63d_2d_v129_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_logmagslope_252d_2d_v130_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_logmagslope_21d_2d_v131_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_logmagslope_63d_2d_v132_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_logmagslope_252d_2d_v133_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_to_mcap_dil|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_logslope_63d_2d_v134_signal(sbcomp, marketcap, closeadj):
    base = np.log((sbcomp / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_to_mcap_dil|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_logslope_252d_2d_v135_signal(sbcomp, marketcap, closeadj):
    base = np.log((sbcomp / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_pps|
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_logslope_63d_2d_v136_signal(sbcomp, sharesbas, closeadj):
    base = np.log((_f036_sbc_pps(sbcomp, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_pps|
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_logslope_252d_2d_v137_signal(sbcomp, sharesbas, closeadj):
    base = np.log((_f036_sbc_pps(sbcomp, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_to_raise|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_logslope_63d_2d_v138_signal(sbcomp, ncfcommon, closeadj):
    base = np.log((sbcomp / ncfcommon.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_to_raise|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_logslope_252d_2d_v139_signal(sbcomp, ncfcommon, closeadj):
    base = np.log((sbcomp / ncfcommon.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_per_dilshare|
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_logslope_63d_2d_v140_signal(sbcomp, shareswadil, closeadj):
    base = np.log((sbcomp / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_per_dilshare|
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_logslope_252d_2d_v141_signal(sbcomp, shareswadil, closeadj):
    base = np.log((sbcomp / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_yoy_chg|
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_logslope_63d_2d_v142_signal(sbcomp, closeadj):
    base = np.log((sbcomp.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_yoy_chg|
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_logslope_252d_2d_v143_signal(sbcomp, closeadj):
    base = np.log((sbcomp.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dil_drag_index|
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_logslope_63d_2d_v144_signal(sbcomp, equity, closeadj):
    base = np.log((sbcomp / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dil_drag_index|
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_logslope_252d_2d_v145_signal(sbcomp, equity, closeadj):
    base = np.log((sbcomp / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_to_revgrowth|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_logslope_63d_2d_v146_signal(sbcomp, revenue, closeadj):
    base = np.log((sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_to_revgrowth|
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_logslope_252d_2d_v147_signal(sbcomp, revenue, closeadj):
    base = np.log((sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

