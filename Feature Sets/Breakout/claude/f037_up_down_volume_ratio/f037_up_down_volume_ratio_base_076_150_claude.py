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


# 21d sign of (up - down)
def f037udv_f037_up_down_volume_ratio_signspread_21d_base_v076_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of (up - down)
def f037udv_f037_up_down_volume_ratio_signspread_63d_base_v077_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of (up - down)
def f037udv_f037_up_down_volume_ratio_signspread_252d_base_v078_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of ud ratio > 1 × close
def f037udv_f037_up_down_volume_ratio_signud_21d_base_v079_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) - 1.0
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of ud ratio > 1 × close
def f037udv_f037_up_down_volume_ratio_signud_63d_base_v080_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) - 1.0
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of ud ratio > 1 × close
def f037udv_f037_up_down_volume_ratio_signud_252d_base_v081_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252) - 1.0
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up volume × close × normalized
def f037udv_f037_up_down_volume_ratio_upvolxclnorm_21d_base_v082_signal(closeadj, volume):
    base = _safe_div(_f037_up_vol(closeadj, volume, 21), _mean(volume, 21) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up volume × close × normalized
def f037udv_f037_up_down_volume_ratio_upvolxclnorm_63d_base_v083_signal(closeadj, volume):
    base = _safe_div(_f037_up_vol(closeadj, volume, 63), _mean(volume, 63) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up volume × close × normalized
def f037udv_f037_up_down_volume_ratio_upvolxclnorm_252d_base_v084_signal(closeadj, volume):
    base = _safe_div(_f037_up_vol(closeadj, volume, 252), _mean(volume, 126) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down volume × close × normalized
def f037udv_f037_up_down_volume_ratio_dnvolxclnorm_21d_base_v085_signal(closeadj, volume):
    base = _safe_div(_f037_down_vol(closeadj, volume, 21), _mean(volume, 21) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down volume × close × normalized
def f037udv_f037_up_down_volume_ratio_dnvolxclnorm_63d_base_v086_signal(closeadj, volume):
    base = _safe_div(_f037_down_vol(closeadj, volume, 63), _mean(volume, 63) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down volume × close × normalized
def f037udv_f037_up_down_volume_ratio_dnvolxclnorm_252d_base_v087_signal(closeadj, volume):
    base = _safe_div(_f037_down_vol(closeadj, volume, 252), _mean(volume, 126) + 1.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of ud_ratio × close
def f037udv_f037_up_down_volume_ratio_emaud_21d_base_v088_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of ud_ratio × close
def f037udv_f037_up_down_volume_ratio_emaud_63d_base_v089_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of ud_ratio × close
def f037udv_f037_up_down_volume_ratio_emaud_126d_base_v090_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 126).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of ud_ratio × close
def f037udv_f037_up_down_volume_ratio_emaud_252d_base_v091_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 252).ewm(span=126, adjust=False, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of up vol × close
def f037udv_f037_up_down_volume_ratio_emaupvol_21d_base_v092_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of up vol × close
def f037udv_f037_up_down_volume_ratio_emaupvol_63d_base_v093_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of up vol × close
def f037udv_f037_up_down_volume_ratio_emaupvol_252d_base_v094_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 252).ewm(span=126, adjust=False, min_periods=21).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of down vol × close
def f037udv_f037_up_down_volume_ratio_emadnvol_21d_base_v095_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of down vol × close
def f037udv_f037_up_down_volume_ratio_emadnvol_63d_base_v096_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of down vol × close
def f037udv_f037_up_down_volume_ratio_emadnvol_252d_base_v097_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 252).ewm(span=126, adjust=False, min_periods=21).mean() * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol minus close roll-mean × close-vol
def f037udv_f037_up_down_volume_ratio_upvolxclmean_21d_base_v098_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 21) * _mean(closeadj, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up vol × close roll-mean
def f037udv_f037_up_down_volume_ratio_upvolxclmean_63d_base_v099_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 63) * _mean(closeadj, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up vol × close roll-mean
def f037udv_f037_up_down_volume_ratio_upvolxclmean_252d_base_v100_signal(closeadj, volume):
    result = _f037_up_vol(closeadj, volume, 252) * _mean(closeadj, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down vol × close roll-mean
def f037udv_f037_up_down_volume_ratio_dnvolxclmean_21d_base_v101_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 21) * _mean(closeadj, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down vol × close roll-mean
def f037udv_f037_up_down_volume_ratio_dnvolxclmean_63d_base_v102_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 63) * _mean(closeadj, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down vol × close roll-mean
def f037udv_f037_up_down_volume_ratio_dnvolxclmean_252d_base_v103_signal(closeadj, volume):
    result = _f037_down_vol(closeadj, volume, 252) * _mean(closeadj, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud_ratio × close std
def f037udv_f037_up_down_volume_ratio_udxclstd_21d_base_v104_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud_ratio × close std
def f037udv_f037_up_down_volume_ratio_udxclstd_63d_base_v105_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ud_ratio × close std
def f037udv_f037_up_down_volume_ratio_udxclstd_252d_base_v106_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 252) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud spread × z-close
def f037udv_f037_up_down_volume_ratio_spreadxzcl_21d_base_v107_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)
    result = spread * _z(closeadj, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud spread × z-close
def f037udv_f037_up_down_volume_ratio_spreadxzcl_63d_base_v108_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)
    result = spread * _z(closeadj, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ud spread × z-close
def f037udv_f037_up_down_volume_ratio_spreadxzcl_252d_base_v109_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)
    result = spread * _z(closeadj, 252) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sqrt(ud_ratio) × close
def f037udv_f037_up_down_volume_ratio_sqrtud_21d_base_v110_signal(closeadj, volume):
    result = np.sqrt(_f037_ud_ratio(closeadj, volume, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sqrt(ud_ratio) × close
def f037udv_f037_up_down_volume_ratio_sqrtud_63d_base_v111_signal(closeadj, volume):
    result = np.sqrt(_f037_ud_ratio(closeadj, volume, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sqrt(ud_ratio) × close
def f037udv_f037_up_down_volume_ratio_sqrtud_252d_base_v112_signal(closeadj, volume):
    result = np.sqrt(_f037_ud_ratio(closeadj, volume, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sq ud_ratio × close
def f037udv_f037_up_down_volume_ratio_squd_21d_base_v113_signal(closeadj, volume):
    r = _f037_ud_ratio(closeadj, volume, 21)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sq ud_ratio × close
def f037udv_f037_up_down_volume_ratio_squd_63d_base_v114_signal(closeadj, volume):
    r = _f037_ud_ratio(closeadj, volume, 63)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up minus down (normalized) × volume z
def f037udv_f037_up_down_volume_ratio_udnormxvolz_21d_base_v115_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    result = _safe_div(upv - dnv, upv + dnv) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up minus down (normalized) × volume z
def f037udv_f037_up_down_volume_ratio_udnormxvolz_63d_base_v116_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    result = _safe_div(upv - dnv, upv + dnv) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up minus down (normalized) × volume z
def f037udv_f037_up_down_volume_ratio_udnormxvolz_252d_base_v117_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    result = _safe_div(upv - dnv, upv + dnv) * _z(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud_ratio × volume × close
def f037udv_f037_up_down_volume_ratio_udxvolxcl_21d_base_v118_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud_ratio × volume × close
def f037udv_f037_up_down_volume_ratio_udxvolxcl_63d_base_v119_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ud_ratio × volume × close
def f037udv_f037_up_down_volume_ratio_udxvolxcl_252d_base_v120_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 252) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up share (up vol / total day count) × close
def f037udv_f037_up_down_volume_ratio_updaycnt_21d_base_v121_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    total_vol = volume.rolling(21, min_periods=5).sum()
    result = _safe_div(upv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up share (up vol / total day count) × close
def f037udv_f037_up_down_volume_ratio_updaycnt_63d_base_v122_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    total_vol = volume.rolling(63, min_periods=10).sum()
    result = _safe_div(upv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up share × close
def f037udv_f037_up_down_volume_ratio_updaycnt_252d_base_v123_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    total_vol = volume.rolling(252, min_periods=21).sum()
    result = _safe_div(upv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up - down share × close
def f037udv_f037_up_down_volume_ratio_uddifsh_21d_base_v124_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    total_vol = volume.rolling(21, min_periods=5).sum()
    result = _safe_div(upv - dnv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up - down share × close
def f037udv_f037_up_down_volume_ratio_uddifsh_63d_base_v125_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    total_vol = volume.rolling(63, min_periods=10).sum()
    result = _safe_div(upv - dnv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up - down share × close
def f037udv_f037_up_down_volume_ratio_uddifsh_252d_base_v126_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    total_vol = volume.rolling(252, min_periods=21).sum()
    result = _safe_div(upv - dnv, total_vol) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up share - down share × volume mean
def f037udv_f037_up_down_volume_ratio_udsharexvm_21d_base_v127_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    total_vol = volume.rolling(21, min_periods=5).sum()
    result = _safe_div(upv - dnv, total_vol) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud spread × close × volume mean
def f037udv_f037_up_down_volume_ratio_spreadxclxvm_63d_base_v128_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)
    result = spread * closeadj * _mean(volume, 63) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ud spread × close × volume mean
def f037udv_f037_up_down_volume_ratio_spreadxclxvm_252d_base_v129_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)
    result = spread * closeadj * _mean(volume, 126) / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud_ratio × close × volume mean
def f037udv_f037_up_down_volume_ratio_udxclxvm_21d_base_v130_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * closeadj * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud_ratio × close × volume mean
def f037udv_f037_up_down_volume_ratio_udxclxvm_63d_base_v131_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * closeadj * _mean(volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ud_ratio × close × volume mean
def f037udv_f037_up_down_volume_ratio_udxclxvm_252d_base_v132_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 252) * closeadj * _mean(volume, 126) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d abs(ud_ratio - 1) × close (deviation from neutrality)
def f037udv_f037_up_down_volume_ratio_uddev_21d_base_v133_signal(closeadj, volume):
    result = (_f037_ud_ratio(closeadj, volume, 21) - 1.0).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d abs(ud_ratio - 1) × close
def f037udv_f037_up_down_volume_ratio_uddev_63d_base_v134_signal(closeadj, volume):
    result = (_f037_ud_ratio(closeadj, volume, 63) - 1.0).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs(ud_ratio - 1) × close
def f037udv_f037_up_down_volume_ratio_uddev_252d_base_v135_signal(closeadj, volume):
    result = (_f037_ud_ratio(closeadj, volume, 252) - 1.0).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud spread × volume z
def f037udv_f037_up_down_volume_ratio_spreadxvolz_21d_base_v136_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)
    result = spread * _z(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud spread × volume z
def f037udv_f037_up_down_volume_ratio_spreadxvolz_63d_base_v137_signal(closeadj, volume):
    spread = _f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)
    result = spread * _z(volume, 63) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol / (up vol + down vol) - 0.5 deviation × close
def f037udv_f037_up_down_volume_ratio_upbias_21d_base_v138_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    bias = _safe_div(upv, upv + dnv) - 0.5
    result = bias * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up bias × close
def f037udv_f037_up_down_volume_ratio_upbias_63d_base_v139_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    bias = _safe_div(upv, upv + dnv) - 0.5
    result = bias * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up bias × close
def f037udv_f037_up_down_volume_ratio_upbias_252d_base_v140_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    bias = _safe_div(upv, upv + dnv) - 0.5
    result = bias * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol vs 252d up vol gap × close
def f037udv_f037_up_down_volume_ratio_upvolgap_21_252_base_v141_signal(closeadj, volume):
    s21 = _f037_up_vol(closeadj, volume, 21) / 21.0
    s252 = _f037_up_vol(closeadj, volume, 252) / 252.0
    result = (s21 - s252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down vol vs 252d down vol gap × close
def f037udv_f037_up_down_volume_ratio_dnvolgap_21_252_base_v142_signal(closeadj, volume):
    s21 = _f037_down_vol(closeadj, volume, 21) / 21.0
    s252 = _f037_down_vol(closeadj, volume, 252) / 252.0
    result = (s21 - s252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud ratio change from 252d ud ratio × close
def f037udv_f037_up_down_volume_ratio_udregime_21_252_base_v143_signal(closeadj, volume):
    short_r = _f037_ud_ratio(closeadj, volume, 21)
    long_r = _f037_ud_ratio(closeadj, volume, 252)
    result = _safe_div(short_r - long_r, long_r.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud ratio change from 504d × close
def f037udv_f037_up_down_volume_ratio_udregime_63_504_base_v144_signal(closeadj, volume):
    short_r = _f037_ud_ratio(closeadj, volume, 63)
    long_r = _f037_ud_ratio(closeadj, volume, 504)
    result = _safe_div(short_r - long_r, long_r.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ud_ratio × close mean × volume mean
def f037udv_f037_up_down_volume_ratio_udxcmxvm_21d_base_v145_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 21) * _mean(closeadj, 21) * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ud_ratio × close mean × volume mean
def f037udv_f037_up_down_volume_ratio_udxcmxvm_63d_base_v146_signal(closeadj, volume):
    result = _f037_ud_ratio(closeadj, volume, 63) * _mean(closeadj, 63) * _mean(volume, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol minus 252d up vol normalized × close
def f037udv_f037_up_down_volume_ratio_upvolregime_21_252_base_v147_signal(closeadj, volume):
    up21 = _f037_up_vol(closeadj, volume, 21) / 21.0
    up252 = _f037_up_vol(closeadj, volume, 252) / 252.0
    result = _safe_div(up21 - up252, up252.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down vol minus 252d down vol normalized × close
def f037udv_f037_up_down_volume_ratio_dnvolregime_21_252_base_v148_signal(closeadj, volume):
    dn21 = _f037_down_vol(closeadj, volume, 21) / 21.0
    dn252 = _f037_down_vol(closeadj, volume, 252) / 252.0
    result = _safe_div(dn21 - dn252, dn252.abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up vol × down vol product × close
def f037udv_f037_up_down_volume_ratio_udprodxcl_21d_base_v149_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    result = (upv * dnv) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up vol × down vol product × close
def f037udv_f037_up_down_volume_ratio_udprodxcl_63d_base_v150_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    result = (upv * dnv) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f037udv_f037_up_down_volume_ratio_signspread_21d_base_v076_signal,
    f037udv_f037_up_down_volume_ratio_signspread_63d_base_v077_signal,
    f037udv_f037_up_down_volume_ratio_signspread_252d_base_v078_signal,
    f037udv_f037_up_down_volume_ratio_signud_21d_base_v079_signal,
    f037udv_f037_up_down_volume_ratio_signud_63d_base_v080_signal,
    f037udv_f037_up_down_volume_ratio_signud_252d_base_v081_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclnorm_21d_base_v082_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclnorm_63d_base_v083_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclnorm_252d_base_v084_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclnorm_21d_base_v085_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclnorm_63d_base_v086_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclnorm_252d_base_v087_signal,
    f037udv_f037_up_down_volume_ratio_emaud_21d_base_v088_signal,
    f037udv_f037_up_down_volume_ratio_emaud_63d_base_v089_signal,
    f037udv_f037_up_down_volume_ratio_emaud_126d_base_v090_signal,
    f037udv_f037_up_down_volume_ratio_emaud_252d_base_v091_signal,
    f037udv_f037_up_down_volume_ratio_emaupvol_21d_base_v092_signal,
    f037udv_f037_up_down_volume_ratio_emaupvol_63d_base_v093_signal,
    f037udv_f037_up_down_volume_ratio_emaupvol_252d_base_v094_signal,
    f037udv_f037_up_down_volume_ratio_emadnvol_21d_base_v095_signal,
    f037udv_f037_up_down_volume_ratio_emadnvol_63d_base_v096_signal,
    f037udv_f037_up_down_volume_ratio_emadnvol_252d_base_v097_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclmean_21d_base_v098_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclmean_63d_base_v099_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclmean_252d_base_v100_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclmean_21d_base_v101_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclmean_63d_base_v102_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclmean_252d_base_v103_signal,
    f037udv_f037_up_down_volume_ratio_udxclstd_21d_base_v104_signal,
    f037udv_f037_up_down_volume_ratio_udxclstd_63d_base_v105_signal,
    f037udv_f037_up_down_volume_ratio_udxclstd_252d_base_v106_signal,
    f037udv_f037_up_down_volume_ratio_spreadxzcl_21d_base_v107_signal,
    f037udv_f037_up_down_volume_ratio_spreadxzcl_63d_base_v108_signal,
    f037udv_f037_up_down_volume_ratio_spreadxzcl_252d_base_v109_signal,
    f037udv_f037_up_down_volume_ratio_sqrtud_21d_base_v110_signal,
    f037udv_f037_up_down_volume_ratio_sqrtud_63d_base_v111_signal,
    f037udv_f037_up_down_volume_ratio_sqrtud_252d_base_v112_signal,
    f037udv_f037_up_down_volume_ratio_squd_21d_base_v113_signal,
    f037udv_f037_up_down_volume_ratio_squd_63d_base_v114_signal,
    f037udv_f037_up_down_volume_ratio_udnormxvolz_21d_base_v115_signal,
    f037udv_f037_up_down_volume_ratio_udnormxvolz_63d_base_v116_signal,
    f037udv_f037_up_down_volume_ratio_udnormxvolz_252d_base_v117_signal,
    f037udv_f037_up_down_volume_ratio_udxvolxcl_21d_base_v118_signal,
    f037udv_f037_up_down_volume_ratio_udxvolxcl_63d_base_v119_signal,
    f037udv_f037_up_down_volume_ratio_udxvolxcl_252d_base_v120_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_21d_base_v121_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_63d_base_v122_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_252d_base_v123_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_21d_base_v124_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_63d_base_v125_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_252d_base_v126_signal,
    f037udv_f037_up_down_volume_ratio_udsharexvm_21d_base_v127_signal,
    f037udv_f037_up_down_volume_ratio_spreadxclxvm_63d_base_v128_signal,
    f037udv_f037_up_down_volume_ratio_spreadxclxvm_252d_base_v129_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_21d_base_v130_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_63d_base_v131_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_252d_base_v132_signal,
    f037udv_f037_up_down_volume_ratio_uddev_21d_base_v133_signal,
    f037udv_f037_up_down_volume_ratio_uddev_63d_base_v134_signal,
    f037udv_f037_up_down_volume_ratio_uddev_252d_base_v135_signal,
    f037udv_f037_up_down_volume_ratio_spreadxvolz_21d_base_v136_signal,
    f037udv_f037_up_down_volume_ratio_spreadxvolz_63d_base_v137_signal,
    f037udv_f037_up_down_volume_ratio_upbias_21d_base_v138_signal,
    f037udv_f037_up_down_volume_ratio_upbias_63d_base_v139_signal,
    f037udv_f037_up_down_volume_ratio_upbias_252d_base_v140_signal,
    f037udv_f037_up_down_volume_ratio_upvolgap_21_252_base_v141_signal,
    f037udv_f037_up_down_volume_ratio_dnvolgap_21_252_base_v142_signal,
    f037udv_f037_up_down_volume_ratio_udregime_21_252_base_v143_signal,
    f037udv_f037_up_down_volume_ratio_udregime_63_504_base_v144_signal,
    f037udv_f037_up_down_volume_ratio_udxcmxvm_21d_base_v145_signal,
    f037udv_f037_up_down_volume_ratio_udxcmxvm_63d_base_v146_signal,
    f037udv_f037_up_down_volume_ratio_upvolregime_21_252_base_v147_signal,
    f037udv_f037_up_down_volume_ratio_dnvolregime_21_252_base_v148_signal,
    f037udv_f037_up_down_volume_ratio_udprodxcl_21d_base_v149_signal,
    f037udv_f037_up_down_volume_ratio_udprodxcl_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F037_UP_DOWN_VOLUME_RATIO_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f037_up_down_volume_ratio_base_076_150_claude: {n_features} features pass")
