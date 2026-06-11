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
def _f08_payout_floor(payoutratio, w):
    # rolling min as durability floor
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()


def _f08_payout_durability(payoutratio, eps, w):
    # stable payoutratio when eps grows; penalize when eps falls
    eg = eps.pct_change(w).fillna(0)
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return p_smooth * (1.0 + eg)


def _f08_payout_sustainability(payoutratio, fcfps, w):
    # payout vs fcfps coverage
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    cov = fcfps.rolling(w, min_periods=max(1, w // 2)).mean() / fcfps.rolling(w, min_periods=max(1, w // 2)).mean().abs().replace(0, np.nan)
    return p_smooth - cov.abs()


def f08upd_f08_utility_payout_durability_pfloor_mean_5d_base_v001_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_mean_21d_base_v002_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_mean_63d_base_v003_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_mean_126d_base_v004_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_mean_252d_base_v005_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_std_5d_base_v006_signal(payoutratio, closeadj):
    result = _std(_f08_payout_floor(payoutratio, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_std_21d_base_v007_signal(payoutratio, closeadj):
    result = _std(_f08_payout_floor(payoutratio, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_std_63d_base_v008_signal(payoutratio, closeadj):
    result = _std(_f08_payout_floor(payoutratio, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_std_126d_base_v009_signal(payoutratio, closeadj):
    result = _std(_f08_payout_floor(payoutratio, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_std_252d_base_v010_signal(payoutratio, closeadj):
    result = _std(_f08_payout_floor(payoutratio, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_z_5d_base_v011_signal(payoutratio, closeadj):
    result = _z(_f08_payout_floor(payoutratio, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_z_21d_base_v012_signal(payoutratio, closeadj):
    result = _z(_f08_payout_floor(payoutratio, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_z_63d_base_v013_signal(payoutratio, closeadj):
    result = _z(_f08_payout_floor(payoutratio, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_z_126d_base_v014_signal(payoutratio, closeadj):
    result = _z(_f08_payout_floor(payoutratio, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_z_252d_base_v015_signal(payoutratio, closeadj):
    result = _z(_f08_payout_floor(payoutratio, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_ema_5d_base_v016_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_ema_21d_base_v017_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_ema_63d_base_v018_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_ema_126d_base_v019_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_ema_252d_base_v020_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_range_5d_base_v021_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_range_21d_base_v022_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_range_63d_base_v023_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_range_126d_base_v024_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_range_252d_base_v025_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_mean_5d_base_v026_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_mean_21d_base_v027_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_mean_63d_base_v028_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_mean_126d_base_v029_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_mean_252d_base_v030_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_std_5d_base_v031_signal(payoutratio, eps, closeadj):
    result = _std(_f08_payout_durability(payoutratio, eps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_std_21d_base_v032_signal(payoutratio, eps, closeadj):
    result = _std(_f08_payout_durability(payoutratio, eps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_std_63d_base_v033_signal(payoutratio, eps, closeadj):
    result = _std(_f08_payout_durability(payoutratio, eps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_std_126d_base_v034_signal(payoutratio, eps, closeadj):
    result = _std(_f08_payout_durability(payoutratio, eps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_std_252d_base_v035_signal(payoutratio, eps, closeadj):
    result = _std(_f08_payout_durability(payoutratio, eps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_z_5d_base_v036_signal(payoutratio, eps, closeadj):
    result = _z(_f08_payout_durability(payoutratio, eps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_z_21d_base_v037_signal(payoutratio, eps, closeadj):
    result = _z(_f08_payout_durability(payoutratio, eps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_z_63d_base_v038_signal(payoutratio, eps, closeadj):
    result = _z(_f08_payout_durability(payoutratio, eps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_z_126d_base_v039_signal(payoutratio, eps, closeadj):
    result = _z(_f08_payout_durability(payoutratio, eps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_z_252d_base_v040_signal(payoutratio, eps, closeadj):
    result = _z(_f08_payout_durability(payoutratio, eps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_ema_5d_base_v041_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_ema_21d_base_v042_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_ema_63d_base_v043_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_ema_126d_base_v044_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_ema_252d_base_v045_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_range_5d_base_v046_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_range_21d_base_v047_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_range_63d_base_v048_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_range_126d_base_v049_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_range_252d_base_v050_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_mean_5d_base_v051_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_mean_21d_base_v052_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_mean_63d_base_v053_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_mean_126d_base_v054_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_mean_252d_base_v055_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_std_5d_base_v056_signal(payoutratio, fcfps, closeadj):
    result = _std(_f08_payout_sustainability(payoutratio, fcfps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_std_21d_base_v057_signal(payoutratio, fcfps, closeadj):
    result = _std(_f08_payout_sustainability(payoutratio, fcfps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_std_63d_base_v058_signal(payoutratio, fcfps, closeadj):
    result = _std(_f08_payout_sustainability(payoutratio, fcfps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_std_126d_base_v059_signal(payoutratio, fcfps, closeadj):
    result = _std(_f08_payout_sustainability(payoutratio, fcfps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_std_252d_base_v060_signal(payoutratio, fcfps, closeadj):
    result = _std(_f08_payout_sustainability(payoutratio, fcfps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_z_5d_base_v061_signal(payoutratio, fcfps, closeadj):
    result = _z(_f08_payout_sustainability(payoutratio, fcfps, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_z_21d_base_v062_signal(payoutratio, fcfps, closeadj):
    result = _z(_f08_payout_sustainability(payoutratio, fcfps, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_z_63d_base_v063_signal(payoutratio, fcfps, closeadj):
    result = _z(_f08_payout_sustainability(payoutratio, fcfps, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_z_126d_base_v064_signal(payoutratio, fcfps, closeadj):
    result = _z(_f08_payout_sustainability(payoutratio, fcfps, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_z_252d_base_v065_signal(payoutratio, fcfps, closeadj):
    result = _z(_f08_payout_sustainability(payoutratio, fcfps, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_ema_5d_base_v066_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_ema_21d_base_v067_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_ema_63d_base_v068_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_ema_126d_base_v069_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_ema_252d_base_v070_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_range_5d_base_v071_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_range_21d_base_v072_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_range_63d_base_v073_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_range_126d_base_v074_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_range_252d_base_v075_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f08upd_f08_utility_payout_durability_pfloor_mean_5d_base_v001_signal,
    f08upd_f08_utility_payout_durability_pfloor_mean_21d_base_v002_signal,
    f08upd_f08_utility_payout_durability_pfloor_mean_63d_base_v003_signal,
    f08upd_f08_utility_payout_durability_pfloor_mean_126d_base_v004_signal,
    f08upd_f08_utility_payout_durability_pfloor_mean_252d_base_v005_signal,
    f08upd_f08_utility_payout_durability_pfloor_std_5d_base_v006_signal,
    f08upd_f08_utility_payout_durability_pfloor_std_21d_base_v007_signal,
    f08upd_f08_utility_payout_durability_pfloor_std_63d_base_v008_signal,
    f08upd_f08_utility_payout_durability_pfloor_std_126d_base_v009_signal,
    f08upd_f08_utility_payout_durability_pfloor_std_252d_base_v010_signal,
    f08upd_f08_utility_payout_durability_pfloor_z_5d_base_v011_signal,
    f08upd_f08_utility_payout_durability_pfloor_z_21d_base_v012_signal,
    f08upd_f08_utility_payout_durability_pfloor_z_63d_base_v013_signal,
    f08upd_f08_utility_payout_durability_pfloor_z_126d_base_v014_signal,
    f08upd_f08_utility_payout_durability_pfloor_z_252d_base_v015_signal,
    f08upd_f08_utility_payout_durability_pfloor_ema_5d_base_v016_signal,
    f08upd_f08_utility_payout_durability_pfloor_ema_21d_base_v017_signal,
    f08upd_f08_utility_payout_durability_pfloor_ema_63d_base_v018_signal,
    f08upd_f08_utility_payout_durability_pfloor_ema_126d_base_v019_signal,
    f08upd_f08_utility_payout_durability_pfloor_ema_252d_base_v020_signal,
    f08upd_f08_utility_payout_durability_pfloor_range_5d_base_v021_signal,
    f08upd_f08_utility_payout_durability_pfloor_range_21d_base_v022_signal,
    f08upd_f08_utility_payout_durability_pfloor_range_63d_base_v023_signal,
    f08upd_f08_utility_payout_durability_pfloor_range_126d_base_v024_signal,
    f08upd_f08_utility_payout_durability_pfloor_range_252d_base_v025_signal,
    f08upd_f08_utility_payout_durability_pdur_mean_5d_base_v026_signal,
    f08upd_f08_utility_payout_durability_pdur_mean_21d_base_v027_signal,
    f08upd_f08_utility_payout_durability_pdur_mean_63d_base_v028_signal,
    f08upd_f08_utility_payout_durability_pdur_mean_126d_base_v029_signal,
    f08upd_f08_utility_payout_durability_pdur_mean_252d_base_v030_signal,
    f08upd_f08_utility_payout_durability_pdur_std_5d_base_v031_signal,
    f08upd_f08_utility_payout_durability_pdur_std_21d_base_v032_signal,
    f08upd_f08_utility_payout_durability_pdur_std_63d_base_v033_signal,
    f08upd_f08_utility_payout_durability_pdur_std_126d_base_v034_signal,
    f08upd_f08_utility_payout_durability_pdur_std_252d_base_v035_signal,
    f08upd_f08_utility_payout_durability_pdur_z_5d_base_v036_signal,
    f08upd_f08_utility_payout_durability_pdur_z_21d_base_v037_signal,
    f08upd_f08_utility_payout_durability_pdur_z_63d_base_v038_signal,
    f08upd_f08_utility_payout_durability_pdur_z_126d_base_v039_signal,
    f08upd_f08_utility_payout_durability_pdur_z_252d_base_v040_signal,
    f08upd_f08_utility_payout_durability_pdur_ema_5d_base_v041_signal,
    f08upd_f08_utility_payout_durability_pdur_ema_21d_base_v042_signal,
    f08upd_f08_utility_payout_durability_pdur_ema_63d_base_v043_signal,
    f08upd_f08_utility_payout_durability_pdur_ema_126d_base_v044_signal,
    f08upd_f08_utility_payout_durability_pdur_ema_252d_base_v045_signal,
    f08upd_f08_utility_payout_durability_pdur_range_5d_base_v046_signal,
    f08upd_f08_utility_payout_durability_pdur_range_21d_base_v047_signal,
    f08upd_f08_utility_payout_durability_pdur_range_63d_base_v048_signal,
    f08upd_f08_utility_payout_durability_pdur_range_126d_base_v049_signal,
    f08upd_f08_utility_payout_durability_pdur_range_252d_base_v050_signal,
    f08upd_f08_utility_payout_durability_psus_mean_5d_base_v051_signal,
    f08upd_f08_utility_payout_durability_psus_mean_21d_base_v052_signal,
    f08upd_f08_utility_payout_durability_psus_mean_63d_base_v053_signal,
    f08upd_f08_utility_payout_durability_psus_mean_126d_base_v054_signal,
    f08upd_f08_utility_payout_durability_psus_mean_252d_base_v055_signal,
    f08upd_f08_utility_payout_durability_psus_std_5d_base_v056_signal,
    f08upd_f08_utility_payout_durability_psus_std_21d_base_v057_signal,
    f08upd_f08_utility_payout_durability_psus_std_63d_base_v058_signal,
    f08upd_f08_utility_payout_durability_psus_std_126d_base_v059_signal,
    f08upd_f08_utility_payout_durability_psus_std_252d_base_v060_signal,
    f08upd_f08_utility_payout_durability_psus_z_5d_base_v061_signal,
    f08upd_f08_utility_payout_durability_psus_z_21d_base_v062_signal,
    f08upd_f08_utility_payout_durability_psus_z_63d_base_v063_signal,
    f08upd_f08_utility_payout_durability_psus_z_126d_base_v064_signal,
    f08upd_f08_utility_payout_durability_psus_z_252d_base_v065_signal,
    f08upd_f08_utility_payout_durability_psus_ema_5d_base_v066_signal,
    f08upd_f08_utility_payout_durability_psus_ema_21d_base_v067_signal,
    f08upd_f08_utility_payout_durability_psus_ema_63d_base_v068_signal,
    f08upd_f08_utility_payout_durability_psus_ema_126d_base_v069_signal,
    f08upd_f08_utility_payout_durability_psus_ema_252d_base_v070_signal,
    f08upd_f08_utility_payout_durability_psus_range_5d_base_v071_signal,
    f08upd_f08_utility_payout_durability_psus_range_21d_base_v072_signal,
    f08upd_f08_utility_payout_durability_psus_range_63d_base_v073_signal,
    f08upd_f08_utility_payout_durability_psus_range_126d_base_v074_signal,
    f08upd_f08_utility_payout_durability_psus_range_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_UTILITY_PAYOUT_DURABILITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    fcfps = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")

    cols = {
        "closeadj": closeadj, "eps": eps, "fcfps": fcfps, "dps": dps,
        "payoutratio": payoutratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_payout_floor", "_f08_payout_durability", "_f08_payout_sustainability",)
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
    print(f"OK f08_utility_payout_durability_base_001_075_claude: {n_features} features pass")
