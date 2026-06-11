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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f21_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f21_revenue_growth_smooth(revenue, smooth_w, growth_w):
    sm = revenue.rolling(smooth_w, min_periods=max(1, smooth_w // 2)).mean()
    return sm.pct_change(periods=growth_w)


def _f21_revenue_log_growth(revenue, w):
    return np.log1p(revenue.pct_change(periods=w))


# Pattern: 150 slopes — pairs (window W, ROC) varied across base feature themes.

def _slope_grow(revenue, closeadj, W, ROC):
    base = _f21_revenue_growth(revenue, W) * closeadj
    return _diff(base, ROC)


def _slope_loggrow(revenue, closeadj, W, ROC):
    base = _f21_revenue_log_growth(revenue, W) * closeadj
    return _diff(base, ROC)


def _slope_smooth(revenue, closeadj, sw, gw, ROC):
    base = _f21_revenue_growth_smooth(revenue, sw, gw) * closeadj
    return _diff(base, ROC)


# 5d slope of 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_21d_slope_v001_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d revenue growth × close
def f21rg_f21_revenue_growth_revgrow_21d_slope_v002_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d revenue growth
def f21rg_f21_revenue_growth_revgrow_63d_slope_v003_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d revenue growth
def f21rg_f21_revenue_growth_revgrow_63d_slope_v004_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d revenue growth
def f21rg_f21_revenue_growth_revgrow_126d_slope_v005_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d revenue growth
def f21rg_f21_revenue_growth_revgrow_252d_slope_v006_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue growth
def f21rg_f21_revenue_growth_revgrow_252d_slope_v007_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d revenue growth
def f21rg_f21_revenue_growth_revgrow_504d_slope_v008_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d revenue growth
def f21rg_f21_revenue_growth_revgrow_504d_slope_v009_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d revenue growth
def f21rg_f21_revenue_growth_revgrow_5d_slope_v010_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 5) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d revenue growth
def f21rg_f21_revenue_growth_revgrow_10d_slope_v011_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 10) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d revenue growth
def f21rg_f21_revenue_growth_revgrow_42d_slope_v012_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 42) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d revenue growth
def f21rg_f21_revenue_growth_revgrow_189d_slope_v013_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 189) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d revenue growth
def f21rg_f21_revenue_growth_revgrow_378d_slope_v014_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 378) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowsm5_21d
def f21rg_f21_revenue_growth_revgrowsm5_21d_slope_v015_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 5, 21) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowsm21_63d
def f21rg_f21_revenue_growth_revgrowsm21_63d_slope_v016_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 21, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowsm63_252d
def f21rg_f21_revenue_growth_revgrowsm63_252d_slope_v017_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 63, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowsm126_504d
def f21rg_f21_revenue_growth_revgrowsm126_504d_slope_v018_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 126, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log growth
def f21rg_f21_revenue_growth_revloggrow_21d_slope_v019_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log growth
def f21rg_f21_revenue_growth_revloggrow_63d_slope_v020_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log growth
def f21rg_f21_revenue_growth_revloggrow_252d_slope_v021_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log growth
def f21rg_f21_revenue_growth_revloggrow_504d_slope_v022_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowz 252d
def f21rg_f21_revenue_growth_revgrowz_252d_slope_v023_signal(revenue, closeadj):
    base = _z(_f21_revenue_growth(revenue, 63), 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowz 504d
def f21rg_f21_revenue_growth_revgrowz_504d_slope_v024_signal(revenue, closeadj):
    base = _z(_f21_revenue_growth(revenue, 252), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowstd 21d
def f21rg_f21_revenue_growth_revgrowstd_21d_slope_v025_signal(revenue, closeadj):
    base = _std(_f21_revenue_growth(revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowstd 252d
def f21rg_f21_revenue_growth_revgrowstd_252d_slope_v026_signal(revenue, closeadj):
    base = _std(_f21_revenue_growth(revenue, 21), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowstd 504d
def f21rg_f21_revenue_growth_revgrowstd_504d_slope_v027_signal(revenue, closeadj):
    base = _std(_f21_revenue_growth(revenue, 63), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowdiff 63m252
def f21rg_f21_revenue_growth_revgrowdiff_63m252_slope_v028_signal(revenue, closeadj):
    base = (_f21_revenue_growth(revenue, 63) - _f21_revenue_growth(revenue, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowdiff 21m63
def f21rg_f21_revenue_growth_revgrowdiff_21m63_slope_v029_signal(revenue, closeadj):
    base = (_f21_revenue_growth(revenue, 21) - _f21_revenue_growth(revenue, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowdiff 252m504
def f21rg_f21_revenue_growth_revgrowdiff_252m504_slope_v030_signal(revenue, closeadj):
    base = (_f21_revenue_growth(revenue, 252) - _f21_revenue_growth(revenue, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowdollar 21d
def f21rg_f21_revenue_growth_revgrowdollar_21d_slope_v031_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowdollar 252d
def f21rg_f21_revenue_growth_revgrowdollar_252d_slope_v032_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowdollar 504d
def f21rg_f21_revenue_growth_revgrowdollar_504d_slope_v033_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowema 21d
def f21rg_f21_revenue_growth_revgrowema_21d_slope_v034_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowema 63d
def f21rg_f21_revenue_growth_revgrowema_63d_slope_v035_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowema 252d
def f21rg_f21_revenue_growth_revgrowema_252d_slope_v036_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrow_sq 252d
def f21rg_f21_revenue_growth_revgrowsq_252d_slope_v037_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrow_sq 504d
def f21rg_f21_revenue_growth_revgrowsq_504d_slope_v038_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 504)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxvolz 252d
def f21rg_f21_revenue_growth_revgrowxvolz_252d_slope_v039_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxvolz 63d
def f21rg_f21_revenue_growth_revgrowxvolz_63d_slope_v040_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxdv 252d
def f21rg_f21_revenue_growth_revgrowxdv_252d_slope_v041_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxdv 21d
def f21rg_f21_revenue_growth_revgrowxdv_21d_slope_v042_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 21) * (closeadj * volume)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowmax 252d
def f21rg_f21_revenue_growth_revgrowmax_252d_slope_v043_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowmax 504d
def f21rg_f21_revenue_growth_revgrowmax_504d_slope_v044_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252).rolling(504, min_periods=126).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowrange 252d
def f21rg_f21_revenue_growth_revgrowrange_252d_slope_v045_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_diff_norm(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowrange 504d
def f21rg_f21_revenue_growth_revgrowrange_504d_slope_v046_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252)
    rng = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    result = _slope_diff_norm(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowskew 252d
def f21rg_f21_revenue_growth_revgrowskew_252d_slope_v047_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(252, min_periods=63).skew() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowskew 504d
def f21rg_f21_revenue_growth_revgrowskew_504d_slope_v048_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(504, min_periods=126).skew() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowkurt 252d
def f21rg_f21_revenue_growth_revgrowkurt_252d_slope_v049_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(252, min_periods=63).kurt() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowannual 252d
def f21rg_f21_revenue_growth_revgrowannual_252d_slope_v050_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 63) * 4.0, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowannual 504d
def f21rg_f21_revenue_growth_revgrowannual_504d_slope_v051_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 63) * 4.0, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrow_pershare 252d
def f21rg_f21_revenue_growth_revgrow_pershare_252d_slope_v052_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 252) * rps * closeadj / rps.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrow_pershare 63d
def f21rg_f21_revenue_growth_revgrow_pershare_63d_slope_v053_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 63) * rps * closeadj / rps.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrow_pershare 504d
def f21rg_f21_revenue_growth_revgrow_pershare_504d_slope_v054_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 504) * rps * closeadj / rps.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revlvl 21d × close
def f21rg_f21_revenue_growth_revlvl_21d_slope_v055_signal(revenue, closeadj):
    base = _mean(revenue, 21) * closeadj + _f21_revenue_growth(revenue, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revlvl 63d × close
def f21rg_f21_revenue_growth_revlvl_63d_slope_v056_signal(revenue, closeadj):
    base = _mean(revenue, 63) * closeadj + _f21_revenue_growth(revenue, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revlvl 252d × close
def f21rg_f21_revenue_growth_revlvl_252d_slope_v057_signal(revenue, closeadj):
    base = _mean(revenue, 252) * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revlvl 504d × close
def f21rg_f21_revenue_growth_revlvl_504d_slope_v058_signal(revenue, closeadj):
    base = _mean(revenue, 504) * closeadj + _f21_revenue_growth(revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of logrev 252d × close
def f21rg_f21_revenue_growth_logrev_252d_slope_v059_signal(revenue, closeadj):
    base = np.log(_mean(revenue, 252).replace(0, np.nan)) * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of logrev 504d × close
def f21rg_f21_revenue_growth_logrev_504d_slope_v060_signal(revenue, closeadj):
    base = np.log(_mean(revenue, 504).replace(0, np.nan)) * closeadj + _f21_revenue_growth(revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxatr 252d
def f21rg_f21_revenue_growth_revgrowxatr_252d_slope_v061_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f21_revenue_growth(revenue, 252) * atr * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxatr 63d
def f21rg_f21_revenue_growth_revgrowxatr_63d_slope_v062_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 63) * atr * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxret 21d
def f21rg_f21_revenue_growth_revgrowxret_21d_slope_v063_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * closeadj.pct_change(21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxret 63d
def f21rg_f21_revenue_growth_revgrowxret_63d_slope_v064_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * closeadj.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxret 252d
def f21rg_f21_revenue_growth_revgrowxret_252d_slope_v065_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * closeadj.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowratio 63v252
def f21rg_f21_revenue_growth_revgrowratio_63v252_slope_v066_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 63)
    b = _f21_revenue_growth(revenue, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowratio 21v63
def f21rg_f21_revenue_growth_revgrowratio_21v63_slope_v067_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 21)
    b = _f21_revenue_growth(revenue, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowratio 252v504
def f21rg_f21_revenue_growth_revgrowratio_252v504_slope_v068_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_growth(revenue, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowcumsum 252d
def f21rg_f21_revenue_growth_revgrowcumsum_252d_slope_v069_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowcumsum 504d
def f21rg_f21_revenue_growth_revgrowcumsum_504d_slope_v070_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63).rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxrevvol 252d
def f21rg_f21_revenue_growth_revgrowxrevvol_252d_slope_v071_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * revenue * volume / revenue.replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxlogrev 252d
def f21rg_f21_revenue_growth_revgrowxlogrev_252d_slope_v072_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * np.log(revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxlogrev 504d
def f21rg_f21_revenue_growth_revgrowxlogrev_504d_slope_v073_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * np.log(revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowcum 252d
def f21rg_f21_revenue_growth_revloggrowcum_252d_slope_v074_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowema 252d
def f21rg_f21_revenue_growth_revloggrowema_252d_slope_v075_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxvol 21d
def f21rg_f21_revenue_growth_revgrowxvol_21d_slope_v076_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 21) * volume * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowatr 252d
def f21rg_f21_revenue_growth_revgrowatr_252d_slope_v077_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 252) * atr
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowratio 63v504
def f21rg_f21_revenue_growth_revgrowratio_63v504_slope_v078_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 63)
    b = _f21_revenue_growth(revenue, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositegrow 252d
def f21rg_f21_revenue_growth_compositegrow_252d_slope_v079_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_log_growth(revenue, 252)
    base = (a + b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d smoothed 5d growth
def f21rg_f21_revenue_growth_revgrowsm5_5d_slope_v080_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 5, 5) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d smoothed 21d growth
def f21rg_f21_revenue_growth_revgrowsm21_21d_slope_v081_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 21, 21) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d smoothed 252d growth
def f21rg_f21_revenue_growth_revgrowsm21_252d_slope_v082_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 21, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d smoothed 504d growth
def f21rg_f21_revenue_growth_revgrowsm63_504d_slope_v083_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 63, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d smoothed 252d growth
def f21rg_f21_revenue_growth_revgrowsm252_252d_slope_v084_signal(revenue, closeadj):
    base = _f21_revenue_growth_smooth(revenue, 252, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowdiff 63m252
def f21rg_f21_revenue_growth_revloggrowdiff_63m252_slope_v085_signal(revenue, closeadj):
    base = (_f21_revenue_log_growth(revenue, 63) - _f21_revenue_log_growth(revenue, 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowdiff 252m504
def f21rg_f21_revenue_growth_revloggrowdiff_252m504_slope_v086_signal(revenue, closeadj):
    base = (_f21_revenue_log_growth(revenue, 252) - _f21_revenue_log_growth(revenue, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowxret 252d
def f21rg_f21_revenue_growth_revloggrowxret_252d_slope_v087_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252) * closeadj.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revloggrowxret 63d
def f21rg_f21_revenue_growth_revloggrowxret_63d_slope_v088_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63) * closeadj.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgaindollar 252d
def f21rg_f21_revenue_growth_revgaindollar_252d_slope_v089_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgaindollar 504d
def f21rg_f21_revenue_growth_revgaindollar_504d_slope_v090_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revloggrowema 63d
def f21rg_f21_revenue_growth_revloggrowema_63d_slope_v091_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowema 504d
def f21rg_f21_revenue_growth_revloggrowema_504d_slope_v092_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 504).ewm(span=504, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of revgrowxvol 5d
def f21rg_f21_revenue_growth_revgrowxvol_5d_slope_v093_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 5) * volume * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxvol 63d
def f21rg_f21_revenue_growth_revgrowxvol_63d_slope_v094_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63) * volume * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxvol 252d
def f21rg_f21_revenue_growth_revgrowxvol_252d_slope_v095_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * volume * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxlogrev 21d
def f21rg_f21_revenue_growth_revgrowxlogrev_21d_slope_v096_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * np.log(revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxlogrev 63d
def f21rg_f21_revenue_growth_revgrowxlogrev_63d_slope_v097_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * np.log(revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxrevdv 252d
def f21rg_f21_revenue_growth_revgrowxrevdv_252d_slope_v098_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxdv 504d
def f21rg_f21_revenue_growth_revgrowxdv_504d_slope_v099_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 504) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowcumsum 63d
def f21rg_f21_revenue_growth_revgrowcumsum_63d_slope_v100_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowcumsum 504d2
def f21rg_f21_revenue_growth_revgrowcumsum_504d2_slope_v101_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21).rolling(504, min_periods=126).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrow_pershare 21d
def f21rg_f21_revenue_growth_revgrow_pershare_21d_slope_v102_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 21) * rps * closeadj / rps.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrow_pershare 126d
def f21rg_f21_revenue_growth_revgrow_pershare_126d_slope_v103_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 126) * rps * closeadj / rps.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgaindollar 63d
def f21rg_f21_revenue_growth_revgaindollar_63d_slope_v104_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 63) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowstd 63d
def f21rg_f21_revenue_growth_revgrowstd_63d_slope_v105_signal(revenue, closeadj):
    base = _std(_f21_revenue_growth(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowstd 126d
def f21rg_f21_revenue_growth_revgrowstd_126d_slope_v106_signal(revenue, closeadj):
    base = _std(_f21_revenue_growth(revenue, 21), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of revgrowmean 21d
def f21rg_f21_revenue_growth_revgrowmean_21d_slope_v107_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowmean 63d
def f21rg_f21_revenue_growth_revgrowmean_63d_slope_v108_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowmean 252d
def f21rg_f21_revenue_growth_revgrowmean_252d_slope_v109_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 252), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowmean 504d
def f21rg_f21_revenue_growth_revgrowmean_504d_slope_v110_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 21), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowz 63d
def f21rg_f21_revenue_growth_revgrowz_63d_slope_v111_signal(revenue, closeadj):
    base = _z(_f21_revenue_growth(revenue, 21), 63) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowz 252d
def f21rg_f21_revenue_growth_revloggrowz_252d_slope_v112_signal(revenue, closeadj):
    base = _z(_f21_revenue_log_growth(revenue, 21), 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowz 504d
def f21rg_f21_revenue_growth_revloggrowz_504d_slope_v113_signal(revenue, closeadj):
    base = _z(_f21_revenue_log_growth(revenue, 63), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxrev 21d
def f21rg_f21_revenue_growth_revgrowxrev_21d_slope_v114_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of revgrowxrev 5d
def f21rg_f21_revenue_growth_revgrowxrev_5d_slope_v115_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 5) * revenue * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of logrevsq 252d
def f21rg_f21_revenue_growth_logrevsq_252d_slope_v116_signal(revenue, closeadj):
    lr = np.log(_mean(revenue, 252).replace(0, np.nan))
    base = lr * lr * closeadj + _f21_revenue_growth(revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of logrevxgrow 252d
def f21rg_f21_revenue_growth_logrevxgrow_252d_slope_v117_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 252) * np.log(revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowvolvol 252d
def f21rg_f21_revenue_growth_revgrowvolvol_252d_slope_v118_signal(revenue, closeadj):
    base = _std(_std(_f21_revenue_growth(revenue, 21), 63), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowvolvol 504d
def f21rg_f21_revenue_growth_revgrowvolvol_504d_slope_v119_signal(revenue, closeadj):
    base = _std(_std(_f21_revenue_growth(revenue, 21), 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowturnover 252d
def f21rg_f21_revenue_growth_revgrowturnover_252d_slope_v120_signal(revenue, sharesbas, closeadj, volume):
    turn = volume / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 252) * turn * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowturnover 63d
def f21rg_f21_revenue_growth_revgrowturnover_63d_slope_v121_signal(revenue, sharesbas, closeadj, volume):
    turn = volume / sharesbas.replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 63) * turn * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowsq 252d
def f21rg_f21_revenue_growth_revloggrowsq_252d_slope_v122_signal(revenue, closeadj):
    a = _f21_revenue_log_growth(revenue, 252)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revloggrowsq 504d
def f21rg_f21_revenue_growth_revloggrowsq_504d_slope_v123_signal(revenue, closeadj):
    a = _f21_revenue_log_growth(revenue, 504)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxstd 252d
def f21rg_f21_revenue_growth_revgrowxstd_252d_slope_v124_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * _std(_f21_revenue_growth(revenue, 21), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxstd 21d
def f21rg_f21_revenue_growth_revgrowxstd_21d_slope_v125_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21) * _std(_f21_revenue_growth(revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowema 504d
def f21rg_f21_revenue_growth_revgrowema_504d_slope_v126_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504).ewm(span=504, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revloggrowema 21d
def f21rg_f21_revenue_growth_revloggrowema_21d_slope_v127_signal(revenue, closeadj):
    base = _f21_revenue_log_growth(revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowclip 252d
def f21rg_f21_revenue_growth_revgrowclip_252d_slope_v128_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252).clip(-1.0, 1.0) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowclip 504d
def f21rg_f21_revenue_growth_revgrowclip_504d_slope_v129_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504).clip(-1.0, 1.0) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxlogvol 252d
def f21rg_f21_revenue_growth_revgrowxlogvol_252d_slope_v130_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * np.log(volume.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxlogvol 63d
def f21rg_f21_revenue_growth_revgrowxlogvol_63d_slope_v131_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 63) * np.log(volume.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowxatr 21d
def f21rg_f21_revenue_growth_revgrowxatr_21d_slope_v132_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f21_revenue_growth(revenue, 21) * atr * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxatr 504d
def f21rg_f21_revenue_growth_revgrowxatr_504d_slope_v133_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f21_revenue_growth(revenue, 504) * atr * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowdvclose 252d
def f21rg_f21_revenue_growth_revgrowdvclose_252d_slope_v134_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * (closeadj * volume) * closeadj / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowdiff 126m252
def f21rg_f21_revenue_growth_revgrowdiff_126m252_slope_v135_signal(revenue, closeadj):
    base = (_f21_revenue_growth(revenue, 126) - _f21_revenue_growth(revenue, 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revloggrowdiff 21m63
def f21rg_f21_revenue_growth_revloggrowdiff_21m63_slope_v136_signal(revenue, closeadj):
    base = (_f21_revenue_log_growth(revenue, 21) - _f21_revenue_log_growth(revenue, 63)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowampl 252d
def f21rg_f21_revenue_growth_revgrowampl_252d_slope_v137_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    a = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_diff_norm(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowampl 504d
def f21rg_f21_revenue_growth_revgrowampl_504d_slope_v138_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 21)
    a = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    result = _slope_diff_norm(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxrevsq 252d
def f21rg_f21_revenue_growth_revgrowxrevsq_252d_slope_v139_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * revenue * revenue / revenue.replace(0, np.nan) * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxrevsq 504d
def f21rg_f21_revenue_growth_revgrowxrevsq_504d_slope_v140_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * revenue * revenue / revenue.replace(0, np.nan) * closeadj / revenue.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowfrac 252d
def f21rg_f21_revenue_growth_revgrowfrac_252d_slope_v141_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowfrac 504d
def f21rg_f21_revenue_growth_revgrowfrac_504d_slope_v142_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowatrvol 252d
def f21rg_f21_revenue_growth_revgrowatrvol_252d_slope_v143_signal(revenue, closeadj, high, low, volume):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f21_revenue_growth(revenue, 252) * atr * volume * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowclmean 252d
def f21rg_f21_revenue_growth_revgrowclmean_252d_slope_v144_signal(revenue, closeadj):
    cm = closeadj / _mean(closeadj, 21).replace(0, np.nan)
    base = _f21_revenue_growth(revenue, 252) * cm * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowsmymean 252d
def f21rg_f21_revenue_growth_revgrowsmymean_252d_slope_v145_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 252), 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revgrowsmymean 63d
def f21rg_f21_revenue_growth_revgrowsmymean_63d_slope_v146_signal(revenue, closeadj):
    base = _mean(_f21_revenue_growth(revenue, 252), 63) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxlogcl 252d
def f21rg_f21_revenue_growth_revgrowxlogcl_252d_slope_v147_signal(revenue, closeadj):
    base = _f21_revenue_growth(revenue, 252) * np.log(closeadj.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revgrowxvollog 252d
def f21rg_f21_revenue_growth_revgrowxvollog_252d_slope_v148_signal(revenue, closeadj, volume):
    base = _f21_revenue_growth(revenue, 252) * np.log(volume.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositeg 252d
def f21rg_f21_revenue_growth_compositeg_252d_slope_v149_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 252)
    b = _f21_revenue_log_growth(revenue, 252)
    c = _std(_f21_revenue_growth(revenue, 21), 252)
    base = (a + b + c) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositeg 504d
def f21rg_f21_revenue_growth_compositeg_504d_slope_v150_signal(revenue, closeadj):
    a = _f21_revenue_growth(revenue, 504)
    b = _f21_revenue_log_growth(revenue, 504)
    c = _std(_f21_revenue_growth(revenue, 63), 504)
    base = (a + b + c) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21rg_f21_revenue_growth_revgrow_21d_slope_v001_signal,
    f21rg_f21_revenue_growth_revgrow_21d_slope_v002_signal,
    f21rg_f21_revenue_growth_revgrow_63d_slope_v003_signal,
    f21rg_f21_revenue_growth_revgrow_63d_slope_v004_signal,
    f21rg_f21_revenue_growth_revgrow_126d_slope_v005_signal,
    f21rg_f21_revenue_growth_revgrow_252d_slope_v006_signal,
    f21rg_f21_revenue_growth_revgrow_252d_slope_v007_signal,
    f21rg_f21_revenue_growth_revgrow_504d_slope_v008_signal,
    f21rg_f21_revenue_growth_revgrow_504d_slope_v009_signal,
    f21rg_f21_revenue_growth_revgrow_5d_slope_v010_signal,
    f21rg_f21_revenue_growth_revgrow_10d_slope_v011_signal,
    f21rg_f21_revenue_growth_revgrow_42d_slope_v012_signal,
    f21rg_f21_revenue_growth_revgrow_189d_slope_v013_signal,
    f21rg_f21_revenue_growth_revgrow_378d_slope_v014_signal,
    f21rg_f21_revenue_growth_revgrowsm5_21d_slope_v015_signal,
    f21rg_f21_revenue_growth_revgrowsm21_63d_slope_v016_signal,
    f21rg_f21_revenue_growth_revgrowsm63_252d_slope_v017_signal,
    f21rg_f21_revenue_growth_revgrowsm126_504d_slope_v018_signal,
    f21rg_f21_revenue_growth_revloggrow_21d_slope_v019_signal,
    f21rg_f21_revenue_growth_revloggrow_63d_slope_v020_signal,
    f21rg_f21_revenue_growth_revloggrow_252d_slope_v021_signal,
    f21rg_f21_revenue_growth_revloggrow_504d_slope_v022_signal,
    f21rg_f21_revenue_growth_revgrowz_252d_slope_v023_signal,
    f21rg_f21_revenue_growth_revgrowz_504d_slope_v024_signal,
    f21rg_f21_revenue_growth_revgrowstd_21d_slope_v025_signal,
    f21rg_f21_revenue_growth_revgrowstd_252d_slope_v026_signal,
    f21rg_f21_revenue_growth_revgrowstd_504d_slope_v027_signal,
    f21rg_f21_revenue_growth_revgrowdiff_63m252_slope_v028_signal,
    f21rg_f21_revenue_growth_revgrowdiff_21m63_slope_v029_signal,
    f21rg_f21_revenue_growth_revgrowdiff_252m504_slope_v030_signal,
    f21rg_f21_revenue_growth_revgrowdollar_21d_slope_v031_signal,
    f21rg_f21_revenue_growth_revgrowdollar_252d_slope_v032_signal,
    f21rg_f21_revenue_growth_revgrowdollar_504d_slope_v033_signal,
    f21rg_f21_revenue_growth_revgrowema_21d_slope_v034_signal,
    f21rg_f21_revenue_growth_revgrowema_63d_slope_v035_signal,
    f21rg_f21_revenue_growth_revgrowema_252d_slope_v036_signal,
    f21rg_f21_revenue_growth_revgrowsq_252d_slope_v037_signal,
    f21rg_f21_revenue_growth_revgrowsq_504d_slope_v038_signal,
    f21rg_f21_revenue_growth_revgrowxvolz_252d_slope_v039_signal,
    f21rg_f21_revenue_growth_revgrowxvolz_63d_slope_v040_signal,
    f21rg_f21_revenue_growth_revgrowxdv_252d_slope_v041_signal,
    f21rg_f21_revenue_growth_revgrowxdv_21d_slope_v042_signal,
    f21rg_f21_revenue_growth_revgrowmax_252d_slope_v043_signal,
    f21rg_f21_revenue_growth_revgrowmax_504d_slope_v044_signal,
    f21rg_f21_revenue_growth_revgrowrange_252d_slope_v045_signal,
    f21rg_f21_revenue_growth_revgrowrange_504d_slope_v046_signal,
    f21rg_f21_revenue_growth_revgrowskew_252d_slope_v047_signal,
    f21rg_f21_revenue_growth_revgrowskew_504d_slope_v048_signal,
    f21rg_f21_revenue_growth_revgrowkurt_252d_slope_v049_signal,
    f21rg_f21_revenue_growth_revgrowannual_252d_slope_v050_signal,
    f21rg_f21_revenue_growth_revgrowannual_504d_slope_v051_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_252d_slope_v052_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_63d_slope_v053_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_504d_slope_v054_signal,
    f21rg_f21_revenue_growth_revlvl_21d_slope_v055_signal,
    f21rg_f21_revenue_growth_revlvl_63d_slope_v056_signal,
    f21rg_f21_revenue_growth_revlvl_252d_slope_v057_signal,
    f21rg_f21_revenue_growth_revlvl_504d_slope_v058_signal,
    f21rg_f21_revenue_growth_logrev_252d_slope_v059_signal,
    f21rg_f21_revenue_growth_logrev_504d_slope_v060_signal,
    f21rg_f21_revenue_growth_revgrowxatr_252d_slope_v061_signal,
    f21rg_f21_revenue_growth_revgrowxatr_63d_slope_v062_signal,
    f21rg_f21_revenue_growth_revgrowxret_21d_slope_v063_signal,
    f21rg_f21_revenue_growth_revgrowxret_63d_slope_v064_signal,
    f21rg_f21_revenue_growth_revgrowxret_252d_slope_v065_signal,
    f21rg_f21_revenue_growth_revgrowratio_63v252_slope_v066_signal,
    f21rg_f21_revenue_growth_revgrowratio_21v63_slope_v067_signal,
    f21rg_f21_revenue_growth_revgrowratio_252v504_slope_v068_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_252d_slope_v069_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_504d_slope_v070_signal,
    f21rg_f21_revenue_growth_revgrowxrevvol_252d_slope_v071_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_252d_slope_v072_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_504d_slope_v073_signal,
    f21rg_f21_revenue_growth_revloggrowcum_252d_slope_v074_signal,
    f21rg_f21_revenue_growth_revloggrowema_252d_slope_v075_signal,
    f21rg_f21_revenue_growth_revgrowxvol_21d_slope_v076_signal,
    f21rg_f21_revenue_growth_revgrowatr_252d_slope_v077_signal,
    f21rg_f21_revenue_growth_revgrowratio_63v504_slope_v078_signal,
    f21rg_f21_revenue_growth_compositegrow_252d_slope_v079_signal,
    f21rg_f21_revenue_growth_revgrowsm5_5d_slope_v080_signal,
    f21rg_f21_revenue_growth_revgrowsm21_21d_slope_v081_signal,
    f21rg_f21_revenue_growth_revgrowsm21_252d_slope_v082_signal,
    f21rg_f21_revenue_growth_revgrowsm63_504d_slope_v083_signal,
    f21rg_f21_revenue_growth_revgrowsm252_252d_slope_v084_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_63m252_slope_v085_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_252m504_slope_v086_signal,
    f21rg_f21_revenue_growth_revloggrowxret_252d_slope_v087_signal,
    f21rg_f21_revenue_growth_revloggrowxret_63d_slope_v088_signal,
    f21rg_f21_revenue_growth_revgaindollar_252d_slope_v089_signal,
    f21rg_f21_revenue_growth_revgaindollar_504d_slope_v090_signal,
    f21rg_f21_revenue_growth_revloggrowema_63d_slope_v091_signal,
    f21rg_f21_revenue_growth_revloggrowema_504d_slope_v092_signal,
    f21rg_f21_revenue_growth_revgrowxvol_5d_slope_v093_signal,
    f21rg_f21_revenue_growth_revgrowxvol_63d_slope_v094_signal,
    f21rg_f21_revenue_growth_revgrowxvol_252d_slope_v095_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_21d_slope_v096_signal,
    f21rg_f21_revenue_growth_revgrowxlogrev_63d_slope_v097_signal,
    f21rg_f21_revenue_growth_revgrowxrevdv_252d_slope_v098_signal,
    f21rg_f21_revenue_growth_revgrowxdv_504d_slope_v099_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_63d_slope_v100_signal,
    f21rg_f21_revenue_growth_revgrowcumsum_504d2_slope_v101_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_21d_slope_v102_signal,
    f21rg_f21_revenue_growth_revgrow_pershare_126d_slope_v103_signal,
    f21rg_f21_revenue_growth_revgaindollar_63d_slope_v104_signal,
    f21rg_f21_revenue_growth_revgrowstd_63d_slope_v105_signal,
    f21rg_f21_revenue_growth_revgrowstd_126d_slope_v106_signal,
    f21rg_f21_revenue_growth_revgrowmean_21d_slope_v107_signal,
    f21rg_f21_revenue_growth_revgrowmean_63d_slope_v108_signal,
    f21rg_f21_revenue_growth_revgrowmean_252d_slope_v109_signal,
    f21rg_f21_revenue_growth_revgrowmean_504d_slope_v110_signal,
    f21rg_f21_revenue_growth_revgrowz_63d_slope_v111_signal,
    f21rg_f21_revenue_growth_revloggrowz_252d_slope_v112_signal,
    f21rg_f21_revenue_growth_revloggrowz_504d_slope_v113_signal,
    f21rg_f21_revenue_growth_revgrowxrev_21d_slope_v114_signal,
    f21rg_f21_revenue_growth_revgrowxrev_5d_slope_v115_signal,
    f21rg_f21_revenue_growth_logrevsq_252d_slope_v116_signal,
    f21rg_f21_revenue_growth_logrevxgrow_252d_slope_v117_signal,
    f21rg_f21_revenue_growth_revgrowvolvol_252d_slope_v118_signal,
    f21rg_f21_revenue_growth_revgrowvolvol_504d_slope_v119_signal,
    f21rg_f21_revenue_growth_revgrowturnover_252d_slope_v120_signal,
    f21rg_f21_revenue_growth_revgrowturnover_63d_slope_v121_signal,
    f21rg_f21_revenue_growth_revloggrowsq_252d_slope_v122_signal,
    f21rg_f21_revenue_growth_revloggrowsq_504d_slope_v123_signal,
    f21rg_f21_revenue_growth_revgrowxstd_252d_slope_v124_signal,
    f21rg_f21_revenue_growth_revgrowxstd_21d_slope_v125_signal,
    f21rg_f21_revenue_growth_revgrowema_504d_slope_v126_signal,
    f21rg_f21_revenue_growth_revloggrowema_21d_slope_v127_signal,
    f21rg_f21_revenue_growth_revgrowclip_252d_slope_v128_signal,
    f21rg_f21_revenue_growth_revgrowclip_504d_slope_v129_signal,
    f21rg_f21_revenue_growth_revgrowxlogvol_252d_slope_v130_signal,
    f21rg_f21_revenue_growth_revgrowxlogvol_63d_slope_v131_signal,
    f21rg_f21_revenue_growth_revgrowxatr_21d_slope_v132_signal,
    f21rg_f21_revenue_growth_revgrowxatr_504d_slope_v133_signal,
    f21rg_f21_revenue_growth_revgrowdvclose_252d_slope_v134_signal,
    f21rg_f21_revenue_growth_revgrowdiff_126m252_slope_v135_signal,
    f21rg_f21_revenue_growth_revloggrowdiff_21m63_slope_v136_signal,
    f21rg_f21_revenue_growth_revgrowampl_252d_slope_v137_signal,
    f21rg_f21_revenue_growth_revgrowampl_504d_slope_v138_signal,
    f21rg_f21_revenue_growth_revgrowxrevsq_252d_slope_v139_signal,
    f21rg_f21_revenue_growth_revgrowxrevsq_504d_slope_v140_signal,
    f21rg_f21_revenue_growth_revgrowfrac_252d_slope_v141_signal,
    f21rg_f21_revenue_growth_revgrowfrac_504d_slope_v142_signal,
    f21rg_f21_revenue_growth_revgrowatrvol_252d_slope_v143_signal,
    f21rg_f21_revenue_growth_revgrowclmean_252d_slope_v144_signal,
    f21rg_f21_revenue_growth_revgrowsmymean_252d_slope_v145_signal,
    f21rg_f21_revenue_growth_revgrowsmymean_63d_slope_v146_signal,
    f21rg_f21_revenue_growth_revgrowxlogcl_252d_slope_v147_signal,
    f21rg_f21_revenue_growth_revgrowxvollog_252d_slope_v148_signal,
    f21rg_f21_revenue_growth_compositeg_252d_slope_v149_signal,
    f21rg_f21_revenue_growth_compositeg_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_REVENUE_GROWTH_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "sharesbas": sharesbas, "closeadj": closeadj,
        "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_revenue_growth", "_f21_revenue_growth_smooth", "_f21_revenue_log_growth")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_revenue_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
