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


# 21d mean of eps_lvl scaled by closeadj
def f056eps_f056_eps_level_eps_lvl_mean_21d_base_v001_signal(eps, closeadj):
    base = eps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_lvl scaled by closeadj
def f056eps_f056_eps_level_eps_lvl_mean_63d_base_v002_signal(eps, closeadj):
    base = eps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_lvl scaled by closeadj
def f056eps_f056_eps_level_eps_lvl_mean_126d_base_v003_signal(eps, closeadj):
    base = eps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_lvl scaled by closeadj
def f056eps_f056_eps_level_eps_lvl_mean_252d_base_v004_signal(eps, closeadj):
    base = eps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_lvl scaled by closeadj
def f056eps_f056_eps_level_eps_lvl_mean_504d_base_v005_signal(eps, closeadj):
    base = eps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of epsdil_lvl scaled by closeadj
def f056eps_f056_eps_level_epsdil_lvl_mean_21d_base_v006_signal(epsdil, closeadj):
    base = epsdil
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of epsdil_lvl scaled by closeadj
def f056eps_f056_eps_level_epsdil_lvl_mean_63d_base_v007_signal(epsdil, closeadj):
    base = epsdil
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of epsdil_lvl scaled by closeadj
def f056eps_f056_eps_level_epsdil_lvl_mean_126d_base_v008_signal(epsdil, closeadj):
    base = epsdil
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of epsdil_lvl scaled by closeadj
def f056eps_f056_eps_level_epsdil_lvl_mean_252d_base_v009_signal(epsdil, closeadj):
    base = epsdil
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of epsdil_lvl scaled by closeadj
def f056eps_f056_eps_level_epsdil_lvl_mean_504d_base_v010_signal(epsdil, closeadj):
    base = epsdil
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_yield scaled by closeadj
def f056eps_f056_eps_level_eps_yield_mean_21d_base_v011_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_yield scaled by closeadj
def f056eps_f056_eps_level_eps_yield_mean_63d_base_v012_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_yield scaled by closeadj
def f056eps_f056_eps_level_eps_yield_mean_126d_base_v013_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_yield scaled by closeadj
def f056eps_f056_eps_level_eps_yield_mean_252d_base_v014_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_yield scaled by closeadj
def f056eps_f056_eps_level_eps_yield_mean_504d_base_v015_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_sign scaled by closeadj
def f056eps_f056_eps_level_eps_sign_mean_21d_base_v016_signal(eps, closeadj):
    base = np.sign(eps)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_sign scaled by closeadj
def f056eps_f056_eps_level_eps_sign_mean_63d_base_v017_signal(eps, closeadj):
    base = np.sign(eps)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_sign scaled by closeadj
def f056eps_f056_eps_level_eps_sign_mean_126d_base_v018_signal(eps, closeadj):
    base = np.sign(eps)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_sign scaled by closeadj
def f056eps_f056_eps_level_eps_sign_mean_252d_base_v019_signal(eps, closeadj):
    base = np.sign(eps)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_sign scaled by closeadj
def f056eps_f056_eps_level_eps_sign_mean_504d_base_v020_signal(eps, closeadj):
    base = np.sign(eps)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of epsusd_lvl scaled by closeadj
