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
def _f036_sbc_pps(sbcomp, sharesbas):
    return sbcomp / sharesbas.replace(0, np.nan).abs()


# 63d z-score of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_z_63d_base_v076_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_z_126d_base_v077_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_z_252d_base_v078_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_z_504d_base_v079_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_z_63d_base_v080_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_z_126d_base_v081_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_z_252d_base_v082_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_z_504d_base_v083_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_z_63d_base_v084_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_z_126d_base_v085_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_z_252d_base_v086_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_z_504d_base_v087_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_z_63d_base_v088_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_z_126d_base_v089_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_z_252d_base_v090_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_z_504d_base_v091_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_z_63d_base_v092_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_z_126d_base_v093_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_z_252d_base_v094_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_z_504d_base_v095_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_z_63d_base_v096_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_z_126d_base_v097_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_z_252d_base_v098_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_z_504d_base_v099_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_z_63d_base_v100_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_z_126d_base_v101_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_z_252d_base_v102_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_z_504d_base_v103_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_distmax_252d_base_v104_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_distmax_504d_base_v105_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_distmax_252d_base_v106_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_distmax_504d_base_v107_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_distmax_252d_base_v108_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_distmax_504d_base_v109_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_distmax_252d_base_v110_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_distmax_504d_base_v111_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_distmax_252d_base_v112_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_distmax_504d_base_v113_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_distmax_252d_base_v114_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_distmax_504d_base_v115_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_distmax_252d_base_v116_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_distmax_504d_base_v117_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_distmed_126d_base_v118_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_distmed_252d_base_v119_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_distmed_504d_base_v120_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_distmed_126d_base_v121_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_distmed_252d_base_v122_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_distmed_504d_base_v123_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_distmed_126d_base_v124_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_distmed_252d_base_v125_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_distmed_504d_base_v126_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_distmed_126d_base_v127_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_distmed_252d_base_v128_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_distmed_504d_base_v129_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_distmed_126d_base_v130_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_distmed_252d_base_v131_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_distmed_504d_base_v132_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_distmed_126d_base_v133_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_distmed_252d_base_v134_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_distmed_504d_base_v135_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_distmed_126d_base_v136_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_distmed_252d_base_v137_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_distmed_504d_base_v138_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_chg_63d_base_v139_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_chg_252d_base_v140_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_chg_63d_base_v141_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_chg_252d_base_v142_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_chg_63d_base_v143_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_chg_252d_base_v144_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_chg_63d_base_v145_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_chg_252d_base_v146_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_chg_63d_base_v147_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_chg_252d_base_v148_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_chg_63d_base_v149_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_chg_252d_base_v150_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

