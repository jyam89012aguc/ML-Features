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


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _f030_low_vol_indicator(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    deficit = (long_vol - vol) / long_vol.replace(0, np.nan)
    return deficit * closeadj


def _f030_compression_duration(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    low = (vol < long_vol * 0.7).astype(float)
    grp = (low.diff().fillna(0).abs().cumsum())
    dur = low.groupby(grp).cumsum() * closeadj
    return dur + (long_vol - vol).abs() * closeadj * 0.01


def _f030_coil_length(closeadj, w):
    ret = closeadj.pct_change()
    vol = ret.rolling(w, min_periods=max(1, w // 2)).std()
    long_vol = ret.rolling(max(w * 4, 63), min_periods=max(1, w // 2)).std()
    ratio = vol / long_vol.replace(0, np.nan)
    coiled = (ratio < 1.0).astype(float)
    return coiled.rolling(max(w * 2, 21), min_periods=max(1, w // 2)).sum() * closeadj + ratio * closeadj * 0.01

def f030cmd_f030_compression_duration_lowvol_tanh_5d_base_v076_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_5d_base_v077_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_5d_base_v078_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_10d_base_v079_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_10d_base_v080_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_10d_base_v081_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_21d_base_v082_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_21d_base_v083_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_21d_base_v084_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_42d_base_v085_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_42d_base_v086_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_42d_base_v087_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_63d_base_v088_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_63d_base_v089_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_63d_base_v090_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_126d_base_v091_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_126d_base_v092_signal(closeadj):
    base = _f030_compression_duration(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_126d_base_v093_signal(closeadj):
    base = _f030_coil_length(closeadj, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_189d_base_v094_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_189d_base_v095_signal(closeadj):
    base = _f030_compression_duration(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_189d_base_v096_signal(closeadj):
    base = _f030_coil_length(closeadj, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_252d_base_v097_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_252d_base_v098_signal(closeadj):
    base = _f030_compression_duration(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_252d_base_v099_signal(closeadj):
    base = _f030_coil_length(closeadj, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_378d_base_v100_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_378d_base_v101_signal(closeadj):
    base = _f030_compression_duration(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_378d_base_v102_signal(closeadj):
    base = _f030_coil_length(closeadj, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_tanh_504d_base_v103_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_tanh_504d_base_v104_signal(closeadj):
    base = _f030_compression_duration(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_tanh_504d_base_v105_signal(closeadj):
    base = _f030_coil_length(closeadj, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_5d_base_v106_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_5d_base_v107_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_5d_base_v108_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_10d_base_v109_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_10d_base_v110_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_10d_base_v111_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_21d_base_v112_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_21d_base_v113_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_21d_base_v114_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_42d_base_v115_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_42d_base_v116_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_42d_base_v117_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_63d_base_v118_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_63d_base_v119_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_63d_base_v120_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_126d_base_v121_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_126d_base_v122_signal(closeadj):
    base = _f030_compression_duration(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_126d_base_v123_signal(closeadj):
    base = _f030_coil_length(closeadj, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_189d_base_v124_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_189d_base_v125_signal(closeadj):
    base = _f030_compression_duration(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_189d_base_v126_signal(closeadj):
    base = _f030_coil_length(closeadj, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_252d_base_v127_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_252d_base_v128_signal(closeadj):
    base = _f030_compression_duration(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_252d_base_v129_signal(closeadj):
    base = _f030_coil_length(closeadj, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_378d_base_v130_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_378d_base_v131_signal(closeadj):
    base = _f030_compression_duration(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_378d_base_v132_signal(closeadj):
    base = _f030_coil_length(closeadj, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_zclip_504d_base_v133_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_zclip_504d_base_v134_signal(closeadj):
    base = _f030_compression_duration(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_zclip_504d_base_v135_signal(closeadj):
    base = _f030_coil_length(closeadj, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_var63_5d_base_v136_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_var63_5d_base_v137_signal(closeadj):
    base = _f030_compression_duration(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_var63_5d_base_v138_signal(closeadj):
    base = _f030_coil_length(closeadj, 5)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_var63_10d_base_v139_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_var63_10d_base_v140_signal(closeadj):
    base = _f030_compression_duration(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_var63_10d_base_v141_signal(closeadj):
    base = _f030_coil_length(closeadj, 10)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_var63_21d_base_v142_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_var63_21d_base_v143_signal(closeadj):
    base = _f030_compression_duration(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_var63_21d_base_v144_signal(closeadj):
    base = _f030_coil_length(closeadj, 21)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_var63_42d_base_v145_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_var63_42d_base_v146_signal(closeadj):
    base = _f030_compression_duration(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_var63_42d_base_v147_signal(closeadj):
    base = _f030_coil_length(closeadj, 42)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_lowvol_var63_63d_base_v148_signal(closeadj):
    base = _f030_low_vol_indicator(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_compdur_var63_63d_base_v149_signal(closeadj):
    base = _f030_compression_duration(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f030cmd_f030_compression_duration_coil_var63_63d_base_v150_signal(closeadj):
    base = _f030_coil_length(closeadj, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f030cmd_f030_compression_duration_lowvol_tanh_5d_base_v076_signal,
    f030cmd_f030_compression_duration_compdur_tanh_5d_base_v077_signal,
    f030cmd_f030_compression_duration_coil_tanh_5d_base_v078_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_10d_base_v079_signal,
    f030cmd_f030_compression_duration_compdur_tanh_10d_base_v080_signal,
    f030cmd_f030_compression_duration_coil_tanh_10d_base_v081_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_21d_base_v082_signal,
    f030cmd_f030_compression_duration_compdur_tanh_21d_base_v083_signal,
    f030cmd_f030_compression_duration_coil_tanh_21d_base_v084_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_42d_base_v085_signal,
    f030cmd_f030_compression_duration_compdur_tanh_42d_base_v086_signal,
    f030cmd_f030_compression_duration_coil_tanh_42d_base_v087_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_63d_base_v088_signal,
    f030cmd_f030_compression_duration_compdur_tanh_63d_base_v089_signal,
    f030cmd_f030_compression_duration_coil_tanh_63d_base_v090_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_126d_base_v091_signal,
    f030cmd_f030_compression_duration_compdur_tanh_126d_base_v092_signal,
    f030cmd_f030_compression_duration_coil_tanh_126d_base_v093_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_189d_base_v094_signal,
    f030cmd_f030_compression_duration_compdur_tanh_189d_base_v095_signal,
    f030cmd_f030_compression_duration_coil_tanh_189d_base_v096_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_252d_base_v097_signal,
    f030cmd_f030_compression_duration_compdur_tanh_252d_base_v098_signal,
    f030cmd_f030_compression_duration_coil_tanh_252d_base_v099_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_378d_base_v100_signal,
    f030cmd_f030_compression_duration_compdur_tanh_378d_base_v101_signal,
    f030cmd_f030_compression_duration_coil_tanh_378d_base_v102_signal,
    f030cmd_f030_compression_duration_lowvol_tanh_504d_base_v103_signal,
    f030cmd_f030_compression_duration_compdur_tanh_504d_base_v104_signal,
    f030cmd_f030_compression_duration_coil_tanh_504d_base_v105_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_5d_base_v106_signal,
    f030cmd_f030_compression_duration_compdur_zclip_5d_base_v107_signal,
    f030cmd_f030_compression_duration_coil_zclip_5d_base_v108_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_10d_base_v109_signal,
    f030cmd_f030_compression_duration_compdur_zclip_10d_base_v110_signal,
    f030cmd_f030_compression_duration_coil_zclip_10d_base_v111_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_21d_base_v112_signal,
    f030cmd_f030_compression_duration_compdur_zclip_21d_base_v113_signal,
    f030cmd_f030_compression_duration_coil_zclip_21d_base_v114_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_42d_base_v115_signal,
    f030cmd_f030_compression_duration_compdur_zclip_42d_base_v116_signal,
    f030cmd_f030_compression_duration_coil_zclip_42d_base_v117_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_63d_base_v118_signal,
    f030cmd_f030_compression_duration_compdur_zclip_63d_base_v119_signal,
    f030cmd_f030_compression_duration_coil_zclip_63d_base_v120_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_126d_base_v121_signal,
    f030cmd_f030_compression_duration_compdur_zclip_126d_base_v122_signal,
    f030cmd_f030_compression_duration_coil_zclip_126d_base_v123_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_189d_base_v124_signal,
    f030cmd_f030_compression_duration_compdur_zclip_189d_base_v125_signal,
    f030cmd_f030_compression_duration_coil_zclip_189d_base_v126_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_252d_base_v127_signal,
    f030cmd_f030_compression_duration_compdur_zclip_252d_base_v128_signal,
    f030cmd_f030_compression_duration_coil_zclip_252d_base_v129_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_378d_base_v130_signal,
    f030cmd_f030_compression_duration_compdur_zclip_378d_base_v131_signal,
    f030cmd_f030_compression_duration_coil_zclip_378d_base_v132_signal,
    f030cmd_f030_compression_duration_lowvol_zclip_504d_base_v133_signal,
    f030cmd_f030_compression_duration_compdur_zclip_504d_base_v134_signal,
    f030cmd_f030_compression_duration_coil_zclip_504d_base_v135_signal,
    f030cmd_f030_compression_duration_lowvol_var63_5d_base_v136_signal,
    f030cmd_f030_compression_duration_compdur_var63_5d_base_v137_signal,
    f030cmd_f030_compression_duration_coil_var63_5d_base_v138_signal,
    f030cmd_f030_compression_duration_lowvol_var63_10d_base_v139_signal,
    f030cmd_f030_compression_duration_compdur_var63_10d_base_v140_signal,
    f030cmd_f030_compression_duration_coil_var63_10d_base_v141_signal,
    f030cmd_f030_compression_duration_lowvol_var63_21d_base_v142_signal,
    f030cmd_f030_compression_duration_compdur_var63_21d_base_v143_signal,
    f030cmd_f030_compression_duration_coil_var63_21d_base_v144_signal,
    f030cmd_f030_compression_duration_lowvol_var63_42d_base_v145_signal,
    f030cmd_f030_compression_duration_compdur_var63_42d_base_v146_signal,
    f030cmd_f030_compression_duration_coil_var63_42d_base_v147_signal,
    f030cmd_f030_compression_duration_lowvol_var63_63d_base_v148_signal,
    f030cmd_f030_compression_duration_compdur_var63_63d_base_v149_signal,
    f030cmd_f030_compression_duration_coil_var63_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F030_COMPRESSION_DURATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f030_low_vol_indicator', '_f030_compression_duration', '_f030_coil_length')
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
    print(f"OK f030_compression_duration_base_076_150_claude: {n_features} features pass")
