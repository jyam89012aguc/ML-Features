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
def _f042_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 63d z-score of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_z_63d_base_v076_signal(intangibles, closeadj):
    base = intangibles
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_z_126d_base_v077_signal(intangibles, closeadj):
    base = intangibles
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_z_252d_base_v078_signal(intangibles, closeadj):
    base = intangibles
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_z_504d_base_v079_signal(intangibles, closeadj):
    base = intangibles
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_z_63d_base_v080_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_z_126d_base_v081_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_z_252d_base_v082_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_z_504d_base_v083_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_z_63d_base_v084_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_z_126d_base_v085_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_z_252d_base_v086_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_z_504d_base_v087_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_z_63d_base_v088_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_z_126d_base_v089_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_z_252d_base_v090_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_z_504d_base_v091_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_z_63d_base_v092_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_z_126d_base_v093_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_z_252d_base_v094_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_z_504d_base_v095_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_z_63d_base_v096_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_z_126d_base_v097_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_z_252d_base_v098_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_z_504d_base_v099_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_z_63d_base_v100_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_z_126d_base_v101_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_z_252d_base_v102_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_z_504d_base_v103_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_distmax_252d_base_v104_signal(intangibles, closeadj):
    base = intangibles
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_distmax_504d_base_v105_signal(intangibles, closeadj):
    base = intangibles
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_distmax_252d_base_v106_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_distmax_504d_base_v107_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_distmax_252d_base_v108_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_distmax_504d_base_v109_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_distmax_252d_base_v110_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_distmax_504d_base_v111_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_distmax_252d_base_v112_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_distmax_504d_base_v113_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_distmax_252d_base_v114_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_distmax_504d_base_v115_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_distmax_252d_base_v116_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_distmax_504d_base_v117_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_distmed_126d_base_v118_signal(intangibles, closeadj):
    base = intangibles
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_distmed_252d_base_v119_signal(intangibles, closeadj):
    base = intangibles
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_distmed_504d_base_v120_signal(intangibles, closeadj):
    base = intangibles
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_distmed_126d_base_v121_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_distmed_252d_base_v122_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_distmed_504d_base_v123_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_distmed_126d_base_v124_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_distmed_252d_base_v125_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_distmed_504d_base_v126_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_distmed_126d_base_v127_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_distmed_252d_base_v128_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_distmed_504d_base_v129_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_distmed_126d_base_v130_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_distmed_252d_base_v131_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_distmed_504d_base_v132_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_distmed_126d_base_v133_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_distmed_252d_base_v134_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_distmed_504d_base_v135_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_distmed_126d_base_v136_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_distmed_252d_base_v137_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_distmed_504d_base_v138_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_chg_63d_base_v139_signal(intangibles, closeadj):
    base = intangibles
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_chg_252d_base_v140_signal(intangibles, closeadj):
    base = intangibles
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_chg_63d_base_v141_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_chg_252d_base_v142_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_chg_63d_base_v143_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_chg_252d_base_v144_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_chg_63d_base_v145_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_chg_252d_base_v146_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_chg_63d_base_v147_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_chg_252d_base_v148_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_chg_63d_base_v149_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_chg_252d_base_v150_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

