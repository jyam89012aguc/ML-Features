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
def _f045_dso(receivables, revenue):
    return 365 * receivables / revenue.abs().replace(0, np.nan)


# 21d acceleration of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accel_21d_3d_v001_signal(receivables, closeadj):
    base = receivables
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accel_63d_3d_v002_signal(receivables, closeadj):
    base = receivables
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accel_126d_3d_v003_signal(receivables, closeadj):
    base = receivables
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accel_252d_3d_v004_signal(receivables, closeadj):
    base = receivables
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accel_21d_3d_v005_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accel_63d_3d_v006_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accel_126d_3d_v007_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accel_252d_3d_v008_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accel_21d_3d_v009_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accel_63d_3d_v010_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accel_126d_3d_v011_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accel_252d_3d_v012_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accel_21d_3d_v013_signal(payables, closeadj):
    base = payables
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accel_63d_3d_v014_signal(payables, closeadj):
    base = payables
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accel_126d_3d_v015_signal(payables, closeadj):
    base = payables
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accel_252d_3d_v016_signal(payables, closeadj):
    base = payables
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accel_21d_3d_v017_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accel_63d_3d_v018_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accel_126d_3d_v019_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accel_252d_3d_v020_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accel_21d_3d_v021_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accel_63d_3d_v022_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accel_126d_3d_v023_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accel_252d_3d_v024_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accel_21d_3d_v025_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accel_63d_3d_v026_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accel_126d_3d_v027_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accel_252d_3d_v028_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slopez_21d_z126_3d_v029_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slopez_63d_z252_3d_v030_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slopez_126d_z252_3d_v031_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slopez_252d_z504_3d_v032_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slopez_21d_z126_3d_v033_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slopez_63d_z252_3d_v034_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slopez_126d_z252_3d_v035_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slopez_252d_z504_3d_v036_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slopez_21d_z126_3d_v037_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slopez_63d_z252_3d_v038_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slopez_126d_z252_3d_v039_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slopez_252d_z504_3d_v040_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slopez_21d_z126_3d_v041_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slopez_63d_z252_3d_v042_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slopez_126d_z252_3d_v043_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slopez_252d_z504_3d_v044_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slopez_21d_z126_3d_v045_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slopez_63d_z252_3d_v046_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slopez_126d_z252_3d_v047_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slopez_252d_z504_3d_v048_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slopez_21d_z126_3d_v049_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slopez_63d_z252_3d_v050_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slopez_126d_z252_3d_v051_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slopez_252d_z504_3d_v052_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slopez_21d_z126_3d_v053_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slopez_63d_z252_3d_v054_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slopez_126d_z252_3d_v055_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slopez_252d_z504_3d_v056_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_jerk_21d_3d_v057_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_jerk_63d_3d_v058_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_jerk_126d_3d_v059_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_jerk_21d_3d_v060_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_jerk_63d_3d_v061_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_jerk_126d_3d_v062_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_jerk_21d_3d_v063_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_jerk_63d_3d_v064_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_jerk_126d_3d_v065_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_jerk_21d_3d_v066_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_jerk_63d_3d_v067_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_jerk_126d_3d_v068_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_jerk_21d_3d_v069_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_jerk_63d_3d_v070_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_jerk_126d_3d_v071_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_jerk_21d_3d_v072_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_jerk_63d_3d_v073_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_jerk_126d_3d_v074_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_jerk_21d_3d_v075_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_jerk_63d_3d_v076_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_jerk_126d_3d_v077_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of receivables_lvl smoothed over 252d
def f045rpb_f045_receivables_payables_receivables_lvl_smoothaccel_63d_sm252_3d_v078_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of receivables_lvl smoothed over 504d
def f045rpb_f045_receivables_payables_receivables_lvl_smoothaccel_252d_sm504_3d_v079_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_per_share smoothed over 252d
def f045rpb_f045_receivables_payables_rcv_per_share_smoothaccel_63d_sm252_3d_v080_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_per_share smoothed over 504d
def f045rpb_f045_receivables_payables_rcv_per_share_smoothaccel_252d_sm504_3d_v081_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_yoy smoothed over 252d
def f045rpb_f045_receivables_payables_rcv_yoy_smoothaccel_63d_sm252_3d_v082_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_yoy smoothed over 504d
def f045rpb_f045_receivables_payables_rcv_yoy_smoothaccel_252d_sm504_3d_v083_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of payables_lvl smoothed over 252d
def f045rpb_f045_receivables_payables_payables_lvl_smoothaccel_63d_sm252_3d_v084_signal(payables, closeadj):
    base = payables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of payables_lvl smoothed over 504d
