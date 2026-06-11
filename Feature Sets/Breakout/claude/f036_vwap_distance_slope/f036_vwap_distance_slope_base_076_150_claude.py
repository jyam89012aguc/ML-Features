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
def _f036_vwap(close, volume, w):
    pv = (close * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return pv / vv.replace(0, np.nan)


def _f036_vwap_distance(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return (close - vwap) / vwap.replace(0, np.nan).abs()


def _f036_vwap_slope(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return vwap.diff(periods=w) / vwap.abs().replace(0, np.nan)


# 21d sign of vwap distance × close
def f036vds_f036_vwap_distance_slope_signdist_21d_base_v076_signal(closeadj, volume):
    result = np.sign(_f036_vwap_distance(closeadj, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of vwap distance × close
def f036vds_f036_vwap_distance_slope_signdist_63d_base_v077_signal(closeadj, volume):
    result = np.sign(_f036_vwap_distance(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of vwap distance × close
def f036vds_f036_vwap_distance_slope_signdist_252d_base_v078_signal(closeadj, volume):
    result = np.sign(_f036_vwap_distance(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of vwap slope × close
def f036vds_f036_vwap_distance_slope_signslope_21d_base_v079_signal(closeadj, volume):
    result = np.sign(_f036_vwap_slope(closeadj, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of vwap slope × close
def f036vds_f036_vwap_distance_slope_signslope_63d_base_v080_signal(closeadj, volume):
    result = np.sign(_f036_vwap_slope(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of vwap slope × close
def f036vds_f036_vwap_distance_slope_signslope_252d_base_v081_signal(closeadj, volume):
    result = np.sign(_f036_vwap_slope(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log abs vwap × close
def f036vds_f036_vwap_distance_slope_logvwap_21d_base_v082_signal(closeadj, volume):
    result = np.log(_f036_vwap(closeadj, volume, 21).abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log abs vwap × close
def f036vds_f036_vwap_distance_slope_logvwap_63d_base_v083_signal(closeadj, volume):
    result = np.log(_f036_vwap(closeadj, volume, 63).abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log abs vwap × close
def f036vds_f036_vwap_distance_slope_logvwap_252d_base_v084_signal(closeadj, volume):
    result = np.log(_f036_vwap(closeadj, volume, 252).abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap ratio (close/vwap)
def f036vds_f036_vwap_distance_slope_vwapratio_21d_base_v085_signal(closeadj, volume):
    result = _safe_div(closeadj, _f036_vwap(closeadj, volume, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap ratio
def f036vds_f036_vwap_distance_slope_vwapratio_63d_base_v086_signal(closeadj, volume):
    result = _safe_div(closeadj, _f036_vwap(closeadj, volume, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap ratio
def f036vds_f036_vwap_distance_slope_vwapratio_126d_base_v087_signal(closeadj, volume):
    result = _safe_div(closeadj, _f036_vwap(closeadj, volume, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap ratio
def f036vds_f036_vwap_distance_slope_vwapratio_252d_base_v088_signal(closeadj, volume):
    result = _safe_div(closeadj, _f036_vwap(closeadj, volume, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vwap ratio
def f036vds_f036_vwap_distance_slope_vwapratio_504d_base_v089_signal(closeadj, volume):
    result = _safe_div(closeadj, _f036_vwap(closeadj, volume, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap gap × volume z
def f036vds_f036_vwap_distance_slope_gapxvolz_21d_base_v090_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 21)
    result = base * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap gap × volume z
def f036vds_f036_vwap_distance_slope_gapxvolz_63d_base_v091_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 63)
    result = base * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vwap gap × volume z
def f036vds_f036_vwap_distance_slope_gapxvolz_126d_base_v092_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 126)
    result = base * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap gap × volume z
def f036vds_f036_vwap_distance_slope_gapxvolz_252d_base_v093_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 252)
    result = base * _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance squared × close
def f036vds_f036_vwap_distance_slope_distsq_21d_base_v094_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance squared × close
def f036vds_f036_vwap_distance_slope_distsq_63d_base_v095_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance squared × close
def f036vds_f036_vwap_distance_slope_distsq_252d_base_v096_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope squared × close
def f036vds_f036_vwap_distance_slope_slopesq_21d_base_v097_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope squared × close
def f036vds_f036_vwap_distance_slope_slopesq_63d_base_v098_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope squared × close
def f036vds_f036_vwap_distance_slope_slopesq_252d_base_v099_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vwap distance × close
def f036vds_f036_vwap_distance_slope_emadist_21d_base_v100_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vwap distance × close
def f036vds_f036_vwap_distance_slope_emadist_63d_base_v101_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of vwap distance × close
def f036vds_f036_vwap_distance_slope_emadist_126d_base_v102_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 126).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of vwap slope × close
def f036vds_f036_vwap_distance_slope_emaslope_21d_base_v103_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of vwap slope × close
def f036vds_f036_vwap_distance_slope_emaslope_63d_base_v104_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of vwap slope × close
def f036vds_f036_vwap_distance_slope_emaslope_126d_base_v105_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 126).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × log volume
def f036vds_f036_vwap_distance_slope_distxlogv_21d_base_v106_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × log volume
def f036vds_f036_vwap_distance_slope_distxlogv_63d_base_v107_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × log volume
def f036vds_f036_vwap_distance_slope_distxlogv_252d_base_v108_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × log volume
def f036vds_f036_vwap_distance_slope_slopexlogv_21d_base_v109_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × log volume
def f036vds_f036_vwap_distance_slope_slopexlogv_63d_base_v110_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d short-vwap minus long-vwap (21 vs 252)
def f036vds_f036_vwap_distance_slope_vwapminus_21_252_base_v111_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 21) - _f036_vwap(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 504d vwap minus
def f036vds_f036_vwap_distance_slope_vwapminus_21_504_base_v112_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 21) - _f036_vwap(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 252d vwap minus
def f036vds_f036_vwap_distance_slope_vwapminus_63_252_base_v113_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 63) - _f036_vwap(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 504d vwap minus
def f036vds_f036_vwap_distance_slope_vwapminus_63_504_base_v114_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 63) - _f036_vwap(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 504d vwap minus
def f036vds_f036_vwap_distance_slope_vwapminus_126_504_base_v115_signal(closeadj, volume):
    result = _f036_vwap(closeadj, volume, 126) - _f036_vwap(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × close roll-mean
def f036vds_f036_vwap_distance_slope_distxclmean_21d_base_v116_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × close roll-mean
def f036vds_f036_vwap_distance_slope_distxclmean_63d_base_v117_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × close roll-mean
def f036vds_f036_vwap_distance_slope_distxclmean_252d_base_v118_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × close roll-mean
def f036vds_f036_vwap_distance_slope_slopexclmean_21d_base_v119_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × close roll-mean
def f036vds_f036_vwap_distance_slope_slopexclmean_63d_base_v120_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × close roll-mean
def f036vds_f036_vwap_distance_slope_slopexclmean_252d_base_v121_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × volume mean (21d)
def f036vds_f036_vwap_distance_slope_distxvmean_21d_base_v122_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × volume mean (63d)
def f036vds_f036_vwap_distance_slope_distxvmean_63d_base_v123_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * _mean(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × volume mean (126d)
def f036vds_f036_vwap_distance_slope_distxvmean_252d_base_v124_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * _mean(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × volume mean (21d)
def f036vds_f036_vwap_distance_slope_slopexvmean_21d_base_v125_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × volume mean (63d)
def f036vds_f036_vwap_distance_slope_slopexvmean_63d_base_v126_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * _mean(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × volume mean (126d)
def f036vds_f036_vwap_distance_slope_slopexvmean_252d_base_v127_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * _mean(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × close std
def f036vds_f036_vwap_distance_slope_distxclstd_21d_base_v128_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × close std
def f036vds_f036_vwap_distance_slope_distxclstd_63d_base_v129_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × close std
def f036vds_f036_vwap_distance_slope_distxclstd_252d_base_v130_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope × close std
def f036vds_f036_vwap_distance_slope_slopexclstd_21d_base_v131_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × close std
def f036vds_f036_vwap_distance_slope_slopexclstd_63d_base_v132_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope × close std
def f036vds_f036_vwap_distance_slope_slopexclstd_252d_base_v133_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × z-close
def f036vds_f036_vwap_distance_slope_distxzcl_21d_base_v134_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance × z-close
def f036vds_f036_vwap_distance_slope_distxzcl_63d_base_v135_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * _z(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance × z-close
def f036vds_f036_vwap_distance_slope_distxzcl_252d_base_v136_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252) * _z(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite: distance × volume × close
def f036vds_f036_vwap_distance_slope_distxvolxcl_21d_base_v137_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: distance × volume × close
def f036vds_f036_vwap_distance_slope_distxvolxcl_63d_base_v138_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite: slope × volume × close
def f036vds_f036_vwap_distance_slope_slopexvolxcl_21d_base_v139_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: slope × volume × close
def f036vds_f036_vwap_distance_slope_slopexvolxcl_63d_base_v140_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63) * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance abs × close (depth)
def f036vds_f036_vwap_distance_slope_absdist_21d_base_v141_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap distance abs × close
def f036vds_f036_vwap_distance_slope_absdist_63d_base_v142_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap distance abs × close
def f036vds_f036_vwap_distance_slope_absdist_252d_base_v143_signal(closeadj, volume):
    result = _f036_vwap_distance(closeadj, volume, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap slope abs × close
def f036vds_f036_vwap_distance_slope_absslope_21d_base_v144_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope abs × close
def f036vds_f036_vwap_distance_slope_absslope_63d_base_v145_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vwap slope abs × close
def f036vds_f036_vwap_distance_slope_absslope_252d_base_v146_signal(closeadj, volume):
    result = _f036_vwap_slope(closeadj, volume, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d short vwap gap vs long vwap gap
def f036vds_f036_vwap_distance_slope_gapratio_21_252_base_v147_signal(closeadj, volume):
    short_gap = closeadj - _f036_vwap(closeadj, volume, 21)
    long_gap = closeadj - _f036_vwap(closeadj, volume, 252)
    result = short_gap - long_gap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite vwap reset signal × volume
def f036vds_f036_vwap_distance_slope_compreset_63d_base_v148_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) - _f036_vwap_distance(closeadj, volume, 252)
    result = base * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vwap distance × close cumsum proxy (running close × dist)
def f036vds_f036_vwap_distance_slope_distxcumcl_21d_base_v149_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21)
    result = base * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vwap slope × close cumsum proxy (mean dollar volume)
def f036vds_f036_vwap_distance_slope_slopexcumcl_63d_base_v150_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63)
    result = base * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f036vds_f036_vwap_distance_slope_signdist_21d_base_v076_signal,
    f036vds_f036_vwap_distance_slope_signdist_63d_base_v077_signal,
    f036vds_f036_vwap_distance_slope_signdist_252d_base_v078_signal,
    f036vds_f036_vwap_distance_slope_signslope_21d_base_v079_signal,
    f036vds_f036_vwap_distance_slope_signslope_63d_base_v080_signal,
    f036vds_f036_vwap_distance_slope_signslope_252d_base_v081_signal,
    f036vds_f036_vwap_distance_slope_logvwap_21d_base_v082_signal,
    f036vds_f036_vwap_distance_slope_logvwap_63d_base_v083_signal,
    f036vds_f036_vwap_distance_slope_logvwap_252d_base_v084_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_21d_base_v085_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_63d_base_v086_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_126d_base_v087_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_252d_base_v088_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_504d_base_v089_signal,
    f036vds_f036_vwap_distance_slope_gapxvolz_21d_base_v090_signal,
    f036vds_f036_vwap_distance_slope_gapxvolz_63d_base_v091_signal,
    f036vds_f036_vwap_distance_slope_gapxvolz_126d_base_v092_signal,
    f036vds_f036_vwap_distance_slope_gapxvolz_252d_base_v093_signal,
    f036vds_f036_vwap_distance_slope_distsq_21d_base_v094_signal,
    f036vds_f036_vwap_distance_slope_distsq_63d_base_v095_signal,
    f036vds_f036_vwap_distance_slope_distsq_252d_base_v096_signal,
    f036vds_f036_vwap_distance_slope_slopesq_21d_base_v097_signal,
    f036vds_f036_vwap_distance_slope_slopesq_63d_base_v098_signal,
    f036vds_f036_vwap_distance_slope_slopesq_252d_base_v099_signal,
    f036vds_f036_vwap_distance_slope_emadist_21d_base_v100_signal,
    f036vds_f036_vwap_distance_slope_emadist_63d_base_v101_signal,
    f036vds_f036_vwap_distance_slope_emadist_126d_base_v102_signal,
    f036vds_f036_vwap_distance_slope_emaslope_21d_base_v103_signal,
    f036vds_f036_vwap_distance_slope_emaslope_63d_base_v104_signal,
    f036vds_f036_vwap_distance_slope_emaslope_126d_base_v105_signal,
    f036vds_f036_vwap_distance_slope_distxlogv_21d_base_v106_signal,
    f036vds_f036_vwap_distance_slope_distxlogv_63d_base_v107_signal,
    f036vds_f036_vwap_distance_slope_distxlogv_252d_base_v108_signal,
    f036vds_f036_vwap_distance_slope_slopexlogv_21d_base_v109_signal,
    f036vds_f036_vwap_distance_slope_slopexlogv_63d_base_v110_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_21_252_base_v111_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_21_504_base_v112_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_63_252_base_v113_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_63_504_base_v114_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_126_504_base_v115_signal,
    f036vds_f036_vwap_distance_slope_distxclmean_21d_base_v116_signal,
    f036vds_f036_vwap_distance_slope_distxclmean_63d_base_v117_signal,
    f036vds_f036_vwap_distance_slope_distxclmean_252d_base_v118_signal,
    f036vds_f036_vwap_distance_slope_slopexclmean_21d_base_v119_signal,
    f036vds_f036_vwap_distance_slope_slopexclmean_63d_base_v120_signal,
    f036vds_f036_vwap_distance_slope_slopexclmean_252d_base_v121_signal,
    f036vds_f036_vwap_distance_slope_distxvmean_21d_base_v122_signal,
    f036vds_f036_vwap_distance_slope_distxvmean_63d_base_v123_signal,
    f036vds_f036_vwap_distance_slope_distxvmean_252d_base_v124_signal,
    f036vds_f036_vwap_distance_slope_slopexvmean_21d_base_v125_signal,
    f036vds_f036_vwap_distance_slope_slopexvmean_63d_base_v126_signal,
    f036vds_f036_vwap_distance_slope_slopexvmean_252d_base_v127_signal,
    f036vds_f036_vwap_distance_slope_distxclstd_21d_base_v128_signal,
    f036vds_f036_vwap_distance_slope_distxclstd_63d_base_v129_signal,
    f036vds_f036_vwap_distance_slope_distxclstd_252d_base_v130_signal,
    f036vds_f036_vwap_distance_slope_slopexclstd_21d_base_v131_signal,
    f036vds_f036_vwap_distance_slope_slopexclstd_63d_base_v132_signal,
    f036vds_f036_vwap_distance_slope_slopexclstd_252d_base_v133_signal,
    f036vds_f036_vwap_distance_slope_distxzcl_21d_base_v134_signal,
    f036vds_f036_vwap_distance_slope_distxzcl_63d_base_v135_signal,
    f036vds_f036_vwap_distance_slope_distxzcl_252d_base_v136_signal,
    f036vds_f036_vwap_distance_slope_distxvolxcl_21d_base_v137_signal,
    f036vds_f036_vwap_distance_slope_distxvolxcl_63d_base_v138_signal,
    f036vds_f036_vwap_distance_slope_slopexvolxcl_21d_base_v139_signal,
    f036vds_f036_vwap_distance_slope_slopexvolxcl_63d_base_v140_signal,
    f036vds_f036_vwap_distance_slope_absdist_21d_base_v141_signal,
    f036vds_f036_vwap_distance_slope_absdist_63d_base_v142_signal,
    f036vds_f036_vwap_distance_slope_absdist_252d_base_v143_signal,
    f036vds_f036_vwap_distance_slope_absslope_21d_base_v144_signal,
    f036vds_f036_vwap_distance_slope_absslope_63d_base_v145_signal,
    f036vds_f036_vwap_distance_slope_absslope_252d_base_v146_signal,
    f036vds_f036_vwap_distance_slope_gapratio_21_252_base_v147_signal,
    f036vds_f036_vwap_distance_slope_compreset_63d_base_v148_signal,
    f036vds_f036_vwap_distance_slope_distxcumcl_21d_base_v149_signal,
    f036vds_f036_vwap_distance_slope_slopexcumcl_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F036_VWAP_DISTANCE_SLOPE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f036_vwap", "_f036_vwap_distance", "_f036_vwap_slope")
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
    print(f"OK f036_vwap_distance_slope_base_076_150_claude: {n_features} features pass")
