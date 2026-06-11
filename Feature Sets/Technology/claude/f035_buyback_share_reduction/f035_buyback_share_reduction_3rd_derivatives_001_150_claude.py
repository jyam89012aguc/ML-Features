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


# 21d acceleration of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accel_21d_3d_v001_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accel_63d_3d_v002_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accel_126d_3d_v003_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accel_252d_3d_v004_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accel_21d_3d_v005_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accel_63d_3d_v006_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accel_126d_3d_v007_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accel_252d_3d_v008_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accel_21d_3d_v009_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accel_63d_3d_v010_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accel_126d_3d_v011_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accel_252d_3d_v012_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accel_21d_3d_v013_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accel_63d_3d_v014_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accel_126d_3d_v015_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accel_252d_3d_v016_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accel_21d_3d_v017_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accel_63d_3d_v018_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accel_126d_3d_v019_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accel_252d_3d_v020_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accel_21d_3d_v021_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accel_63d_3d_v022_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accel_126d_3d_v023_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accel_252d_3d_v024_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accel_21d_3d_v025_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accel_63d_3d_v026_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accel_126d_3d_v027_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accel_252d_3d_v028_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slopez_21d_z126_3d_v029_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slopez_63d_z252_3d_v030_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slopez_126d_z252_3d_v031_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_slopez_252d_z504_3d_v032_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slopez_21d_z126_3d_v033_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slopez_63d_z252_3d_v034_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slopez_126d_z252_3d_v035_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_slopez_252d_z504_3d_v036_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slopez_21d_z126_3d_v037_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slopez_63d_z252_3d_v038_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slopez_126d_z252_3d_v039_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_slopez_252d_z504_3d_v040_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slopez_21d_z126_3d_v041_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slopez_63d_z252_3d_v042_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slopez_126d_z252_3d_v043_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_slopez_252d_z504_3d_v044_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slopez_21d_z126_3d_v045_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slopez_63d_z252_3d_v046_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slopez_126d_z252_3d_v047_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_slopez_252d_z504_3d_v048_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slopez_21d_z126_3d_v049_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slopez_63d_z252_3d_v050_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slopez_126d_z252_3d_v051_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_slopez_252d_z504_3d_v052_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slopez_21d_z126_3d_v053_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slopez_63d_z252_3d_v054_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slopez_126d_z252_3d_v055_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_slopez_252d_z504_3d_v056_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_jerk_21d_3d_v057_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_jerk_63d_3d_v058_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_jerk_126d_3d_v059_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_jerk_21d_3d_v060_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_jerk_63d_3d_v061_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_jerk_126d_3d_v062_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_jerk_21d_3d_v063_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_jerk_63d_3d_v064_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_jerk_126d_3d_v065_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_jerk_21d_3d_v066_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_jerk_63d_3d_v067_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_jerk_126d_3d_v068_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_jerk_21d_3d_v069_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_jerk_63d_3d_v070_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_jerk_126d_3d_v071_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_jerk_21d_3d_v072_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_jerk_63d_3d_v073_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_jerk_126d_3d_v074_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_jerk_21d_3d_v075_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_jerk_63d_3d_v076_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_jerk_126d_3d_v077_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of share_red_252d smoothed over 252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_smoothaccel_63d_sm252_3d_v078_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of share_red_252d smoothed over 504d
def f035bsr_f035_buyback_share_reduction_share_red_252d_smoothaccel_252d_sm504_3d_v079_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of share_red_504d smoothed over 252d
def f035bsr_f035_buyback_share_reduction_share_red_504d_smoothaccel_63d_sm252_3d_v080_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of share_red_504d smoothed over 504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_smoothaccel_252d_sm504_3d_v081_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of buyback_yield_proxy smoothed over 252d
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_smoothaccel_63d_sm252_3d_v082_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of buyback_yield_proxy smoothed over 504d
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_smoothaccel_252d_sm504_3d_v083_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of net_dil_after_sbc smoothed over 252d
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_smoothaccel_63d_sm252_3d_v084_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of net_dil_after_sbc smoothed over 504d
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_smoothaccel_252d_sm504_3d_v085_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of buyback_to_mcap smoothed over 252d
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_smoothaccel_63d_sm252_3d_v086_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of buyback_to_mcap smoothed over 504d
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_smoothaccel_252d_sm504_3d_v087_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of buyback_to_fcf smoothed over 252d
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_smoothaccel_63d_sm252_3d_v088_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of buyback_to_fcf smoothed over 504d
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_smoothaccel_252d_sm504_3d_v089_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dil_minus_buyback smoothed over 252d
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_smoothaccel_63d_sm252_3d_v090_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dil_minus_buyback smoothed over 504d
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_smoothaccel_252d_sm504_3d_v091_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accelz_21d_z252_3d_v092_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_accelz_63d_z504_3d_v093_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accelz_21d_z252_3d_v094_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_accelz_63d_z504_3d_v095_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accelz_21d_z252_3d_v096_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_accelz_63d_z504_3d_v097_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accelz_21d_z252_3d_v098_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_accelz_63d_z504_3d_v099_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accelz_21d_z252_3d_v100_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_accelz_63d_z504_3d_v101_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accelz_21d_z252_3d_v102_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_accelz_63d_z504_3d_v103_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accelz_21d_z252_3d_v104_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_accelz_63d_z504_3d_v105_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in share_red_252d (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_share_red_252d_signflip_63d_3d_v106_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in share_red_252d (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_share_red_252d_signflip_252d_3d_v107_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in share_red_504d (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_share_red_504d_signflip_63d_3d_v108_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in share_red_504d (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_share_red_504d_signflip_252d_3d_v109_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in buyback_yield_proxy (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_signflip_63d_3d_v110_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in buyback_yield_proxy (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_signflip_252d_3d_v111_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in net_dil_after_sbc (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_signflip_63d_3d_v112_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in net_dil_after_sbc (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_signflip_252d_3d_v113_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in buyback_to_mcap (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_signflip_63d_3d_v114_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in buyback_to_mcap (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_signflip_252d_3d_v115_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in buyback_to_fcf (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_signflip_63d_3d_v116_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in buyback_to_fcf (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_signflip_252d_3d_v117_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dil_minus_buyback (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_signflip_63d_3d_v118_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dil_minus_buyback (raw count, no price scaling)
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_signflip_252d_3d_v119_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of share_red_252d normalized by 252d range
def f035bsr_f035_buyback_share_reduction_share_red_252d_rngaccel_63d_r252_3d_v120_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of share_red_252d normalized by 504d range
def f035bsr_f035_buyback_share_reduction_share_red_252d_rngaccel_252d_r504_3d_v121_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of share_red_504d normalized by 252d range
def f035bsr_f035_buyback_share_reduction_share_red_504d_rngaccel_63d_r252_3d_v122_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of share_red_504d normalized by 504d range
def f035bsr_f035_buyback_share_reduction_share_red_504d_rngaccel_252d_r504_3d_v123_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_yield_proxy normalized by 252d range
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_rngaccel_63d_r252_3d_v124_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_yield_proxy normalized by 504d range
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_rngaccel_252d_r504_3d_v125_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_dil_after_sbc normalized by 252d range
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_rngaccel_63d_r252_3d_v126_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_dil_after_sbc normalized by 504d range
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_rngaccel_252d_r504_3d_v127_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_to_mcap normalized by 252d range
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_rngaccel_63d_r252_3d_v128_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_to_mcap normalized by 504d range
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_rngaccel_252d_r504_3d_v129_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of buyback_to_fcf normalized by 252d range
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_rngaccel_63d_r252_3d_v130_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of buyback_to_fcf normalized by 504d range
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_rngaccel_252d_r504_3d_v131_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dil_minus_buyback normalized by 252d range
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_rngaccel_63d_r252_3d_v132_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dil_minus_buyback normalized by 504d range
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_rngaccel_252d_r504_3d_v133_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_cumslope_21d_3d_v134_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_cumslope_63d_3d_v135_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_cumslope_252d_3d_v136_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_cumslope_21d_3d_v137_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_cumslope_63d_3d_v138_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_cumslope_252d_3d_v139_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_cumslope_21d_3d_v140_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_cumslope_63d_3d_v141_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_cumslope_252d_3d_v142_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_cumslope_21d_3d_v143_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_cumslope_63d_3d_v144_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_cumslope_252d_3d_v145_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_cumslope_21d_3d_v146_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_cumslope_63d_3d_v147_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_cumslope_252d_3d_v148_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_cumslope_21d_3d_v149_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_cumslope_63d_3d_v150_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

