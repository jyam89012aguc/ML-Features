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
def _f80_ee(evebitda):
    return evebitda


# 21d mean of eez
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_base_v001_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of eez
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_base_v002_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of eez
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_base_v003_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of eez
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_base_v004_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of eez
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_base_v005_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of eez
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_base_v006_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of eez
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_base_v007_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of eez
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_base_v008_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of eez
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_base_v009_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of eez
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_base_v010_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of eez (median/MAD)
def f80ee_f80_semi_ev_ebitda_z_eez_robustz_21d_base_v011_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of eez (median/MAD)
def f80ee_f80_semi_ev_ebitda_z_eez_robustz_63d_base_v012_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of eez (median/MAD)
def f80ee_f80_semi_ev_ebitda_z_eez_robustz_126d_base_v013_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of eez (median/MAD)
def f80ee_f80_semi_ev_ebitda_z_eez_robustz_252d_base_v014_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of eez (median/MAD)
def f80ee_f80_semi_ev_ebitda_z_eez_robustz_504d_base_v015_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of eez
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_base_v016_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of eez
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_base_v017_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of eez
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_base_v018_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of eez
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_base_v019_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of eez
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_base_v020_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of eez
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_base_v021_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of eez
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_base_v022_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of eez
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_base_v023_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of eez
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_base_v024_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of eez
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_base_v025_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_base_v026_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 21) - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_base_v027_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 63) - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_base_v028_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 126) - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_base_v029_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 252) - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of eez
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_base_v030_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _max(r, 504) - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of eez in rolling range
def f80ee_f80_semi_ev_ebitda_z_eez_pos_21d_base_v031_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    lo = _min(r, 21)
    hi = _max(r, 21)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of eez in rolling range
def f80ee_f80_semi_ev_ebitda_z_eez_pos_63d_base_v032_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    lo = _min(r, 63)
    hi = _max(r, 63)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of eez in rolling range
def f80ee_f80_semi_ev_ebitda_z_eez_pos_126d_base_v033_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    lo = _min(r, 126)
    hi = _max(r, 126)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of eez in rolling range
def f80ee_f80_semi_ev_ebitda_z_eez_pos_252d_base_v034_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    lo = _min(r, 252)
    hi = _max(r, 252)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of eez in rolling range
def f80ee_f80_semi_ev_ebitda_z_eez_pos_504d_base_v035_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    lo = _min(r, 504)
    hi = _max(r, 504)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of eez from peak
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_base_v036_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of eez from peak
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_base_v037_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of eez from peak
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_base_v038_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of eez from peak
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_base_v039_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of eez from peak
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_base_v040_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of eez above trough
def f80ee_f80_semi_ev_ebitda_z_eez_up_21d_base_v041_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    trough = _min(r, 21)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of eez above trough
def f80ee_f80_semi_ev_ebitda_z_eez_up_63d_base_v042_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    trough = _min(r, 63)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of eez above trough
def f80ee_f80_semi_ev_ebitda_z_eez_up_126d_base_v043_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    trough = _min(r, 126)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of eez above trough
def f80ee_f80_semi_ev_ebitda_z_eez_up_252d_base_v044_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    trough = _min(r, 252)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of eez above trough
def f80ee_f80_semi_ev_ebitda_z_eez_up_504d_base_v045_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    trough = _min(r, 504)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of eez
def f80ee_f80_semi_ev_ebitda_z_eez_std_21d_base_v046_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _std(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of eez
def f80ee_f80_semi_ev_ebitda_z_eez_std_63d_base_v047_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _std(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of eez
def f80ee_f80_semi_ev_ebitda_z_eez_std_126d_base_v048_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of eez
def f80ee_f80_semi_ev_ebitda_z_eez_std_252d_base_v049_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _std(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of eez
def f80ee_f80_semi_ev_ebitda_z_eez_std_504d_base_v050_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = _std(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of eez
def f80ee_f80_semi_ev_ebitda_z_eez_skew_21d_base_v051_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of eez
def f80ee_f80_semi_ev_ebitda_z_eez_skew_63d_base_v052_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of eez
def f80ee_f80_semi_ev_ebitda_z_eez_skew_126d_base_v053_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of eez
def f80ee_f80_semi_ev_ebitda_z_eez_skew_252d_base_v054_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of eez
def f80ee_f80_semi_ev_ebitda_z_eez_skew_504d_base_v055_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of eez
def f80ee_f80_semi_ev_ebitda_z_eez_kurt_21d_base_v056_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of eez
def f80ee_f80_semi_ev_ebitda_z_eez_kurt_63d_base_v057_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of eez
def f80ee_f80_semi_ev_ebitda_z_eez_kurt_126d_base_v058_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of eez
def f80ee_f80_semi_ev_ebitda_z_eez_kurt_252d_base_v059_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of eez
def f80ee_f80_semi_ev_ebitda_z_eez_kurt_504d_base_v060_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of eez above rolling median
def f80ee_f80_semi_ev_ebitda_z_eez_hit_21d_base_v061_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(21, min_periods=11).median()
    result = (r > med).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of eez above rolling median
def f80ee_f80_semi_ev_ebitda_z_eez_hit_63d_base_v062_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(63, min_periods=32).median()
    result = (r > med).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of eez above rolling median
def f80ee_f80_semi_ev_ebitda_z_eez_hit_126d_base_v063_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(126, min_periods=63).median()
    result = (r > med).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of eez above rolling median
def f80ee_f80_semi_ev_ebitda_z_eez_hit_252d_base_v064_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(252, min_periods=126).median()
    result = (r > med).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of eez above rolling median
def f80ee_f80_semi_ev_ebitda_z_eez_hit_504d_base_v065_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    med = r.rolling(504, min_periods=252).median()
    result = (r > med).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed-cumsum of eez changes
def f80ee_f80_semi_ev_ebitda_z_eez_signcum_21d_base_v066_signal(evebitda, closeadj):
    r = _f80_ee(evebitda).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed-cumsum of eez changes
def f80ee_f80_semi_ev_ebitda_z_eez_signcum_63d_base_v067_signal(evebitda, closeadj):
    r = _f80_ee(evebitda).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed-cumsum of eez changes
def f80ee_f80_semi_ev_ebitda_z_eez_signcum_126d_base_v068_signal(evebitda, closeadj):
    r = _f80_ee(evebitda).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed-cumsum of eez changes
def f80ee_f80_semi_ev_ebitda_z_eez_signcum_252d_base_v069_signal(evebitda, closeadj):
    r = _f80_ee(evebitda).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed-cumsum of eez changes
def f80ee_f80_semi_ev_ebitda_z_eez_signcum_504d_base_v070_signal(evebitda, closeadj):
    r = _f80_ee(evebitda).diff()
    result = pd.Series(np.sign(r), index=r.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 5d vs 21d EMA crossover of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_5v21_base_v071_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 63d EMA crossover of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_21v63_base_v072_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 126d EMA crossover of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_63v126_base_v073_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 252d EMA crossover of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_126v252_base_v074_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vs 504d EMA crossover of eez
def f80ee_f80_semi_ev_ebitda_z_eez_ema_252v504_base_v075_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
