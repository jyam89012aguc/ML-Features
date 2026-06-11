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


# 21d acceleration of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accel_21d_3d_v001_signal(eps, closeadj):
    base = eps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accel_63d_3d_v002_signal(eps, closeadj):
    base = eps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accel_126d_3d_v003_signal(eps, closeadj):
    base = eps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accel_252d_3d_v004_signal(eps, closeadj):
    base = eps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accel_21d_3d_v005_signal(epsdil, closeadj):
    base = epsdil
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accel_63d_3d_v006_signal(epsdil, closeadj):
    base = epsdil
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accel_126d_3d_v007_signal(epsdil, closeadj):
    base = epsdil
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accel_252d_3d_v008_signal(epsdil, closeadj):
    base = epsdil
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_yield
def f056eps_f056_eps_level_eps_yield_accel_21d_3d_v009_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_yield
def f056eps_f056_eps_level_eps_yield_accel_63d_3d_v010_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_yield
def f056eps_f056_eps_level_eps_yield_accel_126d_3d_v011_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_yield
def f056eps_f056_eps_level_eps_yield_accel_252d_3d_v012_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_sign
def f056eps_f056_eps_level_eps_sign_accel_21d_3d_v013_signal(eps, closeadj):
    base = np.sign(eps)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_sign
def f056eps_f056_eps_level_eps_sign_accel_63d_3d_v014_signal(eps, closeadj):
    base = np.sign(eps)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_sign
def f056eps_f056_eps_level_eps_sign_accel_126d_3d_v015_signal(eps, closeadj):
    base = np.sign(eps)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_sign
def f056eps_f056_eps_level_eps_sign_accel_252d_3d_v016_signal(eps, closeadj):
    base = np.sign(eps)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accel_21d_3d_v017_signal(epsusd, closeadj):
    base = epsusd
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accel_63d_3d_v018_signal(epsusd, closeadj):
    base = epsusd
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accel_126d_3d_v019_signal(epsusd, closeadj):
    base = epsusd
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accel_252d_3d_v020_signal(epsusd, closeadj):
    base = epsusd
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accel_21d_3d_v021_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accel_63d_3d_v022_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accel_126d_3d_v023_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accel_252d_3d_v024_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accel_21d_3d_v025_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accel_63d_3d_v026_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accel_126d_3d_v027_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accel_252d_3d_v028_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slopez_21d_z126_3d_v029_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slopez_63d_z252_3d_v030_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slopez_126d_z252_3d_v031_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_slopez_252d_z504_3d_v032_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slopez_21d_z126_3d_v033_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slopez_63d_z252_3d_v034_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slopez_126d_z252_3d_v035_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_slopez_252d_z504_3d_v036_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_yield
def f056eps_f056_eps_level_eps_yield_slopez_21d_z126_3d_v037_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_yield
def f056eps_f056_eps_level_eps_yield_slopez_63d_z252_3d_v038_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_yield
def f056eps_f056_eps_level_eps_yield_slopez_126d_z252_3d_v039_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_yield
def f056eps_f056_eps_level_eps_yield_slopez_252d_z504_3d_v040_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_sign
def f056eps_f056_eps_level_eps_sign_slopez_21d_z126_3d_v041_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_sign
def f056eps_f056_eps_level_eps_sign_slopez_63d_z252_3d_v042_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_sign
def f056eps_f056_eps_level_eps_sign_slopez_126d_z252_3d_v043_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_sign
def f056eps_f056_eps_level_eps_sign_slopez_252d_z504_3d_v044_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slopez_21d_z126_3d_v045_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slopez_63d_z252_3d_v046_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slopez_126d_z252_3d_v047_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_slopez_252d_z504_3d_v048_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slopez_21d_z126_3d_v049_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slopez_63d_z252_3d_v050_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slopez_126d_z252_3d_v051_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_slopez_252d_z504_3d_v052_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slopez_21d_z126_3d_v053_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slopez_63d_z252_3d_v054_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slopez_126d_z252_3d_v055_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_slopez_252d_z504_3d_v056_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_lvl
def f056eps_f056_eps_level_eps_lvl_jerk_21d_3d_v057_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_lvl
def f056eps_f056_eps_level_eps_lvl_jerk_63d_3d_v058_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_lvl
def f056eps_f056_eps_level_eps_lvl_jerk_126d_3d_v059_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_jerk_21d_3d_v060_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_jerk_63d_3d_v061_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_jerk_126d_3d_v062_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_yield
def f056eps_f056_eps_level_eps_yield_jerk_21d_3d_v063_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_yield
def f056eps_f056_eps_level_eps_yield_jerk_63d_3d_v064_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_yield
def f056eps_f056_eps_level_eps_yield_jerk_126d_3d_v065_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_sign
def f056eps_f056_eps_level_eps_sign_jerk_21d_3d_v066_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_sign
def f056eps_f056_eps_level_eps_sign_jerk_63d_3d_v067_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_sign
def f056eps_f056_eps_level_eps_sign_jerk_126d_3d_v068_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_jerk_21d_3d_v069_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_jerk_63d_3d_v070_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_jerk_126d_3d_v071_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_jerk_21d_3d_v072_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_jerk_63d_3d_v073_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_jerk_126d_3d_v074_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_jerk_21d_3d_v075_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_jerk_63d_3d_v076_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_jerk_126d_3d_v077_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_lvl smoothed over 252d
def f056eps_f056_eps_level_eps_lvl_smoothaccel_63d_sm252_3d_v078_signal(eps, closeadj):
    base = eps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_lvl smoothed over 504d
