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
def _f84ey_own_ey(pe):
    return 1.0 / pe.replace(0, np.nan)


def _f84ey_spread(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) - sp500_ey_avg


def _f84ey_ratio(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) / sp500_ey_avg.replace(0, np.nan)


def _f84ey_log_ratio(pe, sp500_ey_avg):
    own = 1.0 / pe.replace(0, np.nan)
    return np.log(own.abs() / sp500_ey_avg.replace(0, np.nan).abs())


# 21d level of own earnings yield (1/pe)
def f84ey_f84_semi_ey_spread_owney_21d_base_v001_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _mean(own, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of own earnings yield
def f84ey_f84_semi_ey_spread_owney_63d_base_v002_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _mean(own, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of own earnings yield
def f84ey_f84_semi_ey_spread_owney_126d_base_v003_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _mean(own, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of own earnings yield
def f84ey_f84_semi_ey_spread_owney_252d_base_v004_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _mean(own, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of own earnings yield
def f84ey_f84_semi_ey_spread_owney_504d_base_v005_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _mean(own, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of EY spread vs SP500
def f84ey_f84_semi_ey_spread_spread_21d_base_v006_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _mean(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of EY spread vs SP500
def f84ey_f84_semi_ey_spread_spread_63d_base_v007_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _mean(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of EY spread vs SP500
def f84ey_f84_semi_ey_spread_spread_126d_base_v008_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _mean(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of EY spread vs SP500
def f84ey_f84_semi_ey_spread_spread_252d_base_v009_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _mean(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of EY spread vs SP500
def f84ey_f84_semi_ey_spread_spread_504d_base_v010_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _mean(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of EY spread
def f84ey_f84_semi_ey_spread_spreadz_21d_base_v011_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of EY spread
def f84ey_f84_semi_ey_spread_spreadz_63d_base_v012_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of EY spread
def f84ey_f84_semi_ey_spread_spreadz_126d_base_v013_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of EY spread
def f84ey_f84_semi_ey_spread_spreadz_252d_base_v014_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of EY spread
def f84ey_f84_semi_ey_spread_spreadz_504d_base_v015_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score (median/MAD) of EY spread
def f84ey_f84_semi_ey_spread_spreadrobustz_21d_base_v016_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(21, min_periods=11).median()
    mad = (sp - med).abs().rolling(21, min_periods=11).median()
    result = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score (median/MAD) of EY spread
def f84ey_f84_semi_ey_spread_spreadrobustz_63d_base_v017_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(63, min_periods=32).median()
    mad = (sp - med).abs().rolling(63, min_periods=32).median()
    result = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score (median/MAD) of EY spread
def f84ey_f84_semi_ey_spread_spreadrobustz_126d_base_v018_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(126, min_periods=63).median()
    mad = (sp - med).abs().rolling(126, min_periods=63).median()
    result = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score (median/MAD) of EY spread
def f84ey_f84_semi_ey_spread_spreadrobustz_252d_base_v019_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(252, min_periods=126).median()
    mad = (sp - med).abs().rolling(252, min_periods=126).median()
    result = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score (median/MAD) of EY spread
def f84ey_f84_semi_ey_spread_spreadrobustz_504d_base_v020_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(504, min_periods=252).median()
    mad = (sp - med).abs().rolling(504, min_periods=252).median()
    result = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of EY spread
def f84ey_f84_semi_ey_spread_spreadmax_21d_base_v021_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of EY spread
def f84ey_f84_semi_ey_spread_spreadmax_63d_base_v022_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of EY spread
def f84ey_f84_semi_ey_spread_spreadmax_126d_base_v023_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of EY spread
def f84ey_f84_semi_ey_spread_spreadmax_252d_base_v024_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of EY spread
def f84ey_f84_semi_ey_spread_spreadmax_504d_base_v025_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of EY spread
def f84ey_f84_semi_ey_spread_spreadmin_21d_base_v026_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _min(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of EY spread
def f84ey_f84_semi_ey_spread_spreadmin_63d_base_v027_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _min(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of EY spread
def f84ey_f84_semi_ey_spread_spreadmin_126d_base_v028_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _min(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of EY spread
def f84ey_f84_semi_ey_spread_spreadmin_252d_base_v029_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _min(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of EY spread
def f84ey_f84_semi_ey_spread_spreadmin_504d_base_v030_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _min(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of EY spread (max - min)
def f84ey_f84_semi_ey_spread_spreadrng_21d_base_v031_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 21) - _min(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of EY spread (max - min)
def f84ey_f84_semi_ey_spread_spreadrng_63d_base_v032_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 63) - _min(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of EY spread (max - min)
def f84ey_f84_semi_ey_spread_spreadrng_126d_base_v033_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 126) - _min(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of EY spread (max - min)
def f84ey_f84_semi_ey_spread_spreadrng_252d_base_v034_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 252) - _min(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of EY spread (max - min)
def f84ey_f84_semi_ey_spread_spreadrng_504d_base_v035_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _max(sp, 504) - _min(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of EY spread
def f84ey_f84_semi_ey_spread_spreadpos_21d_base_v036_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 21)
    hi = _max(sp, 21)
    result = (sp - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of EY spread
def f84ey_f84_semi_ey_spread_spreadpos_63d_base_v037_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 63)
    hi = _max(sp, 63)
    result = (sp - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of EY spread
def f84ey_f84_semi_ey_spread_spreadpos_126d_base_v038_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 126)
    hi = _max(sp, 126)
    result = (sp - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of EY spread
def f84ey_f84_semi_ey_spread_spreadpos_252d_base_v039_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 252)
    hi = _max(sp, 252)
    result = (sp - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of EY spread
def f84ey_f84_semi_ey_spread_spreadpos_504d_base_v040_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 504)
    hi = _max(sp, 504)
    result = (sp - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of EY spread from rolling peak
def f84ey_f84_semi_ey_spread_spreaddd_21d_base_v041_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    peak = _max(sp, 21)
    result = sp - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of EY spread from rolling peak
def f84ey_f84_semi_ey_spread_spreaddd_63d_base_v042_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    peak = _max(sp, 63)
    result = sp - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of EY spread from rolling peak
def f84ey_f84_semi_ey_spread_spreaddd_126d_base_v043_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    peak = _max(sp, 126)
    result = sp - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of EY spread from rolling peak
def f84ey_f84_semi_ey_spread_spreaddd_252d_base_v044_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    peak = _max(sp, 252)
    result = sp - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of EY spread from rolling peak
def f84ey_f84_semi_ey_spread_spreaddd_504d_base_v045_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    peak = _max(sp, 504)
    result = sp - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of EY spread above rolling trough
def f84ey_f84_semi_ey_spread_spreadup_21d_base_v046_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    trough = _min(sp, 21)
    result = sp - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of EY spread above rolling trough
def f84ey_f84_semi_ey_spread_spreadup_63d_base_v047_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    trough = _min(sp, 63)
    result = sp - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of EY spread above rolling trough
def f84ey_f84_semi_ey_spread_spreadup_126d_base_v048_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    trough = _min(sp, 126)
    result = sp - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of EY spread above rolling trough
def f84ey_f84_semi_ey_spread_spreadup_252d_base_v049_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    trough = _min(sp, 252)
    result = sp - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of EY spread above rolling trough
def f84ey_f84_semi_ey_spread_spreadup_504d_base_v050_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    trough = _min(sp, 504)
    result = sp - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of EY spread (own cheaper vs SPY)
def f84ey_f84_semi_ey_spread_spreadsign_21d_base_v051_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = pd.Series(np.sign(sp), index=sp.index).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of EY spread
def f84ey_f84_semi_ey_spread_spreadsign_63d_base_v052_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = pd.Series(np.sign(sp), index=sp.index).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sign of EY spread
def f84ey_f84_semi_ey_spread_spreadsign_126d_base_v053_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = pd.Series(np.sign(sp), index=sp.index).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of EY spread
def f84ey_f84_semi_ey_spread_spreadsign_252d_base_v054_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = pd.Series(np.sign(sp), index=sp.index).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sign of EY spread
def f84ey_f84_semi_ey_spread_spreadsign_504d_base_v055_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = pd.Series(np.sign(sp), index=sp.index).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d streak of consecutive cheaper days (own EY > SP500 EY)
def f84ey_f84_semi_ey_spread_spreadstreak_21d_base_v056_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    cheap = (sp > 0).astype(float)
    result = cheap.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d streak of consecutive cheaper days
def f84ey_f84_semi_ey_spread_spreadstreak_63d_base_v057_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    cheap = (sp > 0).astype(float)
    result = cheap.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d streak of consecutive cheaper days
def f84ey_f84_semi_ey_spread_spreadstreak_126d_base_v058_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    cheap = (sp > 0).astype(float)
    result = cheap.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d streak of consecutive cheaper days
def f84ey_f84_semi_ey_spread_spreadstreak_252d_base_v059_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    cheap = (sp > 0).astype(float)
    result = cheap.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d streak of consecutive cheaper days
def f84ey_f84_semi_ey_spread_spreadstreak_504d_base_v060_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    cheap = (sp > 0).astype(float)
    result = cheap.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of own_ey/sp500_ey ratio
def f84ey_f84_semi_ey_spread_ratio_21d_base_v061_signal(pe, sp500_ey_avg, closeadj):
    r = _f84ey_ratio(pe, sp500_ey_avg)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of own_ey/sp500_ey ratio
def f84ey_f84_semi_ey_spread_ratio_63d_base_v062_signal(pe, sp500_ey_avg, closeadj):
    r = _f84ey_ratio(pe, sp500_ey_avg)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of own_ey/sp500_ey ratio
def f84ey_f84_semi_ey_spread_ratio_126d_base_v063_signal(pe, sp500_ey_avg, closeadj):
    r = _f84ey_ratio(pe, sp500_ey_avg)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of own_ey/sp500_ey ratio
def f84ey_f84_semi_ey_spread_ratio_252d_base_v064_signal(pe, sp500_ey_avg, closeadj):
    r = _f84ey_ratio(pe, sp500_ey_avg)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of own_ey/sp500_ey ratio
def f84ey_f84_semi_ey_spread_ratio_504d_base_v065_signal(pe, sp500_ey_avg, closeadj):
    r = _f84ey_ratio(pe, sp500_ey_avg)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-ratio of own_ey to sp500_ey
def f84ey_f84_semi_ey_spread_logratio_21d_base_v066_signal(pe, sp500_ey_avg, closeadj):
    lr = _f84ey_log_ratio(pe, sp500_ey_avg)
    result = _mean(lr, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-ratio of own_ey to sp500_ey
def f84ey_f84_semi_ey_spread_logratio_63d_base_v067_signal(pe, sp500_ey_avg, closeadj):
    lr = _f84ey_log_ratio(pe, sp500_ey_avg)
    result = _mean(lr, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-ratio of own_ey to sp500_ey
def f84ey_f84_semi_ey_spread_logratio_126d_base_v068_signal(pe, sp500_ey_avg, closeadj):
    lr = _f84ey_log_ratio(pe, sp500_ey_avg)
    result = _mean(lr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-ratio of own_ey to sp500_ey
def f84ey_f84_semi_ey_spread_logratio_252d_base_v069_signal(pe, sp500_ey_avg, closeadj):
    lr = _f84ey_log_ratio(pe, sp500_ey_avg)
    result = _mean(lr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-ratio of own_ey to sp500_ey
def f84ey_f84_semi_ey_spread_logratio_504d_base_v070_signal(pe, sp500_ey_avg, closeadj):
    lr = _f84ey_log_ratio(pe, sp500_ey_avg)
    result = _mean(lr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_5v21_base_v071_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.ewm(span=5, adjust=False).mean() - sp.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_21v63_base_v072_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.ewm(span=21, adjust=False).mean() - sp.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_63v126_base_v073_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.ewm(span=63, adjust=False).mean() - sp.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_126v252_base_v074_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.ewm(span=126, adjust=False).mean() - sp.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_252v504_base_v075_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.ewm(span=252, adjust=False).mean() - sp.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
