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
def _f032_dil_spread(shareswadil, sharesbas):
    return (shareswadil - sharesbas) / sharesbas.replace(0, np.nan).abs()


# 21d acceleration of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accel_21d_3d_v001_signal(shareswa, closeadj):
    base = shareswa
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accel_63d_3d_v002_signal(shareswa, closeadj):
    base = shareswa
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accel_126d_3d_v003_signal(shareswa, closeadj):
    base = shareswa
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accel_252d_3d_v004_signal(shareswa, closeadj):
    base = shareswa
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accel_21d_3d_v005_signal(shareswadil, closeadj):
    base = shareswadil
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accel_63d_3d_v006_signal(shareswadil, closeadj):
    base = shareswadil
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accel_126d_3d_v007_signal(shareswadil, closeadj):
    base = shareswadil
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accel_252d_3d_v008_signal(shareswadil, closeadj):
    base = shareswadil
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accel_21d_3d_v009_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accel_63d_3d_v010_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accel_126d_3d_v011_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accel_252d_3d_v012_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accel_21d_3d_v013_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accel_63d_3d_v014_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accel_126d_3d_v015_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accel_252d_3d_v016_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accel_21d_3d_v017_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accel_63d_3d_v018_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accel_126d_3d_v019_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accel_252d_3d_v020_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accel_21d_3d_v021_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accel_63d_3d_v022_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accel_126d_3d_v023_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accel_252d_3d_v024_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accel_21d_3d_v025_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accel_63d_3d_v026_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accel_126d_3d_v027_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accel_252d_3d_v028_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slopez_21d_z126_3d_v029_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slopez_63d_z252_3d_v030_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slopez_126d_z252_3d_v031_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slopez_252d_z504_3d_v032_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slopez_21d_z126_3d_v033_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slopez_63d_z252_3d_v034_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slopez_126d_z252_3d_v035_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slopez_252d_z504_3d_v036_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slopez_21d_z126_3d_v037_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slopez_63d_z252_3d_v038_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slopez_126d_z252_3d_v039_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slopez_252d_z504_3d_v040_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slopez_21d_z126_3d_v041_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slopez_63d_z252_3d_v042_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slopez_126d_z252_3d_v043_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slopez_252d_z504_3d_v044_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slopez_21d_z126_3d_v045_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slopez_63d_z252_3d_v046_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slopez_126d_z252_3d_v047_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slopez_252d_z504_3d_v048_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slopez_21d_z126_3d_v049_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slopez_63d_z252_3d_v050_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slopez_126d_z252_3d_v051_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slopez_252d_z504_3d_v052_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slopez_21d_z126_3d_v053_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slopez_63d_z252_3d_v054_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slopez_126d_z252_3d_v055_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slopez_252d_z504_3d_v056_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_jerk_21d_3d_v057_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_jerk_63d_3d_v058_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_jerk_126d_3d_v059_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_jerk_21d_3d_v060_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_jerk_63d_3d_v061_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_jerk_126d_3d_v062_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dil_spread
def f032shd_f032_shares_diluted_dil_spread_jerk_21d_3d_v063_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dil_spread
def f032shd_f032_shares_diluted_dil_spread_jerk_63d_3d_v064_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dil_spread
def f032shd_f032_shares_diluted_dil_spread_jerk_126d_3d_v065_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_jerk_21d_3d_v066_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_jerk_63d_3d_v067_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_jerk_126d_3d_v068_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_jerk_21d_3d_v069_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_jerk_63d_3d_v070_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_jerk_126d_3d_v071_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_jerk_21d_3d_v072_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_jerk_63d_3d_v073_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_jerk_126d_3d_v074_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_jerk_21d_3d_v075_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_jerk_63d_3d_v076_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_jerk_126d_3d_v077_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of shareswa_lvl smoothed over 252d
def f032shd_f032_shares_diluted_shareswa_lvl_smoothaccel_63d_sm252_3d_v078_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of shareswa_lvl smoothed over 504d
def f032shd_f032_shares_diluted_shareswa_lvl_smoothaccel_252d_sm504_3d_v079_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of shareswadil_lvl smoothed over 252d
def f032shd_f032_shares_diluted_shareswadil_lvl_smoothaccel_63d_sm252_3d_v080_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of shareswadil_lvl smoothed over 504d
def f032shd_f032_shares_diluted_shareswadil_lvl_smoothaccel_252d_sm504_3d_v081_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dil_spread smoothed over 252d
def f032shd_f032_shares_diluted_dil_spread_smoothaccel_63d_sm252_3d_v082_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dil_spread smoothed over 504d
def f032shd_f032_shares_diluted_dil_spread_smoothaccel_252d_sm504_3d_v083_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dilbasic_ratio smoothed over 252d
def f032shd_f032_shares_diluted_dilbasic_ratio_smoothaccel_63d_sm252_3d_v084_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dilbasic_ratio smoothed over 504d
def f032shd_f032_shares_diluted_dilbasic_ratio_smoothaccel_252d_sm504_3d_v085_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of shareswa_yoy smoothed over 252d
def f032shd_f032_shares_diluted_shareswa_yoy_smoothaccel_63d_sm252_3d_v086_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of shareswa_yoy smoothed over 504d
def f032shd_f032_shares_diluted_shareswa_yoy_smoothaccel_252d_sm504_3d_v087_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of shareswadil_yoy smoothed over 252d
def f032shd_f032_shares_diluted_shareswadil_yoy_smoothaccel_63d_sm252_3d_v088_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of shareswadil_yoy smoothed over 504d
def f032shd_f032_shares_diluted_shareswadil_yoy_smoothaccel_252d_sm504_3d_v089_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dilution_overhang smoothed over 252d
def f032shd_f032_shares_diluted_dilution_overhang_smoothaccel_63d_sm252_3d_v090_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dilution_overhang smoothed over 504d
def f032shd_f032_shares_diluted_dilution_overhang_smoothaccel_252d_sm504_3d_v091_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accelz_21d_z252_3d_v092_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_accelz_63d_z504_3d_v093_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accelz_21d_z252_3d_v094_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_accelz_63d_z504_3d_v095_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accelz_21d_z252_3d_v096_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dil_spread
def f032shd_f032_shares_diluted_dil_spread_accelz_63d_z504_3d_v097_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accelz_21d_z252_3d_v098_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_accelz_63d_z504_3d_v099_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accelz_21d_z252_3d_v100_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_accelz_63d_z504_3d_v101_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accelz_21d_z252_3d_v102_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_accelz_63d_z504_3d_v103_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accelz_21d_z252_3d_v104_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_accelz_63d_z504_3d_v105_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in shareswa_lvl (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswa_lvl_signflip_63d_3d_v106_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in shareswa_lvl (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswa_lvl_signflip_252d_3d_v107_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in shareswadil_lvl (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswadil_lvl_signflip_63d_3d_v108_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in shareswadil_lvl (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswadil_lvl_signflip_252d_3d_v109_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dil_spread (raw count, no price scaling)
def f032shd_f032_shares_diluted_dil_spread_signflip_63d_3d_v110_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dil_spread (raw count, no price scaling)
def f032shd_f032_shares_diluted_dil_spread_signflip_252d_3d_v111_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dilbasic_ratio (raw count, no price scaling)
def f032shd_f032_shares_diluted_dilbasic_ratio_signflip_63d_3d_v112_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dilbasic_ratio (raw count, no price scaling)
def f032shd_f032_shares_diluted_dilbasic_ratio_signflip_252d_3d_v113_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in shareswa_yoy (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswa_yoy_signflip_63d_3d_v114_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in shareswa_yoy (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswa_yoy_signflip_252d_3d_v115_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in shareswadil_yoy (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswadil_yoy_signflip_63d_3d_v116_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in shareswadil_yoy (raw count, no price scaling)
def f032shd_f032_shares_diluted_shareswadil_yoy_signflip_252d_3d_v117_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dilution_overhang (raw count, no price scaling)
def f032shd_f032_shares_diluted_dilution_overhang_signflip_63d_3d_v118_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dilution_overhang (raw count, no price scaling)
def f032shd_f032_shares_diluted_dilution_overhang_signflip_252d_3d_v119_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswa_lvl normalized by 252d range
def f032shd_f032_shares_diluted_shareswa_lvl_rngaccel_63d_r252_3d_v120_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswa_lvl normalized by 504d range
def f032shd_f032_shares_diluted_shareswa_lvl_rngaccel_252d_r504_3d_v121_signal(shareswa, closeadj):
    base = shareswa
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswadil_lvl normalized by 252d range
def f032shd_f032_shares_diluted_shareswadil_lvl_rngaccel_63d_r252_3d_v122_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswadil_lvl normalized by 504d range
def f032shd_f032_shares_diluted_shareswadil_lvl_rngaccel_252d_r504_3d_v123_signal(shareswadil, closeadj):
    base = shareswadil
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_spread normalized by 252d range
def f032shd_f032_shares_diluted_dil_spread_rngaccel_63d_r252_3d_v124_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_spread normalized by 504d range
def f032shd_f032_shares_diluted_dil_spread_rngaccel_252d_r504_3d_v125_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dilbasic_ratio normalized by 252d range
def f032shd_f032_shares_diluted_dilbasic_ratio_rngaccel_63d_r252_3d_v126_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dilbasic_ratio normalized by 504d range
def f032shd_f032_shares_diluted_dilbasic_ratio_rngaccel_252d_r504_3d_v127_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswa_yoy normalized by 252d range
def f032shd_f032_shares_diluted_shareswa_yoy_rngaccel_63d_r252_3d_v128_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswa_yoy normalized by 504d range
def f032shd_f032_shares_diluted_shareswa_yoy_rngaccel_252d_r504_3d_v129_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of shareswadil_yoy normalized by 252d range
def f032shd_f032_shares_diluted_shareswadil_yoy_rngaccel_63d_r252_3d_v130_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of shareswadil_yoy normalized by 504d range
def f032shd_f032_shares_diluted_shareswadil_yoy_rngaccel_252d_r504_3d_v131_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dilution_overhang normalized by 252d range
def f032shd_f032_shares_diluted_dilution_overhang_rngaccel_63d_r252_3d_v132_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dilution_overhang normalized by 504d range
def f032shd_f032_shares_diluted_dilution_overhang_rngaccel_252d_r504_3d_v133_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_cumslope_21d_3d_v134_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_cumslope_63d_3d_v135_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_cumslope_252d_3d_v136_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_cumslope_21d_3d_v137_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_cumslope_63d_3d_v138_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_cumslope_252d_3d_v139_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_cumslope_21d_3d_v140_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_cumslope_63d_3d_v141_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_cumslope_252d_3d_v142_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_cumslope_21d_3d_v143_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_cumslope_63d_3d_v144_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_cumslope_252d_3d_v145_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_cumslope_21d_3d_v146_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_cumslope_63d_3d_v147_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_cumslope_252d_3d_v148_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_cumslope_21d_3d_v149_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_cumslope_63d_3d_v150_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

