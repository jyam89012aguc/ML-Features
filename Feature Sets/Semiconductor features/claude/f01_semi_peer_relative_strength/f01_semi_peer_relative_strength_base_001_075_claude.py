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


def _log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# ===== folder domain primitives =====
def _f01_log_return(s, n):
    return np.log(s / s.shift(n))


def _f01_rs_spread(own, bas, n):
    return np.log(own / own.shift(n)) - np.log(bas / bas.shift(n))


def _f01_rs_ratio(own, bas):
    return own / bas.replace(0, np.nan)


def _f01_rs_log_ratio(own, bas):
    return np.log(own.replace(0, np.nan).abs() / bas.replace(0, np.nan).abs())


# 21d log-return spread vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsret_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    result = _f01_rs_spread(closeadj, semi_basket_closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-return spread vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsret_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    result = _f01_rs_spread(closeadj, semi_basket_closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-return spread vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsret_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    result = _f01_rs_spread(closeadj, semi_basket_closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-return spread vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsret_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    result = _f01_rs_spread(closeadj, semi_basket_closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-return spread vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsret_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    result = _f01_rs_spread(closeadj, semi_basket_closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RS log-ratio level relative to 63d mean
def f01prs_f01_semi_peer_relative_strength_rsratio_21d_base_v006_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS log-ratio level relative to 126d mean
def f01prs_f01_semi_peer_relative_strength_rsratio_63d_base_v007_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d RS log-ratio level relative to 252d mean
def f01prs_f01_semi_peer_relative_strength_rsratio_126d_base_v008_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d RS log-ratio level relative to 504d mean
def f01prs_f01_semi_peer_relative_strength_rsratio_252d_base_v009_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d RS log-ratio level relative to 756d mean
def f01prs_f01_semi_peer_relative_strength_rsratio_504d_base_v010_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r - _mean(r, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of RS log-ratio (median/MAD)
def f01prs_f01_semi_peer_relative_strength_rsrobustz_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of RS log-ratio (median/MAD)
def f01prs_f01_semi_peer_relative_strength_rsrobustz_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of RS log-ratio (median/MAD)
def f01prs_f01_semi_peer_relative_strength_rsrobustz_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of RS log-ratio (median/MAD)
def f01prs_f01_semi_peer_relative_strength_rsrobustz_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of RS log-ratio (median/MAD)
def f01prs_f01_semi_peer_relative_strength_rsrobustz_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days own beats basket
def f01prs_f01_semi_peer_relative_strength_rshits_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days own beats basket
def f01prs_f01_semi_peer_relative_strength_rshits_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days own beats basket
def f01prs_f01_semi_peer_relative_strength_rshits_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days own beats basket
def f01prs_f01_semi_peer_relative_strength_rshits_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days own beats basket
def f01prs_f01_semi_peer_relative_strength_rshits_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio own vs basket
def f01prs_f01_semi_peer_relative_strength_rsfrac_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio own vs basket
def f01prs_f01_semi_peer_relative_strength_rsfrac_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio own vs basket
def f01prs_f01_semi_peer_relative_strength_rsfrac_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio own vs basket
def f01prs_f01_semi_peer_relative_strength_rsfrac_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio own vs basket
def f01prs_f01_semi_peer_relative_strength_rsfrac_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = (own > bas).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = pd.Series(np.sign(own - bas), index=own.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = pd.Series(np.sign(own - bas), index=own.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = pd.Series(np.sign(own - bas), index=own.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = pd.Series(np.sign(own - bas), index=own.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    own = closeadj.pct_change()
    bas = semi_basket_closeadj.pct_change()
    result = pd.Series(np.sign(own - bas), index=own.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of RS log-ratio (RS volatility)
def f01prs_f01_semi_peer_relative_strength_rsstd_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    result = _std(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of RS log-ratio (RS volatility)
def f01prs_f01_semi_peer_relative_strength_rsstd_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    result = _std(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of RS log-ratio (RS volatility)
def f01prs_f01_semi_peer_relative_strength_rsstd_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of RS log-ratio (RS volatility)
def f01prs_f01_semi_peer_relative_strength_rsstd_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    result = _std(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of RS log-ratio (RS volatility)
def f01prs_f01_semi_peer_relative_strength_rsstd_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    result = _std(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmax_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmax_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmax_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmax_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmax_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmin_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmin_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmin_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmin_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsmin_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of RS log-ratio (max - min)
def f01prs_f01_semi_peer_relative_strength_rsrng_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 21) - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of RS log-ratio (max - min)
def f01prs_f01_semi_peer_relative_strength_rsrng_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 63) - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of RS log-ratio (max - min)
def f01prs_f01_semi_peer_relative_strength_rsrng_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 126) - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of RS log-ratio (max - min)
def f01prs_f01_semi_peer_relative_strength_rsrng_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 252) - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of RS log-ratio (max - min)
def f01prs_f01_semi_peer_relative_strength_rsrng_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _max(r, 504) - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RS log-ratio position in its rolling range
def f01prs_f01_semi_peer_relative_strength_rspos_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = _min(r, 21)
    hi = _max(r, 21)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS log-ratio position in its rolling range
def f01prs_f01_semi_peer_relative_strength_rspos_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = _min(r, 63)
    hi = _max(r, 63)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d RS log-ratio position in its rolling range
def f01prs_f01_semi_peer_relative_strength_rspos_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = _min(r, 126)
    hi = _max(r, 126)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d RS log-ratio position in its rolling range
def f01prs_f01_semi_peer_relative_strength_rspos_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = _min(r, 252)
    hi = _max(r, 252)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d RS log-ratio position in its rolling range
def f01prs_f01_semi_peer_relative_strength_rspos_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = _min(r, 504)
    hi = _max(r, 504)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of RS log-ratio from its rolling peak
def f01prs_f01_semi_peer_relative_strength_rsdd_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of RS log-ratio from its rolling peak
def f01prs_f01_semi_peer_relative_strength_rsdd_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of RS log-ratio from its rolling peak
def f01prs_f01_semi_peer_relative_strength_rsdd_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of RS log-ratio from its rolling peak
def f01prs_f01_semi_peer_relative_strength_rsdd_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of RS log-ratio from its rolling peak
def f01prs_f01_semi_peer_relative_strength_rsdd_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of RS log-ratio above rolling trough
def f01prs_f01_semi_peer_relative_strength_rsup_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    trough = _min(r, 21)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of RS log-ratio above rolling trough
def f01prs_f01_semi_peer_relative_strength_rsup_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    trough = _min(r, 63)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of RS log-ratio above rolling trough
def f01prs_f01_semi_peer_relative_strength_rsup_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    trough = _min(r, 126)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of RS log-ratio above rolling trough
def f01prs_f01_semi_peer_relative_strength_rsup_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    trough = _min(r, 252)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of RS log-ratio above rolling trough
def f01prs_f01_semi_peer_relative_strength_rsup_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    trough = _min(r, 504)
    result = r - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RS ema fast-slow crossover (5d vs 21d)
def f01prs_f01_semi_peer_relative_strength_rsema_5v21_base_v071_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 63d RS ema crossover
def f01prs_f01_semi_peer_relative_strength_rsema_21v63_base_v072_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 126d RS ema crossover
def f01prs_f01_semi_peer_relative_strength_rsema_63v126_base_v073_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 252d RS ema crossover
def f01prs_f01_semi_peer_relative_strength_rsema_126v252_base_v074_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vs 504d RS ema crossover
def f01prs_f01_semi_peer_relative_strength_rsema_252v504_base_v075_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
