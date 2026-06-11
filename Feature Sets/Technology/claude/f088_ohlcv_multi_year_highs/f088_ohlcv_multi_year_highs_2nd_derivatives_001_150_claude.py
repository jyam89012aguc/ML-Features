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
def _f088_disthigh(close, w):
    hi = close.rolling(w, min_periods=max(1, w//2)).max()
    return (close - hi) / hi.replace(0, np.nan).abs()


# 21d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_slope_21d_2d_v001_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_slope_63d_2d_v002_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_slope_126d_2d_v003_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_slope_252d_2d_v004_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_slope_504d_2d_v005_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_slope_21d_2d_v006_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_slope_63d_2d_v007_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_slope_126d_2d_v008_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_slope_252d_2d_v009_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_slope_504d_2d_v010_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_slope_21d_2d_v011_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_slope_63d_2d_v012_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_slope_126d_2d_v013_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_slope_252d_2d_v014_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_slope_504d_2d_v015_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_slope_21d_2d_v016_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_slope_63d_2d_v017_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_slope_126d_2d_v018_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_slope_252d_2d_v019_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_slope_504d_2d_v020_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_slope_21d_2d_v021_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_slope_63d_2d_v022_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_slope_126d_2d_v023_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_slope_252d_2d_v024_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_slope_504d_2d_v025_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_slope_21d_2d_v026_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_slope_63d_2d_v027_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_slope_126d_2d_v028_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_slope_252d_2d_v029_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_slope_504d_2d_v030_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_slope_21d_2d_v031_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_slope_63d_2d_v032_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_slope_126d_2d_v033_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_slope_252d_2d_v034_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_slope_504d_2d_v035_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sm21_sl21_2d_v036_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sm63_sl21_2d_v037_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sm63_sl63_2d_v038_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sm252_sl63_2d_v039_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sm252_sl126_2d_v040_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sm21_sl21_2d_v041_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sm63_sl21_2d_v042_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sm63_sl63_2d_v043_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sm252_sl63_2d_v044_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sm252_sl126_2d_v045_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sm21_sl21_2d_v046_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 756), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sm63_sl21_2d_v047_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 756), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sm63_sl63_2d_v048_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 756), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sm252_sl63_2d_v049_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 756), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sm252_sl126_2d_v050_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 756), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sm21_sl21_2d_v051_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 1260), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sm63_sl21_2d_v052_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 1260), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sm63_sl63_2d_v053_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 1260), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sm252_sl63_2d_v054_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 1260), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sm252_sl126_2d_v055_signal(closeadj):
    base = _mean(_f088_disthigh(closeadj, 1260), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sm21_sl21_2d_v056_signal(closeadj):
    base = _mean((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sm63_sl21_2d_v057_signal(closeadj):
    base = _mean((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sm63_sl63_2d_v058_signal(closeadj):
    base = _mean((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sm252_sl63_2d_v059_signal(closeadj):
    base = _mean((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sm252_sl126_2d_v060_signal(closeadj):
    base = _mean((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sm21_sl21_2d_v061_signal(closeadj):
    base = _mean(closeadj.rolling(504, min_periods=126).rank(pct=True), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sm63_sl21_2d_v062_signal(closeadj):
    base = _mean(closeadj.rolling(504, min_periods=126).rank(pct=True), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sm63_sl63_2d_v063_signal(closeadj):
    base = _mean(closeadj.rolling(504, min_periods=126).rank(pct=True), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sm252_sl63_2d_v064_signal(closeadj):
    base = _mean(closeadj.rolling(504, min_periods=126).rank(pct=True), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sm252_sl126_2d_v065_signal(closeadj):
    base = _mean(closeadj.rolling(504, min_periods=126).rank(pct=True), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sm21_sl21_2d_v066_signal(closeadj):
    base = _mean((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sm63_sl21_2d_v067_signal(closeadj):
    base = _mean((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sm63_sl63_2d_v068_signal(closeadj):
    base = _mean((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sm252_sl63_2d_v069_signal(closeadj):
    base = _mean((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sm252_sl126_2d_v070_signal(closeadj):
    base = _mean((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_pctslope_21d_2d_v071_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_pctslope_63d_2d_v072_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_pctslope_252d_2d_v073_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_pctslope_21d_2d_v074_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_pctslope_63d_2d_v075_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_pctslope_252d_2d_v076_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_pctslope_21d_2d_v077_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_pctslope_63d_2d_v078_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_pctslope_252d_2d_v079_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_pctslope_21d_2d_v080_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_pctslope_63d_2d_v081_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_pctslope_252d_2d_v082_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_pctslope_21d_2d_v083_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_pctslope_63d_2d_v084_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_pctslope_252d_2d_v085_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_pctslope_21d_2d_v086_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_pctslope_63d_2d_v087_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_pctslope_252d_2d_v088_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_pctslope_21d_2d_v089_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_pctslope_63d_2d_v090_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_pctslope_252d_2d_v091_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sgnslope_21d_2d_v092_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sgnslope_63d_2d_v093_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_sgnslope_252d_2d_v094_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sgnslope_21d_2d_v095_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sgnslope_63d_2d_v096_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_sgnslope_252d_2d_v097_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sgnslope_21d_2d_v098_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sgnslope_63d_2d_v099_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_sgnslope_252d_2d_v100_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sgnslope_21d_2d_v101_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sgnslope_63d_2d_v102_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_sgnslope_252d_2d_v103_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sgnslope_21d_2d_v104_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sgnslope_63d_2d_v105_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_sgnslope_252d_2d_v106_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sgnslope_21d_2d_v107_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sgnslope_63d_2d_v108_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_sgnslope_252d_2d_v109_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sgnslope_21d_2d_v110_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sgnslope_63d_2d_v111_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_sgnslope_252d_2d_v112_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_logmagslope_21d_2d_v113_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_logmagslope_63d_2d_v114_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of disthigh_252d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_logmagslope_252d_2d_v115_signal(closeadj):
    base = _f088_disthigh(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_logmagslope_21d_2d_v116_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_logmagslope_63d_2d_v117_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of disthigh_504d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_logmagslope_252d_2d_v118_signal(closeadj):
    base = _f088_disthigh(closeadj, 504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_logmagslope_21d_2d_v119_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_logmagslope_63d_2d_v120_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of disthigh_756d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_logmagslope_252d_2d_v121_signal(closeadj):
    base = _f088_disthigh(closeadj, 756)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_logmagslope_21d_2d_v122_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_logmagslope_63d_2d_v123_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of disthigh_1260d
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_logmagslope_252d_2d_v124_signal(closeadj):
    base = _f088_disthigh(closeadj, 1260)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_logmagslope_21d_2d_v125_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_logmagslope_63d_2d_v126_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of new_high_252_flag
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_logmagslope_252d_2d_v127_signal(closeadj):
    base = (closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_logmagslope_21d_2d_v128_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_logmagslope_63d_2d_v129_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of high_pctile_504
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_logmagslope_252d_2d_v130_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_logmagslope_21d_2d_v131_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_logmagslope_63d_2d_v132_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of days_since_252high
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_logmagslope_252d_2d_v133_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|disthigh_252d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_logslope_63d_2d_v134_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|disthigh_252d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_252d_logslope_252d_2d_v135_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|disthigh_504d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_logslope_63d_2d_v136_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|disthigh_504d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_504d_logslope_252d_2d_v137_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|disthigh_756d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_logslope_63d_2d_v138_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 756)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|disthigh_756d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_756d_logslope_252d_2d_v139_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 756)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|disthigh_1260d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_logslope_63d_2d_v140_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 1260)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|disthigh_1260d|
def f088hi_f088_ohlcv_multi_year_highs_disthigh_1260d_logslope_252d_2d_v141_signal(closeadj):
    base = np.log((_f088_disthigh(closeadj, 1260)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|new_high_252_flag|
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_logslope_63d_2d_v142_signal(closeadj):
    base = np.log(((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|new_high_252_flag|
def f088hi_f088_ohlcv_multi_year_highs_new_high_252_flag_logslope_252d_2d_v143_signal(closeadj):
    base = np.log(((closeadj >= closeadj.rolling(252, min_periods=63).max()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|high_pctile_504|
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_logslope_63d_2d_v144_signal(closeadj):
    base = np.log((closeadj.rolling(504, min_periods=126).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|high_pctile_504|
def f088hi_f088_ohlcv_multi_year_highs_high_pctile_504_logslope_252d_2d_v145_signal(closeadj):
    base = np.log((closeadj.rolling(504, min_periods=126).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|days_since_252high|
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_logslope_63d_2d_v146_signal(closeadj):
    base = np.log(((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|days_since_252high|
def f088hi_f088_ohlcv_multi_year_highs_days_since_252high_logslope_252d_2d_v147_signal(closeadj):
    base = np.log(((closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmax(), raw=False))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

