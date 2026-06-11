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
def _f04_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f04_rot_spread(semi, spx, n):
    return np.log(semi / semi.shift(n)) - np.log(spx / spx.shift(n))


def _f04_rs_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())

# 21d semi-basket vs sp500 log-return spread (rotation)
def f04sr_f04_semi_sector_rotation_semispx_21d_base_v001_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d semi-basket vs sp500 log-return spread (rotation)
def f04sr_f04_semi_sector_rotation_semispx_63d_base_v002_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d semi-basket vs sp500 log-return spread (rotation)
def f04sr_f04_semi_sector_rotation_semispx_126d_base_v003_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d semi-basket vs sp500 log-return spread (rotation)
def f04sr_f04_semi_sector_rotation_semispx_252d_base_v004_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d semi-basket vs sp500 log-return spread (rotation)
def f04sr_f04_semi_sector_rotation_semispx_504d_base_v005_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own vs sp500 log-return spread
def f04sr_f04_semi_sector_rotation_ownspx_21d_base_v006_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, sp500_closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own vs sp500 log-return spread
def f04sr_f04_semi_sector_rotation_ownspx_63d_base_v007_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, sp500_closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own vs sp500 log-return spread
def f04sr_f04_semi_sector_rotation_ownspx_126d_base_v008_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, sp500_closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own vs sp500 log-return spread
def f04sr_f04_semi_sector_rotation_ownspx_252d_base_v009_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, sp500_closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own vs sp500 log-return spread
def f04sr_f04_semi_sector_rotation_ownspx_504d_base_v010_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, sp500_closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own vs semi-basket log-return spread
def f04sr_f04_semi_sector_rotation_ownsemi_21d_base_v011_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, semi_basket_closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own vs semi-basket log-return spread
def f04sr_f04_semi_sector_rotation_ownsemi_63d_base_v012_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, semi_basket_closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own vs semi-basket log-return spread
def f04sr_f04_semi_sector_rotation_ownsemi_126d_base_v013_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, semi_basket_closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own vs semi-basket log-return spread
def f04sr_f04_semi_sector_rotation_ownsemi_252d_base_v014_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, semi_basket_closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own vs semi-basket log-return spread
def f04sr_f04_semi_sector_rotation_ownsemi_504d_base_v015_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    result = _f04_rot_spread(closeadj, semi_basket_closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of semi vs spx log-return spread
def f04sr_f04_semi_sector_rotation_semispxz_21d_base_v016_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 21)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of semi vs spx log-return spread
def f04sr_f04_semi_sector_rotation_semispxz_63d_base_v017_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 63)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of semi vs spx log-return spread
def f04sr_f04_semi_sector_rotation_semispxz_126d_base_v018_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 126)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of semi vs spx log-return spread
def f04sr_f04_semi_sector_rotation_semispxz_252d_base_v019_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 252)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of semi vs spx log-return spread
def f04sr_f04_semi_sector_rotation_semispxz_504d_base_v020_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(semi_basket_closeadj, sp500_closeadj, 504)
    result = _z(s, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of own vs spx log-return spread
def f04sr_f04_semi_sector_rotation_ownspxz_21d_base_v021_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(closeadj, sp500_closeadj, 21)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of own vs spx log-return spread
def f04sr_f04_semi_sector_rotation_ownspxz_63d_base_v022_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(closeadj, sp500_closeadj, 63)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of own vs spx log-return spread
def f04sr_f04_semi_sector_rotation_ownspxz_126d_base_v023_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(closeadj, sp500_closeadj, 126)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of own vs spx log-return spread
def f04sr_f04_semi_sector_rotation_ownspxz_252d_base_v024_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(closeadj, sp500_closeadj, 252)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of own vs spx log-return spread
def f04sr_f04_semi_sector_rotation_ownspxz_504d_base_v025_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = _f04_rot_spread(closeadj, sp500_closeadj, 504)
    result = _z(s, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days semi outperforms spx
def f04sr_f04_semi_sector_rotation_semibeatspxfrac_21d_base_v026_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days semi outperforms spx
def f04sr_f04_semi_sector_rotation_semibeatspxfrac_63d_base_v027_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days semi outperforms spx
def f04sr_f04_semi_sector_rotation_semibeatspxfrac_126d_base_v028_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days semi outperforms spx
def f04sr_f04_semi_sector_rotation_semibeatspxfrac_252d_base_v029_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days semi outperforms spx
def f04sr_f04_semi_sector_rotation_semibeatspxfrac_504d_base_v030_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days own outperforms spx
def f04sr_f04_semi_sector_rotation_ownbeatspxfrac_21d_base_v031_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o > x).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days own outperforms spx
def f04sr_f04_semi_sector_rotation_ownbeatspxfrac_63d_base_v032_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o > x).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days own outperforms spx
def f04sr_f04_semi_sector_rotation_ownbeatspxfrac_126d_base_v033_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o > x).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days own outperforms spx
def f04sr_f04_semi_sector_rotation_ownbeatspxfrac_252d_base_v034_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o > x).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days own outperforms spx
def f04sr_f04_semi_sector_rotation_ownbeatspxfrac_504d_base_v035_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o > x).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days semi beats spx
def f04sr_f04_semi_sector_rotation_semibeatspxcnt_21d_base_v036_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days semi beats spx
def f04sr_f04_semi_sector_rotation_semibeatspxcnt_63d_base_v037_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days semi beats spx
def f04sr_f04_semi_sector_rotation_semibeatspxcnt_126d_base_v038_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days semi beats spx
def f04sr_f04_semi_sector_rotation_semibeatspxcnt_252d_base_v039_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days semi beats spx
def f04sr_f04_semi_sector_rotation_semibeatspxcnt_504d_base_v040_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (s > x).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative semi vs spx outperformance
def f04sr_f04_semi_sector_rotation_semispxsigncum_21d_base_v041_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(s - x), index=s.index).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative semi vs spx outperformance
def f04sr_f04_semi_sector_rotation_semispxsigncum_63d_base_v042_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(s - x), index=s.index).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative semi vs spx outperformance
def f04sr_f04_semi_sector_rotation_semispxsigncum_126d_base_v043_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(s - x), index=s.index).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative semi vs spx outperformance
def f04sr_f04_semi_sector_rotation_semispxsigncum_252d_base_v044_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(s - x), index=s.index).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative semi vs spx outperformance
def f04sr_f04_semi_sector_rotation_semispxsigncum_504d_base_v045_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(s - x), index=s.index).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative own vs spx outperformance
def f04sr_f04_semi_sector_rotation_ownspxsigncum_21d_base_v046_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(o - x), index=o.index).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative own vs spx outperformance
def f04sr_f04_semi_sector_rotation_ownspxsigncum_63d_base_v047_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(o - x), index=o.index).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative own vs spx outperformance
def f04sr_f04_semi_sector_rotation_ownspxsigncum_126d_base_v048_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(o - x), index=o.index).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative own vs spx outperformance
def f04sr_f04_semi_sector_rotation_ownspxsigncum_252d_base_v049_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(o - x), index=o.index).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative own vs spx outperformance
def f04sr_f04_semi_sector_rotation_ownspxsigncum_504d_base_v050_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = pd.Series(np.sign(o - x), index=o.index).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-ratio semi/spx less 63d mean
def f04sr_f04_semi_sector_rotation_semispxratio_21d_base_v051_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-ratio semi/spx less 126d mean
def f04sr_f04_semi_sector_rotation_semispxratio_63d_base_v052_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-ratio semi/spx less 252d mean
def f04sr_f04_semi_sector_rotation_semispxratio_126d_base_v053_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-ratio semi/spx less 504d mean
def f04sr_f04_semi_sector_rotation_semispxratio_252d_base_v054_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-ratio semi/spx less 756d mean
def f04sr_f04_semi_sector_rotation_semispxratio_504d_base_v055_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r - _mean(r, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-ratio own/spx less 63d mean
def f04sr_f04_semi_sector_rotation_ownspxratio_21d_base_v056_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-ratio own/spx less 126d mean
def f04sr_f04_semi_sector_rotation_ownspxratio_63d_base_v057_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-ratio own/spx less 252d mean
def f04sr_f04_semi_sector_rotation_ownspxratio_126d_base_v058_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-ratio own/spx less 504d mean
def f04sr_f04_semi_sector_rotation_ownspxratio_252d_base_v059_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-ratio own/spx less 756d mean
def f04sr_f04_semi_sector_rotation_ownspxratio_504d_base_v060_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r - _mean(r, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of semi/spx log-ratio
def f04sr_f04_semi_sector_rotation_semispxema_5v21_base_v061_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of semi/spx log-ratio
def f04sr_f04_semi_sector_rotation_semispxema_21v63_base_v062_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of semi/spx log-ratio
def f04sr_f04_semi_sector_rotation_semispxema_63v126_base_v063_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of semi/spx log-ratio
def f04sr_f04_semi_sector_rotation_semispxema_126v252_base_v064_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of semi/spx log-ratio
def f04sr_f04_semi_sector_rotation_semispxema_252v504_base_v065_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of own/spx log-ratio
def f04sr_f04_semi_sector_rotation_ownspxema_5v21_base_v066_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of own/spx log-ratio
def f04sr_f04_semi_sector_rotation_ownspxema_21v63_base_v067_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of own/spx log-ratio
def f04sr_f04_semi_sector_rotation_ownspxema_63v126_base_v068_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of own/spx log-ratio
def f04sr_f04_semi_sector_rotation_ownspxema_126v252_base_v069_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of own/spx log-ratio
def f04sr_f04_semi_sector_rotation_ownspxema_252v504_base_v070_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(closeadj, sp500_closeadj)
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of semi-spx return spread (rotation vol)
def f04sr_f04_semi_sector_rotation_semispxstd_21d_base_v071_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(s - x, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of semi-spx return spread (rotation vol)
def f04sr_f04_semi_sector_rotation_semispxstd_63d_base_v072_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(s - x, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of semi-spx return spread (rotation vol)
def f04sr_f04_semi_sector_rotation_semispxstd_126d_base_v073_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(s - x, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of semi-spx return spread (rotation vol)
def f04sr_f04_semi_sector_rotation_semispxstd_252d_base_v074_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(s - x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of semi-spx return spread (rotation vol)
def f04sr_f04_semi_sector_rotation_semispxstd_504d_base_v075_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(s - x, 504)
    return result.replace([np.inf, -np.inf], np.nan)


