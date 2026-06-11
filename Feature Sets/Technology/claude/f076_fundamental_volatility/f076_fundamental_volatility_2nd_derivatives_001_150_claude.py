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
def _f076_vol(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std()


# 21d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slope_21d_2d_v001_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slope_63d_2d_v002_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slope_126d_2d_v003_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slope_252d_2d_v004_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slope_504d_2d_v005_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slope_21d_2d_v006_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slope_63d_2d_v007_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slope_126d_2d_v008_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slope_252d_2d_v009_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slope_504d_2d_v010_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slope_21d_2d_v011_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slope_63d_2d_v012_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slope_126d_2d_v013_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slope_252d_2d_v014_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slope_504d_2d_v015_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slope_21d_2d_v016_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slope_63d_2d_v017_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slope_126d_2d_v018_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slope_252d_2d_v019_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slope_504d_2d_v020_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slope_21d_2d_v021_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slope_63d_2d_v022_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slope_126d_2d_v023_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slope_252d_2d_v024_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slope_504d_2d_v025_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slope_21d_2d_v026_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slope_63d_2d_v027_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slope_126d_2d_v028_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slope_252d_2d_v029_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slope_504d_2d_v030_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slope_21d_2d_v031_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slope_63d_2d_v032_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slope_126d_2d_v033_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slope_252d_2d_v034_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slope_504d_2d_v035_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sm21_sl21_2d_v036_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sm63_sl21_2d_v037_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sm63_sl63_2d_v038_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sm252_sl63_2d_v039_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sm252_sl126_2d_v040_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sm21_sl21_2d_v041_signal(ncfo, closeadj):
    base = _mean(_f076_vol(ncfo, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sm63_sl21_2d_v042_signal(ncfo, closeadj):
    base = _mean(_f076_vol(ncfo, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sm63_sl63_2d_v043_signal(ncfo, closeadj):
    base = _mean(_f076_vol(ncfo, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sm252_sl63_2d_v044_signal(ncfo, closeadj):
    base = _mean(_f076_vol(ncfo, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sm252_sl126_2d_v045_signal(ncfo, closeadj):
    base = _mean(_f076_vol(ncfo, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sm21_sl21_2d_v046_signal(rnd, closeadj):
    base = _mean(_f076_vol(rnd, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sm63_sl21_2d_v047_signal(rnd, closeadj):
    base = _mean(_f076_vol(rnd, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sm63_sl63_2d_v048_signal(rnd, closeadj):
    base = _mean(_f076_vol(rnd, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sm252_sl63_2d_v049_signal(rnd, closeadj):
    base = _mean(_f076_vol(rnd, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sm252_sl126_2d_v050_signal(rnd, closeadj):
    base = _mean(_f076_vol(rnd, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sm21_sl21_2d_v051_signal(netinc, closeadj):
    base = _mean(_f076_vol(netinc, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sm63_sl21_2d_v052_signal(netinc, closeadj):
    base = _mean(_f076_vol(netinc, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sm63_sl63_2d_v053_signal(netinc, closeadj):
    base = _mean(_f076_vol(netinc, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sm252_sl63_2d_v054_signal(netinc, closeadj):
    base = _mean(_f076_vol(netinc, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sm252_sl126_2d_v055_signal(netinc, closeadj):
    base = _mean(_f076_vol(netinc, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sm21_sl21_2d_v056_signal(opinc, closeadj):
    base = _mean(_f076_vol(opinc, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sm63_sl21_2d_v057_signal(opinc, closeadj):
    base = _mean(_f076_vol(opinc, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sm63_sl63_2d_v058_signal(opinc, closeadj):
    base = _mean(_f076_vol(opinc, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sm252_sl63_2d_v059_signal(opinc, closeadj):
    base = _mean(_f076_vol(opinc, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sm252_sl126_2d_v060_signal(opinc, closeadj):
    base = _mean(_f076_vol(opinc, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sm21_sl21_2d_v061_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sm63_sl21_2d_v062_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sm63_sl63_2d_v063_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sm252_sl63_2d_v064_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sm252_sl126_2d_v065_signal(revenue, closeadj):
    base = _mean(_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sm21_sl21_2d_v066_signal(revenue, closeadj):
    base = _mean(-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sm63_sl21_2d_v067_signal(revenue, closeadj):
    base = _mean(-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sm63_sl63_2d_v068_signal(revenue, closeadj):
    base = _mean(-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sm252_sl63_2d_v069_signal(revenue, closeadj):
    base = _mean(-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sm252_sl126_2d_v070_signal(revenue, closeadj):
    base = _mean(-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_pctslope_21d_2d_v071_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_pctslope_63d_2d_v072_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_pctslope_252d_2d_v073_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_pctslope_21d_2d_v074_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_pctslope_63d_2d_v075_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_pctslope_252d_2d_v076_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_pctslope_21d_2d_v077_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_pctslope_63d_2d_v078_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_pctslope_252d_2d_v079_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_pctslope_21d_2d_v080_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_pctslope_63d_2d_v081_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_pctslope_252d_2d_v082_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_pctslope_21d_2d_v083_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_pctslope_63d_2d_v084_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_pctslope_252d_2d_v085_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_pctslope_21d_2d_v086_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_pctslope_63d_2d_v087_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_pctslope_252d_2d_v088_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_pctslope_21d_2d_v089_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_pctslope_63d_2d_v090_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_pctslope_252d_2d_v091_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sgnslope_21d_2d_v092_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sgnslope_63d_2d_v093_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_sgnslope_252d_2d_v094_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sgnslope_21d_2d_v095_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sgnslope_63d_2d_v096_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_sgnslope_252d_2d_v097_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sgnslope_21d_2d_v098_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sgnslope_63d_2d_v099_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_sgnslope_252d_2d_v100_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sgnslope_21d_2d_v101_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sgnslope_63d_2d_v102_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_sgnslope_252d_2d_v103_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sgnslope_21d_2d_v104_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sgnslope_63d_2d_v105_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_sgnslope_252d_2d_v106_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sgnslope_21d_2d_v107_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sgnslope_63d_2d_v108_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_sgnslope_252d_2d_v109_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sgnslope_21d_2d_v110_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sgnslope_63d_2d_v111_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_sgnslope_252d_2d_v112_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_logmagslope_21d_2d_v113_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_logmagslope_63d_2d_v114_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_logmagslope_252d_2d_v115_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_logmagslope_21d_2d_v116_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_logmagslope_63d_2d_v117_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_logmagslope_252d_2d_v118_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_logmagslope_21d_2d_v119_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_logmagslope_63d_2d_v120_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_logmagslope_252d_2d_v121_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_logmagslope_21d_2d_v122_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_logmagslope_63d_2d_v123_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_logmagslope_252d_2d_v124_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_logmagslope_21d_2d_v125_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_logmagslope_63d_2d_v126_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_logmagslope_252d_2d_v127_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_logmagslope_21d_2d_v128_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_logmagslope_63d_2d_v129_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_logmagslope_252d_2d_v130_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_logmagslope_21d_2d_v131_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_logmagslope_63d_2d_v132_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_logmagslope_252d_2d_v133_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_vol_252|
def f076fvl_f076_fundamental_volatility_rev_vol_252_logslope_63d_2d_v134_signal(revenue, closeadj):
    base = np.log((_f076_vol(revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_vol_252|
def f076fvl_f076_fundamental_volatility_rev_vol_252_logslope_252d_2d_v135_signal(revenue, closeadj):
    base = np.log((_f076_vol(revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_vol_252|
def f076fvl_f076_fundamental_volatility_ocf_vol_252_logslope_63d_2d_v136_signal(ncfo, closeadj):
    base = np.log((_f076_vol(ncfo, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_vol_252|
def f076fvl_f076_fundamental_volatility_ocf_vol_252_logslope_252d_2d_v137_signal(ncfo, closeadj):
    base = np.log((_f076_vol(ncfo, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_vol_252|
def f076fvl_f076_fundamental_volatility_rnd_vol_252_logslope_63d_2d_v138_signal(rnd, closeadj):
    base = np.log((_f076_vol(rnd, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_vol_252|
def f076fvl_f076_fundamental_volatility_rnd_vol_252_logslope_252d_2d_v139_signal(rnd, closeadj):
    base = np.log((_f076_vol(rnd, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ni_vol_252|
def f076fvl_f076_fundamental_volatility_ni_vol_252_logslope_63d_2d_v140_signal(netinc, closeadj):
    base = np.log((_f076_vol(netinc, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ni_vol_252|
def f076fvl_f076_fundamental_volatility_ni_vol_252_logslope_252d_2d_v141_signal(netinc, closeadj):
    base = np.log((_f076_vol(netinc, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|opinc_vol_252|
def f076fvl_f076_fundamental_volatility_opinc_vol_252_logslope_63d_2d_v142_signal(opinc, closeadj):
    base = np.log((_f076_vol(opinc, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|opinc_vol_252|
def f076fvl_f076_fundamental_volatility_opinc_vol_252_logslope_252d_2d_v143_signal(opinc, closeadj):
    base = np.log((_f076_vol(opinc, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_cv_504|
def f076fvl_f076_fundamental_volatility_rev_cv_504_logslope_63d_2d_v144_signal(revenue, closeadj):
    base = np.log((_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_cv_504|
def f076fvl_f076_fundamental_volatility_rev_cv_504_logslope_252d_2d_v145_signal(revenue, closeadj):
    base = np.log((_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|stability_score|
def f076fvl_f076_fundamental_volatility_stability_score_logslope_63d_2d_v146_signal(revenue, closeadj):
    base = np.log((-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|stability_score|
def f076fvl_f076_fundamental_volatility_stability_score_logslope_252d_2d_v147_signal(revenue, closeadj):
    base = np.log((-_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

