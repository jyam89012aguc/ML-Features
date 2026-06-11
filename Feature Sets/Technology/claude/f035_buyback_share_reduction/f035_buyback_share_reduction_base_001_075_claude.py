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
def _f035_share_red(sharesbas, n):
    return -sharesbas.diff(periods=n)


# 21d mean of share_red_252d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_252d_mean_21d_base_v001_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of share_red_252d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_252d_mean_63d_base_v002_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of share_red_252d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_252d_mean_126d_base_v003_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of share_red_252d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_252d_mean_252d_base_v004_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of share_red_252d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_252d_mean_504d_base_v005_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of share_red_504d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_504d_mean_21d_base_v006_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of share_red_504d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_504d_mean_63d_base_v007_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of share_red_504d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_504d_mean_126d_base_v008_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of share_red_504d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_504d_mean_252d_base_v009_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of share_red_504d scaled by closeadj
def f035bsr_f035_buyback_share_reduction_share_red_504d_mean_504d_base_v010_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of buyback_yield_proxy scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_mean_21d_base_v011_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of buyback_yield_proxy scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_mean_63d_base_v012_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of buyback_yield_proxy scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_mean_126d_base_v013_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of buyback_yield_proxy scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_mean_252d_base_v014_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of buyback_yield_proxy scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_mean_504d_base_v015_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_dil_after_sbc scaled by closeadj
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_mean_21d_base_v016_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_dil_after_sbc scaled by closeadj
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_mean_63d_base_v017_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_dil_after_sbc scaled by closeadj
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_mean_126d_base_v018_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_dil_after_sbc scaled by closeadj
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_mean_252d_base_v019_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_dil_after_sbc scaled by closeadj
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_mean_504d_base_v020_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of buyback_to_mcap scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_mean_21d_base_v021_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of buyback_to_mcap scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_mean_63d_base_v022_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of buyback_to_mcap scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_mean_126d_base_v023_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of buyback_to_mcap scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_mean_252d_base_v024_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of buyback_to_mcap scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_mean_504d_base_v025_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of buyback_to_fcf scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_mean_21d_base_v026_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of buyback_to_fcf scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_mean_63d_base_v027_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of buyback_to_fcf scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_mean_126d_base_v028_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of buyback_to_fcf scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_mean_252d_base_v029_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of buyback_to_fcf scaled by closeadj
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_mean_504d_base_v030_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dil_minus_buyback scaled by closeadj
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_mean_21d_base_v031_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dil_minus_buyback scaled by closeadj
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_mean_63d_base_v032_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dil_minus_buyback scaled by closeadj
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_mean_126d_base_v033_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dil_minus_buyback scaled by closeadj
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_mean_252d_base_v034_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dil_minus_buyback scaled by closeadj
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_mean_504d_base_v035_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_median_63d_base_v036_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_median_252d_base_v037_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_median_504d_base_v038_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_median_63d_base_v039_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_median_252d_base_v040_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_median_504d_base_v041_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_median_63d_base_v042_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_median_252d_base_v043_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_median_504d_base_v044_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_median_63d_base_v045_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_median_252d_base_v046_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_median_504d_base_v047_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_median_63d_base_v048_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_median_252d_base_v049_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_median_504d_base_v050_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_median_63d_base_v051_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_median_252d_base_v052_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_median_504d_base_v053_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_median_63d_base_v054_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_median_252d_base_v055_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_median_504d_base_v056_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_rmax_252d_base_v057_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_rmax_504d_base_v058_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_rmax_252d_base_v059_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_rmax_504d_base_v060_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_rmax_252d_base_v061_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_rmax_504d_base_v062_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_rmax_252d_base_v063_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_rmax_504d_base_v064_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_rmax_252d_base_v065_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_rmax_504d_base_v066_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_rmax_252d_base_v067_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_rmax_504d_base_v068_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_rmax_252d_base_v069_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_rmax_504d_base_v070_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_rmin_252d_base_v071_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_rmin_504d_base_v072_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_rmin_252d_base_v073_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_rmin_504d_base_v074_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_rmin_252d_base_v075_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

