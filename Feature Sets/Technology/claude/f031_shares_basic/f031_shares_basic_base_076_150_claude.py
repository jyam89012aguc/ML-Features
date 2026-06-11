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


# 63d z-score of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_z_63d_base_v076_signal(sharesbas, closeadj):
    base = sharesbas
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_z_126d_base_v077_signal(sharesbas, closeadj):
    base = sharesbas
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_z_252d_base_v078_signal(sharesbas, closeadj):
    base = sharesbas
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_z_504d_base_v079_signal(sharesbas, closeadj):
    base = sharesbas
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_z_63d_base_v080_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_z_126d_base_v081_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_z_252d_base_v082_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_z_504d_base_v083_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_z_63d_base_v084_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_z_126d_base_v085_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_z_252d_base_v086_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_z_504d_base_v087_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_z_63d_base_v088_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_z_126d_base_v089_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_z_252d_base_v090_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_z_504d_base_v091_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_z_63d_base_v092_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_z_126d_base_v093_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_z_252d_base_v094_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_z_504d_base_v095_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_z_63d_base_v096_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_z_126d_base_v097_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_z_252d_base_v098_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_z_504d_base_v099_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_z_63d_base_v100_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_z_126d_base_v101_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_z_252d_base_v102_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_z_504d_base_v103_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_distmax_252d_base_v104_signal(sharesbas, closeadj):
    base = sharesbas
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_distmax_504d_base_v105_signal(sharesbas, closeadj):
    base = sharesbas
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_distmax_252d_base_v106_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_distmax_504d_base_v107_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_distmax_252d_base_v108_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_distmax_504d_base_v109_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_distmax_252d_base_v110_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_distmax_504d_base_v111_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_distmax_252d_base_v112_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_distmax_504d_base_v113_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_distmax_252d_base_v114_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_distmax_504d_base_v115_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_distmax_252d_base_v116_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_distmax_504d_base_v117_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_distmed_126d_base_v118_signal(sharesbas, closeadj):
    base = sharesbas
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_distmed_252d_base_v119_signal(sharesbas, closeadj):
    base = sharesbas
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_distmed_504d_base_v120_signal(sharesbas, closeadj):
    base = sharesbas
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_distmed_126d_base_v121_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_distmed_252d_base_v122_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_distmed_504d_base_v123_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_distmed_126d_base_v124_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_distmed_252d_base_v125_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_distmed_504d_base_v126_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_distmed_126d_base_v127_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_distmed_252d_base_v128_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_distmed_504d_base_v129_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_distmed_126d_base_v130_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_distmed_252d_base_v131_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_distmed_504d_base_v132_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_distmed_126d_base_v133_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_distmed_252d_base_v134_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_distmed_504d_base_v135_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_distmed_126d_base_v136_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_distmed_252d_base_v137_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sharesbas_to_mcap
def f031shb_f031_shares_basic_sharesbas_to_mcap_distmed_504d_base_v138_signal(sharesbas, marketcap, closeadj):
    base = sharesbas / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_chg_63d_base_v139_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_lvl
def f031shb_f031_shares_basic_sharesbas_lvl_chg_252d_base_v140_signal(sharesbas, closeadj):
    base = sharesbas
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_chg_63d_base_v141_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_log
def f031shb_f031_shares_basic_sharesbas_log_chg_252d_base_v142_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_chg_63d_base_v143_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_qoq
def f031shb_f031_shares_basic_sharesbas_qoq_chg_252d_base_v144_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_chg_63d_base_v145_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_yoy
def f031shb_f031_shares_basic_sharesbas_yoy_chg_252d_base_v146_signal(sharesbas, closeadj):
    base = _f031_share_yoy(sharesbas)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_chg_63d_base_v147_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_3y
def f031shb_f031_shares_basic_sharesbas_3y_chg_252d_base_v148_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=756)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_chg_63d_base_v149_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sharesbas_5y
def f031shb_f031_shares_basic_sharesbas_5y_chg_252d_base_v150_signal(sharesbas, closeadj):
    base = sharesbas.pct_change(periods=1260)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

