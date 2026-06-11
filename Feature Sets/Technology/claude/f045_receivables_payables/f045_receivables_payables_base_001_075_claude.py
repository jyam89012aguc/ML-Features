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


# 21d mean of receivables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_receivables_lvl_mean_21d_base_v001_signal(receivables, closeadj):
    base = receivables
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of receivables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_receivables_lvl_mean_63d_base_v002_signal(receivables, closeadj):
    base = receivables
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of receivables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_receivables_lvl_mean_126d_base_v003_signal(receivables, closeadj):
    base = receivables
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of receivables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_receivables_lvl_mean_252d_base_v004_signal(receivables, closeadj):
    base = receivables
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of receivables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_receivables_lvl_mean_504d_base_v005_signal(receivables, closeadj):
    base = receivables
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_per_share_mean_21d_base_v006_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_per_share_mean_63d_base_v007_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_per_share_mean_126d_base_v008_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_per_share_mean_252d_base_v009_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_per_share_mean_504d_base_v010_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_yoy scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_yoy_mean_21d_base_v011_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_yoy scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_yoy_mean_63d_base_v012_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_yoy scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_yoy_mean_126d_base_v013_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_yoy scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_yoy_mean_252d_base_v014_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_yoy scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_yoy_mean_504d_base_v015_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of payables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_payables_lvl_mean_21d_base_v016_signal(payables, closeadj):
    base = payables
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of payables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_payables_lvl_mean_63d_base_v017_signal(payables, closeadj):
    base = payables
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of payables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_payables_lvl_mean_126d_base_v018_signal(payables, closeadj):
    base = payables
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of payables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_payables_lvl_mean_252d_base_v019_signal(payables, closeadj):
    base = payables
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of payables_lvl scaled by closeadj
def f045rpb_f045_receivables_payables_payables_lvl_mean_504d_base_v020_signal(payables, closeadj):
    base = payables
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pay_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_pay_per_share_mean_21d_base_v021_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pay_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_pay_per_share_mean_63d_base_v022_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pay_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_pay_per_share_mean_126d_base_v023_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pay_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_pay_per_share_mean_252d_base_v024_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pay_per_share scaled by closeadj
def f045rpb_f045_receivables_payables_pay_per_share_mean_504d_base_v025_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_minus_pay scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_minus_pay_mean_21d_base_v026_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_minus_pay scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_minus_pay_mean_63d_base_v027_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_minus_pay scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_minus_pay_mean_126d_base_v028_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_minus_pay scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_minus_pay_mean_252d_base_v029_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_minus_pay scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_minus_pay_mean_504d_base_v030_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rcv_pay_ratio scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_pay_ratio_mean_21d_base_v031_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rcv_pay_ratio scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_pay_ratio_mean_63d_base_v032_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rcv_pay_ratio scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_pay_ratio_mean_126d_base_v033_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rcv_pay_ratio scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_pay_ratio_mean_252d_base_v034_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rcv_pay_ratio scaled by closeadj
def f045rpb_f045_receivables_payables_rcv_pay_ratio_mean_504d_base_v035_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_median_63d_base_v036_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_median_252d_base_v037_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_median_504d_base_v038_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_median_63d_base_v039_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_median_252d_base_v040_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_median_504d_base_v041_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_median_63d_base_v042_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_median_252d_base_v043_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_median_504d_base_v044_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_median_63d_base_v045_signal(payables, closeadj):
    base = payables
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_median_252d_base_v046_signal(payables, closeadj):
    base = payables
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_median_504d_base_v047_signal(payables, closeadj):
    base = payables
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_median_63d_base_v048_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_median_252d_base_v049_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_median_504d_base_v050_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_median_63d_base_v051_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_median_252d_base_v052_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_median_504d_base_v053_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_median_63d_base_v054_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_median_252d_base_v055_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_median_504d_base_v056_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_rmax_252d_base_v057_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_rmax_504d_base_v058_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_rmax_252d_base_v059_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_rmax_504d_base_v060_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_rmax_252d_base_v061_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_rmax_504d_base_v062_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_rmax_252d_base_v063_signal(payables, closeadj):
    base = payables
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of payables_lvl
def f045rpb_f045_receivables_payables_payables_lvl_rmax_504d_base_v064_signal(payables, closeadj):
    base = payables
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_rmax_252d_base_v065_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of pay_per_share
def f045rpb_f045_receivables_payables_pay_per_share_rmax_504d_base_v066_signal(payables, sharesbas, closeadj):
    base = payables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_rmax_252d_base_v067_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_minus_pay
def f045rpb_f045_receivables_payables_rcv_minus_pay_rmax_504d_base_v068_signal(receivables, payables, closeadj):
    base = receivables - payables
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_rmax_252d_base_v069_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rcv_pay_ratio
def f045rpb_f045_receivables_payables_rcv_pay_ratio_rmax_504d_base_v070_signal(receivables, payables, closeadj):
    base = receivables / payables.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_rmin_252d_base_v071_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of receivables_lvl
def f045rpb_f045_receivables_payables_receivables_lvl_rmin_504d_base_v072_signal(receivables, closeadj):
    base = receivables
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_rmin_252d_base_v073_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rcv_per_share
def f045rpb_f045_receivables_payables_rcv_per_share_rmin_504d_base_v074_signal(receivables, sharesbas, closeadj):
    base = receivables / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rcv_yoy
def f045rpb_f045_receivables_payables_rcv_yoy_rmin_252d_base_v075_signal(receivables, closeadj):
    base = receivables.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

