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
def _f066_at(revenue, assetsavg):
    return revenue / assetsavg.replace(0, np.nan).abs()


# 63d z-score of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_z_63d_base_v076_signal(assetturnover, closeadj):
    base = assetturnover
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_z_126d_base_v077_signal(assetturnover, closeadj):
    base = assetturnover
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_z_252d_base_v078_signal(assetturnover, closeadj):
    base = assetturnover
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_z_504d_base_v079_signal(assetturnover, closeadj):
    base = assetturnover
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_z_63d_base_v080_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_z_126d_base_v081_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_z_252d_base_v082_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_z_504d_base_v083_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_z_63d_base_v084_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_z_126d_base_v085_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_z_252d_base_v086_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_z_504d_base_v087_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_z_63d_base_v088_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_z_126d_base_v089_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_z_252d_base_v090_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_z_504d_base_v091_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_z_63d_base_v092_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_z_126d_base_v093_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_z_252d_base_v094_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_z_504d_base_v095_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_z_63d_base_v096_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_z_126d_base_v097_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_z_252d_base_v098_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_z_504d_base_v099_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_z_63d_base_v100_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_z_126d_base_v101_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_z_252d_base_v102_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_z_504d_base_v103_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_distmax_252d_base_v104_signal(assetturnover, closeadj):
    base = assetturnover
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_distmax_504d_base_v105_signal(assetturnover, closeadj):
    base = assetturnover
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_distmax_252d_base_v106_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_distmax_504d_base_v107_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_distmax_252d_base_v108_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_distmax_504d_base_v109_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_distmax_252d_base_v110_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_distmax_504d_base_v111_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_distmax_252d_base_v112_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_distmax_504d_base_v113_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_distmax_252d_base_v114_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_distmax_504d_base_v115_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_distmax_252d_base_v116_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_distmax_504d_base_v117_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_distmed_126d_base_v118_signal(assetturnover, closeadj):
    base = assetturnover
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_distmed_252d_base_v119_signal(assetturnover, closeadj):
    base = assetturnover
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_distmed_504d_base_v120_signal(assetturnover, closeadj):
    base = assetturnover
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_distmed_126d_base_v121_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_distmed_252d_base_v122_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_distmed_504d_base_v123_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_distmed_126d_base_v124_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_distmed_252d_base_v125_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_distmed_504d_base_v126_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_distmed_126d_base_v127_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_distmed_252d_base_v128_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_distmed_504d_base_v129_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_distmed_126d_base_v130_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_distmed_252d_base_v131_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_distmed_504d_base_v132_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_distmed_126d_base_v133_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_distmed_252d_base_v134_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_distmed_504d_base_v135_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_distmed_126d_base_v136_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_distmed_252d_base_v137_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_distmed_504d_base_v138_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_chg_63d_base_v139_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_chg_252d_base_v140_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_chg_63d_base_v141_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_chg_252d_base_v142_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_chg_63d_base_v143_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_chg_252d_base_v144_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_chg_63d_base_v145_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_chg_252d_base_v146_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_chg_63d_base_v147_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_chg_252d_base_v148_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_chg_63d_base_v149_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_chg_252d_base_v150_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

