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
def _f056_eps_yield(eps, close):
    return eps / close.replace(0, np.nan).abs()


# 21d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slope_21d_2d_v001_signal(eps, closeadj):
    base = eps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slope_63d_2d_v002_signal(eps, closeadj):
    base = eps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slope_126d_2d_v003_signal(eps, closeadj):
    base = eps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slope_252d_2d_v004_signal(eps, closeadj):
    base = eps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slope_504d_2d_v005_signal(eps, closeadj):
    base = eps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slope_21d_2d_v006_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slope_63d_2d_v007_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slope_126d_2d_v008_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slope_252d_2d_v009_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slope_504d_2d_v010_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_slope_21d_2d_v011_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_slope_63d_2d_v012_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_slope_126d_2d_v013_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_slope_252d_2d_v014_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_slope_504d_2d_v015_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_slope_21d_2d_v016_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_slope_63d_2d_v017_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_slope_126d_2d_v018_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_slope_252d_2d_v019_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_slope_504d_2d_v020_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slope_21d_2d_v021_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slope_63d_2d_v022_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slope_126d_2d_v023_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slope_252d_2d_v024_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slope_504d_2d_v025_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slope_21d_2d_v026_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slope_63d_2d_v027_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slope_126d_2d_v028_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slope_252d_2d_v029_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slope_504d_2d_v030_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slope_21d_2d_v031_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slope_63d_2d_v032_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slope_126d_2d_v033_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slope_252d_2d_v034_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slope_504d_2d_v035_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sm21_sl21_2d_v036_signal(eps, closeadj):
    base = _mean(eps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sm63_sl21_2d_v037_signal(eps, closeadj):
    base = _mean(eps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sm63_sl63_2d_v038_signal(eps, closeadj):
    base = _mean(eps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sm252_sl63_2d_v039_signal(eps, closeadj):
    base = _mean(eps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sm252_sl126_2d_v040_signal(eps, closeadj):
    base = _mean(eps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sm21_sl21_2d_v041_signal(epsdil, closeadj):
    base = _mean(epsdil, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sm63_sl21_2d_v042_signal(epsdil, closeadj):
    base = _mean(epsdil, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sm63_sl63_2d_v043_signal(epsdil, closeadj):
    base = _mean(epsdil, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sm252_sl63_2d_v044_signal(epsdil, closeadj):
    base = _mean(epsdil, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sm252_sl126_2d_v045_signal(epsdil, closeadj):
    base = _mean(epsdil, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sm21_sl21_2d_v046_signal(eps, close, closeadj):
    base = _mean(_f056_eps_yield(eps, close), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sm63_sl21_2d_v047_signal(eps, close, closeadj):
    base = _mean(_f056_eps_yield(eps, close), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sm63_sl63_2d_v048_signal(eps, close, closeadj):
    base = _mean(_f056_eps_yield(eps, close), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sm252_sl63_2d_v049_signal(eps, close, closeadj):
    base = _mean(_f056_eps_yield(eps, close), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sm252_sl126_2d_v050_signal(eps, close, closeadj):
    base = _mean(_f056_eps_yield(eps, close), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sm21_sl21_2d_v051_signal(eps, closeadj):
    base = _mean(np.sign(eps), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sm63_sl21_2d_v052_signal(eps, closeadj):
    base = _mean(np.sign(eps), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sm63_sl63_2d_v053_signal(eps, closeadj):
    base = _mean(np.sign(eps), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sm252_sl63_2d_v054_signal(eps, closeadj):
    base = _mean(np.sign(eps), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sm252_sl126_2d_v055_signal(eps, closeadj):
    base = _mean(np.sign(eps), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sm21_sl21_2d_v056_signal(epsusd, closeadj):
    base = _mean(epsusd, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sm63_sl21_2d_v057_signal(epsusd, closeadj):
    base = _mean(epsusd, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sm63_sl63_2d_v058_signal(epsusd, closeadj):
    base = _mean(epsusd, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sm252_sl63_2d_v059_signal(epsusd, closeadj):
    base = _mean(epsusd, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sm252_sl126_2d_v060_signal(epsusd, closeadj):
    base = _mean(epsusd, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sm21_sl21_2d_v061_signal(epsdil, eps, closeadj):
    base = _mean(epsdil - eps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sm63_sl21_2d_v062_signal(epsdil, eps, closeadj):
    base = _mean(epsdil - eps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sm63_sl63_2d_v063_signal(epsdil, eps, closeadj):
    base = _mean(epsdil - eps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sm252_sl63_2d_v064_signal(epsdil, eps, closeadj):
    base = _mean(epsdil - eps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sm252_sl126_2d_v065_signal(epsdil, eps, closeadj):
    base = _mean(epsdil - eps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sm21_sl21_2d_v066_signal(netinc, sharesbas, closeadj):
    base = _mean(netinc / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sm63_sl21_2d_v067_signal(netinc, sharesbas, closeadj):
    base = _mean(netinc / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sm63_sl63_2d_v068_signal(netinc, sharesbas, closeadj):
    base = _mean(netinc / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sm252_sl63_2d_v069_signal(netinc, sharesbas, closeadj):
    base = _mean(netinc / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sm252_sl126_2d_v070_signal(netinc, sharesbas, closeadj):
    base = _mean(netinc / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_pctslope_21d_2d_v071_signal(eps, closeadj):
    base = eps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_pctslope_63d_2d_v072_signal(eps, closeadj):
    base = eps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_pctslope_252d_2d_v073_signal(eps, closeadj):
    base = eps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_pctslope_21d_2d_v074_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_pctslope_63d_2d_v075_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_pctslope_252d_2d_v076_signal(epsdil, closeadj):
    base = epsdil
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_yield
def f056eps_f056_eps_level_eps_yield_pctslope_21d_2d_v077_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_yield
def f056eps_f056_eps_level_eps_yield_pctslope_63d_2d_v078_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_yield
def f056eps_f056_eps_level_eps_yield_pctslope_252d_2d_v079_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_sign
def f056eps_f056_eps_level_eps_sign_pctslope_21d_2d_v080_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_sign
def f056eps_f056_eps_level_eps_sign_pctslope_63d_2d_v081_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_sign
def f056eps_f056_eps_level_eps_sign_pctslope_252d_2d_v082_signal(eps, closeadj):
    base = np.sign(eps)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_pctslope_21d_2d_v083_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_pctslope_63d_2d_v084_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_pctslope_252d_2d_v085_signal(epsusd, closeadj):
    base = epsusd
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_pctslope_21d_2d_v086_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_pctslope_63d_2d_v087_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_pctslope_252d_2d_v088_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_pctslope_21d_2d_v089_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_pctslope_63d_2d_v090_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_pctslope_252d_2d_v091_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sgnslope_21d_2d_v092_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sgnslope_63d_2d_v093_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_sgnslope_252d_2d_v094_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sgnslope_21d_2d_v095_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sgnslope_63d_2d_v096_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_sgnslope_252d_2d_v097_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sgnslope_21d_2d_v098_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sgnslope_63d_2d_v099_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_sgnslope_252d_2d_v100_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sgnslope_21d_2d_v101_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sgnslope_63d_2d_v102_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_sgnslope_252d_2d_v103_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sgnslope_21d_2d_v104_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sgnslope_63d_2d_v105_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_sgnslope_252d_2d_v106_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sgnslope_21d_2d_v107_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sgnslope_63d_2d_v108_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_sgnslope_252d_2d_v109_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sgnslope_21d_2d_v110_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sgnslope_63d_2d_v111_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_sgnslope_252d_2d_v112_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_logmagslope_21d_2d_v113_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_logmagslope_63d_2d_v114_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_logmagslope_252d_2d_v115_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_logmagslope_21d_2d_v116_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_logmagslope_63d_2d_v117_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_logmagslope_252d_2d_v118_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_logmagslope_21d_2d_v119_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_logmagslope_63d_2d_v120_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_yield
def f056eps_f056_eps_level_eps_yield_logmagslope_252d_2d_v121_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_logmagslope_21d_2d_v122_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_logmagslope_63d_2d_v123_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_sign
def f056eps_f056_eps_level_eps_sign_logmagslope_252d_2d_v124_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_logmagslope_21d_2d_v125_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_logmagslope_63d_2d_v126_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_logmagslope_252d_2d_v127_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_logmagslope_21d_2d_v128_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_logmagslope_63d_2d_v129_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_logmagslope_252d_2d_v130_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_logmagslope_21d_2d_v131_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_logmagslope_63d_2d_v132_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_logmagslope_252d_2d_v133_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_lvl|
def f056eps_f056_eps_level_eps_lvl_logslope_63d_2d_v134_signal(eps, closeadj):
    base = np.log((eps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_lvl|
def f056eps_f056_eps_level_eps_lvl_logslope_252d_2d_v135_signal(eps, closeadj):
    base = np.log((eps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|epsdil_lvl|
def f056eps_f056_eps_level_epsdil_lvl_logslope_63d_2d_v136_signal(epsdil, closeadj):
    base = np.log((epsdil).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|epsdil_lvl|
def f056eps_f056_eps_level_epsdil_lvl_logslope_252d_2d_v137_signal(epsdil, closeadj):
    base = np.log((epsdil).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_yield|
def f056eps_f056_eps_level_eps_yield_logslope_63d_2d_v138_signal(eps, close, closeadj):
    base = np.log((_f056_eps_yield(eps, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_yield|
def f056eps_f056_eps_level_eps_yield_logslope_252d_2d_v139_signal(eps, close, closeadj):
    base = np.log((_f056_eps_yield(eps, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_sign|
def f056eps_f056_eps_level_eps_sign_logslope_63d_2d_v140_signal(eps, closeadj):
    base = np.log((np.sign(eps)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_sign|
def f056eps_f056_eps_level_eps_sign_logslope_252d_2d_v141_signal(eps, closeadj):
    base = np.log((np.sign(eps)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|epsusd_lvl|
def f056eps_f056_eps_level_epsusd_lvl_logslope_63d_2d_v142_signal(epsusd, closeadj):
    base = np.log((epsusd).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|epsusd_lvl|
def f056eps_f056_eps_level_epsusd_lvl_logslope_252d_2d_v143_signal(epsusd, closeadj):
    base = np.log((epsusd).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dil_spread_eps|
def f056eps_f056_eps_level_dil_spread_eps_logslope_63d_2d_v144_signal(epsdil, eps, closeadj):
    base = np.log((epsdil - eps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dil_spread_eps|
def f056eps_f056_eps_level_dil_spread_eps_logslope_252d_2d_v145_signal(epsdil, eps, closeadj):
    base = np.log((epsdil - eps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ni_per_share_calc|
def f056eps_f056_eps_level_ni_per_share_calc_logslope_63d_2d_v146_signal(netinc, sharesbas, closeadj):
    base = np.log((netinc / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ni_per_share_calc|
def f056eps_f056_eps_level_ni_per_share_calc_logslope_252d_2d_v147_signal(netinc, sharesbas, closeadj):
    base = np.log((netinc / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

