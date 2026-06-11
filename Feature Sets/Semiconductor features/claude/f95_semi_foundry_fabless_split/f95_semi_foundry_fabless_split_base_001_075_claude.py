import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


# ===== folder domain primitives =====
def _f95ff_gm(gp, rev):
    return gp / rev.replace(0, np.nan)


def _f95ff_capint(cx, rev):
    return cx / rev.replace(0, np.nan)


def _f95ff_split(gp, cx, rev):
    gm = gp / rev.replace(0, np.nan)
    ci = cx / rev.replace(0, np.nan)
    return gm - ci


# 21d core level (rolling mean)
def f95ff_f95_semi_foundry_fabless_split_lvl_21d_base_v001_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _mean(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d core level (rolling mean)
def f95ff_f95_semi_foundry_fabless_split_lvl_63d_base_v002_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _mean(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d core level (rolling mean)
def f95ff_f95_semi_foundry_fabless_split_lvl_126d_base_v003_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _mean(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d core level (rolling mean)
def f95ff_f95_semi_foundry_fabless_split_lvl_252d_base_v004_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _mean(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d core level (rolling mean)
def f95ff_f95_semi_foundry_fabless_split_lvl_504d_base_v005_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _mean(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of core series
def f95ff_f95_semi_foundry_fabless_split_z_21d_base_v006_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _z(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of core series
def f95ff_f95_semi_foundry_fabless_split_z_63d_base_v007_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _z(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of core series
def f95ff_f95_semi_foundry_fabless_split_z_126d_base_v008_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _z(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of core series
def f95ff_f95_semi_foundry_fabless_split_z_252d_base_v009_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _z(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of core series
def f95ff_f95_semi_foundry_fabless_split_z_504d_base_v010_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _z(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d robust z-score (median/MAD) of core
def f95ff_f95_semi_foundry_fabless_split_robustz_21d_base_v011_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    med = x.rolling(21, min_periods=10).median()
    mad = (x - med).abs().rolling(21, min_periods=10).median()
    result = (x - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d robust z-score (median/MAD) of core
def f95ff_f95_semi_foundry_fabless_split_robustz_63d_base_v012_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    med = x.rolling(63, min_periods=31).median()
    mad = (x - med).abs().rolling(63, min_periods=31).median()
    result = (x - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d robust z-score (median/MAD) of core
def f95ff_f95_semi_foundry_fabless_split_robustz_126d_base_v013_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    med = x.rolling(126, min_periods=63).median()
    mad = (x - med).abs().rolling(126, min_periods=63).median()
    result = (x - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d robust z-score (median/MAD) of core
def f95ff_f95_semi_foundry_fabless_split_robustz_252d_base_v014_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    med = x.rolling(252, min_periods=126).median()
    mad = (x - med).abs().rolling(252, min_periods=126).median()
    result = (x - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d robust z-score (median/MAD) of core
def f95ff_f95_semi_foundry_fabless_split_robustz_504d_base_v015_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    med = x.rolling(504, min_periods=252).median()
    mad = (x - med).abs().rolling(504, min_periods=252).median()
    result = (x - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling max of core
def f95ff_f95_semi_foundry_fabless_split_mx_21d_base_v016_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling max of core
def f95ff_f95_semi_foundry_fabless_split_mx_63d_base_v017_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling max of core
def f95ff_f95_semi_foundry_fabless_split_mx_126d_base_v018_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of core
def f95ff_f95_semi_foundry_fabless_split_mx_252d_base_v019_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of core
def f95ff_f95_semi_foundry_fabless_split_mx_504d_base_v020_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling min of core
def f95ff_f95_semi_foundry_fabless_split_mn_21d_base_v021_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _min(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling min of core
def f95ff_f95_semi_foundry_fabless_split_mn_63d_base_v022_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _min(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling min of core
def f95ff_f95_semi_foundry_fabless_split_mn_126d_base_v023_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _min(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of core
def f95ff_f95_semi_foundry_fabless_split_mn_252d_base_v024_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _min(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of core
def f95ff_f95_semi_foundry_fabless_split_mn_504d_base_v025_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _min(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d range of core (max - min)
def f95ff_f95_semi_foundry_fabless_split_rng_21d_base_v026_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 21) - _min(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d range of core (max - min)
def f95ff_f95_semi_foundry_fabless_split_rng_63d_base_v027_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 63) - _min(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d range of core (max - min)
def f95ff_f95_semi_foundry_fabless_split_rng_126d_base_v028_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 126) - _min(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d range of core (max - min)
def f95ff_f95_semi_foundry_fabless_split_rng_252d_base_v029_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 252) - _min(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d range of core (max - min)
def f95ff_f95_semi_foundry_fabless_split_rng_504d_base_v030_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _max(x, 504) - _min(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d position-in-range of core
def f95ff_f95_semi_foundry_fabless_split_pos_21d_base_v031_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    lo = _min(x, 21)
    hi = _max(x, 21)
    result = (x - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d position-in-range of core
def f95ff_f95_semi_foundry_fabless_split_pos_63d_base_v032_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    lo = _min(x, 63)
    hi = _max(x, 63)
    result = (x - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d position-in-range of core
def f95ff_f95_semi_foundry_fabless_split_pos_126d_base_v033_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    lo = _min(x, 126)
    hi = _max(x, 126)
    result = (x - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d position-in-range of core
def f95ff_f95_semi_foundry_fabless_split_pos_252d_base_v034_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    lo = _min(x, 252)
    hi = _max(x, 252)
    result = (x - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d position-in-range of core
def f95ff_f95_semi_foundry_fabless_split_pos_504d_base_v035_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    lo = _min(x, 504)
    hi = _max(x, 504)
    result = (x - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d drawdown of core from rolling peak
def f95ff_f95_semi_foundry_fabless_split_dd_21d_base_v036_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    peak = _max(x, 21)
    result = x - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 63d drawdown of core from rolling peak
def f95ff_f95_semi_foundry_fabless_split_dd_63d_base_v037_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    peak = _max(x, 63)
    result = x - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 126d drawdown of core from rolling peak
def f95ff_f95_semi_foundry_fabless_split_dd_126d_base_v038_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    peak = _max(x, 126)
    result = x - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 252d drawdown of core from rolling peak
def f95ff_f95_semi_foundry_fabless_split_dd_252d_base_v039_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    peak = _max(x, 252)
    result = x - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 504d drawdown of core from rolling peak
def f95ff_f95_semi_foundry_fabless_split_dd_504d_base_v040_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    peak = _max(x, 504)
    result = x - peak
    return result.replace([np.inf, -np.inf], np.nan)

# 21d run-up of core above rolling trough
def f95ff_f95_semi_foundry_fabless_split_runup_21d_base_v041_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    trough = _min(x, 21)
    result = x - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 63d run-up of core above rolling trough
def f95ff_f95_semi_foundry_fabless_split_runup_63d_base_v042_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    trough = _min(x, 63)
    result = x - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 126d run-up of core above rolling trough
def f95ff_f95_semi_foundry_fabless_split_runup_126d_base_v043_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    trough = _min(x, 126)
    result = x - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 252d run-up of core above rolling trough
def f95ff_f95_semi_foundry_fabless_split_runup_252d_base_v044_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    trough = _min(x, 252)
    result = x - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 504d run-up of core above rolling trough
def f95ff_f95_semi_foundry_fabless_split_runup_504d_base_v045_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    trough = _min(x, 504)
    result = x - trough
    return result.replace([np.inf, -np.inf], np.nan)

# 21d std of core
def f95ff_f95_semi_foundry_fabless_split_std_21d_base_v046_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _std(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d std of core
def f95ff_f95_semi_foundry_fabless_split_std_63d_base_v047_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _std(x, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d std of core
def f95ff_f95_semi_foundry_fabless_split_std_126d_base_v048_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _std(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d std of core
def f95ff_f95_semi_foundry_fabless_split_std_252d_base_v049_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _std(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d std of core
def f95ff_f95_semi_foundry_fabless_split_std_504d_base_v050_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = _std(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d skew of core
def f95ff_f95_semi_foundry_fabless_split_skew_21d_base_v051_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d skew of core
def f95ff_f95_semi_foundry_fabless_split_skew_63d_base_v052_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d skew of core
def f95ff_f95_semi_foundry_fabless_split_skew_126d_base_v053_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d skew of core
def f95ff_f95_semi_foundry_fabless_split_skew_252d_base_v054_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d skew of core
def f95ff_f95_semi_foundry_fabless_split_skew_504d_base_v055_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d kurtosis of core
def f95ff_f95_semi_foundry_fabless_split_kurt_21d_base_v056_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d kurtosis of core
def f95ff_f95_semi_foundry_fabless_split_kurt_63d_base_v057_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d kurtosis of core
def f95ff_f95_semi_foundry_fabless_split_kurt_126d_base_v058_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d kurtosis of core
def f95ff_f95_semi_foundry_fabless_split_kurt_252d_base_v059_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d kurtosis of core
def f95ff_f95_semi_foundry_fabless_split_kurt_504d_base_v060_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hit ratio (frac of positive core)
def f95ff_f95_semi_foundry_fabless_split_hit_21d_base_v061_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = (x > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hit ratio (frac of positive core)
def f95ff_f95_semi_foundry_fabless_split_hit_63d_base_v062_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = (x > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hit ratio (frac of positive core)
def f95ff_f95_semi_foundry_fabless_split_hit_126d_base_v063_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hit ratio (frac of positive core)
def f95ff_f95_semi_foundry_fabless_split_hit_252d_base_v064_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = (x > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hit ratio (frac of positive core)
def f95ff_f95_semi_foundry_fabless_split_hit_504d_base_v065_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = (x > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d signed cumulative count of core direction
def f95ff_f95_semi_foundry_fabless_split_signcum_21d_base_v066_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = pd.Series(np.sign(x), index=x.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d signed cumulative count of core direction
def f95ff_f95_semi_foundry_fabless_split_signcum_63d_base_v067_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = pd.Series(np.sign(x), index=x.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d signed cumulative count of core direction
def f95ff_f95_semi_foundry_fabless_split_signcum_126d_base_v068_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d signed cumulative count of core direction
def f95ff_f95_semi_foundry_fabless_split_signcum_252d_base_v069_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = pd.Series(np.sign(x), index=x.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d signed cumulative count of core direction
def f95ff_f95_semi_foundry_fabless_split_signcum_504d_base_v070_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = pd.Series(np.sign(x), index=x.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover of core (5 vs 21)
def f95ff_f95_semi_foundry_fabless_split_ema_5v21_base_v071_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.ewm(span=5, adjust=False).mean() - x.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover of core (21 vs 63)
def f95ff_f95_semi_foundry_fabless_split_ema_21v63_base_v072_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.ewm(span=21, adjust=False).mean() - x.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover of core (63 vs 126)
def f95ff_f95_semi_foundry_fabless_split_ema_63v126_base_v073_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.ewm(span=63, adjust=False).mean() - x.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover of core (126 vs 252)
def f95ff_f95_semi_foundry_fabless_split_ema_126v252_base_v074_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.ewm(span=126, adjust=False).mean() - x.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# EMA crossover of core (252 vs 504)
def f95ff_f95_semi_foundry_fabless_split_ema_252v504_base_v075_signal(gp, revenue, capex, closeadj):
    x = _f95ff_split(gp, capex, revenue)
    result = x.ewm(span=252, adjust=False).mean() - x.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
