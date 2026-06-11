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
def _f09_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f09_margin_recovery(ebitdamargin, w):
    # current vs rolling min — how far margin recovered from trough
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f09_margin_durability(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    em_std = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm + em) - (gm_std + em_std)


def f09urc_f09_utility_rate_case_signature_mfloor_mean_5d_base_v001_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_mean_21d_base_v002_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_mean_63d_base_v003_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_mean_126d_base_v004_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_mean_252d_base_v005_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_std_5d_base_v006_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_floor(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_std_21d_base_v007_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_floor(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_std_63d_base_v008_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_floor(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_std_126d_base_v009_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_floor(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_std_252d_base_v010_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_floor(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_z_5d_base_v011_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_floor(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_z_21d_base_v012_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_floor(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_z_63d_base_v013_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_floor(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_z_126d_base_v014_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_floor(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_z_252d_base_v015_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_floor(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_ema_5d_base_v016_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_ema_21d_base_v017_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_ema_63d_base_v018_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_ema_126d_base_v019_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_ema_252d_base_v020_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_range_5d_base_v021_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_range_21d_base_v022_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_range_63d_base_v023_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_range_126d_base_v024_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_range_252d_base_v025_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_mean_5d_base_v026_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_mean_21d_base_v027_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_mean_63d_base_v028_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_mean_126d_base_v029_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_mean_252d_base_v030_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_std_5d_base_v031_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_recovery(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_std_21d_base_v032_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_recovery(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_std_63d_base_v033_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_recovery(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_std_126d_base_v034_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_recovery(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_std_252d_base_v035_signal(ebitdamargin, closeadj):
    result = _std(_f09_margin_recovery(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_z_5d_base_v036_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_recovery(ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_z_21d_base_v037_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_recovery(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_z_63d_base_v038_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_recovery(ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_z_126d_base_v039_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_recovery(ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_z_252d_base_v040_signal(ebitdamargin, closeadj):
    result = _z(_f09_margin_recovery(ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_ema_5d_base_v041_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_ema_21d_base_v042_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_ema_63d_base_v043_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_ema_126d_base_v044_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_ema_252d_base_v045_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_range_5d_base_v046_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_range_21d_base_v047_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_range_63d_base_v048_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_range_126d_base_v049_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_range_252d_base_v050_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_mean_5d_base_v051_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_mean_21d_base_v052_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_mean_63d_base_v053_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_mean_126d_base_v054_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_mean_252d_base_v055_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_std_5d_base_v056_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f09_margin_durability(grossmargin, ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_std_21d_base_v057_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f09_margin_durability(grossmargin, ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_std_63d_base_v058_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f09_margin_durability(grossmargin, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_std_126d_base_v059_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f09_margin_durability(grossmargin, ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_std_252d_base_v060_signal(grossmargin, ebitdamargin, closeadj):
    result = _std(_f09_margin_durability(grossmargin, ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_z_5d_base_v061_signal(grossmargin, ebitdamargin, closeadj):
    result = _z(_f09_margin_durability(grossmargin, ebitdamargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_z_21d_base_v062_signal(grossmargin, ebitdamargin, closeadj):
    result = _z(_f09_margin_durability(grossmargin, ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_z_63d_base_v063_signal(grossmargin, ebitdamargin, closeadj):
    result = _z(_f09_margin_durability(grossmargin, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_z_126d_base_v064_signal(grossmargin, ebitdamargin, closeadj):
    result = _z(_f09_margin_durability(grossmargin, ebitdamargin, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_z_252d_base_v065_signal(grossmargin, ebitdamargin, closeadj):
    result = _z(_f09_margin_durability(grossmargin, ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_ema_5d_base_v066_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 5)).ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_ema_21d_base_v067_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_ema_63d_base_v068_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_ema_126d_base_v069_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 126)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_ema_252d_base_v070_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 252)).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_range_5d_base_v071_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 5)
    result = (_b.rolling(5, min_periods=max(1, 5//2)).max() - _b.rolling(5, min_periods=max(1, 5//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_range_21d_base_v072_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = (_b.rolling(21, min_periods=max(1, 21//2)).max() - _b.rolling(21, min_periods=max(1, 21//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_range_63d_base_v073_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = (_b.rolling(63, min_periods=max(1, 63//2)).max() - _b.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_range_126d_base_v074_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 126)
    result = (_b.rolling(126, min_periods=max(1, 126//2)).max() - _b.rolling(126, min_periods=max(1, 126//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_range_252d_base_v075_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 252)
    result = (_b.rolling(252, min_periods=max(1, 252//2)).max() - _b.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f09urc_f09_utility_rate_case_signature_mfloor_mean_5d_base_v001_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_mean_21d_base_v002_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_mean_63d_base_v003_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_mean_126d_base_v004_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_mean_252d_base_v005_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_std_5d_base_v006_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_std_21d_base_v007_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_std_63d_base_v008_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_std_126d_base_v009_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_std_252d_base_v010_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_z_5d_base_v011_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_z_21d_base_v012_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_z_63d_base_v013_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_z_126d_base_v014_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_z_252d_base_v015_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_ema_5d_base_v016_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_ema_21d_base_v017_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_ema_63d_base_v018_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_ema_126d_base_v019_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_ema_252d_base_v020_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_range_5d_base_v021_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_range_21d_base_v022_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_range_63d_base_v023_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_range_126d_base_v024_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_range_252d_base_v025_signal,
    f09urc_f09_utility_rate_case_signature_mrec_mean_5d_base_v026_signal,
    f09urc_f09_utility_rate_case_signature_mrec_mean_21d_base_v027_signal,
    f09urc_f09_utility_rate_case_signature_mrec_mean_63d_base_v028_signal,
    f09urc_f09_utility_rate_case_signature_mrec_mean_126d_base_v029_signal,
    f09urc_f09_utility_rate_case_signature_mrec_mean_252d_base_v030_signal,
    f09urc_f09_utility_rate_case_signature_mrec_std_5d_base_v031_signal,
    f09urc_f09_utility_rate_case_signature_mrec_std_21d_base_v032_signal,
    f09urc_f09_utility_rate_case_signature_mrec_std_63d_base_v033_signal,
    f09urc_f09_utility_rate_case_signature_mrec_std_126d_base_v034_signal,
    f09urc_f09_utility_rate_case_signature_mrec_std_252d_base_v035_signal,
    f09urc_f09_utility_rate_case_signature_mrec_z_5d_base_v036_signal,
    f09urc_f09_utility_rate_case_signature_mrec_z_21d_base_v037_signal,
    f09urc_f09_utility_rate_case_signature_mrec_z_63d_base_v038_signal,
    f09urc_f09_utility_rate_case_signature_mrec_z_126d_base_v039_signal,
    f09urc_f09_utility_rate_case_signature_mrec_z_252d_base_v040_signal,
    f09urc_f09_utility_rate_case_signature_mrec_ema_5d_base_v041_signal,
    f09urc_f09_utility_rate_case_signature_mrec_ema_21d_base_v042_signal,
    f09urc_f09_utility_rate_case_signature_mrec_ema_63d_base_v043_signal,
    f09urc_f09_utility_rate_case_signature_mrec_ema_126d_base_v044_signal,
    f09urc_f09_utility_rate_case_signature_mrec_ema_252d_base_v045_signal,
    f09urc_f09_utility_rate_case_signature_mrec_range_5d_base_v046_signal,
    f09urc_f09_utility_rate_case_signature_mrec_range_21d_base_v047_signal,
    f09urc_f09_utility_rate_case_signature_mrec_range_63d_base_v048_signal,
    f09urc_f09_utility_rate_case_signature_mrec_range_126d_base_v049_signal,
    f09urc_f09_utility_rate_case_signature_mrec_range_252d_base_v050_signal,
    f09urc_f09_utility_rate_case_signature_mdur_mean_5d_base_v051_signal,
    f09urc_f09_utility_rate_case_signature_mdur_mean_21d_base_v052_signal,
    f09urc_f09_utility_rate_case_signature_mdur_mean_63d_base_v053_signal,
    f09urc_f09_utility_rate_case_signature_mdur_mean_126d_base_v054_signal,
    f09urc_f09_utility_rate_case_signature_mdur_mean_252d_base_v055_signal,
    f09urc_f09_utility_rate_case_signature_mdur_std_5d_base_v056_signal,
    f09urc_f09_utility_rate_case_signature_mdur_std_21d_base_v057_signal,
    f09urc_f09_utility_rate_case_signature_mdur_std_63d_base_v058_signal,
    f09urc_f09_utility_rate_case_signature_mdur_std_126d_base_v059_signal,
    f09urc_f09_utility_rate_case_signature_mdur_std_252d_base_v060_signal,
    f09urc_f09_utility_rate_case_signature_mdur_z_5d_base_v061_signal,
    f09urc_f09_utility_rate_case_signature_mdur_z_21d_base_v062_signal,
    f09urc_f09_utility_rate_case_signature_mdur_z_63d_base_v063_signal,
    f09urc_f09_utility_rate_case_signature_mdur_z_126d_base_v064_signal,
    f09urc_f09_utility_rate_case_signature_mdur_z_252d_base_v065_signal,
    f09urc_f09_utility_rate_case_signature_mdur_ema_5d_base_v066_signal,
    f09urc_f09_utility_rate_case_signature_mdur_ema_21d_base_v067_signal,
    f09urc_f09_utility_rate_case_signature_mdur_ema_63d_base_v068_signal,
    f09urc_f09_utility_rate_case_signature_mdur_ema_126d_base_v069_signal,
    f09urc_f09_utility_rate_case_signature_mdur_ema_252d_base_v070_signal,
    f09urc_f09_utility_rate_case_signature_mdur_range_5d_base_v071_signal,
    f09urc_f09_utility_rate_case_signature_mdur_range_21d_base_v072_signal,
    f09urc_f09_utility_rate_case_signature_mdur_range_63d_base_v073_signal,
    f09urc_f09_utility_rate_case_signature_mdur_range_126d_base_v074_signal,
    f09urc_f09_utility_rate_case_signature_mdur_range_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_UTILITY_RATE_CASE_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "grossmargin": grossmargin,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_margin_floor", "_f09_margin_recovery", "_f09_margin_durability",)
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
    print(f"OK f09_utility_rate_case_signature_base_001_075_claude: {n_features} features pass")
