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


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_5d_base_v001_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_5d_base_v002_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_5d_base_v003_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_10d_base_v004_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_10d_base_v005_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_10d_base_v006_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_21d_base_v007_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_21d_base_v008_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_21d_base_v009_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_42d_base_v010_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_42d_base_v011_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_42d_base_v012_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_63d_base_v013_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_63d_base_v014_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_63d_base_v015_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_126d_base_v016_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_126d_base_v017_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_126d_base_v018_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_189d_base_v019_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_189d_base_v020_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_189d_base_v021_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_252d_base_v022_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_252d_base_v023_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_252d_base_v024_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_378d_base_v025_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_378d_base_v026_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_378d_base_v027_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_504d_base_v028_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_504d_base_v029_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_504d_base_v030_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_5d_base_v031_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_5d_base_v032_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_5d_base_v033_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_10d_base_v034_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_10d_base_v035_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_10d_base_v036_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_21d_base_v037_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_21d_base_v038_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_21d_base_v039_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_42d_base_v040_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_42d_base_v041_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_42d_base_v042_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_63d_base_v043_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_63d_base_v044_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_63d_base_v045_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_126d_base_v046_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_126d_base_v047_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_126d_base_v048_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_189d_base_v049_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_189d_base_v050_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_189d_base_v051_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_252d_base_v052_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_252d_base_v053_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_252d_base_v054_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_378d_base_v055_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_378d_base_v056_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_378d_base_v057_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_504d_base_v058_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_504d_base_v059_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_504d_base_v060_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_5d_base_v061_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_5d_base_v062_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_5d_base_v063_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_10d_base_v064_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_10d_base_v065_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_10d_base_v066_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_21d_base_v067_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_21d_base_v068_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_21d_base_v069_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_42d_base_v070_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_42d_base_v071_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_42d_base_v072_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_63d_base_v073_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_payout_signal(payoutratio, dps, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_63d_base_v074_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_insider_payout_combo(sharesbas, payoutratio, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_63d_base_v075_signal(sharesbas, payoutratio, dps, closeadj):
    base = _f091_weighted_signal(sharesbas, dps, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_5d_base_v001_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_5d_base_v002_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_5d_base_v003_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_10d_base_v004_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_10d_base_v005_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_10d_base_v006_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_21d_base_v007_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_21d_base_v008_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_21d_base_v009_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_42d_base_v010_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_42d_base_v011_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_42d_base_v012_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_63d_base_v013_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_63d_base_v014_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_63d_base_v015_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_126d_base_v016_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_126d_base_v017_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_126d_base_v018_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_189d_base_v019_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_189d_base_v020_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_189d_base_v021_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_252d_base_v022_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_252d_base_v023_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_252d_base_v024_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_378d_base_v025_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_378d_base_v026_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_378d_base_v027_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_raw_504d_base_v028_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_raw_504d_base_v029_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_raw_504d_base_v030_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_5d_base_v031_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_5d_base_v032_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_5d_base_v033_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_10d_base_v034_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_10d_base_v035_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_10d_base_v036_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_21d_base_v037_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_21d_base_v038_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_21d_base_v039_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_42d_base_v040_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_42d_base_v041_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_42d_base_v042_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_63d_base_v043_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_63d_base_v044_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_63d_base_v045_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_126d_base_v046_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_126d_base_v047_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_126d_base_v048_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_189d_base_v049_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_189d_base_v050_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_189d_base_v051_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_252d_base_v052_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_252d_base_v053_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_252d_base_v054_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_378d_base_v055_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_378d_base_v056_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_378d_base_v057_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_abs_504d_base_v058_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_abs_504d_base_v059_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_abs_504d_base_v060_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_5d_base_v061_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_5d_base_v062_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_5d_base_v063_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_10d_base_v064_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_10d_base_v065_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_10d_base_v066_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_21d_base_v067_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_21d_base_v068_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_21d_base_v069_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_42d_base_v070_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_42d_base_v071_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_42d_base_v072_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_payoutsig_sqrt_63d_base_v073_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_combo_sqrt_63d_base_v074_signal,
    f091rwi_f091_role_weighted_insider_signal_proxy_wsig_sqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F091_ROLE_WEIGHTED_INSIDER_SIGNAL_PROXY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f091_role_weighted_insider_signal_proxy_base_001_075_claude: {n_features} features pass")
