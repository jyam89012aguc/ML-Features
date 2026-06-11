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
def _f088_disthigh(close, w):
    hi = close.rolling(w, min_periods=max(1, w//2)).max()
    return (close - hi) / hi.replace(0, np.nan).abs()


# 21d mean of disthigh_252d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_mean_21d_base_v001_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of disthigh_252d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_mean_63d_base_v002_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of disthigh_252d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_mean_126d_base_v003_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of disthigh_252d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_mean_252d_base_v004_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of disthigh_252d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_mean_504d_base_v005_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of disthigh_504d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_mean_21d_base_v006_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of disthigh_504d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_mean_63d_base_v007_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of disthigh_504d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_mean_126d_base_v008_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of disthigh_504d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_mean_252d_base_v009_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of disthigh_504d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_mean_504d_base_v010_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of disthigh_756d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_mean_21d_base_v011_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of disthigh_756d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_mean_63d_base_v012_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of disthigh_756d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_mean_126d_base_v013_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of disthigh_756d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_mean_252d_base_v014_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of disthigh_756d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_mean_504d_base_v015_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of disthigh_1260d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_mean_21d_base_v016_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of disthigh_1260d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_mean_63d_base_v017_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of disthigh_1260d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_mean_126d_base_v018_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of disthigh_1260d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_mean_252d_base_v019_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of disthigh_1260d scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_mean_504d_base_v020_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of new_high_252_flag scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_mean_21d_base_v021_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of new_high_252_flag scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_mean_63d_base_v022_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of new_high_252_flag scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_mean_126d_base_v023_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of new_high_252_flag scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_mean_252d_base_v024_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of new_high_252_flag scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_mean_504d_base_v025_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of high_pctile_504 scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_mean_21d_base_v026_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of high_pctile_504 scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_mean_63d_base_v027_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of high_pctile_504 scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_mean_126d_base_v028_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of high_pctile_504 scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_mean_252d_base_v029_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of high_pctile_504 scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_mean_504d_base_v030_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of days_since_252high scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_mean_21d_base_v031_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of days_since_252high scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_mean_63d_base_v032_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of days_since_252high scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_mean_126d_base_v033_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of days_since_252high scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_mean_252d_base_v034_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of days_since_252high scaled by closeadj
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_mean_504d_base_v035_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_median_63d_base_v036_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_median_252d_base_v037_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_median_504d_base_v038_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_median_63d_base_v039_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_median_252d_base_v040_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_median_504d_base_v041_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_median_63d_base_v042_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_median_252d_base_v043_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_median_504d_base_v044_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_median_63d_base_v045_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_median_252d_base_v046_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_median_504d_base_v047_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_median_63d_base_v048_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_median_252d_base_v049_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_median_504d_base_v050_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_median_63d_base_v051_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_median_252d_base_v052_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_median_504d_base_v053_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_median_63d_base_v054_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_median_252d_base_v055_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_median_504d_base_v056_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_rmax_252d_base_v057_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_rmax_504d_base_v058_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_rmax_252d_base_v059_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_rmax_504d_base_v060_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_rmax_252d_base_v061_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_rmax_504d_base_v062_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_rmax_252d_base_v063_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_rmax_504d_base_v064_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_rmax_252d_base_v065_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_rmax_504d_base_v066_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_rmax_252d_base_v067_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_rmax_504d_base_v068_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_rmax_252d_base_v069_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_rmax_504d_base_v070_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_rmin_252d_base_v071_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_rmin_504d_base_v072_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_rmin_252d_base_v073_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_rmin_504d_base_v074_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_rmin_252d_base_v075_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

