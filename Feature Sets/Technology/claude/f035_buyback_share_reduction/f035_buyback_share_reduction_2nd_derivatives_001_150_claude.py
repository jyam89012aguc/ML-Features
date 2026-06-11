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
def _f035_share_red(sharesbas, n):
    return -sharesbas.diff(periods=n)


# 21d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slope_21d_2d_v001_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slope_63d_2d_v002_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slope_126d_2d_v003_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slope_252d_2d_v004_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slope_504d_2d_v005_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slope_21d_2d_v006_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slope_63d_2d_v007_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slope_126d_2d_v008_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slope_252d_2d_v009_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slope_504d_2d_v010_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slope_21d_2d_v011_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slope_63d_2d_v012_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slope_126d_2d_v013_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slope_252d_2d_v014_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slope_504d_2d_v015_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slope_21d_2d_v016_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slope_63d_2d_v017_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slope_126d_2d_v018_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slope_252d_2d_v019_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slope_504d_2d_v020_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slope_21d_2d_v021_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slope_63d_2d_v022_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slope_126d_2d_v023_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slope_252d_2d_v024_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slope_504d_2d_v025_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slope_21d_2d_v026_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slope_63d_2d_v027_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slope_126d_2d_v028_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slope_252d_2d_v029_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slope_504d_2d_v030_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slope_21d_2d_v031_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slope_63d_2d_v032_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slope_126d_2d_v033_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slope_252d_2d_v034_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slope_504d_2d_v035_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sm21_sl21_2d_v036_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sm63_sl21_2d_v037_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sm63_sl63_2d_v038_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sm252_sl63_2d_v039_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sm252_sl126_2d_v040_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sm21_sl21_2d_v041_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sm63_sl21_2d_v042_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sm63_sl63_2d_v043_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sm252_sl63_2d_v044_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sm252_sl126_2d_v045_signal(sharesbas, closeadj):
    base = _mean(_f035_share_red(sharesbas, 504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sm21_sl21_2d_v046_signal(sharesbas, closeadj):
    base = _mean(-sharesbas.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sm63_sl21_2d_v047_signal(sharesbas, closeadj):
    base = _mean(-sharesbas.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sm63_sl63_2d_v048_signal(sharesbas, closeadj):
    base = _mean(-sharesbas.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sm252_sl63_2d_v049_signal(sharesbas, closeadj):
    base = _mean(-sharesbas.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sm252_sl126_2d_v050_signal(sharesbas, closeadj):
    base = _mean(-sharesbas.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sm21_sl21_2d_v051_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = _mean(sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sm63_sl21_2d_v052_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = _mean(sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sm63_sl63_2d_v053_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = _mean(sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sm252_sl63_2d_v054_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = _mean(sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sm252_sl126_2d_v055_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = _mean(sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sm21_sl21_2d_v056_signal(ncfcommon, marketcap, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sm63_sl21_2d_v057_signal(ncfcommon, marketcap, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sm63_sl63_2d_v058_signal(ncfcommon, marketcap, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sm252_sl63_2d_v059_signal(ncfcommon, marketcap, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sm252_sl126_2d_v060_signal(ncfcommon, marketcap, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sm21_sl21_2d_v061_signal(ncfcommon, fcf, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sm63_sl21_2d_v062_signal(ncfcommon, fcf, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sm63_sl63_2d_v063_signal(ncfcommon, fcf, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sm252_sl63_2d_v064_signal(ncfcommon, fcf, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sm252_sl126_2d_v065_signal(ncfcommon, fcf, closeadj):
    base = _mean((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sm21_sl21_2d_v066_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sm63_sl21_2d_v067_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sm63_sl63_2d_v068_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sm252_sl63_2d_v069_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sm252_sl126_2d_v070_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = _mean(sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_pctslope_21d_2d_v071_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_pctslope_63d_2d_v072_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_pctslope_252d_2d_v073_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_pctslope_21d_2d_v074_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_pctslope_63d_2d_v075_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_pctslope_252d_2d_v076_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_pctslope_21d_2d_v077_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_pctslope_63d_2d_v078_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_pctslope_252d_2d_v079_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_pctslope_21d_2d_v080_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_pctslope_63d_2d_v081_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_pctslope_252d_2d_v082_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_pctslope_21d_2d_v083_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_pctslope_63d_2d_v084_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_pctslope_252d_2d_v085_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_pctslope_21d_2d_v086_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_pctslope_63d_2d_v087_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_pctslope_252d_2d_v088_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_pctslope_21d_2d_v089_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_pctslope_63d_2d_v090_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_pctslope_252d_2d_v091_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sgnslope_21d_2d_v092_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sgnslope_63d_2d_v093_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_sgnslope_252d_2d_v094_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sgnslope_21d_2d_v095_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sgnslope_63d_2d_v096_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_sgnslope_252d_2d_v097_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sgnslope_21d_2d_v098_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sgnslope_63d_2d_v099_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_sgnslope_252d_2d_v100_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sgnslope_21d_2d_v101_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sgnslope_63d_2d_v102_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_sgnslope_252d_2d_v103_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sgnslope_21d_2d_v104_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sgnslope_63d_2d_v105_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_sgnslope_252d_2d_v106_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sgnslope_21d_2d_v107_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sgnslope_63d_2d_v108_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_sgnslope_252d_2d_v109_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sgnslope_21d_2d_v110_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sgnslope_63d_2d_v111_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_sgnslope_252d_2d_v112_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_logmagslope_21d_2d_v113_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_logmagslope_63d_2d_v114_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_logmagslope_252d_2d_v115_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_logmagslope_21d_2d_v116_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_logmagslope_63d_2d_v117_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_logmagslope_252d_2d_v118_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_logmagslope_21d_2d_v119_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_logmagslope_63d_2d_v120_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_logmagslope_252d_2d_v121_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_logmagslope_21d_2d_v122_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_logmagslope_63d_2d_v123_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_logmagslope_252d_2d_v124_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_logmagslope_21d_2d_v125_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_logmagslope_63d_2d_v126_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_logmagslope_252d_2d_v127_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_logmagslope_21d_2d_v128_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_logmagslope_63d_2d_v129_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_logmagslope_252d_2d_v130_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_logmagslope_21d_2d_v131_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_logmagslope_63d_2d_v132_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_logmagslope_252d_2d_v133_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|share_red_252d|
def f035bsr_f035_buyback_share_reduction_share_red_252d_logslope_63d_2d_v134_signal(sharesbas, closeadj):
    base = np.log((_f035_share_red(sharesbas, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|share_red_252d|
def f035bsr_f035_buyback_share_reduction_share_red_252d_logslope_252d_2d_v135_signal(sharesbas, closeadj):
    base = np.log((_f035_share_red(sharesbas, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|share_red_504d|
def f035bsr_f035_buyback_share_reduction_share_red_504d_logslope_63d_2d_v136_signal(sharesbas, closeadj):
    base = np.log((_f035_share_red(sharesbas, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|share_red_504d|
def f035bsr_f035_buyback_share_reduction_share_red_504d_logslope_252d_2d_v137_signal(sharesbas, closeadj):
    base = np.log((_f035_share_red(sharesbas, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|buyback_yield_proxy|
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_logslope_63d_2d_v138_signal(sharesbas, closeadj):
    base = np.log((-sharesbas.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|buyback_yield_proxy|
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_logslope_252d_2d_v139_signal(sharesbas, closeadj):
    base = np.log((-sharesbas.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|net_dil_after_sbc|
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_logslope_63d_2d_v140_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = np.log((sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|net_dil_after_sbc|
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_logslope_252d_2d_v141_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = np.log((sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|buyback_to_mcap|
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_logslope_63d_2d_v142_signal(ncfcommon, marketcap, closeadj):
    base = np.log(((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|buyback_to_mcap|
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_logslope_252d_2d_v143_signal(ncfcommon, marketcap, closeadj):
    base = np.log(((-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|buyback_to_fcf|
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_logslope_63d_2d_v144_signal(ncfcommon, fcf, closeadj):
    base = np.log(((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|buyback_to_fcf|
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_logslope_252d_2d_v145_signal(ncfcommon, fcf, closeadj):
    base = np.log(((-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dil_minus_buyback|
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_logslope_63d_2d_v146_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = np.log((sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dil_minus_buyback|
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_logslope_252d_2d_v147_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = np.log((sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

