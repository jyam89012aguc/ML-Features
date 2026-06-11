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
def _f48_om(oi, rev):
    return oi / rev.replace(0, np.nan)


def _f48_om_yoy(oi, rev):
    o = oi / rev.replace(0, np.nan)
    return o - o.shift(252)


# level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_base_v001_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_base_v002_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level of operating margin YoY change (126d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_126d_base_v003_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level of operating margin YoY change (252d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_252d_base_v004_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level of operating margin YoY change (504d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_504d_base_v005_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_base_v006_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_base_v007_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_base_v008_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_252d_base_v009_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_504d_base_v010_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of operating margin YoY change (median/MAD)
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_21d_base_v011_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(21, min_periods=11).median()
    mad = (m - med).abs().rolling(21, min_periods=11).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of operating margin YoY change (median/MAD)
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_base_v012_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of operating margin YoY change (median/MAD)
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_126d_base_v013_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(126, min_periods=63).median()
    mad = (m - med).abs().rolling(126, min_periods=63).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of operating margin YoY change (median/MAD)
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_252d_base_v014_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(252, min_periods=126).median()
    mad = (m - med).abs().rolling(252, min_periods=126).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of operating margin YoY change (median/MAD)
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_504d_base_v015_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(504, min_periods=252).median()
    mad = (m - med).abs().rolling(504, min_periods=252).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling max of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_max_21d_base_v016_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling max of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_max_63d_base_v017_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling max of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_max_126d_base_v018_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling max of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_max_252d_base_v019_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling max of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_max_504d_base_v020_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling min of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_min_21d_base_v021_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling min of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_min_63d_base_v022_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling min of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_min_126d_base_v023_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling min of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_min_252d_base_v024_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling min of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_min_504d_base_v025_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of operating margin YoY change (max - min)
def f48omt_semi_operating_margin_trajectory_omyoy_rng_21d_base_v026_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of operating margin YoY change (max - min)
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_base_v027_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of operating margin YoY change (max - min)
def f48omt_semi_operating_margin_trajectory_omyoy_rng_126d_base_v028_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of operating margin YoY change (max - min)
def f48omt_semi_operating_margin_trajectory_omyoy_rng_252d_base_v029_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of operating margin YoY change (max - min)
def f48omt_semi_operating_margin_trajectory_omyoy_rng_504d_base_v030_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of operating margin YoY change in its rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_21d_base_v031_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of operating margin YoY change in its rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_base_v032_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of operating margin YoY change in its rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_126d_base_v033_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of operating margin YoY change in its rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_252d_base_v034_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of operating margin YoY change in its rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_504d_base_v035_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of operating margin YoY change from rolling peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_21d_base_v036_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of operating margin YoY change from rolling peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_base_v037_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of operating margin YoY change from rolling peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_126d_base_v038_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of operating margin YoY change from rolling peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_252d_base_v039_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of operating margin YoY change from rolling peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_504d_base_v040_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of operating margin YoY change above rolling trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_21d_base_v041_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of operating margin YoY change above rolling trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_base_v042_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of operating margin YoY change above rolling trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_126d_base_v043_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of operating margin YoY change above rolling trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_252d_base_v044_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of operating margin YoY change above rolling trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_504d_base_v045_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of operating margin YoY change (volatility)
def f48omt_semi_operating_margin_trajectory_omyoy_std_21d_base_v046_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of operating margin YoY change (volatility)
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_base_v047_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of operating margin YoY change (volatility)
def f48omt_semi_operating_margin_trajectory_omyoy_std_126d_base_v048_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of operating margin YoY change (volatility)
def f48omt_semi_operating_margin_trajectory_omyoy_std_252d_base_v049_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of operating margin YoY change (volatility)
def f48omt_semi_operating_margin_trajectory_omyoy_std_504d_base_v050_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_21d_base_v051_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_base_v052_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_126d_base_v053_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_252d_base_v054_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_504d_base_v055_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_kurt_21d_base_v056_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_kurt_63d_base_v057_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_kurt_126d_base_v058_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_kurt_252d_base_v059_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_kurt_504d_base_v060_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_21d_base_v061_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = (m.diff() > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_base_v062_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_126d_base_v063_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = (m.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_252d_base_v064_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = (m.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_504d_base_v065_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = (m.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_21d_base_v066_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_base_v067_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_126d_base_v068_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_252d_base_v069_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_504d_base_v070_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA-crossover of operating margin YoY change (fast vs slow)
def f48omt_semi_operating_margin_trajectory_omyoy_ema_21d_base_v071_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.ewm(span=max(2, 21//4), adjust=False).mean() - m.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA-crossover of operating margin YoY change (fast vs slow)
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_base_v072_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA-crossover of operating margin YoY change (fast vs slow)
def f48omt_semi_operating_margin_trajectory_omyoy_ema_126d_base_v073_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.ewm(span=max(2, 126//4), adjust=False).mean() - m.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA-crossover of operating margin YoY change (fast vs slow)
def f48omt_semi_operating_margin_trajectory_omyoy_ema_252d_base_v074_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.ewm(span=max(2, 252//4), adjust=False).mean() - m.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA-crossover of operating margin YoY change (fast vs slow)
def f48omt_semi_operating_margin_trajectory_omyoy_ema_504d_base_v075_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    result = m.ewm(span=max(2, 504//4), adjust=False).mean() - m.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
