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
def _f045_dso(receivables, revenue):
    return 365 * receivables / revenue.abs().replace(0, np.nan)


# 63d z-score of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_z_63d_base_v076_signal(receivables, closeadj):
    base = receivables
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_z_126d_base_v077_signal(receivables, closeadj):
    base = receivables
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_z_252d_base_v078_signal(receivables, closeadj):
    base = receivables
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_z_504d_base_v079_signal(receivables, closeadj):
    base = receivables
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_z_63d_base_v080_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_z_126d_base_v081_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_z_252d_base_v082_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_z_504d_base_v083_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_z_63d_base_v084_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_z_126d_base_v085_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_z_252d_base_v086_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_z_504d_base_v087_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_z_63d_base_v088_signal(payables, closeadj):
    base = payables
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_z_126d_base_v089_signal(payables, closeadj):
    base = payables
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_z_252d_base_v090_signal(payables, closeadj):
    base = payables
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_z_504d_base_v091_signal(payables, closeadj):
    base = payables
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_z_63d_base_v092_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_z_126d_base_v093_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_z_252d_base_v094_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_z_504d_base_v095_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_z_63d_base_v096_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_z_126d_base_v097_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_z_252d_base_v098_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_z_504d_base_v099_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_z_63d_base_v100_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_z_126d_base_v101_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_z_252d_base_v102_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_z_504d_base_v103_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_distmax_252d_base_v104_signal(receivables, closeadj):
    base = receivables
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_distmax_504d_base_v105_signal(receivables, closeadj):
    base = receivables
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_distmax_252d_base_v106_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_distmax_504d_base_v107_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_distmax_252d_base_v108_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_distmax_504d_base_v109_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_distmax_252d_base_v110_signal(payables, closeadj):
    base = payables
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_distmax_504d_base_v111_signal(payables, closeadj):
    base = payables
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_distmax_252d_base_v112_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_distmax_504d_base_v113_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_distmax_252d_base_v114_signal(receivables, payables, closeadj):
    base = receivables - payables
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_distmax_504d_base_v115_signal(receivables, payables, closeadj):
    base = receivables - payables
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_distmax_252d_base_v116_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_distmax_504d_base_v117_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_distmed_126d_base_v118_signal(receivables, closeadj):
    base = receivables
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_distmed_252d_base_v119_signal(receivables, closeadj):
    base = receivables
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_distmed_504d_base_v120_signal(receivables, closeadj):
    base = receivables
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_distmed_126d_base_v121_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_distmed_252d_base_v122_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_distmed_504d_base_v123_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_distmed_126d_base_v124_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_distmed_252d_base_v125_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_distmed_504d_base_v126_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_distmed_126d_base_v127_signal(payables, closeadj):
    base = payables
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_distmed_252d_base_v128_signal(payables, closeadj):
    base = payables
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_distmed_504d_base_v129_signal(payables, closeadj):
    base = payables
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_distmed_126d_base_v130_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_distmed_252d_base_v131_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_distmed_504d_base_v132_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_distmed_126d_base_v133_signal(receivables, payables, closeadj):
    base = receivables - payables
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_distmed_252d_base_v134_signal(receivables, payables, closeadj):
    base = receivables - payables
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_distmed_504d_base_v135_signal(receivables, payables, closeadj):
    base = receivables - payables
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_distmed_126d_base_v136_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_distmed_252d_base_v137_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_distmed_504d_base_v138_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_chg_63d_base_v139_signal(receivables, closeadj):
    base = receivables
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_chg_252d_base_v140_signal(receivables, closeadj):
    base = receivables
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_chg_63d_base_v141_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_chg_252d_base_v142_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_chg_63d_base_v143_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_chg_252d_base_v144_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_chg_63d_base_v145_signal(payables, closeadj):
    base = payables
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_chg_252d_base_v146_signal(payables, closeadj):
    base = payables
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_chg_63d_base_v147_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_chg_252d_base_v148_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_chg_63d_base_v149_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_chg_252d_base_v150_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

