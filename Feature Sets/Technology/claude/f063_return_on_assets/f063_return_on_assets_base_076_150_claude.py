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


# 63d z-score of roa_calc
def f063roa_f063_return_on_assets_roa_calc_z_63d_base_v076_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roa_calc
def f063roa_f063_return_on_assets_roa_calc_z_126d_base_v077_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roa_calc
def f063roa_f063_return_on_assets_roa_calc_z_252d_base_v078_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roa_calc
def f063roa_f063_return_on_assets_roa_calc_z_504d_base_v079_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_z_63d_base_v080_signal(roa, closeadj):
    base = roa
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_z_126d_base_v081_signal(roa, closeadj):
    base = roa
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_z_252d_base_v082_signal(roa, closeadj):
    base = roa
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_z_504d_base_v083_signal(roa, closeadj):
    base = roa
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_z_63d_base_v084_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_z_126d_base_v085_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_z_252d_base_v086_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_z_504d_base_v087_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_z_63d_base_v088_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_z_126d_base_v089_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_z_252d_base_v090_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_z_504d_base_v091_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_z_63d_base_v092_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_z_126d_base_v093_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_z_252d_base_v094_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_z_504d_base_v095_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_z_63d_base_v096_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_z_126d_base_v097_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_z_252d_base_v098_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_z_504d_base_v099_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_z_63d_base_v100_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_z_126d_base_v101_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_z_252d_base_v102_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_z_504d_base_v103_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roa_calc
def f063roa_f063_return_on_assets_roa_calc_distmax_252d_base_v104_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roa_calc
def f063roa_f063_return_on_assets_roa_calc_distmax_504d_base_v105_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_distmax_252d_base_v106_signal(roa, closeadj):
    base = roa
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_distmax_504d_base_v107_signal(roa, closeadj):
    base = roa
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_distmax_252d_base_v108_signal(roa, closeadj):
    base = roa.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_distmax_504d_base_v109_signal(roa, closeadj):
    base = roa.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_distmax_252d_base_v110_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_distmax_504d_base_v111_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_distmax_252d_base_v112_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_distmax_504d_base_v113_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_distmax_252d_base_v114_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_distmax_504d_base_v115_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_distmax_252d_base_v116_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_distmax_504d_base_v117_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_distmed_126d_base_v118_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_distmed_252d_base_v119_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roa_calc
def f063roa_f063_return_on_assets_roa_calc_distmed_504d_base_v120_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_distmed_126d_base_v121_signal(roa, closeadj):
    base = roa
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_distmed_252d_base_v122_signal(roa, closeadj):
    base = roa
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_distmed_504d_base_v123_signal(roa, closeadj):
    base = roa
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_distmed_126d_base_v124_signal(roa, closeadj):
    base = roa.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_distmed_252d_base_v125_signal(roa, closeadj):
    base = roa.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_distmed_504d_base_v126_signal(roa, closeadj):
    base = roa.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_distmed_126d_base_v127_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_distmed_252d_base_v128_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_distmed_504d_base_v129_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_distmed_126d_base_v130_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_distmed_252d_base_v131_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_distmed_504d_base_v132_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_distmed_126d_base_v133_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_distmed_252d_base_v134_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_distmed_504d_base_v135_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_distmed_126d_base_v136_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_distmed_252d_base_v137_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roa_vol_252
def f063roa_f063_return_on_assets_roa_vol_252_distmed_504d_base_v138_signal(roa, closeadj):
    base = roa.rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roa_calc
def f063roa_f063_return_on_assets_roa_calc_chg_63d_base_v139_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roa_calc
def f063roa_f063_return_on_assets_roa_calc_chg_252d_base_v140_signal(netinc, assetsavg, closeadj):
    base = _f063_roa(netinc, assetsavg)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_chg_63d_base_v141_signal(roa, closeadj):
    base = roa
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roa_lvl
def f063roa_f063_return_on_assets_roa_lvl_chg_252d_base_v142_signal(roa, closeadj):
    base = roa
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_chg_63d_base_v143_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in roa_yoy_chg
def f063roa_f063_return_on_assets_roa_yoy_chg_chg_252d_base_v144_signal(roa, closeadj):
    base = roa.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_chg_63d_base_v145_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ebit_roa
def f063roa_f063_return_on_assets_ebit_roa_chg_252d_base_v146_signal(ebit, assetsavg, closeadj):
    base = ebit / assetsavg.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_chg_63d_base_v147_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ocf_roa
def f063roa_f063_return_on_assets_ocf_roa_chg_252d_base_v148_signal(ncfo, assets, closeadj):
    base = ncfo / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_chg_63d_base_v149_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in fcf_roa
def f063roa_f063_return_on_assets_fcf_roa_chg_252d_base_v150_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

