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
def _f12_gap(open_p, close_p):
    return open_p / close_p.shift(1) - 1.0


def _f12_gap_log(open_p, close_p):
    return np.log(open_p.replace(0, np.nan) / close_p.shift(1).replace(0, np.nan))


def _f12_intraday(open_p, close_p):
    return close_p / open_p - 1.0


def _f12_overnight_idx(open_p, close_p):
    g = open_p / close_p.shift(1) - 1.0
    return (1.0 + g).cumprod()


# 21d cumulative overnight gap
def f12og_f12_semi_overnight_gap_cumgap_21d_base_v001_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative overnight gap
def f12og_f12_semi_overnight_gap_cumgap_63d_base_v002_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative overnight gap
def f12og_f12_semi_overnight_gap_cumgap_126d_base_v003_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative overnight gap
def f12og_f12_semi_overnight_gap_cumgap_252d_base_v004_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative overnight gap
def f12og_f12_semi_overnight_gap_cumgap_504d_base_v005_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean overnight gap
def f12og_f12_semi_overnight_gap_meangap_21d_base_v006_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean overnight gap
def f12og_f12_semi_overnight_gap_meangap_63d_base_v007_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean overnight gap
def f12og_f12_semi_overnight_gap_meangap_126d_base_v008_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean overnight gap
def f12og_f12_semi_overnight_gap_meangap_252d_base_v009_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean overnight gap
def f12og_f12_semi_overnight_gap_meangap_504d_base_v010_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of overnight gap
def f12og_f12_semi_overnight_gap_stdgap_21d_base_v011_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _std(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of overnight gap
def f12og_f12_semi_overnight_gap_stdgap_63d_base_v012_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _std(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of overnight gap
def f12og_f12_semi_overnight_gap_stdgap_126d_base_v013_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _std(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of overnight gap
def f12og_f12_semi_overnight_gap_stdgap_252d_base_v014_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _std(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of overnight gap
def f12og_f12_semi_overnight_gap_stdgap_504d_base_v015_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _std(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of overnight gap
def f12og_f12_semi_overnight_gap_zgap_21d_base_v016_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of overnight gap
def f12og_f12_semi_overnight_gap_zgap_63d_base_v017_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of overnight gap
def f12og_f12_semi_overnight_gap_zgap_126d_base_v018_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of overnight gap
def f12og_f12_semi_overnight_gap_zgap_252d_base_v019_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of overnight gap
def f12og_f12_semi_overnight_gap_zgap_504d_base_v020_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _z(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of overnight gap
def f12og_f12_semi_overnight_gap_robustzgap_21d_base_v021_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    med = g.rolling(21, min_periods=11).median()
    mad = (g - med).abs().rolling(21, min_periods=11).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of overnight gap
def f12og_f12_semi_overnight_gap_robustzgap_63d_base_v022_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    med = g.rolling(63, min_periods=32).median()
    mad = (g - med).abs().rolling(63, min_periods=32).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of overnight gap
def f12og_f12_semi_overnight_gap_robustzgap_126d_base_v023_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    med = g.rolling(126, min_periods=63).median()
    mad = (g - med).abs().rolling(126, min_periods=63).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of overnight gap
def f12og_f12_semi_overnight_gap_robustzgap_252d_base_v024_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    med = g.rolling(252, min_periods=126).median()
    mad = (g - med).abs().rolling(252, min_periods=126).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of overnight gap
def f12og_f12_semi_overnight_gap_robustzgap_504d_base_v025_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    med = g.rolling(504, min_periods=252).median()
    mad = (g - med).abs().rolling(504, min_periods=252).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of positive gaps
def f12og_f12_semi_overnight_gap_posgapct_21d_base_v026_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of positive gaps
def f12og_f12_semi_overnight_gap_posgapct_63d_base_v027_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of positive gaps
def f12og_f12_semi_overnight_gap_posgapct_126d_base_v028_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of positive gaps
def f12og_f12_semi_overnight_gap_posgapct_252d_base_v029_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of positive gaps
def f12og_f12_semi_overnight_gap_posgapct_504d_base_v030_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of negative gaps
def f12og_f12_semi_overnight_gap_neggapct_21d_base_v031_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g < 0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of negative gaps
def f12og_f12_semi_overnight_gap_neggapct_63d_base_v032_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g < 0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of negative gaps
def f12og_f12_semi_overnight_gap_neggapct_126d_base_v033_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g < 0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of negative gaps
def f12og_f12_semi_overnight_gap_neggapct_252d_base_v034_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g < 0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of negative gaps
def f12og_f12_semi_overnight_gap_neggapct_504d_base_v035_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g < 0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive gaps
def f12og_f12_semi_overnight_gap_posgaphit_21d_base_v036_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive gaps
def f12og_f12_semi_overnight_gap_posgaphit_63d_base_v037_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive gaps
def f12og_f12_semi_overnight_gap_posgaphit_126d_base_v038_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive gaps
def f12og_f12_semi_overnight_gap_posgaphit_252d_base_v039_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive gaps
def f12og_f12_semi_overnight_gap_posgaphit_504d_base_v040_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = (g > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max overnight gap
def f12og_f12_semi_overnight_gap_maxgap_21d_base_v041_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max overnight gap
def f12og_f12_semi_overnight_gap_maxgap_63d_base_v042_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max overnight gap
def f12og_f12_semi_overnight_gap_maxgap_126d_base_v043_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max overnight gap
def f12og_f12_semi_overnight_gap_maxgap_252d_base_v044_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max overnight gap
def f12og_f12_semi_overnight_gap_maxgap_504d_base_v045_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min overnight gap
def f12og_f12_semi_overnight_gap_mingap_21d_base_v046_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _min(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min overnight gap
def f12og_f12_semi_overnight_gap_mingap_63d_base_v047_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _min(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min overnight gap
def f12og_f12_semi_overnight_gap_mingap_126d_base_v048_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _min(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min overnight gap
def f12og_f12_semi_overnight_gap_mingap_252d_base_v049_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _min(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min overnight gap
def f12og_f12_semi_overnight_gap_mingap_504d_base_v050_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _min(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of overnight gap
def f12og_f12_semi_overnight_gap_rnggap_21d_base_v051_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 21) - _min(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of overnight gap
def f12og_f12_semi_overnight_gap_rnggap_63d_base_v052_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 63) - _min(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of overnight gap
def f12og_f12_semi_overnight_gap_rnggap_126d_base_v053_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 126) - _min(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of overnight gap
def f12og_f12_semi_overnight_gap_rnggap_252d_base_v054_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 252) - _min(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of overnight gap
def f12og_f12_semi_overnight_gap_rnggap_504d_base_v055_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = _max(g, 504) - _min(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of gap
def f12og_f12_semi_overnight_gap_posgap_21d_base_v056_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 21)
    hi = _max(g, 21)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of gap
def f12og_f12_semi_overnight_gap_posgap_63d_base_v057_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of gap
def f12og_f12_semi_overnight_gap_posgap_126d_base_v058_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 126)
    hi = _max(g, 126)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of gap
def f12og_f12_semi_overnight_gap_posgap_252d_base_v059_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of gap
def f12og_f12_semi_overnight_gap_posgap_504d_base_v060_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 504)
    hi = _max(g, 504)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative sum of gap direction
def f12og_f12_semi_overnight_gap_signgapcum_21d_base_v061_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = pd.Series(np.sign(g), index=g.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative sum of gap direction
def f12og_f12_semi_overnight_gap_signgapcum_63d_base_v062_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative sum of gap direction
def f12og_f12_semi_overnight_gap_signgapcum_126d_base_v063_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = pd.Series(np.sign(g), index=g.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative sum of gap direction
def f12og_f12_semi_overnight_gap_signgapcum_252d_base_v064_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative sum of gap direction
def f12og_f12_semi_overnight_gap_signgapcum_504d_base_v065_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = pd.Series(np.sign(g), index=g.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of overnight gap
def f12og_f12_semi_overnight_gap_skewgap_21d_base_v066_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of overnight gap
def f12og_f12_semi_overnight_gap_skewgap_63d_base_v067_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of overnight gap
def f12og_f12_semi_overnight_gap_skewgap_126d_base_v068_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of overnight gap
def f12og_f12_semi_overnight_gap_skewgap_252d_base_v069_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of overnight gap
def f12og_f12_semi_overnight_gap_skewgap_504d_base_v070_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of overnight gap
def f12og_f12_semi_overnight_gap_kurtgap_21d_base_v071_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of overnight gap
def f12og_f12_semi_overnight_gap_kurtgap_63d_base_v072_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of overnight gap
def f12og_f12_semi_overnight_gap_kurtgap_126d_base_v073_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of overnight gap
def f12og_f12_semi_overnight_gap_kurtgap_252d_base_v074_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of overnight gap
def f12og_f12_semi_overnight_gap_kurtgap_504d_base_v075_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    result = g.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)
