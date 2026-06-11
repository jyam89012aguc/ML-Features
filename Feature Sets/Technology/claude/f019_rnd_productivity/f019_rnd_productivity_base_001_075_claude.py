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
def _f019_rev_per_rnd(revenue, rnd):
    return revenue / rnd.abs().replace(0, np.nan)


def _f019_gp_per_rnd(gp, rnd):
    return gp / rnd.abs().replace(0, np.nan)


# 21d mean of rev_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_per_rnd_mean_21d_base_v001_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_per_rnd_mean_63d_base_v002_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_per_rnd_mean_126d_base_v003_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_per_rnd_mean_252d_base_v004_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_per_rnd_mean_504d_base_v005_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_gp_per_rnd_mean_21d_base_v006_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_gp_per_rnd_mean_63d_base_v007_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_gp_per_rnd_mean_126d_base_v008_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_gp_per_rnd_mean_252d_base_v009_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_gp_per_rnd_mean_504d_base_v010_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opinc_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_opinc_per_rnd_mean_21d_base_v011_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opinc_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_opinc_per_rnd_mean_63d_base_v012_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opinc_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_opinc_per_rnd_mean_126d_base_v013_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opinc_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_opinc_per_rnd_mean_252d_base_v014_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opinc_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_opinc_per_rnd_mean_504d_base_v015_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_growth_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_mean_21d_base_v016_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_growth_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_mean_63d_base_v017_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_growth_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_mean_126d_base_v018_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_growth_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_mean_252d_base_v019_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_growth_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_mean_504d_base_v020_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_mean_21d_base_v021_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_mean_63d_base_v022_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_mean_126d_base_v023_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_mean_252d_base_v024_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_mean_504d_base_v025_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_fcf_per_rnd_mean_21d_base_v026_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_fcf_per_rnd_mean_63d_base_v027_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_fcf_per_rnd_mean_126d_base_v028_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_fcf_per_rnd_mean_252d_base_v029_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_fcf_per_rnd_mean_504d_base_v030_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ocf_per_rnd_mean_21d_base_v031_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ocf_per_rnd_mean_63d_base_v032_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ocf_per_rnd_mean_126d_base_v033_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ocf_per_rnd_mean_252d_base_v034_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_per_rnd scaled by closeadj
def f019rdp_f019_rnd_productivity_ocf_per_rnd_mean_504d_base_v035_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_median_63d_base_v036_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_median_252d_base_v037_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_median_504d_base_v038_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_median_63d_base_v039_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_median_252d_base_v040_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_median_504d_base_v041_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_median_63d_base_v042_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_median_252d_base_v043_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_median_504d_base_v044_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_median_63d_base_v045_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_median_252d_base_v046_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_median_504d_base_v047_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_median_63d_base_v048_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_median_252d_base_v049_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_median_504d_base_v050_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_median_63d_base_v051_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_median_252d_base_v052_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_median_504d_base_v053_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_median_63d_base_v054_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_median_252d_base_v055_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_median_504d_base_v056_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_rmax_252d_base_v057_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_rmax_504d_base_v058_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_rmax_252d_base_v059_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_rmax_504d_base_v060_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_rmax_252d_base_v061_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_rmax_504d_base_v062_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_rmax_252d_base_v063_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_rmax_504d_base_v064_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_rmax_252d_base_v065_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_rmax_504d_base_v066_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_rmax_252d_base_v067_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_rmax_504d_base_v068_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_rmax_252d_base_v069_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_rmax_504d_base_v070_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_rmin_252d_base_v071_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_rmin_504d_base_v072_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_rmin_252d_base_v073_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_rmin_504d_base_v074_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_rmin_252d_base_v075_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