def f056eps_f056_eps_level_eps_lvl_smoothaccel_252d_sm504_3d_v079_signal(eps, closeadj):
    base = eps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of epsdil_lvl smoothed over 252d
def f056eps_f056_eps_level_epsdil_lvl_smoothaccel_63d_sm252_3d_v080_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of epsdil_lvl smoothed over 504d
def f056eps_f056_eps_level_epsdil_lvl_smoothaccel_252d_sm504_3d_v081_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_yield smoothed over 252d
def f056eps_f056_eps_level_eps_yield_smoothaccel_63d_sm252_3d_v082_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_yield smoothed over 504d
def f056eps_f056_eps_level_eps_yield_smoothaccel_252d_sm504_3d_v083_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_sign smoothed over 252d
def f056eps_f056_eps_level_eps_sign_smoothaccel_63d_sm252_3d_v084_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_sign smoothed over 504d
def f056eps_f056_eps_level_eps_sign_smoothaccel_252d_sm504_3d_v085_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of epsusd_lvl smoothed over 252d
def f056eps_f056_eps_level_epsusd_lvl_smoothaccel_63d_sm252_3d_v086_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of epsusd_lvl smoothed over 504d
def f056eps_f056_eps_level_epsusd_lvl_smoothaccel_252d_sm504_3d_v087_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dil_spread_eps smoothed over 252d
def f056eps_f056_eps_level_dil_spread_eps_smoothaccel_63d_sm252_3d_v088_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dil_spread_eps smoothed over 504d
def f056eps_f056_eps_level_dil_spread_eps_smoothaccel_252d_sm504_3d_v089_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_per_share_calc smoothed over 252d
def f056eps_f056_eps_level_ni_per_share_calc_smoothaccel_63d_sm252_3d_v090_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_per_share_calc smoothed over 504d
def f056eps_f056_eps_level_ni_per_share_calc_smoothaccel_252d_sm504_3d_v091_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accelz_21d_z252_3d_v092_signal(eps, closeadj):
    base = eps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_lvl
def f056eps_f056_eps_level_eps_lvl_accelz_63d_z504_3d_v093_signal(eps, closeadj):
    base = eps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accelz_21d_z252_3d_v094_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_accelz_63d_z504_3d_v095_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_yield
