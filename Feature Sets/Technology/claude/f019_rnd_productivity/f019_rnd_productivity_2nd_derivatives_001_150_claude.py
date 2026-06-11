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
def _f019_rev_per_rnd(revenue, rnd):
    return revenue / rnd.abs().replace(0, np.nan)


def _f019_gp_per_rnd(gp, rnd):
    return gp / rnd.abs().replace(0, np.nan)


# 21d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slope_21d_2d_v001_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slope_63d_2d_v002_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slope_126d_2d_v003_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slope_252d_2d_v004_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slope_504d_2d_v005_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slope_21d_2d_v006_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slope_63d_2d_v007_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slope_126d_2d_v008_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slope_252d_2d_v009_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slope_504d_2d_v010_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slope_21d_2d_v011_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slope_63d_2d_v012_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slope_126d_2d_v013_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slope_252d_2d_v014_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slope_504d_2d_v015_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slope_21d_2d_v016_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slope_63d_2d_v017_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slope_126d_2d_v018_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slope_252d_2d_v019_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slope_504d_2d_v020_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slope_21d_2d_v021_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slope_63d_2d_v022_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slope_126d_2d_v023_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slope_252d_2d_v024_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slope_504d_2d_v025_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slope_21d_2d_v026_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slope_63d_2d_v027_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slope_126d_2d_v028_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slope_252d_2d_v029_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slope_504d_2d_v030_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slope_21d_2d_v031_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slope_63d_2d_v032_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slope_126d_2d_v033_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slope_252d_2d_v034_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slope_504d_2d_v035_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sm21_sl21_2d_v036_signal(revenue, rnd, closeadj):
    base = _mean(_f019_rev_per_rnd(revenue, rnd), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sm63_sl21_2d_v037_signal(revenue, rnd, closeadj):
    base = _mean(_f019_rev_per_rnd(revenue, rnd), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sm63_sl63_2d_v038_signal(revenue, rnd, closeadj):
    base = _mean(_f019_rev_per_rnd(revenue, rnd), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sm252_sl63_2d_v039_signal(revenue, rnd, closeadj):
    base = _mean(_f019_rev_per_rnd(revenue, rnd), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sm252_sl126_2d_v040_signal(revenue, rnd, closeadj):
    base = _mean(_f019_rev_per_rnd(revenue, rnd), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sm21_sl21_2d_v041_signal(gp, rnd, closeadj):
    base = _mean(_f019_gp_per_rnd(gp, rnd), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sm63_sl21_2d_v042_signal(gp, rnd, closeadj):
    base = _mean(_f019_gp_per_rnd(gp, rnd), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sm63_sl63_2d_v043_signal(gp, rnd, closeadj):
    base = _mean(_f019_gp_per_rnd(gp, rnd), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sm252_sl63_2d_v044_signal(gp, rnd, closeadj):
    base = _mean(_f019_gp_per_rnd(gp, rnd), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sm252_sl126_2d_v045_signal(gp, rnd, closeadj):
    base = _mean(_f019_gp_per_rnd(gp, rnd), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sm21_sl21_2d_v046_signal(opinc, rnd, closeadj):
    base = _mean(opinc / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sm63_sl21_2d_v047_signal(opinc, rnd, closeadj):
    base = _mean(opinc / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sm63_sl63_2d_v048_signal(opinc, rnd, closeadj):
    base = _mean(opinc / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sm252_sl63_2d_v049_signal(opinc, rnd, closeadj):
    base = _mean(opinc / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sm252_sl126_2d_v050_signal(opinc, rnd, closeadj):
    base = _mean(opinc / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sm21_sl21_2d_v051_signal(revenue, rnd, closeadj):
    base = _mean(revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sm63_sl21_2d_v052_signal(revenue, rnd, closeadj):
    base = _mean(revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sm63_sl63_2d_v053_signal(revenue, rnd, closeadj):
    base = _mean(revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sm252_sl63_2d_v054_signal(revenue, rnd, closeadj):
    base = _mean(revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sm252_sl126_2d_v055_signal(revenue, rnd, closeadj):
    base = _mean(revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sm21_sl21_2d_v056_signal(ebitda, rnd, closeadj):
    base = _mean(ebitda / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sm63_sl21_2d_v057_signal(ebitda, rnd, closeadj):
    base = _mean(ebitda / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sm63_sl63_2d_v058_signal(ebitda, rnd, closeadj):
    base = _mean(ebitda / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sm252_sl63_2d_v059_signal(ebitda, rnd, closeadj):
    base = _mean(ebitda / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sm252_sl126_2d_v060_signal(ebitda, rnd, closeadj):
    base = _mean(ebitda / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sm21_sl21_2d_v061_signal(fcf, rnd, closeadj):
    base = _mean(fcf / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sm63_sl21_2d_v062_signal(fcf, rnd, closeadj):
    base = _mean(fcf / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sm63_sl63_2d_v063_signal(fcf, rnd, closeadj):
    base = _mean(fcf / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sm252_sl63_2d_v064_signal(fcf, rnd, closeadj):
    base = _mean(fcf / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sm252_sl126_2d_v065_signal(fcf, rnd, closeadj):
    base = _mean(fcf / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sm21_sl21_2d_v066_signal(ncfo, rnd, closeadj):
    base = _mean(ncfo / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sm63_sl21_2d_v067_signal(ncfo, rnd, closeadj):
    base = _mean(ncfo / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sm63_sl63_2d_v068_signal(ncfo, rnd, closeadj):
    base = _mean(ncfo / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sm252_sl63_2d_v069_signal(ncfo, rnd, closeadj):
    base = _mean(ncfo / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sm252_sl126_2d_v070_signal(ncfo, rnd, closeadj):
    base = _mean(ncfo / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_pctslope_21d_2d_v071_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_pctslope_63d_2d_v072_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_pctslope_252d_2d_v073_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_pctslope_21d_2d_v074_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_pctslope_63d_2d_v075_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_pctslope_252d_2d_v076_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_pctslope_21d_2d_v077_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_pctslope_63d_2d_v078_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_pctslope_252d_2d_v079_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_pctslope_21d_2d_v080_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_pctslope_63d_2d_v081_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_pctslope_252d_2d_v082_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_pctslope_21d_2d_v083_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_pctslope_63d_2d_v084_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_pctslope_252d_2d_v085_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_pctslope_21d_2d_v086_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_pctslope_63d_2d_v087_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_pctslope_252d_2d_v088_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_pctslope_21d_2d_v089_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_pctslope_63d_2d_v090_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_pctslope_252d_2d_v091_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sgnslope_21d_2d_v092_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sgnslope_63d_2d_v093_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_sgnslope_252d_2d_v094_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sgnslope_21d_2d_v095_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sgnslope_63d_2d_v096_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_sgnslope_252d_2d_v097_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sgnslope_21d_2d_v098_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sgnslope_63d_2d_v099_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_sgnslope_252d_2d_v100_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sgnslope_21d_2d_v101_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sgnslope_63d_2d_v102_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_sgnslope_252d_2d_v103_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sgnslope_21d_2d_v104_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sgnslope_63d_2d_v105_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_sgnslope_252d_2d_v106_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sgnslope_21d_2d_v107_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sgnslope_63d_2d_v108_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_sgnslope_252d_2d_v109_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sgnslope_21d_2d_v110_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sgnslope_63d_2d_v111_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_sgnslope_252d_2d_v112_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_logmagslope_21d_2d_v113_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_logmagslope_63d_2d_v114_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_logmagslope_252d_2d_v115_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_logmagslope_21d_2d_v116_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_logmagslope_63d_2d_v117_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_logmagslope_252d_2d_v118_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_logmagslope_21d_2d_v119_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_logmagslope_63d_2d_v120_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_logmagslope_252d_2d_v121_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_logmagslope_21d_2d_v122_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_logmagslope_63d_2d_v123_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_logmagslope_252d_2d_v124_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_logmagslope_21d_2d_v125_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_logmagslope_63d_2d_v126_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_logmagslope_252d_2d_v127_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_logmagslope_21d_2d_v128_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_logmagslope_63d_2d_v129_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_logmagslope_252d_2d_v130_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_logmagslope_21d_2d_v131_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_logmagslope_63d_2d_v132_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_logmagslope_252d_2d_v133_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_per_rnd|
def f019rdp_f019_rnd_productivity_rev_per_rnd_logslope_63d_2d_v134_signal(revenue, rnd, closeadj):
    base = np.log((_f019_rev_per_rnd(revenue, rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_per_rnd|
def f019rdp_f019_rnd_productivity_rev_per_rnd_logslope_252d_2d_v135_signal(revenue, rnd, closeadj):
    base = np.log((_f019_rev_per_rnd(revenue, rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gp_per_rnd|
def f019rdp_f019_rnd_productivity_gp_per_rnd_logslope_63d_2d_v136_signal(gp, rnd, closeadj):
    base = np.log((_f019_gp_per_rnd(gp, rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gp_per_rnd|
def f019rdp_f019_rnd_productivity_gp_per_rnd_logslope_252d_2d_v137_signal(gp, rnd, closeadj):
    base = np.log((_f019_gp_per_rnd(gp, rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|opinc_per_rnd|
def f019rdp_f019_rnd_productivity_opinc_per_rnd_logslope_63d_2d_v138_signal(opinc, rnd, closeadj):
    base = np.log((opinc / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|opinc_per_rnd|
def f019rdp_f019_rnd_productivity_opinc_per_rnd_logslope_252d_2d_v139_signal(opinc, rnd, closeadj):
    base = np.log((opinc / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_growth_per_rnd|
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_logslope_63d_2d_v140_signal(revenue, rnd, closeadj):
    base = np.log((revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_growth_per_rnd|
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_logslope_252d_2d_v141_signal(revenue, rnd, closeadj):
    base = np.log((revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ebitda_per_rnd|
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_logslope_63d_2d_v142_signal(ebitda, rnd, closeadj):
    base = np.log((ebitda / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ebitda_per_rnd|
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_logslope_252d_2d_v143_signal(ebitda, rnd, closeadj):
    base = np.log((ebitda / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|fcf_per_rnd|
def f019rdp_f019_rnd_productivity_fcf_per_rnd_logslope_63d_2d_v144_signal(fcf, rnd, closeadj):
    base = np.log((fcf / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|fcf_per_rnd|
def f019rdp_f019_rnd_productivity_fcf_per_rnd_logslope_252d_2d_v145_signal(fcf, rnd, closeadj):
    base = np.log((fcf / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_per_rnd|
def f019rdp_f019_rnd_productivity_ocf_per_rnd_logslope_63d_2d_v146_signal(ncfo, rnd, closeadj):
    base = np.log((ncfo / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_per_rnd|
def f019rdp_f019_rnd_productivity_ocf_per_rnd_logslope_252d_2d_v147_signal(ncfo, rnd, closeadj):
    base = np.log((ncfo / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

