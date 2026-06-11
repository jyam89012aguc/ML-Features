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
def _f031_share_yoy(sharesbas):
    return sharesbas.pct_change(periods=252)


# 21d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slope_21d_2d_v001_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slope_63d_2d_v002_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slope_126d_2d_v003_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slope_252d_2d_v004_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_slope_504d_2d_v005_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slope_21d_2d_v006_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slope_63d_2d_v007_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slope_126d_2d_v008_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slope_252d_2d_v009_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_slope_504d_2d_v010_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slope_21d_2d_v011_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slope_63d_2d_v012_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slope_126d_2d_v013_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slope_252d_2d_v014_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_slope_504d_2d_v015_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slope_21d_2d_v016_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slope_63d_2d_v017_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slope_126d_2d_v018_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slope_252d_2d_v019_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_slope_504d_2d_v020_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slope_21d_2d_v021_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slope_63d_2d_v022_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slope_126d_2d_v023_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slope_252d_2d_v024_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_slope_504d_2d_v025_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slope_21d_2d_v026_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slope_63d_2d_v027_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slope_126d_2d_v028_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slope_252d_2d_v029_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_slope_504d_2d_v030_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slope_21d_2d_v031_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slope_63d_2d_v032_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slope_126d_2d_v033_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slope_252d_2d_v034_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_slope_504d_2d_v035_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sm21_sl21_2d_v036_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sm63_sl21_2d_v037_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sm63_sl63_2d_v038_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sm252_sl63_2d_v039_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sm252_sl126_2d_v040_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sm21_sl21_2d_v041_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sm63_sl21_2d_v042_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sm63_sl63_2d_v043_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sm252_sl63_2d_v044_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sm252_sl126_2d_v045_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sm21_sl21_2d_v046_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sm63_sl21_2d_v047_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sm63_sl63_2d_v048_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sm252_sl63_2d_v049_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sm252_sl126_2d_v050_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sm21_sl21_2d_v051_signal(sharesbas, closeadj):
    base = _mean(_f031_share_yoy(sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sm63_sl21_2d_v052_signal(sharesbas, closeadj):
    base = _mean(_f031_share_yoy(sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sm63_sl63_2d_v053_signal(sharesbas, closeadj):
    base = _mean(_f031_share_yoy(sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sm252_sl63_2d_v054_signal(sharesbas, closeadj):
    base = _mean(_f031_share_yoy(sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sm252_sl126_2d_v055_signal(sharesbas, closeadj):
    base = _mean(_f031_share_yoy(sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sm21_sl21_2d_v056_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=756), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sm63_sl21_2d_v057_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=756), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sm63_sl63_2d_v058_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=756), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sm252_sl63_2d_v059_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=756), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sm252_sl126_2d_v060_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=756), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sm21_sl21_2d_v061_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=1260), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sm63_sl21_2d_v062_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=1260), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sm63_sl63_2d_v063_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=1260), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sm252_sl63_2d_v064_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=1260), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sm252_sl126_2d_v065_signal(sharesbas, closeadj):
    base = _mean(sharesbas.pct_change(periods=1260), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sm21_sl21_2d_v066_signal(sharesbas, marketcap, closeadj):
    base = _mean(sharesbas / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sm63_sl21_2d_v067_signal(sharesbas, marketcap, closeadj):
    base = _mean(sharesbas / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sm63_sl63_2d_v068_signal(sharesbas, marketcap, closeadj):
    base = _mean(sharesbas / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sm252_sl63_2d_v069_signal(sharesbas, marketcap, closeadj):
    base = _mean(sharesbas / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sm252_sl126_2d_v070_signal(sharesbas, marketcap, closeadj):
    base = _mean(sharesbas / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_pctslope_21d_2d_v071_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_pctslope_63d_2d_v072_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_pctslope_252d_2d_v073_signal(sharesbas, closeadj):
    base = sharesbas
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_pctslope_21d_2d_v074_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_pctslope_63d_2d_v075_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_pctslope_252d_2d_v076_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_pctslope_21d_2d_v077_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_pctslope_63d_2d_v078_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_pctslope_252d_2d_v079_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_pctslope_21d_2d_v080_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_pctslope_63d_2d_v081_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_pctslope_252d_2d_v082_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_pctslope_21d_2d_v083_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_pctslope_63d_2d_v084_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_pctslope_252d_2d_v085_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_pctslope_21d_2d_v086_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_pctslope_63d_2d_v087_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_pctslope_252d_2d_v088_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_pctslope_21d_2d_v089_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_pctslope_63d_2d_v090_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_pctslope_252d_2d_v091_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sgnslope_21d_2d_v092_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sgnslope_63d_2d_v093_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_sgnslope_252d_2d_v094_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sgnslope_21d_2d_v095_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sgnslope_63d_2d_v096_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_sgnslope_252d_2d_v097_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sgnslope_21d_2d_v098_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sgnslope_63d_2d_v099_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_sgnslope_252d_2d_v100_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sgnslope_21d_2d_v101_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sgnslope_63d_2d_v102_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_sgnslope_252d_2d_v103_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sgnslope_21d_2d_v104_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sgnslope_63d_2d_v105_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_sgnslope_252d_2d_v106_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sgnslope_21d_2d_v107_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sgnslope_63d_2d_v108_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_sgnslope_252d_2d_v109_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sgnslope_21d_2d_v110_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sgnslope_63d_2d_v111_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_sgnslope_252d_2d_v112_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_logmagslope_21d_2d_v113_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_logmagslope_63d_2d_v114_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_logmagslope_252d_2d_v115_signal(sharesbas, closeadj):
    base = sharesbas
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_logmagslope_21d_2d_v116_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_logmagslope_63d_2d_v117_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_logmagslope_252d_2d_v118_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_logmagslope_21d_2d_v119_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_logmagslope_63d_2d_v120_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_logmagslope_252d_2d_v121_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_logmagslope_21d_2d_v122_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_logmagslope_63d_2d_v123_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_logmagslope_252d_2d_v124_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_logmagslope_21d_2d_v125_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_logmagslope_63d_2d_v126_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_logmagslope_252d_2d_v127_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_logmagslope_21d_2d_v128_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_logmagslope_63d_2d_v129_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_logmagslope_252d_2d_v130_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_logmagslope_21d_2d_v131_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_logmagslope_63d_2d_v132_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_logmagslope_252d_2d_v133_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_lvl|
def f031shb_f031_shares_basic_sharesbas_lvl_logslope_63d_2d_v134_signal(sharesbas, closeadj):
    base = np.log((sharesbas).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_lvl|
def f031shb_f031_shares_basic_sharesbas_lvl_logslope_252d_2d_v135_signal(sharesbas, closeadj):
    base = np.log((sharesbas).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_log|
def f031shb_f031_shares_basic_sharesbas_log_logslope_63d_2d_v136_signal(sharesbas, closeadj):
    base = np.log((np.log(sharesbas.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_log|
def f031shb_f031_shares_basic_sharesbas_log_logslope_252d_2d_v137_signal(sharesbas, closeadj):
    base = np.log((np.log(sharesbas.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_qoq|
def f031shb_f031_shares_basic_sharesbas_qoq_logslope_63d_2d_v138_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_qoq|
def f031shb_f031_shares_basic_sharesbas_qoq_logslope_252d_2d_v139_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_yoy|
def f031shb_f031_shares_basic_sharesbas_yoy_logslope_63d_2d_v140_signal(sharesbas, closeadj):
    base = np.log((_f031_share_yoy(sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_yoy|
def f031shb_f031_shares_basic_sharesbas_yoy_logslope_252d_2d_v141_signal(sharesbas, closeadj):
    base = np.log((_f031_share_yoy(sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_3y|
def f031shb_f031_shares_basic_sharesbas_3y_logslope_63d_2d_v142_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=756)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_3y|
def f031shb_f031_shares_basic_sharesbas_3y_logslope_252d_2d_v143_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=756)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_5y|
def f031shb_f031_shares_basic_sharesbas_5y_logslope_63d_2d_v144_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=1260)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_5y|
def f031shb_f031_shares_basic_sharesbas_5y_logslope_252d_2d_v145_signal(sharesbas, closeadj):
    base = np.log((sharesbas.pct_change(periods=1260)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sharesbas_to_mcap|
def f031shb_f031_shares_basic_sharesbas_to_mcap_logslope_63d_2d_v146_signal(sharesbas, marketcap, closeadj):
    base = np.log((sharesbas / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sharesbas_to_mcap|
def f031shb_f031_shares_basic_sharesbas_to_mcap_logslope_252d_2d_v147_signal(sharesbas, marketcap, closeadj):
    base = np.log((sharesbas / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

