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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f05_ltd_ratio(debt, deposits):
    return debt / deposits.replace(0, np.nan).abs()


def _f05_ltd_dynamics(debt, deposits, w):
    r = debt / deposits.replace(0, np.nan).abs()
    return r - r.shift(w)


def _f05_ltd_stability(debt, deposits, w):
    r = debt / deposits.replace(0, np.nan).abs()
    m = r.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_5d_base_v001_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_5d_base_v002_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_5d_base_v003_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_5d_base_v004_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_5d_base_v005_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_5d_base_v006_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_5d_base_v007_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_5d_base_v008_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_5d_base_v009_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 5) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_5d_base_v010_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 5), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_5d_base_v011_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_5d_base_v012_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_5d_base_v013_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_5d_base_v014_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 5 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_5d_base_v015_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_10d_base_v016_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_10d_base_v017_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_10d_base_v018_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_10d_base_v019_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 41) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_10d_base_v020_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_10d_base_v021_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_10d_base_v022_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_10d_base_v023_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_10d_base_v024_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 10) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_10d_base_v025_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 10), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_10d_base_v026_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_10d_base_v027_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_10d_base_v028_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_10d_base_v029_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 10 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_10d_base_v030_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_21d_base_v031_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_21d_base_v032_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_21d_base_v033_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_21d_base_v034_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_21d_base_v035_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_21d_base_v036_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_21d_base_v037_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_21d_base_v038_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_21d_base_v039_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_21d_base_v040_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 21), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_21d_base_v041_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_21d_base_v042_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_21d_base_v043_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_21d_base_v044_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 21 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_21d_base_v045_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_42d_base_v046_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_42d_base_v047_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_42d_base_v048_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_42d_base_v049_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_42d_base_v050_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_42d_base_v051_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_42d_base_v052_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_42d_base_v053_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_42d_base_v054_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 42) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_42d_base_v055_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 42), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_42d_base_v056_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_42d_base_v057_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_42d_base_v058_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 42) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_42d_base_v059_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 42 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_42d_base_v060_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_63d_base_v061_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_63d_base_v062_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_63d_base_v063_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_63d_base_v064_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_63d_base_v065_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_63d_base_v066_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_63d_base_v067_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_63d_base_v068_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_63d_base_v069_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 63) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_63d_base_v070_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 63), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_63d_base_v071_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_63d_base_v072_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_63d_base_v073_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_63d_base_v074_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 63 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_63d_base_v075_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_5d_base_v001_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_5d_base_v002_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_5d_base_v003_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_5d_base_v004_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_5d_base_v005_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_5d_base_v006_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_5d_base_v007_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_5d_base_v008_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_5d_base_v009_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_5d_base_v010_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_5d_base_v011_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_5d_base_v012_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_5d_base_v013_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_5d_base_v014_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_5d_base_v015_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_10d_base_v016_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_10d_base_v017_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_10d_base_v018_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_10d_base_v019_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_10d_base_v020_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_10d_base_v021_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_10d_base_v022_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_10d_base_v023_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_10d_base_v024_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_10d_base_v025_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_10d_base_v026_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_10d_base_v027_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_10d_base_v028_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_10d_base_v029_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_10d_base_v030_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_21d_base_v031_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_21d_base_v032_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_21d_base_v033_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_21d_base_v034_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_21d_base_v035_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_21d_base_v036_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_21d_base_v037_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_21d_base_v038_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_21d_base_v039_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_21d_base_v040_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_21d_base_v041_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_21d_base_v042_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_21d_base_v043_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_21d_base_v044_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_21d_base_v045_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_42d_base_v046_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_42d_base_v047_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_42d_base_v048_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_42d_base_v049_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_42d_base_v050_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_42d_base_v051_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_42d_base_v052_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_42d_base_v053_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_42d_base_v054_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_42d_base_v055_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_42d_base_v056_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_42d_base_v057_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_42d_base_v058_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_42d_base_v059_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_42d_base_v060_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_63d_base_v061_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_63d_base_v062_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_63d_base_v063_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_63d_base_v064_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_63d_base_v065_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_63d_base_v066_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_63d_base_v067_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_63d_base_v068_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_63d_base_v069_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_63d_base_v070_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_63d_base_v071_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_63d_base_v072_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_63d_base_v073_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_63d_base_v074_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_LOAN_TO_DEPOSIT_DYNAMICS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deposits     = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="deposits")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "deposits": deposits,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f05_ltd_ratio", "_f05_ltd_dynamics", "_f05_ltd_stability",)
    import hashlib
    seen_bodies = set()
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
        # body hash dup check
        body_lines = [ln.strip() for ln in src.splitlines()
                      if ln.strip() and not ln.strip().startswith("#") and not ln.strip().startswith("def ")]
        body_hash = hashlib.sha1("\n".join(body_lines).encode()).hexdigest()
        assert body_hash not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(body_hash)
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_loan_to_deposit_dynamics_base_001_075_claude: {n_features} features pass, 0 dup bodies")
