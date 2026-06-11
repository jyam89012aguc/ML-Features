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
def _f72_debt_yoy(debt):
    return debt.pct_change(periods=252)


# 21d mean of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_base_v001_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_base_v002_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_base_v003_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_base_v004_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_base_v005_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_base_v006_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_base_v007_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_base_v008_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_base_v009_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_base_v010_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of dyoy (median/MAD)
def f72dt_f72_semi_debt_trajectory_dyoy_robustz_21d_base_v011_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of dyoy (median/MAD)
def f72dt_f72_semi_debt_trajectory_dyoy_robustz_63d_base_v012_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of dyoy (median/MAD)
def f72dt_f72_semi_debt_trajectory_dyoy_robustz_126d_base_v013_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of dyoy (median/MAD)
def f72dt_f72_semi_debt_trajectory_dyoy_robustz_252d_base_v014_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of dyoy (median/MAD)
def f72dt_f72_semi_debt_trajectory_dyoy_robustz_504d_base_v015_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_base_v016_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_base_v017_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_base_v018_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_base_v019_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_base_v020_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_base_v021_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_base_v022_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_base_v023_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_base_v024_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_base_v025_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_base_v026_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 21) - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_base_v027_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 63) - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_base_v028_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 126) - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_base_v029_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 252) - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_base_v030_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _max(r, 504) - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of dyoy in rolling range
def f72dt_f72_semi_debt_trajectory_dyoy_pos_21d_base_v031_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    lo = _min(r, 21)
    hi = _max(r, 21)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of dyoy in rolling range
def f72dt_f72_semi_debt_trajectory_dyoy_pos_63d_base_v032_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    lo = _min(r, 63)
    hi = _max(r, 63)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of dyoy in rolling range
def f72dt_f72_semi_debt_trajectory_dyoy_pos_126d_base_v033_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    lo = _min(r, 126)
    hi = _max(r, 126)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of dyoy in rolling range
def f72dt_f72_semi_debt_trajectory_dyoy_pos_252d_base_v034_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    lo = _min(r, 252)
    hi = _max(r, 252)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of dyoy in rolling range
def f72dt_f72_semi_debt_trajectory_dyoy_pos_504d_base_v035_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    lo = _min(r, 504)
    hi = _max(r, 504)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of dyoy from peak
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_base_v036_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of dyoy from peak
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_base_v037_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of dyoy from peak
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_base_v038_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of dyoy from peak
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_base_v039_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of dyoy from peak
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_base_v040_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of dyoy above trough
def f72dt_f72_semi_debt_trajectory_dyoy_up_21d_base_v041_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    trough = _min(r, 21)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of dyoy above trough
def f72dt_f72_semi_debt_trajectory_dyoy_up_63d_base_v042_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    trough = _min(r, 63)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of dyoy above trough
def f72dt_f72_semi_debt_trajectory_dyoy_up_126d_base_v043_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    trough = _min(r, 126)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of dyoy above trough
def f72dt_f72_semi_debt_trajectory_dyoy_up_252d_base_v044_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    trough = _min(r, 252)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of dyoy above trough
def f72dt_f72_semi_debt_trajectory_dyoy_up_504d_base_v045_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    trough = _min(r, 504)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_std_21d_base_v046_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _std(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_std_63d_base_v047_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _std(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_std_126d_base_v048_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_std_252d_base_v049_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _std(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_std_504d_base_v050_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = _std(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_skew_21d_base_v051_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_skew_63d_base_v052_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_skew_126d_base_v053_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_skew_252d_base_v054_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_skew_504d_base_v055_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_kurt_21d_base_v056_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_kurt_63d_base_v057_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_kurt_126d_base_v058_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_kurt_252d_base_v059_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_kurt_504d_base_v060_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of dyoy above rolling median
def f72dt_f72_semi_debt_trajectory_dyoy_hit_21d_base_v061_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(21, min_periods=11).median()
    result = (r > med).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of dyoy above rolling median
def f72dt_f72_semi_debt_trajectory_dyoy_hit_63d_base_v062_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(63, min_periods=32).median()
    result = (r > med).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of dyoy above rolling median
def f72dt_f72_semi_debt_trajectory_dyoy_hit_126d_base_v063_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(126, min_periods=63).median()
    result = (r > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of dyoy above rolling median
def f72dt_f72_semi_debt_trajectory_dyoy_hit_252d_base_v064_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(252, min_periods=126).median()
    result = (r > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of dyoy above rolling median
def f72dt_f72_semi_debt_trajectory_dyoy_hit_504d_base_v065_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    med = r.rolling(504, min_periods=252).median()
    result = (r > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed-cumsum of dyoy changes
def f72dt_f72_semi_debt_trajectory_dyoy_signcum_21d_base_v066_signal(debt, closeadj):
    r = _f72_debt_yoy(debt).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed-cumsum of dyoy changes
def f72dt_f72_semi_debt_trajectory_dyoy_signcum_63d_base_v067_signal(debt, closeadj):
    r = _f72_debt_yoy(debt).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed-cumsum of dyoy changes
def f72dt_f72_semi_debt_trajectory_dyoy_signcum_126d_base_v068_signal(debt, closeadj):
    r = _f72_debt_yoy(debt).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed-cumsum of dyoy changes
def f72dt_f72_semi_debt_trajectory_dyoy_signcum_252d_base_v069_signal(debt, closeadj):
    r = _f72_debt_yoy(debt).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed-cumsum of dyoy changes
def f72dt_f72_semi_debt_trajectory_dyoy_signcum_504d_base_v070_signal(debt, closeadj):
    r = _f72_debt_yoy(debt).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vs 21d EMA crossover of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_5v21_base_v071_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 63d EMA crossover of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_21v63_base_v072_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 126d EMA crossover of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_63v126_base_v073_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 252d EMA crossover of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_126v252_base_v074_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vs 504d EMA crossover of dyoy
def f72dt_f72_semi_debt_trajectory_dyoy_ema_252v504_base_v075_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