def f056eps_f056_eps_level_epsusd_lvl_mean_21d_base_v021_signal(epsusd, closeadj):
    base = epsusd
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of epsusd_lvl scaled by closeadj
def f056eps_f056_eps_level_epsusd_lvl_mean_63d_base_v022_signal(epsusd, closeadj):
    base = epsusd
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of epsusd_lvl scaled by closeadj
def f056eps_f056_eps_level_epsusd_lvl_mean_126d_base_v023_signal(epsusd, closeadj):
    base = epsusd
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of epsusd_lvl scaled by closeadj
def f056eps_f056_eps_level_epsusd_lvl_mean_252d_base_v024_signal(epsusd, closeadj):
    base = epsusd
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of epsusd_lvl scaled by closeadj
def f056eps_f056_eps_level_epsusd_lvl_mean_504d_base_v025_signal(epsusd, closeadj):
    base = epsusd
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dil_spread_eps scaled by closeadj
def f056eps_f056_eps_level_dil_spread_eps_mean_21d_base_v026_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dil_spread_eps scaled by closeadj
def f056eps_f056_eps_level_dil_spread_eps_mean_63d_base_v027_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dil_spread_eps scaled by closeadj
def f056eps_f056_eps_level_dil_spread_eps_mean_126d_base_v028_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dil_spread_eps scaled by closeadj
def f056eps_f056_eps_level_dil_spread_eps_mean_252d_base_v029_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dil_spread_eps scaled by closeadj
def f056eps_f056_eps_level_dil_spread_eps_mean_504d_base_v030_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ni_per_share_calc scaled by closeadj
def f056eps_f056_eps_level_ni_per_share_calc_mean_21d_base_v031_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ni_per_share_calc scaled by closeadj
def f056eps_f056_eps_level_ni_per_share_calc_mean_63d_base_v032_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ni_per_share_calc scaled by closeadj
def f056eps_f056_eps_level_ni_per_share_calc_mean_126d_base_v033_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ni_per_share_calc scaled by closeadj
def f056eps_f056_eps_level_ni_per_share_calc_mean_252d_base_v034_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ni_per_share_calc scaled by closeadj
def f056eps_f056_eps_level_ni_per_share_calc_mean_504d_base_v035_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_median_63d_base_v036_signal(eps, closeadj):
    base = eps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_median_252d_base_v037_signal(eps, closeadj):
    base = eps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_lvl
def f056eps_f056_eps_level_eps_lvl_median_504d_base_v038_signal(eps, closeadj):
    base = eps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_median_63d_base_v039_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_median_252d_base_v040_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_median_504d_base_v041_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_median_63d_base_v042_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_median_252d_base_v043_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_yield
def f056eps_f056_eps_level_eps_yield_median_504d_base_v044_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_median_63d_base_v045_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_median_252d_base_v046_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_sign
def f056eps_f056_eps_level_eps_sign_median_504d_base_v047_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_median_63d_base_v048_signal(epsusd, closeadj):
    base = epsusd
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_median_252d_base_v049_signal(epsusd, closeadj):
    base = epsusd
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_median_504d_base_v050_signal(epsusd, closeadj):
    base = epsusd
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_median_63d_base_v051_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_median_252d_base_v052_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_median_504d_base_v053_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_median_63d_base_v054_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_median_252d_base_v055_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_median_504d_base_v056_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_lvl
def f056eps_f056_eps_level_eps_lvl_rmax_252d_base_v057_signal(eps, closeadj):
    base = eps
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_lvl
def f056eps_f056_eps_level_eps_lvl_rmax_504d_base_v058_signal(eps, closeadj):
    base = eps
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_rmax_252d_base_v059_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_rmax_504d_base_v060_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_yield
def f056eps_f056_eps_level_eps_yield_rmax_252d_base_v061_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_yield
def f056eps_f056_eps_level_eps_yield_rmax_504d_base_v062_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_sign
def f056eps_f056_eps_level_eps_sign_rmax_252d_base_v063_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_sign
def f056eps_f056_eps_level_eps_sign_rmax_504d_base_v064_signal(eps, closeadj):
    base = np.sign(eps)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_rmax_252d_base_v065_signal(epsusd, closeadj):
    base = epsusd
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_rmax_504d_base_v066_signal(epsusd, closeadj):
    base = epsusd
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_rmax_252d_base_v067_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_rmax_504d_base_v068_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_rmax_252d_base_v069_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_rmax_504d_base_v070_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eps_lvl
def f056eps_f056_eps_level_eps_lvl_rmin_252d_base_v071_signal(eps, closeadj):
    base = eps
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of eps_lvl
def f056eps_f056_eps_level_eps_lvl_rmin_504d_base_v072_signal(eps, closeadj):
    base = eps
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_rmin_252d_base_v073_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_rmin_504d_base_v074_signal(epsdil, closeadj):
    base = epsdil
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eps_yield
def f056eps_f056_eps_level_eps_yield_rmin_252d_base_v075_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

