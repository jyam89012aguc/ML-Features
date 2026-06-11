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
def _f037_up_vol(close, volume, w):
    up = (close.diff() > 0).astype(float)
    return (up * volume).rolling(w, min_periods=max(1, w // 2)).sum()


def _f037_down_vol(close, volume, w):
    down = (close.diff() < 0).astype(float)
    return (down * volume).rolling(w, min_periods=max(1, w // 2)).sum()


def _f037_ud_ratio(close, volume, w):
    upv = _f037_up_vol(close, volume, w)
    dnv = _f037_down_vol(close, volume, w)
    return upv / (dnv + 1.0).replace(0, np.nan)


def _make_base_features():
    return []


# 21d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_21d_base_v001_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 21) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_63d_base_v002_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 63) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_126d_base_v003_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 126) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_252d_base_v004_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 252) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_504d_base_v005_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 504) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_5d_base_v006_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 5) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_10d_base_v007_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 10) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_42d_base_v008_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 42) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_189d_base_v009_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 189) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 378d up volume sum
def f037udv_f037_up_down_volume_ratio_upvol_378d_base_v010_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 378) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_21d_base_v011_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 21) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_63d_base_v012_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 63) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_126d_base_v013_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 126) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_252d_base_v014_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 252) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_504d_base_v015_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 504) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_5d_base_v016_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 5) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_10d_base_v017_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 10) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_42d_base_v018_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 42) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_189d_base_v019_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 189) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 378d down volume sum
def f037udv_f037_up_down_volume_ratio_dnvol_378d_base_v020_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 378) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_21d_base_v021_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_63d_base_v022_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_126d_base_v023_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 126) - _f037_down_vol(closeadj, volume, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_252d_base_v024_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_504d_base_v025_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 504) - _f037_down_vol(closeadj, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_5d_base_v026_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 5) - _f037_down_vol(closeadj, volume, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_10d_base_v027_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 10) - _f037_down_vol(closeadj, volume, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_42d_base_v028_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 42) - _f037_down_vol(closeadj, volume, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_189d_base_v029_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 189) - _f037_down_vol(closeadj, volume, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d up-down spread × close
def f037udv_f037_up_down_volume_ratio_udspread_378d_base_v030_signal(closeadj, volume):
    result = (_f037_up_vol(closeadj, volume, 378) - _f037_down_vol(closeadj, volume, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_21d_base_v031_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_63d_base_v032_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_126d_base_v033_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_252d_base_v034_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_504d_base_v035_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_5d_base_v036_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_10d_base_v037_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_42d_base_v038_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_189d_base_v039_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d up-down ratio × close
def f037udv_f037_up_down_volume_ratio_udratio_378d_base_v040_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up volume × close
def f037udv_f037_up_down_volume_ratio_upvolxcl_21d_base_v041_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up volume × close
def f037udv_f037_up_down_volume_ratio_upvolxcl_63d_base_v042_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up volume × close
def f037udv_f037_up_down_volume_ratio_upvolxcl_252d_base_v043_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down volume × close
def f037udv_f037_up_down_volume_ratio_dnvolxcl_21d_base_v044_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down volume × close
def f037udv_f037_up_down_volume_ratio_dnvolxcl_63d_base_v045_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down volume × close
def f037udv_f037_up_down_volume_ratio_dnvolxcl_252d_base_v046_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean up-down ratio × close
def f037udv_f037_up_down_volume_ratio_meanud_21d_base_v047_signal(closeadj, volume):
    result = _mean(_f037_ud_ratio(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean up-down ratio × close
def f037udv_f037_up_down_volume_ratio_meanud_63d_base_v048_signal(closeadj, volume):
    result = _mean(_f037_ud_ratio(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean up-down ratio × close
def f037udv_f037_up_down_volume_ratio_meanud_126d_base_v049_signal(closeadj, volume):
    result = _mean(_f037_ud_ratio(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean up-down ratio × close
def f037udv_f037_up_down_volume_ratio_meanud_252d_base_v050_signal(closeadj, volume):
    result = _mean(_f037_ud_ratio(closeadj, volume, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std up-down ratio × close
def f037udv_f037_up_down_volume_ratio_stdud_21d_base_v051_signal(closeadj, volume):
    result = _std(_f037_ud_ratio(closeadj, volume, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std up-down ratio × close
def f037udv_f037_up_down_volume_ratio_stdud_63d_base_v052_signal(closeadj, volume):
    result = _std(_f037_ud_ratio(closeadj, volume, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std up-down ratio × close
def f037udv_f037_up_down_volume_ratio_stdud_126d_base_v053_signal(closeadj, volume):
    result = _std(_f037_ud_ratio(closeadj, volume, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of up-down ratio × close
def f037udv_f037_up_down_volume_ratio_zud_21d_base_v054_signal(closeadj, volume):
    result = _z(_f037_ud_ratio(closeadj, volume, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of up-down ratio × close
def f037udv_f037_up_down_volume_ratio_zud_63d_base_v055_signal(closeadj, volume):
    result = _z(_f037_ud_ratio(closeadj, volume, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of up-down ratio × close
def f037udv_f037_up_down_volume_ratio_zud_126d_base_v056_signal(closeadj, volume):
    result = _z(_f037_ud_ratio(closeadj, volume, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log up-down ratio × close
def f037udv_f037_up_down_volume_ratio_logud_21d_base_v057_signal(closeadj, volume):
    result = np.log(_f037_ud_ratio(closeadj, volume, 21).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log up-down ratio × close
def f037udv_f037_up_down_volume_ratio_logud_63d_base_v058_signal(closeadj, volume):
    result = np.log(_f037_ud_ratio(closeadj, volume, 63).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log up-down ratio × close
def f037udv_f037_up_down_volume_ratio_logud_252d_base_v059_signal(closeadj, volume):
    result = np.log(_f037_ud_ratio(closeadj, volume, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up/total volume ratio × close
def f037udv_f037_up_down_volume_ratio_upfrac_21d_base_v060_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    total = upv + _f037_down_vol(closeadj, volume, 21)
    result = _safe_div(upv, total) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up/total volume ratio × close
def f037udv_f037_up_down_volume_ratio_upfrac_63d_base_v061_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    total = upv + _f037_down_vol(closeadj, volume, 63)
    result = _safe_div(upv, total) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up/total volume ratio × close
def f037udv_f037_up_down_volume_ratio_upfrac_252d_base_v062_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    total = upv + _f037_down_vol(closeadj, volume, 252)
    result = _safe_div(upv, total) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-down spread × dollar volume
def f037udv_f037_up_down_volume_ratio_spreadxdv_21d_base_v063_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)
    result = spread * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-down spread × dollar volume
def f037udv_f037_up_down_volume_ratio_spreadxdv_63d_base_v064_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)
    result = spread * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-down spread × dollar volume
def f037udv_f037_up_down_volume_ratio_spreadxdv_252d_base_v065_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)
    result = spread * (closeadj * volume) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-down spread normalized
def f037udv_f037_up_down_volume_ratio_udspreadnorm_21d_base_v066_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    result = _safe_div(upv - dnv, upv + dnv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-down spread normalized
def f037udv_f037_up_down_volume_ratio_udspreadnorm_63d_base_v067_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    result = _safe_div(upv - dnv, upv + dnv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up-down spread normalized
def f037udv_f037_up_down_volume_ratio_udspreadnorm_126d_base_v068_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 126)
    dnv = _f037_down_vol(closeadj, volume, 126)
    result = _safe_div(upv - dnv, upv + dnv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-down spread normalized
def f037udv_f037_up_down_volume_ratio_udspreadnorm_252d_base_v069_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    result = _safe_div(upv - dnv, upv + dnv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up-down spread normalized
def f037udv_f037_up_down_volume_ratio_udspreadnorm_504d_base_v070_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 504)
    dnv = _f037_down_vol(closeadj, volume, 504)
    result = _safe_div(upv - dnv, upv + dnv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-down ratio × volume z
def f037udv_f037_up_down_volume_ratio_udxvolz_21d_base_v071_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-down ratio × volume z
def f037udv_f037_up_down_volume_ratio_udxvolz_63d_base_v072_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio - long-term ratio (21d vs 252d divergence)
def f037udv_f037_up_down_volume_ratio_udlonggap_21_252_base_v073_signal(closeadj, volume):
    result = (_f037_ud_ratio(closeadj, volume, 21) - _f037_ud_ratio(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio - long-term ratio (63d vs 504d)
def f037udv_f037_up_down_volume_ratio_udlonggap_63_504_base_v074_signal(closeadj, volume):
    result = (_f037_ud_ratio(closeadj, volume, 63) - _f037_ud_ratio(closeadj, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol × down vol product (variance proxy)
def f037udv_f037_up_down_volume_ratio_udprod_21d_base_v075_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 21) * _f037_down_vol(closeadj, volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f037udv_f037_up_down_volume_ratio_upvol_21d_base_v001_signal,
    f037udv_f037_up_down_volume_ratio_upvol_63d_base_v002_signal,
    f037udv_f037_up_down_volume_ratio_upvol_126d_base_v003_signal,
    f037udv_f037_up_down_volume_ratio_upvol_252d_base_v004_signal,
    f037udv_f037_up_down_volume_ratio_upvol_504d_base_v005_signal,
    f037udv_f037_up_down_volume_ratio_upvol_5d_base_v006_signal,
    f037udv_f037_up_down_volume_ratio_upvol_10d_base_v007_signal,
    f037udv_f037_up_down_volume_ratio_upvol_42d_base_v008_signal,
    f037udv_f037_up_down_volume_ratio_upvol_189d_base_v009_signal,
    f037udv_f037_up_down_volume_ratio_upvol_378d_base_v010_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_21d_base_v011_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_63d_base_v012_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_126d_base_v013_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_252d_base_v014_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_504d_base_v015_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_5d_base_v016_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_10d_base_v017_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_42d_base_v018_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_189d_base_v019_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_378d_base_v020_signal,
    f037udv_f037_up_down_volume_ratio_udspread_21d_base_v021_signal,
    f037udv_f037_up_down_volume_ratio_udspread_63d_base_v022_signal,
    f037udv_f037_up_down_volume_ratio_udspread_126d_base_v023_signal,
    f037udv_f037_up_down_volume_ratio_udspread_252d_base_v024_signal,
    f037udv_f037_up_down_volume_ratio_udspread_504d_base_v025_signal,
    f037udv_f037_up_down_volume_ratio_udspread_5d_base_v026_signal,
    f037udv_f037_up_down_volume_ratio_udspread_10d_base_v027_signal,
    f037udv_f037_up_down_volume_ratio_udspread_42d_base_v028_signal,
    f037udv_f037_up_down_volume_ratio_udspread_189d_base_v029_signal,
    f037udv_f037_up_down_volume_ratio_udspread_378d_base_v030_signal,
    f037udv_f037_up_down_volume_ratio_udratio_21d_base_v031_signal,
    f037udv_f037_up_down_volume_ratio_udratio_63d_base_v032_signal,
    f037udv_f037_up_down_volume_ratio_udratio_126d_base_v033_signal,
    f037udv_f037_up_down_volume_ratio_udratio_252d_base_v034_signal,
    f037udv_f037_up_down_volume_ratio_udratio_504d_base_v035_signal,
    f037udv_f037_up_down_volume_ratio_udratio_5d_base_v036_signal,
    f037udv_f037_up_down_volume_ratio_udratio_10d_base_v037_signal,
    f037udv_f037_up_down_volume_ratio_udratio_42d_base_v038_signal,
    f037udv_f037_up_down_volume_ratio_udratio_189d_base_v039_signal,
    f037udv_f037_up_down_volume_ratio_udratio_378d_base_v040_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_21d_base_v041_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_63d_base_v042_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_252d_base_v043_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_21d_base_v044_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_63d_base_v045_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_252d_base_v046_signal,
    f037udv_f037_up_down_volume_ratio_meanud_21d_base_v047_signal,
    f037udv_f037_up_down_volume_ratio_meanud_63d_base_v048_signal,
    f037udv_f037_up_down_volume_ratio_meanud_126d_base_v049_signal,
    f037udv_f037_up_down_volume_ratio_meanud_252d_base_v050_signal,
    f037udv_f037_up_down_volume_ratio_stdud_21d_base_v051_signal,
    f037udv_f037_up_down_volume_ratio_stdud_63d_base_v052_signal,
    f037udv_f037_up_down_volume_ratio_stdud_126d_base_v053_signal,
    f037udv_f037_up_down_volume_ratio_zud_21d_base_v054_signal,
    f037udv_f037_up_down_volume_ratio_zud_63d_base_v055_signal,
    f037udv_f037_up_down_volume_ratio_zud_126d_base_v056_signal,
    f037udv_f037_up_down_volume_ratio_logud_21d_base_v057_signal,
    f037udv_f037_up_down_volume_ratio_logud_63d_base_v058_signal,
    f037udv_f037_up_down_volume_ratio_logud_252d_base_v059_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_21d_base_v060_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_63d_base_v061_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_252d_base_v062_signal,
    f037udv_f037_up_down_volume_ratio_spreadxdv_21d_base_v063_signal,
    f037udv_f037_up_down_volume_ratio_spreadxdv_63d_base_v064_signal,
    f037udv_f037_up_down_volume_ratio_spreadxdv_252d_base_v065_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_21d_base_v066_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_63d_base_v067_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_126d_base_v068_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_252d_base_v069_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_504d_base_v070_signal,
    f037udv_f037_up_down_volume_ratio_udxvolz_21d_base_v071_signal,
    f037udv_f037_up_down_volume_ratio_udxvolz_63d_base_v072_signal,
    f037udv_f037_up_down_volume_ratio_udlonggap_21_252_base_v073_signal,
    f037udv_f037_up_down_volume_ratio_udlonggap_63_504_base_v074_signal,
    f037udv_f037_up_down_volume_ratio_udprod_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F037_UP_DOWN_VOLUME_RATIO_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f037_up_vol", "_f037_down_vol", "_f037_ud_ratio")
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
    print(f"OK f037_up_down_volume_ratio_base_001_075_claude: {n_features} features pass")