def f056eps_f056_eps_level_eps_yield_accelz_21d_z252_3d_v096_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_yield
def f056eps_f056_eps_level_eps_yield_accelz_63d_z504_3d_v097_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_sign
def f056eps_f056_eps_level_eps_sign_accelz_21d_z252_3d_v098_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_sign
def f056eps_f056_eps_level_eps_sign_accelz_63d_z504_3d_v099_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accelz_21d_z252_3d_v100_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_accelz_63d_z504_3d_v101_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accelz_21d_z252_3d_v102_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_accelz_63d_z504_3d_v103_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accelz_21d_z252_3d_v104_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_per_share_calc
def f056eps_f056_eps_level_ni_per_share_calc_accelz_63d_z504_3d_v105_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_eps_lvl_signflip_63d_3d_v106_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_eps_lvl_signflip_252d_3d_v107_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in epsdil_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_epsdil_lvl_signflip_63d_3d_v108_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in epsdil_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_epsdil_lvl_signflip_252d_3d_v109_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_yield (raw count, no price scaling)
def f056eps_f056_eps_level_eps_yield_signflip_63d_3d_v110_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_yield (raw count, no price scaling)
def f056eps_f056_eps_level_eps_yield_signflip_252d_3d_v111_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_sign (raw count, no price scaling)
def f056eps_f056_eps_level_eps_sign_signflip_63d_3d_v112_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_sign (raw count, no price scaling)
def f056eps_f056_eps_level_eps_sign_signflip_252d_3d_v113_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in epsusd_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_epsusd_lvl_signflip_63d_3d_v114_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in epsusd_lvl (raw count, no price scaling)
def f056eps_f056_eps_level_epsusd_lvl_signflip_252d_3d_v115_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dil_spread_eps (raw count, no price scaling)
def f056eps_f056_eps_level_dil_spread_eps_signflip_63d_3d_v116_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dil_spread_eps (raw count, no price scaling)
def f056eps_f056_eps_level_dil_spread_eps_signflip_252d_3d_v117_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ni_per_share_calc (raw count, no price scaling)
def f056eps_f056_eps_level_ni_per_share_calc_signflip_63d_3d_v118_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ni_per_share_calc (raw count, no price scaling)
def f056eps_f056_eps_level_ni_per_share_calc_signflip_252d_3d_v119_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_lvl normalized by 252d range
def f056eps_f056_eps_level_eps_lvl_rngaccel_63d_r252_3d_v120_signal(eps, closeadj):
    base = eps
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_lvl normalized by 504d range
def f056eps_f056_eps_level_eps_lvl_rngaccel_252d_r504_3d_v121_signal(eps, closeadj):
    base = eps
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsdil_lvl normalized by 252d range
def f056eps_f056_eps_level_epsdil_lvl_rngaccel_63d_r252_3d_v122_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsdil_lvl normalized by 504d range
def f056eps_f056_eps_level_epsdil_lvl_rngaccel_252d_r504_3d_v123_signal(epsdil, closeadj):
    base = epsdil
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_yield normalized by 252d range
def f056eps_f056_eps_level_eps_yield_rngaccel_63d_r252_3d_v124_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_yield normalized by 504d range
def f056eps_f056_eps_level_eps_yield_rngaccel_252d_r504_3d_v125_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_sign normalized by 252d range
def f056eps_f056_eps_level_eps_sign_rngaccel_63d_r252_3d_v126_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_sign normalized by 504d range
def f056eps_f056_eps_level_eps_sign_rngaccel_252d_r504_3d_v127_signal(eps, closeadj):
    base = np.sign(eps)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsusd_lvl normalized by 252d range
def f056eps_f056_eps_level_epsusd_lvl_rngaccel_63d_r252_3d_v128_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsusd_lvl normalized by 504d range
def f056eps_f056_eps_level_epsusd_lvl_rngaccel_252d_r504_3d_v129_signal(epsusd, closeadj):
    base = epsusd
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_spread_eps normalized by 252d range
def f056eps_f056_eps_level_dil_spread_eps_rngaccel_63d_r252_3d_v130_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_spread_eps normalized by 504d range
def f056eps_f056_eps_level_dil_spread_eps_rngaccel_252d_r504_3d_v131_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_per_share_calc normalized by 252d range
def f056eps_f056_eps_level_ni_per_share_calc_rngaccel_63d_r252_3d_v132_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_per_share_calc normalized by 504d range
def f056eps_f056_eps_level_ni_per_share_calc_rngaccel_252d_r504_3d_v133_signal(netinc, sharesbas, closeadj):
    base = netinc / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_cumslope_21d_3d_v134_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_cumslope_63d_3d_v135_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_lvl
def f056eps_f056_eps_level_eps_lvl_cumslope_252d_3d_v136_signal(eps, closeadj):
    base = eps
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_cumslope_21d_3d_v137_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_cumslope_63d_3d_v138_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of epsdil_lvl
def f056eps_f056_eps_level_epsdil_lvl_cumslope_252d_3d_v139_signal(epsdil, closeadj):
    base = epsdil
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_yield
def f056eps_f056_eps_level_eps_yield_cumslope_21d_3d_v140_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_yield
def f056eps_f056_eps_level_eps_yield_cumslope_63d_3d_v141_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_yield
def f056eps_f056_eps_level_eps_yield_cumslope_252d_3d_v142_signal(eps, close, closeadj):
    base = _f056_eps_yield(eps, close)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_sign
def f056eps_f056_eps_level_eps_sign_cumslope_21d_3d_v143_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_sign
def f056eps_f056_eps_level_eps_sign_cumslope_63d_3d_v144_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_sign
def f056eps_f056_eps_level_eps_sign_cumslope_252d_3d_v145_signal(eps, closeadj):
    base = np.sign(eps)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_cumslope_21d_3d_v146_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_cumslope_63d_3d_v147_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of epsusd_lvl
def f056eps_f056_eps_level_epsusd_lvl_cumslope_252d_3d_v148_signal(epsusd, closeadj):
    base = epsusd
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_cumslope_21d_3d_v149_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dil_spread_eps
def f056eps_f056_eps_level_dil_spread_eps_cumslope_63d_3d_v150_signal(epsdil, eps, closeadj):
    base = epsdil - eps
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

