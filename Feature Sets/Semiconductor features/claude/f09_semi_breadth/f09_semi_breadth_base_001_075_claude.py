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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f09_brd_diff(brd, n):
    return brd - brd.shift(n)


def _f09_brd_dev(brd, w):
    return brd - brd.rolling(w, min_periods=max(1, w // 2)).mean()


def _f09_brd_thrust(brd, threshold=0.5):
    return (brd > threshold).astype(float)


def _f09_brd_above_ma(brd, w):
    return (brd > brd.rolling(w, min_periods=max(1, w // 2)).mean()).astype(float)


# 21d mean of semi basket breadth
def f09br_f09_semi_breadth_brdmean_21d_base_v001_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _mean(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of semi basket breadth
def f09br_f09_semi_breadth_brdmean_63d_base_v002_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _mean(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of semi basket breadth
def f09br_f09_semi_breadth_brdmean_126d_base_v003_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _mean(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of semi basket breadth
def f09br_f09_semi_breadth_brdmean_252d_base_v004_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _mean(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of semi basket breadth
def f09br_f09_semi_breadth_brdmean_504d_base_v005_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _mean(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of semi basket breadth
def f09br_f09_semi_breadth_brdz_21d_base_v006_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of semi basket breadth
def f09br_f09_semi_breadth_brdz_63d_base_v007_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of semi basket breadth
def f09br_f09_semi_breadth_brdz_126d_base_v008_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of semi basket breadth
def f09br_f09_semi_breadth_brdz_252d_base_v009_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of semi basket breadth
def f09br_f09_semi_breadth_brdz_504d_base_v010_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation of breadth from rolling mean
def f09br_f09_semi_breadth_brddev_21d_base_v011_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation of breadth from rolling mean
def f09br_f09_semi_breadth_brddev_63d_base_v012_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation of breadth from rolling mean
def f09br_f09_semi_breadth_brddev_126d_base_v013_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation of breadth from rolling mean
def f09br_f09_semi_breadth_brddev_252d_base_v014_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - _mean(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation of breadth from rolling mean
def f09br_f09_semi_breadth_brddev_504d_base_v015_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - _mean(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of breadth (median/MAD)
def f09br_f09_semi_breadth_brdrobustz_21d_base_v016_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    med = semi_basket_breadth.rolling(21, min_periods=11).median()
    mad = (semi_basket_breadth - med).abs().rolling(21, min_periods=11).median()
    result = (semi_basket_breadth - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of breadth (median/MAD)
def f09br_f09_semi_breadth_brdrobustz_63d_base_v017_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    med = semi_basket_breadth.rolling(63, min_periods=32).median()
    mad = (semi_basket_breadth - med).abs().rolling(63, min_periods=32).median()
    result = (semi_basket_breadth - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of breadth (median/MAD)
def f09br_f09_semi_breadth_brdrobustz_126d_base_v018_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    med = semi_basket_breadth.rolling(126, min_periods=63).median()
    mad = (semi_basket_breadth - med).abs().rolling(126, min_periods=63).median()
    result = (semi_basket_breadth - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of breadth (median/MAD)
def f09br_f09_semi_breadth_brdrobustz_252d_base_v019_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    med = semi_basket_breadth.rolling(252, min_periods=126).median()
    mad = (semi_basket_breadth - med).abs().rolling(252, min_periods=126).median()
    result = (semi_basket_breadth - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of breadth (median/MAD)
def f09br_f09_semi_breadth_brdrobustz_504d_base_v020_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    med = semi_basket_breadth.rolling(504, min_periods=252).median()
    mad = (semi_basket_breadth - med).abs().rolling(504, min_periods=252).median()
    result = (semi_basket_breadth - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of semi basket breadth
def f09br_f09_semi_breadth_brdstd_21d_base_v021_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _std(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of semi basket breadth
def f09br_f09_semi_breadth_brdstd_63d_base_v022_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _std(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of semi basket breadth
def f09br_f09_semi_breadth_brdstd_126d_base_v023_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _std(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of semi basket breadth
def f09br_f09_semi_breadth_brdstd_252d_base_v024_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _std(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of semi basket breadth
def f09br_f09_semi_breadth_brdstd_504d_base_v025_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _std(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days breadth above 0.5 (bullish thrust)
def f09br_f09_semi_breadth_brdthrustup_21d_base_v026_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days breadth above 0.5 (bullish thrust)
def f09br_f09_semi_breadth_brdthrustup_63d_base_v027_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days breadth above 0.5 (bullish thrust)
def f09br_f09_semi_breadth_brdthrustup_126d_base_v028_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days breadth above 0.5 (bullish thrust)
def f09br_f09_semi_breadth_brdthrustup_252d_base_v029_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days breadth above 0.5 (bullish thrust)
def f09br_f09_semi_breadth_brdthrustup_504d_base_v030_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth > 0.5).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days breadth below 0.5 (bearish thrust)
def f09br_f09_semi_breadth_brdthrustdn_21d_base_v031_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth < 0.5).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days breadth below 0.5 (bearish thrust)
def f09br_f09_semi_breadth_brdthrustdn_63d_base_v032_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth < 0.5).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days breadth below 0.5 (bearish thrust)
def f09br_f09_semi_breadth_brdthrustdn_126d_base_v033_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth < 0.5).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days breadth below 0.5 (bearish thrust)
def f09br_f09_semi_breadth_brdthrustdn_252d_base_v034_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth < 0.5).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days breadth below 0.5 (bearish thrust)
def f09br_f09_semi_breadth_brdthrustdn_504d_base_v035_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth < 0.5).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio breadth above its rolling mean
def f09br_f09_semi_breadth_brdabovemafrac_21d_base_v036_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    ma = _mean(semi_basket_breadth, 21)
    result = (semi_basket_breadth > ma).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio breadth above its rolling mean
def f09br_f09_semi_breadth_brdabovemafrac_63d_base_v037_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    ma = _mean(semi_basket_breadth, 63)
    result = (semi_basket_breadth > ma).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio breadth above its rolling mean
def f09br_f09_semi_breadth_brdabovemafrac_126d_base_v038_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    ma = _mean(semi_basket_breadth, 126)
    result = (semi_basket_breadth > ma).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio breadth above its rolling mean
def f09br_f09_semi_breadth_brdabovemafrac_252d_base_v039_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    ma = _mean(semi_basket_breadth, 252)
    result = (semi_basket_breadth > ma).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio breadth above its rolling mean
def f09br_f09_semi_breadth_brdabovemafrac_504d_base_v040_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    ma = _mean(semi_basket_breadth, 504)
    result = (semi_basket_breadth > ma).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of semi basket breadth
def f09br_f09_semi_breadth_brdmax_21d_base_v041_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of semi basket breadth
def f09br_f09_semi_breadth_brdmax_63d_base_v042_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of semi basket breadth
def f09br_f09_semi_breadth_brdmax_126d_base_v043_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of semi basket breadth
def f09br_f09_semi_breadth_brdmax_252d_base_v044_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of semi basket breadth
def f09br_f09_semi_breadth_brdmax_504d_base_v045_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of semi basket breadth
def f09br_f09_semi_breadth_brdmin_21d_base_v046_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _min(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of semi basket breadth
def f09br_f09_semi_breadth_brdmin_63d_base_v047_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _min(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of semi basket breadth
def f09br_f09_semi_breadth_brdmin_126d_base_v048_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _min(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of semi basket breadth
def f09br_f09_semi_breadth_brdmin_252d_base_v049_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _min(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of semi basket breadth
def f09br_f09_semi_breadth_brdmin_504d_base_v050_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _min(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of semi basket breadth
def f09br_f09_semi_breadth_brdrng_21d_base_v051_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 21) - _min(semi_basket_breadth, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of semi basket breadth
def f09br_f09_semi_breadth_brdrng_63d_base_v052_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of semi basket breadth
def f09br_f09_semi_breadth_brdrng_126d_base_v053_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of semi basket breadth
def f09br_f09_semi_breadth_brdrng_252d_base_v054_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of semi basket breadth
def f09br_f09_semi_breadth_brdrng_504d_base_v055_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _max(semi_basket_breadth, 504) - _min(semi_basket_breadth, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d breadth position-in-range
def f09br_f09_semi_breadth_brdpos_21d_base_v056_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 21)
    hi = _max(semi_basket_breadth, 21)
    result = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d breadth position-in-range
def f09br_f09_semi_breadth_brdpos_63d_base_v057_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    result = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breadth position-in-range
def f09br_f09_semi_breadth_brdpos_126d_base_v058_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 126)
    hi = _max(semi_basket_breadth, 126)
    result = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breadth position-in-range
def f09br_f09_semi_breadth_brdpos_252d_base_v059_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    result = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d breadth position-in-range
def f09br_f09_semi_breadth_brdpos_504d_base_v060_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 504)
    hi = _max(semi_basket_breadth, 504)
    result = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d breadth drawdown from rolling peak
def f09br_f09_semi_breadth_brddd_21d_base_v061_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    peak = _max(semi_basket_breadth, 21)
    result = semi_basket_breadth - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d breadth drawdown from rolling peak
def f09br_f09_semi_breadth_brddd_63d_base_v062_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    peak = _max(semi_basket_breadth, 63)
    result = semi_basket_breadth - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breadth drawdown from rolling peak
def f09br_f09_semi_breadth_brddd_126d_base_v063_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    peak = _max(semi_basket_breadth, 126)
    result = semi_basket_breadth - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breadth drawdown from rolling peak
def f09br_f09_semi_breadth_brddd_252d_base_v064_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    peak = _max(semi_basket_breadth, 252)
    result = semi_basket_breadth - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d breadth drawdown from rolling peak
def f09br_f09_semi_breadth_brddd_504d_base_v065_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    peak = _max(semi_basket_breadth, 504)
    result = semi_basket_breadth - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d breadth run-up above rolling trough
def f09br_f09_semi_breadth_brdup_21d_base_v066_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    trough = _min(semi_basket_breadth, 21)
    result = semi_basket_breadth - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d breadth run-up above rolling trough
def f09br_f09_semi_breadth_brdup_63d_base_v067_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    trough = _min(semi_basket_breadth, 63)
    result = semi_basket_breadth - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breadth run-up above rolling trough
def f09br_f09_semi_breadth_brdup_126d_base_v068_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    trough = _min(semi_basket_breadth, 126)
    result = semi_basket_breadth - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breadth run-up above rolling trough
def f09br_f09_semi_breadth_brdup_252d_base_v069_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    trough = _min(semi_basket_breadth, 252)
    result = semi_basket_breadth - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d breadth run-up above rolling trough
def f09br_f09_semi_breadth_brdup_504d_base_v070_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    trough = _min(semi_basket_breadth, 504)
    result = semi_basket_breadth - trough
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EMA crossover 5v21
def f09br_f09_semi_breadth_brdema_5v21_base_v071_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.ewm(span=5, adjust=False).mean() - semi_basket_breadth.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EMA crossover 21v63
def f09br_f09_semi_breadth_brdema_21v63_base_v072_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.ewm(span=21, adjust=False).mean() - semi_basket_breadth.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EMA crossover 63v126
def f09br_f09_semi_breadth_brdema_63v126_base_v073_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.ewm(span=63, adjust=False).mean() - semi_basket_breadth.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EMA crossover 126v252
def f09br_f09_semi_breadth_brdema_126v252_base_v074_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.ewm(span=126, adjust=False).mean() - semi_basket_breadth.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# breadth EMA crossover 252v504
def f09br_f09_semi_breadth_brdema_252v504_base_v075_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.ewm(span=252, adjust=False).mean() - semi_basket_breadth.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
