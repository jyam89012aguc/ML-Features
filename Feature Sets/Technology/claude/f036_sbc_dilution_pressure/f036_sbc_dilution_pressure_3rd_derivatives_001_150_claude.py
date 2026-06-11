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


# 21d acceleration of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accel_21d_3d_v001_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accel_63d_3d_v002_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accel_126d_3d_v003_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accel_252d_3d_v004_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accel_21d_3d_v005_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accel_63d_3d_v006_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accel_126d_3d_v007_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accel_252d_3d_v008_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accel_21d_3d_v009_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accel_63d_3d_v010_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accel_126d_3d_v011_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accel_252d_3d_v012_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accel_21d_3d_v013_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accel_63d_3d_v014_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accel_126d_3d_v015_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accel_252d_3d_v016_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accel_21d_3d_v017_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accel_63d_3d_v018_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accel_126d_3d_v019_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accel_252d_3d_v020_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accel_21d_3d_v021_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accel_63d_3d_v022_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accel_126d_3d_v023_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accel_252d_3d_v024_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accel_21d_3d_v025_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accel_63d_3d_v026_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accel_126d_3d_v027_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accel_252d_3d_v028_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slopez_21d_z126_3d_v029_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slopez_63d_z252_3d_v030_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slopez_126d_z252_3d_v031_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_slopez_252d_z504_3d_v032_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slopez_21d_z126_3d_v033_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slopez_63d_z252_3d_v034_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slopez_126d_z252_3d_v035_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_slopez_252d_z504_3d_v036_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slopez_21d_z126_3d_v037_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slopez_63d_z252_3d_v038_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slopez_126d_z252_3d_v039_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_slopez_252d_z504_3d_v040_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slopez_21d_z126_3d_v041_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slopez_63d_z252_3d_v042_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slopez_126d_z252_3d_v043_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_slopez_252d_z504_3d_v044_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slopez_21d_z126_3d_v045_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slopez_63d_z252_3d_v046_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slopez_126d_z252_3d_v047_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_slopez_252d_z504_3d_v048_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slopez_21d_z126_3d_v049_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slopez_63d_z252_3d_v050_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slopez_126d_z252_3d_v051_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_slopez_252d_z504_3d_v052_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slopez_21d_z126_3d_v053_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slopez_63d_z252_3d_v054_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slopez_126d_z252_3d_v055_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_slopez_252d_z504_3d_v056_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_jerk_21d_3d_v057_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_jerk_63d_3d_v058_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_jerk_126d_3d_v059_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_jerk_21d_3d_v060_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_jerk_63d_3d_v061_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_jerk_126d_3d_v062_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_jerk_21d_3d_v063_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_jerk_63d_3d_v064_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_jerk_126d_3d_v065_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_jerk_21d_3d_v066_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_jerk_63d_3d_v067_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_jerk_126d_3d_v068_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_jerk_21d_3d_v069_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_jerk_63d_3d_v070_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_jerk_126d_3d_v071_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_jerk_21d_3d_v072_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_jerk_63d_3d_v073_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_jerk_126d_3d_v074_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_jerk_21d_3d_v075_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_jerk_63d_3d_v076_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_jerk_126d_3d_v077_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_to_mcap_dil smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_smoothaccel_63d_sm252_3d_v078_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_to_mcap_dil smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_smoothaccel_252d_sm504_3d_v079_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_pps smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_smoothaccel_63d_sm252_3d_v080_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_pps smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_smoothaccel_252d_sm504_3d_v081_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_to_raise smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_smoothaccel_63d_sm252_3d_v082_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_to_raise smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_smoothaccel_252d_sm504_3d_v083_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_per_dilshare smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_smoothaccel_63d_sm252_3d_v084_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_per_dilshare smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_smoothaccel_252d_sm504_3d_v085_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_yoy_chg smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_smoothaccel_63d_sm252_3d_v086_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_yoy_chg smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_smoothaccel_252d_sm504_3d_v087_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dil_drag_index smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_smoothaccel_63d_sm252_3d_v088_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dil_drag_index smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_smoothaccel_252d_sm504_3d_v089_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_to_revgrowth smoothed over 252d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_smoothaccel_63d_sm252_3d_v090_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_to_revgrowth smoothed over 504d
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_smoothaccel_252d_sm504_3d_v091_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accelz_21d_z252_3d_v092_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_accelz_63d_z504_3d_v093_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accelz_21d_z252_3d_v094_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_accelz_63d_z504_3d_v095_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accelz_21d_z252_3d_v096_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_accelz_63d_z504_3d_v097_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accelz_21d_z252_3d_v098_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_accelz_63d_z504_3d_v099_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accelz_21d_z252_3d_v100_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_accelz_63d_z504_3d_v101_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accelz_21d_z252_3d_v102_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_accelz_63d_z504_3d_v103_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accelz_21d_z252_3d_v104_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_accelz_63d_z504_3d_v105_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_to_mcap_dil (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_signflip_63d_3d_v106_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_to_mcap_dil (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_signflip_252d_3d_v107_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_pps (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_signflip_63d_3d_v108_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_pps (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_signflip_252d_3d_v109_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_to_raise (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_signflip_63d_3d_v110_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_to_raise (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_signflip_252d_3d_v111_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_per_dilshare (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_signflip_63d_3d_v112_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_per_dilshare (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_signflip_252d_3d_v113_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_yoy_chg (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_signflip_63d_3d_v114_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_yoy_chg (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_signflip_252d_3d_v115_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dil_drag_index (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_signflip_63d_3d_v116_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dil_drag_index (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_signflip_252d_3d_v117_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_to_revgrowth (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_signflip_63d_3d_v118_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_to_revgrowth (raw count, no price scaling)
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_signflip_252d_3d_v119_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_mcap_dil normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rngaccel_63d_r252_3d_v120_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_mcap_dil normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rngaccel_252d_r504_3d_v121_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_pps normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rngaccel_63d_r252_3d_v122_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_pps normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rngaccel_252d_r504_3d_v123_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_raise normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_rngaccel_63d_r252_3d_v124_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_raise normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_rngaccel_252d_r504_3d_v125_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_per_dilshare normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_rngaccel_63d_r252_3d_v126_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_per_dilshare normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_rngaccel_252d_r504_3d_v127_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_yoy_chg normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_rngaccel_63d_r252_3d_v128_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_yoy_chg normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_rngaccel_252d_r504_3d_v129_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_drag_index normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_rngaccel_63d_r252_3d_v130_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_drag_index normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_rngaccel_252d_r504_3d_v131_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_revgrowth normalized by 252d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_rngaccel_63d_r252_3d_v132_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_revgrowth normalized by 504d range
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_rngaccel_252d_r504_3d_v133_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_cumslope_21d_3d_v134_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_cumslope_63d_3d_v135_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_cumslope_252d_3d_v136_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_cumslope_21d_3d_v137_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_cumslope_63d_3d_v138_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_cumslope_252d_3d_v139_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_cumslope_21d_3d_v140_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_cumslope_63d_3d_v141_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_cumslope_252d_3d_v142_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_cumslope_21d_3d_v143_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_cumslope_63d_3d_v144_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_cumslope_252d_3d_v145_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_cumslope_21d_3d_v146_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_cumslope_63d_3d_v147_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_cumslope_252d_3d_v148_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_cumslope_21d_3d_v149_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_cumslope_63d_3d_v150_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

