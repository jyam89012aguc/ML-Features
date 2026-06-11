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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f091_payout_signal(payoutratio, dps, w):
    s = payoutratio * dps
    return _mean(s, w)


def _f091_insider_payout_combo(sharesbas, payoutratio, w):
    sd = -sharesbas.pct_change(w).fillna(0)
    return _mean(sd + payoutratio, w)


def _f091_weighted_signal(sharesbas, dps, w):
    sd = -sharesbas.pct_change(w).fillna(0)
    return _mean(sd * dps, w)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose_m1_slope_v001_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_base_m2_slope_v002_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose21_m5_slope_v003_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose63_m10_slope_v004_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose126_m100_slope_v005_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose_m1_slope_v006_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_base_m2_slope_v007_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose21_m5_slope_v008_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose63_m10_slope_v009_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose126_m100_slope_v010_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose_m1_slope_v011_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_base_m2_slope_v012_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose21_m5_slope_v013_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose63_m10_slope_v014_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose126_m100_slope_v015_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose_m1_slope_v016_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_base_m2_slope_v017_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose21_m5_slope_v018_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose63_m10_slope_v019_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose126_m100_slope_v020_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose_m1_slope_v021_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_base_m2_slope_v022_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose21_m5_slope_v023_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose63_m10_slope_v024_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose126_m100_slope_v025_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose_m1_slope_v026_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_base_m2_slope_v027_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose21_m5_slope_v028_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose63_m10_slope_v029_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose126_m100_slope_v030_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose_m1_slope_v031_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_base_m2_slope_v032_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose21_m5_slope_v033_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose63_m10_slope_v034_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose126_m100_slope_v035_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose_m1_slope_v036_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_base_m2_slope_v037_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose21_m5_slope_v038_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose63_m10_slope_v039_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose126_m100_slope_v040_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose_m1_slope_v041_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_base_m2_slope_v042_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose21_m5_slope_v043_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose63_m10_slope_v044_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose126_m100_slope_v045_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose_m1_slope_v046_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_base_m2_slope_v047_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose21_m5_slope_v048_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose63_m10_slope_v049_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose126_m100_slope_v050_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose_m1_slope_v051_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_base_m2_slope_v052_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose21_m5_slope_v053_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose63_m10_slope_v054_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose126_m100_slope_v055_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose_m1_slope_v056_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_base_m2_slope_v057_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose21_m5_slope_v058_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose63_m10_slope_v059_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose126_m100_slope_v060_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose_m1_slope_v061_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_base_m2_slope_v062_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose21_m5_slope_v063_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose63_m10_slope_v064_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose126_m100_slope_v065_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose_m1_slope_v066_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_base_m2_slope_v067_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose21_m5_slope_v068_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose63_m10_slope_v069_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose126_m100_slope_v070_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose_m1_slope_v071_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_base_m2_slope_v072_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose21_m5_slope_v073_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose63_m10_slope_v074_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose126_m100_slope_v075_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose_m1_slope_v076_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_base_m2_slope_v077_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose21_m5_slope_v078_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose63_m10_slope_v079_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose126_m100_slope_v080_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose_m1_slope_v081_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_base_m2_slope_v082_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose21_m5_slope_v083_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose63_m10_slope_v084_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose126_m100_slope_v085_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose_m1_slope_v086_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_base_m2_slope_v087_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose21_m5_slope_v088_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose63_m10_slope_v089_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose126_m100_slope_v090_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose_m1_slope_v091_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_base_m2_slope_v092_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose21_m5_slope_v093_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose63_m10_slope_v094_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose126_m100_slope_v095_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose_m1_slope_v096_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_base_m2_slope_v097_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose21_m5_slope_v098_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose63_m10_slope_v099_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose126_m100_slope_v100_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose_m1_slope_v101_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_base_m2_slope_v102_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose21_m5_slope_v103_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose63_m10_slope_v104_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose126_m100_slope_v105_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose_m1_slope_v106_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_base_m2_slope_v107_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose21_m5_slope_v108_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose63_m10_slope_v109_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose126_m100_slope_v110_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose_m1_slope_v111_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_base_m2_slope_v112_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose21_m5_slope_v113_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose63_m10_slope_v114_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose126_m100_slope_v115_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose_m1_slope_v116_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_base_m2_slope_v117_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose21_m5_slope_v118_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose63_m10_slope_v119_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose126_m100_slope_v120_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose_m1_slope_v121_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_base_m2_slope_v122_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose21_m5_slope_v123_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose63_m10_slope_v124_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose126_m100_slope_v125_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose_m1_slope_v126_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_base_m2_slope_v127_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose21_m5_slope_v128_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose63_m10_slope_v129_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose126_m100_slope_v130_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose_m1_slope_v131_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_base_m2_slope_v132_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose21_m5_slope_v133_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose63_m10_slope_v134_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose126_m100_slope_v135_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose_m1_slope_v136_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_base_m2_slope_v137_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose21_m5_slope_v138_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose63_m10_slope_v139_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose126_m100_slope_v140_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose_m1_slope_v141_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_base_m2_slope_v142_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose21_m5_slope_v143_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose63_m10_slope_v144_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose126_m100_slope_v145_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose_m1_slope_v146_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_base_m2_slope_v147_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose21_m5_slope_v148_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose63_m10_slope_v149_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose126_m100_slope_v150_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose_m1_slope_v001_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_base_m2_slope_v002_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose21_m5_slope_v003_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose63_m10_slope_v004_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_5d_xclose126_m100_slope_v005_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose_m1_slope_v006_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_base_m2_slope_v007_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose21_m5_slope_v008_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose63_m10_slope_v009_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_5d_xclose126_m100_slope_v010_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose_m1_slope_v011_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_base_m2_slope_v012_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose21_m5_slope_v013_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose63_m10_slope_v014_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_10d_xclose126_m100_slope_v015_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose_m1_slope_v016_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_base_m2_slope_v017_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose21_m5_slope_v018_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose63_m10_slope_v019_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_10d_xclose126_m100_slope_v020_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose_m1_slope_v021_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_base_m2_slope_v022_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose21_m5_slope_v023_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose63_m10_slope_v024_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_21d_xclose126_m100_slope_v025_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose_m1_slope_v026_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_base_m2_slope_v027_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose21_m5_slope_v028_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose63_m10_slope_v029_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_21d_xclose126_m100_slope_v030_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose_m1_slope_v031_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_base_m2_slope_v032_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose21_m5_slope_v033_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose63_m10_slope_v034_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_42d_xclose126_m100_slope_v035_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose_m1_slope_v036_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_base_m2_slope_v037_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose21_m5_slope_v038_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose63_m10_slope_v039_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_42d_xclose126_m100_slope_v040_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose_m1_slope_v041_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_base_m2_slope_v042_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose21_m5_slope_v043_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose63_m10_slope_v044_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slpct_63d_xclose126_m100_slope_v045_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose_m1_slope_v046_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_base_m2_slope_v047_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose21_m5_slope_v048_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose63_m10_slope_v049_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsignal_5d_slnorm_63d_xclose126_m100_slope_v050_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose_m1_slope_v051_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_base_m2_slope_v052_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose21_m5_slope_v053_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose63_m10_slope_v054_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_5d_xclose126_m100_slope_v055_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose_m1_slope_v056_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_base_m2_slope_v057_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose21_m5_slope_v058_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose63_m10_slope_v059_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_5d_xclose126_m100_slope_v060_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose_m1_slope_v061_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_base_m2_slope_v062_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose21_m5_slope_v063_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose63_m10_slope_v064_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_10d_xclose126_m100_slope_v065_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose_m1_slope_v066_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_base_m2_slope_v067_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose21_m5_slope_v068_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose63_m10_slope_v069_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_10d_xclose126_m100_slope_v070_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose_m1_slope_v071_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_base_m2_slope_v072_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose21_m5_slope_v073_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose63_m10_slope_v074_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_21d_xclose126_m100_slope_v075_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose_m1_slope_v076_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_base_m2_slope_v077_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose21_m5_slope_v078_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose63_m10_slope_v079_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_21d_xclose126_m100_slope_v080_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose_m1_slope_v081_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_base_m2_slope_v082_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose21_m5_slope_v083_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose63_m10_slope_v084_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_42d_xclose126_m100_slope_v085_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose_m1_slope_v086_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_base_m2_slope_v087_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose21_m5_slope_v088_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose63_m10_slope_v089_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_42d_xclose126_m100_slope_v090_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose_m1_slope_v091_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_base_m2_slope_v092_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose21_m5_slope_v093_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose63_m10_slope_v094_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slpct_63d_xclose126_m100_slope_v095_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose_m1_slope_v096_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_base_m2_slope_v097_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose21_m5_slope_v098_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose63_m10_slope_v099_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_insiderpayoutcombo_5d_slnorm_63d_xclose126_m100_slope_v100_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose_m1_slope_v101_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_base_m2_slope_v102_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose21_m5_slope_v103_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose63_m10_slope_v104_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_5d_xclose126_m100_slope_v105_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose_m1_slope_v106_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_base_m2_slope_v107_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose21_m5_slope_v108_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose63_m10_slope_v109_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_5d_xclose126_m100_slope_v110_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose_m1_slope_v111_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_base_m2_slope_v112_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose21_m5_slope_v113_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose63_m10_slope_v114_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_10d_xclose126_m100_slope_v115_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose_m1_slope_v116_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_base_m2_slope_v117_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose21_m5_slope_v118_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose63_m10_slope_v119_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_10d_xclose126_m100_slope_v120_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose_m1_slope_v121_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_base_m2_slope_v122_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose21_m5_slope_v123_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose63_m10_slope_v124_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_21d_xclose126_m100_slope_v125_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose_m1_slope_v126_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_base_m2_slope_v127_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose21_m5_slope_v128_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose63_m10_slope_v129_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_21d_xclose126_m100_slope_v130_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose_m1_slope_v131_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_base_m2_slope_v132_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose21_m5_slope_v133_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose63_m10_slope_v134_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_42d_xclose126_m100_slope_v135_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose_m1_slope_v136_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_base_m2_slope_v137_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose21_m5_slope_v138_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose63_m10_slope_v139_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_42d_xclose126_m100_slope_v140_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose_m1_slope_v141_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_base_m2_slope_v142_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose21_m5_slope_v143_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose63_m10_slope_v144_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slpct_63d_xclose126_m100_slope_v145_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose_m1_slope_v146_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_base_m2_slope_v147_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose21_m5_slope_v148_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose63_m10_slope_v149_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_weightedsignal_5d_slnorm_63d_xclose126_m100_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F091_ROLE_WEIGHTED_INSIDER_SIGNAL_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f091_payout_signal", "_f091_insider_payout_combo", "_f091_weighted_signal")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f091_role_weighted_insider_signal_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
