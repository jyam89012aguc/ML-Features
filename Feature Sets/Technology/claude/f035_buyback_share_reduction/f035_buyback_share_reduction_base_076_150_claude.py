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


# 63d z-score of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_z_63d_base_v076_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_z_126d_base_v077_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_z_252d_base_v078_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_z_504d_base_v079_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_z_63d_base_v080_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_z_126d_base_v081_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_z_252d_base_v082_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_z_504d_base_v083_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_z_63d_base_v084_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_z_126d_base_v085_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_z_252d_base_v086_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_z_504d_base_v087_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_z_63d_base_v088_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_z_126d_base_v089_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_z_252d_base_v090_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_z_504d_base_v091_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_z_63d_base_v092_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_z_126d_base_v093_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_z_252d_base_v094_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_z_504d_base_v095_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_z_63d_base_v096_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_z_126d_base_v097_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_z_252d_base_v098_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_z_504d_base_v099_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_z_63d_base_v100_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_z_126d_base_v101_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_z_252d_base_v102_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_z_504d_base_v103_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_distmax_252d_base_v104_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_distmax_504d_base_v105_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_distmax_252d_base_v106_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_distmax_504d_base_v107_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_distmax_252d_base_v108_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_distmax_504d_base_v109_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_distmax_252d_base_v110_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_distmax_504d_base_v111_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_distmax_252d_base_v112_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_distmax_504d_base_v113_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_distmax_252d_base_v114_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_distmax_504d_base_v115_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_distmax_252d_base_v116_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_distmax_504d_base_v117_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_distmed_126d_base_v118_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_distmed_252d_base_v119_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_distmed_504d_base_v120_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_distmed_126d_base_v121_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_distmed_252d_base_v122_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_distmed_504d_base_v123_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_distmed_126d_base_v124_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_distmed_252d_base_v125_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_distmed_504d_base_v126_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_distmed_126d_base_v127_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_distmed_252d_base_v128_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_distmed_504d_base_v129_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_distmed_126d_base_v130_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_distmed_252d_base_v131_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_distmed_504d_base_v132_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_distmed_126d_base_v133_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_distmed_252d_base_v134_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_distmed_504d_base_v135_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_distmed_126d_base_v136_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_distmed_252d_base_v137_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dil_minus_buyback
def f035bsr_f035_buyback_share_reduction_dil_minus_buyback_distmed_504d_base_v138_signal(sbcomp, ncfcommon, marketcap, closeadj):
    base = sbcomp / marketcap.replace(0, np.nan).abs() - (-ncfcommon).clip(lower=0)/marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_chg_63d_base_v139_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in share_red_252d
def f035bsr_f035_buyback_share_reduction_share_red_252d_chg_252d_base_v140_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_chg_63d_base_v141_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in share_red_504d
def f035bsr_f035_buyback_share_reduction_share_red_504d_chg_252d_base_v142_signal(sharesbas, closeadj):
    base = _f035_share_red(sharesbas, 504)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_chg_63d_base_v143_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in buyback_yield_proxy
def f035bsr_f035_buyback_share_reduction_buyback_yield_proxy_chg_252d_base_v144_signal(sharesbas, closeadj):
    base = -sharesbas.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_chg_63d_base_v145_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in net_dil_after_sbc
def f035bsr_f035_buyback_share_reduction_net_dil_after_sbc_chg_252d_base_v146_signal(sharesbas, sbcomp, marketcap, closeadj):
    base = sharesbas.pct_change(periods=252) - sbcomp/marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_chg_63d_base_v147_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in buyback_to_mcap
def f035bsr_f035_buyback_share_reduction_buyback_to_mcap_chg_252d_base_v148_signal(ncfcommon, marketcap, closeadj):
    base = (-ncfcommon).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_chg_63d_base_v149_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in buyback_to_fcf
def f035bsr_f035_buyback_share_reduction_buyback_to_fcf_chg_252d_base_v150_signal(ncfcommon, fcf, closeadj):
    base = (-ncfcommon).clip(lower=0) / fcf.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

