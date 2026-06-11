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


def _f040_vol_extreme(volume, w):
    m = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    return (volume - m) / sd.replace(0, np.nan)


def _f040_climax_volume(volume, w):
    z = _f040_vol_extreme(volume, w)
    return z.rolling(w, min_periods=max(1, w // 2)).max()


def _f040_climax_intensity(close, volume, w):
    z = _f040_vol_extreme(volume, w)
    range_close = close.rolling(w, min_periods=max(1, w // 2)).max() - close.rolling(w, min_periods=max(1, w // 2)).min()
    return z.abs() * range_close / close.replace(0, np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_5d_base_v076_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 5) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_5d_base_v077_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 5) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_5d_base_v078_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 5) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_10d_base_v079_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 10) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_10d_base_v080_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 10) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_10d_base_v081_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 10) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_21d_base_v082_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_21d_base_v083_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_21d_base_v084_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 21) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_42d_base_v085_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 42) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_42d_base_v086_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 42) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_42d_base_v087_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 42) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_63d_base_v088_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_63d_base_v089_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_63d_base_v090_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 63) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_126d_base_v091_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 126) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_126d_base_v092_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 126) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_126d_base_v093_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 126) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_189d_base_v094_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 189) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_189d_base_v095_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 189) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_189d_base_v096_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 189) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_252d_base_v097_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxlogv_252d_base_v098_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxsqrt_252d_base_v099_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 252) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_vexxvm_378d_base_v100_signal(closeadj, volume):
    result = _f040_vol_extreme(volume, 378) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_5d_base_v101_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 5) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_5d_base_v102_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 5) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_5d_base_v103_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 5) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_10d_base_v104_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 10) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_10d_base_v105_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 10) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_10d_base_v106_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 10) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_21d_base_v107_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_21d_base_v108_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_21d_base_v109_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 21) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_42d_base_v110_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 42) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_42d_base_v111_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 42) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_42d_base_v112_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 42) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_63d_base_v113_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 63) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_63d_base_v114_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 63) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_63d_base_v115_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 63) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_126d_base_v116_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 126) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_126d_base_v117_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 126) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_126d_base_v118_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 126) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_189d_base_v119_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 189) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_189d_base_v120_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 189) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_189d_base_v121_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 189) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_252d_base_v122_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 252) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxstdv_252d_base_v123_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 252) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxsqrt_252d_base_v124_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 252) * np.sqrt(volume.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_climxvm_378d_base_v125_signal(closeadj, volume):
    result = _f040_climax_volume(volume, 378) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_5d_base_v126_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 5) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_5d_base_v127_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 5) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_5d_base_v128_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 5) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_10d_base_v129_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 10) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_10d_base_v130_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 10) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_10d_base_v131_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 10) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_21d_base_v132_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 21) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_21d_base_v133_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 21) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_21d_base_v134_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_42d_base_v135_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 42) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_42d_base_v136_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 42) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_42d_base_v137_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 42) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_63d_base_v138_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 63) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_63d_base_v139_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 63) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_63d_base_v140_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_126d_base_v141_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 126) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_126d_base_v142_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 126) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_126d_base_v143_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 126) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_189d_base_v144_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 189) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_189d_base_v145_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 189) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_189d_base_v146_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 189) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_252d_base_v147_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 252) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxstdv_252d_base_v148_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 252) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxlogv_252d_base_v149_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 252) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f040cvf_f040_climactic_volume_flag_intxvm_378d_base_v150_signal(closeadj, volume):
    result = _f040_climax_intensity(closeadj, volume, 378) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f040cvf_f040_climactic_volume_flag_vexxvm_5d_base_v076_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_5d_base_v077_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_5d_base_v078_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_10d_base_v079_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_10d_base_v080_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_10d_base_v081_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_21d_base_v082_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_21d_base_v083_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_21d_base_v084_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_42d_base_v085_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_42d_base_v086_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_42d_base_v087_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_63d_base_v088_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_63d_base_v089_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_63d_base_v090_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_126d_base_v091_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_126d_base_v092_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_126d_base_v093_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_189d_base_v094_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_189d_base_v095_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_189d_base_v096_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_252d_base_v097_signal,
    f040cvf_f040_climactic_volume_flag_vexxlogv_252d_base_v098_signal,
    f040cvf_f040_climactic_volume_flag_vexxsqrt_252d_base_v099_signal,
    f040cvf_f040_climactic_volume_flag_vexxvm_378d_base_v100_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_5d_base_v101_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_5d_base_v102_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_5d_base_v103_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_10d_base_v104_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_10d_base_v105_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_10d_base_v106_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_21d_base_v107_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_21d_base_v108_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_21d_base_v109_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_42d_base_v110_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_42d_base_v111_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_42d_base_v112_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_63d_base_v113_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_63d_base_v114_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_63d_base_v115_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_126d_base_v116_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_126d_base_v117_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_126d_base_v118_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_189d_base_v119_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_189d_base_v120_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_189d_base_v121_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_252d_base_v122_signal,
    f040cvf_f040_climactic_volume_flag_climxstdv_252d_base_v123_signal,
    f040cvf_f040_climactic_volume_flag_climxsqrt_252d_base_v124_signal,
    f040cvf_f040_climactic_volume_flag_climxvm_378d_base_v125_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_5d_base_v126_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_5d_base_v127_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_5d_base_v128_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_10d_base_v129_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_10d_base_v130_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_10d_base_v131_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_21d_base_v132_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_21d_base_v133_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_21d_base_v134_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_42d_base_v135_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_42d_base_v136_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_42d_base_v137_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_63d_base_v138_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_63d_base_v139_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_63d_base_v140_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_126d_base_v141_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_126d_base_v142_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_126d_base_v143_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_189d_base_v144_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_189d_base_v145_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_189d_base_v146_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_252d_base_v147_signal,
    f040cvf_f040_climactic_volume_flag_intxstdv_252d_base_v148_signal,
    f040cvf_f040_climactic_volume_flag_intxlogv_252d_base_v149_signal,
    f040cvf_f040_climactic_volume_flag_intxvm_378d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F040_CLIMACTIC_VOLUME_FLAG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f040_vol_extreme", "_f040_climax_volume", "_f040_climax_intensity")
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
    print(f"OK f040_climactic_volume_flag_base_076_150_claude: {n_features} features pass")
