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


# 21d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slope_21d_2d_v001_signal(receivables, closeadj):
    base = receivables
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slope_63d_2d_v002_signal(receivables, closeadj):
    base = receivables
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slope_126d_2d_v003_signal(receivables, closeadj):
    base = receivables
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slope_252d_2d_v004_signal(receivables, closeadj):
    base = receivables
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_slope_504d_2d_v005_signal(receivables, closeadj):
    base = receivables
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slope_21d_2d_v006_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slope_63d_2d_v007_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slope_126d_2d_v008_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slope_252d_2d_v009_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_slope_504d_2d_v010_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slope_21d_2d_v011_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slope_63d_2d_v012_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slope_126d_2d_v013_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slope_252d_2d_v014_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_slope_504d_2d_v015_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slope_21d_2d_v016_signal(payables, closeadj):
    base = payables
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slope_63d_2d_v017_signal(payables, closeadj):
    base = payables
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slope_126d_2d_v018_signal(payables, closeadj):
    base = payables
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slope_252d_2d_v019_signal(payables, closeadj):
    base = payables
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_slope_504d_2d_v020_signal(payables, closeadj):
    base = payables
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slope_21d_2d_v021_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slope_63d_2d_v022_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slope_126d_2d_v023_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slope_252d_2d_v024_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_slope_504d_2d_v025_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slope_21d_2d_v026_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slope_63d_2d_v027_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slope_126d_2d_v028_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slope_252d_2d_v029_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_slope_504d_2d_v030_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slope_21d_2d_v031_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slope_63d_2d_v032_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slope_126d_2d_v033_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slope_252d_2d_v034_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_slope_504d_2d_v035_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sm21_sl21_2d_v036_signal(receivables, closeadj):
    base = _mean(receivables, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sm63_sl21_2d_v037_signal(receivables, closeadj):
    base = _mean(receivables, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sm63_sl63_2d_v038_signal(receivables, closeadj):
    base = _mean(receivables, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sm252_sl63_2d_v039_signal(receivables, closeadj):
    base = _mean(receivables, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sm252_sl126_2d_v040_signal(receivables, closeadj):
    base = _mean(receivables, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sm21_sl21_2d_v041_signal(receivables, sharesbas, closeadj):
    base = _mean(receivables / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sm63_sl21_2d_v042_signal(receivables, sharesbas, closeadj):
    base = _mean(receivables / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sm63_sl63_2d_v043_signal(receivables, sharesbas, closeadj):
    base = _mean(receivables / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sm252_sl63_2d_v044_signal(receivables, sharesbas, closeadj):
    base = _mean(receivables / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sm252_sl126_2d_v045_signal(receivables, sharesbas, closeadj):
    base = _mean(receivables / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sm21_sl21_2d_v046_signal(receivables, closeadj):
    base = _mean(receivables.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sm63_sl21_2d_v047_signal(receivables, closeadj):
    base = _mean(receivables.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sm63_sl63_2d_v048_signal(receivables, closeadj):
    base = _mean(receivables.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sm252_sl63_2d_v049_signal(receivables, closeadj):
    base = _mean(receivables.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sm252_sl126_2d_v050_signal(receivables, closeadj):
    base = _mean(receivables.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sm21_sl21_2d_v051_signal(payables, closeadj):
    base = _mean(payables, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sm63_sl21_2d_v052_signal(payables, closeadj):
    base = _mean(payables, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sm63_sl63_2d_v053_signal(payables, closeadj):
    base = _mean(payables, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sm252_sl63_2d_v054_signal(payables, closeadj):
    base = _mean(payables, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sm252_sl126_2d_v055_signal(payables, closeadj):
    base = _mean(payables, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sm21_sl21_2d_v056_signal(payables, sharesbas, closeadj):
    base = _mean(payables / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sm63_sl21_2d_v057_signal(payables, sharesbas, closeadj):
    base = _mean(payables / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sm63_sl63_2d_v058_signal(payables, sharesbas, closeadj):
    base = _mean(payables / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sm252_sl63_2d_v059_signal(payables, sharesbas, closeadj):
    base = _mean(payables / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sm252_sl126_2d_v060_signal(payables, sharesbas, closeadj):
    base = _mean(payables / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sm21_sl21_2d_v061_signal(receivables, payables, closeadj):
    base = _mean(receivables - payables, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sm63_sl21_2d_v062_signal(receivables, payables, closeadj):
    base = _mean(receivables - payables, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sm63_sl63_2d_v063_signal(receivables, payables, closeadj):
    base = _mean(receivables - payables, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sm252_sl63_2d_v064_signal(receivables, payables, closeadj):
    base = _mean(receivables - payables, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sm252_sl126_2d_v065_signal(receivables, payables, closeadj):
    base = _mean(receivables - payables, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sm21_sl21_2d_v066_signal(receivables, payables, closeadj):
    base = _mean(receivables / payables.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sm63_sl21_2d_v067_signal(receivables, payables, closeadj):
    base = _mean(receivables / payables.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sm63_sl63_2d_v068_signal(receivables, payables, closeadj):
    base = _mean(receivables / payables.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sm252_sl63_2d_v069_signal(receivables, payables, closeadj):
    base = _mean(receivables / payables.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sm252_sl126_2d_v070_signal(receivables, payables, closeadj):
    base = _mean(receivables / payables.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_pctslope_21d_2d_v071_signal(receivables, closeadj):
    base = receivables
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_pctslope_63d_2d_v072_signal(receivables, closeadj):
    base = receivables
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_pctslope_252d_2d_v073_signal(receivables, closeadj):
    base = receivables
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_pctslope_21d_2d_v074_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_pctslope_63d_2d_v075_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_pctslope_252d_2d_v076_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_pctslope_21d_2d_v077_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_pctslope_63d_2d_v078_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_pctslope_252d_2d_v079_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_pctslope_21d_2d_v080_signal(payables, closeadj):
    base = payables
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_pctslope_63d_2d_v081_signal(payables, closeadj):
    base = payables
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_pctslope_252d_2d_v082_signal(payables, closeadj):
    base = payables
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_pctslope_21d_2d_v083_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_pctslope_63d_2d_v084_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_pctslope_252d_2d_v085_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_pctslope_21d_2d_v086_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_pctslope_63d_2d_v087_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_pctslope_252d_2d_v088_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_pctslope_21d_2d_v089_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_pctslope_63d_2d_v090_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_pctslope_252d_2d_v091_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sgnslope_21d_2d_v092_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sgnslope_63d_2d_v093_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_sgnslope_252d_2d_v094_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sgnslope_21d_2d_v095_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sgnslope_63d_2d_v096_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_sgnslope_252d_2d_v097_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sgnslope_21d_2d_v098_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sgnslope_63d_2d_v099_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_sgnslope_252d_2d_v100_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sgnslope_21d_2d_v101_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sgnslope_63d_2d_v102_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_sgnslope_252d_2d_v103_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sgnslope_21d_2d_v104_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sgnslope_63d_2d_v105_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_sgnslope_252d_2d_v106_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sgnslope_21d_2d_v107_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sgnslope_63d_2d_v108_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_sgnslope_252d_2d_v109_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sgnslope_21d_2d_v110_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sgnslope_63d_2d_v111_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_sgnslope_252d_2d_v112_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_logmagslope_21d_2d_v113_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_logmagslope_63d_2d_v114_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_logmagslope_252d_2d_v115_signal(receivables, closeadj):
    base = receivables
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_logmagslope_21d_2d_v116_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_logmagslope_63d_2d_v117_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_logmagslope_252d_2d_v118_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_logmagslope_21d_2d_v119_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_logmagslope_63d_2d_v120_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_logmagslope_252d_2d_v121_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_logmagslope_21d_2d_v122_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_logmagslope_63d_2d_v123_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_logmagslope_252d_2d_v124_signal(payables, closeadj):
    base = payables
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_logmagslope_21d_2d_v125_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_logmagslope_63d_2d_v126_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_logmagslope_252d_2d_v127_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_logmagslope_21d_2d_v128_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_logmagslope_63d_2d_v129_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_logmagslope_252d_2d_v130_signal(receivables, payables, closeadj):
    base = receivables - payables
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_logmagslope_21d_2d_v131_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_logmagslope_63d_2d_v132_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_logmagslope_252d_2d_v133_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|receivables_lvl|
def f045rpb_f045_receivables_payables_receivables_lvl_logslope_63d_2d_v134_signal(receivables, closeadj):
    base = np.log((receivables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|receivables_lvl|
def f045rpb_f045_receivables_payables_receivables_lvl_logslope_252d_2d_v135_signal(receivables, closeadj):
    base = np.log((receivables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_per_share|
def f045rpb_f045_receivables_payables_rcv_per_share_logslope_63d_2d_v136_signal(receivables, sharesbas, closeadj):
    base = np.log((receivables / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_per_share|
def f045rpb_f045_receivables_payables_rcv_per_share_logslope_252d_2d_v137_signal(receivables, sharesbas, closeadj):
    base = np.log((receivables / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_yoy|
def f045rpb_f045_receivables_payables_rcv_yoy_logslope_63d_2d_v138_signal(receivables, closeadj):
    base = np.log((receivables.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_yoy|
def f045rpb_f045_receivables_payables_rcv_yoy_logslope_252d_2d_v139_signal(receivables, closeadj):
    base = np.log((receivables.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|payables_lvl|
def f045rpb_f045_receivables_payables_payables_lvl_logslope_63d_2d_v140_signal(payables, closeadj):
    base = np.log((payables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|payables_lvl|
def f045rpb_f045_receivables_payables_payables_lvl_logslope_252d_2d_v141_signal(payables, closeadj):
    base = np.log((payables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|pay_per_share|
def f045rpb_f045_receivables_payables_pay_per_share_logslope_63d_2d_v142_signal(payables, sharesbas, closeadj):
    base = np.log((payables / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|pay_per_share|
def f045rpb_f045_receivables_payables_pay_per_share_logslope_252d_2d_v143_signal(payables, sharesbas, closeadj):
    base = np.log((payables / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_minus_pay|
def f045rpb_f045_receivables_payables_rcv_minus_pay_logslope_63d_2d_v144_signal(receivables, payables, closeadj):
    base = np.log((receivables - payables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_minus_pay|
def f045rpb_f045_receivables_payables_rcv_minus_pay_logslope_252d_2d_v145_signal(receivables, payables, closeadj):
    base = np.log((receivables - payables).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rcv_pay_ratio|
def f045rpb_f045_receivables_payables_rcv_pay_ratio_logslope_63d_2d_v146_signal(receivables, payables, closeadj):
    base = np.log((receivables / payables.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rcv_pay_ratio|
def f045rpb_f045_receivables_payables_rcv_pay_ratio_logslope_252d_2d_v147_signal(receivables, payables, closeadj):
    base = np.log((receivables / payables.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

