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
def _f056_eps_yield(eps, close):
    return eps / close.replace(0, np.nan).abs()


# 63d z-score of eps_lvl
def f056eps_f056_eps_level_eps_lvl_z_63d_base_v076_signal(eps, closeadj):
    base = eps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_lvl
def f056eps_f056_eps_level_eps_lvl_z_126d_base_v077_signal(eps, closeadj):
    base = eps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_lvl
def f056eps_f056_eps_level_eps_lvl_z_252d_base_v078_signal(eps, closeadj):
    base = eps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_lvl
def f056eps_f056_eps_level_eps_lvl_z_504d_base_v079_signal(eps, closeadj):
    base = eps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_z_63d_base_v080_signal(epsdil, closeadj):
    base = epsdil
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_z_126d_base_v081_signal(epsdil, closeadj):
    base = epsdil
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_z_252d_base_v082_signal(epsdil, closeadj):
    base = epsdil
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_z_504d_base_v083_signal(epsdil, closeadj):
    base = epsdil
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_yield
def f056eps_f056_eps_level_eps_yield_z_63d_base_v084_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_yield
def f056eps_f056_eps_level_eps_yield_z_126d_base_v085_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_yield
def f056eps_f056_eps_level_eps_yield_z_252d_base_v086_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_yield
def f056eps_f056_eps_level_eps_yield_z_504d_base_v087_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_sign
def f056eps_f056_eps_level_eps_sign_z_63d_base_v088_signal(eps, closeadj):
    base = np.sign(eps)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_sign
def f056eps_f056_eps_level_eps_sign_z_126d_base_v089_signal(eps, closeadj):
    base = np.sign(eps)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_sign
def f056eps_f056_eps_level_eps_sign_z_252d_base_v090_signal(eps, closeadj):
    base = np.sign(eps)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_sign
def f056eps_f056_eps_level_eps_sign_z_504d_base_v091_signal(eps, closeadj):
    base = np.sign(eps)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_z_63d_base_v092_signal(epsusd, closeadj):
    base = epsusd
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_z_126d_base_v093_signal(epsusd, closeadj):
    base = epsusd
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_z_252d_base_v094_signal(epsusd, closeadj):
    base = epsusd
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_z_504d_base_v095_signal(epsusd, closeadj):
    base = epsusd
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_z_63d_base_v096_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_z_126d_base_v097_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_z_252d_base_v098_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_z_504d_base_v099_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_z_63d_base_v100_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_z_126d_base_v101_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_z_252d_base_v102_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_z_504d_base_v103_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_lvl
def f056eps_f056_eps_level_eps_lvl_distmax_252d_base_v104_signal(eps, closeadj):
    base = eps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_lvl
def f056eps_f056_eps_level_eps_lvl_distmax_504d_base_v105_signal(eps, closeadj):
    base = eps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_distmax_252d_base_v106_signal(epsdil, closeadj):
    base = epsdil
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_distmax_504d_base_v107_signal(epsdil, closeadj):
    base = epsdil
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_yield
def f056eps_f056_eps_level_eps_yield_distmax_252d_base_v108_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_yield
def f056eps_f056_eps_level_eps_yield_distmax_504d_base_v109_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_sign
def f056eps_f056_eps_level_eps_sign_distmax_252d_base_v110_signal(eps, closeadj):
    base = np.sign(eps)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_sign
def f056eps_f056_eps_level_eps_sign_distmax_504d_base_v111_signal(eps, closeadj):
    base = np.sign(eps)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_distmax_252d_base_v112_signal(epsusd, closeadj):
    base = epsusd
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_distmax_504d_base_v113_signal(epsusd, closeadj):
    base = epsusd
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_distmax_252d_base_v114_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_distmax_504d_base_v115_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_distmax_252d_base_v116_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_distmax_504d_base_v117_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_distmed_126d_base_v118_signal(eps, closeadj):
    base = eps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_distmed_252d_base_v119_signal(eps, closeadj):
    base = eps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_distmed_504d_base_v120_signal(eps, closeadj):
    base = eps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_distmed_126d_base_v121_signal(epsdil, closeadj):
    base = epsdil
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_distmed_252d_base_v122_signal(epsdil, closeadj):
    base = epsdil
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_distmed_504d_base_v123_signal(epsdil, closeadj):
    base = epsdil
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_distmed_126d_base_v124_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_distmed_252d_base_v125_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_distmed_504d_base_v126_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_distmed_126d_base_v127_signal(eps, closeadj):
    base = np.sign(eps)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_distmed_252d_base_v128_signal(eps, closeadj):
    base = np.sign(eps)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_distmed_504d_base_v129_signal(eps, closeadj):
    base = np.sign(eps)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_distmed_126d_base_v130_signal(epsusd, closeadj):
    base = epsusd
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_distmed_252d_base_v131_signal(epsusd, closeadj):
    base = epsusd
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_distmed_504d_base_v132_signal(epsusd, closeadj):
    base = epsusd
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_distmed_126d_base_v133_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_distmed_252d_base_v134_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_distmed_504d_base_v135_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_distmed_126d_base_v136_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_distmed_252d_base_v137_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_distmed_504d_base_v138_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_lvl
def f056eps_f056_eps_level_eps_lvl_chg_63d_base_v139_signal(eps, closeadj):
    base = eps
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_lvl
def f056eps_f056_eps_level_eps_lvl_chg_252d_base_v140_signal(eps, closeadj):
    base = eps
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_chg_63d_base_v141_signal(epsdil, closeadj):
    base = epsdil
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_chg_252d_base_v142_signal(epsdil, closeadj):
    base = epsdil
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_yield
def f056eps_f056_eps_level_eps_yield_chg_63d_base_v143_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_yield
def f056eps_f056_eps_level_eps_yield_chg_252d_base_v144_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_sign
def f056eps_f056_eps_level_eps_sign_chg_63d_base_v145_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_sign
def f056eps_f056_eps_level_eps_sign_chg_252d_base_v146_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_chg_63d_base_v147_signal(epsusd, closeadj):
    base = epsusd
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_chg_252d_base_v148_signal(epsusd, closeadj):
    base = epsusd
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_chg_63d_base_v149_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_chg_252d_base_v150_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

