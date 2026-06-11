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
def _f031_share_yoy(sharesbas):
    return sharesbas.pct_change(periods=252)


# 21d mean of sharesbas_lvl scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_lvl_mean_21d_base_v001_signal(sharesbas, closeadj):
    base = sharesbas
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_lvl scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_lvl_mean_63d_base_v002_signal(sharesbas, closeadj):
    base = sharesbas
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_lvl scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_lvl_mean_126d_base_v003_signal(sharesbas, closeadj):
    base = sharesbas
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_lvl scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_lvl_mean_252d_base_v004_signal(sharesbas, closeadj):
    base = sharesbas
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_lvl scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_lvl_mean_504d_base_v005_signal(sharesbas, closeadj):
    base = sharesbas
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_log scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_log_mean_21d_base_v006_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_log scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_log_mean_63d_base_v007_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_log scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_log_mean_126d_base_v008_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_log scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_log_mean_252d_base_v009_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_log scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_log_mean_504d_base_v010_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_qoq scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_qoq_mean_21d_base_v011_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_qoq scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_qoq_mean_63d_base_v012_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_qoq scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_qoq_mean_126d_base_v013_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_qoq scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_qoq_mean_252d_base_v014_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_qoq scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_qoq_mean_504d_base_v015_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_yoy scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_yoy_mean_21d_base_v016_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_yoy scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_yoy_mean_63d_base_v017_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_yoy scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_yoy_mean_126d_base_v018_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_yoy scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_yoy_mean_252d_base_v019_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_yoy scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_yoy_mean_504d_base_v020_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_3y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_3y_mean_21d_base_v021_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_3y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_3y_mean_63d_base_v022_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_3y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_3y_mean_126d_base_v023_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_3y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_3y_mean_252d_base_v024_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_3y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_3y_mean_504d_base_v025_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_5y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_5y_mean_21d_base_v026_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_5y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_5y_mean_63d_base_v027_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_5y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_5y_mean_126d_base_v028_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_5y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_5y_mean_252d_base_v029_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_5y scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_5y_mean_504d_base_v030_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sharesbas_to_mcap scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_to_mcap_mean_21d_base_v031_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sharesbas_to_mcap scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_to_mcap_mean_63d_base_v032_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sharesbas_to_mcap scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_to_mcap_mean_126d_base_v033_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sharesbas_to_mcap scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_to_mcap_mean_252d_base_v034_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sharesbas_to_mcap scaled by closeadj
def f031shb_f031_shares_basic_sharesbas_to_mcap_mean_504d_base_v035_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_median_63d_base_v036_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_median_252d_base_v037_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_median_504d_base_v038_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_median_63d_base_v039_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_median_252d_base_v040_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_median_504d_base_v041_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_median_63d_base_v042_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_median_252d_base_v043_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_median_504d_base_v044_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_median_63d_base_v045_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_median_252d_base_v046_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_median_504d_base_v047_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_median_63d_base_v048_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_median_252d_base_v049_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_median_504d_base_v050_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_median_63d_base_v051_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_median_252d_base_v052_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_median_504d_base_v053_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_median_63d_base_v054_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_median_252d_base_v055_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_median_504d_base_v056_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_rmax_252d_base_v057_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_rmax_504d_base_v058_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_rmax_252d_base_v059_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_rmax_504d_base_v060_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_rmax_252d_base_v061_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_rmax_504d_base_v062_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_rmax_252d_base_v063_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_rmax_504d_base_v064_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_rmax_252d_base_v065_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_rmax_504d_base_v066_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_rmax_252d_base_v067_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_rmax_504d_base_v068_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_rmax_252d_base_v069_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_rmax_504d_base_v070_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_rmin_252d_base_v071_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_rmin_504d_base_v072_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_rmin_252d_base_v073_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_rmin_504d_base_v074_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_rmin_252d_base_v075_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

