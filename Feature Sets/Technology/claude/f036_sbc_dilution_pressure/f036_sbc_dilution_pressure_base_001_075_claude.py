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


# 21d mean of sbc_to_mcap_dil scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_mean_21d_base_v001_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_mcap_dil scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_mean_63d_base_v002_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_mcap_dil scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_mean_126d_base_v003_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_mcap_dil scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_mean_252d_base_v004_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_mcap_dil scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_mean_504d_base_v005_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_pps scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_mean_21d_base_v006_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_pps scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_mean_63d_base_v007_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_pps scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_mean_126d_base_v008_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_pps scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_mean_252d_base_v009_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_pps scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_mean_504d_base_v010_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_raise scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_mean_21d_base_v011_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_raise scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_mean_63d_base_v012_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_raise scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_mean_126d_base_v013_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_raise scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_mean_252d_base_v014_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_raise scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_mean_504d_base_v015_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_per_dilshare scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_mean_21d_base_v016_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_per_dilshare scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_mean_63d_base_v017_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_per_dilshare scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_mean_126d_base_v018_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_per_dilshare scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_mean_252d_base_v019_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_per_dilshare scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_mean_504d_base_v020_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_yoy_chg scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_mean_21d_base_v021_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_yoy_chg scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_mean_63d_base_v022_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_yoy_chg scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_mean_126d_base_v023_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_yoy_chg scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_mean_252d_base_v024_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_yoy_chg scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_mean_504d_base_v025_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dil_drag_index scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_mean_21d_base_v026_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dil_drag_index scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_mean_63d_base_v027_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dil_drag_index scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_mean_126d_base_v028_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dil_drag_index scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_mean_252d_base_v029_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dil_drag_index scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_mean_504d_base_v030_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sbc_to_revgrowth scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_mean_21d_base_v031_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sbc_to_revgrowth scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_mean_63d_base_v032_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sbc_to_revgrowth scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_mean_126d_base_v033_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sbc_to_revgrowth scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_mean_252d_base_v034_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sbc_to_revgrowth scaled by closeadj
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_mean_504d_base_v035_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_median_63d_base_v036_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_median_252d_base_v037_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_median_504d_base_v038_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_median_63d_base_v039_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_median_252d_base_v040_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_median_504d_base_v041_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_median_63d_base_v042_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_median_252d_base_v043_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_median_504d_base_v044_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_median_63d_base_v045_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_median_252d_base_v046_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_median_504d_base_v047_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_median_63d_base_v048_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_median_252d_base_v049_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_median_504d_base_v050_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_median_63d_base_v051_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_median_252d_base_v052_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_median_504d_base_v053_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_median_63d_base_v054_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_median_252d_base_v055_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_median_504d_base_v056_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rmax_252d_base_v057_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rmax_504d_base_v058_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rmax_252d_base_v059_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rmax_504d_base_v060_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_rmax_252d_base_v061_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_rmax_504d_base_v062_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_rmax_252d_base_v063_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_per_dilshare
def f036sdp_f036_sbc_dilution_pressure_sbc_per_dilshare_rmax_504d_base_v064_signal(sbcomp, shareswadil, closeadj):
    base = sbcomp / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_rmax_252d_base_v065_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_yoy_chg
def f036sdp_f036_sbc_dilution_pressure_sbc_yoy_chg_rmax_504d_base_v066_signal(sbcomp, closeadj):
    base = sbcomp.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_rmax_252d_base_v067_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dil_drag_index
def f036sdp_f036_sbc_dilution_pressure_dil_drag_index_rmax_504d_base_v068_signal(sbcomp, equity, closeadj):
    base = sbcomp / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_rmax_252d_base_v069_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sbc_to_revgrowth
def f036sdp_f036_sbc_dilution_pressure_sbc_to_revgrowth_rmax_504d_base_v070_signal(sbcomp, revenue, closeadj):
    base = sbcomp / revenue.diff(periods=252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rmin_252d_base_v071_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sbc_to_mcap_dil
def f036sdp_f036_sbc_dilution_pressure_sbc_to_mcap_dil_rmin_504d_base_v072_signal(sbcomp, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rmin_252d_base_v073_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sbc_pps
def f036sdp_f036_sbc_dilution_pressure_sbc_pps_rmin_504d_base_v074_signal(sbcomp, sharesbas, closeadj):
    base = _f036_sbc_pps(sbcomp, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sbc_to_raise
def f036sdp_f036_sbc_dilution_pressure_sbc_to_raise_rmin_252d_base_v075_signal(sbcomp, ncfcommon, closeadj):
    base = sbcomp / ncfcommon.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