def f045rpb_f045_receivables_payables_payables_lvl_smoothaccel_252d_sm504_3d_v085_signal(payables, closeadj):
    base = payables
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pay_per_share smoothed over 252d
def f045rpb_f045_receivables_payables_pay_per_share_smoothaccel_63d_sm252_3d_v086_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pay_per_share smoothed over 504d
def f045rpb_f045_receivables_payables_pay_per_share_smoothaccel_252d_sm504_3d_v087_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_minus_pay smoothed over 252d
def f045rpb_f045_receivables_payables_rcv_minus_pay_smoothaccel_63d_sm252_3d_v088_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_minus_pay smoothed over 504d
def f045rpb_f045_receivables_payables_rcv_minus_pay_smoothaccel_252d_sm504_3d_v089_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rcv_pay_ratio smoothed over 252d
def f045rpb_f045_receivables_payables_rcv_pay_ratio_smoothaccel_63d_sm252_3d_v090_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rcv_pay_ratio smoothed over 504d
def f045rpb_f045_receivables_payables_rcv_pay_ratio_smoothaccel_252d_sm504_3d_v091_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accelz_21d_z252_3d_v092_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_accelz_63d_z504_3d_v093_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accelz_21d_z252_3d_v094_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_accelz_63d_z504_3d_v095_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accelz_21d_z252_3d_v096_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_accelz_63d_z504_3d_v097_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accelz_21d_z252_3d_v098_signal(payables, closeadj):
    base = payables
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_accelz_63d_z504_3d_v099_signal(payables, closeadj):
    base = payables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accelz_21d_z252_3d_v100_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_accelz_63d_z504_3d_v101_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accelz_21d_z252_3d_v102_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_accelz_63d_z504_3d_v103_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accelz_21d_z252_3d_v104_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_accelz_63d_z504_3d_v105_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in receivables_lvl (raw count, no price scaling)
def f045rpb_f045_receivables_payables_receivables_lvl_signflip_63d_3d_v106_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in receivables_lvl (raw count, no price scaling)
def f045rpb_f045_receivables_payables_receivables_lvl_signflip_252d_3d_v107_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_per_share (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_per_share_signflip_63d_3d_v108_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_per_share (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_per_share_signflip_252d_3d_v109_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_yoy (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_yoy_signflip_63d_3d_v110_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_yoy (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_yoy_signflip_252d_3d_v111_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in payables_lvl (raw count, no price scaling)
def f045rpb_f045_receivables_payables_payables_lvl_signflip_63d_3d_v112_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in payables_lvl (raw count, no price scaling)
def f045rpb_f045_receivables_payables_payables_lvl_signflip_252d_3d_v113_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pay_per_share (raw count, no price scaling)
def f045rpb_f045_receivables_payables_pay_per_share_signflip_63d_3d_v114_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pay_per_share (raw count, no price scaling)
def f045rpb_f045_receivables_payables_pay_per_share_signflip_252d_3d_v115_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_minus_pay (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_minus_pay_signflip_63d_3d_v116_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_minus_pay (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_minus_pay_signflip_252d_3d_v117_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rcv_pay_ratio (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_pay_ratio_signflip_63d_3d_v118_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rcv_pay_ratio (raw count, no price scaling)
def f045rpb_f045_receivables_payables_rcv_pay_ratio_signflip_252d_3d_v119_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of receivables_lvl normalized by 252d range
def f045rpb_f045_receivables_payables_receivables_lvl_rngaccel_63d_r252_3d_v120_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of receivables_lvl normalized by 504d range
def f045rpb_f045_receivables_payables_receivables_lvl_rngaccel_252d_r504_3d_v121_signal(receivables, closeadj):
    base = receivables
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_per_share normalized by 252d range
def f045rpb_f045_receivables_payables_rcv_per_share_rngaccel_63d_r252_3d_v122_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_per_share normalized by 504d range
def f045rpb_f045_receivables_payables_rcv_per_share_rngaccel_252d_r504_3d_v123_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_yoy normalized by 252d range
def f045rpb_f045_receivables_payables_rcv_yoy_rngaccel_63d_r252_3d_v124_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_yoy normalized by 504d range
def f045rpb_f045_receivables_payables_rcv_yoy_rngaccel_252d_r504_3d_v125_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of payables_lvl normalized by 252d range
def f045rpb_f045_receivables_payables_payables_lvl_rngaccel_63d_r252_3d_v126_signal(payables, closeadj):
    base = payables
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of payables_lvl normalized by 504d range
def f045rpb_f045_receivables_payables_payables_lvl_rngaccel_252d_r504_3d_v127_signal(payables, closeadj):
    base = payables
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pay_per_share normalized by 252d range
def f045rpb_f045_receivables_payables_pay_per_share_rngaccel_63d_r252_3d_v128_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pay_per_share normalized by 504d range
def f045rpb_f045_receivables_payables_pay_per_share_rngaccel_252d_r504_3d_v129_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_minus_pay normalized by 252d range
def f045rpb_f045_receivables_payables_rcv_minus_pay_rngaccel_63d_r252_3d_v130_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_minus_pay normalized by 504d range
def f045rpb_f045_receivables_payables_rcv_minus_pay_rngaccel_252d_r504_3d_v131_signal(receivables, payables, closeadj):
    base = receivables - payables
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rcv_pay_ratio normalized by 252d range
def f045rpb_f045_receivables_payables_rcv_pay_ratio_rngaccel_63d_r252_3d_v132_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rcv_pay_ratio normalized by 504d range
def f045rpb_f045_receivables_payables_rcv_pay_ratio_rngaccel_252d_r504_3d_v133_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_cumslope_21d_3d_v134_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_cumslope_63d_3d_v135_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_cumslope_252d_3d_v136_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_cumslope_21d_3d_v137_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_cumslope_63d_3d_v138_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_cumslope_252d_3d_v139_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_cumslope_21d_3d_v140_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_cumslope_63d_3d_v141_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_cumslope_252d_3d_v142_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_cumslope_21d_3d_v143_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_cumslope_63d_3d_v144_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_cumslope_252d_3d_v145_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_cumslope_21d_3d_v146_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_cumslope_63d_3d_v147_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_cumslope_252d_3d_v148_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_cumslope_21d_3d_v149_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_cumslope_63d_3d_v150_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

