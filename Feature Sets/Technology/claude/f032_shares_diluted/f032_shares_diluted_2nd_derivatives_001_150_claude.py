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


# 21d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slope_21d_2d_v001_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slope_63d_2d_v002_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slope_126d_2d_v003_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slope_252d_2d_v004_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_slope_504d_2d_v005_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slope_21d_2d_v006_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slope_63d_2d_v007_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slope_126d_2d_v008_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slope_252d_2d_v009_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_slope_504d_2d_v010_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slope_21d_2d_v011_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slope_63d_2d_v012_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slope_126d_2d_v013_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slope_252d_2d_v014_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_slope_504d_2d_v015_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slope_21d_2d_v016_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slope_63d_2d_v017_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slope_126d_2d_v018_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slope_252d_2d_v019_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_slope_504d_2d_v020_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slope_21d_2d_v021_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slope_63d_2d_v022_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slope_126d_2d_v023_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slope_252d_2d_v024_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_slope_504d_2d_v025_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slope_21d_2d_v026_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slope_63d_2d_v027_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slope_126d_2d_v028_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slope_252d_2d_v029_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_slope_504d_2d_v030_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slope_21d_2d_v031_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slope_63d_2d_v032_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slope_126d_2d_v033_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slope_252d_2d_v034_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_slope_504d_2d_v035_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sm21_sl21_2d_v036_signal(shareswa, closeadj):
    base = _mean(shareswa, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sm63_sl21_2d_v037_signal(shareswa, closeadj):
    base = _mean(shareswa, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sm63_sl63_2d_v038_signal(shareswa, closeadj):
    base = _mean(shareswa, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sm252_sl63_2d_v039_signal(shareswa, closeadj):
    base = _mean(shareswa, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sm252_sl126_2d_v040_signal(shareswa, closeadj):
    base = _mean(shareswa, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sm21_sl21_2d_v041_signal(shareswadil, closeadj):
    base = _mean(shareswadil, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sm63_sl21_2d_v042_signal(shareswadil, closeadj):
    base = _mean(shareswadil, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sm63_sl63_2d_v043_signal(shareswadil, closeadj):
    base = _mean(shareswadil, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sm252_sl63_2d_v044_signal(shareswadil, closeadj):
    base = _mean(shareswadil, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sm252_sl126_2d_v045_signal(shareswadil, closeadj):
    base = _mean(shareswadil, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sm21_sl21_2d_v046_signal(shareswadil, sharesbas, closeadj):
    base = _mean(_f032_dil_spread(shareswadil, sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sm63_sl21_2d_v047_signal(shareswadil, sharesbas, closeadj):
    base = _mean(_f032_dil_spread(shareswadil, sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sm63_sl63_2d_v048_signal(shareswadil, sharesbas, closeadj):
    base = _mean(_f032_dil_spread(shareswadil, sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sm252_sl63_2d_v049_signal(shareswadil, sharesbas, closeadj):
    base = _mean(_f032_dil_spread(shareswadil, sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sm252_sl126_2d_v050_signal(shareswadil, sharesbas, closeadj):
    base = _mean(_f032_dil_spread(shareswadil, sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sm21_sl21_2d_v051_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sm63_sl21_2d_v052_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sm63_sl63_2d_v053_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sm252_sl63_2d_v054_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sm252_sl126_2d_v055_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sm21_sl21_2d_v056_signal(shareswa, closeadj):
    base = _mean(shareswa.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sm63_sl21_2d_v057_signal(shareswa, closeadj):
    base = _mean(shareswa.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sm63_sl63_2d_v058_signal(shareswa, closeadj):
    base = _mean(shareswa.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sm252_sl63_2d_v059_signal(shareswa, closeadj):
    base = _mean(shareswa.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sm252_sl126_2d_v060_signal(shareswa, closeadj):
    base = _mean(shareswa.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sm21_sl21_2d_v061_signal(shareswadil, closeadj):
    base = _mean(shareswadil.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sm63_sl21_2d_v062_signal(shareswadil, closeadj):
    base = _mean(shareswadil.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sm63_sl63_2d_v063_signal(shareswadil, closeadj):
    base = _mean(shareswadil.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sm252_sl63_2d_v064_signal(shareswadil, closeadj):
    base = _mean(shareswadil.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sm252_sl126_2d_v065_signal(shareswadil, closeadj):
    base = _mean(shareswadil.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sm21_sl21_2d_v066_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil - sharesbas, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sm63_sl21_2d_v067_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil - sharesbas, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sm63_sl63_2d_v068_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil - sharesbas, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sm252_sl63_2d_v069_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil - sharesbas, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sm252_sl126_2d_v070_signal(shareswadil, sharesbas, closeadj):
    base = _mean(shareswadil - sharesbas, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_pctslope_21d_2d_v071_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_pctslope_63d_2d_v072_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_pctslope_252d_2d_v073_signal(shareswa, closeadj):
    base = shareswa
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_pctslope_21d_2d_v074_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_pctslope_63d_2d_v075_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_pctslope_252d_2d_v076_signal(shareswadil, closeadj):
    base = shareswadil
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_pctslope_21d_2d_v077_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_pctslope_63d_2d_v078_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_pctslope_252d_2d_v079_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_pctslope_21d_2d_v080_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_pctslope_63d_2d_v081_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_pctslope_252d_2d_v082_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_pctslope_21d_2d_v083_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_pctslope_63d_2d_v084_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_pctslope_252d_2d_v085_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_pctslope_21d_2d_v086_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_pctslope_63d_2d_v087_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_pctslope_252d_2d_v088_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_pctslope_21d_2d_v089_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_pctslope_63d_2d_v090_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_pctslope_252d_2d_v091_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sgnslope_21d_2d_v092_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sgnslope_63d_2d_v093_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_sgnslope_252d_2d_v094_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sgnslope_21d_2d_v095_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sgnslope_63d_2d_v096_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_sgnslope_252d_2d_v097_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sgnslope_21d_2d_v098_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sgnslope_63d_2d_v099_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_sgnslope_252d_2d_v100_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sgnslope_21d_2d_v101_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sgnslope_63d_2d_v102_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_sgnslope_252d_2d_v103_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sgnslope_21d_2d_v104_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sgnslope_63d_2d_v105_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_sgnslope_252d_2d_v106_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sgnslope_21d_2d_v107_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sgnslope_63d_2d_v108_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_sgnslope_252d_2d_v109_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sgnslope_21d_2d_v110_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sgnslope_63d_2d_v111_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_sgnslope_252d_2d_v112_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_logmagslope_21d_2d_v113_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_logmagslope_63d_2d_v114_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_logmagslope_252d_2d_v115_signal(shareswa, closeadj):
    base = shareswa
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_logmagslope_21d_2d_v116_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_logmagslope_63d_2d_v117_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_logmagslope_252d_2d_v118_signal(shareswadil, closeadj):
    base = shareswadil
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_logmagslope_21d_2d_v119_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_logmagslope_63d_2d_v120_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dil_spread
def f032shd_f032_shares_diluted_dil_spread_logmagslope_252d_2d_v121_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_logmagslope_21d_2d_v122_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_logmagslope_63d_2d_v123_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_logmagslope_252d_2d_v124_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_logmagslope_21d_2d_v125_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_logmagslope_63d_2d_v126_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_logmagslope_252d_2d_v127_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_logmagslope_21d_2d_v128_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_logmagslope_63d_2d_v129_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_logmagslope_252d_2d_v130_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_logmagslope_21d_2d_v131_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_logmagslope_63d_2d_v132_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_logmagslope_252d_2d_v133_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|shareswa_lvl|
def f032shd_f032_shares_diluted_shareswa_lvl_logslope_63d_2d_v134_signal(shareswa, closeadj):
    base = np.log((shareswa).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|shareswa_lvl|
def f032shd_f032_shares_diluted_shareswa_lvl_logslope_252d_2d_v135_signal(shareswa, closeadj):
    base = np.log((shareswa).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|shareswadil_lvl|
def f032shd_f032_shares_diluted_shareswadil_lvl_logslope_63d_2d_v136_signal(shareswadil, closeadj):
    base = np.log((shareswadil).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|shareswadil_lvl|
def f032shd_f032_shares_diluted_shareswadil_lvl_logslope_252d_2d_v137_signal(shareswadil, closeadj):
    base = np.log((shareswadil).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dil_spread|
def f032shd_f032_shares_diluted_dil_spread_logslope_63d_2d_v138_signal(shareswadil, sharesbas, closeadj):
    base = np.log((_f032_dil_spread(shareswadil, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dil_spread|
def f032shd_f032_shares_diluted_dil_spread_logslope_252d_2d_v139_signal(shareswadil, sharesbas, closeadj):
    base = np.log((_f032_dil_spread(shareswadil, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dilbasic_ratio|
def f032shd_f032_shares_diluted_dilbasic_ratio_logslope_63d_2d_v140_signal(shareswadil, sharesbas, closeadj):
    base = np.log((shareswadil / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dilbasic_ratio|
def f032shd_f032_shares_diluted_dilbasic_ratio_logslope_252d_2d_v141_signal(shareswadil, sharesbas, closeadj):
    base = np.log((shareswadil / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|shareswa_yoy|
def f032shd_f032_shares_diluted_shareswa_yoy_logslope_63d_2d_v142_signal(shareswa, closeadj):
    base = np.log((shareswa.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|shareswa_yoy|
def f032shd_f032_shares_diluted_shareswa_yoy_logslope_252d_2d_v143_signal(shareswa, closeadj):
    base = np.log((shareswa.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|shareswadil_yoy|
def f032shd_f032_shares_diluted_shareswadil_yoy_logslope_63d_2d_v144_signal(shareswadil, closeadj):
    base = np.log((shareswadil.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|shareswadil_yoy|
def f032shd_f032_shares_diluted_shareswadil_yoy_logslope_252d_2d_v145_signal(shareswadil, closeadj):
    base = np.log((shareswadil.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dilution_overhang|
def f032shd_f032_shares_diluted_dilution_overhang_logslope_63d_2d_v146_signal(shareswadil, sharesbas, closeadj):
    base = np.log((shareswadil - sharesbas).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dilution_overhang|
def f032shd_f032_shares_diluted_dilution_overhang_logslope_252d_2d_v147_signal(shareswadil, sharesbas, closeadj):
    base = np.log((shareswadil - sharesbas).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

