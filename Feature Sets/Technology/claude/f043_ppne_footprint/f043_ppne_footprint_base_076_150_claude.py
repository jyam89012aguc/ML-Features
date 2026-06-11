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
def _f043_ppne_share(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan).abs()


# 63d z-score of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_z_63d_base_v076_signal(ppnenet, closeadj):
    base = ppnenet
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_z_126d_base_v077_signal(ppnenet, closeadj):
    base = ppnenet
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_z_252d_base_v078_signal(ppnenet, closeadj):
    base = ppnenet
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_z_504d_base_v079_signal(ppnenet, closeadj):
    base = ppnenet
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_z_63d_base_v080_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_z_126d_base_v081_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_z_252d_base_v082_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_z_504d_base_v083_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_z_63d_base_v084_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_z_126d_base_v085_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_z_252d_base_v086_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_z_504d_base_v087_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_z_63d_base_v088_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_z_126d_base_v089_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_z_252d_base_v090_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_z_504d_base_v091_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_z_63d_base_v092_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_z_126d_base_v093_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_z_252d_base_v094_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_z_504d_base_v095_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_z_63d_base_v096_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_z_126d_base_v097_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_z_252d_base_v098_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_z_504d_base_v099_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_z_63d_base_v100_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_z_126d_base_v101_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_z_252d_base_v102_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_z_504d_base_v103_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_distmax_252d_base_v104_signal(ppnenet, closeadj):
    base = ppnenet
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_distmax_504d_base_v105_signal(ppnenet, closeadj):
    base = ppnenet
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_distmax_252d_base_v106_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_distmax_504d_base_v107_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_distmax_252d_base_v108_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_distmax_504d_base_v109_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_distmax_252d_base_v110_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_distmax_504d_base_v111_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_distmax_252d_base_v112_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_distmax_504d_base_v113_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_distmax_252d_base_v114_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_distmax_504d_base_v115_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_distmax_252d_base_v116_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_distmax_504d_base_v117_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_distmed_126d_base_v118_signal(ppnenet, closeadj):
    base = ppnenet
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_distmed_252d_base_v119_signal(ppnenet, closeadj):
    base = ppnenet
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_distmed_504d_base_v120_signal(ppnenet, closeadj):
    base = ppnenet
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_distmed_126d_base_v121_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_distmed_252d_base_v122_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_distmed_504d_base_v123_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_distmed_126d_base_v124_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_distmed_252d_base_v125_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_distmed_504d_base_v126_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_distmed_126d_base_v127_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_distmed_252d_base_v128_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_distmed_504d_base_v129_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_distmed_126d_base_v130_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_distmed_252d_base_v131_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_distmed_504d_base_v132_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_distmed_126d_base_v133_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_distmed_252d_base_v134_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_distmed_504d_base_v135_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_distmed_126d_base_v136_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_distmed_252d_base_v137_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_distmed_504d_base_v138_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_chg_63d_base_v139_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_chg_252d_base_v140_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_chg_63d_base_v141_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_chg_252d_base_v142_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_chg_63d_base_v143_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_chg_252d_base_v144_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_chg_63d_base_v145_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_chg_252d_base_v146_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_chg_63d_base_v147_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_chg_252d_base_v148_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_chg_63d_base_v149_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_chg_252d_base_v150_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

