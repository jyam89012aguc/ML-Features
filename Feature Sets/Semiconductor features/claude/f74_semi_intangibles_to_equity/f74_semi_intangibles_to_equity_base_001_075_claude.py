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
def _f74_int_eq(intangibles, equity):
    return intangibles / equity.replace(0, np.nan)


# 21d mean of intq
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_base_v001_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of intq
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_base_v002_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of intq
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_base_v003_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of intq
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_base_v004_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of intq
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_base_v005_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of intq
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_base_v006_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of intq
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_base_v007_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of intq
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_base_v008_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of intq
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_base_v009_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of intq
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_base_v010_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of intq (median/MAD)
def f74ie_f74_semi_intangibles_to_equity_intq_robustz_21d_base_v011_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of intq (median/MAD)
def f74ie_f74_semi_intangibles_to_equity_intq_robustz_63d_base_v012_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of intq (median/MAD)
def f74ie_f74_semi_intangibles_to_equity_intq_robustz_126d_base_v013_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of intq (median/MAD)
def f74ie_f74_semi_intangibles_to_equity_intq_robustz_252d_base_v014_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of intq (median/MAD)
def f74ie_f74_semi_intangibles_to_equity_intq_robustz_504d_base_v015_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of intq
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_base_v016_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of intq
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_base_v017_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of intq
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_base_v018_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of intq
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_base_v019_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of intq
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_base_v020_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of intq
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_base_v021_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of intq
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_base_v022_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of intq
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_base_v023_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of intq
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_base_v024_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of intq
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_base_v025_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of intq
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_base_v026_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 21) - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of intq
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_base_v027_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 63) - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of intq
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_base_v028_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 126) - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of intq
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_base_v029_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 252) - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of intq
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_base_v030_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _max(r, 504) - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of intq in rolling range
def f74ie_f74_semi_intangibles_to_equity_intq_pos_21d_base_v031_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    lo = _min(r, 21)
    hi = _max(r, 21)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of intq in rolling range
def f74ie_f74_semi_intangibles_to_equity_intq_pos_63d_base_v032_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    lo = _min(r, 63)
    hi = _max(r, 63)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of intq in rolling range
def f74ie_f74_semi_intangibles_to_equity_intq_pos_126d_base_v033_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    lo = _min(r, 126)
    hi = _max(r, 126)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of intq in rolling range
def f74ie_f74_semi_intangibles_to_equity_intq_pos_252d_base_v034_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    lo = _min(r, 252)
    hi = _max(r, 252)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of intq in rolling range
def f74ie_f74_semi_intangibles_to_equity_intq_pos_504d_base_v035_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    lo = _min(r, 504)
    hi = _max(r, 504)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of intq from peak
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_base_v036_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of intq from peak
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_base_v037_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of intq from peak
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_base_v038_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of intq from peak
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_base_v039_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of intq from peak
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_base_v040_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of intq above trough
def f74ie_f74_semi_intangibles_to_equity_intq_up_21d_base_v041_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    trough = _min(r, 21)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of intq above trough
def f74ie_f74_semi_intangibles_to_equity_intq_up_63d_base_v042_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    trough = _min(r, 63)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of intq above trough
def f74ie_f74_semi_intangibles_to_equity_intq_up_126d_base_v043_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    trough = _min(r, 126)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of intq above trough
def f74ie_f74_semi_intangibles_to_equity_intq_up_252d_base_v044_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    trough = _min(r, 252)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of intq above trough
def f74ie_f74_semi_intangibles_to_equity_intq_up_504d_base_v045_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    trough = _min(r, 504)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of intq
def f74ie_f74_semi_intangibles_to_equity_intq_std_21d_base_v046_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _std(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of intq
def f74ie_f74_semi_intangibles_to_equity_intq_std_63d_base_v047_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _std(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of intq
def f74ie_f74_semi_intangibles_to_equity_intq_std_126d_base_v048_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of intq
def f74ie_f74_semi_intangibles_to_equity_intq_std_252d_base_v049_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _std(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of intq
def f74ie_f74_semi_intangibles_to_equity_intq_std_504d_base_v050_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = _std(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of intq
def f74ie_f74_semi_intangibles_to_equity_intq_skew_21d_base_v051_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of intq
def f74ie_f74_semi_intangibles_to_equity_intq_skew_63d_base_v052_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of intq
def f74ie_f74_semi_intangibles_to_equity_intq_skew_126d_base_v053_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of intq
def f74ie_f74_semi_intangibles_to_equity_intq_skew_252d_base_v054_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of intq
def f74ie_f74_semi_intangibles_to_equity_intq_skew_504d_base_v055_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of intq
def f74ie_f74_semi_intangibles_to_equity_intq_kurt_21d_base_v056_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of intq
def f74ie_f74_semi_intangibles_to_equity_intq_kurt_63d_base_v057_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of intq
def f74ie_f74_semi_intangibles_to_equity_intq_kurt_126d_base_v058_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of intq
def f74ie_f74_semi_intangibles_to_equity_intq_kurt_252d_base_v059_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of intq
def f74ie_f74_semi_intangibles_to_equity_intq_kurt_504d_base_v060_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of intq above rolling median
def f74ie_f74_semi_intangibles_to_equity_intq_hit_21d_base_v061_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(21, min_periods=11).median()
    result = (r > med).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of intq above rolling median
def f74ie_f74_semi_intangibles_to_equity_intq_hit_63d_base_v062_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(63, min_periods=32).median()
    result = (r > med).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of intq above rolling median
def f74ie_f74_semi_intangibles_to_equity_intq_hit_126d_base_v063_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(126, min_periods=63).median()
    result = (r > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of intq above rolling median
def f74ie_f74_semi_intangibles_to_equity_intq_hit_252d_base_v064_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(252, min_periods=126).median()
    result = (r > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of intq above rolling median
def f74ie_f74_semi_intangibles_to_equity_intq_hit_504d_base_v065_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    med = r.rolling(504, min_periods=252).median()
    result = (r > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed-cumsum of intq changes
def f74ie_f74_semi_intangibles_to_equity_intq_signcum_21d_base_v066_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed-cumsum of intq changes
def f74ie_f74_semi_intangibles_to_equity_intq_signcum_63d_base_v067_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed-cumsum of intq changes
def f74ie_f74_semi_intangibles_to_equity_intq_signcum_126d_base_v068_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed-cumsum of intq changes
def f74ie_f74_semi_intangibles_to_equity_intq_signcum_252d_base_v069_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed-cumsum of intq changes
def f74ie_f74_semi_intangibles_to_equity_intq_signcum_504d_base_v070_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vs 21d EMA crossover of intq
def f74ie_f74_semi_intangibles_to_equity_intq_ema_5v21_base_v071_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 63d EMA crossover of intq
def f74ie_f74_semi_intangibles_to_equity_intq_ema_21v63_base_v072_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 126d EMA crossover of intq
def f74ie_f74_semi_intangibles_to_equity_intq_ema_63v126_base_v073_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 252d EMA crossover of intq
def f74ie_f74_semi_intangibles_to_equity_intq_ema_126v252_base_v074_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vs 504d EMA crossover of intq
def f74ie_f74_semi_intangibles_to_equity_intq_ema_252v504_base_v075_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
